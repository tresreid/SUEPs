ALL_SUBSYSTEMS+=HiggsAnalysis
subdirs_src_HiggsAnalysis = src_HiggsAnalysis_CombinedLimit
ALL_PACKAGES += HiggsAnalysis/CombinedLimit
subdirs_src_HiggsAnalysis_CombinedLimit := src_HiggsAnalysis_CombinedLimit_bin src_HiggsAnalysis_CombinedLimit_data src_HiggsAnalysis_CombinedLimit_macros src_HiggsAnalysis_CombinedLimit_python src_HiggsAnalysis_CombinedLimit_scripts src_HiggsAnalysis_CombinedLimit_src src_HiggsAnalysis_CombinedLimit_test
ifeq ($(strip $(combine)),)
combine := self/src/HiggsAnalysis/CombinedLimit/bin
combine_files := $(patsubst src/HiggsAnalysis/CombinedLimit/bin/%,%,$(foreach file,combine.cpp,$(eval xfile:=$(wildcard src/HiggsAnalysis/CombinedLimit/bin/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/HiggsAnalysis/CombinedLimit/bin/$(file). Please fix src/HiggsAnalysis/CombinedLimit/bin/BuildFile.))))
combine_BuildFile    := $(WORKINGDIR)/cache/bf/src/HiggsAnalysis/CombinedLimit/bin/BuildFile
combine_LOC_USE := self  HiggsAnalysis/CombinedLimit boost_program_options
combine_PACKAGE := self/src/HiggsAnalysis/CombinedLimit/bin
ALL_PRODS += combine
combine_INIT_FUNC        += $$(eval $$(call Binary,combine,src/HiggsAnalysis/CombinedLimit/bin,src_HiggsAnalysis_CombinedLimit_bin,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_BIN),bin,$(SCRAMSTORENAME_LOGS)))
combine_CLASS := BINARY
else
$(eval $(call MultipleWarningMsg,combine,src/HiggsAnalysis/CombinedLimit/bin))
endif
ALL_COMMONRULES += src_HiggsAnalysis_CombinedLimit_bin
src_HiggsAnalysis_CombinedLimit_bin_parent := HiggsAnalysis/CombinedLimit
src_HiggsAnalysis_CombinedLimit_bin_INIT_FUNC += $$(eval $$(call CommonProductRules,src_HiggsAnalysis_CombinedLimit_bin,src/HiggsAnalysis/CombinedLimit/bin,BINARY))
ifeq ($(strip $(PyHiggsAnalysisCombinedLimit)),)
PyHiggsAnalysisCombinedLimit := self/src/HiggsAnalysis/CombinedLimit/python
src_HiggsAnalysis_CombinedLimit_python_parent := 
ALL_PYTHON_DIRS += $(patsubst src/%,%,src/HiggsAnalysis/CombinedLimit/python)
PyHiggsAnalysisCombinedLimit_files := $(patsubst src/HiggsAnalysis/CombinedLimit/python/%,%,$(wildcard $(foreach dir,src/HiggsAnalysis/CombinedLimit/python ,$(foreach ext,$(SRC_FILES_SUFFIXES),$(dir)/*.$(ext)))))
PyHiggsAnalysisCombinedLimit_LOC_USE := self  
PyHiggsAnalysisCombinedLimit_PACKAGE := self/src/HiggsAnalysis/CombinedLimit/python
ALL_PRODS += PyHiggsAnalysisCombinedLimit
PyHiggsAnalysisCombinedLimit_INIT_FUNC        += $$(eval $$(call PythonProduct,PyHiggsAnalysisCombinedLimit,src/HiggsAnalysis/CombinedLimit/python,src_HiggsAnalysis_CombinedLimit_python,1,1,$(SCRAMSTORENAME_PYTHON),$(SCRAMSTORENAME_LIB),,))
else
$(eval $(call MultipleWarningMsg,PyHiggsAnalysisCombinedLimit,src/HiggsAnalysis/CombinedLimit/python))
endif
ALL_COMMONRULES += src_HiggsAnalysis_CombinedLimit_python
src_HiggsAnalysis_CombinedLimit_python_INIT_FUNC += $$(eval $$(call CommonProductRules,src_HiggsAnalysis_CombinedLimit_python,src/HiggsAnalysis/CombinedLimit/python,PYTHON))
src_HiggsAnalysis_CombinedLimit_scripts_files := $(filter-out \#% %\#,$(notdir $(wildcard $(foreach dir,$(LOCALTOP)/src/HiggsAnalysis/CombinedLimit/scripts,$(dir)/*))))
$(eval $(call Src2StoreCopy,src_HiggsAnalysis_CombinedLimit_scripts,src/HiggsAnalysis/CombinedLimit/scripts,$(SCRAMSTORENAME_BIN),*))
ALL_COMMONRULES += src_HiggsAnalysis_CombinedLimit_test
src_HiggsAnalysis_CombinedLimit_test_parent := HiggsAnalysis/CombinedLimit
src_HiggsAnalysis_CombinedLimit_test_INIT_FUNC += $$(eval $$(call CommonProductRules,src_HiggsAnalysis_CombinedLimit_test,src/HiggsAnalysis/CombinedLimit/test,TEST))
ALL_SUBSYSTEMS+=CombineHarvester
subdirs_src_CombineHarvester = src_CombineHarvester_CombinePdfs src_CombineHarvester_CombineTools src_CombineHarvester_docs
ALL_PACKAGES += CombineHarvester/CombinePdfs
subdirs_src_CombineHarvester_CombinePdfs := src_CombineHarvester_CombinePdfs_bin src_CombineHarvester_CombinePdfs_python src_CombineHarvester_CombinePdfs_scripts src_CombineHarvester_CombinePdfs_src
ifeq ($(strip $(SMLegacyMorphing)),)
SMLegacyMorphing := self/src/CombineHarvester/CombinePdfs/bin
SMLegacyMorphing_files := $(patsubst src/CombineHarvester/CombinePdfs/bin/%,%,$(foreach file,SMLegacyMorphing.cpp,$(eval xfile:=$(wildcard src/CombineHarvester/CombinePdfs/bin/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/CombineHarvester/CombinePdfs/bin/$(file). Please fix src/CombineHarvester/CombinePdfs/bin/BuildFile.))))
SMLegacyMorphing_BuildFile    := $(WORKINGDIR)/cache/bf/src/CombineHarvester/CombinePdfs/bin/BuildFile
SMLegacyMorphing_LOC_USE := self  root rootmath roofit roostats histfactory libxml2 vdt python boost_program_options boost_filesystem boost_python boost_regex rootpy CombineHarvester/CombineTools CombineHarvester/CombinePdfs
SMLegacyMorphing_PACKAGE := self/src/CombineHarvester/CombinePdfs/bin
ALL_PRODS += SMLegacyMorphing
SMLegacyMorphing_INIT_FUNC        += $$(eval $$(call Binary,SMLegacyMorphing,src/CombineHarvester/CombinePdfs/bin,src_CombineHarvester_CombinePdfs_bin,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_BIN),bin,$(SCRAMSTORENAME_LOGS)))
SMLegacyMorphing_CLASS := BINARY
else
$(eval $(call MultipleWarningMsg,SMLegacyMorphing,src/CombineHarvester/CombinePdfs/bin))
endif
ifeq ($(strip $(ContourPlot)),)
ContourPlot := self/src/CombineHarvester/CombinePdfs/bin
ContourPlot_files := $(patsubst src/CombineHarvester/CombinePdfs/bin/%,%,$(foreach file,ContourPlot.cpp,$(eval xfile:=$(wildcard src/CombineHarvester/CombinePdfs/bin/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/CombineHarvester/CombinePdfs/bin/$(file). Please fix src/CombineHarvester/CombinePdfs/bin/BuildFile.))))
ContourPlot_BuildFile    := $(WORKINGDIR)/cache/bf/src/CombineHarvester/CombinePdfs/bin/BuildFile
ContourPlot_LOC_USE := self  root rootmath roofit roostats histfactory libxml2 vdt python boost_program_options boost_filesystem boost_python boost_regex rootpy CombineHarvester/CombineTools CombineHarvester/CombinePdfs
ContourPlot_PACKAGE := self/src/CombineHarvester/CombinePdfs/bin
ALL_PRODS += ContourPlot
ContourPlot_INIT_FUNC        += $$(eval $$(call Binary,ContourPlot,src/CombineHarvester/CombinePdfs/bin,src_CombineHarvester_CombinePdfs_bin,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_BIN),bin,$(SCRAMSTORENAME_LOGS)))
ContourPlot_CLASS := BINARY
else
$(eval $(call MultipleWarningMsg,ContourPlot,src/CombineHarvester/CombinePdfs/bin))
endif
ifeq ($(strip $(ParametricMSSM)),)
ParametricMSSM := self/src/CombineHarvester/CombinePdfs/bin
ParametricMSSM_files := $(patsubst src/CombineHarvester/CombinePdfs/bin/%,%,$(foreach file,ParametricMSSM.cpp,$(eval xfile:=$(wildcard src/CombineHarvester/CombinePdfs/bin/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/CombineHarvester/CombinePdfs/bin/$(file). Please fix src/CombineHarvester/CombinePdfs/bin/BuildFile.))))
ParametricMSSM_BuildFile    := $(WORKINGDIR)/cache/bf/src/CombineHarvester/CombinePdfs/bin/BuildFile
ParametricMSSM_LOC_USE := self  root rootmath roofit roostats histfactory libxml2 vdt python boost_program_options boost_filesystem boost_python boost_regex rootpy CombineHarvester/CombineTools CombineHarvester/CombinePdfs
ParametricMSSM_PACKAGE := self/src/CombineHarvester/CombinePdfs/bin
ALL_PRODS += ParametricMSSM
ParametricMSSM_INIT_FUNC        += $$(eval $$(call Binary,ParametricMSSM,src/CombineHarvester/CombinePdfs/bin,src_CombineHarvester_CombinePdfs_bin,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_BIN),bin,$(SCRAMSTORENAME_LOGS)))
ParametricMSSM_CLASS := BINARY
else
$(eval $(call MultipleWarningMsg,ParametricMSSM,src/CombineHarvester/CombinePdfs/bin))
endif
ifeq ($(strip $(PlotParametric)),)
PlotParametric := self/src/CombineHarvester/CombinePdfs/bin
PlotParametric_files := $(patsubst src/CombineHarvester/CombinePdfs/bin/%,%,$(foreach file,PlotParametric.cpp,$(eval xfile:=$(wildcard src/CombineHarvester/CombinePdfs/bin/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/CombineHarvester/CombinePdfs/bin/$(file). Please fix src/CombineHarvester/CombinePdfs/bin/BuildFile.))))
PlotParametric_BuildFile    := $(WORKINGDIR)/cache/bf/src/CombineHarvester/CombinePdfs/bin/BuildFile
PlotParametric_LOC_USE := self  root rootmath roofit roostats histfactory libxml2 vdt python boost_program_options boost_filesystem boost_python boost_regex rootpy CombineHarvester/CombineTools CombineHarvester/CombinePdfs
PlotParametric_PACKAGE := self/src/CombineHarvester/CombinePdfs/bin
ALL_PRODS += PlotParametric
PlotParametric_INIT_FUNC        += $$(eval $$(call Binary,PlotParametric,src/CombineHarvester/CombinePdfs/bin,src_CombineHarvester_CombinePdfs_bin,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_BIN),bin,$(SCRAMSTORENAME_LOGS)))
PlotParametric_CLASS := BINARY
else
$(eval $(call MultipleWarningMsg,PlotParametric,src/CombineHarvester/CombinePdfs/bin))
endif
ALL_COMMONRULES += src_CombineHarvester_CombinePdfs_bin
src_CombineHarvester_CombinePdfs_bin_parent := CombineHarvester/CombinePdfs
src_CombineHarvester_CombinePdfs_bin_INIT_FUNC += $$(eval $$(call CommonProductRules,src_CombineHarvester_CombinePdfs_bin,src/CombineHarvester/CombinePdfs/bin,BINARY))
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
src_CombineHarvester_CombinePdfs_scripts_files := $(filter-out \#% %\#,$(notdir $(wildcard $(foreach dir,$(LOCALTOP)/src/CombineHarvester/CombinePdfs/scripts,$(dir)/*))))
$(eval $(call Src2StoreCopy,src_CombineHarvester_CombinePdfs_scripts,src/CombineHarvester/CombinePdfs/scripts,$(SCRAMSTORENAME_BIN),*))
ALL_PACKAGES += CombineHarvester/CombineTools
subdirs_src_CombineHarvester_CombineTools := src_CombineHarvester_CombineTools_bin src_CombineHarvester_CombineTools_input src_CombineHarvester_CombineTools_macros src_CombineHarvester_CombineTools_python src_CombineHarvester_CombineTools_scripts src_CombineHarvester_CombineTools_src
ifeq ($(strip $(PostFitShapesFromWorkspace)),)
PostFitShapesFromWorkspace := self/src/CombineHarvester/CombineTools/bin
PostFitShapesFromWorkspace_files := $(patsubst src/CombineHarvester/CombineTools/bin/%,%,$(foreach file,PostFitShapesFromWorkspace.cpp,$(eval xfile:=$(wildcard src/CombineHarvester/CombineTools/bin/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/CombineHarvester/CombineTools/bin/$(file). Please fix src/CombineHarvester/CombineTools/bin/BuildFile.))))
PostFitShapesFromWorkspace_BuildFile    := $(WORKINGDIR)/cache/bf/src/CombineHarvester/CombineTools/bin/BuildFile
PostFitShapesFromWorkspace_LOC_USE := self  root rootmath roofit roostats histfactory libxml2 vdt python boost_program_options boost_filesystem boost_python boost_regex rootpy CombineHarvester/CombineTools
PostFitShapesFromWorkspace_PACKAGE := self/src/CombineHarvester/CombineTools/bin
ALL_PRODS += PostFitShapesFromWorkspace
PostFitShapesFromWorkspace_INIT_FUNC        += $$(eval $$(call Binary,PostFitShapesFromWorkspace,src/CombineHarvester/CombineTools/bin,src_CombineHarvester_CombineTools_bin,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_BIN),bin,$(SCRAMSTORENAME_LOGS)))
PostFitShapesFromWorkspace_CLASS := BINARY
else
$(eval $(call MultipleWarningMsg,PostFitShapesFromWorkspace,src/CombineHarvester/CombineTools/bin))
endif
ifeq ($(strip $(SOBPlot)),)
SOBPlot := self/src/CombineHarvester/CombineTools/bin
SOBPlot_files := $(patsubst src/CombineHarvester/CombineTools/bin/%,%,$(foreach file,SOBPlot.cpp,$(eval xfile:=$(wildcard src/CombineHarvester/CombineTools/bin/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/CombineHarvester/CombineTools/bin/$(file). Please fix src/CombineHarvester/CombineTools/bin/BuildFile.))))
SOBPlot_BuildFile    := $(WORKINGDIR)/cache/bf/src/CombineHarvester/CombineTools/bin/BuildFile
SOBPlot_LOC_USE := self  root rootmath roofit roostats histfactory libxml2 vdt python boost_program_options boost_filesystem boost_python boost_regex rootpy CombineHarvester/CombineTools
SOBPlot_PACKAGE := self/src/CombineHarvester/CombineTools/bin
ALL_PRODS += SOBPlot
SOBPlot_INIT_FUNC        += $$(eval $$(call Binary,SOBPlot,src/CombineHarvester/CombineTools/bin,src_CombineHarvester_CombineTools_bin,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_BIN),bin,$(SCRAMSTORENAME_LOGS)))
SOBPlot_CLASS := BINARY
else
$(eval $(call MultipleWarningMsg,SOBPlot,src/CombineHarvester/CombineTools/bin))
endif
ifeq ($(strip $(SMLegacyExample)),)
SMLegacyExample := self/src/CombineHarvester/CombineTools/bin
SMLegacyExample_files := $(patsubst src/CombineHarvester/CombineTools/bin/%,%,$(foreach file,SMLegacyExample.cpp,$(eval xfile:=$(wildcard src/CombineHarvester/CombineTools/bin/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/CombineHarvester/CombineTools/bin/$(file). Please fix src/CombineHarvester/CombineTools/bin/BuildFile.))))
SMLegacyExample_BuildFile    := $(WORKINGDIR)/cache/bf/src/CombineHarvester/CombineTools/bin/BuildFile
SMLegacyExample_LOC_USE := self  root rootmath roofit roostats histfactory libxml2 vdt python boost_program_options boost_filesystem boost_python boost_regex rootpy CombineHarvester/CombineTools
SMLegacyExample_PACKAGE := self/src/CombineHarvester/CombineTools/bin
ALL_PRODS += SMLegacyExample
SMLegacyExample_INIT_FUNC        += $$(eval $$(call Binary,SMLegacyExample,src/CombineHarvester/CombineTools/bin,src_CombineHarvester_CombineTools_bin,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_BIN),bin,$(SCRAMSTORENAME_LOGS)))
SMLegacyExample_CLASS := BINARY
else
$(eval $(call MultipleWarningMsg,SMLegacyExample,src/CombineHarvester/CombineTools/bin))
endif
ifeq ($(strip $(SBWeighted)),)
SBWeighted := self/src/CombineHarvester/CombineTools/bin
SBWeighted_files := $(patsubst src/CombineHarvester/CombineTools/bin/%,%,$(foreach file,SBWeighted.cpp,$(eval xfile:=$(wildcard src/CombineHarvester/CombineTools/bin/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/CombineHarvester/CombineTools/bin/$(file). Please fix src/CombineHarvester/CombineTools/bin/BuildFile.))))
SBWeighted_BuildFile    := $(WORKINGDIR)/cache/bf/src/CombineHarvester/CombineTools/bin/BuildFile
SBWeighted_LOC_USE := self  root rootmath roofit roostats histfactory libxml2 vdt python boost_program_options boost_filesystem boost_python boost_regex rootpy CombineHarvester/CombineTools
SBWeighted_PACKAGE := self/src/CombineHarvester/CombineTools/bin
ALL_PRODS += SBWeighted
SBWeighted_INIT_FUNC        += $$(eval $$(call Binary,SBWeighted,src/CombineHarvester/CombineTools/bin,src_CombineHarvester_CombineTools_bin,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_BIN),bin,$(SCRAMSTORENAME_LOGS)))
SBWeighted_CLASS := BINARY
else
$(eval $(call MultipleWarningMsg,SBWeighted,src/CombineHarvester/CombineTools/bin))
endif
ifeq ($(strip $(Example1)),)
Example1 := self/src/CombineHarvester/CombineTools/bin
Example1_files := $(patsubst src/CombineHarvester/CombineTools/bin/%,%,$(foreach file,Example1.cpp,$(eval xfile:=$(wildcard src/CombineHarvester/CombineTools/bin/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/CombineHarvester/CombineTools/bin/$(file). Please fix src/CombineHarvester/CombineTools/bin/BuildFile.))))
Example1_BuildFile    := $(WORKINGDIR)/cache/bf/src/CombineHarvester/CombineTools/bin/BuildFile
Example1_LOC_USE := self  root rootmath roofit roostats histfactory libxml2 vdt python boost_program_options boost_filesystem boost_python boost_regex rootpy CombineHarvester/CombineTools
Example1_PACKAGE := self/src/CombineHarvester/CombineTools/bin
ALL_PRODS += Example1
Example1_INIT_FUNC        += $$(eval $$(call Binary,Example1,src/CombineHarvester/CombineTools/bin,src_CombineHarvester_CombineTools_bin,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_BIN),bin,$(SCRAMSTORENAME_LOGS)))
Example1_CLASS := BINARY
else
$(eval $(call MultipleWarningMsg,Example1,src/CombineHarvester/CombineTools/bin))
endif
ifeq ($(strip $(Example3)),)
Example3 := self/src/CombineHarvester/CombineTools/bin
Example3_files := $(patsubst src/CombineHarvester/CombineTools/bin/%,%,$(foreach file,Example3.cpp,$(eval xfile:=$(wildcard src/CombineHarvester/CombineTools/bin/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/CombineHarvester/CombineTools/bin/$(file). Please fix src/CombineHarvester/CombineTools/bin/BuildFile.))))
Example3_BuildFile    := $(WORKINGDIR)/cache/bf/src/CombineHarvester/CombineTools/bin/BuildFile
Example3_LOC_USE := self  root rootmath roofit roostats histfactory libxml2 vdt python boost_program_options boost_filesystem boost_python boost_regex rootpy CombineHarvester/CombineTools
Example3_PACKAGE := self/src/CombineHarvester/CombineTools/bin
ALL_PRODS += Example3
Example3_INIT_FUNC        += $$(eval $$(call Binary,Example3,src/CombineHarvester/CombineTools/bin,src_CombineHarvester_CombineTools_bin,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_BIN),bin,$(SCRAMSTORENAME_LOGS)))
Example3_CLASS := BINARY
else
$(eval $(call MultipleWarningMsg,Example3,src/CombineHarvester/CombineTools/bin))
endif
ifeq ($(strip $(MSSMYieldTable)),)
MSSMYieldTable := self/src/CombineHarvester/CombineTools/bin
MSSMYieldTable_files := $(patsubst src/CombineHarvester/CombineTools/bin/%,%,$(foreach file,MSSMYieldTable.cpp,$(eval xfile:=$(wildcard src/CombineHarvester/CombineTools/bin/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/CombineHarvester/CombineTools/bin/$(file). Please fix src/CombineHarvester/CombineTools/bin/BuildFile.))))
MSSMYieldTable_BuildFile    := $(WORKINGDIR)/cache/bf/src/CombineHarvester/CombineTools/bin/BuildFile
MSSMYieldTable_LOC_USE := self  root rootmath roofit roostats histfactory libxml2 vdt python boost_program_options boost_filesystem boost_python boost_regex rootpy CombineHarvester/CombineTools
MSSMYieldTable_PACKAGE := self/src/CombineHarvester/CombineTools/bin
ALL_PRODS += MSSMYieldTable
MSSMYieldTable_INIT_FUNC        += $$(eval $$(call Binary,MSSMYieldTable,src/CombineHarvester/CombineTools/bin,src_CombineHarvester_CombineTools_bin,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_BIN),bin,$(SCRAMSTORENAME_LOGS)))
MSSMYieldTable_CLASS := BINARY
else
$(eval $(call MultipleWarningMsg,MSSMYieldTable,src/CombineHarvester/CombineTools/bin))
endif
ifeq ($(strip $(PrePost)),)
PrePost := self/src/CombineHarvester/CombineTools/bin
PrePost_files := $(patsubst src/CombineHarvester/CombineTools/bin/%,%,$(foreach file,PrePost.cpp,$(eval xfile:=$(wildcard src/CombineHarvester/CombineTools/bin/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/CombineHarvester/CombineTools/bin/$(file). Please fix src/CombineHarvester/CombineTools/bin/BuildFile.))))
PrePost_BuildFile    := $(WORKINGDIR)/cache/bf/src/CombineHarvester/CombineTools/bin/BuildFile
PrePost_LOC_USE := self  root rootmath roofit roostats histfactory libxml2 vdt python boost_program_options boost_filesystem boost_python boost_regex rootpy CombineHarvester/CombineTools
PrePost_PACKAGE := self/src/CombineHarvester/CombineTools/bin
ALL_PRODS += PrePost
PrePost_INIT_FUNC        += $$(eval $$(call Binary,PrePost,src/CombineHarvester/CombineTools/bin,src_CombineHarvester_CombineTools_bin,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_BIN),bin,$(SCRAMSTORENAME_LOGS)))
PrePost_CLASS := BINARY
else
$(eval $(call MultipleWarningMsg,PrePost,src/CombineHarvester/CombineTools/bin))
endif
ifeq ($(strip $(RoundTrip)),)
RoundTrip := self/src/CombineHarvester/CombineTools/bin
RoundTrip_files := $(patsubst src/CombineHarvester/CombineTools/bin/%,%,$(foreach file,RoundTrip.cpp,$(eval xfile:=$(wildcard src/CombineHarvester/CombineTools/bin/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/CombineHarvester/CombineTools/bin/$(file). Please fix src/CombineHarvester/CombineTools/bin/BuildFile.))))
RoundTrip_BuildFile    := $(WORKINGDIR)/cache/bf/src/CombineHarvester/CombineTools/bin/BuildFile
RoundTrip_LOC_USE := self  root rootmath roofit roostats histfactory libxml2 vdt python boost_program_options boost_filesystem boost_python boost_regex rootpy CombineHarvester/CombineTools
RoundTrip_PACKAGE := self/src/CombineHarvester/CombineTools/bin
ALL_PRODS += RoundTrip
RoundTrip_INIT_FUNC        += $$(eval $$(call Binary,RoundTrip,src/CombineHarvester/CombineTools/bin,src_CombineHarvester_CombineTools_bin,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_BIN),bin,$(SCRAMSTORENAME_LOGS)))
RoundTrip_CLASS := BINARY
else
$(eval $(call MultipleWarningMsg,RoundTrip,src/CombineHarvester/CombineTools/bin))
endif
ifeq ($(strip $(MSSMtauptYieldTable)),)
MSSMtauptYieldTable := self/src/CombineHarvester/CombineTools/bin
MSSMtauptYieldTable_files := $(patsubst src/CombineHarvester/CombineTools/bin/%,%,$(foreach file,MSSMtauptYieldTable.cpp,$(eval xfile:=$(wildcard src/CombineHarvester/CombineTools/bin/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/CombineHarvester/CombineTools/bin/$(file). Please fix src/CombineHarvester/CombineTools/bin/BuildFile.))))
MSSMtauptYieldTable_BuildFile    := $(WORKINGDIR)/cache/bf/src/CombineHarvester/CombineTools/bin/BuildFile
MSSMtauptYieldTable_LOC_USE := self  root rootmath roofit roostats histfactory libxml2 vdt python boost_program_options boost_filesystem boost_python boost_regex rootpy CombineHarvester/CombineTools
MSSMtauptYieldTable_PACKAGE := self/src/CombineHarvester/CombineTools/bin
ALL_PRODS += MSSMtauptYieldTable
MSSMtauptYieldTable_INIT_FUNC        += $$(eval $$(call Binary,MSSMtauptYieldTable,src/CombineHarvester/CombineTools/bin,src_CombineHarvester_CombineTools_bin,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_BIN),bin,$(SCRAMSTORENAME_LOGS)))
MSSMtauptYieldTable_CLASS := BINARY
else
$(eval $(call MultipleWarningMsg,MSSMtauptYieldTable,src/CombineHarvester/CombineTools/bin))
endif
ifeq ($(strip $(GamGamExample)),)
GamGamExample := self/src/CombineHarvester/CombineTools/bin
GamGamExample_files := $(patsubst src/CombineHarvester/CombineTools/bin/%,%,$(foreach file,GamGamExample.cpp,$(eval xfile:=$(wildcard src/CombineHarvester/CombineTools/bin/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/CombineHarvester/CombineTools/bin/$(file). Please fix src/CombineHarvester/CombineTools/bin/BuildFile.))))
GamGamExample_BuildFile    := $(WORKINGDIR)/cache/bf/src/CombineHarvester/CombineTools/bin/BuildFile
GamGamExample_LOC_USE := self  root rootmath roofit roostats histfactory libxml2 vdt python boost_program_options boost_filesystem boost_python boost_regex rootpy CombineHarvester/CombineTools
GamGamExample_PACKAGE := self/src/CombineHarvester/CombineTools/bin
ALL_PRODS += GamGamExample
GamGamExample_INIT_FUNC        += $$(eval $$(call Binary,GamGamExample,src/CombineHarvester/CombineTools/bin,src_CombineHarvester_CombineTools_bin,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_BIN),bin,$(SCRAMSTORENAME_LOGS)))
GamGamExample_CLASS := BINARY
else
$(eval $(call MultipleWarningMsg,GamGamExample,src/CombineHarvester/CombineTools/bin))
endif
ifeq ($(strip $(YieldTable)),)
YieldTable := self/src/CombineHarvester/CombineTools/bin
YieldTable_files := $(patsubst src/CombineHarvester/CombineTools/bin/%,%,$(foreach file,YieldTable.cpp,$(eval xfile:=$(wildcard src/CombineHarvester/CombineTools/bin/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/CombineHarvester/CombineTools/bin/$(file). Please fix src/CombineHarvester/CombineTools/bin/BuildFile.))))
YieldTable_BuildFile    := $(WORKINGDIR)/cache/bf/src/CombineHarvester/CombineTools/bin/BuildFile
YieldTable_LOC_USE := self  root rootmath roofit roostats histfactory libxml2 vdt python boost_program_options boost_filesystem boost_python boost_regex rootpy CombineHarvester/CombineTools
YieldTable_PACKAGE := self/src/CombineHarvester/CombineTools/bin
ALL_PRODS += YieldTable
YieldTable_INIT_FUNC        += $$(eval $$(call Binary,YieldTable,src/CombineHarvester/CombineTools/bin,src_CombineHarvester_CombineTools_bin,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_BIN),bin,$(SCRAMSTORENAME_LOGS)))
YieldTable_CLASS := BINARY
else
$(eval $(call MultipleWarningMsg,YieldTable,src/CombineHarvester/CombineTools/bin))
endif
ifeq ($(strip $(PlotTest)),)
PlotTest := self/src/CombineHarvester/CombineTools/bin
PlotTest_files := $(patsubst src/CombineHarvester/CombineTools/bin/%,%,$(foreach file,PlotTest.cpp,$(eval xfile:=$(wildcard src/CombineHarvester/CombineTools/bin/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/CombineHarvester/CombineTools/bin/$(file). Please fix src/CombineHarvester/CombineTools/bin/BuildFile.))))
PlotTest_BuildFile    := $(WORKINGDIR)/cache/bf/src/CombineHarvester/CombineTools/bin/BuildFile
PlotTest_LOC_USE := self  root rootmath roofit roostats histfactory libxml2 vdt python boost_program_options boost_filesystem boost_python boost_regex rootpy CombineHarvester/CombineTools
PlotTest_PACKAGE := self/src/CombineHarvester/CombineTools/bin
ALL_PRODS += PlotTest
PlotTest_INIT_FUNC        += $$(eval $$(call Binary,PlotTest,src/CombineHarvester/CombineTools/bin,src_CombineHarvester_CombineTools_bin,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_BIN),bin,$(SCRAMSTORENAME_LOGS)))
PlotTest_CLASS := BINARY
else
$(eval $(call MultipleWarningMsg,PlotTest,src/CombineHarvester/CombineTools/bin))
endif
ifeq ($(strip $(PostFitPlot2)),)
PostFitPlot2 := self/src/CombineHarvester/CombineTools/bin
PostFitPlot2_files := $(patsubst src/CombineHarvester/CombineTools/bin/%,%,$(foreach file,PostFitPlot2.cpp,$(eval xfile:=$(wildcard src/CombineHarvester/CombineTools/bin/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/CombineHarvester/CombineTools/bin/$(file). Please fix src/CombineHarvester/CombineTools/bin/BuildFile.))))
PostFitPlot2_BuildFile    := $(WORKINGDIR)/cache/bf/src/CombineHarvester/CombineTools/bin/BuildFile
PostFitPlot2_LOC_USE := self  root rootmath roofit roostats histfactory libxml2 vdt python boost_program_options boost_filesystem boost_python boost_regex rootpy CombineHarvester/CombineTools
PostFitPlot2_PACKAGE := self/src/CombineHarvester/CombineTools/bin
ALL_PRODS += PostFitPlot2
PostFitPlot2_INIT_FUNC        += $$(eval $$(call Binary,PostFitPlot2,src/CombineHarvester/CombineTools/bin,src_CombineHarvester_CombineTools_bin,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_BIN),bin,$(SCRAMSTORENAME_LOGS)))
PostFitPlot2_CLASS := BINARY
else
$(eval $(call MultipleWarningMsg,PostFitPlot2,src/CombineHarvester/CombineTools/bin))
endif
ifeq ($(strip $(hzz4l)),)
hzz4l := self/src/CombineHarvester/CombineTools/bin
hzz4l_files := $(patsubst src/CombineHarvester/CombineTools/bin/%,%,$(foreach file,hzz4l.cpp,$(eval xfile:=$(wildcard src/CombineHarvester/CombineTools/bin/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/CombineHarvester/CombineTools/bin/$(file). Please fix src/CombineHarvester/CombineTools/bin/BuildFile.))))
hzz4l_BuildFile    := $(WORKINGDIR)/cache/bf/src/CombineHarvester/CombineTools/bin/BuildFile
hzz4l_LOC_USE := self  root rootmath roofit roostats histfactory libxml2 vdt python boost_program_options boost_filesystem boost_python boost_regex rootpy CombineHarvester/CombineTools
hzz4l_PACKAGE := self/src/CombineHarvester/CombineTools/bin
ALL_PRODS += hzz4l
hzz4l_INIT_FUNC        += $$(eval $$(call Binary,hzz4l,src/CombineHarvester/CombineTools/bin,src_CombineHarvester_CombineTools_bin,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_BIN),bin,$(SCRAMSTORENAME_LOGS)))
hzz4l_CLASS := BINARY
else
$(eval $(call MultipleWarningMsg,hzz4l,src/CombineHarvester/CombineTools/bin))
endif
ifeq ($(strip $(PrintPulls)),)
PrintPulls := self/src/CombineHarvester/CombineTools/bin
PrintPulls_files := $(patsubst src/CombineHarvester/CombineTools/bin/%,%,$(foreach file,PrintPulls.cpp,$(eval xfile:=$(wildcard src/CombineHarvester/CombineTools/bin/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/CombineHarvester/CombineTools/bin/$(file). Please fix src/CombineHarvester/CombineTools/bin/BuildFile.))))
PrintPulls_BuildFile    := $(WORKINGDIR)/cache/bf/src/CombineHarvester/CombineTools/bin/BuildFile
PrintPulls_LOC_USE := self  root rootmath roofit roostats histfactory libxml2 vdt python boost_program_options boost_filesystem boost_python boost_regex rootpy CombineHarvester/CombineTools
PrintPulls_PACKAGE := self/src/CombineHarvester/CombineTools/bin
ALL_PRODS += PrintPulls
PrintPulls_INIT_FUNC        += $$(eval $$(call Binary,PrintPulls,src/CombineHarvester/CombineTools/bin,src_CombineHarvester_CombineTools_bin,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_BIN),bin,$(SCRAMSTORENAME_LOGS)))
PrintPulls_CLASS := BINARY
else
$(eval $(call MultipleWarningMsg,PrintPulls,src/CombineHarvester/CombineTools/bin))
endif
ifeq ($(strip $(NuisanceSummary)),)
NuisanceSummary := self/src/CombineHarvester/CombineTools/bin
NuisanceSummary_files := $(patsubst src/CombineHarvester/CombineTools/bin/%,%,$(foreach file,NuisanceSummary.cpp,$(eval xfile:=$(wildcard src/CombineHarvester/CombineTools/bin/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/CombineHarvester/CombineTools/bin/$(file). Please fix src/CombineHarvester/CombineTools/bin/BuildFile.))))
NuisanceSummary_BuildFile    := $(WORKINGDIR)/cache/bf/src/CombineHarvester/CombineTools/bin/BuildFile
NuisanceSummary_LOC_USE := self  root rootmath roofit roostats histfactory libxml2 vdt python boost_program_options boost_filesystem boost_python boost_regex rootpy CombineHarvester/CombineTools
NuisanceSummary_PACKAGE := self/src/CombineHarvester/CombineTools/bin
ALL_PRODS += NuisanceSummary
NuisanceSummary_INIT_FUNC        += $$(eval $$(call Binary,NuisanceSummary,src/CombineHarvester/CombineTools/bin,src_CombineHarvester_CombineTools_bin,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_BIN),bin,$(SCRAMSTORENAME_LOGS)))
NuisanceSummary_CLASS := BINARY
else
$(eval $(call MultipleWarningMsg,NuisanceSummary,src/CombineHarvester/CombineTools/bin))
endif
ifeq ($(strip $(Plot1DScan)),)
Plot1DScan := self/src/CombineHarvester/CombineTools/bin
Plot1DScan_files := $(patsubst src/CombineHarvester/CombineTools/bin/%,%,$(foreach file,Plot1DScan.cpp,$(eval xfile:=$(wildcard src/CombineHarvester/CombineTools/bin/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/CombineHarvester/CombineTools/bin/$(file). Please fix src/CombineHarvester/CombineTools/bin/BuildFile.))))
Plot1DScan_BuildFile    := $(WORKINGDIR)/cache/bf/src/CombineHarvester/CombineTools/bin/BuildFile
Plot1DScan_LOC_USE := self  root rootmath roofit roostats histfactory libxml2 vdt python boost_program_options boost_filesystem boost_python boost_regex rootpy CombineHarvester/CombineTools
Plot1DScan_PACKAGE := self/src/CombineHarvester/CombineTools/bin
ALL_PRODS += Plot1DScan
Plot1DScan_INIT_FUNC        += $$(eval $$(call Binary,Plot1DScan,src/CombineHarvester/CombineTools/bin,src_CombineHarvester_CombineTools_bin,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_BIN),bin,$(SCRAMSTORENAME_LOGS)))
Plot1DScan_CLASS := BINARY
else
$(eval $(call MultipleWarningMsg,Plot1DScan,src/CombineHarvester/CombineTools/bin))
endif
ifeq ($(strip $(LimitCompare)),)
LimitCompare := self/src/CombineHarvester/CombineTools/bin
LimitCompare_files := $(patsubst src/CombineHarvester/CombineTools/bin/%,%,$(foreach file,LimitCompare.cpp,$(eval xfile:=$(wildcard src/CombineHarvester/CombineTools/bin/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/CombineHarvester/CombineTools/bin/$(file). Please fix src/CombineHarvester/CombineTools/bin/BuildFile.))))
LimitCompare_BuildFile    := $(WORKINGDIR)/cache/bf/src/CombineHarvester/CombineTools/bin/BuildFile
LimitCompare_LOC_USE := self  root rootmath roofit roostats histfactory libxml2 vdt python boost_program_options boost_filesystem boost_python boost_regex rootpy CombineHarvester/CombineTools
LimitCompare_PACKAGE := self/src/CombineHarvester/CombineTools/bin
ALL_PRODS += LimitCompare
LimitCompare_INIT_FUNC        += $$(eval $$(call Binary,LimitCompare,src/CombineHarvester/CombineTools/bin,src_CombineHarvester_CombineTools_bin,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_BIN),bin,$(SCRAMSTORENAME_LOGS)))
LimitCompare_CLASS := BINARY
else
$(eval $(call MultipleWarningMsg,LimitCompare,src/CombineHarvester/CombineTools/bin))
endif
ifeq ($(strip $(MSSMUpdate)),)
MSSMUpdate := self/src/CombineHarvester/CombineTools/bin
MSSMUpdate_files := $(patsubst src/CombineHarvester/CombineTools/bin/%,%,$(foreach file,MSSMUpdate.cpp,$(eval xfile:=$(wildcard src/CombineHarvester/CombineTools/bin/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/CombineHarvester/CombineTools/bin/$(file). Please fix src/CombineHarvester/CombineTools/bin/BuildFile.))))
MSSMUpdate_BuildFile    := $(WORKINGDIR)/cache/bf/src/CombineHarvester/CombineTools/bin/BuildFile
MSSMUpdate_LOC_USE := self  root rootmath roofit roostats histfactory libxml2 vdt python boost_program_options boost_filesystem boost_python boost_regex rootpy CombineHarvester/CombineTools
MSSMUpdate_PACKAGE := self/src/CombineHarvester/CombineTools/bin
ALL_PRODS += MSSMUpdate
MSSMUpdate_INIT_FUNC        += $$(eval $$(call Binary,MSSMUpdate,src/CombineHarvester/CombineTools/bin,src_CombineHarvester_CombineTools_bin,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_BIN),bin,$(SCRAMSTORENAME_LOGS)))
MSSMUpdate_CLASS := BINARY
else
$(eval $(call MultipleWarningMsg,MSSMUpdate,src/CombineHarvester/CombineTools/bin))
endif
ifeq ($(strip $(PlotMassScan)),)
PlotMassScan := self/src/CombineHarvester/CombineTools/bin
PlotMassScan_files := $(patsubst src/CombineHarvester/CombineTools/bin/%,%,$(foreach file,PlotMassScan.cpp,$(eval xfile:=$(wildcard src/CombineHarvester/CombineTools/bin/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/CombineHarvester/CombineTools/bin/$(file). Please fix src/CombineHarvester/CombineTools/bin/BuildFile.))))
PlotMassScan_BuildFile    := $(WORKINGDIR)/cache/bf/src/CombineHarvester/CombineTools/bin/BuildFile
PlotMassScan_LOC_USE := self  root rootmath roofit roostats histfactory libxml2 vdt python boost_program_options boost_filesystem boost_python boost_regex rootpy CombineHarvester/CombineTools
PlotMassScan_PACKAGE := self/src/CombineHarvester/CombineTools/bin
ALL_PRODS += PlotMassScan
PlotMassScan_INIT_FUNC        += $$(eval $$(call Binary,PlotMassScan,src/CombineHarvester/CombineTools/bin,src_CombineHarvester_CombineTools_bin,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_BIN),bin,$(SCRAMSTORENAME_LOGS)))
PlotMassScan_CLASS := BINARY
else
$(eval $(call MultipleWarningMsg,PlotMassScan,src/CombineHarvester/CombineTools/bin))
endif
ifeq ($(strip $(Example2)),)
Example2 := self/src/CombineHarvester/CombineTools/bin
Example2_files := $(patsubst src/CombineHarvester/CombineTools/bin/%,%,$(foreach file,Example2.cpp,$(eval xfile:=$(wildcard src/CombineHarvester/CombineTools/bin/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/CombineHarvester/CombineTools/bin/$(file). Please fix src/CombineHarvester/CombineTools/bin/BuildFile.))))
Example2_BuildFile    := $(WORKINGDIR)/cache/bf/src/CombineHarvester/CombineTools/bin/BuildFile
Example2_LOC_USE := self  root rootmath roofit roostats histfactory libxml2 vdt python boost_program_options boost_filesystem boost_python boost_regex rootpy CombineHarvester/CombineTools
Example2_PACKAGE := self/src/CombineHarvester/CombineTools/bin
ALL_PRODS += Example2
Example2_INIT_FUNC        += $$(eval $$(call Binary,Example2,src/CombineHarvester/CombineTools/bin,src_CombineHarvester_CombineTools_bin,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_BIN),bin,$(SCRAMSTORENAME_LOGS)))
Example2_CLASS := BINARY
else
$(eval $(call MultipleWarningMsg,Example2,src/CombineHarvester/CombineTools/bin))
endif
ifeq ($(strip $(ImpactsTable)),)
ImpactsTable := self/src/CombineHarvester/CombineTools/bin
ImpactsTable_files := $(patsubst src/CombineHarvester/CombineTools/bin/%,%,$(foreach file,ImpactsTable.cpp,$(eval xfile:=$(wildcard src/CombineHarvester/CombineTools/bin/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/CombineHarvester/CombineTools/bin/$(file). Please fix src/CombineHarvester/CombineTools/bin/BuildFile.))))
ImpactsTable_BuildFile    := $(WORKINGDIR)/cache/bf/src/CombineHarvester/CombineTools/bin/BuildFile
ImpactsTable_LOC_USE := self  root rootmath roofit roostats histfactory libxml2 vdt python boost_program_options boost_filesystem boost_python boost_regex rootpy CombineHarvester/CombineTools
ImpactsTable_PACKAGE := self/src/CombineHarvester/CombineTools/bin
ALL_PRODS += ImpactsTable
ImpactsTable_INIT_FUNC        += $$(eval $$(call Binary,ImpactsTable,src/CombineHarvester/CombineTools/bin,src_CombineHarvester_CombineTools_bin,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_BIN),bin,$(SCRAMSTORENAME_LOGS)))
ImpactsTable_CLASS := BINARY
else
$(eval $(call MultipleWarningMsg,ImpactsTable,src/CombineHarvester/CombineTools/bin))
endif
ifeq ($(strip $(MSSMExample)),)
MSSMExample := self/src/CombineHarvester/CombineTools/bin
MSSMExample_files := $(patsubst src/CombineHarvester/CombineTools/bin/%,%,$(foreach file,MSSMExample.cpp,$(eval xfile:=$(wildcard src/CombineHarvester/CombineTools/bin/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/CombineHarvester/CombineTools/bin/$(file). Please fix src/CombineHarvester/CombineTools/bin/BuildFile.))))
MSSMExample_BuildFile    := $(WORKINGDIR)/cache/bf/src/CombineHarvester/CombineTools/bin/BuildFile
MSSMExample_LOC_USE := self  root rootmath roofit roostats histfactory libxml2 vdt python boost_program_options boost_filesystem boost_python boost_regex rootpy CombineHarvester/CombineTools
MSSMExample_PACKAGE := self/src/CombineHarvester/CombineTools/bin
ALL_PRODS += MSSMExample
MSSMExample_INIT_FUNC        += $$(eval $$(call Binary,MSSMExample,src/CombineHarvester/CombineTools/bin,src_CombineHarvester_CombineTools_bin,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_BIN),bin,$(SCRAMSTORENAME_LOGS)))
MSSMExample_CLASS := BINARY
else
$(eval $(call MultipleWarningMsg,MSSMExample,src/CombineHarvester/CombineTools/bin))
endif
ALL_COMMONRULES += src_CombineHarvester_CombineTools_bin
src_CombineHarvester_CombineTools_bin_parent := CombineHarvester/CombineTools
src_CombineHarvester_CombineTools_bin_INIT_FUNC += $$(eval $$(call CommonProductRules,src_CombineHarvester_CombineTools_bin,src/CombineHarvester/CombineTools/bin,BINARY))
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
src_CombineHarvester_CombineTools_scripts_files := $(filter-out \#% %\#,$(notdir $(wildcard $(foreach dir,$(LOCALTOP)/src/CombineHarvester/CombineTools/scripts,$(dir)/*))))
$(eval $(call Src2StoreCopy,src_CombineHarvester_CombineTools_scripts,src/CombineHarvester/CombineTools/scripts,$(SCRAMSTORENAME_BIN),*))
ALL_PACKAGES += CombineHarvester/docs
subdirs_src_CombineHarvester_docs := src_CombineHarvester_docs_figures
