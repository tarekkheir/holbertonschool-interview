#!/usr/bin/python3
"""Lockboxes Module"""


def checkKeys(keys, box):
    """checks if the keys of the safe are not similar to the existing keys"""

    new_keys = []

    for k in box:
        if k not in keys:
            new_keys.append(k)

    return new_keys


def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened."""

    size = len(boxes)

    if size == 0:
        return False

    keys = boxes[0]
    boxes[0] = [-1]

    while keys:

        new_keys = []

        for key in keys:

            if boxes[key] != [-1]:
                new_keys += checkKeys(keys, boxes[key])
                boxes[key] = [-1]

        keys = new_keys

    if boxes.count([-1]) == size:
        return True

    return False
