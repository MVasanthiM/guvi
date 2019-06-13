s,e=map(int,input().split())
for num in range(s+1,e):
  sum=0
  t=num
  while(t>0):
    d=t%10
    sum+=d**3
    t//=10
  if(num==sum):
    print(num,end=' ')
