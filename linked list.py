# include<bits/stdc++.h>
using namespace std;

class Name{
    public:
    string name1;
    int age1; 
       
    Name* prev;
    Name* next;

    // creating constructor
    Name(string d, int a){
        this-> name1 = d;
        this-> age1 = a;
        this->prev = NULL;
        this-> next = NULL;
        
    }  
    };
// function to connect the nodes in the linked list.
void connectNode(Name* &node1, Name* &node2, Name* &node3){

    node1->prev = NULL; 
    node1->next = node2;
    node2->next = node3;
    node2->prev = node1;
    node3->next = NULL;
    node3->prev = node2;   
};

// function to print the node.

void print(Name* node1){
    Name* temp = node1;

    while(temp!= NULL){
        cout << temp->name1 << " "; 
        cout  << temp->age1 << endl;
        temp = temp->next;
        }
};

int main(){
    Name* node1 = new Name("Manoj",48);
    Name* node2 = new Name("Babita ",45);
    Name* node3 = new Name("Gourav",19);

    connectNode(node1,node2,node3);
  
    
   print(node1);

   return 0;   

}