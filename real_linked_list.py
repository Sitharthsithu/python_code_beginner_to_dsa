class Node:
    def __init__(self,data):
        self.data=data #10     20     30
        self.next=None #<>     <>      none
        
node1=Node(10)
node2=Node(20)
node3=Node(30)
node1.next=node2
node2.next=node3
print(node1.data,node1.next)
print(node2.data,node2.next)
print(node3.data,node3.next)


current = node1  # start from the head
while current is not None:
    print(current.data)
    current = current.next
