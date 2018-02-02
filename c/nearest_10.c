#include <stdio.h>
int main()
{
    int a;
    scanf("%d",&a);
    while(a%10 != 0) a++;
    printf("%d",a);
}
