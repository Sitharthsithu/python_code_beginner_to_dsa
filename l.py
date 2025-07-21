class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def append(self,data):
        newnode=Node(data)
        if head is None:
            head=newnode
        else:
            currnode=head
            while currnode.next:
                currnode=currnode.next
            currnode.next=nn
        
a=SLL()
a.append(5)
print(a)