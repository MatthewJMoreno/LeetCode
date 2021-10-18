'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example:
  Input: head = [1,2,3,4,5], n = 2
  Output: [1,2,3,5]
'''
from ListNode import ListNode

def create_ll(n):
  head = ListNode()
  cur_node = head

  for i in range(n):
    cur_node.next = ListNode(i + 1)
    cur_node = cur_node.next

  return head.next

def print_ll(head):
  if head == None:
    return ''

  string = []
  string.append(str(head.val))

  cur_node = head.next

  while cur_node != None:
    string.append(' -> ')
    string.append(str(cur_node.val))
    cur_node = cur_node.next
  
  return ''.join(string)


class Solution:
  def len_of_ll(self, head):
    count = 0
    cur_node = head

    while cur_node != None:
      count += 1
      cur_node = cur_node.next
    
    return count

  def removeNthFromEnd(self, head, n):
    ll_len = self.len_of_ll(head)
    
    if ll_len == 1:
      return None
    
    if n == ll_len:
      return head.next
    
    num_iters = ll_len - n - 1
    slow_pointer = head
    fast_pointer = head.next

    for i in range(num_iters):
      slow_pointer = slow_pointer.next
      fast_pointer = fast_pointer.next
    
    slow_pointer.next = fast_pointer.next
    fast_pointer = None

    return head

sol = Solution()
test_1 = create_ll(1)
test_2 = create_ll(5)
test_3 = create_ll(5)
test_4 = create_ll(2)

print(f'll before: {print_ll(test_1)}')
test_1_result = sol.removeNthFromEnd(test_1, 1)
print(f'll after: {print_ll(test_1_result)}')

print()

print(f'll before: {print_ll(test_2)}')
test_2_result = sol.removeNthFromEnd(test_2, 5)
print(f'll after: {print_ll(test_2_result)}')

print()

print(f'll before: {print_ll(test_3)}')
test_3_result = sol.removeNthFromEnd(test_3, 4)
print(f'll after: {print_ll(test_3_result)}')

print()

print(f'll before: {print_ll(test_4)}')
test_4_result = sol.removeNthFromEnd(test_4, 2)
print(f'll after: {print_ll(test_4_result)}')