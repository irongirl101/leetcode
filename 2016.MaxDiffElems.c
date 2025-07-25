#include <stdio.h> 

int main(){
    int nums[] = {1,5,2,10}; 
    int diff = -1; 
    int len = sizeof(nums)/sizeof(nums[0]); 
    for(int i = 0; i<len; i++){
        if(i+1<len && diff<nums[i+1]-nums[i]){
            diff = nums[i+1]-nums[i]; 
            printf("%d\n", diff); 
        }
    }
    printf("%d", diff); 
    return 0; 
}