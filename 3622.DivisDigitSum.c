#include <stdio.h> 

int main(){
    int n  = 99; 
    int n1 = n; 
    int sum = 0; 
    int prod = 1; 
    while (n>0)
    {
        sum+=n%10; 
        prod*=n%10; 
        n/=10; 
    }

    if(n1%(sum+prod)==0){
        printf("true\n"); 
    }
    else{
        printf("false\n"); 
    }
    
}