from sage.arith.misc import random_prime as random_prime
from sage.categories.morphism import Morphism as Morphism
from sage.groups.additive_abelian.additive_abelian_wrapper import AdditiveAbelianGroupWrapper as AdditiveAbelianGroupWrapper
from sage.groups.generic import multiple as multiple, order_from_multiple as order_from_multiple
from sage.libs.pari import pari as pari
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.prandom import randrange as randrange
from sage.quadratic_forms.binary_qf import BinaryQF as BinaryQF
from sage.rings.finite_rings.integer_mod import Mod as Mod
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.element import AdditiveGroupElement as AdditiveGroupElement
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class BQFClassGroup(Parent, UniqueRepresentation):
    '''
    This type represents the class group for a given discriminant `D`.

    - For `D < 0`, the group is the class group of *positive definite*
      binary quadratic forms. The "full" form class group is the direct
      sum of two isomorphic copies of this group (one for positive
      definite forms and one for negative definite forms).

    - For `D > 0`, this functionality is currently not implemented.

    EXAMPLES::

        sage: BQFClassGroup(-4)
        Form Class Group of Discriminant -4
        sage: BQFClassGroup(-6)
        Traceback (most recent call last):
        ...
        ValueError: not a discriminant

    The discriminant need not be fundamental::

        sage: BQFClassGroup(-22^2)
        Form Class Group of Discriminant -484
    '''
    def __init__(self, D, *, check: bool = True) -> None:
        """
        Construct the class group for a given discriminant `D`.

        TESTS:

        Check that positive discriminants are rejected until code is
        written for them::

            sage: BQFClassGroup(101)
            Traceback (most recent call last):
            ...
            NotImplementedError: positive discriminants are not yet supported
        """
    def zero(self):
        """
        Return the neutral element of this group.

        This is the class of the principal binary quadratic form of
        the respective discriminant.

        EXAMPLES::

            sage: Cl = BQFClassGroup(-999)
            sage: cl = Cl.zero(); cl
            Class of x^2 + x*y + 250*y^2
            sage: cl + cl == cl
            True
        """
    def random_element(self):
        """
        Return a somewhat random element of this form class group.

        ALGORITHM:

        Sample random odd primes `a` until `b^2 = D \\pmod{4a}` has a
        solution `b \\in \\ZZ` and set `c = (b^2-D)/(4a)`. Flip a coin
        to choose the sign of `b`. Then return the class of `[a,b,c]`.

        .. NOTE::

            No strict guarantees are being made about the distribution of
            classes sampled by this function. Heuristically, however, it
            should be fairly close to uniform.

        EXAMPLES::

            sage: Cl = BQFClassGroup(-999); Cl
            Form Class Group of Discriminant -999
            sage: cl = Cl.random_element(); cl  # random
            Class of 10*x^2 + x*y + 25*y^2
            sage: cl.form().discriminant()
            -999
        """
    def __hash__(self) -> int:
        """
        Return a hash value for this form class group.

        EXAMPLES::

            sage: hash(BQFClassGroup(-999))  # random
            -4246560339810542104
        """
    def discriminant(self):
        """
        Return the discriminant of the forms in this form class group.

        EXAMPLES::

            sage: BQFClassGroup(-999).discriminant()
            -999
        """
    @cached_method
    def order(self):
        """
        Return the order of this form class group (the *class number*).

        ALGORITHM: :func:`sage.rings.number_field.order.quadratic_order_class_number`.

        EXAMPLES::

            sage: BQFClassGroup(-4).order()
            1
            sage: BQFClassGroup(-11).order()
            1
            sage: BQFClassGroup(-67).order()
            1
            sage: BQFClassGroup(-163).order()
            1
            sage: BQFClassGroup(-999).order()
            24
            sage: BQFClassGroup(-9999).order()
            88
            sage: BQFClassGroup(-99999).order()
            224
        """
    cardinality = order
    @cached_method
    def abelian_group(self):
        """
        Return the structure of this form class group as an
        :class:`AdditiveAbelianGroupWrapper` object.

        ALGORITHM: :pari:`quadclassunit`

        EXAMPLES::

            sage: Cl = BQFClassGroup(-4*777)
            sage: Cl.order()
            16
            sage: G = Cl.abelian_group(); G
            Additive abelian group isomorphic to Z/4 + Z/2 + Z/2 embedded in
            Form Class Group of Discriminant -3108
            sage: G.gens()  # random
            (Class of 11*x^2 + 4*x*y + 71*y^2,
             Class of 6*x^2 + 6*x*y + 131*y^2,
             Class of 2*x^2 + 2*x*y + 389*y^2)
            sage: [g.order() for g in G.gens()]
            [4, 2, 2]
            sage: G.discrete_log(Cl.random_element())  # random
            (3, 0, 1)
        """
    def gens(self) -> tuple:
        """
        Return a generating set of this form class group.

        EXAMPLES::

            sage: Cl = BQFClassGroup(-4*419)
            sage: Cl.gens()
            (Class of 3*x^2 + 2*x*y + 140*y^2,)

        ::

            sage: Cl = BQFClassGroup(-4*777)
            sage: Cl.gens()  # random
            (Class of 11*x^2 + 4*x*y + 71*y^2,
             Class of 6*x^2 + 6*x*y + 131*y^2,
             Class of 2*x^2 + 2*x*y + 389*y^2)
        """

class BQFClassGroup_element(AdditiveGroupElement):
    """
    This type represents elements of class groups of binary quadratic forms.

    Users should not need to construct objects of this type directly; it can
    be accessed via either the :class:`BQFClassGroup` parent object or the
    :meth:`~BinaryQF.form_class` method associated to binary quadratic forms.

    Currently only classes of positive definite forms are supported.

    EXAMPLES::

        sage: F = BinaryQF([22, 91, 99])
        sage: F.form_class()  # indirect doctest
        Class of 5*x^2 - 3*x*y + 22*y^2

    ::

        sage: Cl = BQFClassGroup(-4*419)
        sage: Cl.zero()
        Class of x^2 + 419*y^2
        sage: Cl.gens()[0]  # indirect doctest
        Class of 3*x^2 + 2*x*y + 140*y^2
    """
    def __init__(self, F, parent, *, check: bool = True, reduce: bool = True) -> None:
        """
        Constructor for classes of binary quadratic forms.

        EXAMPLES::

            sage: Cl = BQFClassGroup(-431)
            sage: F = BinaryQF([22, 91, 99])
            sage: from sage.quadratic_forms.bqf_class_group import BQFClassGroup_element
            sage: BQFClassGroup_element(F, parent=Cl)
            Class of 5*x^2 - 3*x*y + 22*y^2
        """
    def form(self):
        """
        Return a reduced quadratic form in this class.

        (For `D < 0`, each class contains a *unique* reduced form.)

        EXAMPLES::

            sage: F = BinaryQF([3221, 2114, 350])
            sage: cl = F.form_class()
            sage: cl.form()
            29*x^2 + 14*x*y + 350*y^2
            sage: cl.form() == F.reduced_form()
            True
        """
    def __mul__(self, other):
        """
        Return an integer multiple of this form class with respect to
        repeated composition.

        ALGORITHM: :func:`multiple`

        EXAMPLES::

            sage: F = BinaryQF([11,21,31])
            sage: cl = F.form_class(); cl
            Class of 11*x^2 - x*y + 21*y^2
            sage: cl*0 == cl.parent().zero()        # indirect doctest
            True
            sage: cl*1 == cl                        # indirect doctest
            True
            sage: cl*(-1) == -cl                    # indirect doctest
            True
            sage: cl*2 == cl + cl                   # indirect doctest
            True
            sage: cl*5 == cl + cl + cl + cl + cl    # indirect doctest
            True
            sage: 5*cl == cl*5                      # indirect doctest
            True
            sage: cl*(-5) == -(5*cl)                # indirect doctest
            True
        """
    __rmul__ = __mul__
    def __eq__(self, other) -> bool:
        """
        Test two form classes for equality.

        EXAMPLES::

            sage: F = BinaryQF([11,21,31])
            sage: cl = F.form_class(); cl
            Class of 11*x^2 - x*y + 21*y^2
            sage: cl == cl      # indirect doctest
            True
            sage: -cl == cl     # indirect doctest
            False
        """
    def __ne__(self, other) -> bool:
        """
        Test two form classes for inequality.

        EXAMPLES::

            sage: F = BinaryQF([11,21,31])
            sage: cl = F.form_class(); cl
            Class of 11*x^2 - x*y + 21*y^2
            sage: cl != cl      # indirect doctest
            False
            sage: -cl != cl     # indirect doctest
            True
        """
    def __lt__(self, other) -> bool:
        """
        Compare two form classes according to the lexicographic ordering
        on their coefficient lists.

        EXAMPLES::

            sage: cl1 = BinaryQF([7,55,141]).form_class(); cl1
            Class of 7*x^2 - x*y + 33*y^2
            sage: cl2 = BinaryQF([11,21,31]).form_class(); cl2
            Class of 11*x^2 - x*y + 21*y^2
            sage: cl1 < cl2     # indirect doctest
            True
            sage: cl1 > cl2     # indirect doctest
            False
        """
    def __bool__(self) -> bool:
        """
        Return ``True`` if this form class is *not* the principal class
        and ``False`` otherwise.

        EXAMPLES::

            sage: cl = BinaryQF([11,21,31]).form_class()
            sage: bool(cl)
            True
            sage: bool(0*cl)
            False
        """
    def is_zero(self) -> bool:
        """
        Return ``True`` if this form class is the principal class and
        ``False`` otherwise.

        EXAMPLES::

            sage: cl = BinaryQF([11,21,31]).form_class()
            sage: cl.is_zero()
            False
            sage: (0*cl).is_zero()
            True
        """
    def __hash__(self) -> int:
        """
        Return a hash value for this form class.

        EXAMPLES::

            sage: cl = BinaryQF([11,21,31]).form_class()
            sage: hash(cl)  # random
            -7760578299759721732
        """
    @cached_method
    def order(self):
        """
        Return the order of this form class in its class group.

        ALGORITHM: :meth:`BQFClassGroup.order` and :func:`order_from_multiple`

        EXAMPLES::

            sage: cl = BinaryQF([11,21,31]).form_class()
            sage: cl.order()
            10
            sage: (cl+cl).order()
            5
            sage: (cl+cl+cl).order()
            10
            sage: (5*cl).order()
            2
        """

class BQFClassGroupQuotientMorphism(Morphism):
    """
    Let `D` be a discriminant and `f > 0` an integer.

    Given the class groups `G` and `H` of discriminants `f^2 D` and `D`,
    this class represents the natural projection morphism `G \\to H` which
    is defined by composing the class representative `[a,b,c]` with the
    principal form of the target discriminant.

    Alternatively, evaluating this map can be characterized as finding a
    class representative `[a,b,c]` satisfying `f^2 \\mid a` and `f \\mid b`
    and substituting `x \\mapsto x/f`.

    This map is a well-defined group homomorphism.

    EXAMPLES::

        sage: from sage.quadratic_forms.bqf_class_group import BQFClassGroupQuotientMorphism
        sage: G = BQFClassGroup(-4*117117)
        sage: H = BQFClassGroup(-4*77)
        sage: proj = BQFClassGroupQuotientMorphism(G, H)
        sage: elt = G(BinaryQF(333, 306, 422))
        sage: proj(elt)
        Class of 9*x^2 + 4*x*y + 9*y^2

    TESTS:

    Check that it is really a group homomorphism::

        sage: D = -randrange(1, 10^4)
        sage: D *= 4 if D%4 not in (0,1) else 1
        sage: f = randrange(1, 10^3)
        sage: G = BQFClassGroup(f^2*D)
        sage: H = BQFClassGroup(D)
        sage: proj = G.hom(H)
        sage: proj(G.zero()) == H.zero()
        True
        sage: elt1 = G.random_element()
        sage: elt2 = G.random_element()
        sage: proj(elt1 + elt2) == proj(elt1) + proj(elt2)
        True

    Check that it satisfies compatibility::

        sage: ff = f * randrange(1, 10^3)
        sage: F = BQFClassGroup(ff^2*D)
        sage: proj = F.hom(H)
        sage: proj1 = F.hom(G)
        sage: proj2 = G.hom(H)
        sage: elt = F.random_element()
        sage: proj(elt) == proj2(proj1(elt))
        True
    """
    def __init__(self, G, H) -> None:
        """
        Initialize this morphism between class groups of binary
        quadratic forms.

        EXAMPLES::

            sage: from sage.quadratic_forms.bqf_class_group import BQFClassGroupQuotientMorphism
            sage: G = BQFClassGroup(-4*117117)
            sage: H = BQFClassGroup(-4*77)
            sage: f = BQFClassGroupQuotientMorphism(G, H)
            sage: TestSuite(f).run(skip='_test_category')
        """
