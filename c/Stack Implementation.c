#include<stdio.h>
#define SIZE 5
int stack[SIZE];
top=-1;

int isFull()
{
    if(top==SIZE-1)
    {
        printf("True\n");
        return 1;
    }
    else
    {
        printf("False\n");
        return 0;
    }
}

int isEmpty()
{
    if(top==-1)
    {
        printf("True\n");
        return 1;
    }
    else
    {
        printf("False\n");
        return 0;
    }
}


int push()
{
    int x;
    printf("Enter element to be pushed in stack\n");
    scanf("%d",&x);
    if(top==SIZE-1)
    {
        printf("Overflow\n");
    }
    else
    {
        top++;
        stack[top]=x;
    }
}

int pop()
{
    if(top==-1)
    {
        printf("Underflow\n");
    }
    else
    {
        printf("Popped element is %d\n",stack[top]);
        top--;
    }
}
int display()
{
    if(top==-1)
    {
        printf("Stack is empty\n");
    }
    else
    {
        for(int i=top;i>=0;i--)
        {
            printf("%d ",stack[i]);
        }
        printf("\n");
    }
}

int peek()
{
    if(top==-1)
    {
        printf("Stack is empty\n");
    }
    else
    {
        printf("%d\n",stack[top]);
    }
}

void main()
{
    int choice;

    while(1)
    {
    printf("Enter your choice:\n");
    printf("\n 1.Push\n 2.Pop\n 3.Peek\n 4.Display\n 5.Isfull\n 6.Isempty\n 7.exit\n");
    scanf("%d",&choice);

    switch(choice)
    {
    case 1:
        push();
        break;
    case 2:
        pop();
        break;
    case 3:
        peek();
        break;
    case 4:
        display();
        break;
    case 5:
        isFull();
        break;
    case 6:
        isEmpty();
        break;
    case 7:
        exit(0);
    default:
        printf("Invalid choice\n");
        break;
    }

    }
}
