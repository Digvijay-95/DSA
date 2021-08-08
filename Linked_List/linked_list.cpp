#include<iostream>
using namespace std;
class Node{
	public:
		int Data;
		Node *next;
};

class Linked_list: protected Node{
	
	private:
		Node* head; //HEAD pointer points to head
		Node* tail; //Tail pointer points to tail
	
	public:	
		Linked_list(int a){ //Creates the first node 
			head =new Node; //new node
			head->Data=a; //data initialized
			head->next=NULL; //next to null
			tail=head; //tail
			cout<<"successfully Done!"<<endl;
		}
		void append(int a){
			Node* temp;  //temperory pointers
			temp=new Node; //new node created
			tail->next=temp; // New node attached to previous
			tail=temp; //tail is now updated
			tail->Data=a; //data initialized
			tail->next=NULL; //next to null
			cout<<"Pushed Successfully!"<<endl;
		}
		void print(){
			Node* itr=head; //iterator initialized to head
			while(itr!=NULL){ 
				cout<<itr->Data<<'|';
				itr=itr->next; //jumping to next node
			}
			cout<<endl; //pushes cursor to next line, making free way for other methods
		}
		
		void del(int a=-1){
			Node* itr; //iterator pointer
			if(a==-1){
			for(itr=head;itr->next!=tail;itr=itr->next){
				} // going till the second last node
				delete tail; //delete the last node 
				tail=itr; //updating tail
				tail->next=NULL; //updating tail next
			
			}else{ 
				for(index=0;index!=a;index++){	
				}								
			
			
			}
			
		void insert(int data, int index){
			
			
			
			}
			
		
		}


};


int main(){
	Linked_list a(10);
	a.append(7);
	a.append(8);
	a.append(99);
	a.print();
	a.del();
	a.print();
	return 0;
}
