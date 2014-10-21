#include <iostream>
#include<string> 
#include <set>  
#include <algorithm>
using namespace std;

double getJac(const char*str1, const char*str2, int step) {  
	string s1 = str1;  
	string s2 = str2;  
	int m = strlen(str1);  
	int n = strlen(str2);  
	set<string> S;  
	set<string> T;  
	for(int i=0; i<=m-step; i++) {  
		string tmp = s1.substr(i, step);  
		S.insert(tmp);  
	}  
	for(int i=0; i<=n-step; i++) {  
		string tmp = s2.substr(i, step);  
		T.insert(tmp);  
	}  
	int commonNum = 0;  
	set<string>::iterator iter1;  
	for(iter1=S.begin();iter1!=S.end();iter1++) {  
		int isIn = T.count(*iter1);  
		commonNum += isIn;        
	}  
	int mergeNum =S.size()+T.size()-commonNum;  
	return double(commonNum)/mergeNum;  
}  
int main()
{
	char str1[] = "I do not like green eggs and ham";
	char str2[] = "I do not like them Sam I am";
	cout<<getJac(str1,str2,2);
}
