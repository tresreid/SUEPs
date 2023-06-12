ifeq ($(strip $(CombineHarvester/CombineTools)),)
ALL_COMMONRULES += src_CombineHarvester_CombineTools_src
src_CombineHarvester_CombineTools_src_parent := CombineHarvester/CombineTools
src_CombineHarvester_CombineTools_src_INIT_FUNC := $$(eval $$(call CommonProductRules,src_CombineHarvester_CombineTools_src,src/CombineHarvester/CombineTools/src,LIBRARY))
CombineHarvesterCombineTools := self/CombineHarvester/CombineTools
CombineHarvester/CombineTools := CombineHarvesterCombineTools
CombineHarvesterCombineTools_files := $(patsubst src/CombineHarvester/CombineTools/src/%,%,$(wildcard $(foreach dir,src/CombineHarvester/CombineTools/src ,$(foreach ext,$(SRC_FILES_SUFFIXES),$(dir)/*.$(ext)))))
CombineHarvesterCombineTools_BuildFile    := $(WORKINGDIR)/cache/bf/src/CombineHarvester/CombineTools/BuildFile
CombineHarvesterCombineTools_LOC_FLAGS_CXXFLAGS   := -fno-guess-branch-probability -fno-devirtualize -fno-tree-forwprop
CombineHarvesterCombineTools_LOC_USE := self  root rootmath roofit roostats histfactory libxml2 vdt python boost_program_options boost_filesystem boost_python boost_regex rootpy HiggsAnalysis/CombinedLimit
CombineHarvesterCombineTools_EX_LIB   := CombineHarvesterCombineTools
CombineHarvesterCombineTools_EX_USE   := $(foreach d,$(CombineHarvesterCombineTools_LOC_USE),$(if $($(d)_EX_FLAGS_NO_RECURSIVE_EXPORT),,$d))
CombineHarvesterCombineTools_PACKAGE := self/src/CombineHarvester/CombineTools/src
ALL_PRODS += CombineHarvesterCombineTools
CombineHarvesterCombineTools_CLASS := LIBRARY
CombineHarvester/CombineTools_forbigobj+=CombineHarvesterCombineTools
CombineHarvesterCombineTools_INIT_FUNC        += $$(eval $$(call Library,CombineHarvesterCombineTools,src/CombineHarvester/CombineTools/src,src_CombineHarvester_CombineTools_src,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_LIB),$(SCRAMSTORENAME_LOGS)))
endif
ifeq ($(strip $(HiggsAnalysis/CombinedLimit)),)
ALL_COMMONRULES += src_HiggsAnalysis_CombinedLimit_src
src_HiggsAnalysis_CombinedLimit_src_parent := HiggsAnalysis/CombinedLimit
src_HiggsAnalysis_CombinedLimit_src_INIT_FUNC := $$(eval $$(call CommonProductRules,src_HiggsAnalysis_CombinedLimit_src,src/HiggsAnalysis/CombinedLimit/src,LIBRARY))
HiggsAnalysisCombinedLimit := self/HiggsAnalysis/CombinedLimit
HiggsAnalysis/CombinedLimit := HiggsAnalysisCombinedLimit
HiggsAnalysisCombinedLimit_files := $(patsubst src/HiggsAnalysis/CombinedLimit/src/%,%,$(wildcard $(foreach dir,src/HiggsAnalysis/CombinedLimit/src ,$(foreach ext,$(SRC_FILES_SUFFIXES),$(dir)/*.$(ext)))))
HiggsAnalysisCombinedLimit_BuildFile    := $(WORKINGDIR)/cache/bf/src/HiggsAnalysis/CombinedLimit/BuildFile
HiggsAnalysisCombinedLimit_LOC_LIB   := Smatrix
HiggsAnalysisCombinedLimit_LOC_USE := self  root rootmath roofit roostats histfactory libxml2 vdt boost_program_options boost_filesystem
HiggsAnalysisCombinedLimit_LCGDICTS  := x 
HiggsAnalysisCombinedLimit_PRE_INIT_FUNC += $$(eval $$(call LCGDict,HiggsAnalysisCombinedLimit,src/HiggsAnalysis/CombinedLimit/src/classes.h,src/HiggsAnalysis/CombinedLimit/src/classes_def.xml,$(SCRAMSTORENAME_LIB),$(GENREFLEX_ARGS) --fail_on_warnings,))
HiggsAnalysisCombinedLimit_EX_LIB   := HiggsAnalysisCombinedLimit
HiggsAnalysisCombinedLimit_EX_USE   := $(foreach d,$(HiggsAnalysisCombinedLimit_LOC_USE),$(if $($(d)_EX_FLAGS_NO_RECURSIVE_EXPORT),,$d))
HiggsAnalysisCombinedLimit_PACKAGE := self/src/HiggsAnalysis/CombinedLimit/src
ALL_PRODS += HiggsAnalysisCombinedLimit
HiggsAnalysisCombinedLimit_CLASS := LIBRARY
HiggsAnalysis/CombinedLimit_forbigobj+=HiggsAnalysisCombinedLimit
HiggsAnalysisCombinedLimit_INIT_FUNC        += $$(eval $$(call Library,HiggsAnalysisCombinedLimit,src/HiggsAnalysis/CombinedLimit/src,src_HiggsAnalysis_CombinedLimit_src,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_LIB),$(SCRAMSTORENAME_LOGS)))
endif
