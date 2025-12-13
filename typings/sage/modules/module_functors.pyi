from sage.categories.modules import Modules as Modules
from sage.categories.pushout import ConstructionFunctor as ConstructionFunctor

class QuotientModuleFunctor(ConstructionFunctor):
    """
    Construct the quotient of a module by a submodule.

    INPUT:

    - ``relations`` -- a module

    .. NOTE::

        This construction functor keeps track of the basis of defining
        ``relations``. It can only be applied to free modules into which
        this basis coerces.

    EXAMPLES::

        sage: A = (1/2)*ZZ^2
        sage: B = 2*ZZ^2
        sage: Q = A / B
        sage: F = Q.construction()[0]
        sage: F
        QuotientModuleFunctor
        sage: F(A) == Q
        True

    The modules are constructed from the cover not the ambient module::

        sage: F(B.ambient_module()) == Q
        False

    We can construct quotients from different modules::

        sage: F((1/2)*ZZ^2)
        Finitely generated module V/W over Integer Ring with invariants (4, 4)
        sage: F(ZZ^2)
        Finitely generated module V/W over Integer Ring with invariants (2, 2)
        sage: F(2*ZZ^2)
        Finitely generated module V/W over Integer Ring with invariants ()

    This functor is used for constructing pushouts::

        sage: A = ZZ^3
        sage: x,y,z = A.basis()
        sage: A1 = A.submodule([x])
        sage: A2 = A.submodule([y, 2*x])
        sage: B1 = A.submodule([])
        sage: B2 = A.submodule([2*x])
        sage: Q1 = A1 / B1
        sage: Q2 = A2 / B2
        sage: q3 = Q1.an_element() + Q2.an_element()
    """
    rank: int
    def __init__(self, relations) -> None:
        """
        Initialization of ``self``.

        TESTS::

            sage: from sage.modules.module_functors import QuotientModuleFunctor
            sage: B = (2/3)*ZZ^2
            sage: F = QuotientModuleFunctor(B)
            sage: TestSuite(F).run()
        """
    def relations(self):
        """
        Return the defining relations of ``self``.

        EXAMPLES::

            sage: A = (ZZ**2) / span([[4,0],[0,3]], ZZ)
            sage: A.construction()[0].relations()
            Free module of degree 2 and rank 2 over Integer Ring
            Echelon basis matrix:
            [4 0]
            [0 3]
        """
    def __eq__(self, other):
        """
        The quotient functor ``self`` is equal to ``other`` if
        it is a :class:`QuotientModuleFunctor` and the relations
        subspace are equal.

        EXAMPLES::

            sage: F1 = ((ZZ^3) / (4*ZZ^3)).construction()[0]
            sage: F2 = ((2*ZZ^3) / (4*ZZ^3)).construction()[0]
            sage: F1 == F2
            True
            sage: F3 = ((ZZ^3) / (8*ZZ^3)).construction()[0]
            sage: F1 == F3
            False
        """
    def __ne__(self, other):
        """
        Check whether ``self`` is not equal to ``other``.

        EXAMPLES::

            sage: F1 = ((ZZ^3) / (4*ZZ^3)).construction()[0]
            sage: F2 = ((2*ZZ^3) / (4*ZZ^3)).construction()[0]
            sage: F1 != F2
            False
            sage: F3 = ((ZZ^3) / (8*ZZ^3)).construction()[0]
            sage: F1 != F3
            True
        """
    def merge(self, other):
        """
        Merge the construction functors ``self`` and ``other``.

        EXAMPLES::

            sage: A = ZZ^3
            sage: x,y,z = A.basis()
            sage: A1 = A.submodule([x])
            sage: A2 = A.submodule([y, 2*x])
            sage: B1 = A.submodule([])
            sage: B2 = A.submodule([2*x])
            sage: Q1 = A1 / B1
            sage: Q2 = A2 / B2
            sage: F1 = Q1.construction()[0]
            sage: F2 = Q2.construction()[0]
            sage: F3 = F1.merge(F2)
            sage: q3 = Q1.an_element() + Q2.an_element()
            sage: q3.parent() == F3(A1 + A2)
            True

            sage: G = A1.construction()[0]; G
            SubspaceFunctor
            sage: F1.merge(G)
            sage: F2.merge(G)
        """
