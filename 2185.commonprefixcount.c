#include <stdio.h> 
#include <string.h>
int main(){
    char *words[] = {"leetcode","win","loops","success"}; 
    //char str1[] = "abcdefg"; 
    char str[] = "code"; 
    //char *prefixed[] = {"","","",""}; 
    int count = 0; 
    for(int j = 0; j <sizeof(words)/sizeof(words[0]); j++){
        for (int i = 0; i < sizeof(str)/sizeof(str[0]); i++)
            {
                if(words[j][i]==str[i]){
                    //printf("%c",str[i]); 
                    //prefixed[j] = words[j]; 
                    count++; 
                    //printf("%d\n", count); 
                }
            }
    }
    int x = sizeof(str)/sizeof(str[0]); 
    //printf("%d %d\n", x-1, count-1); 
    printf("%d\n", (count-1)/(x-1)); 
    //printf("%zu\n", count/(sizeof(str)/sizeof(str[0]))); 
    /*int count = 1; 
    for(int i = 0; i<sizeof(prefixed)/sizeof(prefixed[0]); i++){
        if(strcasecmp(prefixed[i],"")==0){
            printf("%s\n", prefixed[i]); 
            count++; 
        }
        
    } 
    printf("%d",count); */ 

    
}