'''digits=[9]
s=''

for i in digits:
    s+=str(i)

num=str(int(s)+1)
outdig=[]
for i in num:
    outdig.append(int(i))

print(outdig)
'''

def add(digits):
    a = digits[len(digits)-1] + 1
    aq = a//10 
    am = a% 10 
    digits[len(digits)-2]+= aq 
    digits[len(digits)-1] = am 
    return digits

digits = [8,9]


if len(digits)>1:
    print(add(digits))
elif len(digits)==1:
    digits.append(0)
    digits[0],digits[1] = digits[1],digits[0]
    print(add(digits))
