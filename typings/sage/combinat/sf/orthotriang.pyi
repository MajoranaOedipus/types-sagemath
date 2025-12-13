from . import sfa as sfa
from sage.categories.homset import Hom as Hom
from sage.categories.morphism import SetMorphism as SetMorphism
from sage.combinat.sf.sfa import SymmetricFunctionsFunctor as SymmetricFunctionsFunctor
from sage.misc.persist import register_unpickle_override as register_unpickle_override

class SymmetricFunctionAlgebra_orthotriang(sfa.SymmetricFunctionAlgebra_generic):
    class Element(sfa.SymmetricFunctionAlgebra_generic.Element): ...
    @staticmethod
    def __classcall__(cls, Sym, base, scalar, prefix, basis_name, leading_coeff=None):
        """
        Normalize the arguments.

        TESTS::

            sage: from sage.combinat.sf.sfa import zee
            sage: from sage.combinat.sf.orthotriang import SymmetricFunctionAlgebra_orthotriang
            sage: Sym = SymmetricFunctions(QQ)
            sage: m = Sym.m()
            sage: B1 = SymmetricFunctionAlgebra_orthotriang(Sym, m, zee, 's', 'Schur')
            sage: B2 = SymmetricFunctionAlgebra_orthotriang(Sym, m, zee, 's', 'Schur', None)
            sage: B1 is B2
            True
        """
    def __init__(self, Sym, base, scalar, prefix, basis_name, leading_coeff) -> None:
        '''
        Initialization of the symmetric function algebra defined via orthotriangular rules.

        INPUT:

        - ``self`` -- a basis determined by an orthotriangular definition
        - ``Sym`` -- ring of symmetric functions
        - ``base`` -- an instance of a basis of the ring of symmetric functions
          (e.g. the Schur functions)
        - ``scalar`` -- a function ``zee`` on partitions. The function
          ``zee`` determines the scalar product on the power sum basis
          with normalization `\\langle p_{\\mu}, p_{\\mu} \\rangle =
          \\mathrm{zee}(\\mu)`.
        - ``prefix`` -- the prefix used to display the basis
        - ``basis_name`` -- the name used for the basis

        .. NOTE::

            The base ring is required to be a `\\QQ`-algebra for this
            method to be usable, since the scalar product is defined by
            its values on the power sum basis.

        EXAMPLES::

            sage: from sage.combinat.sf.sfa import zee
            sage: from sage.combinat.sf.orthotriang import SymmetricFunctionAlgebra_orthotriang
            sage: Sym = SymmetricFunctions(QQ)
            sage: m = Sym.m()
            sage: s = SymmetricFunctionAlgebra_orthotriang(Sym, m, zee, \'s\', \'Schur\'); s
            Symmetric Functions over Rational Field in the Schur basis

        TESTS::

            sage: TestSuite(s).run(elements=[s[1,1]+2*s[2], s[1]+3*s[1,1]])
            sage: TestSuite(s).run(skip=["_test_associativity", "_test_prod"])  # long time (7s on sage.math, 2011)

        Note: ``s.an_element()`` is of degree 4; so we skip
        ``_test_associativity`` and ``_test_prod`` which involve
        (currently?) expensive calculations up to degree 12.
        '''
    def construction(self):
        """
        Return a pair ``(F, R)``, where ``F`` is a
        :class:`SymmetricFunctionsFunctor` and `R` is a ring, such
        that ``F(R)`` returns ``self``.

        EXAMPLES::

            sage: from sage.combinat.sf.sfa import zee
            sage: from sage.combinat.sf.orthotriang import SymmetricFunctionAlgebra_orthotriang
            sage: Sym = SymmetricFunctions(QQ)
            sage: m = Sym.m()
            sage: s = SymmetricFunctionAlgebra_orthotriang(Sym, m, zee, 's', 'Schur')
            sage: s.construction()
            (SymmetricFunctionsFunctor[Schur], Rational Field)
        """
    def product(self, left, right):
        """
        Return ``left`` * ``right`` by converting both to the base and then
        converting back to ``self``.

        INPUT:

        - ``self`` -- a basis determined by an orthotriangular definition
        - ``left``, ``right`` -- elements in ``self``

        OUTPUT: the expansion of the product of ``left`` and ``right`` in the basis ``self``

        EXAMPLES::

            sage: from sage.combinat.sf.sfa import zee
            sage: from sage.combinat.sf.orthotriang import SymmetricFunctionAlgebra_orthotriang
            sage: Sym = SymmetricFunctions(QQ)
            sage: m = Sym.m()
            sage: s = SymmetricFunctionAlgebra_orthotriang(Sym, m, zee, 's', 'Schur functions')
            sage: s([1])*s([2,1]) #indirect doctest
            s[2, 1, 1] + s[2, 2] + s[3, 1]
        """

class OrthotriangBasisFunctor(SymmetricFunctionsFunctor):
    """
    A constructor for algebras of symmetric functions constructed by
    orthogonality and triangularity.

    EXAMPLES::

        sage: from sage.combinat.sf.sfa import zee
        sage: from sage.combinat.sf.orthotriang import SymmetricFunctionAlgebra_orthotriang
        sage: Sym = SymmetricFunctions(QQ)
        sage: m = Sym.m()
        sage: s = SymmetricFunctionAlgebra_orthotriang(Sym, m, zee, 's', 'Schur')
        sage: s.construction()
        (SymmetricFunctionsFunctor[Schur], Rational Field)
    """
    def __init__(self, basis) -> None:
        """
        Initialize the functor.

        INPUT:

        - ``basis`` -- the basis of the symmetric function algebra

        TESTS::

            sage: from sage.combinat.sf.sfa import zee
            sage: from sage.combinat.sf.orthotriang import SymmetricFunctionAlgebra_orthotriang
            sage: Sym = SymmetricFunctions(QQ)
            sage: m = Sym.m()
            sage: s = SymmetricFunctionAlgebra_orthotriang(Sym, m, zee, 's', 'Schur')
            sage: F, R = s.construction()
            sage: TestSuite(F).run()
        """
