#! python3
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')


def solution(S):
    if len(S) % 2 == 1:
        return 0
    matched = {"]":"[", "}":"{", ")": "("}
    to_push = ["[", "{", "("]
    stack = []
    for element in S:
        if element in to_push:
            stack.append(element)
        else:
            if len(stack) == 0:
                return 0
            elif matched[element] != stack.pop():
                return 0
    if len(stack) == 0:
        return 1
    else:
        return 0


probl = "([]"
x = solution(probl)
print(x)