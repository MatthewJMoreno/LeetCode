"""
An n-bit gray code sequence is a sequence of 2n integers where:

Every integer is in the inclusive range [0, 2n - 1],
The first integer is 0,
An integer appears no more than once in the sequence,
The binary representation of every pair of adjacent integers differs by exactly one bit, and
The binary representation of the first and last integers differs by exactly one bit.
Given an integer n, return any valid n-bit gray code sequence.
"""

def determine_neighbore(index, offset, used_numbers, gray_sequence, n):
  # generate a list of all numbers that differ from unused_numbers[index] by 1 bit
  # exclude the numbers that we have already used
  # take the smallest one
  valid_neighbores = [gray_sequence[index] ^ (1 << x) for x in range(n) if used_numbers[(gray_sequence[index] ^ (1 << x))] == 0]
  if len(valid_neighbores) == 0:
    print("all nums: {}".format([gray_sequence[index] ^ (1 << x) for x in range(n)]))
    print("index: {}".format(index))
    print("offset: {}".format(offset))
    print("used numbers: {}".format(used_numbers))
    print("gray sequence {}".format(gray_sequence))
    print("n: {}".format(n))
    print("valid neighbores: {}".format(valid_neighbores))
  neighbore = min([(gray_sequence[index] ^ (1 << x)) for x in range(n) if used_numbers[(gray_sequence[index] ^ (1 << x))] == 0])
  
  gray_sequence[index + offset] = neighbore
  used_numbers[neighbore] = 1

def determine_neighbore_test(index, n):
  used_numbers = {x:0 for x in range(2 ** n)}

  start = 0
  end = 2 ** n - 1

  gray_sequence = [0 for x in range(2 ** n)]
  gray_sequence[start] = 0
  gray_sequence[end] = 1

  used_numbers[gray_sequence[start]] = 1
  used_numbers[gray_sequence[end]] = 1
  #print("used_numbers[index]: {}".format(used_numbers[start]))

  #print([(gray_sequence[start] ^ (1 << x)) for x in range(n) if used_numbers[(gray_sequence[start] ^ (1 << x))] == 0])  #determine_neighbore(0, 1, used_numbers, gray_sequence)
  #print(gray_sequence)
  #print("used numbers {}".format(used_numbers))

  determine_neighbore(start, 1, used_numbers, gray_sequence, n)
  #print("used numbers {}".format(used_numbers))

  determine_neighbore(end, -1, used_numbers, gray_sequence, n)
  #print("used numbers {}".format(used_numbers))
  start += 1
  end -= 1

  determine_neighbore(start, 1, used_numbers, gray_sequence, n)
  #print("used numbers {}".format(used_numbers))

  determine_neighbore(end, -1, used_numbers, gray_sequence, n)
  #print("used numbers {}".format(used_numbers))
  start += 1
  end -= 1

  determine_neighbore(start, 1, used_numbers, gray_sequence, n)
  #print("used numbers {}".format(used_numbers))

  determine_neighbore(end, -1, used_numbers, gray_sequence, n)
  #print("used numbers {}".format(used_numbers))
  start += 1
  end -= 1

  #print(gray_sequence)

# given two numbers, a and b, determine how many bits they differ
def hamming_distance(a, b, n):
  count = 0

  for i in range(n):
    if not((a >> i) & 1 == (b >> i) & 1):
      count += 1
  
  return count

# determine_neighbore_test(0, 3)
def is_gray_code(gray_code, n):
  if gray_code[0] != 0:
    return False
  
  if hamming_distance(gray_code[0], gray_code[len(gray_code) - 1], n) != 1:
    return False
  
  for i in range(len(gray_code) - 1):
    if hamming_distance(gray_code[i], gray_code[i+1], n) != 1:
      return False
  
  return True

def gray_code(n):
  # all nums start out unused, flip value to 1 once placed in gray_sequence
  used_numbers = { x:0 for x in range(2 ** n) }
  gray_sequence = [ 0 for x in range(2 ** n) ]

  #start from both ends of gray_sequence, filling it in at the ends, working
  #our way towards the middle
  start = 0
  end = (2 ** n) - 1

  gray_sequence[start] = 0
  gray_sequence[end] = 1

  used_numbers[gray_sequence[start]] = 1
  used_numbers[gray_sequence[end]] = 1
  
  while True:
    if start + 1 > end - 1:
      break;

    determine_neighbore(start, 1, used_numbers, gray_sequence, n)
    start += 1

    determine_neighbore(end, -1, used_numbers, gray_sequence, n)
    end -= 1
  
  return gray_sequence


n=5
print(gray_code(n))
print(is_gray_code(gray_code(n), n))