from __future__ import division
data = []
n = input()
for i in range(n):
    data = data + map(int,raw_input().split(" "))
print sum(data)/(n*n)
