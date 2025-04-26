# Binary Search Tree (BST) Implementation in Python

This project implements a simple **Binary Search Tree** (BST) with two main methods:
- `insert(value)`: Adds a new node to the tree.
- `contains(value)`: Checks if a value exists in the tree.

---

## Classes

### Node
A helper class to create tree nodes.
- `value`: The value stored in the node.
- `left`: Pointer to the left child node.
- `right`: Pointer to the right child node.

### BinarySearchTree
The main BST class to manage nodes.
- `root`: The top node of the tree (initially `None`).

**Methods:**
- `insert(value)`: 
  - Inserts a value into the BST.
  - Returns `True` if inserted successfully.
  - Returns `False` if the value already exists.

- `contains(value)`:
  - Returns `True` if the value is found.
  - Returns `False` otherwise.

---

## Example Usage

```python
# Create a BST instance
bst = BinarySearchTree()

# Insert values
bst.insert(10)  # True
bst.insert(5)   # True
bst.insert(15)  # True
bst.insert(10)  # False (duplicate)

# Check for values
bst.contains(10)  # True
bst.contains(5)   # True
bst.contains(15)  # True
bst.contains(20)  # False
```

---

## How to Run

1. Save the code into a `.py` file (e.g., `bst.py`).
2. Run the file using Python:

```bash
python bst.py
```

---

## Notes

- This is a basic BST and does **not** handle balancing (like AVL or Red-Black Trees).
- Good for learning purposes or small projects!

---
