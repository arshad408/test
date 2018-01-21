a,b = raw_input().split(" ")
if sum([ord(i) for i in a]) > sum([ord(i) for i in b]):
	print a
else:
	print b
