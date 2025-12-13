from sage.arith.misc import binomial as binomial, divisors as divisors, moebius as moebius
from sage.categories.homset import Hom as Hom
from sage.categories.morphism import SetMorphism as SetMorphism
from sage.combinat.sf.sfa import SymmetricFunctionAlgebra_generic as SFA_generic
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.integer import Integer as Integer

class Character_generic(SFA_generic): ...

class InducedTrivialCharacterBasis(Character_generic):
    """
    The induced trivial symmetric group character basis of
    the symmetric functions.

    This is a basis of the symmetric functions that has the
    property that ``self(la).character_to_frobenius_image(n)``
    is equal to ``h([n-sum(la)]+la)``.

    It has the property that the (outer) structure
    constants are the analogue of the stable Kronecker
    coefficients on the complete basis.

    This basis is introduced in [OZ2015]_.

    EXAMPLES::

        sage: Sym = SymmetricFunctions(QQ)
        sage: s = Sym.s()
        sage: h = Sym.h()
        sage: ht = SymmetricFunctions(QQ).ht()
        sage: st = SymmetricFunctions(QQ).st()
        sage: ht(s[2,1])
        ht[1, 1] + ht[2, 1] - ht[3]
        sage: s(ht[2,1])
        s[1] - 2*s[1, 1] - 2*s[2] + s[2, 1] + s[3]
        sage: ht(h[2,1])
        ht[1] + 2*ht[1, 1] + ht[2, 1]
        sage: h(ht[2,1])
        h[1] - 2*h[1, 1] + h[2, 1]
        sage: st(ht[2,1])
        st[] + 2*st[1] + st[1, 1] + 2*st[2] + st[2, 1] + st[3]
        sage: ht(st[2,1])
        ht[1] - ht[1, 1] + ht[2, 1] - ht[3]
        sage: ht[2]*ht[1,1]
        ht[1, 1] + 2*ht[1, 1, 1] + ht[2, 1, 1]
        sage: h[4,2].kronecker_product(h[4,1,1])
        h[2, 2, 1, 1] + 2*h[3, 1, 1, 1] + h[4, 1, 1]
        sage: s(st[2,1])
        3*s[1] - 2*s[1, 1] - 2*s[2] + s[2, 1]
        sage: st(s[2,1])
        st[] + 3*st[1] + 2*st[1, 1] + 2*st[2] + st[2, 1]
        sage: st[2]*st[1]
        st[1] + st[1, 1] + st[2] + st[2, 1] + st[3]
        sage: s[4,2].kronecker_product(s[5,1])
        s[3, 2, 1] + s[3, 3] + s[4, 1, 1] + s[4, 2] + s[5, 1]

    TESTS::

        sage: TestSuite(ht).run()
    """
    def __init__(self, Sym) -> None:
        """
        Initialize the basis and register coercions.

        The coercions are set up between the ``other_basis``.

        INPUT:

        - ``Sym`` -- an instance of the symmetric function algebra
        - ``pfix`` -- a prefix to use for the basis

        EXAMPLES::

            sage: Sym = SymmetricFunctions(QQ)
            sage: ht = SymmetricFunctions(QQ).ht(); ht
            Symmetric Functions over Rational Field in the induced trivial
             symmetric group character basis
        """

class IrreducibleCharacterBasis(Character_generic):
    """
    The irreducible symmetric group character basis of
    the symmetric functions.

    This is a basis of the symmetric functions that has the
    property that ``self(la).character_to_frobenius_image(n)``
    is equal to ``s([n-sum(la)]+la)``.

    It should also have the property that the (outer) structure
    constants are the analogue of the stable Kronecker
    coefficients on the Schur basis.

    This basis is introduced in [OZ2015]_.

    EXAMPLES::

        sage: Sym = SymmetricFunctions(QQ)
        sage: s = Sym.s()
        sage: h = Sym.h()
        sage: ht = SymmetricFunctions(QQ).ht()
        sage: st = SymmetricFunctions(QQ).st()
        sage: st(ht[2,1])
        st[] + 2*st[1] + st[1, 1] + 2*st[2] + st[2, 1] + st[3]
        sage: ht(st[2,1])
        ht[1] - ht[1, 1] + ht[2, 1] - ht[3]
        sage: s(st[2,1])
        3*s[1] - 2*s[1, 1] - 2*s[2] + s[2, 1]
        sage: st(s[2,1])
        st[] + 3*st[1] + 2*st[1, 1] + 2*st[2] + st[2, 1]
        sage: st[2]*st[1]
        st[1] + st[1, 1] + st[2] + st[2, 1] + st[3]
        sage: s[4,2].kronecker_product(s[5,1])
        s[3, 2, 1] + s[3, 3] + s[4, 1, 1] + s[4, 2] + s[5, 1]
        sage: st[1,1,1].counit()
        -1
        sage: all(sum(c*st(la)*st(mu).antipode() for
        ....:    ((la,mu),c) in st(ga).coproduct())==st(st(ga).counit())
        ....:    for ga in Partitions(3))
        True

    TESTS::

        sage: TestSuite(st).run()
    """
    def __init__(self, Sym) -> None:
        """
        Initialize the basis and register coercions.

        The coercions are set up between the ``other_basis``

        INPUT:

        - ``Sym`` -- an instance of the symmetric function algebra
        - ``pfix`` -- a prefix to use for the basis

        EXAMPLES::

            sage: Sym = SymmetricFunctions(QQ)
            sage: ht = SymmetricFunctions(QQ).ht(); ht
            Symmetric Functions over Rational Field in the induced trivial
             symmetric group character basis
            sage: st = SymmetricFunctions(QQ).st(); st
            Symmetric Functions over Rational Field in the irreducible
             symmetric group character basis
        """
