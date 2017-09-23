'''
Day 15: Linked List
Task:
Complete the insert function in your editor so that it creates a new Node
(pass date as the Node constructor argument) and inserts it at the tail of the
linked list referenced by the head parameter. Once the new node is added,
return the reference to the head node.

Your insert function should return a reference to the  node of the linked list.

Sample Input:
The first line contains T, the number of test cases.
The T subsequent lines of test cases each contain an integer to be inserted
at the list's tail.
4
2
3
4
1

Sample Output:
2 3 4 1

Explanation:
T = 4, so the locked code in the editor will be inserting 4 nodes.
The list is initially empty, so head is null; accounting for this, our code
returns a new node containing the data value 2 as the head of our list.
We then create and insert nodes 3, 4, and 1 at the tail of our list.
The resulting list returned by the last call to insert is [2,3,4,1] ,
so the printed output is 2 3 4 1.
'''


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        # Complete this method
        n = Node(data)

        if not head:
            head = n
        else:
            current = head
            while current.next:
                current = current.next
            current.next = n
        return head


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head)
