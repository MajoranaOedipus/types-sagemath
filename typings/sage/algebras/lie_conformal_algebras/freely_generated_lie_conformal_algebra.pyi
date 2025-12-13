from .lie_conformal_algebra_with_basis import LieConformalAlgebraWithBasis as LieConformalAlgebraWithBasis
from sage.categories.cartesian_product import cartesian_product as cartesian_product
from sage.rings.integer import Integer as Integer
from sage.sets.disjoint_union_enumerated_sets import DisjointUnionEnumeratedSets as DisjointUnionEnumeratedSets
from sage.sets.family import Family as Family
from sage.sets.non_negative_integers import NonNegativeIntegers as NonNegativeIntegers

class FreelyGeneratedLieConformalAlgebra(LieConformalAlgebraWithBasis):
    """
    Base class for a central extension of a freely generated Lie
    conformal algebra.

    This class provides minimal functionality, it sets up the
    family of Lie conformal algebra generators.

    .. NOTE::

        We now only accept direct sums of free modules plus
        some central generators `C_i` such that `TC_i = 0`.
    """
    def __init__(self, R, index_set=None, central_elements=None, category=None, element_class=None, prefix=None, **kwds) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: V = lie_conformal_algebras.Virasoro(QQ)
            sage: TestSuite(V).run()
        """
    def lie_conformal_algebra_generators(self):
        """
        The generators of this Lie conformal algebra.

        OUTPUT: a (possibly infinite) family of generators (as an
        `R[T]`-module) of this Lie conformal algebra.

        EXAMPLES::

            sage: Vir = lie_conformal_algebras.Virasoro(QQ)
            sage: Vir.lie_conformal_algebra_generators()
            (L, C)
            sage: V = lie_conformal_algebras.Affine(QQ,'A1')
            sage: V.lie_conformal_algebra_generators()
            (B[alpha[1]], B[alphacheck[1]], B[-alpha[1]], B['K'])
        """
    def central_elements(self):
        """
        The central generators of this Lie conformal algebra.

        EXAMPLES::

            sage: Vir = lie_conformal_algebras.Virasoro(QQ)
            sage: Vir.central_elements()
            (C,)
            sage: V = lie_conformal_algebras.Affine(QQ, 'A1')
            sage: V.central_elements()
            (B['K'],)
        """
