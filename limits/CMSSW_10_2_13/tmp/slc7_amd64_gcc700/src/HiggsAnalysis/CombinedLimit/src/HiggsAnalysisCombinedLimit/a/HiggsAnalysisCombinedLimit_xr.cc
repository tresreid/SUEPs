// Do NOT change. Changes will be lost next time file is generated

#define R__DICTIONARY_FILENAME tmpdIslc7_amd64_gcc700dIsrcdIHiggsAnalysisdICombinedLimitdIsrcdIHiggsAnalysisCombinedLimitdIadIHiggsAnalysisCombinedLimit_xr

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
#include "src/HiggsAnalysis/CombinedLimit/src/classes.h"

// Header files passed via #pragma extra_include

namespace ROOT {
   static TClass *__gnu_cxxcLcL__normal_iteratorlEvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR_Dictionary();
   static void __gnu_cxxcLcL__normal_iteratorlEvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR_TClassManip(TClass*);
   static void *new___gnu_cxxcLcL__normal_iteratorlEvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR(void *p = 0);
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR(Long_t size, void *p);
   static void delete___gnu_cxxcLcL__normal_iteratorlEvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR(void *p);
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR(void *p);
   static void destruct___gnu_cxxcLcL__normal_iteratorlEvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::__gnu_cxx::__normal_iterator<vector<double>*,vector<vector<double> > >*)
   {
      ::__gnu_cxx::__normal_iterator<vector<double>*,vector<vector<double> > > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::__gnu_cxx::__normal_iterator<vector<double>*,vector<vector<double> > >));
      static ::ROOT::TGenericClassInfo 
         instance("__gnu_cxx::__normal_iterator<vector<double>*,vector<vector<double> > >", "string", 760,
                  typeid(::__gnu_cxx::__normal_iterator<vector<double>*,vector<vector<double> > >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &__gnu_cxxcLcL__normal_iteratorlEvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(::__gnu_cxx::__normal_iterator<vector<double>*,vector<vector<double> > >) );
      instance.SetNew(&new___gnu_cxxcLcL__normal_iteratorlEvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR);
      instance.SetNewArray(&newArray___gnu_cxxcLcL__normal_iteratorlEvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR);
      instance.SetDelete(&delete___gnu_cxxcLcL__normal_iteratorlEvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR);
      instance.SetDeleteArray(&deleteArray___gnu_cxxcLcL__normal_iteratorlEvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR);
      instance.SetDestructor(&destruct___gnu_cxxcLcL__normal_iteratorlEvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR);

      ::ROOT::AddClassAlternate("__gnu_cxx::__normal_iterator<vector<double>*,vector<vector<double> > >","vector<std::vector<Double_t> >::iterator");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::__gnu_cxx::__normal_iterator<vector<double>*,vector<vector<double> > >*)
   {
      return GenerateInitInstanceLocal((::__gnu_cxx::__normal_iterator<vector<double>*,vector<vector<double> > >*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<vector<double>*,vector<vector<double> > >*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *__gnu_cxxcLcL__normal_iteratorlEvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<vector<double>*,vector<vector<double> > >*)0x0)->GetClass();
      __gnu_cxxcLcL__normal_iteratorlEvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void __gnu_cxxcLcL__normal_iteratorlEvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *__gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR_Dictionary();
   static void __gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR_TClassManip(TClass*);
   static void *new___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR(void *p = 0);
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR(Long_t size, void *p);
   static void delete___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR(void *p);
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR(void *p);
   static void destruct___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::__gnu_cxx::__normal_iterator<const vector<double>*,vector<vector<double> > >*)
   {
      ::__gnu_cxx::__normal_iterator<const vector<double>*,vector<vector<double> > > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::__gnu_cxx::__normal_iterator<const vector<double>*,vector<vector<double> > >));
      static ::ROOT::TGenericClassInfo 
         instance("__gnu_cxx::__normal_iterator<const vector<double>*,vector<vector<double> > >", "string", 760,
                  typeid(::__gnu_cxx::__normal_iterator<const vector<double>*,vector<vector<double> > >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &__gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(::__gnu_cxx::__normal_iterator<const vector<double>*,vector<vector<double> > >) );
      instance.SetNew(&new___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR);
      instance.SetNewArray(&newArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR);
      instance.SetDelete(&delete___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR);
      instance.SetDeleteArray(&deleteArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR);
      instance.SetDestructor(&destruct___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR);

      ::ROOT::AddClassAlternate("__gnu_cxx::__normal_iterator<const vector<double>*,vector<vector<double> > >","vector<std::vector<Double_t> >::const_iterator");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::__gnu_cxx::__normal_iterator<const vector<double>*,vector<vector<double> > >*)
   {
      return GenerateInitInstanceLocal((::__gnu_cxx::__normal_iterator<const vector<double>*,vector<vector<double> > >*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<const vector<double>*,vector<vector<double> > >*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *__gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<const vector<double>*,vector<vector<double> > >*)0x0)->GetClass();
      __gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void __gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *__gnu_cxxcLcL__normal_iteratorlEvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR_Dictionary();
   static void __gnu_cxxcLcL__normal_iteratorlEvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR_TClassManip(TClass*);
   static void *new___gnu_cxxcLcL__normal_iteratorlEvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR(void *p = 0);
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR(Long_t size, void *p);
   static void delete___gnu_cxxcLcL__normal_iteratorlEvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR(void *p);
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR(void *p);
   static void destruct___gnu_cxxcLcL__normal_iteratorlEvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::__gnu_cxx::__normal_iterator<vector<float>*,vector<vector<float> > >*)
   {
      ::__gnu_cxx::__normal_iterator<vector<float>*,vector<vector<float> > > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::__gnu_cxx::__normal_iterator<vector<float>*,vector<vector<float> > >));
      static ::ROOT::TGenericClassInfo 
         instance("__gnu_cxx::__normal_iterator<vector<float>*,vector<vector<float> > >", "string", 760,
                  typeid(::__gnu_cxx::__normal_iterator<vector<float>*,vector<vector<float> > >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &__gnu_cxxcLcL__normal_iteratorlEvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(::__gnu_cxx::__normal_iterator<vector<float>*,vector<vector<float> > >) );
      instance.SetNew(&new___gnu_cxxcLcL__normal_iteratorlEvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR);
      instance.SetNewArray(&newArray___gnu_cxxcLcL__normal_iteratorlEvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR);
      instance.SetDelete(&delete___gnu_cxxcLcL__normal_iteratorlEvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR);
      instance.SetDeleteArray(&deleteArray___gnu_cxxcLcL__normal_iteratorlEvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR);
      instance.SetDestructor(&destruct___gnu_cxxcLcL__normal_iteratorlEvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR);

      ::ROOT::AddClassAlternate("__gnu_cxx::__normal_iterator<vector<float>*,vector<vector<float> > >","vector<std::vector<Float_t> >::iterator");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::__gnu_cxx::__normal_iterator<vector<float>*,vector<vector<float> > >*)
   {
      return GenerateInitInstanceLocal((::__gnu_cxx::__normal_iterator<vector<float>*,vector<vector<float> > >*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<vector<float>*,vector<vector<float> > >*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *__gnu_cxxcLcL__normal_iteratorlEvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<vector<float>*,vector<vector<float> > >*)0x0)->GetClass();
      __gnu_cxxcLcL__normal_iteratorlEvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void __gnu_cxxcLcL__normal_iteratorlEvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *__gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR_Dictionary();
   static void __gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR_TClassManip(TClass*);
   static void *new___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR(void *p = 0);
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR(Long_t size, void *p);
   static void delete___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR(void *p);
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR(void *p);
   static void destruct___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::__gnu_cxx::__normal_iterator<const vector<float>*,vector<vector<float> > >*)
   {
      ::__gnu_cxx::__normal_iterator<const vector<float>*,vector<vector<float> > > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::__gnu_cxx::__normal_iterator<const vector<float>*,vector<vector<float> > >));
      static ::ROOT::TGenericClassInfo 
         instance("__gnu_cxx::__normal_iterator<const vector<float>*,vector<vector<float> > >", "string", 760,
                  typeid(::__gnu_cxx::__normal_iterator<const vector<float>*,vector<vector<float> > >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &__gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(::__gnu_cxx::__normal_iterator<const vector<float>*,vector<vector<float> > >) );
      instance.SetNew(&new___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR);
      instance.SetNewArray(&newArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR);
      instance.SetDelete(&delete___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR);
      instance.SetDeleteArray(&deleteArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR);
      instance.SetDestructor(&destruct___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR);

      ::ROOT::AddClassAlternate("__gnu_cxx::__normal_iterator<const vector<float>*,vector<vector<float> > >","vector<std::vector<Float_t> >::const_iterator");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::__gnu_cxx::__normal_iterator<const vector<float>*,vector<vector<float> > >*)
   {
      return GenerateInitInstanceLocal((::__gnu_cxx::__normal_iterator<const vector<float>*,vector<vector<float> > >*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<const vector<float>*,vector<vector<float> > >*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *__gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<const vector<float>*,vector<vector<float> > >*)0x0)->GetClass();
      __gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void __gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *__gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR_Dictionary();
   static void __gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR_TClassManip(TClass*);
   static void *new___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR(void *p = 0);
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR(Long_t size, void *p);
   static void delete___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR(void *p);
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR(void *p);
   static void destruct___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::__gnu_cxx::__normal_iterator<vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > >*)
   {
      ::__gnu_cxx::__normal_iterator<vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::__gnu_cxx::__normal_iterator<vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > >));
      static ::ROOT::TGenericClassInfo 
         instance("__gnu_cxx::__normal_iterator<vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > >", "string", 760,
                  typeid(::__gnu_cxx::__normal_iterator<vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &__gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(::__gnu_cxx::__normal_iterator<vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > >) );
      instance.SetNew(&new___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR);
      instance.SetNewArray(&newArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR);
      instance.SetDelete(&delete___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR);
      instance.SetDeleteArray(&deleteArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR);
      instance.SetDestructor(&destruct___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR);

      ::ROOT::AddClassAlternate("__gnu_cxx::__normal_iterator<vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > >","vector<std::vector<std::vector<std::vector<Float_t> > > >::iterator");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::__gnu_cxx::__normal_iterator<vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > >*)
   {
      return GenerateInitInstanceLocal((::__gnu_cxx::__normal_iterator<vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > >*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > >*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *__gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > >*)0x0)->GetClass();
      __gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void __gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *__gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR_Dictionary();
   static void __gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR_TClassManip(TClass*);
   static void *new___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR(void *p = 0);
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR(Long_t size, void *p);
   static void delete___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR(void *p);
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR(void *p);
   static void destruct___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::__gnu_cxx::__normal_iterator<const vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > >*)
   {
      ::__gnu_cxx::__normal_iterator<const vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::__gnu_cxx::__normal_iterator<const vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > >));
      static ::ROOT::TGenericClassInfo 
         instance("__gnu_cxx::__normal_iterator<const vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > >", "string", 760,
                  typeid(::__gnu_cxx::__normal_iterator<const vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &__gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(::__gnu_cxx::__normal_iterator<const vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > >) );
      instance.SetNew(&new___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR);
      instance.SetNewArray(&newArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR);
      instance.SetDelete(&delete___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR);
      instance.SetDeleteArray(&deleteArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR);
      instance.SetDestructor(&destruct___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR);

      ::ROOT::AddClassAlternate("__gnu_cxx::__normal_iterator<const vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > >","vector<std::vector<std::vector<std::vector<Float_t> > > >::const_iterator");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::__gnu_cxx::__normal_iterator<const vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > >*)
   {
      return GenerateInitInstanceLocal((::__gnu_cxx::__normal_iterator<const vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > >*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<const vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > >*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *__gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<const vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > >*)0x0)->GetClass();
      __gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void __gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *__gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR_Dictionary();
   static void __gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR_TClassManip(TClass*);
   static void *new___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR(void *p = 0);
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR(Long_t size, void *p);
   static void delete___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR(void *p);
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR(void *p);
   static void destruct___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::__gnu_cxx::__normal_iterator<vector<vector<float> >*,vector<vector<vector<float> > > >*)
   {
      ::__gnu_cxx::__normal_iterator<vector<vector<float> >*,vector<vector<vector<float> > > > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::__gnu_cxx::__normal_iterator<vector<vector<float> >*,vector<vector<vector<float> > > >));
      static ::ROOT::TGenericClassInfo 
         instance("__gnu_cxx::__normal_iterator<vector<vector<float> >*,vector<vector<vector<float> > > >", "string", 760,
                  typeid(::__gnu_cxx::__normal_iterator<vector<vector<float> >*,vector<vector<vector<float> > > >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &__gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(::__gnu_cxx::__normal_iterator<vector<vector<float> >*,vector<vector<vector<float> > > >) );
      instance.SetNew(&new___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR);
      instance.SetNewArray(&newArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR);
      instance.SetDelete(&delete___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR);
      instance.SetDeleteArray(&deleteArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR);
      instance.SetDestructor(&destruct___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR);

      ::ROOT::AddClassAlternate("__gnu_cxx::__normal_iterator<vector<vector<float> >*,vector<vector<vector<float> > > >","vector<std::vector<std::vector<Float_t> > >::iterator");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::__gnu_cxx::__normal_iterator<vector<vector<float> >*,vector<vector<vector<float> > > >*)
   {
      return GenerateInitInstanceLocal((::__gnu_cxx::__normal_iterator<vector<vector<float> >*,vector<vector<vector<float> > > >*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<vector<vector<float> >*,vector<vector<vector<float> > > >*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *__gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<vector<vector<float> >*,vector<vector<vector<float> > > >*)0x0)->GetClass();
      __gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void __gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *__gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR_Dictionary();
   static void __gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR_TClassManip(TClass*);
   static void *new___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR(void *p = 0);
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR(Long_t size, void *p);
   static void delete___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR(void *p);
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR(void *p);
   static void destruct___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::__gnu_cxx::__normal_iterator<const vector<vector<float> >*,vector<vector<vector<float> > > >*)
   {
      ::__gnu_cxx::__normal_iterator<const vector<vector<float> >*,vector<vector<vector<float> > > > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::__gnu_cxx::__normal_iterator<const vector<vector<float> >*,vector<vector<vector<float> > > >));
      static ::ROOT::TGenericClassInfo 
         instance("__gnu_cxx::__normal_iterator<const vector<vector<float> >*,vector<vector<vector<float> > > >", "string", 760,
                  typeid(::__gnu_cxx::__normal_iterator<const vector<vector<float> >*,vector<vector<vector<float> > > >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &__gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(::__gnu_cxx::__normal_iterator<const vector<vector<float> >*,vector<vector<vector<float> > > >) );
      instance.SetNew(&new___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR);
      instance.SetNewArray(&newArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR);
      instance.SetDelete(&delete___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR);
      instance.SetDeleteArray(&deleteArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR);
      instance.SetDestructor(&destruct___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR);

      ::ROOT::AddClassAlternate("__gnu_cxx::__normal_iterator<const vector<vector<float> >*,vector<vector<vector<float> > > >","vector<std::vector<std::vector<Float_t> > >::const_iterator");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::__gnu_cxx::__normal_iterator<const vector<vector<float> >*,vector<vector<vector<float> > > >*)
   {
      return GenerateInitInstanceLocal((::__gnu_cxx::__normal_iterator<const vector<vector<float> >*,vector<vector<vector<float> > > >*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<const vector<vector<float> >*,vector<vector<vector<float> > > >*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *__gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<const vector<vector<float> >*,vector<vector<vector<float> > > >*)0x0)->GetClass();
      __gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void __gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *__gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR_Dictionary();
   static void __gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR_TClassManip(TClass*);
   static void *new___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR(void *p = 0);
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR(Long_t size, void *p);
   static void delete___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR(void *p);
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR(void *p);
   static void destruct___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > >*)
   {
      ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > >));
      static ::ROOT::TGenericClassInfo 
         instance("__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > >", "string", 760,
                  typeid(::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &__gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > >) );
      instance.SetNew(&new___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR);
      instance.SetNewArray(&newArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR);
      instance.SetDelete(&delete___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR);
      instance.SetDeleteArray(&deleteArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR);
      instance.SetDestructor(&destruct___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR);

      ::ROOT::AddClassAlternate("__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > >","vector<std::vector<std::vector<std::vector<std::vector<std::vector<Float_t> > > > > >::iterator");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > >*)
   {
      return GenerateInitInstanceLocal((::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > >*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > >*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *__gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > >*)0x0)->GetClass();
      __gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void __gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *__gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR_Dictionary();
   static void __gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR_TClassManip(TClass*);
   static void *new___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR(void *p = 0);
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR(Long_t size, void *p);
   static void delete___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR(void *p);
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR(void *p);
   static void destruct___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > >*)
   {
      ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > >));
      static ::ROOT::TGenericClassInfo 
         instance("__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > >", "string", 760,
                  typeid(::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &__gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > >) );
      instance.SetNew(&new___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR);
      instance.SetNewArray(&newArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR);
      instance.SetDelete(&delete___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR);
      instance.SetDeleteArray(&deleteArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR);
      instance.SetDestructor(&destruct___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR);

      ::ROOT::AddClassAlternate("__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > >","vector<std::vector<std::vector<std::vector<std::vector<std::vector<Float_t> > > > > >::const_iterator");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > >*)
   {
      return GenerateInitInstanceLocal((::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > >*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > >*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *__gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > >*)0x0)->GetClass();
      __gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void __gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *__gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR_Dictionary();
   static void __gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR_TClassManip(TClass*);
   static void *new___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR(void *p = 0);
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR(Long_t size, void *p);
   static void delete___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR(void *p);
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR(void *p);
   static void destruct___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > >*)
   {
      ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > >));
      static ::ROOT::TGenericClassInfo 
         instance("__gnu_cxx::__normal_iterator<vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > >", "string", 760,
                  typeid(::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &__gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > >) );
      instance.SetNew(&new___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR);
      instance.SetNewArray(&newArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR);
      instance.SetDelete(&delete___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR);
      instance.SetDeleteArray(&deleteArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR);
      instance.SetDestructor(&destruct___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR);

      ::ROOT::AddClassAlternate("__gnu_cxx::__normal_iterator<vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > >","vector<std::vector<std::vector<std::vector<std::vector<Float_t> > > > >::iterator");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > >*)
   {
      return GenerateInitInstanceLocal((::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > >*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > >*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *__gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > >*)0x0)->GetClass();
      __gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void __gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *__gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR_Dictionary();
   static void __gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR_TClassManip(TClass*);
   static void *new___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR(void *p = 0);
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR(Long_t size, void *p);
   static void delete___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR(void *p);
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR(void *p);
   static void destruct___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > >*)
   {
      ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > >));
      static ::ROOT::TGenericClassInfo 
         instance("__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > >", "string", 760,
                  typeid(::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &__gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > >) );
      instance.SetNew(&new___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR);
      instance.SetNewArray(&newArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR);
      instance.SetDelete(&delete___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR);
      instance.SetDeleteArray(&deleteArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR);
      instance.SetDestructor(&destruct___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR);

      ::ROOT::AddClassAlternate("__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > >","vector<std::vector<std::vector<std::vector<std::vector<Float_t> > > > >::const_iterator");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > >*)
   {
      return GenerateInitInstanceLocal((::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > >*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > >*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *__gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > >*)0x0)->GetClass();
      __gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void __gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *__gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR_Dictionary();
   static void __gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR_TClassManip(TClass*);
   static void *new___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR(void *p = 0);
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR(Long_t size, void *p);
   static void delete___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR(void *p);
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR(void *p);
   static void destruct___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > >*)
   {
      ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > >));
      static ::ROOT::TGenericClassInfo 
         instance("__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > >", "string", 760,
                  typeid(::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &__gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > >) );
      instance.SetNew(&new___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR);
      instance.SetNewArray(&newArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR);
      instance.SetDelete(&delete___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR);
      instance.SetDeleteArray(&deleteArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR);
      instance.SetDestructor(&destruct___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR);

      ::ROOT::AddClassAlternate("__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > >","vector<std::vector<std::vector<std::vector<std::vector<std::vector<Double_t> > > > > >::iterator");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > >*)
   {
      return GenerateInitInstanceLocal((::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > >*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > >*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *__gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > >*)0x0)->GetClass();
      __gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void __gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *__gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR_Dictionary();
   static void __gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR_TClassManip(TClass*);
   static void *new___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR(void *p = 0);
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR(Long_t size, void *p);
   static void delete___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR(void *p);
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR(void *p);
   static void destruct___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > >*)
   {
      ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > >));
      static ::ROOT::TGenericClassInfo 
         instance("__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > >", "string", 760,
                  typeid(::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &__gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > >) );
      instance.SetNew(&new___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR);
      instance.SetNewArray(&newArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR);
      instance.SetDelete(&delete___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR);
      instance.SetDeleteArray(&deleteArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR);
      instance.SetDestructor(&destruct___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR);

      ::ROOT::AddClassAlternate("__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > >","vector<std::vector<std::vector<std::vector<std::vector<std::vector<Double_t> > > > > >::const_iterator");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > >*)
   {
      return GenerateInitInstanceLocal((::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > >*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > >*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *__gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > >*)0x0)->GetClass();
      __gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void __gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *__gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR_Dictionary();
   static void __gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR_TClassManip(TClass*);
   static void *new___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR(void *p = 0);
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR(Long_t size, void *p);
   static void delete___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR(void *p);
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR(void *p);
   static void destruct___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > >*)
   {
      ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > >));
      static ::ROOT::TGenericClassInfo 
         instance("__gnu_cxx::__normal_iterator<vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > >", "string", 760,
                  typeid(::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &__gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > >) );
      instance.SetNew(&new___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR);
      instance.SetNewArray(&newArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR);
      instance.SetDelete(&delete___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR);
      instance.SetDeleteArray(&deleteArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR);
      instance.SetDestructor(&destruct___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR);

      ::ROOT::AddClassAlternate("__gnu_cxx::__normal_iterator<vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > >","vector<std::vector<std::vector<std::vector<std::vector<Double_t> > > > >::iterator");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > >*)
   {
      return GenerateInitInstanceLocal((::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > >*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > >*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *__gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > >*)0x0)->GetClass();
      __gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void __gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *__gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR_Dictionary();
   static void __gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR_TClassManip(TClass*);
   static void *new___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR(void *p = 0);
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR(Long_t size, void *p);
   static void delete___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR(void *p);
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR(void *p);
   static void destruct___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > >*)
   {
      ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > >));
      static ::ROOT::TGenericClassInfo 
         instance("__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > >", "string", 760,
                  typeid(::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &__gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > >) );
      instance.SetNew(&new___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR);
      instance.SetNewArray(&newArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR);
      instance.SetDelete(&delete___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR);
      instance.SetDeleteArray(&deleteArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR);
      instance.SetDestructor(&destruct___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR);

      ::ROOT::AddClassAlternate("__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > >","vector<std::vector<std::vector<std::vector<std::vector<Double_t> > > > >::const_iterator");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > >*)
   {
      return GenerateInitInstanceLocal((::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > >*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > >*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *__gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > >*)0x0)->GetClass();
      __gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void __gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *__gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR_Dictionary();
   static void __gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR_TClassManip(TClass*);
   static void *new___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR(void *p = 0);
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR(Long_t size, void *p);
   static void delete___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR(void *p);
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR(void *p);
   static void destruct___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::__gnu_cxx::__normal_iterator<vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > >*)
   {
      ::__gnu_cxx::__normal_iterator<vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::__gnu_cxx::__normal_iterator<vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > >));
      static ::ROOT::TGenericClassInfo 
         instance("__gnu_cxx::__normal_iterator<vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > >", "string", 760,
                  typeid(::__gnu_cxx::__normal_iterator<vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &__gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(::__gnu_cxx::__normal_iterator<vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > >) );
      instance.SetNew(&new___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR);
      instance.SetNewArray(&newArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR);
      instance.SetDelete(&delete___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR);
      instance.SetDeleteArray(&deleteArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR);
      instance.SetDestructor(&destruct___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR);

      ::ROOT::AddClassAlternate("__gnu_cxx::__normal_iterator<vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > >","vector<std::vector<std::vector<std::vector<Double_t> > > >::iterator");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::__gnu_cxx::__normal_iterator<vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > >*)
   {
      return GenerateInitInstanceLocal((::__gnu_cxx::__normal_iterator<vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > >*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > >*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *__gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > >*)0x0)->GetClass();
      __gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void __gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *__gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR_Dictionary();
   static void __gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR_TClassManip(TClass*);
   static void *new___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR(void *p = 0);
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR(Long_t size, void *p);
   static void delete___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR(void *p);
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR(void *p);
   static void destruct___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::__gnu_cxx::__normal_iterator<const vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > >*)
   {
      ::__gnu_cxx::__normal_iterator<const vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::__gnu_cxx::__normal_iterator<const vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > >));
      static ::ROOT::TGenericClassInfo 
         instance("__gnu_cxx::__normal_iterator<const vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > >", "string", 760,
                  typeid(::__gnu_cxx::__normal_iterator<const vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &__gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(::__gnu_cxx::__normal_iterator<const vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > >) );
      instance.SetNew(&new___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR);
      instance.SetNewArray(&newArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR);
      instance.SetDelete(&delete___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR);
      instance.SetDeleteArray(&deleteArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR);
      instance.SetDestructor(&destruct___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR);

      ::ROOT::AddClassAlternate("__gnu_cxx::__normal_iterator<const vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > >","vector<std::vector<std::vector<std::vector<Double_t> > > >::const_iterator");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::__gnu_cxx::__normal_iterator<const vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > >*)
   {
      return GenerateInitInstanceLocal((::__gnu_cxx::__normal_iterator<const vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > >*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<const vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > >*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *__gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<const vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > >*)0x0)->GetClass();
      __gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void __gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *__gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR_Dictionary();
   static void __gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR_TClassManip(TClass*);
   static void *new___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR(void *p = 0);
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR(Long_t size, void *p);
   static void delete___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR(void *p);
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR(void *p);
   static void destruct___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::__gnu_cxx::__normal_iterator<vector<vector<double> >*,vector<vector<vector<double> > > >*)
   {
      ::__gnu_cxx::__normal_iterator<vector<vector<double> >*,vector<vector<vector<double> > > > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::__gnu_cxx::__normal_iterator<vector<vector<double> >*,vector<vector<vector<double> > > >));
      static ::ROOT::TGenericClassInfo 
         instance("__gnu_cxx::__normal_iterator<vector<vector<double> >*,vector<vector<vector<double> > > >", "string", 760,
                  typeid(::__gnu_cxx::__normal_iterator<vector<vector<double> >*,vector<vector<vector<double> > > >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &__gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(::__gnu_cxx::__normal_iterator<vector<vector<double> >*,vector<vector<vector<double> > > >) );
      instance.SetNew(&new___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR);
      instance.SetNewArray(&newArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR);
      instance.SetDelete(&delete___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR);
      instance.SetDeleteArray(&deleteArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR);
      instance.SetDestructor(&destruct___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR);

      ::ROOT::AddClassAlternate("__gnu_cxx::__normal_iterator<vector<vector<double> >*,vector<vector<vector<double> > > >","vector<std::vector<std::vector<Double_t> > >::iterator");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::__gnu_cxx::__normal_iterator<vector<vector<double> >*,vector<vector<vector<double> > > >*)
   {
      return GenerateInitInstanceLocal((::__gnu_cxx::__normal_iterator<vector<vector<double> >*,vector<vector<vector<double> > > >*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<vector<vector<double> >*,vector<vector<vector<double> > > >*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *__gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<vector<vector<double> >*,vector<vector<vector<double> > > >*)0x0)->GetClass();
      __gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void __gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *__gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR_Dictionary();
   static void __gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR_TClassManip(TClass*);
   static void *new___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR(void *p = 0);
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR(Long_t size, void *p);
   static void delete___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR(void *p);
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR(void *p);
   static void destruct___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::__gnu_cxx::__normal_iterator<const vector<vector<double> >*,vector<vector<vector<double> > > >*)
   {
      ::__gnu_cxx::__normal_iterator<const vector<vector<double> >*,vector<vector<vector<double> > > > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::__gnu_cxx::__normal_iterator<const vector<vector<double> >*,vector<vector<vector<double> > > >));
      static ::ROOT::TGenericClassInfo 
         instance("__gnu_cxx::__normal_iterator<const vector<vector<double> >*,vector<vector<vector<double> > > >", "string", 760,
                  typeid(::__gnu_cxx::__normal_iterator<const vector<vector<double> >*,vector<vector<vector<double> > > >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &__gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(::__gnu_cxx::__normal_iterator<const vector<vector<double> >*,vector<vector<vector<double> > > >) );
      instance.SetNew(&new___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR);
      instance.SetNewArray(&newArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR);
      instance.SetDelete(&delete___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR);
      instance.SetDeleteArray(&deleteArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR);
      instance.SetDestructor(&destruct___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR);

      ::ROOT::AddClassAlternate("__gnu_cxx::__normal_iterator<const vector<vector<double> >*,vector<vector<vector<double> > > >","vector<std::vector<std::vector<Double_t> > >::const_iterator");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::__gnu_cxx::__normal_iterator<const vector<vector<double> >*,vector<vector<vector<double> > > >*)
   {
      return GenerateInitInstanceLocal((::__gnu_cxx::__normal_iterator<const vector<vector<double> >*,vector<vector<vector<double> > > >*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<const vector<vector<double> >*,vector<vector<vector<double> > > >*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *__gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::__gnu_cxx::__normal_iterator<const vector<vector<double> >*,vector<vector<vector<double> > > >*)0x0)->GetClass();
      __gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void __gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static void *new_TestProposal(void *p = 0);
   static void *newArray_TestProposal(Long_t size, void *p);
   static void delete_TestProposal(void *p);
   static void deleteArray_TestProposal(void *p);
   static void destruct_TestProposal(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::TestProposal*)
   {
      ::TestProposal *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::TestProposal >(0);
      static ::ROOT::TGenericClassInfo 
         instance("TestProposal", ::TestProposal::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/TestProposal.h", 13,
                  typeid(::TestProposal), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::TestProposal::Dictionary, isa_proxy, 4,
                  sizeof(::TestProposal) );
      instance.SetNew(&new_TestProposal);
      instance.SetNewArray(&newArray_TestProposal);
      instance.SetDelete(&delete_TestProposal);
      instance.SetDeleteArray(&deleteArray_TestProposal);
      instance.SetDestructor(&destruct_TestProposal);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::TestProposal*)
   {
      return GenerateInitInstanceLocal((::TestProposal*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::TestProposal*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_DebugProposal(void *p = 0);
   static void *newArray_DebugProposal(Long_t size, void *p);
   static void delete_DebugProposal(void *p);
   static void deleteArray_DebugProposal(void *p);
   static void destruct_DebugProposal(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::DebugProposal*)
   {
      ::DebugProposal *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::DebugProposal >(0);
      static ::ROOT::TGenericClassInfo 
         instance("DebugProposal", ::DebugProposal::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/DebugProposal.h", 14,
                  typeid(::DebugProposal), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::DebugProposal::Dictionary, isa_proxy, 4,
                  sizeof(::DebugProposal) );
      instance.SetNew(&new_DebugProposal);
      instance.SetNewArray(&newArray_DebugProposal);
      instance.SetDelete(&delete_DebugProposal);
      instance.SetDeleteArray(&deleteArray_DebugProposal);
      instance.SetDestructor(&destruct_DebugProposal);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::DebugProposal*)
   {
      return GenerateInitInstanceLocal((::DebugProposal*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::DebugProposal*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_VerticalInterpPdf(void *p = 0);
   static void *newArray_VerticalInterpPdf(Long_t size, void *p);
   static void delete_VerticalInterpPdf(void *p);
   static void deleteArray_VerticalInterpPdf(void *p);
   static void destruct_VerticalInterpPdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::VerticalInterpPdf*)
   {
      ::VerticalInterpPdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::VerticalInterpPdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("VerticalInterpPdf", ::VerticalInterpPdf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/VerticalInterpPdf.h", 12,
                  typeid(::VerticalInterpPdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::VerticalInterpPdf::Dictionary, isa_proxy, 4,
                  sizeof(::VerticalInterpPdf) );
      instance.SetNew(&new_VerticalInterpPdf);
      instance.SetNewArray(&newArray_VerticalInterpPdf);
      instance.SetDelete(&delete_VerticalInterpPdf);
      instance.SetDeleteArray(&deleteArray_VerticalInterpPdf);
      instance.SetDestructor(&destruct_VerticalInterpPdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::VerticalInterpPdf*)
   {
      return GenerateInitInstanceLocal((::VerticalInterpPdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::VerticalInterpPdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_SimpleCacheSentry(void *p = 0);
   static void *newArray_SimpleCacheSentry(Long_t size, void *p);
   static void delete_SimpleCacheSentry(void *p);
   static void deleteArray_SimpleCacheSentry(void *p);
   static void destruct_SimpleCacheSentry(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::SimpleCacheSentry*)
   {
      ::SimpleCacheSentry *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::SimpleCacheSentry >(0);
      static ::ROOT::TGenericClassInfo 
         instance("SimpleCacheSentry", ::SimpleCacheSentry::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/SimpleCacheSentry.h", 8,
                  typeid(::SimpleCacheSentry), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::SimpleCacheSentry::Dictionary, isa_proxy, 4,
                  sizeof(::SimpleCacheSentry) );
      instance.SetNew(&new_SimpleCacheSentry);
      instance.SetNewArray(&newArray_SimpleCacheSentry);
      instance.SetDelete(&delete_SimpleCacheSentry);
      instance.SetDeleteArray(&deleteArray_SimpleCacheSentry);
      instance.SetDestructor(&destruct_SimpleCacheSentry);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::SimpleCacheSentry*)
   {
      return GenerateInitInstanceLocal((::SimpleCacheSentry*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::SimpleCacheSentry*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static TClass *FastTemplate_Dictionary();
   static void FastTemplate_TClassManip(TClass*);
   static void *new_FastTemplate(void *p = 0);
   static void *newArray_FastTemplate(Long_t size, void *p);
   static void delete_FastTemplate(void *p);
   static void deleteArray_FastTemplate(void *p);
   static void destruct_FastTemplate(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::FastTemplate*)
   {
      ::FastTemplate *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::FastTemplate));
      static ::ROOT::TGenericClassInfo 
         instance("FastTemplate", "HiggsAnalysis/CombinedLimit/interface/FastTemplate_Old.h", 10,
                  typeid(::FastTemplate), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &FastTemplate_Dictionary, isa_proxy, 4,
                  sizeof(::FastTemplate) );
      instance.SetNew(&new_FastTemplate);
      instance.SetNewArray(&newArray_FastTemplate);
      instance.SetDelete(&delete_FastTemplate);
      instance.SetDeleteArray(&deleteArray_FastTemplate);
      instance.SetDestructor(&destruct_FastTemplate);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::FastTemplate*)
   {
      return GenerateInitInstanceLocal((::FastTemplate*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::FastTemplate*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *FastTemplate_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::FastTemplate*)0x0)->GetClass();
      FastTemplate_TClassManip(theClass);
   return theClass;
   }

   static void FastTemplate_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *FastHisto_Dictionary();
   static void FastHisto_TClassManip(TClass*);
   static void *new_FastHisto(void *p = 0);
   static void *newArray_FastHisto(Long_t size, void *p);
   static void delete_FastHisto(void *p);
   static void deleteArray_FastHisto(void *p);
   static void destruct_FastHisto(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::FastHisto*)
   {
      ::FastHisto *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::FastHisto));
      static ::ROOT::TGenericClassInfo 
         instance("FastHisto", "HiggsAnalysis/CombinedLimit/interface/FastTemplate_Old.h", 83,
                  typeid(::FastHisto), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &FastHisto_Dictionary, isa_proxy, 4,
                  sizeof(::FastHisto) );
      instance.SetNew(&new_FastHisto);
      instance.SetNewArray(&newArray_FastHisto);
      instance.SetDelete(&delete_FastHisto);
      instance.SetDeleteArray(&deleteArray_FastHisto);
      instance.SetDestructor(&destruct_FastHisto);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::FastHisto*)
   {
      return GenerateInitInstanceLocal((::FastHisto*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::FastHisto*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *FastHisto_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::FastHisto*)0x0)->GetClass();
      FastHisto_TClassManip(theClass);
   return theClass;
   }

   static void FastHisto_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *FastHisto2D_Dictionary();
   static void FastHisto2D_TClassManip(TClass*);
   static void *new_FastHisto2D(void *p = 0);
   static void *newArray_FastHisto2D(Long_t size, void *p);
   static void delete_FastHisto2D(void *p);
   static void deleteArray_FastHisto2D(void *p);
   static void destruct_FastHisto2D(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::FastHisto2D*)
   {
      ::FastHisto2D *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::FastHisto2D));
      static ::ROOT::TGenericClassInfo 
         instance("FastHisto2D", "HiggsAnalysis/CombinedLimit/interface/FastTemplate_Old.h", 132,
                  typeid(::FastHisto2D), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &FastHisto2D_Dictionary, isa_proxy, 4,
                  sizeof(::FastHisto2D) );
      instance.SetNew(&new_FastHisto2D);
      instance.SetNewArray(&newArray_FastHisto2D);
      instance.SetDelete(&delete_FastHisto2D);
      instance.SetDeleteArray(&deleteArray_FastHisto2D);
      instance.SetDestructor(&destruct_FastHisto2D);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::FastHisto2D*)
   {
      return GenerateInitInstanceLocal((::FastHisto2D*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::FastHisto2D*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *FastHisto2D_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::FastHisto2D*)0x0)->GetClass();
      FastHisto2D_TClassManip(theClass);
   return theClass;
   }

   static void FastHisto2D_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *FastHisto3D_Dictionary();
   static void FastHisto3D_TClassManip(TClass*);
   static void *new_FastHisto3D(void *p = 0);
   static void *newArray_FastHisto3D(Long_t size, void *p);
   static void delete_FastHisto3D(void *p);
   static void deleteArray_FastHisto3D(void *p);
   static void destruct_FastHisto3D(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::FastHisto3D*)
   {
      ::FastHisto3D *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::FastHisto3D));
      static ::ROOT::TGenericClassInfo 
         instance("FastHisto3D", "HiggsAnalysis/CombinedLimit/interface/FastTemplate_Old.h", 183,
                  typeid(::FastHisto3D), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &FastHisto3D_Dictionary, isa_proxy, 4,
                  sizeof(::FastHisto3D) );
      instance.SetNew(&new_FastHisto3D);
      instance.SetNewArray(&newArray_FastHisto3D);
      instance.SetDelete(&delete_FastHisto3D);
      instance.SetDeleteArray(&deleteArray_FastHisto3D);
      instance.SetDestructor(&destruct_FastHisto3D);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::FastHisto3D*)
   {
      return GenerateInitInstanceLocal((::FastHisto3D*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::FastHisto3D*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *FastHisto3D_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::FastHisto3D*)0x0)->GetClass();
      FastHisto3D_TClassManip(theClass);
   return theClass;
   }

   static void FastHisto3D_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static void *new_VerticalInterpHistPdf(void *p = 0);
   static void *newArray_VerticalInterpHistPdf(Long_t size, void *p);
   static void delete_VerticalInterpHistPdf(void *p);
   static void deleteArray_VerticalInterpHistPdf(void *p);
   static void destruct_VerticalInterpHistPdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::VerticalInterpHistPdf*)
   {
      ::VerticalInterpHistPdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::VerticalInterpHistPdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("VerticalInterpHistPdf", ::VerticalInterpHistPdf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/VerticalInterpHistPdf.h", 20,
                  typeid(::VerticalInterpHistPdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::VerticalInterpHistPdf::Dictionary, isa_proxy, 4,
                  sizeof(::VerticalInterpHistPdf) );
      instance.SetNew(&new_VerticalInterpHistPdf);
      instance.SetNewArray(&newArray_VerticalInterpHistPdf);
      instance.SetDelete(&delete_VerticalInterpHistPdf);
      instance.SetDeleteArray(&deleteArray_VerticalInterpHistPdf);
      instance.SetDestructor(&destruct_VerticalInterpHistPdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::VerticalInterpHistPdf*)
   {
      return GenerateInitInstanceLocal((::VerticalInterpHistPdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::VerticalInterpHistPdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void delete_FastVerticalInterpHistPdfBase(void *p);
   static void deleteArray_FastVerticalInterpHistPdfBase(void *p);
   static void destruct_FastVerticalInterpHistPdfBase(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::FastVerticalInterpHistPdfBase*)
   {
      ::FastVerticalInterpHistPdfBase *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::FastVerticalInterpHistPdfBase >(0);
      static ::ROOT::TGenericClassInfo 
         instance("FastVerticalInterpHistPdfBase", ::FastVerticalInterpHistPdfBase::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/VerticalInterpHistPdf.h", 70,
                  typeid(::FastVerticalInterpHistPdfBase), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::FastVerticalInterpHistPdfBase::Dictionary, isa_proxy, 4,
                  sizeof(::FastVerticalInterpHistPdfBase) );
      instance.SetDelete(&delete_FastVerticalInterpHistPdfBase);
      instance.SetDeleteArray(&deleteArray_FastVerticalInterpHistPdfBase);
      instance.SetDestructor(&destruct_FastVerticalInterpHistPdfBase);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::FastVerticalInterpHistPdfBase*)
   {
      return GenerateInitInstanceLocal((::FastVerticalInterpHistPdfBase*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::FastVerticalInterpHistPdfBase*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static TClass *FastVerticalInterpHistPdfBasecLcLMorph_Dictionary();
   static void FastVerticalInterpHistPdfBasecLcLMorph_TClassManip(TClass*);
   static void *new_FastVerticalInterpHistPdfBasecLcLMorph(void *p = 0);
   static void *newArray_FastVerticalInterpHistPdfBasecLcLMorph(Long_t size, void *p);
   static void delete_FastVerticalInterpHistPdfBasecLcLMorph(void *p);
   static void deleteArray_FastVerticalInterpHistPdfBasecLcLMorph(void *p);
   static void destruct_FastVerticalInterpHistPdfBasecLcLMorph(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::FastVerticalInterpHistPdfBase::Morph*)
   {
      ::FastVerticalInterpHistPdfBase::Morph *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::FastVerticalInterpHistPdfBase::Morph));
      static ::ROOT::TGenericClassInfo 
         instance("FastVerticalInterpHistPdfBase::Morph", "HiggsAnalysis/CombinedLimit/interface/VerticalInterpHistPdf.h", 87,
                  typeid(::FastVerticalInterpHistPdfBase::Morph), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &FastVerticalInterpHistPdfBasecLcLMorph_Dictionary, isa_proxy, 4,
                  sizeof(::FastVerticalInterpHistPdfBase::Morph) );
      instance.SetNew(&new_FastVerticalInterpHistPdfBasecLcLMorph);
      instance.SetNewArray(&newArray_FastVerticalInterpHistPdfBasecLcLMorph);
      instance.SetDelete(&delete_FastVerticalInterpHistPdfBasecLcLMorph);
      instance.SetDeleteArray(&deleteArray_FastVerticalInterpHistPdfBasecLcLMorph);
      instance.SetDestructor(&destruct_FastVerticalInterpHistPdfBasecLcLMorph);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::FastVerticalInterpHistPdfBase::Morph*)
   {
      return GenerateInitInstanceLocal((::FastVerticalInterpHistPdfBase::Morph*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::FastVerticalInterpHistPdfBase::Morph*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *FastVerticalInterpHistPdfBasecLcLMorph_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::FastVerticalInterpHistPdfBase::Morph*)0x0)->GetClass();
      FastVerticalInterpHistPdfBasecLcLMorph_TClassManip(theClass);
   return theClass;
   }

   static void FastVerticalInterpHistPdfBasecLcLMorph_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static void *new_FastVerticalInterpHistPdf(void *p = 0);
   static void *newArray_FastVerticalInterpHistPdf(Long_t size, void *p);
   static void delete_FastVerticalInterpHistPdf(void *p);
   static void deleteArray_FastVerticalInterpHistPdf(void *p);
   static void destruct_FastVerticalInterpHistPdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::FastVerticalInterpHistPdf*)
   {
      ::FastVerticalInterpHistPdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::FastVerticalInterpHistPdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("FastVerticalInterpHistPdf", ::FastVerticalInterpHistPdf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/VerticalInterpHistPdf.h", 128,
                  typeid(::FastVerticalInterpHistPdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::FastVerticalInterpHistPdf::Dictionary, isa_proxy, 4,
                  sizeof(::FastVerticalInterpHistPdf) );
      instance.SetNew(&new_FastVerticalInterpHistPdf);
      instance.SetNewArray(&newArray_FastVerticalInterpHistPdf);
      instance.SetDelete(&delete_FastVerticalInterpHistPdf);
      instance.SetDeleteArray(&deleteArray_FastVerticalInterpHistPdf);
      instance.SetDestructor(&destruct_FastVerticalInterpHistPdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::FastVerticalInterpHistPdf*)
   {
      return GenerateInitInstanceLocal((::FastVerticalInterpHistPdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::FastVerticalInterpHistPdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_FastVerticalInterpHistPdf2D(void *p = 0);
   static void *newArray_FastVerticalInterpHistPdf2D(Long_t size, void *p);
   static void delete_FastVerticalInterpHistPdf2D(void *p);
   static void deleteArray_FastVerticalInterpHistPdf2D(void *p);
   static void destruct_FastVerticalInterpHistPdf2D(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::FastVerticalInterpHistPdf2D*)
   {
      ::FastVerticalInterpHistPdf2D *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::FastVerticalInterpHistPdf2D >(0);
      static ::ROOT::TGenericClassInfo 
         instance("FastVerticalInterpHistPdf2D", ::FastVerticalInterpHistPdf2D::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/VerticalInterpHistPdf.h", 183,
                  typeid(::FastVerticalInterpHistPdf2D), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::FastVerticalInterpHistPdf2D::Dictionary, isa_proxy, 4,
                  sizeof(::FastVerticalInterpHistPdf2D) );
      instance.SetNew(&new_FastVerticalInterpHistPdf2D);
      instance.SetNewArray(&newArray_FastVerticalInterpHistPdf2D);
      instance.SetDelete(&delete_FastVerticalInterpHistPdf2D);
      instance.SetDeleteArray(&deleteArray_FastVerticalInterpHistPdf2D);
      instance.SetDestructor(&destruct_FastVerticalInterpHistPdf2D);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::FastVerticalInterpHistPdf2D*)
   {
      return GenerateInitInstanceLocal((::FastVerticalInterpHistPdf2D*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::FastVerticalInterpHistPdf2D*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void delete_FastVerticalInterpHistPdf2Base(void *p);
   static void deleteArray_FastVerticalInterpHistPdf2Base(void *p);
   static void destruct_FastVerticalInterpHistPdf2Base(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::FastVerticalInterpHistPdf2Base*)
   {
      ::FastVerticalInterpHistPdf2Base *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::FastVerticalInterpHistPdf2Base >(0);
      static ::ROOT::TGenericClassInfo 
         instance("FastVerticalInterpHistPdf2Base", ::FastVerticalInterpHistPdf2Base::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/VerticalInterpHistPdf.h", 233,
                  typeid(::FastVerticalInterpHistPdf2Base), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::FastVerticalInterpHistPdf2Base::Dictionary, isa_proxy, 4,
                  sizeof(::FastVerticalInterpHistPdf2Base) );
      instance.SetDelete(&delete_FastVerticalInterpHistPdf2Base);
      instance.SetDeleteArray(&deleteArray_FastVerticalInterpHistPdf2Base);
      instance.SetDestructor(&destruct_FastVerticalInterpHistPdf2Base);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::FastVerticalInterpHistPdf2Base*)
   {
      return GenerateInitInstanceLocal((::FastVerticalInterpHistPdf2Base*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::FastVerticalInterpHistPdf2Base*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_FastVerticalInterpHistPdf2(void *p = 0);
   static void *newArray_FastVerticalInterpHistPdf2(Long_t size, void *p);
   static void delete_FastVerticalInterpHistPdf2(void *p);
   static void deleteArray_FastVerticalInterpHistPdf2(void *p);
   static void destruct_FastVerticalInterpHistPdf2(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::FastVerticalInterpHistPdf2*)
   {
      ::FastVerticalInterpHistPdf2 *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::FastVerticalInterpHistPdf2 >(0);
      static ::ROOT::TGenericClassInfo 
         instance("FastVerticalInterpHistPdf2", ::FastVerticalInterpHistPdf2::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/VerticalInterpHistPdf.h", 297,
                  typeid(::FastVerticalInterpHistPdf2), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::FastVerticalInterpHistPdf2::Dictionary, isa_proxy, 4,
                  sizeof(::FastVerticalInterpHistPdf2) );
      instance.SetNew(&new_FastVerticalInterpHistPdf2);
      instance.SetNewArray(&newArray_FastVerticalInterpHistPdf2);
      instance.SetDelete(&delete_FastVerticalInterpHistPdf2);
      instance.SetDeleteArray(&deleteArray_FastVerticalInterpHistPdf2);
      instance.SetDestructor(&destruct_FastVerticalInterpHistPdf2);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::FastVerticalInterpHistPdf2*)
   {
      return GenerateInitInstanceLocal((::FastVerticalInterpHistPdf2*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::FastVerticalInterpHistPdf2*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_FastVerticalInterpHistPdf2D2(void *p = 0);
   static void *newArray_FastVerticalInterpHistPdf2D2(Long_t size, void *p);
   static void delete_FastVerticalInterpHistPdf2D2(void *p);
   static void deleteArray_FastVerticalInterpHistPdf2D2(void *p);
   static void destruct_FastVerticalInterpHistPdf2D2(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::FastVerticalInterpHistPdf2D2*)
   {
      ::FastVerticalInterpHistPdf2D2 *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::FastVerticalInterpHistPdf2D2 >(0);
      static ::ROOT::TGenericClassInfo 
         instance("FastVerticalInterpHistPdf2D2", ::FastVerticalInterpHistPdf2D2::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/VerticalInterpHistPdf.h", 351,
                  typeid(::FastVerticalInterpHistPdf2D2), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::FastVerticalInterpHistPdf2D2::Dictionary, isa_proxy, 4,
                  sizeof(::FastVerticalInterpHistPdf2D2) );
      instance.SetNew(&new_FastVerticalInterpHistPdf2D2);
      instance.SetNewArray(&newArray_FastVerticalInterpHistPdf2D2);
      instance.SetDelete(&delete_FastVerticalInterpHistPdf2D2);
      instance.SetDeleteArray(&deleteArray_FastVerticalInterpHistPdf2D2);
      instance.SetDestructor(&destruct_FastVerticalInterpHistPdf2D2);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::FastVerticalInterpHistPdf2D2*)
   {
      return GenerateInitInstanceLocal((::FastVerticalInterpHistPdf2D2*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::FastVerticalInterpHistPdf2D2*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_FastVerticalInterpHistPdf3D(void *p = 0);
   static void *newArray_FastVerticalInterpHistPdf3D(Long_t size, void *p);
   static void delete_FastVerticalInterpHistPdf3D(void *p);
   static void deleteArray_FastVerticalInterpHistPdf3D(void *p);
   static void destruct_FastVerticalInterpHistPdf3D(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::FastVerticalInterpHistPdf3D*)
   {
      ::FastVerticalInterpHistPdf3D *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::FastVerticalInterpHistPdf3D >(0);
      static ::ROOT::TGenericClassInfo 
         instance("FastVerticalInterpHistPdf3D", ::FastVerticalInterpHistPdf3D::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/VerticalInterpHistPdf.h", 393,
                  typeid(::FastVerticalInterpHistPdf3D), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::FastVerticalInterpHistPdf3D::Dictionary, isa_proxy, 4,
                  sizeof(::FastVerticalInterpHistPdf3D) );
      instance.SetNew(&new_FastVerticalInterpHistPdf3D);
      instance.SetNewArray(&newArray_FastVerticalInterpHistPdf3D);
      instance.SetDelete(&delete_FastVerticalInterpHistPdf3D);
      instance.SetDeleteArray(&deleteArray_FastVerticalInterpHistPdf3D);
      instance.SetDestructor(&destruct_FastVerticalInterpHistPdf3D);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::FastVerticalInterpHistPdf3D*)
   {
      return GenerateInitInstanceLocal((::FastVerticalInterpHistPdf3D*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::FastVerticalInterpHistPdf3D*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_AsymPow(void *p = 0);
   static void *newArray_AsymPow(Long_t size, void *p);
   static void delete_AsymPow(void *p);
   static void deleteArray_AsymPow(void *p);
   static void destruct_AsymPow(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::AsymPow*)
   {
      ::AsymPow *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::AsymPow >(0);
      static ::ROOT::TGenericClassInfo 
         instance("AsymPow", ::AsymPow::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/AsymPow.h", 22,
                  typeid(::AsymPow), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::AsymPow::Dictionary, isa_proxy, 4,
                  sizeof(::AsymPow) );
      instance.SetNew(&new_AsymPow);
      instance.SetNewArray(&newArray_AsymPow);
      instance.SetDelete(&delete_AsymPow);
      instance.SetDeleteArray(&deleteArray_AsymPow);
      instance.SetDestructor(&destruct_AsymPow);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::AsymPow*)
   {
      return GenerateInitInstanceLocal((::AsymPow*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::AsymPow*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_AsymQuad(void *p = 0);
   static void *newArray_AsymQuad(Long_t size, void *p);
   static void delete_AsymQuad(void *p);
   static void deleteArray_AsymQuad(void *p);
   static void destruct_AsymQuad(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::AsymQuad*)
   {
      ::AsymQuad *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::AsymQuad >(0);
      static ::ROOT::TGenericClassInfo 
         instance("AsymQuad", ::AsymQuad::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/AsymQuad.h", 24,
                  typeid(::AsymQuad), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::AsymQuad::Dictionary, isa_proxy, 4,
                  sizeof(::AsymQuad) );
      instance.SetNew(&new_AsymQuad);
      instance.SetNewArray(&newArray_AsymQuad);
      instance.SetDelete(&delete_AsymQuad);
      instance.SetDeleteArray(&deleteArray_AsymQuad);
      instance.SetDestructor(&destruct_AsymQuad);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::AsymQuad*)
   {
      return GenerateInitInstanceLocal((::AsymQuad*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::AsymQuad*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_CombDataSetFactory(void *p = 0);
   static void *newArray_CombDataSetFactory(Long_t size, void *p);
   static void delete_CombDataSetFactory(void *p);
   static void deleteArray_CombDataSetFactory(void *p);
   static void destruct_CombDataSetFactory(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::CombDataSetFactory*)
   {
      ::CombDataSetFactory *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::CombDataSetFactory >(0);
      static ::ROOT::TGenericClassInfo 
         instance("CombDataSetFactory", ::CombDataSetFactory::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/CombDataSetFactory.h", 20,
                  typeid(::CombDataSetFactory), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::CombDataSetFactory::Dictionary, isa_proxy, 4,
                  sizeof(::CombDataSetFactory) );
      instance.SetNew(&new_CombDataSetFactory);
      instance.SetNewArray(&newArray_CombDataSetFactory);
      instance.SetDelete(&delete_CombDataSetFactory);
      instance.SetDeleteArray(&deleteArray_CombDataSetFactory);
      instance.SetDestructor(&destruct_CombDataSetFactory);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::CombDataSetFactory*)
   {
      return GenerateInitInstanceLocal((::CombDataSetFactory*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::CombDataSetFactory*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_TH1Keys(void *p = 0);
   static void *newArray_TH1Keys(Long_t size, void *p);
   static void delete_TH1Keys(void *p);
   static void deleteArray_TH1Keys(void *p);
   static void destruct_TH1Keys(void *p);
   static void directoryAutoAdd_TH1Keys(void *obj, TDirectory *dir);
   static Long64_t merge_TH1Keys(void *obj, TCollection *coll,TFileMergeInfo *info);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::TH1Keys*)
   {
      ::TH1Keys *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::TH1Keys >(0);
      static ::ROOT::TGenericClassInfo 
         instance("TH1Keys", ::TH1Keys::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/TH1Keys.h", 10,
                  typeid(::TH1Keys), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::TH1Keys::Dictionary, isa_proxy, 4,
                  sizeof(::TH1Keys) );
      instance.SetNew(&new_TH1Keys);
      instance.SetNewArray(&newArray_TH1Keys);
      instance.SetDelete(&delete_TH1Keys);
      instance.SetDeleteArray(&deleteArray_TH1Keys);
      instance.SetDestructor(&destruct_TH1Keys);
      instance.SetDirectoryAutoAdd(&directoryAutoAdd_TH1Keys);
      instance.SetMerge(&merge_TH1Keys);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::TH1Keys*)
   {
      return GenerateInitInstanceLocal((::TH1Keys*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::TH1Keys*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooSimultaneousOpt(void *p = 0);
   static void *newArray_RooSimultaneousOpt(Long_t size, void *p);
   static void delete_RooSimultaneousOpt(void *p);
   static void deleteArray_RooSimultaneousOpt(void *p);
   static void destruct_RooSimultaneousOpt(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooSimultaneousOpt*)
   {
      ::RooSimultaneousOpt *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooSimultaneousOpt >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooSimultaneousOpt", ::RooSimultaneousOpt::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/RooSimultaneousOpt.h", 9,
                  typeid(::RooSimultaneousOpt), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooSimultaneousOpt::Dictionary, isa_proxy, 4,
                  sizeof(::RooSimultaneousOpt) );
      instance.SetNew(&new_RooSimultaneousOpt);
      instance.SetNewArray(&newArray_RooSimultaneousOpt);
      instance.SetDelete(&delete_RooSimultaneousOpt);
      instance.SetDeleteArray(&deleteArray_RooSimultaneousOpt);
      instance.SetDestructor(&destruct_RooSimultaneousOpt);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooSimultaneousOpt*)
   {
      return GenerateInitInstanceLocal((::RooSimultaneousOpt*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooSimultaneousOpt*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_HZZ4L_RooCTauPdf_1D(void *p = 0);
   static void *newArray_HZZ4L_RooCTauPdf_1D(Long_t size, void *p);
   static void delete_HZZ4L_RooCTauPdf_1D(void *p);
   static void deleteArray_HZZ4L_RooCTauPdf_1D(void *p);
   static void destruct_HZZ4L_RooCTauPdf_1D(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::HZZ4L_RooCTauPdf_1D*)
   {
      ::HZZ4L_RooCTauPdf_1D *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::HZZ4L_RooCTauPdf_1D >(0);
      static ::ROOT::TGenericClassInfo 
         instance("HZZ4L_RooCTauPdf_1D", ::HZZ4L_RooCTauPdf_1D::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4L_RooCTauPdf_1D.h", 22,
                  typeid(::HZZ4L_RooCTauPdf_1D), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::HZZ4L_RooCTauPdf_1D::Dictionary, isa_proxy, 4,
                  sizeof(::HZZ4L_RooCTauPdf_1D) );
      instance.SetNew(&new_HZZ4L_RooCTauPdf_1D);
      instance.SetNewArray(&newArray_HZZ4L_RooCTauPdf_1D);
      instance.SetDelete(&delete_HZZ4L_RooCTauPdf_1D);
      instance.SetDeleteArray(&deleteArray_HZZ4L_RooCTauPdf_1D);
      instance.SetDestructor(&destruct_HZZ4L_RooCTauPdf_1D);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::HZZ4L_RooCTauPdf_1D*)
   {
      return GenerateInitInstanceLocal((::HZZ4L_RooCTauPdf_1D*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::HZZ4L_RooCTauPdf_1D*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_HZZ4L_RooCTauPdf_1D_Expanded(void *p = 0);
   static void *newArray_HZZ4L_RooCTauPdf_1D_Expanded(Long_t size, void *p);
   static void delete_HZZ4L_RooCTauPdf_1D_Expanded(void *p);
   static void deleteArray_HZZ4L_RooCTauPdf_1D_Expanded(void *p);
   static void destruct_HZZ4L_RooCTauPdf_1D_Expanded(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::HZZ4L_RooCTauPdf_1D_Expanded*)
   {
      ::HZZ4L_RooCTauPdf_1D_Expanded *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::HZZ4L_RooCTauPdf_1D_Expanded >(0);
      static ::ROOT::TGenericClassInfo 
         instance("HZZ4L_RooCTauPdf_1D_Expanded", ::HZZ4L_RooCTauPdf_1D_Expanded::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4L_RooCTauPdf_1D_Expanded.h", 22,
                  typeid(::HZZ4L_RooCTauPdf_1D_Expanded), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::HZZ4L_RooCTauPdf_1D_Expanded::Dictionary, isa_proxy, 4,
                  sizeof(::HZZ4L_RooCTauPdf_1D_Expanded) );
      instance.SetNew(&new_HZZ4L_RooCTauPdf_1D_Expanded);
      instance.SetNewArray(&newArray_HZZ4L_RooCTauPdf_1D_Expanded);
      instance.SetDelete(&delete_HZZ4L_RooCTauPdf_1D_Expanded);
      instance.SetDeleteArray(&deleteArray_HZZ4L_RooCTauPdf_1D_Expanded);
      instance.SetDestructor(&destruct_HZZ4L_RooCTauPdf_1D_Expanded);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::HZZ4L_RooCTauPdf_1D_Expanded*)
   {
      return GenerateInitInstanceLocal((::HZZ4L_RooCTauPdf_1D_Expanded*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::HZZ4L_RooCTauPdf_1D_Expanded*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_HZZ4L_RooCTauPdf_2D(void *p = 0);
   static void *newArray_HZZ4L_RooCTauPdf_2D(Long_t size, void *p);
   static void delete_HZZ4L_RooCTauPdf_2D(void *p);
   static void deleteArray_HZZ4L_RooCTauPdf_2D(void *p);
   static void destruct_HZZ4L_RooCTauPdf_2D(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::HZZ4L_RooCTauPdf_2D*)
   {
      ::HZZ4L_RooCTauPdf_2D *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::HZZ4L_RooCTauPdf_2D >(0);
      static ::ROOT::TGenericClassInfo 
         instance("HZZ4L_RooCTauPdf_2D", ::HZZ4L_RooCTauPdf_2D::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4L_RooCTauPdf_2D.h", 22,
                  typeid(::HZZ4L_RooCTauPdf_2D), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::HZZ4L_RooCTauPdf_2D::Dictionary, isa_proxy, 4,
                  sizeof(::HZZ4L_RooCTauPdf_2D) );
      instance.SetNew(&new_HZZ4L_RooCTauPdf_2D);
      instance.SetNewArray(&newArray_HZZ4L_RooCTauPdf_2D);
      instance.SetDelete(&delete_HZZ4L_RooCTauPdf_2D);
      instance.SetDeleteArray(&deleteArray_HZZ4L_RooCTauPdf_2D);
      instance.SetDestructor(&destruct_HZZ4L_RooCTauPdf_2D);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::HZZ4L_RooCTauPdf_2D*)
   {
      return GenerateInitInstanceLocal((::HZZ4L_RooCTauPdf_2D*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::HZZ4L_RooCTauPdf_2D*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooqqZZPdf(void *p = 0);
   static void *newArray_RooqqZZPdf(Long_t size, void *p);
   static void delete_RooqqZZPdf(void *p);
   static void deleteArray_RooqqZZPdf(void *p);
   static void destruct_RooqqZZPdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooqqZZPdf*)
   {
      ::RooqqZZPdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooqqZZPdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooqqZZPdf", ::RooqqZZPdf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h", 42,
                  typeid(::RooqqZZPdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooqqZZPdf::Dictionary, isa_proxy, 4,
                  sizeof(::RooqqZZPdf) );
      instance.SetNew(&new_RooqqZZPdf);
      instance.SetNewArray(&newArray_RooqqZZPdf);
      instance.SetDelete(&delete_RooqqZZPdf);
      instance.SetDeleteArray(&deleteArray_RooqqZZPdf);
      instance.SetDestructor(&destruct_RooqqZZPdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooqqZZPdf*)
   {
      return GenerateInitInstanceLocal((::RooqqZZPdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooqqZZPdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooggZZPdf(void *p = 0);
   static void *newArray_RooggZZPdf(Long_t size, void *p);
   static void delete_RooggZZPdf(void *p);
   static void deleteArray_RooggZZPdf(void *p);
   static void destruct_RooggZZPdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooggZZPdf*)
   {
      ::RooggZZPdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooggZZPdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooggZZPdf", ::RooggZZPdf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h", 78,
                  typeid(::RooggZZPdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooggZZPdf::Dictionary, isa_proxy, 4,
                  sizeof(::RooggZZPdf) );
      instance.SetNew(&new_RooggZZPdf);
      instance.SetNewArray(&newArray_RooggZZPdf);
      instance.SetDelete(&delete_RooggZZPdf);
      instance.SetDeleteArray(&deleteArray_RooggZZPdf);
      instance.SetDestructor(&destruct_RooggZZPdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooggZZPdf*)
   {
      return GenerateInitInstanceLocal((::RooggZZPdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooggZZPdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooqqZZPdf_v2(void *p = 0);
   static void *newArray_RooqqZZPdf_v2(Long_t size, void *p);
   static void delete_RooqqZZPdf_v2(void *p);
   static void deleteArray_RooqqZZPdf_v2(void *p);
   static void destruct_RooqqZZPdf_v2(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooqqZZPdf_v2*)
   {
      ::RooqqZZPdf_v2 *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooqqZZPdf_v2 >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooqqZZPdf_v2", ::RooqqZZPdf_v2::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h", 115,
                  typeid(::RooqqZZPdf_v2), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooqqZZPdf_v2::Dictionary, isa_proxy, 4,
                  sizeof(::RooqqZZPdf_v2) );
      instance.SetNew(&new_RooqqZZPdf_v2);
      instance.SetNewArray(&newArray_RooqqZZPdf_v2);
      instance.SetDelete(&delete_RooqqZZPdf_v2);
      instance.SetDeleteArray(&deleteArray_RooqqZZPdf_v2);
      instance.SetDestructor(&destruct_RooqqZZPdf_v2);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooqqZZPdf_v2*)
   {
      return GenerateInitInstanceLocal((::RooqqZZPdf_v2*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooqqZZPdf_v2*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooVBFZZPdf(void *p = 0);
   static void *newArray_RooVBFZZPdf(Long_t size, void *p);
   static void delete_RooVBFZZPdf(void *p);
   static void deleteArray_RooVBFZZPdf(void *p);
   static void destruct_RooVBFZZPdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooVBFZZPdf*)
   {
      ::RooVBFZZPdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooVBFZZPdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooVBFZZPdf", ::RooVBFZZPdf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h", 170,
                  typeid(::RooVBFZZPdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooVBFZZPdf::Dictionary, isa_proxy, 4,
                  sizeof(::RooVBFZZPdf) );
      instance.SetNew(&new_RooVBFZZPdf);
      instance.SetNewArray(&newArray_RooVBFZZPdf);
      instance.SetDelete(&delete_RooVBFZZPdf);
      instance.SetDeleteArray(&deleteArray_RooVBFZZPdf);
      instance.SetDestructor(&destruct_RooVBFZZPdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooVBFZZPdf*)
   {
      return GenerateInitInstanceLocal((::RooVBFZZPdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooVBFZZPdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooVBFZZPdf_v2(void *p = 0);
   static void *newArray_RooVBFZZPdf_v2(Long_t size, void *p);
   static void delete_RooVBFZZPdf_v2(void *p);
   static void deleteArray_RooVBFZZPdf_v2(void *p);
   static void destruct_RooVBFZZPdf_v2(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooVBFZZPdf_v2*)
   {
      ::RooVBFZZPdf_v2 *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooVBFZZPdf_v2 >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooVBFZZPdf_v2", ::RooVBFZZPdf_v2::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h", 231,
                  typeid(::RooVBFZZPdf_v2), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooVBFZZPdf_v2::Dictionary, isa_proxy, 4,
                  sizeof(::RooVBFZZPdf_v2) );
      instance.SetNew(&new_RooVBFZZPdf_v2);
      instance.SetNewArray(&newArray_RooVBFZZPdf_v2);
      instance.SetDelete(&delete_RooVBFZZPdf_v2);
      instance.SetDeleteArray(&deleteArray_RooVBFZZPdf_v2);
      instance.SetDestructor(&destruct_RooVBFZZPdf_v2);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooVBFZZPdf_v2*)
   {
      return GenerateInitInstanceLocal((::RooVBFZZPdf_v2*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooVBFZZPdf_v2*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooggZZPdf_v2(void *p = 0);
   static void *newArray_RooggZZPdf_v2(Long_t size, void *p);
   static void delete_RooggZZPdf_v2(void *p);
   static void deleteArray_RooggZZPdf_v2(void *p);
   static void destruct_RooggZZPdf_v2(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooggZZPdf_v2*)
   {
      ::RooggZZPdf_v2 *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooggZZPdf_v2 >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooggZZPdf_v2", ::RooggZZPdf_v2::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h", 282,
                  typeid(::RooggZZPdf_v2), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooggZZPdf_v2::Dictionary, isa_proxy, 4,
                  sizeof(::RooggZZPdf_v2) );
      instance.SetNew(&new_RooggZZPdf_v2);
      instance.SetNewArray(&newArray_RooggZZPdf_v2);
      instance.SetDelete(&delete_RooggZZPdf_v2);
      instance.SetDeleteArray(&deleteArray_RooggZZPdf_v2);
      instance.SetDestructor(&destruct_RooggZZPdf_v2);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooggZZPdf_v2*)
   {
      return GenerateInitInstanceLocal((::RooggZZPdf_v2*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooggZZPdf_v2*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooBetaFunc_v2(void *p = 0);
   static void *newArray_RooBetaFunc_v2(Long_t size, void *p);
   static void delete_RooBetaFunc_v2(void *p);
   static void deleteArray_RooBetaFunc_v2(void *p);
   static void destruct_RooBetaFunc_v2(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooBetaFunc_v2*)
   {
      ::RooBetaFunc_v2 *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooBetaFunc_v2 >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooBetaFunc_v2", ::RooBetaFunc_v2::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h", 324,
                  typeid(::RooBetaFunc_v2), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooBetaFunc_v2::Dictionary, isa_proxy, 4,
                  sizeof(::RooBetaFunc_v2) );
      instance.SetNew(&new_RooBetaFunc_v2);
      instance.SetNewArray(&newArray_RooBetaFunc_v2);
      instance.SetDelete(&delete_RooBetaFunc_v2);
      instance.SetDeleteArray(&deleteArray_RooBetaFunc_v2);
      instance.SetDestructor(&destruct_RooBetaFunc_v2);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooBetaFunc_v2*)
   {
      return GenerateInitInstanceLocal((::RooBetaFunc_v2*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooBetaFunc_v2*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_Roo4lMasses2D_Bkg(void *p = 0);
   static void *newArray_Roo4lMasses2D_Bkg(Long_t size, void *p);
   static void delete_Roo4lMasses2D_Bkg(void *p);
   static void deleteArray_Roo4lMasses2D_Bkg(void *p);
   static void destruct_Roo4lMasses2D_Bkg(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::Roo4lMasses2D_Bkg*)
   {
      ::Roo4lMasses2D_Bkg *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::Roo4lMasses2D_Bkg >(0);
      static ::ROOT::TGenericClassInfo 
         instance("Roo4lMasses2D_Bkg", ::Roo4lMasses2D_Bkg::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h", 367,
                  typeid(::Roo4lMasses2D_Bkg), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::Roo4lMasses2D_Bkg::Dictionary, isa_proxy, 4,
                  sizeof(::Roo4lMasses2D_Bkg) );
      instance.SetNew(&new_Roo4lMasses2D_Bkg);
      instance.SetNewArray(&newArray_Roo4lMasses2D_Bkg);
      instance.SetDelete(&delete_Roo4lMasses2D_Bkg);
      instance.SetDeleteArray(&deleteArray_Roo4lMasses2D_Bkg);
      instance.SetDestructor(&destruct_Roo4lMasses2D_Bkg);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::Roo4lMasses2D_Bkg*)
   {
      return GenerateInitInstanceLocal((::Roo4lMasses2D_Bkg*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::Roo4lMasses2D_Bkg*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_Roo4lMasses2D_BkgGGZZ(void *p = 0);
   static void *newArray_Roo4lMasses2D_BkgGGZZ(Long_t size, void *p);
   static void delete_Roo4lMasses2D_BkgGGZZ(void *p);
   static void deleteArray_Roo4lMasses2D_BkgGGZZ(void *p);
   static void destruct_Roo4lMasses2D_BkgGGZZ(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::Roo4lMasses2D_BkgGGZZ*)
   {
      ::Roo4lMasses2D_BkgGGZZ *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::Roo4lMasses2D_BkgGGZZ >(0);
      static ::ROOT::TGenericClassInfo 
         instance("Roo4lMasses2D_BkgGGZZ", ::Roo4lMasses2D_BkgGGZZ::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h", 394,
                  typeid(::Roo4lMasses2D_BkgGGZZ), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::Roo4lMasses2D_BkgGGZZ::Dictionary, isa_proxy, 4,
                  sizeof(::Roo4lMasses2D_BkgGGZZ) );
      instance.SetNew(&new_Roo4lMasses2D_BkgGGZZ);
      instance.SetNewArray(&newArray_Roo4lMasses2D_BkgGGZZ);
      instance.SetDelete(&delete_Roo4lMasses2D_BkgGGZZ);
      instance.SetDeleteArray(&deleteArray_Roo4lMasses2D_BkgGGZZ);
      instance.SetDestructor(&destruct_Roo4lMasses2D_BkgGGZZ);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::Roo4lMasses2D_BkgGGZZ*)
   {
      return GenerateInitInstanceLocal((::Roo4lMasses2D_BkgGGZZ*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::Roo4lMasses2D_BkgGGZZ*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_Roo4lMasses2D(void *p = 0);
   static void *newArray_Roo4lMasses2D(Long_t size, void *p);
   static void delete_Roo4lMasses2D(void *p);
   static void deleteArray_Roo4lMasses2D(void *p);
   static void destruct_Roo4lMasses2D(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::Roo4lMasses2D*)
   {
      ::Roo4lMasses2D *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::Roo4lMasses2D >(0);
      static ::ROOT::TGenericClassInfo 
         instance("Roo4lMasses2D", ::Roo4lMasses2D::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h", 427,
                  typeid(::Roo4lMasses2D), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::Roo4lMasses2D::Dictionary, isa_proxy, 4,
                  sizeof(::Roo4lMasses2D) );
      instance.SetNew(&new_Roo4lMasses2D);
      instance.SetNewArray(&newArray_Roo4lMasses2D);
      instance.SetDelete(&delete_Roo4lMasses2D);
      instance.SetDeleteArray(&deleteArray_Roo4lMasses2D);
      instance.SetDestructor(&destruct_Roo4lMasses2D);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::Roo4lMasses2D*)
   {
      return GenerateInitInstanceLocal((::Roo4lMasses2D*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::Roo4lMasses2D*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooFourMuMassShapePdf2(void *p = 0);
   static void *newArray_RooFourMuMassShapePdf2(Long_t size, void *p);
   static void delete_RooFourMuMassShapePdf2(void *p);
   static void deleteArray_RooFourMuMassShapePdf2(void *p);
   static void destruct_RooFourMuMassShapePdf2(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooFourMuMassShapePdf2*)
   {
      ::RooFourMuMassShapePdf2 *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooFourMuMassShapePdf2 >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooFourMuMassShapePdf2", ::RooFourMuMassShapePdf2::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h", 470,
                  typeid(::RooFourMuMassShapePdf2), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooFourMuMassShapePdf2::Dictionary, isa_proxy, 4,
                  sizeof(::RooFourMuMassShapePdf2) );
      instance.SetNew(&new_RooFourMuMassShapePdf2);
      instance.SetNewArray(&newArray_RooFourMuMassShapePdf2);
      instance.SetDelete(&delete_RooFourMuMassShapePdf2);
      instance.SetDeleteArray(&deleteArray_RooFourMuMassShapePdf2);
      instance.SetDestructor(&destruct_RooFourMuMassShapePdf2);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooFourMuMassShapePdf2*)
   {
      return GenerateInitInstanceLocal((::RooFourMuMassShapePdf2*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooFourMuMassShapePdf2*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooFourEMassShapePdf2(void *p = 0);
   static void *newArray_RooFourEMassShapePdf2(Long_t size, void *p);
   static void delete_RooFourEMassShapePdf2(void *p);
   static void deleteArray_RooFourEMassShapePdf2(void *p);
   static void destruct_RooFourEMassShapePdf2(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooFourEMassShapePdf2*)
   {
      ::RooFourEMassShapePdf2 *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooFourEMassShapePdf2 >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooFourEMassShapePdf2", ::RooFourEMassShapePdf2::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h", 494,
                  typeid(::RooFourEMassShapePdf2), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooFourEMassShapePdf2::Dictionary, isa_proxy, 4,
                  sizeof(::RooFourEMassShapePdf2) );
      instance.SetNew(&new_RooFourEMassShapePdf2);
      instance.SetNewArray(&newArray_RooFourEMassShapePdf2);
      instance.SetDelete(&delete_RooFourEMassShapePdf2);
      instance.SetDeleteArray(&deleteArray_RooFourEMassShapePdf2);
      instance.SetDestructor(&destruct_RooFourEMassShapePdf2);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooFourEMassShapePdf2*)
   {
      return GenerateInitInstanceLocal((::RooFourEMassShapePdf2*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooFourEMassShapePdf2*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooTwoETwoMuMassShapePdf2(void *p = 0);
   static void *newArray_RooTwoETwoMuMassShapePdf2(Long_t size, void *p);
   static void delete_RooTwoETwoMuMassShapePdf2(void *p);
   static void deleteArray_RooTwoETwoMuMassShapePdf2(void *p);
   static void destruct_RooTwoETwoMuMassShapePdf2(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooTwoETwoMuMassShapePdf2*)
   {
      ::RooTwoETwoMuMassShapePdf2 *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooTwoETwoMuMassShapePdf2 >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooTwoETwoMuMassShapePdf2", ::RooTwoETwoMuMassShapePdf2::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h", 519,
                  typeid(::RooTwoETwoMuMassShapePdf2), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooTwoETwoMuMassShapePdf2::Dictionary, isa_proxy, 4,
                  sizeof(::RooTwoETwoMuMassShapePdf2) );
      instance.SetNew(&new_RooTwoETwoMuMassShapePdf2);
      instance.SetNewArray(&newArray_RooTwoETwoMuMassShapePdf2);
      instance.SetDelete(&delete_RooTwoETwoMuMassShapePdf2);
      instance.SetDeleteArray(&deleteArray_RooTwoETwoMuMassShapePdf2);
      instance.SetDestructor(&destruct_RooTwoETwoMuMassShapePdf2);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooTwoETwoMuMassShapePdf2*)
   {
      return GenerateInitInstanceLocal((::RooTwoETwoMuMassShapePdf2*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooTwoETwoMuMassShapePdf2*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooFourMuMassRes(void *p = 0);
   static void *newArray_RooFourMuMassRes(Long_t size, void *p);
   static void delete_RooFourMuMassRes(void *p);
   static void deleteArray_RooFourMuMassRes(void *p);
   static void destruct_RooFourMuMassRes(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooFourMuMassRes*)
   {
      ::RooFourMuMassRes *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooFourMuMassRes >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooFourMuMassRes", ::RooFourMuMassRes::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h", 543,
                  typeid(::RooFourMuMassRes), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooFourMuMassRes::Dictionary, isa_proxy, 4,
                  sizeof(::RooFourMuMassRes) );
      instance.SetNew(&new_RooFourMuMassRes);
      instance.SetNewArray(&newArray_RooFourMuMassRes);
      instance.SetDelete(&delete_RooFourMuMassRes);
      instance.SetDeleteArray(&deleteArray_RooFourMuMassRes);
      instance.SetDestructor(&destruct_RooFourMuMassRes);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooFourMuMassRes*)
   {
      return GenerateInitInstanceLocal((::RooFourMuMassRes*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooFourMuMassRes*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooFourEMassRes(void *p = 0);
   static void *newArray_RooFourEMassRes(Long_t size, void *p);
   static void delete_RooFourEMassRes(void *p);
   static void deleteArray_RooFourEMassRes(void *p);
   static void destruct_RooFourEMassRes(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooFourEMassRes*)
   {
      ::RooFourEMassRes *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooFourEMassRes >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooFourEMassRes", ::RooFourEMassRes::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h", 565,
                  typeid(::RooFourEMassRes), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooFourEMassRes::Dictionary, isa_proxy, 4,
                  sizeof(::RooFourEMassRes) );
      instance.SetNew(&new_RooFourEMassRes);
      instance.SetNewArray(&newArray_RooFourEMassRes);
      instance.SetDelete(&delete_RooFourEMassRes);
      instance.SetDeleteArray(&deleteArray_RooFourEMassRes);
      instance.SetDestructor(&destruct_RooFourEMassRes);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooFourEMassRes*)
   {
      return GenerateInitInstanceLocal((::RooFourEMassRes*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooFourEMassRes*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooTwoETwoMuMassRes(void *p = 0);
   static void *newArray_RooTwoETwoMuMassRes(Long_t size, void *p);
   static void delete_RooTwoETwoMuMassRes(void *p);
   static void deleteArray_RooTwoETwoMuMassRes(void *p);
   static void destruct_RooTwoETwoMuMassRes(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooTwoETwoMuMassRes*)
   {
      ::RooTwoETwoMuMassRes *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooTwoETwoMuMassRes >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooTwoETwoMuMassRes", ::RooTwoETwoMuMassRes::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h", 588,
                  typeid(::RooTwoETwoMuMassRes), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooTwoETwoMuMassRes::Dictionary, isa_proxy, 4,
                  sizeof(::RooTwoETwoMuMassRes) );
      instance.SetNew(&new_RooTwoETwoMuMassRes);
      instance.SetNewArray(&newArray_RooTwoETwoMuMassRes);
      instance.SetDelete(&delete_RooTwoETwoMuMassRes);
      instance.SetDeleteArray(&deleteArray_RooTwoETwoMuMassRes);
      instance.SetDestructor(&destruct_RooTwoETwoMuMassRes);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooTwoETwoMuMassRes*)
   {
      return GenerateInitInstanceLocal((::RooTwoETwoMuMassRes*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooTwoETwoMuMassRes*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooRelBW1(void *p = 0);
   static void *newArray_RooRelBW1(Long_t size, void *p);
   static void delete_RooRelBW1(void *p);
   static void deleteArray_RooRelBW1(void *p);
   static void destruct_RooRelBW1(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooRelBW1*)
   {
      ::RooRelBW1 *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooRelBW1 >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooRelBW1", ::RooRelBW1::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h", 611,
                  typeid(::RooRelBW1), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooRelBW1::Dictionary, isa_proxy, 4,
                  sizeof(::RooRelBW1) );
      instance.SetNew(&new_RooRelBW1);
      instance.SetNewArray(&newArray_RooRelBW1);
      instance.SetDelete(&delete_RooRelBW1);
      instance.SetDeleteArray(&deleteArray_RooRelBW1);
      instance.SetDestructor(&destruct_RooRelBW1);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooRelBW1*)
   {
      return GenerateInitInstanceLocal((::RooRelBW1*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooRelBW1*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooRelBWUF(void *p = 0);
   static void *newArray_RooRelBWUF(Long_t size, void *p);
   static void delete_RooRelBWUF(void *p);
   static void deleteArray_RooRelBWUF(void *p);
   static void destruct_RooRelBWUF(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooRelBWUF*)
   {
      ::RooRelBWUF *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooRelBWUF >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooRelBWUF", ::RooRelBWUF::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h", 637,
                  typeid(::RooRelBWUF), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooRelBWUF::Dictionary, isa_proxy, 4,
                  sizeof(::RooRelBWUF) );
      instance.SetNew(&new_RooRelBWUF);
      instance.SetNewArray(&newArray_RooRelBWUF);
      instance.SetDelete(&delete_RooRelBWUF);
      instance.SetDeleteArray(&deleteArray_RooRelBWUF);
      instance.SetDestructor(&destruct_RooRelBWUF);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooRelBWUF*)
   {
      return GenerateInitInstanceLocal((::RooRelBWUF*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooRelBWUF*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooRelBWUF_SM4(void *p = 0);
   static void *newArray_RooRelBWUF_SM4(Long_t size, void *p);
   static void delete_RooRelBWUF_SM4(void *p);
   static void deleteArray_RooRelBWUF_SM4(void *p);
   static void destruct_RooRelBWUF_SM4(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooRelBWUF_SM4*)
   {
      ::RooRelBWUF_SM4 *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooRelBWUF_SM4 >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooRelBWUF_SM4", ::RooRelBWUF_SM4::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h", 662,
                  typeid(::RooRelBWUF_SM4), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooRelBWUF_SM4::Dictionary, isa_proxy, 4,
                  sizeof(::RooRelBWUF_SM4) );
      instance.SetNew(&new_RooRelBWUF_SM4);
      instance.SetNewArray(&newArray_RooRelBWUF_SM4);
      instance.SetDelete(&delete_RooRelBWUF_SM4);
      instance.SetDeleteArray(&deleteArray_RooRelBWUF_SM4);
      instance.SetDestructor(&destruct_RooRelBWUF_SM4);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooRelBWUF_SM4*)
   {
      return GenerateInitInstanceLocal((::RooRelBWUF_SM4*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooRelBWUF_SM4*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooRelBWUFParamWidth(void *p = 0);
   static void *newArray_RooRelBWUFParamWidth(Long_t size, void *p);
   static void delete_RooRelBWUFParamWidth(void *p);
   static void deleteArray_RooRelBWUFParamWidth(void *p);
   static void destruct_RooRelBWUFParamWidth(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooRelBWUFParamWidth*)
   {
      ::RooRelBWUFParamWidth *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooRelBWUFParamWidth >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooRelBWUFParamWidth", ::RooRelBWUFParamWidth::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h", 687,
                  typeid(::RooRelBWUFParamWidth), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooRelBWUFParamWidth::Dictionary, isa_proxy, 4,
                  sizeof(::RooRelBWUFParamWidth) );
      instance.SetNew(&new_RooRelBWUFParamWidth);
      instance.SetNewArray(&newArray_RooRelBWUFParamWidth);
      instance.SetDelete(&delete_RooRelBWUFParamWidth);
      instance.SetDeleteArray(&deleteArray_RooRelBWUFParamWidth);
      instance.SetDestructor(&destruct_RooRelBWUFParamWidth);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooRelBWUFParamWidth*)
   {
      return GenerateInitInstanceLocal((::RooRelBWUFParamWidth*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooRelBWUFParamWidth*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooRelBWUFParam(void *p = 0);
   static void *newArray_RooRelBWUFParam(Long_t size, void *p);
   static void delete_RooRelBWUFParam(void *p);
   static void deleteArray_RooRelBWUFParam(void *p);
   static void destruct_RooRelBWUFParam(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooRelBWUFParam*)
   {
      ::RooRelBWUFParam *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooRelBWUFParam >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooRelBWUFParam", ::RooRelBWUFParam::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h", 712,
                  typeid(::RooRelBWUFParam), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooRelBWUFParam::Dictionary, isa_proxy, 4,
                  sizeof(::RooRelBWUFParam) );
      instance.SetNew(&new_RooRelBWUFParam);
      instance.SetNewArray(&newArray_RooRelBWUFParam);
      instance.SetDelete(&delete_RooRelBWUFParam);
      instance.SetDeleteArray(&deleteArray_RooRelBWUFParam);
      instance.SetDestructor(&destruct_RooRelBWUFParam);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooRelBWUFParam*)
   {
      return GenerateInitInstanceLocal((::RooRelBWUFParam*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooRelBWUFParam*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooRelBWHighMass(void *p = 0);
   static void *newArray_RooRelBWHighMass(Long_t size, void *p);
   static void delete_RooRelBWHighMass(void *p);
   static void deleteArray_RooRelBWHighMass(void *p);
   static void destruct_RooRelBWHighMass(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooRelBWHighMass*)
   {
      ::RooRelBWHighMass *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooRelBWHighMass >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooRelBWHighMass", ::RooRelBWHighMass::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h", 741,
                  typeid(::RooRelBWHighMass), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooRelBWHighMass::Dictionary, isa_proxy, 4,
                  sizeof(::RooRelBWHighMass) );
      instance.SetNew(&new_RooRelBWHighMass);
      instance.SetNewArray(&newArray_RooRelBWHighMass);
      instance.SetDelete(&delete_RooRelBWHighMass);
      instance.SetDeleteArray(&deleteArray_RooRelBWHighMass);
      instance.SetDestructor(&destruct_RooRelBWHighMass);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooRelBWHighMass*)
   {
      return GenerateInitInstanceLocal((::RooRelBWHighMass*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooRelBWHighMass*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooTsallis(void *p = 0);
   static void *newArray_RooTsallis(Long_t size, void *p);
   static void delete_RooTsallis(void *p);
   static void deleteArray_RooTsallis(void *p);
   static void destruct_RooTsallis(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooTsallis*)
   {
      ::RooTsallis *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooTsallis >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooTsallis", ::RooTsallis::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h", 767,
                  typeid(::RooTsallis), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooTsallis::Dictionary, isa_proxy, 4,
                  sizeof(::RooTsallis) );
      instance.SetNew(&new_RooTsallis);
      instance.SetNewArray(&newArray_RooTsallis);
      instance.SetDelete(&delete_RooTsallis);
      instance.SetDeleteArray(&deleteArray_RooTsallis);
      instance.SetDestructor(&destruct_RooTsallis);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooTsallis*)
   {
      return GenerateInitInstanceLocal((::RooTsallis*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooTsallis*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooaDoubleCBxBW(void *p = 0);
   static void *newArray_RooaDoubleCBxBW(Long_t size, void *p);
   static void delete_RooaDoubleCBxBW(void *p);
   static void deleteArray_RooaDoubleCBxBW(void *p);
   static void destruct_RooaDoubleCBxBW(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooaDoubleCBxBW*)
   {
      ::RooaDoubleCBxBW *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooaDoubleCBxBW >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooaDoubleCBxBW", ::RooaDoubleCBxBW::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h", 808,
                  typeid(::RooaDoubleCBxBW), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooaDoubleCBxBW::Dictionary, isa_proxy, 4,
                  sizeof(::RooaDoubleCBxBW) );
      instance.SetNew(&new_RooaDoubleCBxBW);
      instance.SetNewArray(&newArray_RooaDoubleCBxBW);
      instance.SetDelete(&delete_RooaDoubleCBxBW);
      instance.SetDeleteArray(&deleteArray_RooaDoubleCBxBW);
      instance.SetDestructor(&destruct_RooaDoubleCBxBW);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooaDoubleCBxBW*)
   {
      return GenerateInitInstanceLocal((::RooaDoubleCBxBW*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooaDoubleCBxBW*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooCPSHighMassGGH(void *p = 0);
   static void *newArray_RooCPSHighMassGGH(Long_t size, void *p);
   static void delete_RooCPSHighMassGGH(void *p);
   static void deleteArray_RooCPSHighMassGGH(void *p);
   static void destruct_RooCPSHighMassGGH(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooCPSHighMassGGH*)
   {
      ::RooCPSHighMassGGH *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooCPSHighMassGGH >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooCPSHighMassGGH", ::RooCPSHighMassGGH::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h", 858,
                  typeid(::RooCPSHighMassGGH), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooCPSHighMassGGH::Dictionary, isa_proxy, 4,
                  sizeof(::RooCPSHighMassGGH) );
      instance.SetNew(&new_RooCPSHighMassGGH);
      instance.SetNewArray(&newArray_RooCPSHighMassGGH);
      instance.SetDelete(&delete_RooCPSHighMassGGH);
      instance.SetDeleteArray(&deleteArray_RooCPSHighMassGGH);
      instance.SetDestructor(&destruct_RooCPSHighMassGGH);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooCPSHighMassGGH*)
   {
      return GenerateInitInstanceLocal((::RooCPSHighMassGGH*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooCPSHighMassGGH*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooBWHighMassGGH(void *p = 0);
   static void *newArray_RooBWHighMassGGH(Long_t size, void *p);
   static void delete_RooBWHighMassGGH(void *p);
   static void deleteArray_RooBWHighMassGGH(void *p);
   static void destruct_RooBWHighMassGGH(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooBWHighMassGGH*)
   {
      ::RooBWHighMassGGH *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooBWHighMassGGH >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooBWHighMassGGH", ::RooBWHighMassGGH::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h", 910,
                  typeid(::RooBWHighMassGGH), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooBWHighMassGGH::Dictionary, isa_proxy, 4,
                  sizeof(::RooBWHighMassGGH) );
      instance.SetNew(&new_RooBWHighMassGGH);
      instance.SetNewArray(&newArray_RooBWHighMassGGH);
      instance.SetDelete(&delete_RooBWHighMassGGH);
      instance.SetDeleteArray(&deleteArray_RooBWHighMassGGH);
      instance.SetDestructor(&destruct_RooBWHighMassGGH);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooBWHighMassGGH*)
   {
      return GenerateInitInstanceLocal((::RooBWHighMassGGH*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooBWHighMassGGH*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooCPSHighMassGGHNoInterf(void *p = 0);
   static void *newArray_RooCPSHighMassGGHNoInterf(Long_t size, void *p);
   static void delete_RooCPSHighMassGGHNoInterf(void *p);
   static void deleteArray_RooCPSHighMassGGHNoInterf(void *p);
   static void destruct_RooCPSHighMassGGHNoInterf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooCPSHighMassGGHNoInterf*)
   {
      ::RooCPSHighMassGGHNoInterf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooCPSHighMassGGHNoInterf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooCPSHighMassGGHNoInterf", ::RooCPSHighMassGGHNoInterf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h", 960,
                  typeid(::RooCPSHighMassGGHNoInterf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooCPSHighMassGGHNoInterf::Dictionary, isa_proxy, 4,
                  sizeof(::RooCPSHighMassGGHNoInterf) );
      instance.SetNew(&new_RooCPSHighMassGGHNoInterf);
      instance.SetNewArray(&newArray_RooCPSHighMassGGHNoInterf);
      instance.SetDelete(&delete_RooCPSHighMassGGHNoInterf);
      instance.SetDeleteArray(&deleteArray_RooCPSHighMassGGHNoInterf);
      instance.SetDestructor(&destruct_RooCPSHighMassGGHNoInterf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooCPSHighMassGGHNoInterf*)
   {
      return GenerateInitInstanceLocal((::RooCPSHighMassGGHNoInterf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooCPSHighMassGGHNoInterf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooCPSHighMassVBF(void *p = 0);
   static void *newArray_RooCPSHighMassVBF(Long_t size, void *p);
   static void delete_RooCPSHighMassVBF(void *p);
   static void deleteArray_RooCPSHighMassVBF(void *p);
   static void destruct_RooCPSHighMassVBF(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooCPSHighMassVBF*)
   {
      ::RooCPSHighMassVBF *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooCPSHighMassVBF >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooCPSHighMassVBF", ::RooCPSHighMassVBF::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h", 1003,
                  typeid(::RooCPSHighMassVBF), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooCPSHighMassVBF::Dictionary, isa_proxy, 4,
                  sizeof(::RooCPSHighMassVBF) );
      instance.SetNew(&new_RooCPSHighMassVBF);
      instance.SetNewArray(&newArray_RooCPSHighMassVBF);
      instance.SetDelete(&delete_RooCPSHighMassVBF);
      instance.SetDeleteArray(&deleteArray_RooCPSHighMassVBF);
      instance.SetDestructor(&destruct_RooCPSHighMassVBF);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooCPSHighMassVBF*)
   {
      return GenerateInitInstanceLocal((::RooCPSHighMassVBF*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooCPSHighMassVBF*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooCPSHighMassVBFNoInterf(void *p = 0);
   static void *newArray_RooCPSHighMassVBFNoInterf(Long_t size, void *p);
   static void delete_RooCPSHighMassVBFNoInterf(void *p);
   static void deleteArray_RooCPSHighMassVBFNoInterf(void *p);
   static void destruct_RooCPSHighMassVBFNoInterf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooCPSHighMassVBFNoInterf*)
   {
      ::RooCPSHighMassVBFNoInterf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooCPSHighMassVBFNoInterf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooCPSHighMassVBFNoInterf", ::RooCPSHighMassVBFNoInterf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h", 1054,
                  typeid(::RooCPSHighMassVBFNoInterf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooCPSHighMassVBFNoInterf::Dictionary, isa_proxy, 4,
                  sizeof(::RooCPSHighMassVBFNoInterf) );
      instance.SetNew(&new_RooCPSHighMassVBFNoInterf);
      instance.SetNewArray(&newArray_RooCPSHighMassVBFNoInterf);
      instance.SetDelete(&delete_RooCPSHighMassVBFNoInterf);
      instance.SetDeleteArray(&deleteArray_RooCPSHighMassVBFNoInterf);
      instance.SetDestructor(&destruct_RooCPSHighMassVBFNoInterf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooCPSHighMassVBFNoInterf*)
   {
      return GenerateInitInstanceLocal((::RooCPSHighMassVBFNoInterf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooCPSHighMassVBFNoInterf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooSigPlusInt(void *p = 0);
   static void *newArray_RooSigPlusInt(Long_t size, void *p);
   static void delete_RooSigPlusInt(void *p);
   static void deleteArray_RooSigPlusInt(void *p);
   static void destruct_RooSigPlusInt(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooSigPlusInt*)
   {
      ::RooSigPlusInt *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooSigPlusInt >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooSigPlusInt", ::RooSigPlusInt::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h", 1095,
                  typeid(::RooSigPlusInt), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooSigPlusInt::Dictionary, isa_proxy, 4,
                  sizeof(::RooSigPlusInt) );
      instance.SetNew(&new_RooSigPlusInt);
      instance.SetNewArray(&newArray_RooSigPlusInt);
      instance.SetDelete(&delete_RooSigPlusInt);
      instance.SetDeleteArray(&deleteArray_RooSigPlusInt);
      instance.SetDestructor(&destruct_RooSigPlusInt);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooSigPlusInt*)
   {
      return GenerateInitInstanceLocal((::RooSigPlusInt*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooSigPlusInt*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooErfExpPdf(void *p = 0);
   static void *newArray_RooErfExpPdf(Long_t size, void *p);
   static void delete_RooErfExpPdf(void *p);
   static void deleteArray_RooErfExpPdf(void *p);
   static void destruct_RooErfExpPdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooErfExpPdf*)
   {
      ::RooErfExpPdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooErfExpPdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooErfExpPdf", ::RooErfExpPdf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h", 20,
                  typeid(::RooErfExpPdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooErfExpPdf::Dictionary, isa_proxy, 4,
                  sizeof(::RooErfExpPdf) );
      instance.SetNew(&new_RooErfExpPdf);
      instance.SetNewArray(&newArray_RooErfExpPdf);
      instance.SetDelete(&delete_RooErfExpPdf);
      instance.SetDeleteArray(&deleteArray_RooErfExpPdf);
      instance.SetDestructor(&destruct_RooErfExpPdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooErfExpPdf*)
   {
      return GenerateInitInstanceLocal((::RooErfExpPdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooErfExpPdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooAlpha(void *p = 0);
   static void *newArray_RooAlpha(Long_t size, void *p);
   static void delete_RooAlpha(void *p);
   static void deleteArray_RooAlpha(void *p);
   static void destruct_RooAlpha(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooAlpha*)
   {
      ::RooAlpha *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooAlpha >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooAlpha", ::RooAlpha::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h", 55,
                  typeid(::RooAlpha), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooAlpha::Dictionary, isa_proxy, 4,
                  sizeof(::RooAlpha) );
      instance.SetNew(&new_RooAlpha);
      instance.SetNewArray(&newArray_RooAlpha);
      instance.SetDelete(&delete_RooAlpha);
      instance.SetDeleteArray(&deleteArray_RooAlpha);
      instance.SetDestructor(&destruct_RooAlpha);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooAlpha*)
   {
      return GenerateInitInstanceLocal((::RooAlpha*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooAlpha*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooAlphaExp(void *p = 0);
   static void *newArray_RooAlphaExp(Long_t size, void *p);
   static void delete_RooAlphaExp(void *p);
   static void deleteArray_RooAlphaExp(void *p);
   static void destruct_RooAlphaExp(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooAlphaExp*)
   {
      ::RooAlphaExp *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooAlphaExp >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooAlphaExp", ::RooAlphaExp::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h", 97,
                  typeid(::RooAlphaExp), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooAlphaExp::Dictionary, isa_proxy, 4,
                  sizeof(::RooAlphaExp) );
      instance.SetNew(&new_RooAlphaExp);
      instance.SetNewArray(&newArray_RooAlphaExp);
      instance.SetDelete(&delete_RooAlphaExp);
      instance.SetDeleteArray(&deleteArray_RooAlphaExp);
      instance.SetDestructor(&destruct_RooAlphaExp);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooAlphaExp*)
   {
      return GenerateInitInstanceLocal((::RooAlphaExp*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooAlphaExp*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooBWRunPdf(void *p = 0);
   static void *newArray_RooBWRunPdf(Long_t size, void *p);
   static void delete_RooBWRunPdf(void *p);
   static void deleteArray_RooBWRunPdf(void *p);
   static void destruct_RooBWRunPdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooBWRunPdf*)
   {
      ::RooBWRunPdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooBWRunPdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooBWRunPdf", ::RooBWRunPdf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h", 130,
                  typeid(::RooBWRunPdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooBWRunPdf::Dictionary, isa_proxy, 4,
                  sizeof(::RooBWRunPdf) );
      instance.SetNew(&new_RooBWRunPdf);
      instance.SetNewArray(&newArray_RooBWRunPdf);
      instance.SetDelete(&delete_RooBWRunPdf);
      instance.SetDeleteArray(&deleteArray_RooBWRunPdf);
      instance.SetDestructor(&destruct_RooBWRunPdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooBWRunPdf*)
   {
      return GenerateInitInstanceLocal((::RooBWRunPdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooBWRunPdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooErfPow2Pdf(void *p = 0);
   static void *newArray_RooErfPow2Pdf(Long_t size, void *p);
   static void delete_RooErfPow2Pdf(void *p);
   static void deleteArray_RooErfPow2Pdf(void *p);
   static void destruct_RooErfPow2Pdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooErfPow2Pdf*)
   {
      ::RooErfPow2Pdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooErfPow2Pdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooErfPow2Pdf", ::RooErfPow2Pdf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h", 161,
                  typeid(::RooErfPow2Pdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooErfPow2Pdf::Dictionary, isa_proxy, 4,
                  sizeof(::RooErfPow2Pdf) );
      instance.SetNew(&new_RooErfPow2Pdf);
      instance.SetNewArray(&newArray_RooErfPow2Pdf);
      instance.SetDelete(&delete_RooErfPow2Pdf);
      instance.SetDeleteArray(&deleteArray_RooErfPow2Pdf);
      instance.SetDestructor(&destruct_RooErfPow2Pdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooErfPow2Pdf*)
   {
      return GenerateInitInstanceLocal((::RooErfPow2Pdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooErfPow2Pdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooAlpha4ErfPow2Pdf(void *p = 0);
   static void *newArray_RooAlpha4ErfPow2Pdf(Long_t size, void *p);
   static void delete_RooAlpha4ErfPow2Pdf(void *p);
   static void deleteArray_RooAlpha4ErfPow2Pdf(void *p);
   static void destruct_RooAlpha4ErfPow2Pdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooAlpha4ErfPow2Pdf*)
   {
      ::RooAlpha4ErfPow2Pdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooAlpha4ErfPow2Pdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooAlpha4ErfPow2Pdf", ::RooAlpha4ErfPow2Pdf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h", 195,
                  typeid(::RooAlpha4ErfPow2Pdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooAlpha4ErfPow2Pdf::Dictionary, isa_proxy, 4,
                  sizeof(::RooAlpha4ErfPow2Pdf) );
      instance.SetNew(&new_RooAlpha4ErfPow2Pdf);
      instance.SetNewArray(&newArray_RooAlpha4ErfPow2Pdf);
      instance.SetDelete(&delete_RooAlpha4ErfPow2Pdf);
      instance.SetDeleteArray(&deleteArray_RooAlpha4ErfPow2Pdf);
      instance.SetDestructor(&destruct_RooAlpha4ErfPow2Pdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooAlpha4ErfPow2Pdf*)
   {
      return GenerateInitInstanceLocal((::RooAlpha4ErfPow2Pdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooAlpha4ErfPow2Pdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooErfPowExpPdf(void *p = 0);
   static void *newArray_RooErfPowExpPdf(Long_t size, void *p);
   static void delete_RooErfPowExpPdf(void *p);
   static void deleteArray_RooErfPowExpPdf(void *p);
   static void destruct_RooErfPowExpPdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooErfPowExpPdf*)
   {
      ::RooErfPowExpPdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooErfPowExpPdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooErfPowExpPdf", ::RooErfPowExpPdf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h", 241,
                  typeid(::RooErfPowExpPdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooErfPowExpPdf::Dictionary, isa_proxy, 4,
                  sizeof(::RooErfPowExpPdf) );
      instance.SetNew(&new_RooErfPowExpPdf);
      instance.SetNewArray(&newArray_RooErfPowExpPdf);
      instance.SetDelete(&delete_RooErfPowExpPdf);
      instance.SetDeleteArray(&deleteArray_RooErfPowExpPdf);
      instance.SetDestructor(&destruct_RooErfPowExpPdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooErfPowExpPdf*)
   {
      return GenerateInitInstanceLocal((::RooErfPowExpPdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooErfPowExpPdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooAlpha4ErfPowExpPdf(void *p = 0);
   static void *newArray_RooAlpha4ErfPowExpPdf(Long_t size, void *p);
   static void delete_RooAlpha4ErfPowExpPdf(void *p);
   static void deleteArray_RooAlpha4ErfPowExpPdf(void *p);
   static void destruct_RooAlpha4ErfPowExpPdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooAlpha4ErfPowExpPdf*)
   {
      ::RooAlpha4ErfPowExpPdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooAlpha4ErfPowExpPdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooAlpha4ErfPowExpPdf", ::RooAlpha4ErfPowExpPdf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h", 275,
                  typeid(::RooAlpha4ErfPowExpPdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooAlpha4ErfPowExpPdf::Dictionary, isa_proxy, 4,
                  sizeof(::RooAlpha4ErfPowExpPdf) );
      instance.SetNew(&new_RooAlpha4ErfPowExpPdf);
      instance.SetNewArray(&newArray_RooAlpha4ErfPowExpPdf);
      instance.SetDelete(&delete_RooAlpha4ErfPowExpPdf);
      instance.SetDeleteArray(&deleteArray_RooAlpha4ErfPowExpPdf);
      instance.SetDestructor(&destruct_RooAlpha4ErfPowExpPdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooAlpha4ErfPowExpPdf*)
   {
      return GenerateInitInstanceLocal((::RooAlpha4ErfPowExpPdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooAlpha4ErfPowExpPdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooGausExpPdf(void *p = 0);
   static void *newArray_RooGausExpPdf(Long_t size, void *p);
   static void delete_RooGausExpPdf(void *p);
   static void deleteArray_RooGausExpPdf(void *p);
   static void destruct_RooGausExpPdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooGausExpPdf*)
   {
      ::RooGausExpPdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooGausExpPdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooGausExpPdf", ::RooGausExpPdf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h", 319,
                  typeid(::RooGausExpPdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooGausExpPdf::Dictionary, isa_proxy, 4,
                  sizeof(::RooGausExpPdf) );
      instance.SetNew(&new_RooGausExpPdf);
      instance.SetNewArray(&newArray_RooGausExpPdf);
      instance.SetDelete(&delete_RooGausExpPdf);
      instance.SetDeleteArray(&deleteArray_RooGausExpPdf);
      instance.SetDestructor(&destruct_RooGausExpPdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooGausExpPdf*)
   {
      return GenerateInitInstanceLocal((::RooGausExpPdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooGausExpPdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooAlpha4GausExpPdf(void *p = 0);
   static void *newArray_RooAlpha4GausExpPdf(Long_t size, void *p);
   static void delete_RooAlpha4GausExpPdf(void *p);
   static void deleteArray_RooAlpha4GausExpPdf(void *p);
   static void destruct_RooAlpha4GausExpPdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooAlpha4GausExpPdf*)
   {
      ::RooAlpha4GausExpPdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooAlpha4GausExpPdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooAlpha4GausExpPdf", ::RooAlpha4GausExpPdf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h", 351,
                  typeid(::RooAlpha4GausExpPdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooAlpha4GausExpPdf::Dictionary, isa_proxy, 4,
                  sizeof(::RooAlpha4GausExpPdf) );
      instance.SetNew(&new_RooAlpha4GausExpPdf);
      instance.SetNewArray(&newArray_RooAlpha4GausExpPdf);
      instance.SetDelete(&delete_RooAlpha4GausExpPdf);
      instance.SetDeleteArray(&deleteArray_RooAlpha4GausExpPdf);
      instance.SetDestructor(&destruct_RooAlpha4GausExpPdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooAlpha4GausExpPdf*)
   {
      return GenerateInitInstanceLocal((::RooAlpha4GausExpPdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooAlpha4GausExpPdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooErfPowPdf(void *p = 0);
   static void *newArray_RooErfPowPdf(Long_t size, void *p);
   static void delete_RooErfPowPdf(void *p);
   static void deleteArray_RooErfPowPdf(void *p);
   static void destruct_RooErfPowPdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooErfPowPdf*)
   {
      ::RooErfPowPdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooErfPowPdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooErfPowPdf", ::RooErfPowPdf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h", 392,
                  typeid(::RooErfPowPdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooErfPowPdf::Dictionary, isa_proxy, 4,
                  sizeof(::RooErfPowPdf) );
      instance.SetNew(&new_RooErfPowPdf);
      instance.SetNewArray(&newArray_RooErfPowPdf);
      instance.SetDelete(&delete_RooErfPowPdf);
      instance.SetDeleteArray(&deleteArray_RooErfPowPdf);
      instance.SetDestructor(&destruct_RooErfPowPdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooErfPowPdf*)
   {
      return GenerateInitInstanceLocal((::RooErfPowPdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooErfPowPdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooAlpha4ErfPowPdf(void *p = 0);
   static void *newArray_RooAlpha4ErfPowPdf(Long_t size, void *p);
   static void delete_RooAlpha4ErfPowPdf(void *p);
   static void deleteArray_RooAlpha4ErfPowPdf(void *p);
   static void destruct_RooAlpha4ErfPowPdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooAlpha4ErfPowPdf*)
   {
      ::RooAlpha4ErfPowPdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooAlpha4ErfPowPdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooAlpha4ErfPowPdf", ::RooAlpha4ErfPowPdf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h", 423,
                  typeid(::RooAlpha4ErfPowPdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooAlpha4ErfPowPdf::Dictionary, isa_proxy, 4,
                  sizeof(::RooAlpha4ErfPowPdf) );
      instance.SetNew(&new_RooAlpha4ErfPowPdf);
      instance.SetNewArray(&newArray_RooAlpha4ErfPowPdf);
      instance.SetDelete(&delete_RooAlpha4ErfPowPdf);
      instance.SetDeleteArray(&deleteArray_RooAlpha4ErfPowPdf);
      instance.SetDestructor(&destruct_RooAlpha4ErfPowPdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooAlpha4ErfPowPdf*)
   {
      return GenerateInitInstanceLocal((::RooAlpha4ErfPowPdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooAlpha4ErfPowPdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooPow2Pdf(void *p = 0);
   static void *newArray_RooPow2Pdf(Long_t size, void *p);
   static void delete_RooPow2Pdf(void *p);
   static void deleteArray_RooPow2Pdf(void *p);
   static void destruct_RooPow2Pdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooPow2Pdf*)
   {
      ::RooPow2Pdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooPow2Pdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooPow2Pdf", ::RooPow2Pdf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h", 460,
                  typeid(::RooPow2Pdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooPow2Pdf::Dictionary, isa_proxy, 4,
                  sizeof(::RooPow2Pdf) );
      instance.SetNew(&new_RooPow2Pdf);
      instance.SetNewArray(&newArray_RooPow2Pdf);
      instance.SetDelete(&delete_RooPow2Pdf);
      instance.SetDeleteArray(&deleteArray_RooPow2Pdf);
      instance.SetDestructor(&destruct_RooPow2Pdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooPow2Pdf*)
   {
      return GenerateInitInstanceLocal((::RooPow2Pdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooPow2Pdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooPowPdf(void *p = 0);
   static void *newArray_RooPowPdf(Long_t size, void *p);
   static void delete_RooPowPdf(void *p);
   static void deleteArray_RooPowPdf(void *p);
   static void destruct_RooPowPdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooPowPdf*)
   {
      ::RooPowPdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooPowPdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooPowPdf", ::RooPowPdf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h", 489,
                  typeid(::RooPowPdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooPowPdf::Dictionary, isa_proxy, 4,
                  sizeof(::RooPowPdf) );
      instance.SetNew(&new_RooPowPdf);
      instance.SetNewArray(&newArray_RooPowPdf);
      instance.SetDelete(&delete_RooPowPdf);
      instance.SetDeleteArray(&deleteArray_RooPowPdf);
      instance.SetDestructor(&destruct_RooPowPdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooPowPdf*)
   {
      return GenerateInitInstanceLocal((::RooPowPdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooPowPdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooQCDPdf(void *p = 0);
   static void *newArray_RooQCDPdf(Long_t size, void *p);
   static void delete_RooQCDPdf(void *p);
   static void deleteArray_RooQCDPdf(void *p);
   static void destruct_RooQCDPdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooQCDPdf*)
   {
      ::RooQCDPdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooQCDPdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooQCDPdf", ::RooQCDPdf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h", 516,
                  typeid(::RooQCDPdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooQCDPdf::Dictionary, isa_proxy, 4,
                  sizeof(::RooQCDPdf) );
      instance.SetNew(&new_RooQCDPdf);
      instance.SetNewArray(&newArray_RooQCDPdf);
      instance.SetDelete(&delete_RooQCDPdf);
      instance.SetDeleteArray(&deleteArray_RooQCDPdf);
      instance.SetDestructor(&destruct_RooQCDPdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooQCDPdf*)
   {
      return GenerateInitInstanceLocal((::RooQCDPdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooQCDPdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooUser1Pdf(void *p = 0);
   static void *newArray_RooUser1Pdf(Long_t size, void *p);
   static void delete_RooUser1Pdf(void *p);
   static void deleteArray_RooUser1Pdf(void *p);
   static void destruct_RooUser1Pdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooUser1Pdf*)
   {
      ::RooUser1Pdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooUser1Pdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooUser1Pdf", ::RooUser1Pdf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h", 547,
                  typeid(::RooUser1Pdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooUser1Pdf::Dictionary, isa_proxy, 4,
                  sizeof(::RooUser1Pdf) );
      instance.SetNew(&new_RooUser1Pdf);
      instance.SetNewArray(&newArray_RooUser1Pdf);
      instance.SetDelete(&delete_RooUser1Pdf);
      instance.SetDeleteArray(&deleteArray_RooUser1Pdf);
      instance.SetDestructor(&destruct_RooUser1Pdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooUser1Pdf*)
   {
      return GenerateInitInstanceLocal((::RooUser1Pdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooUser1Pdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooExpNPdf(void *p = 0);
   static void *newArray_RooExpNPdf(Long_t size, void *p);
   static void delete_RooExpNPdf(void *p);
   static void deleteArray_RooExpNPdf(void *p);
   static void destruct_RooExpNPdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooExpNPdf*)
   {
      ::RooExpNPdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooExpNPdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooExpNPdf", ::RooExpNPdf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h", 579,
                  typeid(::RooExpNPdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooExpNPdf::Dictionary, isa_proxy, 4,
                  sizeof(::RooExpNPdf) );
      instance.SetNew(&new_RooExpNPdf);
      instance.SetNewArray(&newArray_RooExpNPdf);
      instance.SetDelete(&delete_RooExpNPdf);
      instance.SetDeleteArray(&deleteArray_RooExpNPdf);
      instance.SetDestructor(&destruct_RooExpNPdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooExpNPdf*)
   {
      return GenerateInitInstanceLocal((::RooExpNPdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooExpNPdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooAlpha4ExpNPdf(void *p = 0);
   static void *newArray_RooAlpha4ExpNPdf(Long_t size, void *p);
   static void delete_RooAlpha4ExpNPdf(void *p);
   static void deleteArray_RooAlpha4ExpNPdf(void *p);
   static void destruct_RooAlpha4ExpNPdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooAlpha4ExpNPdf*)
   {
      ::RooAlpha4ExpNPdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooAlpha4ExpNPdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooAlpha4ExpNPdf", ::RooAlpha4ExpNPdf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h", 607,
                  typeid(::RooAlpha4ExpNPdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooAlpha4ExpNPdf::Dictionary, isa_proxy, 4,
                  sizeof(::RooAlpha4ExpNPdf) );
      instance.SetNew(&new_RooAlpha4ExpNPdf);
      instance.SetNewArray(&newArray_RooAlpha4ExpNPdf);
      instance.SetDelete(&delete_RooAlpha4ExpNPdf);
      instance.SetDeleteArray(&deleteArray_RooAlpha4ExpNPdf);
      instance.SetDestructor(&destruct_RooAlpha4ExpNPdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooAlpha4ExpNPdf*)
   {
      return GenerateInitInstanceLocal((::RooAlpha4ExpNPdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooAlpha4ExpNPdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooExpTailPdf(void *p = 0);
   static void *newArray_RooExpTailPdf(Long_t size, void *p);
   static void delete_RooExpTailPdf(void *p);
   static void deleteArray_RooExpTailPdf(void *p);
   static void destruct_RooExpTailPdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooExpTailPdf*)
   {
      ::RooExpTailPdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooExpTailPdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooExpTailPdf", ::RooExpTailPdf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h", 642,
                  typeid(::RooExpTailPdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooExpTailPdf::Dictionary, isa_proxy, 4,
                  sizeof(::RooExpTailPdf) );
      instance.SetNew(&new_RooExpTailPdf);
      instance.SetNewArray(&newArray_RooExpTailPdf);
      instance.SetDelete(&delete_RooExpTailPdf);
      instance.SetDeleteArray(&deleteArray_RooExpTailPdf);
      instance.SetDestructor(&destruct_RooExpTailPdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooExpTailPdf*)
   {
      return GenerateInitInstanceLocal((::RooExpTailPdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooExpTailPdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooAlpha4ExpTailPdf(void *p = 0);
   static void *newArray_RooAlpha4ExpTailPdf(Long_t size, void *p);
   static void delete_RooAlpha4ExpTailPdf(void *p);
   static void deleteArray_RooAlpha4ExpTailPdf(void *p);
   static void destruct_RooAlpha4ExpTailPdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooAlpha4ExpTailPdf*)
   {
      ::RooAlpha4ExpTailPdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooAlpha4ExpTailPdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooAlpha4ExpTailPdf", ::RooAlpha4ExpTailPdf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h", 670,
                  typeid(::RooAlpha4ExpTailPdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooAlpha4ExpTailPdf::Dictionary, isa_proxy, 4,
                  sizeof(::RooAlpha4ExpTailPdf) );
      instance.SetNew(&new_RooAlpha4ExpTailPdf);
      instance.SetNewArray(&newArray_RooAlpha4ExpTailPdf);
      instance.SetDelete(&delete_RooAlpha4ExpTailPdf);
      instance.SetDeleteArray(&deleteArray_RooAlpha4ExpTailPdf);
      instance.SetDestructor(&destruct_RooAlpha4ExpTailPdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooAlpha4ExpTailPdf*)
   {
      return GenerateInitInstanceLocal((::RooAlpha4ExpTailPdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooAlpha4ExpTailPdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_Roo2ExpPdf(void *p = 0);
   static void *newArray_Roo2ExpPdf(Long_t size, void *p);
   static void delete_Roo2ExpPdf(void *p);
   static void deleteArray_Roo2ExpPdf(void *p);
   static void destruct_Roo2ExpPdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::Roo2ExpPdf*)
   {
      ::Roo2ExpPdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::Roo2ExpPdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("Roo2ExpPdf", ::Roo2ExpPdf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h", 705,
                  typeid(::Roo2ExpPdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::Roo2ExpPdf::Dictionary, isa_proxy, 4,
                  sizeof(::Roo2ExpPdf) );
      instance.SetNew(&new_Roo2ExpPdf);
      instance.SetNewArray(&newArray_Roo2ExpPdf);
      instance.SetDelete(&delete_Roo2ExpPdf);
      instance.SetDeleteArray(&deleteArray_Roo2ExpPdf);
      instance.SetDestructor(&destruct_Roo2ExpPdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::Roo2ExpPdf*)
   {
      return GenerateInitInstanceLocal((::Roo2ExpPdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::Roo2ExpPdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooAlpha42ExpPdf(void *p = 0);
   static void *newArray_RooAlpha42ExpPdf(Long_t size, void *p);
   static void delete_RooAlpha42ExpPdf(void *p);
   static void deleteArray_RooAlpha42ExpPdf(void *p);
   static void destruct_RooAlpha42ExpPdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooAlpha42ExpPdf*)
   {
      ::RooAlpha42ExpPdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooAlpha42ExpPdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooAlpha42ExpPdf", ::RooAlpha42ExpPdf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h", 735,
                  typeid(::RooAlpha42ExpPdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooAlpha42ExpPdf::Dictionary, isa_proxy, 4,
                  sizeof(::RooAlpha42ExpPdf) );
      instance.SetNew(&new_RooAlpha42ExpPdf);
      instance.SetNewArray(&newArray_RooAlpha42ExpPdf);
      instance.SetDelete(&delete_RooAlpha42ExpPdf);
      instance.SetDeleteArray(&deleteArray_RooAlpha42ExpPdf);
      instance.SetDestructor(&destruct_RooAlpha42ExpPdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooAlpha42ExpPdf*)
   {
      return GenerateInitInstanceLocal((::RooAlpha42ExpPdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooAlpha42ExpPdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooAnaExpNPdf(void *p = 0);
   static void *newArray_RooAnaExpNPdf(Long_t size, void *p);
   static void delete_RooAnaExpNPdf(void *p);
   static void deleteArray_RooAnaExpNPdf(void *p);
   static void destruct_RooAnaExpNPdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooAnaExpNPdf*)
   {
      ::RooAnaExpNPdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooAnaExpNPdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooAnaExpNPdf", ::RooAnaExpNPdf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h", 772,
                  typeid(::RooAnaExpNPdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooAnaExpNPdf::Dictionary, isa_proxy, 4,
                  sizeof(::RooAnaExpNPdf) );
      instance.SetNew(&new_RooAnaExpNPdf);
      instance.SetNewArray(&newArray_RooAnaExpNPdf);
      instance.SetDelete(&delete_RooAnaExpNPdf);
      instance.SetDeleteArray(&deleteArray_RooAnaExpNPdf);
      instance.SetDestructor(&destruct_RooAnaExpNPdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooAnaExpNPdf*)
   {
      return GenerateInitInstanceLocal((::RooAnaExpNPdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooAnaExpNPdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooDoubleCrystalBall(void *p = 0);
   static void *newArray_RooDoubleCrystalBall(Long_t size, void *p);
   static void delete_RooDoubleCrystalBall(void *p);
   static void deleteArray_RooDoubleCrystalBall(void *p);
   static void destruct_RooDoubleCrystalBall(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooDoubleCrystalBall*)
   {
      ::RooDoubleCrystalBall *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooDoubleCrystalBall >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooDoubleCrystalBall", ::RooDoubleCrystalBall::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h", 804,
                  typeid(::RooDoubleCrystalBall), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooDoubleCrystalBall::Dictionary, isa_proxy, 4,
                  sizeof(::RooDoubleCrystalBall) );
      instance.SetNew(&new_RooDoubleCrystalBall);
      instance.SetNewArray(&newArray_RooDoubleCrystalBall);
      instance.SetDelete(&delete_RooDoubleCrystalBall);
      instance.SetDeleteArray(&deleteArray_RooDoubleCrystalBall);
      instance.SetDestructor(&destruct_RooDoubleCrystalBall);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooDoubleCrystalBall*)
   {
      return GenerateInitInstanceLocal((::RooDoubleCrystalBall*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooDoubleCrystalBall*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooCB(void *p = 0);
   static void *newArray_RooCB(Long_t size, void *p);
   static void delete_RooCB(void *p);
   static void deleteArray_RooCB(void *p);
   static void destruct_RooCB(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooCB*)
   {
      ::RooCB *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooCB >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooCB", ::RooCB::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ2L2QRooPdfs.h", 8,
                  typeid(::RooCB), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooCB::Dictionary, isa_proxy, 4,
                  sizeof(::RooCB) );
      instance.SetNew(&new_RooCB);
      instance.SetNewArray(&newArray_RooCB);
      instance.SetDelete(&delete_RooCB);
      instance.SetDeleteArray(&deleteArray_RooCB);
      instance.SetDestructor(&destruct_RooCB);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooCB*)
   {
      return GenerateInitInstanceLocal((::RooCB*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooCB*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooDoubleCB(void *p = 0);
   static void *newArray_RooDoubleCB(Long_t size, void *p);
   static void delete_RooDoubleCB(void *p);
   static void deleteArray_RooDoubleCB(void *p);
   static void destruct_RooDoubleCB(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooDoubleCB*)
   {
      ::RooDoubleCB *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooDoubleCB >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooDoubleCB", ::RooDoubleCB::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ2L2QRooPdfs.h", 40,
                  typeid(::RooDoubleCB), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooDoubleCB::Dictionary, isa_proxy, 4,
                  sizeof(::RooDoubleCB) );
      instance.SetNew(&new_RooDoubleCB);
      instance.SetNewArray(&newArray_RooDoubleCB);
      instance.SetDelete(&delete_RooDoubleCB);
      instance.SetDeleteArray(&deleteArray_RooDoubleCB);
      instance.SetDestructor(&destruct_RooDoubleCB);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooDoubleCB*)
   {
      return GenerateInitInstanceLocal((::RooDoubleCB*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooDoubleCB*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooFermi(void *p = 0);
   static void *newArray_RooFermi(Long_t size, void *p);
   static void delete_RooFermi(void *p);
   static void deleteArray_RooFermi(void *p);
   static void destruct_RooFermi(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooFermi*)
   {
      ::RooFermi *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooFermi >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooFermi", ::RooFermi::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ2L2QRooPdfs.h", 86,
                  typeid(::RooFermi), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooFermi::Dictionary, isa_proxy, 4,
                  sizeof(::RooFermi) );
      instance.SetNew(&new_RooFermi);
      instance.SetNewArray(&newArray_RooFermi);
      instance.SetDelete(&delete_RooFermi);
      instance.SetDeleteArray(&deleteArray_RooFermi);
      instance.SetDestructor(&destruct_RooFermi);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooFermi*)
   {
      return GenerateInitInstanceLocal((::RooFermi*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooFermi*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooRelBW(void *p = 0);
   static void *newArray_RooRelBW(Long_t size, void *p);
   static void delete_RooRelBW(void *p);
   static void deleteArray_RooRelBW(void *p);
   static void destruct_RooRelBW(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooRelBW*)
   {
      ::RooRelBW *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooRelBW >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooRelBW", ::RooRelBW::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ2L2QRooPdfs.h", 111,
                  typeid(::RooRelBW), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooRelBW::Dictionary, isa_proxy, 4,
                  sizeof(::RooRelBW) );
      instance.SetNew(&new_RooRelBW);
      instance.SetNewArray(&newArray_RooRelBW);
      instance.SetDelete(&delete_RooRelBW);
      instance.SetDeleteArray(&deleteArray_RooRelBW);
      instance.SetDestructor(&destruct_RooRelBW);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooRelBW*)
   {
      return GenerateInitInstanceLocal((::RooRelBW*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooRelBW*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_Triangle(void *p = 0);
   static void *newArray_Triangle(Long_t size, void *p);
   static void delete_Triangle(void *p);
   static void deleteArray_Triangle(void *p);
   static void destruct_Triangle(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::Triangle*)
   {
      ::Triangle *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::Triangle >(0);
      static ::ROOT::TGenericClassInfo 
         instance("Triangle", ::Triangle::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ2L2QRooPdfs.h", 139,
                  typeid(::Triangle), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::Triangle::Dictionary, isa_proxy, 4,
                  sizeof(::Triangle) );
      instance.SetNew(&new_Triangle);
      instance.SetNewArray(&newArray_Triangle);
      instance.SetDelete(&delete_Triangle);
      instance.SetDeleteArray(&deleteArray_Triangle);
      instance.SetDestructor(&destruct_Triangle);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::Triangle*)
   {
      return GenerateInitInstanceLocal((::Triangle*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::Triangle*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooLevelledExp(void *p = 0);
   static void *newArray_RooLevelledExp(Long_t size, void *p);
   static void delete_RooLevelledExp(void *p);
   static void deleteArray_RooLevelledExp(void *p);
   static void destruct_RooLevelledExp(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooLevelledExp*)
   {
      ::RooLevelledExp *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooLevelledExp >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooLevelledExp", ::RooLevelledExp::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ2L2QRooPdfs.h", 172,
                  typeid(::RooLevelledExp), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooLevelledExp::Dictionary, isa_proxy, 4,
                  sizeof(::RooLevelledExp) );
      instance.SetNew(&new_RooLevelledExp);
      instance.SetNewArray(&newArray_RooLevelledExp);
      instance.SetDelete(&delete_RooLevelledExp);
      instance.SetDeleteArray(&deleteArray_RooLevelledExp);
      instance.SetDestructor(&destruct_RooLevelledExp);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooLevelledExp*)
   {
      return GenerateInitInstanceLocal((::RooLevelledExp*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooLevelledExp*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooPower(void *p = 0);
   static void *newArray_RooPower(Long_t size, void *p);
   static void delete_RooPower(void *p);
   static void deleteArray_RooPower(void *p);
   static void destruct_RooPower(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooPower*)
   {
      ::RooPower *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooPower >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooPower", ::RooPower::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HGGRooPdfs.h", 25,
                  typeid(::RooPower), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooPower::Dictionary, isa_proxy, 4,
                  sizeof(::RooPower) );
      instance.SetNew(&new_RooPower);
      instance.SetNewArray(&newArray_RooPower);
      instance.SetDelete(&delete_RooPower);
      instance.SetDeleteArray(&deleteArray_RooPower);
      instance.SetDestructor(&destruct_RooPower);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooPower*)
   {
      return GenerateInitInstanceLocal((::RooPower*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooPower*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooStepBernstein(void *p = 0);
   static void *newArray_RooStepBernstein(Long_t size, void *p);
   static void delete_RooStepBernstein(void *p);
   static void deleteArray_RooStepBernstein(void *p);
   static void destruct_RooStepBernstein(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooStepBernstein*)
   {
      ::RooStepBernstein *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooStepBernstein >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooStepBernstein", ::RooStepBernstein::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZGRooPdfs.h", 23,
                  typeid(::RooStepBernstein), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooStepBernstein::Dictionary, isa_proxy, 4,
                  sizeof(::RooStepBernstein) );
      instance.SetNew(&new_RooStepBernstein);
      instance.SetNewArray(&newArray_RooStepBernstein);
      instance.SetDelete(&delete_RooStepBernstein);
      instance.SetDeleteArray(&deleteArray_RooStepBernstein);
      instance.SetDestructor(&destruct_RooStepBernstein);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooStepBernstein*)
   {
      return GenerateInitInstanceLocal((::RooStepBernstein*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooStepBernstein*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooGaussStepBernstein(void *p = 0);
   static void *newArray_RooGaussStepBernstein(Long_t size, void *p);
   static void delete_RooGaussStepBernstein(void *p);
   static void deleteArray_RooGaussStepBernstein(void *p);
   static void destruct_RooGaussStepBernstein(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooGaussStepBernstein*)
   {
      ::RooGaussStepBernstein *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooGaussStepBernstein >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooGaussStepBernstein", ::RooGaussStepBernstein::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZGRooPdfs.h", 49,
                  typeid(::RooGaussStepBernstein), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooGaussStepBernstein::Dictionary, isa_proxy, 4,
                  sizeof(::RooGaussStepBernstein) );
      instance.SetNew(&new_RooGaussStepBernstein);
      instance.SetNewArray(&newArray_RooGaussStepBernstein);
      instance.SetDelete(&delete_RooGaussStepBernstein);
      instance.SetDeleteArray(&deleteArray_RooGaussStepBernstein);
      instance.SetDestructor(&destruct_RooGaussStepBernstein);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooGaussStepBernstein*)
   {
      return GenerateInitInstanceLocal((::RooGaussStepBernstein*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooGaussStepBernstein*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static TClass *cmsmathcLcLSequentialMinimizer_Dictionary();
   static void cmsmathcLcLSequentialMinimizer_TClassManip(TClass*);
   static void *new_cmsmathcLcLSequentialMinimizer(void *p = 0);
   static void *newArray_cmsmathcLcLSequentialMinimizer(Long_t size, void *p);
   static void delete_cmsmathcLcLSequentialMinimizer(void *p);
   static void deleteArray_cmsmathcLcLSequentialMinimizer(void *p);
   static void destruct_cmsmathcLcLSequentialMinimizer(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::cmsmath::SequentialMinimizer*)
   {
      ::cmsmath::SequentialMinimizer *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::cmsmath::SequentialMinimizer));
      static ::ROOT::TGenericClassInfo 
         instance("cmsmath::SequentialMinimizer", "HiggsAnalysis/CombinedLimit/interface/SequentialMinimizer.h", 109,
                  typeid(::cmsmath::SequentialMinimizer), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &cmsmathcLcLSequentialMinimizer_Dictionary, isa_proxy, 4,
                  sizeof(::cmsmath::SequentialMinimizer) );
      instance.SetNew(&new_cmsmathcLcLSequentialMinimizer);
      instance.SetNewArray(&newArray_cmsmathcLcLSequentialMinimizer);
      instance.SetDelete(&delete_cmsmathcLcLSequentialMinimizer);
      instance.SetDeleteArray(&deleteArray_cmsmathcLcLSequentialMinimizer);
      instance.SetDestructor(&destruct_cmsmathcLcLSequentialMinimizer);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::cmsmath::SequentialMinimizer*)
   {
      return GenerateInitInstanceLocal((::cmsmath::SequentialMinimizer*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::cmsmath::SequentialMinimizer*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *cmsmathcLcLSequentialMinimizer_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::cmsmath::SequentialMinimizer*)0x0)->GetClass();
      cmsmathcLcLSequentialMinimizer_TClassManip(theClass);
   return theClass;
   }

   static void cmsmathcLcLSequentialMinimizer_TClassManip(TClass* theClass){
      theClass->CreateAttributeMap();
      TDictAttributeMap* attrMap( theClass->GetAttributeMap() );
      attrMap->AddProperty("transient","true");
   }

} // end of namespace ROOT

namespace ROOT {
   static void *new_ProcessNormalization(void *p = 0);
   static void *newArray_ProcessNormalization(Long_t size, void *p);
   static void delete_ProcessNormalization(void *p);
   static void deleteArray_ProcessNormalization(void *p);
   static void destruct_ProcessNormalization(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ProcessNormalization*)
   {
      ::ProcessNormalization *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::ProcessNormalization >(0);
      static ::ROOT::TGenericClassInfo 
         instance("ProcessNormalization", ::ProcessNormalization::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/ProcessNormalization.h", 17,
                  typeid(::ProcessNormalization), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::ProcessNormalization::Dictionary, isa_proxy, 4,
                  sizeof(::ProcessNormalization) );
      instance.SetNew(&new_ProcessNormalization);
      instance.SetNewArray(&newArray_ProcessNormalization);
      instance.SetDelete(&delete_ProcessNormalization);
      instance.SetDeleteArray(&deleteArray_ProcessNormalization);
      instance.SetDestructor(&destruct_ProcessNormalization);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ProcessNormalization*)
   {
      return GenerateInitInstanceLocal((::ProcessNormalization*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::ProcessNormalization*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooRealFlooredSumPdf(void *p = 0);
   static void *newArray_RooRealFlooredSumPdf(Long_t size, void *p);
   static void delete_RooRealFlooredSumPdf(void *p);
   static void deleteArray_RooRealFlooredSumPdf(void *p);
   static void destruct_RooRealFlooredSumPdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooRealFlooredSumPdf*)
   {
      ::RooRealFlooredSumPdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooRealFlooredSumPdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooRealFlooredSumPdf", ::RooRealFlooredSumPdf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/RooRealFlooredSumPdf.h", 27,
                  typeid(::RooRealFlooredSumPdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooRealFlooredSumPdf::Dictionary, isa_proxy, 4,
                  sizeof(::RooRealFlooredSumPdf) );
      instance.SetNew(&new_RooRealFlooredSumPdf);
      instance.SetNewArray(&newArray_RooRealFlooredSumPdf);
      instance.SetDelete(&delete_RooRealFlooredSumPdf);
      instance.SetDeleteArray(&deleteArray_RooRealFlooredSumPdf);
      instance.SetDestructor(&destruct_RooRealFlooredSumPdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooRealFlooredSumPdf*)
   {
      return GenerateInitInstanceLocal((::RooRealFlooredSumPdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooRealFlooredSumPdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooSpline1D(void *p = 0);
   static void *newArray_RooSpline1D(Long_t size, void *p);
   static void delete_RooSpline1D(void *p);
   static void deleteArray_RooSpline1D(void *p);
   static void destruct_RooSpline1D(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooSpline1D*)
   {
      ::RooSpline1D *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooSpline1D >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooSpline1D", ::RooSpline1D::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/RooSpline1D.h", 18,
                  typeid(::RooSpline1D), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooSpline1D::Dictionary, isa_proxy, 4,
                  sizeof(::RooSpline1D) );
      instance.SetNew(&new_RooSpline1D);
      instance.SetNewArray(&newArray_RooSpline1D);
      instance.SetDelete(&delete_RooSpline1D);
      instance.SetDeleteArray(&deleteArray_RooSpline1D);
      instance.SetDestructor(&destruct_RooSpline1D);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooSpline1D*)
   {
      return GenerateInitInstanceLocal((::RooSpline1D*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooSpline1D*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooSplineND(void *p = 0);
   static void *newArray_RooSplineND(Long_t size, void *p);
   static void delete_RooSplineND(void *p);
   static void deleteArray_RooSplineND(void *p);
   static void destruct_RooSplineND(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooSplineND*)
   {
      ::RooSplineND *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooSplineND >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooSplineND", ::RooSplineND::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/RooSplineND.h", 61,
                  typeid(::RooSplineND), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooSplineND::Dictionary, isa_proxy, 4,
                  sizeof(::RooSplineND) );
      instance.SetNew(&new_RooSplineND);
      instance.SetNewArray(&newArray_RooSplineND);
      instance.SetDelete(&delete_RooSplineND);
      instance.SetDeleteArray(&deleteArray_RooSplineND);
      instance.SetDestructor(&destruct_RooSplineND);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooSplineND*)
   {
      return GenerateInitInstanceLocal((::RooSplineND*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooSplineND*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void delete_RooScaleLOSM(void *p);
   static void deleteArray_RooScaleLOSM(void *p);
   static void destruct_RooScaleLOSM(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooScaleLOSM*)
   {
      ::RooScaleLOSM *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooScaleLOSM >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooScaleLOSM", ::RooScaleLOSM::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/RooScaleLOSM.h", 14,
                  typeid(::RooScaleLOSM), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooScaleLOSM::Dictionary, isa_proxy, 4,
                  sizeof(::RooScaleLOSM) );
      instance.SetDelete(&delete_RooScaleLOSM);
      instance.SetDeleteArray(&deleteArray_RooScaleLOSM);
      instance.SetDestructor(&destruct_RooScaleLOSM);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooScaleLOSM*)
   {
      return GenerateInitInstanceLocal((::RooScaleLOSM*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooScaleLOSM*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooScaleHGamGamLOSM(void *p = 0);
   static void *newArray_RooScaleHGamGamLOSM(Long_t size, void *p);
   static void delete_RooScaleHGamGamLOSM(void *p);
   static void deleteArray_RooScaleHGamGamLOSM(void *p);
   static void destruct_RooScaleHGamGamLOSM(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooScaleHGamGamLOSM*)
   {
      ::RooScaleHGamGamLOSM *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooScaleHGamGamLOSM >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooScaleHGamGamLOSM", ::RooScaleHGamGamLOSM::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/RooScaleLOSM.h", 40,
                  typeid(::RooScaleHGamGamLOSM), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooScaleHGamGamLOSM::Dictionary, isa_proxy, 4,
                  sizeof(::RooScaleHGamGamLOSM) );
      instance.SetNew(&new_RooScaleHGamGamLOSM);
      instance.SetNewArray(&newArray_RooScaleHGamGamLOSM);
      instance.SetDelete(&delete_RooScaleHGamGamLOSM);
      instance.SetDeleteArray(&deleteArray_RooScaleHGamGamLOSM);
      instance.SetDestructor(&destruct_RooScaleHGamGamLOSM);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooScaleHGamGamLOSM*)
   {
      return GenerateInitInstanceLocal((::RooScaleHGamGamLOSM*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooScaleHGamGamLOSM*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooScaleHGluGluLOSM(void *p = 0);
   static void *newArray_RooScaleHGluGluLOSM(Long_t size, void *p);
   static void delete_RooScaleHGluGluLOSM(void *p);
   static void deleteArray_RooScaleHGluGluLOSM(void *p);
   static void destruct_RooScaleHGluGluLOSM(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooScaleHGluGluLOSM*)
   {
      ::RooScaleHGluGluLOSM *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooScaleHGluGluLOSM >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooScaleHGluGluLOSM", ::RooScaleHGluGluLOSM::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/RooScaleLOSM.h", 59,
                  typeid(::RooScaleHGluGluLOSM), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooScaleHGluGluLOSM::Dictionary, isa_proxy, 4,
                  sizeof(::RooScaleHGluGluLOSM) );
      instance.SetNew(&new_RooScaleHGluGluLOSM);
      instance.SetNewArray(&newArray_RooScaleHGluGluLOSM);
      instance.SetDelete(&delete_RooScaleHGluGluLOSM);
      instance.SetDeleteArray(&deleteArray_RooScaleHGluGluLOSM);
      instance.SetDestructor(&destruct_RooScaleHGluGluLOSM);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooScaleHGluGluLOSM*)
   {
      return GenerateInitInstanceLocal((::RooScaleHGluGluLOSM*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooScaleHGluGluLOSM*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooScaleHGamGamLOSMPlusX(void *p = 0);
   static void *newArray_RooScaleHGamGamLOSMPlusX(Long_t size, void *p);
   static void delete_RooScaleHGamGamLOSMPlusX(void *p);
   static void deleteArray_RooScaleHGamGamLOSMPlusX(void *p);
   static void destruct_RooScaleHGamGamLOSMPlusX(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooScaleHGamGamLOSMPlusX*)
   {
      ::RooScaleHGamGamLOSMPlusX *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooScaleHGamGamLOSMPlusX >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooScaleHGamGamLOSMPlusX", ::RooScaleHGamGamLOSMPlusX::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/RooScaleLOSM.h", 78,
                  typeid(::RooScaleHGamGamLOSMPlusX), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooScaleHGamGamLOSMPlusX::Dictionary, isa_proxy, 4,
                  sizeof(::RooScaleHGamGamLOSMPlusX) );
      instance.SetNew(&new_RooScaleHGamGamLOSMPlusX);
      instance.SetNewArray(&newArray_RooScaleHGamGamLOSMPlusX);
      instance.SetDelete(&delete_RooScaleHGamGamLOSMPlusX);
      instance.SetDeleteArray(&deleteArray_RooScaleHGamGamLOSMPlusX);
      instance.SetDestructor(&destruct_RooScaleHGamGamLOSMPlusX);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooScaleHGamGamLOSMPlusX*)
   {
      return GenerateInitInstanceLocal((::RooScaleHGamGamLOSMPlusX*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooScaleHGamGamLOSMPlusX*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooScaleHGluGluLOSMPlusX(void *p = 0);
   static void *newArray_RooScaleHGluGluLOSMPlusX(Long_t size, void *p);
   static void delete_RooScaleHGluGluLOSMPlusX(void *p);
   static void deleteArray_RooScaleHGluGluLOSMPlusX(void *p);
   static void destruct_RooScaleHGluGluLOSMPlusX(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooScaleHGluGluLOSMPlusX*)
   {
      ::RooScaleHGluGluLOSMPlusX *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooScaleHGluGluLOSMPlusX >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooScaleHGluGluLOSMPlusX", ::RooScaleHGluGluLOSMPlusX::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/RooScaleLOSM.h", 97,
                  typeid(::RooScaleHGluGluLOSMPlusX), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooScaleHGluGluLOSMPlusX::Dictionary, isa_proxy, 4,
                  sizeof(::RooScaleHGluGluLOSMPlusX) );
      instance.SetNew(&new_RooScaleHGluGluLOSMPlusX);
      instance.SetNewArray(&newArray_RooScaleHGluGluLOSMPlusX);
      instance.SetDelete(&delete_RooScaleHGluGluLOSMPlusX);
      instance.SetDeleteArray(&deleteArray_RooScaleHGluGluLOSMPlusX);
      instance.SetDestructor(&destruct_RooScaleHGluGluLOSMPlusX);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooScaleHGluGluLOSMPlusX*)
   {
      return GenerateInitInstanceLocal((::RooScaleHGluGluLOSMPlusX*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooScaleHGluGluLOSMPlusX*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_rVrFLikelihood(void *p = 0);
   static void *newArray_rVrFLikelihood(Long_t size, void *p);
   static void delete_rVrFLikelihood(void *p);
   static void deleteArray_rVrFLikelihood(void *p);
   static void destruct_rVrFLikelihood(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::rVrFLikelihood*)
   {
      ::rVrFLikelihood *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::rVrFLikelihood >(0);
      static ::ROOT::TGenericClassInfo 
         instance("rVrFLikelihood", ::rVrFLikelihood::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/rVrFLikelihood.h", 9,
                  typeid(::rVrFLikelihood), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::rVrFLikelihood::Dictionary, isa_proxy, 4,
                  sizeof(::rVrFLikelihood) );
      instance.SetNew(&new_rVrFLikelihood);
      instance.SetNewArray(&newArray_rVrFLikelihood);
      instance.SetDelete(&delete_rVrFLikelihood);
      instance.SetDeleteArray(&deleteArray_rVrFLikelihood);
      instance.SetDestructor(&destruct_rVrFLikelihood);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::rVrFLikelihood*)
   {
      return GenerateInitInstanceLocal((::rVrFLikelihood*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::rVrFLikelihood*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooMultiPdf(void *p = 0);
   static void *newArray_RooMultiPdf(Long_t size, void *p);
   static void delete_RooMultiPdf(void *p);
   static void deleteArray_RooMultiPdf(void *p);
   static void destruct_RooMultiPdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooMultiPdf*)
   {
      ::RooMultiPdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooMultiPdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooMultiPdf", ::RooMultiPdf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/RooMultiPdf.h", 34,
                  typeid(::RooMultiPdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooMultiPdf::Dictionary, isa_proxy, 4,
                  sizeof(::RooMultiPdf) );
      instance.SetNew(&new_RooMultiPdf);
      instance.SetNewArray(&newArray_RooMultiPdf);
      instance.SetDelete(&delete_RooMultiPdf);
      instance.SetDeleteArray(&deleteArray_RooMultiPdf);
      instance.SetDestructor(&destruct_RooMultiPdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooMultiPdf*)
   {
      return GenerateInitInstanceLocal((::RooMultiPdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooMultiPdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static TClass *RooBernsteinFastlE1gR_Dictionary();
   static void RooBernsteinFastlE1gR_TClassManip(TClass*);
   static void *new_RooBernsteinFastlE1gR(void *p = 0);
   static void *newArray_RooBernsteinFastlE1gR(Long_t size, void *p);
   static void delete_RooBernsteinFastlE1gR(void *p);
   static void deleteArray_RooBernsteinFastlE1gR(void *p);
   static void destruct_RooBernsteinFastlE1gR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooBernsteinFast<1>*)
   {
      ::RooBernsteinFast<1> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooBernsteinFast<1> >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooBernsteinFast<1>", ::RooBernsteinFast<1>::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/RooBernsteinFast.h", 23,
                  typeid(::RooBernsteinFast<1>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &RooBernsteinFastlE1gR_Dictionary, isa_proxy, 4,
                  sizeof(::RooBernsteinFast<1>) );
      instance.SetNew(&new_RooBernsteinFastlE1gR);
      instance.SetNewArray(&newArray_RooBernsteinFastlE1gR);
      instance.SetDelete(&delete_RooBernsteinFastlE1gR);
      instance.SetDeleteArray(&deleteArray_RooBernsteinFastlE1gR);
      instance.SetDestructor(&destruct_RooBernsteinFastlE1gR);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooBernsteinFast<1>*)
   {
      return GenerateInitInstanceLocal((::RooBernsteinFast<1>*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooBernsteinFast<1>*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *RooBernsteinFastlE1gR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::RooBernsteinFast<1>*)0x0)->GetClass();
      RooBernsteinFastlE1gR_TClassManip(theClass);
   return theClass;
   }

   static void RooBernsteinFastlE1gR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *RooBernsteinFastlE2gR_Dictionary();
   static void RooBernsteinFastlE2gR_TClassManip(TClass*);
   static void *new_RooBernsteinFastlE2gR(void *p = 0);
   static void *newArray_RooBernsteinFastlE2gR(Long_t size, void *p);
   static void delete_RooBernsteinFastlE2gR(void *p);
   static void deleteArray_RooBernsteinFastlE2gR(void *p);
   static void destruct_RooBernsteinFastlE2gR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooBernsteinFast<2>*)
   {
      ::RooBernsteinFast<2> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooBernsteinFast<2> >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooBernsteinFast<2>", ::RooBernsteinFast<2>::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/RooBernsteinFast.h", 23,
                  typeid(::RooBernsteinFast<2>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &RooBernsteinFastlE2gR_Dictionary, isa_proxy, 4,
                  sizeof(::RooBernsteinFast<2>) );
      instance.SetNew(&new_RooBernsteinFastlE2gR);
      instance.SetNewArray(&newArray_RooBernsteinFastlE2gR);
      instance.SetDelete(&delete_RooBernsteinFastlE2gR);
      instance.SetDeleteArray(&deleteArray_RooBernsteinFastlE2gR);
      instance.SetDestructor(&destruct_RooBernsteinFastlE2gR);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooBernsteinFast<2>*)
   {
      return GenerateInitInstanceLocal((::RooBernsteinFast<2>*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooBernsteinFast<2>*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *RooBernsteinFastlE2gR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::RooBernsteinFast<2>*)0x0)->GetClass();
      RooBernsteinFastlE2gR_TClassManip(theClass);
   return theClass;
   }

   static void RooBernsteinFastlE2gR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *RooBernsteinFastlE3gR_Dictionary();
   static void RooBernsteinFastlE3gR_TClassManip(TClass*);
   static void *new_RooBernsteinFastlE3gR(void *p = 0);
   static void *newArray_RooBernsteinFastlE3gR(Long_t size, void *p);
   static void delete_RooBernsteinFastlE3gR(void *p);
   static void deleteArray_RooBernsteinFastlE3gR(void *p);
   static void destruct_RooBernsteinFastlE3gR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooBernsteinFast<3>*)
   {
      ::RooBernsteinFast<3> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooBernsteinFast<3> >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooBernsteinFast<3>", ::RooBernsteinFast<3>::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/RooBernsteinFast.h", 23,
                  typeid(::RooBernsteinFast<3>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &RooBernsteinFastlE3gR_Dictionary, isa_proxy, 4,
                  sizeof(::RooBernsteinFast<3>) );
      instance.SetNew(&new_RooBernsteinFastlE3gR);
      instance.SetNewArray(&newArray_RooBernsteinFastlE3gR);
      instance.SetDelete(&delete_RooBernsteinFastlE3gR);
      instance.SetDeleteArray(&deleteArray_RooBernsteinFastlE3gR);
      instance.SetDestructor(&destruct_RooBernsteinFastlE3gR);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooBernsteinFast<3>*)
   {
      return GenerateInitInstanceLocal((::RooBernsteinFast<3>*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooBernsteinFast<3>*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *RooBernsteinFastlE3gR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::RooBernsteinFast<3>*)0x0)->GetClass();
      RooBernsteinFastlE3gR_TClassManip(theClass);
   return theClass;
   }

   static void RooBernsteinFastlE3gR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *RooBernsteinFastlE4gR_Dictionary();
   static void RooBernsteinFastlE4gR_TClassManip(TClass*);
   static void *new_RooBernsteinFastlE4gR(void *p = 0);
   static void *newArray_RooBernsteinFastlE4gR(Long_t size, void *p);
   static void delete_RooBernsteinFastlE4gR(void *p);
   static void deleteArray_RooBernsteinFastlE4gR(void *p);
   static void destruct_RooBernsteinFastlE4gR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooBernsteinFast<4>*)
   {
      ::RooBernsteinFast<4> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooBernsteinFast<4> >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooBernsteinFast<4>", ::RooBernsteinFast<4>::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/RooBernsteinFast.h", 23,
                  typeid(::RooBernsteinFast<4>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &RooBernsteinFastlE4gR_Dictionary, isa_proxy, 4,
                  sizeof(::RooBernsteinFast<4>) );
      instance.SetNew(&new_RooBernsteinFastlE4gR);
      instance.SetNewArray(&newArray_RooBernsteinFastlE4gR);
      instance.SetDelete(&delete_RooBernsteinFastlE4gR);
      instance.SetDeleteArray(&deleteArray_RooBernsteinFastlE4gR);
      instance.SetDestructor(&destruct_RooBernsteinFastlE4gR);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooBernsteinFast<4>*)
   {
      return GenerateInitInstanceLocal((::RooBernsteinFast<4>*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooBernsteinFast<4>*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *RooBernsteinFastlE4gR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::RooBernsteinFast<4>*)0x0)->GetClass();
      RooBernsteinFastlE4gR_TClassManip(theClass);
   return theClass;
   }

   static void RooBernsteinFastlE4gR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *RooBernsteinFastlE5gR_Dictionary();
   static void RooBernsteinFastlE5gR_TClassManip(TClass*);
   static void *new_RooBernsteinFastlE5gR(void *p = 0);
   static void *newArray_RooBernsteinFastlE5gR(Long_t size, void *p);
   static void delete_RooBernsteinFastlE5gR(void *p);
   static void deleteArray_RooBernsteinFastlE5gR(void *p);
   static void destruct_RooBernsteinFastlE5gR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooBernsteinFast<5>*)
   {
      ::RooBernsteinFast<5> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooBernsteinFast<5> >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooBernsteinFast<5>", ::RooBernsteinFast<5>::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/RooBernsteinFast.h", 23,
                  typeid(::RooBernsteinFast<5>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &RooBernsteinFastlE5gR_Dictionary, isa_proxy, 4,
                  sizeof(::RooBernsteinFast<5>) );
      instance.SetNew(&new_RooBernsteinFastlE5gR);
      instance.SetNewArray(&newArray_RooBernsteinFastlE5gR);
      instance.SetDelete(&delete_RooBernsteinFastlE5gR);
      instance.SetDeleteArray(&deleteArray_RooBernsteinFastlE5gR);
      instance.SetDestructor(&destruct_RooBernsteinFastlE5gR);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooBernsteinFast<5>*)
   {
      return GenerateInitInstanceLocal((::RooBernsteinFast<5>*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooBernsteinFast<5>*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *RooBernsteinFastlE5gR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::RooBernsteinFast<5>*)0x0)->GetClass();
      RooBernsteinFastlE5gR_TClassManip(theClass);
   return theClass;
   }

   static void RooBernsteinFastlE5gR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *RooBernsteinFastlE6gR_Dictionary();
   static void RooBernsteinFastlE6gR_TClassManip(TClass*);
   static void *new_RooBernsteinFastlE6gR(void *p = 0);
   static void *newArray_RooBernsteinFastlE6gR(Long_t size, void *p);
   static void delete_RooBernsteinFastlE6gR(void *p);
   static void deleteArray_RooBernsteinFastlE6gR(void *p);
   static void destruct_RooBernsteinFastlE6gR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooBernsteinFast<6>*)
   {
      ::RooBernsteinFast<6> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooBernsteinFast<6> >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooBernsteinFast<6>", ::RooBernsteinFast<6>::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/RooBernsteinFast.h", 23,
                  typeid(::RooBernsteinFast<6>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &RooBernsteinFastlE6gR_Dictionary, isa_proxy, 4,
                  sizeof(::RooBernsteinFast<6>) );
      instance.SetNew(&new_RooBernsteinFastlE6gR);
      instance.SetNewArray(&newArray_RooBernsteinFastlE6gR);
      instance.SetDelete(&delete_RooBernsteinFastlE6gR);
      instance.SetDeleteArray(&deleteArray_RooBernsteinFastlE6gR);
      instance.SetDestructor(&destruct_RooBernsteinFastlE6gR);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooBernsteinFast<6>*)
   {
      return GenerateInitInstanceLocal((::RooBernsteinFast<6>*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooBernsteinFast<6>*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *RooBernsteinFastlE6gR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::RooBernsteinFast<6>*)0x0)->GetClass();
      RooBernsteinFastlE6gR_TClassManip(theClass);
   return theClass;
   }

   static void RooBernsteinFastlE6gR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *RooBernsteinFastlE7gR_Dictionary();
   static void RooBernsteinFastlE7gR_TClassManip(TClass*);
   static void *new_RooBernsteinFastlE7gR(void *p = 0);
   static void *newArray_RooBernsteinFastlE7gR(Long_t size, void *p);
   static void delete_RooBernsteinFastlE7gR(void *p);
   static void deleteArray_RooBernsteinFastlE7gR(void *p);
   static void destruct_RooBernsteinFastlE7gR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooBernsteinFast<7>*)
   {
      ::RooBernsteinFast<7> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooBernsteinFast<7> >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooBernsteinFast<7>", ::RooBernsteinFast<7>::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/RooBernsteinFast.h", 23,
                  typeid(::RooBernsteinFast<7>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &RooBernsteinFastlE7gR_Dictionary, isa_proxy, 4,
                  sizeof(::RooBernsteinFast<7>) );
      instance.SetNew(&new_RooBernsteinFastlE7gR);
      instance.SetNewArray(&newArray_RooBernsteinFastlE7gR);
      instance.SetDelete(&delete_RooBernsteinFastlE7gR);
      instance.SetDeleteArray(&deleteArray_RooBernsteinFastlE7gR);
      instance.SetDestructor(&destruct_RooBernsteinFastlE7gR);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooBernsteinFast<7>*)
   {
      return GenerateInitInstanceLocal((::RooBernsteinFast<7>*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooBernsteinFast<7>*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *RooBernsteinFastlE7gR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::RooBernsteinFast<7>*)0x0)->GetClass();
      RooBernsteinFastlE7gR_TClassManip(theClass);
   return theClass;
   }

   static void RooBernsteinFastlE7gR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static void *new_SimpleGaussianConstraint(void *p = 0);
   static void *newArray_SimpleGaussianConstraint(Long_t size, void *p);
   static void delete_SimpleGaussianConstraint(void *p);
   static void deleteArray_SimpleGaussianConstraint(void *p);
   static void destruct_SimpleGaussianConstraint(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::SimpleGaussianConstraint*)
   {
      ::SimpleGaussianConstraint *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::SimpleGaussianConstraint >(0);
      static ::ROOT::TGenericClassInfo 
         instance("SimpleGaussianConstraint", ::SimpleGaussianConstraint::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/SimpleGaussianConstraint.h", 6,
                  typeid(::SimpleGaussianConstraint), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::SimpleGaussianConstraint::Dictionary, isa_proxy, 4,
                  sizeof(::SimpleGaussianConstraint) );
      instance.SetNew(&new_SimpleGaussianConstraint);
      instance.SetNewArray(&newArray_SimpleGaussianConstraint);
      instance.SetDelete(&delete_SimpleGaussianConstraint);
      instance.SetDeleteArray(&deleteArray_SimpleGaussianConstraint);
      instance.SetDestructor(&destruct_SimpleGaussianConstraint);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::SimpleGaussianConstraint*)
   {
      return GenerateInitInstanceLocal((::SimpleGaussianConstraint*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::SimpleGaussianConstraint*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_SimplePoissonConstraint(void *p = 0);
   static void *newArray_SimplePoissonConstraint(Long_t size, void *p);
   static void delete_SimplePoissonConstraint(void *p);
   static void deleteArray_SimplePoissonConstraint(void *p);
   static void destruct_SimplePoissonConstraint(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::SimplePoissonConstraint*)
   {
      ::SimplePoissonConstraint *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::SimplePoissonConstraint >(0);
      static ::ROOT::TGenericClassInfo 
         instance("SimplePoissonConstraint", ::SimplePoissonConstraint::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/SimplePoissonConstraint.h", 7,
                  typeid(::SimplePoissonConstraint), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::SimplePoissonConstraint::Dictionary, isa_proxy, 4,
                  sizeof(::SimplePoissonConstraint) );
      instance.SetNew(&new_SimplePoissonConstraint);
      instance.SetNewArray(&newArray_SimplePoissonConstraint);
      instance.SetDelete(&delete_SimplePoissonConstraint);
      instance.SetDeleteArray(&deleteArray_SimplePoissonConstraint);
      instance.SetDestructor(&destruct_SimplePoissonConstraint);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::SimplePoissonConstraint*)
   {
      return GenerateInitInstanceLocal((::SimplePoissonConstraint*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::SimplePoissonConstraint*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_SimpleConstraintGroup(void *p = 0);
   static void *newArray_SimpleConstraintGroup(Long_t size, void *p);
   static void delete_SimpleConstraintGroup(void *p);
   static void deleteArray_SimpleConstraintGroup(void *p);
   static void destruct_SimpleConstraintGroup(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::SimpleConstraintGroup*)
   {
      ::SimpleConstraintGroup *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::SimpleConstraintGroup >(0);
      static ::ROOT::TGenericClassInfo 
         instance("SimpleConstraintGroup", ::SimpleConstraintGroup::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/SimpleConstraintGroup.h", 8,
                  typeid(::SimpleConstraintGroup), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::SimpleConstraintGroup::Dictionary, isa_proxy, 4,
                  sizeof(::SimpleConstraintGroup) );
      instance.SetNew(&new_SimpleConstraintGroup);
      instance.SetNewArray(&newArray_SimpleConstraintGroup);
      instance.SetDelete(&delete_SimpleConstraintGroup);
      instance.SetDeleteArray(&deleteArray_SimpleConstraintGroup);
      instance.SetDestructor(&destruct_SimpleConstraintGroup);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::SimpleConstraintGroup*)
   {
      return GenerateInitInstanceLocal((::SimpleConstraintGroup*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::SimpleConstraintGroup*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooStatscLcLHistFactorycLcLRooBSplineBases(void *p = 0);
   static void *newArray_RooStatscLcLHistFactorycLcLRooBSplineBases(Long_t size, void *p);
   static void delete_RooStatscLcLHistFactorycLcLRooBSplineBases(void *p);
   static void deleteArray_RooStatscLcLHistFactorycLcLRooBSplineBases(void *p);
   static void destruct_RooStatscLcLHistFactorycLcLRooBSplineBases(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooStats::HistFactory::RooBSplineBases*)
   {
      ::RooStats::HistFactory::RooBSplineBases *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooStats::HistFactory::RooBSplineBases >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooStats::HistFactory::RooBSplineBases", ::RooStats::HistFactory::RooBSplineBases::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/AtlasPdfs.h", 27,
                  typeid(::RooStats::HistFactory::RooBSplineBases), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooStats::HistFactory::RooBSplineBases::Dictionary, isa_proxy, 4,
                  sizeof(::RooStats::HistFactory::RooBSplineBases) );
      instance.SetNew(&new_RooStatscLcLHistFactorycLcLRooBSplineBases);
      instance.SetNewArray(&newArray_RooStatscLcLHistFactorycLcLRooBSplineBases);
      instance.SetDelete(&delete_RooStatscLcLHistFactorycLcLRooBSplineBases);
      instance.SetDeleteArray(&deleteArray_RooStatscLcLHistFactorycLcLRooBSplineBases);
      instance.SetDestructor(&destruct_RooStatscLcLHistFactorycLcLRooBSplineBases);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooStats::HistFactory::RooBSplineBases*)
   {
      return GenerateInitInstanceLocal((::RooStats::HistFactory::RooBSplineBases*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooStats::HistFactory::RooBSplineBases*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooStatscLcLHistFactorycLcLRooBSpline(void *p = 0);
   static void *newArray_RooStatscLcLHistFactorycLcLRooBSpline(Long_t size, void *p);
   static void delete_RooStatscLcLHistFactorycLcLRooBSpline(void *p);
   static void deleteArray_RooStatscLcLHistFactorycLcLRooBSpline(void *p);
   static void destruct_RooStatscLcLHistFactorycLcLRooBSpline(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooStats::HistFactory::RooBSpline*)
   {
      ::RooStats::HistFactory::RooBSpline *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooStats::HistFactory::RooBSpline >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooStats::HistFactory::RooBSpline", ::RooStats::HistFactory::RooBSpline::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/AtlasPdfs.h", 107,
                  typeid(::RooStats::HistFactory::RooBSpline), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooStats::HistFactory::RooBSpline::Dictionary, isa_proxy, 4,
                  sizeof(::RooStats::HistFactory::RooBSpline) );
      instance.SetNew(&new_RooStatscLcLHistFactorycLcLRooBSpline);
      instance.SetNewArray(&newArray_RooStatscLcLHistFactorycLcLRooBSpline);
      instance.SetDelete(&delete_RooStatscLcLHistFactorycLcLRooBSpline);
      instance.SetDeleteArray(&deleteArray_RooStatscLcLHistFactorycLcLRooBSpline);
      instance.SetDestructor(&destruct_RooStatscLcLHistFactorycLcLRooBSpline);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooStats::HistFactory::RooBSpline*)
   {
      return GenerateInitInstanceLocal((::RooStats::HistFactory::RooBSpline*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooStats::HistFactory::RooBSpline*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooParamKeysPdf(void *p = 0);
   static void *newArray_RooParamKeysPdf(Long_t size, void *p);
   static void delete_RooParamKeysPdf(void *p);
   static void deleteArray_RooParamKeysPdf(void *p);
   static void destruct_RooParamKeysPdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooParamKeysPdf*)
   {
      ::RooParamKeysPdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooParamKeysPdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooParamKeysPdf", ::RooParamKeysPdf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/AtlasPdfs.h", 194,
                  typeid(::RooParamKeysPdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooParamKeysPdf::Dictionary, isa_proxy, 4,
                  sizeof(::RooParamKeysPdf) );
      instance.SetNew(&new_RooParamKeysPdf);
      instance.SetNewArray(&newArray_RooParamKeysPdf);
      instance.SetDelete(&delete_RooParamKeysPdf);
      instance.SetDeleteArray(&deleteArray_RooParamKeysPdf);
      instance.SetDestructor(&destruct_RooParamKeysPdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooParamKeysPdf*)
   {
      return GenerateInitInstanceLocal((::RooParamKeysPdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooParamKeysPdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooStarMomentMorph(void *p = 0);
   static void *newArray_RooStarMomentMorph(Long_t size, void *p);
   static void delete_RooStarMomentMorph(void *p);
   static void deleteArray_RooStarMomentMorph(void *p);
   static void destruct_RooStarMomentMorph(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooStarMomentMorph*)
   {
      ::RooStarMomentMorph *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooStarMomentMorph >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooStarMomentMorph", ::RooStarMomentMorph::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/AtlasPdfs.h", 292,
                  typeid(::RooStarMomentMorph), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooStarMomentMorph::Dictionary, isa_proxy, 4,
                  sizeof(::RooStarMomentMorph) );
      instance.SetNew(&new_RooStarMomentMorph);
      instance.SetNewArray(&newArray_RooStarMomentMorph);
      instance.SetDelete(&delete_RooStarMomentMorph);
      instance.SetDeleteArray(&deleteArray_RooStarMomentMorph);
      instance.SetDestructor(&destruct_RooStarMomentMorph);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooStarMomentMorph*)
   {
      return GenerateInitInstanceLocal((::RooStarMomentMorph*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooStarMomentMorph*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static TClass *FastHistoAxis_tlEdoublegR_Dictionary();
   static void FastHistoAxis_tlEdoublegR_TClassManip(TClass*);
   static void *new_FastHistoAxis_tlEdoublegR(void *p = 0);
   static void *newArray_FastHistoAxis_tlEdoublegR(Long_t size, void *p);
   static void delete_FastHistoAxis_tlEdoublegR(void *p);
   static void deleteArray_FastHistoAxis_tlEdoublegR(void *p);
   static void destruct_FastHistoAxis_tlEdoublegR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::FastHistoAxis_t<double>*)
   {
      ::FastHistoAxis_t<double> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::FastHistoAxis_t<double>));
      static ::ROOT::TGenericClassInfo 
         instance("FastHistoAxis_t<double>", "HiggsAnalysis/CombinedLimit/interface/FastTemplate.h", 11,
                  typeid(::FastHistoAxis_t<double>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &FastHistoAxis_tlEdoublegR_Dictionary, isa_proxy, 4,
                  sizeof(::FastHistoAxis_t<double>) );
      instance.SetNew(&new_FastHistoAxis_tlEdoublegR);
      instance.SetNewArray(&newArray_FastHistoAxis_tlEdoublegR);
      instance.SetDelete(&delete_FastHistoAxis_tlEdoublegR);
      instance.SetDeleteArray(&deleteArray_FastHistoAxis_tlEdoublegR);
      instance.SetDestructor(&destruct_FastHistoAxis_tlEdoublegR);

      ::ROOT::AddClassAlternate("FastHistoAxis_t<double>","FastHistoAxis_d");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::FastHistoAxis_t<double>*)
   {
      return GenerateInitInstanceLocal((::FastHistoAxis_t<double>*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::FastHistoAxis_t<double>*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *FastHistoAxis_tlEdoublegR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::FastHistoAxis_t<double>*)0x0)->GetClass();
      FastHistoAxis_tlEdoublegR_TClassManip(theClass);
   return theClass;
   }

   static void FastHistoAxis_tlEdoublegR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *FastHistoAxis_tlEfloatgR_Dictionary();
   static void FastHistoAxis_tlEfloatgR_TClassManip(TClass*);
   static void *new_FastHistoAxis_tlEfloatgR(void *p = 0);
   static void *newArray_FastHistoAxis_tlEfloatgR(Long_t size, void *p);
   static void delete_FastHistoAxis_tlEfloatgR(void *p);
   static void deleteArray_FastHistoAxis_tlEfloatgR(void *p);
   static void destruct_FastHistoAxis_tlEfloatgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::FastHistoAxis_t<float>*)
   {
      ::FastHistoAxis_t<float> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::FastHistoAxis_t<float>));
      static ::ROOT::TGenericClassInfo 
         instance("FastHistoAxis_t<float>", "HiggsAnalysis/CombinedLimit/interface/FastTemplate.h", 11,
                  typeid(::FastHistoAxis_t<float>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &FastHistoAxis_tlEfloatgR_Dictionary, isa_proxy, 4,
                  sizeof(::FastHistoAxis_t<float>) );
      instance.SetNew(&new_FastHistoAxis_tlEfloatgR);
      instance.SetNewArray(&newArray_FastHistoAxis_tlEfloatgR);
      instance.SetDelete(&delete_FastHistoAxis_tlEfloatgR);
      instance.SetDeleteArray(&deleteArray_FastHistoAxis_tlEfloatgR);
      instance.SetDestructor(&destruct_FastHistoAxis_tlEfloatgR);

      ::ROOT::AddClassAlternate("FastHistoAxis_t<float>","FastHistoAxis_f");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::FastHistoAxis_t<float>*)
   {
      return GenerateInitInstanceLocal((::FastHistoAxis_t<float>*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::FastHistoAxis_t<float>*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *FastHistoAxis_tlEfloatgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::FastHistoAxis_t<float>*)0x0)->GetClass();
      FastHistoAxis_tlEfloatgR_TClassManip(theClass);
   return theClass;
   }

   static void FastHistoAxis_tlEfloatgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *FastTemplate_tlEdoublegR_Dictionary();
   static void FastTemplate_tlEdoublegR_TClassManip(TClass*);
   static void *new_FastTemplate_tlEdoublegR(void *p = 0);
   static void *newArray_FastTemplate_tlEdoublegR(Long_t size, void *p);
   static void delete_FastTemplate_tlEdoublegR(void *p);
   static void deleteArray_FastTemplate_tlEdoublegR(void *p);
   static void destruct_FastTemplate_tlEdoublegR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::FastTemplate_t<double>*)
   {
      ::FastTemplate_t<double> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::FastTemplate_t<double>));
      static ::ROOT::TGenericClassInfo 
         instance("FastTemplate_t<double>", "HiggsAnalysis/CombinedLimit/interface/FastTemplate.h", 68,
                  typeid(::FastTemplate_t<double>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &FastTemplate_tlEdoublegR_Dictionary, isa_proxy, 4,
                  sizeof(::FastTemplate_t<double>) );
      instance.SetNew(&new_FastTemplate_tlEdoublegR);
      instance.SetNewArray(&newArray_FastTemplate_tlEdoublegR);
      instance.SetDelete(&delete_FastTemplate_tlEdoublegR);
      instance.SetDeleteArray(&deleteArray_FastTemplate_tlEdoublegR);
      instance.SetDestructor(&destruct_FastTemplate_tlEdoublegR);

      ::ROOT::AddClassAlternate("FastTemplate_t<double>","FastTemplate_d");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::FastTemplate_t<double>*)
   {
      return GenerateInitInstanceLocal((::FastTemplate_t<double>*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::FastTemplate_t<double>*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *FastTemplate_tlEdoublegR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::FastTemplate_t<double>*)0x0)->GetClass();
      FastTemplate_tlEdoublegR_TClassManip(theClass);
   return theClass;
   }

   static void FastTemplate_tlEdoublegR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *FastTemplate_tlEfloatgR_Dictionary();
   static void FastTemplate_tlEfloatgR_TClassManip(TClass*);
   static void *new_FastTemplate_tlEfloatgR(void *p = 0);
   static void *newArray_FastTemplate_tlEfloatgR(Long_t size, void *p);
   static void delete_FastTemplate_tlEfloatgR(void *p);
   static void deleteArray_FastTemplate_tlEfloatgR(void *p);
   static void destruct_FastTemplate_tlEfloatgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::FastTemplate_t<float>*)
   {
      ::FastTemplate_t<float> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::FastTemplate_t<float>));
      static ::ROOT::TGenericClassInfo 
         instance("FastTemplate_t<float>", "HiggsAnalysis/CombinedLimit/interface/FastTemplate.h", 68,
                  typeid(::FastTemplate_t<float>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &FastTemplate_tlEfloatgR_Dictionary, isa_proxy, 4,
                  sizeof(::FastTemplate_t<float>) );
      instance.SetNew(&new_FastTemplate_tlEfloatgR);
      instance.SetNewArray(&newArray_FastTemplate_tlEfloatgR);
      instance.SetDelete(&delete_FastTemplate_tlEfloatgR);
      instance.SetDeleteArray(&deleteArray_FastTemplate_tlEfloatgR);
      instance.SetDestructor(&destruct_FastTemplate_tlEfloatgR);

      ::ROOT::AddClassAlternate("FastTemplate_t<float>","FastTemplate_f");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::FastTemplate_t<float>*)
   {
      return GenerateInitInstanceLocal((::FastTemplate_t<float>*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::FastTemplate_t<float>*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *FastTemplate_tlEfloatgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::FastTemplate_t<float>*)0x0)->GetClass();
      FastTemplate_tlEfloatgR_TClassManip(theClass);
   return theClass;
   }

   static void FastTemplate_tlEfloatgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *FastHisto_tlEdoublecOdoublegR_Dictionary();
   static void FastHisto_tlEdoublecOdoublegR_TClassManip(TClass*);
   static void *new_FastHisto_tlEdoublecOdoublegR(void *p = 0);
   static void *newArray_FastHisto_tlEdoublecOdoublegR(Long_t size, void *p);
   static void delete_FastHisto_tlEdoublecOdoublegR(void *p);
   static void deleteArray_FastHisto_tlEdoublecOdoublegR(void *p);
   static void destruct_FastHisto_tlEdoublecOdoublegR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::FastHisto_t<double,double>*)
   {
      ::FastHisto_t<double,double> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::FastHisto_t<double,double>));
      static ::ROOT::TGenericClassInfo 
         instance("FastHisto_t<double,double>", "HiggsAnalysis/CombinedLimit/interface/FastTemplate.h", 139,
                  typeid(::FastHisto_t<double,double>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &FastHisto_tlEdoublecOdoublegR_Dictionary, isa_proxy, 4,
                  sizeof(::FastHisto_t<double,double>) );
      instance.SetNew(&new_FastHisto_tlEdoublecOdoublegR);
      instance.SetNewArray(&newArray_FastHisto_tlEdoublecOdoublegR);
      instance.SetDelete(&delete_FastHisto_tlEdoublecOdoublegR);
      instance.SetDeleteArray(&deleteArray_FastHisto_tlEdoublecOdoublegR);
      instance.SetDestructor(&destruct_FastHisto_tlEdoublecOdoublegR);

      ::ROOT::AddClassAlternate("FastHisto_t<double,double>","FastHisto_d");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::FastHisto_t<double,double>*)
   {
      return GenerateInitInstanceLocal((::FastHisto_t<double,double>*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::FastHisto_t<double,double>*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *FastHisto_tlEdoublecOdoublegR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::FastHisto_t<double,double>*)0x0)->GetClass();
      FastHisto_tlEdoublecOdoublegR_TClassManip(theClass);
   return theClass;
   }

   static void FastHisto_tlEdoublecOdoublegR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *FastHisto_tlEfloatcOdoublegR_Dictionary();
   static void FastHisto_tlEfloatcOdoublegR_TClassManip(TClass*);
   static void *new_FastHisto_tlEfloatcOdoublegR(void *p = 0);
   static void *newArray_FastHisto_tlEfloatcOdoublegR(Long_t size, void *p);
   static void delete_FastHisto_tlEfloatcOdoublegR(void *p);
   static void deleteArray_FastHisto_tlEfloatcOdoublegR(void *p);
   static void destruct_FastHisto_tlEfloatcOdoublegR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::FastHisto_t<float,double>*)
   {
      ::FastHisto_t<float,double> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::FastHisto_t<float,double>));
      static ::ROOT::TGenericClassInfo 
         instance("FastHisto_t<float,double>", "HiggsAnalysis/CombinedLimit/interface/FastTemplate.h", 139,
                  typeid(::FastHisto_t<float,double>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &FastHisto_tlEfloatcOdoublegR_Dictionary, isa_proxy, 4,
                  sizeof(::FastHisto_t<float,double>) );
      instance.SetNew(&new_FastHisto_tlEfloatcOdoublegR);
      instance.SetNewArray(&newArray_FastHisto_tlEfloatcOdoublegR);
      instance.SetDelete(&delete_FastHisto_tlEfloatcOdoublegR);
      instance.SetDeleteArray(&deleteArray_FastHisto_tlEfloatcOdoublegR);
      instance.SetDestructor(&destruct_FastHisto_tlEfloatcOdoublegR);

      ::ROOT::AddClassAlternate("FastHisto_t<float,double>","FastHisto_f");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::FastHisto_t<float,double>*)
   {
      return GenerateInitInstanceLocal((::FastHisto_t<float,double>*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::FastHisto_t<float,double>*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *FastHisto_tlEfloatcOdoublegR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::FastHisto_t<float,double>*)0x0)->GetClass();
      FastHisto_tlEfloatcOdoublegR_TClassManip(theClass);
   return theClass;
   }

   static void FastHisto_tlEfloatcOdoublegR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *FastHisto2D_tlEdoublecOdoublegR_Dictionary();
   static void FastHisto2D_tlEdoublecOdoublegR_TClassManip(TClass*);
   static void *new_FastHisto2D_tlEdoublecOdoublegR(void *p = 0);
   static void *newArray_FastHisto2D_tlEdoublecOdoublegR(Long_t size, void *p);
   static void delete_FastHisto2D_tlEdoublecOdoublegR(void *p);
   static void deleteArray_FastHisto2D_tlEdoublecOdoublegR(void *p);
   static void destruct_FastHisto2D_tlEdoublecOdoublegR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::FastHisto2D_t<double,double>*)
   {
      ::FastHisto2D_t<double,double> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::FastHisto2D_t<double,double>));
      static ::ROOT::TGenericClassInfo 
         instance("FastHisto2D_t<double,double>", "HiggsAnalysis/CombinedLimit/interface/FastTemplate.h", 205,
                  typeid(::FastHisto2D_t<double,double>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &FastHisto2D_tlEdoublecOdoublegR_Dictionary, isa_proxy, 4,
                  sizeof(::FastHisto2D_t<double,double>) );
      instance.SetNew(&new_FastHisto2D_tlEdoublecOdoublegR);
      instance.SetNewArray(&newArray_FastHisto2D_tlEdoublecOdoublegR);
      instance.SetDelete(&delete_FastHisto2D_tlEdoublecOdoublegR);
      instance.SetDeleteArray(&deleteArray_FastHisto2D_tlEdoublecOdoublegR);
      instance.SetDestructor(&destruct_FastHisto2D_tlEdoublecOdoublegR);

      ::ROOT::AddClassAlternate("FastHisto2D_t<double,double>","FastHisto2D_d");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::FastHisto2D_t<double,double>*)
   {
      return GenerateInitInstanceLocal((::FastHisto2D_t<double,double>*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::FastHisto2D_t<double,double>*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *FastHisto2D_tlEdoublecOdoublegR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::FastHisto2D_t<double,double>*)0x0)->GetClass();
      FastHisto2D_tlEdoublecOdoublegR_TClassManip(theClass);
   return theClass;
   }

   static void FastHisto2D_tlEdoublecOdoublegR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *FastHisto2D_tlEfloatcOdoublegR_Dictionary();
   static void FastHisto2D_tlEfloatcOdoublegR_TClassManip(TClass*);
   static void *new_FastHisto2D_tlEfloatcOdoublegR(void *p = 0);
   static void *newArray_FastHisto2D_tlEfloatcOdoublegR(Long_t size, void *p);
   static void delete_FastHisto2D_tlEfloatcOdoublegR(void *p);
   static void deleteArray_FastHisto2D_tlEfloatcOdoublegR(void *p);
   static void destruct_FastHisto2D_tlEfloatcOdoublegR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::FastHisto2D_t<float,double>*)
   {
      ::FastHisto2D_t<float,double> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::FastHisto2D_t<float,double>));
      static ::ROOT::TGenericClassInfo 
         instance("FastHisto2D_t<float,double>", "HiggsAnalysis/CombinedLimit/interface/FastTemplate.h", 205,
                  typeid(::FastHisto2D_t<float,double>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &FastHisto2D_tlEfloatcOdoublegR_Dictionary, isa_proxy, 4,
                  sizeof(::FastHisto2D_t<float,double>) );
      instance.SetNew(&new_FastHisto2D_tlEfloatcOdoublegR);
      instance.SetNewArray(&newArray_FastHisto2D_tlEfloatcOdoublegR);
      instance.SetDelete(&delete_FastHisto2D_tlEfloatcOdoublegR);
      instance.SetDeleteArray(&deleteArray_FastHisto2D_tlEfloatcOdoublegR);
      instance.SetDestructor(&destruct_FastHisto2D_tlEfloatcOdoublegR);

      ::ROOT::AddClassAlternate("FastHisto2D_t<float,double>","FastHisto2D_f");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::FastHisto2D_t<float,double>*)
   {
      return GenerateInitInstanceLocal((::FastHisto2D_t<float,double>*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::FastHisto2D_t<float,double>*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *FastHisto2D_tlEfloatcOdoublegR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::FastHisto2D_t<float,double>*)0x0)->GetClass();
      FastHisto2D_tlEfloatcOdoublegR_TClassManip(theClass);
   return theClass;
   }

   static void FastHisto2D_tlEfloatcOdoublegR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *FastHisto3D_tlEdoublecOdoublegR_Dictionary();
   static void FastHisto3D_tlEdoublecOdoublegR_TClassManip(TClass*);
   static void *new_FastHisto3D_tlEdoublecOdoublegR(void *p = 0);
   static void *newArray_FastHisto3D_tlEdoublecOdoublegR(Long_t size, void *p);
   static void delete_FastHisto3D_tlEdoublecOdoublegR(void *p);
   static void deleteArray_FastHisto3D_tlEdoublecOdoublegR(void *p);
   static void destruct_FastHisto3D_tlEdoublecOdoublegR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::FastHisto3D_t<double,double>*)
   {
      ::FastHisto3D_t<double,double> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::FastHisto3D_t<double,double>));
      static ::ROOT::TGenericClassInfo 
         instance("FastHisto3D_t<double,double>", "HiggsAnalysis/CombinedLimit/interface/FastTemplate.h", 292,
                  typeid(::FastHisto3D_t<double,double>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &FastHisto3D_tlEdoublecOdoublegR_Dictionary, isa_proxy, 4,
                  sizeof(::FastHisto3D_t<double,double>) );
      instance.SetNew(&new_FastHisto3D_tlEdoublecOdoublegR);
      instance.SetNewArray(&newArray_FastHisto3D_tlEdoublecOdoublegR);
      instance.SetDelete(&delete_FastHisto3D_tlEdoublecOdoublegR);
      instance.SetDeleteArray(&deleteArray_FastHisto3D_tlEdoublecOdoublegR);
      instance.SetDestructor(&destruct_FastHisto3D_tlEdoublecOdoublegR);

      ::ROOT::AddClassAlternate("FastHisto3D_t<double,double>","FastHisto3D_d");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::FastHisto3D_t<double,double>*)
   {
      return GenerateInitInstanceLocal((::FastHisto3D_t<double,double>*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::FastHisto3D_t<double,double>*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *FastHisto3D_tlEdoublecOdoublegR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::FastHisto3D_t<double,double>*)0x0)->GetClass();
      FastHisto3D_tlEdoublecOdoublegR_TClassManip(theClass);
   return theClass;
   }

   static void FastHisto3D_tlEdoublecOdoublegR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *FastHisto3D_tlEfloatcOdoublegR_Dictionary();
   static void FastHisto3D_tlEfloatcOdoublegR_TClassManip(TClass*);
   static void *new_FastHisto3D_tlEfloatcOdoublegR(void *p = 0);
   static void *newArray_FastHisto3D_tlEfloatcOdoublegR(Long_t size, void *p);
   static void delete_FastHisto3D_tlEfloatcOdoublegR(void *p);
   static void deleteArray_FastHisto3D_tlEfloatcOdoublegR(void *p);
   static void destruct_FastHisto3D_tlEfloatcOdoublegR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::FastHisto3D_t<float,double>*)
   {
      ::FastHisto3D_t<float,double> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::FastHisto3D_t<float,double>));
      static ::ROOT::TGenericClassInfo 
         instance("FastHisto3D_t<float,double>", "HiggsAnalysis/CombinedLimit/interface/FastTemplate.h", 292,
                  typeid(::FastHisto3D_t<float,double>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &FastHisto3D_tlEfloatcOdoublegR_Dictionary, isa_proxy, 4,
                  sizeof(::FastHisto3D_t<float,double>) );
      instance.SetNew(&new_FastHisto3D_tlEfloatcOdoublegR);
      instance.SetNewArray(&newArray_FastHisto3D_tlEfloatcOdoublegR);
      instance.SetDelete(&delete_FastHisto3D_tlEfloatcOdoublegR);
      instance.SetDeleteArray(&deleteArray_FastHisto3D_tlEfloatcOdoublegR);
      instance.SetDestructor(&destruct_FastHisto3D_tlEfloatcOdoublegR);

      ::ROOT::AddClassAlternate("FastHisto3D_t<float,double>","FastHisto3D_f");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::FastHisto3D_t<float,double>*)
   {
      return GenerateInitInstanceLocal((::FastHisto3D_t<float,double>*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::FastHisto3D_t<float,double>*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *FastHisto3D_tlEfloatcOdoublegR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::FastHisto3D_t<float,double>*)0x0)->GetClass();
      FastHisto3D_tlEfloatcOdoublegR_TClassManip(theClass);
   return theClass;
   }

   static void FastHisto3D_tlEfloatcOdoublegR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *FastTemplateFunc_tlEfloatgR_Dictionary();
   static void FastTemplateFunc_tlEfloatgR_TClassManip(TClass*);
   static void delete_FastTemplateFunc_tlEfloatgR(void *p);
   static void deleteArray_FastTemplateFunc_tlEfloatgR(void *p);
   static void destruct_FastTemplateFunc_tlEfloatgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::FastTemplateFunc_t<float>*)
   {
      ::FastTemplateFunc_t<float> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::FastTemplateFunc_t<float> >(0);
      static ::ROOT::TGenericClassInfo 
         instance("FastTemplateFunc_t<float>", ::FastTemplateFunc_t<float>::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/FastTemplateFunc.h", 11,
                  typeid(::FastTemplateFunc_t<float>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &FastTemplateFunc_tlEfloatgR_Dictionary, isa_proxy, 4,
                  sizeof(::FastTemplateFunc_t<float>) );
      instance.SetDelete(&delete_FastTemplateFunc_tlEfloatgR);
      instance.SetDeleteArray(&deleteArray_FastTemplateFunc_tlEfloatgR);
      instance.SetDestructor(&destruct_FastTemplateFunc_tlEfloatgR);

      ::ROOT::AddClassAlternate("FastTemplateFunc_t<float>","FastTemplateFunc_f");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::FastTemplateFunc_t<float>*)
   {
      return GenerateInitInstanceLocal((::FastTemplateFunc_t<float>*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::FastTemplateFunc_t<float>*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *FastTemplateFunc_tlEfloatgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::FastTemplateFunc_t<float>*)0x0)->GetClass();
      FastTemplateFunc_tlEfloatgR_TClassManip(theClass);
   return theClass;
   }

   static void FastTemplateFunc_tlEfloatgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *FastTemplateFunc_tlEdoublegR_Dictionary();
   static void FastTemplateFunc_tlEdoublegR_TClassManip(TClass*);
   static void delete_FastTemplateFunc_tlEdoublegR(void *p);
   static void deleteArray_FastTemplateFunc_tlEdoublegR(void *p);
   static void destruct_FastTemplateFunc_tlEdoublegR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::FastTemplateFunc_t<double>*)
   {
      ::FastTemplateFunc_t<double> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::FastTemplateFunc_t<double> >(0);
      static ::ROOT::TGenericClassInfo 
         instance("FastTemplateFunc_t<double>", ::FastTemplateFunc_t<double>::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/FastTemplateFunc.h", 11,
                  typeid(::FastTemplateFunc_t<double>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &FastTemplateFunc_tlEdoublegR_Dictionary, isa_proxy, 4,
                  sizeof(::FastTemplateFunc_t<double>) );
      instance.SetDelete(&delete_FastTemplateFunc_tlEdoublegR);
      instance.SetDeleteArray(&deleteArray_FastTemplateFunc_tlEdoublegR);
      instance.SetDestructor(&destruct_FastTemplateFunc_tlEdoublegR);

      ::ROOT::AddClassAlternate("FastTemplateFunc_t<double>","FastTemplateFunc_d");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::FastTemplateFunc_t<double>*)
   {
      return GenerateInitInstanceLocal((::FastTemplateFunc_t<double>*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::FastTemplateFunc_t<double>*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *FastTemplateFunc_tlEdoublegR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::FastTemplateFunc_t<double>*)0x0)->GetClass();
      FastTemplateFunc_tlEdoublegR_TClassManip(theClass);
   return theClass;
   }

   static void FastTemplateFunc_tlEdoublegR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *FastHistoFunc_tlEfloatcOdoublegR_Dictionary();
   static void FastHistoFunc_tlEfloatcOdoublegR_TClassManip(TClass*);
   static void *new_FastHistoFunc_tlEfloatcOdoublegR(void *p = 0);
   static void *newArray_FastHistoFunc_tlEfloatcOdoublegR(Long_t size, void *p);
   static void delete_FastHistoFunc_tlEfloatcOdoublegR(void *p);
   static void deleteArray_FastHistoFunc_tlEfloatcOdoublegR(void *p);
   static void destruct_FastHistoFunc_tlEfloatcOdoublegR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::FastHistoFunc_t<float,double>*)
   {
      ::FastHistoFunc_t<float,double> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::FastHistoFunc_t<float,double> >(0);
      static ::ROOT::TGenericClassInfo 
         instance("FastHistoFunc_t<float,double>", ::FastHistoFunc_t<float,double>::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/FastTemplateFunc.h", 45,
                  typeid(::FastHistoFunc_t<float,double>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &FastHistoFunc_tlEfloatcOdoublegR_Dictionary, isa_proxy, 4,
                  sizeof(::FastHistoFunc_t<float,double>) );
      instance.SetNew(&new_FastHistoFunc_tlEfloatcOdoublegR);
      instance.SetNewArray(&newArray_FastHistoFunc_tlEfloatcOdoublegR);
      instance.SetDelete(&delete_FastHistoFunc_tlEfloatcOdoublegR);
      instance.SetDeleteArray(&deleteArray_FastHistoFunc_tlEfloatcOdoublegR);
      instance.SetDestructor(&destruct_FastHistoFunc_tlEfloatcOdoublegR);

      ::ROOT::AddClassAlternate("FastHistoFunc_t<float,double>","FastHistoFunc_f");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::FastHistoFunc_t<float,double>*)
   {
      return GenerateInitInstanceLocal((::FastHistoFunc_t<float,double>*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::FastHistoFunc_t<float,double>*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *FastHistoFunc_tlEfloatcOdoublegR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::FastHistoFunc_t<float,double>*)0x0)->GetClass();
      FastHistoFunc_tlEfloatcOdoublegR_TClassManip(theClass);
   return theClass;
   }

   static void FastHistoFunc_tlEfloatcOdoublegR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *FastHistoFunc_tlEdoublecOdoublegR_Dictionary();
   static void FastHistoFunc_tlEdoublecOdoublegR_TClassManip(TClass*);
   static void *new_FastHistoFunc_tlEdoublecOdoublegR(void *p = 0);
   static void *newArray_FastHistoFunc_tlEdoublecOdoublegR(Long_t size, void *p);
   static void delete_FastHistoFunc_tlEdoublecOdoublegR(void *p);
   static void deleteArray_FastHistoFunc_tlEdoublecOdoublegR(void *p);
   static void destruct_FastHistoFunc_tlEdoublecOdoublegR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::FastHistoFunc_t<double,double>*)
   {
      ::FastHistoFunc_t<double,double> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::FastHistoFunc_t<double,double> >(0);
      static ::ROOT::TGenericClassInfo 
         instance("FastHistoFunc_t<double,double>", ::FastHistoFunc_t<double,double>::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/FastTemplateFunc.h", 45,
                  typeid(::FastHistoFunc_t<double,double>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &FastHistoFunc_tlEdoublecOdoublegR_Dictionary, isa_proxy, 4,
                  sizeof(::FastHistoFunc_t<double,double>) );
      instance.SetNew(&new_FastHistoFunc_tlEdoublecOdoublegR);
      instance.SetNewArray(&newArray_FastHistoFunc_tlEdoublecOdoublegR);
      instance.SetDelete(&delete_FastHistoFunc_tlEdoublecOdoublegR);
      instance.SetDeleteArray(&deleteArray_FastHistoFunc_tlEdoublecOdoublegR);
      instance.SetDestructor(&destruct_FastHistoFunc_tlEdoublecOdoublegR);

      ::ROOT::AddClassAlternate("FastHistoFunc_t<double,double>","FastHistoFunc_d");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::FastHistoFunc_t<double,double>*)
   {
      return GenerateInitInstanceLocal((::FastHistoFunc_t<double,double>*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::FastHistoFunc_t<double,double>*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *FastHistoFunc_tlEdoublecOdoublegR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::FastHistoFunc_t<double,double>*)0x0)->GetClass();
      FastHistoFunc_tlEdoublecOdoublegR_TClassManip(theClass);
   return theClass;
   }

   static void FastHistoFunc_tlEdoublecOdoublegR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *FastHisto2DFunc_tlEfloatcOdoublegR_Dictionary();
   static void FastHisto2DFunc_tlEfloatcOdoublegR_TClassManip(TClass*);
   static void *new_FastHisto2DFunc_tlEfloatcOdoublegR(void *p = 0);
   static void *newArray_FastHisto2DFunc_tlEfloatcOdoublegR(Long_t size, void *p);
   static void delete_FastHisto2DFunc_tlEfloatcOdoublegR(void *p);
   static void deleteArray_FastHisto2DFunc_tlEfloatcOdoublegR(void *p);
   static void destruct_FastHisto2DFunc_tlEfloatcOdoublegR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::FastHisto2DFunc_t<float,double>*)
   {
      ::FastHisto2DFunc_t<float,double> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::FastHisto2DFunc_t<float,double> >(0);
      static ::ROOT::TGenericClassInfo 
         instance("FastHisto2DFunc_t<float,double>", ::FastHisto2DFunc_t<float,double>::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/FastTemplateFunc.h", 106,
                  typeid(::FastHisto2DFunc_t<float,double>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &FastHisto2DFunc_tlEfloatcOdoublegR_Dictionary, isa_proxy, 4,
                  sizeof(::FastHisto2DFunc_t<float,double>) );
      instance.SetNew(&new_FastHisto2DFunc_tlEfloatcOdoublegR);
      instance.SetNewArray(&newArray_FastHisto2DFunc_tlEfloatcOdoublegR);
      instance.SetDelete(&delete_FastHisto2DFunc_tlEfloatcOdoublegR);
      instance.SetDeleteArray(&deleteArray_FastHisto2DFunc_tlEfloatcOdoublegR);
      instance.SetDestructor(&destruct_FastHisto2DFunc_tlEfloatcOdoublegR);

      ::ROOT::AddClassAlternate("FastHisto2DFunc_t<float,double>","FastHisto2DFunc_f");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::FastHisto2DFunc_t<float,double>*)
   {
      return GenerateInitInstanceLocal((::FastHisto2DFunc_t<float,double>*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::FastHisto2DFunc_t<float,double>*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *FastHisto2DFunc_tlEfloatcOdoublegR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::FastHisto2DFunc_t<float,double>*)0x0)->GetClass();
      FastHisto2DFunc_tlEfloatcOdoublegR_TClassManip(theClass);
   return theClass;
   }

   static void FastHisto2DFunc_tlEfloatcOdoublegR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *FastHisto2DFunc_tlEdoublecOdoublegR_Dictionary();
   static void FastHisto2DFunc_tlEdoublecOdoublegR_TClassManip(TClass*);
   static void *new_FastHisto2DFunc_tlEdoublecOdoublegR(void *p = 0);
   static void *newArray_FastHisto2DFunc_tlEdoublecOdoublegR(Long_t size, void *p);
   static void delete_FastHisto2DFunc_tlEdoublecOdoublegR(void *p);
   static void deleteArray_FastHisto2DFunc_tlEdoublecOdoublegR(void *p);
   static void destruct_FastHisto2DFunc_tlEdoublecOdoublegR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::FastHisto2DFunc_t<double,double>*)
   {
      ::FastHisto2DFunc_t<double,double> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::FastHisto2DFunc_t<double,double> >(0);
      static ::ROOT::TGenericClassInfo 
         instance("FastHisto2DFunc_t<double,double>", ::FastHisto2DFunc_t<double,double>::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/FastTemplateFunc.h", 106,
                  typeid(::FastHisto2DFunc_t<double,double>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &FastHisto2DFunc_tlEdoublecOdoublegR_Dictionary, isa_proxy, 4,
                  sizeof(::FastHisto2DFunc_t<double,double>) );
      instance.SetNew(&new_FastHisto2DFunc_tlEdoublecOdoublegR);
      instance.SetNewArray(&newArray_FastHisto2DFunc_tlEdoublecOdoublegR);
      instance.SetDelete(&delete_FastHisto2DFunc_tlEdoublecOdoublegR);
      instance.SetDeleteArray(&deleteArray_FastHisto2DFunc_tlEdoublecOdoublegR);
      instance.SetDestructor(&destruct_FastHisto2DFunc_tlEdoublecOdoublegR);

      ::ROOT::AddClassAlternate("FastHisto2DFunc_t<double,double>","FastHisto2DFunc_d");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::FastHisto2DFunc_t<double,double>*)
   {
      return GenerateInitInstanceLocal((::FastHisto2DFunc_t<double,double>*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::FastHisto2DFunc_t<double,double>*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *FastHisto2DFunc_tlEdoublecOdoublegR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::FastHisto2DFunc_t<double,double>*)0x0)->GetClass();
      FastHisto2DFunc_tlEdoublecOdoublegR_TClassManip(theClass);
   return theClass;
   }

   static void FastHisto2DFunc_tlEdoublecOdoublegR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *FastHisto3DFunc_tlEfloatcOdoublegR_Dictionary();
   static void FastHisto3DFunc_tlEfloatcOdoublegR_TClassManip(TClass*);
   static void *new_FastHisto3DFunc_tlEfloatcOdoublegR(void *p = 0);
   static void *newArray_FastHisto3DFunc_tlEfloatcOdoublegR(Long_t size, void *p);
   static void delete_FastHisto3DFunc_tlEfloatcOdoublegR(void *p);
   static void deleteArray_FastHisto3DFunc_tlEfloatcOdoublegR(void *p);
   static void destruct_FastHisto3DFunc_tlEfloatcOdoublegR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::FastHisto3DFunc_t<float,double>*)
   {
      ::FastHisto3DFunc_t<float,double> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::FastHisto3DFunc_t<float,double> >(0);
      static ::ROOT::TGenericClassInfo 
         instance("FastHisto3DFunc_t<float,double>", ::FastHisto3DFunc_t<float,double>::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/FastTemplateFunc.h", 198,
                  typeid(::FastHisto3DFunc_t<float,double>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &FastHisto3DFunc_tlEfloatcOdoublegR_Dictionary, isa_proxy, 4,
                  sizeof(::FastHisto3DFunc_t<float,double>) );
      instance.SetNew(&new_FastHisto3DFunc_tlEfloatcOdoublegR);
      instance.SetNewArray(&newArray_FastHisto3DFunc_tlEfloatcOdoublegR);
      instance.SetDelete(&delete_FastHisto3DFunc_tlEfloatcOdoublegR);
      instance.SetDeleteArray(&deleteArray_FastHisto3DFunc_tlEfloatcOdoublegR);
      instance.SetDestructor(&destruct_FastHisto3DFunc_tlEfloatcOdoublegR);

      ::ROOT::AddClassAlternate("FastHisto3DFunc_t<float,double>","FastHisto3DFunc_f");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::FastHisto3DFunc_t<float,double>*)
   {
      return GenerateInitInstanceLocal((::FastHisto3DFunc_t<float,double>*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::FastHisto3DFunc_t<float,double>*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *FastHisto3DFunc_tlEfloatcOdoublegR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::FastHisto3DFunc_t<float,double>*)0x0)->GetClass();
      FastHisto3DFunc_tlEfloatcOdoublegR_TClassManip(theClass);
   return theClass;
   }

   static void FastHisto3DFunc_tlEfloatcOdoublegR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *FastHisto3DFunc_tlEdoublecOdoublegR_Dictionary();
   static void FastHisto3DFunc_tlEdoublecOdoublegR_TClassManip(TClass*);
   static void *new_FastHisto3DFunc_tlEdoublecOdoublegR(void *p = 0);
   static void *newArray_FastHisto3DFunc_tlEdoublecOdoublegR(Long_t size, void *p);
   static void delete_FastHisto3DFunc_tlEdoublecOdoublegR(void *p);
   static void deleteArray_FastHisto3DFunc_tlEdoublecOdoublegR(void *p);
   static void destruct_FastHisto3DFunc_tlEdoublecOdoublegR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::FastHisto3DFunc_t<double,double>*)
   {
      ::FastHisto3DFunc_t<double,double> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::FastHisto3DFunc_t<double,double> >(0);
      static ::ROOT::TGenericClassInfo 
         instance("FastHisto3DFunc_t<double,double>", ::FastHisto3DFunc_t<double,double>::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/FastTemplateFunc.h", 198,
                  typeid(::FastHisto3DFunc_t<double,double>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &FastHisto3DFunc_tlEdoublecOdoublegR_Dictionary, isa_proxy, 4,
                  sizeof(::FastHisto3DFunc_t<double,double>) );
      instance.SetNew(&new_FastHisto3DFunc_tlEdoublecOdoublegR);
      instance.SetNewArray(&newArray_FastHisto3DFunc_tlEdoublecOdoublegR);
      instance.SetDelete(&delete_FastHisto3DFunc_tlEdoublecOdoublegR);
      instance.SetDeleteArray(&deleteArray_FastHisto3DFunc_tlEdoublecOdoublegR);
      instance.SetDestructor(&destruct_FastHisto3DFunc_tlEdoublecOdoublegR);

      ::ROOT::AddClassAlternate("FastHisto3DFunc_t<double,double>","FastHisto3DFunc_d");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::FastHisto3DFunc_t<double,double>*)
   {
      return GenerateInitInstanceLocal((::FastHisto3DFunc_t<double,double>*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::FastHisto3DFunc_t<double,double>*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *FastHisto3DFunc_tlEdoublecOdoublegR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::FastHisto3DFunc_t<double,double>*)0x0)->GetClass();
      FastHisto3DFunc_tlEdoublecOdoublegR_TClassManip(theClass);
   return theClass;
   }

   static void FastHisto3DFunc_tlEdoublecOdoublegR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static void *new_HZZ4L_RooSpinZeroPdf(void *p = 0);
   static void *newArray_HZZ4L_RooSpinZeroPdf(Long_t size, void *p);
   static void delete_HZZ4L_RooSpinZeroPdf(void *p);
   static void deleteArray_HZZ4L_RooSpinZeroPdf(void *p);
   static void destruct_HZZ4L_RooSpinZeroPdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::HZZ4L_RooSpinZeroPdf*)
   {
      ::HZZ4L_RooSpinZeroPdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::HZZ4L_RooSpinZeroPdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("HZZ4L_RooSpinZeroPdf", ::HZZ4L_RooSpinZeroPdf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4L_RooSpinZeroPdf.h", 21,
                  typeid(::HZZ4L_RooSpinZeroPdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::HZZ4L_RooSpinZeroPdf::Dictionary, isa_proxy, 4,
                  sizeof(::HZZ4L_RooSpinZeroPdf) );
      instance.SetNew(&new_HZZ4L_RooSpinZeroPdf);
      instance.SetNewArray(&newArray_HZZ4L_RooSpinZeroPdf);
      instance.SetDelete(&delete_HZZ4L_RooSpinZeroPdf);
      instance.SetDeleteArray(&deleteArray_HZZ4L_RooSpinZeroPdf);
      instance.SetDestructor(&destruct_HZZ4L_RooSpinZeroPdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::HZZ4L_RooSpinZeroPdf*)
   {
      return GenerateInitInstanceLocal((::HZZ4L_RooSpinZeroPdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::HZZ4L_RooSpinZeroPdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_HZZ4L_RooSpinZeroPdf_1D(void *p = 0);
   static void *newArray_HZZ4L_RooSpinZeroPdf_1D(Long_t size, void *p);
   static void delete_HZZ4L_RooSpinZeroPdf_1D(void *p);
   static void deleteArray_HZZ4L_RooSpinZeroPdf_1D(void *p);
   static void destruct_HZZ4L_RooSpinZeroPdf_1D(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::HZZ4L_RooSpinZeroPdf_1D*)
   {
      ::HZZ4L_RooSpinZeroPdf_1D *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::HZZ4L_RooSpinZeroPdf_1D >(0);
      static ::ROOT::TGenericClassInfo 
         instance("HZZ4L_RooSpinZeroPdf_1D", ::HZZ4L_RooSpinZeroPdf_1D::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4L_RooSpinZeroPdf_1D.h", 22,
                  typeid(::HZZ4L_RooSpinZeroPdf_1D), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::HZZ4L_RooSpinZeroPdf_1D::Dictionary, isa_proxy, 4,
                  sizeof(::HZZ4L_RooSpinZeroPdf_1D) );
      instance.SetNew(&new_HZZ4L_RooSpinZeroPdf_1D);
      instance.SetNewArray(&newArray_HZZ4L_RooSpinZeroPdf_1D);
      instance.SetDelete(&delete_HZZ4L_RooSpinZeroPdf_1D);
      instance.SetDeleteArray(&deleteArray_HZZ4L_RooSpinZeroPdf_1D);
      instance.SetDestructor(&destruct_HZZ4L_RooSpinZeroPdf_1D);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::HZZ4L_RooSpinZeroPdf_1D*)
   {
      return GenerateInitInstanceLocal((::HZZ4L_RooSpinZeroPdf_1D*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::HZZ4L_RooSpinZeroPdf_1D*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_HZZ4L_RooSpinZeroPdf_2D(void *p = 0);
   static void *newArray_HZZ4L_RooSpinZeroPdf_2D(Long_t size, void *p);
   static void delete_HZZ4L_RooSpinZeroPdf_2D(void *p);
   static void deleteArray_HZZ4L_RooSpinZeroPdf_2D(void *p);
   static void destruct_HZZ4L_RooSpinZeroPdf_2D(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::HZZ4L_RooSpinZeroPdf_2D*)
   {
      ::HZZ4L_RooSpinZeroPdf_2D *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::HZZ4L_RooSpinZeroPdf_2D >(0);
      static ::ROOT::TGenericClassInfo 
         instance("HZZ4L_RooSpinZeroPdf_2D", ::HZZ4L_RooSpinZeroPdf_2D::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4L_RooSpinZeroPdf_2D.h", 24,
                  typeid(::HZZ4L_RooSpinZeroPdf_2D), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::HZZ4L_RooSpinZeroPdf_2D::Dictionary, isa_proxy, 4,
                  sizeof(::HZZ4L_RooSpinZeroPdf_2D) );
      instance.SetNew(&new_HZZ4L_RooSpinZeroPdf_2D);
      instance.SetNewArray(&newArray_HZZ4L_RooSpinZeroPdf_2D);
      instance.SetDelete(&delete_HZZ4L_RooSpinZeroPdf_2D);
      instance.SetDeleteArray(&deleteArray_HZZ4L_RooSpinZeroPdf_2D);
      instance.SetDestructor(&destruct_HZZ4L_RooSpinZeroPdf_2D);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::HZZ4L_RooSpinZeroPdf_2D*)
   {
      return GenerateInitInstanceLocal((::HZZ4L_RooSpinZeroPdf_2D*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::HZZ4L_RooSpinZeroPdf_2D*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_HZZ4L_RooSpinZeroPdf_phase(void *p = 0);
   static void *newArray_HZZ4L_RooSpinZeroPdf_phase(Long_t size, void *p);
   static void delete_HZZ4L_RooSpinZeroPdf_phase(void *p);
   static void deleteArray_HZZ4L_RooSpinZeroPdf_phase(void *p);
   static void destruct_HZZ4L_RooSpinZeroPdf_phase(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::HZZ4L_RooSpinZeroPdf_phase*)
   {
      ::HZZ4L_RooSpinZeroPdf_phase *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::HZZ4L_RooSpinZeroPdf_phase >(0);
      static ::ROOT::TGenericClassInfo 
         instance("HZZ4L_RooSpinZeroPdf_phase", ::HZZ4L_RooSpinZeroPdf_phase::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4L_RooSpinZeroPdf_phase.h", 21,
                  typeid(::HZZ4L_RooSpinZeroPdf_phase), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::HZZ4L_RooSpinZeroPdf_phase::Dictionary, isa_proxy, 4,
                  sizeof(::HZZ4L_RooSpinZeroPdf_phase) );
      instance.SetNew(&new_HZZ4L_RooSpinZeroPdf_phase);
      instance.SetNewArray(&newArray_HZZ4L_RooSpinZeroPdf_phase);
      instance.SetDelete(&delete_HZZ4L_RooSpinZeroPdf_phase);
      instance.SetDeleteArray(&deleteArray_HZZ4L_RooSpinZeroPdf_phase);
      instance.SetDestructor(&destruct_HZZ4L_RooSpinZeroPdf_phase);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::HZZ4L_RooSpinZeroPdf_phase*)
   {
      return GenerateInitInstanceLocal((::HZZ4L_RooSpinZeroPdf_phase*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::HZZ4L_RooSpinZeroPdf_phase*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_VBFHZZ4L_RooSpinZeroPdf(void *p = 0);
   static void *newArray_VBFHZZ4L_RooSpinZeroPdf(Long_t size, void *p);
   static void delete_VBFHZZ4L_RooSpinZeroPdf(void *p);
   static void deleteArray_VBFHZZ4L_RooSpinZeroPdf(void *p);
   static void destruct_VBFHZZ4L_RooSpinZeroPdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::VBFHZZ4L_RooSpinZeroPdf*)
   {
      ::VBFHZZ4L_RooSpinZeroPdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::VBFHZZ4L_RooSpinZeroPdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("VBFHZZ4L_RooSpinZeroPdf", ::VBFHZZ4L_RooSpinZeroPdf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/VBFHZZ4L_RooSpinZeroPdf.h", 24,
                  typeid(::VBFHZZ4L_RooSpinZeroPdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::VBFHZZ4L_RooSpinZeroPdf::Dictionary, isa_proxy, 4,
                  sizeof(::VBFHZZ4L_RooSpinZeroPdf) );
      instance.SetNew(&new_VBFHZZ4L_RooSpinZeroPdf);
      instance.SetNewArray(&newArray_VBFHZZ4L_RooSpinZeroPdf);
      instance.SetDelete(&delete_VBFHZZ4L_RooSpinZeroPdf);
      instance.SetDeleteArray(&deleteArray_VBFHZZ4L_RooSpinZeroPdf);
      instance.SetDestructor(&destruct_VBFHZZ4L_RooSpinZeroPdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::VBFHZZ4L_RooSpinZeroPdf*)
   {
      return GenerateInitInstanceLocal((::VBFHZZ4L_RooSpinZeroPdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::VBFHZZ4L_RooSpinZeroPdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_VBFHZZ4L_RooSpinZeroPdf_fast(void *p = 0);
   static void *newArray_VBFHZZ4L_RooSpinZeroPdf_fast(Long_t size, void *p);
   static void delete_VBFHZZ4L_RooSpinZeroPdf_fast(void *p);
   static void deleteArray_VBFHZZ4L_RooSpinZeroPdf_fast(void *p);
   static void destruct_VBFHZZ4L_RooSpinZeroPdf_fast(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::VBFHZZ4L_RooSpinZeroPdf_fast*)
   {
      ::VBFHZZ4L_RooSpinZeroPdf_fast *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::VBFHZZ4L_RooSpinZeroPdf_fast >(0);
      static ::ROOT::TGenericClassInfo 
         instance("VBFHZZ4L_RooSpinZeroPdf_fast", ::VBFHZZ4L_RooSpinZeroPdf_fast::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/VBFHZZ4L_RooSpinZeroPdf_fast.h", 12,
                  typeid(::VBFHZZ4L_RooSpinZeroPdf_fast), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::VBFHZZ4L_RooSpinZeroPdf_fast::Dictionary, isa_proxy, 4,
                  sizeof(::VBFHZZ4L_RooSpinZeroPdf_fast) );
      instance.SetNew(&new_VBFHZZ4L_RooSpinZeroPdf_fast);
      instance.SetNewArray(&newArray_VBFHZZ4L_RooSpinZeroPdf_fast);
      instance.SetDelete(&delete_VBFHZZ4L_RooSpinZeroPdf_fast);
      instance.SetDeleteArray(&deleteArray_VBFHZZ4L_RooSpinZeroPdf_fast);
      instance.SetDestructor(&destruct_VBFHZZ4L_RooSpinZeroPdf_fast);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::VBFHZZ4L_RooSpinZeroPdf_fast*)
   {
      return GenerateInitInstanceLocal((::VBFHZZ4L_RooSpinZeroPdf_fast*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::VBFHZZ4L_RooSpinZeroPdf_fast*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_HZZ4L_RooSpinZeroPdf_1D_fast(void *p = 0);
   static void *newArray_HZZ4L_RooSpinZeroPdf_1D_fast(Long_t size, void *p);
   static void delete_HZZ4L_RooSpinZeroPdf_1D_fast(void *p);
   static void deleteArray_HZZ4L_RooSpinZeroPdf_1D_fast(void *p);
   static void destruct_HZZ4L_RooSpinZeroPdf_1D_fast(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::HZZ4L_RooSpinZeroPdf_1D_fast*)
   {
      ::HZZ4L_RooSpinZeroPdf_1D_fast *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::HZZ4L_RooSpinZeroPdf_1D_fast >(0);
      static ::ROOT::TGenericClassInfo 
         instance("HZZ4L_RooSpinZeroPdf_1D_fast", ::HZZ4L_RooSpinZeroPdf_1D_fast::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4L_RooSpinZeroPdf_1D_fast.h", 12,
                  typeid(::HZZ4L_RooSpinZeroPdf_1D_fast), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::HZZ4L_RooSpinZeroPdf_1D_fast::Dictionary, isa_proxy, 4,
                  sizeof(::HZZ4L_RooSpinZeroPdf_1D_fast) );
      instance.SetNew(&new_HZZ4L_RooSpinZeroPdf_1D_fast);
      instance.SetNewArray(&newArray_HZZ4L_RooSpinZeroPdf_1D_fast);
      instance.SetDelete(&delete_HZZ4L_RooSpinZeroPdf_1D_fast);
      instance.SetDeleteArray(&deleteArray_HZZ4L_RooSpinZeroPdf_1D_fast);
      instance.SetDestructor(&destruct_HZZ4L_RooSpinZeroPdf_1D_fast);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::HZZ4L_RooSpinZeroPdf_1D_fast*)
   {
      return GenerateInitInstanceLocal((::HZZ4L_RooSpinZeroPdf_1D_fast*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::HZZ4L_RooSpinZeroPdf_1D_fast*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_HZZ4L_RooSpinZeroPdf_2D_fast(void *p = 0);
   static void *newArray_HZZ4L_RooSpinZeroPdf_2D_fast(Long_t size, void *p);
   static void delete_HZZ4L_RooSpinZeroPdf_2D_fast(void *p);
   static void deleteArray_HZZ4L_RooSpinZeroPdf_2D_fast(void *p);
   static void destruct_HZZ4L_RooSpinZeroPdf_2D_fast(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::HZZ4L_RooSpinZeroPdf_2D_fast*)
   {
      ::HZZ4L_RooSpinZeroPdf_2D_fast *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::HZZ4L_RooSpinZeroPdf_2D_fast >(0);
      static ::ROOT::TGenericClassInfo 
         instance("HZZ4L_RooSpinZeroPdf_2D_fast", ::HZZ4L_RooSpinZeroPdf_2D_fast::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4L_RooSpinZeroPdf_2D_fast.h", 12,
                  typeid(::HZZ4L_RooSpinZeroPdf_2D_fast), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::HZZ4L_RooSpinZeroPdf_2D_fast::Dictionary, isa_proxy, 4,
                  sizeof(::HZZ4L_RooSpinZeroPdf_2D_fast) );
      instance.SetNew(&new_HZZ4L_RooSpinZeroPdf_2D_fast);
      instance.SetNewArray(&newArray_HZZ4L_RooSpinZeroPdf_2D_fast);
      instance.SetDelete(&delete_HZZ4L_RooSpinZeroPdf_2D_fast);
      instance.SetDeleteArray(&deleteArray_HZZ4L_RooSpinZeroPdf_2D_fast);
      instance.SetDestructor(&destruct_HZZ4L_RooSpinZeroPdf_2D_fast);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::HZZ4L_RooSpinZeroPdf_2D_fast*)
   {
      return GenerateInitInstanceLocal((::HZZ4L_RooSpinZeroPdf_2D_fast*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::HZZ4L_RooSpinZeroPdf_2D_fast*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_HZZ4L_RooSpinZeroPdf_phase_fast(void *p = 0);
   static void *newArray_HZZ4L_RooSpinZeroPdf_phase_fast(Long_t size, void *p);
   static void delete_HZZ4L_RooSpinZeroPdf_phase_fast(void *p);
   static void deleteArray_HZZ4L_RooSpinZeroPdf_phase_fast(void *p);
   static void destruct_HZZ4L_RooSpinZeroPdf_phase_fast(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::HZZ4L_RooSpinZeroPdf_phase_fast*)
   {
      ::HZZ4L_RooSpinZeroPdf_phase_fast *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::HZZ4L_RooSpinZeroPdf_phase_fast >(0);
      static ::ROOT::TGenericClassInfo 
         instance("HZZ4L_RooSpinZeroPdf_phase_fast", ::HZZ4L_RooSpinZeroPdf_phase_fast::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HZZ4L_RooSpinZeroPdf_phase_fast.h", 12,
                  typeid(::HZZ4L_RooSpinZeroPdf_phase_fast), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::HZZ4L_RooSpinZeroPdf_phase_fast::Dictionary, isa_proxy, 4,
                  sizeof(::HZZ4L_RooSpinZeroPdf_phase_fast) );
      instance.SetNew(&new_HZZ4L_RooSpinZeroPdf_phase_fast);
      instance.SetNewArray(&newArray_HZZ4L_RooSpinZeroPdf_phase_fast);
      instance.SetDelete(&delete_HZZ4L_RooSpinZeroPdf_phase_fast);
      instance.SetDeleteArray(&deleteArray_HZZ4L_RooSpinZeroPdf_phase_fast);
      instance.SetDestructor(&destruct_HZZ4L_RooSpinZeroPdf_phase_fast);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::HZZ4L_RooSpinZeroPdf_phase_fast*)
   {
      return GenerateInitInstanceLocal((::HZZ4L_RooSpinZeroPdf_phase_fast*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::HZZ4L_RooSpinZeroPdf_phase_fast*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_VVHZZ4L_RooSpinZeroPdf_1D_fast(void *p = 0);
   static void *newArray_VVHZZ4L_RooSpinZeroPdf_1D_fast(Long_t size, void *p);
   static void delete_VVHZZ4L_RooSpinZeroPdf_1D_fast(void *p);
   static void deleteArray_VVHZZ4L_RooSpinZeroPdf_1D_fast(void *p);
   static void destruct_VVHZZ4L_RooSpinZeroPdf_1D_fast(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::VVHZZ4L_RooSpinZeroPdf_1D_fast*)
   {
      ::VVHZZ4L_RooSpinZeroPdf_1D_fast *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::VVHZZ4L_RooSpinZeroPdf_1D_fast >(0);
      static ::ROOT::TGenericClassInfo 
         instance("VVHZZ4L_RooSpinZeroPdf_1D_fast", ::VVHZZ4L_RooSpinZeroPdf_1D_fast::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/VVHZZ4L_RooSpinZeroPdf_1D_fast.h", 12,
                  typeid(::VVHZZ4L_RooSpinZeroPdf_1D_fast), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::VVHZZ4L_RooSpinZeroPdf_1D_fast::Dictionary, isa_proxy, 4,
                  sizeof(::VVHZZ4L_RooSpinZeroPdf_1D_fast) );
      instance.SetNew(&new_VVHZZ4L_RooSpinZeroPdf_1D_fast);
      instance.SetNewArray(&newArray_VVHZZ4L_RooSpinZeroPdf_1D_fast);
      instance.SetDelete(&delete_VVHZZ4L_RooSpinZeroPdf_1D_fast);
      instance.SetDeleteArray(&deleteArray_VVHZZ4L_RooSpinZeroPdf_1D_fast);
      instance.SetDestructor(&destruct_VVHZZ4L_RooSpinZeroPdf_1D_fast);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::VVHZZ4L_RooSpinZeroPdf_1D_fast*)
   {
      return GenerateInitInstanceLocal((::VVHZZ4L_RooSpinZeroPdf_1D_fast*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::VVHZZ4L_RooSpinZeroPdf_1D_fast*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooChebyshevPDF(void *p = 0);
   static void *newArray_RooChebyshevPDF(Long_t size, void *p);
   static void delete_RooChebyshevPDF(void *p);
   static void deleteArray_RooChebyshevPDF(void *p);
   static void destruct_RooChebyshevPDF(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooChebyshevPDF*)
   {
      ::RooChebyshevPDF *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooChebyshevPDF >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooChebyshevPDF", ::RooChebyshevPDF::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HWWLVJJRooPdfs.h", 16,
                  typeid(::RooChebyshevPDF), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooChebyshevPDF::Dictionary, isa_proxy, 4,
                  sizeof(::RooChebyshevPDF) );
      instance.SetNew(&new_RooChebyshevPDF);
      instance.SetNewArray(&newArray_RooChebyshevPDF);
      instance.SetDelete(&delete_RooChebyshevPDF);
      instance.SetDeleteArray(&deleteArray_RooChebyshevPDF);
      instance.SetDestructor(&destruct_RooChebyshevPDF);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooChebyshevPDF*)
   {
      return GenerateInitInstanceLocal((::RooChebyshevPDF*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooChebyshevPDF*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooErfPdf(void *p = 0);
   static void *newArray_RooErfPdf(Long_t size, void *p);
   static void delete_RooErfPdf(void *p);
   static void deleteArray_RooErfPdf(void *p);
   static void destruct_RooErfPdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooErfPdf*)
   {
      ::RooErfPdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooErfPdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooErfPdf", ::RooErfPdf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HWWLVJJRooPdfs.h", 51,
                  typeid(::RooErfPdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooErfPdf::Dictionary, isa_proxy, 4,
                  sizeof(::RooErfPdf) );
      instance.SetNew(&new_RooErfPdf);
      instance.SetNewArray(&newArray_RooErfPdf);
      instance.SetDelete(&delete_RooErfPdf);
      instance.SetDeleteArray(&deleteArray_RooErfPdf);
      instance.SetDestructor(&destruct_RooErfPdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooErfPdf*)
   {
      return GenerateInitInstanceLocal((::RooErfPdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooErfPdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooPowerExpPdf(void *p = 0);
   static void *newArray_RooPowerExpPdf(Long_t size, void *p);
   static void delete_RooPowerExpPdf(void *p);
   static void deleteArray_RooPowerExpPdf(void *p);
   static void destruct_RooPowerExpPdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooPowerExpPdf*)
   {
      ::RooPowerExpPdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooPowerExpPdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooPowerExpPdf", ::RooPowerExpPdf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HWWLVJJRooPdfs.h", 87,
                  typeid(::RooPowerExpPdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooPowerExpPdf::Dictionary, isa_proxy, 4,
                  sizeof(::RooPowerExpPdf) );
      instance.SetNew(&new_RooPowerExpPdf);
      instance.SetNewArray(&newArray_RooPowerExpPdf);
      instance.SetDelete(&delete_RooPowerExpPdf);
      instance.SetDeleteArray(&deleteArray_RooPowerExpPdf);
      instance.SetDestructor(&destruct_RooPowerExpPdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooPowerExpPdf*)
   {
      return GenerateInitInstanceLocal((::RooPowerExpPdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooPowerExpPdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooTH1DPdf(void *p = 0);
   static void *newArray_RooTH1DPdf(Long_t size, void *p);
   static void delete_RooTH1DPdf(void *p);
   static void deleteArray_RooTH1DPdf(void *p);
   static void destruct_RooTH1DPdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooTH1DPdf*)
   {
      ::RooTH1DPdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooTH1DPdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooTH1DPdf", ::RooTH1DPdf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HWWLVJJRooPdfs.h", 121,
                  typeid(::RooTH1DPdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooTH1DPdf::Dictionary, isa_proxy, 4,
                  sizeof(::RooTH1DPdf) );
      instance.SetNew(&new_RooTH1DPdf);
      instance.SetNewArray(&newArray_RooTH1DPdf);
      instance.SetDelete(&delete_RooTH1DPdf);
      instance.SetDeleteArray(&deleteArray_RooTH1DPdf);
      instance.SetDestructor(&destruct_RooTH1DPdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooTH1DPdf*)
   {
      return GenerateInitInstanceLocal((::RooTH1DPdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooTH1DPdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooPowerFunction(void *p = 0);
   static void *newArray_RooPowerFunction(Long_t size, void *p);
   static void delete_RooPowerFunction(void *p);
   static void deleteArray_RooPowerFunction(void *p);
   static void destruct_RooPowerFunction(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooPowerFunction*)
   {
      ::RooPowerFunction *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooPowerFunction >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooPowerFunction", ::RooPowerFunction::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HWWLVJJRooPdfs.h", 148,
                  typeid(::RooPowerFunction), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooPowerFunction::Dictionary, isa_proxy, 4,
                  sizeof(::RooPowerFunction) );
      instance.SetNew(&new_RooPowerFunction);
      instance.SetNewArray(&newArray_RooPowerFunction);
      instance.SetDelete(&delete_RooPowerFunction);
      instance.SetDeleteArray(&deleteArray_RooPowerFunction);
      instance.SetDestructor(&destruct_RooPowerFunction);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooPowerFunction*)
   {
      return GenerateInitInstanceLocal((::RooPowerFunction*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooPowerFunction*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooPowerLaw(void *p = 0);
   static void *newArray_RooPowerLaw(Long_t size, void *p);
   static void delete_RooPowerLaw(void *p);
   static void deleteArray_RooPowerLaw(void *p);
   static void destruct_RooPowerLaw(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooPowerLaw*)
   {
      ::RooPowerLaw *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooPowerLaw >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooPowerLaw", ::RooPowerLaw::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HWWLVJJRooPdfs.h", 177,
                  typeid(::RooPowerLaw), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooPowerLaw::Dictionary, isa_proxy, 4,
                  sizeof(::RooPowerLaw) );
      instance.SetNew(&new_RooPowerLaw);
      instance.SetNewArray(&newArray_RooPowerLaw);
      instance.SetDelete(&delete_RooPowerLaw);
      instance.SetDeleteArray(&deleteArray_RooPowerLaw);
      instance.SetDestructor(&destruct_RooPowerLaw);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooPowerLaw*)
   {
      return GenerateInitInstanceLocal((::RooPowerLaw*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooPowerLaw*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooExpPoly(void *p = 0);
   static void *newArray_RooExpPoly(Long_t size, void *p);
   static void delete_RooExpPoly(void *p);
   static void deleteArray_RooExpPoly(void *p);
   static void destruct_RooExpPoly(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooExpPoly*)
   {
      ::RooExpPoly *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooExpPoly >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooExpPoly", ::RooExpPoly::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/HWWLVJJRooPdfs.h", 202,
                  typeid(::RooExpPoly), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooExpPoly::Dictionary, isa_proxy, 4,
                  sizeof(::RooExpPoly) );
      instance.SetNew(&new_RooExpPoly);
      instance.SetNewArray(&newArray_RooExpPoly);
      instance.SetDelete(&delete_RooExpPoly);
      instance.SetDeleteArray(&deleteArray_RooExpPoly);
      instance.SetDestructor(&destruct_RooExpPoly);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooExpPoly*)
   {
      return GenerateInitInstanceLocal((::RooExpPoly*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooExpPoly*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooMorphingPdf(void *p = 0);
   static void *newArray_RooMorphingPdf(Long_t size, void *p);
   static void delete_RooMorphingPdf(void *p);
   static void deleteArray_RooMorphingPdf(void *p);
   static void destruct_RooMorphingPdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooMorphingPdf*)
   {
      ::RooMorphingPdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooMorphingPdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooMorphingPdf", ::RooMorphingPdf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/RooMorphingPdf.h", 15,
                  typeid(::RooMorphingPdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooMorphingPdf::Dictionary, isa_proxy, 4,
                  sizeof(::RooMorphingPdf) );
      instance.SetNew(&new_RooMorphingPdf);
      instance.SetNewArray(&newArray_RooMorphingPdf);
      instance.SetDelete(&delete_RooMorphingPdf);
      instance.SetDeleteArray(&deleteArray_RooMorphingPdf);
      instance.SetDestructor(&destruct_RooMorphingPdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooMorphingPdf*)
   {
      return GenerateInitInstanceLocal((::RooMorphingPdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooMorphingPdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooParametricHist(void *p = 0);
   static void *newArray_RooParametricHist(Long_t size, void *p);
   static void delete_RooParametricHist(void *p);
   static void deleteArray_RooParametricHist(void *p);
   static void destruct_RooParametricHist(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooParametricHist*)
   {
      ::RooParametricHist *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooParametricHist >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooParametricHist", ::RooParametricHist::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/RooParametricHist.h", 18,
                  typeid(::RooParametricHist), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooParametricHist::Dictionary, isa_proxy, 4,
                  sizeof(::RooParametricHist) );
      instance.SetNew(&new_RooParametricHist);
      instance.SetNewArray(&newArray_RooParametricHist);
      instance.SetDelete(&delete_RooParametricHist);
      instance.SetDeleteArray(&deleteArray_RooParametricHist);
      instance.SetDestructor(&destruct_RooParametricHist);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooParametricHist*)
   {
      return GenerateInitInstanceLocal((::RooParametricHist*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooParametricHist*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooParametricShapeBinPdf(void *p = 0);
   static void *newArray_RooParametricShapeBinPdf(Long_t size, void *p);
   static void delete_RooParametricShapeBinPdf(void *p);
   static void deleteArray_RooParametricShapeBinPdf(void *p);
   static void destruct_RooParametricShapeBinPdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooParametricShapeBinPdf*)
   {
      ::RooParametricShapeBinPdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooParametricShapeBinPdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooParametricShapeBinPdf", ::RooParametricShapeBinPdf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/RooParametricShapeBinPdf.h", 17,
                  typeid(::RooParametricShapeBinPdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooParametricShapeBinPdf::Dictionary, isa_proxy, 4,
                  sizeof(::RooParametricShapeBinPdf) );
      instance.SetNew(&new_RooParametricShapeBinPdf);
      instance.SetNewArray(&newArray_RooParametricShapeBinPdf);
      instance.SetDelete(&delete_RooParametricShapeBinPdf);
      instance.SetDeleteArray(&deleteArray_RooParametricShapeBinPdf);
      instance.SetDestructor(&destruct_RooParametricShapeBinPdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooParametricShapeBinPdf*)
   {
      return GenerateInitInstanceLocal((::RooParametricShapeBinPdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooParametricShapeBinPdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_GaussExp(void *p = 0);
   static void *newArray_GaussExp(Long_t size, void *p);
   static void delete_GaussExp(void *p);
   static void deleteArray_GaussExp(void *p);
   static void destruct_GaussExp(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::GaussExp*)
   {
      ::GaussExp *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::GaussExp >(0);
      static ::ROOT::TGenericClassInfo 
         instance("GaussExp", ::GaussExp::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/GaussExp.h", 16,
                  typeid(::GaussExp), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::GaussExp::Dictionary, isa_proxy, 4,
                  sizeof(::GaussExp) );
      instance.SetNew(&new_GaussExp);
      instance.SetNewArray(&newArray_GaussExp);
      instance.SetDelete(&delete_GaussExp);
      instance.SetDeleteArray(&deleteArray_GaussExp);
      instance.SetDestructor(&destruct_GaussExp);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::GaussExp*)
   {
      return GenerateInitInstanceLocal((::GaussExp*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::GaussExp*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooDoubleCBFast(void *p = 0);
   static void *newArray_RooDoubleCBFast(Long_t size, void *p);
   static void delete_RooDoubleCBFast(void *p);
   static void deleteArray_RooDoubleCBFast(void *p);
   static void destruct_RooDoubleCBFast(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooDoubleCBFast*)
   {
      ::RooDoubleCBFast *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooDoubleCBFast >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooDoubleCBFast", ::RooDoubleCBFast::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/RooDoubleCBFast.h", 8,
                  typeid(::RooDoubleCBFast), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooDoubleCBFast::Dictionary, isa_proxy, 4,
                  sizeof(::RooDoubleCBFast) );
      instance.SetNew(&new_RooDoubleCBFast);
      instance.SetNewArray(&newArray_RooDoubleCBFast);
      instance.SetDelete(&delete_RooDoubleCBFast);
      instance.SetDeleteArray(&deleteArray_RooDoubleCBFast);
      instance.SetDestructor(&destruct_RooDoubleCBFast);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooDoubleCBFast*)
   {
      return GenerateInitInstanceLocal((::RooDoubleCBFast*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooDoubleCBFast*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_CMSHistFunc(void *p = 0);
   static void *newArray_CMSHistFunc(Long_t size, void *p);
   static void delete_CMSHistFunc(void *p);
   static void deleteArray_CMSHistFunc(void *p);
   static void destruct_CMSHistFunc(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::CMSHistFunc*)
   {
      ::CMSHistFunc *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::CMSHistFunc >(0);
      static ::ROOT::TGenericClassInfo 
         instance("CMSHistFunc", ::CMSHistFunc::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/CMSHistFunc.h", 21,
                  typeid(::CMSHistFunc), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::CMSHistFunc::Dictionary, isa_proxy, 4,
                  sizeof(::CMSHistFunc) );
      instance.SetNew(&new_CMSHistFunc);
      instance.SetNewArray(&newArray_CMSHistFunc);
      instance.SetDelete(&delete_CMSHistFunc);
      instance.SetDeleteArray(&deleteArray_CMSHistFunc);
      instance.SetDestructor(&destruct_CMSHistFunc);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::CMSHistFunc*)
   {
      return GenerateInitInstanceLocal((::CMSHistFunc*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::CMSHistFunc*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_CMSHistErrorPropagator(void *p = 0);
   static void *newArray_CMSHistErrorPropagator(Long_t size, void *p);
   static void delete_CMSHistErrorPropagator(void *p);
   static void deleteArray_CMSHistErrorPropagator(void *p);
   static void destruct_CMSHistErrorPropagator(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::CMSHistErrorPropagator*)
   {
      ::CMSHistErrorPropagator *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::CMSHistErrorPropagator >(0);
      static ::ROOT::TGenericClassInfo 
         instance("CMSHistErrorPropagator", ::CMSHistErrorPropagator::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/CMSHistErrorPropagator.h", 17,
                  typeid(::CMSHistErrorPropagator), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::CMSHistErrorPropagator::Dictionary, isa_proxy, 4,
                  sizeof(::CMSHistErrorPropagator) );
      instance.SetNew(&new_CMSHistErrorPropagator);
      instance.SetNewArray(&newArray_CMSHistErrorPropagator);
      instance.SetDelete(&delete_CMSHistErrorPropagator);
      instance.SetDeleteArray(&deleteArray_CMSHistErrorPropagator);
      instance.SetDestructor(&destruct_CMSHistErrorPropagator);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::CMSHistErrorPropagator*)
   {
      return GenerateInitInstanceLocal((::CMSHistErrorPropagator*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::CMSHistErrorPropagator*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_CMSHistFuncWrapper(void *p = 0);
   static void *newArray_CMSHistFuncWrapper(Long_t size, void *p);
   static void delete_CMSHistFuncWrapper(void *p);
   static void deleteArray_CMSHistFuncWrapper(void *p);
   static void destruct_CMSHistFuncWrapper(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::CMSHistFuncWrapper*)
   {
      ::CMSHistFuncWrapper *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::CMSHistFuncWrapper >(0);
      static ::ROOT::TGenericClassInfo 
         instance("CMSHistFuncWrapper", ::CMSHistFuncWrapper::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/CMSHistFuncWrapper.h", 18,
                  typeid(::CMSHistFuncWrapper), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::CMSHistFuncWrapper::Dictionary, isa_proxy, 4,
                  sizeof(::CMSHistFuncWrapper) );
      instance.SetNew(&new_CMSHistFuncWrapper);
      instance.SetNewArray(&newArray_CMSHistFuncWrapper);
      instance.SetDelete(&delete_CMSHistFuncWrapper);
      instance.SetDeleteArray(&deleteArray_CMSHistFuncWrapper);
      instance.SetDestructor(&destruct_CMSHistFuncWrapper);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::CMSHistFuncWrapper*)
   {
      return GenerateInitInstanceLocal((::CMSHistFuncWrapper*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::CMSHistFuncWrapper*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooTaylorExpansion(void *p = 0);
   static void *newArray_RooTaylorExpansion(Long_t size, void *p);
   static void delete_RooTaylorExpansion(void *p);
   static void deleteArray_RooTaylorExpansion(void *p);
   static void destruct_RooTaylorExpansion(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooTaylorExpansion*)
   {
      ::RooTaylorExpansion *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooTaylorExpansion >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooTaylorExpansion", ::RooTaylorExpansion::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/RooTaylorExpansion.h", 13,
                  typeid(::RooTaylorExpansion), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooTaylorExpansion::Dictionary, isa_proxy, 4,
                  sizeof(::RooTaylorExpansion) );
      instance.SetNew(&new_RooTaylorExpansion);
      instance.SetNewArray(&newArray_RooTaylorExpansion);
      instance.SetDelete(&delete_RooTaylorExpansion);
      instance.SetDeleteArray(&deleteArray_RooTaylorExpansion);
      instance.SetDestructor(&destruct_RooTaylorExpansion);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooTaylorExpansion*)
   {
      return GenerateInitInstanceLocal((::RooTaylorExpansion*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooTaylorExpansion*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_SimpleTaylorExpansion1D(void *p = 0);
   static void *newArray_SimpleTaylorExpansion1D(Long_t size, void *p);
   static void delete_SimpleTaylorExpansion1D(void *p);
   static void deleteArray_SimpleTaylorExpansion1D(void *p);
   static void destruct_SimpleTaylorExpansion1D(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::SimpleTaylorExpansion1D*)
   {
      ::SimpleTaylorExpansion1D *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::SimpleTaylorExpansion1D >(0);
      static ::ROOT::TGenericClassInfo 
         instance("SimpleTaylorExpansion1D", ::SimpleTaylorExpansion1D::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/SimpleTaylorExpansion1D.h", 17,
                  typeid(::SimpleTaylorExpansion1D), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::SimpleTaylorExpansion1D::Dictionary, isa_proxy, 4,
                  sizeof(::SimpleTaylorExpansion1D) );
      instance.SetNew(&new_SimpleTaylorExpansion1D);
      instance.SetNewArray(&newArray_SimpleTaylorExpansion1D);
      instance.SetDelete(&delete_SimpleTaylorExpansion1D);
      instance.SetDeleteArray(&deleteArray_SimpleTaylorExpansion1D);
      instance.SetDestructor(&destruct_SimpleTaylorExpansion1D);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::SimpleTaylorExpansion1D*)
   {
      return GenerateInitInstanceLocal((::SimpleTaylorExpansion1D*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::SimpleTaylorExpansion1D*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooPiecewisePolynomial(void *p = 0);
   static void *newArray_RooPiecewisePolynomial(Long_t size, void *p);
   static void delete_RooPiecewisePolynomial(void *p);
   static void deleteArray_RooPiecewisePolynomial(void *p);
   static void destruct_RooPiecewisePolynomial(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooPiecewisePolynomial*)
   {
      ::RooPiecewisePolynomial *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooPiecewisePolynomial >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooPiecewisePolynomial", ::RooPiecewisePolynomial::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/RooPiecewisePolynomial.h", 11,
                  typeid(::RooPiecewisePolynomial), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooPiecewisePolynomial::Dictionary, isa_proxy, 4,
                  sizeof(::RooPiecewisePolynomial) );
      instance.SetNew(&new_RooPiecewisePolynomial);
      instance.SetNewArray(&newArray_RooPiecewisePolynomial);
      instance.SetDelete(&delete_RooPiecewisePolynomial);
      instance.SetDeleteArray(&deleteArray_RooPiecewisePolynomial);
      instance.SetDestructor(&destruct_RooPiecewisePolynomial);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooPiecewisePolynomial*)
   {
      return GenerateInitInstanceLocal((::RooPiecewisePolynomial*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooPiecewisePolynomial*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void delete_RooNCSplineCore(void *p);
   static void deleteArray_RooNCSplineCore(void *p);
   static void destruct_RooNCSplineCore(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooNCSplineCore*)
   {
      ::RooNCSplineCore *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooNCSplineCore >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooNCSplineCore", ::RooNCSplineCore::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/RooNCSplineCore.h", 15,
                  typeid(::RooNCSplineCore), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooNCSplineCore::Dictionary, isa_proxy, 4,
                  sizeof(::RooNCSplineCore) );
      instance.SetDelete(&delete_RooNCSplineCore);
      instance.SetDeleteArray(&deleteArray_RooNCSplineCore);
      instance.SetDestructor(&destruct_RooNCSplineCore);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooNCSplineCore*)
   {
      return GenerateInitInstanceLocal((::RooNCSplineCore*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooNCSplineCore*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooNCSpline_1D_fast(void *p = 0);
   static void *newArray_RooNCSpline_1D_fast(Long_t size, void *p);
   static void delete_RooNCSpline_1D_fast(void *p);
   static void deleteArray_RooNCSpline_1D_fast(void *p);
   static void destruct_RooNCSpline_1D_fast(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooNCSpline_1D_fast*)
   {
      ::RooNCSpline_1D_fast *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooNCSpline_1D_fast >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooNCSpline_1D_fast", ::RooNCSpline_1D_fast::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/RooNCSpline_1D_fast.h", 12,
                  typeid(::RooNCSpline_1D_fast), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooNCSpline_1D_fast::Dictionary, isa_proxy, 4,
                  sizeof(::RooNCSpline_1D_fast) );
      instance.SetNew(&new_RooNCSpline_1D_fast);
      instance.SetNewArray(&newArray_RooNCSpline_1D_fast);
      instance.SetDelete(&delete_RooNCSpline_1D_fast);
      instance.SetDeleteArray(&deleteArray_RooNCSpline_1D_fast);
      instance.SetDestructor(&destruct_RooNCSpline_1D_fast);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooNCSpline_1D_fast*)
   {
      return GenerateInitInstanceLocal((::RooNCSpline_1D_fast*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooNCSpline_1D_fast*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooNCSpline_2D_fast(void *p = 0);
   static void *newArray_RooNCSpline_2D_fast(Long_t size, void *p);
   static void delete_RooNCSpline_2D_fast(void *p);
   static void deleteArray_RooNCSpline_2D_fast(void *p);
   static void destruct_RooNCSpline_2D_fast(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooNCSpline_2D_fast*)
   {
      ::RooNCSpline_2D_fast *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooNCSpline_2D_fast >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooNCSpline_2D_fast", ::RooNCSpline_2D_fast::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/RooNCSpline_2D_fast.h", 11,
                  typeid(::RooNCSpline_2D_fast), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooNCSpline_2D_fast::Dictionary, isa_proxy, 4,
                  sizeof(::RooNCSpline_2D_fast) );
      instance.SetNew(&new_RooNCSpline_2D_fast);
      instance.SetNewArray(&newArray_RooNCSpline_2D_fast);
      instance.SetDelete(&delete_RooNCSpline_2D_fast);
      instance.SetDeleteArray(&deleteArray_RooNCSpline_2D_fast);
      instance.SetDestructor(&destruct_RooNCSpline_2D_fast);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooNCSpline_2D_fast*)
   {
      return GenerateInitInstanceLocal((::RooNCSpline_2D_fast*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooNCSpline_2D_fast*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooNCSpline_3D_fast(void *p = 0);
   static void *newArray_RooNCSpline_3D_fast(Long_t size, void *p);
   static void delete_RooNCSpline_3D_fast(void *p);
   static void deleteArray_RooNCSpline_3D_fast(void *p);
   static void destruct_RooNCSpline_3D_fast(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooNCSpline_3D_fast*)
   {
      ::RooNCSpline_3D_fast *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooNCSpline_3D_fast >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooNCSpline_3D_fast", ::RooNCSpline_3D_fast::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/RooNCSpline_3D_fast.h", 11,
                  typeid(::RooNCSpline_3D_fast), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooNCSpline_3D_fast::Dictionary, isa_proxy, 4,
                  sizeof(::RooNCSpline_3D_fast) );
      instance.SetNew(&new_RooNCSpline_3D_fast);
      instance.SetNewArray(&newArray_RooNCSpline_3D_fast);
      instance.SetDelete(&delete_RooNCSpline_3D_fast);
      instance.SetDeleteArray(&deleteArray_RooNCSpline_3D_fast);
      instance.SetDestructor(&destruct_RooNCSpline_3D_fast);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooNCSpline_3D_fast*)
   {
      return GenerateInitInstanceLocal((::RooNCSpline_3D_fast*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooNCSpline_3D_fast*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooFuncPdf(void *p = 0);
   static void *newArray_RooFuncPdf(Long_t size, void *p);
   static void delete_RooFuncPdf(void *p);
   static void deleteArray_RooFuncPdf(void *p);
   static void destruct_RooFuncPdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooFuncPdf*)
   {
      ::RooFuncPdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooFuncPdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooFuncPdf", ::RooFuncPdf::Class_Version(), "HiggsAnalysis/CombinedLimit/interface/RooFuncPdf.h", 7,
                  typeid(::RooFuncPdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooFuncPdf::Dictionary, isa_proxy, 4,
                  sizeof(::RooFuncPdf) );
      instance.SetNew(&new_RooFuncPdf);
      instance.SetNewArray(&newArray_RooFuncPdf);
      instance.SetDelete(&delete_RooFuncPdf);
      instance.SetDeleteArray(&deleteArray_RooFuncPdf);
      instance.SetDestructor(&destruct_RooFuncPdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooFuncPdf*)
   {
      return GenerateInitInstanceLocal((::RooFuncPdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooFuncPdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

//______________________________________________________________________________
atomic_TClass_ptr TestProposal::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *TestProposal::Class_Name()
{
   return "TestProposal";
}

//______________________________________________________________________________
const char *TestProposal::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::TestProposal*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int TestProposal::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::TestProposal*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *TestProposal::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::TestProposal*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *TestProposal::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::TestProposal*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr DebugProposal::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *DebugProposal::Class_Name()
{
   return "DebugProposal";
}

//______________________________________________________________________________
const char *DebugProposal::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::DebugProposal*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int DebugProposal::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::DebugProposal*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *DebugProposal::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::DebugProposal*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *DebugProposal::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::DebugProposal*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr VerticalInterpPdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *VerticalInterpPdf::Class_Name()
{
   return "VerticalInterpPdf";
}

//______________________________________________________________________________
const char *VerticalInterpPdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::VerticalInterpPdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int VerticalInterpPdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::VerticalInterpPdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *VerticalInterpPdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::VerticalInterpPdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *VerticalInterpPdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::VerticalInterpPdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr SimpleCacheSentry::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *SimpleCacheSentry::Class_Name()
{
   return "SimpleCacheSentry";
}

//______________________________________________________________________________
const char *SimpleCacheSentry::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SimpleCacheSentry*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int SimpleCacheSentry::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SimpleCacheSentry*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *SimpleCacheSentry::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SimpleCacheSentry*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *SimpleCacheSentry::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SimpleCacheSentry*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr VerticalInterpHistPdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *VerticalInterpHistPdf::Class_Name()
{
   return "VerticalInterpHistPdf";
}

//______________________________________________________________________________
const char *VerticalInterpHistPdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::VerticalInterpHistPdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int VerticalInterpHistPdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::VerticalInterpHistPdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *VerticalInterpHistPdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::VerticalInterpHistPdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *VerticalInterpHistPdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::VerticalInterpHistPdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr FastVerticalInterpHistPdfBase::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *FastVerticalInterpHistPdfBase::Class_Name()
{
   return "FastVerticalInterpHistPdfBase";
}

//______________________________________________________________________________
const char *FastVerticalInterpHistPdfBase::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::FastVerticalInterpHistPdfBase*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int FastVerticalInterpHistPdfBase::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::FastVerticalInterpHistPdfBase*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *FastVerticalInterpHistPdfBase::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::FastVerticalInterpHistPdfBase*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *FastVerticalInterpHistPdfBase::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::FastVerticalInterpHistPdfBase*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr FastVerticalInterpHistPdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *FastVerticalInterpHistPdf::Class_Name()
{
   return "FastVerticalInterpHistPdf";
}

//______________________________________________________________________________
const char *FastVerticalInterpHistPdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::FastVerticalInterpHistPdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int FastVerticalInterpHistPdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::FastVerticalInterpHistPdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *FastVerticalInterpHistPdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::FastVerticalInterpHistPdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *FastVerticalInterpHistPdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::FastVerticalInterpHistPdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr FastVerticalInterpHistPdf2D::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *FastVerticalInterpHistPdf2D::Class_Name()
{
   return "FastVerticalInterpHistPdf2D";
}

//______________________________________________________________________________
const char *FastVerticalInterpHistPdf2D::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::FastVerticalInterpHistPdf2D*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int FastVerticalInterpHistPdf2D::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::FastVerticalInterpHistPdf2D*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *FastVerticalInterpHistPdf2D::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::FastVerticalInterpHistPdf2D*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *FastVerticalInterpHistPdf2D::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::FastVerticalInterpHistPdf2D*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr FastVerticalInterpHistPdf2Base::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *FastVerticalInterpHistPdf2Base::Class_Name()
{
   return "FastVerticalInterpHistPdf2Base";
}

//______________________________________________________________________________
const char *FastVerticalInterpHistPdf2Base::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::FastVerticalInterpHistPdf2Base*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int FastVerticalInterpHistPdf2Base::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::FastVerticalInterpHistPdf2Base*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *FastVerticalInterpHistPdf2Base::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::FastVerticalInterpHistPdf2Base*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *FastVerticalInterpHistPdf2Base::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::FastVerticalInterpHistPdf2Base*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr FastVerticalInterpHistPdf2::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *FastVerticalInterpHistPdf2::Class_Name()
{
   return "FastVerticalInterpHistPdf2";
}

//______________________________________________________________________________
const char *FastVerticalInterpHistPdf2::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::FastVerticalInterpHistPdf2*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int FastVerticalInterpHistPdf2::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::FastVerticalInterpHistPdf2*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *FastVerticalInterpHistPdf2::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::FastVerticalInterpHistPdf2*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *FastVerticalInterpHistPdf2::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::FastVerticalInterpHistPdf2*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr FastVerticalInterpHistPdf2D2::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *FastVerticalInterpHistPdf2D2::Class_Name()
{
   return "FastVerticalInterpHistPdf2D2";
}

//______________________________________________________________________________
const char *FastVerticalInterpHistPdf2D2::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::FastVerticalInterpHistPdf2D2*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int FastVerticalInterpHistPdf2D2::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::FastVerticalInterpHistPdf2D2*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *FastVerticalInterpHistPdf2D2::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::FastVerticalInterpHistPdf2D2*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *FastVerticalInterpHistPdf2D2::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::FastVerticalInterpHistPdf2D2*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr FastVerticalInterpHistPdf3D::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *FastVerticalInterpHistPdf3D::Class_Name()
{
   return "FastVerticalInterpHistPdf3D";
}

//______________________________________________________________________________
const char *FastVerticalInterpHistPdf3D::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::FastVerticalInterpHistPdf3D*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int FastVerticalInterpHistPdf3D::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::FastVerticalInterpHistPdf3D*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *FastVerticalInterpHistPdf3D::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::FastVerticalInterpHistPdf3D*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *FastVerticalInterpHistPdf3D::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::FastVerticalInterpHistPdf3D*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr AsymPow::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *AsymPow::Class_Name()
{
   return "AsymPow";
}

//______________________________________________________________________________
const char *AsymPow::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::AsymPow*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int AsymPow::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::AsymPow*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *AsymPow::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::AsymPow*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *AsymPow::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::AsymPow*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr AsymQuad::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *AsymQuad::Class_Name()
{
   return "AsymQuad";
}

//______________________________________________________________________________
const char *AsymQuad::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::AsymQuad*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int AsymQuad::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::AsymQuad*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *AsymQuad::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::AsymQuad*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *AsymQuad::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::AsymQuad*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr CombDataSetFactory::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *CombDataSetFactory::Class_Name()
{
   return "CombDataSetFactory";
}

//______________________________________________________________________________
const char *CombDataSetFactory::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::CombDataSetFactory*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int CombDataSetFactory::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::CombDataSetFactory*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *CombDataSetFactory::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::CombDataSetFactory*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *CombDataSetFactory::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::CombDataSetFactory*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr TH1Keys::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *TH1Keys::Class_Name()
{
   return "TH1Keys";
}

//______________________________________________________________________________
const char *TH1Keys::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::TH1Keys*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int TH1Keys::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::TH1Keys*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *TH1Keys::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::TH1Keys*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *TH1Keys::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::TH1Keys*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooSimultaneousOpt::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooSimultaneousOpt::Class_Name()
{
   return "RooSimultaneousOpt";
}

//______________________________________________________________________________
const char *RooSimultaneousOpt::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooSimultaneousOpt*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooSimultaneousOpt::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooSimultaneousOpt*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooSimultaneousOpt::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooSimultaneousOpt*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooSimultaneousOpt::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooSimultaneousOpt*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr HZZ4L_RooCTauPdf_1D::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *HZZ4L_RooCTauPdf_1D::Class_Name()
{
   return "HZZ4L_RooCTauPdf_1D";
}

//______________________________________________________________________________
const char *HZZ4L_RooCTauPdf_1D::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooCTauPdf_1D*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int HZZ4L_RooCTauPdf_1D::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooCTauPdf_1D*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *HZZ4L_RooCTauPdf_1D::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooCTauPdf_1D*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *HZZ4L_RooCTauPdf_1D::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooCTauPdf_1D*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr HZZ4L_RooCTauPdf_1D_Expanded::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *HZZ4L_RooCTauPdf_1D_Expanded::Class_Name()
{
   return "HZZ4L_RooCTauPdf_1D_Expanded";
}

//______________________________________________________________________________
const char *HZZ4L_RooCTauPdf_1D_Expanded::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooCTauPdf_1D_Expanded*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int HZZ4L_RooCTauPdf_1D_Expanded::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooCTauPdf_1D_Expanded*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *HZZ4L_RooCTauPdf_1D_Expanded::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooCTauPdf_1D_Expanded*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *HZZ4L_RooCTauPdf_1D_Expanded::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooCTauPdf_1D_Expanded*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr HZZ4L_RooCTauPdf_2D::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *HZZ4L_RooCTauPdf_2D::Class_Name()
{
   return "HZZ4L_RooCTauPdf_2D";
}

//______________________________________________________________________________
const char *HZZ4L_RooCTauPdf_2D::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooCTauPdf_2D*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int HZZ4L_RooCTauPdf_2D::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooCTauPdf_2D*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *HZZ4L_RooCTauPdf_2D::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooCTauPdf_2D*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *HZZ4L_RooCTauPdf_2D::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooCTauPdf_2D*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooqqZZPdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooqqZZPdf::Class_Name()
{
   return "RooqqZZPdf";
}

//______________________________________________________________________________
const char *RooqqZZPdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooqqZZPdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooqqZZPdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooqqZZPdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooqqZZPdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooqqZZPdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooqqZZPdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooqqZZPdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooggZZPdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooggZZPdf::Class_Name()
{
   return "RooggZZPdf";
}

//______________________________________________________________________________
const char *RooggZZPdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooggZZPdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooggZZPdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooggZZPdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooggZZPdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooggZZPdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooggZZPdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooggZZPdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooqqZZPdf_v2::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooqqZZPdf_v2::Class_Name()
{
   return "RooqqZZPdf_v2";
}

//______________________________________________________________________________
const char *RooqqZZPdf_v2::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooqqZZPdf_v2*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooqqZZPdf_v2::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooqqZZPdf_v2*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooqqZZPdf_v2::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooqqZZPdf_v2*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooqqZZPdf_v2::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooqqZZPdf_v2*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooVBFZZPdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooVBFZZPdf::Class_Name()
{
   return "RooVBFZZPdf";
}

//______________________________________________________________________________
const char *RooVBFZZPdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooVBFZZPdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooVBFZZPdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooVBFZZPdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooVBFZZPdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooVBFZZPdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooVBFZZPdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooVBFZZPdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooVBFZZPdf_v2::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooVBFZZPdf_v2::Class_Name()
{
   return "RooVBFZZPdf_v2";
}

//______________________________________________________________________________
const char *RooVBFZZPdf_v2::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooVBFZZPdf_v2*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooVBFZZPdf_v2::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooVBFZZPdf_v2*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooVBFZZPdf_v2::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooVBFZZPdf_v2*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooVBFZZPdf_v2::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooVBFZZPdf_v2*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooggZZPdf_v2::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooggZZPdf_v2::Class_Name()
{
   return "RooggZZPdf_v2";
}

//______________________________________________________________________________
const char *RooggZZPdf_v2::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooggZZPdf_v2*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooggZZPdf_v2::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooggZZPdf_v2*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooggZZPdf_v2::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooggZZPdf_v2*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooggZZPdf_v2::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooggZZPdf_v2*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooBetaFunc_v2::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooBetaFunc_v2::Class_Name()
{
   return "RooBetaFunc_v2";
}

//______________________________________________________________________________
const char *RooBetaFunc_v2::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooBetaFunc_v2*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooBetaFunc_v2::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooBetaFunc_v2*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooBetaFunc_v2::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooBetaFunc_v2*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooBetaFunc_v2::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooBetaFunc_v2*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr Roo4lMasses2D_Bkg::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *Roo4lMasses2D_Bkg::Class_Name()
{
   return "Roo4lMasses2D_Bkg";
}

//______________________________________________________________________________
const char *Roo4lMasses2D_Bkg::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::Roo4lMasses2D_Bkg*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int Roo4lMasses2D_Bkg::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::Roo4lMasses2D_Bkg*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *Roo4lMasses2D_Bkg::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::Roo4lMasses2D_Bkg*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *Roo4lMasses2D_Bkg::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::Roo4lMasses2D_Bkg*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr Roo4lMasses2D_BkgGGZZ::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *Roo4lMasses2D_BkgGGZZ::Class_Name()
{
   return "Roo4lMasses2D_BkgGGZZ";
}

//______________________________________________________________________________
const char *Roo4lMasses2D_BkgGGZZ::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::Roo4lMasses2D_BkgGGZZ*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int Roo4lMasses2D_BkgGGZZ::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::Roo4lMasses2D_BkgGGZZ*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *Roo4lMasses2D_BkgGGZZ::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::Roo4lMasses2D_BkgGGZZ*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *Roo4lMasses2D_BkgGGZZ::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::Roo4lMasses2D_BkgGGZZ*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr Roo4lMasses2D::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *Roo4lMasses2D::Class_Name()
{
   return "Roo4lMasses2D";
}

//______________________________________________________________________________
const char *Roo4lMasses2D::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::Roo4lMasses2D*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int Roo4lMasses2D::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::Roo4lMasses2D*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *Roo4lMasses2D::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::Roo4lMasses2D*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *Roo4lMasses2D::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::Roo4lMasses2D*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooFourMuMassShapePdf2::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooFourMuMassShapePdf2::Class_Name()
{
   return "RooFourMuMassShapePdf2";
}

//______________________________________________________________________________
const char *RooFourMuMassShapePdf2::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooFourMuMassShapePdf2*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooFourMuMassShapePdf2::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooFourMuMassShapePdf2*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooFourMuMassShapePdf2::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooFourMuMassShapePdf2*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooFourMuMassShapePdf2::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooFourMuMassShapePdf2*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooFourEMassShapePdf2::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooFourEMassShapePdf2::Class_Name()
{
   return "RooFourEMassShapePdf2";
}

//______________________________________________________________________________
const char *RooFourEMassShapePdf2::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooFourEMassShapePdf2*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooFourEMassShapePdf2::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooFourEMassShapePdf2*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooFourEMassShapePdf2::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooFourEMassShapePdf2*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooFourEMassShapePdf2::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooFourEMassShapePdf2*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooTwoETwoMuMassShapePdf2::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooTwoETwoMuMassShapePdf2::Class_Name()
{
   return "RooTwoETwoMuMassShapePdf2";
}

//______________________________________________________________________________
const char *RooTwoETwoMuMassShapePdf2::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooTwoETwoMuMassShapePdf2*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooTwoETwoMuMassShapePdf2::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooTwoETwoMuMassShapePdf2*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooTwoETwoMuMassShapePdf2::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooTwoETwoMuMassShapePdf2*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooTwoETwoMuMassShapePdf2::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooTwoETwoMuMassShapePdf2*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooFourMuMassRes::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooFourMuMassRes::Class_Name()
{
   return "RooFourMuMassRes";
}

//______________________________________________________________________________
const char *RooFourMuMassRes::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooFourMuMassRes*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooFourMuMassRes::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooFourMuMassRes*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooFourMuMassRes::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooFourMuMassRes*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooFourMuMassRes::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooFourMuMassRes*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooFourEMassRes::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooFourEMassRes::Class_Name()
{
   return "RooFourEMassRes";
}

//______________________________________________________________________________
const char *RooFourEMassRes::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooFourEMassRes*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooFourEMassRes::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooFourEMassRes*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooFourEMassRes::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooFourEMassRes*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooFourEMassRes::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooFourEMassRes*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooTwoETwoMuMassRes::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooTwoETwoMuMassRes::Class_Name()
{
   return "RooTwoETwoMuMassRes";
}

//______________________________________________________________________________
const char *RooTwoETwoMuMassRes::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooTwoETwoMuMassRes*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooTwoETwoMuMassRes::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooTwoETwoMuMassRes*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooTwoETwoMuMassRes::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooTwoETwoMuMassRes*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooTwoETwoMuMassRes::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooTwoETwoMuMassRes*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooRelBW1::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooRelBW1::Class_Name()
{
   return "RooRelBW1";
}

//______________________________________________________________________________
const char *RooRelBW1::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooRelBW1*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooRelBW1::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooRelBW1*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooRelBW1::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooRelBW1*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooRelBW1::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooRelBW1*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooRelBWUF::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooRelBWUF::Class_Name()
{
   return "RooRelBWUF";
}

//______________________________________________________________________________
const char *RooRelBWUF::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooRelBWUF*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooRelBWUF::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooRelBWUF*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooRelBWUF::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooRelBWUF*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooRelBWUF::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooRelBWUF*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooRelBWUF_SM4::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooRelBWUF_SM4::Class_Name()
{
   return "RooRelBWUF_SM4";
}

//______________________________________________________________________________
const char *RooRelBWUF_SM4::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooRelBWUF_SM4*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooRelBWUF_SM4::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooRelBWUF_SM4*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooRelBWUF_SM4::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooRelBWUF_SM4*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooRelBWUF_SM4::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooRelBWUF_SM4*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooRelBWUFParamWidth::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooRelBWUFParamWidth::Class_Name()
{
   return "RooRelBWUFParamWidth";
}

//______________________________________________________________________________
const char *RooRelBWUFParamWidth::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooRelBWUFParamWidth*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooRelBWUFParamWidth::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooRelBWUFParamWidth*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooRelBWUFParamWidth::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooRelBWUFParamWidth*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooRelBWUFParamWidth::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooRelBWUFParamWidth*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooRelBWUFParam::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooRelBWUFParam::Class_Name()
{
   return "RooRelBWUFParam";
}

//______________________________________________________________________________
const char *RooRelBWUFParam::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooRelBWUFParam*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooRelBWUFParam::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooRelBWUFParam*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooRelBWUFParam::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooRelBWUFParam*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooRelBWUFParam::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooRelBWUFParam*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooRelBWHighMass::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooRelBWHighMass::Class_Name()
{
   return "RooRelBWHighMass";
}

//______________________________________________________________________________
const char *RooRelBWHighMass::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooRelBWHighMass*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooRelBWHighMass::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooRelBWHighMass*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooRelBWHighMass::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooRelBWHighMass*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooRelBWHighMass::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooRelBWHighMass*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooTsallis::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooTsallis::Class_Name()
{
   return "RooTsallis";
}

//______________________________________________________________________________
const char *RooTsallis::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooTsallis*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooTsallis::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooTsallis*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooTsallis::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooTsallis*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooTsallis::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooTsallis*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooaDoubleCBxBW::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooaDoubleCBxBW::Class_Name()
{
   return "RooaDoubleCBxBW";
}

//______________________________________________________________________________
const char *RooaDoubleCBxBW::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooaDoubleCBxBW*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooaDoubleCBxBW::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooaDoubleCBxBW*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooaDoubleCBxBW::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooaDoubleCBxBW*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooaDoubleCBxBW::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooaDoubleCBxBW*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooCPSHighMassGGH::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooCPSHighMassGGH::Class_Name()
{
   return "RooCPSHighMassGGH";
}

//______________________________________________________________________________
const char *RooCPSHighMassGGH::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooCPSHighMassGGH*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooCPSHighMassGGH::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooCPSHighMassGGH*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooCPSHighMassGGH::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooCPSHighMassGGH*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooCPSHighMassGGH::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooCPSHighMassGGH*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooBWHighMassGGH::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooBWHighMassGGH::Class_Name()
{
   return "RooBWHighMassGGH";
}

//______________________________________________________________________________
const char *RooBWHighMassGGH::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooBWHighMassGGH*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooBWHighMassGGH::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooBWHighMassGGH*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooBWHighMassGGH::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooBWHighMassGGH*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooBWHighMassGGH::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooBWHighMassGGH*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooCPSHighMassGGHNoInterf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooCPSHighMassGGHNoInterf::Class_Name()
{
   return "RooCPSHighMassGGHNoInterf";
}

//______________________________________________________________________________
const char *RooCPSHighMassGGHNoInterf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooCPSHighMassGGHNoInterf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooCPSHighMassGGHNoInterf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooCPSHighMassGGHNoInterf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooCPSHighMassGGHNoInterf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooCPSHighMassGGHNoInterf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooCPSHighMassGGHNoInterf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooCPSHighMassGGHNoInterf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooCPSHighMassVBF::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooCPSHighMassVBF::Class_Name()
{
   return "RooCPSHighMassVBF";
}

//______________________________________________________________________________
const char *RooCPSHighMassVBF::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooCPSHighMassVBF*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooCPSHighMassVBF::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooCPSHighMassVBF*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooCPSHighMassVBF::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooCPSHighMassVBF*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooCPSHighMassVBF::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooCPSHighMassVBF*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooCPSHighMassVBFNoInterf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooCPSHighMassVBFNoInterf::Class_Name()
{
   return "RooCPSHighMassVBFNoInterf";
}

//______________________________________________________________________________
const char *RooCPSHighMassVBFNoInterf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooCPSHighMassVBFNoInterf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooCPSHighMassVBFNoInterf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooCPSHighMassVBFNoInterf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooCPSHighMassVBFNoInterf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooCPSHighMassVBFNoInterf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooCPSHighMassVBFNoInterf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooCPSHighMassVBFNoInterf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooSigPlusInt::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooSigPlusInt::Class_Name()
{
   return "RooSigPlusInt";
}

//______________________________________________________________________________
const char *RooSigPlusInt::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooSigPlusInt*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooSigPlusInt::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooSigPlusInt*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooSigPlusInt::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooSigPlusInt*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooSigPlusInt::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooSigPlusInt*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooErfExpPdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooErfExpPdf::Class_Name()
{
   return "RooErfExpPdf";
}

//______________________________________________________________________________
const char *RooErfExpPdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooErfExpPdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooErfExpPdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooErfExpPdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooErfExpPdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooErfExpPdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooErfExpPdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooErfExpPdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooAlpha::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooAlpha::Class_Name()
{
   return "RooAlpha";
}

//______________________________________________________________________________
const char *RooAlpha::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooAlpha*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooAlpha::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooAlpha*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooAlpha::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooAlpha*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooAlpha::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooAlpha*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooAlphaExp::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooAlphaExp::Class_Name()
{
   return "RooAlphaExp";
}

//______________________________________________________________________________
const char *RooAlphaExp::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooAlphaExp*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooAlphaExp::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooAlphaExp*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooAlphaExp::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooAlphaExp*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooAlphaExp::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooAlphaExp*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooBWRunPdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooBWRunPdf::Class_Name()
{
   return "RooBWRunPdf";
}

//______________________________________________________________________________
const char *RooBWRunPdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooBWRunPdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooBWRunPdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooBWRunPdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooBWRunPdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooBWRunPdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooBWRunPdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooBWRunPdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooErfPow2Pdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooErfPow2Pdf::Class_Name()
{
   return "RooErfPow2Pdf";
}

//______________________________________________________________________________
const char *RooErfPow2Pdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooErfPow2Pdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooErfPow2Pdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooErfPow2Pdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooErfPow2Pdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooErfPow2Pdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooErfPow2Pdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooErfPow2Pdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooAlpha4ErfPow2Pdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooAlpha4ErfPow2Pdf::Class_Name()
{
   return "RooAlpha4ErfPow2Pdf";
}

//______________________________________________________________________________
const char *RooAlpha4ErfPow2Pdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooAlpha4ErfPow2Pdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooAlpha4ErfPow2Pdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooAlpha4ErfPow2Pdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooAlpha4ErfPow2Pdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooAlpha4ErfPow2Pdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooAlpha4ErfPow2Pdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooAlpha4ErfPow2Pdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooErfPowExpPdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooErfPowExpPdf::Class_Name()
{
   return "RooErfPowExpPdf";
}

//______________________________________________________________________________
const char *RooErfPowExpPdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooErfPowExpPdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooErfPowExpPdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooErfPowExpPdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooErfPowExpPdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooErfPowExpPdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooErfPowExpPdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooErfPowExpPdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooAlpha4ErfPowExpPdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooAlpha4ErfPowExpPdf::Class_Name()
{
   return "RooAlpha4ErfPowExpPdf";
}

//______________________________________________________________________________
const char *RooAlpha4ErfPowExpPdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooAlpha4ErfPowExpPdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooAlpha4ErfPowExpPdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooAlpha4ErfPowExpPdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooAlpha4ErfPowExpPdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooAlpha4ErfPowExpPdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooAlpha4ErfPowExpPdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooAlpha4ErfPowExpPdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooGausExpPdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooGausExpPdf::Class_Name()
{
   return "RooGausExpPdf";
}

//______________________________________________________________________________
const char *RooGausExpPdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooGausExpPdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooGausExpPdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooGausExpPdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooGausExpPdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooGausExpPdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooGausExpPdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooGausExpPdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooAlpha4GausExpPdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooAlpha4GausExpPdf::Class_Name()
{
   return "RooAlpha4GausExpPdf";
}

//______________________________________________________________________________
const char *RooAlpha4GausExpPdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooAlpha4GausExpPdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooAlpha4GausExpPdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooAlpha4GausExpPdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooAlpha4GausExpPdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooAlpha4GausExpPdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooAlpha4GausExpPdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooAlpha4GausExpPdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooErfPowPdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooErfPowPdf::Class_Name()
{
   return "RooErfPowPdf";
}

//______________________________________________________________________________
const char *RooErfPowPdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooErfPowPdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooErfPowPdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooErfPowPdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooErfPowPdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooErfPowPdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooErfPowPdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooErfPowPdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooAlpha4ErfPowPdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooAlpha4ErfPowPdf::Class_Name()
{
   return "RooAlpha4ErfPowPdf";
}

//______________________________________________________________________________
const char *RooAlpha4ErfPowPdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooAlpha4ErfPowPdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooAlpha4ErfPowPdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooAlpha4ErfPowPdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooAlpha4ErfPowPdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooAlpha4ErfPowPdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooAlpha4ErfPowPdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooAlpha4ErfPowPdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooPow2Pdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooPow2Pdf::Class_Name()
{
   return "RooPow2Pdf";
}

//______________________________________________________________________________
const char *RooPow2Pdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooPow2Pdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooPow2Pdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooPow2Pdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooPow2Pdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooPow2Pdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooPow2Pdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooPow2Pdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooPowPdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooPowPdf::Class_Name()
{
   return "RooPowPdf";
}

//______________________________________________________________________________
const char *RooPowPdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooPowPdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooPowPdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooPowPdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooPowPdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooPowPdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooPowPdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooPowPdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooQCDPdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooQCDPdf::Class_Name()
{
   return "RooQCDPdf";
}

//______________________________________________________________________________
const char *RooQCDPdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooQCDPdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooQCDPdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooQCDPdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooQCDPdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooQCDPdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooQCDPdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooQCDPdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooUser1Pdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooUser1Pdf::Class_Name()
{
   return "RooUser1Pdf";
}

//______________________________________________________________________________
const char *RooUser1Pdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooUser1Pdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooUser1Pdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooUser1Pdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooUser1Pdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooUser1Pdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooUser1Pdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooUser1Pdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooExpNPdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooExpNPdf::Class_Name()
{
   return "RooExpNPdf";
}

//______________________________________________________________________________
const char *RooExpNPdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooExpNPdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooExpNPdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooExpNPdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooExpNPdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooExpNPdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooExpNPdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooExpNPdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooAlpha4ExpNPdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooAlpha4ExpNPdf::Class_Name()
{
   return "RooAlpha4ExpNPdf";
}

//______________________________________________________________________________
const char *RooAlpha4ExpNPdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooAlpha4ExpNPdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooAlpha4ExpNPdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooAlpha4ExpNPdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooAlpha4ExpNPdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooAlpha4ExpNPdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooAlpha4ExpNPdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooAlpha4ExpNPdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooExpTailPdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooExpTailPdf::Class_Name()
{
   return "RooExpTailPdf";
}

//______________________________________________________________________________
const char *RooExpTailPdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooExpTailPdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooExpTailPdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooExpTailPdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooExpTailPdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooExpTailPdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooExpTailPdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooExpTailPdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooAlpha4ExpTailPdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooAlpha4ExpTailPdf::Class_Name()
{
   return "RooAlpha4ExpTailPdf";
}

//______________________________________________________________________________
const char *RooAlpha4ExpTailPdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooAlpha4ExpTailPdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooAlpha4ExpTailPdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooAlpha4ExpTailPdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooAlpha4ExpTailPdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooAlpha4ExpTailPdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooAlpha4ExpTailPdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooAlpha4ExpTailPdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr Roo2ExpPdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *Roo2ExpPdf::Class_Name()
{
   return "Roo2ExpPdf";
}

//______________________________________________________________________________
const char *Roo2ExpPdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::Roo2ExpPdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int Roo2ExpPdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::Roo2ExpPdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *Roo2ExpPdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::Roo2ExpPdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *Roo2ExpPdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::Roo2ExpPdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooAlpha42ExpPdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooAlpha42ExpPdf::Class_Name()
{
   return "RooAlpha42ExpPdf";
}

//______________________________________________________________________________
const char *RooAlpha42ExpPdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooAlpha42ExpPdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooAlpha42ExpPdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooAlpha42ExpPdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooAlpha42ExpPdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooAlpha42ExpPdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooAlpha42ExpPdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooAlpha42ExpPdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooAnaExpNPdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooAnaExpNPdf::Class_Name()
{
   return "RooAnaExpNPdf";
}

//______________________________________________________________________________
const char *RooAnaExpNPdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooAnaExpNPdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooAnaExpNPdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooAnaExpNPdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooAnaExpNPdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooAnaExpNPdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooAnaExpNPdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooAnaExpNPdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooDoubleCrystalBall::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooDoubleCrystalBall::Class_Name()
{
   return "RooDoubleCrystalBall";
}

//______________________________________________________________________________
const char *RooDoubleCrystalBall::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooDoubleCrystalBall*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooDoubleCrystalBall::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooDoubleCrystalBall*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooDoubleCrystalBall::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooDoubleCrystalBall*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooDoubleCrystalBall::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooDoubleCrystalBall*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooCB::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooCB::Class_Name()
{
   return "RooCB";
}

//______________________________________________________________________________
const char *RooCB::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooCB*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooCB::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooCB*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooCB::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooCB*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooCB::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooCB*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooDoubleCB::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooDoubleCB::Class_Name()
{
   return "RooDoubleCB";
}

//______________________________________________________________________________
const char *RooDoubleCB::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooDoubleCB*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooDoubleCB::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooDoubleCB*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooDoubleCB::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooDoubleCB*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooDoubleCB::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooDoubleCB*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooFermi::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooFermi::Class_Name()
{
   return "RooFermi";
}

//______________________________________________________________________________
const char *RooFermi::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooFermi*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooFermi::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooFermi*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooFermi::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooFermi*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooFermi::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooFermi*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooRelBW::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooRelBW::Class_Name()
{
   return "RooRelBW";
}

//______________________________________________________________________________
const char *RooRelBW::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooRelBW*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooRelBW::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooRelBW*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooRelBW::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooRelBW*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooRelBW::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooRelBW*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr Triangle::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *Triangle::Class_Name()
{
   return "Triangle";
}

//______________________________________________________________________________
const char *Triangle::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::Triangle*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int Triangle::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::Triangle*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *Triangle::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::Triangle*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *Triangle::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::Triangle*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooLevelledExp::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooLevelledExp::Class_Name()
{
   return "RooLevelledExp";
}

//______________________________________________________________________________
const char *RooLevelledExp::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooLevelledExp*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooLevelledExp::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooLevelledExp*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooLevelledExp::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooLevelledExp*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooLevelledExp::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooLevelledExp*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooPower::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooPower::Class_Name()
{
   return "RooPower";
}

//______________________________________________________________________________
const char *RooPower::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooPower*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooPower::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooPower*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooPower::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooPower*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooPower::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooPower*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooStepBernstein::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooStepBernstein::Class_Name()
{
   return "RooStepBernstein";
}

//______________________________________________________________________________
const char *RooStepBernstein::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooStepBernstein*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooStepBernstein::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooStepBernstein*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooStepBernstein::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooStepBernstein*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooStepBernstein::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooStepBernstein*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooGaussStepBernstein::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooGaussStepBernstein::Class_Name()
{
   return "RooGaussStepBernstein";
}

//______________________________________________________________________________
const char *RooGaussStepBernstein::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooGaussStepBernstein*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooGaussStepBernstein::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooGaussStepBernstein*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooGaussStepBernstein::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooGaussStepBernstein*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooGaussStepBernstein::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooGaussStepBernstein*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr ProcessNormalization::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *ProcessNormalization::Class_Name()
{
   return "ProcessNormalization";
}

//______________________________________________________________________________
const char *ProcessNormalization::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProcessNormalization*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int ProcessNormalization::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProcessNormalization*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *ProcessNormalization::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProcessNormalization*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *ProcessNormalization::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProcessNormalization*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooRealFlooredSumPdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooRealFlooredSumPdf::Class_Name()
{
   return "RooRealFlooredSumPdf";
}

//______________________________________________________________________________
const char *RooRealFlooredSumPdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooRealFlooredSumPdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooRealFlooredSumPdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooRealFlooredSumPdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooRealFlooredSumPdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooRealFlooredSumPdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooRealFlooredSumPdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooRealFlooredSumPdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooSpline1D::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooSpline1D::Class_Name()
{
   return "RooSpline1D";
}

//______________________________________________________________________________
const char *RooSpline1D::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooSpline1D*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooSpline1D::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooSpline1D*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooSpline1D::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooSpline1D*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooSpline1D::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooSpline1D*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooSplineND::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooSplineND::Class_Name()
{
   return "RooSplineND";
}

//______________________________________________________________________________
const char *RooSplineND::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooSplineND*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooSplineND::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooSplineND*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooSplineND::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooSplineND*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooSplineND::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooSplineND*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooScaleLOSM::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooScaleLOSM::Class_Name()
{
   return "RooScaleLOSM";
}

//______________________________________________________________________________
const char *RooScaleLOSM::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooScaleLOSM*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooScaleLOSM::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooScaleLOSM*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooScaleLOSM::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooScaleLOSM*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooScaleLOSM::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooScaleLOSM*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooScaleHGamGamLOSM::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooScaleHGamGamLOSM::Class_Name()
{
   return "RooScaleHGamGamLOSM";
}

//______________________________________________________________________________
const char *RooScaleHGamGamLOSM::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooScaleHGamGamLOSM*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooScaleHGamGamLOSM::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooScaleHGamGamLOSM*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooScaleHGamGamLOSM::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooScaleHGamGamLOSM*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooScaleHGamGamLOSM::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooScaleHGamGamLOSM*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooScaleHGluGluLOSM::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooScaleHGluGluLOSM::Class_Name()
{
   return "RooScaleHGluGluLOSM";
}

//______________________________________________________________________________
const char *RooScaleHGluGluLOSM::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooScaleHGluGluLOSM*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooScaleHGluGluLOSM::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooScaleHGluGluLOSM*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooScaleHGluGluLOSM::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooScaleHGluGluLOSM*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooScaleHGluGluLOSM::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooScaleHGluGluLOSM*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooScaleHGamGamLOSMPlusX::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooScaleHGamGamLOSMPlusX::Class_Name()
{
   return "RooScaleHGamGamLOSMPlusX";
}

//______________________________________________________________________________
const char *RooScaleHGamGamLOSMPlusX::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooScaleHGamGamLOSMPlusX*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooScaleHGamGamLOSMPlusX::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooScaleHGamGamLOSMPlusX*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooScaleHGamGamLOSMPlusX::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooScaleHGamGamLOSMPlusX*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooScaleHGamGamLOSMPlusX::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooScaleHGamGamLOSMPlusX*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooScaleHGluGluLOSMPlusX::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooScaleHGluGluLOSMPlusX::Class_Name()
{
   return "RooScaleHGluGluLOSMPlusX";
}

//______________________________________________________________________________
const char *RooScaleHGluGluLOSMPlusX::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooScaleHGluGluLOSMPlusX*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooScaleHGluGluLOSMPlusX::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooScaleHGluGluLOSMPlusX*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooScaleHGluGluLOSMPlusX::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooScaleHGluGluLOSMPlusX*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooScaleHGluGluLOSMPlusX::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooScaleHGluGluLOSMPlusX*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr rVrFLikelihood::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *rVrFLikelihood::Class_Name()
{
   return "rVrFLikelihood";
}

//______________________________________________________________________________
const char *rVrFLikelihood::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::rVrFLikelihood*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int rVrFLikelihood::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::rVrFLikelihood*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *rVrFLikelihood::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::rVrFLikelihood*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *rVrFLikelihood::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::rVrFLikelihood*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooMultiPdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooMultiPdf::Class_Name()
{
   return "RooMultiPdf";
}

//______________________________________________________________________________
const char *RooMultiPdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooMultiPdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooMultiPdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooMultiPdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooMultiPdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooMultiPdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooMultiPdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooMultiPdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr RooBernsteinFast<1>::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *RooBernsteinFast<1>::Class_Name()
{
   return "RooBernsteinFast<1>";
}

//______________________________________________________________________________
template <> const char *RooBernsteinFast<1>::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooBernsteinFast<1>*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int RooBernsteinFast<1>::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooBernsteinFast<1>*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *RooBernsteinFast<1>::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooBernsteinFast<1>*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *RooBernsteinFast<1>::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooBernsteinFast<1>*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr RooBernsteinFast<2>::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *RooBernsteinFast<2>::Class_Name()
{
   return "RooBernsteinFast<2>";
}

//______________________________________________________________________________
template <> const char *RooBernsteinFast<2>::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooBernsteinFast<2>*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int RooBernsteinFast<2>::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooBernsteinFast<2>*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *RooBernsteinFast<2>::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooBernsteinFast<2>*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *RooBernsteinFast<2>::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooBernsteinFast<2>*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr RooBernsteinFast<3>::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *RooBernsteinFast<3>::Class_Name()
{
   return "RooBernsteinFast<3>";
}

//______________________________________________________________________________
template <> const char *RooBernsteinFast<3>::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooBernsteinFast<3>*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int RooBernsteinFast<3>::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooBernsteinFast<3>*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *RooBernsteinFast<3>::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooBernsteinFast<3>*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *RooBernsteinFast<3>::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooBernsteinFast<3>*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr RooBernsteinFast<4>::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *RooBernsteinFast<4>::Class_Name()
{
   return "RooBernsteinFast<4>";
}

//______________________________________________________________________________
template <> const char *RooBernsteinFast<4>::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooBernsteinFast<4>*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int RooBernsteinFast<4>::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooBernsteinFast<4>*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *RooBernsteinFast<4>::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooBernsteinFast<4>*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *RooBernsteinFast<4>::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooBernsteinFast<4>*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr RooBernsteinFast<5>::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *RooBernsteinFast<5>::Class_Name()
{
   return "RooBernsteinFast<5>";
}

//______________________________________________________________________________
template <> const char *RooBernsteinFast<5>::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooBernsteinFast<5>*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int RooBernsteinFast<5>::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooBernsteinFast<5>*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *RooBernsteinFast<5>::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooBernsteinFast<5>*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *RooBernsteinFast<5>::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooBernsteinFast<5>*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr RooBernsteinFast<6>::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *RooBernsteinFast<6>::Class_Name()
{
   return "RooBernsteinFast<6>";
}

//______________________________________________________________________________
template <> const char *RooBernsteinFast<6>::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooBernsteinFast<6>*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int RooBernsteinFast<6>::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooBernsteinFast<6>*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *RooBernsteinFast<6>::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooBernsteinFast<6>*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *RooBernsteinFast<6>::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooBernsteinFast<6>*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr RooBernsteinFast<7>::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *RooBernsteinFast<7>::Class_Name()
{
   return "RooBernsteinFast<7>";
}

//______________________________________________________________________________
template <> const char *RooBernsteinFast<7>::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooBernsteinFast<7>*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int RooBernsteinFast<7>::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooBernsteinFast<7>*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *RooBernsteinFast<7>::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooBernsteinFast<7>*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *RooBernsteinFast<7>::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooBernsteinFast<7>*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr SimpleGaussianConstraint::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *SimpleGaussianConstraint::Class_Name()
{
   return "SimpleGaussianConstraint";
}

//______________________________________________________________________________
const char *SimpleGaussianConstraint::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SimpleGaussianConstraint*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int SimpleGaussianConstraint::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SimpleGaussianConstraint*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *SimpleGaussianConstraint::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SimpleGaussianConstraint*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *SimpleGaussianConstraint::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SimpleGaussianConstraint*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr SimplePoissonConstraint::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *SimplePoissonConstraint::Class_Name()
{
   return "SimplePoissonConstraint";
}

//______________________________________________________________________________
const char *SimplePoissonConstraint::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SimplePoissonConstraint*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int SimplePoissonConstraint::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SimplePoissonConstraint*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *SimplePoissonConstraint::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SimplePoissonConstraint*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *SimplePoissonConstraint::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SimplePoissonConstraint*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr SimpleConstraintGroup::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *SimpleConstraintGroup::Class_Name()
{
   return "SimpleConstraintGroup";
}

//______________________________________________________________________________
const char *SimpleConstraintGroup::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SimpleConstraintGroup*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int SimpleConstraintGroup::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SimpleConstraintGroup*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *SimpleConstraintGroup::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SimpleConstraintGroup*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *SimpleConstraintGroup::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SimpleConstraintGroup*)0x0)->GetClass(); }
   return fgIsA;
}

namespace RooStats {
   namespace HistFactory {
//______________________________________________________________________________
atomic_TClass_ptr RooBSplineBases::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooBSplineBases::Class_Name()
{
   return "RooStats::HistFactory::RooBSplineBases";
}

//______________________________________________________________________________
const char *RooBSplineBases::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooStats::HistFactory::RooBSplineBases*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooBSplineBases::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooStats::HistFactory::RooBSplineBases*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooBSplineBases::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooStats::HistFactory::RooBSplineBases*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooBSplineBases::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooStats::HistFactory::RooBSplineBases*)0x0)->GetClass(); }
   return fgIsA;
}

} // namespace RooStats::HistFactory
} // namespace RooStats::HistFactory
namespace RooStats {
   namespace HistFactory {
//______________________________________________________________________________
atomic_TClass_ptr RooBSpline::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooBSpline::Class_Name()
{
   return "RooStats::HistFactory::RooBSpline";
}

//______________________________________________________________________________
const char *RooBSpline::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooStats::HistFactory::RooBSpline*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooBSpline::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooStats::HistFactory::RooBSpline*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooBSpline::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooStats::HistFactory::RooBSpline*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooBSpline::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooStats::HistFactory::RooBSpline*)0x0)->GetClass(); }
   return fgIsA;
}

} // namespace RooStats::HistFactory
} // namespace RooStats::HistFactory
//______________________________________________________________________________
atomic_TClass_ptr RooParamKeysPdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooParamKeysPdf::Class_Name()
{
   return "RooParamKeysPdf";
}

//______________________________________________________________________________
const char *RooParamKeysPdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooParamKeysPdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooParamKeysPdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooParamKeysPdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooParamKeysPdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooParamKeysPdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooParamKeysPdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooParamKeysPdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooStarMomentMorph::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooStarMomentMorph::Class_Name()
{
   return "RooStarMomentMorph";
}

//______________________________________________________________________________
const char *RooStarMomentMorph::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooStarMomentMorph*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooStarMomentMorph::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooStarMomentMorph*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooStarMomentMorph::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooStarMomentMorph*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooStarMomentMorph::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooStarMomentMorph*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr FastTemplateFunc_t<float>::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *FastTemplateFunc_t<float>::Class_Name()
{
   return "FastTemplateFunc_t<float>";
}

//______________________________________________________________________________
template <> const char *FastTemplateFunc_t<float>::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::FastTemplateFunc_t<float>*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int FastTemplateFunc_t<float>::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::FastTemplateFunc_t<float>*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *FastTemplateFunc_t<float>::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::FastTemplateFunc_t<float>*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *FastTemplateFunc_t<float>::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::FastTemplateFunc_t<float>*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr FastTemplateFunc_t<double>::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *FastTemplateFunc_t<double>::Class_Name()
{
   return "FastTemplateFunc_t<double>";
}

//______________________________________________________________________________
template <> const char *FastTemplateFunc_t<double>::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::FastTemplateFunc_t<double>*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int FastTemplateFunc_t<double>::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::FastTemplateFunc_t<double>*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *FastTemplateFunc_t<double>::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::FastTemplateFunc_t<double>*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *FastTemplateFunc_t<double>::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::FastTemplateFunc_t<double>*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr FastHistoFunc_t<float,double>::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *FastHistoFunc_t<float,double>::Class_Name()
{
   return "FastHistoFunc_t<float,double>";
}

//______________________________________________________________________________
template <> const char *FastHistoFunc_t<float,double>::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::FastHistoFunc_t<float,double>*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int FastHistoFunc_t<float,double>::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::FastHistoFunc_t<float,double>*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *FastHistoFunc_t<float,double>::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::FastHistoFunc_t<float,double>*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *FastHistoFunc_t<float,double>::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::FastHistoFunc_t<float,double>*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr FastHistoFunc_t<double,double>::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *FastHistoFunc_t<double,double>::Class_Name()
{
   return "FastHistoFunc_t<double,double>";
}

//______________________________________________________________________________
template <> const char *FastHistoFunc_t<double,double>::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::FastHistoFunc_t<double,double>*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int FastHistoFunc_t<double,double>::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::FastHistoFunc_t<double,double>*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *FastHistoFunc_t<double,double>::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::FastHistoFunc_t<double,double>*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *FastHistoFunc_t<double,double>::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::FastHistoFunc_t<double,double>*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr FastHisto2DFunc_t<float,double>::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *FastHisto2DFunc_t<float,double>::Class_Name()
{
   return "FastHisto2DFunc_t<float,double>";
}

//______________________________________________________________________________
template <> const char *FastHisto2DFunc_t<float,double>::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::FastHisto2DFunc_t<float,double>*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int FastHisto2DFunc_t<float,double>::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::FastHisto2DFunc_t<float,double>*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *FastHisto2DFunc_t<float,double>::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::FastHisto2DFunc_t<float,double>*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *FastHisto2DFunc_t<float,double>::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::FastHisto2DFunc_t<float,double>*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr FastHisto2DFunc_t<double,double>::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *FastHisto2DFunc_t<double,double>::Class_Name()
{
   return "FastHisto2DFunc_t<double,double>";
}

//______________________________________________________________________________
template <> const char *FastHisto2DFunc_t<double,double>::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::FastHisto2DFunc_t<double,double>*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int FastHisto2DFunc_t<double,double>::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::FastHisto2DFunc_t<double,double>*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *FastHisto2DFunc_t<double,double>::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::FastHisto2DFunc_t<double,double>*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *FastHisto2DFunc_t<double,double>::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::FastHisto2DFunc_t<double,double>*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr FastHisto3DFunc_t<float,double>::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *FastHisto3DFunc_t<float,double>::Class_Name()
{
   return "FastHisto3DFunc_t<float,double>";
}

//______________________________________________________________________________
template <> const char *FastHisto3DFunc_t<float,double>::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::FastHisto3DFunc_t<float,double>*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int FastHisto3DFunc_t<float,double>::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::FastHisto3DFunc_t<float,double>*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *FastHisto3DFunc_t<float,double>::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::FastHisto3DFunc_t<float,double>*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *FastHisto3DFunc_t<float,double>::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::FastHisto3DFunc_t<float,double>*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr FastHisto3DFunc_t<double,double>::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *FastHisto3DFunc_t<double,double>::Class_Name()
{
   return "FastHisto3DFunc_t<double,double>";
}

//______________________________________________________________________________
template <> const char *FastHisto3DFunc_t<double,double>::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::FastHisto3DFunc_t<double,double>*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int FastHisto3DFunc_t<double,double>::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::FastHisto3DFunc_t<double,double>*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *FastHisto3DFunc_t<double,double>::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::FastHisto3DFunc_t<double,double>*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *FastHisto3DFunc_t<double,double>::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::FastHisto3DFunc_t<double,double>*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr HZZ4L_RooSpinZeroPdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *HZZ4L_RooSpinZeroPdf::Class_Name()
{
   return "HZZ4L_RooSpinZeroPdf";
}

//______________________________________________________________________________
const char *HZZ4L_RooSpinZeroPdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooSpinZeroPdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int HZZ4L_RooSpinZeroPdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooSpinZeroPdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *HZZ4L_RooSpinZeroPdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooSpinZeroPdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *HZZ4L_RooSpinZeroPdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooSpinZeroPdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr HZZ4L_RooSpinZeroPdf_1D::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *HZZ4L_RooSpinZeroPdf_1D::Class_Name()
{
   return "HZZ4L_RooSpinZeroPdf_1D";
}

//______________________________________________________________________________
const char *HZZ4L_RooSpinZeroPdf_1D::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooSpinZeroPdf_1D*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int HZZ4L_RooSpinZeroPdf_1D::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooSpinZeroPdf_1D*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *HZZ4L_RooSpinZeroPdf_1D::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooSpinZeroPdf_1D*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *HZZ4L_RooSpinZeroPdf_1D::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooSpinZeroPdf_1D*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr HZZ4L_RooSpinZeroPdf_2D::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *HZZ4L_RooSpinZeroPdf_2D::Class_Name()
{
   return "HZZ4L_RooSpinZeroPdf_2D";
}

//______________________________________________________________________________
const char *HZZ4L_RooSpinZeroPdf_2D::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooSpinZeroPdf_2D*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int HZZ4L_RooSpinZeroPdf_2D::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooSpinZeroPdf_2D*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *HZZ4L_RooSpinZeroPdf_2D::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooSpinZeroPdf_2D*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *HZZ4L_RooSpinZeroPdf_2D::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooSpinZeroPdf_2D*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr HZZ4L_RooSpinZeroPdf_phase::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *HZZ4L_RooSpinZeroPdf_phase::Class_Name()
{
   return "HZZ4L_RooSpinZeroPdf_phase";
}

//______________________________________________________________________________
const char *HZZ4L_RooSpinZeroPdf_phase::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooSpinZeroPdf_phase*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int HZZ4L_RooSpinZeroPdf_phase::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooSpinZeroPdf_phase*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *HZZ4L_RooSpinZeroPdf_phase::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooSpinZeroPdf_phase*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *HZZ4L_RooSpinZeroPdf_phase::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooSpinZeroPdf_phase*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr VBFHZZ4L_RooSpinZeroPdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *VBFHZZ4L_RooSpinZeroPdf::Class_Name()
{
   return "VBFHZZ4L_RooSpinZeroPdf";
}

//______________________________________________________________________________
const char *VBFHZZ4L_RooSpinZeroPdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::VBFHZZ4L_RooSpinZeroPdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int VBFHZZ4L_RooSpinZeroPdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::VBFHZZ4L_RooSpinZeroPdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *VBFHZZ4L_RooSpinZeroPdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::VBFHZZ4L_RooSpinZeroPdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *VBFHZZ4L_RooSpinZeroPdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::VBFHZZ4L_RooSpinZeroPdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr VBFHZZ4L_RooSpinZeroPdf_fast::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *VBFHZZ4L_RooSpinZeroPdf_fast::Class_Name()
{
   return "VBFHZZ4L_RooSpinZeroPdf_fast";
}

//______________________________________________________________________________
const char *VBFHZZ4L_RooSpinZeroPdf_fast::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::VBFHZZ4L_RooSpinZeroPdf_fast*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int VBFHZZ4L_RooSpinZeroPdf_fast::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::VBFHZZ4L_RooSpinZeroPdf_fast*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *VBFHZZ4L_RooSpinZeroPdf_fast::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::VBFHZZ4L_RooSpinZeroPdf_fast*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *VBFHZZ4L_RooSpinZeroPdf_fast::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::VBFHZZ4L_RooSpinZeroPdf_fast*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr HZZ4L_RooSpinZeroPdf_1D_fast::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *HZZ4L_RooSpinZeroPdf_1D_fast::Class_Name()
{
   return "HZZ4L_RooSpinZeroPdf_1D_fast";
}

//______________________________________________________________________________
const char *HZZ4L_RooSpinZeroPdf_1D_fast::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooSpinZeroPdf_1D_fast*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int HZZ4L_RooSpinZeroPdf_1D_fast::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooSpinZeroPdf_1D_fast*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *HZZ4L_RooSpinZeroPdf_1D_fast::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooSpinZeroPdf_1D_fast*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *HZZ4L_RooSpinZeroPdf_1D_fast::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooSpinZeroPdf_1D_fast*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr HZZ4L_RooSpinZeroPdf_2D_fast::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *HZZ4L_RooSpinZeroPdf_2D_fast::Class_Name()
{
   return "HZZ4L_RooSpinZeroPdf_2D_fast";
}

//______________________________________________________________________________
const char *HZZ4L_RooSpinZeroPdf_2D_fast::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooSpinZeroPdf_2D_fast*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int HZZ4L_RooSpinZeroPdf_2D_fast::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooSpinZeroPdf_2D_fast*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *HZZ4L_RooSpinZeroPdf_2D_fast::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooSpinZeroPdf_2D_fast*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *HZZ4L_RooSpinZeroPdf_2D_fast::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooSpinZeroPdf_2D_fast*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr HZZ4L_RooSpinZeroPdf_phase_fast::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *HZZ4L_RooSpinZeroPdf_phase_fast::Class_Name()
{
   return "HZZ4L_RooSpinZeroPdf_phase_fast";
}

//______________________________________________________________________________
const char *HZZ4L_RooSpinZeroPdf_phase_fast::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooSpinZeroPdf_phase_fast*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int HZZ4L_RooSpinZeroPdf_phase_fast::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooSpinZeroPdf_phase_fast*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *HZZ4L_RooSpinZeroPdf_phase_fast::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooSpinZeroPdf_phase_fast*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *HZZ4L_RooSpinZeroPdf_phase_fast::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::HZZ4L_RooSpinZeroPdf_phase_fast*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr VVHZZ4L_RooSpinZeroPdf_1D_fast::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *VVHZZ4L_RooSpinZeroPdf_1D_fast::Class_Name()
{
   return "VVHZZ4L_RooSpinZeroPdf_1D_fast";
}

//______________________________________________________________________________
const char *VVHZZ4L_RooSpinZeroPdf_1D_fast::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::VVHZZ4L_RooSpinZeroPdf_1D_fast*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int VVHZZ4L_RooSpinZeroPdf_1D_fast::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::VVHZZ4L_RooSpinZeroPdf_1D_fast*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *VVHZZ4L_RooSpinZeroPdf_1D_fast::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::VVHZZ4L_RooSpinZeroPdf_1D_fast*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *VVHZZ4L_RooSpinZeroPdf_1D_fast::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::VVHZZ4L_RooSpinZeroPdf_1D_fast*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooChebyshevPDF::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooChebyshevPDF::Class_Name()
{
   return "RooChebyshevPDF";
}

//______________________________________________________________________________
const char *RooChebyshevPDF::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooChebyshevPDF*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooChebyshevPDF::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooChebyshevPDF*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooChebyshevPDF::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooChebyshevPDF*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooChebyshevPDF::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooChebyshevPDF*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooErfPdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooErfPdf::Class_Name()
{
   return "RooErfPdf";
}

//______________________________________________________________________________
const char *RooErfPdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooErfPdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooErfPdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooErfPdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooErfPdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooErfPdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooErfPdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooErfPdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooPowerExpPdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooPowerExpPdf::Class_Name()
{
   return "RooPowerExpPdf";
}

//______________________________________________________________________________
const char *RooPowerExpPdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooPowerExpPdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooPowerExpPdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooPowerExpPdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooPowerExpPdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooPowerExpPdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooPowerExpPdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooPowerExpPdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooTH1DPdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooTH1DPdf::Class_Name()
{
   return "RooTH1DPdf";
}

//______________________________________________________________________________
const char *RooTH1DPdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooTH1DPdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooTH1DPdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooTH1DPdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooTH1DPdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooTH1DPdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooTH1DPdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooTH1DPdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooPowerFunction::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooPowerFunction::Class_Name()
{
   return "RooPowerFunction";
}

//______________________________________________________________________________
const char *RooPowerFunction::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooPowerFunction*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooPowerFunction::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooPowerFunction*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooPowerFunction::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooPowerFunction*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooPowerFunction::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooPowerFunction*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooPowerLaw::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooPowerLaw::Class_Name()
{
   return "RooPowerLaw";
}

//______________________________________________________________________________
const char *RooPowerLaw::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooPowerLaw*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooPowerLaw::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooPowerLaw*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooPowerLaw::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooPowerLaw*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooPowerLaw::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooPowerLaw*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooExpPoly::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooExpPoly::Class_Name()
{
   return "RooExpPoly";
}

//______________________________________________________________________________
const char *RooExpPoly::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooExpPoly*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooExpPoly::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooExpPoly*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooExpPoly::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooExpPoly*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooExpPoly::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooExpPoly*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooMorphingPdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooMorphingPdf::Class_Name()
{
   return "RooMorphingPdf";
}

//______________________________________________________________________________
const char *RooMorphingPdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooMorphingPdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooMorphingPdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooMorphingPdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooMorphingPdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooMorphingPdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooMorphingPdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooMorphingPdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooParametricHist::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooParametricHist::Class_Name()
{
   return "RooParametricHist";
}

//______________________________________________________________________________
const char *RooParametricHist::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooParametricHist*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooParametricHist::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooParametricHist*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooParametricHist::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooParametricHist*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooParametricHist::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooParametricHist*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooParametricShapeBinPdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooParametricShapeBinPdf::Class_Name()
{
   return "RooParametricShapeBinPdf";
}

//______________________________________________________________________________
const char *RooParametricShapeBinPdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooParametricShapeBinPdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooParametricShapeBinPdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooParametricShapeBinPdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooParametricShapeBinPdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooParametricShapeBinPdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooParametricShapeBinPdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooParametricShapeBinPdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr GaussExp::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *GaussExp::Class_Name()
{
   return "GaussExp";
}

//______________________________________________________________________________
const char *GaussExp::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::GaussExp*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int GaussExp::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::GaussExp*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *GaussExp::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::GaussExp*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *GaussExp::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::GaussExp*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooDoubleCBFast::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooDoubleCBFast::Class_Name()
{
   return "RooDoubleCBFast";
}

//______________________________________________________________________________
const char *RooDoubleCBFast::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooDoubleCBFast*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooDoubleCBFast::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooDoubleCBFast*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooDoubleCBFast::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooDoubleCBFast*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooDoubleCBFast::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooDoubleCBFast*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr CMSHistFunc::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *CMSHistFunc::Class_Name()
{
   return "CMSHistFunc";
}

//______________________________________________________________________________
const char *CMSHistFunc::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::CMSHistFunc*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int CMSHistFunc::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::CMSHistFunc*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *CMSHistFunc::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::CMSHistFunc*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *CMSHistFunc::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::CMSHistFunc*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr CMSHistErrorPropagator::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *CMSHistErrorPropagator::Class_Name()
{
   return "CMSHistErrorPropagator";
}

//______________________________________________________________________________
const char *CMSHistErrorPropagator::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::CMSHistErrorPropagator*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int CMSHistErrorPropagator::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::CMSHistErrorPropagator*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *CMSHistErrorPropagator::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::CMSHistErrorPropagator*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *CMSHistErrorPropagator::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::CMSHistErrorPropagator*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr CMSHistFuncWrapper::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *CMSHistFuncWrapper::Class_Name()
{
   return "CMSHistFuncWrapper";
}

//______________________________________________________________________________
const char *CMSHistFuncWrapper::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::CMSHistFuncWrapper*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int CMSHistFuncWrapper::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::CMSHistFuncWrapper*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *CMSHistFuncWrapper::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::CMSHistFuncWrapper*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *CMSHistFuncWrapper::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::CMSHistFuncWrapper*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooTaylorExpansion::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooTaylorExpansion::Class_Name()
{
   return "RooTaylorExpansion";
}

//______________________________________________________________________________
const char *RooTaylorExpansion::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooTaylorExpansion*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooTaylorExpansion::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooTaylorExpansion*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooTaylorExpansion::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooTaylorExpansion*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooTaylorExpansion::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooTaylorExpansion*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr SimpleTaylorExpansion1D::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *SimpleTaylorExpansion1D::Class_Name()
{
   return "SimpleTaylorExpansion1D";
}

//______________________________________________________________________________
const char *SimpleTaylorExpansion1D::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SimpleTaylorExpansion1D*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int SimpleTaylorExpansion1D::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SimpleTaylorExpansion1D*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *SimpleTaylorExpansion1D::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SimpleTaylorExpansion1D*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *SimpleTaylorExpansion1D::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SimpleTaylorExpansion1D*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooPiecewisePolynomial::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooPiecewisePolynomial::Class_Name()
{
   return "RooPiecewisePolynomial";
}

//______________________________________________________________________________
const char *RooPiecewisePolynomial::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooPiecewisePolynomial*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooPiecewisePolynomial::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooPiecewisePolynomial*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooPiecewisePolynomial::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooPiecewisePolynomial*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooPiecewisePolynomial::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooPiecewisePolynomial*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooNCSplineCore::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooNCSplineCore::Class_Name()
{
   return "RooNCSplineCore";
}

//______________________________________________________________________________
const char *RooNCSplineCore::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooNCSplineCore*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooNCSplineCore::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooNCSplineCore*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooNCSplineCore::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooNCSplineCore*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooNCSplineCore::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooNCSplineCore*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooNCSpline_1D_fast::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooNCSpline_1D_fast::Class_Name()
{
   return "RooNCSpline_1D_fast";
}

//______________________________________________________________________________
const char *RooNCSpline_1D_fast::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooNCSpline_1D_fast*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooNCSpline_1D_fast::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooNCSpline_1D_fast*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooNCSpline_1D_fast::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooNCSpline_1D_fast*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooNCSpline_1D_fast::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooNCSpline_1D_fast*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooNCSpline_2D_fast::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooNCSpline_2D_fast::Class_Name()
{
   return "RooNCSpline_2D_fast";
}

//______________________________________________________________________________
const char *RooNCSpline_2D_fast::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooNCSpline_2D_fast*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooNCSpline_2D_fast::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooNCSpline_2D_fast*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooNCSpline_2D_fast::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooNCSpline_2D_fast*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooNCSpline_2D_fast::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooNCSpline_2D_fast*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooNCSpline_3D_fast::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooNCSpline_3D_fast::Class_Name()
{
   return "RooNCSpline_3D_fast";
}

//______________________________________________________________________________
const char *RooNCSpline_3D_fast::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooNCSpline_3D_fast*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooNCSpline_3D_fast::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooNCSpline_3D_fast*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooNCSpline_3D_fast::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooNCSpline_3D_fast*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooNCSpline_3D_fast::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooNCSpline_3D_fast*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooFuncPdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooFuncPdf::Class_Name()
{
   return "RooFuncPdf";
}

//______________________________________________________________________________
const char *RooFuncPdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooFuncPdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooFuncPdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooFuncPdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooFuncPdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooFuncPdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooFuncPdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooFuncPdf*)0x0)->GetClass(); }
   return fgIsA;
}

namespace ROOT {
   // Wrappers around operator new
   static void *new___gnu_cxxcLcL__normal_iteratorlEvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<vector<double>*,vector<vector<double> > > : new ::__gnu_cxx::__normal_iterator<vector<double>*,vector<vector<double> > >;
   }
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<vector<double>*,vector<vector<double> > >[nElements] : new ::__gnu_cxx::__normal_iterator<vector<double>*,vector<vector<double> > >[nElements];
   }
   // Wrapper around operator delete
   static void delete___gnu_cxxcLcL__normal_iteratorlEvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR(void *p) {
      delete ((::__gnu_cxx::__normal_iterator<vector<double>*,vector<vector<double> > >*)p);
   }
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR(void *p) {
      delete [] ((::__gnu_cxx::__normal_iterator<vector<double>*,vector<vector<double> > >*)p);
   }
   static void destruct___gnu_cxxcLcL__normal_iteratorlEvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR(void *p) {
      typedef ::__gnu_cxx::__normal_iterator<vector<double>*,vector<vector<double> > > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::__gnu_cxx::__normal_iterator<vector<double>*,vector<vector<double> > >

namespace ROOT {
   // Wrappers around operator new
   static void *new___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<const vector<double>*,vector<vector<double> > > : new ::__gnu_cxx::__normal_iterator<const vector<double>*,vector<vector<double> > >;
   }
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<const vector<double>*,vector<vector<double> > >[nElements] : new ::__gnu_cxx::__normal_iterator<const vector<double>*,vector<vector<double> > >[nElements];
   }
   // Wrapper around operator delete
   static void delete___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR(void *p) {
      delete ((::__gnu_cxx::__normal_iterator<const vector<double>*,vector<vector<double> > >*)p);
   }
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR(void *p) {
      delete [] ((::__gnu_cxx::__normal_iterator<const vector<double>*,vector<vector<double> > >*)p);
   }
   static void destruct___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEdoublegRmUcOvectorlEvectorlEdoublegRsPgRsPgR(void *p) {
      typedef ::__gnu_cxx::__normal_iterator<const vector<double>*,vector<vector<double> > > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::__gnu_cxx::__normal_iterator<const vector<double>*,vector<vector<double> > >

namespace ROOT {
   // Wrappers around operator new
   static void *new___gnu_cxxcLcL__normal_iteratorlEvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<vector<float>*,vector<vector<float> > > : new ::__gnu_cxx::__normal_iterator<vector<float>*,vector<vector<float> > >;
   }
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<vector<float>*,vector<vector<float> > >[nElements] : new ::__gnu_cxx::__normal_iterator<vector<float>*,vector<vector<float> > >[nElements];
   }
   // Wrapper around operator delete
   static void delete___gnu_cxxcLcL__normal_iteratorlEvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR(void *p) {
      delete ((::__gnu_cxx::__normal_iterator<vector<float>*,vector<vector<float> > >*)p);
   }
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR(void *p) {
      delete [] ((::__gnu_cxx::__normal_iterator<vector<float>*,vector<vector<float> > >*)p);
   }
   static void destruct___gnu_cxxcLcL__normal_iteratorlEvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR(void *p) {
      typedef ::__gnu_cxx::__normal_iterator<vector<float>*,vector<vector<float> > > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::__gnu_cxx::__normal_iterator<vector<float>*,vector<vector<float> > >

namespace ROOT {
   // Wrappers around operator new
   static void *new___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<const vector<float>*,vector<vector<float> > > : new ::__gnu_cxx::__normal_iterator<const vector<float>*,vector<vector<float> > >;
   }
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<const vector<float>*,vector<vector<float> > >[nElements] : new ::__gnu_cxx::__normal_iterator<const vector<float>*,vector<vector<float> > >[nElements];
   }
   // Wrapper around operator delete
   static void delete___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR(void *p) {
      delete ((::__gnu_cxx::__normal_iterator<const vector<float>*,vector<vector<float> > >*)p);
   }
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR(void *p) {
      delete [] ((::__gnu_cxx::__normal_iterator<const vector<float>*,vector<vector<float> > >*)p);
   }
   static void destruct___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEfloatgRmUcOvectorlEvectorlEfloatgRsPgRsPgR(void *p) {
      typedef ::__gnu_cxx::__normal_iterator<const vector<float>*,vector<vector<float> > > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::__gnu_cxx::__normal_iterator<const vector<float>*,vector<vector<float> > >

namespace ROOT {
   // Wrappers around operator new
   static void *new___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > > : new ::__gnu_cxx::__normal_iterator<vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > >;
   }
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > >[nElements] : new ::__gnu_cxx::__normal_iterator<vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > >[nElements];
   }
   // Wrapper around operator delete
   static void delete___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR(void *p) {
      delete ((::__gnu_cxx::__normal_iterator<vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > >*)p);
   }
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR(void *p) {
      delete [] ((::__gnu_cxx::__normal_iterator<vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > >*)p);
   }
   static void destruct___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR(void *p) {
      typedef ::__gnu_cxx::__normal_iterator<vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::__gnu_cxx::__normal_iterator<vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > >

namespace ROOT {
   // Wrappers around operator new
   static void *new___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<const vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > > : new ::__gnu_cxx::__normal_iterator<const vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > >;
   }
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<const vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > >[nElements] : new ::__gnu_cxx::__normal_iterator<const vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > >[nElements];
   }
   // Wrapper around operator delete
   static void delete___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR(void *p) {
      delete ((::__gnu_cxx::__normal_iterator<const vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > >*)p);
   }
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR(void *p) {
      delete [] ((::__gnu_cxx::__normal_iterator<const vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > >*)p);
   }
   static void destruct___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEfloatgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR(void *p) {
      typedef ::__gnu_cxx::__normal_iterator<const vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::__gnu_cxx::__normal_iterator<const vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > >

namespace ROOT {
   // Wrappers around operator new
   static void *new___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<vector<vector<float> >*,vector<vector<vector<float> > > > : new ::__gnu_cxx::__normal_iterator<vector<vector<float> >*,vector<vector<vector<float> > > >;
   }
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<vector<vector<float> >*,vector<vector<vector<float> > > >[nElements] : new ::__gnu_cxx::__normal_iterator<vector<vector<float> >*,vector<vector<vector<float> > > >[nElements];
   }
   // Wrapper around operator delete
   static void delete___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR(void *p) {
      delete ((::__gnu_cxx::__normal_iterator<vector<vector<float> >*,vector<vector<vector<float> > > >*)p);
   }
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR(void *p) {
      delete [] ((::__gnu_cxx::__normal_iterator<vector<vector<float> >*,vector<vector<vector<float> > > >*)p);
   }
   static void destruct___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR(void *p) {
      typedef ::__gnu_cxx::__normal_iterator<vector<vector<float> >*,vector<vector<vector<float> > > > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::__gnu_cxx::__normal_iterator<vector<vector<float> >*,vector<vector<vector<float> > > >

namespace ROOT {
   // Wrappers around operator new
   static void *new___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<const vector<vector<float> >*,vector<vector<vector<float> > > > : new ::__gnu_cxx::__normal_iterator<const vector<vector<float> >*,vector<vector<vector<float> > > >;
   }
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<const vector<vector<float> >*,vector<vector<vector<float> > > >[nElements] : new ::__gnu_cxx::__normal_iterator<const vector<vector<float> >*,vector<vector<vector<float> > > >[nElements];
   }
   // Wrapper around operator delete
   static void delete___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR(void *p) {
      delete ((::__gnu_cxx::__normal_iterator<const vector<vector<float> >*,vector<vector<vector<float> > > >*)p);
   }
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR(void *p) {
      delete [] ((::__gnu_cxx::__normal_iterator<const vector<vector<float> >*,vector<vector<vector<float> > > >*)p);
   }
   static void destruct___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEfloatgRsPgRmUcOvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR(void *p) {
      typedef ::__gnu_cxx::__normal_iterator<const vector<vector<float> >*,vector<vector<vector<float> > > > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::__gnu_cxx::__normal_iterator<const vector<vector<float> >*,vector<vector<vector<float> > > >

namespace ROOT {
   // Wrappers around operator new
   static void *new___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > > : new ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > >;
   }
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > >[nElements] : new ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > >[nElements];
   }
   // Wrapper around operator delete
   static void delete___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR(void *p) {
      delete ((::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > >*)p);
   }
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR(void *p) {
      delete [] ((::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > >*)p);
   }
   static void destruct___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR(void *p) {
      typedef ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > >

namespace ROOT {
   // Wrappers around operator new
   static void *new___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > > : new ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > >;
   }
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > >[nElements] : new ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > >[nElements];
   }
   // Wrapper around operator delete
   static void delete___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR(void *p) {
      delete ((::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > >*)p);
   }
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR(void *p) {
      delete [] ((::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > >*)p);
   }
   static void destruct___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgRsPgR(void *p) {
      typedef ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > >

namespace ROOT {
   // Wrappers around operator new
   static void *new___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > > : new ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > >;
   }
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > >[nElements] : new ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > >[nElements];
   }
   // Wrapper around operator delete
   static void delete___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR(void *p) {
      delete ((::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > >*)p);
   }
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR(void *p) {
      delete [] ((::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > >*)p);
   }
   static void destruct___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR(void *p) {
      typedef ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > >

namespace ROOT {
   // Wrappers around operator new
   static void *new___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > > : new ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > >;
   }
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > >[nElements] : new ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > >[nElements];
   }
   // Wrapper around operator delete
   static void delete___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR(void *p) {
      delete ((::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > >*)p);
   }
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR(void *p) {
      delete [] ((::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > >*)p);
   }
   static void destruct___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR(void *p) {
      typedef ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > >

namespace ROOT {
   // Wrappers around operator new
   static void *new___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > > : new ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > >;
   }
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > >[nElements] : new ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > >[nElements];
   }
   // Wrapper around operator delete
   static void delete___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR(void *p) {
      delete ((::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > >*)p);
   }
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR(void *p) {
      delete [] ((::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > >*)p);
   }
   static void destruct___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR(void *p) {
      typedef ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > >

namespace ROOT {
   // Wrappers around operator new
   static void *new___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > > : new ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > >;
   }
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > >[nElements] : new ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > >[nElements];
   }
   // Wrapper around operator delete
   static void delete___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR(void *p) {
      delete ((::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > >*)p);
   }
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR(void *p) {
      delete [] ((::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > >*)p);
   }
   static void destruct___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgRsPgR(void *p) {
      typedef ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > >

namespace ROOT {
   // Wrappers around operator new
   static void *new___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > > : new ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > >;
   }
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > >[nElements] : new ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > >[nElements];
   }
   // Wrapper around operator delete
   static void delete___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR(void *p) {
      delete ((::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > >*)p);
   }
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR(void *p) {
      delete [] ((::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > >*)p);
   }
   static void destruct___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR(void *p) {
      typedef ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::__gnu_cxx::__normal_iterator<vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > >

namespace ROOT {
   // Wrappers around operator new
   static void *new___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > > : new ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > >;
   }
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > >[nElements] : new ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > >[nElements];
   }
   // Wrapper around operator delete
   static void delete___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR(void *p) {
      delete ((::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > >*)p);
   }
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR(void *p) {
      delete [] ((::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > >*)p);
   }
   static void destruct___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR(void *p) {
      typedef ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > >

namespace ROOT {
   // Wrappers around operator new
   static void *new___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > > : new ::__gnu_cxx::__normal_iterator<vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > >;
   }
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > >[nElements] : new ::__gnu_cxx::__normal_iterator<vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > >[nElements];
   }
   // Wrapper around operator delete
   static void delete___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR(void *p) {
      delete ((::__gnu_cxx::__normal_iterator<vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > >*)p);
   }
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR(void *p) {
      delete [] ((::__gnu_cxx::__normal_iterator<vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > >*)p);
   }
   static void destruct___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR(void *p) {
      typedef ::__gnu_cxx::__normal_iterator<vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::__gnu_cxx::__normal_iterator<vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > >

namespace ROOT {
   // Wrappers around operator new
   static void *new___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<const vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > > : new ::__gnu_cxx::__normal_iterator<const vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > >;
   }
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<const vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > >[nElements] : new ::__gnu_cxx::__normal_iterator<const vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > >[nElements];
   }
   // Wrapper around operator delete
   static void delete___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR(void *p) {
      delete ((::__gnu_cxx::__normal_iterator<const vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > >*)p);
   }
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR(void *p) {
      delete [] ((::__gnu_cxx::__normal_iterator<const vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > >*)p);
   }
   static void destruct___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEvectorlEdoublegRsPgRsPgRmUcOvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR(void *p) {
      typedef ::__gnu_cxx::__normal_iterator<const vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::__gnu_cxx::__normal_iterator<const vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > >

namespace ROOT {
   // Wrappers around operator new
   static void *new___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<vector<vector<double> >*,vector<vector<vector<double> > > > : new ::__gnu_cxx::__normal_iterator<vector<vector<double> >*,vector<vector<vector<double> > > >;
   }
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<vector<vector<double> >*,vector<vector<vector<double> > > >[nElements] : new ::__gnu_cxx::__normal_iterator<vector<vector<double> >*,vector<vector<vector<double> > > >[nElements];
   }
   // Wrapper around operator delete
   static void delete___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR(void *p) {
      delete ((::__gnu_cxx::__normal_iterator<vector<vector<double> >*,vector<vector<vector<double> > > >*)p);
   }
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR(void *p) {
      delete [] ((::__gnu_cxx::__normal_iterator<vector<vector<double> >*,vector<vector<vector<double> > > >*)p);
   }
   static void destruct___gnu_cxxcLcL__normal_iteratorlEvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR(void *p) {
      typedef ::__gnu_cxx::__normal_iterator<vector<vector<double> >*,vector<vector<vector<double> > > > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::__gnu_cxx::__normal_iterator<vector<vector<double> >*,vector<vector<vector<double> > > >

namespace ROOT {
   // Wrappers around operator new
   static void *new___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<const vector<vector<double> >*,vector<vector<vector<double> > > > : new ::__gnu_cxx::__normal_iterator<const vector<vector<double> >*,vector<vector<vector<double> > > >;
   }
   static void *newArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::__gnu_cxx::__normal_iterator<const vector<vector<double> >*,vector<vector<vector<double> > > >[nElements] : new ::__gnu_cxx::__normal_iterator<const vector<vector<double> >*,vector<vector<vector<double> > > >[nElements];
   }
   // Wrapper around operator delete
   static void delete___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR(void *p) {
      delete ((::__gnu_cxx::__normal_iterator<const vector<vector<double> >*,vector<vector<vector<double> > > >*)p);
   }
   static void deleteArray___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR(void *p) {
      delete [] ((::__gnu_cxx::__normal_iterator<const vector<vector<double> >*,vector<vector<vector<double> > > >*)p);
   }
   static void destruct___gnu_cxxcLcL__normal_iteratorlEconstsPvectorlEvectorlEdoublegRsPgRmUcOvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR(void *p) {
      typedef ::__gnu_cxx::__normal_iterator<const vector<vector<double> >*,vector<vector<vector<double> > > > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::__gnu_cxx::__normal_iterator<const vector<vector<double> >*,vector<vector<vector<double> > > >

//______________________________________________________________________________
void TestProposal::Streamer(TBuffer &R__b)
{
   // Stream an object of class TestProposal.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(TestProposal::Class(),this);
   } else {
      R__b.WriteClassBuffer(TestProposal::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_TestProposal(void *p) {
      return  p ? new(p) ::TestProposal : new ::TestProposal;
   }
   static void *newArray_TestProposal(Long_t nElements, void *p) {
      return p ? new(p) ::TestProposal[nElements] : new ::TestProposal[nElements];
   }
   // Wrapper around operator delete
   static void delete_TestProposal(void *p) {
      delete ((::TestProposal*)p);
   }
   static void deleteArray_TestProposal(void *p) {
      delete [] ((::TestProposal*)p);
   }
   static void destruct_TestProposal(void *p) {
      typedef ::TestProposal current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::TestProposal

//______________________________________________________________________________
void DebugProposal::Streamer(TBuffer &R__b)
{
   // Stream an object of class DebugProposal.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(DebugProposal::Class(),this);
   } else {
      R__b.WriteClassBuffer(DebugProposal::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_DebugProposal(void *p) {
      return  p ? new(p) ::DebugProposal : new ::DebugProposal;
   }
   static void *newArray_DebugProposal(Long_t nElements, void *p) {
      return p ? new(p) ::DebugProposal[nElements] : new ::DebugProposal[nElements];
   }
   // Wrapper around operator delete
   static void delete_DebugProposal(void *p) {
      delete ((::DebugProposal*)p);
   }
   static void deleteArray_DebugProposal(void *p) {
      delete [] ((::DebugProposal*)p);
   }
   static void destruct_DebugProposal(void *p) {
      typedef ::DebugProposal current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::DebugProposal

//______________________________________________________________________________
void VerticalInterpPdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class VerticalInterpPdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(VerticalInterpPdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(VerticalInterpPdf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_VerticalInterpPdf(void *p) {
      return  p ? new(p) ::VerticalInterpPdf : new ::VerticalInterpPdf;
   }
   static void *newArray_VerticalInterpPdf(Long_t nElements, void *p) {
      return p ? new(p) ::VerticalInterpPdf[nElements] : new ::VerticalInterpPdf[nElements];
   }
   // Wrapper around operator delete
   static void delete_VerticalInterpPdf(void *p) {
      delete ((::VerticalInterpPdf*)p);
   }
   static void deleteArray_VerticalInterpPdf(void *p) {
      delete [] ((::VerticalInterpPdf*)p);
   }
   static void destruct_VerticalInterpPdf(void *p) {
      typedef ::VerticalInterpPdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::VerticalInterpPdf

//______________________________________________________________________________
void SimpleCacheSentry::Streamer(TBuffer &R__b)
{
   // Stream an object of class SimpleCacheSentry.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(SimpleCacheSentry::Class(),this);
   } else {
      R__b.WriteClassBuffer(SimpleCacheSentry::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_SimpleCacheSentry(void *p) {
      return  p ? new(p) ::SimpleCacheSentry : new ::SimpleCacheSentry;
   }
   static void *newArray_SimpleCacheSentry(Long_t nElements, void *p) {
      return p ? new(p) ::SimpleCacheSentry[nElements] : new ::SimpleCacheSentry[nElements];
   }
   // Wrapper around operator delete
   static void delete_SimpleCacheSentry(void *p) {
      delete ((::SimpleCacheSentry*)p);
   }
   static void deleteArray_SimpleCacheSentry(void *p) {
      delete [] ((::SimpleCacheSentry*)p);
   }
   static void destruct_SimpleCacheSentry(void *p) {
      typedef ::SimpleCacheSentry current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::SimpleCacheSentry

namespace ROOT {
   // Wrappers around operator new
   static void *new_FastTemplate(void *p) {
      return  p ? new(p) ::FastTemplate : new ::FastTemplate;
   }
   static void *newArray_FastTemplate(Long_t nElements, void *p) {
      return p ? new(p) ::FastTemplate[nElements] : new ::FastTemplate[nElements];
   }
   // Wrapper around operator delete
   static void delete_FastTemplate(void *p) {
      delete ((::FastTemplate*)p);
   }
   static void deleteArray_FastTemplate(void *p) {
      delete [] ((::FastTemplate*)p);
   }
   static void destruct_FastTemplate(void *p) {
      typedef ::FastTemplate current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::FastTemplate

namespace ROOT {
   // Wrappers around operator new
   static void *new_FastHisto(void *p) {
      return  p ? new(p) ::FastHisto : new ::FastHisto;
   }
   static void *newArray_FastHisto(Long_t nElements, void *p) {
      return p ? new(p) ::FastHisto[nElements] : new ::FastHisto[nElements];
   }
   // Wrapper around operator delete
   static void delete_FastHisto(void *p) {
      delete ((::FastHisto*)p);
   }
   static void deleteArray_FastHisto(void *p) {
      delete [] ((::FastHisto*)p);
   }
   static void destruct_FastHisto(void *p) {
      typedef ::FastHisto current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::FastHisto

namespace ROOT {
   // Wrappers around operator new
   static void *new_FastHisto2D(void *p) {
      return  p ? new(p) ::FastHisto2D : new ::FastHisto2D;
   }
   static void *newArray_FastHisto2D(Long_t nElements, void *p) {
      return p ? new(p) ::FastHisto2D[nElements] : new ::FastHisto2D[nElements];
   }
   // Wrapper around operator delete
   static void delete_FastHisto2D(void *p) {
      delete ((::FastHisto2D*)p);
   }
   static void deleteArray_FastHisto2D(void *p) {
      delete [] ((::FastHisto2D*)p);
   }
   static void destruct_FastHisto2D(void *p) {
      typedef ::FastHisto2D current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::FastHisto2D

namespace ROOT {
   // Wrappers around operator new
   static void *new_FastHisto3D(void *p) {
      return  p ? new(p) ::FastHisto3D : new ::FastHisto3D;
   }
   static void *newArray_FastHisto3D(Long_t nElements, void *p) {
      return p ? new(p) ::FastHisto3D[nElements] : new ::FastHisto3D[nElements];
   }
   // Wrapper around operator delete
   static void delete_FastHisto3D(void *p) {
      delete ((::FastHisto3D*)p);
   }
   static void deleteArray_FastHisto3D(void *p) {
      delete [] ((::FastHisto3D*)p);
   }
   static void destruct_FastHisto3D(void *p) {
      typedef ::FastHisto3D current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::FastHisto3D

//______________________________________________________________________________
void VerticalInterpHistPdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class VerticalInterpHistPdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(VerticalInterpHistPdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(VerticalInterpHistPdf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_VerticalInterpHistPdf(void *p) {
      return  p ? new(p) ::VerticalInterpHistPdf : new ::VerticalInterpHistPdf;
   }
   static void *newArray_VerticalInterpHistPdf(Long_t nElements, void *p) {
      return p ? new(p) ::VerticalInterpHistPdf[nElements] : new ::VerticalInterpHistPdf[nElements];
   }
   // Wrapper around operator delete
   static void delete_VerticalInterpHistPdf(void *p) {
      delete ((::VerticalInterpHistPdf*)p);
   }
   static void deleteArray_VerticalInterpHistPdf(void *p) {
      delete [] ((::VerticalInterpHistPdf*)p);
   }
   static void destruct_VerticalInterpHistPdf(void *p) {
      typedef ::VerticalInterpHistPdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::VerticalInterpHistPdf

//______________________________________________________________________________
void FastVerticalInterpHistPdfBase::Streamer(TBuffer &R__b)
{
   // Stream an object of class FastVerticalInterpHistPdfBase.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(FastVerticalInterpHistPdfBase::Class(),this);
   } else {
      R__b.WriteClassBuffer(FastVerticalInterpHistPdfBase::Class(),this);
   }
}

namespace ROOT {
   // Wrapper around operator delete
   static void delete_FastVerticalInterpHistPdfBase(void *p) {
      delete ((::FastVerticalInterpHistPdfBase*)p);
   }
   static void deleteArray_FastVerticalInterpHistPdfBase(void *p) {
      delete [] ((::FastVerticalInterpHistPdfBase*)p);
   }
   static void destruct_FastVerticalInterpHistPdfBase(void *p) {
      typedef ::FastVerticalInterpHistPdfBase current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::FastVerticalInterpHistPdfBase

namespace ROOT {
   // Wrappers around operator new
   static void *new_FastVerticalInterpHistPdfBasecLcLMorph(void *p) {
      return  p ? new(p) ::FastVerticalInterpHistPdfBase::Morph : new ::FastVerticalInterpHistPdfBase::Morph;
   }
   static void *newArray_FastVerticalInterpHistPdfBasecLcLMorph(Long_t nElements, void *p) {
      return p ? new(p) ::FastVerticalInterpHistPdfBase::Morph[nElements] : new ::FastVerticalInterpHistPdfBase::Morph[nElements];
   }
   // Wrapper around operator delete
   static void delete_FastVerticalInterpHistPdfBasecLcLMorph(void *p) {
      delete ((::FastVerticalInterpHistPdfBase::Morph*)p);
   }
   static void deleteArray_FastVerticalInterpHistPdfBasecLcLMorph(void *p) {
      delete [] ((::FastVerticalInterpHistPdfBase::Morph*)p);
   }
   static void destruct_FastVerticalInterpHistPdfBasecLcLMorph(void *p) {
      typedef ::FastVerticalInterpHistPdfBase::Morph current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::FastVerticalInterpHistPdfBase::Morph

//______________________________________________________________________________
void FastVerticalInterpHistPdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class FastVerticalInterpHistPdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(FastVerticalInterpHistPdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(FastVerticalInterpHistPdf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_FastVerticalInterpHistPdf(void *p) {
      return  p ? new(p) ::FastVerticalInterpHistPdf : new ::FastVerticalInterpHistPdf;
   }
   static void *newArray_FastVerticalInterpHistPdf(Long_t nElements, void *p) {
      return p ? new(p) ::FastVerticalInterpHistPdf[nElements] : new ::FastVerticalInterpHistPdf[nElements];
   }
   // Wrapper around operator delete
   static void delete_FastVerticalInterpHistPdf(void *p) {
      delete ((::FastVerticalInterpHistPdf*)p);
   }
   static void deleteArray_FastVerticalInterpHistPdf(void *p) {
      delete [] ((::FastVerticalInterpHistPdf*)p);
   }
   static void destruct_FastVerticalInterpHistPdf(void *p) {
      typedef ::FastVerticalInterpHistPdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::FastVerticalInterpHistPdf

//______________________________________________________________________________
void FastVerticalInterpHistPdf2D::Streamer(TBuffer &R__b)
{
   // Stream an object of class FastVerticalInterpHistPdf2D.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(FastVerticalInterpHistPdf2D::Class(),this);
   } else {
      R__b.WriteClassBuffer(FastVerticalInterpHistPdf2D::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_FastVerticalInterpHistPdf2D(void *p) {
      return  p ? new(p) ::FastVerticalInterpHistPdf2D : new ::FastVerticalInterpHistPdf2D;
   }
   static void *newArray_FastVerticalInterpHistPdf2D(Long_t nElements, void *p) {
      return p ? new(p) ::FastVerticalInterpHistPdf2D[nElements] : new ::FastVerticalInterpHistPdf2D[nElements];
   }
   // Wrapper around operator delete
   static void delete_FastVerticalInterpHistPdf2D(void *p) {
      delete ((::FastVerticalInterpHistPdf2D*)p);
   }
   static void deleteArray_FastVerticalInterpHistPdf2D(void *p) {
      delete [] ((::FastVerticalInterpHistPdf2D*)p);
   }
   static void destruct_FastVerticalInterpHistPdf2D(void *p) {
      typedef ::FastVerticalInterpHistPdf2D current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::FastVerticalInterpHistPdf2D

//______________________________________________________________________________
void FastVerticalInterpHistPdf2Base::Streamer(TBuffer &R__b)
{
   // Stream an object of class FastVerticalInterpHistPdf2Base.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(FastVerticalInterpHistPdf2Base::Class(),this);
   } else {
      R__b.WriteClassBuffer(FastVerticalInterpHistPdf2Base::Class(),this);
   }
}

namespace ROOT {
   // Wrapper around operator delete
   static void delete_FastVerticalInterpHistPdf2Base(void *p) {
      delete ((::FastVerticalInterpHistPdf2Base*)p);
   }
   static void deleteArray_FastVerticalInterpHistPdf2Base(void *p) {
      delete [] ((::FastVerticalInterpHistPdf2Base*)p);
   }
   static void destruct_FastVerticalInterpHistPdf2Base(void *p) {
      typedef ::FastVerticalInterpHistPdf2Base current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::FastVerticalInterpHistPdf2Base

//______________________________________________________________________________
void FastVerticalInterpHistPdf2::Streamer(TBuffer &R__b)
{
   // Stream an object of class FastVerticalInterpHistPdf2.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(FastVerticalInterpHistPdf2::Class(),this);
   } else {
      R__b.WriteClassBuffer(FastVerticalInterpHistPdf2::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_FastVerticalInterpHistPdf2(void *p) {
      return  p ? new(p) ::FastVerticalInterpHistPdf2 : new ::FastVerticalInterpHistPdf2;
   }
   static void *newArray_FastVerticalInterpHistPdf2(Long_t nElements, void *p) {
      return p ? new(p) ::FastVerticalInterpHistPdf2[nElements] : new ::FastVerticalInterpHistPdf2[nElements];
   }
   // Wrapper around operator delete
   static void delete_FastVerticalInterpHistPdf2(void *p) {
      delete ((::FastVerticalInterpHistPdf2*)p);
   }
   static void deleteArray_FastVerticalInterpHistPdf2(void *p) {
      delete [] ((::FastVerticalInterpHistPdf2*)p);
   }
   static void destruct_FastVerticalInterpHistPdf2(void *p) {
      typedef ::FastVerticalInterpHistPdf2 current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::FastVerticalInterpHistPdf2

//______________________________________________________________________________
void FastVerticalInterpHistPdf2D2::Streamer(TBuffer &R__b)
{
   // Stream an object of class FastVerticalInterpHistPdf2D2.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(FastVerticalInterpHistPdf2D2::Class(),this);
   } else {
      R__b.WriteClassBuffer(FastVerticalInterpHistPdf2D2::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_FastVerticalInterpHistPdf2D2(void *p) {
      return  p ? new(p) ::FastVerticalInterpHistPdf2D2 : new ::FastVerticalInterpHistPdf2D2;
   }
   static void *newArray_FastVerticalInterpHistPdf2D2(Long_t nElements, void *p) {
      return p ? new(p) ::FastVerticalInterpHistPdf2D2[nElements] : new ::FastVerticalInterpHistPdf2D2[nElements];
   }
   // Wrapper around operator delete
   static void delete_FastVerticalInterpHistPdf2D2(void *p) {
      delete ((::FastVerticalInterpHistPdf2D2*)p);
   }
   static void deleteArray_FastVerticalInterpHistPdf2D2(void *p) {
      delete [] ((::FastVerticalInterpHistPdf2D2*)p);
   }
   static void destruct_FastVerticalInterpHistPdf2D2(void *p) {
      typedef ::FastVerticalInterpHistPdf2D2 current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::FastVerticalInterpHistPdf2D2

//______________________________________________________________________________
void FastVerticalInterpHistPdf3D::Streamer(TBuffer &R__b)
{
   // Stream an object of class FastVerticalInterpHistPdf3D.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(FastVerticalInterpHistPdf3D::Class(),this);
   } else {
      R__b.WriteClassBuffer(FastVerticalInterpHistPdf3D::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_FastVerticalInterpHistPdf3D(void *p) {
      return  p ? new(p) ::FastVerticalInterpHistPdf3D : new ::FastVerticalInterpHistPdf3D;
   }
   static void *newArray_FastVerticalInterpHistPdf3D(Long_t nElements, void *p) {
      return p ? new(p) ::FastVerticalInterpHistPdf3D[nElements] : new ::FastVerticalInterpHistPdf3D[nElements];
   }
   // Wrapper around operator delete
   static void delete_FastVerticalInterpHistPdf3D(void *p) {
      delete ((::FastVerticalInterpHistPdf3D*)p);
   }
   static void deleteArray_FastVerticalInterpHistPdf3D(void *p) {
      delete [] ((::FastVerticalInterpHistPdf3D*)p);
   }
   static void destruct_FastVerticalInterpHistPdf3D(void *p) {
      typedef ::FastVerticalInterpHistPdf3D current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::FastVerticalInterpHistPdf3D

//______________________________________________________________________________
void AsymPow::Streamer(TBuffer &R__b)
{
   // Stream an object of class AsymPow.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(AsymPow::Class(),this);
   } else {
      R__b.WriteClassBuffer(AsymPow::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_AsymPow(void *p) {
      return  p ? new(p) ::AsymPow : new ::AsymPow;
   }
   static void *newArray_AsymPow(Long_t nElements, void *p) {
      return p ? new(p) ::AsymPow[nElements] : new ::AsymPow[nElements];
   }
   // Wrapper around operator delete
   static void delete_AsymPow(void *p) {
      delete ((::AsymPow*)p);
   }
   static void deleteArray_AsymPow(void *p) {
      delete [] ((::AsymPow*)p);
   }
   static void destruct_AsymPow(void *p) {
      typedef ::AsymPow current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::AsymPow

//______________________________________________________________________________
void AsymQuad::Streamer(TBuffer &R__b)
{
   // Stream an object of class AsymQuad.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(AsymQuad::Class(),this);
   } else {
      R__b.WriteClassBuffer(AsymQuad::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_AsymQuad(void *p) {
      return  p ? new(p) ::AsymQuad : new ::AsymQuad;
   }
   static void *newArray_AsymQuad(Long_t nElements, void *p) {
      return p ? new(p) ::AsymQuad[nElements] : new ::AsymQuad[nElements];
   }
   // Wrapper around operator delete
   static void delete_AsymQuad(void *p) {
      delete ((::AsymQuad*)p);
   }
   static void deleteArray_AsymQuad(void *p) {
      delete [] ((::AsymQuad*)p);
   }
   static void destruct_AsymQuad(void *p) {
      typedef ::AsymQuad current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::AsymQuad

//______________________________________________________________________________
void CombDataSetFactory::Streamer(TBuffer &R__b)
{
   // Stream an object of class CombDataSetFactory.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(CombDataSetFactory::Class(),this);
   } else {
      R__b.WriteClassBuffer(CombDataSetFactory::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_CombDataSetFactory(void *p) {
      return  p ? new(p) ::CombDataSetFactory : new ::CombDataSetFactory;
   }
   static void *newArray_CombDataSetFactory(Long_t nElements, void *p) {
      return p ? new(p) ::CombDataSetFactory[nElements] : new ::CombDataSetFactory[nElements];
   }
   // Wrapper around operator delete
   static void delete_CombDataSetFactory(void *p) {
      delete ((::CombDataSetFactory*)p);
   }
   static void deleteArray_CombDataSetFactory(void *p) {
      delete [] ((::CombDataSetFactory*)p);
   }
   static void destruct_CombDataSetFactory(void *p) {
      typedef ::CombDataSetFactory current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::CombDataSetFactory

//______________________________________________________________________________
void TH1Keys::Streamer(TBuffer &R__b)
{
   // Stream an object of class TH1Keys.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(TH1Keys::Class(),this);
   } else {
      R__b.WriteClassBuffer(TH1Keys::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_TH1Keys(void *p) {
      return  p ? new(p) ::TH1Keys : new ::TH1Keys;
   }
   static void *newArray_TH1Keys(Long_t nElements, void *p) {
      return p ? new(p) ::TH1Keys[nElements] : new ::TH1Keys[nElements];
   }
   // Wrapper around operator delete
   static void delete_TH1Keys(void *p) {
      delete ((::TH1Keys*)p);
   }
   static void deleteArray_TH1Keys(void *p) {
      delete [] ((::TH1Keys*)p);
   }
   static void destruct_TH1Keys(void *p) {
      typedef ::TH1Keys current_t;
      ((current_t*)p)->~current_t();
   }
   // Wrapper around the directory auto add.
   static void directoryAutoAdd_TH1Keys(void *p, TDirectory *dir) {
      ((::TH1Keys*)p)->DirectoryAutoAdd(dir);
   }
   // Wrapper around the merge function.
   static Long64_t  merge_TH1Keys(void *obj,TCollection *coll,TFileMergeInfo *) {
      return ((::TH1Keys*)obj)->Merge(coll);
   }
} // end of namespace ROOT for class ::TH1Keys

//______________________________________________________________________________
void RooSimultaneousOpt::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooSimultaneousOpt.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooSimultaneousOpt::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooSimultaneousOpt::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooSimultaneousOpt(void *p) {
      return  p ? new(p) ::RooSimultaneousOpt : new ::RooSimultaneousOpt;
   }
   static void *newArray_RooSimultaneousOpt(Long_t nElements, void *p) {
      return p ? new(p) ::RooSimultaneousOpt[nElements] : new ::RooSimultaneousOpt[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooSimultaneousOpt(void *p) {
      delete ((::RooSimultaneousOpt*)p);
   }
   static void deleteArray_RooSimultaneousOpt(void *p) {
      delete [] ((::RooSimultaneousOpt*)p);
   }
   static void destruct_RooSimultaneousOpt(void *p) {
      typedef ::RooSimultaneousOpt current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooSimultaneousOpt

//______________________________________________________________________________
void HZZ4L_RooCTauPdf_1D::Streamer(TBuffer &R__b)
{
   // Stream an object of class HZZ4L_RooCTauPdf_1D.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(HZZ4L_RooCTauPdf_1D::Class(),this);
   } else {
      R__b.WriteClassBuffer(HZZ4L_RooCTauPdf_1D::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_HZZ4L_RooCTauPdf_1D(void *p) {
      return  p ? new(p) ::HZZ4L_RooCTauPdf_1D : new ::HZZ4L_RooCTauPdf_1D;
   }
   static void *newArray_HZZ4L_RooCTauPdf_1D(Long_t nElements, void *p) {
      return p ? new(p) ::HZZ4L_RooCTauPdf_1D[nElements] : new ::HZZ4L_RooCTauPdf_1D[nElements];
   }
   // Wrapper around operator delete
   static void delete_HZZ4L_RooCTauPdf_1D(void *p) {
      delete ((::HZZ4L_RooCTauPdf_1D*)p);
   }
   static void deleteArray_HZZ4L_RooCTauPdf_1D(void *p) {
      delete [] ((::HZZ4L_RooCTauPdf_1D*)p);
   }
   static void destruct_HZZ4L_RooCTauPdf_1D(void *p) {
      typedef ::HZZ4L_RooCTauPdf_1D current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::HZZ4L_RooCTauPdf_1D

//______________________________________________________________________________
void HZZ4L_RooCTauPdf_1D_Expanded::Streamer(TBuffer &R__b)
{
   // Stream an object of class HZZ4L_RooCTauPdf_1D_Expanded.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(HZZ4L_RooCTauPdf_1D_Expanded::Class(),this);
   } else {
      R__b.WriteClassBuffer(HZZ4L_RooCTauPdf_1D_Expanded::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_HZZ4L_RooCTauPdf_1D_Expanded(void *p) {
      return  p ? new(p) ::HZZ4L_RooCTauPdf_1D_Expanded : new ::HZZ4L_RooCTauPdf_1D_Expanded;
   }
   static void *newArray_HZZ4L_RooCTauPdf_1D_Expanded(Long_t nElements, void *p) {
      return p ? new(p) ::HZZ4L_RooCTauPdf_1D_Expanded[nElements] : new ::HZZ4L_RooCTauPdf_1D_Expanded[nElements];
   }
   // Wrapper around operator delete
   static void delete_HZZ4L_RooCTauPdf_1D_Expanded(void *p) {
      delete ((::HZZ4L_RooCTauPdf_1D_Expanded*)p);
   }
   static void deleteArray_HZZ4L_RooCTauPdf_1D_Expanded(void *p) {
      delete [] ((::HZZ4L_RooCTauPdf_1D_Expanded*)p);
   }
   static void destruct_HZZ4L_RooCTauPdf_1D_Expanded(void *p) {
      typedef ::HZZ4L_RooCTauPdf_1D_Expanded current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::HZZ4L_RooCTauPdf_1D_Expanded

//______________________________________________________________________________
void HZZ4L_RooCTauPdf_2D::Streamer(TBuffer &R__b)
{
   // Stream an object of class HZZ4L_RooCTauPdf_2D.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(HZZ4L_RooCTauPdf_2D::Class(),this);
   } else {
      R__b.WriteClassBuffer(HZZ4L_RooCTauPdf_2D::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_HZZ4L_RooCTauPdf_2D(void *p) {
      return  p ? new(p) ::HZZ4L_RooCTauPdf_2D : new ::HZZ4L_RooCTauPdf_2D;
   }
   static void *newArray_HZZ4L_RooCTauPdf_2D(Long_t nElements, void *p) {
      return p ? new(p) ::HZZ4L_RooCTauPdf_2D[nElements] : new ::HZZ4L_RooCTauPdf_2D[nElements];
   }
   // Wrapper around operator delete
   static void delete_HZZ4L_RooCTauPdf_2D(void *p) {
      delete ((::HZZ4L_RooCTauPdf_2D*)p);
   }
   static void deleteArray_HZZ4L_RooCTauPdf_2D(void *p) {
      delete [] ((::HZZ4L_RooCTauPdf_2D*)p);
   }
   static void destruct_HZZ4L_RooCTauPdf_2D(void *p) {
      typedef ::HZZ4L_RooCTauPdf_2D current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::HZZ4L_RooCTauPdf_2D

//______________________________________________________________________________
void RooqqZZPdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooqqZZPdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooqqZZPdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooqqZZPdf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooqqZZPdf(void *p) {
      return  p ? new(p) ::RooqqZZPdf : new ::RooqqZZPdf;
   }
   static void *newArray_RooqqZZPdf(Long_t nElements, void *p) {
      return p ? new(p) ::RooqqZZPdf[nElements] : new ::RooqqZZPdf[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooqqZZPdf(void *p) {
      delete ((::RooqqZZPdf*)p);
   }
   static void deleteArray_RooqqZZPdf(void *p) {
      delete [] ((::RooqqZZPdf*)p);
   }
   static void destruct_RooqqZZPdf(void *p) {
      typedef ::RooqqZZPdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooqqZZPdf

//______________________________________________________________________________
void RooggZZPdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooggZZPdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooggZZPdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooggZZPdf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooggZZPdf(void *p) {
      return  p ? new(p) ::RooggZZPdf : new ::RooggZZPdf;
   }
   static void *newArray_RooggZZPdf(Long_t nElements, void *p) {
      return p ? new(p) ::RooggZZPdf[nElements] : new ::RooggZZPdf[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooggZZPdf(void *p) {
      delete ((::RooggZZPdf*)p);
   }
   static void deleteArray_RooggZZPdf(void *p) {
      delete [] ((::RooggZZPdf*)p);
   }
   static void destruct_RooggZZPdf(void *p) {
      typedef ::RooggZZPdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooggZZPdf

//______________________________________________________________________________
void RooqqZZPdf_v2::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooqqZZPdf_v2.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooqqZZPdf_v2::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooqqZZPdf_v2::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooqqZZPdf_v2(void *p) {
      return  p ? new(p) ::RooqqZZPdf_v2 : new ::RooqqZZPdf_v2;
   }
   static void *newArray_RooqqZZPdf_v2(Long_t nElements, void *p) {
      return p ? new(p) ::RooqqZZPdf_v2[nElements] : new ::RooqqZZPdf_v2[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooqqZZPdf_v2(void *p) {
      delete ((::RooqqZZPdf_v2*)p);
   }
   static void deleteArray_RooqqZZPdf_v2(void *p) {
      delete [] ((::RooqqZZPdf_v2*)p);
   }
   static void destruct_RooqqZZPdf_v2(void *p) {
      typedef ::RooqqZZPdf_v2 current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooqqZZPdf_v2

//______________________________________________________________________________
void RooVBFZZPdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooVBFZZPdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooVBFZZPdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooVBFZZPdf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooVBFZZPdf(void *p) {
      return  p ? new(p) ::RooVBFZZPdf : new ::RooVBFZZPdf;
   }
   static void *newArray_RooVBFZZPdf(Long_t nElements, void *p) {
      return p ? new(p) ::RooVBFZZPdf[nElements] : new ::RooVBFZZPdf[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooVBFZZPdf(void *p) {
      delete ((::RooVBFZZPdf*)p);
   }
   static void deleteArray_RooVBFZZPdf(void *p) {
      delete [] ((::RooVBFZZPdf*)p);
   }
   static void destruct_RooVBFZZPdf(void *p) {
      typedef ::RooVBFZZPdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooVBFZZPdf

//______________________________________________________________________________
void RooVBFZZPdf_v2::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooVBFZZPdf_v2.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooVBFZZPdf_v2::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooVBFZZPdf_v2::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooVBFZZPdf_v2(void *p) {
      return  p ? new(p) ::RooVBFZZPdf_v2 : new ::RooVBFZZPdf_v2;
   }
   static void *newArray_RooVBFZZPdf_v2(Long_t nElements, void *p) {
      return p ? new(p) ::RooVBFZZPdf_v2[nElements] : new ::RooVBFZZPdf_v2[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooVBFZZPdf_v2(void *p) {
      delete ((::RooVBFZZPdf_v2*)p);
   }
   static void deleteArray_RooVBFZZPdf_v2(void *p) {
      delete [] ((::RooVBFZZPdf_v2*)p);
   }
   static void destruct_RooVBFZZPdf_v2(void *p) {
      typedef ::RooVBFZZPdf_v2 current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooVBFZZPdf_v2

//______________________________________________________________________________
void RooggZZPdf_v2::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooggZZPdf_v2.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooggZZPdf_v2::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooggZZPdf_v2::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooggZZPdf_v2(void *p) {
      return  p ? new(p) ::RooggZZPdf_v2 : new ::RooggZZPdf_v2;
   }
   static void *newArray_RooggZZPdf_v2(Long_t nElements, void *p) {
      return p ? new(p) ::RooggZZPdf_v2[nElements] : new ::RooggZZPdf_v2[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooggZZPdf_v2(void *p) {
      delete ((::RooggZZPdf_v2*)p);
   }
   static void deleteArray_RooggZZPdf_v2(void *p) {
      delete [] ((::RooggZZPdf_v2*)p);
   }
   static void destruct_RooggZZPdf_v2(void *p) {
      typedef ::RooggZZPdf_v2 current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooggZZPdf_v2

//______________________________________________________________________________
void RooBetaFunc_v2::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooBetaFunc_v2.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooBetaFunc_v2::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooBetaFunc_v2::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooBetaFunc_v2(void *p) {
      return  p ? new(p) ::RooBetaFunc_v2 : new ::RooBetaFunc_v2;
   }
   static void *newArray_RooBetaFunc_v2(Long_t nElements, void *p) {
      return p ? new(p) ::RooBetaFunc_v2[nElements] : new ::RooBetaFunc_v2[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooBetaFunc_v2(void *p) {
      delete ((::RooBetaFunc_v2*)p);
   }
   static void deleteArray_RooBetaFunc_v2(void *p) {
      delete [] ((::RooBetaFunc_v2*)p);
   }
   static void destruct_RooBetaFunc_v2(void *p) {
      typedef ::RooBetaFunc_v2 current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooBetaFunc_v2

//______________________________________________________________________________
void Roo4lMasses2D_Bkg::Streamer(TBuffer &R__b)
{
   // Stream an object of class Roo4lMasses2D_Bkg.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(Roo4lMasses2D_Bkg::Class(),this);
   } else {
      R__b.WriteClassBuffer(Roo4lMasses2D_Bkg::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_Roo4lMasses2D_Bkg(void *p) {
      return  p ? new(p) ::Roo4lMasses2D_Bkg : new ::Roo4lMasses2D_Bkg;
   }
   static void *newArray_Roo4lMasses2D_Bkg(Long_t nElements, void *p) {
      return p ? new(p) ::Roo4lMasses2D_Bkg[nElements] : new ::Roo4lMasses2D_Bkg[nElements];
   }
   // Wrapper around operator delete
   static void delete_Roo4lMasses2D_Bkg(void *p) {
      delete ((::Roo4lMasses2D_Bkg*)p);
   }
   static void deleteArray_Roo4lMasses2D_Bkg(void *p) {
      delete [] ((::Roo4lMasses2D_Bkg*)p);
   }
   static void destruct_Roo4lMasses2D_Bkg(void *p) {
      typedef ::Roo4lMasses2D_Bkg current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::Roo4lMasses2D_Bkg

//______________________________________________________________________________
void Roo4lMasses2D_BkgGGZZ::Streamer(TBuffer &R__b)
{
   // Stream an object of class Roo4lMasses2D_BkgGGZZ.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(Roo4lMasses2D_BkgGGZZ::Class(),this);
   } else {
      R__b.WriteClassBuffer(Roo4lMasses2D_BkgGGZZ::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_Roo4lMasses2D_BkgGGZZ(void *p) {
      return  p ? new(p) ::Roo4lMasses2D_BkgGGZZ : new ::Roo4lMasses2D_BkgGGZZ;
   }
   static void *newArray_Roo4lMasses2D_BkgGGZZ(Long_t nElements, void *p) {
      return p ? new(p) ::Roo4lMasses2D_BkgGGZZ[nElements] : new ::Roo4lMasses2D_BkgGGZZ[nElements];
   }
   // Wrapper around operator delete
   static void delete_Roo4lMasses2D_BkgGGZZ(void *p) {
      delete ((::Roo4lMasses2D_BkgGGZZ*)p);
   }
   static void deleteArray_Roo4lMasses2D_BkgGGZZ(void *p) {
      delete [] ((::Roo4lMasses2D_BkgGGZZ*)p);
   }
   static void destruct_Roo4lMasses2D_BkgGGZZ(void *p) {
      typedef ::Roo4lMasses2D_BkgGGZZ current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::Roo4lMasses2D_BkgGGZZ

//______________________________________________________________________________
void Roo4lMasses2D::Streamer(TBuffer &R__b)
{
   // Stream an object of class Roo4lMasses2D.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(Roo4lMasses2D::Class(),this);
   } else {
      R__b.WriteClassBuffer(Roo4lMasses2D::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_Roo4lMasses2D(void *p) {
      return  p ? new(p) ::Roo4lMasses2D : new ::Roo4lMasses2D;
   }
   static void *newArray_Roo4lMasses2D(Long_t nElements, void *p) {
      return p ? new(p) ::Roo4lMasses2D[nElements] : new ::Roo4lMasses2D[nElements];
   }
   // Wrapper around operator delete
   static void delete_Roo4lMasses2D(void *p) {
      delete ((::Roo4lMasses2D*)p);
   }
   static void deleteArray_Roo4lMasses2D(void *p) {
      delete [] ((::Roo4lMasses2D*)p);
   }
   static void destruct_Roo4lMasses2D(void *p) {
      typedef ::Roo4lMasses2D current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::Roo4lMasses2D

//______________________________________________________________________________
void RooFourMuMassShapePdf2::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooFourMuMassShapePdf2.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooFourMuMassShapePdf2::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooFourMuMassShapePdf2::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooFourMuMassShapePdf2(void *p) {
      return  p ? new(p) ::RooFourMuMassShapePdf2 : new ::RooFourMuMassShapePdf2;
   }
   static void *newArray_RooFourMuMassShapePdf2(Long_t nElements, void *p) {
      return p ? new(p) ::RooFourMuMassShapePdf2[nElements] : new ::RooFourMuMassShapePdf2[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooFourMuMassShapePdf2(void *p) {
      delete ((::RooFourMuMassShapePdf2*)p);
   }
   static void deleteArray_RooFourMuMassShapePdf2(void *p) {
      delete [] ((::RooFourMuMassShapePdf2*)p);
   }
   static void destruct_RooFourMuMassShapePdf2(void *p) {
      typedef ::RooFourMuMassShapePdf2 current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooFourMuMassShapePdf2

//______________________________________________________________________________
void RooFourEMassShapePdf2::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooFourEMassShapePdf2.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooFourEMassShapePdf2::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooFourEMassShapePdf2::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooFourEMassShapePdf2(void *p) {
      return  p ? new(p) ::RooFourEMassShapePdf2 : new ::RooFourEMassShapePdf2;
   }
   static void *newArray_RooFourEMassShapePdf2(Long_t nElements, void *p) {
      return p ? new(p) ::RooFourEMassShapePdf2[nElements] : new ::RooFourEMassShapePdf2[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooFourEMassShapePdf2(void *p) {
      delete ((::RooFourEMassShapePdf2*)p);
   }
   static void deleteArray_RooFourEMassShapePdf2(void *p) {
      delete [] ((::RooFourEMassShapePdf2*)p);
   }
   static void destruct_RooFourEMassShapePdf2(void *p) {
      typedef ::RooFourEMassShapePdf2 current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooFourEMassShapePdf2

//______________________________________________________________________________
void RooTwoETwoMuMassShapePdf2::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooTwoETwoMuMassShapePdf2.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooTwoETwoMuMassShapePdf2::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooTwoETwoMuMassShapePdf2::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooTwoETwoMuMassShapePdf2(void *p) {
      return  p ? new(p) ::RooTwoETwoMuMassShapePdf2 : new ::RooTwoETwoMuMassShapePdf2;
   }
   static void *newArray_RooTwoETwoMuMassShapePdf2(Long_t nElements, void *p) {
      return p ? new(p) ::RooTwoETwoMuMassShapePdf2[nElements] : new ::RooTwoETwoMuMassShapePdf2[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooTwoETwoMuMassShapePdf2(void *p) {
      delete ((::RooTwoETwoMuMassShapePdf2*)p);
   }
   static void deleteArray_RooTwoETwoMuMassShapePdf2(void *p) {
      delete [] ((::RooTwoETwoMuMassShapePdf2*)p);
   }
   static void destruct_RooTwoETwoMuMassShapePdf2(void *p) {
      typedef ::RooTwoETwoMuMassShapePdf2 current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooTwoETwoMuMassShapePdf2

//______________________________________________________________________________
void RooFourMuMassRes::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooFourMuMassRes.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooFourMuMassRes::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooFourMuMassRes::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooFourMuMassRes(void *p) {
      return  p ? new(p) ::RooFourMuMassRes : new ::RooFourMuMassRes;
   }
   static void *newArray_RooFourMuMassRes(Long_t nElements, void *p) {
      return p ? new(p) ::RooFourMuMassRes[nElements] : new ::RooFourMuMassRes[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooFourMuMassRes(void *p) {
      delete ((::RooFourMuMassRes*)p);
   }
   static void deleteArray_RooFourMuMassRes(void *p) {
      delete [] ((::RooFourMuMassRes*)p);
   }
   static void destruct_RooFourMuMassRes(void *p) {
      typedef ::RooFourMuMassRes current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooFourMuMassRes

//______________________________________________________________________________
void RooFourEMassRes::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooFourEMassRes.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooFourEMassRes::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooFourEMassRes::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooFourEMassRes(void *p) {
      return  p ? new(p) ::RooFourEMassRes : new ::RooFourEMassRes;
   }
   static void *newArray_RooFourEMassRes(Long_t nElements, void *p) {
      return p ? new(p) ::RooFourEMassRes[nElements] : new ::RooFourEMassRes[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooFourEMassRes(void *p) {
      delete ((::RooFourEMassRes*)p);
   }
   static void deleteArray_RooFourEMassRes(void *p) {
      delete [] ((::RooFourEMassRes*)p);
   }
   static void destruct_RooFourEMassRes(void *p) {
      typedef ::RooFourEMassRes current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooFourEMassRes

//______________________________________________________________________________
void RooTwoETwoMuMassRes::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooTwoETwoMuMassRes.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooTwoETwoMuMassRes::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooTwoETwoMuMassRes::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooTwoETwoMuMassRes(void *p) {
      return  p ? new(p) ::RooTwoETwoMuMassRes : new ::RooTwoETwoMuMassRes;
   }
   static void *newArray_RooTwoETwoMuMassRes(Long_t nElements, void *p) {
      return p ? new(p) ::RooTwoETwoMuMassRes[nElements] : new ::RooTwoETwoMuMassRes[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooTwoETwoMuMassRes(void *p) {
      delete ((::RooTwoETwoMuMassRes*)p);
   }
   static void deleteArray_RooTwoETwoMuMassRes(void *p) {
      delete [] ((::RooTwoETwoMuMassRes*)p);
   }
   static void destruct_RooTwoETwoMuMassRes(void *p) {
      typedef ::RooTwoETwoMuMassRes current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooTwoETwoMuMassRes

//______________________________________________________________________________
void RooRelBW1::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooRelBW1.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooRelBW1::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooRelBW1::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooRelBW1(void *p) {
      return  p ? new(p) ::RooRelBW1 : new ::RooRelBW1;
   }
   static void *newArray_RooRelBW1(Long_t nElements, void *p) {
      return p ? new(p) ::RooRelBW1[nElements] : new ::RooRelBW1[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooRelBW1(void *p) {
      delete ((::RooRelBW1*)p);
   }
   static void deleteArray_RooRelBW1(void *p) {
      delete [] ((::RooRelBW1*)p);
   }
   static void destruct_RooRelBW1(void *p) {
      typedef ::RooRelBW1 current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooRelBW1

//______________________________________________________________________________
void RooRelBWUF::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooRelBWUF.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooRelBWUF::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooRelBWUF::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooRelBWUF(void *p) {
      return  p ? new(p) ::RooRelBWUF : new ::RooRelBWUF;
   }
   static void *newArray_RooRelBWUF(Long_t nElements, void *p) {
      return p ? new(p) ::RooRelBWUF[nElements] : new ::RooRelBWUF[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooRelBWUF(void *p) {
      delete ((::RooRelBWUF*)p);
   }
   static void deleteArray_RooRelBWUF(void *p) {
      delete [] ((::RooRelBWUF*)p);
   }
   static void destruct_RooRelBWUF(void *p) {
      typedef ::RooRelBWUF current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooRelBWUF

//______________________________________________________________________________
void RooRelBWUF_SM4::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooRelBWUF_SM4.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooRelBWUF_SM4::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooRelBWUF_SM4::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooRelBWUF_SM4(void *p) {
      return  p ? new(p) ::RooRelBWUF_SM4 : new ::RooRelBWUF_SM4;
   }
   static void *newArray_RooRelBWUF_SM4(Long_t nElements, void *p) {
      return p ? new(p) ::RooRelBWUF_SM4[nElements] : new ::RooRelBWUF_SM4[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooRelBWUF_SM4(void *p) {
      delete ((::RooRelBWUF_SM4*)p);
   }
   static void deleteArray_RooRelBWUF_SM4(void *p) {
      delete [] ((::RooRelBWUF_SM4*)p);
   }
   static void destruct_RooRelBWUF_SM4(void *p) {
      typedef ::RooRelBWUF_SM4 current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooRelBWUF_SM4

//______________________________________________________________________________
void RooRelBWUFParamWidth::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooRelBWUFParamWidth.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooRelBWUFParamWidth::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooRelBWUFParamWidth::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooRelBWUFParamWidth(void *p) {
      return  p ? new(p) ::RooRelBWUFParamWidth : new ::RooRelBWUFParamWidth;
   }
   static void *newArray_RooRelBWUFParamWidth(Long_t nElements, void *p) {
      return p ? new(p) ::RooRelBWUFParamWidth[nElements] : new ::RooRelBWUFParamWidth[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooRelBWUFParamWidth(void *p) {
      delete ((::RooRelBWUFParamWidth*)p);
   }
   static void deleteArray_RooRelBWUFParamWidth(void *p) {
      delete [] ((::RooRelBWUFParamWidth*)p);
   }
   static void destruct_RooRelBWUFParamWidth(void *p) {
      typedef ::RooRelBWUFParamWidth current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooRelBWUFParamWidth

//______________________________________________________________________________
void RooRelBWUFParam::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooRelBWUFParam.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooRelBWUFParam::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooRelBWUFParam::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooRelBWUFParam(void *p) {
      return  p ? new(p) ::RooRelBWUFParam : new ::RooRelBWUFParam;
   }
   static void *newArray_RooRelBWUFParam(Long_t nElements, void *p) {
      return p ? new(p) ::RooRelBWUFParam[nElements] : new ::RooRelBWUFParam[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooRelBWUFParam(void *p) {
      delete ((::RooRelBWUFParam*)p);
   }
   static void deleteArray_RooRelBWUFParam(void *p) {
      delete [] ((::RooRelBWUFParam*)p);
   }
   static void destruct_RooRelBWUFParam(void *p) {
      typedef ::RooRelBWUFParam current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooRelBWUFParam

//______________________________________________________________________________
void RooRelBWHighMass::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooRelBWHighMass.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooRelBWHighMass::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooRelBWHighMass::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooRelBWHighMass(void *p) {
      return  p ? new(p) ::RooRelBWHighMass : new ::RooRelBWHighMass;
   }
   static void *newArray_RooRelBWHighMass(Long_t nElements, void *p) {
      return p ? new(p) ::RooRelBWHighMass[nElements] : new ::RooRelBWHighMass[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooRelBWHighMass(void *p) {
      delete ((::RooRelBWHighMass*)p);
   }
   static void deleteArray_RooRelBWHighMass(void *p) {
      delete [] ((::RooRelBWHighMass*)p);
   }
   static void destruct_RooRelBWHighMass(void *p) {
      typedef ::RooRelBWHighMass current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooRelBWHighMass

//______________________________________________________________________________
void RooTsallis::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooTsallis.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooTsallis::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooTsallis::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooTsallis(void *p) {
      return  p ? new(p) ::RooTsallis : new ::RooTsallis;
   }
   static void *newArray_RooTsallis(Long_t nElements, void *p) {
      return p ? new(p) ::RooTsallis[nElements] : new ::RooTsallis[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooTsallis(void *p) {
      delete ((::RooTsallis*)p);
   }
   static void deleteArray_RooTsallis(void *p) {
      delete [] ((::RooTsallis*)p);
   }
   static void destruct_RooTsallis(void *p) {
      typedef ::RooTsallis current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooTsallis

//______________________________________________________________________________
void RooaDoubleCBxBW::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooaDoubleCBxBW.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooaDoubleCBxBW::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooaDoubleCBxBW::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooaDoubleCBxBW(void *p) {
      return  p ? new(p) ::RooaDoubleCBxBW : new ::RooaDoubleCBxBW;
   }
   static void *newArray_RooaDoubleCBxBW(Long_t nElements, void *p) {
      return p ? new(p) ::RooaDoubleCBxBW[nElements] : new ::RooaDoubleCBxBW[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooaDoubleCBxBW(void *p) {
      delete ((::RooaDoubleCBxBW*)p);
   }
   static void deleteArray_RooaDoubleCBxBW(void *p) {
      delete [] ((::RooaDoubleCBxBW*)p);
   }
   static void destruct_RooaDoubleCBxBW(void *p) {
      typedef ::RooaDoubleCBxBW current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooaDoubleCBxBW

//______________________________________________________________________________
void RooCPSHighMassGGH::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooCPSHighMassGGH.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooCPSHighMassGGH::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooCPSHighMassGGH::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooCPSHighMassGGH(void *p) {
      return  p ? new(p) ::RooCPSHighMassGGH : new ::RooCPSHighMassGGH;
   }
   static void *newArray_RooCPSHighMassGGH(Long_t nElements, void *p) {
      return p ? new(p) ::RooCPSHighMassGGH[nElements] : new ::RooCPSHighMassGGH[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooCPSHighMassGGH(void *p) {
      delete ((::RooCPSHighMassGGH*)p);
   }
   static void deleteArray_RooCPSHighMassGGH(void *p) {
      delete [] ((::RooCPSHighMassGGH*)p);
   }
   static void destruct_RooCPSHighMassGGH(void *p) {
      typedef ::RooCPSHighMassGGH current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooCPSHighMassGGH

//______________________________________________________________________________
void RooBWHighMassGGH::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooBWHighMassGGH.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooBWHighMassGGH::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooBWHighMassGGH::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooBWHighMassGGH(void *p) {
      return  p ? new(p) ::RooBWHighMassGGH : new ::RooBWHighMassGGH;
   }
   static void *newArray_RooBWHighMassGGH(Long_t nElements, void *p) {
      return p ? new(p) ::RooBWHighMassGGH[nElements] : new ::RooBWHighMassGGH[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooBWHighMassGGH(void *p) {
      delete ((::RooBWHighMassGGH*)p);
   }
   static void deleteArray_RooBWHighMassGGH(void *p) {
      delete [] ((::RooBWHighMassGGH*)p);
   }
   static void destruct_RooBWHighMassGGH(void *p) {
      typedef ::RooBWHighMassGGH current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooBWHighMassGGH

//______________________________________________________________________________
void RooCPSHighMassGGHNoInterf::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooCPSHighMassGGHNoInterf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooCPSHighMassGGHNoInterf::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooCPSHighMassGGHNoInterf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooCPSHighMassGGHNoInterf(void *p) {
      return  p ? new(p) ::RooCPSHighMassGGHNoInterf : new ::RooCPSHighMassGGHNoInterf;
   }
   static void *newArray_RooCPSHighMassGGHNoInterf(Long_t nElements, void *p) {
      return p ? new(p) ::RooCPSHighMassGGHNoInterf[nElements] : new ::RooCPSHighMassGGHNoInterf[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooCPSHighMassGGHNoInterf(void *p) {
      delete ((::RooCPSHighMassGGHNoInterf*)p);
   }
   static void deleteArray_RooCPSHighMassGGHNoInterf(void *p) {
      delete [] ((::RooCPSHighMassGGHNoInterf*)p);
   }
   static void destruct_RooCPSHighMassGGHNoInterf(void *p) {
      typedef ::RooCPSHighMassGGHNoInterf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooCPSHighMassGGHNoInterf

//______________________________________________________________________________
void RooCPSHighMassVBF::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooCPSHighMassVBF.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooCPSHighMassVBF::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooCPSHighMassVBF::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooCPSHighMassVBF(void *p) {
      return  p ? new(p) ::RooCPSHighMassVBF : new ::RooCPSHighMassVBF;
   }
   static void *newArray_RooCPSHighMassVBF(Long_t nElements, void *p) {
      return p ? new(p) ::RooCPSHighMassVBF[nElements] : new ::RooCPSHighMassVBF[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooCPSHighMassVBF(void *p) {
      delete ((::RooCPSHighMassVBF*)p);
   }
   static void deleteArray_RooCPSHighMassVBF(void *p) {
      delete [] ((::RooCPSHighMassVBF*)p);
   }
   static void destruct_RooCPSHighMassVBF(void *p) {
      typedef ::RooCPSHighMassVBF current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooCPSHighMassVBF

//______________________________________________________________________________
void RooCPSHighMassVBFNoInterf::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooCPSHighMassVBFNoInterf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooCPSHighMassVBFNoInterf::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooCPSHighMassVBFNoInterf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooCPSHighMassVBFNoInterf(void *p) {
      return  p ? new(p) ::RooCPSHighMassVBFNoInterf : new ::RooCPSHighMassVBFNoInterf;
   }
   static void *newArray_RooCPSHighMassVBFNoInterf(Long_t nElements, void *p) {
      return p ? new(p) ::RooCPSHighMassVBFNoInterf[nElements] : new ::RooCPSHighMassVBFNoInterf[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooCPSHighMassVBFNoInterf(void *p) {
      delete ((::RooCPSHighMassVBFNoInterf*)p);
   }
   static void deleteArray_RooCPSHighMassVBFNoInterf(void *p) {
      delete [] ((::RooCPSHighMassVBFNoInterf*)p);
   }
   static void destruct_RooCPSHighMassVBFNoInterf(void *p) {
      typedef ::RooCPSHighMassVBFNoInterf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooCPSHighMassVBFNoInterf

//______________________________________________________________________________
void RooSigPlusInt::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooSigPlusInt.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooSigPlusInt::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooSigPlusInt::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooSigPlusInt(void *p) {
      return  p ? new(p) ::RooSigPlusInt : new ::RooSigPlusInt;
   }
   static void *newArray_RooSigPlusInt(Long_t nElements, void *p) {
      return p ? new(p) ::RooSigPlusInt[nElements] : new ::RooSigPlusInt[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooSigPlusInt(void *p) {
      delete ((::RooSigPlusInt*)p);
   }
   static void deleteArray_RooSigPlusInt(void *p) {
      delete [] ((::RooSigPlusInt*)p);
   }
   static void destruct_RooSigPlusInt(void *p) {
      typedef ::RooSigPlusInt current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooSigPlusInt

//______________________________________________________________________________
void RooErfExpPdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooErfExpPdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooErfExpPdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooErfExpPdf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooErfExpPdf(void *p) {
      return  p ? new(p) ::RooErfExpPdf : new ::RooErfExpPdf;
   }
   static void *newArray_RooErfExpPdf(Long_t nElements, void *p) {
      return p ? new(p) ::RooErfExpPdf[nElements] : new ::RooErfExpPdf[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooErfExpPdf(void *p) {
      delete ((::RooErfExpPdf*)p);
   }
   static void deleteArray_RooErfExpPdf(void *p) {
      delete [] ((::RooErfExpPdf*)p);
   }
   static void destruct_RooErfExpPdf(void *p) {
      typedef ::RooErfExpPdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooErfExpPdf

//______________________________________________________________________________
void RooAlpha::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooAlpha.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooAlpha::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooAlpha::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooAlpha(void *p) {
      return  p ? new(p) ::RooAlpha : new ::RooAlpha;
   }
   static void *newArray_RooAlpha(Long_t nElements, void *p) {
      return p ? new(p) ::RooAlpha[nElements] : new ::RooAlpha[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooAlpha(void *p) {
      delete ((::RooAlpha*)p);
   }
   static void deleteArray_RooAlpha(void *p) {
      delete [] ((::RooAlpha*)p);
   }
   static void destruct_RooAlpha(void *p) {
      typedef ::RooAlpha current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooAlpha

//______________________________________________________________________________
void RooAlphaExp::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooAlphaExp.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooAlphaExp::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooAlphaExp::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooAlphaExp(void *p) {
      return  p ? new(p) ::RooAlphaExp : new ::RooAlphaExp;
   }
   static void *newArray_RooAlphaExp(Long_t nElements, void *p) {
      return p ? new(p) ::RooAlphaExp[nElements] : new ::RooAlphaExp[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooAlphaExp(void *p) {
      delete ((::RooAlphaExp*)p);
   }
   static void deleteArray_RooAlphaExp(void *p) {
      delete [] ((::RooAlphaExp*)p);
   }
   static void destruct_RooAlphaExp(void *p) {
      typedef ::RooAlphaExp current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooAlphaExp

//______________________________________________________________________________
void RooBWRunPdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooBWRunPdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooBWRunPdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooBWRunPdf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooBWRunPdf(void *p) {
      return  p ? new(p) ::RooBWRunPdf : new ::RooBWRunPdf;
   }
   static void *newArray_RooBWRunPdf(Long_t nElements, void *p) {
      return p ? new(p) ::RooBWRunPdf[nElements] : new ::RooBWRunPdf[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooBWRunPdf(void *p) {
      delete ((::RooBWRunPdf*)p);
   }
   static void deleteArray_RooBWRunPdf(void *p) {
      delete [] ((::RooBWRunPdf*)p);
   }
   static void destruct_RooBWRunPdf(void *p) {
      typedef ::RooBWRunPdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooBWRunPdf

//______________________________________________________________________________
void RooErfPow2Pdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooErfPow2Pdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooErfPow2Pdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooErfPow2Pdf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooErfPow2Pdf(void *p) {
      return  p ? new(p) ::RooErfPow2Pdf : new ::RooErfPow2Pdf;
   }
   static void *newArray_RooErfPow2Pdf(Long_t nElements, void *p) {
      return p ? new(p) ::RooErfPow2Pdf[nElements] : new ::RooErfPow2Pdf[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooErfPow2Pdf(void *p) {
      delete ((::RooErfPow2Pdf*)p);
   }
   static void deleteArray_RooErfPow2Pdf(void *p) {
      delete [] ((::RooErfPow2Pdf*)p);
   }
   static void destruct_RooErfPow2Pdf(void *p) {
      typedef ::RooErfPow2Pdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooErfPow2Pdf

//______________________________________________________________________________
void RooAlpha4ErfPow2Pdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooAlpha4ErfPow2Pdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooAlpha4ErfPow2Pdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooAlpha4ErfPow2Pdf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooAlpha4ErfPow2Pdf(void *p) {
      return  p ? new(p) ::RooAlpha4ErfPow2Pdf : new ::RooAlpha4ErfPow2Pdf;
   }
   static void *newArray_RooAlpha4ErfPow2Pdf(Long_t nElements, void *p) {
      return p ? new(p) ::RooAlpha4ErfPow2Pdf[nElements] : new ::RooAlpha4ErfPow2Pdf[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooAlpha4ErfPow2Pdf(void *p) {
      delete ((::RooAlpha4ErfPow2Pdf*)p);
   }
   static void deleteArray_RooAlpha4ErfPow2Pdf(void *p) {
      delete [] ((::RooAlpha4ErfPow2Pdf*)p);
   }
   static void destruct_RooAlpha4ErfPow2Pdf(void *p) {
      typedef ::RooAlpha4ErfPow2Pdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooAlpha4ErfPow2Pdf

//______________________________________________________________________________
void RooErfPowExpPdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooErfPowExpPdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooErfPowExpPdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooErfPowExpPdf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooErfPowExpPdf(void *p) {
      return  p ? new(p) ::RooErfPowExpPdf : new ::RooErfPowExpPdf;
   }
   static void *newArray_RooErfPowExpPdf(Long_t nElements, void *p) {
      return p ? new(p) ::RooErfPowExpPdf[nElements] : new ::RooErfPowExpPdf[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooErfPowExpPdf(void *p) {
      delete ((::RooErfPowExpPdf*)p);
   }
   static void deleteArray_RooErfPowExpPdf(void *p) {
      delete [] ((::RooErfPowExpPdf*)p);
   }
   static void destruct_RooErfPowExpPdf(void *p) {
      typedef ::RooErfPowExpPdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooErfPowExpPdf

//______________________________________________________________________________
void RooAlpha4ErfPowExpPdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooAlpha4ErfPowExpPdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooAlpha4ErfPowExpPdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooAlpha4ErfPowExpPdf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooAlpha4ErfPowExpPdf(void *p) {
      return  p ? new(p) ::RooAlpha4ErfPowExpPdf : new ::RooAlpha4ErfPowExpPdf;
   }
   static void *newArray_RooAlpha4ErfPowExpPdf(Long_t nElements, void *p) {
      return p ? new(p) ::RooAlpha4ErfPowExpPdf[nElements] : new ::RooAlpha4ErfPowExpPdf[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooAlpha4ErfPowExpPdf(void *p) {
      delete ((::RooAlpha4ErfPowExpPdf*)p);
   }
   static void deleteArray_RooAlpha4ErfPowExpPdf(void *p) {
      delete [] ((::RooAlpha4ErfPowExpPdf*)p);
   }
   static void destruct_RooAlpha4ErfPowExpPdf(void *p) {
      typedef ::RooAlpha4ErfPowExpPdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooAlpha4ErfPowExpPdf

//______________________________________________________________________________
void RooGausExpPdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooGausExpPdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooGausExpPdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooGausExpPdf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooGausExpPdf(void *p) {
      return  p ? new(p) ::RooGausExpPdf : new ::RooGausExpPdf;
   }
   static void *newArray_RooGausExpPdf(Long_t nElements, void *p) {
      return p ? new(p) ::RooGausExpPdf[nElements] : new ::RooGausExpPdf[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooGausExpPdf(void *p) {
      delete ((::RooGausExpPdf*)p);
   }
   static void deleteArray_RooGausExpPdf(void *p) {
      delete [] ((::RooGausExpPdf*)p);
   }
   static void destruct_RooGausExpPdf(void *p) {
      typedef ::RooGausExpPdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooGausExpPdf

//______________________________________________________________________________
void RooAlpha4GausExpPdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooAlpha4GausExpPdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooAlpha4GausExpPdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooAlpha4GausExpPdf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooAlpha4GausExpPdf(void *p) {
      return  p ? new(p) ::RooAlpha4GausExpPdf : new ::RooAlpha4GausExpPdf;
   }
   static void *newArray_RooAlpha4GausExpPdf(Long_t nElements, void *p) {
      return p ? new(p) ::RooAlpha4GausExpPdf[nElements] : new ::RooAlpha4GausExpPdf[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooAlpha4GausExpPdf(void *p) {
      delete ((::RooAlpha4GausExpPdf*)p);
   }
   static void deleteArray_RooAlpha4GausExpPdf(void *p) {
      delete [] ((::RooAlpha4GausExpPdf*)p);
   }
   static void destruct_RooAlpha4GausExpPdf(void *p) {
      typedef ::RooAlpha4GausExpPdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooAlpha4GausExpPdf

//______________________________________________________________________________
void RooErfPowPdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooErfPowPdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooErfPowPdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooErfPowPdf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooErfPowPdf(void *p) {
      return  p ? new(p) ::RooErfPowPdf : new ::RooErfPowPdf;
   }
   static void *newArray_RooErfPowPdf(Long_t nElements, void *p) {
      return p ? new(p) ::RooErfPowPdf[nElements] : new ::RooErfPowPdf[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooErfPowPdf(void *p) {
      delete ((::RooErfPowPdf*)p);
   }
   static void deleteArray_RooErfPowPdf(void *p) {
      delete [] ((::RooErfPowPdf*)p);
   }
   static void destruct_RooErfPowPdf(void *p) {
      typedef ::RooErfPowPdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooErfPowPdf

//______________________________________________________________________________
void RooAlpha4ErfPowPdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooAlpha4ErfPowPdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooAlpha4ErfPowPdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooAlpha4ErfPowPdf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooAlpha4ErfPowPdf(void *p) {
      return  p ? new(p) ::RooAlpha4ErfPowPdf : new ::RooAlpha4ErfPowPdf;
   }
   static void *newArray_RooAlpha4ErfPowPdf(Long_t nElements, void *p) {
      return p ? new(p) ::RooAlpha4ErfPowPdf[nElements] : new ::RooAlpha4ErfPowPdf[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooAlpha4ErfPowPdf(void *p) {
      delete ((::RooAlpha4ErfPowPdf*)p);
   }
   static void deleteArray_RooAlpha4ErfPowPdf(void *p) {
      delete [] ((::RooAlpha4ErfPowPdf*)p);
   }
   static void destruct_RooAlpha4ErfPowPdf(void *p) {
      typedef ::RooAlpha4ErfPowPdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooAlpha4ErfPowPdf

//______________________________________________________________________________
void RooPow2Pdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooPow2Pdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooPow2Pdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooPow2Pdf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooPow2Pdf(void *p) {
      return  p ? new(p) ::RooPow2Pdf : new ::RooPow2Pdf;
   }
   static void *newArray_RooPow2Pdf(Long_t nElements, void *p) {
      return p ? new(p) ::RooPow2Pdf[nElements] : new ::RooPow2Pdf[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooPow2Pdf(void *p) {
      delete ((::RooPow2Pdf*)p);
   }
   static void deleteArray_RooPow2Pdf(void *p) {
      delete [] ((::RooPow2Pdf*)p);
   }
   static void destruct_RooPow2Pdf(void *p) {
      typedef ::RooPow2Pdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooPow2Pdf

//______________________________________________________________________________
void RooPowPdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooPowPdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooPowPdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooPowPdf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooPowPdf(void *p) {
      return  p ? new(p) ::RooPowPdf : new ::RooPowPdf;
   }
   static void *newArray_RooPowPdf(Long_t nElements, void *p) {
      return p ? new(p) ::RooPowPdf[nElements] : new ::RooPowPdf[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooPowPdf(void *p) {
      delete ((::RooPowPdf*)p);
   }
   static void deleteArray_RooPowPdf(void *p) {
      delete [] ((::RooPowPdf*)p);
   }
   static void destruct_RooPowPdf(void *p) {
      typedef ::RooPowPdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooPowPdf

//______________________________________________________________________________
void RooQCDPdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooQCDPdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooQCDPdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooQCDPdf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooQCDPdf(void *p) {
      return  p ? new(p) ::RooQCDPdf : new ::RooQCDPdf;
   }
   static void *newArray_RooQCDPdf(Long_t nElements, void *p) {
      return p ? new(p) ::RooQCDPdf[nElements] : new ::RooQCDPdf[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooQCDPdf(void *p) {
      delete ((::RooQCDPdf*)p);
   }
   static void deleteArray_RooQCDPdf(void *p) {
      delete [] ((::RooQCDPdf*)p);
   }
   static void destruct_RooQCDPdf(void *p) {
      typedef ::RooQCDPdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooQCDPdf

//______________________________________________________________________________
void RooUser1Pdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooUser1Pdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooUser1Pdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooUser1Pdf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooUser1Pdf(void *p) {
      return  p ? new(p) ::RooUser1Pdf : new ::RooUser1Pdf;
   }
   static void *newArray_RooUser1Pdf(Long_t nElements, void *p) {
      return p ? new(p) ::RooUser1Pdf[nElements] : new ::RooUser1Pdf[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooUser1Pdf(void *p) {
      delete ((::RooUser1Pdf*)p);
   }
   static void deleteArray_RooUser1Pdf(void *p) {
      delete [] ((::RooUser1Pdf*)p);
   }
   static void destruct_RooUser1Pdf(void *p) {
      typedef ::RooUser1Pdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooUser1Pdf

//______________________________________________________________________________
void RooExpNPdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooExpNPdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooExpNPdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooExpNPdf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooExpNPdf(void *p) {
      return  p ? new(p) ::RooExpNPdf : new ::RooExpNPdf;
   }
   static void *newArray_RooExpNPdf(Long_t nElements, void *p) {
      return p ? new(p) ::RooExpNPdf[nElements] : new ::RooExpNPdf[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooExpNPdf(void *p) {
      delete ((::RooExpNPdf*)p);
   }
   static void deleteArray_RooExpNPdf(void *p) {
      delete [] ((::RooExpNPdf*)p);
   }
   static void destruct_RooExpNPdf(void *p) {
      typedef ::RooExpNPdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooExpNPdf

//______________________________________________________________________________
void RooAlpha4ExpNPdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooAlpha4ExpNPdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooAlpha4ExpNPdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooAlpha4ExpNPdf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooAlpha4ExpNPdf(void *p) {
      return  p ? new(p) ::RooAlpha4ExpNPdf : new ::RooAlpha4ExpNPdf;
   }
   static void *newArray_RooAlpha4ExpNPdf(Long_t nElements, void *p) {
      return p ? new(p) ::RooAlpha4ExpNPdf[nElements] : new ::RooAlpha4ExpNPdf[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooAlpha4ExpNPdf(void *p) {
      delete ((::RooAlpha4ExpNPdf*)p);
   }
   static void deleteArray_RooAlpha4ExpNPdf(void *p) {
      delete [] ((::RooAlpha4ExpNPdf*)p);
   }
   static void destruct_RooAlpha4ExpNPdf(void *p) {
      typedef ::RooAlpha4ExpNPdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooAlpha4ExpNPdf

//______________________________________________________________________________
void RooExpTailPdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooExpTailPdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooExpTailPdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooExpTailPdf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooExpTailPdf(void *p) {
      return  p ? new(p) ::RooExpTailPdf : new ::RooExpTailPdf;
   }
   static void *newArray_RooExpTailPdf(Long_t nElements, void *p) {
      return p ? new(p) ::RooExpTailPdf[nElements] : new ::RooExpTailPdf[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooExpTailPdf(void *p) {
      delete ((::RooExpTailPdf*)p);
   }
   static void deleteArray_RooExpTailPdf(void *p) {
      delete [] ((::RooExpTailPdf*)p);
   }
   static void destruct_RooExpTailPdf(void *p) {
      typedef ::RooExpTailPdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooExpTailPdf

//______________________________________________________________________________
void RooAlpha4ExpTailPdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooAlpha4ExpTailPdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooAlpha4ExpTailPdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooAlpha4ExpTailPdf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooAlpha4ExpTailPdf(void *p) {
      return  p ? new(p) ::RooAlpha4ExpTailPdf : new ::RooAlpha4ExpTailPdf;
   }
   static void *newArray_RooAlpha4ExpTailPdf(Long_t nElements, void *p) {
      return p ? new(p) ::RooAlpha4ExpTailPdf[nElements] : new ::RooAlpha4ExpTailPdf[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooAlpha4ExpTailPdf(void *p) {
      delete ((::RooAlpha4ExpTailPdf*)p);
   }
   static void deleteArray_RooAlpha4ExpTailPdf(void *p) {
      delete [] ((::RooAlpha4ExpTailPdf*)p);
   }
   static void destruct_RooAlpha4ExpTailPdf(void *p) {
      typedef ::RooAlpha4ExpTailPdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooAlpha4ExpTailPdf

//______________________________________________________________________________
void Roo2ExpPdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class Roo2ExpPdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(Roo2ExpPdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(Roo2ExpPdf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_Roo2ExpPdf(void *p) {
      return  p ? new(p) ::Roo2ExpPdf : new ::Roo2ExpPdf;
   }
   static void *newArray_Roo2ExpPdf(Long_t nElements, void *p) {
      return p ? new(p) ::Roo2ExpPdf[nElements] : new ::Roo2ExpPdf[nElements];
   }
   // Wrapper around operator delete
   static void delete_Roo2ExpPdf(void *p) {
      delete ((::Roo2ExpPdf*)p);
   }
   static void deleteArray_Roo2ExpPdf(void *p) {
      delete [] ((::Roo2ExpPdf*)p);
   }
   static void destruct_Roo2ExpPdf(void *p) {
      typedef ::Roo2ExpPdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::Roo2ExpPdf

//______________________________________________________________________________
void RooAlpha42ExpPdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooAlpha42ExpPdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooAlpha42ExpPdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooAlpha42ExpPdf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooAlpha42ExpPdf(void *p) {
      return  p ? new(p) ::RooAlpha42ExpPdf : new ::RooAlpha42ExpPdf;
   }
   static void *newArray_RooAlpha42ExpPdf(Long_t nElements, void *p) {
      return p ? new(p) ::RooAlpha42ExpPdf[nElements] : new ::RooAlpha42ExpPdf[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooAlpha42ExpPdf(void *p) {
      delete ((::RooAlpha42ExpPdf*)p);
   }
   static void deleteArray_RooAlpha42ExpPdf(void *p) {
      delete [] ((::RooAlpha42ExpPdf*)p);
   }
   static void destruct_RooAlpha42ExpPdf(void *p) {
      typedef ::RooAlpha42ExpPdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooAlpha42ExpPdf

//______________________________________________________________________________
void RooAnaExpNPdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooAnaExpNPdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooAnaExpNPdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooAnaExpNPdf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooAnaExpNPdf(void *p) {
      return  p ? new(p) ::RooAnaExpNPdf : new ::RooAnaExpNPdf;
   }
   static void *newArray_RooAnaExpNPdf(Long_t nElements, void *p) {
      return p ? new(p) ::RooAnaExpNPdf[nElements] : new ::RooAnaExpNPdf[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooAnaExpNPdf(void *p) {
      delete ((::RooAnaExpNPdf*)p);
   }
   static void deleteArray_RooAnaExpNPdf(void *p) {
      delete [] ((::RooAnaExpNPdf*)p);
   }
   static void destruct_RooAnaExpNPdf(void *p) {
      typedef ::RooAnaExpNPdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooAnaExpNPdf

//______________________________________________________________________________
void RooDoubleCrystalBall::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooDoubleCrystalBall.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooDoubleCrystalBall::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooDoubleCrystalBall::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooDoubleCrystalBall(void *p) {
      return  p ? new(p) ::RooDoubleCrystalBall : new ::RooDoubleCrystalBall;
   }
   static void *newArray_RooDoubleCrystalBall(Long_t nElements, void *p) {
      return p ? new(p) ::RooDoubleCrystalBall[nElements] : new ::RooDoubleCrystalBall[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooDoubleCrystalBall(void *p) {
      delete ((::RooDoubleCrystalBall*)p);
   }
   static void deleteArray_RooDoubleCrystalBall(void *p) {
      delete [] ((::RooDoubleCrystalBall*)p);
   }
   static void destruct_RooDoubleCrystalBall(void *p) {
      typedef ::RooDoubleCrystalBall current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooDoubleCrystalBall

//______________________________________________________________________________
void RooCB::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooCB.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooCB::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooCB::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooCB(void *p) {
      return  p ? new(p) ::RooCB : new ::RooCB;
   }
   static void *newArray_RooCB(Long_t nElements, void *p) {
      return p ? new(p) ::RooCB[nElements] : new ::RooCB[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooCB(void *p) {
      delete ((::RooCB*)p);
   }
   static void deleteArray_RooCB(void *p) {
      delete [] ((::RooCB*)p);
   }
   static void destruct_RooCB(void *p) {
      typedef ::RooCB current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooCB

//______________________________________________________________________________
void RooDoubleCB::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooDoubleCB.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooDoubleCB::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooDoubleCB::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooDoubleCB(void *p) {
      return  p ? new(p) ::RooDoubleCB : new ::RooDoubleCB;
   }
   static void *newArray_RooDoubleCB(Long_t nElements, void *p) {
      return p ? new(p) ::RooDoubleCB[nElements] : new ::RooDoubleCB[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooDoubleCB(void *p) {
      delete ((::RooDoubleCB*)p);
   }
   static void deleteArray_RooDoubleCB(void *p) {
      delete [] ((::RooDoubleCB*)p);
   }
   static void destruct_RooDoubleCB(void *p) {
      typedef ::RooDoubleCB current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooDoubleCB

//______________________________________________________________________________
void RooFermi::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooFermi.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooFermi::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooFermi::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooFermi(void *p) {
      return  p ? new(p) ::RooFermi : new ::RooFermi;
   }
   static void *newArray_RooFermi(Long_t nElements, void *p) {
      return p ? new(p) ::RooFermi[nElements] : new ::RooFermi[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooFermi(void *p) {
      delete ((::RooFermi*)p);
   }
   static void deleteArray_RooFermi(void *p) {
      delete [] ((::RooFermi*)p);
   }
   static void destruct_RooFermi(void *p) {
      typedef ::RooFermi current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooFermi

//______________________________________________________________________________
void RooRelBW::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooRelBW.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooRelBW::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooRelBW::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooRelBW(void *p) {
      return  p ? new(p) ::RooRelBW : new ::RooRelBW;
   }
   static void *newArray_RooRelBW(Long_t nElements, void *p) {
      return p ? new(p) ::RooRelBW[nElements] : new ::RooRelBW[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooRelBW(void *p) {
      delete ((::RooRelBW*)p);
   }
   static void deleteArray_RooRelBW(void *p) {
      delete [] ((::RooRelBW*)p);
   }
   static void destruct_RooRelBW(void *p) {
      typedef ::RooRelBW current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooRelBW

//______________________________________________________________________________
void Triangle::Streamer(TBuffer &R__b)
{
   // Stream an object of class Triangle.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(Triangle::Class(),this);
   } else {
      R__b.WriteClassBuffer(Triangle::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_Triangle(void *p) {
      return  p ? new(p) ::Triangle : new ::Triangle;
   }
   static void *newArray_Triangle(Long_t nElements, void *p) {
      return p ? new(p) ::Triangle[nElements] : new ::Triangle[nElements];
   }
   // Wrapper around operator delete
   static void delete_Triangle(void *p) {
      delete ((::Triangle*)p);
   }
   static void deleteArray_Triangle(void *p) {
      delete [] ((::Triangle*)p);
   }
   static void destruct_Triangle(void *p) {
      typedef ::Triangle current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::Triangle

//______________________________________________________________________________
void RooLevelledExp::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooLevelledExp.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooLevelledExp::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooLevelledExp::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooLevelledExp(void *p) {
      return  p ? new(p) ::RooLevelledExp : new ::RooLevelledExp;
   }
   static void *newArray_RooLevelledExp(Long_t nElements, void *p) {
      return p ? new(p) ::RooLevelledExp[nElements] : new ::RooLevelledExp[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooLevelledExp(void *p) {
      delete ((::RooLevelledExp*)p);
   }
   static void deleteArray_RooLevelledExp(void *p) {
      delete [] ((::RooLevelledExp*)p);
   }
   static void destruct_RooLevelledExp(void *p) {
      typedef ::RooLevelledExp current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooLevelledExp

//______________________________________________________________________________
void RooPower::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooPower.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooPower::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooPower::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooPower(void *p) {
      return  p ? new(p) ::RooPower : new ::RooPower;
   }
   static void *newArray_RooPower(Long_t nElements, void *p) {
      return p ? new(p) ::RooPower[nElements] : new ::RooPower[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooPower(void *p) {
      delete ((::RooPower*)p);
   }
   static void deleteArray_RooPower(void *p) {
      delete [] ((::RooPower*)p);
   }
   static void destruct_RooPower(void *p) {
      typedef ::RooPower current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooPower

//______________________________________________________________________________
void RooStepBernstein::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooStepBernstein.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooStepBernstein::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooStepBernstein::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooStepBernstein(void *p) {
      return  p ? new(p) ::RooStepBernstein : new ::RooStepBernstein;
   }
   static void *newArray_RooStepBernstein(Long_t nElements, void *p) {
      return p ? new(p) ::RooStepBernstein[nElements] : new ::RooStepBernstein[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooStepBernstein(void *p) {
      delete ((::RooStepBernstein*)p);
   }
   static void deleteArray_RooStepBernstein(void *p) {
      delete [] ((::RooStepBernstein*)p);
   }
   static void destruct_RooStepBernstein(void *p) {
      typedef ::RooStepBernstein current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooStepBernstein

//______________________________________________________________________________
void RooGaussStepBernstein::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooGaussStepBernstein.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooGaussStepBernstein::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooGaussStepBernstein::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooGaussStepBernstein(void *p) {
      return  p ? new(p) ::RooGaussStepBernstein : new ::RooGaussStepBernstein;
   }
   static void *newArray_RooGaussStepBernstein(Long_t nElements, void *p) {
      return p ? new(p) ::RooGaussStepBernstein[nElements] : new ::RooGaussStepBernstein[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooGaussStepBernstein(void *p) {
      delete ((::RooGaussStepBernstein*)p);
   }
   static void deleteArray_RooGaussStepBernstein(void *p) {
      delete [] ((::RooGaussStepBernstein*)p);
   }
   static void destruct_RooGaussStepBernstein(void *p) {
      typedef ::RooGaussStepBernstein current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooGaussStepBernstein

namespace ROOT {
   // Wrappers around operator new
   static void *new_cmsmathcLcLSequentialMinimizer(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::cmsmath::SequentialMinimizer : new ::cmsmath::SequentialMinimizer;
   }
   static void *newArray_cmsmathcLcLSequentialMinimizer(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::cmsmath::SequentialMinimizer[nElements] : new ::cmsmath::SequentialMinimizer[nElements];
   }
   // Wrapper around operator delete
   static void delete_cmsmathcLcLSequentialMinimizer(void *p) {
      delete ((::cmsmath::SequentialMinimizer*)p);
   }
   static void deleteArray_cmsmathcLcLSequentialMinimizer(void *p) {
      delete [] ((::cmsmath::SequentialMinimizer*)p);
   }
   static void destruct_cmsmathcLcLSequentialMinimizer(void *p) {
      typedef ::cmsmath::SequentialMinimizer current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::cmsmath::SequentialMinimizer

//______________________________________________________________________________
void ProcessNormalization::Streamer(TBuffer &R__b)
{
   // Stream an object of class ProcessNormalization.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(ProcessNormalization::Class(),this);
   } else {
      R__b.WriteClassBuffer(ProcessNormalization::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_ProcessNormalization(void *p) {
      return  p ? new(p) ::ProcessNormalization : new ::ProcessNormalization;
   }
   static void *newArray_ProcessNormalization(Long_t nElements, void *p) {
      return p ? new(p) ::ProcessNormalization[nElements] : new ::ProcessNormalization[nElements];
   }
   // Wrapper around operator delete
   static void delete_ProcessNormalization(void *p) {
      delete ((::ProcessNormalization*)p);
   }
   static void deleteArray_ProcessNormalization(void *p) {
      delete [] ((::ProcessNormalization*)p);
   }
   static void destruct_ProcessNormalization(void *p) {
      typedef ::ProcessNormalization current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::ProcessNormalization

//______________________________________________________________________________
void RooRealFlooredSumPdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooRealFlooredSumPdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooRealFlooredSumPdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooRealFlooredSumPdf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooRealFlooredSumPdf(void *p) {
      return  p ? new(p) ::RooRealFlooredSumPdf : new ::RooRealFlooredSumPdf;
   }
   static void *newArray_RooRealFlooredSumPdf(Long_t nElements, void *p) {
      return p ? new(p) ::RooRealFlooredSumPdf[nElements] : new ::RooRealFlooredSumPdf[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooRealFlooredSumPdf(void *p) {
      delete ((::RooRealFlooredSumPdf*)p);
   }
   static void deleteArray_RooRealFlooredSumPdf(void *p) {
      delete [] ((::RooRealFlooredSumPdf*)p);
   }
   static void destruct_RooRealFlooredSumPdf(void *p) {
      typedef ::RooRealFlooredSumPdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooRealFlooredSumPdf

//______________________________________________________________________________
void RooSpline1D::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooSpline1D.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooSpline1D::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooSpline1D::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooSpline1D(void *p) {
      return  p ? new(p) ::RooSpline1D : new ::RooSpline1D;
   }
   static void *newArray_RooSpline1D(Long_t nElements, void *p) {
      return p ? new(p) ::RooSpline1D[nElements] : new ::RooSpline1D[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooSpline1D(void *p) {
      delete ((::RooSpline1D*)p);
   }
   static void deleteArray_RooSpline1D(void *p) {
      delete [] ((::RooSpline1D*)p);
   }
   static void destruct_RooSpline1D(void *p) {
      typedef ::RooSpline1D current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooSpline1D

//______________________________________________________________________________
void RooSplineND::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooSplineND.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooSplineND::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooSplineND::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooSplineND(void *p) {
      return  p ? new(p) ::RooSplineND : new ::RooSplineND;
   }
   static void *newArray_RooSplineND(Long_t nElements, void *p) {
      return p ? new(p) ::RooSplineND[nElements] : new ::RooSplineND[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooSplineND(void *p) {
      delete ((::RooSplineND*)p);
   }
   static void deleteArray_RooSplineND(void *p) {
      delete [] ((::RooSplineND*)p);
   }
   static void destruct_RooSplineND(void *p) {
      typedef ::RooSplineND current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooSplineND

//______________________________________________________________________________
void RooScaleLOSM::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooScaleLOSM.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooScaleLOSM::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooScaleLOSM::Class(),this);
   }
}

namespace ROOT {
   // Wrapper around operator delete
   static void delete_RooScaleLOSM(void *p) {
      delete ((::RooScaleLOSM*)p);
   }
   static void deleteArray_RooScaleLOSM(void *p) {
      delete [] ((::RooScaleLOSM*)p);
   }
   static void destruct_RooScaleLOSM(void *p) {
      typedef ::RooScaleLOSM current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooScaleLOSM

//______________________________________________________________________________
void RooScaleHGamGamLOSM::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooScaleHGamGamLOSM.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooScaleHGamGamLOSM::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooScaleHGamGamLOSM::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooScaleHGamGamLOSM(void *p) {
      return  p ? new(p) ::RooScaleHGamGamLOSM : new ::RooScaleHGamGamLOSM;
   }
   static void *newArray_RooScaleHGamGamLOSM(Long_t nElements, void *p) {
      return p ? new(p) ::RooScaleHGamGamLOSM[nElements] : new ::RooScaleHGamGamLOSM[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooScaleHGamGamLOSM(void *p) {
      delete ((::RooScaleHGamGamLOSM*)p);
   }
   static void deleteArray_RooScaleHGamGamLOSM(void *p) {
      delete [] ((::RooScaleHGamGamLOSM*)p);
   }
   static void destruct_RooScaleHGamGamLOSM(void *p) {
      typedef ::RooScaleHGamGamLOSM current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooScaleHGamGamLOSM

//______________________________________________________________________________
void RooScaleHGluGluLOSM::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooScaleHGluGluLOSM.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooScaleHGluGluLOSM::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooScaleHGluGluLOSM::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooScaleHGluGluLOSM(void *p) {
      return  p ? new(p) ::RooScaleHGluGluLOSM : new ::RooScaleHGluGluLOSM;
   }
   static void *newArray_RooScaleHGluGluLOSM(Long_t nElements, void *p) {
      return p ? new(p) ::RooScaleHGluGluLOSM[nElements] : new ::RooScaleHGluGluLOSM[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooScaleHGluGluLOSM(void *p) {
      delete ((::RooScaleHGluGluLOSM*)p);
   }
   static void deleteArray_RooScaleHGluGluLOSM(void *p) {
      delete [] ((::RooScaleHGluGluLOSM*)p);
   }
   static void destruct_RooScaleHGluGluLOSM(void *p) {
      typedef ::RooScaleHGluGluLOSM current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooScaleHGluGluLOSM

//______________________________________________________________________________
void RooScaleHGamGamLOSMPlusX::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooScaleHGamGamLOSMPlusX.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooScaleHGamGamLOSMPlusX::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooScaleHGamGamLOSMPlusX::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooScaleHGamGamLOSMPlusX(void *p) {
      return  p ? new(p) ::RooScaleHGamGamLOSMPlusX : new ::RooScaleHGamGamLOSMPlusX;
   }
   static void *newArray_RooScaleHGamGamLOSMPlusX(Long_t nElements, void *p) {
      return p ? new(p) ::RooScaleHGamGamLOSMPlusX[nElements] : new ::RooScaleHGamGamLOSMPlusX[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooScaleHGamGamLOSMPlusX(void *p) {
      delete ((::RooScaleHGamGamLOSMPlusX*)p);
   }
   static void deleteArray_RooScaleHGamGamLOSMPlusX(void *p) {
      delete [] ((::RooScaleHGamGamLOSMPlusX*)p);
   }
   static void destruct_RooScaleHGamGamLOSMPlusX(void *p) {
      typedef ::RooScaleHGamGamLOSMPlusX current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooScaleHGamGamLOSMPlusX

//______________________________________________________________________________
void RooScaleHGluGluLOSMPlusX::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooScaleHGluGluLOSMPlusX.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooScaleHGluGluLOSMPlusX::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooScaleHGluGluLOSMPlusX::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooScaleHGluGluLOSMPlusX(void *p) {
      return  p ? new(p) ::RooScaleHGluGluLOSMPlusX : new ::RooScaleHGluGluLOSMPlusX;
   }
   static void *newArray_RooScaleHGluGluLOSMPlusX(Long_t nElements, void *p) {
      return p ? new(p) ::RooScaleHGluGluLOSMPlusX[nElements] : new ::RooScaleHGluGluLOSMPlusX[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooScaleHGluGluLOSMPlusX(void *p) {
      delete ((::RooScaleHGluGluLOSMPlusX*)p);
   }
   static void deleteArray_RooScaleHGluGluLOSMPlusX(void *p) {
      delete [] ((::RooScaleHGluGluLOSMPlusX*)p);
   }
   static void destruct_RooScaleHGluGluLOSMPlusX(void *p) {
      typedef ::RooScaleHGluGluLOSMPlusX current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooScaleHGluGluLOSMPlusX

//______________________________________________________________________________
void rVrFLikelihood::Streamer(TBuffer &R__b)
{
   // Stream an object of class rVrFLikelihood.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(rVrFLikelihood::Class(),this);
   } else {
      R__b.WriteClassBuffer(rVrFLikelihood::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_rVrFLikelihood(void *p) {
      return  p ? new(p) ::rVrFLikelihood : new ::rVrFLikelihood;
   }
   static void *newArray_rVrFLikelihood(Long_t nElements, void *p) {
      return p ? new(p) ::rVrFLikelihood[nElements] : new ::rVrFLikelihood[nElements];
   }
   // Wrapper around operator delete
   static void delete_rVrFLikelihood(void *p) {
      delete ((::rVrFLikelihood*)p);
   }
   static void deleteArray_rVrFLikelihood(void *p) {
      delete [] ((::rVrFLikelihood*)p);
   }
   static void destruct_rVrFLikelihood(void *p) {
      typedef ::rVrFLikelihood current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::rVrFLikelihood

//______________________________________________________________________________
void RooMultiPdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooMultiPdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooMultiPdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooMultiPdf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooMultiPdf(void *p) {
      return  p ? new(p) ::RooMultiPdf : new ::RooMultiPdf;
   }
   static void *newArray_RooMultiPdf(Long_t nElements, void *p) {
      return p ? new(p) ::RooMultiPdf[nElements] : new ::RooMultiPdf[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooMultiPdf(void *p) {
      delete ((::RooMultiPdf*)p);
   }
   static void deleteArray_RooMultiPdf(void *p) {
      delete [] ((::RooMultiPdf*)p);
   }
   static void destruct_RooMultiPdf(void *p) {
      typedef ::RooMultiPdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooMultiPdf

//______________________________________________________________________________
template <> void RooBernsteinFast<1>::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooBernsteinFast<1>.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooBernsteinFast<1>::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooBernsteinFast<1>::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooBernsteinFastlE1gR(void *p) {
      return  p ? new(p) ::RooBernsteinFast<1> : new ::RooBernsteinFast<1>;
   }
   static void *newArray_RooBernsteinFastlE1gR(Long_t nElements, void *p) {
      return p ? new(p) ::RooBernsteinFast<1>[nElements] : new ::RooBernsteinFast<1>[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooBernsteinFastlE1gR(void *p) {
      delete ((::RooBernsteinFast<1>*)p);
   }
   static void deleteArray_RooBernsteinFastlE1gR(void *p) {
      delete [] ((::RooBernsteinFast<1>*)p);
   }
   static void destruct_RooBernsteinFastlE1gR(void *p) {
      typedef ::RooBernsteinFast<1> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooBernsteinFast<1>

//______________________________________________________________________________
template <> void RooBernsteinFast<2>::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooBernsteinFast<2>.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooBernsteinFast<2>::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooBernsteinFast<2>::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooBernsteinFastlE2gR(void *p) {
      return  p ? new(p) ::RooBernsteinFast<2> : new ::RooBernsteinFast<2>;
   }
   static void *newArray_RooBernsteinFastlE2gR(Long_t nElements, void *p) {
      return p ? new(p) ::RooBernsteinFast<2>[nElements] : new ::RooBernsteinFast<2>[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooBernsteinFastlE2gR(void *p) {
      delete ((::RooBernsteinFast<2>*)p);
   }
   static void deleteArray_RooBernsteinFastlE2gR(void *p) {
      delete [] ((::RooBernsteinFast<2>*)p);
   }
   static void destruct_RooBernsteinFastlE2gR(void *p) {
      typedef ::RooBernsteinFast<2> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooBernsteinFast<2>

//______________________________________________________________________________
template <> void RooBernsteinFast<3>::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooBernsteinFast<3>.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooBernsteinFast<3>::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooBernsteinFast<3>::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooBernsteinFastlE3gR(void *p) {
      return  p ? new(p) ::RooBernsteinFast<3> : new ::RooBernsteinFast<3>;
   }
   static void *newArray_RooBernsteinFastlE3gR(Long_t nElements, void *p) {
      return p ? new(p) ::RooBernsteinFast<3>[nElements] : new ::RooBernsteinFast<3>[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooBernsteinFastlE3gR(void *p) {
      delete ((::RooBernsteinFast<3>*)p);
   }
   static void deleteArray_RooBernsteinFastlE3gR(void *p) {
      delete [] ((::RooBernsteinFast<3>*)p);
   }
   static void destruct_RooBernsteinFastlE3gR(void *p) {
      typedef ::RooBernsteinFast<3> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooBernsteinFast<3>

//______________________________________________________________________________
template <> void RooBernsteinFast<4>::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooBernsteinFast<4>.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooBernsteinFast<4>::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooBernsteinFast<4>::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooBernsteinFastlE4gR(void *p) {
      return  p ? new(p) ::RooBernsteinFast<4> : new ::RooBernsteinFast<4>;
   }
   static void *newArray_RooBernsteinFastlE4gR(Long_t nElements, void *p) {
      return p ? new(p) ::RooBernsteinFast<4>[nElements] : new ::RooBernsteinFast<4>[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooBernsteinFastlE4gR(void *p) {
      delete ((::RooBernsteinFast<4>*)p);
   }
   static void deleteArray_RooBernsteinFastlE4gR(void *p) {
      delete [] ((::RooBernsteinFast<4>*)p);
   }
   static void destruct_RooBernsteinFastlE4gR(void *p) {
      typedef ::RooBernsteinFast<4> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooBernsteinFast<4>

//______________________________________________________________________________
template <> void RooBernsteinFast<5>::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooBernsteinFast<5>.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooBernsteinFast<5>::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooBernsteinFast<5>::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooBernsteinFastlE5gR(void *p) {
      return  p ? new(p) ::RooBernsteinFast<5> : new ::RooBernsteinFast<5>;
   }
   static void *newArray_RooBernsteinFastlE5gR(Long_t nElements, void *p) {
      return p ? new(p) ::RooBernsteinFast<5>[nElements] : new ::RooBernsteinFast<5>[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooBernsteinFastlE5gR(void *p) {
      delete ((::RooBernsteinFast<5>*)p);
   }
   static void deleteArray_RooBernsteinFastlE5gR(void *p) {
      delete [] ((::RooBernsteinFast<5>*)p);
   }
   static void destruct_RooBernsteinFastlE5gR(void *p) {
      typedef ::RooBernsteinFast<5> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooBernsteinFast<5>

//______________________________________________________________________________
template <> void RooBernsteinFast<6>::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooBernsteinFast<6>.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooBernsteinFast<6>::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooBernsteinFast<6>::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooBernsteinFastlE6gR(void *p) {
      return  p ? new(p) ::RooBernsteinFast<6> : new ::RooBernsteinFast<6>;
   }
   static void *newArray_RooBernsteinFastlE6gR(Long_t nElements, void *p) {
      return p ? new(p) ::RooBernsteinFast<6>[nElements] : new ::RooBernsteinFast<6>[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooBernsteinFastlE6gR(void *p) {
      delete ((::RooBernsteinFast<6>*)p);
   }
   static void deleteArray_RooBernsteinFastlE6gR(void *p) {
      delete [] ((::RooBernsteinFast<6>*)p);
   }
   static void destruct_RooBernsteinFastlE6gR(void *p) {
      typedef ::RooBernsteinFast<6> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooBernsteinFast<6>

//______________________________________________________________________________
template <> void RooBernsteinFast<7>::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooBernsteinFast<7>.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooBernsteinFast<7>::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooBernsteinFast<7>::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooBernsteinFastlE7gR(void *p) {
      return  p ? new(p) ::RooBernsteinFast<7> : new ::RooBernsteinFast<7>;
   }
   static void *newArray_RooBernsteinFastlE7gR(Long_t nElements, void *p) {
      return p ? new(p) ::RooBernsteinFast<7>[nElements] : new ::RooBernsteinFast<7>[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooBernsteinFastlE7gR(void *p) {
      delete ((::RooBernsteinFast<7>*)p);
   }
   static void deleteArray_RooBernsteinFastlE7gR(void *p) {
      delete [] ((::RooBernsteinFast<7>*)p);
   }
   static void destruct_RooBernsteinFastlE7gR(void *p) {
      typedef ::RooBernsteinFast<7> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooBernsteinFast<7>

//______________________________________________________________________________
void SimpleGaussianConstraint::Streamer(TBuffer &R__b)
{
   // Stream an object of class SimpleGaussianConstraint.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(SimpleGaussianConstraint::Class(),this);
   } else {
      R__b.WriteClassBuffer(SimpleGaussianConstraint::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_SimpleGaussianConstraint(void *p) {
      return  p ? new(p) ::SimpleGaussianConstraint : new ::SimpleGaussianConstraint;
   }
   static void *newArray_SimpleGaussianConstraint(Long_t nElements, void *p) {
      return p ? new(p) ::SimpleGaussianConstraint[nElements] : new ::SimpleGaussianConstraint[nElements];
   }
   // Wrapper around operator delete
   static void delete_SimpleGaussianConstraint(void *p) {
      delete ((::SimpleGaussianConstraint*)p);
   }
   static void deleteArray_SimpleGaussianConstraint(void *p) {
      delete [] ((::SimpleGaussianConstraint*)p);
   }
   static void destruct_SimpleGaussianConstraint(void *p) {
      typedef ::SimpleGaussianConstraint current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::SimpleGaussianConstraint

//______________________________________________________________________________
void SimplePoissonConstraint::Streamer(TBuffer &R__b)
{
   // Stream an object of class SimplePoissonConstraint.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(SimplePoissonConstraint::Class(),this);
   } else {
      R__b.WriteClassBuffer(SimplePoissonConstraint::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_SimplePoissonConstraint(void *p) {
      return  p ? new(p) ::SimplePoissonConstraint : new ::SimplePoissonConstraint;
   }
   static void *newArray_SimplePoissonConstraint(Long_t nElements, void *p) {
      return p ? new(p) ::SimplePoissonConstraint[nElements] : new ::SimplePoissonConstraint[nElements];
   }
   // Wrapper around operator delete
   static void delete_SimplePoissonConstraint(void *p) {
      delete ((::SimplePoissonConstraint*)p);
   }
   static void deleteArray_SimplePoissonConstraint(void *p) {
      delete [] ((::SimplePoissonConstraint*)p);
   }
   static void destruct_SimplePoissonConstraint(void *p) {
      typedef ::SimplePoissonConstraint current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::SimplePoissonConstraint

//______________________________________________________________________________
void SimpleConstraintGroup::Streamer(TBuffer &R__b)
{
   // Stream an object of class SimpleConstraintGroup.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(SimpleConstraintGroup::Class(),this);
   } else {
      R__b.WriteClassBuffer(SimpleConstraintGroup::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_SimpleConstraintGroup(void *p) {
      return  p ? new(p) ::SimpleConstraintGroup : new ::SimpleConstraintGroup;
   }
   static void *newArray_SimpleConstraintGroup(Long_t nElements, void *p) {
      return p ? new(p) ::SimpleConstraintGroup[nElements] : new ::SimpleConstraintGroup[nElements];
   }
   // Wrapper around operator delete
   static void delete_SimpleConstraintGroup(void *p) {
      delete ((::SimpleConstraintGroup*)p);
   }
   static void deleteArray_SimpleConstraintGroup(void *p) {
      delete [] ((::SimpleConstraintGroup*)p);
   }
   static void destruct_SimpleConstraintGroup(void *p) {
      typedef ::SimpleConstraintGroup current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::SimpleConstraintGroup

namespace RooStats {
   namespace HistFactory {
//______________________________________________________________________________
void RooBSplineBases::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooStats::HistFactory::RooBSplineBases.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooStats::HistFactory::RooBSplineBases::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooStats::HistFactory::RooBSplineBases::Class(),this);
   }
}

} // namespace RooStats::HistFactory
} // namespace RooStats::HistFactory
namespace ROOT {
   // Wrappers around operator new
   static void *new_RooStatscLcLHistFactorycLcLRooBSplineBases(void *p) {
      return  p ? new(p) ::RooStats::HistFactory::RooBSplineBases : new ::RooStats::HistFactory::RooBSplineBases;
   }
   static void *newArray_RooStatscLcLHistFactorycLcLRooBSplineBases(Long_t nElements, void *p) {
      return p ? new(p) ::RooStats::HistFactory::RooBSplineBases[nElements] : new ::RooStats::HistFactory::RooBSplineBases[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooStatscLcLHistFactorycLcLRooBSplineBases(void *p) {
      delete ((::RooStats::HistFactory::RooBSplineBases*)p);
   }
   static void deleteArray_RooStatscLcLHistFactorycLcLRooBSplineBases(void *p) {
      delete [] ((::RooStats::HistFactory::RooBSplineBases*)p);
   }
   static void destruct_RooStatscLcLHistFactorycLcLRooBSplineBases(void *p) {
      typedef ::RooStats::HistFactory::RooBSplineBases current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooStats::HistFactory::RooBSplineBases

namespace RooStats {
   namespace HistFactory {
//______________________________________________________________________________
void RooBSpline::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooStats::HistFactory::RooBSpline.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooStats::HistFactory::RooBSpline::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooStats::HistFactory::RooBSpline::Class(),this);
   }
}

} // namespace RooStats::HistFactory
} // namespace RooStats::HistFactory
namespace ROOT {
   // Wrappers around operator new
   static void *new_RooStatscLcLHistFactorycLcLRooBSpline(void *p) {
      return  p ? new(p) ::RooStats::HistFactory::RooBSpline : new ::RooStats::HistFactory::RooBSpline;
   }
   static void *newArray_RooStatscLcLHistFactorycLcLRooBSpline(Long_t nElements, void *p) {
      return p ? new(p) ::RooStats::HistFactory::RooBSpline[nElements] : new ::RooStats::HistFactory::RooBSpline[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooStatscLcLHistFactorycLcLRooBSpline(void *p) {
      delete ((::RooStats::HistFactory::RooBSpline*)p);
   }
   static void deleteArray_RooStatscLcLHistFactorycLcLRooBSpline(void *p) {
      delete [] ((::RooStats::HistFactory::RooBSpline*)p);
   }
   static void destruct_RooStatscLcLHistFactorycLcLRooBSpline(void *p) {
      typedef ::RooStats::HistFactory::RooBSpline current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooStats::HistFactory::RooBSpline

//______________________________________________________________________________
void RooParamKeysPdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooParamKeysPdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooParamKeysPdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooParamKeysPdf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooParamKeysPdf(void *p) {
      return  p ? new(p) ::RooParamKeysPdf : new ::RooParamKeysPdf;
   }
   static void *newArray_RooParamKeysPdf(Long_t nElements, void *p) {
      return p ? new(p) ::RooParamKeysPdf[nElements] : new ::RooParamKeysPdf[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooParamKeysPdf(void *p) {
      delete ((::RooParamKeysPdf*)p);
   }
   static void deleteArray_RooParamKeysPdf(void *p) {
      delete [] ((::RooParamKeysPdf*)p);
   }
   static void destruct_RooParamKeysPdf(void *p) {
      typedef ::RooParamKeysPdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooParamKeysPdf

//______________________________________________________________________________
void RooStarMomentMorph::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooStarMomentMorph.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooStarMomentMorph::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooStarMomentMorph::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooStarMomentMorph(void *p) {
      return  p ? new(p) ::RooStarMomentMorph : new ::RooStarMomentMorph;
   }
   static void *newArray_RooStarMomentMorph(Long_t nElements, void *p) {
      return p ? new(p) ::RooStarMomentMorph[nElements] : new ::RooStarMomentMorph[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooStarMomentMorph(void *p) {
      delete ((::RooStarMomentMorph*)p);
   }
   static void deleteArray_RooStarMomentMorph(void *p) {
      delete [] ((::RooStarMomentMorph*)p);
   }
   static void destruct_RooStarMomentMorph(void *p) {
      typedef ::RooStarMomentMorph current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooStarMomentMorph

namespace ROOT {
   // Wrappers around operator new
   static void *new_FastHistoAxis_tlEdoublegR(void *p) {
      return  p ? new(p) ::FastHistoAxis_t<double> : new ::FastHistoAxis_t<double>;
   }
   static void *newArray_FastHistoAxis_tlEdoublegR(Long_t nElements, void *p) {
      return p ? new(p) ::FastHistoAxis_t<double>[nElements] : new ::FastHistoAxis_t<double>[nElements];
   }
   // Wrapper around operator delete
   static void delete_FastHistoAxis_tlEdoublegR(void *p) {
      delete ((::FastHistoAxis_t<double>*)p);
   }
   static void deleteArray_FastHistoAxis_tlEdoublegR(void *p) {
      delete [] ((::FastHistoAxis_t<double>*)p);
   }
   static void destruct_FastHistoAxis_tlEdoublegR(void *p) {
      typedef ::FastHistoAxis_t<double> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::FastHistoAxis_t<double>

namespace ROOT {
   // Wrappers around operator new
   static void *new_FastHistoAxis_tlEfloatgR(void *p) {
      return  p ? new(p) ::FastHistoAxis_t<float> : new ::FastHistoAxis_t<float>;
   }
   static void *newArray_FastHistoAxis_tlEfloatgR(Long_t nElements, void *p) {
      return p ? new(p) ::FastHistoAxis_t<float>[nElements] : new ::FastHistoAxis_t<float>[nElements];
   }
   // Wrapper around operator delete
   static void delete_FastHistoAxis_tlEfloatgR(void *p) {
      delete ((::FastHistoAxis_t<float>*)p);
   }
   static void deleteArray_FastHistoAxis_tlEfloatgR(void *p) {
      delete [] ((::FastHistoAxis_t<float>*)p);
   }
   static void destruct_FastHistoAxis_tlEfloatgR(void *p) {
      typedef ::FastHistoAxis_t<float> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::FastHistoAxis_t<float>

namespace ROOT {
   // Wrappers around operator new
   static void *new_FastTemplate_tlEdoublegR(void *p) {
      return  p ? new(p) ::FastTemplate_t<double> : new ::FastTemplate_t<double>;
   }
   static void *newArray_FastTemplate_tlEdoublegR(Long_t nElements, void *p) {
      return p ? new(p) ::FastTemplate_t<double>[nElements] : new ::FastTemplate_t<double>[nElements];
   }
   // Wrapper around operator delete
   static void delete_FastTemplate_tlEdoublegR(void *p) {
      delete ((::FastTemplate_t<double>*)p);
   }
   static void deleteArray_FastTemplate_tlEdoublegR(void *p) {
      delete [] ((::FastTemplate_t<double>*)p);
   }
   static void destruct_FastTemplate_tlEdoublegR(void *p) {
      typedef ::FastTemplate_t<double> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::FastTemplate_t<double>

namespace ROOT {
   // Wrappers around operator new
   static void *new_FastTemplate_tlEfloatgR(void *p) {
      return  p ? new(p) ::FastTemplate_t<float> : new ::FastTemplate_t<float>;
   }
   static void *newArray_FastTemplate_tlEfloatgR(Long_t nElements, void *p) {
      return p ? new(p) ::FastTemplate_t<float>[nElements] : new ::FastTemplate_t<float>[nElements];
   }
   // Wrapper around operator delete
   static void delete_FastTemplate_tlEfloatgR(void *p) {
      delete ((::FastTemplate_t<float>*)p);
   }
   static void deleteArray_FastTemplate_tlEfloatgR(void *p) {
      delete [] ((::FastTemplate_t<float>*)p);
   }
   static void destruct_FastTemplate_tlEfloatgR(void *p) {
      typedef ::FastTemplate_t<float> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::FastTemplate_t<float>

namespace ROOT {
   // Wrappers around operator new
   static void *new_FastHisto_tlEdoublecOdoublegR(void *p) {
      return  p ? new(p) ::FastHisto_t<double,double> : new ::FastHisto_t<double,double>;
   }
   static void *newArray_FastHisto_tlEdoublecOdoublegR(Long_t nElements, void *p) {
      return p ? new(p) ::FastHisto_t<double,double>[nElements] : new ::FastHisto_t<double,double>[nElements];
   }
   // Wrapper around operator delete
   static void delete_FastHisto_tlEdoublecOdoublegR(void *p) {
      delete ((::FastHisto_t<double,double>*)p);
   }
   static void deleteArray_FastHisto_tlEdoublecOdoublegR(void *p) {
      delete [] ((::FastHisto_t<double,double>*)p);
   }
   static void destruct_FastHisto_tlEdoublecOdoublegR(void *p) {
      typedef ::FastHisto_t<double,double> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::FastHisto_t<double,double>

namespace ROOT {
   // Wrappers around operator new
   static void *new_FastHisto_tlEfloatcOdoublegR(void *p) {
      return  p ? new(p) ::FastHisto_t<float,double> : new ::FastHisto_t<float,double>;
   }
   static void *newArray_FastHisto_tlEfloatcOdoublegR(Long_t nElements, void *p) {
      return p ? new(p) ::FastHisto_t<float,double>[nElements] : new ::FastHisto_t<float,double>[nElements];
   }
   // Wrapper around operator delete
   static void delete_FastHisto_tlEfloatcOdoublegR(void *p) {
      delete ((::FastHisto_t<float,double>*)p);
   }
   static void deleteArray_FastHisto_tlEfloatcOdoublegR(void *p) {
      delete [] ((::FastHisto_t<float,double>*)p);
   }
   static void destruct_FastHisto_tlEfloatcOdoublegR(void *p) {
      typedef ::FastHisto_t<float,double> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::FastHisto_t<float,double>

namespace ROOT {
   // Wrappers around operator new
   static void *new_FastHisto2D_tlEdoublecOdoublegR(void *p) {
      return  p ? new(p) ::FastHisto2D_t<double,double> : new ::FastHisto2D_t<double,double>;
   }
   static void *newArray_FastHisto2D_tlEdoublecOdoublegR(Long_t nElements, void *p) {
      return p ? new(p) ::FastHisto2D_t<double,double>[nElements] : new ::FastHisto2D_t<double,double>[nElements];
   }
   // Wrapper around operator delete
   static void delete_FastHisto2D_tlEdoublecOdoublegR(void *p) {
      delete ((::FastHisto2D_t<double,double>*)p);
   }
   static void deleteArray_FastHisto2D_tlEdoublecOdoublegR(void *p) {
      delete [] ((::FastHisto2D_t<double,double>*)p);
   }
   static void destruct_FastHisto2D_tlEdoublecOdoublegR(void *p) {
      typedef ::FastHisto2D_t<double,double> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::FastHisto2D_t<double,double>

namespace ROOT {
   // Wrappers around operator new
   static void *new_FastHisto2D_tlEfloatcOdoublegR(void *p) {
      return  p ? new(p) ::FastHisto2D_t<float,double> : new ::FastHisto2D_t<float,double>;
   }
   static void *newArray_FastHisto2D_tlEfloatcOdoublegR(Long_t nElements, void *p) {
      return p ? new(p) ::FastHisto2D_t<float,double>[nElements] : new ::FastHisto2D_t<float,double>[nElements];
   }
   // Wrapper around operator delete
   static void delete_FastHisto2D_tlEfloatcOdoublegR(void *p) {
      delete ((::FastHisto2D_t<float,double>*)p);
   }
   static void deleteArray_FastHisto2D_tlEfloatcOdoublegR(void *p) {
      delete [] ((::FastHisto2D_t<float,double>*)p);
   }
   static void destruct_FastHisto2D_tlEfloatcOdoublegR(void *p) {
      typedef ::FastHisto2D_t<float,double> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::FastHisto2D_t<float,double>

namespace ROOT {
   // Wrappers around operator new
   static void *new_FastHisto3D_tlEdoublecOdoublegR(void *p) {
      return  p ? new(p) ::FastHisto3D_t<double,double> : new ::FastHisto3D_t<double,double>;
   }
   static void *newArray_FastHisto3D_tlEdoublecOdoublegR(Long_t nElements, void *p) {
      return p ? new(p) ::FastHisto3D_t<double,double>[nElements] : new ::FastHisto3D_t<double,double>[nElements];
   }
   // Wrapper around operator delete
   static void delete_FastHisto3D_tlEdoublecOdoublegR(void *p) {
      delete ((::FastHisto3D_t<double,double>*)p);
   }
   static void deleteArray_FastHisto3D_tlEdoublecOdoublegR(void *p) {
      delete [] ((::FastHisto3D_t<double,double>*)p);
   }
   static void destruct_FastHisto3D_tlEdoublecOdoublegR(void *p) {
      typedef ::FastHisto3D_t<double,double> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::FastHisto3D_t<double,double>

namespace ROOT {
   // Wrappers around operator new
   static void *new_FastHisto3D_tlEfloatcOdoublegR(void *p) {
      return  p ? new(p) ::FastHisto3D_t<float,double> : new ::FastHisto3D_t<float,double>;
   }
   static void *newArray_FastHisto3D_tlEfloatcOdoublegR(Long_t nElements, void *p) {
      return p ? new(p) ::FastHisto3D_t<float,double>[nElements] : new ::FastHisto3D_t<float,double>[nElements];
   }
   // Wrapper around operator delete
   static void delete_FastHisto3D_tlEfloatcOdoublegR(void *p) {
      delete ((::FastHisto3D_t<float,double>*)p);
   }
   static void deleteArray_FastHisto3D_tlEfloatcOdoublegR(void *p) {
      delete [] ((::FastHisto3D_t<float,double>*)p);
   }
   static void destruct_FastHisto3D_tlEfloatcOdoublegR(void *p) {
      typedef ::FastHisto3D_t<float,double> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::FastHisto3D_t<float,double>

//______________________________________________________________________________
template <> void FastTemplateFunc_t<float>::Streamer(TBuffer &R__b)
{
   // Stream an object of class FastTemplateFunc_t<float>.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(FastTemplateFunc_t<float>::Class(),this);
   } else {
      R__b.WriteClassBuffer(FastTemplateFunc_t<float>::Class(),this);
   }
}

namespace ROOT {
   // Wrapper around operator delete
   static void delete_FastTemplateFunc_tlEfloatgR(void *p) {
      delete ((::FastTemplateFunc_t<float>*)p);
   }
   static void deleteArray_FastTemplateFunc_tlEfloatgR(void *p) {
      delete [] ((::FastTemplateFunc_t<float>*)p);
   }
   static void destruct_FastTemplateFunc_tlEfloatgR(void *p) {
      typedef ::FastTemplateFunc_t<float> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::FastTemplateFunc_t<float>

//______________________________________________________________________________
template <> void FastTemplateFunc_t<double>::Streamer(TBuffer &R__b)
{
   // Stream an object of class FastTemplateFunc_t<double>.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(FastTemplateFunc_t<double>::Class(),this);
   } else {
      R__b.WriteClassBuffer(FastTemplateFunc_t<double>::Class(),this);
   }
}

namespace ROOT {
   // Wrapper around operator delete
   static void delete_FastTemplateFunc_tlEdoublegR(void *p) {
      delete ((::FastTemplateFunc_t<double>*)p);
   }
   static void deleteArray_FastTemplateFunc_tlEdoublegR(void *p) {
      delete [] ((::FastTemplateFunc_t<double>*)p);
   }
   static void destruct_FastTemplateFunc_tlEdoublegR(void *p) {
      typedef ::FastTemplateFunc_t<double> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::FastTemplateFunc_t<double>

//______________________________________________________________________________
template <> void FastHistoFunc_t<float,double>::Streamer(TBuffer &R__b)
{
   // Stream an object of class FastHistoFunc_t<float,double>.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(FastHistoFunc_t<float,double>::Class(),this);
   } else {
      R__b.WriteClassBuffer(FastHistoFunc_t<float,double>::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_FastHistoFunc_tlEfloatcOdoublegR(void *p) {
      return  p ? new(p) ::FastHistoFunc_t<float,double> : new ::FastHistoFunc_t<float,double>;
   }
   static void *newArray_FastHistoFunc_tlEfloatcOdoublegR(Long_t nElements, void *p) {
      return p ? new(p) ::FastHistoFunc_t<float,double>[nElements] : new ::FastHistoFunc_t<float,double>[nElements];
   }
   // Wrapper around operator delete
   static void delete_FastHistoFunc_tlEfloatcOdoublegR(void *p) {
      delete ((::FastHistoFunc_t<float,double>*)p);
   }
   static void deleteArray_FastHistoFunc_tlEfloatcOdoublegR(void *p) {
      delete [] ((::FastHistoFunc_t<float,double>*)p);
   }
   static void destruct_FastHistoFunc_tlEfloatcOdoublegR(void *p) {
      typedef ::FastHistoFunc_t<float,double> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::FastHistoFunc_t<float,double>

//______________________________________________________________________________
template <> void FastHistoFunc_t<double,double>::Streamer(TBuffer &R__b)
{
   // Stream an object of class FastHistoFunc_t<double,double>.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(FastHistoFunc_t<double,double>::Class(),this);
   } else {
      R__b.WriteClassBuffer(FastHistoFunc_t<double,double>::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_FastHistoFunc_tlEdoublecOdoublegR(void *p) {
      return  p ? new(p) ::FastHistoFunc_t<double,double> : new ::FastHistoFunc_t<double,double>;
   }
   static void *newArray_FastHistoFunc_tlEdoublecOdoublegR(Long_t nElements, void *p) {
      return p ? new(p) ::FastHistoFunc_t<double,double>[nElements] : new ::FastHistoFunc_t<double,double>[nElements];
   }
   // Wrapper around operator delete
   static void delete_FastHistoFunc_tlEdoublecOdoublegR(void *p) {
      delete ((::FastHistoFunc_t<double,double>*)p);
   }
   static void deleteArray_FastHistoFunc_tlEdoublecOdoublegR(void *p) {
      delete [] ((::FastHistoFunc_t<double,double>*)p);
   }
   static void destruct_FastHistoFunc_tlEdoublecOdoublegR(void *p) {
      typedef ::FastHistoFunc_t<double,double> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::FastHistoFunc_t<double,double>

//______________________________________________________________________________
template <> void FastHisto2DFunc_t<float,double>::Streamer(TBuffer &R__b)
{
   // Stream an object of class FastHisto2DFunc_t<float,double>.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(FastHisto2DFunc_t<float,double>::Class(),this);
   } else {
      R__b.WriteClassBuffer(FastHisto2DFunc_t<float,double>::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_FastHisto2DFunc_tlEfloatcOdoublegR(void *p) {
      return  p ? new(p) ::FastHisto2DFunc_t<float,double> : new ::FastHisto2DFunc_t<float,double>;
   }
   static void *newArray_FastHisto2DFunc_tlEfloatcOdoublegR(Long_t nElements, void *p) {
      return p ? new(p) ::FastHisto2DFunc_t<float,double>[nElements] : new ::FastHisto2DFunc_t<float,double>[nElements];
   }
   // Wrapper around operator delete
   static void delete_FastHisto2DFunc_tlEfloatcOdoublegR(void *p) {
      delete ((::FastHisto2DFunc_t<float,double>*)p);
   }
   static void deleteArray_FastHisto2DFunc_tlEfloatcOdoublegR(void *p) {
      delete [] ((::FastHisto2DFunc_t<float,double>*)p);
   }
   static void destruct_FastHisto2DFunc_tlEfloatcOdoublegR(void *p) {
      typedef ::FastHisto2DFunc_t<float,double> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::FastHisto2DFunc_t<float,double>

//______________________________________________________________________________
template <> void FastHisto2DFunc_t<double,double>::Streamer(TBuffer &R__b)
{
   // Stream an object of class FastHisto2DFunc_t<double,double>.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(FastHisto2DFunc_t<double,double>::Class(),this);
   } else {
      R__b.WriteClassBuffer(FastHisto2DFunc_t<double,double>::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_FastHisto2DFunc_tlEdoublecOdoublegR(void *p) {
      return  p ? new(p) ::FastHisto2DFunc_t<double,double> : new ::FastHisto2DFunc_t<double,double>;
   }
   static void *newArray_FastHisto2DFunc_tlEdoublecOdoublegR(Long_t nElements, void *p) {
      return p ? new(p) ::FastHisto2DFunc_t<double,double>[nElements] : new ::FastHisto2DFunc_t<double,double>[nElements];
   }
   // Wrapper around operator delete
   static void delete_FastHisto2DFunc_tlEdoublecOdoublegR(void *p) {
      delete ((::FastHisto2DFunc_t<double,double>*)p);
   }
   static void deleteArray_FastHisto2DFunc_tlEdoublecOdoublegR(void *p) {
      delete [] ((::FastHisto2DFunc_t<double,double>*)p);
   }
   static void destruct_FastHisto2DFunc_tlEdoublecOdoublegR(void *p) {
      typedef ::FastHisto2DFunc_t<double,double> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::FastHisto2DFunc_t<double,double>

//______________________________________________________________________________
template <> void FastHisto3DFunc_t<float,double>::Streamer(TBuffer &R__b)
{
   // Stream an object of class FastHisto3DFunc_t<float,double>.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(FastHisto3DFunc_t<float,double>::Class(),this);
   } else {
      R__b.WriteClassBuffer(FastHisto3DFunc_t<float,double>::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_FastHisto3DFunc_tlEfloatcOdoublegR(void *p) {
      return  p ? new(p) ::FastHisto3DFunc_t<float,double> : new ::FastHisto3DFunc_t<float,double>;
   }
   static void *newArray_FastHisto3DFunc_tlEfloatcOdoublegR(Long_t nElements, void *p) {
      return p ? new(p) ::FastHisto3DFunc_t<float,double>[nElements] : new ::FastHisto3DFunc_t<float,double>[nElements];
   }
   // Wrapper around operator delete
   static void delete_FastHisto3DFunc_tlEfloatcOdoublegR(void *p) {
      delete ((::FastHisto3DFunc_t<float,double>*)p);
   }
   static void deleteArray_FastHisto3DFunc_tlEfloatcOdoublegR(void *p) {
      delete [] ((::FastHisto3DFunc_t<float,double>*)p);
   }
   static void destruct_FastHisto3DFunc_tlEfloatcOdoublegR(void *p) {
      typedef ::FastHisto3DFunc_t<float,double> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::FastHisto3DFunc_t<float,double>

//______________________________________________________________________________
template <> void FastHisto3DFunc_t<double,double>::Streamer(TBuffer &R__b)
{
   // Stream an object of class FastHisto3DFunc_t<double,double>.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(FastHisto3DFunc_t<double,double>::Class(),this);
   } else {
      R__b.WriteClassBuffer(FastHisto3DFunc_t<double,double>::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_FastHisto3DFunc_tlEdoublecOdoublegR(void *p) {
      return  p ? new(p) ::FastHisto3DFunc_t<double,double> : new ::FastHisto3DFunc_t<double,double>;
   }
   static void *newArray_FastHisto3DFunc_tlEdoublecOdoublegR(Long_t nElements, void *p) {
      return p ? new(p) ::FastHisto3DFunc_t<double,double>[nElements] : new ::FastHisto3DFunc_t<double,double>[nElements];
   }
   // Wrapper around operator delete
   static void delete_FastHisto3DFunc_tlEdoublecOdoublegR(void *p) {
      delete ((::FastHisto3DFunc_t<double,double>*)p);
   }
   static void deleteArray_FastHisto3DFunc_tlEdoublecOdoublegR(void *p) {
      delete [] ((::FastHisto3DFunc_t<double,double>*)p);
   }
   static void destruct_FastHisto3DFunc_tlEdoublecOdoublegR(void *p) {
      typedef ::FastHisto3DFunc_t<double,double> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::FastHisto3DFunc_t<double,double>

//______________________________________________________________________________
void HZZ4L_RooSpinZeroPdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class HZZ4L_RooSpinZeroPdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(HZZ4L_RooSpinZeroPdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(HZZ4L_RooSpinZeroPdf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_HZZ4L_RooSpinZeroPdf(void *p) {
      return  p ? new(p) ::HZZ4L_RooSpinZeroPdf : new ::HZZ4L_RooSpinZeroPdf;
   }
   static void *newArray_HZZ4L_RooSpinZeroPdf(Long_t nElements, void *p) {
      return p ? new(p) ::HZZ4L_RooSpinZeroPdf[nElements] : new ::HZZ4L_RooSpinZeroPdf[nElements];
   }
   // Wrapper around operator delete
   static void delete_HZZ4L_RooSpinZeroPdf(void *p) {
      delete ((::HZZ4L_RooSpinZeroPdf*)p);
   }
   static void deleteArray_HZZ4L_RooSpinZeroPdf(void *p) {
      delete [] ((::HZZ4L_RooSpinZeroPdf*)p);
   }
   static void destruct_HZZ4L_RooSpinZeroPdf(void *p) {
      typedef ::HZZ4L_RooSpinZeroPdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::HZZ4L_RooSpinZeroPdf

//______________________________________________________________________________
void HZZ4L_RooSpinZeroPdf_1D::Streamer(TBuffer &R__b)
{
   // Stream an object of class HZZ4L_RooSpinZeroPdf_1D.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(HZZ4L_RooSpinZeroPdf_1D::Class(),this);
   } else {
      R__b.WriteClassBuffer(HZZ4L_RooSpinZeroPdf_1D::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_HZZ4L_RooSpinZeroPdf_1D(void *p) {
      return  p ? new(p) ::HZZ4L_RooSpinZeroPdf_1D : new ::HZZ4L_RooSpinZeroPdf_1D;
   }
   static void *newArray_HZZ4L_RooSpinZeroPdf_1D(Long_t nElements, void *p) {
      return p ? new(p) ::HZZ4L_RooSpinZeroPdf_1D[nElements] : new ::HZZ4L_RooSpinZeroPdf_1D[nElements];
   }
   // Wrapper around operator delete
   static void delete_HZZ4L_RooSpinZeroPdf_1D(void *p) {
      delete ((::HZZ4L_RooSpinZeroPdf_1D*)p);
   }
   static void deleteArray_HZZ4L_RooSpinZeroPdf_1D(void *p) {
      delete [] ((::HZZ4L_RooSpinZeroPdf_1D*)p);
   }
   static void destruct_HZZ4L_RooSpinZeroPdf_1D(void *p) {
      typedef ::HZZ4L_RooSpinZeroPdf_1D current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::HZZ4L_RooSpinZeroPdf_1D

//______________________________________________________________________________
void HZZ4L_RooSpinZeroPdf_2D::Streamer(TBuffer &R__b)
{
   // Stream an object of class HZZ4L_RooSpinZeroPdf_2D.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(HZZ4L_RooSpinZeroPdf_2D::Class(),this);
   } else {
      R__b.WriteClassBuffer(HZZ4L_RooSpinZeroPdf_2D::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_HZZ4L_RooSpinZeroPdf_2D(void *p) {
      return  p ? new(p) ::HZZ4L_RooSpinZeroPdf_2D : new ::HZZ4L_RooSpinZeroPdf_2D;
   }
   static void *newArray_HZZ4L_RooSpinZeroPdf_2D(Long_t nElements, void *p) {
      return p ? new(p) ::HZZ4L_RooSpinZeroPdf_2D[nElements] : new ::HZZ4L_RooSpinZeroPdf_2D[nElements];
   }
   // Wrapper around operator delete
   static void delete_HZZ4L_RooSpinZeroPdf_2D(void *p) {
      delete ((::HZZ4L_RooSpinZeroPdf_2D*)p);
   }
   static void deleteArray_HZZ4L_RooSpinZeroPdf_2D(void *p) {
      delete [] ((::HZZ4L_RooSpinZeroPdf_2D*)p);
   }
   static void destruct_HZZ4L_RooSpinZeroPdf_2D(void *p) {
      typedef ::HZZ4L_RooSpinZeroPdf_2D current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::HZZ4L_RooSpinZeroPdf_2D

//______________________________________________________________________________
void HZZ4L_RooSpinZeroPdf_phase::Streamer(TBuffer &R__b)
{
   // Stream an object of class HZZ4L_RooSpinZeroPdf_phase.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(HZZ4L_RooSpinZeroPdf_phase::Class(),this);
   } else {
      R__b.WriteClassBuffer(HZZ4L_RooSpinZeroPdf_phase::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_HZZ4L_RooSpinZeroPdf_phase(void *p) {
      return  p ? new(p) ::HZZ4L_RooSpinZeroPdf_phase : new ::HZZ4L_RooSpinZeroPdf_phase;
   }
   static void *newArray_HZZ4L_RooSpinZeroPdf_phase(Long_t nElements, void *p) {
      return p ? new(p) ::HZZ4L_RooSpinZeroPdf_phase[nElements] : new ::HZZ4L_RooSpinZeroPdf_phase[nElements];
   }
   // Wrapper around operator delete
   static void delete_HZZ4L_RooSpinZeroPdf_phase(void *p) {
      delete ((::HZZ4L_RooSpinZeroPdf_phase*)p);
   }
   static void deleteArray_HZZ4L_RooSpinZeroPdf_phase(void *p) {
      delete [] ((::HZZ4L_RooSpinZeroPdf_phase*)p);
   }
   static void destruct_HZZ4L_RooSpinZeroPdf_phase(void *p) {
      typedef ::HZZ4L_RooSpinZeroPdf_phase current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::HZZ4L_RooSpinZeroPdf_phase

//______________________________________________________________________________
void VBFHZZ4L_RooSpinZeroPdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class VBFHZZ4L_RooSpinZeroPdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(VBFHZZ4L_RooSpinZeroPdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(VBFHZZ4L_RooSpinZeroPdf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_VBFHZZ4L_RooSpinZeroPdf(void *p) {
      return  p ? new(p) ::VBFHZZ4L_RooSpinZeroPdf : new ::VBFHZZ4L_RooSpinZeroPdf;
   }
   static void *newArray_VBFHZZ4L_RooSpinZeroPdf(Long_t nElements, void *p) {
      return p ? new(p) ::VBFHZZ4L_RooSpinZeroPdf[nElements] : new ::VBFHZZ4L_RooSpinZeroPdf[nElements];
   }
   // Wrapper around operator delete
   static void delete_VBFHZZ4L_RooSpinZeroPdf(void *p) {
      delete ((::VBFHZZ4L_RooSpinZeroPdf*)p);
   }
   static void deleteArray_VBFHZZ4L_RooSpinZeroPdf(void *p) {
      delete [] ((::VBFHZZ4L_RooSpinZeroPdf*)p);
   }
   static void destruct_VBFHZZ4L_RooSpinZeroPdf(void *p) {
      typedef ::VBFHZZ4L_RooSpinZeroPdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::VBFHZZ4L_RooSpinZeroPdf

//______________________________________________________________________________
void VBFHZZ4L_RooSpinZeroPdf_fast::Streamer(TBuffer &R__b)
{
   // Stream an object of class VBFHZZ4L_RooSpinZeroPdf_fast.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(VBFHZZ4L_RooSpinZeroPdf_fast::Class(),this);
   } else {
      R__b.WriteClassBuffer(VBFHZZ4L_RooSpinZeroPdf_fast::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_VBFHZZ4L_RooSpinZeroPdf_fast(void *p) {
      return  p ? new(p) ::VBFHZZ4L_RooSpinZeroPdf_fast : new ::VBFHZZ4L_RooSpinZeroPdf_fast;
   }
   static void *newArray_VBFHZZ4L_RooSpinZeroPdf_fast(Long_t nElements, void *p) {
      return p ? new(p) ::VBFHZZ4L_RooSpinZeroPdf_fast[nElements] : new ::VBFHZZ4L_RooSpinZeroPdf_fast[nElements];
   }
   // Wrapper around operator delete
   static void delete_VBFHZZ4L_RooSpinZeroPdf_fast(void *p) {
      delete ((::VBFHZZ4L_RooSpinZeroPdf_fast*)p);
   }
   static void deleteArray_VBFHZZ4L_RooSpinZeroPdf_fast(void *p) {
      delete [] ((::VBFHZZ4L_RooSpinZeroPdf_fast*)p);
   }
   static void destruct_VBFHZZ4L_RooSpinZeroPdf_fast(void *p) {
      typedef ::VBFHZZ4L_RooSpinZeroPdf_fast current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::VBFHZZ4L_RooSpinZeroPdf_fast

//______________________________________________________________________________
void HZZ4L_RooSpinZeroPdf_1D_fast::Streamer(TBuffer &R__b)
{
   // Stream an object of class HZZ4L_RooSpinZeroPdf_1D_fast.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(HZZ4L_RooSpinZeroPdf_1D_fast::Class(),this);
   } else {
      R__b.WriteClassBuffer(HZZ4L_RooSpinZeroPdf_1D_fast::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_HZZ4L_RooSpinZeroPdf_1D_fast(void *p) {
      return  p ? new(p) ::HZZ4L_RooSpinZeroPdf_1D_fast : new ::HZZ4L_RooSpinZeroPdf_1D_fast;
   }
   static void *newArray_HZZ4L_RooSpinZeroPdf_1D_fast(Long_t nElements, void *p) {
      return p ? new(p) ::HZZ4L_RooSpinZeroPdf_1D_fast[nElements] : new ::HZZ4L_RooSpinZeroPdf_1D_fast[nElements];
   }
   // Wrapper around operator delete
   static void delete_HZZ4L_RooSpinZeroPdf_1D_fast(void *p) {
      delete ((::HZZ4L_RooSpinZeroPdf_1D_fast*)p);
   }
   static void deleteArray_HZZ4L_RooSpinZeroPdf_1D_fast(void *p) {
      delete [] ((::HZZ4L_RooSpinZeroPdf_1D_fast*)p);
   }
   static void destruct_HZZ4L_RooSpinZeroPdf_1D_fast(void *p) {
      typedef ::HZZ4L_RooSpinZeroPdf_1D_fast current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::HZZ4L_RooSpinZeroPdf_1D_fast

//______________________________________________________________________________
void HZZ4L_RooSpinZeroPdf_2D_fast::Streamer(TBuffer &R__b)
{
   // Stream an object of class HZZ4L_RooSpinZeroPdf_2D_fast.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(HZZ4L_RooSpinZeroPdf_2D_fast::Class(),this);
   } else {
      R__b.WriteClassBuffer(HZZ4L_RooSpinZeroPdf_2D_fast::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_HZZ4L_RooSpinZeroPdf_2D_fast(void *p) {
      return  p ? new(p) ::HZZ4L_RooSpinZeroPdf_2D_fast : new ::HZZ4L_RooSpinZeroPdf_2D_fast;
   }
   static void *newArray_HZZ4L_RooSpinZeroPdf_2D_fast(Long_t nElements, void *p) {
      return p ? new(p) ::HZZ4L_RooSpinZeroPdf_2D_fast[nElements] : new ::HZZ4L_RooSpinZeroPdf_2D_fast[nElements];
   }
   // Wrapper around operator delete
   static void delete_HZZ4L_RooSpinZeroPdf_2D_fast(void *p) {
      delete ((::HZZ4L_RooSpinZeroPdf_2D_fast*)p);
   }
   static void deleteArray_HZZ4L_RooSpinZeroPdf_2D_fast(void *p) {
      delete [] ((::HZZ4L_RooSpinZeroPdf_2D_fast*)p);
   }
   static void destruct_HZZ4L_RooSpinZeroPdf_2D_fast(void *p) {
      typedef ::HZZ4L_RooSpinZeroPdf_2D_fast current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::HZZ4L_RooSpinZeroPdf_2D_fast

//______________________________________________________________________________
void HZZ4L_RooSpinZeroPdf_phase_fast::Streamer(TBuffer &R__b)
{
   // Stream an object of class HZZ4L_RooSpinZeroPdf_phase_fast.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(HZZ4L_RooSpinZeroPdf_phase_fast::Class(),this);
   } else {
      R__b.WriteClassBuffer(HZZ4L_RooSpinZeroPdf_phase_fast::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_HZZ4L_RooSpinZeroPdf_phase_fast(void *p) {
      return  p ? new(p) ::HZZ4L_RooSpinZeroPdf_phase_fast : new ::HZZ4L_RooSpinZeroPdf_phase_fast;
   }
   static void *newArray_HZZ4L_RooSpinZeroPdf_phase_fast(Long_t nElements, void *p) {
      return p ? new(p) ::HZZ4L_RooSpinZeroPdf_phase_fast[nElements] : new ::HZZ4L_RooSpinZeroPdf_phase_fast[nElements];
   }
   // Wrapper around operator delete
   static void delete_HZZ4L_RooSpinZeroPdf_phase_fast(void *p) {
      delete ((::HZZ4L_RooSpinZeroPdf_phase_fast*)p);
   }
   static void deleteArray_HZZ4L_RooSpinZeroPdf_phase_fast(void *p) {
      delete [] ((::HZZ4L_RooSpinZeroPdf_phase_fast*)p);
   }
   static void destruct_HZZ4L_RooSpinZeroPdf_phase_fast(void *p) {
      typedef ::HZZ4L_RooSpinZeroPdf_phase_fast current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::HZZ4L_RooSpinZeroPdf_phase_fast

//______________________________________________________________________________
void VVHZZ4L_RooSpinZeroPdf_1D_fast::Streamer(TBuffer &R__b)
{
   // Stream an object of class VVHZZ4L_RooSpinZeroPdf_1D_fast.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(VVHZZ4L_RooSpinZeroPdf_1D_fast::Class(),this);
   } else {
      R__b.WriteClassBuffer(VVHZZ4L_RooSpinZeroPdf_1D_fast::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_VVHZZ4L_RooSpinZeroPdf_1D_fast(void *p) {
      return  p ? new(p) ::VVHZZ4L_RooSpinZeroPdf_1D_fast : new ::VVHZZ4L_RooSpinZeroPdf_1D_fast;
   }
   static void *newArray_VVHZZ4L_RooSpinZeroPdf_1D_fast(Long_t nElements, void *p) {
      return p ? new(p) ::VVHZZ4L_RooSpinZeroPdf_1D_fast[nElements] : new ::VVHZZ4L_RooSpinZeroPdf_1D_fast[nElements];
   }
   // Wrapper around operator delete
   static void delete_VVHZZ4L_RooSpinZeroPdf_1D_fast(void *p) {
      delete ((::VVHZZ4L_RooSpinZeroPdf_1D_fast*)p);
   }
   static void deleteArray_VVHZZ4L_RooSpinZeroPdf_1D_fast(void *p) {
      delete [] ((::VVHZZ4L_RooSpinZeroPdf_1D_fast*)p);
   }
   static void destruct_VVHZZ4L_RooSpinZeroPdf_1D_fast(void *p) {
      typedef ::VVHZZ4L_RooSpinZeroPdf_1D_fast current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::VVHZZ4L_RooSpinZeroPdf_1D_fast

//______________________________________________________________________________
void RooChebyshevPDF::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooChebyshevPDF.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooChebyshevPDF::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooChebyshevPDF::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooChebyshevPDF(void *p) {
      return  p ? new(p) ::RooChebyshevPDF : new ::RooChebyshevPDF;
   }
   static void *newArray_RooChebyshevPDF(Long_t nElements, void *p) {
      return p ? new(p) ::RooChebyshevPDF[nElements] : new ::RooChebyshevPDF[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooChebyshevPDF(void *p) {
      delete ((::RooChebyshevPDF*)p);
   }
   static void deleteArray_RooChebyshevPDF(void *p) {
      delete [] ((::RooChebyshevPDF*)p);
   }
   static void destruct_RooChebyshevPDF(void *p) {
      typedef ::RooChebyshevPDF current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooChebyshevPDF

//______________________________________________________________________________
void RooErfPdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooErfPdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooErfPdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooErfPdf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooErfPdf(void *p) {
      return  p ? new(p) ::RooErfPdf : new ::RooErfPdf;
   }
   static void *newArray_RooErfPdf(Long_t nElements, void *p) {
      return p ? new(p) ::RooErfPdf[nElements] : new ::RooErfPdf[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooErfPdf(void *p) {
      delete ((::RooErfPdf*)p);
   }
   static void deleteArray_RooErfPdf(void *p) {
      delete [] ((::RooErfPdf*)p);
   }
   static void destruct_RooErfPdf(void *p) {
      typedef ::RooErfPdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooErfPdf

//______________________________________________________________________________
void RooPowerExpPdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooPowerExpPdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooPowerExpPdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooPowerExpPdf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooPowerExpPdf(void *p) {
      return  p ? new(p) ::RooPowerExpPdf : new ::RooPowerExpPdf;
   }
   static void *newArray_RooPowerExpPdf(Long_t nElements, void *p) {
      return p ? new(p) ::RooPowerExpPdf[nElements] : new ::RooPowerExpPdf[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooPowerExpPdf(void *p) {
      delete ((::RooPowerExpPdf*)p);
   }
   static void deleteArray_RooPowerExpPdf(void *p) {
      delete [] ((::RooPowerExpPdf*)p);
   }
   static void destruct_RooPowerExpPdf(void *p) {
      typedef ::RooPowerExpPdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooPowerExpPdf

//______________________________________________________________________________
void RooTH1DPdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooTH1DPdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooTH1DPdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooTH1DPdf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooTH1DPdf(void *p) {
      return  p ? new(p) ::RooTH1DPdf : new ::RooTH1DPdf;
   }
   static void *newArray_RooTH1DPdf(Long_t nElements, void *p) {
      return p ? new(p) ::RooTH1DPdf[nElements] : new ::RooTH1DPdf[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooTH1DPdf(void *p) {
      delete ((::RooTH1DPdf*)p);
   }
   static void deleteArray_RooTH1DPdf(void *p) {
      delete [] ((::RooTH1DPdf*)p);
   }
   static void destruct_RooTH1DPdf(void *p) {
      typedef ::RooTH1DPdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooTH1DPdf

//______________________________________________________________________________
void RooPowerFunction::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooPowerFunction.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooPowerFunction::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooPowerFunction::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooPowerFunction(void *p) {
      return  p ? new(p) ::RooPowerFunction : new ::RooPowerFunction;
   }
   static void *newArray_RooPowerFunction(Long_t nElements, void *p) {
      return p ? new(p) ::RooPowerFunction[nElements] : new ::RooPowerFunction[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooPowerFunction(void *p) {
      delete ((::RooPowerFunction*)p);
   }
   static void deleteArray_RooPowerFunction(void *p) {
      delete [] ((::RooPowerFunction*)p);
   }
   static void destruct_RooPowerFunction(void *p) {
      typedef ::RooPowerFunction current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooPowerFunction

//______________________________________________________________________________
void RooPowerLaw::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooPowerLaw.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooPowerLaw::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooPowerLaw::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooPowerLaw(void *p) {
      return  p ? new(p) ::RooPowerLaw : new ::RooPowerLaw;
   }
   static void *newArray_RooPowerLaw(Long_t nElements, void *p) {
      return p ? new(p) ::RooPowerLaw[nElements] : new ::RooPowerLaw[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooPowerLaw(void *p) {
      delete ((::RooPowerLaw*)p);
   }
   static void deleteArray_RooPowerLaw(void *p) {
      delete [] ((::RooPowerLaw*)p);
   }
   static void destruct_RooPowerLaw(void *p) {
      typedef ::RooPowerLaw current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooPowerLaw

//______________________________________________________________________________
void RooExpPoly::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooExpPoly.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooExpPoly::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooExpPoly::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooExpPoly(void *p) {
      return  p ? new(p) ::RooExpPoly : new ::RooExpPoly;
   }
   static void *newArray_RooExpPoly(Long_t nElements, void *p) {
      return p ? new(p) ::RooExpPoly[nElements] : new ::RooExpPoly[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooExpPoly(void *p) {
      delete ((::RooExpPoly*)p);
   }
   static void deleteArray_RooExpPoly(void *p) {
      delete [] ((::RooExpPoly*)p);
   }
   static void destruct_RooExpPoly(void *p) {
      typedef ::RooExpPoly current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooExpPoly

//______________________________________________________________________________
void RooMorphingPdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooMorphingPdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooMorphingPdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooMorphingPdf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooMorphingPdf(void *p) {
      return  p ? new(p) ::RooMorphingPdf : new ::RooMorphingPdf;
   }
   static void *newArray_RooMorphingPdf(Long_t nElements, void *p) {
      return p ? new(p) ::RooMorphingPdf[nElements] : new ::RooMorphingPdf[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooMorphingPdf(void *p) {
      delete ((::RooMorphingPdf*)p);
   }
   static void deleteArray_RooMorphingPdf(void *p) {
      delete [] ((::RooMorphingPdf*)p);
   }
   static void destruct_RooMorphingPdf(void *p) {
      typedef ::RooMorphingPdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooMorphingPdf

//______________________________________________________________________________
void RooParametricHist::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooParametricHist.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooParametricHist::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooParametricHist::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooParametricHist(void *p) {
      return  p ? new(p) ::RooParametricHist : new ::RooParametricHist;
   }
   static void *newArray_RooParametricHist(Long_t nElements, void *p) {
      return p ? new(p) ::RooParametricHist[nElements] : new ::RooParametricHist[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooParametricHist(void *p) {
      delete ((::RooParametricHist*)p);
   }
   static void deleteArray_RooParametricHist(void *p) {
      delete [] ((::RooParametricHist*)p);
   }
   static void destruct_RooParametricHist(void *p) {
      typedef ::RooParametricHist current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooParametricHist

//______________________________________________________________________________
void RooParametricShapeBinPdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooParametricShapeBinPdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooParametricShapeBinPdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooParametricShapeBinPdf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooParametricShapeBinPdf(void *p) {
      return  p ? new(p) ::RooParametricShapeBinPdf : new ::RooParametricShapeBinPdf;
   }
   static void *newArray_RooParametricShapeBinPdf(Long_t nElements, void *p) {
      return p ? new(p) ::RooParametricShapeBinPdf[nElements] : new ::RooParametricShapeBinPdf[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooParametricShapeBinPdf(void *p) {
      delete ((::RooParametricShapeBinPdf*)p);
   }
   static void deleteArray_RooParametricShapeBinPdf(void *p) {
      delete [] ((::RooParametricShapeBinPdf*)p);
   }
   static void destruct_RooParametricShapeBinPdf(void *p) {
      typedef ::RooParametricShapeBinPdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooParametricShapeBinPdf

//______________________________________________________________________________
void GaussExp::Streamer(TBuffer &R__b)
{
   // Stream an object of class GaussExp.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(GaussExp::Class(),this);
   } else {
      R__b.WriteClassBuffer(GaussExp::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_GaussExp(void *p) {
      return  p ? new(p) ::GaussExp : new ::GaussExp;
   }
   static void *newArray_GaussExp(Long_t nElements, void *p) {
      return p ? new(p) ::GaussExp[nElements] : new ::GaussExp[nElements];
   }
   // Wrapper around operator delete
   static void delete_GaussExp(void *p) {
      delete ((::GaussExp*)p);
   }
   static void deleteArray_GaussExp(void *p) {
      delete [] ((::GaussExp*)p);
   }
   static void destruct_GaussExp(void *p) {
      typedef ::GaussExp current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::GaussExp

//______________________________________________________________________________
void RooDoubleCBFast::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooDoubleCBFast.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooDoubleCBFast::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooDoubleCBFast::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooDoubleCBFast(void *p) {
      return  p ? new(p) ::RooDoubleCBFast : new ::RooDoubleCBFast;
   }
   static void *newArray_RooDoubleCBFast(Long_t nElements, void *p) {
      return p ? new(p) ::RooDoubleCBFast[nElements] : new ::RooDoubleCBFast[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooDoubleCBFast(void *p) {
      delete ((::RooDoubleCBFast*)p);
   }
   static void deleteArray_RooDoubleCBFast(void *p) {
      delete [] ((::RooDoubleCBFast*)p);
   }
   static void destruct_RooDoubleCBFast(void *p) {
      typedef ::RooDoubleCBFast current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooDoubleCBFast

//______________________________________________________________________________
void CMSHistFunc::Streamer(TBuffer &R__b)
{
   // Stream an object of class CMSHistFunc.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(CMSHistFunc::Class(),this);
   } else {
      R__b.WriteClassBuffer(CMSHistFunc::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_CMSHistFunc(void *p) {
      return  p ? new(p) ::CMSHistFunc : new ::CMSHistFunc;
   }
   static void *newArray_CMSHistFunc(Long_t nElements, void *p) {
      return p ? new(p) ::CMSHistFunc[nElements] : new ::CMSHistFunc[nElements];
   }
   // Wrapper around operator delete
   static void delete_CMSHistFunc(void *p) {
      delete ((::CMSHistFunc*)p);
   }
   static void deleteArray_CMSHistFunc(void *p) {
      delete [] ((::CMSHistFunc*)p);
   }
   static void destruct_CMSHistFunc(void *p) {
      typedef ::CMSHistFunc current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::CMSHistFunc

//______________________________________________________________________________
void CMSHistErrorPropagator::Streamer(TBuffer &R__b)
{
   // Stream an object of class CMSHistErrorPropagator.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(CMSHistErrorPropagator::Class(),this);
   } else {
      R__b.WriteClassBuffer(CMSHistErrorPropagator::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_CMSHistErrorPropagator(void *p) {
      return  p ? new(p) ::CMSHistErrorPropagator : new ::CMSHistErrorPropagator;
   }
   static void *newArray_CMSHistErrorPropagator(Long_t nElements, void *p) {
      return p ? new(p) ::CMSHistErrorPropagator[nElements] : new ::CMSHistErrorPropagator[nElements];
   }
   // Wrapper around operator delete
   static void delete_CMSHistErrorPropagator(void *p) {
      delete ((::CMSHistErrorPropagator*)p);
   }
   static void deleteArray_CMSHistErrorPropagator(void *p) {
      delete [] ((::CMSHistErrorPropagator*)p);
   }
   static void destruct_CMSHistErrorPropagator(void *p) {
      typedef ::CMSHistErrorPropagator current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::CMSHistErrorPropagator

//______________________________________________________________________________
void CMSHistFuncWrapper::Streamer(TBuffer &R__b)
{
   // Stream an object of class CMSHistFuncWrapper.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(CMSHistFuncWrapper::Class(),this);
   } else {
      R__b.WriteClassBuffer(CMSHistFuncWrapper::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_CMSHistFuncWrapper(void *p) {
      return  p ? new(p) ::CMSHistFuncWrapper : new ::CMSHistFuncWrapper;
   }
   static void *newArray_CMSHistFuncWrapper(Long_t nElements, void *p) {
      return p ? new(p) ::CMSHistFuncWrapper[nElements] : new ::CMSHistFuncWrapper[nElements];
   }
   // Wrapper around operator delete
   static void delete_CMSHistFuncWrapper(void *p) {
      delete ((::CMSHistFuncWrapper*)p);
   }
   static void deleteArray_CMSHistFuncWrapper(void *p) {
      delete [] ((::CMSHistFuncWrapper*)p);
   }
   static void destruct_CMSHistFuncWrapper(void *p) {
      typedef ::CMSHistFuncWrapper current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::CMSHistFuncWrapper

//______________________________________________________________________________
void RooTaylorExpansion::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooTaylorExpansion.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooTaylorExpansion::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooTaylorExpansion::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooTaylorExpansion(void *p) {
      return  p ? new(p) ::RooTaylorExpansion : new ::RooTaylorExpansion;
   }
   static void *newArray_RooTaylorExpansion(Long_t nElements, void *p) {
      return p ? new(p) ::RooTaylorExpansion[nElements] : new ::RooTaylorExpansion[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooTaylorExpansion(void *p) {
      delete ((::RooTaylorExpansion*)p);
   }
   static void deleteArray_RooTaylorExpansion(void *p) {
      delete [] ((::RooTaylorExpansion*)p);
   }
   static void destruct_RooTaylorExpansion(void *p) {
      typedef ::RooTaylorExpansion current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooTaylorExpansion

//______________________________________________________________________________
void SimpleTaylorExpansion1D::Streamer(TBuffer &R__b)
{
   // Stream an object of class SimpleTaylorExpansion1D.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(SimpleTaylorExpansion1D::Class(),this);
   } else {
      R__b.WriteClassBuffer(SimpleTaylorExpansion1D::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_SimpleTaylorExpansion1D(void *p) {
      return  p ? new(p) ::SimpleTaylorExpansion1D : new ::SimpleTaylorExpansion1D;
   }
   static void *newArray_SimpleTaylorExpansion1D(Long_t nElements, void *p) {
      return p ? new(p) ::SimpleTaylorExpansion1D[nElements] : new ::SimpleTaylorExpansion1D[nElements];
   }
   // Wrapper around operator delete
   static void delete_SimpleTaylorExpansion1D(void *p) {
      delete ((::SimpleTaylorExpansion1D*)p);
   }
   static void deleteArray_SimpleTaylorExpansion1D(void *p) {
      delete [] ((::SimpleTaylorExpansion1D*)p);
   }
   static void destruct_SimpleTaylorExpansion1D(void *p) {
      typedef ::SimpleTaylorExpansion1D current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::SimpleTaylorExpansion1D

//______________________________________________________________________________
void RooPiecewisePolynomial::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooPiecewisePolynomial.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooPiecewisePolynomial::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooPiecewisePolynomial::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooPiecewisePolynomial(void *p) {
      return  p ? new(p) ::RooPiecewisePolynomial : new ::RooPiecewisePolynomial;
   }
   static void *newArray_RooPiecewisePolynomial(Long_t nElements, void *p) {
      return p ? new(p) ::RooPiecewisePolynomial[nElements] : new ::RooPiecewisePolynomial[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooPiecewisePolynomial(void *p) {
      delete ((::RooPiecewisePolynomial*)p);
   }
   static void deleteArray_RooPiecewisePolynomial(void *p) {
      delete [] ((::RooPiecewisePolynomial*)p);
   }
   static void destruct_RooPiecewisePolynomial(void *p) {
      typedef ::RooPiecewisePolynomial current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooPiecewisePolynomial

//______________________________________________________________________________
void RooNCSplineCore::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooNCSplineCore.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooNCSplineCore::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooNCSplineCore::Class(),this);
   }
}

namespace ROOT {
   // Wrapper around operator delete
   static void delete_RooNCSplineCore(void *p) {
      delete ((::RooNCSplineCore*)p);
   }
   static void deleteArray_RooNCSplineCore(void *p) {
      delete [] ((::RooNCSplineCore*)p);
   }
   static void destruct_RooNCSplineCore(void *p) {
      typedef ::RooNCSplineCore current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooNCSplineCore

//______________________________________________________________________________
void RooNCSpline_1D_fast::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooNCSpline_1D_fast.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooNCSpline_1D_fast::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooNCSpline_1D_fast::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooNCSpline_1D_fast(void *p) {
      return  p ? new(p) ::RooNCSpline_1D_fast : new ::RooNCSpline_1D_fast;
   }
   static void *newArray_RooNCSpline_1D_fast(Long_t nElements, void *p) {
      return p ? new(p) ::RooNCSpline_1D_fast[nElements] : new ::RooNCSpline_1D_fast[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooNCSpline_1D_fast(void *p) {
      delete ((::RooNCSpline_1D_fast*)p);
   }
   static void deleteArray_RooNCSpline_1D_fast(void *p) {
      delete [] ((::RooNCSpline_1D_fast*)p);
   }
   static void destruct_RooNCSpline_1D_fast(void *p) {
      typedef ::RooNCSpline_1D_fast current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooNCSpline_1D_fast

//______________________________________________________________________________
void RooNCSpline_2D_fast::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooNCSpline_2D_fast.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooNCSpline_2D_fast::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooNCSpline_2D_fast::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooNCSpline_2D_fast(void *p) {
      return  p ? new(p) ::RooNCSpline_2D_fast : new ::RooNCSpline_2D_fast;
   }
   static void *newArray_RooNCSpline_2D_fast(Long_t nElements, void *p) {
      return p ? new(p) ::RooNCSpline_2D_fast[nElements] : new ::RooNCSpline_2D_fast[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooNCSpline_2D_fast(void *p) {
      delete ((::RooNCSpline_2D_fast*)p);
   }
   static void deleteArray_RooNCSpline_2D_fast(void *p) {
      delete [] ((::RooNCSpline_2D_fast*)p);
   }
   static void destruct_RooNCSpline_2D_fast(void *p) {
      typedef ::RooNCSpline_2D_fast current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooNCSpline_2D_fast

//______________________________________________________________________________
void RooNCSpline_3D_fast::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooNCSpline_3D_fast.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooNCSpline_3D_fast::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooNCSpline_3D_fast::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooNCSpline_3D_fast(void *p) {
      return  p ? new(p) ::RooNCSpline_3D_fast : new ::RooNCSpline_3D_fast;
   }
   static void *newArray_RooNCSpline_3D_fast(Long_t nElements, void *p) {
      return p ? new(p) ::RooNCSpline_3D_fast[nElements] : new ::RooNCSpline_3D_fast[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooNCSpline_3D_fast(void *p) {
      delete ((::RooNCSpline_3D_fast*)p);
   }
   static void deleteArray_RooNCSpline_3D_fast(void *p) {
      delete [] ((::RooNCSpline_3D_fast*)p);
   }
   static void destruct_RooNCSpline_3D_fast(void *p) {
      typedef ::RooNCSpline_3D_fast current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooNCSpline_3D_fast

//______________________________________________________________________________
void RooFuncPdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooFuncPdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooFuncPdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooFuncPdf::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooFuncPdf(void *p) {
      return  p ? new(p) ::RooFuncPdf : new ::RooFuncPdf;
   }
   static void *newArray_RooFuncPdf(Long_t nElements, void *p) {
      return p ? new(p) ::RooFuncPdf[nElements] : new ::RooFuncPdf[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooFuncPdf(void *p) {
      delete ((::RooFuncPdf*)p);
   }
   static void deleteArray_RooFuncPdf(void *p) {
      delete [] ((::RooFuncPdf*)p);
   }
   static void destruct_RooFuncPdf(void *p) {
      typedef ::RooFuncPdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooFuncPdf

namespace ROOT {
   static TClass *vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR_Dictionary();
   static void vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR_TClassManip(TClass*);
   static void *new_vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR(void *p = 0);
   static void *newArray_vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR(Long_t size, void *p);
   static void delete_vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR(void *p);
   static void deleteArray_vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR(void *p);
   static void destruct_vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<vector<vector<vector<vector<vector<float> > > > > >*)
   {
      vector<vector<vector<vector<vector<vector<float> > > > > > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<vector<vector<vector<vector<vector<float> > > > > >));
      static ::ROOT::TGenericClassInfo 
         instance("vector<vector<vector<vector<vector<vector<float> > > > > >", -2, "vector", 216,
                  typeid(vector<vector<vector<vector<vector<vector<float> > > > > >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(vector<vector<vector<vector<vector<vector<float> > > > > >) );
      instance.SetNew(&new_vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR);
      instance.SetNewArray(&newArray_vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR);
      instance.SetDelete(&delete_vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR);
      instance.SetDeleteArray(&deleteArray_vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR);
      instance.SetDestructor(&destruct_vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<vector<vector<vector<vector<vector<float> > > > > > >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const vector<vector<vector<vector<vector<vector<float> > > > > >*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<vector<vector<vector<vector<vector<float> > > > > >*)0x0)->GetClass();
      vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<vector<vector<vector<vector<vector<float> > > > > > : new vector<vector<vector<vector<vector<vector<float> > > > > >;
   }
   static void *newArray_vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<vector<vector<vector<vector<vector<float> > > > > >[nElements] : new vector<vector<vector<vector<vector<vector<float> > > > > >[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR(void *p) {
      delete ((vector<vector<vector<vector<vector<vector<float> > > > > >*)p);
   }
   static void deleteArray_vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR(void *p) {
      delete [] ((vector<vector<vector<vector<vector<vector<float> > > > > >*)p);
   }
   static void destruct_vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgRsPgR(void *p) {
      typedef vector<vector<vector<vector<vector<vector<float> > > > > > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<vector<vector<vector<vector<vector<float> > > > > >

namespace ROOT {
   static TClass *vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR_Dictionary();
   static void vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR_TClassManip(TClass*);
   static void *new_vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR(void *p = 0);
   static void *newArray_vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR(Long_t size, void *p);
   static void delete_vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR(void *p);
   static void deleteArray_vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR(void *p);
   static void destruct_vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<vector<vector<vector<vector<vector<double> > > > > >*)
   {
      vector<vector<vector<vector<vector<vector<double> > > > > > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<vector<vector<vector<vector<vector<double> > > > > >));
      static ::ROOT::TGenericClassInfo 
         instance("vector<vector<vector<vector<vector<vector<double> > > > > >", -2, "vector", 216,
                  typeid(vector<vector<vector<vector<vector<vector<double> > > > > >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(vector<vector<vector<vector<vector<vector<double> > > > > >) );
      instance.SetNew(&new_vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR);
      instance.SetNewArray(&newArray_vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR);
      instance.SetDelete(&delete_vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR);
      instance.SetDeleteArray(&deleteArray_vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR);
      instance.SetDestructor(&destruct_vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<vector<vector<vector<vector<vector<double> > > > > > >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const vector<vector<vector<vector<vector<vector<double> > > > > >*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<vector<vector<vector<vector<vector<double> > > > > >*)0x0)->GetClass();
      vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<vector<vector<vector<vector<vector<double> > > > > > : new vector<vector<vector<vector<vector<vector<double> > > > > >;
   }
   static void *newArray_vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<vector<vector<vector<vector<vector<double> > > > > >[nElements] : new vector<vector<vector<vector<vector<vector<double> > > > > >[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR(void *p) {
      delete ((vector<vector<vector<vector<vector<vector<double> > > > > >*)p);
   }
   static void deleteArray_vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR(void *p) {
      delete [] ((vector<vector<vector<vector<vector<vector<double> > > > > >*)p);
   }
   static void destruct_vectorlEvectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgRsPgR(void *p) {
      typedef vector<vector<vector<vector<vector<vector<double> > > > > > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<vector<vector<vector<vector<vector<double> > > > > >

namespace ROOT {
   static TClass *vectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR_Dictionary();
   static void vectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR_TClassManip(TClass*);
   static void *new_vectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR(void *p = 0);
   static void *newArray_vectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR(Long_t size, void *p);
   static void delete_vectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR(void *p);
   static void deleteArray_vectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR(void *p);
   static void destruct_vectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<vector<vector<vector<vector<float> > > > >*)
   {
      vector<vector<vector<vector<vector<float> > > > > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<vector<vector<vector<vector<float> > > > >));
      static ::ROOT::TGenericClassInfo 
         instance("vector<vector<vector<vector<vector<float> > > > >", -2, "vector", 216,
                  typeid(vector<vector<vector<vector<vector<float> > > > >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(vector<vector<vector<vector<vector<float> > > > >) );
      instance.SetNew(&new_vectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR);
      instance.SetNewArray(&newArray_vectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR);
      instance.SetDelete(&delete_vectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR);
      instance.SetDeleteArray(&deleteArray_vectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR);
      instance.SetDestructor(&destruct_vectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<vector<vector<vector<vector<float> > > > > >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const vector<vector<vector<vector<vector<float> > > > >*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<vector<vector<vector<vector<float> > > > >*)0x0)->GetClass();
      vectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<vector<vector<vector<vector<float> > > > > : new vector<vector<vector<vector<vector<float> > > > >;
   }
   static void *newArray_vectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<vector<vector<vector<vector<float> > > > >[nElements] : new vector<vector<vector<vector<vector<float> > > > >[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR(void *p) {
      delete ((vector<vector<vector<vector<vector<float> > > > >*)p);
   }
   static void deleteArray_vectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR(void *p) {
      delete [] ((vector<vector<vector<vector<vector<float> > > > >*)p);
   }
   static void destruct_vectorlEvectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgRsPgR(void *p) {
      typedef vector<vector<vector<vector<vector<float> > > > > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<vector<vector<vector<vector<float> > > > >

namespace ROOT {
   static TClass *vectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR_Dictionary();
   static void vectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR_TClassManip(TClass*);
   static void *new_vectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR(void *p = 0);
   static void *newArray_vectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR(Long_t size, void *p);
   static void delete_vectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR(void *p);
   static void deleteArray_vectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR(void *p);
   static void destruct_vectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<vector<vector<vector<vector<double> > > > >*)
   {
      vector<vector<vector<vector<vector<double> > > > > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<vector<vector<vector<vector<double> > > > >));
      static ::ROOT::TGenericClassInfo 
         instance("vector<vector<vector<vector<vector<double> > > > >", -2, "vector", 216,
                  typeid(vector<vector<vector<vector<vector<double> > > > >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(vector<vector<vector<vector<vector<double> > > > >) );
      instance.SetNew(&new_vectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR);
      instance.SetNewArray(&newArray_vectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR);
      instance.SetDelete(&delete_vectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR);
      instance.SetDeleteArray(&deleteArray_vectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR);
      instance.SetDestructor(&destruct_vectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<vector<vector<vector<vector<double> > > > > >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const vector<vector<vector<vector<vector<double> > > > >*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<vector<vector<vector<vector<double> > > > >*)0x0)->GetClass();
      vectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<vector<vector<vector<vector<double> > > > > : new vector<vector<vector<vector<vector<double> > > > >;
   }
   static void *newArray_vectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<vector<vector<vector<vector<double> > > > >[nElements] : new vector<vector<vector<vector<vector<double> > > > >[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR(void *p) {
      delete ((vector<vector<vector<vector<vector<double> > > > >*)p);
   }
   static void deleteArray_vectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR(void *p) {
      delete [] ((vector<vector<vector<vector<vector<double> > > > >*)p);
   }
   static void destruct_vectorlEvectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgRsPgR(void *p) {
      typedef vector<vector<vector<vector<vector<double> > > > > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<vector<vector<vector<vector<double> > > > >

namespace ROOT {
   static TClass *vectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR_Dictionary();
   static void vectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR_TClassManip(TClass*);
   static void *new_vectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR(void *p = 0);
   static void *newArray_vectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR(Long_t size, void *p);
   static void delete_vectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR(void *p);
   static void deleteArray_vectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR(void *p);
   static void destruct_vectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<vector<vector<vector<float> > > >*)
   {
      vector<vector<vector<vector<float> > > > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<vector<vector<vector<float> > > >));
      static ::ROOT::TGenericClassInfo 
         instance("vector<vector<vector<vector<float> > > >", -2, "vector", 216,
                  typeid(vector<vector<vector<vector<float> > > >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(vector<vector<vector<vector<float> > > >) );
      instance.SetNew(&new_vectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR);
      instance.SetNewArray(&newArray_vectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR);
      instance.SetDelete(&delete_vectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR);
      instance.SetDeleteArray(&deleteArray_vectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR);
      instance.SetDestructor(&destruct_vectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<vector<vector<vector<float> > > > >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const vector<vector<vector<vector<float> > > >*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<vector<vector<vector<float> > > >*)0x0)->GetClass();
      vectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<vector<vector<vector<float> > > > : new vector<vector<vector<vector<float> > > >;
   }
   static void *newArray_vectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<vector<vector<vector<float> > > >[nElements] : new vector<vector<vector<vector<float> > > >[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR(void *p) {
      delete ((vector<vector<vector<vector<float> > > >*)p);
   }
   static void deleteArray_vectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR(void *p) {
      delete [] ((vector<vector<vector<vector<float> > > >*)p);
   }
   static void destruct_vectorlEvectorlEvectorlEvectorlEfloatgRsPgRsPgRsPgR(void *p) {
      typedef vector<vector<vector<vector<float> > > > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<vector<vector<vector<float> > > >

namespace ROOT {
   static TClass *vectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR_Dictionary();
   static void vectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR_TClassManip(TClass*);
   static void *new_vectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR(void *p = 0);
   static void *newArray_vectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR(Long_t size, void *p);
   static void delete_vectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR(void *p);
   static void deleteArray_vectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR(void *p);
   static void destruct_vectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<vector<vector<vector<double> > > >*)
   {
      vector<vector<vector<vector<double> > > > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<vector<vector<vector<double> > > >));
      static ::ROOT::TGenericClassInfo 
         instance("vector<vector<vector<vector<double> > > >", -2, "vector", 216,
                  typeid(vector<vector<vector<vector<double> > > >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(vector<vector<vector<vector<double> > > >) );
      instance.SetNew(&new_vectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR);
      instance.SetNewArray(&newArray_vectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR);
      instance.SetDelete(&delete_vectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR);
      instance.SetDeleteArray(&deleteArray_vectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR);
      instance.SetDestructor(&destruct_vectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<vector<vector<vector<double> > > > >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const vector<vector<vector<vector<double> > > >*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<vector<vector<vector<double> > > >*)0x0)->GetClass();
      vectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<vector<vector<vector<double> > > > : new vector<vector<vector<vector<double> > > >;
   }
   static void *newArray_vectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<vector<vector<vector<double> > > >[nElements] : new vector<vector<vector<vector<double> > > >[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR(void *p) {
      delete ((vector<vector<vector<vector<double> > > >*)p);
   }
   static void deleteArray_vectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR(void *p) {
      delete [] ((vector<vector<vector<vector<double> > > >*)p);
   }
   static void destruct_vectorlEvectorlEvectorlEvectorlEdoublegRsPgRsPgRsPgR(void *p) {
      typedef vector<vector<vector<vector<double> > > > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<vector<vector<vector<double> > > >

namespace ROOT {
   static TClass *vectorlEvectorlEvectorlEfloatgRsPgRsPgR_Dictionary();
   static void vectorlEvectorlEvectorlEfloatgRsPgRsPgR_TClassManip(TClass*);
   static void *new_vectorlEvectorlEvectorlEfloatgRsPgRsPgR(void *p = 0);
   static void *newArray_vectorlEvectorlEvectorlEfloatgRsPgRsPgR(Long_t size, void *p);
   static void delete_vectorlEvectorlEvectorlEfloatgRsPgRsPgR(void *p);
   static void deleteArray_vectorlEvectorlEvectorlEfloatgRsPgRsPgR(void *p);
   static void destruct_vectorlEvectorlEvectorlEfloatgRsPgRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<vector<vector<float> > >*)
   {
      vector<vector<vector<float> > > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<vector<vector<float> > >));
      static ::ROOT::TGenericClassInfo 
         instance("vector<vector<vector<float> > >", -2, "vector", 216,
                  typeid(vector<vector<vector<float> > >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlEvectorlEvectorlEfloatgRsPgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(vector<vector<vector<float> > >) );
      instance.SetNew(&new_vectorlEvectorlEvectorlEfloatgRsPgRsPgR);
      instance.SetNewArray(&newArray_vectorlEvectorlEvectorlEfloatgRsPgRsPgR);
      instance.SetDelete(&delete_vectorlEvectorlEvectorlEfloatgRsPgRsPgR);
      instance.SetDeleteArray(&deleteArray_vectorlEvectorlEvectorlEfloatgRsPgRsPgR);
      instance.SetDestructor(&destruct_vectorlEvectorlEvectorlEfloatgRsPgRsPgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<vector<vector<float> > > >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const vector<vector<vector<float> > >*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlEvectorlEvectorlEfloatgRsPgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<vector<vector<float> > >*)0x0)->GetClass();
      vectorlEvectorlEvectorlEfloatgRsPgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlEvectorlEvectorlEfloatgRsPgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlEvectorlEvectorlEfloatgRsPgRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<vector<vector<float> > > : new vector<vector<vector<float> > >;
   }
   static void *newArray_vectorlEvectorlEvectorlEfloatgRsPgRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<vector<vector<float> > >[nElements] : new vector<vector<vector<float> > >[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlEvectorlEvectorlEfloatgRsPgRsPgR(void *p) {
      delete ((vector<vector<vector<float> > >*)p);
   }
   static void deleteArray_vectorlEvectorlEvectorlEfloatgRsPgRsPgR(void *p) {
      delete [] ((vector<vector<vector<float> > >*)p);
   }
   static void destruct_vectorlEvectorlEvectorlEfloatgRsPgRsPgR(void *p) {
      typedef vector<vector<vector<float> > > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<vector<vector<float> > >

namespace ROOT {
   static TClass *vectorlEvectorlEvectorlEdoublegRsPgRsPgR_Dictionary();
   static void vectorlEvectorlEvectorlEdoublegRsPgRsPgR_TClassManip(TClass*);
   static void *new_vectorlEvectorlEvectorlEdoublegRsPgRsPgR(void *p = 0);
   static void *newArray_vectorlEvectorlEvectorlEdoublegRsPgRsPgR(Long_t size, void *p);
   static void delete_vectorlEvectorlEvectorlEdoublegRsPgRsPgR(void *p);
   static void deleteArray_vectorlEvectorlEvectorlEdoublegRsPgRsPgR(void *p);
   static void destruct_vectorlEvectorlEvectorlEdoublegRsPgRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<vector<vector<double> > >*)
   {
      vector<vector<vector<double> > > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<vector<vector<double> > >));
      static ::ROOT::TGenericClassInfo 
         instance("vector<vector<vector<double> > >", -2, "vector", 216,
                  typeid(vector<vector<vector<double> > >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlEvectorlEvectorlEdoublegRsPgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(vector<vector<vector<double> > >) );
      instance.SetNew(&new_vectorlEvectorlEvectorlEdoublegRsPgRsPgR);
      instance.SetNewArray(&newArray_vectorlEvectorlEvectorlEdoublegRsPgRsPgR);
      instance.SetDelete(&delete_vectorlEvectorlEvectorlEdoublegRsPgRsPgR);
      instance.SetDeleteArray(&deleteArray_vectorlEvectorlEvectorlEdoublegRsPgRsPgR);
      instance.SetDestructor(&destruct_vectorlEvectorlEvectorlEdoublegRsPgRsPgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<vector<vector<double> > > >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const vector<vector<vector<double> > >*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlEvectorlEvectorlEdoublegRsPgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<vector<vector<double> > >*)0x0)->GetClass();
      vectorlEvectorlEvectorlEdoublegRsPgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlEvectorlEvectorlEdoublegRsPgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlEvectorlEvectorlEdoublegRsPgRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<vector<vector<double> > > : new vector<vector<vector<double> > >;
   }
   static void *newArray_vectorlEvectorlEvectorlEdoublegRsPgRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<vector<vector<double> > >[nElements] : new vector<vector<vector<double> > >[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlEvectorlEvectorlEdoublegRsPgRsPgR(void *p) {
      delete ((vector<vector<vector<double> > >*)p);
   }
   static void deleteArray_vectorlEvectorlEvectorlEdoublegRsPgRsPgR(void *p) {
      delete [] ((vector<vector<vector<double> > >*)p);
   }
   static void destruct_vectorlEvectorlEvectorlEdoublegRsPgRsPgR(void *p) {
      typedef vector<vector<vector<double> > > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<vector<vector<double> > >

namespace ROOT {
   static TClass *vectorlEvectorlEfloatgRsPgR_Dictionary();
   static void vectorlEvectorlEfloatgRsPgR_TClassManip(TClass*);
   static void *new_vectorlEvectorlEfloatgRsPgR(void *p = 0);
   static void *newArray_vectorlEvectorlEfloatgRsPgR(Long_t size, void *p);
   static void delete_vectorlEvectorlEfloatgRsPgR(void *p);
   static void deleteArray_vectorlEvectorlEfloatgRsPgR(void *p);
   static void destruct_vectorlEvectorlEfloatgRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<vector<float> >*)
   {
      vector<vector<float> > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<vector<float> >));
      static ::ROOT::TGenericClassInfo 
         instance("vector<vector<float> >", -2, "vector", 216,
                  typeid(vector<vector<float> >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlEvectorlEfloatgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(vector<vector<float> >) );
      instance.SetNew(&new_vectorlEvectorlEfloatgRsPgR);
      instance.SetNewArray(&newArray_vectorlEvectorlEfloatgRsPgR);
      instance.SetDelete(&delete_vectorlEvectorlEfloatgRsPgR);
      instance.SetDeleteArray(&deleteArray_vectorlEvectorlEfloatgRsPgR);
      instance.SetDestructor(&destruct_vectorlEvectorlEfloatgRsPgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<vector<float> > >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const vector<vector<float> >*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlEvectorlEfloatgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<vector<float> >*)0x0)->GetClass();
      vectorlEvectorlEfloatgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlEvectorlEfloatgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlEvectorlEfloatgRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<vector<float> > : new vector<vector<float> >;
   }
   static void *newArray_vectorlEvectorlEfloatgRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<vector<float> >[nElements] : new vector<vector<float> >[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlEvectorlEfloatgRsPgR(void *p) {
      delete ((vector<vector<float> >*)p);
   }
   static void deleteArray_vectorlEvectorlEfloatgRsPgR(void *p) {
      delete [] ((vector<vector<float> >*)p);
   }
   static void destruct_vectorlEvectorlEfloatgRsPgR(void *p) {
      typedef vector<vector<float> > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<vector<float> >

namespace ROOT {
   static TClass *vectorlEvectorlEdoublegRsPgR_Dictionary();
   static void vectorlEvectorlEdoublegRsPgR_TClassManip(TClass*);
   static void *new_vectorlEvectorlEdoublegRsPgR(void *p = 0);
   static void *newArray_vectorlEvectorlEdoublegRsPgR(Long_t size, void *p);
   static void delete_vectorlEvectorlEdoublegRsPgR(void *p);
   static void deleteArray_vectorlEvectorlEdoublegRsPgR(void *p);
   static void destruct_vectorlEvectorlEdoublegRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<vector<double> >*)
   {
      vector<vector<double> > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<vector<double> >));
      static ::ROOT::TGenericClassInfo 
         instance("vector<vector<double> >", -2, "vector", 216,
                  typeid(vector<vector<double> >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlEvectorlEdoublegRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(vector<vector<double> >) );
      instance.SetNew(&new_vectorlEvectorlEdoublegRsPgR);
      instance.SetNewArray(&newArray_vectorlEvectorlEdoublegRsPgR);
      instance.SetDelete(&delete_vectorlEvectorlEdoublegRsPgR);
      instance.SetDeleteArray(&deleteArray_vectorlEvectorlEdoublegRsPgR);
      instance.SetDestructor(&destruct_vectorlEvectorlEdoublegRsPgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<vector<double> > >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const vector<vector<double> >*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlEvectorlEdoublegRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<vector<double> >*)0x0)->GetClass();
      vectorlEvectorlEdoublegRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlEvectorlEdoublegRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlEvectorlEdoublegRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<vector<double> > : new vector<vector<double> >;
   }
   static void *newArray_vectorlEvectorlEdoublegRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<vector<double> >[nElements] : new vector<vector<double> >[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlEvectorlEdoublegRsPgR(void *p) {
      delete ((vector<vector<double> >*)p);
   }
   static void deleteArray_vectorlEvectorlEdoublegRsPgR(void *p) {
      delete [] ((vector<vector<double> >*)p);
   }
   static void destruct_vectorlEvectorlEdoublegRsPgR(void *p) {
      typedef vector<vector<double> > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<vector<double> >

namespace ROOT {
   static TClass *vectorlEintgR_Dictionary();
   static void vectorlEintgR_TClassManip(TClass*);
   static void *new_vectorlEintgR(void *p = 0);
   static void *newArray_vectorlEintgR(Long_t size, void *p);
   static void delete_vectorlEintgR(void *p);
   static void deleteArray_vectorlEintgR(void *p);
   static void destruct_vectorlEintgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<int>*)
   {
      vector<int> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<int>));
      static ::ROOT::TGenericClassInfo 
         instance("vector<int>", -2, "vector", 216,
                  typeid(vector<int>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlEintgR_Dictionary, isa_proxy, 4,
                  sizeof(vector<int>) );
      instance.SetNew(&new_vectorlEintgR);
      instance.SetNewArray(&newArray_vectorlEintgR);
      instance.SetDelete(&delete_vectorlEintgR);
      instance.SetDeleteArray(&deleteArray_vectorlEintgR);
      instance.SetDestructor(&destruct_vectorlEintgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<int> >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const vector<int>*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlEintgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<int>*)0x0)->GetClass();
      vectorlEintgR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlEintgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlEintgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<int> : new vector<int>;
   }
   static void *newArray_vectorlEintgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<int>[nElements] : new vector<int>[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlEintgR(void *p) {
      delete ((vector<int>*)p);
   }
   static void deleteArray_vectorlEintgR(void *p) {
      delete [] ((vector<int>*)p);
   }
   static void destruct_vectorlEintgR(void *p) {
      typedef vector<int> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<int>

namespace ROOT {
   static TClass *vectorlEfloatgR_Dictionary();
   static void vectorlEfloatgR_TClassManip(TClass*);
   static void *new_vectorlEfloatgR(void *p = 0);
   static void *newArray_vectorlEfloatgR(Long_t size, void *p);
   static void delete_vectorlEfloatgR(void *p);
   static void deleteArray_vectorlEfloatgR(void *p);
   static void destruct_vectorlEfloatgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<float>*)
   {
      vector<float> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<float>));
      static ::ROOT::TGenericClassInfo 
         instance("vector<float>", -2, "vector", 216,
                  typeid(vector<float>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlEfloatgR_Dictionary, isa_proxy, 4,
                  sizeof(vector<float>) );
      instance.SetNew(&new_vectorlEfloatgR);
      instance.SetNewArray(&newArray_vectorlEfloatgR);
      instance.SetDelete(&delete_vectorlEfloatgR);
      instance.SetDeleteArray(&deleteArray_vectorlEfloatgR);
      instance.SetDestructor(&destruct_vectorlEfloatgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<float> >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const vector<float>*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlEfloatgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<float>*)0x0)->GetClass();
      vectorlEfloatgR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlEfloatgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlEfloatgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<float> : new vector<float>;
   }
   static void *newArray_vectorlEfloatgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<float>[nElements] : new vector<float>[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlEfloatgR(void *p) {
      delete ((vector<float>*)p);
   }
   static void deleteArray_vectorlEfloatgR(void *p) {
      delete [] ((vector<float>*)p);
   }
   static void destruct_vectorlEfloatgR(void *p) {
      typedef vector<float> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<float>

namespace ROOT {
   static TClass *vectorlEdoublegR_Dictionary();
   static void vectorlEdoublegR_TClassManip(TClass*);
   static void *new_vectorlEdoublegR(void *p = 0);
   static void *newArray_vectorlEdoublegR(Long_t size, void *p);
   static void delete_vectorlEdoublegR(void *p);
   static void deleteArray_vectorlEdoublegR(void *p);
   static void destruct_vectorlEdoublegR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<double>*)
   {
      vector<double> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<double>));
      static ::ROOT::TGenericClassInfo 
         instance("vector<double>", -2, "vector", 216,
                  typeid(vector<double>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlEdoublegR_Dictionary, isa_proxy, 4,
                  sizeof(vector<double>) );
      instance.SetNew(&new_vectorlEdoublegR);
      instance.SetNewArray(&newArray_vectorlEdoublegR);
      instance.SetDelete(&delete_vectorlEdoublegR);
      instance.SetDeleteArray(&deleteArray_vectorlEdoublegR);
      instance.SetDestructor(&destruct_vectorlEdoublegR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<double> >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const vector<double>*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlEdoublegR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<double>*)0x0)->GetClass();
      vectorlEdoublegR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlEdoublegR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlEdoublegR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<double> : new vector<double>;
   }
   static void *newArray_vectorlEdoublegR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<double>[nElements] : new vector<double>[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlEdoublegR(void *p) {
      delete ((vector<double>*)p);
   }
   static void deleteArray_vectorlEdoublegR(void *p) {
      delete [] ((vector<double>*)p);
   }
   static void destruct_vectorlEdoublegR(void *p) {
      typedef vector<double> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<double>

namespace ROOT {
   static TClass *maplEvectorlEintgRcOintgR_Dictionary();
   static void maplEvectorlEintgRcOintgR_TClassManip(TClass*);
   static void *new_maplEvectorlEintgRcOintgR(void *p = 0);
   static void *newArray_maplEvectorlEintgRcOintgR(Long_t size, void *p);
   static void delete_maplEvectorlEintgRcOintgR(void *p);
   static void deleteArray_maplEvectorlEintgRcOintgR(void *p);
   static void destruct_maplEvectorlEintgRcOintgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const map<vector<int>,int>*)
   {
      map<vector<int>,int> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(map<vector<int>,int>));
      static ::ROOT::TGenericClassInfo 
         instance("map<vector<int>,int>", -2, "map", 99,
                  typeid(map<vector<int>,int>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &maplEvectorlEintgRcOintgR_Dictionary, isa_proxy, 4,
                  sizeof(map<vector<int>,int>) );
      instance.SetNew(&new_maplEvectorlEintgRcOintgR);
      instance.SetNewArray(&newArray_maplEvectorlEintgRcOintgR);
      instance.SetDelete(&delete_maplEvectorlEintgRcOintgR);
      instance.SetDeleteArray(&deleteArray_maplEvectorlEintgRcOintgR);
      instance.SetDestructor(&destruct_maplEvectorlEintgRcOintgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::MapInsert< map<vector<int>,int> >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const map<vector<int>,int>*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *maplEvectorlEintgRcOintgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const map<vector<int>,int>*)0x0)->GetClass();
      maplEvectorlEintgRcOintgR_TClassManip(theClass);
   return theClass;
   }

   static void maplEvectorlEintgRcOintgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_maplEvectorlEintgRcOintgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) map<vector<int>,int> : new map<vector<int>,int>;
   }
   static void *newArray_maplEvectorlEintgRcOintgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) map<vector<int>,int>[nElements] : new map<vector<int>,int>[nElements];
   }
   // Wrapper around operator delete
   static void delete_maplEvectorlEintgRcOintgR(void *p) {
      delete ((map<vector<int>,int>*)p);
   }
   static void deleteArray_maplEvectorlEintgRcOintgR(void *p) {
      delete [] ((map<vector<int>,int>*)p);
   }
   static void destruct_maplEvectorlEintgRcOintgR(void *p) {
      typedef map<vector<int>,int> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class map<vector<int>,int>

namespace ROOT {
   static TClass *maplEintcOvectorlEdoublegRsPgR_Dictionary();
   static void maplEintcOvectorlEdoublegRsPgR_TClassManip(TClass*);
   static void *new_maplEintcOvectorlEdoublegRsPgR(void *p = 0);
   static void *newArray_maplEintcOvectorlEdoublegRsPgR(Long_t size, void *p);
   static void delete_maplEintcOvectorlEdoublegRsPgR(void *p);
   static void deleteArray_maplEintcOvectorlEdoublegRsPgR(void *p);
   static void destruct_maplEintcOvectorlEdoublegRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const map<int,vector<double> >*)
   {
      map<int,vector<double> > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(map<int,vector<double> >));
      static ::ROOT::TGenericClassInfo 
         instance("map<int,vector<double> >", -2, "map", 99,
                  typeid(map<int,vector<double> >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &maplEintcOvectorlEdoublegRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(map<int,vector<double> >) );
      instance.SetNew(&new_maplEintcOvectorlEdoublegRsPgR);
      instance.SetNewArray(&newArray_maplEintcOvectorlEdoublegRsPgR);
      instance.SetDelete(&delete_maplEintcOvectorlEdoublegRsPgR);
      instance.SetDeleteArray(&deleteArray_maplEintcOvectorlEdoublegRsPgR);
      instance.SetDestructor(&destruct_maplEintcOvectorlEdoublegRsPgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::MapInsert< map<int,vector<double> > >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const map<int,vector<double> >*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *maplEintcOvectorlEdoublegRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const map<int,vector<double> >*)0x0)->GetClass();
      maplEintcOvectorlEdoublegRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void maplEintcOvectorlEdoublegRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_maplEintcOvectorlEdoublegRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) map<int,vector<double> > : new map<int,vector<double> >;
   }
   static void *newArray_maplEintcOvectorlEdoublegRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) map<int,vector<double> >[nElements] : new map<int,vector<double> >[nElements];
   }
   // Wrapper around operator delete
   static void delete_maplEintcOvectorlEdoublegRsPgR(void *p) {
      delete ((map<int,vector<double> >*)p);
   }
   static void deleteArray_maplEintcOvectorlEdoublegRsPgR(void *p) {
      delete [] ((map<int,vector<double> >*)p);
   }
   static void destruct_maplEintcOvectorlEdoublegRsPgR(void *p) {
      typedef map<int,vector<double> > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class map<int,vector<double> >

namespace ROOT {
   static TClass *maplEintcOpairlEdoublecOdoublegRsPgR_Dictionary();
   static void maplEintcOpairlEdoublecOdoublegRsPgR_TClassManip(TClass*);
   static void *new_maplEintcOpairlEdoublecOdoublegRsPgR(void *p = 0);
   static void *newArray_maplEintcOpairlEdoublecOdoublegRsPgR(Long_t size, void *p);
   static void delete_maplEintcOpairlEdoublecOdoublegRsPgR(void *p);
   static void deleteArray_maplEintcOpairlEdoublecOdoublegRsPgR(void *p);
   static void destruct_maplEintcOpairlEdoublecOdoublegRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const map<int,pair<double,double> >*)
   {
      map<int,pair<double,double> > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(map<int,pair<double,double> >));
      static ::ROOT::TGenericClassInfo 
         instance("map<int,pair<double,double> >", -2, "map", 99,
                  typeid(map<int,pair<double,double> >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &maplEintcOpairlEdoublecOdoublegRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(map<int,pair<double,double> >) );
      instance.SetNew(&new_maplEintcOpairlEdoublecOdoublegRsPgR);
      instance.SetNewArray(&newArray_maplEintcOpairlEdoublecOdoublegRsPgR);
      instance.SetDelete(&delete_maplEintcOpairlEdoublecOdoublegRsPgR);
      instance.SetDeleteArray(&deleteArray_maplEintcOpairlEdoublecOdoublegRsPgR);
      instance.SetDestructor(&destruct_maplEintcOpairlEdoublecOdoublegRsPgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::MapInsert< map<int,pair<double,double> > >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const map<int,pair<double,double> >*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *maplEintcOpairlEdoublecOdoublegRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const map<int,pair<double,double> >*)0x0)->GetClass();
      maplEintcOpairlEdoublecOdoublegRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void maplEintcOpairlEdoublecOdoublegRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_maplEintcOpairlEdoublecOdoublegRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) map<int,pair<double,double> > : new map<int,pair<double,double> >;
   }
   static void *newArray_maplEintcOpairlEdoublecOdoublegRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) map<int,pair<double,double> >[nElements] : new map<int,pair<double,double> >[nElements];
   }
   // Wrapper around operator delete
   static void delete_maplEintcOpairlEdoublecOdoublegRsPgR(void *p) {
      delete ((map<int,pair<double,double> >*)p);
   }
   static void deleteArray_maplEintcOpairlEdoublecOdoublegRsPgR(void *p) {
      delete [] ((map<int,pair<double,double> >*)p);
   }
   static void destruct_maplEintcOpairlEdoublecOdoublegRsPgR(void *p) {
      typedef map<int,pair<double,double> > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class map<int,pair<double,double> >

namespace {
  void TriggerDictionaryInitialization_HiggsAnalysisCombinedLimit_xr_Impl() {
    static const char* headers[] = {
0    };
    static const char* includePaths[] = {
"/uscms_data/d3/mreid/sueps/analysis/SUEPs/limits/CMSSW_10_2_13/src",
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
"/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/eigen/64060da8461a627eb25b5a7bc0616776068db58b/include/eigen3",
"/cvmfs/cms.cern.ch/slc7_amd64_gcc700/lcg/root/6.12.07-gnimlf5/include",
"/uscms_data/d3/mreid/sueps/analysis/SUEPs/limits/CMSSW_10_2_13/",
0
    };
    static const char* fwdDeclCode = R"DICTFWDDCLS(
#line 1 "HiggsAnalysisCombinedLimit_xr dictionary forward declarations' payload"
#pragma clang diagnostic ignored "-Wkeyword-compat"
#pragma clang diagnostic ignored "-Wignored-attributes"
#pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
extern int __Cling_Autoloading_Map;
namespace std{template <typename _Tp> class __attribute__((annotate("$clingAutoload$bits/allocator.h")))  __attribute__((annotate("$clingAutoload$string")))  allocator;
}
namespace std{template <typename _T1, typename _T2> struct __attribute__((annotate("$clingAutoload$bits/stl_pair.h")))  __attribute__((annotate("$clingAutoload$string")))  pair;
}
class __attribute__((annotate(R"ATTRDUMP(transient@@@true)ATTRDUMP"))) __attribute__((annotate(R"ATTRDUMP(A concrete implementation of ProposalFunction, that uniformly samples the parameter space.)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/TestProposal.h")))  TestProposal;
class __attribute__((annotate(R"ATTRDUMP(transient@@@true)ATTRDUMP"))) __attribute__((annotate(R"ATTRDUMP(A concrete implementation of ProposalFunction, that uniformly samples the parameter space.)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/DebugProposal.h")))  DebugProposal;
class __attribute__((annotate(R"ATTRDUMP(PDF constructed from a sum of (non-pdf) functions)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/VerticalInterpPdf.h")))  VerticalInterpPdf;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/SimpleCacheSentry.h")))  __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/VerticalInterpHistPdf.h")))  SimpleCacheSentry;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/FastTemplate_Old.h")))  __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/VerticalInterpHistPdf.h")))  FastTemplate;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/FastTemplate_Old.h")))  __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/VerticalInterpHistPdf.h")))  FastHisto;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/FastTemplate_Old.h")))  __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/VerticalInterpHistPdf.h")))  FastHisto2D;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/FastTemplate_Old.h")))  __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/VerticalInterpHistPdf.h")))  FastHisto3D;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/VerticalInterpHistPdf.h")))  VerticalInterpHistPdf;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/VerticalInterpHistPdf.h")))  FastVerticalInterpHistPdfBase;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/VerticalInterpHistPdf.h")))  FastVerticalInterpHistPdf;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/VerticalInterpHistPdf.h")))  FastVerticalInterpHistPdf2D;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/VerticalInterpHistPdf.h")))  FastVerticalInterpHistPdf2Base;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/VerticalInterpHistPdf.h")))  FastVerticalInterpHistPdf2;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/VerticalInterpHistPdf.h")))  FastVerticalInterpHistPdf2D2;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/VerticalInterpHistPdf.h")))  FastVerticalInterpHistPdf3D;
class __attribute__((annotate(R"ATTRDUMP(Asymmetric power)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/AsymPow.h")))  AsymPow;
class __attribute__((annotate(R"ATTRDUMP(Asymmetric power)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/AsymQuad.h")))  AsymQuad;
class __attribute__((annotate(R"ATTRDUMP(transient@@@true)ATTRDUMP"))) __attribute__((annotate(R"ATTRDUMP(Make RooDataHist)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/CombDataSetFactory.h")))  CombDataSetFactory;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/TH1Keys.h")))  TH1Keys;
class __attribute__((annotate(R"ATTRDUMP(Variant of RooSimultaneous that can put together binned and unbinned stuff)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/RooSimultaneousOpt.h")))  RooSimultaneousOpt;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4L_RooCTauPdf_1D.h")))  HZZ4L_RooCTauPdf_1D;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4L_RooCTauPdf_1D_Expanded.h")))  HZZ4L_RooCTauPdf_1D_Expanded;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4L_RooCTauPdf_2D.h")))  HZZ4L_RooCTauPdf_2D;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h")))  RooqqZZPdf;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h")))  RooggZZPdf;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h")))  RooqqZZPdf_v2;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h")))  RooVBFZZPdf;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h")))  RooVBFZZPdf_v2;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h")))  RooggZZPdf_v2;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h")))  RooBetaFunc_v2;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h")))  Roo4lMasses2D_Bkg;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h")))  Roo4lMasses2D_BkgGGZZ;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h")))  Roo4lMasses2D;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h")))  RooFourMuMassShapePdf2;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h")))  RooFourEMassShapePdf2;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h")))  RooTwoETwoMuMassShapePdf2;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h")))  RooFourMuMassRes;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h")))  RooFourEMassRes;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h")))  RooTwoETwoMuMassRes;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h")))  RooRelBW1;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h")))  RooRelBWUF;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h")))  RooRelBWUF_SM4;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h")))  RooRelBWUFParamWidth;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h")))  RooRelBWUFParam;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h")))  RooRelBWHighMass;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h")))  RooTsallis;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h")))  RooaDoubleCBxBW;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h")))  RooCPSHighMassGGH;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h")))  RooBWHighMassGGH;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h")))  RooCPSHighMassGGHNoInterf;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h")))  RooCPSHighMassVBF;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h")))  RooCPSHighMassVBFNoInterf;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h")))  RooSigPlusInt;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h")))  RooErfExpPdf;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h")))  RooAlpha;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h")))  RooAlphaExp;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h")))  RooBWRunPdf;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h")))  RooErfPow2Pdf;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h")))  RooAlpha4ErfPow2Pdf;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h")))  RooErfPowExpPdf;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h")))  RooAlpha4ErfPowExpPdf;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h")))  RooGausExpPdf;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h")))  RooAlpha4GausExpPdf;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h")))  RooErfPowPdf;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h")))  RooAlpha4ErfPowPdf;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h")))  RooPow2Pdf;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h")))  RooPowPdf;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h")))  RooQCDPdf;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h")))  RooUser1Pdf;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h")))  RooExpNPdf;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h")))  RooAlpha4ExpNPdf;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h")))  RooExpTailPdf;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h")))  RooAlpha4ExpTailPdf;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h")))  Roo2ExpPdf;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h")))  RooAlpha42ExpPdf;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h")))  RooAnaExpNPdf;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h")))  RooDoubleCrystalBall;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ2L2QRooPdfs.h")))  RooCB;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ2L2QRooPdfs.h")))  RooDoubleCB;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ2L2QRooPdfs.h")))  RooFermi;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ2L2QRooPdfs.h")))  RooRelBW;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ2L2QRooPdfs.h")))  Triangle;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ2L2QRooPdfs.h")))  RooLevelledExp;
class __attribute__((annotate(R"ATTRDUMP(Exponential PDF)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HGGRooPdfs.h")))  RooPower;
class __attribute__((annotate(R"ATTRDUMP(Bernstein polynomial PDF with step function)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZGRooPdfs.h")))  RooStepBernstein;
class __attribute__((annotate(R"ATTRDUMP(Bernstein polynomial PDF with step function convoluted with gaussian)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZGRooPdfs.h")))  RooGaussStepBernstein;
namespace cmsmath{class __attribute__((annotate(R"ATTRDUMP(transient@@@true)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/SequentialMinimizer.h")))  SequentialMinimizer;}
class __attribute__((annotate(R"ATTRDUMP(Process normalization interpolator)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/ProcessNormalization.h")))  ProcessNormalization;
class __attribute__((annotate(R"ATTRDUMP(PDF constructed from a sum of (non-pdf) functions)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/RooRealFlooredSumPdf.h")))  RooRealFlooredSumPdf;
class __attribute__((annotate(R"ATTRDUMP(Smooth interpolation)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/RooSpline1D.h")))  RooSpline1D;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/RooSplineND.h")))  RooSplineND;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/RooScaleLOSM.h")))  RooScaleLOSM;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/RooScaleLOSM.h")))  RooScaleHGamGamLOSM;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/RooScaleLOSM.h")))  RooScaleHGluGluLOSM;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/RooScaleLOSM.h")))  RooScaleHGamGamLOSMPlusX;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/RooScaleLOSM.h")))  RooScaleHGluGluLOSMPlusX;
class __attribute__((annotate(R"ATTRDUMP(transient@@@true)ATTRDUMP"))) __attribute__((annotate(R"ATTRDUMP(Asymmetric power)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/rVrFLikelihood.h")))  rVrFLikelihood;
class __attribute__((annotate(R"ATTRDUMP(Multi PDF)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/RooMultiPdf.h")))  RooMultiPdf;
template <int N> class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/RooBernsteinFast.h")))  RooBernsteinFast;

class __attribute__((annotate(R"ATTRDUMP(Gaussian PDF with fast log)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/SimpleGaussianConstraint.h")))  SimpleGaussianConstraint;
class __attribute__((annotate(R"ATTRDUMP(Poisson PDF with fast log)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/SimplePoissonConstraint.h")))  SimplePoissonConstraint;
class __attribute__((annotate(R"ATTRDUMP(transient@@@true)ATTRDUMP"))) __attribute__((annotate(R"ATTRDUMP(group of constraints)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/SimpleConstraintGroup.h")))  SimpleConstraintGroup;
namespace RooStats{namespace HistFactory{class __attribute__((annotate(R"ATTRDUMP(Uniform B-Spline)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/AtlasPdfs.h")))  RooBSplineBases;}}
namespace RooStats{namespace HistFactory{class __attribute__((annotate(R"ATTRDUMP(Uniform B-Spline)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/AtlasPdfs.h")))  RooBSpline;}}
class __attribute__((annotate(R"ATTRDUMP(One-dimensional non-parametric kernel estimation p.d.f.)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/AtlasPdfs.h")))  RooParamKeysPdf;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/AtlasPdfs.h")))  RooStarMomentMorph;
template <typename U> class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/FastTemplateFunc.h")))  FastHistoAxis_t;

template <typename T> class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/FastTemplateFunc.h")))  FastTemplate_t;

typedef double Double_t __attribute__((annotate("$clingAutoload$RtypesCore.h"))) ;
template <typename T, typename U = Double_t> class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/FastTemplateFunc.h")))  FastHisto_t;

template <typename T, typename U = Double_t> class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/FastTemplateFunc.h")))  FastHisto2D_t;

template <typename T, typename U = Double_t> class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/FastTemplateFunc.h")))  FastHisto3D_t;

template <typename T> class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/FastTemplateFunc.h")))  FastTemplateFunc_t;

template <typename T, typename U = Double_t> class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/FastTemplateFunc.h")))  FastHistoFunc_t;

template <typename T, typename U = Double_t> class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/FastTemplateFunc.h")))  FastHisto2DFunc_t;

template <typename T, typename U = Double_t> class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/FastTemplateFunc.h")))  FastHisto3DFunc_t;

class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4L_RooSpinZeroPdf.h")))  HZZ4L_RooSpinZeroPdf;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4L_RooSpinZeroPdf_1D.h")))  HZZ4L_RooSpinZeroPdf_1D;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4L_RooSpinZeroPdf_2D.h")))  HZZ4L_RooSpinZeroPdf_2D;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4L_RooSpinZeroPdf_phase.h")))  HZZ4L_RooSpinZeroPdf_phase;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/VBFHZZ4L_RooSpinZeroPdf.h")))  VBFHZZ4L_RooSpinZeroPdf;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/VBFHZZ4L_RooSpinZeroPdf_fast.h")))  VBFHZZ4L_RooSpinZeroPdf_fast;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4L_RooSpinZeroPdf_1D_fast.h")))  HZZ4L_RooSpinZeroPdf_1D_fast;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4L_RooSpinZeroPdf_2D_fast.h")))  HZZ4L_RooSpinZeroPdf_2D_fast;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HZZ4L_RooSpinZeroPdf_phase_fast.h")))  HZZ4L_RooSpinZeroPdf_phase_fast;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/VVHZZ4L_RooSpinZeroPdf_1D_fast.h")))  VVHZZ4L_RooSpinZeroPdf_1D_fast;
class __attribute__((annotate(R"ATTRDUMP(Chebyshev polynomial implementation.)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HWWLVJJRooPdfs.h")))  RooChebyshevPDF;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HWWLVJJRooPdfs.h")))  RooErfPdf;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HWWLVJJRooPdfs.h")))  RooPowerExpPdf;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HWWLVJJRooPdfs.h")))  RooTH1DPdf;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HWWLVJJRooPdfs.h")))  RooPowerFunction;
class __attribute__((annotate(R"ATTRDUMP(Power law PDF)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HWWLVJJRooPdfs.h")))  RooPowerLaw;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/HWWLVJJRooPdfs.h")))  RooExpPoly;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/RooMorphingPdf.h")))  RooMorphingPdf;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/RooParametricHist.h")))  RooParametricHist;
class __attribute__((annotate(R"ATTRDUMP(RooParametricShapeBinPdf function)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/RooParametricShapeBinPdf.h")))  RooParametricShapeBinPdf;
class __attribute__((annotate(R"ATTRDUMP(Your description goes here...)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/GaussExp.h")))  GaussExp;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/RooDoubleCBFast.h")))  RooDoubleCBFast;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/CMSHistFunc.h")))  CMSHistFunc;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/CMSHistErrorPropagator.h")))  CMSHistErrorPropagator;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/CMSHistFuncWrapper.h")))  CMSHistFuncWrapper;
class __attribute__((annotate(R"ATTRDUMP(Multivariate Gaussian PDF with correlations)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/RooTaylorExpansion.h")))  RooTaylorExpansion;
class __attribute__((annotate(R"ATTRDUMP(Simple Taylor Expansion in 1D)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/SimpleTaylorExpansion1D.h")))  SimpleTaylorExpansion1D;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/RooPiecewisePolynomial.h")))  RooPiecewisePolynomial;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/RooNCSplineCore.h")))  RooNCSplineCore;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/RooNCSpline_1D_fast.h")))  RooNCSpline_1D_fast;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/RooNCSpline_2D_fast.h")))  RooNCSpline_2D_fast;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/RooNCSpline_3D_fast.h")))  RooNCSpline_3D_fast;
class __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/RooFuncPdf.h")))  RooFuncPdf;
typedef FastHistoAxis_t<Double_t> FastHistoAxis_d __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/FastTemplateFunc.h"))) ;
typedef FastTemplate_t<Double_t> FastTemplate_d __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/FastTemplateFunc.h"))) ;
typedef FastHisto_t<Double_t> FastHisto_d __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/FastTemplateFunc.h"))) ;
typedef FastHisto2D_t<Double_t> FastHisto2D_d __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/FastTemplateFunc.h"))) ;
typedef FastHisto3D_t<Double_t> FastHisto3D_d __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/FastTemplateFunc.h"))) ;
typedef float Float_t __attribute__((annotate("$clingAutoload$RtypesCore.h"))) ;
typedef FastHistoAxis_t<Float_t> FastHistoAxis_f __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/FastTemplateFunc.h"))) ;
typedef FastTemplate_t<Float_t> FastTemplate_f __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/FastTemplateFunc.h"))) ;
typedef FastHisto_t<Float_t> FastHisto_f __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/FastTemplateFunc.h"))) ;
typedef FastHisto2D_t<Float_t> FastHisto2D_f __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/FastTemplateFunc.h"))) ;
typedef FastHisto3D_t<Float_t> FastHisto3D_f __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/FastTemplateFunc.h"))) ;
typedef FastTemplateFunc_t<Float_t> FastTemplateFunc_f __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/FastTemplateFunc.h"))) ;
typedef FastTemplateFunc_t<Double_t> FastTemplateFunc_d __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/FastTemplateFunc.h"))) ;
typedef FastHistoFunc_t<Float_t> FastHistoFunc_f __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/FastTemplateFunc.h"))) ;
typedef FastHistoFunc_t<Double_t> FastHistoFunc_d __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/FastTemplateFunc.h"))) ;
typedef FastHisto2DFunc_t<Float_t> FastHisto2DFunc_f __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/FastTemplateFunc.h"))) ;
typedef FastHisto2DFunc_t<Double_t> FastHisto2DFunc_d __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/FastTemplateFunc.h"))) ;
typedef FastHisto3DFunc_t<Float_t> FastHisto3DFunc_f __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/FastTemplateFunc.h"))) ;
typedef FastHisto3DFunc_t<Double_t> FastHisto3DFunc_d __attribute__((annotate("$clingAutoload$HiggsAnalysis/CombinedLimit/interface/FastTemplateFunc.h"))) ;
)DICTFWDDCLS";
    static const char* payloadCode = R"DICTPAYLOAD(
#line 1 "HiggsAnalysisCombinedLimit_xr dictionary payload"

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
#ifndef EIGEN_DONT_PARALLELIZE
  #define EIGEN_DONT_PARALLELIZE 1
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
#include "HiggsAnalysis/CombinedLimit/interface/TestProposal.h"
#include "HiggsAnalysis/CombinedLimit/interface/DebugProposal.h"
#include "HiggsAnalysis/CombinedLimit/interface/VerticalInterpPdf.h"
#include "HiggsAnalysis/CombinedLimit/interface/VerticalInterpHistPdf.h"
#include "HiggsAnalysis/CombinedLimit/interface/AsymPow.h"
#include "HiggsAnalysis/CombinedLimit/interface/AsymQuad.h"
#include "HiggsAnalysis/CombinedLimit/interface/CombDataSetFactory.h"
#include "HiggsAnalysis/CombinedLimit/interface/TH1Keys.h"
#include "HiggsAnalysis/CombinedLimit/interface/RooSimultaneousOpt.h"
#include "HiggsAnalysis/CombinedLimit/interface/SimpleCacheSentry.h"
#include "HiggsAnalysis/CombinedLimit/interface/th1fmorph.h"
#include "HiggsAnalysis/CombinedLimit/interface/HZZ4L_RooCTauPdf_1D.h"
#include "HiggsAnalysis/CombinedLimit/interface/HZZ4L_RooCTauPdf_1D_Expanded.h"
#include "HiggsAnalysis/CombinedLimit/interface/HZZ4L_RooCTauPdf_2D.h"
#include "HiggsAnalysis/CombinedLimit/interface/HZZ4LRooPdfs.h"
#include "HiggsAnalysis/CombinedLimit/interface/HWWLVJRooPdfs.h"
#include "HiggsAnalysis/CombinedLimit/interface/HZZ2L2QRooPdfs.h"
#include "HiggsAnalysis/CombinedLimit/interface/HGGRooPdfs.h"
#include "HiggsAnalysis/CombinedLimit/interface/HZGRooPdfs.h"
#include "HiggsAnalysis/CombinedLimit/interface/SequentialMinimizer.h"
#include "HiggsAnalysis/CombinedLimit/interface/ProcessNormalization.h"
#include "HiggsAnalysis/CombinedLimit/interface/RooRealFlooredSumPdf.h"
#include "HiggsAnalysis/CombinedLimit/interface/RooSpline1D.h"
#include "HiggsAnalysis/CombinedLimit/interface/RooSplineND.h"
#include "HiggsAnalysis/CombinedLimit/interface/RooScaleLOSM.h"
#include "HiggsAnalysis/CombinedLimit/interface/rVrFLikelihood.h"
#include "HiggsAnalysis/CombinedLimit/interface/RooMultiPdf.h"
#include "HiggsAnalysis/CombinedLimit/interface/RooBernsteinFast.h"
#include "HiggsAnalysis/CombinedLimit/interface/SimpleGaussianConstraint.h"
#include "HiggsAnalysis/CombinedLimit/interface/SimplePoissonConstraint.h"
#include "HiggsAnalysis/CombinedLimit/interface/SimpleConstraintGroup.h"
#include "HiggsAnalysis/CombinedLimit/interface/AtlasPdfs.h"
#include "HiggsAnalysis/CombinedLimit/interface/FastTemplateFunc.h"
#include "HiggsAnalysis/CombinedLimit/interface/HZZ4L_RooSpinZeroPdf.h"
#include "HiggsAnalysis/CombinedLimit/interface/HZZ4L_RooSpinZeroPdf_1D.h"
#include "HiggsAnalysis/CombinedLimit/interface/HZZ4L_RooSpinZeroPdf_2D.h"
#include "HiggsAnalysis/CombinedLimit/interface/HZZ4L_RooSpinZeroPdf_phase.h"
#include "HiggsAnalysis/CombinedLimit/interface/VBFHZZ4L_RooSpinZeroPdf.h"
#include "HiggsAnalysis/CombinedLimit/interface/VBFHZZ4L_RooSpinZeroPdf_fast.h"

#include "HiggsAnalysis/CombinedLimit/interface/HZZ4L_RooSpinZeroPdf_1D_fast.h"
#include "HiggsAnalysis/CombinedLimit/interface/HZZ4L_RooSpinZeroPdf_2D_fast.h"
#include "HiggsAnalysis/CombinedLimit/interface/HZZ4L_RooSpinZeroPdf_phase_fast.h"
#include "HiggsAnalysis/CombinedLimit/interface/VVHZZ4L_RooSpinZeroPdf_1D_fast.h"

#include "HiggsAnalysis/CombinedLimit/interface/HWWLVJJRooPdfs.h"
//#include "HiggsAnalysis/CombinedLimit/interface/RooMomentMorphND.h"
#include "HiggsAnalysis/CombinedLimit/interface/RooMorphingPdf.h"
#include "HiggsAnalysis/CombinedLimit/interface/RooParametricHist.h"
#include "HiggsAnalysis/CombinedLimit/interface/RooParametricShapeBinPdf.h"
#include "HiggsAnalysis/CombinedLimit/interface/GaussExp.h"
#include "HiggsAnalysis/CombinedLimit/interface/RooDoubleCBFast.h"
#include "HiggsAnalysis/CombinedLimit/interface/CMSHistFunc.h"
#include "HiggsAnalysis/CombinedLimit/interface/CMSHistErrorPropagator.h"
#include "HiggsAnalysis/CombinedLimit/interface/CMSHistFuncWrapper.h"
#include "HiggsAnalysis/CombinedLimit/interface/RooTaylorExpansion.h"
#include "HiggsAnalysis/CombinedLimit/interface/SimpleTaylorExpansion1D.h"

#include "HiggsAnalysis/CombinedLimit/interface/RooPiecewisePolynomial.h"

#include "HiggsAnalysis/CombinedLimit/interface/RooNCSplineCore.h"
#include "HiggsAnalysis/CombinedLimit/interface/RooNCSpline_1D_fast.h"
#include "HiggsAnalysis/CombinedLimit/interface/RooNCSpline_2D_fast.h"
#include "HiggsAnalysis/CombinedLimit/interface/RooNCSpline_3D_fast.h"
#include "HiggsAnalysis/CombinedLimit/interface/RooFuncPdf.h"

namespace {
    struct dictionary {
	RooBernsteinFast<1> my_RooBernsteinFast_1;
	RooBernsteinFast<2> my_RooBernsteinFast_2;
	RooBernsteinFast<3> my_RooBernsteinFast_3;
	RooBernsteinFast<4> my_RooBernsteinFast_4;
	RooBernsteinFast<5> my_RooBernsteinFast_5;
	RooBernsteinFast<6> my_RooBernsteinFast_6;
	RooBernsteinFast<7> my_RooBernsteinFast_7;
    };
}

#undef  _BACKWARD_BACKWARD_WARNING_H
)DICTPAYLOAD";
    static const char* classesHeaders[]={
"AsymPow", payloadCode, "@",
"AsymQuad", payloadCode, "@",
"CMSHistErrorPropagator", payloadCode, "@",
"CMSHistFunc", payloadCode, "@",
"CMSHistFuncWrapper", payloadCode, "@",
"CombDataSetFactory", payloadCode, "@",
"DebugProposal", payloadCode, "@",
"FastHisto", payloadCode, "@",
"FastHisto2D", payloadCode, "@",
"FastHisto2DFunc_d", payloadCode, "@",
"FastHisto2DFunc_f", payloadCode, "@",
"FastHisto2DFunc_t<double,double>", payloadCode, "@",
"FastHisto2DFunc_t<float,double>", payloadCode, "@",
"FastHisto2D_d", payloadCode, "@",
"FastHisto2D_f", payloadCode, "@",
"FastHisto2D_t<double,double>", payloadCode, "@",
"FastHisto2D_t<float,double>", payloadCode, "@",
"FastHisto3D", payloadCode, "@",
"FastHisto3DFunc_d", payloadCode, "@",
"FastHisto3DFunc_f", payloadCode, "@",
"FastHisto3DFunc_t<double,double>", payloadCode, "@",
"FastHisto3DFunc_t<float,double>", payloadCode, "@",
"FastHisto3D_d", payloadCode, "@",
"FastHisto3D_f", payloadCode, "@",
"FastHisto3D_t<double,double>", payloadCode, "@",
"FastHisto3D_t<float,double>", payloadCode, "@",
"FastHistoAxis_d", payloadCode, "@",
"FastHistoAxis_f", payloadCode, "@",
"FastHistoAxis_t<double>", payloadCode, "@",
"FastHistoAxis_t<float>", payloadCode, "@",
"FastHistoFunc_d", payloadCode, "@",
"FastHistoFunc_f", payloadCode, "@",
"FastHistoFunc_t<double,double>", payloadCode, "@",
"FastHistoFunc_t<float,double>", payloadCode, "@",
"FastHisto_d", payloadCode, "@",
"FastHisto_f", payloadCode, "@",
"FastHisto_t<double,double>", payloadCode, "@",
"FastHisto_t<float,double>", payloadCode, "@",
"FastTemplate", payloadCode, "@",
"FastTemplateFunc_d", payloadCode, "@",
"FastTemplateFunc_f", payloadCode, "@",
"FastTemplateFunc_t<double>", payloadCode, "@",
"FastTemplateFunc_t<float>", payloadCode, "@",
"FastTemplate_d", payloadCode, "@",
"FastTemplate_f", payloadCode, "@",
"FastTemplate_t<double>", payloadCode, "@",
"FastTemplate_t<float>", payloadCode, "@",
"FastVerticalInterpHistPdf", payloadCode, "@",
"FastVerticalInterpHistPdf2", payloadCode, "@",
"FastVerticalInterpHistPdf2Base", payloadCode, "@",
"FastVerticalInterpHistPdf2D", payloadCode, "@",
"FastVerticalInterpHistPdf2D2", payloadCode, "@",
"FastVerticalInterpHistPdf3D", payloadCode, "@",
"FastVerticalInterpHistPdfBase", payloadCode, "@",
"FastVerticalInterpHistPdfBase::Morph", payloadCode, "@",
"GaussExp", payloadCode, "@",
"HZZ4L_RooCTauPdf_1D", payloadCode, "@",
"HZZ4L_RooCTauPdf_1D_Expanded", payloadCode, "@",
"HZZ4L_RooCTauPdf_2D", payloadCode, "@",
"HZZ4L_RooSpinZeroPdf", payloadCode, "@",
"HZZ4L_RooSpinZeroPdf_1D", payloadCode, "@",
"HZZ4L_RooSpinZeroPdf_1D_fast", payloadCode, "@",
"HZZ4L_RooSpinZeroPdf_2D", payloadCode, "@",
"HZZ4L_RooSpinZeroPdf_2D_fast", payloadCode, "@",
"HZZ4L_RooSpinZeroPdf_phase", payloadCode, "@",
"HZZ4L_RooSpinZeroPdf_phase_fast", payloadCode, "@",
"ProcessNormalization", payloadCode, "@",
"Roo2ExpPdf", payloadCode, "@",
"Roo4lMasses2D", payloadCode, "@",
"Roo4lMasses2D_Bkg", payloadCode, "@",
"Roo4lMasses2D_BkgGGZZ", payloadCode, "@",
"RooAlpha", payloadCode, "@",
"RooAlpha42ExpPdf", payloadCode, "@",
"RooAlpha4ErfPow2Pdf", payloadCode, "@",
"RooAlpha4ErfPowExpPdf", payloadCode, "@",
"RooAlpha4ErfPowPdf", payloadCode, "@",
"RooAlpha4ExpNPdf", payloadCode, "@",
"RooAlpha4ExpTailPdf", payloadCode, "@",
"RooAlpha4GausExpPdf", payloadCode, "@",
"RooAlphaExp", payloadCode, "@",
"RooAnaExpNPdf", payloadCode, "@",
"RooBWHighMassGGH", payloadCode, "@",
"RooBWRunPdf", payloadCode, "@",
"RooBernsteinFast<1>", payloadCode, "@",
"RooBernsteinFast<2>", payloadCode, "@",
"RooBernsteinFast<3>", payloadCode, "@",
"RooBernsteinFast<4>", payloadCode, "@",
"RooBernsteinFast<5>", payloadCode, "@",
"RooBernsteinFast<6>", payloadCode, "@",
"RooBernsteinFast<7>", payloadCode, "@",
"RooBetaFunc_v2", payloadCode, "@",
"RooCB", payloadCode, "@",
"RooCPSHighMassGGH", payloadCode, "@",
"RooCPSHighMassGGHNoInterf", payloadCode, "@",
"RooCPSHighMassVBF", payloadCode, "@",
"RooCPSHighMassVBFNoInterf", payloadCode, "@",
"RooChebyshevPDF", payloadCode, "@",
"RooDoubleCB", payloadCode, "@",
"RooDoubleCBFast", payloadCode, "@",
"RooDoubleCrystalBall", payloadCode, "@",
"RooErfExpPdf", payloadCode, "@",
"RooErfPdf", payloadCode, "@",
"RooErfPow2Pdf", payloadCode, "@",
"RooErfPowExpPdf", payloadCode, "@",
"RooErfPowPdf", payloadCode, "@",
"RooExpNPdf", payloadCode, "@",
"RooExpPoly", payloadCode, "@",
"RooExpTailPdf", payloadCode, "@",
"RooFermi", payloadCode, "@",
"RooFourEMassRes", payloadCode, "@",
"RooFourEMassShapePdf2", payloadCode, "@",
"RooFourMuMassRes", payloadCode, "@",
"RooFourMuMassShapePdf2", payloadCode, "@",
"RooFuncPdf", payloadCode, "@",
"RooGausExpPdf", payloadCode, "@",
"RooGaussStepBernstein", payloadCode, "@",
"RooLevelledExp", payloadCode, "@",
"RooMorphingPdf", payloadCode, "@",
"RooMultiPdf", payloadCode, "@",
"RooNCSplineCore", payloadCode, "@",
"RooNCSpline_1D_fast", payloadCode, "@",
"RooNCSpline_2D_fast", payloadCode, "@",
"RooNCSpline_3D_fast", payloadCode, "@",
"RooParamKeysPdf", payloadCode, "@",
"RooParametricHist", payloadCode, "@",
"RooParametricShapeBinPdf", payloadCode, "@",
"RooPiecewisePolynomial", payloadCode, "@",
"RooPow2Pdf", payloadCode, "@",
"RooPowPdf", payloadCode, "@",
"RooPower", payloadCode, "@",
"RooPowerExpPdf", payloadCode, "@",
"RooPowerFunction", payloadCode, "@",
"RooPowerLaw", payloadCode, "@",
"RooQCDPdf", payloadCode, "@",
"RooRealFlooredSumPdf", payloadCode, "@",
"RooRelBW", payloadCode, "@",
"RooRelBW1", payloadCode, "@",
"RooRelBWHighMass", payloadCode, "@",
"RooRelBWUF", payloadCode, "@",
"RooRelBWUFParam", payloadCode, "@",
"RooRelBWUFParamWidth", payloadCode, "@",
"RooRelBWUF_SM4", payloadCode, "@",
"RooScaleHGamGamLOSM", payloadCode, "@",
"RooScaleHGamGamLOSMPlusX", payloadCode, "@",
"RooScaleHGluGluLOSM", payloadCode, "@",
"RooScaleHGluGluLOSMPlusX", payloadCode, "@",
"RooScaleLOSM", payloadCode, "@",
"RooSigPlusInt", payloadCode, "@",
"RooSimultaneousOpt", payloadCode, "@",
"RooSpline1D", payloadCode, "@",
"RooSplineND", payloadCode, "@",
"RooStarMomentMorph", payloadCode, "@",
"RooStats::HistFactory::RooBSpline", payloadCode, "@",
"RooStats::HistFactory::RooBSplineBases", payloadCode, "@",
"RooStepBernstein", payloadCode, "@",
"RooTH1DPdf", payloadCode, "@",
"RooTaylorExpansion", payloadCode, "@",
"RooTsallis", payloadCode, "@",
"RooTwoETwoMuMassRes", payloadCode, "@",
"RooTwoETwoMuMassShapePdf2", payloadCode, "@",
"RooUser1Pdf", payloadCode, "@",
"RooVBFZZPdf", payloadCode, "@",
"RooVBFZZPdf_v2", payloadCode, "@",
"RooaDoubleCBxBW", payloadCode, "@",
"RooggZZPdf", payloadCode, "@",
"RooggZZPdf_v2", payloadCode, "@",
"RooqqZZPdf", payloadCode, "@",
"RooqqZZPdf_v2", payloadCode, "@",
"SimpleCacheSentry", payloadCode, "@",
"SimpleConstraintGroup", payloadCode, "@",
"SimpleGaussianConstraint", payloadCode, "@",
"SimplePoissonConstraint", payloadCode, "@",
"SimpleTaylorExpansion1D", payloadCode, "@",
"TH1Keys", payloadCode, "@",
"TestProposal", payloadCode, "@",
"Triangle", payloadCode, "@",
"VBFHZZ4L_RooSpinZeroPdf", payloadCode, "@",
"VBFHZZ4L_RooSpinZeroPdf_fast", payloadCode, "@",
"VVHZZ4L_RooSpinZeroPdf_1D_fast", payloadCode, "@",
"VerticalInterpHistPdf", payloadCode, "@",
"VerticalInterpPdf", payloadCode, "@",
"__gnu_cxx::__normal_iterator<const vector<double>*,vector<vector<double> > >", payloadCode, "@",
"__gnu_cxx::__normal_iterator<const vector<float>*,vector<vector<float> > >", payloadCode, "@",
"__gnu_cxx::__normal_iterator<const vector<vector<double> >*,vector<vector<vector<double> > > >", payloadCode, "@",
"__gnu_cxx::__normal_iterator<const vector<vector<float> >*,vector<vector<vector<float> > > >", payloadCode, "@",
"__gnu_cxx::__normal_iterator<const vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > >", payloadCode, "@",
"__gnu_cxx::__normal_iterator<const vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > >", payloadCode, "@",
"__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > >", payloadCode, "@",
"__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > >", payloadCode, "@",
"__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > >", payloadCode, "@",
"__gnu_cxx::__normal_iterator<const vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > >", payloadCode, "@",
"__gnu_cxx::__normal_iterator<vector<double>*,vector<vector<double> > >", payloadCode, "@",
"__gnu_cxx::__normal_iterator<vector<float>*,vector<vector<float> > >", payloadCode, "@",
"__gnu_cxx::__normal_iterator<vector<vector<double> >*,vector<vector<vector<double> > > >", payloadCode, "@",
"__gnu_cxx::__normal_iterator<vector<vector<float> >*,vector<vector<vector<float> > > >", payloadCode, "@",
"__gnu_cxx::__normal_iterator<vector<vector<vector<double> > >*,vector<vector<vector<vector<double> > > > >", payloadCode, "@",
"__gnu_cxx::__normal_iterator<vector<vector<vector<float> > >*,vector<vector<vector<vector<float> > > > >", payloadCode, "@",
"__gnu_cxx::__normal_iterator<vector<vector<vector<vector<double> > > >*,vector<vector<vector<vector<vector<double> > > > > >", payloadCode, "@",
"__gnu_cxx::__normal_iterator<vector<vector<vector<vector<float> > > >*,vector<vector<vector<vector<vector<float> > > > > >", payloadCode, "@",
"__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<double> > > > >*,vector<vector<vector<vector<vector<vector<double> > > > > > >", payloadCode, "@",
"__gnu_cxx::__normal_iterator<vector<vector<vector<vector<vector<float> > > > >*,vector<vector<vector<vector<vector<vector<float> > > > > > >", payloadCode, "@",
"cmsmath::SequentialMinimizer", payloadCode, "@",
"rVrFLikelihood", payloadCode, "@",
"vector<std::vector<Double_t> >::const_iterator", payloadCode, "@",
"vector<std::vector<Double_t> >::iterator", payloadCode, "@",
"vector<std::vector<Float_t> >::const_iterator", payloadCode, "@",
"vector<std::vector<Float_t> >::iterator", payloadCode, "@",
"vector<std::vector<std::vector<Double_t> > >::const_iterator", payloadCode, "@",
"vector<std::vector<std::vector<Double_t> > >::iterator", payloadCode, "@",
"vector<std::vector<std::vector<Float_t> > >::const_iterator", payloadCode, "@",
"vector<std::vector<std::vector<Float_t> > >::iterator", payloadCode, "@",
"vector<std::vector<std::vector<std::vector<Double_t> > > >::const_iterator", payloadCode, "@",
"vector<std::vector<std::vector<std::vector<Double_t> > > >::iterator", payloadCode, "@",
"vector<std::vector<std::vector<std::vector<Float_t> > > >::const_iterator", payloadCode, "@",
"vector<std::vector<std::vector<std::vector<Float_t> > > >::iterator", payloadCode, "@",
"vector<std::vector<std::vector<std::vector<std::vector<Double_t> > > > >::const_iterator", payloadCode, "@",
"vector<std::vector<std::vector<std::vector<std::vector<Double_t> > > > >::iterator", payloadCode, "@",
"vector<std::vector<std::vector<std::vector<std::vector<Float_t> > > > >::const_iterator", payloadCode, "@",
"vector<std::vector<std::vector<std::vector<std::vector<Float_t> > > > >::iterator", payloadCode, "@",
"vector<std::vector<std::vector<std::vector<std::vector<std::vector<Double_t> > > > > >::const_iterator", payloadCode, "@",
"vector<std::vector<std::vector<std::vector<std::vector<std::vector<Double_t> > > > > >::iterator", payloadCode, "@",
"vector<std::vector<std::vector<std::vector<std::vector<std::vector<Float_t> > > > > >::const_iterator", payloadCode, "@",
"vector<std::vector<std::vector<std::vector<std::vector<std::vector<Float_t> > > > > >::iterator", payloadCode, "@",
nullptr};

    static bool isInitialized = false;
    if (!isInitialized) {
      TROOT::RegisterModule("HiggsAnalysisCombinedLimit_xr",
        headers, includePaths, payloadCode, fwdDeclCode,
        TriggerDictionaryInitialization_HiggsAnalysisCombinedLimit_xr_Impl, {}, classesHeaders);
      isInitialized = true;
    }
  }
  static struct DictInit {
    DictInit() {
      TriggerDictionaryInitialization_HiggsAnalysisCombinedLimit_xr_Impl();
    }
  } __TheDictionaryInitializer;
}
void TriggerDictionaryInitialization_HiggsAnalysisCombinedLimit_xr() {
  TriggerDictionaryInitialization_HiggsAnalysisCombinedLimit_xr_Impl();
}
