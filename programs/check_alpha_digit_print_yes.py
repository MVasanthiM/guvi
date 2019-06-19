b=input()
h=0
l=0
for i in b:
  if i.isalpha():
    h=1
    break
for i in b:
  if i.isdigit():
    l=1
    break
if h==1 and l==1:
  print("Yes")   
else:
  print("No")   
