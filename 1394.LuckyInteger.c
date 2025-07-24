#include <stdio.h> 

int main(){
    int arr[] = {3,3,0,2,7,9,5,5,5,2,3,4,4,4,1,5,5}; 
    int final = -1; 
    for(int i = 0; i<(sizeof(arr)/sizeof(arr[0]));i++){
        int pos = arr[i]; 
        int count = 1; 
        for(int j = i+1;j<(sizeof(arr)/sizeof(arr[0]));j++){
            if(pos == arr[j]){
                count++; 
            }
        }
        if(pos==count && final<pos){
            final = pos; 
        }
    }
    printf("%d\n", final); 
    return 0; 
}