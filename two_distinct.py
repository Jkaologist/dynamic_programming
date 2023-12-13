def two_distinct(arr1, arr2):
    common_numbers = set()
    if len(arr2) >= len(arr1):
        for num in arr2:
            if num in arr1 and num not in common_numbers:
                common_numbers.add(num)
    else:
        for num in arr1:
            if num in arr2 and num not in common_numbers:
                common_numbers.add(num)
    return list(common_numbers)


print(two_distinct([1, 3, 3, 3, 3, 5, 7, 8, 11], [2, 3, 8, 12]))
