# Closure: 状態をキープした関数を作ることができる

# 状態が静的
def power(exponent):
    def inner_power(base):
        return base ** exponent
    return inner_power


power_four = power(4)
print(power_four(2))

power_five = power(5)
print(power_five(2))

# 状態が動的
def average():
    nums = []

    def innner_average(num):
        nums.append(num)
        return sum(nums) / len(nums)
    return innner_average


average_nums = average()
print(average_nums(5))
print(average_nums(15))
