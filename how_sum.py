def how_sum(target, numbers, memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    for num in numbers:
        rem = target - num
        result = how_sum(rem, numbers)
        if result is not None:
            result.append(num)
            memo[target] = num
            return result
    memo[target] = None
    return None


# print(how_sum(7, [2, 3]))
print(how_sum(7, [3, 4]))
# print(how_sum(8, [2, 3, 5]))
# print(how_sum(300, [7, 14]))
