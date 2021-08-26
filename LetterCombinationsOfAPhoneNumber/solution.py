'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
'''

def dfs_letter_combinations(phone_number, phone_book, words, word, depth):
  if depth == len(phone_number):
    words.append(word)
    return
  
  chars = phone_book[int(phone_number[depth])]

  for char in chars:
    word += char
    dfs_letter_combinations(phone_number, phone_book, words, word, depth + 1)
    word = word[ :len(word) - 1]

def letter_combinations(phone_number):
  if len(phone_number) == 0:
    return []
    
  phone_book = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
  words = []
  word = ''
  depth = 0

  dfs_letter_combinations(phone_number, phone_book, words, word, depth)
  
  return words


letter_combinations('23')
letter_combinations('2')
letter_combinations('')