'''
Hash Tables: Ransom Note
Easy
https://www.hackerrank.com/challenges/ctci-ransom-note/problem
'''

#!/bin/python3
import collections

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    m = collections.Counter(magazine)
    n = collections.Counter(note)
    m.subtract(n)

    res = [x if x < 0 else None for x in m.values()]
    if not any(res):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])

    magazine = input().rstrip().split()
    note = input().rstrip().split()

    checkMagazine(magazine, note)
