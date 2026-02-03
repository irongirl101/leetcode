#include <stdio.h>
#include <string.h>


int main(){ 
    char ransomNote[] = "a"; 
    char magazine[] = "ab"; 
    // once letter is hit, remove letter from both 
    //after the looping of magazine is done and theres a letter still in the note, return false
    //else return true
    int note_count = sizeof(ransomNote); 
    int magazine_count = sizeof(magazine);
    int i = 0; 
    while (note_count>0){
        for(int j = 0;j<magazine_count;j++){
            if(ransomNote[i]==magazine[j]){
                i++; 
            }
        }
    }

}