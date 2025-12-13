from .lie_conformal_algebra_with_structure_coefs import LieConformalAlgebraWithStructureCoefficients as LieConformalAlgebraWithStructureCoefficients
from sage.matrix.special import identity_matrix as identity_matrix
from sage.structure.indexed_generators import standardize_names_index_set as standardize_names_index_set

class WeylLieConformalAlgebra(LieConformalAlgebraWithStructureCoefficients):
    """
    The Weyl Lie conformal algebra.

    INPUT:

    - ``R`` -- a commutative ring; the base ring of this Lie
      conformal algebra
    - ``ngens`` -- an even positive Integer (default: `2`); the number
      of non-central generators of this Lie conformal algebra
    - ``gram_matrix`` -- a matrix (default: ``None``); a non-singular
      skew-symmetric square matrix with coefficients in `R`
    - ``names`` -- list or tuple of strings; alternative names
      for the generators
    - ``index_set`` -- an enumerated set; alternative indexing set
      for the generators

    OUTPUT:

    The Weyl Lie conformal algebra with generators
     `\\alpha_i`, `i=1,...,ngens` and `\\lambda`-brackets

     .. MATH::

        [{\\alpha_i}_{\\lambda} \\alpha_j] = M_{ij} K,

    where `M` is the ``gram_matrix`` above.

    .. NOTE::

        The returned Lie conformal algebra is not `H`-graded. For
        a related `H`-graded Lie conformal algebra see
        :class:`BosonicGhostsLieConformalAlgebra<sage.algebras.\\\n        lie_conformal_algebras.bosonic_ghosts_lie_conformal_algebra\\\n        .BosonicGhostsLieConformalAlgebra>`.

    EXAMPLES::

        sage: lie_conformal_algebras.Weyl(QQ)
        The Weyl Lie conformal algebra with generators (alpha0, alpha1, K) over Rational Field
        sage: R = lie_conformal_algebras.Weyl(QQbar, gram_matrix=Matrix(QQ,[[0,1],[-1,0]]), names = ('a','b'))
        sage: R.inject_variables()
        Defining a, b, K
        sage: a.bracket(b)
        {0: K}
        sage: b.bracket(a)
        {0: -K}

        sage: R = lie_conformal_algebras.Weyl(QQbar, ngens=4)
        sage: R.gram_matrix()
        [ 0  0| 1  0]
        [ 0  0| 0  1]
        [-----+-----]
        [-1  0| 0  0]
        [ 0 -1| 0  0]
        sage: R.inject_variables()
        Defining alpha0, alpha1, alpha2, alpha3, K
        sage: alpha0.bracket(alpha2)
        {0: K}

        sage: R = lie_conformal_algebras.Weyl(QQ); R.category()
        Category of finitely generated Lie conformal algebras with basis over Rational Field
        sage: R in LieConformalAlgebras(QQ).Graded()
        False
        sage: R.inject_variables()
        Defining alpha0, alpha1, K
        sage: alpha0.degree()
        Traceback (most recent call last):
        ...
        AttributeError: 'WeylLieConformalAlgebra_with_category.element_class' object has no attribute 'degree'...

    TESTS::

        sage: lie_conformal_algebras.Weyl(ZZ, gram_matrix=identity_matrix(ZZ,3))
        Traceback (most recent call last):
        ...
        ValueError: the Gram_matrix should be a non degenerate skew-symmetric 3 x 3 matrix, got [1 0 0]
        [0 1 0]
        [0 0 1]
    """
    def __init__(self, R, ngens=None, gram_matrix=None, names=None, index_set=None) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: V = lie_conformal_algebras.Weyl(QQ)
            sage: TestSuite(V).run()
        """
    def gram_matrix(self):
        """
        The Gram matrix that specifies the `\\lambda`-brackets of the
        generators.

        EXAMPLES::

            sage: R = lie_conformal_algebras.Weyl(QQbar, ngens=4)
            sage: R.gram_matrix()
            [ 0  0| 1  0]
            [ 0  0| 0  1]
            [-----+-----]
            [-1  0| 0  0]
            [ 0 -1| 0  0]
        """
