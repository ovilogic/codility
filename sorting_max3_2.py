#! python3
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')

A = [-5, -6, -4, -7, -10]


def solution(A):
    A.sort()
    result = A[-3] * A[-2] * A[-1]

    negatives_back = []
    negatives_front = []
    for i in A[:2]:
        if i < 0:
            negatives_back.append(i)
    for i in range(-3, 0):
        if A[i] == 0:
            A[i], A[-4] = A[-4], A[i]
        if A[i] < 0:
            negatives_front.append(A[i])
    # print('back {}'.format(negatives_back))
    # print('front {}'.format(negatives_front))
    # print(A)
    if len(negatives_back) == 2 and len(negatives_front) < 3:
        product_back = negatives_back[0] * negatives_back[1]
        result = product_back * A[-1]
        if len(negatives_front) < 1:
            if product_back < (A[-3] * A[-2]):
                result = A[-3] * A[-2] * A[-1]

    if len(A) > 3 and A[-4] == 0 and result < 0:
        result = 0
    return result


print(solution(A))
