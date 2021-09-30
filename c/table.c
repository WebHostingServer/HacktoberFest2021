#include<stdio.h>
#include<conio.h>
void main(){
    int n,i;
    n = 2;
    while (n<=20)
    {
    i=1;
    printf("\n");
    while (i<=10)
    {
        printf("%5d", n*i);
        i++;
    }
    n++;
    }
}