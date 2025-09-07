#include <stdio.h> 
#include <stdlib.h> 

struct Node{
    int data; 
    struct Node* link; 
}; 
//this is to create a node 
struct Node* createNode(int x){
    struct Node* newnode = (struct Node*)malloc(sizeof(struct Node)); 
    newnode->data = x; 
    newnode->link = NULL; 
    return newnode; 
}
//we only need insert at end
void InsertEnd(struct Node**head, int x){
    struct Node* newnode = createNode(x); 
    if(*head==NULL){
        *head= newnode; 
        return;
    }
    struct Node* temp = *head; 
    while(temp->link!=NULL){
        temp = temp->link; 
    }
    temp->link = newnode; 
}

void Display(struct Node** head){
    if(*head == NULL){
        printf("Empty list\n"); 
        return; 
    }
    struct Node* temp = *head; 
    while (temp->link!=NULL)
    {
        printf("%d->",temp->data); 
        temp = temp->link; 
    }
    printf("%d\n", temp->data); 
}
int Count(struct Node**head){
    int count = 0; 
    struct Node* temp = *head; 
    while (temp->link!=NULL)
    {
        count+=1; 
        temp=temp->link; 
    }

    return count; 
    
    
}
//head1->L1, head2->L2, head->final
void Merge(struct Node**head1, struct Node**head2, struct Node**head){
    struct Node* temp1 = *head1; 
    struct Node* temp2 = *head2; 
    struct Node* temp = *head; 
    while (temp1->link!=NULL)
    {
        if(temp1->data==temp2->data){
            
        }
    }
    

}
int main(){
    struct Node* L1 = NULL; 
    struct Node* L2 = NULL; 

    InsertEnd(&L1,1); 
    InsertEnd(&L1,2); 
    InsertEnd(&L1,4); 

    
    InsertEnd(&L2,1); 
    InsertEnd(&L2,3); 
    InsertEnd(&L2,4); 


    Display(&L1); 
    Display(&L2); 


}

