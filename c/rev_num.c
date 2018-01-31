#include <stdio.h>
#include<string.h>
int main()
{
    int n,t=0,rm;
    scanf("%d",&n);
    while(n>0){
        rm = n%10;
        t = t * 10 + rm;
        n /= 10;
    }
    printf("%d",t);
    return 0;
}
