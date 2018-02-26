_ = input()
data = map(int,raw_input().split(" "))
tmp = []
k = 1
for i in data:
    if i in tmp:
        print i
        k = 0
        break
    tmp.append(i)
if k==1:
    print "unique"
