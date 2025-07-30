class Node:
    def __init__(self,new_data):
        self.data = new_data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = Node(0)
        self.length = 0
    def search(self,value):
        curr = self.head.next
        while curr:
            if curr.data == value:
                return True
            curr = curr.next
        return False
    def insert(self,value):
        curr = self.head
        while curr.next:
            curr = curr.next
        a = Node(value)
        curr.next = a
        self.length += 1
    def ins(self,value):
        curr = self.head.next
        new_node = Node(value)
        new_node.next = curr
        self.head.next = new_node
        self.length += 1
    def reverse(self):
        prev = None
        curr = self.head.next
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        self.head.next = prev


    def display(self):
        curr = self.head.next  # skip dummy
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.ins(5)
ll.display()
print(ll.search(30))
print(ll.length)
ll.reverse()
ll.display()



        