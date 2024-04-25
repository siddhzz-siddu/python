class Node:
    def _init_(self, data):
       self.data = data
       self.next = None
       
class LinkedList:
    def _init_(self):
        self.head = None
        self.last_node = None
        
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
 
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next
 
a_llist = LinkedList()
n = int(input('How many elements would you like to add? '))
l=[]
l1=[]
for i in range(n):
    data = int(input('Enter data item: '))
    a_llist.append(data)
    if data%5==0 and data!=0:
        l.append(data)
        l.sort(reverse=True)
    elif data%5!=0 or data==0:
        l1.append(data)
        l1.sort(reverse=True)

print(l+l1)