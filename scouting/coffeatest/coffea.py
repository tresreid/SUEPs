import uproot
import awkward as ak
from coffea.nanoevents.methods import vector
import coffea.hist as hist
import matplotlib.pyplot as plt
ak.behavior.update(vector.behavior)

fin = uproot.open("newData_ntrack/%s_ntrack.root"%("sig400_darkPho"))
tree = fin["mmtree/tree"]
print(fin)
print(tree)

# let's build the lepton arrays back into objects
# in the future, some of this verbosity can be reduced
arrays = tree.arrays(how=dict).items()
print(arrays)
