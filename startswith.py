def startswith(start,n):
  even_numbers=[]
  i=0
  while(i<n): 
    #print("start:", start)
    if start % 2 == 0:
      even_numbers.append(start)
      i+=1
    start+=1
  return even_numbers
#print(startswith(5,7))


def startswith(start,n):
  even_numbers=[]
  for i in range(n):
    print("start:", start)
    if start % 2 == 0:
      even_numbers.append(start)
    start+=1
  return even_numbers
print(startswith(2,4))
  
