h1,m1 = map(int,raw_input().split(" "))
h2,m2 = map(int,raw_input().split(" "))

if (m1-m2) < 0 :
    print str(h1 - h2 - 1) + " " + str(60 + (m1-m2) )
else:
    print str(h1 - h2)+ " " + str(m1 - m2)
