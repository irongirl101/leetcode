#include <stdio.h> 

int main(){
    int nums[] = {-5,-10,-5}; 
    int greatest = 0; 
    /*for(int i = 0; i<(sizeof(nums)/sizeof(nums[0]));i++){
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
    }*/ 
    int len = (sizeof(nums)/sizeof(nums[0])); 
    for(int i = 0; i<len ;i++){
        int j = i+1; 
        if(j==len){
            j = 0; 
            if(nums[j]>=nums[i] && greatest<nums[j]-nums[i]){ 
                greatest = nums[j]-nums[i];}
            else if(nums[i]>nums[j] && greatest<nums[i]-nums[j]){ 
                greatest = nums[i]-nums[j];}
        }
        else if(j<len){
            if(nums[j]>=nums[i] && greatest<nums[j]-nums[i]){ 
                greatest = nums[j]-nums[i];}
            else if(nums[i]>nums[j] && greatest<nums[i]-nums[j]){ 
                greatest = nums[i]-nums[j];}
        }
    }
    printf("%d", greatest); 
    return 0; 
}