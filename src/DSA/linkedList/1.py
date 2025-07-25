class Node:
    def __init__(self,new_data):
        self.data = new_data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = Node(0)
        self.length = 0

    def search(self, key):
        curr = self.head.next
        while curr:
            if curr.next:                
                print("cur node: ",curr.data)
                print("Next node data:", curr.next.data)
            else:
                print("Next node: None")

            if curr.data == key:
                return True
            curr = curr.next
        return False
    
    def insert(self,value):
        a = Node(value)
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = a
        self.length += 1

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
ll.display()
print(ll.search(30)) # True
#print(ll.search(40)) # False






