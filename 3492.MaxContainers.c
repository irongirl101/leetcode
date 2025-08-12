#include <stdio.h> 

int main(){
    int n = 3; 
    int w = 5; 
    int max_weight = 20; 
    int sum = 0; 
    int count = 0; 

    for(int i=0;i<n*n;i++){
        if (sum<max_weight){
            sum+=w;
            count++;
        }
        else{
            break;
        }
    }
    printf("%d",count); 

    return 0; 
}