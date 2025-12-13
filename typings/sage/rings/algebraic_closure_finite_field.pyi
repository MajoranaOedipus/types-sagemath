from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.fast_methods import WithEqualityById as WithEqualityById
from sage.rings.finite_rings.finite_field_base import FiniteField as FiniteField
from sage.rings.ring import Field as Field
from sage.sets.family import AbstractFamily as AbstractFamily
from sage.structure.element import Element as Element, FieldElement as FieldElement
from sage.structure.richcmp import richcmp as richcmp

class AlgebraicClosureFiniteFieldElement(FieldElement):
    """
    Element of an algebraic closure of a finite field.

    EXAMPLES::

        sage: F = GF(3).algebraic_closure()
        sage: F.gen(2)
        z2
        sage: type(F.gen(2))
        <class 'sage.rings.algebraic_closure_finite_field.AlgebraicClosureFiniteField_pseudo_conway_with_category.element_class'>
    """
    def __init__(self, parent, value) -> None:
        """
        TESTS::

            sage: F = GF(3).algebraic_closure()
            sage: TestSuite(F.gen(2)).run(skip=['_test_pickling'])

        .. NOTE::

            The ``_test_pickling`` test has to be skipped because
            there is no coercion map between the parents of ``x``
            and ``loads(dumps(x))``.
        """
    def __hash__(self):
        """
        TESTS::

            sage: F = GF(2).algebraic_closure()
            sage: hash(F.zero())
            0
            sage: hash(F.one())
            1
            sage: z1 = F.gen(1)
            sage: z2 = F.gen(2)
            sage: z3 = F.gen(3)
            sage: z4 = F.gen(4)

            sage: hash(z2) == hash(z3+z2-z3)
            True
            sage: hash(F.zero()) == hash(z3+z2-z3-z2)
            True

            sage: X = [z4**i for i in range(2**4-1)]
            sage: X.append(F.zero())
            sage: X.extend([z3, z3**2, z3*z4])
            sage: assert len(X) == len(set(hash(x) for x in X))

            sage: F = GF(3).algebraic_closure()
            sage: z1 = F.gen(1)
            sage: z2 = F.gen(2)
            sage: z3 = F.gen(3)
            sage: z4 = F.gen(4)

            sage: hash(z2) == hash(z3+z2-z3)
            True

            sage: X = [z4**i for i in range(3**4-1)]
            sage: X.append(F.zero())
            sage: X.extend([z3, z3**2, z3*z4])
            sage: assert len(X) == len(set(hash(x) for x in X))

        Check that :issue:`19956` is fixed::

            sage: R.<x,y> = GF(2).algebraic_closure()[]
            sage: x.resultant(y)
            y
        """
    def __pow__(self, exp):
        """
        TESTS::

            sage: F2 = GF(2).algebraic_closure()
            sage: z12 = F2.gen(3*4)
            sage: z12**3
            z12^3
            sage: z12**13
            z12^8 + z12^7 + z12^6 + z12^4 + z12^2 + z12
        """
    def change_level(self, n):
        """
        Return a representation of ``self`` as an element of the
        subfield of degree `n` of the parent, if possible.

        EXAMPLES::

            sage: F = GF(3).algebraic_closure()
            sage: z = F.gen(4)
            sage: (z^10).change_level(6)
            2*z6^5 + 2*z6^3 + z6^2 + 2*z6 + 2
            sage: z.change_level(6)
            Traceback (most recent call last):
            ...
            ValueError: z4 is not in the image of Ring morphism:
              From: Finite Field in z2 of size 3^2
              To:   Finite Field in z4 of size 3^4
              Defn: z2 |--> 2*z4^3 + 2*z4^2 + 1

            sage: a = F(1).change_level(3); a
            1
            sage: a.change_level(2)
            1
            sage: F.gen(3).change_level(1)
            Traceback (most recent call last):
            ...
            ValueError: z3 is not in the image of Ring morphism:
              From: Finite Field of size 3
              To:   Finite Field in z3 of size 3^3
              Defn: 1 |--> 1
        """
    def minpoly(self):
        """
        Return the minimal polynomial of ``self`` over the prime
        field.

        EXAMPLES::

            sage: F = GF(11).algebraic_closure()
            sage: F.gen(3).minpoly()
            x^3 + 2*x + 9
        """
    minimal_polynomial = minpoly
    def is_square(self):
        """
        Return ``True`` if ``self`` is a square.

        This always returns ``True``.

        EXAMPLES::

            sage: F = GF(3).algebraic_closure()
            sage: F.gen(2).is_square()
            True
        """
    def sqrt(self, all: bool = False):
        """
        Return a square root of ``self``.

        If the optional keyword argument ``all`` is set to ``True``,
        return a list of all square roots of ``self`` instead.

        EXAMPLES::

            sage: F = GF(3).algebraic_closure()
            sage: F.gen(2).sqrt()
            z4^3 + z4 + 1
            sage: F.gen(2).sqrt(all=True)
            [z4^3 + z4 + 1, 2*z4^3 + 2*z4 + 2]
            sage: (F.gen(2)^2).sqrt()
            z2
            sage: (F.gen(2)^2).sqrt(all=True)
            [z2, 2*z2]
        """
    def nth_root(self, n):
        """
        Return an `n`-th root of ``self``.

        EXAMPLES::

            sage: F = GF(5).algebraic_closure()
            sage: t = F.gen(2) + 1
            sage: s = t.nth_root(15); s
            4*z6^5 + 3*z6^4 + 2*z6^3 + 2*z6^2 + 4
            sage: s**15 == t
            True

        .. TODO::

            This function could probably be made faster.
        """
    def multiplicative_order(self):
        """
        Return the multiplicative order of ``self``.

        EXAMPLES::

            sage: K = GF(7).algebraic_closure()
            sage: K.gen(5).multiplicative_order()
            16806
            sage: (K.gen(1) + K.gen(2) + K.gen(3)).multiplicative_order()
            7353
        """
    def pth_power(self, k: int = 1):
        """
        Return the `p^k`-th power of ``self``, where `p` is the
        characteristic of ``self.parent()``.

        EXAMPLES::

            sage: K = GF(13).algebraic_closure('t')
            sage: t3 = K.gen(3)
            sage: s = 1 + t3 + t3**2
            sage: s.pth_power()
            10*t3^2 + 6*t3
            sage: s.pth_power(2)
            2*t3^2 + 6*t3 + 11
            sage: s.pth_power(3)
            t3^2 + t3 + 1
            sage: s.pth_power(3).parent() is K
            True
        """
    def pth_root(self, k: int = 1):
        """
        Return the unique `p^k`-th root of ``self``, where `p` is the
        characteristic of ``self.parent()``.

        EXAMPLES::

            sage: K = GF(13).algebraic_closure('t')
            sage: t3 = K.gen(3)
            sage: s = 1 + t3 + t3**2
            sage: s.pth_root()
            2*t3^2 + 6*t3 + 11
            sage: s.pth_root(2)
            10*t3^2 + 6*t3
            sage: s.pth_root(3)
            t3^2 + t3 + 1
            sage: s.pth_root(2).parent() is K
            True
        """
    def as_finite_field_element(self, minimal: bool = False):
        """
        Return ``self`` as a finite field element.

        INPUT:

        - ``minimal`` -- boolean (default: ``False``); if ``True``,
          always return the smallest subfield containing ``self``

        OUTPUT:

        - a triple (``field``, ``element``, ``morphism``) where
          ``field`` is a finite field, ``element`` an element of
          ``field`` and ``morphism`` a morphism from ``field`` to
          ``self.parent()``.

        EXAMPLES::

            sage: F = GF(3).algebraic_closure('t')
            sage: t = F.gen(5)
            sage: t.as_finite_field_element()
            (Finite Field in t5 of size 3^5,
             t5,
             Ring morphism:
              From: Finite Field in t5 of size 3^5
              To:   Algebraic closure of Finite Field of size 3
              Defn: t5 |--> t5)

        By default, ``field`` is not necessarily minimal.  We can
        force it to be minimal using the ``minimal`` option::

            sage: s = t + 1 - t
            sage: s.as_finite_field_element()[0]
            Finite Field in t5 of size 3^5
            sage: s.as_finite_field_element(minimal=True)[0]
            Finite Field of size 3

        This also works when the element has to be converted between
        two non-trivial finite subfields (see :issue:`16509`)::

            sage: K = GF(5).algebraic_closure()
            sage: z = K.gen(5) - K.gen(5) + K.gen(2)
            sage: z.as_finite_field_element(minimal=True)
            (Finite Field in z2 of size 5^2, z2, Ring morphism:
               From: Finite Field in z2 of size 5^2
               To:   Algebraic closure of Finite Field of size 5
               Defn: z2 |--> z2)

        There are automatic coercions between the various
        subfields::

            sage: a = K.gen(2) + 1
            sage: _,b,_ = a.as_finite_field_element()
            sage: K4 = K.subfield(4)[0]
            sage: K4(b)
            z4^3 + z4^2 + z4 + 4
            sage: b.minimal_polynomial() == K4(b).minimal_polynomial()
            True
            sage: K(K4(b)) == K(b)
            True

        You can also use the inclusions that are implemented at
        the level of the algebraic closure::

            sage: f = K.inclusion(2,4); f
            Ring morphism:
              From: Finite Field in z2 of size 5^2
              To:   Finite Field in z4 of size 5^4
              Defn: z2 |--> z4^3 + z4^2 + z4 + 3
            sage: f(b)
            z4^3 + z4^2 + z4 + 4
        """

class AlgebraicClosureFiniteField_generic(Field):
    """
    Algebraic closure of a finite field.

    TESTS::

        sage: GF(3).algebraic_closure().cardinality()
        +Infinity

        sage: GF(3).algebraic_closure().is_finite()
        False
    """
    def __init__(self, base_ring, name, category=None) -> None:
        """
        TESTS::

            sage: from sage.rings.algebraic_closure_finite_field import AlgebraicClosureFiniteField_generic
            sage: F = AlgebraicClosureFiniteField_generic(GF(5), 'z')
            sage: F
            Algebraic closure of Finite Field of size 5
        """
    def __eq__(self, other):
        """
        Compare ``self`` with ``other``.

        TESTS::

            sage: F3 = GF(3).algebraic_closure()
            sage: F3 == F3
            True
            sage: F5 = GF(5).algebraic_closure()
            sage: F3 == F5
            False
        """
    def __ne__(self, other):
        """
        Check whether ``self`` and ``other`` are not equal.

        TESTS::

            sage: F3 = GF(3).algebraic_closure()
            sage: F3 != F3
            False
            sage: F5 = GF(5).algebraic_closure()
            sage: F3 != F5
            True
        """
    def characteristic(self):
        """
        Return the characteristic of ``self``.

        EXAMPLES::

            sage: from sage.rings.algebraic_closure_finite_field import AlgebraicClosureFiniteField
            sage: p = next_prime(1000)
            sage: F = AlgebraicClosureFiniteField(GF(p), 'z')
            sage: F.characteristic() == p
            True
        """
    Element = AlgebraicClosureFiniteFieldElement
    def subfield(self, n):
        """
        Return the unique subfield of degree `n` of ``self``
        together with its canonical embedding into ``self``.

        EXAMPLES::

            sage: F = GF(3).algebraic_closure()
            sage: F.subfield(1)
            (Finite Field of size 3,
             Ring morphism:
               From: Finite Field of size 3
               To:   Algebraic closure of Finite Field of size 3
               Defn: 1 |--> 1)
            sage: F.subfield(4)
            (Finite Field in z4 of size 3^4,
             Ring morphism:
               From: Finite Field in z4 of size 3^4
               To:   Algebraic closure of Finite Field of size 3
               Defn: z4 |--> z4)
        """
    def inclusion(self, m, n):
        """
        Return the canonical inclusion map from the subfield
        of degree `m` to the subfield of degree `n`.

        EXAMPLES::

            sage: F = GF(3).algebraic_closure()
            sage: F.inclusion(1, 2)
            Ring morphism:
              From: Finite Field of size 3
              To:   Finite Field in z2 of size 3^2
              Defn: 1 |--> 1
            sage: F.inclusion(2, 4)
            Ring morphism:
              From: Finite Field in z2 of size 3^2
              To:   Finite Field in z4 of size 3^4
              Defn: z2 |--> 2*z4^3 + 2*z4^2 + 1
        """
    def ngens(self):
        """
        Return the number of generators of ``self``, which is
        infinity.

        EXAMPLES::

            sage: from sage.rings.algebraic_closure_finite_field import AlgebraicClosureFiniteField
            sage: AlgebraicClosureFiniteField(GF(5), 'z').ngens()
            +Infinity
        """
    def gen(self, n):
        """
        Return the `n`-th generator of ``self``.

        EXAMPLES::

            sage: from sage.rings.algebraic_closure_finite_field import AlgebraicClosureFiniteField
            sage: F = AlgebraicClosureFiniteField(GF(5), 'z')
            sage: F.gen(2)
            z2
        """
    def gens(self) -> AbstractFamily:
        """
        Return a family of generators of ``self``.

        OUTPUT:

        - a :class:`~sage.sets.family.Family`, indexed by the positive
          integers, whose `n`-th element is ``self.gen(n)``.

        EXAMPLES::

            sage: from sage.rings.algebraic_closure_finite_field import AlgebraicClosureFiniteField
            sage: F = AlgebraicClosureFiniteField(GF(5), 'z')
            sage: g = F.gens(); g
            Lazy family (...(i))_{i in Positive integers}
            sage: g[3]
            z3
        """
    def algebraic_closure(self):
        """
        Return an algebraic closure of ``self``.

        This always returns ``self``.

        EXAMPLES::

            sage: from sage.rings.algebraic_closure_finite_field import AlgebraicClosureFiniteField
            sage: F = AlgebraicClosureFiniteField(GF(5), 'z')
            sage: F.algebraic_closure() is F
            True
        """
    def some_elements(self):
        """
        Return some elements of this field.

        EXAMPLES::

            sage: F = GF(7).algebraic_closure()
            sage: F.some_elements()
            (1, z2, z3 + 1)
        """

class AlgebraicClosureFiniteField_pseudo_conway(WithEqualityById, AlgebraicClosureFiniteField_generic):
    """
    Algebraic closure of a finite field, constructed using
    pseudo-Conway polynomials.

    EXAMPLES::

        sage: F = GF(5).algebraic_closure(implementation='pseudo_conway')
        sage: F.cardinality()
        +Infinity
        sage: F.algebraic_closure() is F
        True
        sage: x = F(3).nth_root(12); x
        z4^3 + z4^2 + 4*z4
        sage: x**12
        3

    TESTS::

        sage: F3 = GF(3).algebraic_closure()
        sage: F3 == F3
        True
        sage: F5 = GF(5).algebraic_closure()
        sage: F3 == F5
        False
    """
    def __init__(self, base_ring, name, category=None, lattice=None, use_database: bool = True) -> None:
        """
        INPUT:

        - ``base_ring`` -- the finite field of which to construct an
          algebraic closure.  Currently only prime fields are
          accepted.

        - ``name`` -- prefix to use for generators of the finite
          subfields

        - ``category`` -- if provided, specifies the category in which
          this algebraic closure will be placed

        - ``lattice`` -- :class:`~sage.rings.finite_rings.conway_polynomials.PseudoConwayPolynomialLattice`
          (default: ``None``); if provided, use this pseudo-Conway
          polynomial lattice to construct an algebraic closure.

        - ``use_database`` -- boolean.  If ``True`` (default), use actual
          Conway polynomials whenever they are available in the
          database.  If ``False``, always compute pseudo-Conway
          polynomials from scratch.

        TESTS::

            sage: F = GF(5).algebraic_closure(implementation='pseudo_conway')
            sage: print(F.__class__.__name__)
            AlgebraicClosureFiniteField_pseudo_conway_with_category
            sage: TestSuite(F).run(skip=['_test_elements', '_test_pickling'])

            sage: from sage.rings.finite_rings.conway_polynomials import PseudoConwayLattice
            sage: L = PseudoConwayLattice(11, use_database=False)
            sage: F = GF(7).algebraic_closure(lattice=L)
            Traceback (most recent call last):
            ...
            TypeError: lattice must be a pseudo-Conway lattice with characteristic 7
            sage: F = GF(11).algebraic_closure(lattice=L)
            sage: F.gen(2).minimal_polynomial()
            x^2 + 4*x + 2

            sage: F = GF(11).algebraic_closure(use_database=True)
            sage: F.gen(2).minimal_polynomial()
            x^2 + 7*x + 2

        .. NOTE::

            In the test suite, ``_test_pickling`` has to be skipped
            because ``F`` and ``loads(dumps(F))`` cannot consistently
            be made to compare equal, and ``_test_elements`` has to be
            skipped for the reason described in
            :meth:`AlgebraicClosureFiniteFieldElement.__init__`.
        """

def AlgebraicClosureFiniteField(base_ring, name, category=None, implementation=None, **kwds):
    """
    Construct an algebraic closure of a finite field.

    The recommended way to use this functionality is by calling the
    :meth:`~sage.rings.finite_rings.finite_field_base.FiniteField.algebraic_closure`
    method of the finite field.

    .. NOTE::

        Algebraic closures of finite fields in Sage do not have the
        unique representation property, because they are not
        determined up to unique isomorphism by their defining data.

    EXAMPLES::

        sage: from sage.rings.algebraic_closure_finite_field import AlgebraicClosureFiniteField
        sage: F = GF(2).algebraic_closure()
        sage: F1 = AlgebraicClosureFiniteField(GF(2), 'z')
        sage: F1 is F
        False

    In the pseudo-Conway implementation, non-identical instances never
    compare equal::

        sage: F1 == F
        False
        sage: loads(dumps(F)) == F
        False

    This is to ensure that the result of comparing two instances
    cannot change with time.
    """
