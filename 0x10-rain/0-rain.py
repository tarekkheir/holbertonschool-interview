#!/usr/bin/python3
"""Rain challenge"""


def rain(walls) -> int:
    """calculate how many square units of water
    will be retained after it rains."""

    if not walls:
        return None

    i = 0
    water = 0
    check = 0

    for w in walls:
        if w > 0:
            if check == 0:
                tmp = i
                tmp_height = w
                check = 1
            else:
                width = i - tmp + 1
                if tmp_height < w:
                    height = tmp_height
                else:
                    height = w
                surface = width * height
                water += surface - (height * 2)
                tmp = i
                tmp_height = w
        i += 1

    return water


"""print("enter to second option")
            print("w : {}".format(w))
            print("i : {}".format(i))"""
