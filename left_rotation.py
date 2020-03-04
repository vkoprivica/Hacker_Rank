def rotLeft(a, d):
    return a[d:] + a[:d]


a = [1, 2, 3, 4, 5]
# a = ['a','b','c','d','e']
d = 4
n = 5

print(rotLeft(a, d))
