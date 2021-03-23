a = 10

def read():
    print(a)

def mod1 ():
    global a
    a = 5

def mod2 ():
    a = 15

read()
mod1()
read()
mod2()
read()

print ("Value of a using nonlocal is : ",end="")

def outer():
    a = 5

    def inner ():
        nonlocal a
        a = 20

    inner()

    print(a)

outer()

print("Value of a without using nonlocal is : ", end="")


def outer():
    a = 5

    def inner():
        a = 10

    inner()
    print(a)


outer()

print("Value of a using global is : ", end="")


def outer():
    a = 5

    def inner():
        global  a
        a = 10

    inner()
    print(a)


outer()