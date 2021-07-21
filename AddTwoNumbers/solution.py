"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def add_two_numbers(l1, l2):
  sum_list = ListNode()
  sum_list_head = sum_list
  quotient = 0

  l1_head = l1
  l2_head = l2

  while l1_head != None and l2_head != None:
    sum = l1_head.val + l2_head.val + quotient
    quotient = sum // 10
    remainder = sum % 10

    sum_list_head.next = ListNode(remainder)
    sum_list_head = sum_list_head.next
    
    l1_head = l1_head.next
    l2_head = l2_head.next
  
  while l1_head != None:
    sum = l1_head.val + quotient
    quotient = sum // 10
    remainder = sum % 10
    sum_list_head.next = ListNode(remainder)
    sum_list_head = sum_list_head.next
    l1_head = l1_head.next

  while l2_head != None:
    sum = l2_head.val + quotient
    quotient = sum // 10
    remainder = sum % 10
    sum_list_head.next = ListNode(remainder)
    sum_list_head = sum_list_head.next
    l2_head = l2_head.next
  
  if quotient == 1:
    sum_list_head.next = ListNode(1)
  
  return sum_list.next


def add_two_nums_test():
  l1 = ListNode()
  l1_head = l1

  l2 = ListNode()
  l2_head = l2

  l1_head.next = ListNode(3)
  l2_head.next = ListNode(7)
  l1_head = l1_head.next
  l2_head = l2_head.next

  l1_head.next = ListNode(1)
  l2_head.next = ListNode(2)
  l1_head = l1_head.next
  l2_head = l2_head.next

  l1_head.next = ListNode(2)
  l2_head.next = ListNode(5)
  l1_head = l1_head.next
  l2_head = l2_head.next

  result = add_two_numbers(l1.next, l2.next)
  while result != None:
    #print(result.val)
    result = result.next
  
add_two_nums_test()

  