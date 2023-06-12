// Do NOT change. Changes will be lost next time file is generated

#define R__DICTIONARY_FILENAME tmpdIslc7_amd64_gcc700dIsrcdICombineHarvesterdICombinePdfsdIsrcdICombineHarvesterCombinePdfsdIadICombineHarvesterCombinePdfs_xr

/*******************************************************************/
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#define G__DICTIONARY
#include "RConfig.h"
#include "TClass.h"
#include "TDictAttributeMap.h"
#include "TInterpreter.h"
#include "TROOT.h"
#include "TBuffer.h"
#include "TMemberInspector.h"
#include "TInterpreter.h"
#include "TVirtualMutex.h"
#include "TError.h"

#ifndef G__ROOT
#define G__ROOT
#endif

#include "RtypesImp.h"
#include "TIsAProxy.h"
#include "TFileMergeInfo.h"
#include <algorithm>
#include "TCollectionProxyInfo.h"
/*******************************************************************/

#include "TDataMember.h"

// Since CINT ignores the std namespace, we need to do so in this file.
namespace std {} using namespace std;

// Header files passed as explicit arguments
#include "src/CombineHarvester/CombinePdfs/src/classes.h"

// Header files passed via #pragma extra_include

namespace ROOT {
   static TClass *chcLcLCMSHistFuncFactory_Dictionary();
   static void chcLcLCMSHistFuncFactory_TClassManip(TClass*);
   static void *new_chcLcLCMSHistFuncFactory(void *p = 0);
   static void *newArray_chcLcLCMSHistFuncFactory(Long_t size, void *p);
   static void delete_chcLcLCMSHistFuncFactory(void *p);
   static void deleteArray_chcLcLCMSHistFuncFactory(void *p);
   static void destruct_chcLcLCMSHistFuncFactory(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ch::CMSHistFuncFactory*)
   {
      ::ch::CMSHistFuncFactory *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::ch::CMSHistFuncFactory));
      static ::ROOT::TGenericClassInfo 
         instance("ch::CMSHistFuncFactory", "CombineHarvester/CombinePdfs/interface/CMSHistFuncFactory.h", 21,
                  typeid(::ch::CMSHistFuncFactory), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &chcLcLCMSHistFuncFactory_Dictionary, isa_proxy, 4,
                  sizeof(::ch::CMSHistFuncFactory) );
      instance.SetNew(&new_chcLcLCMSHistFuncFactory);
      instance.SetNewArray(&newArray_chcLcLCMSHistFuncFactory);
      instance.SetDelete(&delete_chcLcLCMSHistFuncFactory);
      instance.SetDeleteArray(&deleteArray_chcLcLCMSHistFuncFactory);
      instance.SetDestructor(&destruct_chcLcLCMSHistFuncFactory);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ch::CMSHistFuncFactory*)
   {
      return GenerateInitInstanceLocal((::ch::CMSHistFuncFactory*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::ch::CMSHistFuncFactory*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *chcLcLCMSHistFuncFactory_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::ch::CMSHistFuncFactory*)0x0)->GetClass();
      chcLcLCMSHistFuncFactory_TClassManip(theClass);
   return theClass;
   }

   static void chcLcLCMSHistFuncFactory_TClassManip(TClass* theClass){
      theClass->CreateAttributeMap();
      TDictAttributeMap* attrMap( theClass->GetAttributeMap() );
      attrMap->AddProperty("transient","true");
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_chcLcLCMSHistFuncFactory(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::ch::CMSHistFuncFactory : new ::ch::CMSHistFuncFactory;
   }
   static void *newArray_chcLcLCMSHistFuncFactory(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::ch::CMSHistFuncFactory[nElements] : new ::ch::CMSHistFuncFactory[nElements];
   }
   // Wrapper around operator delete
   static void delete_chcLcLCMSHistFuncFactory(void *p) {
      delete ((::ch::CMSHistFuncFactory*)p);
   }
   static void deleteArray_chcLcLCMSHistFuncFactory(void *p) {
      delete [] ((::ch::CMSHistFuncFactory*)p);
   }
   static void destruct_chcLcLCMSHistFuncFactory(void *p) {
      typedef ::ch::CMSHistFuncFactory current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::ch::CMSHistFuncFactory

namespace {
  void TriggerDictionaryInitialization_CombineHarvesterCombinePdfs_xr_Impl() {
    static const char* headers[] = {
0    };
    static const char* includePaths[] = {
"/uscms_data/d3/mreid/sueps/analysis/SUEPs/limittest/CMSSW_10_2_13/src",
"/cvmfs/cms.cern.ch/slc7_amd64_gcc700/cms/cmssw/CMSSW_10_2_13/src",
"/cvmfs/cms.cern.ch/slc7_amd64_gcc700/lcg/root/6.12.07-gnimlf5/include",
"/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/pcre/8.37-omkpbe2/include",
"/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/boost/1.63.0-gnimlf/include",
"/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/bz2lib/1.0.6-omkpbe2/include",
"/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/gsl/2.2.1-omkpbe2/include",
"/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/libxml2/2.9.1-omkpbe2/include/libxml2",
"/cvmfs/cms.cern.ch/slc7_amd64_gcc700/cms/vdt/0.4.0-gnimlf/include",
"/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/xz/5.2.2-omkpbe2/include",
"/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/zlib-x86_64/1.2.11-omkpbe2/include",
"/cvmfs/cms.cern.ch/slc7_amd64_gcc700/lcg/root/6.12.07-gnimlf5/include",
"/uscms_data/d3/mreid/sueps/analysis/SUEPs/limittest/CMSSW_10_2_13/",
0
    };
    static const char* fwdDeclCode = R"DICTFWDDCLS(
#line 1 "CombineHarvesterCombinePdfs_xr dictionary forward declarations' payload"
#pragma clang diagnostic ignored "-Wkeyword-compat"
#pragma clang diagnostic ignored "-Wignored-attributes"
#pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
extern int __Cling_Autoloading_Map;
namespace ch{class __attribute__((annotate(R"ATTRDUMP(transient@@@true)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$CombineHarvester/CombinePdfs/interface/CMSHistFuncFactory.h")))  CMSHistFuncFactory;}
)DICTFWDDCLS";
    static const char* payloadCode = R"DICTPAYLOAD(
#line 1 "CombineHarvesterCombinePdfs_xr dictionary payload"

#ifndef G__VECTOR_HAS_CLASS_ITERATOR
  #define G__VECTOR_HAS_CLASS_ITERATOR 1
#endif
#ifndef CMS_DICT_IMPL
  #define CMS_DICT_IMPL 1
#endif
#ifndef _REENTRANT
  #define _REENTRANT 1
#endif
#ifndef GNUSOURCE
  #define GNUSOURCE 1
#endif
#ifndef __STRICT_ANSI__
  #define __STRICT_ANSI__ 1
#endif
#ifndef GNU_GCC
  #define GNU_GCC 1
#endif
#ifndef _GNU_SOURCE
  #define _GNU_SOURCE 1
#endif
#ifndef BOOST_SPIRIT_THREADSAFE
  #define BOOST_SPIRIT_THREADSAFE 1
#endif
#ifndef PHOENIX_THREADSAFE
  #define PHOENIX_THREADSAFE 1
#endif
#ifndef CMSSW_GIT_HASH
  #define CMSSW_GIT_HASH "CMSSW_10_2_13"
#endif
#ifndef PROJECT_NAME
  #define PROJECT_NAME "CMSSW"
#endif
#ifndef PROJECT_VERSION
  #define PROJECT_VERSION "CMSSW_10_2_13"
#endif
#ifndef CMSSW_REFLEX_DICT
  #define CMSSW_REFLEX_DICT 1
#endif

#define _BACKWARD_BACKWARD_WARNING_H
#include "CombineHarvester/CombinePdfs/interface/MorphFunctions.h"
#include "CombineHarvester/CombinePdfs/interface/CMSHistFuncFactory.h"


#undef  _BACKWARD_BACKWARD_WARNING_H
)DICTPAYLOAD";
    static const char* classesHeaders[]={
"ch::BuildRooMorphing", payloadCode, "@",
"ch::CMSHistFuncFactory", payloadCode, "@",
nullptr};

    static bool isInitialized = false;
    if (!isInitialized) {
      TROOT::RegisterModule("CombineHarvesterCombinePdfs_xr",
        headers, includePaths, payloadCode, fwdDeclCode,
        TriggerDictionaryInitialization_CombineHarvesterCombinePdfs_xr_Impl, {}, classesHeaders);
      isInitialized = true;
    }
  }
  static struct DictInit {
    DictInit() {
      TriggerDictionaryInitialization_CombineHarvesterCombinePdfs_xr_Impl();
    }
  } __TheDictionaryInitializer;
}
void TriggerDictionaryInitialization_CombineHarvesterCombinePdfs_xr() {
  TriggerDictionaryInitialization_CombineHarvesterCombinePdfs_xr_Impl();
}
