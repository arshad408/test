data = raw_input()
a = ""
b = ""
for i in range(0,len(data)):
    if i%2 == 0:
        a += data[i]
    else:
        b += data[i]
print "{} {}".format(a,b)
