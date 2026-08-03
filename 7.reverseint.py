x = 120
y = [] 
c = 1
while x>0: 
   y.append(x%10)
   x = x//10 
   c*=10

n = 0
for i in y: 
   c = c//10
   n += i*c
print(n)