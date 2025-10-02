def nums_sum(*args):
    n_sum = 0
    p_sum = 0
    for num in args:
        if num>0:
            p_sum+=num
        else:
            n_sum+=num
    return n_sum, p_sum

nums=map(int, input().split())
neg_nums, pos_nums = nums_sum(*nums)
print(neg_nums)
print(pos_nums)

if abs(neg_nums)>pos_nums:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")