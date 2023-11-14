x = 0


def f():
    global x
    y = 1

    def g():
        nonlocal y
        y = 2

    g()
    x = y


f()
print(x)
