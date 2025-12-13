from .set import Set_add_sub_operators as Set_add_sub_operators, Set_base as Set_base, Set_boolean_operators as Set_boolean_operators
from collections.abc import Iterator
from sage.categories.enumerated_sets import EnumeratedSets as EnumeratedSets
from sage.categories.map import Map as Map
from sage.categories.poor_man_map import PoorManMap as PoorManMap
from sage.categories.sets_cat import Sets as Sets
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.infinity import Infinity as Infinity
from sage.rings.integer import Integer as Integer
from sage.structure.element import Expression as Expression
from sage.structure.parent import Parent as Parent

class ImageSubobject(Parent):
    """
    The subset defined as the image of another set under a fixed map.

    Let `f: X \\to Y` be a function. Then the image of `f` is defined as

    .. MATH::

        \\{ f(x) | x \\in X \\} \\subseteq Y.

    INPUT:

    - ``map`` -- a function

    - ``domain_subset`` -- the set `X`; optional if `f` has a domain

    - ``is_injective`` -- whether the ``map`` is injective:
      - ``None`` (default): infer from ``map`` or default to ``False``
      - ``False``: do not assume that ``map`` is injective
      - ``True``: ``map`` is known to be injective
      - ``'check'``: raise an error when ``map`` is not injective

    - ``inverse`` -- function (optional); a map from `f(X)` to `X`;
      if ``map.inverse_image`` exists, it is not recommended to provide this
      as it will be used automatically

    EXAMPLES::

        sage: import itertools
        sage: from sage.sets.image_set import ImageSubobject
        sage: D = ZZ
        sage: I = ImageSubobject(abs, ZZ, is_injective='check')
        sage: list(itertools.islice(I, 10))
        Traceback (most recent call last):
        ...
        ValueError: The map <built-in function abs> from Integer Ring is not injective: 1
    """
    def __init__(self, map, domain_subset, *, category=None, is_injective=None, inverse=None) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: # needs sage.modules
            sage: M = CombinatorialFreeModule(ZZ, [0,1,2,3])
            sage: R.<x,y> = QQ[]
            sage: H = Hom(M, R, category=Sets())
            sage: f = H(lambda v: v[0]*x + v[1]*(x^2-y) + v[2]^2*(y+2) + v[3] - v[0]^2)
            sage: Im = f.image()
            sage: TestSuite(Im).run(skip=['_test_an_element', '_test_pickling',
            ....:                         '_test_some_elements', '_test_elements'])

        TESTS:

        Implementing ``inverse_image`` automatically makes :meth:`__contains__` work::

            sage: R.<x> = QQ[]
            sage: S.<y> = QQ[]
            sage: R.hom([y^2]).inverse_image(y^4)
            x^2
            sage: y^4 in R.hom([y^2]).image()
            True
        """
    def __eq__(self, other):
        """
        EXAMPLES::

            sage: from sage.sets.image_set import ImageSubobject
            sage: D = ZZ
            sage: def f(x):
            ....:     return 2 * x
            sage: I = ImageSubobject(f, ZZ)
            sage: I == ImageSubobject(f, ZZ)
            True

        This method does not take into account whether an inverse is provided,
        injectivity is declared, or the category::

            sage: def f_inv(y):
            ....:     return y // 2
            sage: I == ImageSubobject(f, ZZ, inverse=f_inv)
            True
            sage: I == ImageSubobject(f, ZZ, is_injective=True)
            True
            sage: I.category()
            Category of enumerated subobjects of sets
            sage: I == ImageSubobject(f, ZZ, category=EnumeratedSets().Infinite())
            True
        """
    def __ne__(self, other):
        """
        EXAMPLES::

            sage: from sage.sets.image_set import ImageSubobject
            sage: D = ZZ
            sage: def f(x):
            ....:     return 2 * x
            sage: I = ImageSubobject(f, ZZ)
            sage: I != ImageSubobject(f, QQ)
            True
        """
    def __hash__(self):
        """
        TESTS::

            sage: from sage.sets.image_set import ImageSubobject
            sage: def f(x):
            ....:     return 2 * x
            sage: I = ImageSubobject(f, ZZ)
            sage: hash(I) == hash(ImageSubobject(f, ZZ))
            True
        """
    def ambient(self):
        """
        Return the ambient set of ``self``, which is the codomain of
        the defining map.

        EXAMPLES::

            sage: # needs sage.modules
            sage: M = CombinatorialFreeModule(QQ, [0, 1, 2, 3])
            sage: R.<x,y> = ZZ[]
            sage: H = Hom(M, R, category=Sets())
            sage: f = H(lambda v: floor(v[0])*x + ceil(v[3] - v[0]^2))
            sage: Im = f.image()
            sage: Im.ambient() is R
            True

            sage: P = Partitions(3).map(attrcall('conjugate'))                          # needs sage.combinat
            sage: P.ambient() is None                                                   # needs sage.combinat
            True

            sage: R = Permutations(10).map(attrcall('reduced_word'))
            sage: R.ambient() is None
            True
        """
    def lift(self, x):
        """
        Return the lift ``x`` to the ambient space, which is ``x``.

        EXAMPLES::

            sage: # needs sage.modules
            sage: M = CombinatorialFreeModule(QQ, [0, 1, 2, 3])
            sage: R.<x,y> = ZZ[]
            sage: H = Hom(M, R, category=Sets())
            sage: f = H(lambda v: floor(v[0])*x + ceil(v[3] - v[0]^2))
            sage: Im = f.image()
            sage: p = Im.lift(Im.an_element()); p
            2*x - 4
            sage: p.parent() is R
            True
        """
    def retract(self, x):
        """
        Return the retract of ``x`` from the ambient space, which is ``x``.

        .. WARNING::

            This does not check that ``x`` is actually in the image.

        EXAMPLES::

            sage: # needs sage.modules
            sage: M = CombinatorialFreeModule(QQ, [0, 1, 2, 3])
            sage: R.<x,y> = ZZ[]
            sage: H = Hom(M, R, category=Sets())
            sage: f = H(lambda v: floor(v[0])*x + ceil(v[3] - v[0]^2))
            sage: Im = f.image()
            sage: p = 2 * x - 4
            sage: Im.retract(p).parent()
            Multivariate Polynomial Ring in x, y over Integer Ring
        """
    @cached_method
    def cardinality(self) -> Integer:
        """
        Return the cardinality of ``self``.

        EXAMPLES:

        Injective case (note that
        :meth:`~sage.categories.enumerated_sets.EnumeratedSets.ParentMethods.map`
        defaults to ``is_injective=True``):

            sage: R = Permutations(10).map(attrcall('reduced_word'))
            sage: R.cardinality()
            3628800

            sage: Evens = ZZ.map(lambda x: 2 * x)
            sage: Evens.cardinality()
            +Infinity

        Non-injective case::

            sage: Z7 = Set(range(7))
            sage: from sage.sets.image_set import ImageSet
            sage: Z4711 = ImageSet(lambda x: x**4 % 11, Z7, is_injective=False)
            sage: Z4711.cardinality()
            6

            sage: Squares = ImageSet(lambda x: x^2, ZZ, is_injective=False,
            ....:                    category=Sets().Infinite())
            sage: Squares.cardinality()
            +Infinity

            sage: Mod2 = ZZ.map(lambda x: x % 2, is_injective=False)
            sage: Mod2.cardinality()
            Traceback (most recent call last):
            ...
            NotImplementedError: cannot determine cardinality of a
            non-injective image of an infinite set
        """
    def __iter__(self) -> Iterator:
        """
        Return an iterator over the elements of ``self``.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = Partitions()
            sage: H = Hom(P, ZZ)
            sage: f = H(ZZ.sum)
            sage: X = f.image()
            sage: it = iter(X)
            sage: [next(it) for _ in range(5)]
            [0, 1, 2, 3, 4]
        """

class ImageSet(ImageSubobject, Set_base, Set_add_sub_operators, Set_boolean_operators):
    """
    Image of a set by a map.

    EXAMPLES::

        sage: from sage.sets.image_set import ImageSet

    Symbolics::

        sage: ImageSet(sin, RealSet.open(0, pi/4))                                      # needs sage.symbolic
        Image of (0, 1/4*pi) by The map sin from (0, 1/4*pi)
        sage: _.an_element()                                                            # needs sage.symbolic
        1/2*sqrt(-sqrt(2) + 2)

        sage: # needs sage.symbolic
        sage: sos(x,y) = x^2 + y^2; sos
        (x, y) |--> x^2 + y^2
        sage: ImageSet(sos, ZZ^2)
        Image of
         Ambient free module of rank 2 over the principal ideal domain Integer Ring by
         The map (x, y) |--> x^2 + y^2 from Vector space of dimension 2 over Symbolic Ring
        sage: _.an_element()
        1
        sage: ImageSet(sos, Set([(3, 4), (3, -4)]))
        Image of {...(3, -4)...} by
         The map (x, y) |--> x^2 + y^2 from Vector space of dimension 2 over Symbolic Ring
        sage: _.an_element()
        25
    """
