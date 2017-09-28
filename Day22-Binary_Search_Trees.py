'''
Day 22: Binary Search Trees
Task:
The height of a binary search tree is the number of edges between the
tree's root and its furthest leaf. You are given a pointer, root, pointing
to the root of a binary search tree. Complete the getHeight function provided
in your editor so that it returns the height of the binary search tree.

Sample Input:
7
3
5
2
1
4
6
7

Sample Output:
3
'''


class Node:

    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:

    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def getHeight(self, root):
        # Write your code here
        left = 0
        right = 0
        if root:
            if root.left:
                left = 1 + self.getHeight(root.left)
            if root.right:
                right = 1 + self.getHeight(root.right)
        return max(left, right)


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
height = myTree.getHeight(root)
print(height)
