#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct Array
{
    int A[10];
    int size;
    int length;
};

void Display(struct Array arr)
{
    for (int i = 0; i < arr.length; i++)
        printf("%d", arr.A[i]);
    printf("\n");
}


int binarySearch(struct Array arr, int key)
{
    int i, low, mid, high;
    low = 0;
    high = arr.length - 1;
    mid = floor((low + high) / 2);

    while (low <= high && arr.A[mid] != key)
    {
        if (key < arr.A[mid])
            high = mid - 1;
        else
            low = mid + 1;
        mid = floor((low + high) / 2);
    }

    if (arr.A[mid] == key)
        i = mid;
    else
        return -1;
    return i;
}

int main()
{
    struct Array arr = {{1, 2, 3, 4, 5, 6, 7, 8}, 10, 8};
    Display(arr);
    printf("%d", binarySearch(arr, 7));

    return 0;
}
