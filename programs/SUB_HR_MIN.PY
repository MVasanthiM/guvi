h,m=map(int,input().split())
h1,m1=map(int,input().split())
a=h-h1
a1=m-m1
if a<0:
  a=-a
if a1<0:
  a1=-a1
print(a,a1,end=" ")  
