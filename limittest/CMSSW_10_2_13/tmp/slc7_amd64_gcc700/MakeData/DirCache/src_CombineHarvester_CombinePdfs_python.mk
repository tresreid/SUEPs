ifeq ($(strip $(PyCombineHarvesterCombinePdfs)),)
PyCombineHarvesterCombinePdfs := self/src/CombineHarvester/CombinePdfs/python
src_CombineHarvester_CombinePdfs_python_parent := 
ALL_PYTHON_DIRS += $(patsubst src/%,%,src/CombineHarvester/CombinePdfs/python)
PyCombineHarvesterCombinePdfs_files := $(patsubst src/CombineHarvester/CombinePdfs/python/%,%,$(wildcard $(foreach dir,src/CombineHarvester/CombinePdfs/python ,$(foreach ext,$(SRC_FILES_SUFFIXES),$(dir)/*.$(ext)))))
PyCombineHarvesterCombinePdfs_LOC_USE := self  
PyCombineHarvesterCombinePdfs_PACKAGE := self/src/CombineHarvester/CombinePdfs/python
ALL_PRODS += PyCombineHarvesterCombinePdfs
PyCombineHarvesterCombinePdfs_INIT_FUNC        += $$(eval $$(call PythonProduct,PyCombineHarvesterCombinePdfs,src/CombineHarvester/CombinePdfs/python,src_CombineHarvester_CombinePdfs_python,1,1,$(SCRAMSTORENAME_PYTHON),$(SCRAMSTORENAME_LIB),,))
else
$(eval $(call MultipleWarningMsg,PyCombineHarvesterCombinePdfs,src/CombineHarvester/CombinePdfs/python))
endif
ALL_COMMONRULES += src_CombineHarvester_CombinePdfs_python
src_CombineHarvester_CombinePdfs_python_INIT_FUNC += $$(eval $$(call CommonProductRules,src_CombineHarvester_CombinePdfs_python,src/CombineHarvester/CombinePdfs/python,PYTHON))
