from .cartan_type import CartanType_standard_finite as CartanType_standard_finite
from sage.combinat.root_system.root_system import RootSystem as RootSystem

class CartanType(CartanType_standard_finite):
    """
    Cartan Type `Q_n`.

    .. SEEALSO:: :func:`~sage.combinat.root_systems.cartan_type.CartanType`
    """
    def __init__(self, m) -> None:
        """
        EXAMPLES::

            sage: ct = CartanType(['Q',4])
            sage: ct
            ['Q', 4]
            sage: ct._repr_(compact = True)
            'Q4'

            sage: ct.is_irreducible()
            True
            sage: ct.is_finite()
            True
            sage: ct.is_affine()
            False
            sage: ct.is_simply_laced()
            True
            sage: ct.dual()
            ['Q', 4]

        TESTS::

            sage: TestSuite(ct).run()
        """
    def __reduce__(self):
        """
        TESTS::

            sage: T = CartanType(['Q', 4])
            sage: T.__reduce__()
            (CartanType, ('Q', 4))
            sage: T == loads(dumps(T))
            True
        """
    def index_set(self):
        """
        Return the index set for Cartan type Q.

        The index set for type Q is of the form
        `\\{-n, \\ldots, -1, 1, \\ldots, n\\}`.

        EXAMPLES::

            sage: CartanType(['Q', 3]).index_set()
            (1, 2, -2, -1)
        """
    def root_system(self):
        """
        Return the root system of ``self``.

        EXAMPLES::

            sage: Q = CartanType(['Q',3])
            sage: Q.root_system()
            Root system of type ['A', 2]
        """
    def is_irreducible(self):
        """
        Return whether this Cartan type is irreducible.

        EXAMPLES::

            sage: Q = CartanType(['Q',3])
            sage: Q.is_irreducible()
            True
        """
    def is_simply_laced(self):
        """
        Return whether this Cartan type is simply-laced.

        EXAMPLES::

            sage: Q = CartanType(['Q',3])
            sage: Q.is_simply_laced()
            True
        """
    def dual(self):
        """
        Return dual of ``self``.

        EXAMPLES::

            sage: Q = CartanType(['Q',3])
            sage: Q.dual()
            ['Q', 3]
        """
