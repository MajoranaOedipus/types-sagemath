import _cython_3_2_1
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.rings.integer import Integer as Integer
from typing import Any, overload

FS_ENCODING: str
get_precision: _cython_3_2_1.cython_function_or_method
initprimes: _cython_3_2_1.cython_function_or_method
parse_point_list: _cython_3_2_1.cython_function_or_method
set_precision: _cython_3_2_1.cython_function_or_method

class _Curvedata:
    """_Curvedata(a1, a2, a3, a4, a6, min_on_init=0)"""
    def __init__(self, a1, a2, a3, a4, a6, min_on_init=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 253)

                Constructor for Curvedata class.

                INPUT:

                - ``a1``, ``a2``, ``a3``, ``a4``, ``a6`` -- integer coefficients of a
                  Weierstrass equation (must be nonsingular)

                - ``min_on_init`` -- integer (default: 0); flag controlling whether
                  the constructed curve is replaced by a global minimal model.
                  If nonzero then this minimisation does take place.

                EXAMPLES::

                    sage: from sage.libs.eclib.mwrank import _Curvedata
                    sage: _Curvedata(1,2,3,4,5)
                    [1,2,3,4,5]
                    b2 = 9       b4 = 11         b6 = 29         b8 = 35
                    c4 = -183           c6 = -3429
                    disc = -10351       (# real components = 1)
                    #torsion not yet computed

                A non-minimal example::

                    sage: _Curvedata(0,0,0,0,64)
                    [0,0,0,0,64]
                    b2 = 0       b4 = 0  b6 = 256        b8 = 0
                    c4 = 0              c6 = -55296
                    disc = -1769472     (# real components = 1)
                    #torsion not yet computed

                    sage: _Curvedata(0,0,0,0,64,min_on_init=1)
                    [0,0,0,0,1] (reduced minimal model)
                    b2 = 0       b4 = 0  b6 = 4  b8 = 0
                    c4 = 0              c6 = -864
                    disc = -432 (# real components = 1)
                    #torsion not yet computed
        """
    @overload
    def conductor(self) -> Any:
        """_Curvedata.conductor(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 442)

        The conductor of this elliptic curve.

        OUTPUT:

        (Integer) The conductor.

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: E = _Curvedata(1,2,3,4,5)
            sage: E.discriminant()
            -10351
            sage: E = _Curvedata(100,200,300,400,500)
            sage: E.conductor()
            126958110400"""
    @overload
    def conductor(self) -> Any:
        """_Curvedata.conductor(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 442)

        The conductor of this elliptic curve.

        OUTPUT:

        (Integer) The conductor.

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: E = _Curvedata(1,2,3,4,5)
            sage: E.discriminant()
            -10351
            sage: E = _Curvedata(100,200,300,400,500)
            sage: E.conductor()
            126958110400"""
    def cps_bound(self) -> Any:
        """_Curvedata.cps_bound(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 358)

        The Cremona-Prickett-Siksek height bound for this elliptic curve.

        OUTPUT:

        (float) A nonnegative real number `B` such that for every
        rational point on this elliptic curve `E`, `h(P)\\le\\hat{h}(P)
        + B`, where `h(P)` is the naive height and `\\hat{h}(P)` the
        canonical height.

        .. NOTE::

            Since ``eclib`` can compute this to arbitrary precision, we
            could return a Sage real, but this is only a bound and in
            the contexts in which it is used extra precision is irrelevant.

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: E = _Curvedata(1,2,3,4,5)
            sage: E.cps_bound()
            0.11912451909250982...

        Note that this is a better bound than Silverman's in this case::

            sage: E.silverman_bound()
            6.52226179519101..."""
    @overload
    def discriminant(self) -> Any:
        """_Curvedata.discriminant(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 419)

        The discriminant of this elliptic curve.

        OUTPUT:

        (Integer) The discriminant.

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: E = _Curvedata(1,2,3,4,5)
            sage: E.discriminant()
            -10351
            sage: E = _Curvedata(100,200,300,400,500)
            sage: E.discriminant()
            -1269581104000000
            sage: ZZ(E.discriminant())
            -1269581104000000"""
    @overload
    def discriminant(self) -> Any:
        """_Curvedata.discriminant(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 419)

        The discriminant of this elliptic curve.

        OUTPUT:

        (Integer) The discriminant.

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: E = _Curvedata(1,2,3,4,5)
            sage: E.discriminant()
            -10351
            sage: E = _Curvedata(100,200,300,400,500)
            sage: E.discriminant()
            -1269581104000000
            sage: ZZ(E.discriminant())
            -1269581104000000"""
    @overload
    def discriminant(self) -> Any:
        """_Curvedata.discriminant(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 419)

        The discriminant of this elliptic curve.

        OUTPUT:

        (Integer) The discriminant.

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: E = _Curvedata(1,2,3,4,5)
            sage: E.discriminant()
            -10351
            sage: E = _Curvedata(100,200,300,400,500)
            sage: E.discriminant()
            -1269581104000000
            sage: ZZ(E.discriminant())
            -1269581104000000"""
    @overload
    def discriminant(self) -> Any:
        """_Curvedata.discriminant(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 419)

        The discriminant of this elliptic curve.

        OUTPUT:

        (Integer) The discriminant.

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: E = _Curvedata(1,2,3,4,5)
            sage: E.discriminant()
            -10351
            sage: E = _Curvedata(100,200,300,400,500)
            sage: E.discriminant()
            -1269581104000000
            sage: ZZ(E.discriminant())
            -1269581104000000"""
    def height_constant(self) -> Any:
        """_Curvedata.height_constant(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 392)

        A height bound for this elliptic curve.

        OUTPUT:

        (float) A nonnegative real number `B` such that for every
        rational point on this elliptic curve `E`, `h(P)\\le\\hat{h}(P)
        + B`, where `h(P)` is the naive height and `\\hat{h}(P)` the
        canonical height.  This is the minimum of the Silverman and
        Cremona_Prickett-Siksek height bounds.

        .. NOTE::

            Since ``eclib`` can compute this to arbitrary precision, we
            could return a Sage real, but this is only a bound and in
            the contexts in which it is used extra precision is irrelevant.

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: E = _Curvedata(1,2,3,4,5)
            sage: E.height_constant()
            0.119124519092509..."""
    @overload
    def isogeny_class(self, verbose=...) -> Any:
        """_Curvedata.isogeny_class(self, verbose=False)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 463)

        The isogeny class of this elliptic curve.

        OUTPUT:

        (tuple) A tuple consisting of (1) a list of the curves in the
        isogeny class, each as a list of its Weierstrass coefficients;
        (2) a matrix of the degrees of the isogenies between the
        curves in the class (prime degrees only).

        .. warning::

           The list may not be complete, if the precision is too low.
           Use ``mwrank_set_precision()`` to increase the precision.

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: E = _Curvedata(1,0,1,4,-6)
            sage: E.conductor()
            14
            sage: E.isogeny_class()
            ([[1, 0, 1, 4, -6], [1, 0, 1, -36, -70], [1, 0, 1, -1, 0], [1, 0, 1, -171, -874], [1, 0, 1, -11, 12], [1, 0, 1, -2731, -55146]], [[0, 2, 3, 3, 0, 0], [2, 0, 0, 0, 3, 3], [3, 0, 0, 0, 2, 0], [3, 0, 0, 0, 0, 2], [0, 3, 2, 0, 0, 0], [0, 3, 0, 2, 0, 0]])"""
    @overload
    def isogeny_class(self) -> Any:
        """_Curvedata.isogeny_class(self, verbose=False)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 463)

        The isogeny class of this elliptic curve.

        OUTPUT:

        (tuple) A tuple consisting of (1) a list of the curves in the
        isogeny class, each as a list of its Weierstrass coefficients;
        (2) a matrix of the degrees of the isogenies between the
        curves in the class (prime degrees only).

        .. warning::

           The list may not be complete, if the precision is too low.
           Use ``mwrank_set_precision()`` to increase the precision.

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: E = _Curvedata(1,0,1,4,-6)
            sage: E.conductor()
            14
            sage: E.isogeny_class()
            ([[1, 0, 1, 4, -6], [1, 0, 1, -36, -70], [1, 0, 1, -1, 0], [1, 0, 1, -171, -874], [1, 0, 1, -11, 12], [1, 0, 1, -2731, -55146]], [[0, 2, 3, 3, 0, 0], [2, 0, 0, 0, 3, 3], [3, 0, 0, 0, 2, 0], [3, 0, 0, 0, 0, 2], [0, 3, 2, 0, 0, 0], [0, 3, 0, 2, 0, 0]])"""
    def silverman_bound(self) -> Any:
        """_Curvedata.silverman_bound(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 329)

        The Silverman height bound for this elliptic curve.

        OUTPUT:

        (float) A nonnegative real number `B` such that for every
        rational point on this elliptic curve `E`, `h(P)\\le\\hat{h}(P)
        + B`, where `h(P)` is the naive height and `\\hat{h}(P)` the
        canonical height.

        .. NOTE::

            Since eclib can compute this to arbitrary precision, we
            could return a Sage real, but this is only a bound and in
            the contexts in which it is used extra precision is
            irrelevant.

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: E = _Curvedata(1,2,3,4,5)
            sage: E.silverman_bound()
            6.52226179519101...
            sage: type(E.silverman_bound())
            <class 'float'>"""

class _bigint:
    """_bigint(x='0')

    File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 182)

    Cython class wrapping eclib's bigint class."""
    def __init__(self, x=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 188)

                Constructor for bigint class.

                INPUT:

                - ``x`` -- string or int: a string representing a decimal
                  integer, or a Sage integer

                EXAMPLES::

                    sage: from sage.libs.eclib.mwrank import _bigint
                    sage: _bigint(123)
                    123
                    sage: _bigint('123')
                    123
                    sage: type(_bigint(123))
                    <class 'sage.libs.eclib.mwrank._bigint'>
        """

class _mw:
    """_mw(_Curvedata curve, verb=False, pp=1, maxr=999)

    File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 524)

    Cython class wrapping eclib's mw class."""
    def __init__(self, _Curvedatacurve, verb=..., pp=..., maxr=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 532)

                Constructor for mw class.

                INPUT:

                - ``curve`` -- _Curvedata; an elliptic curve

                - ``verb`` -- boolean (default: ``False``); verbosity flag (controls
                  amount of output produced in point searches)

                - ``pp`` -- integer (default: 1); process points flag (if nonzero,
                  the points found are processed, so that at all times only a
                  `\\ZZ`-basis for the subgroup generated by the points found
                  so far is stored. If zero, no processing is done and all
                  points found are stored).

                - ``maxr`` -- integer (default: 999); maximum rank (quit point
                  searching once the points found generate a subgroup of this
                  rank. Useful if an upper bound for the rank is already known).

                EXAMPLES::

                    sage: from sage.libs.eclib.mwrank import _mw
                    sage: from sage.libs.eclib.mwrank import _Curvedata
                    sage: E = _Curvedata(1,0,1,4,-6)
                    sage: EQ = _mw(E)
                    sage: EQ
                    []
                    sage: type(EQ)
                    <class 'sage.libs.eclib.mwrank._mw'>

                    sage: E = _Curvedata(0,0,1,-7,6)
                    sage: EQ = _mw(E)
                    sage: EQ.search(2)
                    sage: EQ
                    [[1:-1:1], [-2:3:1], [-14:25:8]]

                Example to illustrate the verbose parameter::

                    sage: from sage.libs.eclib.mwrank import _mw
                    sage: from sage.libs.eclib.mwrank import _Curvedata
                    sage: E = _Curvedata(0,0,1,-7,6)
                    sage: EQ = _mw(E, verb=False)
                    sage: EQ.search(1)
                    sage: EQ = _mw(E, verb=True)
                    sage: EQ.search(1)
                    P1 = [0:1:0]         is torsion point, order 1
                    P1 = [-3:0:1]         is generator number 1
                    saturating up to 20...Saturation index bound (for points of good reduction)  = 3
                    Reducing saturation bound from given value 20 to computed index bound 3
                    Tamagawa index primes are [ 2 ]...
                    Checking saturation at [ 2 3 ]
                    Checking 2-saturation
                    Points were proved 2-saturated (max q used = 7)
                    Checking 3-saturation
                    Points were proved 3-saturated (max q used = 7)
                    done
                    P2 = [-2:3:1]         is generator number 2
                    saturating up to 20...Saturation index bound (for points of good reduction)  = 4
                    Reducing saturation bound from given value 20 to computed index bound 4
                    Tamagawa index primes are [ 2 ]...
                    Checking saturation at [ 2 3 ]
                    Checking 2-saturation
                    possible kernel vector = [1,1]
                    This point may be in 2E(Q): [14:-52:1]
                    ...and it is!
                    Replacing old generator #1 with new generator [1:-1:1]
                    Reducing index bound from 4 to 2
                    Points have successfully been 2-saturated (max q used = 7)
                    Index gain = 2^1
                    done, index = 2.
                    Gained index 2, new generators = [ [1:-1:1] [-2:3:1] ]
                    P3 = [-14:25:8]       is generator number 3
                    saturating up to 20...Saturation index bound (for points of good reduction)  = 3
                    Reducing saturation bound from given value 20 to computed index bound 3
                    Tamagawa index primes are [ 2 ]...
                    Checking saturation at [ 2 3 ]
                    Checking 2-saturation
                    Points were proved 2-saturated (max q used = 11)
                    Checking 3-saturation
                    Points were proved 3-saturated (max q used = 13)
                    done, index = 1.
                    P4 = [-1:3:1]        = -1*P1 + -1*P2 + -1*P3 (mod torsion)
                    P4 = [0:2:1]         = 2*P1 + 0*P2 + 1*P3 (mod torsion)
                    P4 = [2:13:8]        = -3*P1 + 1*P2 + -1*P3 (mod torsion)
                    P4 = [1:0:1]         = -1*P1 + 0*P2 + 0*P3 (mod torsion)
                    P4 = [2:0:1]         = -1*P1 + 1*P2 + 0*P3 (mod torsion)
                    P4 = [18:7:8]        = -2*P1 + -1*P2 + -1*P3 (mod torsion)
                    P4 = [3:3:1]         = 1*P1 + 0*P2 + 1*P3 (mod torsion)
                    P4 = [4:6:1]         = 0*P1 + -1*P2 + -1*P3 (mod torsion)
                    P4 = [36:69:64]      = 1*P1 + -2*P2 + 0*P3 (mod torsion)
                    P4 = [68:-25:64]     = -2*P1 + -1*P2 + -2*P3 (mod torsion)
                    P4 = [12:35:27]      = 1*P1 + -1*P2 + -1*P3 (mod torsion)
                    sage: EQ
                    [[1:-1:1], [-2:3:1], [-14:25:8]]

                Example to illustrate the process points ``pp`` parameter::

                    sage: from sage.libs.eclib.mwrank import _mw
                    sage: from sage.libs.eclib.mwrank import _Curvedata
                    sage: E = _Curvedata(0,0,1,-7,6)
                    sage: EQ = _mw(E, pp=1)
                    sage: EQ.search(1); EQ
                    [[1:-1:1], [-2:3:1], [-14:25:8]]
                    sage: EQ = _mw(E, pp=0)
                    sage: EQ.search(1); EQ
                    [[-3:0:1], [-2:3:1], [-14:25:8], [-1:3:1], [0:2:1], [2:13:8], [1:0:1], [2:0:1], [18:7:8], [3:3:1], [4:6:1], [36:69:64], [68:-25:64], [12:35:27]]
        """
    @overload
    def getbasis(self) -> Any:
        """_mw.getbasis(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 738)

        Return the current basis of the mw structure.

        OUTPUT:

        (list) list of integer triples giving the projective
        coordinates of the points in the basis.

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: from sage.libs.eclib.mwrank import _mw
            sage: E = _Curvedata(0,1,1,-2,0)
            sage: EQ = _mw(E)
            sage: EQ.search(3)
            sage: EQ.getbasis()
            [[0, -1, 1], [-1, 1, 1]]
            sage: EQ.rank()
            2"""
    @overload
    def getbasis(self) -> Any:
        """_mw.getbasis(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 738)

        Return the current basis of the mw structure.

        OUTPUT:

        (list) list of integer triples giving the projective
        coordinates of the points in the basis.

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: from sage.libs.eclib.mwrank import _mw
            sage: E = _Curvedata(0,1,1,-2,0)
            sage: EQ = _mw(E)
            sage: EQ.search(3)
            sage: EQ.getbasis()
            [[0, -1, 1], [-1, 1, 1]]
            sage: EQ.rank()
            2"""
    def process(self, point, saturation_bound=...) -> Any:
        """_mw.process(self, point, saturation_bound=0)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 674)

        Processes the given point, adding it to the mw group.

        INPUT:

        - ``point`` -- tuple or list of 3 integers; an :exc:`ArithmeticError` is
          raised if the point is not on the curve

        - ``saturation_bound`` -- integer (default: 0); saturate at primes up
          to ``saturation_bound``. No saturation is done if
          ``saturation_bound=0``.  If ``saturation_bound=-1`` then
          saturation is done at all primes, by computing a bound on
          the saturation index.  Note that it is more efficient to add
          several points at once and then saturate just once at the end.

        .. NOTE::

            The eclib function which implements this only carries out
            any saturation if the rank of the points increases upon
            adding the new point.  This is because it is assumed that
            one saturates as ones goes along.

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: from sage.libs.eclib.mwrank import _mw
            sage: E = _Curvedata(0,1,1,-2,0)
            sage: EQ = _mw(E)

        Initially the list of gens is empty::

            sage: EQ
            []

        We process a point of infinite order::

            sage: EQ.process([-1,1,1])
            sage: EQ
            [[-1:1:1]]

        And another independent one::

            sage: EQ.process([0,-1,1])
            sage: EQ
            [[-1:1:1], [0:-1:1]]

        Processing a point dependent on the current basis will not
        change the basis::

            sage: EQ.process([4,8,1])
            sage: EQ
            [[-1:1:1], [0:-1:1]]"""
    @overload
    def rank(self) -> Any:
        """_mw.rank(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 795)

        Return the rank of the current basis of the mw group.

        OUTPUT:

        (Integer) The current rank.

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: from sage.libs.eclib.mwrank import _mw
            sage: E = _Curvedata(0,1,1,-2,0)
            sage: EQ = _mw(E)
            sage: EQ.search(3)
            sage: EQ.getbasis()
            [[0, -1, 1], [-1, 1, 1]]
            sage: EQ.rank()
            2"""
    @overload
    def rank(self) -> Any:
        """_mw.rank(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 795)

        Return the rank of the current basis of the mw group.

        OUTPUT:

        (Integer) The current rank.

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: from sage.libs.eclib.mwrank import _mw
            sage: E = _Curvedata(0,1,1,-2,0)
            sage: EQ = _mw(E)
            sage: EQ.search(3)
            sage: EQ.getbasis()
            [[0, -1, 1], [-1, 1, 1]]
            sage: EQ.rank()
            2"""
    @overload
    def regulator(self) -> Any:
        """_mw.regulator(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 763)

        Return the regulator of the current basis of the mw group.

        OUTPUT:

        (double) The current regulator.

        .. TODO::

            ``eclib`` computes the regulator to arbitrary precision, and
            the full precision value should be returned.

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: from sage.libs.eclib.mwrank import _mw
            sage: E = _Curvedata(0,1,1,-2,0)
            sage: EQ = _mw(E)
            sage: EQ.search(3)
            sage: EQ.getbasis()
            [[0, -1, 1], [-1, 1, 1]]
            sage: EQ.rank()
            2
            sage: EQ.regulator()
            0.15246017794314376"""
    @overload
    def regulator(self) -> Any:
        """_mw.regulator(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 763)

        Return the regulator of the current basis of the mw group.

        OUTPUT:

        (double) The current regulator.

        .. TODO::

            ``eclib`` computes the regulator to arbitrary precision, and
            the full precision value should be returned.

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: from sage.libs.eclib.mwrank import _mw
            sage: E = _Curvedata(0,1,1,-2,0)
            sage: EQ = _mw(E)
            sage: EQ.search(3)
            sage: EQ.getbasis()
            [[0, -1, 1], [-1, 1, 1]]
            sage: EQ.rank()
            2
            sage: EQ.regulator()
            0.15246017794314376"""
    @overload
    def saturate(self, intsat_bd=..., intsat_low_bd=...) -> Any:
        """_mw.saturate(self, int sat_bd=-1, int sat_low_bd=2)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 820)

        Saturates the current subgroup of the mw group.

        INPUT:

        - ``sat_bnd`` -- integer (default: -1); upper bound on primes at
          which to saturate.  If -1 (default), compute a bound for the
          primes which may not be saturated, and use that.  Otherwise,
          the bound used is the minimum of the value of ``sat_bnd``
          and the computed bound.

        - ``sat_low_bd`` -- integer (default: 2); only do saturation at
          prime not less than this.  For example, if the points have
          been found via 2-descent they should already be 2-saturated,
          and ``sat_low_bd=3`` is appropriate.

        OUTPUT:

        (tuple) (success flag, index, list) The success flag will be 1
        unless something failed (usually an indication that the points
        were not saturated but eclib was not able to divide out
        successfully).  The index is the index of the mw group before
        saturation in the mw group after.  The list is a string
        representation of the primes at which saturation was not
        proved or achieved.

        .. NOTE::

        ``eclib`` will compute a bound on the saturation index.  If
        the computed saturation bound is very large and ``sat_bnd`` is
        -1, ``eclib`` may output a warning, but will still attempt to
        saturate up to the computed bound.  If a positive value of
        ``sat_bnd`` is given which is greater than the computed bound,
        `p`-saturation will only be carried out for primes up to the
        compated bound.  Setting ``sat_low_bnd`` to a value greater
        than 2 allows for saturation to be done incrementally, or for
        exactly one prime `p` by setting both ``sat_bd`` and
        ``sat_low_bd`` to `p`.

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: from sage.libs.eclib.mwrank import _mw
            sage: E = _Curvedata(0,1,1,-2,0)
            sage: EQ = _mw(E)
            sage: EQ.process([494, -5720, 6859]) # 3 times another point
            sage: EQ
            [[494:-5720:6859]]
            sage: EQ.saturate()
            (1, 3, '[ ]')
            sage: EQ
            [[-1:1:1]]

        If we set the saturation bound at 2, then saturation will not
        enlarge the basis, but the success flag is still 1 (True)
        since we did not ask to check 3-saturation::

            sage: EQ = _mw(E)
            sage: EQ.process([494, -5720, 6859]) # 3 times another point
            sage: EQ.saturate(sat_bd=2)
            (1, 1, '[ ]')
            sage: EQ
            [[494:-5720:6859]]"""
    @overload
    def saturate(self) -> Any:
        """_mw.saturate(self, int sat_bd=-1, int sat_low_bd=2)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 820)

        Saturates the current subgroup of the mw group.

        INPUT:

        - ``sat_bnd`` -- integer (default: -1); upper bound on primes at
          which to saturate.  If -1 (default), compute a bound for the
          primes which may not be saturated, and use that.  Otherwise,
          the bound used is the minimum of the value of ``sat_bnd``
          and the computed bound.

        - ``sat_low_bd`` -- integer (default: 2); only do saturation at
          prime not less than this.  For example, if the points have
          been found via 2-descent they should already be 2-saturated,
          and ``sat_low_bd=3`` is appropriate.

        OUTPUT:

        (tuple) (success flag, index, list) The success flag will be 1
        unless something failed (usually an indication that the points
        were not saturated but eclib was not able to divide out
        successfully).  The index is the index of the mw group before
        saturation in the mw group after.  The list is a string
        representation of the primes at which saturation was not
        proved or achieved.

        .. NOTE::

        ``eclib`` will compute a bound on the saturation index.  If
        the computed saturation bound is very large and ``sat_bnd`` is
        -1, ``eclib`` may output a warning, but will still attempt to
        saturate up to the computed bound.  If a positive value of
        ``sat_bnd`` is given which is greater than the computed bound,
        `p`-saturation will only be carried out for primes up to the
        compated bound.  Setting ``sat_low_bnd`` to a value greater
        than 2 allows for saturation to be done incrementally, or for
        exactly one prime `p` by setting both ``sat_bd`` and
        ``sat_low_bd`` to `p`.

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: from sage.libs.eclib.mwrank import _mw
            sage: E = _Curvedata(0,1,1,-2,0)
            sage: EQ = _mw(E)
            sage: EQ.process([494, -5720, 6859]) # 3 times another point
            sage: EQ
            [[494:-5720:6859]]
            sage: EQ.saturate()
            (1, 3, '[ ]')
            sage: EQ
            [[-1:1:1]]

        If we set the saturation bound at 2, then saturation will not
        enlarge the basis, but the success flag is still 1 (True)
        since we did not ask to check 3-saturation::

            sage: EQ = _mw(E)
            sage: EQ.process([494, -5720, 6859]) # 3 times another point
            sage: EQ.saturate(sat_bd=2)
            (1, 1, '[ ]')
            sage: EQ
            [[494:-5720:6859]]"""
    @overload
    def saturate(self, sat_bd=...) -> Any:
        """_mw.saturate(self, int sat_bd=-1, int sat_low_bd=2)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 820)

        Saturates the current subgroup of the mw group.

        INPUT:

        - ``sat_bnd`` -- integer (default: -1); upper bound on primes at
          which to saturate.  If -1 (default), compute a bound for the
          primes which may not be saturated, and use that.  Otherwise,
          the bound used is the minimum of the value of ``sat_bnd``
          and the computed bound.

        - ``sat_low_bd`` -- integer (default: 2); only do saturation at
          prime not less than this.  For example, if the points have
          been found via 2-descent they should already be 2-saturated,
          and ``sat_low_bd=3`` is appropriate.

        OUTPUT:

        (tuple) (success flag, index, list) The success flag will be 1
        unless something failed (usually an indication that the points
        were not saturated but eclib was not able to divide out
        successfully).  The index is the index of the mw group before
        saturation in the mw group after.  The list is a string
        representation of the primes at which saturation was not
        proved or achieved.

        .. NOTE::

        ``eclib`` will compute a bound on the saturation index.  If
        the computed saturation bound is very large and ``sat_bnd`` is
        -1, ``eclib`` may output a warning, but will still attempt to
        saturate up to the computed bound.  If a positive value of
        ``sat_bnd`` is given which is greater than the computed bound,
        `p`-saturation will only be carried out for primes up to the
        compated bound.  Setting ``sat_low_bnd`` to a value greater
        than 2 allows for saturation to be done incrementally, or for
        exactly one prime `p` by setting both ``sat_bd`` and
        ``sat_low_bd`` to `p`.

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: from sage.libs.eclib.mwrank import _mw
            sage: E = _Curvedata(0,1,1,-2,0)
            sage: EQ = _mw(E)
            sage: EQ.process([494, -5720, 6859]) # 3 times another point
            sage: EQ
            [[494:-5720:6859]]
            sage: EQ.saturate()
            (1, 3, '[ ]')
            sage: EQ
            [[-1:1:1]]

        If we set the saturation bound at 2, then saturation will not
        enlarge the basis, but the success flag is still 1 (True)
        since we did not ask to check 3-saturation::

            sage: EQ = _mw(E)
            sage: EQ.process([494, -5720, 6859]) # 3 times another point
            sage: EQ.saturate(sat_bd=2)
            (1, 1, '[ ]')
            sage: EQ
            [[494:-5720:6859]]"""
    def search(self, h_lim, intmoduli_option=..., intverb=...) -> Any:
        '''_mw.search(self, h_lim, int moduli_option=0, int verb=0)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 893)

        Search for points in the mw group.

        INPUT:

        - ``h_lim`` -- integer; bound on logarithmic naive height of points

        - ``moduli_option`` -- integer (default: 0); option for sieving
          strategy.  The default (0) uses an adapted version of
          Stoll\'s ratpoints code and is recommended.

        - ``verb`` -- integer (default: 0); level of verbosity.  If 0, no
          output.  If positive, the points are output as found and
          some details of the processing, finding linear relations,
          and partial saturation are output.

        .. NOTE::

            The effect of the search is also governed by the class
            options, notably whether the points found are processed:
            meaning that linear relations are found and saturation is
            carried out, with the result that the list of generators
            will always contain a `\\ZZ`-span of the saturation of the
            points found, modulo torsion.

        OUTPUT: none; the effect of the search is to update the list of generators

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: from sage.libs.eclib.mwrank import _mw
            sage: E = _Curvedata(0,0,1,-19569,-4064513) # 873c1
            sage: EQ = _mw(E)
            sage: EQ = _mw(E)
            sage: for i in [1..11]:
            ....:     print("{} {} {}".format(i, EQ.search(i), EQ))
            1 None []
            2 None []
            3 None []
            4 None []
            5 None []
            6 None []
            7 None []
            8 None []
            9 None []
            10 None []
            11 None [[3639568:106817593:4096]]'''

class _two_descent:
    """_two_descent()

    File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 951)

    Cython class wrapping eclib's two_descent class."""
    def __init__(self) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 957)

                Constructor for two_descent class.

                EXAMPLES::

                    sage: from sage.libs.eclib.mwrank import _two_descent
                    sage: D2 = _two_descent()
        """
    @overload
    def do_descent(self, _Curvedatacurve, intverb=..., intsel=..., intfirstlim=..., intsecondlim=..., intn_aux=..., intsecond_descent=...) -> Any:
        """_two_descent.do_descent(self, _Curvedata curve, int verb=1, int sel=0, int firstlim=20, int secondlim=8, int n_aux=-1, int second_descent=1)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 974)

        Carry out a 2-descent.

        INPUT:

        - ``curvedata`` -- _Curvedata; the curve on which to do descent

        - ``verb`` -- integer (default: 1); verbosity level

        - ``sel`` -- integer (default: 0); Selmer-only flag.  If 1, only
          the 2-Selmer group will be computed, with no rational
          points.  Useful as a faster way of getting an upper bound on
          the rank.

        - ``firstlim``, ``secondlim``, ``n_aux``, ``second_descent`` --
          see ``first_limit``, ``second_limit``, ``n_aux``, ``second_descent``
          respectively in :meth:`~sage.libs.eclib.interface.mwrank_EllipticCurve.two_descent`
          (although ``second_descent`` here is ``1`` or ``0`` instead of ``True`` or ``False``
          respectively)

        OUTPUT: none

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: CD = _Curvedata(0,0,1,-7,6)
            sage: from sage.libs.eclib.mwrank import _two_descent
            sage: D2 = _two_descent()
            sage: D2.do_descent(CD)
            Basic pair: I=336, J=-10800
            disc=35092224
            ...
            Mordell rank contribution from B=im(eps) = 3
            Selmer  rank contribution from B=im(eps) = 3
            Sha     rank contribution from B=im(eps) = 0
            Mordell rank contribution from A=ker(eps) = 0
            Selmer  rank contribution from A=ker(eps) = 0
            Sha     rank contribution from A=ker(eps) = 0
            sage: D2.getrank()
            3
            sage: D2.getcertain()
            1
            sage: D2.ok()
            1"""
    @overload
    def do_descent(self, CD) -> Any:
        """_two_descent.do_descent(self, _Curvedata curve, int verb=1, int sel=0, int firstlim=20, int secondlim=8, int n_aux=-1, int second_descent=1)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 974)

        Carry out a 2-descent.

        INPUT:

        - ``curvedata`` -- _Curvedata; the curve on which to do descent

        - ``verb`` -- integer (default: 1); verbosity level

        - ``sel`` -- integer (default: 0); Selmer-only flag.  If 1, only
          the 2-Selmer group will be computed, with no rational
          points.  Useful as a faster way of getting an upper bound on
          the rank.

        - ``firstlim``, ``secondlim``, ``n_aux``, ``second_descent`` --
          see ``first_limit``, ``second_limit``, ``n_aux``, ``second_descent``
          respectively in :meth:`~sage.libs.eclib.interface.mwrank_EllipticCurve.two_descent`
          (although ``second_descent`` here is ``1`` or ``0`` instead of ``True`` or ``False``
          respectively)

        OUTPUT: none

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: CD = _Curvedata(0,0,1,-7,6)
            sage: from sage.libs.eclib.mwrank import _two_descent
            sage: D2 = _two_descent()
            sage: D2.do_descent(CD)
            Basic pair: I=336, J=-10800
            disc=35092224
            ...
            Mordell rank contribution from B=im(eps) = 3
            Selmer  rank contribution from B=im(eps) = 3
            Sha     rank contribution from B=im(eps) = 0
            Mordell rank contribution from A=ker(eps) = 0
            Selmer  rank contribution from A=ker(eps) = 0
            Sha     rank contribution from A=ker(eps) = 0
            sage: D2.getrank()
            3
            sage: D2.getcertain()
            1
            sage: D2.ok()
            1"""
    def getbasis(self) -> Any:
        """_two_descent.getbasis(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 1229)

        Return the basis of points found by doing a 2-descent.

        If the success and certain flags are 1, this will be a
        `\\ZZ/2\\ZZ`-basis for `E(\\QQ)/2E(\\QQ)` (modulo torsion),
        otherwise possibly only for a proper subgroup.

        .. NOTE::

            You must call ``saturate()`` first, or a :exc:`RunTimeError`
            will be raised.

        OUTPUT:

        (string) String representation of the list of points after
        saturation.

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: CD = _Curvedata(0,0,1,-7,6)
            sage: from sage.libs.eclib.mwrank import _two_descent
            sage: D2 = _two_descent()
            sage: D2.do_descent(CD)
            Basic pair: I=336, J=-10800
            disc=35092224
            ...
            Mordell rank contribution from B=im(eps) = 3
            Selmer  rank contribution from B=im(eps) = 3
            Sha     rank contribution from B=im(eps) = 0
            Mordell rank contribution from A=ker(eps) = 0
            Selmer  rank contribution from A=ker(eps) = 0
            Sha     rank contribution from A=ker(eps) = 0
            sage: D2.saturate()
            Searching for points (bound = 8)...done:
              found points which generate a subgroup of rank 3
              and regulator 0.417...
            Processing points found during 2-descent...done:
              now regulator = 0.417...
            No saturation being done
            sage: D2.getbasis()
            '[[1:-1:1], [-2:3:1], [-14:25:8]]'"""
    @overload
    def getcertain(self) -> Any:
        """_two_descent.getcertain(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 1155)

        Return the certainty flag (after doing a 2-descent).

        OUTPUT: boolean; ``True`` if the rank upper and lower bounds are equal

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: CD = _Curvedata(0,0,1,-7,6)
            sage: from sage.libs.eclib.mwrank import _two_descent
            sage: D2 = _two_descent()
            sage: D2.do_descent(CD)
            Basic pair: I=336, J=-10800
            disc=35092224
            ...
            Mordell rank contribution from B=im(eps) = 3
            Selmer  rank contribution from B=im(eps) = 3
            Sha     rank contribution from B=im(eps) = 0
            Mordell rank contribution from A=ker(eps) = 0
            Selmer  rank contribution from A=ker(eps) = 0
            Sha     rank contribution from A=ker(eps) = 0
            sage: D2.getcertain()
            1"""
    @overload
    def getcertain(self) -> Any:
        """_two_descent.getcertain(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 1155)

        Return the certainty flag (after doing a 2-descent).

        OUTPUT: boolean; ``True`` if the rank upper and lower bounds are equal

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: CD = _Curvedata(0,0,1,-7,6)
            sage: from sage.libs.eclib.mwrank import _two_descent
            sage: D2 = _two_descent()
            sage: D2.do_descent(CD)
            Basic pair: I=336, J=-10800
            disc=35092224
            ...
            Mordell rank contribution from B=im(eps) = 3
            Selmer  rank contribution from B=im(eps) = 3
            Sha     rank contribution from B=im(eps) = 0
            Mordell rank contribution from A=ker(eps) = 0
            Selmer  rank contribution from A=ker(eps) = 0
            Sha     rank contribution from A=ker(eps) = 0
            sage: D2.getcertain()
            1"""
    @overload
    def getrank(self) -> Any:
        """_two_descent.getrank(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 1030)

        Return the rank (after doing a 2-descent).

        OUTPUT:

        (Integer) the rank (or an upper bound).

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: CD = _Curvedata(0,0,1,-7,6)
            sage: from sage.libs.eclib.mwrank import _two_descent
            sage: D2 = _two_descent()
            sage: D2.do_descent(CD)
            Basic pair: I=336, J=-10800
            disc=35092224
            ...
            Mordell rank contribution from B=im(eps) = 3
            Selmer  rank contribution from B=im(eps) = 3
            Sha     rank contribution from B=im(eps) = 0
            Mordell rank contribution from A=ker(eps) = 0
            Selmer  rank contribution from A=ker(eps) = 0
            Sha     rank contribution from A=ker(eps) = 0
            sage: D2.getrank()
            3"""
    @overload
    def getrank(self) -> Any:
        """_two_descent.getrank(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 1030)

        Return the rank (after doing a 2-descent).

        OUTPUT:

        (Integer) the rank (or an upper bound).

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: CD = _Curvedata(0,0,1,-7,6)
            sage: from sage.libs.eclib.mwrank import _two_descent
            sage: D2 = _two_descent()
            sage: D2.do_descent(CD)
            Basic pair: I=336, J=-10800
            disc=35092224
            ...
            Mordell rank contribution from B=im(eps) = 3
            Selmer  rank contribution from B=im(eps) = 3
            Sha     rank contribution from B=im(eps) = 0
            Mordell rank contribution from A=ker(eps) = 0
            Selmer  rank contribution from A=ker(eps) = 0
            Sha     rank contribution from A=ker(eps) = 0
            sage: D2.getrank()
            3"""
    @overload
    def getrankbound(self) -> Any:
        """_two_descent.getrankbound(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 1063)

        Return the rank upper bound (after doing a 2-descent).

        OUTPUT:

        (Integer) an upper bound on the rank.

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: CD = _Curvedata(0,0,1,-7,6)
            sage: from sage.libs.eclib.mwrank import _two_descent
            sage: D2 = _two_descent()
            sage: D2.do_descent(CD)
            Basic pair: I=336, J=-10800
            disc=35092224
            ...
            Mordell rank contribution from B=im(eps) = 3
            Selmer  rank contribution from B=im(eps) = 3
            Sha     rank contribution from B=im(eps) = 0
            Mordell rank contribution from A=ker(eps) = 0
            Selmer  rank contribution from A=ker(eps) = 0
            Sha     rank contribution from A=ker(eps) = 0
            sage: D2.getrankbound()
            3"""
    @overload
    def getrankbound(self) -> Any:
        """_two_descent.getrankbound(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 1063)

        Return the rank upper bound (after doing a 2-descent).

        OUTPUT:

        (Integer) an upper bound on the rank.

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: CD = _Curvedata(0,0,1,-7,6)
            sage: from sage.libs.eclib.mwrank import _two_descent
            sage: D2 = _two_descent()
            sage: D2.do_descent(CD)
            Basic pair: I=336, J=-10800
            disc=35092224
            ...
            Mordell rank contribution from B=im(eps) = 3
            Selmer  rank contribution from B=im(eps) = 3
            Sha     rank contribution from B=im(eps) = 0
            Mordell rank contribution from A=ker(eps) = 0
            Selmer  rank contribution from A=ker(eps) = 0
            Sha     rank contribution from A=ker(eps) = 0
            sage: D2.getrankbound()
            3"""
    @overload
    def getselmer(self) -> Any:
        """_two_descent.getselmer(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 1096)

        Return the 2-Selmer rank (after doing a 2-descent).

        OUTPUT:

        (Integer) The 2-Selmer rank.

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: CD = _Curvedata(0,0,1,-7,6)
            sage: from sage.libs.eclib.mwrank import _two_descent
            sage: D2 = _two_descent()
            sage: D2.do_descent(CD)
            Basic pair: I=336, J=-10800
            disc=35092224
            ...
            Mordell rank contribution from B=im(eps) = 3
            Selmer  rank contribution from B=im(eps) = 3
            Sha     rank contribution from B=im(eps) = 0
            Mordell rank contribution from A=ker(eps) = 0
            Selmer  rank contribution from A=ker(eps) = 0
            Sha     rank contribution from A=ker(eps) = 0
            sage: D2.getselmer()
            3"""
    @overload
    def getselmer(self) -> Any:
        """_two_descent.getselmer(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 1096)

        Return the 2-Selmer rank (after doing a 2-descent).

        OUTPUT:

        (Integer) The 2-Selmer rank.

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: CD = _Curvedata(0,0,1,-7,6)
            sage: from sage.libs.eclib.mwrank import _two_descent
            sage: D2 = _two_descent()
            sage: D2.do_descent(CD)
            Basic pair: I=336, J=-10800
            disc=35092224
            ...
            Mordell rank contribution from B=im(eps) = 3
            Selmer  rank contribution from B=im(eps) = 3
            Sha     rank contribution from B=im(eps) = 0
            Mordell rank contribution from A=ker(eps) = 0
            Selmer  rank contribution from A=ker(eps) = 0
            Sha     rank contribution from A=ker(eps) = 0
            sage: D2.getselmer()
            3"""
    @overload
    def ok(self) -> Any:
        """_two_descent.ok(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 1128)

        Return the success flag (after doing a 2-descent).

        OUTPUT: boolean flag indicating whether or not 2-descent was successful

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: CD = _Curvedata(0,0,1,-7,6)
            sage: from sage.libs.eclib.mwrank import _two_descent
            sage: D2 = _two_descent()
            sage: D2.do_descent(CD)
            Basic pair: I=336, J=-10800
            disc=35092224
            ...
            Mordell rank contribution from B=im(eps) = 3
            Selmer  rank contribution from B=im(eps) = 3
            Sha     rank contribution from B=im(eps) = 0
            Mordell rank contribution from A=ker(eps) = 0
            Selmer  rank contribution from A=ker(eps) = 0
            Sha     rank contribution from A=ker(eps) = 0
            sage: D2.ok()
            1"""
    @overload
    def ok(self) -> Any:
        """_two_descent.ok(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 1128)

        Return the success flag (after doing a 2-descent).

        OUTPUT: boolean flag indicating whether or not 2-descent was successful

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: CD = _Curvedata(0,0,1,-7,6)
            sage: from sage.libs.eclib.mwrank import _two_descent
            sage: D2 = _two_descent()
            sage: D2.do_descent(CD)
            Basic pair: I=336, J=-10800
            disc=35092224
            ...
            Mordell rank contribution from B=im(eps) = 3
            Selmer  rank contribution from B=im(eps) = 3
            Sha     rank contribution from B=im(eps) = 0
            Mordell rank contribution from A=ker(eps) = 0
            Selmer  rank contribution from A=ker(eps) = 0
            Sha     rank contribution from A=ker(eps) = 0
            sage: D2.ok()
            1"""
    @overload
    def regulator(self) -> Any:
        """_two_descent.regulator(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 1276)

        Return the regulator of the points found by doing a 2-descent.

        OUTPUT:

        (double) The regulator (of the subgroup found by 2-descent).

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: CD = _Curvedata(0,0,1,-7,6)
            sage: from sage.libs.eclib.mwrank import _two_descent
            sage: D2 = _two_descent()
            sage: D2.do_descent(CD)
            Basic pair: I=336, J=-10800
            disc=35092224
            ...
            Mordell rank contribution from B=im(eps) = 3
            Selmer  rank contribution from B=im(eps) = 3
            Sha     rank contribution from B=im(eps) = 0
            Mordell rank contribution from A=ker(eps) = 0
            Selmer  rank contribution from A=ker(eps) = 0
            Sha     rank contribution from A=ker(eps) = 0

        If called before calling ``saturate()``, a bogus value of 1.0
        is returned::

            sage: D2.regulator()
            1.0

        After saturation, both ``getbasis()`` and ``regulator()``
        return the basis and regulator of the subgroup found by
        2-descent::

            sage: D2.saturate()
            Searching for points (bound = 8)...done:
              found points which generate a subgroup of rank 3
              and regulator 0.417...
            Processing points found during 2-descent...done:
              now regulator = 0.417...
            No saturation being done
            sage: D2.getbasis()
            '[[1:-1:1], [-2:3:1], [-14:25:8]]'
            sage: D2.regulator()
            0.417143558758384"""
    @overload
    def regulator(self) -> Any:
        """_two_descent.regulator(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 1276)

        Return the regulator of the points found by doing a 2-descent.

        OUTPUT:

        (double) The regulator (of the subgroup found by 2-descent).

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: CD = _Curvedata(0,0,1,-7,6)
            sage: from sage.libs.eclib.mwrank import _two_descent
            sage: D2 = _two_descent()
            sage: D2.do_descent(CD)
            Basic pair: I=336, J=-10800
            disc=35092224
            ...
            Mordell rank contribution from B=im(eps) = 3
            Selmer  rank contribution from B=im(eps) = 3
            Sha     rank contribution from B=im(eps) = 0
            Mordell rank contribution from A=ker(eps) = 0
            Selmer  rank contribution from A=ker(eps) = 0
            Sha     rank contribution from A=ker(eps) = 0

        If called before calling ``saturate()``, a bogus value of 1.0
        is returned::

            sage: D2.regulator()
            1.0

        After saturation, both ``getbasis()`` and ``regulator()``
        return the basis and regulator of the subgroup found by
        2-descent::

            sage: D2.saturate()
            Searching for points (bound = 8)...done:
              found points which generate a subgroup of rank 3
              and regulator 0.417...
            Processing points found during 2-descent...done:
              now regulator = 0.417...
            No saturation being done
            sage: D2.getbasis()
            '[[1:-1:1], [-2:3:1], [-14:25:8]]'
            sage: D2.regulator()
            0.417143558758384"""
    @overload
    def regulator(self) -> Any:
        """_two_descent.regulator(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 1276)

        Return the regulator of the points found by doing a 2-descent.

        OUTPUT:

        (double) The regulator (of the subgroup found by 2-descent).

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: CD = _Curvedata(0,0,1,-7,6)
            sage: from sage.libs.eclib.mwrank import _two_descent
            sage: D2 = _two_descent()
            sage: D2.do_descent(CD)
            Basic pair: I=336, J=-10800
            disc=35092224
            ...
            Mordell rank contribution from B=im(eps) = 3
            Selmer  rank contribution from B=im(eps) = 3
            Sha     rank contribution from B=im(eps) = 0
            Mordell rank contribution from A=ker(eps) = 0
            Selmer  rank contribution from A=ker(eps) = 0
            Sha     rank contribution from A=ker(eps) = 0

        If called before calling ``saturate()``, a bogus value of 1.0
        is returned::

            sage: D2.regulator()
            1.0

        After saturation, both ``getbasis()`` and ``regulator()``
        return the basis and regulator of the subgroup found by
        2-descent::

            sage: D2.saturate()
            Searching for points (bound = 8)...done:
              found points which generate a subgroup of rank 3
              and regulator 0.417...
            Processing points found during 2-descent...done:
              now regulator = 0.417...
            No saturation being done
            sage: D2.getbasis()
            '[[1:-1:1], [-2:3:1], [-14:25:8]]'
            sage: D2.regulator()
            0.417143558758384"""
    @overload
    def regulator(self) -> Any:
        """_two_descent.regulator(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 1276)

        Return the regulator of the points found by doing a 2-descent.

        OUTPUT:

        (double) The regulator (of the subgroup found by 2-descent).

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: CD = _Curvedata(0,0,1,-7,6)
            sage: from sage.libs.eclib.mwrank import _two_descent
            sage: D2 = _two_descent()
            sage: D2.do_descent(CD)
            Basic pair: I=336, J=-10800
            disc=35092224
            ...
            Mordell rank contribution from B=im(eps) = 3
            Selmer  rank contribution from B=im(eps) = 3
            Sha     rank contribution from B=im(eps) = 0
            Mordell rank contribution from A=ker(eps) = 0
            Selmer  rank contribution from A=ker(eps) = 0
            Sha     rank contribution from A=ker(eps) = 0

        If called before calling ``saturate()``, a bogus value of 1.0
        is returned::

            sage: D2.regulator()
            1.0

        After saturation, both ``getbasis()`` and ``regulator()``
        return the basis and regulator of the subgroup found by
        2-descent::

            sage: D2.saturate()
            Searching for points (bound = 8)...done:
              found points which generate a subgroup of rank 3
              and regulator 0.417...
            Processing points found during 2-descent...done:
              now regulator = 0.417...
            No saturation being done
            sage: D2.getbasis()
            '[[1:-1:1], [-2:3:1], [-14:25:8]]'
            sage: D2.regulator()
            0.417143558758384"""
    @overload
    def saturate(self, saturation_bound=..., lower=...) -> Any:
        """_two_descent.saturate(self, saturation_bound=0, lower=3)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 1182)

        Carries out saturation of the points found by a 2-descent.

        INPUT:

        - ``saturation_bound`` -- integer; an upper bound on the primes
          `p` at which `p`-saturation will be carried out, or -1, in
          which case ``eclib`` will compute an upper bound on the
          saturation index.

        - ``lower`` -- integer (default: 3); do no `p`-saturation for `p`
          less than this.  The default is 3 since the points found
          during 2-descent will be 2-saturated.

        OUTPUT: none

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: CD = _Curvedata(0,0,1,-7,6)
            sage: from sage.libs.eclib.mwrank import _two_descent
            sage: D2 = _two_descent()
            sage: D2.do_descent(CD)
            Basic pair: I=336, J=-10800
            disc=35092224
            ...
            Mordell rank contribution from B=im(eps) = 3
            Selmer  rank contribution from B=im(eps) = 3
            Sha     rank contribution from B=im(eps) = 0
            Mordell rank contribution from A=ker(eps) = 0
            Selmer  rank contribution from A=ker(eps) = 0
            Sha     rank contribution from A=ker(eps) = 0
            sage: D2.saturate()
            Searching for points (bound = 8)...done:
              found points which generate a subgroup of rank 3
              and regulator 0.417...
            Processing points found during 2-descent...done:
              now regulator = 0.417...
            No saturation being done
            sage: D2.getbasis()
            '[[1:-1:1], [-2:3:1], [-14:25:8]]'"""
    @overload
    def saturate(self) -> Any:
        """_two_descent.saturate(self, saturation_bound=0, lower=3)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mwrank.pyx (starting at line 1182)

        Carries out saturation of the points found by a 2-descent.

        INPUT:

        - ``saturation_bound`` -- integer; an upper bound on the primes
          `p` at which `p`-saturation will be carried out, or -1, in
          which case ``eclib`` will compute an upper bound on the
          saturation index.

        - ``lower`` -- integer (default: 3); do no `p`-saturation for `p`
          less than this.  The default is 3 since the points found
          during 2-descent will be 2-saturated.

        OUTPUT: none

        EXAMPLES::

            sage: from sage.libs.eclib.mwrank import _Curvedata
            sage: CD = _Curvedata(0,0,1,-7,6)
            sage: from sage.libs.eclib.mwrank import _two_descent
            sage: D2 = _two_descent()
            sage: D2.do_descent(CD)
            Basic pair: I=336, J=-10800
            disc=35092224
            ...
            Mordell rank contribution from B=im(eps) = 3
            Selmer  rank contribution from B=im(eps) = 3
            Sha     rank contribution from B=im(eps) = 0
            Mordell rank contribution from A=ker(eps) = 0
            Selmer  rank contribution from A=ker(eps) = 0
            Sha     rank contribution from A=ker(eps) = 0
            sage: D2.saturate()
            Searching for points (bound = 8)...done:
              found points which generate a subgroup of rank 3
              and regulator 0.417...
            Processing points found during 2-descent...done:
              now regulator = 0.417...
            No saturation being done
            sage: D2.getbasis()
            '[[1:-1:1], [-2:3:1], [-14:25:8]]'"""
