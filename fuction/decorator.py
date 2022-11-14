# Decorator: 関数に機能を付属する（デコレートする）

def greeting(func):
    def inner(*args, **kwargs):
        print("Hello")
        func(*args, **kwargs)
        print("Nice to meet you")
    return inner


@greeting
def say_name(name):
    print(f"I'm {name}")


say_name("Taro")