# Paul An
# memoization in recursive fibonacci
memory = dict()


def fibonacci(n):
    if (n == 0):
        memory[n] = 0
    if (n == 1 or n == 2):
        memory[n] = 1
    if not n in memory.keys():
        memory[n] = fibonacci(n - 2) + fibonacci(n - 1)
    # Write your code here.
    return memory[n]


n = int(raw_input())
print(fibonacci(n))
