A = map(int,raw_input().split(" "))
B = map(int,raw_input().split(" "))
C = map(int,raw_input().split(" "))
if ( A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1]) ) == 0:
    print "yes"
else:
    print "no"
