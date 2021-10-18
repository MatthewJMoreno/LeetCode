'''
Implement a singly linked list that does the following
    - keeps track of the start
    - Can add a new node to the end of the linked list
    - Can insert a new node anywhere front or back
    - Can delete a node
    - Can print out the entire linked list
'''

from typing import final


class Node():
    def __init__(self, val = -1):
        self.next = None
        self.val = val
    
    def __str__(self):
        return str(self.val)

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def get_head(self):
        return self.head
    
    def get_tail(self):
        return self.tail
    
    def get_length(self):
        return self.length
    
    def insert_into_empty_list(self, node):
        self.head = node
        self.tail = node
        self.head.next = self.tail
    
    def add(self, data):
        new_node = Node(data)
        if self.head == None:
            self.insert_into_empty_list(new_node)
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1
    
    def insert(self, data, index):
        if index < 0:
            raise ValueError('A negative index isn\'t allowed')
        
        if index >= self.length + 1:
            raise ValueError(f'The index must be in the range (inclusive) [{0}, {self.length}]')

        new_node = Node(data)

        if self.head is None:
            self.insert_into_empty_list(new_node)
            return True
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            print(self.head.val)
            return True
        
        if index == self.length:
            self.add(data)
            return True
    
    def find(self, val):
        curr_node = self.head

        while curr_node is not None:
            if curr_node.val == val:
                return curr_node
            
            curr_node = curr_node.next
        
        return None
    
    def __str__(self):
        result = []
        result.append(str(self.head))

        if self.head.next == None:
            return ''.join(result)
        
        curr_node = self.head.next

        while curr_node is not None:
            print(curr_node.val)
            result.append(' -> ')
            result.append(str(curr_node))
            curr_node = curr_node.next
        
        return ''.join(result)

node_1_data = -11
node_2_data = 13
node_3_data = 5
node_4_data = 134
node_5_data = 2343


ll = LinkedList()

ll.add(node_1_data)
test_1 = ll.get_head()
print(f"test_1: {test_1}")

ll.add(node_2_data)
test_2 = test_1.next
print(f"test_2: {test_2}")

ll.add(node_3_data)
print(ll)
print(f'length: {ll.get_length()}')

ll.add(node_4_data)
ll.add(node_5_data)
print(f'length: {ll.get_length()}')

print(ll)
result = ll.find(42)
if result is None:
    print("42 not found")
else:
    print(result)

try:
    ll.insert(node_2_data, -3)
except Exception as e:
    print(e)

try:
    ll.insert(node_2_data, 6)
except Exception as e:
    print(e)

empty_ll = LinkedList()
try:
    empty_ll.insert(node_2_data, 0)
except Exception as e:
    print(e)

try:
    ll.insert(node_3_data, 0)
except Exception as e:
    print(e)

print(ll)