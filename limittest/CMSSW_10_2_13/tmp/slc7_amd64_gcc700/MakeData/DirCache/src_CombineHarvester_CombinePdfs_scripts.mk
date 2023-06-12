src_CombineHarvester_CombinePdfs_scripts_files := $(filter-out \#% %\#,$(notdir $(wildcard $(foreach dir,$(LOCALTOP)/src/CombineHarvester/CombinePdfs/scripts,$(dir)/*))))
$(eval $(call Src2StoreCopy,src_CombineHarvester_CombinePdfs_scripts,src/CombineHarvester/CombinePdfs/scripts,$(SCRAMSTORENAME_BIN),*))
