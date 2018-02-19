p1 = map(int,raw_input().split(" "))
p2 = map(int,raw_input().split(" "))
p3 = map(int,raw_input().split(" "))
if (p1[0]==p2[0]==p3[0]) or (p1[1]==p2[1]==p3[1]):
    print "yes"
else:
    print "no"
