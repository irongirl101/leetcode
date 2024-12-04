digits=[9]
s=''

for i in digits:
    s+=str(i)

num=str(int(s)+1)
outdig=[]
for i in num:
    outdig.append(int(i))

print(outdig)
