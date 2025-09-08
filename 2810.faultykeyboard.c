#include <stdio.h>
#include <stdlib.h> 
char* reverse(char* str){
    int len = 0;
    while (str[len] != '\0') len++;
    char* s = (char*)malloc((len + 1) * sizeof(char));
    if (!s) return NULL;
    for (int i = 0; i < len; i++) {
        s[i] = str[len - 1 - i];
    }
    s[len] = '\0';
    return s;
}
int main(){

    char str[] = "string"; 
    int len = 0;
    while (str[len] != '\0') len++;
    char* s = (char*)malloc((len + 1) * sizeof(char));
    for(int i = 0; i<sizeof(str); i++){
        if(str[i]!='i'){
            
        }
    }

    

    return 0; 
}
