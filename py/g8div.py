a = sorted(map(int,raw_input().split(" ")))
print max([i for i in range(a[0],a[1]+1) if (a[0]%i==0) and (a[1]%i==0)])
