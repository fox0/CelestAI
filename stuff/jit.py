import timeit

from numba.decorators import jit
from numba.types import float64, complex128


def func0(n: float) -> complex:
    tmp = n + 4
    for i in range(1_000_000):
        tmp += i
    return tmp + 3j


@jit(complex128(float64), nopython=True)
def func1(n: float) -> complex:
    tmp = n + 4
    for i in range(1_000_000):
        tmp += i
    return tmp + 3j


@jit(complex128(float64), locals={'tmp': complex128}, nopython=True)
def func2(n: float) -> complex:
    tmp = n + 4
    for i in range(1_000_000):
        tmp += i
    return tmp + 3j


if __name__ == '__main__':
    # func1.inspect_types()
    # print(fff.nopython_signatures)

    print(timeit.timeit('func0(42.0)', setup='from __main__ import func0', number=500))
    print(timeit.timeit('func3(42.0)', setup='from stuff.module import func3', number=500))
    print(timeit.timeit('func1(42.0)', setup='from __main__ import func1', number=500))
    print(timeit.timeit('func2(42.0)', setup='from __main__ import func2', number=500))

    # 65.70823388599092
    # [INFO] Yep, I'm compiled. stuff/module.cpython-38-x86_64-linux-gnu.so
    # 0.7534044600324705
    # 0.666124967043288
    # 0.6662616740213707
