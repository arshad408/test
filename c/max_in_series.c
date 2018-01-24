#include<stdio.h>
int main()
{
    int i,max,data[10];
    for(i=0;i<10;i++) scanf("%d",&data[i]);
    max = data[0];
    for(i=1;i<10;i++) if(data[i] > max) max = data[i];
    printf("%d",max);
    return 0;
}
