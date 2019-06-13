f=int(input())
j=1
if f<0:
  print()
elif f==0:
  print("1")
else:
  for i in range(1,f+1):
    j=j*i
  print(j)    
