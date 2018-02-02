a,b = map(int,raw_input().split(" "))
def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) 
    if x in seen: return False
    seen.add(x)
  return True

if is_square(a*b):
    print "yes"
else:
    print "no"
