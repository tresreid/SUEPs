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
