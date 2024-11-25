
'''
go through each str, then in each str, goes through each letter. If common prefix doesnt exist, break. 
first takes 1st letter of 1st str, and then checks in the other ones. if it does start with it, then continue, else break it off there. 
then goes to 2nd letter, checks, and process continues. 
'''
'''i=0 #iterating -> goes through each letter in the 1st word 
final_str=''
j=1 #iterating though each str'''

'''while isPrefix:
    str1= strs[0] #takes the first word 
    letter= str1[i] #gives each letter 
    print('letter: ',letter)
    i+=1
    next_word= strs[j]
    j+=1
    print('next word: ',next_word)'''
'''for j in strs: 
        if j!= str1: #going though each string in the list, as long as its not the first word 
            if j[i]==letter: #if the letter is corresponding with the letter in the other words
                final_str+=letter
                i+=1
            else:
                print('j[i]',j[i])
                #isPrefix=False #breaks it here
                print("Broken")'''
            
strs=["ball","basket","bag","doge"]
len_of_strs=[]

class min_str(object): 
    def make_list(strs,len_of_strs): #making list of the len of strs 
        for i in strs:
            len_of_strs.append(len(i))
        return len_of_strs

    def get_minimum_str(len_of_strs): # getting the minimum value of the list 
        minimum_len=min(len_of_strs)
        return(minimum_len)
    
    def get_index(minimum_len): #getting the index of that 
        main_str= strs[len_of_strs.index(minimum_len)]
        return main_str

x=min_str.make_list(strs,len_of_strs)
len_of_min_str=min_str.get_minimum_str(x)
index_of_min_str=min_str.get_index(len_of_min_str)


l=strs
l.remove(index_of_min_str)
d={}
for i in l:
    s=''
    for j in range(len_of_min_str):
        if i[j]==index_of_min_str[j]:
            s+=i[j]
        else:
            break   
    d[len(s)]=s



minim= min(list(d.keys()))
if minim!=0:
    print(d[minim])
else:
    print('Empty')


'''
i=0 # iterating through each word 
#j=0 #iterating through each letter
ch='' #final prefix
while isPrefix and i<len(strs)-1:
    print('i1',i)
    j=0
    if j< len_of_min_str: 
        if strs[i]!= index_of_min_str: 
            print('j',j)
            print('index',index_of_min_str[j])
            if index_of_min_str[j]== strs[i][j]:
                print(strs[i])
                ch+=index_of_min_str[j]
            print('i2',i)
            j+=1
            i+=1
            print('i2',i)
        else:
            i+=1
            #print(i)
    
    else:
        break
    #i+=1
    #print(i)

print(ch)
'''
'''
i=0 #goes through each letter in the least len word 
j=
common_prefix=''
while i<len(x) and isPrefix: #as long as i is less than the least len word 
    xletter=x[i]#getting each letter #i=0
    print('letter:',xletter)

    i+=1'''
'''for j in strs:#going through each word
        if j!=x:#if j is not x 
            if j[i]==xletter:#checking if that letter, at that position is equal to the next or not 
                isPrefix=True
                print(i)
                print(j[i],j)  

            else:
                isPrefix=False
                print(i)
                print(j[i],j)
                break
            i+=1'''
'''print(j[i])
                print(isPrefix)
                isPrefix=False
                print(isPrefix)
                break'''



'''for i in index_of_min_str:
    for j in strs:
        if j!=index_of_min_str:
            '''

