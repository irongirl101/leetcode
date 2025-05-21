#include <stdio.h> 
#include <string.h>
int main(){
    char *words[] = {"leetcode","win","loops","success"}; 
    
    char str[] = "code"; 
    
    int count = 0; 
    for(int j = 0; j <sizeof(words)/sizeof(words[0]); j++){
        for (int i = 0; i < sizeof(str)/sizeof(str[0]); i++)
            {
                if(words[j][i]==str[i]){
                    count++; 
                   
                }
            }
    }
    int x = sizeof(str)/sizeof(str[0]); 
    printf("%d\n", (count-1)/(x-1)); 
    

    
}