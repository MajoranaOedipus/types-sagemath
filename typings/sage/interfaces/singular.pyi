r"""
Interface to Singular

Introduction
------------

This interface is extremely flexible, since it's exactly like
typing into the Singular interpreter, and anything that works there
should work here.

The Singular interface will only work if Singular is installed on
your computer; this should be the case, since Singular is included
with Sage. The interface offers three pieces of functionality:

#. ``singular_console()`` -- a function that dumps you
   into an interactive command-line Singular session.

#. ``singular(expr, type='def')`` -- creation of a
   Singular object. This provides a Pythonic interface to Singular.
   For example, if ``f=singular(10)``, then
   ``f.factorize()`` returns the factorization of
   `10` computed using Singular.

#. ``singular.eval(expr)`` -- evaluation of arbitrary
   Singular expressions, with the result returned as a string.

Of course, there are polynomial rings and ideals in Sage as well
(often based on a C-library interface to Singular). One can convert
an object in the Singular interpreter interface to Sage by the
method ``sage()``.


Tutorial
--------

EXAMPLES: First we illustrate multivariate polynomial
factorization::

    sage: R1 = singular.ring(0, '(x,y)', 'dp')
    sage: R1
    polynomial ring, over a field, global ordering
    // coefficients: QQ...
    // number of vars : 2
    //        block   1 : ordering dp
    //                  : names    x y
    //        block   2 : ordering C
    sage: f = singular('9x16 - 18x13y2 - 9x12y3 + 9x10y4 - 18x11y2 + 36x8y4 + 18x7y5 - 18x5y6 + 9x6y4 - 18x3y6 - 9x2y7 + 9y8')
    sage: f
    9*x^16-18*x^13*y^2-9*x^12*y^3+9*x^10*y^4-18*x^11*y^2+36*x^8*y^4+18*x^7*y^5-18*x^5*y^6+9*x^6*y^4-18*x^3*y^6-9*x^2*y^7+9*y^8
    sage: f.parent()
    Singular

::

    sage: F = f.factorize(); F
    [1]:
       _[1]=9
       _[2]=x^6-2*x^3*y^2-x^2*y^3+y^4
       _[3]=-x^5+y^2
    [2]:
       1,1,2

::

    sage: F[1]
    9,
    x^6-2*x^3*y^2-x^2*y^3+y^4,
    -x^5+y^2
    sage: F[1][2]
    x^6-2*x^3*y^2-x^2*y^3+y^4

We can convert `f` and each exponent back to Sage objects
as well.

::

    sage: g = f.sage(); g
    9*x^16 - 18*x^13*y^2 - 9*x^12*y^3 + 9*x^10*y^4 - 18*x^11*y^2 + 36*x^8*y^4 + 18*x^7*y^5 - 18*x^5*y^6 + 9*x^6*y^4 - 18*x^3*y^6 - 9*x^2*y^7 + 9*y^8
    sage: F[1][2].sage()
    x^6 - 2*x^3*y^2 - x^2*y^3 + y^4
    sage: g.parent()
    Multivariate Polynomial Ring in x, y over Rational Field

This example illustrates polynomial GCD's::

    sage: R2 = singular.ring(0, '(x,y,z)', 'lp')
    sage: a = singular.new('3x2*(x+y)')
    sage: b = singular.new('9x*(y2-x2)')
    sage: g = a.gcd(b)
    sage: g
    x^2+x*y

This example illustrates computation of a Groebner basis::

    sage: R3 = singular.ring(0, '(a,b,c,d)', 'lp')
    sage: I = singular.ideal(['a + b + c + d', 'a*b + a*d + b*c + c*d', 'a*b*c + a*b*d + a*c*d + b*c*d', 'a*b*c*d - 1'])
    sage: I2 = I.groebner()
    sage: I2
    c^2*d^6-c^2*d^2-d^4+1,
    c^3*d^2+c^2*d^3-c-d,
    b*d^4-b+d^5-d,
    b*c-b*d^5+c^2*d^4+c*d-d^6-d^2,
    b^2+2*b*d+d^2,
    a+b+c+d

The following example is the same as the one in the Singular - Gap
interface documentation::

    sage: R  = singular.ring(0, '(x0,x1,x2)', 'lp')
    sage: I1 = singular.ideal(['x0*x1*x2 -x0^2*x2', 'x0^2*x1*x2-x0*x1^2*x2-x0*x1*x2^2', 'x0*x1-x0*x2-x1*x2'])
    sage: I2 = I1.groebner()
    sage: I2
    x1^2*x2^2,
    x0*x2^3-x1^2*x2^2+x1*x2^3,
    x0*x1-x0*x2-x1*x2,
    x0^2*x2-x0*x2^2-x1*x2^2
    sage: I2.sage()
    Ideal (x1^2*x2^2, x0*x2^3 - x1^2*x2^2 + x1*x2^3, x0*x1 - x0*x2 - x1*x2, x0^2*x2 - x0*x2^2 - x1*x2^2) of Multivariate Polynomial Ring in x0, x1, x2 over Rational Field


This example illustrates moving a polynomial from one ring to
another. It also illustrates calling a method of an object with an
argument.

::

    sage: R = singular.ring(0, '(x,y,z)', 'dp')
    sage: f = singular('x3+y3+(x-y)*x2y2+z2')
    sage: f
    x^3*y^2-x^2*y^3+x^3+y^3+z^2
    sage: R1 = singular.ring(0, '(x,y,z)', 'ds')
    sage: f = R.fetch(f)
    sage: f
    z^2+x^3+y^3+x^3*y^2-x^2*y^3

We can calculate the Milnor number of `f`::

    sage: _=singular.LIB('sing.lib')     # assign to _ to suppress printing
    sage: f.milnor()
    4

The Jacobian applied twice yields the Hessian matrix of
`f`, with which we can compute.

::

    sage: H = f.jacob().jacob()
    sage: H
    6*x+6*x*y^2-2*y^3,6*x^2*y-6*x*y^2,  0,
    6*x^2*y-6*x*y^2,  6*y+2*x^3-6*x^2*y,0,
    0,                0,                2
    sage: H.sage()
    [6*x + 6*x*y^2 - 2*y^3     6*x^2*y - 6*x*y^2                     0]
    [    6*x^2*y - 6*x*y^2 6*y + 2*x^3 - 6*x^2*y                     0]
    [                    0                     0                     2]
    sage: H.det()   # This is a polynomial in Singular
    72*x*y+24*x^4-72*x^3*y+72*x*y^3-24*y^4-48*x^4*y^2+64*x^3*y^3-48*x^2*y^4
    sage: H.det().sage()   # This is the corresponding polynomial in Sage
    72*x*y + 24*x^4 - 72*x^3*y + 72*x*y^3 - 24*y^4 - 48*x^4*y^2 + 64*x^3*y^3 - 48*x^2*y^4

The 1x1 and 2x2 minors::

    sage: H.minor(1)
    2,
    6*y+2*x^3-6*x^2*y,
    6*x^2*y-6*x*y^2,
    6*x^2*y-6*x*y^2,
    6*x+6*x*y^2-2*y^3,
    0,
    0,
    0,
    0
    sage: H.minor(2)
    12*y+4*x^3-12*x^2*y,
    12*x^2*y-12*x*y^2,
    12*x^2*y-12*x*y^2,
    12*x+12*x*y^2-4*y^3,
    -36*x*y-12*x^4+36*x^3*y-36*x*y^3+12*y^4+24*x^4*y^2-32*x^3*y^3+24*x^2*y^4,
    0,
    0,
    0,
    0

::

    sage: _=singular.eval('option(redSB)')
    sage: H.minor(1).groebner()
    1

Computing the Genus
-------------------

We compute the projective genus of ideals that define curves over
`\QQ`. It is *very important* to load the
``normal.lib`` library before calling the
``genus`` command, or you'll get an error message.

EXAMPLES::

    sage: singular.lib('normal.lib')
    sage: R = singular.ring(0,'(x,y)','dp')
    sage: i2 = singular.ideal('y9 - x2*(x-1)^9 + x')
    sage: i2.genus()
    40

Note that the genus can be much smaller than the degree::

    sage: i = singular.ideal('y9 - x2*(x-1)^9')
    sage: i.genus()
    0

An Important Concept
--------------------

The following illustrates an important concept: how Sage interacts
with the data being used and returned by Singular. Let's compute a
Groebner basis for some ideal, using Singular through Sage.

::

    sage: singular.lib('polylib.lib')
    sage: singular.ring(32003, '(a,b,c,d,e,f)', 'lp')
    polynomial ring, over a field, global ordering
    // coefficients: ZZ/32003...
    // number of vars : 6
    //        block   1 : ordering lp
    //                        : names    a b c d e f
    //        block   2 : ordering C
    sage: I = singular.ideal('cyclic(6)')
    sage: g = singular('groebner(I)')
    Traceback (most recent call last):
    ...
    TypeError: Singular error:
    ...

We restart everything and try again, but correctly.

::

    sage: singular.quit()
    sage: singular.lib('polylib.lib'); R = singular.ring(32003, '(a,b,c,d,e,f)', 'lp')
    sage: I = singular.ideal('cyclic(6)')
    sage: I.groebner()
    f^48-2554*f^42-15674*f^36+12326*f^30-12326*f^18+15674*f^12+2554*f^6-1,
    ...

It's important to understand why the first attempt at computing a
basis failed. The line where we gave singular the input
'groebner(I)' was useless because Singular has no idea what 'I' is!
Although 'I' is an object that we computed with calls to Singular
functions, it actually lives in Sage. As a consequence, the name
'I' means nothing to Singular. When we called
``I.groebner()``, Sage was able to call the groebner
function on 'I' in Singular, since 'I' actually means something to
Sage.

Long Input
----------

The Singular interface reads in even very long input (using files)
in a robust manner, as long as you are creating a new object.

::

    sage: t = '"%s"'%10^15000   # 15 thousand character string (note that normal Singular input must be at most 10000)
    sage: a = singular.eval(t)
    sage: a = singular(t)

TESTS:

We test an automatic coercion::

    sage: a = 3*singular('2'); a
    6
    sage: type(a)
    <class 'sage.interfaces.singular.SingularElement'>
    sage: a = singular('2')*3; a
    6
    sage: type(a)
    <class 'sage.interfaces.singular.SingularElement'>

Create a ring over GF(9) to check that ``gftables`` has been installed,
see :issue:`11645`::

    sage: singular.eval("ring testgf9 = (9,x),(a,b,c,d,e,f),(M((1,2,3,0)),wp(2,3),lp);")
    ''

Verify that :issue:`17720` is fixed::

    sage: R.<p> = QQ[]
    sage: K.<p> = QQ.extension(p^2 - p - 1)
    sage: r.<x,z> = K[]
    sage: I = r.ideal(z)
    sage: I.primary_decomposition()
    [Ideal (z) of Multivariate Polynomial Ring in x, z over Number Field in p with defining polynomial p^2 - p - 1]
    sage: [ J.gens() for J in I.primary_decomposition("gtz")]
    [[z]]

AUTHORS:

- David Joyner and William Stein (2005): first version

- Neal Harris (unknown): perhaps added "An Important Concept"

- Martin Albrecht (2006-03-05): code so singular.[tab] and x =
  singular(...), x.[tab] includes all singular commands.

- Martin Albrecht (2006-03-06): This patch adds the equality symbol to
  singular. Also fix a problem in which " " as prompt means comparison
  will break all further communication with Singular.

- Martin Albrecht (2006-03-13): added current_ring() and
  current_ring_name()

- William Stein (2006-04-10): Fixed problems with ideal constructor

- Martin Albrecht (2006-05-18): added sage_poly.

- Simon King (2010-11-23): Reduce the overhead caused by waiting for
  the Singular prompt by doing garbage collection differently.

- Simon King (2011-06-06): Make conversion from Singular to Sage more flexible.

- Simon King (2015): Extend pickling capabilities.
"""
import sage.interfaces.abc
import types
from _typeshed import Incomplete
from sage.interfaces.expect import Expect as Expect, ExpectElement as ExpectElement, ExpectFunction as ExpectFunction, FunctionElement as FunctionElement
from sage.interfaces.tab_completion import ExtraTabCompletion as ExtraTabCompletion
from sage.misc.instancedoc import instancedoc as instancedoc
from sage.misc.verbose import get_verbose as get_verbose
from sage.structure.element import RingElement as RingElement
from sage.structure.sequence import Sequence_generic as Sequence_generic

class SingularError(RuntimeError):
    """
    Raised if Singular printed an error message
    """

class Singular(ExtraTabCompletion, Expect):
    """
    Interface to the Singular interpreter.

    EXAMPLES: A Groebner basis example.

    ::

        sage: R = singular.ring(0, '(x0,x1,x2)', 'lp')
        sage: I = singular.ideal([ 'x0*x1*x2 -x0^2*x2', 'x0^2*x1*x2-x0*x1^2*x2-x0*x1*x2^2', 'x0*x1-x0*x2-x1*x2'])
        sage: I.groebner()
        x1^2*x2^2,
        x0*x2^3-x1^2*x2^2+x1*x2^3,
        x0*x1-x0*x2-x1*x2,
        x0^2*x2-x0*x2^2-x1*x2^2

    AUTHORS:

    - David Joyner and William Stein
    """
    def __init__(self, maxread=None, script_subdirectory=None, logfile=None, server=None, server_tmpdir=None, seed=None) -> None:
        """
        EXAMPLES::

            sage: from sage.interfaces.singular import singular
            sage: singular == loads(dumps(singular))
            True
        """
    def set_seed(self, seed=None):
        """
        Set the seed for singular interpreter.

        The seed should be an integer at least 1
        and not more than 30 bits.
        See
        http://www.singular.uni-kl.de/Manual/html/sing_19.htm#SEC26
        and
        http://www.singular.uni-kl.de/Manual/html/sing_283.htm#SEC323

        EXAMPLES::

            sage: s = Singular()
            sage: s.set_seed(1)
            1
            sage: [s.random(1,10) for i in range(5)]
            [8, 10, 4, 9, 1]
        """
    def __reduce__(self):
        """
        EXAMPLES::

            sage: from sage.interfaces.singular import singular
            sage: singular.__reduce__()
            (<function reduce_load_Singular at 0x...>, ())
        """
    def eval(self, x, allow_semicolon: bool = True, strip: bool = True, **kwds):
        """
        Send the code x to the Singular interpreter and return the output
        as a string.

        INPUT:

        - ``x`` -- string (of code)

        - ``allow_semicolon`` -- (default: ``False``) if ``False`` then
          raise a :exc:`TypeError` if the input line contains a semicolon

        - ``strip`` -- ignored

        EXAMPLES::

            sage: singular.eval('2 > 1')
            '1'
            sage: singular.eval('2 + 2')
            '4'

        if the verbosity level is `> 1` comments are also printed
        and not only returned.

        ::

            sage: r = singular.ring(0,'(x,y,z)','dp')
            sage: i = singular.ideal(['x^2','y^2','z^2'])
            sage: s = i.std()
            sage: singular.eval('hilb(%s)'%(s.name()))
            '...// dimension (affine) = 0\\n//
            degree (affine) = 8'

        ::

            sage: from sage.misc.verbose import set_verbose
            sage: set_verbose(1)
            sage: o = singular.eval('hilb(%s)'%(s.name()))
            ...// dimension (affine) = 0
            // degree (affine)  = 8

        This is mainly useful if this method is called implicitly. Because
        then intermediate results, debugging outputs and printed statements
        are printed

        ::

            sage: o = s.hilb()
            ...// dimension (affine) = 0
            // degree (affine)  = 8
            // ** right side is not a datum, assignment ignored
            ...

        rather than ignored

        ::

            sage: set_verbose(0)
            sage: o = s.hilb()
        """
    def set(self, type, name, value) -> None:
        """
        Set the variable with given name to the given value.

        REMARK:

        If a variable in the Singular interface was previously marked for
        deletion, the actual deletion is done here, before the new variable
        is created in Singular.

        EXAMPLES::

            sage: singular.set('int', 'x', '2')
            sage: singular.get('x')
            '2'

        We test that an unused variable is only actually deleted if this method
        is called::

            sage: a = singular(3)
            sage: n = a.name()
            sage: del a
            sage: singular.eval(n)
            '3'
            sage: singular.set('int', 'y', '5')
            sage: singular.eval('defined(%s)'%n)
            '0'
        """
    def get(self, var):
        """
        Get string representation of variable named var.

        EXAMPLES::

            sage: singular.set('int', 'x', '2')
            sage: singular.get('x')
            '2'
        """
    def clear(self, var) -> None:
        '''
        Clear the variable named ``var``.

        EXAMPLES::

            sage: singular.set(\'int\', \'x\', \'2\')
            sage: singular.get(\'x\')
            \'2\'
            sage: singular.clear(\'x\')

        "Clearing the variable" means to allow to free the memory
        that it uses in the Singular sub-process. However, the
        actual deletion of the variable is only committed when
        the next element in the Singular interface is created::

            sage: singular.get(\'x\')
            \'2\'
            sage: a = singular(3)
            sage: singular.get(\'x\')
            \'`x`\'
        '''
    def __call__(self, x, type: str = 'def'):
        """
        Create a singular object X with given type determined by the string
        x. This returns var, where var is built using the Singular
        statement type var = ... x ... Note that the actual name of var
        could be anything, and can be recovered using X.name().

        The object X returned can be used like any Sage object, and wraps
        an object in ``self``. The standard arithmetic operators work. Moreover
        if foo is a function then X.foo(y,z,...) calls foo(X, y, z, ...)
        and returns the corresponding object.

        EXAMPLES::

            sage: R = singular.ring(0, '(x0,x1,x2)', 'lp')
            sage: I = singular.ideal([ 'x0*x1*x2 -x0^2*x2', 'x0^2*x1*x2-x0*x1^2*x2-x0*x1*x2^2', 'x0*x1-x0*x2-x1*x2'])
            sage: I
             -x0^2*x2+x0*x1*x2,
            x0^2*x1*x2-x0*x1^2*x2-x0*x1*x2^2,
            x0*x1-x0*x2-x1*x2
            sage: type(I)
            <class 'sage.interfaces.singular.SingularElement'>
            sage: I.parent()
            Singular
        """
    def cputime(self, t=None):
        """
        Return the amount of CPU time that the Singular session has used.
        If ``t`` is not None, then it returns the difference
        between the current CPU time and ``t``.

        EXAMPLES::

            sage: t = singular.cputime()
            sage: R = singular.ring(0, '(x0,x1,x2)', 'lp')
            sage: I = singular.ideal([ 'x0*x1*x2 -x0^2*x2', 'x0^2*x1*x2-x0*x1^2*x2-x0*x1*x2^2', 'x0*x1-x0*x2-x1*x2'])
            sage: gb = I.groebner()
            sage: singular.cputime(t) #random
            0.02
        """
    def lib(self, lib, reload: bool = False) -> None:
        """
        Load the Singular library named lib.

        Note that if the library was already loaded during this session it
        is not reloaded unless the optional reload argument is ``True`` (the
        default is ``False``).

        EXAMPLES::

            sage: singular.lib('sing.lib')
            sage: singular.lib('sing.lib', reload=True)
        """
    LIB = lib
    load = lib
    def ideal(self, *gens):
        '''
        Return the ideal generated by gens.

        INPUT:

        - ``gens`` -- list or tuple of Singular objects (or
          objects that can be made into Singular objects via evaluation)

        OUTPUT: the Singular ideal generated by the given list of gens

        EXAMPLES: A Groebner basis example done in a different way.

        ::

            sage: _ = singular.eval("ring R=0,(x0,x1,x2),lp")
            sage: i1 = singular.ideal([ \'x0*x1*x2 -x0^2*x2\', \'x0^2*x1*x2-x0*x1^2*x2-x0*x1*x2^2\', \'x0*x1-x0*x2-x1*x2\'])
            sage: i1
            -x0^2*x2+x0*x1*x2,
            x0^2*x1*x2-x0*x1^2*x2-x0*x1*x2^2,
            x0*x1-x0*x2-x1*x2

        ::

            sage: i2 = singular.ideal(\'groebner(%s);\'%i1.name())
            sage: i2
            x1^2*x2^2,
            x0*x2^3-x1^2*x2^2+x1*x2^3,
            x0*x1-x0*x2-x1*x2,
            x0^2*x2-x0*x2^2-x1*x2^2
        '''
    def list(self, x):
        '''
        Create a list in Singular from a Sage list ``x``.

        EXAMPLES::

            sage: singular.list([1,2])
            [1]:
               1
            [2]:
               2

            sage: singular.list([1,2,[3,4]])
            [1]:
               1
            [2]:
               2
            [3]:
               [1]:
                  3
               [2]:
                  4

            sage: R.<x,y> = QQ[]
            sage: singular.list([1,2,[x,ideal(x,y)]])
            [1]:
               1
            [2]:
               2
            [3]:
               [1]:
                  x
               [2]:
                  _[1]=x
                  _[2]=y

        Strings have to be escaped before passing them to this method::

            sage: singular.list([1,2,\'"hi"\'])
            [1]:
               1
            [2]:
               2
            [3]:
               hi

        TESTS:

        Check that a list already converted to Singular can be
        embedded into a list to be converted::

            sage: singular.list([1, 2, singular.list([3, 4])])
            [1]:
               1
            [2]:
               2
            [3]:
               [1]:
                  3
               [2]:
                  4
        '''
    def matrix(self, nrows, ncols, entries=None):
        '''
        EXAMPLES::

            sage: singular.lib("matrix")
            sage: R = singular.ring(0, \'(x,y,z)\', \'dp\')
            sage: A = singular.matrix(3,2,\'1,2,3,4,5,6\')
            sage: A
            1,2,
            3,4,
            5,6
            sage: A.gauss_col()
            2,-1,
            1,0,
            0,1

        AUTHORS:

        - Martin Albrecht (2006-01-14)
        '''
    def ring(self, char: int = 0, vars: str = '(x)', order: str = 'lp', check=None):
        '''
        Create a Singular ring and makes it the current ring.

        INPUT:

        - ``char`` -- string; a string specifying the characteristic
          of the base ring, in the format accepted by Singular (see
          examples below)

        - ``vars`` -- tuple or string defining the variable names

        - ``order`` -- string; the monomial order (default: ``\'lp\'``)

        OUTPUT: a Singular ring

        .. NOTE::

           This function is *not* identical to calling the Singular
           ``ring`` function. In particular, it also attempts to
           "kill" the variable names, so they can actually be used
           without getting errors, and it sets printing of elements
           for this range to short (i.e., with \\*\'s and carets).

        EXAMPLES: We first declare `\\QQ[x,y,z]` with degree reverse
        lexicographic ordering.

        ::

            sage: R = singular.ring(0, \'(x,y,z)\', \'dp\')
            sage: R
            polynomial ring, over a field, global ordering
            // coefficients: QQ...
            // number of vars : 3
            //        block   1 : ordering dp
            //                  : names    x y z
            //        block   2 : ordering C

        ::

            sage: R1 = singular.ring(32003, \'(x,y,z)\', \'dp\')
            sage: R2 = singular.ring(32003, \'(a,b,c,d)\', \'lp\')

        This is a ring in variables named x(1) through x(10) over the
        finite field of order `7`::

            sage: R3 = singular.ring(7, \'(x(1..10))\', \'ds\')

        This is a polynomial ring over the transcendental extension
        `\\QQ(a)` of `\\QQ`::

            sage: R4 = singular.ring(\'(0,a)\', \'(mu,nu)\', \'lp\')

        This is a ring over the field of single-precision floats::

            sage: R5 = singular.ring(\'real\', \'(a,b)\', \'lp\')

        This is over 50-digit floats::

            sage: R6 = singular.ring(\'(real,50)\', \'(a,b)\', \'lp\')
            sage: R7 = singular.ring(\'(complex,50,i)\', \'(a,b)\', \'lp\')

        To use a ring that you\'ve defined, use the set_ring() method on
        the ring. This sets the ring to be the "current ring". For
        example,

        ::

            sage: R = singular.ring(7, \'(a,b)\', \'ds\')
            sage: S = singular.ring(\'real\', \'(a,b)\', \'lp\')
            sage: singular.new(\'10*a\')
            (1.000e+01)*a
            sage: R.set_ring()
            sage: singular.new(\'10*a\')
            3*a
        '''
    def string(self, x):
        '''
        Create a Singular string from a Sage string. Note that the Sage
        string has to be "double-quoted".

        EXAMPLES::

            sage: singular.string(\'"Sage"\')
            Sage
        '''
    def set_ring(self, R) -> None:
        """
        Set the current Singular ring to `R`.

        EXAMPLES::

            sage: R = singular.ring(7, '(a,b)', 'ds')
            sage: S = singular.ring('real', '(a,b)', 'lp')
            sage: singular.current_ring()
            polynomial ring, over a field, global ordering
            // coefficients: Float()...
            // number of vars : 2
            //        block   1 : ordering lp
            //                  : names    a b
            //        block   2 : ordering C
            sage: singular.set_ring(R)
            sage: singular.current_ring()
            polynomial ring, over a field, local ordering
            // coefficients: ZZ/7...
            // number of vars : 2
            //        block   1 : ordering ds
            //                  : names    a b
            //        block   2 : ordering C
        """
    setring = set_ring
    def current_ring_name(self):
        """
        Return the Singular name of the currently active ring in
        Singular.

        OUTPUT: currently active ring's name

        EXAMPLES::

            sage: r = PolynomialRing(GF(127),3,'xyz')
            sage: r._singular_().name() == singular.current_ring_name()
            True
        """
    def current_ring(self):
        """
        Return the current ring of the running Singular session.

        EXAMPLES::

            sage: r = PolynomialRing(GF(127),3,'xyz', order='invlex')
            sage: r._singular_()
            polynomial ring, over a field, global ordering
            // coefficients: ZZ/127...
            // number of vars : 3
            //        block   1 : ordering ip
            //                  : names    x y z
            //        block   2 : ordering C
            sage: singular.current_ring()
            polynomial ring, over a field, global ordering
            // coefficients: ZZ/127...
            // number of vars : 3
            //        block   1 : ordering ip
            //                  : names    x y z
            //        block   2 : ordering C
        """
    def console(self) -> None:
        """
        EXAMPLES::

            sage: singular_console() #not tested
                                 SINGULAR                             /  Development
             A Computer Algebra System for Polynomial Computations   /   version 3-0-4
                                                                   0<
                 by: G.-M. Greuel, G. Pfister, H. Schoenemann        \\   Nov 2007
            FB Mathematik der Universitaet, D-67653 Kaiserslautern    \\\n        """
    def version(self):
        '''
        Return the version of Singular being used.

        EXAMPLES::

            sage: singular.version()
            "Singular ... version 4...
        '''
    def option(self, cmd=None, val=None):
        """
        Access to Singular's options as follows:

        Syntax: option() Returns a string of all defined options.

        Syntax: option( 'option_name' ) Sets an option. Note to disable an
        option, use the prefix no.

        Syntax: option( 'get' ) Returns an intvec of the state of all
        options.

        Syntax: option( 'set', intvec_expression ) Restores the state of
        all options from an intvec (produced by option('get')).

        EXAMPLES::

            sage: singular.option()
            //options: redefine loadLib usage prompt
            sage: singular.option('get')
            0,
            10321
            sage: old_options = _
            sage: singular.option('noredefine')
            sage: singular.option()
            //options: loadLib usage prompt
            sage: singular.option('set', old_options)
            sage: singular.option('get')
            0,
            10321
        """

class SingularElement(ExtraTabCompletion, ExpectElement, sage.interfaces.abc.SingularElement):
    def __init__(self, parent, type, value, is_name: bool = False) -> None:
        """
        EXAMPLES::

            sage: a = singular(2)
            sage: loads(dumps(a))
            2
        """
    def __copy__(self):
        """
        Return a copy of ``self``.

        EXAMPLES::

            sage: R=singular.ring(0,'(x,y)','dp')
            sage: M=singular.matrix(3,3,'0,0,-x, 0,y,0, x*y,0,0')
            sage: N=copy(M)
            sage: N[1,1]=singular('x+y')
            sage: N
            x+y,0,-x,
            0,  y,0,
            x*y,0,0
            sage: M
            0,  0,-x,
            0,  y,0,
            x*y,0,0
            sage: L=R.ringlist()
            sage: L[4]=singular.ideal('x**2-5')
            sage: Q=L.ring()
            sage: otherR=singular.ring(5,'(x)','dp')
            sage: cpQ=copy(Q)
            sage: cpQ.set_ring()
            sage: cpQ
            polynomial ring, over a field, global ordering
            // coefficients: QQ...
            // number of vars : 2
            //        block   1 : ordering dp
            //                  : names    x y
            //        block   2 : ordering C
            // quotient ring from ideal
            _[1]=x^2-5
            sage: R.fetch(M)
            0,  0,-x,
            0,  y,0,
            x*y,0,0
        """
    def __len__(self) -> int:
        """
        Return the size of this Singular element.

        EXAMPLES::

            sage: R = singular.ring(0, '(x,y,z)', 'dp')
            sage: A = singular.matrix(2,2)
            sage: len(A)
            4
        """
    def __setitem__(self, n, value) -> None:
        """
        Set the `n`-th element of ``self`` to `x`.

        INPUT:

        - ``n`` -- integer *or* a 2-tuple (for setting
          matrix elements)

        - ``value`` -- anything (is coerced to a Singular
          object if it is not one already)

        OUTPUT: changes elements of ``self``

        EXAMPLES::

            sage: R = singular.ring(0, '(x,y,z)', 'dp')
            sage: A = singular.matrix(2,2)
            sage: A
            0,0,
            0,0
            sage: A[1,1] = 5
            sage: A
            5,0,
            0,0
            sage: A[1,2] = '5*x + y + z3'
            sage: A
            5,z^3+5*x+y,
            0,0
        """
    def __bool__(self) -> bool:
        """
        Return ``True`` if this Singular element is not zero.

        EXAMPLES::

            sage: bool(singular(0))
            False
            sage: bool(singular(1))
            True
        """
    def sage_polystring(self):
        """
        If this Singular element is a polynomial, return a string
        representation of this polynomial that is suitable for evaluation
        in Python. Thus \\* is used for multiplication and \\*\\* for
        exponentiation. This function is primarily used internally.

        The short=0 option *must* be set for the parent ring or this
        function will not work as expected. This option is set by default
        for rings created using ``singular.ring`` or set using
        ``ring_name.set_ring()``.

        EXAMPLES::

            sage: R = singular.ring(0,'(x,y)')
            sage: f = singular('x^3 + 3*y^11 + 5')
            sage: f
            x^3+3*y^11+5
            sage: f.sage_polystring()
            'x**3+3*y**11+5'
        """
    def sage_global_ring(self):
        '''
        Return the current basering in Singular as a polynomial ring or quotient ring.

        EXAMPLES::

            sage: singular.eval(\'ring r1 = (9,x),(a,b,c,d,e,f),(M((1,2,3,0)),wp(2,3),lp)\')
            \'\'
            sage: R = singular(\'r1\').sage_global_ring()
            sage: R
            Multivariate Polynomial Ring in a, b, c, d, e, f over Finite Field in x of size 3^2
            sage: R.term_order()
            Block term order with blocks:
            (Matrix term order with matrix
            [1 2]
            [3 0],
             Weighted degree reverse lexicographic term order with weights (2, 3),
             Lexicographic term order of length 2)

        ::

            sage: singular.eval(\'ring r2 = (0,x),(a,b,c),dp\')
            \'\'
            sage: singular(\'r2\').sage_global_ring()
            Multivariate Polynomial Ring in a, b, c over Fraction Field of Univariate Polynomial Ring in x over Rational Field

        ::

            sage: singular.eval(\'ring r3 = (3,z),(a,b,c),dp\')
            \'\'
            sage: singular.eval(\'minpoly = 1+z+z2+z3+z4\')
            \'\'
            sage: singular(\'r3\').sage_global_ring()
            Multivariate Polynomial Ring in a, b, c over Finite Field in z of size 3^4

        Real and complex fields in both Singular and Sage are defined with a precision.
        The precision in Singular is given in terms of digits, but in Sage it is given
        in terms of bits. So, the digit precision is internally converted to a reasonable
        bit precision::

            sage: singular.eval(\'ring r4 = (real,20),(a,b,c),dp\')
            \'\'
            sage: singular(\'r4\').sage_global_ring()
            Multivariate Polynomial Ring in a, b, c over Real Field with 70 bits of precision

        The case of complex coefficients is not fully supported, yet, since
        the generator of a complex field in Sage is always called "I"::

            sage: singular.eval(\'ring r5 = (complex,15,j),(a,b,c),dp\')
            \'\'
            sage: R = singular(\'r5\').sage_global_ring(); R
            Multivariate Polynomial Ring in a, b, c over Complex Field with 54 bits of precision
            sage: R.base_ring()(\'k\')
            Traceback (most recent call last):
            ...
            ValueError: given string \'k\' is not a complex number
            sage: R.base_ring()(\'I\')
            1.00000000000000*I

        An example where the base ring is a polynomial ring over an extension of the rational field::

            sage: singular.eval(\'ring r7 = (0,a), (x,y), dp\')
            \'\'
            sage: singular.eval(\'minpoly = a2 + 1\')
            \'\'
            sage: singular(\'r7\').sage_global_ring()
            Multivariate Polynomial Ring in x, y over Number Field in a with defining polynomial a^2 + 1

        In our last example, the base ring is a quotient ring::

            sage: singular.eval(\'ring r6 = (9,a), (x,y,z),lp\')
            \'\'
            sage: Q = singular(\'std(ideal(x^2,x+y^2+z^3))\', type=\'qring\')
            sage: Q.sage_global_ring()
            Quotient of Multivariate Polynomial Ring in x, y, z over Finite Field in a of size 3^2 by the ideal (y^4 - y^2*z^3 + z^6, x + y^2 + z^3)

        AUTHOR:

        - Simon King (2011-06-06)
        '''
    def sage_poly(self, R=None, kcache=None):
        '''
        Return a Sage polynomial in the ring r matching the provided poly
        which is a singular polynomial.

        INPUT:

        - ``R`` -- (default: ``None``) an optional polynomial ring.
          If it is provided, then you have to make sure that it
          matches the current singular ring as, e.g., returned by
          ``singular.current_ring()``. By default, the output of
          :meth:`sage_global_ring` is used.

        - ``kcache`` -- (default: ``None``) an optional dictionary
          for faster finite field lookups, this is mainly useful for finite
          extension fields


        OUTPUT: MPolynomial

        EXAMPLES::

            sage: R = PolynomialRing(GF(2^8,\'a\'), \'x,y\')
            sage: f = R(\'a^20*x^2*y+a^10+x\')
            sage: f._singular_().sage_poly(R) == f
            True
            sage: R = PolynomialRing(GF(2^8,\'a\'), \'x\', implementation=\'singular\')
            sage: f = R(\'a^20*x^3+x^2+a^10\')
            sage: f._singular_().sage_poly(R) == f
            True

        ::

            sage: P.<x,y> = PolynomialRing(QQ, 2)
            sage: f = x*y**3 - 1/9 * x + 1; f
            x*y^3 - 1/9*x + 1
            sage: singular(f)
            x*y^3-1/9*x+1
            sage: P(singular(f))
            x*y^3 - 1/9*x + 1

        TESTS::

            sage: singular.eval(\'ring r = (3,z),(a,b,c),dp\')
            \'\'
            sage: singular.eval(\'minpoly = 1+z+z2+z3+z4\')
            \'\'
            sage: p = singular(\'z^4*a^3+z^2*a*b*c\')
            sage: p.sage_poly()
            (-z^3 - z^2 - z - 1)*a^3 + (z^2)*a*b*c
            sage: singular(\'z^4\')
            (-z3-z2-z-1)

        Test that :issue:`25297` is fixed::

            sage: R.<x,y> = QQ[]
            sage: SE.<xbar,ybar> = R.quotient(x^2 + y^2 - 1)
            sage: P = ideal(xbar,ybar)
            sage: P2 = P._singular_().sage()
            sage: P2.0.lift().parent()
            Multivariate Polynomial Ring in x, y over Rational Field

        Test that :issue:`29396` is fixed::

            sage: Rxz.<x,z> = RR[]
            sage: f = x**3 + x*z + 1
            sage: f.discriminant(x)
            -4.00000000000000*z^3 - 27.0000000000000
            sage: Rx.<x> = RR[]
            sage: Rx("x + 7.5")._singular_().sage_poly()
            x + 7.50000
            sage: Rx("x + 7.5")._singular_().sage_poly(Rx)
            x + 7.50000000000000

        AUTHORS:

        - Martin Albrecht (2006-05-18)
        - Simon King (2011-06-06): Deal with Singular\'s short polynomial representation,
          automatic construction of a polynomial ring, if it is not explicitly given.

        .. NOTE::

           For very simple polynomials
           ``eval(SingularElement.sage_polystring())`` is faster than
           SingularElement.sage_poly(R), maybe we should detect the
           crossover point (in dependence of the string length) and
           choose an appropriate conversion strategy
        '''
    def sage_matrix(self, R, sparse: bool = True):
        """
        Return Sage matrix for ``self``.

        INPUT:

        - ``R`` -- (default: ``None``) an optional ring, over which
          the resulting matrix is going to be defined.
          By default, the output of :meth:`sage_global_ring` is used.

        - ``sparse`` -- boolean (default: ``True``); whether the
          resulting matrix is sparse or not

        EXAMPLES::

            sage: R = singular.ring(0, '(x,y,z)', 'dp')
            sage: A = singular.matrix(2,2)
            sage: A.sage_matrix(ZZ)
            [0 0]
            [0 0]
            sage: A.sage_matrix(RDF)
            [0.0 0.0]
            [0.0 0.0]
        """
    def is_string(self):
        '''
        Tell whether this element is a string.

        EXAMPLES::

            sage: singular(\'"abc"\').is_string()
            True
            sage: singular(\'1\').is_string()
            False
        '''
    def set_ring(self) -> None:
        """
        Set the current ring in Singular to be ``self``.

        EXAMPLES::

            sage: R = singular.ring(7, '(a,b)', 'ds')
            sage: S = singular.ring('real', '(a,b)', 'lp')
            sage: singular.current_ring()
            polynomial ring, over a field, global ordering
            // coefficients: Float()...
            // number of vars : 2
            //        block   1 : ordering lp
            //                  : names    a b
            //        block   2 : ordering C
            sage: R.set_ring()
            sage: singular.current_ring()
            polynomial ring, over a field, local ordering
            // coefficients: ZZ/7...
            // number of vars : 2
            //        block   1 : ordering ds
            //                  : names    a b
            //        block   2 : ordering C
        """
    def sage_flattened_str_list(self):
        """
        EXAMPLES::

            sage: R=singular.ring(0,'(x,y)','dp')
            sage: RL = R.ringlist()
            sage: RL.sage_flattened_str_list()
            ['0', 'x', 'y', 'dp', '1,1', 'C', '0', '_[1]=0']
        """
    def sage_structured_str_list(self):
        """
        If ``self`` is a Singular list of lists of Singular elements, return
        corresponding Sage list of lists of strings.

        EXAMPLES::

            sage: R=singular.ring(0,'(x,y)','dp')
            sage: RL=R.ringlist()
            sage: RL
            [1]:
               0
            [2]:
               [1]:
                  x
               [2]:
                  y
            [3]:
               [1]:
                  [1]:
                     dp
                  [2]:
                     1,1
               [2]:
                  [1]:
                     C
                  [2]:
                     0
            [4]:
               _[1]=0
            sage: RL.sage_structured_str_list()
            ['0', ['x', 'y'], [['dp', '1,\\n1'], ['C', '0']], '0']
        """
    def type(self):
        """
        Return the internal type of this element.

        EXAMPLES::

            sage: R = PolynomialRing(GF(2^8,'a'),2,'x')
            sage: R._singular_().type()
            'ring'
            sage: fs = singular('x0^2','poly')
            sage: fs.type()
            'poly'
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: R = singular.ring(0, '(x,y,z)', 'dp')
            sage: A = singular.matrix(2,2)
            sage: list(iter(A))
            [[0], [0]]
            sage: A[1,1] = 1; A[1,2] = 2
            sage: A[2,1] = 3; A[2,2] = 4
            sage: list(iter(A))
            [[1,3], [2,4]]
        """
    def attrib(self, name, value=None):
        """
        Get and set attributes for ``self``.

        INPUT:

        - ``name`` -- string to choose the attribute

        - ``value`` -- boolean value or ``None`` for reading,
          (default: ``None``)

        VALUES: isSB - the standard basis property is set by all commands
        computing a standard basis like groebner, std, stdhilb etc.; used
        by lift, dim, degree, mult, hilb, vdim, kbase isHomog - the weight
        vector for homogeneous or quasihomogeneous ideals/modules isCI -
        complete intersection property isCM - Cohen-Macaulay property rank
        - set the rank of a module (see nrows) withSB - value of type
        ideal, resp. module, is std withHilb - value of type intvec is
        hilb(_,1) (see hilb) withRes - value of type list is a free
        resolution withDim - value of type int is the dimension (see dim)
        withMult - value of type int is the multiplicity (see mult)

        EXAMPLES::

            sage: P.<x,y,z> = PolynomialRing(QQ)
            sage: I = Ideal([z^2, y*z, y^2, x*z, x*y, x^2])
            sage: Ibar = I._singular_()
            sage: Ibar.attrib('isSB')
            0
            sage: singular.eval('vdim(%s)'%Ibar.name()) # sage7 name is random
            // ** sage7 is no standard basis
            4
            sage: Ibar.attrib('isSB',1)
            sage: singular.eval('vdim(%s)'%Ibar.name())
            '4'
        """

class SingularFunction(ExpectFunction): ...
class SingularFunctionElement(FunctionElement): ...

def is_SingularElement(x):
    """
    Return ``True`` if ``x`` is of type :class:`SingularElement`.

    This function is deprecated; use :func:`isinstance`
    (of :class:`sage.interfaces.abc.SingularElement`) instead.

    EXAMPLES::

        sage: from sage.interfaces.singular import is_SingularElement
        sage: is_SingularElement(singular(2))
        doctest:...: DeprecationWarning: the function is_SingularElement is deprecated; use isinstance(x, sage.interfaces.abc.SingularElement) instead
        See https://github.com/sagemath/sage/issues/34804 for details.
        True
        sage: is_SingularElement(2)
        False
    """
def get_docstring(name, prefix: bool = False, code: bool = False):
    '''
    Return the docstring for the function ``name``.

    INPUT:

    - ``name`` -- a Singular function name
    - ``prefix`` -- boolean (default: ``False``); whether or not to
      include the prefix stating that what follows is from the
      Singular documentation.
    - ``code`` -- boolean (default: ``False``); whether or not to
      format the result as a reStructuredText code block. This is
      intended to support the feature requested in :issue:`11268`.

    OUTPUT:

    A string describing the Singular function ``name``. A
    :class:`KeyError` is raised if the function was not found in the
    Singular documentation. If the "info" is not on the user\'s
    ``PATH``, an :class:`OSError` will be raised. If "info" was found
    but failed to execute, a :class:`subprocess.CalledProcessError`
    will be raised instead.

    EXAMPLES::

        sage: from sage.interfaces.singular import get_docstring
        sage: \'groebner\' in get_docstring(\'groebner\')  # needs_info
        True
        sage: \'standard.lib\' in get_docstring(\'groebner\')  # needs info
        True

    The ``prefix=True`` form is used in Sage\'s generated docstrings::

        sage: from sage.interfaces.singular import get_docstring
        sage: print(get_docstring("factorize", prefix=True))  # needs info
        The Singular documentation for "factorize" is given below.
        ...

    TESTS:

    Non-existent functions raise a :class:`KeyError`::

        sage: from sage.interfaces.singular import get_docstring
        sage: get_docstring("mysql_real_escape_string")  # needs info
        Traceback (most recent call last):
        ...
        KeyError: \'mysql_real_escape_string\'

    This is true also for nodes that exist in the documentation but
    are not function nodes::

        sage: from sage.interfaces.singular import get_docstring
        sage: get_docstring("Preface")  # needs info
        Traceback (most recent call last):
        ...
        KeyError: \'Preface\'

    If GNU Info is not installed, we politely decline to do anything::

        sage: from sage.interfaces.singular import get_docstring
        sage: from sage.features.info import Info
        sage: Info().hide()
        sage: get_docstring(\'groebner\')
        Traceback (most recent call last):
        ...
        OSError: GNU Info is not installed. Singular\'s documentation
        will not be available.
        sage: Info().unhide()
    '''

singular: Singular

def reduce_load_Singular():
    """
    EXAMPLES::

        sage: from sage.interfaces.singular import reduce_load_Singular
        sage: reduce_load_Singular()
        Singular
    """
def singular_console() -> None:
    """
    Spawn a new Singular command-line session.

    EXAMPLES::

        sage: singular_console() #not tested
                             SINGULAR                             /  Development
         A Computer Algebra System for Polynomial Computations   /   version 3-0-4
                                                               0<
             by: G.-M. Greuel, G. Pfister, H. Schoenemann        \\   Nov 2007
        FB Mathematik der Universitaet, D-67653 Kaiserslautern    \\\n    """
def singular_version():
    '''
    Return the version of Singular being used.

    EXAMPLES::

        sage: singular.version()
        "Singular ... version 4...
    '''

class SingularGBLogPrettyPrinter:
    """
    A device which prints Singular Groebner basis computation logs
    more verbatim.
    """
    rng_chng: Incomplete
    new_elem: Incomplete
    red_zero: Incomplete
    red_post: Incomplete
    cri_hilb: Incomplete
    hig_corn: Incomplete
    num_crit: Incomplete
    red_num: Incomplete
    deg_lead: Incomplete
    red_para: Incomplete
    red_betr: Incomplete
    non_mini: Incomplete
    crt_lne1: Incomplete
    crt_lne2: Incomplete
    pat_sync: Incomplete
    global_pattern: Incomplete
    verbosity: Incomplete
    curr_deg: int
    max_deg: int
    nf: int
    prod: int
    ext_prod: int
    chain: int
    storage: str
    sync: Incomplete
    def __init__(self, verbosity: int = 1) -> None:
        '''
        Construct a new Singular Groebner Basis log pretty printer.

        INPUT:

        - ``verbosity`` -- how much information should be printed
          (between 0 and 3)

        EXAMPLES::

            sage: from sage.interfaces.singular import SingularGBLogPrettyPrinter
            sage: s0 = SingularGBLogPrettyPrinter(verbosity=0)
            sage: s1 = SingularGBLogPrettyPrinter(verbosity=1)
            sage: s0.write("[1:2]12")

            sage: s1.write("[1:2]12")
            Leading term degree: 12.
        '''
    def write(self, s) -> None:
        '''
        EXAMPLES::

            sage: from sage.interfaces.singular import SingularGBLogPrettyPrinter
            sage: s3 = SingularGBLogPrettyPrinter(verbosity=3)
            sage: s3.write("(S:1337)")
            Performing complete reduction of 1337 elements.
            sage: s3.write("M[389,12]")
            Parallel reduction of 389 elements with 12 nonzero output elements.
        '''
    def flush(self) -> None:
        """
        EXAMPLES::

            sage: from sage.interfaces.singular import SingularGBLogPrettyPrinter
            sage: s3 = SingularGBLogPrettyPrinter(verbosity=3)
            sage: s3.flush()
        """

class SingularGBDefaultContext:
    """
    Within this context all Singular Groebner basis calculations are
    reduced automatically.

    AUTHORS:

    - Martin Albrecht
    - Simon King
    """
    singular: Incomplete
    def __init__(self, singular=None) -> None:
        """
        Within this context all Singular Groebner basis calculations
        are reduced automatically.

        INPUT:

        - ``singular`` -- Singular instance (default: default instance)

        EXAMPLES::

            sage: from sage.interfaces.singular import SingularGBDefaultContext
            sage: P.<a,b,c> = PolynomialRing(QQ,3, order='lex')
            sage: I = sage.rings.ideal.Katsura(P,3)
            sage: singular.option('noredTail')
            sage: singular.option('noredThrough')
            sage: Is = I._singular_()
            sage: gb = Is.groebner()
            sage: gb
            84*c^4-40*c^3+c^2+c,
            7*b+210*c^3-79*c^2+3*c,
            a+2*b+2*c-1

        ::

            sage: with SingularGBDefaultContext(): rgb = Is.groebner()
            sage: rgb
            84*c^4-40*c^3+c^2+c,
            7*b+210*c^3-79*c^2+3*c,
            7*a-420*c^3+158*c^2+8*c-7

        Note that both bases are Groebner bases because they have
        pairwise prime leading monomials but that the monic version of
        the last element in ``rgb`` is smaller than the last element
        of ``gb`` with respect to the lexicographical term ordering. ::

            sage: (7*a-420*c^3+158*c^2+8*c-7)/7 < (a+2*b+2*c-1)
            True

        .. NOTE::

           This context is used automatically internally whenever a
           Groebner basis is computed so the user does not need to use
           it manually.
        """
    bck_degBound: Incomplete
    bck_multBound: Incomplete
    o: Incomplete
    def __enter__(self) -> None:
        """
        EXAMPLES::

            sage: from sage.interfaces.singular import SingularGBDefaultContext
            sage: P.<a,b,c> = PolynomialRing(QQ,3, order='lex')
            sage: I = sage.rings.ideal.Katsura(P,3)
            sage: singular.option('noredTail')
            sage: singular.option('noredThrough')
            sage: Is = I._singular_()
            sage: with SingularGBDefaultContext(): rgb = Is.groebner()
            sage: rgb
            84*c^4-40*c^3+c^2+c,
            7*b+210*c^3-79*c^2+3*c,
            7*a-420*c^3+158*c^2+8*c-7
        """
    def __exit__(self, typ: type[BaseException] | None, value: BaseException | None, tb: types.TracebackType | None) -> None:
        """
        EXAMPLES::

            sage: from sage.interfaces.singular import SingularGBDefaultContext
            sage: P.<a,b,c> = PolynomialRing(QQ,3, order='lex')
            sage: I = sage.rings.ideal.Katsura(P,3)
            sage: singular.option('noredTail')
            sage: singular.option('noredThrough')
            sage: Is = I._singular_()
            sage: with SingularGBDefaultContext(): rgb = Is.groebner()
            sage: rgb
            84*c^4-40*c^3+c^2+c,
            7*b+210*c^3-79*c^2+3*c,
            7*a-420*c^3+158*c^2+8*c-7
        """

def singular_gb_standard_options(func):
    '''
    Decorator to force a reduced Singular groebner basis.

    TESTS::

        sage: P.<a,b,c,d,e> = PolynomialRing(GF(127))
        sage: J = sage.rings.ideal.Cyclic(P).homogenize()
        sage: from sage.misc.sageinspect import sage_getsource
        sage: "basis" in sage_getsource(J.interreduced_basis) #indirect doctest
        True

    The following tests against a bug that was fixed in :issue:`11298`::

        sage: from sage.misc.sageinspect import sage_getsourcelines, sage_getargspec
        sage: P.<x,y> = QQ[]
        sage: I = P*[x,y]
        sage: sage_getargspec(I.interreduced_basis)
        FullArgSpec(args=[\'self\'], varargs=None, varkw=None, defaults=None,
                    kwonlyargs=[], kwonlydefaults=None, annotations={})
        sage: sage_getsourcelines(I.interreduced_basis)
        ([\'    @handle_AA_and_QQbar\\n\',
          \'    @singular_gb_standard_options\\n\',
          \'    @libsingular_gb_standard_options\\n\',
          \'    def interreduced_basis(self):\\n\', \'
          ...
          \'        return self.basis.reduced()\\n\'], ...)

    .. NOTE::

       This decorator is used automatically internally so the user
       does not need to use it manually.
    '''
