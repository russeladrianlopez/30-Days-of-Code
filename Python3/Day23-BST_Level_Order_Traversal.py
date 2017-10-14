'''
Day 23: BST Level-Order Traversal
Task:
A level-order traversal, also known as a breadth-first search, visits each
level of a tree's nodes from left to right, top to bottom. You are given a
pointer, root, pointing to the root of a binary search tree. Complete the
levelOrder function provided in your editor so that it prints the level-order
traversal of the binary search tree.

Hint: You'll find a queue helpful in completing this challenge.

Sample Input:
6
3
5
4
7
2
1

Sample Output:
3 2 5 1 4 7
'''

import sys


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

    def levelOrder(self, root):
            # Write your code here

        if root:
            queue = [root]
            while queue:
                node = queue.pop()
                print(node.data, end=" ")
                if node.left:
                    queue.insert(0, node.left)
                if node.right:
                    queue.insert(0, node.right)


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
myTree.levelOrder(root)
