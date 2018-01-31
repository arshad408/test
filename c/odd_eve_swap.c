#include <stdio.h>
#include<string.h>

int main()
{
    char a[5],t;
    int sum=0,i;
    scanf("%s",&a);
    for(i=0;i<strlen(a);i=i+2){
        t = a[i];
        a[i] = a[i+1];
        a[i+1] = t;
    }
    printf("%s",a);
}
