while(True):
    data = raw_input()
    if data == "":
        break
    data = data.split(" ")
    print int(data[1]) - int(data[0])
