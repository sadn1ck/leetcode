class Solution:
    def findTwoElement(self, arr, n):
        missing, repeated = 0, 0
        store = [0]*(n+1)
        for i in arr:
            store[i] += 1
        for i in range(len(store)):
            if store[i] == 0 and i != 0:
                missing = i
            if store[i] == 2:
                repeated = i
        return [repeated, missing]


"""
Given an unsorted array Arr of size N of positive integers. 
One number 'A' from set {1, 2, …N} is missing and one number 'B' occurs twice in array. 
Find these two numbers.
"""
