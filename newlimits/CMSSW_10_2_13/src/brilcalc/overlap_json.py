import json

#with open('/uscms/home/mreid/nobackup/sueps/analysis/SUEPs/scouting/systematics/GoldenJSON/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt') as json_file:
with open('/uscms/home/mreid/nobackup/sueps/analysis/SUEPs/scouting/systematics/GoldenJSON/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt') as json_file:
#with open('/uscms/home/mreid/nobackup/sueps/analysis/SUEPs/scouting/systematics/GoldenJSON/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt') as json_file:
    golden = json.load(json_file)
year=17


#runs = ["A","B","C","D"]
#runs = ["B","C","D","E","F","G","H"]
runs = ["C","D","E","F"]
for run in runs:

  with open('output_trig%s_%s/lumiSummary_test.json'%(run,year)) as json_file:
  #with open('output_run%s_%s_v2/lumiSummary_test.json'%(run,year)) as json_file:
      data = json.load(json_file)
  
  #print(data)
  #print(golden)
  
  new_lums = {}
  for key in data.keys():
    if key in golden:
      new_lums[key] = data[key]
    else:
      print(key)
  with open("newoutput/lumiSummaryGolden_trig%s_%s.json"%(run,year), "w") as outfile:
      json.dump(new_lums, outfile,indent=2)
      #outfile.write("\n")
