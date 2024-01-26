def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_and_print_primes(arr):
    primes = []
    for num in arr:
        if is_prime(num) and num not in primes:
            primes.append(num)
    primes.sort()
    print(*primes)
n = int(input())
arr = list(map(int, input().split()*n))

find_and_print_primes(arr)