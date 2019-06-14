n=int(input())
ls=list(map(int,input().split()))
a=sorted(ls)
for i in range(n):
  print(a[i],end=" ")
