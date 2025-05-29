#ifndef _MYDLL_H
#define _MYDLL_H

#if defined(BUILD_DLL)
#    define DLL_EXP __declspec(dllexport)
#else
# if defined(BUILD_APP)
#    define DLL_EXP __declspec(dllimport)
# else
#    define DLL_EXP
# endif
#endif

#include <vector>
#include <string>

/*extern bool IsDllInit;
extern bool canhessian;
extern bool cangradient;
extern int dimension;
extern int functionCount;
extern std::vector <double> params;
extern std::vector <double> leftaxis;
extern std::vector <double> rightaxis;
extern std::vector <std::string> func_names;
extern std::vector < int > func1_params;
extern std::vector < int > func2_params;*/
//----------------------------------------------------------------------------
extern "C" int DLL_EXP getFunctionCount();
extern "C" int DLL_EXP getFuncParamsCount(int num);
extern "C" int DLL_EXP getDimension();
extern "C" double DLL_EXP getParamValue(int num);
extern "C" std::string DLL_EXP setParamValue(int num,double value);
extern "C" double DLL_EXP getLeftAxis(int num);
extern "C" std::string DLL_EXP setLeftAxis(int num,double value);
extern "C" double DLL_EXP getRightAxis(int num);
extern "C" std::string DLL_EXP setRightAxis(int num,double value);
extern "C" std::string DLL_EXP getFuncName(int num);
extern "C" void DLL_EXP getFuncParams(int num,std::vector<int>& vec);
//extern "C" bool DLL_EXP isObject();
extern "C" bool DLL_EXP canHessian();
extern "C" bool DLL_EXP canGradient();
extern "C" double DLL_EXP getValue(std::vector<double>&,int num);
extern "C" void DLL_EXP getGradient(std::vector<double>&,int num,std::vector<double> &);
extern "C" void DLL_EXP getHessian(std::vector<double>&,int num,std::vector< std::vector<double> >&);

extern "C" void DLL_EXP getAll(std::vector< std::string >& );
extern "C" void DLL_EXP InitDll();
#endif
