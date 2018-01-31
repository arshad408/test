def is_prime(a):
    return all(a % i for i in xrange(2, a))

i,j = raw_input().split(" ")
m = 0
for k in range(int(i),int(j)+1):
    if is_prime(k):
        m += 1
print m
