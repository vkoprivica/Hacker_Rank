import math
import os
import random
import re
import sys


def minimumBribes(q):
    new_q = list(range(1, n + 1))
    swap_count = 0
    for i in range(len(q) - 1):
        if q[i] - i > 3:
            answer = "Too chaotic"
            break

        else:
            while q[i] > new_q[i]:
                if new_q[i + 1] == q[i]:
                    new_q[i], new_q[i + 1] = new_q[i + 1], new_q[i]
                    swap_count += 1

                elif new_q[i + 2] == q[i]:
                    new_q[i + 1], new_q[i + 2] = new_q[i + 2], new_q[i + 1]
                    swap_count += 1
            answer = swap_count

    print(answer)


if __name__ == "__main__":
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
