'''
Implement a singly linked list that does the following
    - keeps track of the start
    - Can add a new node to the end of the linked list
    - Can insert a new node anywhere front or back
    - Can delete a node
    - Can print out the entire linked list
'''

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
    
    def add(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
            self.head.next = self.tail
        else:
            self.tail.next = node
            self.tail = node
        
        self.length += 1
            
    
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
            result.append(' -> ')
            result.append(str(curr_node))
            curr_node = curr_node.next
        
        return ''.join(result)

node_1 = Node(-11)
node_2 = Node(13)
node_3 = Node(5)
node_4 = Node(134)
node_5 = Node(2343)


ll = LinkedList()

ll.add(node_1)
test_1 = ll.get_head()
print(f"test_1: {test_1}")

ll.add(node_2)
test_2 = test_1.next
print(f"test_2: {test_2}")

ll.add(node_3)
print(ll)
print(f'length: {ll.get_length()}')

ll.add(node_4)
ll.add(node_5)
print(f'length: {ll.get_length()}')

print(ll)
result = ll.find(42)
if result is None:
    print("42 not found")
else:
    print(result)