#assuming that the alphabets are a and b 
s = 'aaab'
p = 'ab'

# to find length of a in s/p 
def length(x,s): 
    count = 0; 
    for i in s: 
        if i == x: 
            count+=1 
    return count 

def a(count_a_s,count_a_p,x_pos):
    if count_a_s>=count_a_p and p[x_pos]=="a": 
        return True 
    elif count_a_s == 0 and p[x_pos] == "a":
        return True
    elif count_a_s==count_a_p:
        return True
    else: 
        return False

def b(count_b_s,count_b_p,x_pos): 
    if count_b_s>=count_b_p and p[x_pos]=="b": 
        return True 
    elif count_b_s == 0 and p[x_pos] == "a":
        return True 
    elif count_b_s==count_b_p:
        return True
    else: 
        return False
        

def isMatch(s,p): 
    for i in p: 
        if i == '*': 
            pos = p.index(i)
            x_pos = pos-1
        else: 
            x_pos = -1 
    if x_pos!=-1:
        if 'a' in p and 'b' in p:
            count_a_s = length('a',s)
            count_b_s = length('b',s)
            count_a_p = length('a',p)
            count_b_p = length('b',p)
            return a(count_a_s,count_a_p,x_pos) and b(count_b_s,count_b_p,x_pos)
        elif 'a' in p and 'b' not in p: 
            count_a_s = length('a',s)
            count_a_p = length('a',p)
            return a(count_a_s,count_a_p,x_pos)
        elif 'b' in p and 'a' not in p: 
            count_b_s = length('b',s)
            count_b_p = length('b',p)
            return b(count_b_s,count_b_p,x_pos)
        elif '.' in p: 
            return True
    else: 

        if 'a' in p and 'b' not in p: 
            count_a_s = length('a',s)
            count_a_p = length('a',p)
            if(count_a_s>count_a_p): 
                return False
        elif 'b' in p and 'a' not in p: 
            count_b_s = length('b',s)
            count_b_p = length('b',p)
            if(count_b_s>count_b_p): 
                return False   
        else: 
            return True 
        return False
   

print(isMatch(s,p))
