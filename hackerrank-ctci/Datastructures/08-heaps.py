'''
Heaps: Find the Running Median
Hard
https://www.hackerrank.com/challenges/ctci-find-the-running-median/problem
'''

#!/bin/python3
import heapq


if __name__ == '__main__':
    n = int(input())

    maxHeap = []
    minHeap = []
    
    def orderHeaps():
        smallerHeap = minHeap if len(minHeap) < len(maxHeap) else maxHeap
        largerHeap = minHeap if len(minHeap) >= len(maxHeap) else maxHeap
        return (smallerHeap, largerHeap)
    
    def addToHeap(item):
        if maxHeap and item > abs(maxHeap[0]):
            heapq.heappush(minHeap, item)
        else:
            heapq.heappush(maxHeap, -1 * item)

    def rebalanceHeaps():
        (smallerHeap, largerHeap) = orderHeaps()
        
        while (len(largerHeap) - len(smallerHeap) >= 2):
            element = -1 * heapq.heappop(largerHeap)
            heapq.heappush(smallerHeap, element)
    
    def getMedianValue():
        (smallerHeap, largerHeap) = orderHeaps()
        
        if ((len(smallerHeap) + len(largerHeap)) % 2 == 1):
            return float(abs(largerHeap[0]))
        else:
            return round((abs(smallerHeap[0]) + abs(largerHeap[0]))/2, 1)
    
    for _ in range(n):
        a_item = int(input())
        addToHeap(a_item)
        rebalanceHeaps()
        print(getMedianValue())
                    
        

