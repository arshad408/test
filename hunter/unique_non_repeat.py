hold = []
sp = []
_ = input()
data = map(int,raw_input().split(" "))
for k in data:
    if k in hold:
        if k not in sp:
            sp.append(k)
    else:
        hold.append(k)
print "".join(map(str,[j for j in data if j not in sp]))
