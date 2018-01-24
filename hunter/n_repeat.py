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
if len(sp) > 0:
  print " ".join(sorted(sp))
else:
  print "unique"
