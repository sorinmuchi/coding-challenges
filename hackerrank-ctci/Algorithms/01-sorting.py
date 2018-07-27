'''
Sorting: Bubble Sort
Easy
https://www.hackerrank.com/challenges/ctci-bubble-sort/problem
'''


#!/bin/python3

# Complete the countSwaps function below.
def countSwaps(a):
    swaps = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if i < j and a[i] > a[j]:
                swaps += 1
                a[i], a[j] = a[j], a[i]

    return (swaps, a[0], a[-1])

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    swaps, first, last = countSwaps(a)

    print('Array is sorted in', swaps, 'swaps.')
    print('First Element:', first)
    print('Last Element:', last)
