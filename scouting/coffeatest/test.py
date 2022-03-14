import uproot
import awkward as ak
from coffea.nanoevents.methods import vector
import coffea.hist as hist
import matplotlib.pyplot as plt
ak.behavior.update(vector.behavior)

fin = uproot.open("HZZ.root")
tree = fin["events"]
print(fin)
print(tree)

# let's build the lepton arrays back into objects
# in the future, some of this verbosity can be reduced
arrays = {k.replace('Electron_', ''): v for k, v in tree.arrays(filter_name="Electron_*", how=dict).items()}
electrons = ak.zip({'x': arrays.pop('Px'), 
                    'y': arrays.pop('Py'), 
                    'z': arrays.pop("Pz"),
                    't': arrays.pop("E"),
                    },
                    with_name="LorentzVector"
)


arrays = {k.replace('Muon_', ''): v for k,v in tree.arrays(filter_name="Muon_*", how=dict).items()}
muons = ak.zip({'x': arrays.pop('Px'), 
                'y': arrays.pop('Py'), 
                'z': arrays.pop("Pz"),
                't': arrays.pop("E"),
                },
                with_name="LorentzVector"
)

print("Avg. electrons/event:", ak.sum(ak.num(electrons))/tree.num_entries)
print("Avg. muons/event:", ak.sum(ak.num(muons))/tree.num_entries)


lepton_kinematics = hist.Hist(
    "Events",
    hist.Cat("flavor", "Lepton flavor"),
    hist.Bin("pt", "$p_{T}$", 19, 10, 100),
    hist.Bin("eta", "$\eta$", [-2.5, -1.4, 0, 1.4, 2.5]),
)

# Pass keyword arguments to fill, all arrays must be flat numpy arrays
# User is responsible for ensuring all arrays have same jagged structure!
lepton_kinematics.fill(
    flavor="electron",
    pt=ak.flatten(electrons.pt),
    eta=ak.flatten(electrons.eta)
)
lepton_kinematics.fill(
    flavor="muon",
    pt=ak.flatten(muons.pt),
    eta=ak.flatten(muons.eta)
)

# Now we can start to manipulate this single histogram to plot different views of the data
# here we look at lepton pt for all eta
lepton_pt = lepton_kinematics.integrate("eta")

fig, ax = plt.subplots()

ax = hist.plot1d(
    lepton_pt,
    overlay="flavor",
    stack=True,
    fill_opts={'alpha': .5, 'edgecolor': (0,0,0,0.3)}
)
# all plot calls return the matplotlib axes object, from which
# you can edit features afterwards using matplotlib object-oriented syntax
# e.g. maybe you really miss '90s graphics...
ax.get_legend().shadow = True
#Path("Plots/var").mkdir(parents=True,exist_ok=True)
fig.savefig("../Plots/test")
plt.close()
fig1, ax1 = plt.subplots()
lepton_pt.label = "Density"
ax1 = hist.plot1d(lepton_pt,overlay="flavor", density=True)
fig1.savefig("../Plots/test2")
plt.close()
