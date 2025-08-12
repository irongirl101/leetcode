#include <stdio.h>

int abs_int(int a,int b){
    if(a-b>0){
        return a-b; 
    }
    else return b-a; 
}

int main(){
    int x = 1; 
    int y = 5; 
    int z = 3; 

    if(abs_int(x,z)<abs_int(y,z)){
        printf("1"); 
    }
    else if (abs_int(x,z)>abs_int(y,z))
    {
       printf("2"); 
    }
    else if (abs_int(x,z)==abs_int(y,z))
    {
        printf("0"); 
    }
    
    
}