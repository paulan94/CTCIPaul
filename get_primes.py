import math
def is_prime(n):
    if n <= 1:
        return False
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(3,math.sqrt(n)+1, 2):
        if (n % i == 0):
            return False
    return True