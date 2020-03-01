def hourglassSum(arr):
    highest = -63
    for i in range(4):
        for j in range(4):
            count_j = 0
            summary = 0
            while count_j < 3:
                summary = summary + arr[i][j + count_j] + arr[i + 2][j + count_j]
                count_j += 1
            summary = summary + arr[i + 1][j + 1]
            if highest < summary:
                highest = summary
    return highest


"""
arr = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0],
]

"""
arr = [
    [-9, -9, -9, 1, 1, 1],
    [0, -9, 0, 4, 3, 2],
    [-9, -9, -9, 1, 2, 3],
    [0, 0, 8, 6, 6, 0],
    [0, 0, 0, -2, 0, 0],
    [0, 0, 1, 2, 4, 0],
]

"""
array = [
[1,2,3,4,5,6],
[7,8,9,10,11,12],
[13,14,15,16,17,18],
[0,0,2,4,4,0],
[0,0,0,2,0,0],
[0,0,1,2,4,0]
]
"""

print(hourglassSum(arr))
