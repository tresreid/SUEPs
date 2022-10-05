import awkward as ak
from coffea import hist, processor
import uproot
from coffea.nanoevents import NanoEventsFactory, BaseSchema
import matplotlib.pyplot as plt
import mplhep as hep
import numpy as np
import uproot
import pickle

lumi = 1#59.74*1000
scaled = {}
scaled_1 = {}
with open("outhists/myhistos_RunA_0.p", "rb") as pkl_file:
    out = pickle.load(pkl_file)
    for name, h in out.items():
      if "PFcand_dR" in name or "res" in name or "gen" in name or "alldR" in name or "scalar" in name:
        continue
      if isinstance(h, hist.Hist):
        #print(name)
        scaled[name] = h.copy()
        scaled_1[name] = h.copy()
outhists1 = ["RunA_%s"%x for x in range(1,12)]
outhists1 = outhists1 + ["RunA_%s"%x for x in range(13, 23)]
outhists = ["RunA_%s"%x for x in range(1,12)]
outhists = outhists + ["RunA_%s"%x for x in range(13, 41)]
outhists = outhists + ["RunA_%s"%x for x in range(42, 94)]
outhists = outhists + ["RunA_%s"%x for x in range(95, 108)]
outhists = outhists + ["RunA_%s"%x for x in range(109, 117)] 
outhists = outhists + ["RunA_%s"%x for x in range(118, 181)]
outhists = outhists + ["RunA_%s"%x for x in range(182, 198)]
outhists = outhists + ["RunA_%s"%x for x in range(201, 269)]
outhists = outhists + ["RunA_%s"%x for x in range(270, 280)]
outhists = outhists + ["RunA_%s"%x for x in range(281, 285)]
outhists = outhists + ["RunA_%s"%x for x in range(286, 307)]
outhists = outhists + ["RunA_%s"%x for x in range(309, 320)]
outhists = outhists + ["RunA_%s"%x for x in range(321, 325)]
outhists = outhists + ["RunA_%s"%x for x in range(326, 333)]
outhists = outhists + ["RunA_%s"%x for x in range(334, 337)]
outhists = outhists + ["RunA_%s"%x for x in range(338, 348)]
outhists = outhists + ["RunA_%s"%x for x in range(349, 401)]
outhists = outhists + ["RunA_%s"%x for x in range(403, 406)]
outhists = outhists + ["RunA_%s"%x for x in range(408, 418)]
outhists = outhists + ["RunA_%s"%x for x in range(419, 439)]
outhists = outhists + ["RunA_%s"%x for x in range(440, 459)]
outhists = outhists + ["RunA_%s"%x for x in range(460, 461)]
outhists = outhists + ["RunA_%s"%x for x in range(463, 491)]
outhists = outhists + ["RunA_%s"%x for x in range(492, 493)]
outhists = outhists + ["RunA_%s"%x for x in range(494, 503)]
outhists = outhists + ["RunA_%s"%x for x in range(504, 510)]
outhists = outhists + ["RunA_%s"%x for x in range(511, 531)]
outhists = outhists + ["RunA_%s"%x for x in range(532, 534)]
outhists = outhists + ["RunA_%s"%x for x in range(535, 538)]
outhists = outhists + ["RunB_%s"%x for x in range(0,2)]
outhists = outhists + ["RunB_%s"%x for x in range(3 , 35)] 
outhists = outhists + ["RunB_%s"%x for x in range(36 , 38)]
outhists = outhists + ["RunB_%s"%x for x in range(39 , 40)]
outhists = outhists + ["RunB_%s"%x for x in range(41 , 57)]
outhists = outhists + ["RunB_%s"%x for x in range(58 , 70)]
outhists = outhists + ["RunB_%s"%x for x in range(71 , 79)]
outhists = outhists + ["RunB_%s"%x for x in range(80 , 86)]
outhists = outhists + ["RunB_%s"%x for x in range(87 , 96)]
outhists = outhists + ["RunB_%s"%x for x in range(97 , 106)] 
outhists = outhists + ["RunB_%s"%x for x in range(107 , 117)]
outhists = outhists + ["RunB_%s"%x for x in range(118 , 134)]
outhists = outhists + ["RunB_%s"%x for x in range(135 , 138)]
outhists = outhists + ["RunB_%s"%x for x in range(139 , 160)]
outhists = outhists + ["RunB_%s"%x for x in range(161 , 164)]
outhists = outhists + ["RunB_%s"%x for x in range(165 , 166)]
outhists = outhists + ["RunB_%s"%x for x in range(167 , 168)]
outhists = outhists + ["RunB_%s"%x for x in range(169 , 181)]
outhists = outhists + ["RunB_%s"%x for x in range(182 , 197)]
outhists = outhists + ["RunB_%s"%x for x in range(198 , 206)]
outhists = outhists + ["RunB_%s"%x for x in range(207 , 214)]
outhists = outhists + ["RunB_%s"%x for x in range(215 , 217)]
outhists = outhists + ["RunB_%s"%x for x in range(218 , 219)]
outhists = outhists + ["RunB_%s"%x for x in range(220 , 232)]
outhists = outhists + ["RunB_%s"%x for x in range(233 , 234)]
outhists = outhists + ["RunB_%s"%x for x in range(235 , 236)]
outhists = outhists + ["RunB_%s"%x for x in range(237 , 284)]
outhists = outhists + ["RunB_%s"%x for x in range(285 , 288)]
outhists = outhists + ["RunB_%s"%x for x in range(289 , 297)]
outhists = outhists + ["RunB_%s"%x for x in range(298 , 307)]
outhists = outhists + ["RunC_%s"%x for x in range(0 , 7)]
outhists = outhists + ["RunC_%s"%x for x in range(8 , 14)]
outhists = outhists + ["RunC_%s"%x for x in range(15 , 35)]
outhists = outhists + ["RunC_%s"%x for x in range(36 , 78)]
outhists = outhists + ["RunC_%s"%x for x in range(79 , 87)]
outhists = outhists + ["RunC_%s"%x for x in range(88 , 94)]
outhists = outhists + ["RunC_%s"%x for x in range(95 , 106)]
outhists = outhists + ["RunC_%s"%x for x in range(107 , 145)]
outhists = outhists + ["RunC_%s"%x for x in range(146 , 157)]
outhists = outhists + ["RunC_%s"%x for x in range(158 , 213)]
outhists = outhists + ["RunC_%s"%x for x in range(214 , 231)]
outhists = outhists + ["RunC_%s"%x for x in range(232 , 233)]
outhists = outhists + ["RunC_%s"%x for x in range(234 , 239)]
outhists = outhists + ["RunC_%s"%x for x in range(240 , 252)]
outhists = outhists + ["RunC_%s"%x for x in range(253 , 255)]
outhists = outhists + ["RunC_%s"%x for x in range(256 , 264)]
outhists = outhists + ["RunC_%s"%x for x in range(267 , 268)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(0, 4)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(6 ,20)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(21 ,27)] 
outhists = outhists + ["RunD_%sm2t2"%x for x in range(28 ,40)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(41 ,42)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(43 ,59)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(60 ,66)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(67 ,77)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(78 ,84)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(85 ,87)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(88 ,108)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(109 ,119)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(121 ,159)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(160 ,172)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(173 ,205)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(206 ,213)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(214 ,215)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(216 ,224)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(225 ,236)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(237 ,266)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(267 ,278)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(279 ,285)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(286 ,292)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(293 ,298)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(299 ,317)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(318 ,329)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(330 ,352)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(353 ,368)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(370 ,380)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(381 ,384)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(385 ,405)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(406 ,409)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(410 ,504)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(505 ,511)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(512 ,514)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(515 ,558)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(559 ,574)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(577 ,581)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(582 ,623)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(624 ,626)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(627 ,633)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(634 ,664)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(665 ,678)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(679 ,682)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(683 ,694)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(695 ,720)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(721 ,747)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(748 ,754)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(756 ,759)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(760 ,783)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(784 ,799)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(800 ,811)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(812 ,822)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(823 ,841)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(842 ,870)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(871 ,874)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(875 ,892)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(893 ,905)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(906 ,909)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(910 ,918)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(919 ,929)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(930 ,933)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(934 ,940)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(941 ,955)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(956 ,990)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(991 ,993)] 
outhists = outhists + ["RunD_%sm2t2"%x for x in range(994 ,1008)] 
outhists = outhists + ["RunD_%sm2t2"%x for x in range(1010 ,1025)] 
outhists = outhists + ["RunD_%sm2t2"%x for x in range(1026 ,1027)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(1028 ,1029)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(1030 ,1041)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(1042 ,1046)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(1047 ,1048)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(1049 ,1062)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(1063 ,1074)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(1075 ,1077)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(1078 ,1094)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(1095 ,1120)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(1121 ,1128)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(1129 ,1130)]
outhists = outhists + ["RunD_%sm2t2"%x for x in range(1131 ,1132)]

for ohist in outhists:
  with open("outhists/myhistos_%s.p"%(ohist), "rb") as pkl_file:
      print(ohist)
      out = pickle.load(pkl_file)
      for name, h in out.items():
        if "PFcand_dR" in name or "res" in name or "gen" in name or "alldR" in name or "scalar" in name:
          continue
        if isinstance(h, hist.Hist):
          temphist = h.copy()
          scaled[name] = scaled[name]+temphist
with open("outhists/myhistos_Data.p", "wb") as pkl_file:
        pickle.dump(scaled, pkl_file)
for ohist in outhists1:
  with open("outhists/myhistos_%s.p"%(ohist), "rb") as pkl_file:
      print(ohist)
      out = pickle.load(pkl_file)
      for name, h in out.items():
        if "PFcand_dR" in name or "res" in name or "gen" in name or "alldR" in name or "scalar" in name:
          continue
        if isinstance(h, hist.Hist):
          temphist = h.copy()
          scaled_1[name] = scaled_1[name]+temphist
with open("outhists/myhistos_RunA.p", "wb") as pkl_file:
        pickle.dump(scaled_1, pkl_file)
