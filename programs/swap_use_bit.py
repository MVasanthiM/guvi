u,v=map(int,(input().split()))
u=u^v
v=u^v
u=u^v
print(u,v,end=" ")
