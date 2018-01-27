#include <stdio.h>
void sort(int a[],int n) {
   int i,j;
   for(i=0;i<n-1;i++) for(j=0;j<n-i-1;j++) if(a[j]>a[j+1])swap(&a[j],&a[j+1]);
}

void swap(int *p,int *q) {
   int t;
   t=*p;*p=*q; *q=t;
}

int main()
{
    int n,t,data[100];
    scanf("%d",&n);
    for(int i=0;i<n;i++) scanf("%d",&data[i]); 
    sort(data,n);
    n = (n+1)/2;
    printf("%d",data[n-1]);
    return 0;
}
