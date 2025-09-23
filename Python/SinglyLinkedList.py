class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_position(self,data,position):
        if position < 1:
            print("Position must be >=1")
            return
        new_node = Node(data)

        if  position == 1:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        count = 1

        while current is not None and count < position-1:
            current = current.next
            count+=1
        
        if current is None:
            print("Position out of range")
            return
        
        new_node.next = current.next
        current.next = new_node

    def traverse(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while current:
            print(current.data,end=" -> ")
            current = current.next
        print("End")

    def deletion_at_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next

    def deletion_at_end(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        previous = None
        while current.next:
            previous = current
            current = current.next
        previous.next = None

    def deletion_at_position(self,position):
        if position < 1:
            print("Position must be >=1")
            return
        if position == 1:
            self.head = self.head.next
            return
        current = self.head
        count = 1
        while current is not None and count < position-1:
            current = current.next
            count+=1
        if current is None:
            print("Position out of range")
            return
        current.next = current.next.next

if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.append(20)
    ll.append(40)
    ll.append(60)
    ll.traverse()
    ll.insert_at_beginning(10)
    ll.insert_at_position(30,3)
    ll.insert_at_position(50,5)
    ll.traverse()
    ll.deletion_at_beginning()
    ll.traverse()
    ll.deletion_at_end()
    ll.traverse()
    ll.deletion_at_position(3)
    ll.traverse()
