import awkward as ak
from coffea.nanoevents import NanoEventsFactory, NanoAODSchema
from coffea.lookup_tools import extractor

fname = "https://raw.githubusercontent.com/CoffeaTeam/coffea/master/tests/samples/nano_dy.root"
events = NanoEventsFactory.from_root(
    fname,
    schemaclass=NanoAODSchema.v6,
    metadata={"dataset": "DYJets"},
).events()
ext = extractor()
# several histograms can be imported at once using wildcards (*)
ext.add_weight_sets(["testSF2d scalefactors_Tight_Electron jet_corrections/test2/testSF2d.histo.root"])
ext.finalize()

evaluator = ext.make_evaluator()

print("available evaluator keys:")
for key in evaluator.keys():
    print("\t", key)
print("testSF2d:", evaluator['testSF2d'])
print("type of testSF2d:", type(evaluator['testSF2d']))

from coffea.jetmet_tools import FactorizedJetCorrector, JetCorrectionUncertainty
from coffea.jetmet_tools import JECStack, CorrectedJetsFactory
#import awkward as ak
import numpy as np

ext = extractor()
ext.add_weight_sets([
    "* * jet_corrections/test2/Fall17_17Nov2017_V32_MC_L2Relative_AK4PFPuppi.jec.txt",
    "* * jet_corrections/test2/Fall17_17Nov2017_V32_MC_Uncertainty_AK4PFPuppi.junc.txt",
])
ext.finalize()

jec_stack_names = [
    "Fall17_17Nov2017_V32_MC_L2Relative_AK4PFPuppi",
    "Fall17_17Nov2017_V32_MC_Uncertainty_AK4PFPuppi"
]

evaluator = ext.make_evaluator()

jec_inputs = {name: evaluator[name] for name in jec_stack_names}
jec_stack = JECStack(jec_inputs)
### more possibilities are available if you send in more pieces of the JEC stack
# mc2016_ak8_jxform = JECStack(["more", "names", "of", "JEC parts"])

print(dir(evaluator))
name_map = jec_stack.blank_name_map
name_map['JetPt'] = 'pt'
name_map['JetMass'] = 'mass'
name_map['JetEta'] = 'eta'
name_map['JetA'] = 'area'

jets = events.Jet

jets['pt_raw'] = (1 - jets['rawFactor']) * jets['pt']
jets['mass_raw'] = (1 - jets['rawFactor']) * jets['mass']
jets['pt_gen'] = ak.values_astype(ak.fill_none(jets.matched_gen.pt, 0), np.float32)
jets['rho'] = ak.broadcast_arrays(events.fixedGridRhoFastjetAll, jets.pt)[0]
name_map['ptGenJet'] = 'pt_gen'
name_map['ptRaw'] = 'pt_raw'
name_map['massRaw'] = 'mass_raw'
name_map['Rho'] = 'rho'

events_cache = events.caches[0]
print("cache:,",events_cache)
corrector = FactorizedJetCorrector(
    Fall17_17Nov2017_V32_MC_L2Relative_AK4PFPuppi=evaluator['Fall17_17Nov2017_V32_MC_L2Relative_AK4PFPuppi'],
)
uncertainties = JetCorrectionUncertainty(
    Fall17_17Nov2017_V32_MC_Uncertainty_AK4PFPuppi=evaluator['Fall17_17Nov2017_V32_MC_Uncertainty_AK4PFPuppi']
)

jet_factory = CorrectedJetsFactory(name_map, jec_stack)
corrected_jets = jet_factory.build(jets, lazy_cache=events_cache)

print('starting columns:', set(ak.fields(jets)))
print('new columns:', set(ak.fields(corrected_jets)) - set(ak.fields(jets)))
print('untransformed pt ratios', jets.pt/jets.pt_raw)
print('untransformed mass ratios', jets.mass/jets.mass_raw)

print('transformed pt ratios', corrected_jets.pt/corrected_jets.pt_raw)
print('transformed mass ratios', corrected_jets.mass/corrected_jets.mass_raw)

print('JES UP pt ratio', corrected_jets.JES_jes.up.pt/corrected_jets.pt_raw)
print('JES DOWN pt ratio', corrected_jets.JES_jes.down.pt/corrected_jets.pt_raw)
