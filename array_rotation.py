''' An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one
index, and the last element of the array is moved to the first place. For example, the rotation of array
A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).

The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.

Write a function:

def solution(A, K)

that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.
'''


def array_rotate(A, K):
    def one_rotation(copy_A):
        for i in range(len(copy_A) - 1):
            print(i)
            A[0] = copy_A[-1]
            while True:
                A[i + 1] = copy_A[i]
                i = i + 1
                if i == len(A) - 1:
                    break
        return A
    while K:
        copy_A = A[:]
        one_rotation(copy_A)
        K -= 1
    return A


A = [1, 2, 3, 4, 5]
x = array_rotate(A, 6)

print(x)