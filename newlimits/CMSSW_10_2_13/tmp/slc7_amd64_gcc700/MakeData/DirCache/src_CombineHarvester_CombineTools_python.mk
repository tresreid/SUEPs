ifeq ($(strip $(PyCombineHarvesterCombineTools)),)
PyCombineHarvesterCombineTools := self/src/CombineHarvester/CombineTools/python
src_CombineHarvester_CombineTools_python_parent := 
ALL_PYTHON_DIRS += $(patsubst src/%,%,src/CombineHarvester/CombineTools/python)
PyCombineHarvesterCombineTools_files := $(patsubst src/CombineHarvester/CombineTools/python/%,%,$(wildcard $(foreach dir,src/CombineHarvester/CombineTools/python ,$(foreach ext,$(SRC_FILES_SUFFIXES),$(dir)/*.$(ext)))))
PyCombineHarvesterCombineTools_LOC_USE := self  
PyCombineHarvesterCombineTools_PACKAGE := self/src/CombineHarvester/CombineTools/python
ALL_PRODS += PyCombineHarvesterCombineTools
PyCombineHarvesterCombineTools_INIT_FUNC        += $$(eval $$(call PythonProduct,PyCombineHarvesterCombineTools,src/CombineHarvester/CombineTools/python,src_CombineHarvester_CombineTools_python,1,1,$(SCRAMSTORENAME_PYTHON),$(SCRAMSTORENAME_LIB),,))
else
$(eval $(call MultipleWarningMsg,PyCombineHarvesterCombineTools,src/CombineHarvester/CombineTools/python))
endif
ALL_COMMONRULES += src_CombineHarvester_CombineTools_python
src_CombineHarvester_CombineTools_python_INIT_FUNC += $$(eval $$(call CommonProductRules,src_CombineHarvester_CombineTools_python,src/CombineHarvester/CombineTools/python,PYTHON))
