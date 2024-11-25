roman_dict={'I':1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
s=input("Enter roman number: ")
SU=0

class Solution(object):
    def __init__(self):
        roman_number=roman_number.self
        Sum=Sum.self
        higher_number=higher_number.self
        lower_number=lower_number.self
        
'''def sum(s,SU):
    for i in s:
        if i in roman_dict.keys():
            SU+=roman_dict[i]

    return (SU)'''
'''while True:
    try:
        for i in range(len(s)):
            print(roman_dict[s[i]])
    except KeyError:
        break
    if i+1< len(s) and roman_dict[s[i]]<roman_dict[s[i+1]]:
        print(roman_dict[s[i]])'''

higher_number=0
lower_number=0
#if int(s)<4000:
for i in range(len(s)):
    if i+1< len(s) and roman_dict[s[i]]<roman_dict[s[i+1]]:
        higher_number= roman_dict[s[i+1]]
        lower_number=roman_dict[s[i]]
        difference= roman_dict[s[i+1]]-roman_dict[s[i]]
                    #print(difference)
        SU+=difference
    elif roman_dict[s[i]]!=higher_number and roman_dict[s[i]]!=lower_number:
            #print(roman_dict[s[i]])
                    SU+=roman_dict[s[i]]

print(SU)
#else:
    #print("Number not in range. ")