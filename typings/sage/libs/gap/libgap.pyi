"""
Library Interface to GAP

This module implements a fast C library interface to GAP.
To use it, you simply call ``libgap`` (the parent of all
:class:`~sage.libs.gap.element.GapElement` instances) and use it to
convert Sage objects into GAP objects.

EXAMPLES::

    sage: a = libgap(10)
    sage: a
    10
    sage: type(a)
    <class 'sage.libs.gap.element.GapElement_Integer'>
    sage: a*a
    100
    sage: timeit('a*a')   # random output
    625 loops, best of 3: 898 ns per loop

Compared to the expect interface this is >1000 times faster::

    sage: b = gap('10')
    sage: timeit('b*b')   # random output; long time
    125 loops, best of 3: 2.05 ms per loop

If you want to evaluate GAP commands, use the :meth:`Gap.eval` method::

    sage: libgap.eval('List([1..10], i->i^2)')
    [ 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 ]

not to be confused with the ``libgap`` call, which converts Sage
objects to GAP objects, for example strings to strings::

    sage: libgap('List([1..10], i->i^2)')
    "List([1..10], i->i^2)"
    sage: type(_)
    <class 'sage.libs.gap.element.GapElement_String'>

You can usually use the :meth:`~sage.libs.gap.element.GapElement.sage`
method to convert the resulting GAP element back to its Sage
equivalent::

    sage: a.sage()
    10
    sage: type(_)
    <class 'sage.rings.integer.Integer'>

    sage: libgap.eval('5/3 + 7*E(3)').sage()                                            # needs sage.rings.number_field
    7*zeta3 + 5/3

    sage: gens_of_group = libgap.AlternatingGroup(4).GeneratorsOfGroup()
    sage: generators = gens_of_group.sage()
    sage: generators   # a Sage list of Sage permutations!
    [[2, 3, 1], [1, 3, 4, 2]]
    sage: PermutationGroup(generators).cardinality()   # computed in Sage
    12
    sage: libgap.AlternatingGroup(4).Size()            # computed in GAP
    12

We can also specify which group in Sage the permutations should
consider themselves as elements of when converted to Sage::

    sage: A4 = groups.permutation.Alternating(4)
    sage: generators = gens_of_group.sage(parent=A4); generators
    [(1,2,3), (2,3,4)]
    sage: all(gen.parent() is A4 for gen in generators)
    True

So far, the following GAP data types can be directly converted to the
corresponding Sage datatype:

#. GAP booleans ``true`` / ``false`` to Sage booleans ``True`` /
   ``False``. The third GAP boolean value ``fail`` raises a
   :exc:`ValueError`.

#. GAP integers to Sage integers.

#. GAP rational numbers to Sage rational numbers.

#. GAP cyclotomic numbers to Sage cyclotomic numbers.

#. GAP permutations to Sage permutations.

#. The GAP containers ``List`` and ``rec`` are converted to Sage
   containers ``list`` and ``dict``.  Furthermore, the
   :meth:`~sage.libs.gap.element.GapElement.sage` method is applied
   recursively to the entries.

Special support is available for the GAP container classes. GAP lists
can be used as follows::

    sage: lst = libgap([1,5,7]);  lst
    [ 1, 5, 7 ]
    sage: type(lst)
    <class 'sage.libs.gap.element.GapElement_List'>
    sage: len(lst)
    3
    sage: lst[0]
    1
    sage: [ x^2 for x in lst ]
    [1, 25, 49]
    sage: type(_[0])
    <class 'sage.libs.gap.element.GapElement_Integer'>

Note that you can access the elements of GAP ``List`` objects as you
would expect from Python (with indexing starting at 0), but the
elements are still of type
:class:`~sage.libs.gap.element.GapElement`. The other GAP container
type are records, which are similar to Python dictionaries. You can
construct them directly from Python dictionaries::

    sage: libgap({'a':123, 'b':456})
    rec( a := 123, b := 456 )

Or get them as results of computations::

    sage: rec = libgap.eval('rec(a:=123, b:=456, Sym3:=SymmetricGroup(3))')
    sage: rec['Sym3']
    Sym( [ 1 .. 3 ] )
    sage: dict(rec)
    {'Sym3': Sym( [ 1 .. 3 ] ), 'a': 123, 'b': 456}

The output is a Sage dictionary whose keys are Sage strings and whose
Values are instances of :meth:`~sage.libs.gap.element.GapElement`. So,
for example, ``rec['a']`` is not a Sage integer. To recursively
convert the entries into Sage objects, you should use the
:meth:`~sage.libs.gap.element.GapElement.sage` method::

    sage: rec.sage()
    {'Sym3': NotImplementedError('cannot construct equivalent Sage object'...),
     'a': 123,
     'b': 456}

Now ``rec['a']`` is a Sage integer. We have not implemented the
conversion of the GAP symmetric group to the Sage symmetric group yet,
so you end up with a :exc:`NotImplementedError` exception object. The
exception is returned and not raised so that you can work with the
partial result.

While we don't directly support matrices yet, you can convert them to
Gap List of Lists. These lists are then easily converted into Sage
using the recursive expansion of the
:meth:`~sage.libs.gap.element.GapElement.sage` method::

    sage: M = libgap.eval('BlockMatrix([[1,1,[[1, 2],[ 3, 4]]], [1,2,[[9,10],[11,12]]], [2,2,[[5, 6],[ 7, 8]]]],2,2)')
    sage: M
    <block matrix of dimensions (2*2)x(2*2)>
    sage: M.List()   # returns a GAP List of Lists
    [ [ 1, 2, 9, 10 ], [ 3, 4, 11, 12 ], [ 0, 0, 5, 6 ], [ 0, 0, 7, 8 ] ]
    sage: M.List().sage()   # returns a Sage list of lists
    [[1, 2, 9, 10], [3, 4, 11, 12], [0, 0, 5, 6], [0, 0, 7, 8]]
    sage: matrix(ZZ, _)
    [ 1  2  9 10]
    [ 3  4 11 12]
    [ 0  0  5  6]
    [ 0  0  7  8]


Using the GAP C library from Cython
===================================

We are using the GAP API provided by the GAP project since GAP 4.10.

Calls to the GAP C library (functions declared in ``libgap-api.h``)
should be sandwiched between calls to ``GAP_Enter()`` and
``GAP_Leave()``. These are macros defined in ``libgap-api.h`` and must
be used carefully because ``GAP_Enter()`` is defined as two function
calls in succession without braces. The first thing that
``GAP_Enter()`` does is a ``setjmp()`` which plays an important role
in handling errors. The return value from ``GAP_Enter()`` is non-zero
(success) the first time around, and if an error occurs, execution
"jumps" back to ``GAP_Enter()``, this time with a return value of zero
(failure). Due to these quirks, naive attempts to handle the return
value of ``GAP_Enter()`` are doomed to fail.  The correct pattern to
use is::

    try:
        GAP_Enter()
        # further calls to libgap
    finally:
        GAP_Leave()

How this works is subtle. When GAP is initialized, we install an
``error_handler()`` callback that GAP invokes on error. This function
sets a python exception using ``PyErr_Restore()``, but so long as we
remain in C, this exception will not actually be raised. When
``error_handler()`` finishes executing, control returns to GAP which
then jumps back to the previous ``GAP_Enter()``. It is at this point
that we need to raise the (already set) exception, to prevent
re-executing the code that caused an error. To facilitate this,
``GAP_Enter()`` is wrapped by Cython, and the wrapper is qualified
with ``except 0``. This tells Cython to treat a return value of zero
as an error, and raise an exception if an exception is set. (One will
be set if there was an error because our ``error_handler()`` sets
it). Here is a real example::

    cpdef void crash_and_burn() except *:
        x = libgap({'a': 1, 'b': 2})
        cdef unsigned int xlen
        try:
            GAP_Enter()
            xlen = GAP_LenList((<GapElement>x).value)
        finally:
            GAP_Leave()
        print(xlen)

The call to ``GAP_LenList()`` is an error in this case, because
``x.value`` is a GAP record, not a GAP list. In any case, what happens
is,

#. We call the ``GAP_Enter()`` Cython wrapper, which invokes the
   macro, and additionally generates some C code to raise an
   exception if that return value is zero (error). But this is the
   first pass, so for now the macro returns a non-zero (success)
   value.
#. We call ``GAP_LenList(x.value)``, which is an error.
#. GAP invokes our ``error_handler()``, which creates a
   :exc:`sage.libs.gap.util.GAPError`, and sets it active.
#. Control returns to GAP.
#. GAP jumps back to ``GAP_Enter()``.
#. The error branch of ``GAP_Enter()`` is executed. In other words
   we proceed from ``GAP_Enter()`` as if it returned zero (error).
#. An exception is raised, because the ``except 0`` qualifier on the
   Cython wrapper for ``GAP_Enter()`` specifically checks for zero
   and raises any exceptions in that case.
#. Finally, ``GAP_Leave()`` is called to clean up. In a more
   realistic example where failure is not guaranteed, this would
   also have been run to clean up if no errors were raised.

Another unusual aspect of the libgap interface is its signal
handling. Typically, cysignals' ``sig_on()`` and ``sig_off()``
functions are used to wrap code that may take a long time, and as a
result, may need to be interrupted with Ctrl-C. However, it is
possible that interrupting a function execution at an arbitrary
location will lead to inconsistent state. Internally, GAP provides a
mechanism using ``InterruptExecStat``, which sets a flag that tells
GAP to gracefully exit with an error as early as possible. We make use
of this internal mechanism to prevent segmentation faults when GAP
functions are interrupted.

Specifically, we install GAP's own ``SIGINT`` handler (to catch
Ctrl-C) before executing any long-running GAP code, and then later
reinstall the original handler when the GAP code has finished. This is
accomplished using the suggestively-named ``gap_sig_on()`` and
``gap_sig_off()`` functions. After you have called ``gap_sig_on()``,
if GAP receives Ctrl-C, it will invoke our custom ``error_handler()``
that will set a :exc:`KeyboardInterrupt` containing the phrase "user
interrupt". Eventually (as explained in the preceding paragraphs),
control will jump back to the Cython wrapper for ``GAP_Enter()``, and
this exception will be raised.

The safest pattern to use for interruptible libgap code is::

    try:
        gap_sig_on()
        GAP_Enter()
        # further calls to libgap
    finally:
        GAP_Leave()
        gap_sig_off()

Before you attempt to change any of this, please make sure that
you understand the issues that it is intended to fix, e.g.

* https://github.com/sagemath/sage/issues/37026
* https://trofi.github.io/posts/312-the-sagemath-saga.html
* https://github.com/sagemath/sage/pull/40585
* https://github.com/sagemath/sage/pull/40594
* https://github.com/sagemath/sage/issues/40598

AUTHORS:

- William Stein, Robert Miller (2009-06-23): first version
- Volker Braun, Dmitrii Pasechnik, Ivan Andrus (2011-03-25, Sage Days 29):
  almost complete rewrite; first usable version.
- Volker Braun (2012-08-28, GAP/Singular workshop): update to
  gap-4.5.5, make it ready for public consumption.
- Dima Pasechnik (2018-09-18, GAP Days): started the port to native
  libgap API
"""

from typing import Any, overload
from typings_sagemath import Int
from sage.libs.gap.context_managers import GlobalVariableContext
from sage.rings.integer import Integer
from sage.structure.sage_object import SageObject

from sage.libs.gap.element import GapElement, GapElement_Function, GapElement_Integer
from sage.structure.parent import Parent
from sage.rings.integer_ring import ZZ
from sage.misc.cachefunc import cached_method

type _Sage = SageObject | None | dict[str, _Sage] | list[_Sage] | bool

class Gap(Parent):
    r"""
    The libgap interpreter object.

    .. NOTE::

        This object must be instantiated exactly once by the
        libgap. Always use the provided ``libgap`` instance, and never
        instantiate :class:`Gap` manually.

    EXAMPLES::

        sage: libgap.eval('SymmetricGroup(4)')
        Sym( [ 1 .. 4 ] )

    TESTS::

        sage: TestSuite(libgap).run(skip=['_test_category', '_test_elements', '_test_pickling'])
    """

    Element = GapElement

    def eval(self, gap_command: str | Any) -> GapElement:
        """
        Evaluate a gap command and wrap the result.

        INPUT:

        - ``gap_command`` -- string containing a valid gap command
          without the trailing semicolon

        OUTPUT: a :class:`GapElement`

        EXAMPLES::

            sage: libgap.eval('0')
            0
            sage: libgap.eval('"string"')
            "string"
        """
        ...
    def load_package(self, pkg: str):
        """
        If loading fails, raise a :exc:`RuntimeError` exception.

        TESTS::

            sage: libgap.load_package("chevie")
            Traceback (most recent call last):
            ...
            RuntimeError: Error loading GAP package chevie. You may want to
            install gap_packages SPKG.
        """
        ...
    @cached_method
    def function_factory(self, function_name: str) -> GapElement_Function:
        """
        Return a GAP function wrapper.

        This is almost the same as calling
        ``libgap.eval(function_name)``, but faster and makes it
        obvious in your code that you are wrapping a function.

        INPUT:

        - ``function_name`` -- string; the name of a GAP function

        OUTPUT:

        A function wrapper
        :class:`~sage.libs.gap.element.GapElement_Function` for the
        GAP function. Calling it from Sage is equivalent to calling
        the wrapped function from GAP.

        EXAMPLES::

            sage: libgap.function_factory('Print')
            <Gap function "Print">
        """
        ...
    def set_global(self, variable: str, value) -> None:
        """
        Set a GAP global variable.

        INPUT:

        - ``variable`` -- string; the variable name

        - ``value`` -- anything that defines a GAP object

        EXAMPLES::

            sage: libgap.set_global('FooBar', 1)
            sage: libgap.get_global('FooBar')
            1
            sage: libgap.unset_global('FooBar')
            sage: libgap.get_global('FooBar')
            NULL
        """
        ...
    def unset_global(self, variable: str) -> None:
        """
        Remove a GAP global variable.

        INPUT:

        - ``variable`` -- string; the variable name

        EXAMPLES::

            sage: libgap.set_global('FooBar', 1)
            sage: libgap.get_global('FooBar')
            1
            sage: libgap.unset_global('FooBar')
            sage: libgap.get_global('FooBar')
            NULL
        """
        ...
    def get_global(self, variable: str) -> GapElement:
        """
        Get a GAP global variable.

        INPUT:

        - ``variable`` -- string; the variable name

        OUTPUT:

        A :class:`~sage.libs.gap.element.GapElement` wrapping the GAP
        output. A :exc:`ValueError` is raised if there is no such
        variable in GAP.

        EXAMPLES::

            sage: libgap.set_global('FooBar', 1)
            sage: libgap.get_global('FooBar')
            1
            sage: libgap.unset_global('FooBar')
            sage: libgap.get_global('FooBar')
            NULL
        """
        ...
    def global_context(self, variable, value) -> GlobalVariableContext:
        """
        Temporarily change a global variable.

        INPUT:

        - ``variable`` -- string; the variable name

        - ``value`` -- anything that defines a GAP object

        OUTPUT: a context manager that sets/reverts the given global variable

        EXAMPLES::

            sage: libgap.set_global('FooBar', 1)
            sage: with libgap.global_context('FooBar', 2):
            ....:     print(libgap.get_global('FooBar'))
            2
            sage: libgap.get_global('FooBar')
            1
        """
        ...
    @overload
    def set_seed(self) -> Integer: ...
    @overload
    def set_seed[_Int: Int](self, seed: _Int) -> _Int:
        """
        Reseed the standard GAP pseudo-random sources with the given seed.

        Uses a random seed given by ``current_randstate().ZZ_seed()`` if
        ``seed=None``.  Otherwise the seed should be an integer.

        EXAMPLES::

            sage: libgap.set_seed(0)
            0
            sage: [libgap.Random(1, 10) for i in range(5)]
            [2, 3, 3, 4, 2]
        """
    def zero(self) -> GapElement_Integer:
        """
        Return (integer) zero in GAP.

        OUTPUT: a :class:`GapElement`

        EXAMPLES::

            sage: libgap.zero()
            0
        """
        ...
    def one(self) ->  GapElement_Integer:
        r"""
        Return (integer) one in GAP.

        EXAMPLES::

            sage: libgap.one()
            1
            sage: parent(_)
            C library interface to GAP
        """
        ...
    def __init__(self):
        r"""
        The Python constructor.

        EXAMPLES::

            sage: type(libgap)
            <class 'sage.misc.lazy_import.LazyImport'>
            sage: type(libgap._get_object())
            <class 'sage.libs.gap.libgap.Gap'>
        """
        Parent.__init__(self, base=ZZ)
    def __repr__(self):
        r"""
        Return a string representation of ``self``.

        OUTPUT: string

        EXAMPLES::

            sage: libgap
            C library interface to GAP
        """
        return 'C library interface to GAP'
    @cached_method
    def __dir__(self) -> list[str]: # pyright: ignore[reportIncompatibleMethodOverride]
        """
        Customize tab completion.

        EXAMPLES::

           sage: 'OctaveAlgebra' in dir(libgap)
           True
        """
        ...
    def __getattr__(self, name: str) -> GapElement:
        r"""
        The attributes of the Gap object are the Gap functions, and in some
        cases other global variables from GAP.

        INPUT:

        - ``name`` -- string; the name of the GAP function you want to
          call

        OUTPUT:

        A :class:`GapElement`. A :exc:`AttributeError` is raised
        if there is no such function or global variable.

        EXAMPLES::

            sage: libgap.List
            <Gap function "List">
            sage: libgap.GlobalRandomSource
            <RandomSource in IsGAPRandomSource>
        """
        ...
    def show(self) -> dict[str, int | Integer | dict[str, Integer | dict[str, Integer]]]:
        """
        Return statistics about the GAP owned object list.

        This includes the total memory allocated by GAP as returned by
        ``libgap.eval('TotalMemoryAllocated()'), as well as garbage collection
        / object count statistics as returned by
        ``libgap.eval('GasmanStatistics')``, and finally the total number of
        GAP objects held by Sage as :class:`~sage.libs.gap.element.GapElement`
        instances.

        The value ``livekb + deadkb`` will roughly equal the total memory
        allocated for GAP objects (see
        ``libgap.eval('TotalMemoryAllocated()')``).

        .. NOTE::

            Slight complication is that we want to do it without accessing
            libgap objects, so we don't create new GapElements as a side
            effect.

        EXAMPLES::

            sage: a = libgap(123)
            sage: b = libgap(456)
            sage: c = libgap(789)
            sage: del b
            sage: libgap.collect()
            sage: libgap.show()  # random output
            {'gasman_stats': {'full': {'cumulative': 110,
               'deadbags': 321400,
               'deadkb': 12967,
               'freekb': 15492,
               'livebags': 396645,
               'livekb': 37730,
               'time': 110,
               'totalkb': 65536},
              'nfull': 1,
              'npartial': 1},
             'nelements': 23123,
             'total_alloc': 3234234}
        """
        d: dict[str, int | Any] = {'nelements': self.count_GAP_objects()}
        d['total_alloc'] = self.eval('TotalMemoryAllocated()').sage()
        d['gasman_stats'] = self.eval('GasmanStatistics()').sage()
        return d
    def count_GAP_objects(self) -> int:
        """
        Return the number of GAP objects that are being tracked by
        GAP.

        OUTPUT: integer

        EXAMPLES::

            sage: libgap.count_GAP_objects()   # random output
            5
        """
        ...
    def collect(self) -> None:
        """
        Manually run the garbage collector.

        EXAMPLES::

            sage: a = libgap(123)
            sage: del a
            sage: libgap.collect()
        """
        ...

libgap = Gap()