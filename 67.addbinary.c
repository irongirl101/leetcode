#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(){
    char a[] = "1010"; 
    char b[] = "1011"; 
    int len; 
    //int c = 0; 
    char *final;
    if(sizeof(a)>=sizeof(b)){
        len = sizeof(a); 
        final = (char*)malloc(sizeof(a)+1); 
    }
    else{
        len = sizeof(b); 
        final = (char*)malloc(sizeof(b)+1); 
    }
    char c = '0'; 
    for(int i=len-1;i>=0; i--){
        char ap = a[i]; 
        char bp = b[i]; 
        //printf("%d", !strcmp((char[]){c, '\0'}, "0")); 
        if(!strcmp((char[]){c, '\0'}, "0")){
           if((!strcmp((char[]){ap, '\0'}, "0")) & !strcmp((char[]){bp, '\0'}, "0")){
                final[i] = '0'; 
            }
            else if(  (!strcmp((char[]){ap, '\0'}, "1") & (!strcmp((char[]){bp,'\0'},"0")) )|| (!strcmp((char[]){bp, '\0'}, "1")&(!strcmp((char[]){ap, '\0'}, "0")))){
                final[i] = '1'; 
            }
            else if(!strcmp((char[]){ap, '\0'}, "1") & (!strcmp((char[]){bp, '\0'}, "0"))){
                final[i] = '0'; 
                c = '1'; 
            }
        }
        else if(!strcmp((char[]){c, '\0'}, "1")){
            if((!strcmp((char[]){ap, '\0'}, "0")) & !strcmp((char[]){bp, '\0'}, "0")){
            final[i] = '1'; 
            }
            else if(  (!strcmp((char[]){ap, '\0'}, "1") & (!strcmp((char[]){bp,'\0'},"0")) )|| (!strcmp((char[]){bp, '\0'}, "1")&(!strcmp((char[]){ap, '\0'}, "0")))){
                final[i] = '1'; 
                c='1'; 
            }
            else if(!strcmp((char[]){ap, '\0'}, "1") & (!strcmp((char[]){bp, '\0'}, "0"))){
                final[i] = '0'; 
                c = '1'; 
            }
        
        }
        //printf("%d",c); 
        
    }
    printf("%c",c);
    printf("%s\n",final); 
}