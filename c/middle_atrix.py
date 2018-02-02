ip = list(raw_input())
if len(ip)%2 !=0:
    ip[len(ip)/2]= "*"
else:
    ip[len(ip)/2]= "*"
    ip[len(ip)/2 - 1]= "*"
print ''.join(ip)
