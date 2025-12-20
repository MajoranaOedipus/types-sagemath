r"""
Interface to the c++ giac library.

Giac is a general purpose Computer algebra system by Bernard Parisse
released under GPLv3.

- http://www-fourier.ujf-grenoble.fr/~parisse/giac.html
- It is build on C and C++ libraries: NTL (arithmetic), GSL (numerics), GMP
  (big integers), MPFR (bigfloats)
- It  provides fast  algorithms  for multivariate polynomial operations
  (product, GCD, factorisation) and
- symbolic  computations: solver, simplifications, limits/series, integration,
  summation...
- Linear Algebra with numerical or symbolic coefficients.

AUTHORS:

- Frederic Han (2013-09-23): initial version
- Vincent Delecroix (2020-09-02): move inside Sage source code

EXAMPLES:

The class Pygen is the main tool to interact from python/sage with the c++
library giac via cython.  The initialisation of a Pygen just create an object
in giac, but the mathematical computation  is not done. This class is mainly
for cython users.  Here A is a Pygen element, and it is ready for any giac
function.::

    >>> from sagemath_giac.giac import *
    >>> A = Pygen('2+2')
    >>> A
    2+2
    >>> A.eval()
    4

In general, you may prefer to directly create a Pygen and execute the
evaluation in giac. This is exactly the meaning of the :func:`libgiac`
function.::

    >>> a = libgiac('2+2')
    >>> a
    4
    >>> isinstance(a, Pygen)
    True

Most common usage of this package in sage will be with the libgiac() function.
This function is just the composition of the Pygen initialisation and the
evaluation of this object in giac.::

    >>> x,y,z = libgiac('x,y,z')  # add some giac objects
    >>> f = (x+y*3)/(x+z+1)**2 - (x+z+1)**2 / (x+y*3)
    >>> f.factor()
    (3*y-x^2-2*x*z-x-z^2-2*z-1)*(3*y+x^2+2*x*z+3*x+z^2+2*z+1)/((x+z+1)^2*(3*y+x))
    >>> f.normal()
    (-x^4-4*x^3*z-4*x^3-6*x^2*z^2-12*x^2*z-5*x^2+6*x*y-4*x*z^3-12*x*z^2-12*x*z-4*x+9*y^2-z^4-4*z^3-6*z^2-4*z-1)/(x^3+3*x^2*y+2*x^2*z+2*x^2+6*x*y*z+6*x*y+x*z^2+2*x*z+x+3*y*z^2+6*y*z+3*y)

Some settings of giac are available via the ``giacsettings``
element. (Ex: maximal number of threads in computations, allowing
probabilistic algorithms or not...::

    >>> from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing
    >>> from sage.rings.rational_field import QQ
    >>> from sage.rings.ideal import Katsura as KatsuraIdeal
    >>> R = PolynomialRing(QQ,8,'x')
    >>> I = KatsuraIdeal(R,8)
    >>> giacsettings.proba_epsilon = 1e-15  # faster, but can fail
    >>> Igiac = libgiac(I.gens());
    >>> Bgiac = Igiac.gbasis([R.gens()],'revlex')
    >>> len(Bgiac)
    74
    >>> giacsettings.proba_epsilon = 0  # slower, but more reliable
    >>> Igiac = libgiac(I.gens())
    >>> Bgiac = Igiac.gbasis([R.gens()],'revlex')
    >>> len(Bgiac)
    74
    >>> giacsettings.proba_epsilon = 1e-15

  ::

    >>> x = libgiac('x')
    >>> f = libgiac(1) / (libgiac.sin(x*5)+2)
    >>> f.int()
    2/5/sqrt(3)*(atan((-sqrt(3)*sin(5*x)+cos(5*x)+2*sin(5*x)+1)/(sqrt(3)*cos(5*x)+sqrt(3)-2*cos(5*x)+sin(5*x)+2))+5*x/2)
    >>> f.series(x,0,3)
    1/2-5/4*x+25/8*x^2-125/48*x^3+x^4*order_size(x)
    >>> (libgiac.sqrt(5)+libgiac.pi).approx(100)
    5.377660631089582934871817052010779119637787758986631545245841837718337331924013898042449233720899343

TESTS::

    >>> from sagemath_giac.giac import libgiac
    >>> libgiac(3**100)
    515377520732011331036461129765621272702107522001
    >>> libgiac(-3**100)
    -515377520732011331036461129765621272702107522001
    >>> libgiac(-11**1000)
    -2469932918005826334124088385085221477709733385238396234869182951830739390375433175367866116456946191973803561189036523363533798726571008961243792655536655282201820357872673322901148243453211756020067624545609411212063417307681204817377763465511222635167942816318177424600927358163388910854695041070577642045540560963004207926938348086979035423732739933235077042750354729095729602516751896320598857608367865475244863114521391548985943858154775884418927768284663678512441565517194156946312753546771163991252528017732162399536497445066348868438762510366191040118080751580689254476068034620047646422315123643119627205531371694188794408120267120500325775293645416335230014278578281272863450085145349124727476223298887655183167465713337723258182649072572861625150703747030550736347589416285606367521524529665763903537989935510874657420361426804068643262800901916285076966174176854351055183740078763891951775452021781225066361670593917001215032839838911476044840388663443684517735022039957481918726697789827894303408292584258328090724141496484460001

Ensure that signed infinities get converted correctly::

    >>> from sage.rings.infinity import Infinity
    >>> libgiac(+Infinity)
    +infinity
    >>> libgiac(-Infinity)
    -infinity

.. SEEALSO::

    ``libgiac``, ``giacsettings``, ``Pygen``,``loadgiacgen``


GETTING HELP:

- To obtain some help on a giac keyword use the help() method. In sage the
  htmlhelp() method for Pygen element is disabled. Just use the ? or .help()
  method.

- You can find full html documentation about the **giac** functions  at:

      - https://www-fourier.ujf-grenoble.fr/~parisse/giac/doc/en/cascmd_en/

      - https://www-fourier.ujf-grenoble.fr/~parisse/giac/doc/fr/cascmd_fr/

      - https://www-fourier.ujf-grenoble.fr/~parisse/giac/doc/el/cascmd_el/

"""

from cysignals.signals import *
from gmpy2 import import_gmpy2, mpz_set
from sys import maxsize as Pymaxint, version_info as Pyversioninfo
import os
import math

# sage includes
from sage.ext.stdsage import PY_NEW
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing
from sage.rings.integer import Integer
from sage.rings.infinity import AnInfinity
from sage.rings.rational import Rational
from sage.structure.element import Matrix

from sage.symbolic.expression import symbol_table
from sage.calculus.calculus import symbolic_expression_from_string, SR_parser_giac
from sage.symbolic.ring import SR
from sage.symbolic.expression import Expression
from sage.symbolic.expression_conversions import InterfaceInit
from sage.interfaces.giac import giac

import_gmpy2()  # TODO: change to actuall import

class GiacInstance:
    """
    This class is used to create the giac interpreter object.

    EXAMPLES::

        >>> from sagemath_giac.giac import libgiac, GiacInstance
        >>> isinstance(libgiac, GiacInstance)
        True
        >>> libgiac.solve('2*exp(x)<(exp(x*2)-1),x')
        list[x>(ln(sqrt(2)+1))]

    """

    def __init__(self):
        ...

    def __call__(self, s):
        """
    This function evaluate a python/sage object with the giac
    library. It creates in python/sage a Pygen element and evaluate it
    with giac:

    EXAMPLES::

        >>> from sagemath_giac.giac import libgiac
        >>> x,y = libgiac('x,y')
        >>> (x + y*2).cos().texpand()
        cos(x)*(2*cos(y)^2-1)-sin(x)*2*cos(y)*sin(y)

    Coercion, Pygen and internal giac variables: The most useful
    objects will be the Python object of type Pygen::

        >>> x,y,z = libgiac('x,y,z')
        >>> f = sum([x[i] for i in range(5)], libgiac(0))**15/(y+z)
        >>> f.coeff(x[0],12)
        (455*(x[1])^3+1365*(x[1])^2*x[2]+1365*(x[1])^2*x[3]+1365*(x[1])^2*x[4]+1365*x[1]*(x[2])^2+2730*x[1]*x[2]*x[3]+2730*x[1]*x[2]*x[4]+1365*x[1]*(x[3])^2+2730*x[1]*x[3]*x[4]+1365*x[1]*(x[4])^2+455*(x[2])^3+1365*(x[2])^2*x[3]+1365*(x[2])^2*x[4]+1365*x[2]*(x[3])^2+2730*x[2]*x[3]*x[4]+1365*x[2]*(x[4])^2+455*(x[3])^3+1365*(x[3])^2*x[4]+1365*x[3]*(x[4])^2+455*(x[4])^3)/(y+z)

    Warning: The complex number sqrt(-1) is available in SageMath as
    ``I``, but it may appears as ``i``::

        >>> from sage.rings.imaginary_unit import I
        >>> libgiac((libgiac.sqrt(3)*I + 1)**3).normal()
        -8
        >>> libgiac(1+I)
        1+i

    Python integers and reals can be directly converted to giac.::

        >>> libgiac(2**1024).nextprime()
        179769313486231590772930519078902473361797697894230657273430081157732675805500963132708477322407536021120113879871393357658789768814416622492847430639474124377767893424865485276302219601246094119453082952085005768838150682342462881473913110540827237163350510684586298239947245938479716304835356329624224137859
        >>> libgiac(1.234567).erf().approx(10)
        0.9191788641

    The Python object ``y`` defined above is of type Pygen. It is not
    an internal giac variable. (Most of the time you won't need to use
    internal giac variables)::

        >>> libgiac('y:=1'); y
        1
        y
        >>> libgiac.purge('y')
        1
        >>> libgiac('y')
        y

    There are some natural coercion to Pygen elements::

        >>> libgiac.pi > 3.14
        True
        >>> libgiac.pi > 3.15
        False
        >>> libgiac(3) == 3
        True

    Linear Algebra. In Giac/Xcas vectors are just lists and matrices
    are lists of list::

        >>> x,y = libgiac('x,y')
        >>> A = libgiac([[1,2],[3,4]])  # giac matrix
        >>> v = libgiac([x,y]); v  # giac vector
        [x,y]
        >>> A*v  # matrix-vector product
        [x+2*y,3*x+4*y]
        >>> v*v  # dot product
        x*x+y*y

    Remark that ``w=giac([[x],[y]])`` is a matrix of 1 column and 2
    rows. It is not a vector so w*w doesn't make sense.::

        >>> w = libgiac([[x],[y]])
        >>> w.transpose()*w
        matrix[[x*x+y*y]]

    In sage, changing an entry doesn't create a new matrix (see also
    the doc of ``Pygen.__setitem__``)::

        >>> B1 = A
        >>> B1[0,0]=43; B1 # in place affectation changes both B1 and A
        [[43,2],[3,4]]
        >>> A
        [[43,2],[3,4]]
        >>> A[0][0]=A[0][0]+1; A  # similar as A[0,0]=A[0,0]+1
        [[44,2],[3,4]]
        >>> A.pcar(x)  # compute the characteristic polynomial of A
        x^2-48*x+170
        >>> B2=A.copy() # use copy to create another object
        >>> B2[0,0]=55; B2  # here A is not modified
        [[55,2],[3,4]]
        >>> A
        [[44,2],[3,4]]

    Sparse Matrices are available via the table function::

        >>> A = libgiac.table(()); A  # create an empty giac table
        table(
        )
        >>> A[2,3] = 33; A[0,2] = '2/7' # set nonzero entries of the sparse matrix
        >>> A*A  # basic matrix operation are supported with sparse matrices
        table(
        (0,3) = 66/7
        )
        >>> D = libgiac.diag([22,3,'1/7']); D  # some diagonal matrix
        [[22,0,0],[0,3,0],[0,0,1/7]]
        >>> libgiac.table(D)    # to create a sparse matrix from an ordinary one
        table(
        (0,0) = 22,
        (1,1) = 3,
        (2,2) = 1/7
        )

    But many matrix functions apply only with ordinary matrices so
    need conversions::

        >>> B1 = A.matrix(); B1 # convert the sparse matrix to a matrix, but the size is minimal
        [[0,0,2/7,0],[0,0,0,0],[0,0,0,33]]
        >>> B2 = B1.redim(4,4) # so we may need to resize B1
        >>> B2.pmin(x)
        x^3

    Lists of Pygen and Giac lists. Here l1 is a giac list and l2 is a
    python list of Pygen type objects::

        >>> l1 = libgiac(range(10))
        >>> l2 = [libgiac(1)/(i**2+1) for i in l1]
        >>> sum(l2, libgiac(0))
        33054527/16762850

    So l1+l1 is done in giac and means a vector addition. But l2+l2 is
    done in Python so it is the list concatenation::

        >>> l1+l1
        [0,2,4,6,8,10,12,14,16,18]
        >>> l2+l2
        [1, 1/2, 1/5, 1/10, 1/17, 1/26, 1/37, 1/50, 1/65, 1/82, 1, 1/2, 1/5, 1/10, 1/17, 1/26, 1/37, 1/50, 1/65, 1/82]

    Here V is not a Pygen element. We need to push it to giac to use a
    giac method like dim, or we need to use an imported function::

        >>> V = [ [x[i]**j for i in range(8)] for j in range(8)]
        >>> libgiac(V).dim()
        [8,8]
        >>> libgiac.det_minor(V).factor()
        (x[6]-(x[7]))*(x[5]-(x[7]))*(x[5]-(x[6]))*(x[4]-(x[7]))*(x[4]-(x[6]))*(x[4]-(x[5]))*(x[3]-(x[7]))*(x[3]-(x[6]))*(x[3]-(x[5]))*(x[3]-(x[4]))*(x[2]-(x[7]))*(x[2]-(x[6]))*(x[2]-(x[5]))*(x[2]-(x[4]))*(x[2]-(x[3]))*(x[1]-(x[7]))*(x[1]-(x[6]))*(x[1]-(x[5]))*(x[1]-(x[4]))*(x[1]-(x[3]))*(x[1]-(x[2]))*(x[0]-(x[7]))*(x[0]-(x[6]))*(x[0]-(x[5]))*(x[0]-(x[4]))*(x[0]-(x[3]))*(x[0]-(x[2]))*(x[0]-(x[1]))

    Modular objects with ``%``::

        >>> V = libgiac.ranm(5,6) % 2
        >>> V.ker().rowdim()+V.rank()
        6
        >>> a = libgiac(7)%3
        >>> a
        1 % 3
        >>> a % 0
        1
        >>> 7 % 3
        1

    Do not confuse with the python integers::

        >>> type(7 % 3) == type(a)
        False
        >>> type(a) == type(7 % 3)
        False

    Syntax with reserved or unknown Python/sage symbols. In general
    equations needs symbols such as ``=``, ``<`` or ``>`` that have
    another meaning in Python or Sage. So those objects must be
    quoted::

        >>> x = libgiac('x')
        >>> (libgiac.sin(x*3)*2 + 1).solve(x).simplify()
        list[-pi/18,7*pi/18]

        >>> libgiac.solve('x^3-x>x',x)
        list[((x>(-sqrt(2))) and (x<0)),x>(sqrt(2))]

    You can also add some hypothesis to a giac symbol::

        >>> libgiac.assume('x>-pi && x<pi')
        x
        >>> libgiac.solve('sin(3*x)>2*sin(x)',x)
        list[((x>(-5*pi/6)) and (x<(-pi/6))),((x>0) and (x<(pi/6))),((x>(5*pi/6)) and (x<pi))]

    To remove those hypothesis use the giac function ``purge``::

        >>> libgiac.purge('x')
        assume[[],[line[-pi,pi]],[-pi,pi]]
        >>> libgiac.solve('x>0')
        list[x>0]

    Same problems with the ``..``::

        >>> x = libgiac('x')
        >>> f = libgiac(1)/(libgiac.cos(x*4)+5)
        >>> f.int()
        1/2/(2*sqrt(6))*(atan((-sqrt(6)*sin(4*x)+2*sin(4*x))/(sqrt(6)*cos(4*x)+sqrt(6)-2*cos(4*x)+2))+4*x/2)
        >>> libgiac.fMax(f,'x=-0..pi').simplify()
        pi/4,3*pi/4
        >>> libgiac.sum(libgiac(1)/(x**2+1),'x=0..infinity').simplify()
        (pi*exp(pi)^2+pi+exp(pi)^2-1)/(2*exp(pi)^2-2)

    From giac to sage. One can convert a Pygen element to sage with
    the ``sage`` method::

        >>> L = libgiac('[1,sqrt(5),[1.3,x]]')
        >>> L.sage()       # All entries are converted recursively
        [1, sqrt(5), [1.30000000000000, x]]

        >>> from sage.symbolic.ring import SR
        >>> from sage.matrix.constructor import matrix
        >>> n = SR.symbol('n')
        >>> A = matrix([[1,2],[-1,1]])
        >>> B = libgiac(A).matpow(n)    # We compute the symbolic power on A via libgiac
        >>> C = matrix(SR,B); C         # We convert B to sage
        [                     1/2*(I*sqrt(2) + 1)^n + 1/2*(-I*sqrt(2) + 1)^n -1/2*I*sqrt(2)*(I*sqrt(2) + 1)^n + 1/2*I*sqrt(2)*(-I*sqrt(2) + 1)^n]
        [ 1/4*I*sqrt(2)*(I*sqrt(2) + 1)^n - 1/4*I*sqrt(2)*(-I*sqrt(2) + 1)^n                      1/2*(I*sqrt(2) + 1)^n + 1/2*(-I*sqrt(2) + 1)^n]
        >>> (C.subs(n=3)-A**3).expand()
        [0 0]
        [0 0]


   **MEMENTO of usual GIAC functions**:

   - *Expand with simplification*

         * ``ratnormal``, ``normal``, ``simplify``   (from the fastest to the most sophisticated)

         *  NB: ``expand`` function doesn't regroup nor cancel terms, so it could be slow. (pedagogical purpose only?)

   - *Factor/Regroup*

         * ``factor``, ``factors``, ``regroup``, ``cfactor``, ``ifactor``

   - *Misc*

         * ``unapply``, ``op``, ``subst``

   - *Polynomials/Fractions*

         * ``coeff``,  ``gbasis``, ``greduce``, ``lcoeff``, ``pcoeff``, ``canonical_form``,

         * ``proot``,  ``poly2symb``,  ``symb2poly``, ``posubLMQ``, ``poslbdLMQ``, ``VAS``, ``tcoeff``,  ``valuation``

         * ``gcd``, ``egcd``, ``lcm``, ``quo``, ``rem``, ``quorem``, ``abcuv``, ``chinrem``,

         * ``peval``, ``horner``, ``lagrange``, ``ptayl``, ``spline``,  ``sturm``,  ``sturmab``

         * ``partfrac``, ``cpartfrac``

   - *Memory/Variables*

         * ``assume``, ``about``, ``purge``, ``ans``

   - *Calculus/Exact*

         * ``linsolve``,  ``solve``,  ``csolve``,  ``desolve``,  ``seqsolve``, ``reverse_rsolve``, ``matpow``

         * ``limit``, ``series``, ``sum``, ``diff``, ``fMax``, ``fMin``,

         * ``integrate``, ``subst``, ``ibpdv``, ``ibpu``, ``preval``

   - *Calculus/Exp, Log, powers*

         * ``exp2pow``, ``hyp2exp``, ``expexpand``, ``lin``, ``lncollect``, ``lnexpand``, ``powexpand``, ``pow2exp``

   - *Trigo*

         * ``trigexpand``, ``tsimplify``, ``tlin``, ``tcollect``,

         * ``halftan``, ``cos2sintan``, ``sin2costan``, ``tan2sincos``, ``tan2cossin2``, ``tan2sincos2``, ``trigcos``, ``trigsin``, ``trigtan``, ``shift_phase``

         * ``exp2trig``, ``trig2exp``

         * ``atrig2ln``, ``acos2asin``, ``acos2atan``, ``asin2acos``, ``asin2atan``, ``atan2acos``, ``atan2asin``

   - *Linear Algebra*

         * ``identity``, ``matrix``, ``makemat``, ``syst2mat``, ``matpow``, ``table``, ``redim``

         * ``det``,  ``det_minor``, ``rank``, ``ker``, ``image``, ``rref``, ``simplex_reduce``,

         * ``egv``, ``egvl``,  ``eigenvalues``, ``pcar``, ``pcar_hessenberg``, ``pmin``,

         * ``jordan``, ``adjoint_matrix``, ``companion``, ``hessenberg``, ``transpose``,

         * ``cholesky``, ``lll``,  ``lu``, ``qr``, ``svd``, ``a2q``, ``gauss``, ``gramschmidt``,
           ``q2a``, ``isom``, ``mkisom``


   - *Finite Fields*

         * ``%``, ``% 0``, ``mod``, ``GF``, ``powmod``


   - *Integers*

         * ``gcd``, ``iabcuv``, ``ichinrem``, ``idivis``, ``iegcd``,

         * ``ifactor``, ``ifactors``, ``iquo``, ``iquorem``, ``irem``,

         * ``is_prime, is_pseudoprime``, ``lcm``, ``mod``, ``nextprime``, ``pa2b2``, ``prevprime``,
           ``smod``, ``euler``, ``fracmod``

   - *List*

         * ``append``, ``accumulate_head_tail``, ``concat``, ``head``, ``makelist``, ``member``, ``mid``, ``revlist``, ``rotate``, ``shift``, ``size``, ``sizes``, ``sort``, ``suppress``, ``tail``

   - *Set*

         * ``intersect``, ``minus``, ``union``, ``is_element``, ``is_included``
    """
        ...

    def eval(self, code, strip=True, **kwds) -> Pygen:

        if strip:
            code = code.replace("\n","").strip()
        return self(code)

class Pygen:
    pass    #TODO: https://github.com/sagemath/sagemath-giac/blob/main/src/sagemath_giac/giac.pyx

libgiac: GiacInstance