while(True):
    ip = raw_input()
    if ip == "":
        break
    if ip.lower() in ["saturday","sunday"]:
        print "yes"
    else:
        print "no"
