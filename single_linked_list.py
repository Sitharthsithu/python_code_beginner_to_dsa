class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
  
  
  
class LinkedList:
    def __init__(self):
        self.head=None
        
    def insert(self,data):
        new_node=Node(data)  #node(10)
        if self.head is None:
            self.head=new_node
            return
        current=self.head #10
        while current.next: #20
            current=current.next #10=>20 
        current.next=new_node
        
    def display(self):
        current=self.head
        while current:
            print(current.data,end="=>")
            current=current.next
        print("None")


#object=n
#linkedlist=class
n=LinkedList()
#object.function(data)
n.insert(10)
n.insert(20)
n.insert(30)

n.insert(40)
n.display()

