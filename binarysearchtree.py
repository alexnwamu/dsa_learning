
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)
    def search(self,find_val):
        return self.search_helper(self.root,find_val)
    
    def insert(self,new_val):
        return self.insert_helper(self.root,new_val)
    
    def insert_helper(self, node, new_val):
        if new_val < node.value:
            if node.left is None:
                node.left = Node(new_val)
            else:
                self.insert_helper(node.left, new_val)
        else:
            if node.right is None:
                node.right = Node(new_val)
            else:
                self.insert_helper(node.right, new_val)
    
    def search_helper(self,start, find_val):
        if start:
            if start.value is find_val:
                return True
        if start.left and find_val < start.value:
            return self.search_helper(start.left ,find_val)
        if start.right and find_val > start.value:
            return self.search_helper(start.right ,find_val)
        return False
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print (tree.search(4))
# Should be False
print (tree.search(6))