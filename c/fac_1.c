#include <stdio.h>
#include<string.h>
int main()
{
    char j=1,i,n;
    scanf("%d",&n);
    for(i=1;i<=n;i++) j *= i;
    printf("%d",j);
    return 0;
}
