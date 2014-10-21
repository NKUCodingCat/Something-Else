#include <iostream>
#include<string> 

using namespace std;
int main()
{
	//char str1[] = "I do not like green eggs and ham";
	//char str2[] = "I do not like them Sam I am";
	string st1 = "I do not like green eggs and ham";
	string st2 = "I do not like them Sam I am";
	if (st1.size() <2  || (st2.size()<2)){cout<<"×Ö·û´®Ì«¶Ì";return 0;}
	char **p1 = new char * [st1.size()-1];
	char **p2 = new char * [st1.size()-1];
	//·Ö¸î×Ö·û´®
	for(int i = 0;i<st1.size()-1;i++)
	{
		p1[i] = new char [3];
		p1[i][0] = st1.at(i);
		p1[i][1] = st1.at(i+1);
		p1[i][2] = '\0';
	}
	for(int j = 0;j<st2.size()-1;j++)
	{
		p2[j] = new char [3];
		p2[j][0] = st2.at(j);
		p2[j][1] = st2.at(j+1);
		p2[j][2] = '\0';
	}
	char *tmp;
	//È¥ÖØ
	for(int m = 0;m<st1.size() - 1;m++)
	{
		for(int n = m+1;n<st1.size() - 1;n++)
		{
			if ((p1[n] == NULL)||(p1[m] == NULL))
			{
				continue;
			}
			if ((p1[m][0] == p1[n][0]) && (p1[m][1] == p1[n][1]))
			{
				tmp = p1[n];
				p1[n] = NULL;
				delete []tmp;
			}
		}
	}
	for( m = 0;m<st2.size() - 1;m++)
	{
		for(int n = m+1;n<st2.size() - 1;n++)
		{
			if ((p2[n] == NULL)||(p2[m] == NULL))
			{
				continue;
			}
			if ((p2[m][0] == p2[n][0]) && (p2[m][1] == p2[n][1]))
			{
				tmp = p2[n];
				p2[n] = NULL;
				delete []tmp;
			}
		}
	}
	int len = (st1.size()>st2.size())?st1.size():st2.size();
	char **pc = new char * [len-1];
	char **ps = new char * [st1.size()+st2.size()];
	int C = 0;
	int S = 0;
	// =init=
	for(int o = 0;o<len-1;o++)
	{
		pc[o] = NULL;
	}
	for(int p = 0;p<st1.size()+st2.size();p++)
	{
		ps[p] = NULL;
	}
	// find cross
	for(int q = 0;q < st1.size()-1;q++)
	{
		if (p1[q] == NULL)continue;
		for (int r = 0; r< st2.size()-1;r++)
		{
			if (p2[r] == NULL)continue;
			if ((p1[q][0] == p2[r][0]) && (p1[q][1] == p2[r][1]))
			{
				pc[C] = new char [3];
				pc[C][0] = p1[q][0];
				pc[C][1] = p1[q][1];
				pc[C][2] = '\0';
				C++;
			}
		}
	}
	for( i = 0;i<st1.size()-1;i++)
	{
		if (p1[i]==NULL)continue;
		ps[i] = new char [3];
		ps[i][0] = p1[i][0];
		ps[i][1] = p1[i][1];
		ps[i][2] = '\0';
	}
	int k = 0;
	for(j = 0;j<st2.size()-1;j++)
	{
		if (p2[j]==NULL)continue;
		k = j + st1.size();
		ps[k] = new char [3];
		ps[k][0] = p2[j][0];
		ps[k][1] = p2[j][1];
		ps[k][2] = '\0';
	}
	for( m = 0;m<st1.size()+st2.size();m++)
	{
		for(int n = m+1;n<st1.size()+st2.size();n++)
		{
			if ((ps[n] == NULL)||(ps[m] == NULL))
			{
				continue;
			}
			if ((ps[m][0] == ps[n][0]) && (ps[m][1] == ps[n][1]))
			{
				tmp = ps[n];
				ps[n] = NULL;
				delete []tmp;
			}
		}
	}
	for( m = 0;m<st1.size()+st2.size();m++)
	{
		if(ps[m]!=NULL)
		{
			S++;
		}
	}
	cout<<float(C)/float(S);
	//==========»ØÊÕÄÚ´æ=======
	for( j = 0;j<st2.size()-1;j++)
	{
		delete p2[j];
	}
	delete []p2;
	for(j = 0;j<st1.size()-1;j++)
	{
		delete []p1[j];
	}
	delete []p1;
	for( j = 0;j<len-1;j++)
	{
		delete []pc[j];
	}
	delete []pc;
	for(j = 0;j<st1.size()+st2.size();j++)
	{
		delete []ps[j];
	}
	delete []ps;
	return 0;
}
