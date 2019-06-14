n=int(input())
ls=list(map(int,input().split()))
a=sorted(ls)
ans=sum(a)//len(a)
print(ans)


