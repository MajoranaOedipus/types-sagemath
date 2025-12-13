from .con_field import ProjectiveConic_field as ProjectiveConic_field
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import RationalField as RationalField

class ProjectiveConic_number_field(ProjectiveConic_field):
    """
    Create a projective plane conic curve over a number field.
    See ``Conic`` for full documentation.

    EXAMPLES::

        sage: K.<a> = NumberField(x^3 - 2, 'a')
        sage: P.<X, Y, Z> = K[]
        sage: Conic(X^2 + Y^2 - a*Z^2)
        Projective Conic Curve over Number Field in a with defining polynomial x^3 - 2
         defined by X^2 + Y^2 + (-a)*Z^2

    TESTS::

        sage: K.<a> = NumberField(x^3 - 3, 'a')
        sage: Conic([a, 1, -1])._test_pickling()
    """
    def __init__(self, A, f) -> None:
        """
        See ``Conic`` for full documentation.

        EXAMPLES::

            sage: Conic([1, 1, 1])
            Projective Conic Curve over Rational Field defined by x^2 + y^2 + z^2
        """
    def has_rational_point(self, point: bool = False, obstruction: bool = False, algorithm: str = 'default', read_cache: bool = True):
        """
        Return ``True`` if and only if ``self`` has a point
        defined over its base field `B`.

        If ``point`` and ``obstruction`` are both False (default),
        then the output is a boolean ``out`` saying whether ``self``
        has a rational point.

        If ``point`` or ``obstruction`` is ``True``, then the output is
        a pair ``(out, S)``, where ``out`` is as above and:

        - if ``point`` is ``True`` and ``self`` has a rational point,
          then ``S`` is a rational point,

        - if ``obstruction`` is ``True``, ``self`` has no rational point,
          then ``S`` is a prime or infinite place of `B` such that no
          rational point exists over the completion at ``S``.

        Points and obstructions are cached whenever they are found.
        Cached information is used for the output if available, but only
        if ``read_cache`` is ``True``.

        ALGORITHM:

        The parameter ``algorithm``
        specifies the algorithm to be used:

        - ``'rnfisnorm'`` -- use PARI's ``rnfisnorm``
          (cannot be combined with ``obstruction = True``)

        - ``'local'`` -- check if a local solution exists for all primes
          and infinite places of `B` and apply the Hasse principle
          (cannot be combined with ``point = True``)

        - ``'default'`` -- use algorithm ``'rnfisnorm'`` first.
          Then, if no point exists and obstructions are requested, use
          algorithm ``'local'`` to find an obstruction.

        - ``'magma'`` (requires Magma to be installed) --
          delegates the task to the Magma computer algebra
          system

        EXAMPLES:

        An example over `\\QQ` ::

            sage: C = Conic(QQ, [1, 113922743, -310146482690273725409])
            sage: C.has_rational_point(point=True)
            (True, (-76842858034579/5424 : -5316144401/5424 : 1))
            sage: C.has_rational_point(algorithm='local', read_cache=False)
            True

        Examples over number fields::

            sage: K.<i> = QuadraticField(-1)
            sage: C = Conic(K, [1, 3, -5])
            sage: C.has_rational_point(point=True, obstruction=True)
            (False, Fractional ideal (2*i - 1))
            sage: C.has_rational_point(algorithm='rnfisnorm')
            False
            sage: C.has_rational_point(algorithm='rnfisnorm', obstruction=True,
            ....:                      read_cache=False)
            Traceback (most recent call last):
            ...
            ValueError: Algorithm rnfisnorm cannot be combined with
            obstruction = True in has_rational_point

            sage: P.<x> = QQ[]
            sage: L.<b> = NumberField(x^3 - 5)
            sage: C = Conic(L, [1, 2, -3])
            sage: C.has_rational_point(point=True, algorithm='rnfisnorm')
            (True, (-5/3 : 1/3 : 1))

            sage: K.<a> = NumberField(x^4+2)
            sage: Conic(QQ, [4,5,6]).has_rational_point()
            False
            sage: Conic(K, [4,5,6]).has_rational_point()
            True
            sage: Conic(K, [4,5,6]).has_rational_point(algorithm='magma',   # optional - magma
            ....:                                      read_cache=False)
            True

            sage: P.<a> = QuadraticField(2)
            sage: C = Conic(P, [1,1,1])
            sage: C.has_rational_point()
            False
            sage: C.has_rational_point(point=True)
            (False, None)
            sage: C.has_rational_point(obstruction=True)
            (False,
             Ring morphism:
               From: Number Field in a with defining polynomial x^2 - 2
                     with a = 1.414213562373095?
               To:   Algebraic Real Field
               Defn: a |--> -1.414213562373095?)
            sage: C.has_rational_point(point=True, obstruction=True)
            (False,
             Ring morphism:
               From: Number Field in a with defining polynomial x^2 - 2
                     with a = 1.414213562373095?
               To:   Algebraic Real Field
               Defn: a |--> -1.414213562373095?)

        TESTS:

        Create a bunch of conics over number fields and check whether
        ``has_rational_point`` runs without errors for algorithms
        ``'rnfisnorm'`` and ``'local'``. Check if all points returned are
        valid. If Magma is available, then also check if the output agrees with
        Magma. ::

            sage: P.<X> = QQ[]
            sage: Q = P.fraction_field()
            sage: c = [1, X/2, 1/X]
            sage: l = Sequence(cartesian_product_iterator([c for i in range(3)]))
            sage: l = l + [[X, 1, 1, 1, 1, 1]] + [[X, 1/5, 1, 1, 2, 1]]
            sage: K.<a> = QuadraticField(-23)
            sage: L.<b> = QuadraticField(19)
            sage: M.<c> = NumberField(X^3+3*X+1)
            sage: m = [[Q(b)(F.gen()) for b in a] for a in l for F in [K, L, M]]
            sage: d = []
            sage: c = []
            sage: c = [Conic(a) for a in m if a != [0,0,0]]
            sage: d = [C.has_rational_point(algorithm='rnfisnorm', point=True) for C in c] # long time: 3.3 seconds
            sage: all(c[k].defining_polynomial()(Sequence(d[k][1])) == 0 for k in range(len(d)) if d[k][0])
            True
            sage: [C.has_rational_point(algorithm='local', read_cache=False) for C in c] == [o[0] for o in d] # long time: 5 seconds
            True
            sage: [C.has_rational_point(algorithm='magma', read_cache=False) for C in c] == [o[0] for o in d] # long time: 3 seconds, optional - magma
            True

        Create a bunch of conics that are known to have rational points
        already over `\\QQ` and check if points are found by
        ``has_rational_point``. ::

            sage: l = Sequence(cartesian_product_iterator([[-1, 0, 1] for i in range(3)]))
            sage: K.<a> = QuadraticField(-23)
            sage: L.<b> = QuadraticField(19)
            sage: M.<c> = NumberField(x^5+3*x+1)
            sage: m = [[F(b) for b in a] for a in l for F in [K, L, M]]
            sage: c = [Conic(a) for a in m if a != [0,0,0] and a != [1,1,1] and a != [-1,-1,-1]]
            sage: assert all(C.has_rational_point(algorithm='rnfisnorm') for C in c)
            sage: assert all(C.defining_polynomial()(Sequence(C.has_rational_point(point=True)[1])) == 0 for C in c)
            sage: assert all(C.has_rational_point(algorithm='local', read_cache=False) for C in c) # long time: 1 second
        """
    def is_locally_solvable(self, p):
        """
        Return ``True`` if and only if ``self`` has a solution over the
        completion of the base field `B` of ``self`` at ``p``. Here ``p``
        is a finite prime or infinite place of `B`.

        EXAMPLES::

            sage: P.<x> = QQ[]
            sage: K.<a> = NumberField(x^3 + 5)
            sage: C = Conic(K, [1, 2, 3 - a])
            sage: [p1, p2] = K.places()
            sage: C.is_locally_solvable(p1)
            False

            sage: C.is_locally_solvable(p2)
            True

            sage: f = (2*K).factor()
            sage: C.is_locally_solvable(f[0][0])
            True

            sage: C.is_locally_solvable(f[1][0])
            False
        """
    def local_obstructions(self, finite: bool = True, infinite: bool = True, read_cache: bool = True):
        """
        Return the sequence of finite primes and/or infinite places
        such that ``self`` is locally solvable at those primes and places.

        If the base field is `\\QQ`, then the infinite place is denoted `-1`.

        The parameters ``finite`` and ``infinite`` (both ``True`` by default) are
        used to specify whether to look at finite and/or infinite places.
        Note that ``finite = True`` involves factorization of the determinant
        of ``self``, hence may be slow.

        Local obstructions are cached. The parameter ``read_cache``
        specifies whether to look at the cache before computing anything.

        EXAMPLES::

            sage: K.<i> = QuadraticField(-1)
            sage: Conic(K, [1, 2, 3]).local_obstructions()
            []

            sage: L.<a> = QuadraticField(5)
            sage: Conic(L, [1, 2, 3]).local_obstructions()
            [Ring morphism:
               From: Number Field in a with defining polynomial x^2 - 5
                     with a = 2.236067977499790?
               To:   Algebraic Real Field
               Defn: a |--> -2.236067977499790?,
             Ring morphism:
               From: Number Field in a with defining polynomial x^2 - 5
                     with a = 2.236067977499790?
               To:   Algebraic Real Field
               Defn: a |--> 2.236067977499790?]
        """
