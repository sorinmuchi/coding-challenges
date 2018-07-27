'''
Linked Lists: Detect a Cycle
Easy
https://www.hackerrank.com/challenges/ctci-linked-list-cycle/problem
'''

"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    one_step = head
    two_step = head
    
    while one_step.next and two_step.next and two_step.next.next:
        if(one_step == two_step):
            return True

        one_step = one_step.next
        two_step = two_step.next.next
        
    return False
        