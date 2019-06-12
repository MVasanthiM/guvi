g=int(input())
f=g
re=0
while g!=0:
  r=g%10
  re=re*10+r
  g=g//10
if(f==re):
  print("yes")
else:
  print("no")    

   
