#include<stdio.h>
int main()
{
    int i,j,t;
    scanf("%d %d",&i,&j);
    t = i;
    i = j;
    j = t;
    printf("%d %d",i,j);
    return 0;
}
