def greet1(fx):
    def mfx():
        print("good morning")
        fx()
        print("thanks for using this function")
    return mfx

@greet1
def hello():
    print("hello world")

# greet1(hello)()
hello()

def greet2(fx):
    def mfx(*args, **kwargs):
        print("good morning")
        fx(*args, **kwargs)
        print("thanks for using this function")
    return mfx
@greet2
def add(a, b):
    print(a+b)


add(2, 5)
# greet2(add)(2, 5)