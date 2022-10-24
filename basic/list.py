fruits = ['apple', 'peach', 'melon', 'greap']

# .append: 新しいオブジェクトを追加する
print(fruits)
fruits.append('banana')
print(fruits)
# .insert: 指定したindexに指定したオブジェクトを追加
print(fruits)
fruits.insert(3, 'lemon')
print(fruits)
# .remove: マッチした最初のオブジェクトを除く
print(fruits)
fruits.remove('peach')
print(fruits)
# .sort: 昇順に並び替える
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
# .len: リストの要素数を取得する
print(len(fruits))
