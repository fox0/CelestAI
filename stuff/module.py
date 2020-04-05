# cython: language_level=3
import cython

if cython.compiled:
    print('[INFO] Yep, I\'m compiled.', __file__)
else:
    print('[WARNING] Just a lowly interpreted script.', __file__)


# @cython.cfunc
@cython.returns(cython.bint)
@cython.locals(a=cython.int, b=cython.int)
def c_compare(a, b):
    return a == b


x = cython.declare(cython.int)
y = cython.declare(cython.double, 0.57721)
