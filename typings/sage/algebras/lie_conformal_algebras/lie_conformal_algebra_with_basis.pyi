from sage.categories.lie_conformal_algebras import LieConformalAlgebras as LieConformalAlgebras
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule

class LieConformalAlgebraWithBasis(CombinatorialFreeModule):
    """
    Abstract base class for a Lie conformal algebra with a
    preferred basis.

    This class provides no functionality, it simply passes the
    arguments to :class:`CombinatorialFreeModule`.

    EXAMPLES::

        sage: R = lie_conformal_algebras.Virasoro(QQbar);R
        The Virasoro Lie conformal algebra over Algebraic Field

    TESTS::

        sage: R = lie_conformal_algebras.Virasoro(QQ)
        sage: R.0
        L
        sage: R._repr_generator(R.0)
        'L'
        sage: R = lie_conformal_algebras.Affine(QQ, 'A1')
        sage: R.0
        B[alpha[1]]
        sage: R._repr_generator(R.0)
        'B[alpha[1]]'
        sage: R = lie_conformal_algebras.Affine(QQ, 'A1', names = ('e', 'h','f'))
        sage: R.0
        e
        sage: R._repr_generator(R.0)
        'e'
    """
    def __init__(self, R, basis_keys=None, element_class=None, category=None, prefix=None, **kwds) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: V = lie_conformal_algebras.Affine(QQ,'A1')
            sage: TestSuite(V).run()
        """
