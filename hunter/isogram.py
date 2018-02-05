def is_iso(data):
    t = []
    for i in data:
        if i in t:
            return False
        t.append(i)
    return True

while(1):
    dt = raw_input()
    if dt == "":
        break
    if is_iso(dt):
        print "yes"
    else:
        print "no"
