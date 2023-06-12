from lumiSummary import *
from multiprocessing import Pool
#from lumiSummary import sampleInfo
#si = sampleInfo("output/","/store/group/lpcsuep/Scouting/Datav6/2018/ScoutingPFHT+Run2018A-v1+RAW",["FC9BE713-F64F-E811-A2A3-FA163EE49B7B.root"])
#outdir = optlist[0]
#    basedir = optlist[1]
#    verbose = optlist[2]
#    name = optlist[3]
#    files = optlist[4:]

run="F"
data = [line.strip() for line in open("/uscms/home/mreid/nobackup/sueps/analysis/SUEPs/scouting/rootfiles/2017/new_trigger/Trigger_%s.txt"%(run), 'r')]  
#data = [line.strip() for line in open("/uscms/home/mreid/nobackup/sueps/analysis/SUEPs/scouting/rootfiles/2018/new_data/Data_Run%s_v6.txt"%(run), 'r')]  
print(data)
p = Pool(12)
p.map(makeJSON("output_trig%s_17/"%run,"/store/group/lpcsuep/Scouting/Trigger/2017/ScoutingPFCommissioning+Run2017%s-v1+RAW"%run,True,"test",data))
