#!/usr/bin/python3
"""
Solution to lockboxes problem
"""


def canUnlockAll(boxes):
    """
    Determines whether a series of locked boxes can be opened
    based on keys that can be attained.
    Solution to the lockboxes problem
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False
    unlocked = set([0])
    keys = set(boxes[0])
    while keys:
        key = keys.pop()
        if key not in unlocked and key < len(boxes):
            unlocked.add(key)
            keys.update(boxes[key])
        return len(unlocked) == len(boxes)
