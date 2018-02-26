_ = input()
print [j for i, j in enumerate(map(int,raw_input().split(" "))) if (((i%2==0) and (j%2 !=0)) or ((i%2 !=0) and (j%2 ==0)))]
