# Node class for BST
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

# BST class
class BST:
    def __init__(self):
        self.root = None

    # Insert a new key
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.data:
            node.left = self._insert(node.left, key)
        elif key > node.data:
            node.right = self._insert(node.right, key)
        return node

    # Search for a key
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.data == key:
            return node
        if key < node.data:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    # Inorder traversal (Left, Root, Right)
    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.data, end=" ")
            self._inorder(node.right)

# Example usage
bst = BST()
elements = [50, 30, 70, 20, 40, 60, 80]
for el in elements:
    bst.insert(el)

print("Inorder traversal of BST:")
bst.inorder()

key = 60
found = bst.search(key)
if found:
    print(f"\nElement {key} found in BST.")
else:
    print(f"\nElement {key} not found in BST.")
