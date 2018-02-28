import time


def increment_with_hint(x: int) -> int:
    return x + 1


def increment_without_hint(x):
    return x + 1


if __name__ == '__main__':
    loop_count = 20000000
    st = time.time()

    x = 0  # type: int
    for i in range(loop_count):
        x = increment_with_hint(x)
    elapsed_time = time.time() - st
    print("increment_with_hint   : {0}".format(elapsed_time) + "[sec]")

    st = time.time()
    y = 0
    for i in range(loop_count):
        y = increment_without_hint(y)
    elapsed_time = time.time() - st
    print("increment_without_hint: {0}".format(elapsed_time) + "[sec]")
