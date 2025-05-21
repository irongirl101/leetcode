#include <stdio.h> 

int count(int data[],int element){
    int data_size = 3; 
    int count = 0; 
    for(int i= 0; i< data_size; i++){
        if (data[i] == element){
            count++; 
        }
    }
    return count; 
}


int main(){
    int nums[3] = {3,3,3}; 
    if(((nums[0]+nums[1])>nums[2]) && ((nums[0]+nums[2])>nums[1]) && ((nums[1]+nums[2])>nums[0])){
        //printf("Triangle"); 
        int counts[] = {0,0,0}; 
        for(int i = 0; i < 3; i++){
            counts[i] = count(nums,nums[i]); 
        }
        
        for(int i = 0; i<3; i++){
            if (counts[i] == 2){
                printf("Isoceles\n"); 
                break;
            }
            else if (counts[i] == 3){
                printf("Equilateral\n"); 
                break;
            }
            else if(counts[i]==1 && counts[i+1]==1){
                printf("Scalene\n"); 
                break;
            }
 
            
        }
    }
    else{
        printf("none"); 
    }
}