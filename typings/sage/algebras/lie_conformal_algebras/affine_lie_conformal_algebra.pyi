from .graded_lie_conformal_algebra import GradedLieConformalAlgebra as GradedLieConformalAlgebra
from sage.algebras.lie_algebras.lie_algebra import LieAlgebra as LieAlgebra
from sage.rings.integer import Integer as Integer

class AffineLieConformalAlgebra(GradedLieConformalAlgebra):
    '''
    The current or affine Kac-Moody Lie conformal algebra.

    INPUT:

    - ``R`` -- a commutative Ring; the base ring for this Lie
      conformal algebra
    - ``ct`` -- a ``str`` or a :mod:`CartanType<sage.combinat.\\\n      root_system.cartan_type>`; the Cartan Type for
      the corresponding finite dimensional Lie algebra. It must
      correspond to a simple finite dimensional Lie algebra.
    - ``names`` -- list of ``str`` or ``None`` (default: ``None``);
      alternative names for the generators. If ``None`` the
      generators are labeled by the corresponding root and coroot
      vectors.
    - ``prefix`` -- a ``str``; parameter passed to
      :class:`IndexedGenerators<sage.structure.indexed_generators.IndexedGenerators>`
    - ``bracket`` -- a ``str``; parameter passed to
      :class:`IndexedGenerators<sage.structure.indexed_generators.IndexedGenerators>`

    EXAMPLES::

        sage: R = lie_conformal_algebras.Affine(QQ, \'A1\')
        sage: R
        The affine Lie conformal algebra of type [\'A\', 1] over Rational Field
        sage: R.an_element()
        B[alpha[1]] + B[alphacheck[1]] + B[-alpha[1]] + B[\'K\']

        sage: R = lie_conformal_algebras.Affine(QQ, \'A1\', names = (\'e\', \'h\',\'f\'))
        sage: R.inject_variables()
        Defining e, h, f, K
        sage: Family(e.bracket(f.T(3)))
        Finite family {0: 6*T^(3)h, 1: 6*T^(2)h, 2: 6*Th, 3: 6*h, 4: 24*K}

        sage: V = lie_conformal_algebras.Affine(QQ, CartanType(["A",2,1]))
        Traceback (most recent call last):
        ...
        ValueError: only affine algebras of simple finite dimensionalLie algebras are implemented

    OUTPUT:

    The Affine Lie conformal algebra associated with the finite
    dimensional simple Lie algebra of Cartan type ``ct``.
    '''
    def __init__(self, R, ct, names=None, prefix=None, bracket=None) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: V = lie_conformal_algebras.Affine(QQ,'A1')
            sage: TestSuite(V).run()
        """
    def cartan_type(self):
        """
        The Cartan type of this Lie conformal algbera.

        EXAMPLES::

            sage: R = lie_conformal_algebras.Affine(QQ, 'B3')
            sage: R
            The affine Lie conformal algebra of type ['B', 3] over Rational Field
            sage: R.cartan_type()
            ['B', 3]
        """
