#include <stdio.h>
#include<string.h>

int main()
{
    char a[30];
    int i,d=0;
    scanf("%s",&a);
    for(i=0;i<strlen(a);i++){
        if(a[i]=='0' || a[i]=='1') d=1;
        else{
            d=0;break;
        }
    }
    printf((d)?"yes":"no");
}
