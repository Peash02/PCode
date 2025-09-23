class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end=" <-> ")
            temp = temp.next
        print("End")
    
    def iatb(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        
        node.next = self.head
        self.head.prev = node
        self.head = node

    def iate(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node
        node.prev = temp
        node.next = None

    def iatp(self,data,pos):
        node = Node(data)
        if self.head is None:
            print("List is Empty")
            return
        
        if pos < 1:
            print("POsition must be >=1")
            return
        if pos == 1:
            self.iatb(data)
            return
        
        temp = self.head
        count = 1
        while temp is not None and count < pos-1:
            temp = temp.next
            count+=1
        if temp is None:
            print("Position out of range")
            return
        node.next = temp.next
        node.prev = temp
        if temp.next:
            temp.next.prev = node
        temp.next = node
        node.prev = temp

    def deletion_at_beginning(self):
        if self.head is None:
            print("List is Empty")
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    def deletion_at_end(self):
        if self.head is None:
            print("List is Empty")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.prev.next = None

    def deletion_at_position(self,pos):
        if self.head is None:
            print("List is Empty")
            return
        if pos < 1:
            print("Position must be >=1")
            return
        if pos == 1:
            self.deletion_at_beginning()
            return
        temp = self.head
        count = 1
        while temp is not None and count < pos-1:
            temp = temp.next
            count+=1
        if temp is None:
            print("Position out of range")
            return
        temp.next = temp.next.next
        if temp.next is not None:
            temp.next.prev = temp

if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.iate(20)
    dll.iate(40)
    dll.iate(60)
    dll.display()

    dll.iatb(10)
    dll.display()

    dll.iatp(30,3)
    dll.iatp(50,5)
    dll.display()

    dll.deletion_at_beginning()
    dll.display()

    dll.deletion_at_end()
    dll.display()

    dll.deletion_at_position(2)
    dll.display()