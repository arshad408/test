#include <stdio.h>
int main()
{
    int a,i,task=0;
    scanf("%d",&a);
    for(i=2;i<a;i++){
        if(a%i == 0){
            task=1;
            break;
        }
     }
    printf((task)?"yes":"no");
}
