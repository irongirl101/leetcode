#include <stdio.h> 


int main(){
    char s[4] = "abcd"; 
    char t[5] = "abcde"; 
    char final; 
    for(int i = 0; i<sizeof(t); i++){
        for(int j =0; j<sizeof(s);j++){
           if(t[i]==s[j]){
            
            t[i] = '1'; 
            s[j]= '1'; 
           }
           

        }
    }

    for(int i = 0; i<sizeof(t);i++){
        if(t[i]!='1'){
            final = t[i]; 
        }
    }
    printf("%c",final); 
}