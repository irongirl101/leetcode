#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* link;
};

struct Node* createNode(int data) {
    struct Node* newnode = (struct Node*)malloc(sizeof(struct Node));
    newnode->data = data;
    newnode->link = NULL;
    return newnode;
}

void insertHead(struct Node** head, int data) {
    struct Node* newnode = createNode(data);
    newnode->link = *head;
    *head = newnode;
}
void display(struct Node* head) {
    struct Node* temp = head;
    while (temp != NULL) {
        printf("%d->", temp->data);
        temp = temp->link;
    }
    
}
void TwoSum(struct Node** head1,struct Node** head2){
    struct Node* temp1 = *head1; 
    struct Node* temp2 = *head2; 
    struct Node*temp = NULL; 
    while(temp1!=NULL || temp2!=NULL){
        int carry = 0; 
        int sum_no_carry = temp1->data+temp2->data; 
        if(sum_no_carry>=10){
            int carry = sum_no_carry/10; 
            //int sum = 
            //insertHead(&temp,); 
        }
        else{
            int sum = sum_no_carry+carry; 
            insertHead(&temp,sum_no_carry); 
        }
        temp1=temp1->link; 
        temp2=temp2->link; 
    }
    display(temp); 
}


int main() {
    struct Node* head1 = NULL;
    struct Node* head2 = NULL;

    insertHead(&head1, 3);
    insertHead(&head1, 4);
    insertHead(&head1, 2);
    display(head1);
    printf("\n"); 
    insertHead(&head2, 4); 
    insertHead(&head2, 6); 
    insertHead(&head2, 5); 
    display(head2); 
    printf("\n");

    TwoSum(&head1,&head2); 


    return 0; 
}