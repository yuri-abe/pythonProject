# 参照渡し（byref) <-> 値渡し
# 参照渡し -> アドレスを渡している <- pythonでは全て参照渡し
# 値渡し -> 値を渡している

def add_nums(a, b):
    print(f"第一引数のID：{id(a)}")
    print(f"第二引数のID：{id(b)}")
    return a + b


one = 1
two = 2
print(f"oneのID：{id(one)}")
print(f"twoのID：{id(two)}")
print(add_nums(one, two))