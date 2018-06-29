import random

def random_bool():
    bool = [random.randint(0, 1) for x in range(100)]

    return bool

def random_reg():
    c = [x for x in range(10000)]
    random.shuffle(c)
    return c



