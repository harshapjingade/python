def topten():
    n = 1
    while n <=20:
        sq = n*n
        yield sq
        n+=1

for i in topten():
    print(i)