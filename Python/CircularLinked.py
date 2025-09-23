class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class CircularLinked:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("List is Empty")
            return
        temp = self.head
        while True:
            print(temp.data,end=" <-> ")
            temp = temp.next
            if temp == self.head:
                break
        print("HEAD")
    
    def iatb(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.head.prev = node
            self.head.next = node
            return
        
        node.next = self.head
        node.prev = self.head.prev
        self.head.prev.next = node
        self.head = node

    def iate(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.head.prev = node
            self.head.next = node
            return
        
        self.head.prev.next = node
        node.prev = self.head.prev
        node.next = self.head
        self.head.prev = node

    def deletion_at_beginning(self):
        if self.head is None:
            print("List is Empty")
            return
        if self.head.next == self.head:
            self.head = None
            return
        self.head.prev.next = self.head.next
        self.head.next.prev = self.head.prev
        self.head = self.head.next

    def deletion_at_end(self):
        if self.head is None:
            print("List is Empty")
            return
        if self.head.next == self.head:
            self.head = None
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.prev.next = self.head
        self.head.prev = temp.prev

if __name__ == "__main__":
    cll = CircularLinked()
    
    cll.iatb(10)
    cll.display()

    cll.iate(20)
    cll.iate(30)
    cll.iate(40)
    cll.display()

    cll.deletion_at_beginning()
    cll.display()

    cll.deletion_at_end()
    cll.display()

