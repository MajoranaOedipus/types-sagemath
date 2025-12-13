from .lie_conformal_algebra_with_structure_coefs import LieConformalAlgebraWithStructureCoefficients as LieConformalAlgebraWithStructureCoefficients
from sage.categories.lie_conformal_algebras import LieConformalAlgebras as LieConformalAlgebras

class GradedLieConformalAlgebra(LieConformalAlgebraWithStructureCoefficients):
    """
    An H-Graded Lie conformal algebra.

    INPUT:

    - ``R`` -- a commutative ring (default: ``None``); the base
      ring of this Lie conformal algebra. Behaviour is undefined if
      it is not a field of characteristic zero

    - ``s_coeff`` -- dictionary (default: ``None``); as in the
      input of :class:`LieConformalAlgebra`

    - ``names`` -- tuple of strings (default: ``None``); as in the
      input of :class:`LieConformalAlgebra`

    - ``central_elements`` -- tuple of strings (default: ``None``);
      as in the input of :class:`LieConformalAlgebra`

    - ``index_set`` -- enumerated set (default: ``None``); as in the
      input of :class:`LieConformalAlgebra`

    - ``weights`` -- tuple of nonnegative rational numbers
      (default: tuple of ``1``); a list of degrees for this Lie
      conformal algebra.
      This tuple needs to have the same cardinality as
      ``index_set`` or ``names``. Central elements are assumed
      to have weight ``0``.

    - ``category`` -- the category that this Lie conformal algebra
      belongs to

    - ``parity`` -- tuple of ``0`` or ``1`` (default: tuple of
      ``0``); a tuple specifying the parity of each non-central
      generator

    EXAMPLES::

        sage: bosondict = {('a','a'):{1:{('K',0):1}}}
        sage: R = LieConformalAlgebra(QQ,bosondict,names=('a',),central_elements=('K',), weights=(1,))
        sage: R.inject_variables()
        Defining a, K
        sage: a.T(3).degree()
        4
        sage: K.degree()
        0
        sage: R.category()
        Category of H-graded finitely generated Lie conformal algebras with basis over Rational Field
    """
    def __init__(self, R, s_coeff, index_set=None, central_elements=None, category=None, prefix=None, names=None, latex_names=None, parity=None, weights=None, **kwds) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: V = lie_conformal_algebras.Virasoro(QQ)
            sage: TestSuite(V).run()
        """
