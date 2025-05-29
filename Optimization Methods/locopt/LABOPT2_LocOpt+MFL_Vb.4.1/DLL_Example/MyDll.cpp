//---------------------------------------------------------------------------

#include <vcl.h>
#include <windows.h>
#pragma hdrstop
//---------------------------------------------------------------------------
//   Important note about DLL memory management when your DLL uses the
//   static version of the RunTime Library:
//
//   If your DLL exports any functions that pass String objects (or structs/
//   classes containing nested Strings) as parameter or function results,
//   you will need to add the library MEMMGR.LIB to both the DLL project and
//   any other projects that use the DLL.  You will also need to use MEMMGR.LIB
//   if any other projects which use the DLL will be performing new or delete
//   operations on any non-TObject-derived classes which are exported from the
//   DLL. Adding MEMMGR.LIB to your project will change the DLL and its calling
//   EXE's to use the BORLNDMM.DLL as their memory manager.  In these cases,
//   the file BORLNDMM.DLL should be deployed along with your DLL.
//
//   To avoid using BORLNDMM.DLL, pass string information using "char *" or
//   ShortString parameters.
//
//   If your DLL uses the dynamic version of the RTL, you do not need to
//   explicitly add MEMMGR.LIB as this will be done implicitly for you
//---------------------------------------------------------------------------

#pragma argsused

#define BUILD_DLL
#include "MyDll.h"

int WINAPI DllEntryPoint(HINSTANCE hinst, unsigned long reason, void* lpReserved)
{
        return 1;
}
//---------------------------------------------------------------------------

bool IsDllInit=false;
std::vector <double> leftaxis(2);
std::vector <double> rightaxis(2);
std::vector <double> params(3);
std::vector <std::string> func_names(2);
std::vector < int > func1_params(2);
std::vector < int > func2_params(3);
//---------------------------------------------------------------------------
int functionCount=2;
int dimension=2;
bool canhessian=true;
bool cangradient=true;
//----------------------------------------------------------------------------
int getFunctionCount()
{
 return functionCount;
}
//----------------------------------------------------------------------------
int getFuncParamsCount(int num)
{
 switch(num)
 {
  case 0: return func1_params.size();
          break;
  case 1: return func2_params.size();
          break;
  default: return 0;
           break;
 }
}
//----------------------------------------------------------------------------
int getDimension()
{
 return dimension;
}
//----------------------------------------------------------------------------
double getParamValue(int num)
{
 if(params.size()>0)
  if(num<0)
   return params[0];
  else
   if(num>=params.size())
    return params[params.size()-1];
   else
    return params[num];
 else
  return 0;
}
//----------------------------------------------------------------------------
std::string setParamValue(int num,double value)
{
 if((num>=0)&&(num<params.size()))
  params[num]=value;
 return std::string("NO");
}
//----------------------------------------------------------------------------
std::string setLeftAxis(int num,double value)
{
 if((num>=0)&&(num<leftaxis.size()))
  leftaxis[num]=value;
 return std::string("NO");
}
//----------------------------------------------------------------------------
std::string setRightAxis(int num,double value)
{
 if((num>=0)&&(num<rightaxis.size()))
  rightaxis[num]=value;
 return std::string("NO");
}
//----------------------------------------------------------------------------
double getLeftAxis(int num)
{
 if(leftaxis.size()>0)
  if(num<0)
   return leftaxis[0];
  else
   if(num>=leftaxis.size())
    return leftaxis[leftaxis.size()-1];
   else
    return leftaxis[num];
 else
  return 0;
}
//----------------------------------------------------------------------------
double getRightAxis(int num)
{
 if(rightaxis.size()>0)
  if(num<0)
   return rightaxis[0];
  else
   if(num>=rightaxis.size())
    return rightaxis[rightaxis.size()-1];
   else
    return rightaxis[num];
 else
  return 0;
}
//----------------------------------------------------------------------------
std::string getFuncName(int num)
{
 if(func_names.size()>0)
  if(num<0)
   return func_names[0];
  else
   if(num>=func_names.size())
    return func_names[func_names.size()-1];
   else
    return func_names[num];
 else
  return std::string("");
}
//----------------------------------------------------------------------------
void  getFuncParams(int num,std::vector<int>& vec)
{
 switch(num)
 {
  case 0: if(vec.size()==func1_params.size())
           for(int i=0; i<func1_params.size();i++)
            vec[i]=func1_params[i];
          break;
  case 1: if(vec.size()==func2_params.size())
           for(int i=0; i<func2_params.size();i++)
            vec[i]=func2_params[i];
          break;
  default: if(vec.size()==func1_params.size())
           for(int i=0; i<func1_params.size();i++)
            vec[i]=func1_params[i];
 }
}
//----------------------------------------------------------------------------
bool canHessian()
{ return canhessian; }
bool canGradient()
{ return cangradient; }
//----------------------------------------------------------------------------
double getValue(std::vector<double>& v,int num)
{
 if((num>=0)&&(num<functionCount)&&(v.size()>=dimension))
  switch (num)
  {
   case 0: return (params[0]*v[0]*v[0]+params[2]*v[1]);
   case 1: return (params[0]*v[0]*v[0]+params[1]*v[1]+params[2]*v[0]*v[1]);
   default: return 100;
  }
 else
  return 0;
}
void getGradient(std::vector<double>& v,int num,std::vector<double> &gradient)
{
 if((num>=0)&&(num<functionCount)&&(v.size()>=dimension)&&(gradient.size()>=dimension))
  switch (num)
  {
   case 0: gradient[0]=2*params[0]*v[0]; gradient[1]=params[2]; break;
   case 1: gradient[0]=2*params[0]*v[0]+params[2]*v[1]; gradient[1]=params[1]+params[2]*v[0];  break;
  }
}
void DLL_EXP getHessian(std::vector<double>& point,int num,std::vector< std::vector<double> >& res)
{
 if((num>=0)&&(num<functionCount)&&(point.size()>=dimension))
  switch (num)
  {
   case 0: res[0][0]=2*params[0]; res[0][1]=0; res[1][0]=0; res[1][1]=0; break;
   case 1: res[0][0]=2*params[0]; res[0][1]=params[2]; res[1][0]=params[2]; res[1][1]=0; break;
  }
}
//------------------------------------------------------------------------------
void getAll(std::vector< std::string >& vector)
{
 vector.resize(func_names.size());
 for(int i=0; i<func_names.size(); i++)
  vector[i]=func_names[i];
}

void InitDll()
{
 if(IsDllInit)
  return;

 IsDllInit=true;

 params[0]=1;
 params[1]=5;
 params[2]=10;

 leftaxis[0]=-1;//.push_back(-1);
 leftaxis[1]=-1;//.push_back(-1);

 rightaxis[0]=1;//.push_back(1);
 rightaxis[1]=1;//.push_back(1);

 func_names[0]=(std::string("a1*x1^2+a2*x2"));
 func_names[1]=(std::string("a1*x1^2+a2*x2+a3*x1*x2"));

 func1_params[0]=0;
 func1_params[1]=2;
 func2_params[0]=0;
 func2_params[1]=1;
 func2_params[2]=2;
}


