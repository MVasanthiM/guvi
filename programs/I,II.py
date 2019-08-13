f=input()
s=0
d={"I": 1,"II": 2,"V":5,"X":10}
for i in f:
  if i in d:
    s=s+d[i]
print(s)    
    
