from . import sfa as sfa
from sage.combinat.partition import Partitions as Partitions
from sage.libs.lrcalc import lrcalc as lrcalc
from sage.misc.cachefunc import cached_method as cached_method

class SymmetricFunctionAlgebra_symplectic(sfa.SymmetricFunctionAlgebra_generic):
    """
    The symplectic symmetric function basis (or symplectic basis, to be short).

    The symplectic basis `\\{ sp_{\\lambda} \\}` where `\\lambda` is taken over
    all partitions is defined by the following change of basis with the
    Schur functions:

    .. MATH::

        s_{\\lambda} = \\sum_{\\mu} \\left( \\sum_{\\nu \\in V} c^{\\lambda}_{\\mu\\nu}
        \\right) sp_{\\mu}

    where `V` is the set of all partitions with even-height columns and
    `c^{\\lambda}_{\\mu\\nu}` is the usual Littlewood-Richardson (LR)
    coefficients. By the properties of LR coefficients, this can be shown to
    be a upper unitriangular change of basis.

    .. NOTE::

        This is only a filtered basis, not a `\\ZZ`-graded basis. However this
        does respect the induced `(\\ZZ/2\\ZZ)`-grading.

    INPUT:

    - ``Sym`` -- an instance of the ring of the symmetric functions

    REFERENCES:

    .. [ChariKleber2000] Vyjayanthi Chari and Michael Kleber.
       *Symmetric functions and representations of quantum affine algebras*.
       :arxiv:`math/0011161v1`

    .. [KoikeTerada1987] \\K. Koike, I. Terada, *Young-diagrammatic methods for
       the representation theory of the classical groups of type Bn, Cn, Dn*.
       J. Algebra 107 (1987), no. 2, 466-511.

    .. [ShimozonoZabrocki2006] Mark Shimozono and Mike Zabrocki.
       *Deformed universal characters for classical and affine algebras*.
       Journal of Algebra, **299** (2006). :arxiv:`math/0404288`.

    EXAMPLES:

    Here are the first few symplectic symmetric functions, in various bases::

        sage: Sym = SymmetricFunctions(QQ)
        sage: sp = Sym.sp()
        sage: e = Sym.e()
        sage: h = Sym.h()
        sage: p = Sym.p()
        sage: s = Sym.s()
        sage: m = Sym.m()

        sage: p(sp([1]))
        p[1]
        sage: m(sp([1]))
        m[1]
        sage: e(sp([1]))
        e[1]
        sage: h(sp([1]))
        h[1]
        sage: s(sp([1]))
        s[1]

        sage: p(sp([2]))
        1/2*p[1, 1] + 1/2*p[2]
        sage: m(sp([2]))
        m[1, 1] + m[2]
        sage: e(sp([2]))
        e[1, 1] - e[2]
        sage: h(sp([2]))
        h[2]
        sage: s(sp([2]))
        s[2]

        sage: p(sp([3]))
        1/6*p[1, 1, 1] + 1/2*p[2, 1] + 1/3*p[3]
        sage: m(sp([3]))
        m[1, 1, 1] + m[2, 1] + m[3]
        sage: e(sp([3]))
        e[1, 1, 1] - 2*e[2, 1] + e[3]
        sage: h(sp([3]))
        h[3]
        sage: s(sp([3]))
        s[3]

        sage: Sym = SymmetricFunctions(ZZ)
        sage: sp = Sym.sp()
        sage: e = Sym.e()
        sage: h = Sym.h()
        sage: s = Sym.s()
        sage: m = Sym.m()
        sage: p = Sym.p()
        sage: m(sp([4]))
        m[1, 1, 1, 1] + m[2, 1, 1] + m[2, 2] + m[3, 1] + m[4]
        sage: e(sp([4]))
        e[1, 1, 1, 1] - 3*e[2, 1, 1] + e[2, 2] + 2*e[3, 1] - e[4]
        sage: h(sp([4]))
        h[4]
        sage: s(sp([4]))
        s[4]

    Some examples of conversions the other way::

        sage: sp(h[3])
        sp[3]
        sage: sp(e[3])
        sp[1] + sp[1, 1, 1]
        sage: sp(m[2,1])
        -sp[1] - 2*sp[1, 1, 1] + sp[2, 1]
        sage: sp(p[3])
        sp[1, 1, 1] - sp[2, 1] + sp[3]

    Some multiplication::

        sage: sp([2]) * sp([1,1])
        sp[1, 1] + sp[2] + sp[2, 1, 1] + sp[3, 1]
        sage: sp([2,1,1]) * sp([2])
        sp[1, 1] + sp[1, 1, 1, 1] + 2*sp[2, 1, 1] + sp[2, 2] + sp[2, 2, 1, 1]
         + sp[3, 1] + sp[3, 1, 1, 1] + sp[3, 2, 1] + sp[4, 1, 1]
        sage: sp([1,1]) * sp([2,1])
        sp[1] + sp[1, 1, 1] + 2*sp[2, 1] + sp[2, 1, 1, 1] + sp[2, 2, 1]
         + sp[3] + sp[3, 1, 1] + sp[3, 2]

    Examples of the Hopf algebra structure::

        sage: sp([1]).antipode()
        -sp[1]
        sage: sp([2]).antipode()
        sp[] + sp[1, 1]
        sage: sp([1]).coproduct()
        sp[] # sp[1] + sp[1] # sp[]
        sage: sp([2]).coproduct()
        sp[] # sp[2] + sp[1] # sp[1] + sp[2] # sp[]
        sage: sp([1]).counit()
        0
        sage: sp.one().counit()
        1
    """
    def __init__(self, Sym) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: sp = SymmetricFunctions(QQ).sp()
            sage: TestSuite(sp).run()
        """
