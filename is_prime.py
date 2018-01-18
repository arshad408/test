def is_prime(a):
    return all(a % i for i in xrange(2, a))
if is_prime(input()):
  print "yes"
else:
  print "no"
