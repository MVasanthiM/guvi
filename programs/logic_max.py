p=int(input())
l=list(map(int,input().split()))
max=0
for i in l:
  if max<i:
      max=i
print(max)      
