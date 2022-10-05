import matplotlib.pyplot as plt
import mplhep as hep
import numpy as np
import awkward as ak
from math import pi

def jetAngularities(jet, candidates,R0=1.5):
        dR = candidates.deltaR(jet)
        inv = 1/jet.pt
        girth = ak.sum(inv*candidates.pt*dR/(R0),axis=1)
        pt_dispersion = ak.sum(inv*inv*candidates.pt*candidates.pt,axis=1)
        lesHouches = ak.sum(inv*candidates.pt*np.sqrt(dR/R0),axis=1)
        thrust = ak.sum(inv*candidates.pt*(dR/R0)*(dR/R0),axis=1)
        return [girth,pt_dispersion,lesHouches,thrust]
def nSubjettiness( n, jet, candidates, R0=1.5):########DOESN'T Work
        print("Test 1")
        definition = fastjet.JetDefinition(fastjet.antikt_algorithm, R0/np.sqrt(n))
        print("Test 2")
        cluster = fastjet.ClusterSequence(candidates, definition)
        print("Test 3")
        subjets = ak.with_name(cluster.exclusive_jets(n_jets=n),"Momentum4D")
        print("Test 4")
        d0 = ak.sum(subjets.pt*R0,axis=1)
        dR = ak.min(candidates.deltaR(subjets),axis=1)
        numerator = ak.sum(candidates.pt*dR,axis=1)
        print("Test 5")
        return numerator/d0

def get_dr_ring(dr, phi_c=0, eta_c=0, n_points=600):
    deta = np.linspace(-dr, +dr, n_points)
    dphi = np.sqrt(dr**2 - np.square(deta))
    deta = eta_c+np.concatenate((deta, deta[::-1]))
    dphi = phi_c+np.concatenate((dphi, -dphi[::-1]))
    return dphi, deta
def plot_display(fin,ievt,ht,particles,bparticles,suepjet,isrjet,bisrjet,sphericity,nbtracks,isrtracks):
    fig = plt.figure(figsize=(8,8))
    ax = plt.gca()

    ax.set_xlim(-pi,pi)
    ax.set_ylim(-2.5,2.5)
    ax.set_xlabel(r'$\phi$', fontsize=18)
    ax.set_ylabel(r'$\eta$', fontsize=18)
    ax.tick_params(axis='both', which='major', labelsize=12)

    ax.scatter(particles.phi, particles.eta, s=2*particles.pt, c='xkcd:blue', marker='o',label="ID tracks: %d"%len(particles))

    phi_s, eta_s = get_dr_ring(1.5,suepjet.phi, suepjet.eta)
    phi_s = phi_s[1:]
    eta_s = eta_s[1:]
    ax.plot(phi_s[phi_s> pi] - 2*pi, eta_s[phi_s>pi], color='xkcd:green',linestyle='--')
    ax.plot(phi_s[phi_s< -pi] + 2*pi, eta_s[phi_s<-pi], color='xkcd:green',linestyle='--')
    ax.plot(phi_s[phi_s< pi], eta_s[phi_s<pi], color='xkcd:green',linestyle='--',label="SUEP Jet: %d [GeV]; %s tracks"%(suepjet.pt,len(nbtracks)))
    phi_i, eta_i = get_dr_ring(1.5,isrjet.phi, isrjet.eta)
    phi_i = phi_i[1:]
    eta_i = eta_i[1:]
    ax.plot(phi_i[phi_i> pi] - 2*pi, eta_i[phi_i>pi], color='xkcd:red',linestyle='--')
    ax.plot(phi_i[phi_i< -pi] + 2*pi, eta_i[phi_i<-pi], color='xkcd:red',linestyle='--')
    ax.plot(phi_i[phi_i< pi], eta_i[phi_i<pi], color='xkcd:red',linestyle='--',label="ISR Jet: %d [GeV]; %s tracks"%(isrjet.pt,len(isrtracks)))

    plt.legend(title='Event (after selection): %d\n Ht: %d'%(ievt,ht))
    hep.cms.label('',data=False,lumi=59.69,year=2018,loc=2)

    fig.savefig("Displays/nonboosted_%s%s.pdf"%(fin,ievt))
    plt.close()


    fig = plt.figure(figsize=(8,8))
    ax = plt.gca()

    ax.set_xlim(-pi,pi)
    ax.set_ylim(-2.5,2.5)
    ax.set_xlabel(r'$\phi$', fontsize=18)
    ax.set_ylabel(r'$\eta$', fontsize=18)
    ax.tick_params(axis='both', which='major', labelsize=12)
    ax.scatter(bparticles.phi, bparticles.eta, s=2*bparticles.pt, c='xkcd:magenta', marker='o',label="Boosted ISR tracks:%s"%(len(isrtracks)))
    ax.scatter(nbtracks.phi, nbtracks.eta, s=2*nbtracks.pt, c='xkcd:blue', marker='o',label="Boosted SUEP tracks:%s"%len(nbtracks))
    phi_ib, eta_ib = get_dr_ring(1.5,bisrjet.phi, bisrjet.eta)
    phi_ib = phi_ib[1:]
    eta_ib = eta_ib[1:]
    ax.plot(phi_ib[phi_ib> pi] - 2*pi, eta_ib[phi_ib>pi], color='xkcd:orange',linestyle='--')
    ax.plot(phi_ib[phi_ib< -pi] + 2*pi, eta_ib[phi_ib<-pi], color='xkcd:orange',linestyle='--')
    ax.plot(phi_ib[phi_ib< pi], eta_ib[phi_ib<pi], color='xkcd:orange',linestyle='--',label="Boosted ISR Jet: %d [GeV]"%isrjet.pt)
    plt.legend(title='Event: %d\n Ht: %d SUEP Jet pt: %d\n Boosted Sphericity: %.2f'%(ievt,ht,suepjet.pt,sphericity))
    hep.cms.label('',data=False,lumi=59.69,year=2018,loc=2)

    fig.savefig("Displays/boosted_%s%s.pdf"%(fin,ievt))
    plt.close()
def sphericity(self, particles, r):
    norm = ak.sum(particles.p ** r, axis=1, keepdims=True)
    s = np.array([[
                   ak.sum(particles.px * particles.px * particles.p ** (r-2.0), axis=1 ,keepdims=True)/norm,
                   ak.sum(particles.px * particles.py * particles.p ** (r-2.0), axis=1 ,keepdims=True)/norm,
                   ak.sum(particles.px * particles.pz * particles.p ** (r-2.0), axis=1 ,keepdims=True)/norm
                  ],
                  [
                   ak.sum(particles.py * particles.px * particles.p ** (r-2.0), axis=1 ,keepdims=True)/norm,
                   ak.sum(particles.py * particles.py * particles.p ** (r-2.0), axis=1 ,keepdims=True)/norm,
                   ak.sum(particles.py * particles.pz * particles.p ** (r-2.0), axis=1 ,keepdims=True)/norm
                  ],
                  [
                   ak.sum(particles.pz * particles.px * particles.p ** (r-2.0), axis=1 ,keepdims=True)/norm,
                   ak.sum(particles.pz * particles.py * particles.p ** (r-2.0), axis=1 ,keepdims=True)/norm,
                   ak.sum(particles.pz * particles.pz * particles.p ** (r-2.0), axis=1 ,keepdims=True)/norm
                  ]])
    s = np.squeeze(np.moveaxis(s, 2, 0),axis=3)
    evals = np.sort(np.linalg.eigvalsh(s))
    return evals

