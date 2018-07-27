'''
Trees: Is This a Binary Search Tree?
Medium
https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem
'''

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    return boundedCheck(root, -1, 10001)
    
def boundedCheck(root, minV, maxV):
    if root is None:
        return True
    if minV >= root.data or root.data >= maxV:
        return False
    return boundedCheck(root.left, minV, root.data) and boundedCheck(root.right, root.data, maxV)