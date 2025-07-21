class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new

    def display(self):
        cur = self.head
        while cur:
            print(cur.data,end=" ")
            cur = cur.next
            
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()
