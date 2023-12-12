import copy


def best_sum(target, numbers, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    shortest = None

    for num in numbers:
        remainder = target - num
        combination = best_sum(remainder, numbers, memo)
        if combination is not None:
            new_combination = copy.deepcopy(combination)
            new_combination.append(num)
            if shortest is None or len(new_combination) < len(shortest):
                shortest = new_combination

    memo[target] = shortest
    return shortest


print(best_sum(7, [5, 3, 4, 7]))
print(best_sum(8, [2, 3, 5]))
print(best_sum(100, [1, 2, 5, 25]))
