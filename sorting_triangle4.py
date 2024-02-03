#! python3
'''
An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

A[P] + A[Q] > A[R],
A[Q] + A[R] > A[P],
A[R] + A[P] > A[Q].
Write a function:
that, given an array A consisting of N integers, returns 1 if there exists a triangular triplet for this array and
 returns 0 otherwise.
 Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
'''

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')

A = [5, 3, 3]
B = [10, 50, 5, 1]


def solution(A):
    A.sort()
    for i in range(len(A) - 2):
        if A[i] + A[i + 1] > A[i + 2]:
            return 1
    return 0


print(solution(A))