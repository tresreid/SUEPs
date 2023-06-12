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
