

#keep dividing, by thousand, hunderend and each, then get the values, then do string concatenation 

num = 3949  #the number will always be less than 3999 

#could have a better method, but eh works for the time being 

thousands = num // 1000 
hund = (num%1000)
tens = (num%100) 
ones = num % 10         

rom = ''

def convert(x, d= {1:'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500:'D', 1000: 'M'} ):
    keys = list(d.keys())
    sub_d = {}
    for i in d: 
        if x<i and len(sub_d)<3: 
            sub_d[i] = d[i]
            temp1 = keys.index(i)-1
            temp2 = keys.index(i)-2 
            sub_d[keys[temp1]] = d[keys[temp1]]
            sub_d[keys[temp2]] = d[keys[temp2]]
       
    
    


    print(sub_d)


if thousands or hund or tens or ones:
    rom+=(thousands*"M") #this will be constant. 
    convert(hund)
    convert(tens)

    convert(ones)

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
    


