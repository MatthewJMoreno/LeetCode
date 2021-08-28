'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example:
  Input: head = [1,2,3,4,5], n = 2
  Output: [1,2,3,5]
'''
from ListNode import ListNode

def create_linked_list(n):
  head = ListNode
  cur_node = head

  for i in range(n):
    cur_node.next = ListNode(i)
    cur_node = cur_node.next
  
  return head.next

def print_linked_list(ll):
  output = []
  head = ll

  if head is None:
    return ''

  while head.next is not None:
    output.append(str(head.val))
    output.append(' -> ')

    head = head.next

  output.append(str(head.val))

  print(''.join(output))
  

def removeNthFromEnd(head, n):
  nodes = []
  cur_node = head

  while cur_node != None:
    nodes.append(cur_node)
    cur_node = cur_node.next

  length = len(nodes)

  if n == length:
    head = head.next
  elif n == 1:
    nodes[length - 2].next = None
  else:
    previous_node = nodes[length - n -1]
    nodes[length - n] = None
    next_node = nodes[length - n + 1]

    previous_node.next = next_node

  return head


head = create_linked_list(2)
print_linked_list(head)
head = removeNthFromEnd(head, 1)
print_linked_list(head)