_ = input()
data = map(int,raw_input().split(" "))
prev = data[0]
for i in range(1,len(data)):
    if data[i] == prev+1:
        prev = data[i]
    else:
        print prev+1
        break
