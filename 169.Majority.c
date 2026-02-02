#include <stdio.h>

int main(){
    int n = 7; 
    int arr[] = {2,2,1,1,1,2,2};
    int count = n/2;
    for(int i = 0; i<n; i++){
        int c = 0; 
        for(int j = 0; j<n;i++){
            if(i!=j && arr[i]==arr[j] && c<count){
                c++; 
            }
        if(c>=count){
            printf("%d", arr[i]); 
            break;
        }
        }
    }
   


}