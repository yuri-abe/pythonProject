# 再帰関数（Recursive function）

def fibonacci_recursive(n):
    if n < 2:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


print(fibonacci_recursive(5))
