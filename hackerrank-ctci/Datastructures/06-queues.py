'''
Queues: A Tale of Two Stacks
Medium
https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem
'''

class MyQueue(object):

    def __init__(self):
        self.normal = []
        self.inverse = []
    
    def peek(self):
        if (self.inverse):
            return self.inverse[-1]
        else:
            return self.normal[0]
        
    def pop(self):
        if (self.inverse):
            element = self.inverse[-1]
            self.inverse = self.inverse[0:-1]
            return element
        else:
            self.inverse = []
            for e in reversed(self.normal):
                self.inverse.append(e)
            self.normal = []
            self.pop()
        
    def put(self, value):
        self.normal.append(value)


queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())