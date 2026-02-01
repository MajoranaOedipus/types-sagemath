"""

Convert Python functions to PARI closures
*****************************************

AUTHORS:

- Jeroen Demeyer (2015-04-10): initial version, :trac:`18052`.

Examples:

>>> def the_answer():
...     return 42
>>> import cypari2
>>> pari = cypari2.Pari()
>>> f = pari(the_answer)
>>> f()
42

>>> cube = pari(lambda i: i**3)
>>> cube.apply(range(10))
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
"""
from __future__ import annotations
import builtins as __builtins__
from inspect import getfullargspec as getargspec
__all__: list[str] = ['getargspec', 'objtoclosure']
def objtoclosure(f):
    """
    
        Convert a Python function (more generally, any callable) to a PARI
        ``t_CLOSURE``.
    
        .. NOTE::
    
            With the current implementation, the function can be called
            with at most 5 arguments.
    
        .. WARNING::
    
            The function ``f`` which is called through the closure cannot
            be interrupted. Therefore, it is advised to use this only for
            simple functions which do not take a long time.
    
        Examples:
    
        >>> from cypari2.closure import objtoclosure
        >>> def pymul(i,j): return i*j
        >>> mul = objtoclosure(pymul)
        >>> mul
        (v1,v2)->call_python(v1,v2,0,0,0,2,...)
        >>> mul(6,9)
        54
        >>> mul.type()
        't_CLOSURE'
        >>> mul.arity()
        2
        >>> def printme(x):
        ...     print(x)
        >>> objtoclosure(printme)('matid(2)')
        [1, 0; 0, 1]
    
        Construct the Riemann zeta function using a closure:
    
        >>> from cypari2 import Pari; pari = Pari()
        >>> def coeffs(n):
        ...     return [1 for i in range(n)]
        >>> Z = pari.lfuncreate([coeffs, 0, [0], 1, 1, 1, 1])
        >>> Z.lfun(2)
        1.64493406684823
    
        A trivial closure:
    
        >>> f = pari(lambda x: x)
        >>> f(10)
        10
    
        Test various kinds of errors:
    
        >>> mul(4)
        Traceback (most recent call last):
        ...
        TypeError: pymul() ...
        >>> mul(None, None)
        Traceback (most recent call last):
        ...
        ValueError: Cannot convert None to pari
        >>> mul(*range(100))
        Traceback (most recent call last):
        ...
        PariError: call_python: too many parameters in user-defined function call
        >>> mul([1], [2])
        Traceback (most recent call last):
        ...
        PariError: call_python: ...
        
    """
__pyx_capi__: dict  # value = {'_pari_init_closure': <capsule object "int (void)" at 0x70670ae35fd0>, 'objtoclosure': <capsule object "struct __pyx_obj_7cypari2_3gen_Gen *(PyObject *, int __pyx_skip_dispatch)" at 0x70670ae36020>}
__test__: dict 
