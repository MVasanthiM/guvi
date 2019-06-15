number=int(input())
v=0
m=1
while(number>0):
  print(m,end=' ')
  v,m=m,v+m
  number=number-1
