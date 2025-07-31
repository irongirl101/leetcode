#include <stdio.h>

int main(){
    char s[] = "aaaaabbc"; 
    int a1 = 0; 
    int a2 = 0; 
    for(int i = 0; i<sizeof(s);i++){
        int c = 1; 
        char p = s[i]; 
        for(int j = i+1; j<sizeof(s); j++){
            if(p==s[j]){
                c++; 
            }
        }
        if(c%2==0 & c>a2){
            a2= 0; 
        }
        else if(c%2!=0){
            if(c>a1){
                a2 = c; 
            }
        }
    }

    if(a2>a1){
        printf("%d\n",a2-a1);
    }
    else{
        printf("%d\n", a1-a2); 
    }

}