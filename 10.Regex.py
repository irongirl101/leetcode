test = "cabcccd"
regex = "ca*bc*d"


def exp(test,regex):
    test_p = 0 
    regex_p = 0 
    flag = 0 
    while test_p<len(test): 
        if regex_p+1<len(regex) and regex[regex_p+1]=="*" :  
            if test[test_p]==regex[regex_p]: 
                while(test[test_p]==regex[regex_p]): 
                    flag = 0 
                    test_p+=1     
                if test[test_p]==regex[regex_p]: 
                    regex_p+=2
                else: 
                    regex_p+=1
                    test_p-=1
            else: 
                flag = 0 
        elif regex[regex_p]=="*": 
            regex_p+=1
            test_p-=1
            flag = 0 
        else: 
            if test[test_p]==regex[regex_p]: 
                flag = 0 
            else:
                flag = 1 
                break
            
        regex_p+=1
        test_p+=1
    return flag 
        
regex_check = exp(test, regex) 
if regex_check == 1: 
    print(False)
else: 
    print(True)
    
    
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
    

    
   

