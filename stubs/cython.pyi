from typing import TypeVar as __TypeVar, Any as __Any

# functions
__T = __TypeVar('__T')


def declare(type_: __T, value=None) -> __T:
    """
    declare declares a typed variable in the current scope, which can be used in place of the
    cdef type var [= value] construct. This has two forms, the first as an assignment
    (useful as it creates a declaration in interpreted mode as well)
    >>> import cython
    >>> x = cython.declare(cython.int)                 # cdef int x
    >>> y = cython.declare(cython.double, 0.57721)     # cdef double y = 0.57721
    >>> cython.declare(x=cython.int, y=cython.double)  # cdef int x; cdef double y
    """
    pass


def address(var: __T) -> __T:
    """
    address is used in place of the & operator
    >>> import cython
    >>> cython.declare(x=cython.int, x_ptr=cython.p_int)
    >>> x_ptr = cython.address(x)
    """
    pass


def sizeof(type_) -> int:
    """
    sizeof emulates the sizeof operator. It can take both types and expressions.
    >>> import cython
    >>> cython.declare(n=cython.longlong)
    >>> print(cython.sizeof(cython.longlong), cython.sizeof(n))
    """
    pass


def struct(**kwargs) -> __Any:
    """
    struct can be used to create struct types.
    >>> import cython
    >>> MyStruct = cython.struct(x=cython.int, y=cython.int, data=cython.double)
    >>> a = cython.declare(MyStruct)
    >>> b = MyStruct(x=5, y=6, data=2.5)
    """
    pass


def typedef(type_) -> __Any:
    """
    union creates union types with exactly the same syntax as struct
    typedef creates a new type
    >>> import cython
    >>> T = cython.typedef(cython.p_int)   # ctypedef int* T
    """
    pass


# const
compiled = False

# types
char = int
short = int
int = int
long = int
longlong = int

uchar = int
ushort = int
uint = int
ulong = int
ulonglong = int

p_int = int
pp_int = int
ppp_int = int

bint = bool
Py_ssize_t = int

double = float
p_double = float


# cython.pointer(cython.int)
# arrays as cython.int[10]

# decorators
def locals(**kwargs):
    """
    locals is a decorator that is used to specify the types of local variables in the function body
    (including any or all of the argument types)
    >>> import cython
    >>> @cython.locals(a=cython.double, b=cython.double, n=cython.p_double)
    >>> def foo(a, b, x, y): pass
    """
    pass


# todo
# RT = TypeVar('RT')  # return type
#
# def inject_user() -> Callable[[Callable[..., RT]], Callable[..., RT]]:
#     def decorator(func: Callable[..., RT]) -> Callable[..., RT]:
#         def wrapper(*args, **kwargs) -> RT:
#             # ...

def returns(type_):
    pass


def cfunc():
    pass
