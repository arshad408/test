from math import ceil
data = sorted(map(int,raw_input().split(" ")))
print(data[int(ceil(len(data)/2.0)) - 1])
