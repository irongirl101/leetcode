#include <stdio.h>
#include <stdlib.h> 

struct Node{
    int data; 
    struct Node* link; 
}; 

struct Node* createNode(int data){
    struct Node* newnode = (struct Node*)malloc(sizeof(struct Node)); 
    newnode->data = data; 
    newnode->link = NULL; 
    return newnode; 
}
void insertHead(struct Node** head, int data){
    struct Node* newnode = createNode(data); 
    if(head==NULL){
        *head=newnode; 
    }
    newnode->link = *head; 
    *head = newnode; 
}

void TwoSum(struct Node** head1,struct Node** head2){
    struct Node* temp1 = *head1; 
    struct Node* temp2 = *head2; 
    struct Node**temp; 
    while(temp1->link!=NULL || temp2->link!=NULL){
        int sum_no_carry = temp1->data+temp2->data; 
        if(sum_no_carry>=10){
            int sum = sum_no_carry+1; 
            int add = sum%10; 
            insertHead(temp,add); 
        }
        else{
            int sum = sum_no_carry; 
            insertHead(temp,sum); 
        }
        temp1=temp1->link; 
        temp2=temp2->link; 
    }

}
int main(){




    return 0; 
}