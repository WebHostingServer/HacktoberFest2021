#include <stdio.h>
int fabonacci(int number)
{
    if (number == 0)
    {
        return 0;
    }
    else if (number == 1)
    {
        return 1;
    }
    else
    {
        return fabonacci(number - 1) + fabonacci(number - 2);
    }
}

int main()
{
    int number, Fabonacci, i;
    printf("Enter the Number: ");
    scanf("%d", &number);
    for (i = 0; i < number; i++)
    {
        printf("%d\t\n",fabonacci(i));
    }
}