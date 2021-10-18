#include<stdio.h>
#include<conio.h>
#include<bits/stdc++.h>
void main(){
    int i,n,t;
    printf("Enter Target Value \n");
    scanf("%d",&t);
    for(n=1;n<=t;n++){
        for(i=n;i>0;i--){
            printf("%2d",i);
        }
        printf("\n");
    }
}
