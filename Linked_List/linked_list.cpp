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
				if(itr==tail){
					cout<<"INDEX OVERFLOW!";
					break;
					}
				} // going till the second last node
				delete tail; //delete the last node 
				tail=itr; //updating tail
				tail->next=NULL; //updating tail next
			
			}else{
			if(a==0){
				head=head->next;
				}else{ 
					itr=head;
					for(int index=1;index!=a;index++){
						itr = itr->next;
						if(itr==tail){
					cout<<"INDEX OVERFLOW!";
					break;
					} 	
					}
					itr->next=itr->next->next;			
			}	
		}
	}
	
	void insert(int data, int index){
		Node* itr=head;
		Node* temp;
		if(index==0){
			head=new Node;
			head->Data=data;
			head->next=itr;
		}else{
			for(int i=1;i!=index;i++){
				itr=itr->next;
				if(itr==tail){
					cout<<"INDEX OVERFLOW!";
					break;
					}
				}
				temp=itr;
				itr=itr->next;
				temp->next=new Node;
				temp=temp->next;
				temp->Data=data;
				temp->next=itr;
				
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
	a.del(1);
	a.insert(69,0);
	a.insert(143,0);
	a.print();
	a.insert(77,2);
	a.print();
	a.insert(999,8);
	return 0;
}
