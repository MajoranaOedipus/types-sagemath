from . import sfa as sfa
from _typeshed import Incomplete
from sage.categories.homset import Hom as Hom
from sage.categories.morphism import SetMorphism as SetMorphism
from sage.combinat import ribbon_tableau as ribbon_tableau
from sage.combinat.partition import Partition as Partition, Partitions as Partitions
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

hsp_to_m_cache: Incomplete
m_to_hsp_cache: Incomplete
hcosp_to_m_cache: Incomplete
m_to_hcosp_cache: Incomplete
QQt: Incomplete

class LLT_class(UniqueRepresentation):
    """
    A class for working with LLT symmetric functions.

    EXAMPLES::

        sage: Sym = SymmetricFunctions(FractionField(QQ['t']))
        sage: L3 = Sym.llt(3); L3
        level 3 LLT polynomials over Fraction Field of Univariate Polynomial Ring in t over Rational Field
        sage: L3.cospin([3,2,1])
        (t+1)*m[1, 1] + m[2]
        sage: HC3 = L3.hcospin(); HC3
        Symmetric Functions over Fraction Field of Univariate Polynomial Ring in t over Rational Field in the level 3 LLT cospin basis
        sage: m = Sym.monomial()
        sage: m( HC3[1,1] )
        (t+1)*m[1, 1] + m[2]

    We require that the parameter `t` must be in the base ring::

        sage: Symxt = SymmetricFunctions(QQ['x','t'].fraction_field())
        sage: (x,t) = Symxt.base_ring().gens()
        sage: LLT3x = Symxt.llt(3,t=x)
        sage: LLT3 = Symxt.llt(3)
        sage: HS3x = LLT3x.hspin()
        sage: HS3t = LLT3.hspin()
        sage: s = Symxt.schur()
        sage: s(HS3x[2,1])
        s[2, 1] + x*s[3]
        sage: s(HS3t[2,1])
        s[2, 1] + t*s[3]
        sage: HS3x(HS3t[2,1])
        HSp3[2, 1] - (x-t)*HSp3[3]
        sage: s(HS3x(HS3t[2,1]))
        s[2, 1] + t*s[3]
        sage: LLT3t2 = Symxt.llt(3,t=2)
        sage: HC3t2 = LLT3t2.hcospin()
        sage: HS3x(HC3t2[3,1])
        2*HSp3[3, 1] - (2*x-1)*HSp3[4]
    """
    @staticmethod
    def __classcall__(cls, Sym, k, t: str = 't'):
        """
        Normalize the arguments.

        TESTS::

            sage: R.<q, t> = QQ[]
            sage: B1 = SymmetricFunctions(R).llt(3).hspin()
            sage: B2 = SymmetricFunctions(R).llt(3, t).hspin()
            sage: B3 = SymmetricFunctions(R).llt(3, q).hspin()
            sage: B1 is B2
            True
            sage: B1 == B3
            False
        """
    t: Incomplete
    def __init__(self, Sym, k, t) -> None:
        '''
        Class of LLT symmetric function bases.

        INPUT:

        - ``self`` -- a family of LLT symmetric function bases
        - ``k`` -- positive integer (the level)
        - ``t`` -- a parameter (default: `t`)

        EXAMPLES::

            sage: L3 = SymmetricFunctions(FractionField(QQ[\'t\'])).llt(3)
            sage: L3 == loads(dumps(L3))
            True
            sage: TestSuite(L3).run(skip=["_test_associativity","_test_distributivity","_test_prod"])

        TESTS::

            sage: L3 != SymmetricFunctions(FractionField(QQ[\'t\'])).llt(2)
            True
            sage: L3p = SymmetricFunctions(FractionField(QQ[\'t\'])).llt(3,t=1)
            sage: L3 != L3p
            True
            sage: L3p != SymmetricFunctions(QQ).llt(3,t=1)
            True

            sage: Sym = SymmetricFunctions(QQ[\'t\'])
            sage: ks3 = Sym.kschur(3)
            sage: llt3 = Sym.llt(3)
            sage: f = llt3.cospin([[1],[2,1],[1,1]]).omega()
            sage: ks3(f)
            ks3[2, 2, 1, 1] + ks3[2, 2, 2] + t*ks3[3, 1, 1, 1] + t^2*ks3[3, 2, 1]
        '''
    def symmetric_function_ring(self):
        """
        The symmetric function algebra associated to the family of LLT
        symmetric function bases

        INPUT:

        - ``self`` -- a family of LLT symmetric functions bases

        OUTPUT: the symmetric function ring associated to ``self``

        EXAMPLES::

            sage: L3 = SymmetricFunctions(FractionField(QQ['t'])).llt(3)
            sage: L3.symmetric_function_ring()
            Symmetric Functions over Fraction Field of Univariate Polynomial Ring in t over Rational Field
        """
    def base_ring(self):
        """
        Return the base ring of ``self``.

        INPUT:

        - ``self`` -- a family of LLT symmetric functions bases

        OUTPUT: the base ring of the symmetric function ring associated to ``self``

        EXAMPLES::

            sage: SymmetricFunctions(FractionField(QQ['t'])).llt(3).base_ring()
            Fraction Field of Univariate Polynomial Ring in t over Rational Field
        """
    def level(self):
        """
        Return the level of ``self``.

        INPUT:

        - ``self`` -- a family of LLT symmetric functions bases

        OUTPUT: the level is the parameter of `k` in the basis

        EXAMPLES::

            sage: SymmetricFunctions(FractionField(QQ['t'])).llt(3).level()
            3
        """
    def spin_square(self, skp):
        """
        Calculate a single instance of a spin squared LLT symmetric function
        associated with a partition, list of partitions, or a list of skew partitions.

        This family of symmetric functions is defined in [LT2000]_ equation (43).

        INPUT:

        - ``self`` -- a family of LLT symmetric functions bases
        - ``skp`` -- a partition of a list of partitions or a list of skew
          partitions

        OUTPUT:

        the monomial expansion of the LLT symmetric function spin-square
        functions indexed by ``skp``

        EXAMPLES::

            sage: L3 = SymmetricFunctions(FractionField(QQ['t'])).llt(3)
            sage: L3.spin_square([2,1])
            t*m[1]
            sage: L3.spin_square([3,2,1])
            (t^3+t)*m[1, 1] + t^3*m[2]
            sage: L3.spin_square([[1],[1],[1]])
            (t^6+2*t^4+2*t^2+1)*m[1, 1, 1] + (t^6+t^4+t^2)*m[2, 1] + t^6*m[3]
            sage: L3.spin_square([[[2,2],[1]],[[2,1],[]]])
            (2*t^4+3*t^2+1)*m[1, 1, 1, 1] + (t^4+t^2)*m[2, 1, 1] + t^4*m[2, 2]
        """
    def cospin(self, skp):
        """
        Calculate a single instance of the cospin symmetric functions.

        These are the functions defined in [LLT1997]_ equation (26).

        INPUT:

        - ``self`` -- a family of LLT symmetric functions bases
        - ``skp`` -- a partition or a list of partitions or a list of skew
          partitions

        OUTPUT:

        the monomial expansion of the LLT symmetric function cospin
        functions indexed by ``skp``

        EXAMPLES::

            sage: Sym = SymmetricFunctions(FractionField(QQ['t']))
            sage: L3 = Sym.llt(3)
            sage: L3.cospin([2,1])
            m[1]
            sage: L3.cospin([3,2,1])
            (t+1)*m[1, 1] + m[2]
            sage: s = Sym.schur()
            sage: s(L3.cospin([[2],[1],[2]]))
            t^4*s[2, 2, 1] + t^3*s[3, 1, 1] + (t^3+t^2)*s[3, 2] + (t^2+t)*s[4, 1] + s[5]
        """
    def hcospin(self):
        """
        Return the HCospin basis.
        This basis is defined [LLT1997]_ equation (27).

        INPUT:

        - ``self`` -- a family of LLT symmetric functions bases

        OUTPUT: the h-cospin basis of the LLT symmetric functions

        EXAMPLES::

            sage: Sym = SymmetricFunctions(FractionField(QQ['t']))
            sage: HCosp3 = Sym.llt(3).hcospin(); HCosp3
            Symmetric Functions over Fraction Field of Univariate Polynomial Ring in t over Rational Field in the level 3 LLT cospin basis
            sage: HCosp3([1])^2
            1/t*HCosp3[1, 1] + ((t-1)/t)*HCosp3[2]

            sage: s = Sym.schur()
            sage: HCosp3(s([2]))
            HCosp3[2]
            sage: HCosp3(s([1,1]))
            1/t*HCosp3[1, 1] - 1/t*HCosp3[2]
            sage: s(HCosp3([2,1]))
            t*s[2, 1] + s[3]
        """
    def hspin(self):
        """
        Return the HSpin basis.

        This basis is defined [LLT1997]_ equation (28).

        INPUT:

        - ``self`` -- a family of LLT symmetric functions bases

        OUTPUT: the h-spin basis of the LLT symmetric functions

        EXAMPLES::

            sage: Sym = SymmetricFunctions(FractionField(QQ['t']))
            sage: HSp3 = Sym.llt(3).hspin(); HSp3
            Symmetric Functions over Fraction Field of Univariate Polynomial Ring in t over Rational Field in the level 3 LLT spin basis
            sage: HSp3([1])^2
            HSp3[1, 1] + (-t+1)*HSp3[2]

            sage: s = Sym.schur()
            sage: HSp3(s([2]))
            HSp3[2]
            sage: HSp3(s([1,1]))
            HSp3[1, 1] - t*HSp3[2]
            sage: s(HSp3([2,1]))
            s[2, 1] + t*s[3]
        """

class LLT_generic(sfa.SymmetricFunctionAlgebra_generic):
    t: Incomplete
    def __init__(self, llt, prefix) -> None:
        """
        A class of methods which are common to both the hspin and hcospin
        of the LLT symmetric functions.

        INPUT:

        - ``self`` -- an instance of the LLT hspin or hcospin basis
        - ``llt`` -- a family of LLT symmetric functions

        EXAMPLES::

            sage: SymmetricFunctions(FractionField(QQ['t'])).llt(3).hspin()
            Symmetric Functions over Fraction Field of Univariate Polynomial Ring in t over Rational Field in the level 3 LLT spin basis
            sage: SymmetricFunctions(QQ).llt(3,t=2).hspin()
            Symmetric Functions over Rational Field in the level 3 LLT spin with t=2 basis
            sage: QQz = FractionField(QQ['z']); z = QQz.gen()
            sage: SymmetricFunctions(QQz).llt(3,t=z).hspin()
            Symmetric Functions over Fraction Field of Univariate Polynomial Ring in z over Rational Field in the level 3 LLT spin with t=z basis
        """
    def construction(self):
        """
        Return a pair ``(F, R)``, where ``F`` is a
        :class:`SymmetricFunctionsFunctor` and `R` is a ring, such
        that ``F(R)`` returns ``self``.

        EXAMPLES::

            sage: Sym = SymmetricFunctions(FractionField(QQ['t']))
            sage: HSp3 = Sym.llt(3).hspin()
            sage: HSp3.construction()
            (SymmetricFunctionsFunctor[level 3 LLT spin],
             Fraction Field of Univariate Polynomial Ring in t over Rational Field)
        """
    def level(self):
        """
        Return the level of ``self``.

        INPUT:

        - ``self`` -- an instance of the LLT hspin or hcospin basis

        OUTPUT: the level associated to the basis ``self``

        EXAMPLES::

            sage: HSp3 = SymmetricFunctions(FractionField(QQ['t'])).llt(3).hspin()
            sage: HSp3.level()
            3
        """
    def llt_family(self):
        """
        The family of the llt bases of the symmetric functions.

        INPUT:

        - ``self`` -- an instance of the LLT hspin or hcospin basis

        OUTPUT: an instance of the family of LLT bases associated to ``self``

        EXAMPLES::

            sage: HSp3 = SymmetricFunctions(FractionField(QQ['t'])).llt(3).hspin()
            sage: HSp3.llt_family()
            level 3 LLT polynomials over Fraction Field of Univariate Polynomial Ring in t over Rational Field
        """
    def product(self, left, right):
        """
        Convert to the monomial basis, do the multiplication there, and
        convert back to the basis ``self``.

        INPUT:

        - ``self`` -- an instance of the LLT hspin or hcospin basis
        - ``left``, ``right`` -- elements of the symmetric functions

        OUTPUT: the product of ``left`` and ``right`` expanded in the basis ``self``

        EXAMPLES::

            sage: HSp3 = SymmetricFunctions(FractionField(QQ['t'])).llt(3).hspin()
            sage: HSp3.product(HSp3([1]), HSp3([2]))
            HSp3[2, 1] + (-t+1)*HSp3[3]
            sage: HCosp3 = SymmetricFunctions(FractionField(QQ['t'])).llt(3).hcospin()
            sage: HCosp3.product(HCosp3([1]), HSp3([2]))
            1/t*HCosp3[2, 1] + ((t-1)/t)*HCosp3[3]
        """
    class Element(sfa.SymmetricFunctionAlgebra_generic.Element): ...

class LLT_spin(LLT_generic):
    def __init__(self, llt) -> None:
        '''
        A class of methods for the h-spin LLT basis of the symmetric functions.

        INPUT:

        - ``self`` -- an instance of the LLT hcospin basis
        - ``llt`` -- a family of LLT symmetric function bases

        TESTS::

            sage: HSp3 = SymmetricFunctions(FractionField(QQ[\'t\'])).llt(3).hspin()
            sage: TestSuite(HSp3).run(skip = ["_test_associativity", "_test_distributivity", "_test_prod"]) # products are too expensive, long time (10s on sage.math, 2012)
            sage: TestSuite(HSp3).run(elements = [HSp3.t*HSp3[1,1]+HSp3.t*HSp3[2], HSp3[1]+(1+HSp3.t)*HSp3[1,1]])  # long time (depends on previous)

        ::

            sage: HS3t2 = SymmetricFunctions(QQ).llt(3,t=2).hspin()
            sage: TestSuite(HS3t2).run() # products are too expensive, long time (7s on sage.math, 2012)

        ::

            sage: HS3x = SymmetricFunctions(FractionField(QQ[\'x\'])).llt(3,t=x).hspin()
            sage: TestSuite(HS3x).run(skip = ["_test_associativity", "_test_distributivity", "_test_prod"]) # products are too expensive, long time (4s on sage.math, 2012)
            sage: TestSuite(HS3x).run(elements = [HS3x.t*HS3x[1,1]+HS3x.t*HS3x[2], HS3x[1]+(1+HS3x.t)*HS3x[1,1]])  # long time (depends on previous)
        '''
    class Element(LLT_generic.Element): ...

class LLT_cospin(LLT_generic):
    def __init__(self, llt) -> None:
        '''
        A class of methods for the h-cospin LLT basis of the symmetric functions.

        INPUT:

        - ``self`` -- an instance of the LLT hcospin basis
        - ``llt`` -- a family of LLT symmetric function bases

        TESTS::

            sage: HCosp3 = SymmetricFunctions(FractionField(QQ[\'t\'])).llt(3).hcospin()
            sage: TestSuite(HCosp3).run(skip = ["_test_associativity", "_test_distributivity", "_test_prod"]) # products are too expensive, long time (11s on sage.math, 2012)
            sage: TestSuite(HCosp3).run(elements = [HCosp3.t*HCosp3[1,1]+HCosp3.t*HCosp3[2], HCosp3[1]+(1+HCosp3.t)*HCosp3[1,1]])  # long time (depends on previous)

        ::

            sage: HC3t2 = SymmetricFunctions(QQ).llt(3,t=2).hcospin()
            sage: TestSuite(HC3t2).run() # products are too expensive, long time (6s on sage.math, 2012)

        ::

            sage: HC3x = SymmetricFunctions(FractionField(QQ[\'x\'])).llt(3,t=x).hcospin()
            sage: TestSuite(HC3x).run(skip = ["_test_associativity", "_test_distributivity", "_test_prod"]) # products are too expensive, long time (5s on sage.math, 2012)
            sage: TestSuite(HC3x).run(elements = [HC3x.t*HC3x[1,1]+HC3x.t*HC3x[2], HC3x[1]+(1+HC3x.t)*HC3x[1,1]])  # long time (depends on previous)
        '''
    class Element(LLT_generic.Element): ...
