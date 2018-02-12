data =  raw_input().split(" ")
print "".join([i for i in data if data.count(i) == 1])
