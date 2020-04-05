# cython: language_level=3
import cython

if cython.compiled:
    print('[INFO] Yep, I\'m compiled.', __file__)
else:
    print('[WARNING] Just a lowly interpreted script.', __file__)


# @cython.cfunc
@cython.returns(cython.complex)
@cython.locals(n=cython.double, tmp=cython.double, i=cython.longlong)
def func3(n: float) -> complex:
    tmp = n + 4
    for i in range(1_000_000):
        tmp += i
    return tmp + 3j

    # __pyx_v_tmp = __pyx_t_double_complex_from_parts((__pyx_v_n + 4.0), 0);
    # for (__pyx_t_1 = 0; __pyx_t_1 < 0xF4240; __pyx_t_1+=1) {
    #   __pyx_v_i = __pyx_t_1;
    #   __pyx_v_tmp = __Pyx_c_sum_double(__pyx_v_tmp, __pyx_t_double_complex_from_parts(__pyx_v_i, 0));
    # }
