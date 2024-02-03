#! python3
''' A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each
element of the array can be paired with another element that has the same value, except for one element that is left
unpaired. '''

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')

A = [9, 3, 9, 3, 9, 7, 9, 7, 12]


def solution(A):
    if len(A) == 1:
        return A[0]
    A.sort()
    i = 0
    while A[i] == A[i + 1]:
        if i < len(A) - 4:
            i += 2
        else:
            return (A[-1])
    return (A[i])


print(solution(A))