from sage.knots.knotinfo import SymmetryMutant as SymmetryMutant
from sage.misc.cachefunc import cached_method as cached_method
from sage.monoids.indexed_free_monoid import IndexedFreeAbelianMonoid as IndexedFreeAbelianMonoid, IndexedFreeAbelianMonoidElement as IndexedFreeAbelianMonoidElement
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class FreeKnotInfoMonoidElement(IndexedFreeAbelianMonoidElement):
    """
    An element of an indexed free abelian monoid.
    """
    def as_knot(self):
        """
        Return the knot represented by ``self``.

        EXAMPLES::

            sage: from sage.knots.free_knotinfo_monoid import FreeKnotInfoMonoid
            sage: FKIM =  FreeKnotInfoMonoid()
            sage: FKIM.inject_variables(select=3)
            Defining K3_1
            Defining K3_1m
            sage: K = K3_1^2 * K3_1m
            sage: K.as_knot()
            Knot represented by 9 crossings
        """
    def to_knotinfo(self):
        """
        Return a word representing ``self`` as a list of pairs.

        Each pair ``(ki, sym)`` consists of a
        :class:`~sage.knots.knotinfo.KnotInfoBase` instance ``ki`` and
        :class:`~sage.knots.knotinfo.SymmetryMutant` instance ``sym``.

        EXAMPLES::

            sage: from sage.knots.free_knotinfo_monoid import FreeKnotInfoMonoid
            sage: FKIM =  FreeKnotInfoMonoid()
            sage: FKIM.inject_variables(select=3)
            Defining K3_1
            Defining K3_1m
            sage: K = K3_1^2 * K3_1m
            sage: K.to_knotinfo()
            [(<KnotInfo.K3_1: '3_1'>, <SymmetryMutant.itself: 's'>),
            (<KnotInfo.K3_1: '3_1'>, <SymmetryMutant.itself: 's'>),
            (<KnotInfo.K3_1: '3_1'>, <SymmetryMutant.mirror_image: 'm'>)]
        """

class FreeKnotInfoMonoid(IndexedFreeAbelianMonoid):
    Element = FreeKnotInfoMonoidElement
    @staticmethod
    def __classcall_private__(cls, max_crossing_number: int = 6, prefix=None, **kwds):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: from sage.knots.free_knotinfo_monoid import FreeKnotInfoMonoid
            sage: FreeKnotInfoMonoid()
            Free abelian monoid of knots with at most 6 crossings
            sage: FreeKnotInfoMonoid(5)
            Free abelian monoid of knots with at most 5 crossings
        """
    def __init__(self, max_crossing_number, category=None, prefix=None, **kwds) -> None:
        """
        Initialize ``self`` with generators belonging to prime knots with
        at most ``max_crossing_number`` crossings.

        TESTS:

            sage: from sage.knots.free_knotinfo_monoid import FreeKnotInfoMonoid
            sage: FKIM =  FreeKnotInfoMonoid()
            sage: FKIM4 =  FreeKnotInfoMonoid(4)
            sage: TestSuite(FKIM).run()
            sage: TestSuite(FKIM4).run()
        """
    def from_knot(self, knot, unique: bool = True):
        """
        Create an element of this abelian monoid from ``knot``.

        INPUT:

        - ``knot`` -- an instance of :class:`~sage.knots.knot.Knot`

        - ``unique`` -- boolean (default is ``True``). This only affects the case
          where a unique identification is not possible. If set to ``False`` you
          can obtain a matching list (see explanation of the output below)

        OUTPUT:

        An instance of the element class of ``self`` per default. If the keyword
        argument ``unique`` then a list of such instances is returned.

        EXAMPLES::

            sage: from sage.knots.free_knotinfo_monoid import FreeKnotInfoMonoid
            sage: FKIM =  FreeKnotInfoMonoid()
            sage: K = KnotInfo.K5_1.link().mirror_image()
            sage: FKIM.from_knot(K)
            KnotInfo['K5_1m']

            sage: # optional - database_knotinfo
            sage: K = Knot(KnotInfo.K9_12.braid())
            sage: FKIM.from_knot(K)                   # long time
            Traceback (most recent call last):
            ...
            NotImplementedError: this (possibly non prime) knot cannot be
            identified uniquely by KnotInfo
            use keyword argument `unique` to obtain more details
            sage: FKIM.from_knot(K, unique=False)     # long time
            [KnotInfo['K4_1']*KnotInfo['K5_2'], KnotInfo['K9_12']]
        """
    def inject_variables(self, select=None, verbose: bool = True) -> None:
        """
        Inject ``self`` with its name into the namespace of the
        Python code from which this function is called.

        INPUT:

        - ``select`` -- instance of :class:`~sage.knots.knotinfo.KnotInfoBase`,
          :class:`~sage.knots.knotinfo.KnotInfoSeries` or an integer. In all
          cases the input is used to restrict the injected generators to the
          according subset (number of crossings in the case of integer)
        - ``verbose`` -- boolean (optional, default ``True``) to suppress
          the message printed on the invocation

        EXAMPLES::

          sage: from sage.knots.free_knotinfo_monoid import FreeKnotInfoMonoid
          sage: FKIM = FreeKnotInfoMonoid(5)
          sage: FKIM.inject_variables(select=3)
          Defining K3_1
          Defining K3_1m
          sage: FKIM.inject_variables(select=KnotInfo.K5_2)
          Defining K5_2
          Defining K5_2m
          sage: FKIM.inject_variables(select=KnotInfo.K5_2.series())
          Defining K5_1
          Defining K5_1m
          sage: FKIM.inject_variables()
          Defining K0_1
          Defining K4_1
        """
