

#keep dividing, by thousand, hunderend and each, then get the values, then do string concatenation 

num = 3555  #the number will always be less than 3999 

#could have a better method, but eh works for the time being 
'''
{1000: 'M', 500: 'D', 100: 'C'}
{50: 'L', 10: 'X', 5: 'V'}
{5: 'V', 1: 'I', 1000: 'M'}

'''
thousands = num // 1000 
hund = (num%1000)//100
tens = (num%100) //10
ones = num % 10         

rom = ''

def convert(x, d= {1:'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500:'D', 1000: 'M'} ):
    keys = list(d.keys())
    sub_d = {}
    rom = ''
    for i in d: 
        if x<i and len(sub_d)<3: 
            sub_d[i] = d[i]
            temp1 = keys.index(i)-1
            temp2 = keys.index(i)-2 
            sub_d[keys[temp1]] = d[keys[temp1]]
            sub_d[keys[temp2]] = d[keys[temp2]]
  
    if x>=100 or x>=10 or x>=1: 
        if x == max(sub_d)- min(sub_d): # for 9s 
            rom+=(sub_d[min(sub_d)]+sub_d[max(sub_d)])
            return rom
        elif x==400 or x==40  or x == 4:
            for i in sub_d:
                if i!= max(sub_d) and i!= min(sub_d):
                    temp = i 
            if x%400 == 0 or x%40 == 0: 
                rom+=(sub_d[temp]+sub_d[max(sub_d)])
                return rom
            else:
                rom+=(sub_d[min(sub_d)]+sub_d[temp])
                return rom
        elif x<400 or x<40 or x<4: 
            for i in sub_d:
                if i!= max(sub_d) and i!= min(sub_d):
                    temp = i 
            if x%100 == 0: 
                mult = x//100 
                rom+=(sub_d[temp] * mult) 
            elif x%10 == 0:
                mult = x//10
                rom+=(sub_d[temp] * mult) 
            else:
                mult = x
                rom+=(sub_d[min(sub_d)] * mult) 
            return rom
        elif x>400 or x>40 or x>4: 
            print(sub_d)
                
            

            

    
    #6print(sub_d)


if thousands or hund or tens or ones:
    rom+=(thousands*"M") #this will be constant. 
    convert(hund*100)
    convert(tens*10)
    convert(ones)
    if hund>0:
        rom+=convert(hund*100)
    else:
        pass
    if tens>0:
        rom+=convert(tens*10)
    else:
        pass
    if ones>0:
        rom+=convert(ones)
    else:
        pass


    '''if hund == 4: 
        rom += (d[100]+d[500])
    elif hund == 5:
        rom += (d[500])
    elif hund>5 and hund<9: 
        temp = 10-hund 
        rom+= (d[500]+ d[100]*temp)
    elif hund == 9: 
        rom+= (d[100]+d[1000])

    else:
        rom+=(hund*d[100])
    rom+=(tens*d[10])
    rom+=(ones*d[1])'''
print(rom)
    


