#include<stdio.h>
int main()
{
    int n,i,j,k,t;
    scanf("%d",&n);
    i = 1;
    j = 1;
    printf("1 1 ");
    for(k=0;k<n-2;k++){
        t = j;
        j = i+j;
        i = t;
        printf("%d ",j);
    }
}
