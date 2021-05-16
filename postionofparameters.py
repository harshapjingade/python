import sys
i=-1
print sys.argv
for p in sys.argv:
  i+=1
  if p == "c":
    print i
