i=1
n,m = map(int,raw_input().split(" "))
while(True):
    if (i%n==0) and (i%m==0):
        print i
        break
    i = i+1
