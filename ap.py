def ap(terms):
    return len(terms)*(terms[0]+terms[-1])//2

print ap(range(int(raw_input().split(" ")[0]) + 1))
