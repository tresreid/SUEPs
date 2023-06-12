// Do NOT change. Changes will be lost next time file is generated

#define R__DICTIONARY_FILENAME tmpdIslc7_amd64_gcc700dIsrcdICombineHarvesterdICombineToolsdIsrcdICombineHarvesterCombineToolsdIadICombineHarvesterCombineTools_xr

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
#include "src/CombineHarvester/CombineTools/src/classes.h"

// Header files passed via #pragma extra_include

namespace ROOT {
   static TClass *chcLcLObject_Dictionary();
   static void chcLcLObject_TClassManip(TClass*);
   static void *new_chcLcLObject(void *p = 0);
   static void *newArray_chcLcLObject(Long_t size, void *p);
   static void delete_chcLcLObject(void *p);
   static void deleteArray_chcLcLObject(void *p);
   static void destruct_chcLcLObject(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ch::Object*)
   {
      ::ch::Object *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::ch::Object));
      static ::ROOT::TGenericClassInfo 
         instance("ch::Object", "CombineHarvester/CombineTools/interface/Object.h", 8,
                  typeid(::ch::Object), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &chcLcLObject_Dictionary, isa_proxy, 4,
                  sizeof(::ch::Object) );
      instance.SetNew(&new_chcLcLObject);
      instance.SetNewArray(&newArray_chcLcLObject);
      instance.SetDelete(&delete_chcLcLObject);
      instance.SetDeleteArray(&deleteArray_chcLcLObject);
      instance.SetDestructor(&destruct_chcLcLObject);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ch::Object*)
   {
      return GenerateInitInstanceLocal((::ch::Object*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::ch::Object*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *chcLcLObject_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::ch::Object*)0x0)->GetClass();
      chcLcLObject_TClassManip(theClass);
   return theClass;
   }

   static void chcLcLObject_TClassManip(TClass* theClass){
      theClass->CreateAttributeMap();
      TDictAttributeMap* attrMap( theClass->GetAttributeMap() );
      attrMap->AddProperty("transient","true");
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *chcLcLProcess_Dictionary();
   static void chcLcLProcess_TClassManip(TClass*);
   static void *new_chcLcLProcess(void *p = 0);
   static void *newArray_chcLcLProcess(Long_t size, void *p);
   static void delete_chcLcLProcess(void *p);
   static void deleteArray_chcLcLProcess(void *p);
   static void destruct_chcLcLProcess(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ch::Process*)
   {
      ::ch::Process *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::ch::Process));
      static ::ROOT::TGenericClassInfo 
         instance("ch::Process", "CombineHarvester/CombineTools/interface/Process.h", 15,
                  typeid(::ch::Process), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &chcLcLProcess_Dictionary, isa_proxy, 4,
                  sizeof(::ch::Process) );
      instance.SetNew(&new_chcLcLProcess);
      instance.SetNewArray(&newArray_chcLcLProcess);
      instance.SetDelete(&delete_chcLcLProcess);
      instance.SetDeleteArray(&deleteArray_chcLcLProcess);
      instance.SetDestructor(&destruct_chcLcLProcess);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ch::Process*)
   {
      return GenerateInitInstanceLocal((::ch::Process*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::ch::Process*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *chcLcLProcess_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::ch::Process*)0x0)->GetClass();
      chcLcLProcess_TClassManip(theClass);
   return theClass;
   }

   static void chcLcLProcess_TClassManip(TClass* theClass){
      theClass->CreateAttributeMap();
      TDictAttributeMap* attrMap( theClass->GetAttributeMap() );
      attrMap->AddProperty("transient","true");
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *chcLcLSystematic_Dictionary();
   static void chcLcLSystematic_TClassManip(TClass*);
   static void *new_chcLcLSystematic(void *p = 0);
   static void *newArray_chcLcLSystematic(Long_t size, void *p);
   static void delete_chcLcLSystematic(void *p);
   static void deleteArray_chcLcLSystematic(void *p);
   static void destruct_chcLcLSystematic(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ch::Systematic*)
   {
      ::ch::Systematic *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::ch::Systematic));
      static ::ROOT::TGenericClassInfo 
         instance("ch::Systematic", "CombineHarvester/CombineTools/interface/Systematic.h", 12,
                  typeid(::ch::Systematic), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &chcLcLSystematic_Dictionary, isa_proxy, 4,
                  sizeof(::ch::Systematic) );
      instance.SetNew(&new_chcLcLSystematic);
      instance.SetNewArray(&newArray_chcLcLSystematic);
      instance.SetDelete(&delete_chcLcLSystematic);
      instance.SetDeleteArray(&deleteArray_chcLcLSystematic);
      instance.SetDestructor(&destruct_chcLcLSystematic);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ch::Systematic*)
   {
      return GenerateInitInstanceLocal((::ch::Systematic*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::ch::Systematic*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *chcLcLSystematic_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::ch::Systematic*)0x0)->GetClass();
      chcLcLSystematic_TClassManip(theClass);
   return theClass;
   }

   static void chcLcLSystematic_TClassManip(TClass* theClass){
      theClass->CreateAttributeMap();
      TDictAttributeMap* attrMap( theClass->GetAttributeMap() );
      attrMap->AddProperty("transient","true");
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *chcLcLParameter_Dictionary();
   static void chcLcLParameter_TClassManip(TClass*);
   static void *new_chcLcLParameter(void *p = 0);
   static void *newArray_chcLcLParameter(Long_t size, void *p);
   static void delete_chcLcLParameter(void *p);
   static void deleteArray_chcLcLParameter(void *p);
   static void destruct_chcLcLParameter(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ch::Parameter*)
   {
      ::ch::Parameter *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::ch::Parameter));
      static ::ROOT::TGenericClassInfo 
         instance("ch::Parameter", "CombineHarvester/CombineTools/interface/Parameter.h", 12,
                  typeid(::ch::Parameter), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &chcLcLParameter_Dictionary, isa_proxy, 4,
                  sizeof(::ch::Parameter) );
      instance.SetNew(&new_chcLcLParameter);
      instance.SetNewArray(&newArray_chcLcLParameter);
      instance.SetDelete(&delete_chcLcLParameter);
      instance.SetDeleteArray(&deleteArray_chcLcLParameter);
      instance.SetDestructor(&destruct_chcLcLParameter);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ch::Parameter*)
   {
      return GenerateInitInstanceLocal((::ch::Parameter*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::ch::Parameter*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *chcLcLParameter_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::ch::Parameter*)0x0)->GetClass();
      chcLcLParameter_TClassManip(theClass);
   return theClass;
   }

   static void chcLcLParameter_TClassManip(TClass* theClass){
      theClass->CreateAttributeMap();
      TDictAttributeMap* attrMap( theClass->GetAttributeMap() );
      attrMap->AddProperty("transient","true");
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *chcLcLObservation_Dictionary();
   static void chcLcLObservation_TClassManip(TClass*);
   static void *new_chcLcLObservation(void *p = 0);
   static void *newArray_chcLcLObservation(Long_t size, void *p);
   static void delete_chcLcLObservation(void *p);
   static void deleteArray_chcLcLObservation(void *p);
   static void destruct_chcLcLObservation(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ch::Observation*)
   {
      ::ch::Observation *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::ch::Observation));
      static ::ROOT::TGenericClassInfo 
         instance("ch::Observation", "CombineHarvester/CombineTools/interface/Observation.h", 12,
                  typeid(::ch::Observation), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &chcLcLObservation_Dictionary, isa_proxy, 4,
                  sizeof(::ch::Observation) );
      instance.SetNew(&new_chcLcLObservation);
      instance.SetNewArray(&newArray_chcLcLObservation);
      instance.SetDelete(&delete_chcLcLObservation);
      instance.SetDeleteArray(&deleteArray_chcLcLObservation);
      instance.SetDestructor(&destruct_chcLcLObservation);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ch::Observation*)
   {
      return GenerateInitInstanceLocal((::ch::Observation*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::ch::Observation*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *chcLcLObservation_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::ch::Observation*)0x0)->GetClass();
      chcLcLObservation_TClassManip(theClass);
   return theClass;
   }

   static void chcLcLObservation_TClassManip(TClass* theClass){
      theClass->CreateAttributeMap();
      TDictAttributeMap* attrMap( theClass->GetAttributeMap() );
      attrMap->AddProperty("transient","true");
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *chcLcLCombineHarvester_Dictionary();
   static void chcLcLCombineHarvester_TClassManip(TClass*);
   static void *new_chcLcLCombineHarvester(void *p = 0);
   static void *newArray_chcLcLCombineHarvester(Long_t size, void *p);
   static void delete_chcLcLCombineHarvester(void *p);
   static void deleteArray_chcLcLCombineHarvester(void *p);
   static void destruct_chcLcLCombineHarvester(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ch::CombineHarvester*)
   {
      ::ch::CombineHarvester *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::ch::CombineHarvester));
      static ::ROOT::TGenericClassInfo 
         instance("ch::CombineHarvester", "CombineHarvester/CombineTools/interface/CombineHarvester.h", 30,
                  typeid(::ch::CombineHarvester), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &chcLcLCombineHarvester_Dictionary, isa_proxy, 4,
                  sizeof(::ch::CombineHarvester) );
      instance.SetNew(&new_chcLcLCombineHarvester);
      instance.SetNewArray(&newArray_chcLcLCombineHarvester);
      instance.SetDelete(&delete_chcLcLCombineHarvester);
      instance.SetDeleteArray(&deleteArray_chcLcLCombineHarvester);
      instance.SetDestructor(&destruct_chcLcLCombineHarvester);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ch::CombineHarvester*)
   {
      return GenerateInitInstanceLocal((::ch::CombineHarvester*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::ch::CombineHarvester*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *chcLcLCombineHarvester_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::ch::CombineHarvester*)0x0)->GetClass();
      chcLcLCombineHarvester_TClassManip(theClass);
   return theClass;
   }

   static void chcLcLCombineHarvester_TClassManip(TClass* theClass){
      theClass->CreateAttributeMap();
      TDictAttributeMap* attrMap( theClass->GetAttributeMap() );
      attrMap->AddProperty("transient","true");
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *chcLcLCardWriter_Dictionary();
   static void chcLcLCardWriter_TClassManip(TClass*);
   static void delete_chcLcLCardWriter(void *p);
   static void deleteArray_chcLcLCardWriter(void *p);
   static void destruct_chcLcLCardWriter(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ch::CardWriter*)
   {
      ::ch::CardWriter *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::ch::CardWriter));
      static ::ROOT::TGenericClassInfo 
         instance("ch::CardWriter", "CombineHarvester/CombineTools/interface/CardWriter.h", 50,
                  typeid(::ch::CardWriter), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &chcLcLCardWriter_Dictionary, isa_proxy, 4,
                  sizeof(::ch::CardWriter) );
      instance.SetDelete(&delete_chcLcLCardWriter);
      instance.SetDeleteArray(&deleteArray_chcLcLCardWriter);
      instance.SetDestructor(&destruct_chcLcLCardWriter);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ch::CardWriter*)
   {
      return GenerateInitInstanceLocal((::ch::CardWriter*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::ch::CardWriter*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *chcLcLCardWriter_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::ch::CardWriter*)0x0)->GetClass();
      chcLcLCardWriter_TClassManip(theClass);
   return theClass;
   }

   static void chcLcLCardWriter_TClassManip(TClass* theClass){
      theClass->CreateAttributeMap();
      TDictAttributeMap* attrMap( theClass->GetAttributeMap() );
      attrMap->AddProperty("transient","true");
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *chcLcLBinByBinFactory_Dictionary();
   static void chcLcLBinByBinFactory_TClassManip(TClass*);
   static void *new_chcLcLBinByBinFactory(void *p = 0);
   static void *newArray_chcLcLBinByBinFactory(Long_t size, void *p);
   static void delete_chcLcLBinByBinFactory(void *p);
   static void deleteArray_chcLcLBinByBinFactory(void *p);
   static void destruct_chcLcLBinByBinFactory(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ch::BinByBinFactory*)
   {
      ::ch::BinByBinFactory *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::ch::BinByBinFactory));
      static ::ROOT::TGenericClassInfo 
         instance("ch::BinByBinFactory", "CombineHarvester/CombineTools/interface/BinByBin.h", 21,
                  typeid(::ch::BinByBinFactory), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &chcLcLBinByBinFactory_Dictionary, isa_proxy, 4,
                  sizeof(::ch::BinByBinFactory) );
      instance.SetNew(&new_chcLcLBinByBinFactory);
      instance.SetNewArray(&newArray_chcLcLBinByBinFactory);
      instance.SetDelete(&delete_chcLcLBinByBinFactory);
      instance.SetDeleteArray(&deleteArray_chcLcLBinByBinFactory);
      instance.SetDestructor(&destruct_chcLcLBinByBinFactory);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ch::BinByBinFactory*)
   {
      return GenerateInitInstanceLocal((::ch::BinByBinFactory*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::ch::BinByBinFactory*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *chcLcLBinByBinFactory_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::ch::BinByBinFactory*)0x0)->GetClass();
      chcLcLBinByBinFactory_TClassManip(theClass);
   return theClass;
   }

   static void chcLcLBinByBinFactory_TClassManip(TClass* theClass){
      theClass->CreateAttributeMap();
      TDictAttributeMap* attrMap( theClass->GetAttributeMap() );
      attrMap->AddProperty("transient","true");
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *chcLcLAutoRebin_Dictionary();
   static void chcLcLAutoRebin_TClassManip(TClass*);
   static void *new_chcLcLAutoRebin(void *p = 0);
   static void *newArray_chcLcLAutoRebin(Long_t size, void *p);
   static void delete_chcLcLAutoRebin(void *p);
   static void deleteArray_chcLcLAutoRebin(void *p);
   static void destruct_chcLcLAutoRebin(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ch::AutoRebin*)
   {
      ::ch::AutoRebin *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::ch::AutoRebin));
      static ::ROOT::TGenericClassInfo 
         instance("ch::AutoRebin", "CombineHarvester/CombineTools/interface/AutoRebin.h", 19,
                  typeid(::ch::AutoRebin), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &chcLcLAutoRebin_Dictionary, isa_proxy, 4,
                  sizeof(::ch::AutoRebin) );
      instance.SetNew(&new_chcLcLAutoRebin);
      instance.SetNewArray(&newArray_chcLcLAutoRebin);
      instance.SetDelete(&delete_chcLcLAutoRebin);
      instance.SetDeleteArray(&deleteArray_chcLcLAutoRebin);
      instance.SetDestructor(&destruct_chcLcLAutoRebin);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ch::AutoRebin*)
   {
      return GenerateInitInstanceLocal((::ch::AutoRebin*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::ch::AutoRebin*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *chcLcLAutoRebin_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::ch::AutoRebin*)0x0)->GetClass();
      chcLcLAutoRebin_TClassManip(theClass);
   return theClass;
   }

   static void chcLcLAutoRebin_TClassManip(TClass* theClass){
      theClass->CreateAttributeMap();
      TDictAttributeMap* attrMap( theClass->GetAttributeMap() );
      attrMap->AddProperty("transient","true");
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_chcLcLObject(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::ch::Object : new ::ch::Object;
   }
   static void *newArray_chcLcLObject(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::ch::Object[nElements] : new ::ch::Object[nElements];
   }
   // Wrapper around operator delete
   static void delete_chcLcLObject(void *p) {
      delete ((::ch::Object*)p);
   }
   static void deleteArray_chcLcLObject(void *p) {
      delete [] ((::ch::Object*)p);
   }
   static void destruct_chcLcLObject(void *p) {
      typedef ::ch::Object current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::ch::Object

namespace ROOT {
   // Wrappers around operator new
   static void *new_chcLcLProcess(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::ch::Process : new ::ch::Process;
   }
   static void *newArray_chcLcLProcess(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::ch::Process[nElements] : new ::ch::Process[nElements];
   }
   // Wrapper around operator delete
   static void delete_chcLcLProcess(void *p) {
      delete ((::ch::Process*)p);
   }
   static void deleteArray_chcLcLProcess(void *p) {
      delete [] ((::ch::Process*)p);
   }
   static void destruct_chcLcLProcess(void *p) {
      typedef ::ch::Process current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::ch::Process

namespace ROOT {
   // Wrappers around operator new
   static void *new_chcLcLSystematic(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::ch::Systematic : new ::ch::Systematic;
   }
   static void *newArray_chcLcLSystematic(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::ch::Systematic[nElements] : new ::ch::Systematic[nElements];
   }
   // Wrapper around operator delete
   static void delete_chcLcLSystematic(void *p) {
      delete ((::ch::Systematic*)p);
   }
   static void deleteArray_chcLcLSystematic(void *p) {
      delete [] ((::ch::Systematic*)p);
   }
   static void destruct_chcLcLSystematic(void *p) {
      typedef ::ch::Systematic current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::ch::Systematic

namespace ROOT {
   // Wrappers around operator new
   static void *new_chcLcLParameter(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::ch::Parameter : new ::ch::Parameter;
   }
   static void *newArray_chcLcLParameter(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::ch::Parameter[nElements] : new ::ch::Parameter[nElements];
   }
   // Wrapper around operator delete
   static void delete_chcLcLParameter(void *p) {
      delete ((::ch::Parameter*)p);
   }
   static void deleteArray_chcLcLParameter(void *p) {
      delete [] ((::ch::Parameter*)p);
   }
   static void destruct_chcLcLParameter(void *p) {
      typedef ::ch::Parameter current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::ch::Parameter

namespace ROOT {
   // Wrappers around operator new
   static void *new_chcLcLObservation(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::ch::Observation : new ::ch::Observation;
   }
   static void *newArray_chcLcLObservation(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::ch::Observation[nElements] : new ::ch::Observation[nElements];
   }
   // Wrapper around operator delete
   static void delete_chcLcLObservation(void *p) {
      delete ((::ch::Observation*)p);
   }
   static void deleteArray_chcLcLObservation(void *p) {
      delete [] ((::ch::Observation*)p);
   }
   static void destruct_chcLcLObservation(void *p) {
      typedef ::ch::Observation current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::ch::Observation

namespace ROOT {
   // Wrappers around operator new
   static void *new_chcLcLCombineHarvester(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::ch::CombineHarvester : new ::ch::CombineHarvester;
   }
   static void *newArray_chcLcLCombineHarvester(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::ch::CombineHarvester[nElements] : new ::ch::CombineHarvester[nElements];
   }
   // Wrapper around operator delete
   static void delete_chcLcLCombineHarvester(void *p) {
      delete ((::ch::CombineHarvester*)p);
   }
   static void deleteArray_chcLcLCombineHarvester(void *p) {
      delete [] ((::ch::CombineHarvester*)p);
   }
   static void destruct_chcLcLCombineHarvester(void *p) {
      typedef ::ch::CombineHarvester current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::ch::CombineHarvester

namespace ROOT {
   // Wrapper around operator delete
   static void delete_chcLcLCardWriter(void *p) {
      delete ((::ch::CardWriter*)p);
   }
   static void deleteArray_chcLcLCardWriter(void *p) {
      delete [] ((::ch::CardWriter*)p);
   }
   static void destruct_chcLcLCardWriter(void *p) {
      typedef ::ch::CardWriter current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::ch::CardWriter

namespace ROOT {
   // Wrappers around operator new
   static void *new_chcLcLBinByBinFactory(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::ch::BinByBinFactory : new ::ch::BinByBinFactory;
   }
   static void *newArray_chcLcLBinByBinFactory(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::ch::BinByBinFactory[nElements] : new ::ch::BinByBinFactory[nElements];
   }
   // Wrapper around operator delete
   static void delete_chcLcLBinByBinFactory(void *p) {
      delete ((::ch::BinByBinFactory*)p);
   }
   static void deleteArray_chcLcLBinByBinFactory(void *p) {
      delete [] ((::ch::BinByBinFactory*)p);
   }
   static void destruct_chcLcLBinByBinFactory(void *p) {
      typedef ::ch::BinByBinFactory current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::ch::BinByBinFactory

namespace ROOT {
   // Wrappers around operator new
   static void *new_chcLcLAutoRebin(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::ch::AutoRebin : new ::ch::AutoRebin;
   }
   static void *newArray_chcLcLAutoRebin(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::ch::AutoRebin[nElements] : new ::ch::AutoRebin[nElements];
   }
   // Wrapper around operator delete
   static void delete_chcLcLAutoRebin(void *p) {
      delete ((::ch::AutoRebin*)p);
   }
   static void deleteArray_chcLcLAutoRebin(void *p) {
      delete [] ((::ch::AutoRebin*)p);
   }
   static void destruct_chcLcLAutoRebin(void *p) {
      typedef ::ch::AutoRebin current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::ch::AutoRebin

namespace {
  void TriggerDictionaryInitialization_CombineHarvesterCombineTools_xr_Impl() {
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
#line 1 "CombineHarvesterCombineTools_xr dictionary forward declarations' payload"
#pragma clang diagnostic ignored "-Wkeyword-compat"
#pragma clang diagnostic ignored "-Wignored-attributes"
#pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
extern int __Cling_Autoloading_Map;
namespace ch{class __attribute__((annotate(R"ATTRDUMP(transient@@@true)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$CombineHarvester/CombineTools/interface/Object.h")))  __attribute__((annotate("$clingAutoload$CombineHarvester/CombineTools/interface/CombineHarvester.h")))  Object;}
namespace ch{class __attribute__((annotate(R"ATTRDUMP(transient@@@true)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$CombineHarvester/CombineTools/interface/Process.h")))  __attribute__((annotate("$clingAutoload$CombineHarvester/CombineTools/interface/CombineHarvester.h")))  Process;}
namespace ch{class __attribute__((annotate(R"ATTRDUMP(transient@@@true)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$CombineHarvester/CombineTools/interface/Systematic.h")))  __attribute__((annotate("$clingAutoload$CombineHarvester/CombineTools/interface/CombineHarvester.h")))  Systematic;}
namespace ch{class __attribute__((annotate(R"ATTRDUMP(transient@@@true)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$CombineHarvester/CombineTools/interface/Parameter.h")))  __attribute__((annotate("$clingAutoload$CombineHarvester/CombineTools/interface/CombineHarvester.h")))  Parameter;}
namespace ch{class __attribute__((annotate(R"ATTRDUMP(transient@@@true)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$CombineHarvester/CombineTools/interface/Observation.h")))  __attribute__((annotate("$clingAutoload$CombineHarvester/CombineTools/interface/CombineHarvester.h")))  Observation;}
namespace ch{class __attribute__((annotate(R"ATTRDUMP(transient@@@true)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$CombineHarvester/CombineTools/interface/CombineHarvester.h")))  CombineHarvester;}
namespace ch{class __attribute__((annotate(R"ATTRDUMP(transient@@@true)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$CombineHarvester/CombineTools/interface/CardWriter.h")))  CardWriter;}
namespace ch{class __attribute__((annotate(R"ATTRDUMP(transient@@@true)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$CombineHarvester/CombineTools/interface/BinByBin.h")))  BinByBinFactory;}
namespace ch{class __attribute__((annotate(R"ATTRDUMP(transient@@@true)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$CombineHarvester/CombineTools/interface/AutoRebin.h")))  AutoRebin;}
)DICTFWDDCLS";
    static const char* payloadCode = R"DICTPAYLOAD(
#line 1 "CombineHarvesterCombineTools_xr dictionary payload"

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
#include "CombineHarvester/CombineTools/interface/CombineHarvester.h"
#include "CombineHarvester/CombineTools/interface/Observation.h"
#include "CombineHarvester/CombineTools/interface/Parameter.h"
#include "CombineHarvester/CombineTools/interface/CardWriter.h"
#include "CombineHarvester/CombineTools/interface/BinByBin.h"
#include "CombineHarvester/CombineTools/interface/AutoRebin.h"
#include "CombineHarvester/CombineTools/interface/CopyTools.h"
#include "CombineHarvester/CombineTools/interface/Utilities.h"
#include "CombineHarvester/CombineTools/interface/ValidationToolsNoJSON.h"
#include "CombineHarvester/CombineTools/interface/ParseCombineWorkspace.h"

#undef  _BACKWARD_BACKWARD_WARNING_H
)DICTPAYLOAD";
    static const char* classesHeaders[]={
"ch::AutoRebin", payloadCode, "@",
"ch::BinByBinFactory", payloadCode, "@",
"ch::CardWriter", payloadCode, "@",
"ch::CheckEmptyBins", payloadCode, "@",
"ch::CheckEmptyShapes", payloadCode, "@",
"ch::CheckNormEff", payloadCode, "@",
"ch::CheckSizeOfShapeEffect", payloadCode, "@",
"ch::CheckSmallSignals", payloadCode, "@",
"ch::CombineHarvester", payloadCode, "@",
"ch::MassesFromRange", payloadCode, "@",
"ch::Object", payloadCode, "@",
"ch::Observation", payloadCode, "@",
"ch::Parameter", payloadCode, "@",
"ch::ParseCombineWorkspace", payloadCode, "@",
"ch::PrintSystematic", payloadCode, "@",
"ch::Process", payloadCode, "@",
"ch::SetStandardBinNames", payloadCode, "@",
"ch::SplitSyst", payloadCode, "@",
"ch::Systematic", payloadCode, "@",
"ch::TGraphFromTable", payloadCode, "@",
"ch::ValidateCards", payloadCode, "@",
"ch::ValidateShapeTemplates", payloadCode, "@",
"ch::ValidateShapeUncertaintyDirection", payloadCode, "@",
"ch::ValsFromRange", payloadCode, "@",
nullptr};

    static bool isInitialized = false;
    if (!isInitialized) {
      TROOT::RegisterModule("CombineHarvesterCombineTools_xr",
        headers, includePaths, payloadCode, fwdDeclCode,
        TriggerDictionaryInitialization_CombineHarvesterCombineTools_xr_Impl, {}, classesHeaders);
      isInitialized = true;
    }
  }
  static struct DictInit {
    DictInit() {
      TriggerDictionaryInitialization_CombineHarvesterCombineTools_xr_Impl();
    }
  } __TheDictionaryInitializer;
}
void TriggerDictionaryInitialization_CombineHarvesterCombineTools_xr() {
  TriggerDictionaryInitialization_CombineHarvesterCombineTools_xr_Impl();
}
