c,n=map(int,(input().split()))
d=c-n
if d<0:
  d=-(d)
  if d%2==0:
    print("even")
  else:
    print("odd")  
