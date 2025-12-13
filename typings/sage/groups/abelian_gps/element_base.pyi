from sage.arith.misc import GCD as GCD
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.infinity import infinity as infinity
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.element import MultiplicativeGroupElement as MultiplicativeGroupElement
from sage.structure.richcmp import richcmp as richcmp

class AbelianGroupElementBase(MultiplicativeGroupElement):
    """
    Base class for abelian group elements.

    The group element is defined by a tuple whose ``i``-th entry is an
    integer in the range from 0 (inclusively) to ``G.gen(i).order()``
    (exclusively) if the `i`-th generator is of finite order, and an
    arbitrary integer if the `i`-th generator is of infinite order.

    INPUT:

    - ``exponents`` -- ``1`` or a list/tuple/iterable of integers; the
      exponent vector (with respect to the parent generators) defining
      the group element

    - ``parent`` -- abelian group; the parent of the group element

    EXAMPLES::

        sage: F = AbelianGroup(3,[7,8,9])
        sage: Fd = F.dual_group(names='ABC')                                            # needs sage.rings.number_field
        sage: A,B,C = Fd.gens()                                                         # needs sage.rings.number_field
        sage: A*B^-1 in Fd                                                              # needs sage.rings.number_field
        True
    """
    def __init__(self, parent, exponents) -> None:
        """
        Create an element.

        EXAMPLES::

            sage: F = AbelianGroup(3,[7,8,9])
            sage: Fd = F.dual_group(names='ABC')                                        # needs sage.rings.number_field
            sage: A,B,C = Fd.gens()                                                     # needs sage.rings.number_field
            sage: A*B^-1 in Fd                                                          # needs sage.rings.number_field
            True

        Check that :issue:`35216` is fixed::

            sage: M = AbelianGroup([3])
            sage: M([5]) == M([2])
            True
            sage: M([3]).is_trivial()
            True
        """
    def __hash__(self):
        """
        TESTS::

            sage: F = AbelianGroup(3,[7,8,9])
            sage: hash(F.an_element()) # random
            1024
        """
    def exponents(self):
        """
        The exponents of the generators defining the group element.

        OUTPUT:

        A tuple of integers for an abelian group element. The integer
        can be arbitrary if the corresponding generator has infinite
        order. If the generator is of finite order, the integer is in
        the range from 0 (inclusive) to the order (exclusive).

        EXAMPLES::

            sage: F.<a,b,c,f> = AbelianGroup([7,8,9,0])
            sage: (a^3*b^2*c).exponents()
            (3, 2, 1, 0)
            sage: F([3, 2, 1, 0])
            a^3*b^2*c
            sage: (c^42).exponents()
            (0, 0, 6, 0)
            sage: (f^42).exponents()
            (0, 0, 0, 42)
        """
    def list(self):
        """
        Return a copy of the exponent vector.

        Use :meth:`exponents` instead.

        OUTPUT:

        The underlying coordinates used to represent this element.  If
        this is a word in an abelian group on `n` generators, then
        this is a list of nonnegative integers of length `n`.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: F = AbelianGroup(5,[2, 3, 5, 7, 8], names='abcde')
            sage: a,b,c,d,e = F.gens()
            sage: Ad = F.dual_group(names='ABCDE')
            sage: A,B,C,D,E = Ad.gens()
            sage: (A*B*C^2*D^20*E^65).exponents()
            (1, 1, 2, 6, 1)
            sage: X = A*B*C^2*D^2*E^-6
            sage: X.exponents()
            (1, 1, 2, 2, 2)
        """
    @cached_method
    def order(self):
        """
        Return the order of this element.

        OUTPUT: integer or ``infinity``

        EXAMPLES::

            sage: F = AbelianGroup(3,[7,8,9])
            sage: Fd = F.dual_group()                                                   # needs sage.rings.number_field
            sage: A,B,C = Fd.gens()                                                     # needs sage.rings.number_field
            sage: (B*C).order()                                                         # needs sage.rings.number_field
            72

            sage: F = AbelianGroup(3,[7,8,9]); F
            Multiplicative Abelian group isomorphic to C7 x C8 x C9
            sage: F.gens()[2].order()
            9
            sage: a,b,c = F.gens()
            sage: (b*c).order()
            72
            sage: G = AbelianGroup(3,[7,8,9])
            sage: type((G.0 * G.1).order())==Integer
            True
        """
    multiplicative_order = order
    def __pow__(self, n):
        """
        Exponentiate ``self``.

        TESTS::

            sage: G.<a,b> = AbelianGroup(2)
            sage: a^3
            a^3
        """
    def __invert__(self):
        """
        Return the inverse element.

        EXAMPLES::

            sage: G.<a,b> = AbelianGroup([0,5])
            sage: a.inverse()  # indirect doctest
            a^-1
            sage: a.__invert__()
            a^-1
            sage: a^-1
            a^-1
            sage: ~a
            a^-1
            sage: (a*b).exponents()
            (1, 1)
            sage: (a*b).inverse().exponents()
            (-1, 4)
        """
    def is_trivial(self):
        """
        Test whether ``self`` is the trivial group element ``1``.

        OUTPUT: boolean

        EXAMPLES::

            sage: G.<a,b> = AbelianGroup([0,5])
            sage: (a^5).is_trivial()
            False
            sage: (b^5).is_trivial()
            True
        """
