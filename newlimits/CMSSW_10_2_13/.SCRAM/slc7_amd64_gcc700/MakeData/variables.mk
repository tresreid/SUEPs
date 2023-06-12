############## All Tools Variables ################
TOOLS_OVERRIDABLE_FLAGS:=
ALL_LIB_TYPES:=
CUDA_TYPE_COMPILER        := cuda
CUDASRC_FILES_SUFFIXES := cu
CXXSRC_FILES_SUFFIXES     := cxx cc C cpp
CSRC_FILES_SUFFIXES       := c
FORTRANSRC_FILES_SUFFIXES := F f77 f F77
SRC_FILES_SUFFIXES        := $(CXXSRC_FILES_SUFFIXES) $(CSRC_FILES_SUFFIXES) $(FORTRANSRC_FILES_SUFFIXES) $(CUDASRC_FILES_SUFFIXES)
SCRAM_ADMIN_DIR           := .SCRAM/$(SCRAM_ARCH)
SCRAM_TOOLS_DIR           := $(SCRAM_ADMIN_DIR)/timestamps
CFLAGS:=
LIBRARY_CFLAGS:=
TEST_CFLAGS:=
BINARY_CFLAGS:=
EDM_CFLAGS:=
CAPABILITIES_CFLAGS:=
LCGDICT_CFLAGS:=
ROOTDICT_CFLAGS:=
PRECOMPILE_CFLAGS:=
DEV_CFLAGS:=
RELEASE_CFLAGS:=
REM_CFLAGS:=
REM_LIBRARY_CFLAGS:=
REM_TEST_CFLAGS:=
REM_BINARY_CFLAGS:=
REM_EDM_CFLAGS:=
REM_CAPABILITIES_CFLAGS:=
REM_LCGDICT_CFLAGS:=
REM_ROOTDICT_CFLAGS:=
REM_PRECOMPILE_CFLAGS:=
REM_DEV_CFLAGS:=
REM_RELEASE_CFLAGS:=
CPPDEFINES:=
LIBRARY_CPPDEFINES:=
TEST_CPPDEFINES:=
BINARY_CPPDEFINES:=
EDM_CPPDEFINES:=
CAPABILITIES_CPPDEFINES:=
LCGDICT_CPPDEFINES:=
ROOTDICT_CPPDEFINES:=
PRECOMPILE_CPPDEFINES:=
DEV_CPPDEFINES:=
RELEASE_CPPDEFINES:=
REM_CPPDEFINES:=
REM_LIBRARY_CPPDEFINES:=
REM_TEST_CPPDEFINES:=
REM_BINARY_CPPDEFINES:=
REM_EDM_CPPDEFINES:=
REM_CAPABILITIES_CPPDEFINES:=
REM_LCGDICT_CPPDEFINES:=
REM_ROOTDICT_CPPDEFINES:=
REM_PRECOMPILE_CPPDEFINES:=
REM_DEV_CPPDEFINES:=
REM_RELEASE_CPPDEFINES:=
CPPFLAGS:=
LIBRARY_CPPFLAGS:=
TEST_CPPFLAGS:=
BINARY_CPPFLAGS:=
EDM_CPPFLAGS:=
CAPABILITIES_CPPFLAGS:=
LCGDICT_CPPFLAGS:=
ROOTDICT_CPPFLAGS:=
PRECOMPILE_CPPFLAGS:=
DEV_CPPFLAGS:=
RELEASE_CPPFLAGS:=
REM_CPPFLAGS:=
REM_LIBRARY_CPPFLAGS:=
REM_TEST_CPPFLAGS:=
REM_BINARY_CPPFLAGS:=
REM_EDM_CPPFLAGS:=
REM_CAPABILITIES_CPPFLAGS:=
REM_LCGDICT_CPPFLAGS:=
REM_ROOTDICT_CPPFLAGS:=
REM_PRECOMPILE_CPPFLAGS:=
REM_DEV_CPPFLAGS:=
REM_RELEASE_CPPFLAGS:=
CSHAREDOBJECTFLAGS:=
LIBRARY_CSHAREDOBJECTFLAGS:=
TEST_CSHAREDOBJECTFLAGS:=
BINARY_CSHAREDOBJECTFLAGS:=
EDM_CSHAREDOBJECTFLAGS:=
CAPABILITIES_CSHAREDOBJECTFLAGS:=
LCGDICT_CSHAREDOBJECTFLAGS:=
ROOTDICT_CSHAREDOBJECTFLAGS:=
PRECOMPILE_CSHAREDOBJECTFLAGS:=
DEV_CSHAREDOBJECTFLAGS:=
RELEASE_CSHAREDOBJECTFLAGS:=
REM_CSHAREDOBJECTFLAGS:=
REM_LIBRARY_CSHAREDOBJECTFLAGS:=
REM_TEST_CSHAREDOBJECTFLAGS:=
REM_BINARY_CSHAREDOBJECTFLAGS:=
REM_EDM_CSHAREDOBJECTFLAGS:=
REM_CAPABILITIES_CSHAREDOBJECTFLAGS:=
REM_LCGDICT_CSHAREDOBJECTFLAGS:=
REM_ROOTDICT_CSHAREDOBJECTFLAGS:=
REM_PRECOMPILE_CSHAREDOBJECTFLAGS:=
REM_DEV_CSHAREDOBJECTFLAGS:=
REM_RELEASE_CSHAREDOBJECTFLAGS:=
CUDA_FLAGS:=
LIBRARY_CUDA_FLAGS:=
TEST_CUDA_FLAGS:=
BINARY_CUDA_FLAGS:=
EDM_CUDA_FLAGS:=
CAPABILITIES_CUDA_FLAGS:=
LCGDICT_CUDA_FLAGS:=
ROOTDICT_CUDA_FLAGS:=
PRECOMPILE_CUDA_FLAGS:=
DEV_CUDA_FLAGS:=
RELEASE_CUDA_FLAGS:=
REM_CUDA_FLAGS:=
REM_LIBRARY_CUDA_FLAGS:=
REM_TEST_CUDA_FLAGS:=
REM_BINARY_CUDA_FLAGS:=
REM_EDM_CUDA_FLAGS:=
REM_CAPABILITIES_CUDA_FLAGS:=
REM_LCGDICT_CUDA_FLAGS:=
REM_ROOTDICT_CUDA_FLAGS:=
REM_PRECOMPILE_CUDA_FLAGS:=
REM_DEV_CUDA_FLAGS:=
REM_RELEASE_CUDA_FLAGS:=
CUDA_LDFLAGS:=
LIBRARY_CUDA_LDFLAGS:=
TEST_CUDA_LDFLAGS:=
BINARY_CUDA_LDFLAGS:=
EDM_CUDA_LDFLAGS:=
CAPABILITIES_CUDA_LDFLAGS:=
LCGDICT_CUDA_LDFLAGS:=
ROOTDICT_CUDA_LDFLAGS:=
PRECOMPILE_CUDA_LDFLAGS:=
DEV_CUDA_LDFLAGS:=
RELEASE_CUDA_LDFLAGS:=
REM_CUDA_LDFLAGS:=
REM_LIBRARY_CUDA_LDFLAGS:=
REM_TEST_CUDA_LDFLAGS:=
REM_BINARY_CUDA_LDFLAGS:=
REM_EDM_CUDA_LDFLAGS:=
REM_CAPABILITIES_CUDA_LDFLAGS:=
REM_LCGDICT_CUDA_LDFLAGS:=
REM_ROOTDICT_CUDA_LDFLAGS:=
REM_PRECOMPILE_CUDA_LDFLAGS:=
REM_DEV_CUDA_LDFLAGS:=
REM_RELEASE_CUDA_LDFLAGS:=
CXXFLAGS:=
LIBRARY_CXXFLAGS:=
TEST_CXXFLAGS:=
BINARY_CXXFLAGS:=
EDM_CXXFLAGS:=
CAPABILITIES_CXXFLAGS:=
LCGDICT_CXXFLAGS:=
ROOTDICT_CXXFLAGS:=
PRECOMPILE_CXXFLAGS:=
DEV_CXXFLAGS:=
RELEASE_CXXFLAGS:=
REM_CXXFLAGS:=
REM_LIBRARY_CXXFLAGS:=
REM_TEST_CXXFLAGS:=
REM_BINARY_CXXFLAGS:=
REM_EDM_CXXFLAGS:=
REM_CAPABILITIES_CXXFLAGS:=
REM_LCGDICT_CXXFLAGS:=
REM_ROOTDICT_CXXFLAGS:=
REM_PRECOMPILE_CXXFLAGS:=
REM_DEV_CXXFLAGS:=
REM_RELEASE_CXXFLAGS:=
CXXSHAREDFLAGS:=
LIBRARY_CXXSHAREDFLAGS:=
TEST_CXXSHAREDFLAGS:=
BINARY_CXXSHAREDFLAGS:=
EDM_CXXSHAREDFLAGS:=
CAPABILITIES_CXXSHAREDFLAGS:=
LCGDICT_CXXSHAREDFLAGS:=
ROOTDICT_CXXSHAREDFLAGS:=
PRECOMPILE_CXXSHAREDFLAGS:=
DEV_CXXSHAREDFLAGS:=
RELEASE_CXXSHAREDFLAGS:=
REM_CXXSHAREDFLAGS:=
REM_LIBRARY_CXXSHAREDFLAGS:=
REM_TEST_CXXSHAREDFLAGS:=
REM_BINARY_CXXSHAREDFLAGS:=
REM_EDM_CXXSHAREDFLAGS:=
REM_CAPABILITIES_CXXSHAREDFLAGS:=
REM_LCGDICT_CXXSHAREDFLAGS:=
REM_ROOTDICT_CXXSHAREDFLAGS:=
REM_PRECOMPILE_CXXSHAREDFLAGS:=
REM_DEV_CXXSHAREDFLAGS:=
REM_RELEASE_CXXSHAREDFLAGS:=
CXXSHAREDOBJECTFLAGS:=
LIBRARY_CXXSHAREDOBJECTFLAGS:=
TEST_CXXSHAREDOBJECTFLAGS:=
BINARY_CXXSHAREDOBJECTFLAGS:=
EDM_CXXSHAREDOBJECTFLAGS:=
CAPABILITIES_CXXSHAREDOBJECTFLAGS:=
LCGDICT_CXXSHAREDOBJECTFLAGS:=
ROOTDICT_CXXSHAREDOBJECTFLAGS:=
PRECOMPILE_CXXSHAREDOBJECTFLAGS:=
DEV_CXXSHAREDOBJECTFLAGS:=
RELEASE_CXXSHAREDOBJECTFLAGS:=
REM_CXXSHAREDOBJECTFLAGS:=
REM_LIBRARY_CXXSHAREDOBJECTFLAGS:=
REM_TEST_CXXSHAREDOBJECTFLAGS:=
REM_BINARY_CXXSHAREDOBJECTFLAGS:=
REM_EDM_CXXSHAREDOBJECTFLAGS:=
REM_CAPABILITIES_CXXSHAREDOBJECTFLAGS:=
REM_LCGDICT_CXXSHAREDOBJECTFLAGS:=
REM_ROOTDICT_CXXSHAREDOBJECTFLAGS:=
REM_PRECOMPILE_CXXSHAREDOBJECTFLAGS:=
REM_DEV_CXXSHAREDOBJECTFLAGS:=
REM_RELEASE_CXXSHAREDOBJECTFLAGS:=
FFLAGS:=
LIBRARY_FFLAGS:=
TEST_FFLAGS:=
BINARY_FFLAGS:=
EDM_FFLAGS:=
CAPABILITIES_FFLAGS:=
LCGDICT_FFLAGS:=
ROOTDICT_FFLAGS:=
PRECOMPILE_FFLAGS:=
DEV_FFLAGS:=
RELEASE_FFLAGS:=
REM_FFLAGS:=
REM_LIBRARY_FFLAGS:=
REM_TEST_FFLAGS:=
REM_BINARY_FFLAGS:=
REM_EDM_FFLAGS:=
REM_CAPABILITIES_FFLAGS:=
REM_LCGDICT_FFLAGS:=
REM_ROOTDICT_FFLAGS:=
REM_PRECOMPILE_FFLAGS:=
REM_DEV_FFLAGS:=
REM_RELEASE_FFLAGS:=
FOPTIMISEDFLAGS:=
LIBRARY_FOPTIMISEDFLAGS:=
TEST_FOPTIMISEDFLAGS:=
BINARY_FOPTIMISEDFLAGS:=
EDM_FOPTIMISEDFLAGS:=
CAPABILITIES_FOPTIMISEDFLAGS:=
LCGDICT_FOPTIMISEDFLAGS:=
ROOTDICT_FOPTIMISEDFLAGS:=
PRECOMPILE_FOPTIMISEDFLAGS:=
DEV_FOPTIMISEDFLAGS:=
RELEASE_FOPTIMISEDFLAGS:=
REM_FOPTIMISEDFLAGS:=
REM_LIBRARY_FOPTIMISEDFLAGS:=
REM_TEST_FOPTIMISEDFLAGS:=
REM_BINARY_FOPTIMISEDFLAGS:=
REM_EDM_FOPTIMISEDFLAGS:=
REM_CAPABILITIES_FOPTIMISEDFLAGS:=
REM_LCGDICT_FOPTIMISEDFLAGS:=
REM_ROOTDICT_FOPTIMISEDFLAGS:=
REM_PRECOMPILE_FOPTIMISEDFLAGS:=
REM_DEV_FOPTIMISEDFLAGS:=
REM_RELEASE_FOPTIMISEDFLAGS:=
FSHAREDOBJECTFLAGS:=
LIBRARY_FSHAREDOBJECTFLAGS:=
TEST_FSHAREDOBJECTFLAGS:=
BINARY_FSHAREDOBJECTFLAGS:=
EDM_FSHAREDOBJECTFLAGS:=
CAPABILITIES_FSHAREDOBJECTFLAGS:=
LCGDICT_FSHAREDOBJECTFLAGS:=
ROOTDICT_FSHAREDOBJECTFLAGS:=
PRECOMPILE_FSHAREDOBJECTFLAGS:=
DEV_FSHAREDOBJECTFLAGS:=
RELEASE_FSHAREDOBJECTFLAGS:=
REM_FSHAREDOBJECTFLAGS:=
REM_LIBRARY_FSHAREDOBJECTFLAGS:=
REM_TEST_FSHAREDOBJECTFLAGS:=
REM_BINARY_FSHAREDOBJECTFLAGS:=
REM_EDM_FSHAREDOBJECTFLAGS:=
REM_CAPABILITIES_FSHAREDOBJECTFLAGS:=
REM_LCGDICT_FSHAREDOBJECTFLAGS:=
REM_ROOTDICT_FSHAREDOBJECTFLAGS:=
REM_PRECOMPILE_FSHAREDOBJECTFLAGS:=
REM_DEV_FSHAREDOBJECTFLAGS:=
REM_RELEASE_FSHAREDOBJECTFLAGS:=
LDFLAGS:=
LIBRARY_LDFLAGS:=
TEST_LDFLAGS:=
BINARY_LDFLAGS:=
EDM_LDFLAGS:=
CAPABILITIES_LDFLAGS:=
LCGDICT_LDFLAGS:=
ROOTDICT_LDFLAGS:=
PRECOMPILE_LDFLAGS:=
DEV_LDFLAGS:=
RELEASE_LDFLAGS:=
REM_LDFLAGS:=
REM_LIBRARY_LDFLAGS:=
REM_TEST_LDFLAGS:=
REM_BINARY_LDFLAGS:=
REM_EDM_LDFLAGS:=
REM_CAPABILITIES_LDFLAGS:=
REM_LCGDICT_LDFLAGS:=
REM_ROOTDICT_LDFLAGS:=
REM_PRECOMPILE_LDFLAGS:=
REM_DEV_LDFLAGS:=
REM_RELEASE_LDFLAGS:=
LD_UNIT:=
LIBRARY_LD_UNIT:=
TEST_LD_UNIT:=
BINARY_LD_UNIT:=
EDM_LD_UNIT:=
CAPABILITIES_LD_UNIT:=
LCGDICT_LD_UNIT:=
ROOTDICT_LD_UNIT:=
PRECOMPILE_LD_UNIT:=
DEV_LD_UNIT:=
RELEASE_LD_UNIT:=
REM_LD_UNIT:=
REM_LIBRARY_LD_UNIT:=
REM_TEST_LD_UNIT:=
REM_BINARY_LD_UNIT:=
REM_EDM_LD_UNIT:=
REM_CAPABILITIES_LD_UNIT:=
REM_LCGDICT_LD_UNIT:=
REM_ROOTDICT_LD_UNIT:=
REM_PRECOMPILE_LD_UNIT:=
REM_DEV_LD_UNIT:=
REM_RELEASE_LD_UNIT:=
ALL_COMPILER_FLAGS := CFLAGS CPPDEFINES CPPFLAGS CSHAREDOBJECTFLAGS CUDA_FLAGS CUDA_LDFLAGS CXXFLAGS CXXSHAREDFLAGS CXXSHAREDOBJECTFLAGS FFLAGS FOPTIMISEDFLAGS FSHAREDOBJECTFLAGS LDFLAGS LD_UNIT 
SCRAM_MULTIPLE_COMPILERS := yes
SCRAM_DEFAULT_COMPILER    := gcc
SCRAM_COMPILER            := $(SCRAM_DEFAULT_COMPILER)
ifdef COMPILER
SCRAM_COMPILER            := $(COMPILER)
endif
CXX_TYPE_COMPILER := cxxcompiler
C_TYPE_COMPILER := ccompiler
F77_TYPE_COMPILER := f77compiler
ifndef SCRAM_IGNORE_MISSING_COMPILERS
$(if $(wildcard $(SCRAM_TOOLS_DIR)/$(SCRAM_COMPILER)-$(CXX_TYPE_COMPILER)),,$(info ****WARNING: You have selected $(SCRAM_COMPILER) as compiler but there is no $(SCRAM_COMPILER)-$(CXX_TYPE_COMPILER) tool setup. Default compiler $(SCRAM_DEFAULT_COMPILER)-$(CXX_TYPE_COMPILER) will be used to comple CXX files))
$(if $(wildcard $(SCRAM_TOOLS_DIR)/$(SCRAM_COMPILER)-$(C_TYPE_COMPILER)),,$(info ****WARNING: You have selected $(SCRAM_COMPILER) as compiler but there is no $(SCRAM_COMPILER)-$(C_TYPE_COMPILER) tool setup. Default compiler $(SCRAM_DEFAULT_COMPILER)-$(C_TYPE_COMPILER) will be used to comple C files))
$(if $(wildcard $(SCRAM_TOOLS_DIR)/$(SCRAM_COMPILER)-$(F77_TYPE_COMPILER)),,$(info ****WARNING: You have selected $(SCRAM_COMPILER) as compiler but there is no $(SCRAM_COMPILER)-$(F77_TYPE_COMPILER) tool setup. Default compiler $(SCRAM_DEFAULT_COMPILER)-$(F77_TYPE_COMPILER) will be used to comple F77 files))
endif
GCC_CXXCOMPILER_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/gcc/7.0.0-omkpbe2
CXX:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/gcc/7.0.0-omkpbe2/bin/c++
GCC_CCOMPILER_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/gcc/7.0.0-omkpbe2
CC:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/gcc/7.0.0-omkpbe2/bin/gcc
GCC_F77COMPILER_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/gcc/7.0.0-omkpbe2
FC:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/gcc/7.0.0-omkpbe2/bin/gfortran
ALL_TOOLS  += cxxcompiler
cxxcompiler_EX_USE    := $(if $(strip $(wildcard $(LOCALTOP)/$(SCRAM_TOOLS_DIR)/$(SCRAM_COMPILER)-cxxcompiler)),$(SCRAM_COMPILER)-cxxcompiler,$(SCRAM_DEFAULT_COMPILER)-cxxcompiler)
ALL_TOOLS  += ccompiler
ccompiler_EX_USE    := $(if $(strip $(wildcard $(LOCALTOP)/$(SCRAM_TOOLS_DIR)/$(SCRAM_COMPILER)-ccompiler)),$(SCRAM_COMPILER)-ccompiler,$(SCRAM_DEFAULT_COMPILER)-ccompiler)
ALL_TOOLS  += f77compiler
f77compiler_EX_USE    := $(if $(strip $(wildcard $(LOCALTOP)/$(SCRAM_TOOLS_DIR)/$(SCRAM_COMPILER)-f77compiler)),$(SCRAM_COMPILER)-f77compiler,$(SCRAM_DEFAULT_COMPILER)-f77compiler)
CMSSW_BASE:=/uscms_data/d3/mreid/sueps/analysis/SUEPs/newlimits/CMSSW_10_2_13
PROTOBUF_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/protobuf/3.5.2
BINDIR:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/protobuf/3.5.2/bin
CLHEP_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/clhep/2.4.0.0-gnimlf
LAPACK_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/lapack/3.6.1-gnimlf
LIBHEPML_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/libhepml/0.2.1-omkpbe2
BOOST_PYTHON_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/boost/1.63.0-gnimlf
DOXYGEN_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/doxygen/1.8.11-gnimlf
RIVET_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/rivet/2.5.4-gnimlf6
DPM_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/dpm/1.8.0.1-omkpbe2
MAKE_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/gmake/4.2.1-omkpbe2
HEPMC_HEADERS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/hepmc/2.06.07-omkpbe2
CSCTRACKFINDEREMULATION_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/cms/CSCTrackFinderEmulation/1.2-omkpbe2
GCC_ATOMIC_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/gcc/7.0.0-omkpbe2
PY2_JUPYTER_CLIENT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-jupyter_client/5.2.3
LIBUUID_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/libuuid/2.22.2-omkpbe2
FREETYPE_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/freetype/2.5.3-omkpbe2
BLACKHAT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/blackhat/0.9.9-omkpbe4
PY2_THEANO_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-Theano/1.0.2
LIBXSLT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/libxslt/1.1.28-omkpbe4
MCTESTER_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/mctester/1.25.0a-gnimlf6
GIFLIB_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/giflib/4.2.3-omkpbe2
PY2_IPYTHON_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-ipython/5.5.0-gnimlf2
PY2_PYBIND11_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-pybind11/2.2.3
VECGEOM_INTERFACE_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/vecgeom/v00.05.00-gnimlf
TOPREX_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/toprex/4.23-omkpbe2
XTL_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/xtl/0.4.1-gnimlf
TCMALLOC_MINIMAL_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/gperftools/2.6.1-omkpbe2
SIP_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/sip/4.17-omkpbe4
ORACLE_ADMINDIR:=/etc
FASTJET_CONTRIB_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/fastjet-contrib/1.033-omkpbe
LCOV_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/lcov/1.9
PY2_HISTOGRAMMAR_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-histogrammar/1.0.9-gnimlf
PYMINUIT2_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/pyminuit2/0.0.1-gnimlf6
PY2_CYTHON_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-cython/0.28.3
YAML_CPP_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/yaml-cpp/0.6.2-gnimlf
LLVM_ANALYZER_CXXCOMPILER_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/llvm/6.0.0-ogkkac
ifeq ($(strip $(SCRAM_COMPILER)),llvm-analyzer)
CXX:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/llvm/6.0.0-ogkkac/bin/c++-analyzer
endif
XERCES_C_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/xerces-c/3.1.3-omkpbe2
GMP_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/gmp-static/6.1.0-omkpbe2
LLVM_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/llvm/6.0.0-ogkkac
CUB_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/cub/1.8.0-ogkkac
FASTJET_CONTRIB_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/fastjet-contrib/1.033-omkpbe
GEANT4CORE_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/geant4/10.04-gnimlf3
G4LIB:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/geant4/10.04-gnimlf3/lib
PYQT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/pyqt/4.11.4-omkpbe4
HEPMC_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/hepmc/2.06.07-omkpbe2
TAUOLA_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/tauola/27.121.5-omkpbe2
LHAPDF_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/lhapdf/6.2.1-gnimlf2
SCONS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/scons/3.0.1
ifeq ($(strip $(SCRAM_COMPILER)),ccache)
CC:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/ccache/3.1.8-omkpbe2/bin/gcc
endif
ifeq ($(strip $(SCRAM_COMPILER)),ccache)
CXX:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/ccache/3.1.8-omkpbe2/bin/c++
export CCACHE_BASEDIR:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/cms/cmssw/CMSSW_10_2_13
endif
PY2_PYTEST_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-pytest/3.4.1-gnimlf
ifeq ($(strip $(SCRAM_COMPILER)),llvm)
FC:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/gcc/7.0.0-omkpbe2/bin/gfortran
endif
PY2_PYGMENTS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-Pygments/2.2.0-gnimlf
PY2_NBFORMAT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-nbformat/4.4.0-gnimlf
NUMPY_C_API_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-numpy/1.14.1-gnimlf
CURL_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/curl/7.59.0
GNUPLOT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/gnuplot/4.6.5-omkpbe2
MADGRAPH5AMCATNLO_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/madgraph5amcatnlo/2.6.0-gnimlf8
GEANT4STATIC_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/geant4/10.04-gnimlf3
ifeq ($(strip $(SCRAM_COMPILER)),ccache)
FC:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/ccache/3.1.8-omkpbe2/bin/gfortran
endif
DMTCP_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/dmtcp/3.0.0-dev-omkpbe2
PYDATA_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/pythia6/426-omkpbe2
PYCLANG_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/llvm/6.0.0-ogkkac
MXNET_PREDICT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/mxnet-predict/1.2.1
PY2_NOTEBOOK_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-notebook/5.4.0-gnimlf2
CATCH2_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/catch2/2.2.2
PY2_JSONSCHEMA_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-jsonschema/2.6.0-gnimlf
DB6_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/db6/6.0.30-omkpbe2
CVS2GIT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/cvs2git/5419-omkpbe4
PYTHON_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/python/2.7.14-omkpbe4
PYTHON_COMPILE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/python/2.7.14-omkpbe4/lib/python2.7/compileall.py
PYTHIA8_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/pythia8/230-gnimlf4
BZ2LIB_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/bz2lib/1.0.6-omkpbe2
QD_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/qd/2.3.13-omkpbe2
SLOCCOUNT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/sloccount/2.26-omkpbe2
GDBM_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/gdbm/1.10-omkpbe2
LWTNN_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/lwtnn/2.4-gnimlf4
VINCIA_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/vincia/2.2.01-gnimlf4
PY2_HYPEROPT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-hyperopt/0.1-gnimlf2
EXPAT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/expat/2.1.0-omkpbe2
FFTJET_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/fftjet/1.5.0-omkpbe2
PROFESSOR_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/professor/1.4.0-gnimlf6
HEPPDT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/heppdt/3.03.00-omkpbe2
PY2_LINT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-lint/0.25.1-gnimlf
CORAL_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/cms/coral/CORAL_2_3_21-gnimlf9
DAVIX_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/davix/0.6.7-gnimlf2
PYTHON3_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/python3/3.6.4-gnimlf
PYTHON3_COMPILE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/python3/3.6.4-gnimlf/lib/python3.6/compileall.py
OPENLDAP_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/openldap/2.4.45-omkpbe2
MPFR_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/mpfr-static/3.1.3-omkpbe2
PY2_NOSE_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-nose/1.3.7-gnimlf
VECGEOM_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/vecgeom/v00.05.00-gnimlf
LIBFFI_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/libffi/3.2.1-omkpbe2
PY2_CHARDET_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-chardet/3.0.4-gnimlf
CLHEPHEADER_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/clhep/2.4.0.0-gnimlf
JIMMY_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/jimmy/4.2-gnimlf2
DIRE_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/dire/2.002
CLASSLIB_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/classlib/3.1.3-omkpbe2
IGPROF_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/igprof/5.9.16-gnimlf
TCMALLOC_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/gperftools/2.6.1-omkpbe2
ORACLE_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/oracle/12.1.0.2.0
PHOTOS_HEADERS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/photos/215.5-omkpbe2
CHARYBDIS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/charybdis/1.003-gnimlf2
FASTJET_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/fastjet/3.3.0-omkpbe
YODA_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/yoda/1.6.7-gnimlf6
PY2_AVRO_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-avro/1.8.2-gnimlf
GLIBC_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/glibc/2.17-78.el7_2.12-1.166.el6_7.3
LIBTIFF_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/libtiff/4.0.3-omkpbe2
HERWIG_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/herwig/6.521-gnimlf2
GSL_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/gsl/2.2.1-omkpbe2
OPENMPI_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/openmpi/2.1.5
UTM_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/utm/utm_0.7.1-gnimlf
ORACLEOCCI_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/cms/cms_oracleocci_abi_hack/20180210-omkpbe
QT3SUPPORT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/qt/4.8.7-omkpbe2
ROOTRFLX_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/lcg/root/6.12.07-gnimlf5
CUDA_GDB_WRAPPER_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/cuda-gdb-wrapper/1.0-ogkkac
QTDESIGNER_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/qt/4.8.7-omkpbe2
PY2_JUPYTER_CONSOLE_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-jupyter_console/5.2.0-gnimlf2
XROOTD_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/xrootd/4.8.3-gnimlf
GEANT4DATA_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external
ifeq ($(strip $(SCRAM_COMPILER)),distcc)
CXX:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/distcc/3.2rc1-omkpbe4/bin/c++
endif
OPENLOOPS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/openloops/2.0.b
DCAP_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/dcap/2.47.8-omkpbe2
JIMMY_HEADERS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/jimmy/4.2-gnimlf2
PY2_TENSORFLOW_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-tensorflow/1.6.0-gnimlf4
FRONTIER_CLIENT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/frontier_client/2.8.20-omkpbe4
PY2_NBCONVERT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-nbconvert/5.3.1-gnimlf2
LLVM_CCOMPILER_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/llvm/6.0.0-ogkkac
ifeq ($(strip $(SCRAM_COMPILER)),llvm)
CC:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/llvm/6.0.0-ogkkac/bin/clang
endif
GOSAMCONTRIB_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/gosamcontrib/2.0-20150803-omkpbe2
CASCADE_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/cascade/2.2.04-gnimlf2
PACPARSER_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/pacparser/1.3.5-omkpbe2
BOOSTHEADER_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/boost/1.63.0-gnimlf
PYTHIA6_HEADERS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/pythia6/426-omkpbe2
PY2_SYMPY_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-sympy/1.1.1-gnimlf
DD4HEP_CMS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/dd4hep/v01-08x-gnimlf2
PROFESSOR2_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/professor2/2.2.1-gnimlf7
XTENSOR_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/xtensor/0.15.4-gnimlf
PY2_SETUPTOOLS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-setuptools/28.3.0-gnimlf
BOOST_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/boost/1.63.0-gnimlf
CUDA_API_WRAPPERS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/cuda-api-wrappers/20180504-ogkkac
OPENBLAS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/OpenBLAS/0.2.20-omkpbe2
ifeq ($(strip $(SCRAM_COMPILER)),iwyu)
LLVM_CXXCOMPILER_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/llvm/6.0.0-ogkkac
CXX:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/llvm/6.0.0-ogkkac/bin/include-what-you-use
endif
ZLIB_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/zlib-x86_64/1.2.11-omkpbe2
GBL_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/gbl/V02-01-03-gnimlf3
XZ_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/xz/5.2.2-omkpbe2
DD4HEP_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/dd4hep/v01-08x-gnimlf2
LIBXML2_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/libxml2/2.9.1-omkpbe2
STARLIGHT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/starlight/r193-gnimlf
ITTNOTIFY_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/ittnotify/16.06.18-gnimlf
PHOTOSPP_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/photospp/3.61-omkpbe2
MCDB_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/mcdb/1.0.3-omkpbe2
PY2_TABLES_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-tables/3.4.2-gnimlf
SHERPA_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/sherpa/2.2.5-gnimlf
PYTHIA6_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/pythia6/426-omkpbe2
ifeq ($(strip $(SCRAM_COMPILER)),distcc)
CC:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/distcc/3.2rc1-omkpbe4/bin/gcc
endif
FFTW3_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/fftw3/3.3.2-omkpbe2
PY2_TQDM_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-tqdm/4.23.4
THEPEG_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/thepeg/2.1.4-gnimlf
LLVM_ANALYZER_CCOMPILER_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/llvm/6.0.0-ogkkac
ifeq ($(strip $(SCRAM_COMPILER)),llvm-analyzer)
CC:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/llvm/6.0.0-ogkkac/bin/ccc-analyzer
endif
QT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/qt/4.8.7-omkpbe2
SIGCPP_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/sigcpp/2.6.2-omkpbe2
GOOGLE_BENCHMARK_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/google-benchmark/1.4.x
LIBJPEG_TURBO_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/libjpeg-turbo/1.3.1-omkpbe2
PCRE_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/pcre/8.37-omkpbe2
TENSORFLOW_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/tensorflow/1.6.0-gnimlf2
TFCOMPILE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/tensorflow/1.6.0-gnimlf2/bin/tfcompile
PY2_JUPYTER_CORE_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-jupyter_core/4.4.0-gnimlf
TINYXML2_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/tinyxml2/6.2.0
MILLEPEDE_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/millepede/V04-03-08-omkpbe2
OPENSSL_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/openssl/1.0.2d-omkpbe2
TBB_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/tbb/2018_U1-omkpbe2
HDF5_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/hdf5/1.8.17-omkpbe2
ALPGEN_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/alpgen/214-omkpbe2
PY2_VIRTUALENV_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-virtualenv/15.1.0-gnimlf
LIBUNGIF_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/libungif/4.1.4-omkpbe2
PY2_DXR_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-dxr/1.0-ogkkac
GRAPHVIZ_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/graphviz/2.38.0-omkpbe2
CMSSWDATA_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/cms
CMSSW_DATA_PATH:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/cms
PY2_NUMPY_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-numpy/1.14.1-gnimlf
HECTOR_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/hector/1.3.4_patch1-gnimlf6
PY2_VIRTUALENVWRAPPER_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-virtualenvwrapper/4.8.2-gnimlf
JEMALLOC_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/jemalloc/5.1.0
GEANT4_PARFULLCMS:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/geant4-parfullcms/2014.01.27-gnimlf3
QTBASE_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/qt/4.8.7-omkpbe2
PY2_LIZARD_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-lizard/1.12.15-gnimlf
TAUOLA_HEADERS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/tauola/27.121.5-omkpbe2
TKONLINESW_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/tkonlinesw/4.2.0-1_gcc7-gnimlf6
ROOTCLING_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/lcg/root/6.12.07-gnimlf5
TINYXML_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/tinyxml/2.5.3-gnimlf
KTJET_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/ktjet/1.06-gnimlf
CUDA_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/cuda/9.2.148
NVCC:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/cuda/9.2.148/bin/nvcc
CUDA_STUBS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/cuda/9.2.148
VDT_HEADERS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/cms/vdt/0.4.0-gnimlf
VDT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/cms/vdt/0.4.0-gnimlf
PY2_PIP_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-pip/9.0.3-gnimlf
GDB_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/gdb/8.1-omkpbe3
ifeq ($(strip $(SCRAM_COMPILER)),distcc)
FC:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/distcc/3.2rc1-omkpbe4/bin/gfortran
endif
CASCADE_HEADERS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/cascade/2.2.04-gnimlf2
EIGEN_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/eigen/64060da8461a627eb25b5a7bc0616776068db58b
CPPUNIT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/cppunit/1.12.1-omkpbe2
PY2_PLAC_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-plac/0.9.6
GOSAM_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/gosam/2.0.4-33b41ed-gnimlf2
HERWIGPP_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/herwigpp/7.1.4-gnimlf
ROOT_INTERFACE_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/lcg/root/6.12.07-gnimlf5
PY2_DEEPDISH_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-deepdish/0.3.6-gnimlf2
TAUOLAPP_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/tauolapp/1.1.5-gnimlf4
PY2_PBR_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-pbr/3.1.1-gnimlf
DAS_CLIENT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/cms/das_client/v03.01.00-omkpbe4
PY2_FLAWFINDER_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-flawfinder/2.0.6
LIBPNG_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/libpng/1.6.16-omkpbe2
MD5_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/md5/1.0.0-omkpbe2
PHOTOS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/photos/215.5-omkpbe2
SQLITE_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/sqlite/3.22.0-omkpbe
PY2_QTCONSOLE_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-qtconsole/4.3.1-gnimlf2
CGAL_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/cgal/4.2-gnimlf2
EVTGEN_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/evtgen/1.6.0-gnimlf4
GIT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/git/2.17.0
PY2_ROOTPY_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-rootpy/1.0.1-gnimlf6
PY2_FS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-fs/2.0.23
VALGRIND_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/valgrind/3.13.0-omkpbe2
LLVM_CXXCOMPILER_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/llvm/6.0.0-ogkkac
ifeq ($(strip $(SCRAM_COMPILER)),llvm)
CXX:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/llvm/6.0.0-ogkkac/bin/clang++
endif
MESCHACH_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/meschach/1.2.pCMS1-omkpbe2
TOPREX_HEADERS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/toprex/4.23-omkpbe2
ROOFIT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/lcg/root/6.12.07-gnimlf5
GLIMPSE_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/glimpse/4.18.5-omkpbe2
############## All SCRAM ENV variables ################
LOCALTOP:=/uscms_data/d3/mreid/sueps/analysis/SUEPs/newlimits/CMSSW_10_2_13
SCRAM_TMP:=tmp
SCRAM_INIT_LOCALTOP:=/uscms_data/d3/mreid/sueps/analysis/SUEPs/newlimits/CMSSW_10_2_13
SCRAM_BUILDFILE:=BuildFile
RELEASETOP:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/cms/cmssw/CMSSW_10_2_13
SCRAM_INTlog:=logs
SCRAM_GMAKE_PATH:=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/gmake/4.2.1-omkpbe2/bin/
SCRAM_INTwork:=tmp/slc7_amd64_gcc700
SCRAM_PROJECTNAME:=CMSSW
SCRAM_ARCH:=slc7_amd64_gcc700
SCRAM_SOURCEDIR:=src
SCRAM_RTBOURNE_SET:=CMSSW:CMSSW_10_2_13:slc7_amd64_gcc700:V2_2_9_pre16:SRT_
SCRAM_CONFIGCHKSUM:=V05-07-32
SCRAM_RUNTIME_TYPE:=BUILD
SCRAM_LOOKUPDB_WRITE:=/cvmfs/cms.cern.ch
SCRAM_CXX11_ABI:=1
SCRAM_PROJECTVERSION:=CMSSW_10_2_13
SCRAM_CONFIGDIR:=config
################ ALL SCRAM Stores #######################
ALL_PRODUCT_STORES:=
SCRAMSTORENAME_LOGS:=logs/slc7_amd64_gcc700
ALL_PRODUCT_STORES+=$(SCRAMSTORENAME_LOGS)
SCRAMSTORENAME_LIB:=lib/slc7_amd64_gcc700
ALL_PRODUCT_STORES+=$(SCRAMSTORENAME_LIB)
SCRAMSTORENAME_INCLUDE:=include
ALL_PRODUCT_STORES+=$(SCRAMSTORENAME_INCLUDE)
SCRAMSTORENAME_CFIPYTHON:=cfipython/slc7_amd64_gcc700
ALL_PRODUCT_STORES+=$(SCRAMSTORENAME_CFIPYTHON)
SCRAMSTORENAME_STATIC:=static/slc7_amd64_gcc700
ALL_PRODUCT_STORES+=$(SCRAMSTORENAME_STATIC)
SCRAMSTORENAME_BIGLIB:=biglib/slc7_amd64_gcc700
ALL_PRODUCT_STORES+=$(SCRAMSTORENAME_BIGLIB)
SCRAMSTORENAME_OBJS:=objs/slc7_amd64_gcc700
ALL_PRODUCT_STORES+=$(SCRAMSTORENAME_OBJS)
SCRAMSTORENAME_DOC:=doc
ALL_PRODUCT_STORES+=$(SCRAMSTORENAME_DOC)
SCRAMSTORENAME_TEST:=test/slc7_amd64_gcc700
ALL_PRODUCT_STORES+=$(SCRAMSTORENAME_TEST)
SCRAMSTORENAME_PYTHON:=python
ALL_PRODUCT_STORES+=$(SCRAMSTORENAME_PYTHON)
SCRAMSTORENAME_BIN:=bin/slc7_amd64_gcc700
ALL_PRODUCT_STORES+=$(SCRAMSTORENAME_BIN)
