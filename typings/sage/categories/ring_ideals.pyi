from sage.categories.category_types import Category_ideal as Category_ideal
from sage.categories.modules import Modules as Modules
from sage.categories.rings import Rings as Rings

class RingIdeals(Category_ideal):
    """
    The category of two-sided ideals in a fixed ring.

    EXAMPLES::

        sage: Ideals(Integers(200))
        Category of ring ideals in Ring of integers modulo 200
        sage: C = Ideals(IntegerRing()); C
        Category of ring ideals in Integer Ring
        sage: I = C([8,12,18])
        sage: I
        Principal ideal (2) of Integer Ring

    See also: :class:`CommutativeRingIdeals`.

    .. TODO::

         - If useful, implement ``RingLeftIdeals`` and ``RingRightIdeals``
           of which ``RingIdeals`` would be a subcategory.

         - Make ``RingIdeals(R)``, return ``CommutativeRingIdeals(R)``
           when ``R`` is commutative.
    """
    def __init__(self, R) -> None:
        """
        EXAMPLES::

            sage: RingIdeals(ZZ)
            Category of ring ideals in Integer Ring
            sage: RingIdeals(3)
            Traceback (most recent call last):
            ...
            TypeError: R (=3) must be a ring

        TESTS::

            sage: TestSuite(RingIdeals(ZZ)).run()
        """
    def super_categories(self):
        """
        EXAMPLES::

            sage: RingIdeals(ZZ).super_categories()
            [Category of modules over Integer Ring]
            sage: RingIdeals(QQ).super_categories()
            [Category of vector spaces over Rational Field]
        """

Ideals = RingIdeals