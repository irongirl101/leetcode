import math 
def sqrt_newton(num, precision=0.0001):
    if num < 0:
        print('num = 0')
    if num == 0 or num == 1:
        return num

    guess = num / 2.0  
    
    while abs(guess * guess - num) > precision:   
        guess = (guess + num / guess) / 2.0 
    return guess

number = 577
print(math.floor(sqrt_newton(number)))
