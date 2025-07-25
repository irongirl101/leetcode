#include <stdio.h> 

int main(){
    int nums[] = {1,3,2}; 
    int greatest = 0; 
    for(int i = 0; i<(sizeof(nums)/sizeof(nums[0]));i++){
        int pos = nums[i]; 
        for(int j = (sizeof(nums)/sizeof(nums[0]))-1; j>i; j--){
            if(i!=j){
                int diff = nums[j]; 
                if (pos >= diff && pos-diff>greatest){
                    greatest = pos-diff; 
                }
                
                else if( pos<diff && diff-pos>greatest){
                    greatest=diff-pos;}
                }
        }
    }
    printf("%d", greatest); 
    return 0; 
}