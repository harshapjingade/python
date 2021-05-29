n = int(input())
arr=[]
for i in range(n):
  arr.append(int(input()))
set1=set(arr)
result={}
for i in set1:
  if i in arr:
    result[i]=arr.count(i)
for k,v in sorted(result.items(),reverse=True):
  print k,v

