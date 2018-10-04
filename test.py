import math
import os

n, m = [int(i) for i in (input()).split(' ')]

l = [[] for _ in range(n)]
for i in range(n):
    l[i] = [int(i) for i in (input()).split(' ')]
# print(l)

def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]

iters = list(all_perms((0,1,2)))
# print(iters)
max = 0
max_j = -1
for i in range(len(iters)):
    sum = 0
    for j in range(n):
        # print(l[j][iters[i][j]], iters[i][j], i,j)
        sum += l[j][iters[i][j]]
    if sum > max:
        max = sum
        max_j = i
    #     print("used")
    # else:
    #     print("unused")

print(max, max_j)



iters = list(all_perms((0,1,2)))
# print(iters)
max = 0
max_j = -1  