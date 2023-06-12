src_CombineHarvester_CombineTools_scripts_files := $(filter-out \#% %\#,$(notdir $(wildcard $(foreach dir,$(LOCALTOP)/src/CombineHarvester/CombineTools/scripts,$(dir)/*))))
$(eval $(call Src2StoreCopy,src_CombineHarvester_CombineTools_scripts,src/CombineHarvester/CombineTools/scripts,$(SCRAMSTORENAME_BIN),*))
