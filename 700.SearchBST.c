#include <stdio.h>

struct tree{
    int data; 
    struct tree* right; 
    struct tree* left; 
};

struct tree* Search(struct tree* root, int data){
    if(root==NULL){
        return NULL; 
    }
    if(root->data==data){
        return root; 
    }
    struct tree* found = Search(root->left, data);
    if (found != NULL) 
        {return found;} 

    return Search(root->right,data); 
    
}

