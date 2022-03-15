import awkward as ak
from coffea import hist, processor
import uproot
from coffea.nanoevents import NanoEventsFactory, BaseSchema
import matplotlib.pyplot as plt
import mplhep as hep
import numpy as np

# register our candidate behaviors
from coffea.nanoevents.methods import candidate
ak.behavior.update(candidate.behavior)

class MyProcessor(processor.ProcessorABC):
    def __init__(self):
        self._accumulator = processor.dict_accumulator({
            "sumw": processor.defaultdict_accumulator(float),
            "htdist": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","ht",100,0,1500)
            ),
        })

    @property
    def accumulator(self):
        return self._accumulator

    def process(self, arrays):
        output = self.accumulator.identity()
        #print(events)
        #dataset = events.metadata['dataset']
        #arrays = {k: v for k,v in events.arrays(how=dict).items()}
        tright = [item[7] for item in arrays["hltResult"]]
        vals = ak.zip({
               'ht': arrays["ht"],
#               'n_pfcand': arrays.pop("n_pfcand"),
#               'event_sphericity': arrays.pop("event_sphericity"),
#               'eventBoosted_sphericity': arrays.pop("eventBoosted_sphericity"),
#               'n_fatjet': arrays.pop("n_fatjet"),
#               'n_jet': arrays.pop("n_jet"),
#               'n_pfMu': arrays.pop("n_pfMu"),
#               'n_pfEl': arrays.pop("n_pfEl"),
#               'triggerHt': tright,
        })

        #cut = (ak.num(muons) == 2) & (ak.sum(muons.charge) == 0)
        # add first and second muon in every event together
        #dimuon = muons[cut][:, 0] + muons[cut][:, 1]

        #output["sumw"][dataset] += len(events)
        output["htdist"].fill(
            cut="cut 0",
            v1=vals["ht"],
        )

        return output

    def postprocess(self, accumulator):
        return accumulator


# https://github.com/scikit-hep/uproot4/issues/122
uproot.open.defaults["xrootd_handler"] = uproot.source.xrootd.MultithreadedXRootDSource

fileset = {
           'HT700' : [
            "root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/QCD/HT700/F980E45B-3E04-C64B-B9EB-87DD0E1E8783.root",
            "root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/QCD/HT700/F9838A6B-DA97-B24D-91FC-D8453D7618BA.root",
            "root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/QCD/HT700/F9CE0AD2-252B-CB4E-8F3A-9488DAF84A3C.root",
            "root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/QCD/HT700/F9D04630-B90B-0A41-89B6-4960B86187C6.root",
            "root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/QCD/HT700/F9D7DE16-1658-9043-9471-E1D77545A0AF.root",
            "root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/QCD/HT700/F9DD1443-8504-0A49-8CF0-AC8AE55FF6B8.root",
            ]
}

out = processor.run_uproot_job(
      fileset,
      treename="mmtree/tree",
      processor_instance=MyProcessor(),
      executor=processor.iterative_executor,
      executor_args={
          "schema": BaseSchema,
      },
      maxchunks=4,
)
print(out)
scaled = {}
for name, h in out.items():
  if isinstance(h, hist.Hist):
    scaled[name] = h.copy()

fig, ax1 = plt.subplots()

hist.plot1d(
    scaled["htdist"],
    ax=ax1,
    overlay="cut",
    stack=False,
    fill_opts={'alpha': .9, 'edgecolor': (0,0,0,0.3)}
)
#hep.cms.label(loc=2)
hep.cms.label('',data=False,lumi=59.74,year=2018,loc=2)
fig.savefig("Plots/proccess_%s"%("ht"))
plt.close()
