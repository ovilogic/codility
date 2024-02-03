#! python3
''' A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to
 get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.

Count the minimal number of jumps that the small frog must perform to reach its target.

Write a function:

def solution(X, Y, D)

that, given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or
greater than Y.'''
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')


def solution(X, Y, D):

    jumps_raw = (Y - X) % D
    if jumps_raw:
        jumps = (Y - X) // D + 1
    else:
        jumps = (Y - X) // D
    return jumps


print(solution(35, 35, 2))