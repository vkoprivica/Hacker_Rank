import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    # Create new list with no duplicate items.
    no_duplicates = [ar.count(i) for i in set(ar)]
    # Itereate over no duplicate items and count number of calculations devided by 2.
    return sum([int(i / 2) for i in no_duplicates])


n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

# n = 10
# ar = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]


print(sockMerchant(n, ar))
