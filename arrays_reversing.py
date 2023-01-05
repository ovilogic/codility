# Given array A consisting of N integers, return the reversed array


def rev_array(A):
    for x in range(len(A) // 2):
        r = len(A) - 1 - x
        A[x], A[r] = A[r], A[x]
    print(A)
    return A


A = list(range(4))
rev_array(A)