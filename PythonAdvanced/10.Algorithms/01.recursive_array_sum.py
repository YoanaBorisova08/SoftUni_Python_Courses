def sum_recursive(nums, idx=0):
    if idx == len(nums):
        return 0
    return nums[idx] + sum_recursive(nums, idx+1)


numbers = [int(x) for x in input().split()]
print(sum_recursive(numbers))