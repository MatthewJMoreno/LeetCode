'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example:
  Input: head = [1,2,3,4,5], n = 2
  Output: [1,2,3,5]
'''
from .. import ListNode

def removeNthFromEnd(head, n):
  visited = []
  cur_node = head

  while cur_node != None:
    visited.append(cur_node)

    cur_node = cur_node.next
  
  print(len(visited))

test = ListNode(23)
print(test.val)