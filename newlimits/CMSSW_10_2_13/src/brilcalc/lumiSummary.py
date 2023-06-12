import os
import subprocess
from FWCore.PythonUtilities.LumiList import LumiList
from itertools import izip
import array
from multiprocessing import Pool
from optparse import OptionParser
from XRootD import client
import imp
from ROOT import TFile

# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------

class sampleInfo : 

    '''
    Example Use:
    from lumiSummary import sampleInfo
    si = sampleInfo("data2016Lumi/","/store/user/lpcsusyhad/SusyRA2Analysis2015/Run2ProductionV15/",["Run2016B-17Jul2018_ver1-v1.HTMHT_*"])
    '''

    def __init__( self , outName, baseDir, fileNames ) :
        self.fileNames = fileNames
        self.outName = outName
        self.fileList = []
        if baseDir[-1]!="/": baseDir = baseDir+"/"
        for f in fileNames:
            self.addToList(baseDir,f)

    def addToList( self, baseDir, fileName ):
        redirector = "root://cmseos.fnal.gov/"
        xrdfs = client.FileSystem(redirector)
        dirToList = baseDir
        patternToMatch = fileName
        # detect folderized mode
        if "/" in fileName:
            dirToList = baseDir+os.path.dirname(fileName)
            patternToMatch = os.path.basename(fileName)
        if dirToList[-1]!="/": dirToList = dirToList+"/"
        patternToMatch = patternToMatch.strip('*')
        status, listing = xrdfs.dirlist(dirToList)
        if status.status != 0:
            raise Exception("XRootD failed to stat %s%s" % (str(xrdfs.url),baseDir))
        files = [redirector+dirToList+entry.name for entry in listing if patternToMatch in entry.name]
        self.fileList.extend(files)

    def __repr__(self):
        return "%s(%r, %r)" % (self.__class__.__name__, self.outName,self.fileNames)

    def __str__(self):
        dict_of_members = self.__dict__
        list_of_keys = dict_of_members.keys()
        list_of_values = dict_of_members.values()
        max_len_keys = max(len(str(x)) for x in list_of_keys)
        min_len_values = min(len(str(x)) for x in list_of_values)
        key_format="{:<"+str(max_len_keys)+"}"
        value_format="{:<"+str(min_len_values)+"}"
        rep_format = "sampleInfo("
        for ikey, key in enumerate(list_of_keys):
            if ikey != len(list_of_keys)-1:
                rep_format += (key_format+": "+value_format)
                rep_format += ("\n{:<11}")
            else:
                rep_format += (key_format+": {:<"+str(len(str(self.fileNames)))+"}")
                rep_format += ")"
        return rep_format.format('outName',self.outName,' ','fileNames',self.fileNames,' ','fileList',self.fileList)

# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------

#stolen unashamedly from:
#https://github.com/dmwm/CRABClient/blob/master/src/python/CRABClient/Commands/report.py
#https://github.com/dmwm/CRABClient/blob/master/src/python/CRABClient/JobType/BasicJobType.py

def makeJSON(outdir,basedir,verbose,name,files):
#def makeJSON(optlist):
#    outdir = optlist[0]
#    basedir = optlist[1]
#    verbose = optlist[2]
#    name = optlist[3]
#    files = optlist[4:]
    s = sampleInfo(name,basedir,files)
    
    #lumi set for this sample
    mergedLumis = set()

    for f in s.fileList:
        # skip empty paths
        if f == '': continue

        # open the file or skip the file if it can't be opened
        if verbose: print "Trying to open file \"" + f +"\""
        file = TFile.Open(f)
        if file == None: 
            if verbose: print "\tWARNING: Can't open file \"" + f +"\"" 
            continue

        # only keep necessary branches
        t = file.Get("mmtree/tree")
        #t = file.Get("TreeMaker2/PreSelection")
        if t == None: continue
        t.SetBranchStatus("*",0)
        #t.SetBranchStatus("RunNum",1)
        #t.SetBranchStatus("LumiBlockNum",1)
        t.SetBranchStatus("run",1)
        t.SetBranchStatus("lumSec",1)

        #get tree entries
        nentries = t.GetEntries()
        if nentries==0: continue
        t.SetEstimate(nentries)
        t.Draw("run:lumSec","","goff")
        #t.Draw("RunNum:LumiBlockNum","","goff")
        v1 = t.GetV1(); v1.SetSize(t.GetSelectedRows()); a1 = array.array('d',v1); v1 = None;
        v2 = t.GetV2(); v2.SetSize(t.GetSelectedRows()); a2 = array.array('d',v2); v2 = None;
        
        #loop over tree entries
        for run,ls in izip(a1,a2):
            irun = int(run)
            ils = int(ls)
            if not (irun,ils) in mergedLumis:
                mergedLumis.add((irun,ils))

        file.Close()

    ### end loop over files in sample

    #convert the runlumis from list of pairs to dict: [(123,3), (123,4), (123,5), (123,7), (234,6)] => {123 : [3,4,5,7], 234 : [6]}
    mLumisDict = {}
    for k, v in mergedLumis:
        mLumisDict.setdefault(k, []).append(int(v))

    #make lumi list from dict
    mergedLumiList = LumiList(runsAndLumis=mLumisDict)
    if mergedLumiList:
        outfile = outdir+'/lumiSummary_'+s.outName+'.json'
        mergedLumiList.writeJSON(outfile)
        print "wrote "+outfile

# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-o", "--outdir", dest="outdir", default="json", help="output directory for JSON files (default = %default)")
    parser.add_option("-b", "--basedir", dest="basedir", default="/store/group/lpcsuep/Scouting/Datav6/2018/ScoutingPFHT+Run2018A-v1+RAW", help="location of data ntuples (default = %default)")
    parser.add_option("-d", "--dict", dest="dictfile", default="dataSamples.py", help="file containing a list of data sample names and files (default = %default)")
    parser.add_option("-n", "--npool", dest="npool", default=4, help="number of processes to run (0: don't use multiprocessing, for debugging) (default = %default)")
    parser.add_option("-v", "--verbose", dest="verbose", default=False, action="store_true", help="print extra error messages (default = %default)")
    (options, args) = parser.parse_args()

    from ROOT import *
    
    #check for output directory
    if not os.path.isdir(options.outdir):
        os.mkdir(options.outdir)

    module_name = os.path.basename(options.dictfile).replace(".py","")
    print(module_name)
    dict = imp.load_source(module_name,options.dictfile)

    #common list of options
    optlist = [options.outdir, options.basedir, options.verbose]
    
    #prepend common list to dict
    for i,d in enumerate(dict.dataSamples):
        dict.dataSamples[i] = optlist + dict.dataSamples[i]

    if options.npool==0:
        for d in dict.dataSamples:
            makeJSON(d)
    else:
        p = Pool(int(options.npool))
        p.map(makeJSON,dict.dataSamples)
