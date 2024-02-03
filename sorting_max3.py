#! python3
'''
A non-empty array A consisting of N integers is given. The product of triplet (P, Q, R) equates to
A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).
Your goal is to find the >>> maximal product of any triplet <<<.
Write an efficient algorithm for the following assumptions:

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−1,000..1,000].
'''
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')

A = [-3, -1, -2, -2, -5, -6]


def solution(A):
    '''
    Big issue is that 2 negatives multiplied produce a positive.
    result = 0
    if len(A) == 3:
        result = A[-3] * A[-2] * A[-1]
    A.sort()
    print(A)
    negatives = []
    negatives_front = []
    for i in A[:2]:
        if i < 0:
            negatives_front.append(i)
    print(negatives)
    for i in A[-3:]:
        if i < 0:
            negatives.append(i)
    print(f'second negatives {negatives}')

    # If len(negatives) > 0: len(negatives_front) == 2.
    if len(negatives) in [0, 3]:
        if len(negatives) == 0:
            # You then have to have 2 negatives in front to work.
            if len(negatives_front) == 2:
                product_front = negatives_front[0] * negatives_front[1]
                product_pos1 = A[-3] * A[-2]
                product_pos2 = A[-2] * A[-1]
                if product_front < product_pos1:
                    result = product_pos1 * A[-1]
                else:
                    if product_front < product_pos2:

                    result = product_front * A[-1]

        else:
            result = A[-3] * A[-2] * A[-1]
    elif len(negatives) == 1:
        result = A[0] * negatives[0] * A[-1]
    elif len(negatives) == 2:
        # If both are negatives they can't be lower than the lowest negatives at the beginning of the big list now
        # sorted. So choose those 2 instead.
        result = A[0] * A[1] * A[-1]
        # Remember, the list is sorted. So you can never have a positive in front of a negative.
    return result
    '''



print(solution(A))