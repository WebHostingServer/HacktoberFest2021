#include<stdio.h>
#include<conio.h>
#include<ctype.h>
#include<string.h>
int MAX=100;
float st[100];
int top=-1;
void push(float st[],int val);
float pop(float st[]);
int Evaluate(char exp[]);
int main()
{
	char exp[100];
	int value;
	printf("\n Enter the postfix expression\n");
	gets(exp);
	value=Evaluate(exp);
	printf("The value of the postfix expression is %d",value);
	getch();
	return 0;
}
int Evaluate(char exp[])
{
	int i=0,op1,op2,val;
	while(exp[i]!='\0')
	{
		if(isdigit(exp[i]))
		{
			push(st,(exp[i]-'0'));
		}
		else
		{
			op2=pop(st);
			op1=pop(st);
			switch(exp[i])
			{
				case'+':
					val=op1+op2;
					break;
				case'-':
					val=op1-op2;
					break;
				case'*':
					val=op1*op2;
					break;
				case'%':
					val=(int)op1%(int)op2;
					break;
			}
			push(st,val);	
		}
		i++;		
	}
	return(pop(st));
}
void push(float st[],int val)
{
	if(top==MAX-1)
	{
		printf("Stack Overflow");
	}
	else
	{
		top++;
		st[top]=val;
	}
}
float pop(float st[])
{
	float value=-1;
	if(top==-1)
	{
		printf("Stack is empty");
	}
	else
	{
		value=st[top];
		top--;
	}
	return(value);
}
