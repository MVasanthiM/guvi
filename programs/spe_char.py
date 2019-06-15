i=input()
c=0
for s in i:
    if (s.isnumeric() or s.isspace() or s.isalpha())!=True:
      c+=1
print(c)
