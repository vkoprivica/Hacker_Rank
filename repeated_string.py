import math
import os
import random
import re
import sys


def repeatedString(s, n):
    return s.count("a") * (n // len(s)) + s[: n % len(s)].count("a")


s = "ab"
n = 1000000000000


print(repeatedString(s, n))
