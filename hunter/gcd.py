def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
data = map(int,raw_input().split(" "))
print gcd(data[0],data[1])
