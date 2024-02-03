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
    for a in range(len(side_A)):
        for b in range(a, len(side_B)):
            for c in range(b, len(side_C)):
                if side_A[a] + side_B[b] > side_C[c]:
                    if side_B[b] + side_C[c] > side_A[a]:
                        if side_C[c] + side_A[a] > side_B[b]:
                            print(side_A[a], side_B[b], side_C[c])
                            return 1
    return 0




print(solution(A))
