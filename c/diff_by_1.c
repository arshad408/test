#include <stdio.h>
#include<string.h>

int main()
{
    char a[30],b[30],t;
    int j=0,i,d=0;
    scanf("%s %s",&a,&b);
    for(i=0;i<strlen(a);i++) if(a[i] != b[i]) d++;
    if(d==1) printf("yes");
    else printf("no");
}
