test = "cacccd"
regex = "ca*bc*d"

test_p = 0 
regex_p = 0 
print("t|r")
while test_p<len(test): 
    if regex_p+1<len(regex) and regex[regex_p+1]=="*" :  
        if test[test_p]==regex[regex_p]: 
            while(test[test_p]==regex[regex_p]): 
                print(True)
                test_p+=1     
            if test[test_p]==regex[regex_p]: 
                regex_p+=2
            else: 
                regex_p+=1
                test_p-=1
        else: 
            print(False)
    elif regex[regex_p]=="*": 
        regex_p+=1
        test_p-=1
        print(True)
    else: 
        if test[test_p]==regex[regex_p]: 
           print(True)
        else:
            print(False)
            break
        
    regex_p+=1
    test_p+=1
    
    
    
    
'''if regex[regex_p+1]=="*" and regex_p+1 <len(regex): 
        print(regex[regex_p],test[test_p])
        regex_p+=1
        test_p+=1
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
            regex_p+=1 ''' 
    

    
   

