

def find_sum(root):
  if root == None:
    return 0
  return root.data + find_sum(root.left) + find_sum(root.right)