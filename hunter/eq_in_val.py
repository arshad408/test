k = []
_ = input()
for i, j in enumerate(map(int,raw_input().split(" "))):
    if j == i:
        k.append(i)
if len(k) > 0:
    print " ".join(map(str,k))
else:
    print -1
