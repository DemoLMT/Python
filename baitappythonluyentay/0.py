def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
T = int(input("Nhập số lượng bộ test: "))
for _ in range(T):
    n = int(input())
    result = fibonacci(n)
    print(result)
