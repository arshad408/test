def enc(a):
    c = ord(a)+3
    if c > 90:
        c = (ord('Z')-26)+3
    return chr(c)
print [enc(i) for i in list(raw_input())]
