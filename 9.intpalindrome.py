#problem 9 
'''def palindrome(x):
    x_string= str(x)
    if x_string== x_string[::-1]:
        return 'true'
    else:
       return 'false'
a=121
print(palindrome(a))'''
'''
stack program
l=[]
def push():
    while ch in 'nN':
        a=input("Enter push element)
        l.append()
        ch=input("do you want to continue)

def pop():
    if l==[]:
          print("underflow condition)
    else:
        l.pop()
    '''
''' USING STACKS
x='cat' #given string
x_list=[]#list of the seperate values->will be popped
x_listcopy=[]#essentially the same as x_list but is used in a different usecase-> original list 
x_list1=[]#the popped list 
#using stacks 
def push(x):#getting all the str values, putting them in list. 
    for i in x:
        x_list.append(i)#creating two seperate equal lists, where one will have the pop function on it, hence the list will become empty, and the other will be used to compare against
        x_listcopy.append(i)
    
def pushpop():
    if x_list==[]:
        print('underflow condition')
    else:
        for i in range(len(x_list)-1,-1,-1):#popping every element in the list 
            a=x_list.pop(i)
            x_list1.append(a)#the popped values list, in the other way 
def palindromecheck():
    if x_listcopy==x_list1:
        print("palindrome")
    else:
        print('not')

push(x)
pushpop()
palindromecheck()  '''        
'''
given_int=144 #given 
original_int_list=[]# list of given int
original_int_list_copy=[]# copy of original list 
popped_int_list=[] #all popped elements are appended to this list 

def push(given_int):
    while given_int%10!=0:#getting remainder each time
        d1=given_int%10
        given_int=given_int//10
        original_int_list.append(d1)
        original_int_list_copy.append(d1)

def pop():
    if original_int_list==[]:
        print("underflow condition")
    else:
        for i in range(len(original_int_list)-1,-1,-1):
            a=original_int_list_copy.pop(i)
            popped_int_list.append(a)

def ispalindrome():
    if original_int_list==popped_int_list:
        print("palindrome")
    else:
        print('not')

push(given_int)
pop()
ispalindrome()'''

class Stack(object):
    def __init__(self): #initializing the values 
        self.items=[]
        
    def push(self,x): #pushes element into list 
        self.items.append(x)
    
    def pop(self):
        if self.items==[]:
            print("Underflow")  
        else:
            a=self.items.pop() #pops element from list 
            return a 

x=12321

stack_object = Stack()

#pushing in the values 
while x>0:
    d1=x%10
    x=x//10
    stack_object.push(d1)

ispalindrome=True
i=0
while len(stack_object.items)!=0 and ispalindrome and i<len(stack_object.items)-1:
    a=stack_object.items.pop()
    if i<len(stack_object.items) and a==stack_object.items[i]:
        i+=1
    else:
        ispalindrome=False

def isp(x,ispalindrome):
    if x<0:
        return False
    elif  ispalindrome and len(str(x))>=1:
        return True
    else:
        return False
print(isp(x,ispalindrome))

