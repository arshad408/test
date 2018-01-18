def is_prime(a):
    return all(a % i for i in xrange(2, a))

i,j = raw_input().split(" ")
for k in range(int(i)+1,int(j)):
    if is_prime(k):
        print k
