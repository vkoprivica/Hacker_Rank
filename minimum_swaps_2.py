import math
import os
import random
import re
import sys


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    # transfer array list to dictionary for faster processing
    # key + 1 - start key from 1, rather than 0
    arr = {key + 1: val for key, val in enumerate(arr)}
    # create reversed dictionary as it will use as reference
    rev = {key: val for val, key in arr.items()}
    count = 0

    for i in range(1, n):
        while arr[i] != i:
            # save values of dictionary before they get changed
            holder_1, holder_2 = rev[i], arr[i]
            # swap values of arr
            arr[i], arr[holder_1] = i, arr[i]
            # swap values of rev, necessary as arr got swapped
            rev[i], rev[holder_2] = i, holder_1
            count += 1
    print(count)


# arr = [7, 1, 3, 2, 4, 5, 6]
arr = [4, 3, 1, 2]
# arr = [2, 3, 4, 1, 5]


if __name__ == "__main__":

    n = 4  # int(input())
    # arr = list(map(int, input().rstrip().split()))
    res = minimumSwaps(arr)

