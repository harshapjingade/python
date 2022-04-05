strings="HI harsha how are are you harsha"
strings_lower= set(strings.split())

print(' '.join(strings_lower))

m = "HI harsha how are are you harsha"
f=[]
words=m.split()

for i in words:
    if words.count(i)>=1 and i not in f:
        f.append(i)
print(' '.join(f))
