from sage.arith.functions import lcm as lcm
from sage.matrix.constructor import block_matrix as block_matrix, diagonal_matrix as diagonal_matrix, matrix as matrix
from sage.modules.free_module_element import vector as vector
from sage.rings.fraction_field import FractionField_generic as FractionField_generic
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.schemes.plane_conics.con_field import ProjectiveConic_field as ProjectiveConic_field

class ProjectiveConic_rational_function_field(ProjectiveConic_field):
    """
    Create a projective plane conic curve over a rational function field
    `F(t)`, where `F` is any field.

    The algorithms used in this class come mostly from [HC2006]_.

    EXAMPLES::

        sage: K = FractionField(PolynomialRing(QQ, 't'))
        sage: P.<X, Y, Z> = K[]
        sage: Conic(X^2 + Y^2 - Z^2)
        Projective Conic Curve over Fraction Field of Univariate
        Polynomial Ring in t over Rational Field defined by
        X^2 + Y^2 - Z^2

    TESTS::

        sage: K = FractionField(PolynomialRing(QQ, 't'))
        sage: Conic([K(1), 1, -1])._test_pickling()

    REFERENCES:

    - [HC2006]_
    - [Ack2016]_
    """
    def __init__(self, A, f) -> None:
        """
        See ``Conic`` for full documentation.

        EXAMPLES::

            sage: c = Conic([1, 1, 1]); c
            Projective Conic Curve over Rational Field defined by
            x^2 + y^2 + z^2
        """
    def has_rational_point(self, point: bool = False, algorithm: str = 'default', read_cache: bool = True):
        """
        Return ``True`` if and only if the conic ``self``
        has a point over its base field `F(t)`, which is a field of rational
        functions.

        If ``point`` is True, then returns a second output, which is
        a rational point if one exists.

        Points are cached whenever they are found. Cached information
        is used if and only if ``read_cache`` is True.

        The default algorithm does not (yet) work for all base fields `F`.
        In particular, sage is required to have:

        * an algorithm for finding the square root of elements in finite
          extensions of `F`;

        * a factorization and gcd algorithm for `F[t]`;

        * an algorithm for solving conics over `F`.

        ALGORITHM:

        The parameter ``algorithm`` specifies the algorithm
        to be used:

        * ``'default'`` -- use a native Sage implementation, based on the
          algorithm Conic in [HC2006]_.

        * ``'magma'`` (requires Magma to be installed) --
          delegates the task to the Magma computer algebra
          system.

        EXAMPLES:

        We can find points for function fields over (extensions of) `\\QQ`
        and finite fields::

            sage: K.<t> = FractionField(PolynomialRing(QQ, 't'))
            sage: C = Conic(K, [t^2 - 2, 2*t^3, -2*t^3 - 13*t^2 - 2*t + 18])
            sage: C.has_rational_point(point=True)                                      # needs sage.libs.singular
            (True, (3 : (t + 1)/t : 1))

            sage: R.<t> = FiniteField(23)[]
            sage: C = Conic([2, t^2 + 1, t^2 + 5])
            sage: C.has_rational_point()                                                # needs sage.libs.singular
            True
            sage: C.has_rational_point(point=True)                                      # needs sage.libs.singular
            (True, (5*t : 8 : 1))

            sage: # needs sage.rings.number_field
            sage: F.<i> = QuadraticField(-1)
            sage: R.<t> = F[]
            sage: C = Conic([1, i*t, -t^2 + 4])
            sage: C.has_rational_point(point=True)                                      # needs sage.libs.singular
            (True, (-t - 2*i : -2*i : 1))

        It works on non-diagonal conics as well::

            sage: K.<t> = QQ[]
            sage: C = Conic([4, -4, 8, 1, -4, t + 4])
            sage: C.has_rational_point(point=True)                                      # needs sage.libs.singular
            (True, (1/2 : 1 : 0))

        If no point exists output still depends on the argument ``point``::

            sage: K.<t> = QQ[]
            sage: C = Conic(K, [t^2, (t-1), -2*(t-1)])
            sage: C.has_rational_point()                                                # needs sage.libs.singular
            False
            sage: C.has_rational_point(point=True)                                      # needs sage.libs.singular
            (False, None)

        Due to limitations in Sage of algorithms we depend on, it is not
        yet possible to find points on conics over multivariate function fields
        (see the requirements above)::

            sage: F.<t1> = FractionField(QQ['t1'])
            sage: K.<t2> = FractionField(F['t2'])
            sage: a = K(1)
            sage: b = 2*t2^2 + 2*t1*t2 - t1^2
            sage: c = -3*t2^4 - 4*t1*t2^3 + 8*t1^2*t2^2 + 16*t1^3 - t2 - 48*t1^4
            sage: C = Conic([a,b,c])
            sage: C.has_rational_point()                                                # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            NotImplementedError: is_square() not implemented for elements of
            Univariate Quotient Polynomial Ring in tbar over Fraction Field
            of Univariate Polynomial Ring in t1 over Rational Field with
            modulus tbar^2 + t1*tbar - 1/2*t1^2

        In some cases, the algorithm requires us to be
        able to solve conics over `F`. In particular, the following does not
        work::

            sage: P.<u> = QQ[]
            sage: E = P.fraction_field()
            sage: Q.<Y> = E[]
            sage: F.<v> = E.extension(Y^2 - u^3 - 1)
            sage: R.<t> = F[]
            sage: K = R.fraction_field()                                                # needs sage.rings.function_field
            sage: C = Conic(K, [u, v, 1])                                               # needs sage.rings.function_field
            sage: C.has_rational_point()                                                # needs sage.rings.function_field
            Traceback (most recent call last):
            ...
            NotImplementedError: has_rational_point not implemented for conics
            over base field Univariate Quotient Polynomial Ring in v over
            Fraction Field of Univariate Polynomial Ring in u over Rational
            Field with modulus v^2 - u^3 - 1

        TESTS::

            sage: K.<t> = FractionField(PolynomialRing(QQ, 't'))
            sage: a = (2*t^2 - 3/2*t + 1)/(37/3*t^2 + t - 1/4)
            sage: b = (1/2*t^2 + 1/3)/(-73*t^2 - 2*t + 11/4)
            sage: c = (6934/3*t^6 + 8798/3*t^5 - 947/18*t^4 + 3949/9*t^3 + 20983/18*t^2 + 28/3*t - 131/3)/(-2701/3*t^4 - 293/3*t^3 + 301/6*t^2 + 13/4*t - 11/16)
            sage: C = Conic([a,b,c])
            sage: C.has_rational_point(point=True)                                      # needs sage.libs.singular
            (True, (4*t + 4 : 2*t + 2 : 1))

        A long time test::

            sage: K.<t> = FractionField(PolynomialRing(QQ, 't'))
            sage: a = (-1/3*t^6 - 14*t^5 - 1/4*t^4 + 7/2*t^2 - 1/2*t - 1)/(24/5*t^6 - t^5 - 1/4*t^4 + t^3 - 3*t^2 + 8/5*t + 5)
            sage: b = (-3*t^3 + 8*t + 1/2)/(-1/3*t^3 + 3/2*t^2 + 1/12*t + 1/2)
            sage: c = (1232009/225*t^25 - 1015925057/8100*t^24 + 1035477411553/1458000*t^23 + 7901338091/30375*t^22 - 1421379260447/729000*t^21 + 266121260843/972000*t^20 + 80808723191/486000*t^19 - 516656082523/972000*t^18 + 21521589529/40500*t^17 + 4654758997/21600*t^16 - 20064038625227/9720000*t^15 - 173054270347/324000*t^14 + 536200870559/540000*t^13 - 12710739349/50625*t^12 - 197968226971/135000*t^11 - 134122025657/810000*t^10 + 22685316301/120000*t^9 - 2230847689/21600*t^8 - 70624099679/270000*t^7 - 4298763061/270000*t^6 - 41239/216000*t^5 - 13523/36000*t^4 + 493/36000*t^3 + 83/2400*t^2 + 1/300*t + 1/200)/(-27378/125*t^17 + 504387/500*t^16 - 97911/2000*t^15 + 1023531/4000*t^14 + 1874841/8000*t^13 + 865381/12000*t^12 + 15287/375*t^11 + 6039821/6000*t^10 + 599437/1500*t^9 + 18659/250*t^8 + 1218059/6000*t^7 + 2025127/3000*t^6 + 1222759/6000*t^5 + 38573/200*t^4 + 8323/125*t^3 + 15453/125*t^2 + 17031/500*t + 441/10)
            sage: C = Conic([a,b,c])
            sage: C.has_rational_point(point=True)      # long time (4 seconds)         # needs sage.libs.singular
            (True,
            ((-86/9*t^17 + 1907490361/17182854*t^16 - 1363042615/206194248*t^15 - 4383072337/17182854*t^14 + 80370059033/618582744*t^13 + 62186354267/3092913720*t^12 - 1809118729/15861096*t^11 + 1002057383551/6185827440*t^10 - 483841158703/12371654880*t^9 - 627776378677/2061942480*t^8 - 197829033097/6185827440*t^7 + 386127705377/4123884960*t^6 - 5215102697/137462832*t^5 - 35978456911/317221920*t^4 - 1157738773/171828540*t^3 + 27472621/206194248*t^2 + 82006/2863809*t + 2808401/68731416)/(t^13 + 50677847/1272804*t^12 - 3017827697/15273648*t^11 - 144120133/5727618*t^10 - 3819228607/45820944*t^9 + 13738260095/274925664*t^8 - 10164360733/137462832*t^7 - 23583281/3818412*t^6 - 3902993449/137462832*t^5 + 1816361849/137462832*t^4 - 8343925/11455236*t^3 + 7102163/17182854*t^2 - 15173719/11455236*t - 19573057/11455236) : (655/351*t^17 + 4642530179/103097124*t^16 - 149195572469/137462832*t^15 + 1532672896471/412388496*t^14 + 46038188783/137462832*t^13 + 1373933278223/824776992*t^12 - 881883150035/824776992*t^11 + 47830791587/34365708*t^10 + 29359089785/412388496*t^9 + 58511538875/103097124*t^8 - 8651292257/34365708*t^7 + 647251073/51548562*t^6 - 424282657/45820944*t^5 + 212494760/8591427*t^4 + 746976293/22910472*t^3 - 1085/195816*t^2 - 1085/954603*t - 1085/636402)/(t^13 + 50677847/1272804*t^12 - 3017827697/15273648*t^11 - 144120133/5727618*t^10 - 3819228607/45820944*t^9 + 13738260095/274925664*t^8 - 10164360733/137462832*t^7 - 23583281/3818412*t^6 - 3902993449/137462832*t^5 + 1816361849/137462832*t^4 - 8343925/11455236*t^3 + 7102163/17182854*t^2 - 15173719/11455236*t - 19573057/11455236) : 1))


        ``has_rational_point`` used to fail for some conics over function fields
        over finite fields, due to :issue:`20003`::

            sage: K.<t> = PolynomialRing(GF(7))
            sage: C = Conic([5*t^2 + 4, t^2 + 3*t + 3, 6*t^2 + 3*t + 2,
            ....:            5*t^2 + 5, 4*t + 3, 4*t^2 + t + 5])
            sage: C.has_rational_point()
            True
        """
    def find_point(self, supports, roots, case, solution: int = 0):
        """
        Given a solubility certificate like in [HC2006]_, find a point on
        ``self``. Assumes ``self`` is in reduced form (see [HC2006]_ for a
        definition).

        If you don't have a solubility certificate and just want to find a
        point, use the function :meth:`has_rational_point` instead.

        INPUT:

        - ``self`` -- conic in reduced form
        - ``supports`` -- 3-tuple where ``supports[i]`` is a list of all monic
          irreducible `p \\in F[t]` that divide the `i`-th of the 3 coefficients
        - ``roots`` -- 3-tuple containing lists of roots of all elements of
          ``supports[i]``, in the same order
        - ``case`` -- 1 or 0, as in [HC2006]_
        - ``solution`` -- (default: 0) a solution of (5) in [HC2006]_, if
          ``case`` = 0, 0 otherwise

        OUTPUT:

        A point `(x,y,z) \\in F(t)` of ``self``. Output is undefined when the
        input solubility certificate is incorrect.

        ALGORITHM:

        The algorithm used is the algorithm FindPoint in [HC2006]_, with
        a simplification from [Ack2016]_.

        EXAMPLES::

            sage: K.<t> = FractionField(QQ['t'])
            sage: C = Conic(K, [t^2 - 2, 2*t^3, -2*t^3 - 13*t^2 - 2*t + 18])
            sage: C.has_rational_point(point=True)  # indirect test                     # needs sage.libs.singular
            (True, (3 : (t + 1)/t : 1))

        Different solubility certificates give different points::

            sage: # needs sage.rings.number_field
            sage: K.<t> = PolynomialRing(QQ, 't')
            sage: C = Conic(K, [t^2 - 2, 2*t, -2*t^3 - 13*t^2 - 2*t + 18])
            sage: supp = [[t^2 - 2], [t], [t^3 + 13/2*t^2 + t - 9]]
            sage: tbar1 = QQ.extension(supp[0][0], 'tbar').gens()[0]
            sage: tbar2 = QQ.extension(supp[1][0], 'tbar').gens()[0]
            sage: tbar3 = QQ.extension(supp[2][0], 'tbar').gens()[0]
            sage: roots = [[tbar1 + 1], [1/3*tbar2^0], [2/3*tbar3^2 + 11/3*tbar3 - 3]]
            sage: C.find_point(supp, roots, 1)
            (3 : t + 1 : 1)
            sage: roots = [[-tbar1 - 1], [-1/3*tbar2^0], [-2/3*tbar3^2 - 11/3*tbar3 + 3]]
            sage: C.find_point(supp, roots, 1)
            (3 : -t - 1 : 1)
        """
