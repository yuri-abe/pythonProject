age = 30

# ローカルスコープでグローバル変数を操作
def print_age():
    global age
    age = 20
    print(f"I'm {age} years old")

print_age()