#include <stdio.h> 

int main(){

    int fruits[] = {3,6,1}; 
    int baskets[] = {6,4,7}; 

    int count = 0; 
    for(int i = 0; i<sizeof(fruits)/sizeof(fruits[0]);i++){
        for(int j = 0; j<sizeof(baskets)/sizeof(baskets[0]);j++){
            if(fruits[i]<baskets[j] & fruits[i]!=-1 & baskets[j]!=-1){
                //printf("%d %d\n", fruits[i])
                fruits[i] = -1; 
                baskets[j] = -1; 
                count++;
                //printf("%d\n", count); 

            }
            
        }
    }
    int size = sizeof(fruits)/sizeof(fruits[0]); 
    
    printf("%d", size-count); 
}
