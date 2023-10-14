from itertools import permutations

def permute(nums):
    result = list(permutations(nums))
    return result
elements = list(map(int,input().split()))
permutations = permute(elements)
for perm in permutations:
    print(perm)
