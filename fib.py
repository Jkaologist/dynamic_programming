def fib(n, memo = {}):
    if n <= 2:
        return 1
    if n in memo:
        return memo[n]
    else:
        memo[n] = fib(n - 2) + fib (n - 1)
        return memo[n]

print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))