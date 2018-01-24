#include<stdio.h>
int main()
{
    char data[50];
    int i,j;
    scanf("%s %d",&data,&j);
    for(i=0;i<j;i++) printf("%c",data[i]);
}
