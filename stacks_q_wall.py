#! python3
'''
You are going to build a stone wall. The wall should be straight and N meters long, and its thickness should be
constant; however, it should have different heights in different places. The height of the wall is specified by an array
 H of N positive integers. H[I] is the height of the wall from I to I+1 meters to the right of its left end. In
  particular, H[0] is the height of the wall's left end and H[N−1] is the height of the wall's right end.

The wall should be built of cuboid stone blocks (that is, all sides of such blocks are rectangular). Your task is to
compute the minimum number of blocks needed to build the wall.

Write a function:

def solution(H)

that, given an array H of N positive integers specifying the height of the wall, returns the minimum number of blocks
needed to build it.

For example, given array H containing N = 9 integers:

  H[0] = 8    H[1] = 8    H[2] = 5
  H[3] = 7    H[4] = 9    H[5] = 8
  H[6] = 7    H[7] = 4    H[8] = 8
the function should return 7. The figure shows one possible arrangement of seven blocks.
Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array H is an integer within the range [1..1,000,000,000].
'''

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')


def solution(H):
    heights = H
    # geometric logic: the blocks need to be cuboid, all sides are rectangular. Nothing fancy, means that the angles
    # need to be 90 deg.
    # Translated into code, any time your height changes, you start a new block.
    # Going up, would lead to a 270 deg angle,
    # while going down, the same.
    # Your ground level is 0 when you start. But doesn't have to stay that way. To reduce the number of blocks, you
    # raise the ground level to the lowest common floor. You build blocks on that while you can, that is
    # while you don't go
    # any lower.

    # Do blocks need to be individual objects? You only need to count them, so no.

    blocks_count = 0
    levels = [0]

    for i in heights:

        # Going down.
        if i < levels[-1]:
            # If you drop to a level already attained, there is no change of angle, so no new block. This will be the
            # continuation of a block already counted. Simply dropping does not create a new block, while simply rising
            # always does create a new block. This asymmetry is a consequence of moving from left to right.
            levels.pop()
            while i < levels[-1]:
                levels.pop()
            if i > levels[-1]:
                blocks_count += 1
            levels.append(i)
        # Going up.
        elif i > levels[-1]:
            blocks_count += 1
            levels.append(i)
    return blocks_count


test = [8, 8, 5, 7, 9, 8, 7, 4, 8]
s = solution(test)
print(s)




























