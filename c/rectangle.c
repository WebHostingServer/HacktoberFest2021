#include <stdio.h>

int main(void)
{
    int t, a, b, c, d;
    scanf("%d", &t);
    for (int i = 0; i < t; i++)
    {
        scanf("%d %d %d %d", &a, &b, &c, &d);
        if ((a == c && b == d) || (a == b && c == d) || (a == d && b == c))
        {
            printf("YES\n");
        }
        else
            printf("NO\n");
    }

    return 0;
}
