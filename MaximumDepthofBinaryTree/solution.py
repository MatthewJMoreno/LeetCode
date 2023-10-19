class Solution(object):
  def traverse(self, node, depth):
    if node == None:
      return depth - 1
    
    lcd = self.traverse(node.left, depth + 1)
    rcd = self.traverse(node.right, depth + 1)

    if lcd > rcd:
      return lcd
      
    return rcd

  def maxDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    depth = self.traverse(root, 1)
    print(depth)

    return depth