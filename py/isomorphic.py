ip1,ip2 = map(list,raw_input().split(" "))
if len([i for i in ip1 if i in ip1]) == len([i for i in ip2 if i in ip2]):
    print "yes"
else:
    print "no"
