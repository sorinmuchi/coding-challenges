'''
Strings: Making Anagrams
Easy
https://www.hackerrank.com/challenges/ctci-making-anagrams/problem
'''

#!/bin/python3

import os
import collections

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    a = collections.Counter([x for x in a])
    b = collections.Counter([x for x in b])
    a.subtract(b)
        
    return sum([abs(x) for x in a.values()])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a = input()
    b = input()

    res = makeAnagram(a, b)
    fptr.write(str(res) + '\n')
    fptr.close()
