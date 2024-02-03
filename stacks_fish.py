#! python3
'''
You are given two non-empty arrays A and B consisting of N integers. Arrays A and B represent N voracious fish in a river, ordered downstream along the flow of the river.

The fish are numbered from 0 to N − 1. If P and Q are two fish and P < Q, then fish P is initially upstream of fish Q. Initially, each fish has a unique position.

Fish number P is represented by A[P] and B[P]. Array A contains the sizes of the fish. All its elements are unique. Array B contains the directions of the fish. It contains only 0s and/or 1s, where:

0 represents a fish flowing upstream,
1 represents a fish flowing downstream.
If two fish move in opposite directions and there are no other (living) fish between them, they will eventually meet each other. Then only one fish can stay alive − the larger fish eats the smaller one. More precisely, we say that two fish P and Q meet each other when P < Q, B[P] = 1 and B[Q] = 0, and there are no living fish between them. After they meet:

If A[P] > A[Q] then P eats Q, and P will still be flowing downstream,
If A[Q] > A[P] then Q eats P, and Q will still be flowing upstream.
We assume that all the fish are flowing at the same speed. That is, fish moving in the same direction never meet.
The goal is to calculate the number of fish that will stay alive.
'''
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')

A = [0 for i in range(5)]
B = [0 for i in range(5)]

A[0] = 4
A[1] = 3
A[2] = 2
A[3] = 1
A[4] = 5

B[0] = 0
B[1] = 1
B[2] = 0
B[3] = 0
B[4] = 0


def solution(A, B):
    # List B is more important. Unless fish meet, their sizes don't matter.
    # And it's not enough to get a 0 - 1 pair. Only 1 followed by 0 means fish meet. 0-1 means they are moving apart.
    # 0: upstream
    # 1: downstream

    # 3 pieces of information for each fish: position, direction, size.
    # 1 - 0 is the relevant combination

    # Let's rename the arrays to something more relevant. We no longer need to remember
    # what A or B stand for.
    size = A
    direction = B

    live_fish = []
    downstreamers = []
    # forward engine
    for i in range(len(direction)):
        if direction[i] == 0:
            # Position is basically identity, and ID number.
            if len(downstreamers) == 0:
                live_fish.append(i)
            else:
                # Initiate conflict mode
                while downstreamers:
                    '''
                    yes, it’s actually O(N).
It’s a common trap to count the complexity by checking the number of nested for/while. 
However, that’s not always correct. Please note that during the whole function, the while 
loop is executed at most N times, independently with the for loop.
                    '''
                    current = downstreamers.pop()
                    if size[current] > size[i]:
                        downstreamers.append(current)
                        break
                if not downstreamers:
                    live_fish.append(i)
        else:
            downstreamers.append(i)
    solution = len(live_fish) + len(downstreamers)
    return solution


solution(A, B)
