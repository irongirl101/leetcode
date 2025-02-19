#include <stdio.h> 
#include <stdlib.h>

int main(){
    int dividend = -10; 
    int divisor = 3; 
    int c=0;
    int positive_dividend = abs(dividend);
    int positive_divisor = abs(divisor); 
    
    while (positive_dividend>0)
    {   
        positive_dividend-=positive_divisor; 
        c++;
    }
    if(dividend<0 || divisor<0){
        printf("-%d",c-1);
    }
    else{printf("%d",c-1);}
    return 0;
}