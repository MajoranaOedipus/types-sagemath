from .graded_lie_conformal_algebra import GradedLieConformalAlgebra as GradedLieConformalAlgebra
from sage.structure.indexed_generators import standardize_names_index_set as standardize_names_index_set

class AbelianLieConformalAlgebra(GradedLieConformalAlgebra):
    """
    The Abelian Lie conformal algebra.

    INPUT:

    - ``R`` -- a commutative ring; the base ring of this Lie
      conformal algebra
    - ``ngens`` -- positive integer (default: `1`); the number
      of generators of this Lie conformal algebra
    - ``weights`` -- list of positive rational numbers (default:
      `1` for each generator); the weights of the generators. The resulting
      Lie conformal algebra is `H`-graded.
    - ``parity`` -- ``None`` or a list of ``0`` or ``1`` (default:
      ``None``); the parity of the generators. If not ``None`` the
      resulting Lie Conformal algebra is a Super Lie conformal
      algebra
    - ``names`` -- tuple of strings or ``None`` (default: ``None``);
      the list of names of the generators of this algebra.
    - ``index_set`` -- an enumerated set or ``None`` (default:
      ``None``); a set indexing the generators of this Lie
      conformal algebra

    OUTPUT:

    The Abelian Lie conformal algebra with generators `a_i`,
    `i=1,...,n` and vanishing `\\lambda`-brackets, where `n` is
    ``ngens``.

    EXAMPLES::

        sage: R = lie_conformal_algebras.Abelian(QQ,2); R
        The Abelian Lie conformal algebra with generators (a0, a1) over Rational Field
        sage: R.inject_variables()
        Defining a0, a1
        sage: a0.bracket(a1.T(2))
        {}

    TESTS::

        sage: R.central_elements()
        ()
        sage: R.structure_coefficients()
        Finite family {}

    .. TODO::

        implement its own class to speed up arithmetics in this
        case.
    """
    def __init__(self, R, ngens: int = 1, weights=None, parity=None, names=None, index_set=None) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: V = lie_conformal_algebras.Abelian(QQ)
            sage: TestSuite(V).run()
        """
