def can_sum(target, numbers, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False
    for num in numbers:
        remainder = target - num
        if can_sum(remainder, numbers, memo):
            memo[remainder] = True
            return True
    memo[target] = False
    return False


print(can_sum(7, [2, 3]))  # True
print(can_sum(3, [2, 1]))  # True
print(can_sum(55, [5, 11]))  # True
print(can_sum(7, [2, 4]))  # False
print(can_sum(300, [7, 14]))  # False
