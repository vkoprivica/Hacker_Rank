import math
import os
import random
import re
import sys


def countingValleys(n, s):
    count = 0
    count_valleys = 0
    for i in s:
        if i == "U":
            count += 1

        elif i == "D":
            if count == 0:
                count -= 1
                count_valleys += 1
            else:
                count -= 1

    return count_valleys


n = 8
s = "DDUUUUDD"


print(countingValleys(n, s))
