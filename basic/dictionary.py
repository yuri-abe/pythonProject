# dictionary: キーと値の組み合わせを複数保持するデータ型
fruits_colors = {'apple': 'red', 'lemon': 'yellow', 'grapes': 'purple'}

print(fruits_colors['apple'])

fruits_colors['peach'] = 'pink'

print(fruits_colors)

# .keys() .values()
for x in fruits_colors:
    print(x)

# .items()
for fruit, color in fruits_colors.items():
    print(f'{fruit} is {color}')