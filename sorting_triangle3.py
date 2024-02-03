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

A = [10, 1, 5, 8]
B = [10, 50, 5, 1]


def solution(A):

    side_A = [A[i] for i in range(0, len(A) - 2)]
    side_B = [A[i] for i in range(1, len(A) - 1)]
    side_C = [A[i] for i in range(2, len(A))]
    print(side_A, side_B, side_C, sep='\n')
    sum_A = 0
    sum_B = 0
    sum_C = 0
    i = 0
    while i < len(side_A):
        sum_A += side_A[i]
        i += 1
    i = 0
    while i < len(side_B):
        sum_B += side_B[i]
        i += 1
    i = 0
    while i < len(side_C):
        sum_C += side_C[i]
        i += 1
    print(sum_A, sum_B, sum_C)
    if sum_A + sum_B > sum_C:
        if sum_B + sum_C > sum_A:
            if sum_C + sum_A > sum_B:
                return 1
    return 0


print(solution(A))
