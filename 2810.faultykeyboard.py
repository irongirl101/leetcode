def reverse(str):
    final_str=""
    for i in range(len(str)-1,-1,-1):
        final_str+=str[i]
    return final_str

s = "poiinter"
str = ""
for i in range(len(s)): 
    if s[i]!="i": 
        str+=s[i]
    else: 
        str=reverse(str)
print(str)