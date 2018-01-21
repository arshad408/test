def check(n):
    if (n == 0):
        return False
    while (n != 1):
            if (n % 2 != 0):
                return False
            n = n // 2
            print n
    return True
if check(input()):
	print "yes":
else:
	print "no"
