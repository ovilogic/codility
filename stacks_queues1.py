"""
A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..200,000];
string S is made only of the following characters: '(', '{', '[', ']', '}' and/or ')'.
"""
import logging


def nested(S):
    if len(S) == 0:
        return 1
    if len(S) % 2 != 0:
        return 0
    # Stack represents unsolved business, brackets waiting to be closed.
    stack = []
    o = ["(", "[", "{"]
    c = [")", "]", "}"]
    l = [S[i] for i in range(len(S))]
    for i in l:
        # First, filter: does it get stacked or not? Only gets stacked if previous in stack not forming a pair
        # or if it is an open
        # bracket.
        if i in c:
            if len(stack) == 0:
                return 0
            if stack[-1] in o:
                if c.index(i) == o.index(stack[-1]):
                    stack.pop()
                else:
                    return 0
            else:
                stack.append(i)
        else:
            stack.append(i)
    if len(stack) == 0:
        return 1
    else:
        return 0


probl = "{[()()]}"
x = nested(probl)
print(x)
