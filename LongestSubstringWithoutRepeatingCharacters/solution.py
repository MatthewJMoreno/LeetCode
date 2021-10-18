"""
Given a string s, find the length of the longest substring without repeating characters.
"""
import unittest

def lengthOfLongestSubstring(s):
  max_len = 0
  n = len(s)
  start_pointer = 0
  seen_letters = {}

  for i, letter in enumerate(s):
    if letter not in seen_letters:
      seen_letters[letter] = i

    # if we have encountered a letter thats already in seen_letters
    # but was last seen before the start_pointer, that must meen we
    # haven't seen that letter in our current window.
    elif letter in seen_letters and seen_letters[letter] < start_pointer:
      seen_letters[letter] = i
    else:
      max_len = max(max_len, i - start_pointer)
      start_pointer = max(start_pointer + 1, seen_letters[letter] + 1)
      seen_letters[letter] = i
  
  return max(max_len, n - start_pointer)

class TestSubstrSolution(unittest.TestCase):
  def test_len(self):
    test_1 = 'a'
    test_2 = 'aaaa'
    test_3 = 'abab'
    test_4 = 'abcdabcde'
    test_5 = 'abcdefg'
    test_6 = 'aaadvdaqc'

    test_1_expected = 1
    test_2_expected = 1
    test_3_expected = 2
    test_4_expected = 5
    test_5_expected = 7
    test_6_expected = 5

    test_1_actual = lengthOfLongestSubstring(test_1)
    test_2_actual = lengthOfLongestSubstring(test_2)
    test_3_actual = lengthOfLongestSubstring(test_3)
    test_4_actual = lengthOfLongestSubstring(test_4)
    test_5_actual = lengthOfLongestSubstring(test_5)
    test_6_actual = lengthOfLongestSubstring(test_6)

    self.assertEqual(test_1_expected, test_1_actual)
    self.assertEqual(test_2_expected, test_2_actual)
    self.assertEqual(test_3_expected, test_3_actual)
    self.assertEqual(test_4_expected, test_4_actual)
    self.assertEqual(test_5_expected, test_5_actual)
    self.assertEqual(test_6_expected, test_6_actual)

unittest.main()

test_1 = 'a'
test_2 = 'aaaa'
test_3 = 'abab'
test_4 = 'abcdabcde'
test_5 = 'abcdefg'
test_6 = 'aaadvdaqc'

lengthOfLongestSubstring(test_6)
