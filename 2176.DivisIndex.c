#include <stdio.h> 

int main(){
    int nums[] = {1,2,3,4}; 
    int k = 1; 
    int c = 0; 
    int flag = 0; //indicates if its true or false 
    
    int size = sizeof(nums)/sizeof(nums[0]); 

    for(int i = 0;i<size; i++){
        for(int j =0; j<size; j++){
            if(i!=j && nums[i]==nums[j]){
                int num = i*j; 
                flag = 1; 
                if(num%2==0){
                    c++; 
                }
            }
        }
    }

    if(flag == 0){
        printf("%d",0); 
    }
    else if(c==0){
        printf("No pairs");
    }
    else{
        printf("%d",c/2);
    }

}