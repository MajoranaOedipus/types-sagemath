from _typeshed import Incomplete
from sage.arith.misc import GCD as GCD
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.structure.richcmp import richcmp as richcmp, richcmp_method as richcmp_method
from sage.structure.sage_object import SageObject as SageObject

class G1list(SageObject):
    """
    A class representing a list of coset representatives for `\\Gamma_1(N)` in
    `\\SL_2(\\ZZ)`. What we actually calculate is a list of elements of
    `(\\ZZ/N\\ZZ)^2` of exact order `N`.

    TESTS::

        sage: L = sage.modular.modsym.g1list.G1list(18)
        sage: loads(dumps(L)) == L
        True
    """
    def __init__(self, N) -> None:
        """
        EXAMPLES::

            sage: L = sage.modular.modsym.g1list.G1list(6); L # indirect doctest
            List of coset representatives for Gamma_1(6) in SL_2(Z)
        """
    def __richcmp__(self, other, op):
        """
        Compare ``self`` to ``other``.

        EXAMPLES::

            sage: L1 = sage.modular.modsym.g1list.G1list(6)
            sage: L2 = sage.modular.modsym.g1list.G1list(7)
            sage: L1 < L2
            True
            sage: L1 == QQ
            False
        """
    def __getitem__(self, i):
        """
        EXAMPLES::

            sage: L = sage.modular.modsym.g1list.G1list(19); L[100] # indirect doctest
            (5, 6)
        """
    def __len__(self) -> int:
        """
        Return the length of the underlying list.

        EXAMPLES::

            sage: L = sage.modular.modsym.g1list.G1list(24); len(L) # indirect doctest
            384
        """
    def list(self):
        """
        Return a list of vectors representing the cosets.

        Do not change the returned list!

        EXAMPLES::

            sage: L = sage.modular.modsym.g1list.G1list(4); L.list()
            [(0, 1), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 1), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)]
        """
    def normalize(self, u, v):
        """
        Given a pair `(u,v)` of integers, return the unique pair `(u', v')`
        such that the pair `(u', v')` appears in ``self.list()`` and `(u, v)`
        is equivalent to `(u', v')`. This is rather trivial, but is here for
        consistency with the ``P1List`` class which is the equivalent for
        `\\Gamma_0` (where the problem is rather harder).

        This will only make sense if `{\\rm gcd}(u, v, N) = 1`; otherwise the
        output will not be an element of ``self``.

        EXAMPLES::

            sage: L = sage.modular.modsym.g1list.G1list(4); L.normalize(6, 1)
            (2, 1)
            sage: L = sage.modular.modsym.g1list.G1list(4); L.normalize(6, 2) # nonsense!
            (2, 2)
        """

class _G1list_old_pickle(G1list):
    """
    This class exists only for dealing with old pickles.

    This needs to handle both old-style class pickles, where there is
    no input to the class on the initial ``__init__`` call, and the
    new class pickles, we need to have ``__setstate__`` handle it.
    """
    __class__: Incomplete
    def __init__(self) -> None:
        """
        For unpickling old pickles.

        TESTS::

            sage: from sage.modular.modsym.g1list import _G1list_old_pickle
            sage: L = _G1list_old_pickle()
            sage: type(L) == G1list
            True
        """
