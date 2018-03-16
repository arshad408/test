_ = input()
data = [raw_input() for i in range(_)]
pre = ""
for i in range(len(data[0])):
    t = 0
    for j in range(_):
        if data[0][i] == data[j][i]:
            t = t + 1
    if t == _ :
        pre = pre + data[0][i]
    else:
        break
print pre
