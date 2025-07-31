#include <stdio.h> 

int main(){
    int nums[] ={2,1,4}; 
    int flag = 0; 
    int len = sizeof(nums)/sizeof(nums[0]); 
    if(len>1){
        for(int i = 0; i<len; i++){
            if (i+1<len){
                if (nums[i]%2==0 & nums[i+1]%2==0){
                    flag = 0; 
                    break; 
                }
                else if(nums[i]%2!=0 & nums[i+1]%2!=0){
                    flag = 0; 
                    break; 
                } 
                else if (nums[i]%2 == 0 & nums[i+1]%2!=0){
                    flag = 1;}
                
                else if(nums[i]%2!=0 & nums[i+1]%2==0){ 
                    flag = 1 ;}
                
            }
            
    }
     if (flag == 1){ 
        printf("true");}

    else{ 
        printf("false");}

    }
    else{
        printf("true"); 
    }
}