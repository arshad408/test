ip = input()
print " ".join(map(str,[i for i in range(1,ip+1) if ip%i == 0]))
