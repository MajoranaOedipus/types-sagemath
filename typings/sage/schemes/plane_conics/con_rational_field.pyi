from .con_number_field import ProjectiveConic_number_field as ProjectiveConic_number_field
from sage.arith.functions import lcm as lcm
from sage.arith.misc import hilbert_symbol as hilbert_symbol
from sage.matrix.constructor import Matrix as Matrix
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.schemes.projective.projective_space import ProjectiveSpace as ProjectiveSpace
from sage.structure.element import InfinityElement as InfinityElement
from sage.structure.sequence import Sequence as Sequence

class ProjectiveConic_rational_field(ProjectiveConic_number_field):
    """
    Create a projective plane conic curve over `\\QQ`.

    See ``Conic`` for full documentation.

    EXAMPLES::

        sage: P.<X, Y, Z> = QQ[]
        sage: Conic(X^2 + Y^2 - 3*Z^2)
        Projective Conic Curve over Rational Field defined by X^2 + Y^2 - 3*Z^2

    TESTS::

        sage: Conic([2, 1, -1])._test_pickling()
    """
    def __init__(self, A, f) -> None:
        """
        See ``Conic`` for full documentation.

        EXAMPLES::

            sage: Conic([1, 1, 1])
            Projective Conic Curve over Rational Field defined by x^2 + y^2 + z^2
        """
    def has_rational_point(self, point: bool = False, obstruction: bool = False, algorithm: str = 'default', read_cache: bool = True) -> bool:
        """
        Return ``True`` if and only if ``self`` has a point defined over `\\QQ`.

        If ``point`` and ``obstruction`` are both ``False`` (default), then
        the output is a boolean ``out`` saying whether ``self`` has a
        rational point.

        If ``point`` or ``obstruction`` is ``True``, then the output is
        a pair ``(out, S)``, where ``out`` is as above and the following
        holds:

        - if ``point`` is ``True`` and ``self`` has a rational point,
          then ``S`` is a rational point,

        - if ``obstruction`` is ``True`` and ``self`` has no rational point,
          then ``S`` is a prime such that no rational point exists
          over the completion at ``S`` or `-1` if no point exists over `\\RR`.

        Points and obstructions are cached, whenever they are found.
        Cached information is used if and only if ``read_cache`` is ``True``.

        ALGORITHM:

        The parameter ``algorithm``
        specifies the algorithm to be used:

        - ``'qfsolve'`` -- use PARI/GP function :pari:`qfsolve`

        - ``'rnfisnorm'`` -- use PARI's function :pari:`rnfisnorm`
          (cannot be combined with ``obstruction = True``)

        - ``'local'`` -- check if a local solution exists for all primes
          and infinite places of `\\QQ` and apply the Hasse principle
          (cannot be combined with ``point = True``)

        - ``'default'`` -- use ``'qfsolve'``

        - ``'magma'`` (requires Magma to be installed) --
          delegates the task to the Magma computer algebra system.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: C = Conic(QQ, [1, 2, -3])
            sage: C.has_rational_point(point=True)
            (True, (1 : 1 : 1))
            sage: D = Conic(QQ, [1, 3, -5])
            sage: D.has_rational_point(point=True)
            (False, 3)
            sage: P.<X,Y,Z> = QQ[]
            sage: E = Curve(X^2 + Y^2 + Z^2); E
            Projective Conic Curve over Rational Field defined by X^2 + Y^2 + Z^2
            sage: E.has_rational_point(obstruction=True)
            (False, -1)

        The following would not terminate quickly with
        ``algorithm = 'rnfisnorm'`` ::

            sage: C = Conic(QQ, [1, 113922743, -310146482690273725409])
            sage: C.has_rational_point(point=True)                                      # needs sage.libs.pari
            (True, (-76842858034579/5424 : -5316144401/5424 : 1))
            sage: C.has_rational_point(algorithm='local', read_cache=False)
            True
            sage: C.has_rational_point(point=True, algorithm='magma',       # optional - magma
            ....:                      read_cache=False)
            (True, (30106379962113/7913 : 12747947692/7913 : 1))

        TESTS:

        Create a bunch of conics over `\\QQ`, check if ``has_rational_point`` runs without errors
        and returns consistent answers for all algorithms. Check if all points returned are valid. ::

            sage: # needs sage.libs.pari
            sage: l = Sequence(cartesian_product_iterator([[-1, 0, 1] for i in range(6)]))
            sage: c = [Conic(QQ, a) for a in l if a != [0,0,0] and a != (0,0,0,0,0,0)]
            sage: d = []
            sage: d = [[C] + [C.has_rational_point(algorithm=algorithm, read_cache=False,            # long time (7 s)
            ....:                                  obstruction=(algorithm != 'rnfisnorm'),
            ....:                                  point=(algorithm != 'local'))
            ....:             for algorithm in ['local', 'qfsolve', 'rnfisnorm']]
            ....:      for C in c[::10]]
            sage: assert all(e[1][0] == e[2][0] and e[1][0] == e[3][0] for e in d)
            sage: assert all(e[0].defining_polynomial()(Sequence(e[i][1])) == 0 for e in d for i in [2,3] if e[1][0])
        """
    def is_locally_solvable(self, p) -> bool:
        """
        Return ``True`` if and only if ``self`` has a solution over the
        `p`-adic numbers.

        Here `p` is a prime number or equals
        `-1`, infinity, or `\\RR` to denote the infinite place.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: C = Conic(QQ, [1,2,3])
            sage: C.is_locally_solvable(-1)
            False
            sage: C.is_locally_solvable(2)
            False
            sage: C.is_locally_solvable(3)
            True
            sage: C.is_locally_solvable(QQ.hom(RR))
            False
            sage: D = Conic(QQ, [1, 2, -3])
            sage: D.is_locally_solvable(infinity)
            True
            sage: D.is_locally_solvable(RR)
            True
        """
    def local_obstructions(self, finite: bool = True, infinite: bool = True, read_cache: bool = True):
        """
        Return the sequence of finite primes and/or infinite places
        such that ``self`` is locally solvable at those primes and places.

        The infinite place is denoted `-1`.

        The parameters ``finite`` and ``infinite`` (both ``True`` by
        default) are used to specify whether to look at finite and/or
        infinite places.

        Note that ``finite = True`` involves factorization of the determinant
        of ``self``, hence may be slow.

        Local obstructions are cached. The parameter ``read_cache`` specifies
        whether to look at the cache before computing anything.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: Conic(QQ, [1, 1, 1]).local_obstructions()
            [2, -1]
            sage: Conic(QQ, [1, 2, -3]).local_obstructions()
            []
            sage: Conic(QQ, [1, 2, 3, 4, 5, 6]).local_obstructions()
            [41, -1]
        """
    def parametrization(self, point=None, morphism: bool = True):
        """
        Return a parametrization `f` of ``self`` together with the
        inverse of `f`.

        If ``point`` is specified, then that point is used
        for the parametrization. Otherwise, use ``self.rational_point()``
        to find a point.

        If ``morphism`` is ``True``, then `f` is returned in the form
        of a Scheme morphism. Otherwise, it is a tuple of polynomials
        that gives the parametrization.

        ALGORITHM:

        Uses the PARI/GP function :pari:`qfparam`.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: c = Conic([1,1,-1])
            sage: c.parametrization()
            (Scheme morphism:
              From: Projective Space of dimension 1 over Rational Field
              To:   Projective Conic Curve over Rational Field defined by x^2 + y^2 - z^2
              Defn: Defined on coordinates by sending (x : y) to
                    (2*x*y : x^2 - y^2 : x^2 + y^2),
             Scheme morphism:
              From: Projective Conic Curve over Rational Field defined by x^2 + y^2 - z^2
              To:   Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x : y : z) to
                    (1/2*x : -1/2*y + 1/2*z))

        An example with ``morphism = False`` ::

            sage: # needs sage.libs.pari
            sage: R.<x,y,z> = QQ[]
            sage: C = Curve(7*x^2 + 2*y*z + z^2)
            sage: (p, i) = C.parametrization(morphism=False); (p, i)
            ([-2*x*y, x^2 + 7*y^2, -2*x^2], [-1/2*x, 1/7*y + 1/14*z])
            sage: C.defining_polynomial()(p)
            0
            sage: i[0](p) / i[1](p)
            x/y

        A :exc:`ValueError` is raised if ``self`` has no rational point ::

            sage: # needs sage.libs.pari
            sage: C = Conic(x^2 + 2*y^2 + z^2)
            sage: C.parametrization()
            Traceback (most recent call last):
            ...
            ValueError: Conic Projective Conic Curve over Rational Field defined
            by x^2 + 2*y^2 + z^2 has no rational points over Rational Field!

        A :exc:`ValueError` is raised if ``self`` is not smooth ::

            sage: # needs sage.libs.pari
            sage: C = Conic(x^2 + y^2)
            sage: C.parametrization()
            Traceback (most recent call last):
            ...
            ValueError: The conic self (=Projective Conic Curve over Rational Field defined
            by x^2 + y^2) is not smooth, hence does not have a parametrization.
        """
