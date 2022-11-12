# whileループ
count = 0
while count < 10:
    print(count)
    count += 1

# break, continue
while True:
    age = int(input("あなたは何歳ですか"))
    if not 0 <= age <120:
        print("This value is in valid")
        continue
    else:
        print("あなたは{}歳です".format(age))
        break