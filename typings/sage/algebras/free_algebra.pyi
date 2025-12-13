from _typeshed import Incomplete
from sage.algebras.free_algebra_element import FreeAlgebraElement as FreeAlgebraElement
from sage.categories.algebras_with_basis import AlgebrasWithBasis as AlgebrasWithBasis
from sage.categories.functor import Functor as Functor
from sage.categories.pushout import CompositeConstructionFunctor as CompositeConstructionFunctor, ConstructionFunctor as ConstructionFunctor, IdentityConstructionFunctor as IdentityConstructionFunctor
from sage.categories.rings import Rings as Rings
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.combinat.words.word import Word as Word
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.monoids.free_monoid import FreeMonoid as FreeMonoid
from sage.monoids.free_monoid_element import FreeMonoidElement as FreeMonoidElement
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.structure.category_object import normalize_names as normalize_names
from sage.structure.coerce_exceptions import CoercionException as CoercionException
from sage.structure.factory import UniqueFactory as UniqueFactory

class FreeAlgebraFactory(UniqueFactory):
    '''
    A constructor of free algebras.

    See :mod:`~sage.algebras.free_algebra` for examples and corner cases.

    EXAMPLES::

        sage: FreeAlgebra(GF(5),3,\'x\')
        Free Algebra on 3 generators (x0, x1, x2) over Finite Field of size 5
        sage: F.<x,y,z> = FreeAlgebra(GF(5),3)
        sage: (x+y+z)^2
        x^2 + x*y + x*z + y*x + y^2 + y*z + z*x + z*y + z^2
        sage: FreeAlgebra(GF(5),3, \'xx, zba, Y\')
        Free Algebra on 3 generators (xx, zba, Y) over Finite Field of size 5
        sage: FreeAlgebra(GF(5),3, \'abc\')
        Free Algebra on 3 generators (a, b, c) over Finite Field of size 5
        sage: FreeAlgebra(GF(5),1, \'z\')
        Free Algebra on 1 generator (z,) over Finite Field of size 5
        sage: FreeAlgebra(GF(5),1, [\'alpha\'])
        Free Algebra on 1 generator (alpha,) over Finite Field of size 5
        sage: FreeAlgebra(FreeAlgebra(ZZ,1,\'a\'), 2, \'x\')
        Free Algebra on 2 generators (x0, x1) over
         Free Algebra on 1 generator (a,) over Integer Ring

    Free algebras are globally unique::

        sage: F = FreeAlgebra(ZZ,3,\'x,y,z\')
        sage: G = FreeAlgebra(ZZ,3,\'x,y,z\')
        sage: F is G
        True
        sage: F.<x,y,z> = FreeAlgebra(GF(5),3)  # indirect doctest
        sage: F is loads(dumps(F))
        True
        sage: F is FreeAlgebra(GF(5),[\'x\',\'y\',\'z\'])
        True
        sage: copy(F) is F is loads(dumps(F))
        True
        sage: TestSuite(F).run()

    By :issue:`7797`, we provide a different implementation of free
    algebras, based on Singular\'s "letterplace rings". Our letterplace
    wrapper allows for choosing positive integral degree weights for the
    generators of the free algebra. However, only (weighted) homogeneous
    elements are supported. Of course, isomorphic algebras in different
    implementations are not identical::

        sage: # needs sage.libs.singular
        sage: G = FreeAlgebra(GF(5),[\'x\',\'y\',\'z\'], implementation=\'letterplace\')
        sage: F == G
        False
        sage: G is FreeAlgebra(GF(5),[\'x\',\'y\',\'z\'], implementation=\'letterplace\')
        True
        sage: copy(G) is G is loads(dumps(G))
        True
        sage: TestSuite(G).run()

    ::

        sage: # needs sage.libs.singular
        sage: H = FreeAlgebra(GF(5), [\'x\',\'y\',\'z\'], implementation=\'letterplace\',
        ....:                 degrees=[1,2,3])
        sage: F != H != G
        True
        sage: H is FreeAlgebra(GF(5),[\'x\',\'y\',\'z\'], implementation=\'letterplace\',
        ....:                  degrees=[1,2,3])
        True
        sage: copy(H) is H is loads(dumps(H))
        True
        sage: TestSuite(H).run()

    Free algebras commute with their base ring.
    ::

        sage: K.<a,b> = FreeAlgebra(QQ,2)
        sage: K.is_commutative()
        False
        sage: L.<c> = FreeAlgebra(K,1)
        sage: L.is_commutative()
        False
        sage: s = a*b^2 * c^3; s
        a*b^2*c^3
        sage: parent(s)
        Free Algebra on 1 generator (c,) over
         Free Algebra on 2 generators (a, b) over Rational Field
        sage: c^3 * a * b^2
        a*b^2*c^3
    '''
    def create_key(self, base_ring, arg1=None, arg2=None, sparse=None, order=None, names=None, name=None, implementation=None, degrees=None):
        """
        Create the key under which a free algebra is stored.

        TESTS::

            sage: FreeAlgebra.create_key(GF(5),['x','y','z'])
            (Finite Field of size 5, ('x', 'y', 'z'))
            sage: FreeAlgebra.create_key(GF(5),['x','y','z'],3)
            (Finite Field of size 5, ('x', 'y', 'z'))
            sage: FreeAlgebra.create_key(GF(5),3,'xyz')
            (Finite Field of size 5, ('x', 'y', 'z'))

            sage: # needs sage.libs.singular
            sage: FreeAlgebra.create_key(GF(5),['x','y','z'],
            ....:                        implementation='letterplace')
            (Multivariate Polynomial Ring in x, y, z over Finite Field of size 5,)
            sage: FreeAlgebra.create_key(GF(5),['x','y','z'],3,
            ....:                        implementation='letterplace')
            (Multivariate Polynomial Ring in x, y, z over Finite Field of size 5,)
            sage: FreeAlgebra.create_key(GF(5),3,'xyz',
            ....:                        implementation='letterplace')
            (Multivariate Polynomial Ring in x, y, z over Finite Field of size 5,)
            sage: FreeAlgebra.create_key(GF(5),3,'xyz',
            ....:                        implementation='letterplace', degrees=[1,2,3])
            ((1, 2, 3), Multivariate Polynomial Ring in x, y, z, x_ over Finite Field of size 5)
        """
    def create_object(self, version, key):
        """
        Construct the free algebra that belongs to a unique key.

        NOTE:

        Of course, that method should not be called directly,
        since it does not use the cache of free algebras.

        TESTS::

            sage: FreeAlgebra.create_object('4.7.1', (QQ['x','y'],))
            Free Associative Unital Algebra on 2 generators (x, y) over Rational Field
            sage: FreeAlgebra.create_object('4.7.1', (QQ['x','y'],)) is FreeAlgebra(QQ,['x','y'])
            False
        """

FreeAlgebra: FreeAlgebraFactory = FreeAlgebraFactory('FreeAlgebra')

def is_FreeAlgebra(x) -> bool:
    """
    Return ``True`` if x is a free algebra; otherwise, return ``False``.

    EXAMPLES::

        sage: from sage.algebras.free_algebra import is_FreeAlgebra
        sage: is_FreeAlgebra(5)
        doctest:warning...
        DeprecationWarning: the function is_FreeAlgebra is deprecated;
        use 'isinstance(..., (FreeAlgebra_generic, FreeAlgebra_letterplace))' instead
        See https://github.com/sagemath/sage/issues/37896 for details.
        False
        sage: is_FreeAlgebra(ZZ)
        False
        sage: is_FreeAlgebra(FreeAlgebra(ZZ,100,'x'))
        True
        sage: is_FreeAlgebra(FreeAlgebra(ZZ,10,'x',implementation='letterplace'))
        True
        sage: is_FreeAlgebra(FreeAlgebra(ZZ,10,'x',implementation='letterplace',
        ....:                            degrees=list(range(1,11))))
        True
    """

class FreeAlgebra_generic(CombinatorialFreeModule):
    """
    The free algebra on `n` generators over a base ring.

    INPUT:

    - ``R`` -- a ring
    - ``n`` -- integer
    - ``names`` -- the generator names
    - ``degrees`` -- (optional) a tuple or list specifying the
      degrees of all the generators, if omitted, the algebra is not
      graded

    EXAMPLES::

        sage: F.<x,y,z> = FreeAlgebra(QQ, 3); F
        Free Algebra on 3 generators (x, y, z) over Rational Field
        sage: mul(F.gens())
        x*y*z
        sage: mul([ F.gen(i%3) for i in range(12) ])
        x*y*z*x*y*z*x*y*z*x*y*z
        sage: mul([ F.gen(i%3) for i in range(12) ]) + mul([ F.gen(i%2) for i in range(12) ])
        x*y*x*y*x*y*x*y*x*y*x*y + x*y*z*x*y*z*x*y*z*x*y*z
        sage: (2 + x*z + x^2)^2 + (x - y)^2
        4 + 5*x^2 - x*y + 4*x*z - y*x + y^2 + x^4 + x^3*z + x*z*x^2 + x*z*x*z

    TESTS:

    Free algebras commute with their base ring::

        sage: K.<a,b> = FreeAlgebra(QQ)
        sage: K.is_commutative()
        False
        sage: L.<c,d> = FreeAlgebra(K)
        sage: L.is_commutative()
        False
        sage: s = a*b^2 * c^3; s
        a*b^2*c^3
        sage: parent(s)
        Free Algebra on 2 generators (c, d) over Free Algebra on 2 generators (a, b) over Rational Field
        sage: c^3 * a * b^2
        a*b^2*c^3

    Two free algebras are considered the same if they have the same
    base ring, number of generators and variable names, and the same
    implementation::

        sage: F = FreeAlgebra(QQ,3,'x')
        sage: F == FreeAlgebra(QQ,3,'x')
        True
        sage: F is FreeAlgebra(QQ,3,'x')
        True
        sage: F == FreeAlgebra(ZZ,3,'x')
        False
        sage: F == FreeAlgebra(QQ,4,'x')
        False
        sage: F == FreeAlgebra(QQ,3,'y')
        False

    Note that since :issue:`7797` there is a different
    implementation of free algebras. Two corresponding free
    algebras in different implementations are not equal, but there
    is a coercion.
    """
    Element = FreeAlgebraElement
    def __init__(self, R, n, names, degrees=None) -> None:
        """
        The free algebra on `n` generators over a base ring.

        EXAMPLES::

            sage: F.<x,y,z> = FreeAlgebra(QQ, 3); F # indirect doctest
            Free Algebra on 3 generators (x, y, z) over Rational Field

        TESTS:

        Note that the following is *not* the recommended way to create
        a free algebra::

            sage: from sage.algebras.free_algebra import FreeAlgebra_generic
            sage: FreeAlgebra_generic(ZZ, 3, 'abc')
            Free Algebra on 3 generators (a, b, c) over Integer Ring
        """
    def construction(self):
        """
        Return the construction of ``self``.

        EXAMPLES::

            sage: F, R = algebras.Free(QQ,4,'x,y,z,t').construction(); F
            Associative[x,y,z,t]
        """
    def one_basis(self):
        """
        Return the index of the basis element `1`.

        EXAMPLES::

            sage: F = FreeAlgebra(QQ, 2, 'x,y')
            sage: F.one_basis()
            1
            sage: F.one_basis().parent()
            Free monoid on 2 generators (x, y)
        """
    def is_field(self, proof: bool = True) -> bool:
        """
        Return ``True`` if this Free Algebra is a field.

        This happens only if the
        base ring is a field and there are no generators

        EXAMPLES::

            sage: A = FreeAlgebra(QQ,0,'')
            sage: A.is_field()
            True
            sage: A = FreeAlgebra(QQ,1,'x')
            sage: A.is_field()
            False
        """
    def gen(self, i):
        """
        The ``i``-th generator of the algebra.

        EXAMPLES::

            sage: F = FreeAlgebra(ZZ,3,'x,y,z')
            sage: F.gen(0)
            x
        """
    @cached_method
    def algebra_generators(self):
        """
        Return the algebra generators of ``self``.

        EXAMPLES::

            sage: F = FreeAlgebra(ZZ,3,'x,y,z')
            sage: F.algebra_generators()
            Finite family {'x': x, 'y': y, 'z': z}
        """
    @cached_method
    def gens(self) -> tuple:
        """
        Return the generators of ``self``.

        EXAMPLES::

            sage: F = FreeAlgebra(ZZ,3,'x,y,z')
            sage: F.gens()
            (x, y, z)
        """
    def degree_on_basis(self, m):
        """
        Return the degree of the basis element indexed by ``m``.

        EXAMPLES::

            sage: A.<a, b> = FreeAlgebra(QQ, degrees=(1, -1))
            sage: m = A.basis().keys()[42]
            sage: m
            a*b*a*b^2
            sage: A.degree_on_basis(m)
            -1
            sage: (a*b*a*b^2).degree()
            -1
        """
    def product_on_basis(self, x, y):
        """
        Return the product of the basis elements indexed by ``x`` and ``y``.

        EXAMPLES::

            sage: F = FreeAlgebra(ZZ,3,'x,y,z')
            sage: I = F.basis().keys()
            sage: x,y,z = I.gens()
            sage: F.product_on_basis(x*y, z*y)
            x*y*z*y
        """
    def quotient(self, mons, mats=None, names=None, **args):
        """
        Return a quotient algebra.

        The quotient algebra is defined via the action of a free algebra
        `A` on a (finitely generated) free module. The input for the quotient
        algebra is a list of monomials (in the underlying monoid for `A`)
        which form a free basis for the module of `A`, and a list of
        matrices, which give the action of the free generators of `A` on this
        monomial basis.

        EXAMPLES:

        Here is the quaternion algebra defined in terms of three generators::

            sage: n = 3
            sage: A = FreeAlgebra(QQ,n,'i')
            sage: F = A.monoid()
            sage: i, j, k = F.gens()
            sage: mons = [ F(1), i, j, k ]
            sage: M = MatrixSpace(QQ,4)
            sage: mats = [M([0,1,0,0, -1,0,0,0, 0,0,0,-1, 0,0,1,0]),
            ....:         M([0,0,1,0, 0,0,0,1, -1,0,0,0, 0,-1,0,0]),
            ....:         M([0,0,0,1, 0,0,-1,0, 0,1,0,0, -1,0,0,0]) ]
            sage: H.<i,j,k> = A.quotient(mons, mats); H
            Free algebra quotient on 3 generators ('i', 'j', 'k') and dimension 4
             over Rational Field
        """
    quo = quotient
    def ngens(self):
        """
        The number of generators of the algebra.

        EXAMPLES::

            sage: F = FreeAlgebra(ZZ,3,'x,y,z')
            sage: F.ngens()
            3
        """
    def monoid(self):
        """
        The free monoid of generators of the algebra.

        EXAMPLES::

            sage: F = FreeAlgebra(ZZ,3,'x,y,z')
            sage: F.monoid()
            Free monoid on 3 generators (x, y, z)
        """
    def g_algebra(self, relations, names=None, order: str = 'degrevlex', check: bool = True):
        """
        The `G`-Algebra derived from this algebra by relations.

        By default it is assumed that any two variables commute.

        .. TODO::

            - Coercion doesn't work yet, there is some cheating about assumptions
            - The optional argument ``check`` controls checking the degeneracy
              conditions. Furthermore, the default values interfere with
              non-degeneracy conditions.

        EXAMPLES::

            sage: # needs sage.libs.singular
            sage: A.<x,y,z> = FreeAlgebra(QQ,3)
            sage: G = A.g_algebra({y*x: -x*y})
            sage: (x,y,z) = G.gens()
            sage: x*y
            x*y
            sage: y*x
            -x*y
            sage: z*x
            x*z
            sage: (x,y,z) = A.gens()
            sage: G = A.g_algebra({y*x: -x*y + 1})
            sage: (x,y,z) = G.gens()
            sage: y*x
            -x*y + 1
            sage: (x,y,z) = A.gens()
            sage: G = A.g_algebra({y*x: -x*y + z})
            sage: (x,y,z) = G.gens()
            sage: y*x
            -x*y + z

        TESTS::

            sage: S = FractionField(QQ['t'])
            sage: t = S.gen()
            sage: F.<x,y> = FreeAlgebra(S)
            sage: K = F.g_algebra({y*x:-x*y+1+y})
            sage: x,y = K.gens()
            sage: 1+t*y*x
            (-t)*x*y + t*y + (t + 1)
        """
    def poincare_birkhoff_witt_basis(self):
        """
        Return the Poincaré-Birkhoff-Witt (PBW) basis of ``self``.

        EXAMPLES::

            sage: F.<x,y> = FreeAlgebra(QQ, 2)
            sage: F.poincare_birkhoff_witt_basis()
            The Poincare-Birkhoff-Witt basis of Free Algebra on 2 generators (x, y) over Rational Field
        """
    pbw_basis = poincare_birkhoff_witt_basis
    def pbw_element(self, elt):
        """
        Return the element ``elt`` in the Poincaré-Birkhoff-Witt basis.

        EXAMPLES::

            sage: F.<x,y> = FreeAlgebra(QQ, 2)
            sage: F.pbw_element(x*y - y*x + 2)
            2*PBW[1] + PBW[x*y]
            sage: F.pbw_element(F.one())
            PBW[1]
            sage: F.pbw_element(x*y*x + x^3*y)
            PBW[x*y]*PBW[x] + PBW[y]*PBW[x]^2 + PBW[x^3*y]
             + 3*PBW[x^2*y]*PBW[x] + 3*PBW[x*y]*PBW[x]^2 + PBW[y]*PBW[x]^3
        """
    def lie_polynomial(self, w):
        """
        Return the Lie polynomial associated to the Lyndon word ``w``. If
        ``w`` is not Lyndon, then return the product of Lie polynomials of
        the Lyndon factorization of ``w``.

        Given a Lyndon word `w`, the Lie polynomial `L_w` is defined
        recursively by `L_w = [L_u, L_v]`, where `w = uv` is the
        :meth:`standard factorization
        <sage.combinat.words.finite_word.FiniteWord_class.standard_factorization>`
        of `w`, and `L_w = w` when `w` is a single letter.

        INPUT:

        - ``w`` -- a word or an element of the free monoid

        EXAMPLES::

            sage: F = FreeAlgebra(QQ, 3, 'x,y,z')
            sage: M.<x,y,z> = FreeMonoid(3)
            sage: F.lie_polynomial(x*y)
            x*y - y*x
            sage: F.lie_polynomial(y*x)
            y*x
            sage: F.lie_polynomial(x^2*y*x)
            x^2*y*x - 2*x*y*x^2 + y*x^3
            sage: F.lie_polynomial(y*z*x*z*x*z)
            y*z*x*z*x*z - y*z*x*z^2*x - y*z^2*x^2*z + y*z^2*x*z*x
             - z*y*x*z*x*z + z*y*x*z^2*x + z*y*z*x^2*z - z*y*z*x*z*x

        TESTS:

        We test some corner cases and alternative inputs::

            sage: F = FreeAlgebra(QQ, 3, 'x,y,z')
            sage: M.<x,y,z> = FreeMonoid(3)
            sage: F.lie_polynomial(Word('xy'))
            x*y - y*x
            sage: F.lie_polynomial('xy')
            x*y - y*x
            sage: F.lie_polynomial(M.one())
            1
            sage: F.lie_polynomial(Word([]))
            1
            sage: F.lie_polynomial('')
            1

        We check that :issue:`22251` is fixed::

            sage: F.lie_polynomial(x*y*z)
            x*y*z - x*z*y - y*z*x + z*y*x
        """

class PBWBasisOfFreeAlgebra(CombinatorialFreeModule):
    """
    The Poincaré-Birkhoff-Witt basis of the free algebra.

    EXAMPLES::

        sage: F.<x,y> = FreeAlgebra(QQ, 2)
        sage: PBW = F.pbw_basis()
        sage: px, py = PBW.gens()
        sage: px * py
        PBW[x*y] + PBW[y]*PBW[x]
        sage: py * px
        PBW[y]*PBW[x]
        sage: px * py^3 * px - 2*px * py
        -2*PBW[x*y] - 2*PBW[y]*PBW[x] + PBW[x*y^3]*PBW[x]
         + 3*PBW[y]*PBW[x*y^2]*PBW[x] + 3*PBW[y]^2*PBW[x*y]*PBW[x]
         + PBW[y]^3*PBW[x]^2

    We can convert between the two bases::

        sage: p = PBW(x*y - y*x + 2); p
        2*PBW[1] + PBW[x*y]
        sage: F(p)
        2 + x*y - y*x
        sage: f = F.pbw_element(x*y*x + x^3*y + x + 3)
        sage: F(PBW(f)) == f
        True
        sage: p = px*py + py^4*px^2
        sage: F(p)
        x*y + y^4*x^2
        sage: PBW(F(p)) == p
        True

    Note that multiplication in the PBW basis agrees with multiplication
    as monomials::

        sage: F(px * py^3 * px - 2*px * py) == x*y^3*x - 2*x*y
        True

    We verify Examples 1 and 2 in [MR1989]_::

        sage: F.<x,y,z> = FreeAlgebra(QQ)
        sage: PBW = F.pbw_basis()
        sage: PBW(x*y*z)
        PBW[x*y*z] + PBW[x*z*y] + PBW[y]*PBW[x*z] + PBW[y*z]*PBW[x]
         + PBW[z]*PBW[x*y] + PBW[z]*PBW[y]*PBW[x]
        sage: PBW(x*y*y*x)
        PBW[x*y^2]*PBW[x] + 2*PBW[y]*PBW[x*y]*PBW[x] + PBW[y]^2*PBW[x]^2

    TESTS:

    Check that going between the two bases is the identity::

        sage: F = FreeAlgebra(QQ, 2, 'x,y')
        sage: PBW = F.pbw_basis()
        sage: M = F.monoid()
        sage: L = [j.to_monoid_element() for i in range(6) for j in Words('xy', i)]
        sage: all(PBW(F(PBW(m))) == PBW(m) for m in L)
        True
        sage: all(F(PBW(F(m))) == F(m) for m in L)
        True
    """
    @staticmethod
    def __classcall_private__(cls, R, n=None, names=None):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: from sage.algebras.free_algebra import PBWBasisOfFreeAlgebra
            sage: PBW1 = FreeAlgebra(QQ, 2, 'x,y').pbw_basis()
            sage: PBW2.<x,y> = PBWBasisOfFreeAlgebra(QQ)
            sage: PBW3 = PBWBasisOfFreeAlgebra(QQ, 2, ['x','y'])
            sage: PBW1 is PBW2 and PBW2 is PBW3
            True
        """
    def __init__(self, alg) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: PBW = FreeAlgebra(QQ, 2, 'x,y').pbw_basis()
            sage: TestSuite(PBW).run()
        """
    def one_basis(self):
        """
        Return the index of the basis element for `1`.

        EXAMPLES::

            sage: PBW = FreeAlgebra(QQ, 2, 'x,y').pbw_basis()
            sage: PBW.one_basis()
            1
            sage: PBW.one_basis().parent()
            Free monoid on 2 generators (x, y)
        """
    def algebra_generators(self):
        """
        Return the generators of ``self`` as an algebra.

        EXAMPLES::

            sage: PBW = FreeAlgebra(QQ, 2, 'x,y').pbw_basis()
            sage: gens = PBW.algebra_generators(); gens
            (PBW[x], PBW[y])
            sage: all(g.parent() is PBW for g in gens)
            True
        """
    gens = algebra_generators
    def gen(self, i):
        """
        Return the ``i``-th generator of ``self``.

        EXAMPLES::

            sage: PBW = FreeAlgebra(QQ, 2, 'x,y').pbw_basis()
            sage: PBW.gen(0)
            PBW[x]
            sage: PBW.gen(1)
            PBW[y]
        """
    def free_algebra(self):
        """
        Return the associated free algebra of ``self``.

        EXAMPLES::

            sage: PBW = FreeAlgebra(QQ, 2, 'x,y').pbw_basis()
            sage: PBW.free_algebra()
            Free Algebra on 2 generators (x, y) over Rational Field
        """
    def product(self, u, v):
        """
        Return the product of two elements ``u`` and ``v``.

        EXAMPLES::

            sage: F = FreeAlgebra(QQ, 2, 'x,y')
            sage: PBW = F.pbw_basis()
            sage: x, y = PBW.gens()
            sage: PBW.product(x, y)
            PBW[x*y] + PBW[y]*PBW[x]
            sage: PBW.product(y, x)
            PBW[y]*PBW[x]
            sage: PBW.product(y^2*x, x*y*x)
            PBW[y]^2*PBW[x^2*y]*PBW[x] + 2*PBW[y]^2*PBW[x*y]*PBW[x]^2 + PBW[y]^3*PBW[x]^3

        TESTS:

        Check that multiplication agrees with the multiplication in the
        free algebra::

            sage: F = FreeAlgebra(QQ, 2, 'x,y')
            sage: PBW = F.pbw_basis()
            sage: x, y = PBW.gens()
            sage: F(x*y)
            x*y
            sage: F(x*y*x)
            x*y*x
            sage: PBW(F(x)*F(y)*F(x)) == x*y*x
            True
        """
    def expansion(self, t):
        """
        Return the expansion of the element ``t`` of the Poincaré-Birkhoff-Witt
        basis in the monomials of the free algebra.

        EXAMPLES::

            sage: F = FreeAlgebra(QQ, 2, 'x,y')
            sage: PBW = F.pbw_basis()
            sage: x,y = F.monoid().gens()
            sage: PBW.expansion(PBW(x*y))
            x*y - y*x
            sage: PBW.expansion(PBW.one())
            1
            sage: PBW.expansion(PBW(x*y*x) + 2*PBW(x) + 3)
            3 + 2*x + x*y*x - y*x^2

        TESTS:

        Check that we have the correct parent::

            sage: PBW.expansion(PBW(x*y)).parent() is F
            True
            sage: PBW.expansion(PBW.one()).parent() is F
            True
        """
    class Element(CombinatorialFreeModule.Element):
        def expand(self):
            """
            Expand ``self`` in the monomials of the free algebra.

            EXAMPLES::

                sage: F = FreeAlgebra(QQ, 2, 'x,y')
                sage: PBW = F.pbw_basis()
                sage: x,y = F.monoid().gens()
                sage: f = PBW(x^2*y) + PBW(x) + PBW(y^4*x)
                sage: f.expand()
                x + x^2*y - 2*x*y*x + y*x^2 + y^4*x
            """

class AssociativeFunctor(ConstructionFunctor):
    """
    A constructor for free associative algebras.

    EXAMPLES::

        sage: P = algebras.Free(ZZ, 2, 'x,y')
        sage: x,y = P.gens()
        sage: F = P.construction()[0]; F
        Associative[x,y]

        sage: A = GF(5)['a,b']
        sage: a, b = A.gens()
        sage: F(A)
        Free Algebra on 2 generators (x, y) over Multivariate Polynomial Ring in a, b over Finite Field of size 5

        sage: f = A.hom([a+b,a-b],A)
        sage: F(f)
        Generic endomorphism of Free Algebra on 2 generators (x, y)
        over Multivariate Polynomial Ring in a, b over Finite Field of size 5

        sage: F(f)(a * F(A)(x))
        (a+b)*x
    """
    rank: int
    vars: Incomplete
    degs: Incomplete
    def __init__(self, vars, degs=None) -> None:
        """
        EXAMPLES::

            sage: from sage.algebras.free_algebra import AssociativeFunctor
            sage: F = AssociativeFunctor(['x','y'])
            sage: F
            Associative[x,y]
            sage: F(ZZ)
            Free Algebra on 2 generators (x, y)  over Integer Ring
        """
    def __eq__(self, other):
        """
        EXAMPLES::

            sage: F = algebras.Free(ZZ, 3, 'x,y,z').construction()[0]
            sage: G = algebras.Free(QQ, 3, 'x,y,z').construction()[0]
            sage: F == G
            True
            sage: G == loads(dumps(G))
            True
            sage: G = algebras.Free(QQ, 2, 'x,y').construction()[0]
            sage: F == G
            False
        """
    def __mul__(self, other):
        """
        If two Associative functors are given in a row, form a single Associative functor
        with all of the variables.

        EXAMPLES::

            sage: from sage.algebras.free_algebra import AssociativeFunctor
            sage: F = AssociativeFunctor(['x','y'])
            sage: G = AssociativeFunctor(['t'])
            sage: G * F
            Associative[x,y,t]
        """
    def merge(self, other):
        """
        Merge ``self`` with another construction functor, or return ``None``.

        EXAMPLES::

            sage: from sage.algebras.free_algebra import AssociativeFunctor
            sage: F = AssociativeFunctor(['x','y'])
            sage: G = AssociativeFunctor(['t'])
            sage: F.merge(G)
            Associative[x,y,t]
            sage: F.merge(F)
            Associative[x,y]

        With degrees::

            sage: F = AssociativeFunctor(['x','y'], (2,3))
            sage: G = AssociativeFunctor(['t'], (4,))
            sage: H = AssociativeFunctor(['z','y'], (5,3))
            sage: F.merge(G)
            Associative[x,y,t] with degrees (2, 3, 4)
            sage: F.merge(H)
            Associative[x,y,z] with degrees (2, 3, 5)

        Now some actual use cases::

            sage: R = algebras.Free(ZZ, 3, 'x,y,z')
            sage: x,y,z = R.gens()
            sage: 1/2 * x
            1/2*x
            sage: parent(1/2 * x)
            Free Algebra on 3 generators (x, y, z) over Rational Field

            sage: S = algebras.Free(QQ, 2, 'z,t')
            sage: z,t = S.gens()
            sage: x + t
            t + x
            sage: parent(x + t)
            Free Algebra on 4 generators (z, t, x, y) over Rational Field

        TESTS::

            sage: F = AssociativeFunctor(['x','y'], (2,3))
            sage: H = AssociativeFunctor(['z','y'], (5,4))
            sage: F.merge(H)
        """
