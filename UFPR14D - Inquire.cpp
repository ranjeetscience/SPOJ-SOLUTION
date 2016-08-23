'''Every tourist visiting our city must visit the May 4 avenue. There are N houses, numbered from 1 to N. There are Pi 
people living at house i.

The statistic institute is procedding with the survey this year. They will make many queries about the avenue's
population. For each query, two numbers A and B,
with A <= B, are given. You must determine the total number of people living in all houses from house A to house B, inclusive'''

 #include <bits/stdc++.h>
using namespace std;

int main() {
	//code
	long long int t;
	scanf("%lld",&t);
	long long int a[t],i,j,b[t+1];
	
	for(i=0;i<t;i++)
	scanf("%lld",&a[i]);
	b[0]=0;
	for(i=0;i<t;i++)
	    b[i+1]=b[i]+a[i];

	long long int n;
	scanf("%lld",&n);
	for(i=0;i<n;i++)
	{
	    long long int p,q;
	    scanf("%lld %lld",&p,&q);
	    printf("%lld\n",b[q]-b[p-1]);
	}
	return 0;
}
