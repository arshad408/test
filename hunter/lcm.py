def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
def lcm(a,b):
    return (a*b)//gcd(a,b)
data = map(int,raw_input().split(" "))
print lcm(data[0],data[1])
