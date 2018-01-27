#include <stdio.h>
int main()
{
    int total=0;
    int n,t;
    scanf("%d",&n);
    for(int i=n;i>0;i--){
        scanf("%d",&t);
        total += t; 
    }
    printf("%d",total/n);
    return 0;
}
