from binary_search_tree import BST, Node

class AVLNode(Node):
  def __init__(self, value):
    super().__init__(value)

    self.height    = 1
    self.imbalance = 0

  def calculate_height_and_imbalance(self):
    left_height  = self.left_child.height  if self.left_child  is None else 0
    right_height = self.right_child.height if self.right_child is None else 0
    
    self.height    = 1 + max(left_height, right_height)
    self.imbalance = left_height - right_height

  
