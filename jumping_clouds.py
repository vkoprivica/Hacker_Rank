def jumpingOnClouds(c):
    count = 0
    while len(c) >= 3:
        if c[2] == 0:
            count += 1
            c = c[2:]
        elif c[1] == 0:
            count += 1
            c = c[1:]
        else:
            return count

    if len(c) == 2:
        if c[1] == 0:
            return count + 1

    return count


# c = [0,1,1,0,0,1,0]
# c = [0,1,0,0,0,1,0]
# c = [0,0,1,0,0,1,0]
# c = [0,0,0,0,1,0]
c = [0, 0, 0, 1, 0, 0]
# c = [0,0]

print(jumpingOnClouds(c))
