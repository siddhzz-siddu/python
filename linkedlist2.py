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
 
 
def is_equal(llist1, llist2):
        current1 = llist1.head
        current2 = llist2.head
        while (current1 and current2):
            if current1.data <= current2.data:
                return False
            else:
                return True
            current1 = current1.next
            current2 = current2.next
        if current1 is None and current2 is None:
            return False
        else:
            return False
 
 
llist1 = LinkedList()
llist2 = LinkedList()
 
data_list = input('Please enter the elements in the first linked list: ').split()
for data in data_list:
    llist1.append(int(data))
 
data_list = input('Please enter the elements in the second linked list: ').split()
for data in data_list:
    llist2.append(int(data))
 
if is_equal(llist1, llist2):
    print('True')
else:
    print('False', end = '')