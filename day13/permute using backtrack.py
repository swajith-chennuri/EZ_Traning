def permute(nums):
    def backtrack(first=0):
        if first == n:
            result.append(nums[:])
        for i in range(first, n):
            nums[first], nums[i] = nums[i], nums[first]
            backtrack(first + 1)
            nums[first], nums[i] = nums[i], nums[first]  # Backtrack
    n = len(nums)
    result = []
    backtrack()
    return result
elements = list(map(int,input().split()))
permutations = permute(elements)
for perm in permutations:
    print(perm)
