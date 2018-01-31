#include <stdio.h>
#include<string.h>

int convert(char a){
    if(a == 'I') return 1;
    if(a == 'X') return 10;
    if(a == 'V') return 5;
}

int main()
{
    char a[5];
    int sum=0,i;
    scanf("%s",&a);
    for(i=0;i<strlen(a);i++) sum += convert(a[i]);
    printf("%d",sum);
}
