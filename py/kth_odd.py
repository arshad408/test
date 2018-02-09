_,k = map(int,raw_input().split(" "))
print [i for i in map(int,raw_input().split(" ")) if i%2 != 0][k-1]
