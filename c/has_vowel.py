ip = raw_input().lower()
has = 0
if len([i for i in ['a','e','i','o','u'] if i in ip]) > 0 :
    print "yes"
else:
    print "no"
