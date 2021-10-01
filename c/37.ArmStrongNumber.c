#include <stdio.h>
#include <math.h>
int main()
{
    int CountForPower , sum, range, i, considerForNumber, digitToStore, digitPower,RangeDepletion,storedNumber;
    printf("Enter the Range: ");
    scanf("%d", &range);
    RangeDepletion=range;
    while (range != 0)
    {
        CountForPower++;
        range=range/10;
    }
    for (i = 1; i <= RangeDepletion; i++)
    {
        considerForNumber = i;
        storedNumber=i;

        while (considerForNumber != 0)
        {
            digitToStore = considerForNumber % 10;
            digitPower = pow(digitToStore, CountForPower);
            sum += digitPower;
            considerForNumber /= 10;
        }
        if (sum == storedNumber)
        {
            printf("%d", sum);
            printf(" ");
        }
        sum=0;
    }
}