fruits = ['apple', 'greaps', 'peach', 'banana']

# for else
for fruit in fruits:
    print(fruit)
else:
    print('ループが回り切りました') # breakしたらelseには入らない

# while else
count = 0
while count < 10:
    print(count)
    count += 1
else:
    print('countは10未満ではなくなりました')