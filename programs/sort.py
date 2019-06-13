num = int(input())
s=list(map(int,input().split()))
ss=sorted(s)
for i in range(0,len(ss)):
  print(ss[i],end=" ")
