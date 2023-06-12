ifeq ($(strip $(CombineHarvester/CombinePdfs)),)
ALL_COMMONRULES += src_CombineHarvester_CombinePdfs_src
src_CombineHarvester_CombinePdfs_src_parent := CombineHarvester/CombinePdfs
src_CombineHarvester_CombinePdfs_src_INIT_FUNC := $$(eval $$(call CommonProductRules,src_CombineHarvester_CombinePdfs_src,src/CombineHarvester/CombinePdfs/src,LIBRARY))
CombineHarvesterCombinePdfs := self/CombineHarvester/CombinePdfs
CombineHarvester/CombinePdfs := CombineHarvesterCombinePdfs
CombineHarvesterCombinePdfs_files := $(patsubst src/CombineHarvester/CombinePdfs/src/%,%,$(wildcard $(foreach dir,src/CombineHarvester/CombinePdfs/src ,$(foreach ext,$(SRC_FILES_SUFFIXES),$(dir)/*.$(ext)))))
CombineHarvesterCombinePdfs_BuildFile    := $(WORKINGDIR)/cache/bf/src/CombineHarvester/CombinePdfs/BuildFile
CombineHarvesterCombinePdfs_LOC_FLAGS_CXXFLAGS   := -fno-guess-branch-probability -fno-devirtualize -fno-tree-forwprop
CombineHarvesterCombinePdfs_LOC_USE := self  root rootmath roofit roostats histfactory libxml2 vdt boost_program_options boost_filesystem boost_regex CombineHarvester/CombineTools HiggsAnalysis/CombinedLimit
CombineHarvesterCombinePdfs_LCGDICTS  := x 
CombineHarvesterCombinePdfs_PRE_INIT_FUNC += $$(eval $$(call LCGDict,CombineHarvesterCombinePdfs,src/CombineHarvester/CombinePdfs/src/classes.h,src/CombineHarvester/CombinePdfs/src/classes_def.xml,$(SCRAMSTORENAME_LIB),$(GENREFLEX_ARGS) --fail_on_warnings,))
CombineHarvesterCombinePdfs_EX_LIB   := CombineHarvesterCombinePdfs
CombineHarvesterCombinePdfs_EX_USE   := $(foreach d,$(CombineHarvesterCombinePdfs_LOC_USE),$(if $($(d)_EX_FLAGS_NO_RECURSIVE_EXPORT),,$d))
CombineHarvesterCombinePdfs_PACKAGE := self/src/CombineHarvester/CombinePdfs/src
ALL_PRODS += CombineHarvesterCombinePdfs
CombineHarvesterCombinePdfs_CLASS := LIBRARY
CombineHarvester/CombinePdfs_forbigobj+=CombineHarvesterCombinePdfs
CombineHarvesterCombinePdfs_INIT_FUNC        += $$(eval $$(call Library,CombineHarvesterCombinePdfs,src/CombineHarvester/CombinePdfs/src,src_CombineHarvester_CombinePdfs_src,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_LIB),$(SCRAMSTORENAME_LOGS)))
endif
