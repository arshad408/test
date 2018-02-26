_ = raw_input() 
data = map(int,raw_input().split(" "))
if len( [i for i in map(int,raw_input().split(" ")) if i not in data])>0:
    print "NO"
else:
    print "YES"
