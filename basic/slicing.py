# [:]を使用して複数の要素を取得できる（slicing）
even = [2, 4, 6, 8, 10, 12]
# 基本は[開始：未満]
print(even[1:4])

print(even[3:5])
print(even[3:-1])

# 基本は[開始：未満：step]
text = 'Hello World'
print(text[2:10:2])
print(text[::-1])
