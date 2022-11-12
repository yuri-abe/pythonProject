# tuple: 変更できないリスト []ではなく()を使う

date_of_birth = (1995, 5, 24)
print(date_of_birth)

# tupleだとunpackできる
year, month, day = date_of_birth
print(year)
print(month)
print(day)