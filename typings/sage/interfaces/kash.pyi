r"""
Interface to KASH

Sage provides an interface to the KASH computer algebra system,
which is a *free* (as in beer!) but *closed source* program for
algebraic number theory that shares much common code with Magma. To
use KASH, you must first install it. Visit its web page:
http://page.math.tu-berlin.de/~kant/kash.html

.. TODO::

    Update the following sentence.

It is not enough to just have KASH installed on your computer.

The KASH interface offers three pieces of functionality:


#. ``kash_console()`` - A function that dumps you into
   an interactive command-line KASH session. Alternatively,

   type ``!kash`` from the Sage prompt.

#. ``kash(expr)`` - Creation of a Sage object that
   wraps a KASH object. This provides a Pythonic interface to KASH.
   For example, if ``f=kash.new(10)``, then
   ``f.Factors()`` returns the prime factorization of
   `10` computed using KASH.

#. ``kash.function_name(args ...)`` - Call the
   indicated KASH function with the given arguments are return the
   result as a KASH object.

#. ``kash.eval(expr)`` - Evaluation of arbitrary KASH
   expressions, with the result returned as a string.


Issues
------

For some reason hitting :kbd:`Control` + :kbd:`C` to interrupt a calculation
does not work correctly. (TODO)

Tutorial
--------

The examples in this tutorial require that kash be installed.

Basics
~~~~~~

Basic arithmetic is straightforward. First, we obtain the result as
a string.

::

    sage: kash.eval('(9 - 7) * (5 + 6)')                # optional -- kash
    '22'

Next we obtain the result as a new KASH object.

::

    sage: a = kash('(9 - 7) * (5 + 6)'); a              # optional -- kash
    22
    sage: a.parent()                                    # optional -- kash
    Kash

We can do arithmetic and call functions on KASH objects::

    sage: a*a                                           # optional -- kash
    484
    sage: a.Factorial()                                 # optional -- kash
    1124000727777607680000

Integrated Help
~~~~~~~~~~~~~~~

Use the ``kash.help(name)`` command to get help about a
given command. This returns a list of help for each of the
definitions of ``name``. Use ``print
kash.help(name)`` to nicely print out all signatures.

Arithmetic
~~~~~~~~~~

Using the ``kash.new`` command we create Kash objects
on which one can do arithmetic.

::

    sage: # optional - kash
    sage: a = kash(12345)
    sage: b = kash(25)
    sage: a/b
    2469/5
    sage: a**b
    1937659030411463935651167391656422626577614411586152317674869233464019922771432158872187137603759765625

Variable assignment
~~~~~~~~~~~~~~~~~~~

Variable assignment using ``kash`` is takes place in
Sage.

::

    sage: a = kash('32233')                        # optional -- kash
    sage: a                                        # optional -- kash
    32233

In particular, ``a`` is not defined as part of the KASH
session itself.

::

    sage: kash.eval('a')                           # optional -- kash
    "Error, the variable 'a' must have a value"

Use ``a.name()`` to get the name of the KASH variable::

    sage: a.name()                                 # somewhat random; optional - kash
    'sage0'
    sage: kash(a.name())                           # optional -- kash
    32233

Integers and Rationals
~~~~~~~~~~~~~~~~~~~~~~

We illustrate arithmetic with integers and rationals in KASH.

::

    sage: # optional - kash
    sage: F = kash.Factorization(4352)
    sage: F[1]
    <2, 8>
    sage: F[2]
    <17, 1>
    sage: F
    [ <2, 8>, <17, 1> ], extended by:
      ext1 := 1,
      ext2 := Unassign

.. NOTE::

   For some very large numbers KASH's integer factorization seems much
   faster than PARI's (which is the default in Sage).

::

    sage: # optional - kash
    sage: kash.GCD(15,25)
    5
    sage: kash.LCM(15,25)
    75
    sage: kash.Div(25,15)
    1
    sage: kash(17) % kash(5)
    2
    sage: kash.IsPrime(10007)
    TRUE
    sage: kash.IsPrime(2005)
    FALSE

    sage: kash.NextPrime(10007)                    # optional -- kash
    10009

Real and Complex Numbers
~~~~~~~~~~~~~~~~~~~~~~~~

::

    sage: # optional - kash
    sage: kash.Precision()
    30
    sage: kash('R')
    Real field of precision 30
    sage: kash.Precision(40)
    40
    sage: kash('R')
    Real field of precision 40
    sage: z = kash('1 + 2*I')
    sage: z
    1.000000000000000000000000000000000000000 + 2.000000000000000000000000000000000000000*I
    sage: z*z
    -3.000000000000000000000000000000000000000 + 4.000000000000000000000000000000000000000*I

    sage: kash.Cos('1.24')                         # optional -- kash
    0.3247962844387762365776934156973803996992
    sage: kash('1.24').Cos()                       # optional -- kash
    0.3247962844387762365776934156973803996992

    sage: kash.Exp('1.24')                         # optional -- kash
    3.455613464762675598057615494121998175400

    sage: kash.Precision(30)                       # optional -- kash
    30
    sage: kash.Log('3+4*I')                        # optional -- kash
    1.60943791243410037460075933323 + 0.927295218001612232428512462922*I
    sage: kash.Log('I')                            # optional -- kash
    1.57079632679489661923132169164*I

    sage: kash.Sqrt(4)                             # optional -- kash
    2.00000000000000000000000000000
    sage: kash.Sqrt(2)                             # optional -- kash
    1.41421356237309504880168872421

    sage: kash.Floor('9/5')                        # optional -- kash
    1
    sage: kash.Floor('3/5')                        # optional -- kash
    0

    sage: x_c = kash('3+I')                        # optional -- kash
    sage: x_c.Argument()                           # optional -- kash
    0.321750554396642193401404614359
    sage: x_c.Imaginary()                          # optional -- kash
    1.00000000000000000000000000000

Lists
~~~~~

Note that list appends are completely different in KASH than in
Python. Use underscore after the function name for the mutation
version.

::

    sage: # optional - kash
    sage: v = kash([1,2,3]); v
    [ 1, 2, 3 ]
    sage: v[1]
    1
    sage: v[3]
    3
    sage: v.Append([5])
    [ 1, 2, 3, 5 ]
    sage: v
    [ 1, 2, 3 ]
    sage: v.Append_([5, 6])
    SUCCESS
    sage: v
    [ 1, 2, 3, 5, 6 ]
    sage: v.Add(5)
    [ 1, 2, 3, 5, 6, 5 ]
    sage: v
    [ 1, 2, 3, 5, 6 ]
    sage: v.Add_(5)
    SUCCESS
    sage: v
    [ 1, 2, 3, 5, 6, 5 ]

The ``Apply`` command applies a function to each
element of a list::

    sage: # optional - kash
    sage: L = kash([1,2,3,4])
    sage: L.Apply('i -> 3*i')
    [ 3, 6, 9, 12 ]
    sage: L
    [ 1, 2, 3, 4 ]
    sage: L.Apply('IsEven')
    [ FALSE, TRUE, FALSE, TRUE ]
    sage: L
    [ 1, 2, 3, 4 ]

Ranges
~~~~~~

the following are examples of ranges.

::

    sage: # optional - kash
    sage: L = kash('[1..10]')
    sage: L
    [ 1 .. 10 ]
    sage: L = kash('[2,4..100]')
    sage: L
    [ 2, 4 .. 100 ]

Sequences
~~~~~~~~~

Tuples
~~~~~~

Polynomials
~~~~~~~~~~~

::

    sage: # optional - kash
    sage: f = kash('X^3 + X + 1')
    sage: f + f
    2*X^3 + 2*X + 2
    sage: f * f
    X^6 + 2*X^4 + 2*X^3 + X^2 + 2*X + 1
    sage: f.Evaluate(10)
    1011
    sage: Qx = kash.PolynomialAlgebra('Q')
    sage: Qx.gen(1)**5 + kash('7/3')
    sage1.1^5 + 7/3

Number Fields
~~~~~~~~~~~~~

We create an equation order.

::

    sage: f = kash('X^5 + 4*X^4 - 56*X^2 -16*X + 192')    # optional -- kash
    sage: OK = f.EquationOrder()                          # optional -- kash
    sage: OK                                              # optional -- kash
    Equation Order with defining polynomial X^5 + 4*X^4 - 56*X^2 - 16*X + 192 over Z

::

    sage: # optional - kash
    sage: f = kash('X^5 + 4*X^4 - 56*X^2 -16*X + 192')
    sage: O = f.EquationOrder()
    sage: a = O.gen(2)
    sage: a
    [0, 1, 0, 0, 0]
    sage: O.Basis()
    [
    _NG.1,
    _NG.2,
    _NG.3,
    _NG.4,
    _NG.5
    ]
    sage: O.Discriminant()
    1364202618880
    sage: O.MaximalOrder()
    Maximal Order of sage2

    sage: O = kash.MaximalOrder('X^3 - 77')                  # optional -- kash
    sage: I = O.Ideal(5,[2, 1, 0])                           # optional -- kash
    sage: I                    # name sage14 below random; optional -- kash
    Ideal of sage14
    Two element generators:
    [5, 0, 0]
    [2, 1, 0]

    sage: F = I.Factorisation()                  # optional -- kash
    sage: F                    # name sage14 random; optional -- kash
    [
    <Prime Ideal of sage14
    Two element generators:
    [5, 0, 0]
    [2, 1, 0], 1>
    ]

Determining whether an ideal is principal.

::

    sage: I.IsPrincipal()                      # optional -- kash
    FALSE, extended by:
    ext1 := Unassign

Computation of class groups and unit groups::

    sage: # optional - kash
    sage: f = kash('X^5 + 4*X^4 - 56*X^2 -16*X + 192')
    sage: O = kash.EquationOrder(f)
    sage: OK = O.MaximalOrder()
    sage: OK.ClassGroup()
    Abelian Group isomorphic to Z/6
      Defined on 1 generator
      Relations:
      6*sage32.1 = 0, extended by:
      ext1 := Mapping from: grp^abl: sage32 to ids/ord^num: _AA

::

    sage: U = OK.UnitGroup()                                  # optional -- kash
    sage: U        # name sage34 below random; optional -- kash
    Abelian Group isomorphic to Z/2 + Z + Z
      Defined on 3 generators
      Relations:
      2*sage34.1 = 0, extended by:
      ext1 := Mapping from: grp^abl: sage34 to ord^num: sage30

    sage: kash.Apply('x->%s.ext1(x)'%U.name(), U.Generators().List())     # optional -- kash
    [ [1, -1, 0, 0, 0], [1, 1, 0, 0, 0], [-1, 0, 0, 0, 0] ]

Function Fields
~~~~~~~~~~~~~~~

::

    sage: # optional - kash
    sage: k = kash.FiniteField(25)
    sage: kT = k.RationalFunctionField()
    sage: kTy = kT.PolynomialAlgebra()
    sage: T = kT.gen(1)
    sage: y = kTy.gen(1)
    sage: f = y**3 + T**4 + 1

Long Input
----------

The KASH interface reads in even very long input (using files) in a
robust manner, as long as you are creating a new object.

.. NOTE::

   Using ``kash.eval`` for long input is much less robust, and is not
   recommended.

::

    sage: a = kash(range(10000))                                  # optional -- kash

Note that KASH seems to not support string or integer literals with
more than 1024 digits, which is why the above example uses a list
unlike for the other interfaces.
"""
from .expect import Expect as Expect, ExpectElement as ExpectElement
from sage.misc.instancedoc import instancedoc as instancedoc
from sage.misc.sage_eval import sage_eval as sage_eval

class Kash(Expect):
    """
    Interface to the Kash interpreter.

    AUTHORS:

    - William Stein and David Joyner
    """
    def __init__(self, max_workspace_size=None, maxread=None, script_subdirectory=None, restart_on_ctrlc: bool = True, logfile=None, server=None, server_tmpdir=None) -> None:
        """
        INPUT:

        - ``max_workspace_size`` -- (default: ``None``)
          set maximal workspace memory usage to <mem>
          <mem> stands for byte-wise allocation
          <mem>k stands for kilobyte-wise allocation
          <mem>m stands for megabyte-wise allocation
        """
    def clear(self, var) -> None:
        """
        Clear the variable named ``var``.

        Kash variables have a record structure, so if sage1 is a
        polynomial ring, sage1.1 will be its indeterminate.  This
        prevents us from easily reusing variables, since sage1.1
        might still have references even if sage1 does not.

        For now, we don't implement variable clearing to avoid these
        problems, and instead implement this method with a noop.
        """
    def __reduce__(self): ...
    def eval(self, x, newlines: bool = False, strip: bool = True, **kwds):
        """
        Send the code in the string s to the Kash interpreter and return
        the output as a string.

        INPUT:

        - ``s`` -- string containing Kash code

        - ``newlines`` -- boolean (default: ``True``); if ``False``,
          remove all backslash-newlines inserted by the Kash output formatter

        - ``strip`` -- ignored
        """
    def help(self, name=None) -> None:
        """
        Return help on KASH commands.

        This returns help on all commands with a given name.  If name
        is ``None``, return the location of the installed Kash HTML
        documentation.

        EXAMPLES::

            sage: X = kash.help('IntegerRing')   # random; optional -- kash
            1439: IntegerRing() -> <ord^rat>
            1440: IntegerRing(<elt-ord^rat> m) -> <res^rat>
            1441: IntegerRing(<seq()> Q) -> <res^rat>
            1442: IntegerRing(<fld^rat> K) -> <ord^rat>
            1443: IntegerRing(<fld^fra> K) -> <ord^num>
            1444: IntegerRing(<rng> K) -> <rng>
            1445: IntegerRing(<fld^pad> L) -> <ord^pad>

        There is one entry in X for each item found in the documentation
        for this function: If you type ``print(X[0])`` you will
        get help on about the first one, printed nicely to the screen.

        AUTHORS:

        - Sebastion Pauli (2006-02-04): during Sage coding sprint
        """
    def help_search(self, name): ...
    def set(self, var, value) -> None:
        """
        Set the variable var to the given value.
        """
    def get(self, var):
        """
        Get the value of the variable var.
        """
    def function_call(self, function, args=None, kwds=None):
        """
        EXAMPLES::

            sage: kash.function_call('ComplexToPolar', [1+I], {'Results' : 1})   # optional -- kash
            1.41421356237309504880168872421
        """
    def console(self) -> None: ...
    def version(self): ...

class KashElement(ExpectElement):
    def __mod__(self, other): ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool:
        """
        Return ``True`` if this Kash element is not 0 or FALSE.

        EXAMPLES::

            sage: bool(kash('FALSE'))                   # optional -- kash
            False
            sage: bool(kash('TRUE'))                    # optional -- kash
            True

            sage: bool(kash(0))                         # optional -- kash
            False
            sage: bool(kash(1))                         # optional -- kash
            True
        """

class KashDocumentation(list): ...

def is_KashElement(x):
    """
    Return ``True`` if ``x`` is of type :class:`KashElement`.

    EXAMPLES::

        sage: from sage.interfaces.kash import is_KashElement
        sage: is_KashElement(2)
        doctest:...: DeprecationWarning: the function is_KashElement is deprecated; use isinstance(x, sage.interfaces.abc.KashElement) instead
        See https://github.com/sagemath/sage/issues/34804 for details.
        False
        sage: is_KashElement(kash(2))  # optional - kash
        True
    """

kash: Kash

def reduce_load_Kash(): ...
def kash_console() -> None: ...
def kash_version() -> str: ...
