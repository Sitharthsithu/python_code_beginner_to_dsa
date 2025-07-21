class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
        
class linkedlist:
    def __init__(self):
        self.head=None
    
    def insert(self,data):
        node=Node(data,self.head)
        self.head=node
        
    def print(self):
        if self.head is None:
            print("array is empty")
            return
        
        itr=self.head
        llstr=itr.next
        while itr:
            llstr +=str(itr.data)+ '-->'
            itr=itr.next
            
        print(llstr)
        
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        
        itr=self.head
        while itr.next:
            itr=Node(data,None)
            
        def insert_values(self,data_list):
        
l1=linkedlist()
l1.insert(5)
l1.insert(33)