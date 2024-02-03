#! python3
'''
A function that, given an array A consisting of N integers, returns the number of distinct values in array A.
N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
'''
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')


def solution(A):
    A.sort()
    count = 1
    for i in range(1, len(A)):
        if A[i] != A[i - 1]:
            count += 1
    return count