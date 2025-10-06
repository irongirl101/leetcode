test = "caabcccd"
regex = "ca*bc*d"
test_p = 0 
regex_p = 0 

while test_p<len(test): 
    if regex[regex_p+1]=="*" and regex_p+1 <len(regex) and regex[regex_p]!="*": 
        if test[test_p]!= regex[regex_p]: 
            regex_p+=1 
            continue 
        elif test[test_p]== regex[regex_p]: 
            j = 0 
            while(test[j]== regex[regex_p]):
                j+=1
            test_p= j 
            regex_p+=1 
    else: 
        if test[test_p] == regex[regex_p]: 
            test_p+=1 
            regex_p+=1 

