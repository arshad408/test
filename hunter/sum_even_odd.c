#include <stdio.h>
#include<string.h>

int main()
{
    int i,j;
    scanf("%d %d",&i,&j);
    printf(((i+j)%2 == 0)? "even" : "odd");
}
