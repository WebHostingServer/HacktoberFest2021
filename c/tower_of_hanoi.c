#include <stdio.h>
long long pow(long long a,long long b){
	long long ans=1;
	for(int i=0;i<b;i++)ans*=a;
	return ans;	
}
void hanoi(int n,int a,int b,int c){
	if(n==1)printf("%d %d\n",a,c);
	else{
		hanoi(n-1,a,c,b);
		printf("%d %d\n",a,c);
		hanoi(n-1,b,a,c);
	}
}
int main(){
	long long n;
	scanf("%lld",&n);
	printf("%lld\n",pow(2,n)-1);
	hanoi(n,1,2,3);
	return 0;
}