#! python3
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')

'''
A string S consisting of N characters is called properly nested if:

S is empty;
S has the form "(U)" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, string "(()(())())" is properly nested but string "())" isn't.

Write a function:

class Solution { public int solution(String S); }

that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.

For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..1,000,000];
string S is made only of the characters '(' and/or ')'.
'''


def nesting(S):
    string_ = S
    if len(string_) == 0:
        return 1
    if len(string_) % 2 != 0:
        return 0
    # A stack building up material until matched pairs are popped out. Any unmatched
    # character left over after the for-loop means the string is not properly nested.
    # An empty stack at the end means it is properly nested.
    matching_stack = []

    for character in string_:
        if character == "(":
            matching_stack.append(character)
                # You can't have a ")" sitting in the stack, as it would have been popped out
        else:
            if not matching_stack:
                return 0
            else:
                matching_stack.pop()

    if not matching_stack:
        return 1
    else:
        return 0



