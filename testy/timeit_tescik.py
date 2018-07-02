import timeit


def power_list(n):
    return [x ** 2 for x in xrange(n)]


def power_map(n):
    return map(lambda x: x ** 2, xrange(n))


t = timeit.Timer(stmt="timer_3.power_list(5000000)", setup="import timer_3")
print(min(t.repeat(5, 1)))