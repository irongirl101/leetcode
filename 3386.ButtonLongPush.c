#include <stdio.h>

int abs_int(int x,int y){
    if(x>=y){
        return x-y; 
    }
    else{
        return y-x; 
    }
}

int main(){
    int events[][2] = {{10,5},{1,7}}; 
    int diff = events[0][1];
    int index = events[0][0]; 

    for (int i = 1; i < sizeof(events)/sizeof(events[0]); i++)
    {
        if (abs_int(events[i-1][1],events[i][1])>diff)
        {
            diff = abs_int(events[i-1][1],events[i][1]); 
            index = events[i][0]; 
        }
        
    }
    printf("%d",index); 
    
}