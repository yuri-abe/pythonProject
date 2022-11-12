fruits_colors = {'apple': 'red', 'lemon': 'yellow', 'grapes': 'purple'}

if 'peach' in fruits_colors:
    print(fruits_colors['peach'])
else:
    print('The key is not found')

# .get()
fruit = input('フルーツの名前を指定してください')
print(fruits_colors.get(fruit, 'Nothins'))

# .update()
fruits_colors2 = {'peach': 'pink', 'kiwi': 'green'}
fruits_colors.update(fruits_colors2)
print(fruits_colors)
