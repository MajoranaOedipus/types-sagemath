from sage.misc.sageinspect import sage_getargspec as sage_getargspec
from typing import Any, ClassVar

class ArgumentFixer:
    '''ArgumentFixer(f, classmethod=False)

    File: /build/sagemath/src/sage/src/sage/misc/function_mangling.pyx (starting at line 41)

    This class provides functionality to normalize the arguments
    passed into a function.  While the various ways of calling a
    function are perfectly equivalent from the perspective of the
    callee, they don\'t always look the same for an object
    watching the caller.  For example,
    ::

        sage: def f(x=10):
        ....:     return min(1,x)

    the following calls are equivalent,
    ::

        sage: f()
        1
        sage: f(10)
        1
        sage: f(x=10)
        1

    but from the perspective of a wrapper, they are different::

        sage: def wrap(g):
        ....:     def _g(*args, **kwargs):
        ....:         print("{} {}".format(args, kwargs))
        ....:         return g(*args, **kwargs)
        ....:     return _g
        sage: h = wrap(f)
        sage: t = h()
        () {}
        sage: t = h(10)
        (10,) {}
        sage: t = h(x=10)
        () {\'x\': 10}

    For the purpose of cached functions, it is important not
    to distinguish between these uses.

    INPUT:

    - ``f`` -- a function
    - ``classmethod`` -- boolean (default: ``False``); ``True`` if the function
      is a classmethod and therefore the first argument is expected to be the
      class instance. In that case, we ignore the first argument.

    EXAMPLES::

        sage: from sage.misc.function_mangling import ArgumentFixer
        sage: def wrap2(g):
        ....:     af = ArgumentFixer(g)
        ....:     def _g(*args, **kwargs):
        ....:         print(af.fix_to_pos())
        ....:         return g(*args, **kwargs)
        ....:     return _g
        sage: h2 = wrap2(f)
        sage: t = h2()
        ((10,), ())
        sage: t = h2(10)
        ((10,), ())
        sage: t = h2(x=10)
        ((10,), ())

    ::

        sage: class one:
        ....:    def __init__(self, x=1):
        ....:       self.x = x
        sage: af = ArgumentFixer(one.__init__, classmethod=True)
        sage: af.fix_to_pos(1,2,3,a=31,b=2,n=3)
        ((1, 2, 3), ((\'a\', 31), (\'b\', 2), (\'n\', 3)))'''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    f: f
    def __init__(self, f, classmethod=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/misc/function_mangling.pyx (starting at line 114)"""
    def fix_to_named(self, *args, **kwargs) -> Any:
        """ArgumentFixer.fix_to_named(self, *args, **kwargs)

        File: /build/sagemath/src/sage/src/sage/misc/function_mangling.pyx (starting at line 162)

        Normalize the arguments with a preference for named arguments.

        INPUT:

        - any positional and named arguments.

        OUTPUT: we return a tuple

            `(e_1, e_2, ..., e_k), ((n_1, v_1), ... , (n_m, v_m))`

        where `n_1, ... , n_m` are the names of the arguments and
        `v_1, ..., v_m` are the values passed in; and `e_1, ..., e_k` are
        the unnamed arguments.  We minimize `k`.

        The defaults are extracted from the function and filled
        into the list ``K`` of named arguments. The names `n_1, ..., n_t`
        are in order of the function definition, where `t` is the number
        of named arguments.  The remaining names, `n_{t+1}, ..., n_m` are
        given in alphabetical order.  This is useful to extract
        the names of arguments, but **does not** maintain
        equivalence of
        ::

            A,K = self.fix_to_pos(...)
            self.f(*A, **dict(K))`

        and
        ::

            self.f(...)

        in all cases.

        EXAMPLES::

            sage: from sage.misc.function_mangling import ArgumentFixer
            sage: def sum3(a, b, c=3, *args, **kwargs):
            ....:     return a + b + c
            sage: AF = ArgumentFixer(sum3)
            sage: AF.fix_to_named(1, 2, 3, 4, 5, 6, f=14, e=16)
            ((4, 5, 6), (('a', 1), ('b', 2), ('c', 3), ('e', 16), ('f', 14)))
            sage: AF.fix_to_named(1,2,f=14)
            ((), (('a', 1), ('b', 2), ('c', 3), ('f', 14)))"""
    def fix_to_pos(self, *args, **kwds) -> Any:
        '''ArgumentFixer.fix_to_pos(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/misc/function_mangling.pyx (starting at line 230)

        Normalize the arguments with a preference for positional arguments.

        INPUT:

        - ``*args``, ``**kwds`` -- any positional or named arguments

        OUTPUT: we return a tuple

            `(e_1, e_2, ..., e_k), ((n_1, v_1), ... , (n_m, v_m))`

        where `n_1, ... , n_m` are the names of the arguments and
        `v_1, ..., v_m` are the values passed in; and `e_1, ..., e_k`
        are the unnamed arguments. We minimize `m`.

        The commands
        ::

            A,K = self.fix_to_pos(...)
            self.f(*A, **dict(K))

        are equivalent to
        ::

            self.f(...)

        though defaults are extracted from the function and
        appended to the tuple ``A`` of positional arguments.
        The names `n_1, ..., n_m` are given in alphabetical
        order.

        EXAMPLES::

            sage: from sage.misc.function_mangling import ArgumentFixer
            sage: def do_something(a, b, c=3, *args, **kwargs):
            ....:     print("{} {} {} {} {}".format(a, b, c, args,
            ....:                                   sorted(kwargs.items())))
            sage: AF = ArgumentFixer(do_something)
            sage: A, K = AF.fix_to_pos(1, 2, 3, 4, 5, 6, f=14, e=16)
            sage: print("{} {}".format(A, K))
            (1, 2, 3, 4, 5, 6) ((\'e\', 16), (\'f\', 14))
            sage: do_something(*A, **dict(K))
            1 2 3 (4, 5, 6) [(\'e\', 16), (\'f\', 14)]
            sage: do_something(1, 2, 3, 4, 5, 6, f=14, e=16)
            1 2 3 (4, 5, 6) [(\'e\', 16), (\'f\', 14)]'''
