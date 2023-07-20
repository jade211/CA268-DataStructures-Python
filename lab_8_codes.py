# #!/usr/bin/env python3

# # QUESTION 1 ~ Worked on by Jade Hudson and Sruthi Santhosh
# class HashTable:
#     number_elements = 0

#     def __init__(self, n): # ): int = 1):
#         """
#         Create storage for a HashTable with `n` entries.
#         """
#         self.n = n
#         self.store = [[] for i in range(self.n)]

#     def getindex(self, key) -> int:
#         """Get the index corresponding to the given `key`"""
#         _hash = hash(key)
#         return _hash % self.n

#     def put(self, key, value):
#         index = self.getindex(key)
#         found = False

#         for idx, element in enumerate(self.store[index]):
#             if len(element) == 2 and element[0] == key:
#                 self.store[index][idx] = (key, value) # element[1] = value
#                 found = True
#                 break
#         if not found:
#             self.store[index].append((key, value))
#         self.number_elements += 1


#     def get(self, key):
#         """
#         Retrieve the value at the index given by `key`, or `None`.
#         """
#         index = self.getindex(key)
#         return self.store[index]

#     def delete(self, key):
#         """
#         Remove the data at the index `key`, if it exists.
#         """
#         index = self.getindex(key)
#         if self.store[index] is not None:
#             self.number_elements -= 1
#             self.store[index] = None



# h = HashTable(20)
# h.put('DCU', 'D9')
# h.put('TCD', 'D2')
# h.put('UCD', 'D4')

# print(h.getindex('DCU'))
# print(h.get('TCD'))
# h.put('DCU', 'D100')
# print(h.getindex('DCU'))

# h.delete('UCD')
# print(h.get('UCD'))
# print(h.get('DCU'))
# h.put('DCU', 'D111')
# print(h.getindex('DCU'))
# print(h.get('DCU'))

# h.put('DCU', 'D333')
# print(h.getindex('DCU'))
# print(h.get('DCU'))

# h.put('DCU', 'D444')
# print(h.getindex('DCU'))
# print(h.get('DCU'))
# print(h.store)









###########################################
# TREE CODE
class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
   def PrintTree(self):
      print(self.data)

root = Node(10)
# root.PrintTree()



######################

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild= None


node1 = BinaryTreeNode(50)  # root
node2 = BinaryTreeNode(20)  # parent 1 (previously child 1)
node3 = BinaryTreeNode(45)  # parent 2  (previoudly child 2)
node4 = BinaryTreeNode(11)  # child 1
node5 = BinaryTreeNode(15)  # child 2
node6 = BinaryTreeNode(30)  # child 1
node7 = BinaryTreeNode(78)  # child 2

node1.leftChild = node2
node1.rightChild = node3
node2.leftChild = node4
node2.rightChild = node5
node3.leftChild = node6
node3.rightChild = node7

print("Root Node is:")
print(node1.data)

print("left child of the node is:")
print(node1.leftChild.data)

print("right child of the node is:")
print(node1.rightChild.data)

print("Node is:")
print(node2.data)

print("left child of the node is:")
print(node2.leftChild.data)

print("right child of the node is:")
print(node2.rightChild.data)

print("Node is:")
print(node3.data)

print("left child of the node is:")
print(node3.leftChild.data)

print("right child of the node is:")
print(node3.rightChild.data)

print("Node is:")
print(node4.data)

print("left child of the node is:")
print(node4.leftChild)

print("right child of the node is:")
print(node4.rightChild)

print("Node is:")
print(node5.data)

print("left child of the node is:")
print(node5.leftChild)

print("right child of the node is:")
print(node5.rightChild)

print("Node is:")
print(node6.data)

print("left child of the node is:")
print(node6.leftChild)

print("right child of the node is:")
print(node6.rightChild)

print("Node is:")
print(node7.data)

print("left child of the node is:")
print(node7.leftChild)

print("right child of the node is:")
print(node7.rightChild)


##########################

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
 
def height(root):
 
    # Check if the binary tree is empty
    if root is None:
        # If TRUE return 0
        return 0 
    # Recursively call height of each node
    leftAns = height(root.left)
    rightAns = height(root.right)
 
    # Return max(leftHeight, rightHeight) at each iteration
    return max(leftAns, rightAns) + 1
 
# Test the algorithm
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
 
print("Height of the binary tree is: " + str(height(root)))




