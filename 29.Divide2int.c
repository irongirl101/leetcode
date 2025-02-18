#include <stdio.h> 
#include <stdlib.h>

int main(){
    int dividend = abs(-10); 
    int divisor = abs(3); 
    int c=0;
    
    while (dividend>0)
    {   
        dividend-=divisor; 
        c++;
    }
    printf("%d",c-1);

    return 0;
}