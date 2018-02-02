#include <stdio.h>

int main()
{
    int a,b,k;
    scanf("%d\n%d %d",&k,&a,&b);
    printf((k>a && k<b)?"yes":"no");
    return 0;
}
