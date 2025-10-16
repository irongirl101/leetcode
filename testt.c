#include <stdio.h> 

int fact(int n){
    if(n==1){
        return 1; 
    }
    else{
        return n*fact(n-1); 
    }
}

int getnumber()
{
    int x;
    x = 8;
    return x;
}

int main(){
    int in;
    in = getnumber();
    int x = fact(5); 
    printf("%d",x); 


}