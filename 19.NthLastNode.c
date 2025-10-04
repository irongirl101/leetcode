#include <stdio.h>
#include <stdlib.h> 

struct Node{
    int data; 
    struct Node* next; 
}; 

struct Node* createNode(int data){
    struct Node* newnode = (struct Node*)malloc(sizeof(struct Node)); 
    newnode->data = data; 
    newnode->next = NULL; 
    return newnode; 
}

void Insert(struct Node** head, int data){
    struct Node* newnode = createNode(data); 
    if(*head==NULL){
        *head = newnode; 
    }
    newnode->next = *head; 
    *head = newnode; 
}

int length(struct Node** head){
    if(*head == NULL){
        return 0; 
    }
    else{
        int count = 1; 
        struct Node* temp = *head; 
        while (temp->next!=NULL)
        {
            count++; 
            temp = temp->next; 
        }
        return count; 
    }
}
void Delete(struct Node** head,int n){
    int len = length(head); 
    if(len==0){
        printf("Empty"); 
        return; 
    }
    int count = len-n; 
    struct Node* temp = *head; 
    struct Node* prev; 
    for(int i = 0; i<count && temp->next!=NULL;i++){
        prev = temp; 
        temp = temp->next; 
    }
    prev->next = temp->next; 
    free(temp); 


}