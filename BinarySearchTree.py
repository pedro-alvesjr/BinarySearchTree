class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
            new_node = Node(value)
            if self.root == None:
                self.root = new_node
                return True
            temp = self.root
            while True:
                if new_node.value == temp.value:
                    return False
                if new_node.value < temp.value:
                    if temp.left == None:
                        temp.left = new_node
                        return True
                    temp = temp.left
                else:
                    if temp.right == None:
                        temp.right = new_node
                        return True
                    temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

# Create a new BinarySearchTree instance
bst = BinarySearchTree()

# Test insert
print(bst.insert(10))  # Should print True (tree was empty)
print(bst.insert(5))   # Should print True (5 inserted to the left)
print(bst.insert(15))  # Should print True (15 inserted to the right)
print(bst.insert(10))  # Should print False (10 already exists)

# Test contains
print(bst.contains(10))  # Should print True
print(bst.contains(5))   # Should print True
print(bst.contains(15))  # Should print True
print(bst.contains(20))  # Should print False (20 not in tree)
