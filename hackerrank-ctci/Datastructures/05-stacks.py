'''
Stacks: Balanced Brackets
Medium
https://www.hackerrank.com/challenges/ctci-balanced-brackets/problem
'''

#!/bin/python3

brackets = {
    '{': '}',
    '[': ']',
    '(': ')'
}

def isBalanced(expression):
    stack = []
    for bracket in expression:
        if bracket in brackets.keys():
            stack.append(bracket)
        elif bracket in brackets.values() and len(stack) > 0 and brackets[stack[-1]] == bracket:
            stack.pop()
        else:
            return "NO"

    if len(stack) > 0:
        return "NO"

    return "YES"

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        expression = input()
        print(isBalanced(expression))