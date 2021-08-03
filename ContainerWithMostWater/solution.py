'''
Given n non-negative integers a1, a2, ..., an , 
where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of 
the line i is at (i, ai) and (i, 0). Find two lines, which, 
together with the x-axis forms a container, such that the container 
contains the most water.
'''

"""
Domain Partition:
  The set of all inputs can be broken up into 3 main sets:
    1. The solution contains the boundaries
    2. The solution contains only one of the boundaries
    3. The solution doesn't contain the boundaries
"""
def find_most_water(data):
  start = 0
  end = len(data) - 1
  base = end
  area = 0

  while start < end:
    height = min(data[start], data[end])
    if base * height > area:
      area =  base * height
    
    if data[start] > data[end]:
      end -= 1
    else:
      start += 1
    
    base -= 1
  
  return area
    

tests = {
  25: [5,2,1,3,6,5],
  36: [6,3,1,1,20,20,7],
  10: [10,10,1],
  4: [1,4,5],
  30: [5,3,2,15,2,15,3],
  1: [1,1],
  16: [4,3,2,1,4],
  2: [1,2,1]
}

for key, val in tests.items():
  print(find_most_water(val))