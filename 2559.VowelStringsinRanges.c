#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(){
    char *words[] = {"aba","bcb","ece","ee","a"}; 
    int queries[3][2] = {{0,2},{1,4},{1,1}}; 
    int answer[] = {0,0,0}; 
    /*int x = sizeof(queries)/sizeof(queries[0]); 
    printf("%d\n", x); */ 

    int sizequeries = sizeof(queries)/sizeof(queries[0]); 
    int i = 0; 
    char *vowels[5] = {"a","e","i","o","u"}; 
    int size_vowels = 5; 
    while (i<sizequeries)
    {
       int start = queries[i][0]; 
       int end = queries[i][1]; 
       for (int j = start; j < end+1; i++)
       {
           
            printf("%s\n", words[j]); 
            break;    
                
            
       }
       
       
    
       
    }
    
    

    return 0; 
}