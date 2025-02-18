#given a dividend and a divisor, divide without using /,*,% 

#keep minusing, until it reaches a number lower than the divisor, while keeping a count variable, which will give a quotient 


#what about negative division? typically i would ignore the minus sign and then i would add it, and if its a double minus, i would ignore both. 
dividend = -7
divisor = 3
c=0

while True:
    if divisor==0:
        print("unable")
        break
    elif dividend>=divisor and divisor>0:
        dividend-=divisor 
        c+=1
        if dividend<divisor:
            print(c)
            break
    elif dividend<0 and divisor<0:
        dividend-=divisor
        c+=1
        if dividend>=0:
            c-=1
            print(c)
            break
    elif divisor<0 :
        dividend+=divisor
        c-=1
        if dividend<0:
            c+=1
            print(c)
            break
    elif dividend<0: 
        dividend+=divisor
        c-=1
        if dividend>=0:
            c+=1
            print(c)
            break

    

