# lambda関数（無名関数）

# 戻り値で使用するパターン
def power(exponential):
    return lambda base: base ** exponential


third_power = power(3)
print(third_power(2))

# 引数に使用するパターン
numbers = [6, 2, 5, 43, 5, 36, 67, 2]

filtered_num = filter(lambda num: num % 2, numbers)
print (list(filtered_num))