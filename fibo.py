prev = 1
pres = 1
data = [1,1]
for i in range(input() - 2):
    data.append( pres+prev )
    prev,pres = [pres,pres+prev]

print " ".join(map(str,data))
