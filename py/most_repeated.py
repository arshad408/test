mapi = {}
for i in raw_input():
    if i != " ":
        if mapi.has_key(i):
            mapi[i] = mapi[i] + 1
        else:
            mapi[i] = 1
print sorted(mapi, key=mapi.get)[-1]
