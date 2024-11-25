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
stack_object= Stack()

s='[{]}'
d={'{':'}','[':']','(':')'}
if len(s)%2==0:
    for i in s:
        if i in '{[()]}':
            if i in '{[(':
                stack_object.push(i)
            else:
                a=stack_object.pop()
                if d[a]!=i:
                    print('false')
                    break
        else:
            print('false')
            break
    else:
        print('true')
        
else:
    print('false')

        
            
       
            
        
        
        