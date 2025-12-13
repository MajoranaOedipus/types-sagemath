from sage.categories.action import Action as Action
from sage.categories.fields import Fields as Fields
from sage.categories.ore_modules import OreModules as OreModules
from sage.matrix.constructor import matrix as matrix
from sage.matrix.matrix0 import Matrix as Matrix
from sage.matrix.special import identity_matrix as identity_matrix
from sage.misc.latex import latex as latex, latex_variable_name as latex_variable_name
from sage.modules.free_module import FreeModule_ambient as FreeModule_ambient
from sage.modules.free_module_element import FreeModuleElement_generic_dense as FreeModuleElement_generic_dense
from sage.modules.ore_module_element import OreModuleElement as OreModuleElement
from sage.rings.polynomial.ore_polynomial_element import OrePolynomial as OrePolynomial
from sage.structure.sequence import Sequence as Sequence
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class ScalarAction(Action):
    """
    Action by scalar multiplication on Ore modules.
    """
class OreAction(Action):
    """
    Action by left multiplication of Ore polynomial rings
    over Ore modules.
    """

def normalize_names(names, rank):
    """
    Return a normalized form of ``names``.

    INPUT:

    - ``names`` -- a string, a list of strings or ``None``

    - ``rank`` -- the number of names to normalize

    EXAMPLES::

        sage: from sage.modules.ore_module import normalize_names

    When ``names`` is a string, indices are added::

        sage: normalize_names('e', 3)
        ('e0', 'e1', 'e2')

    When ``names`` is a list or a tuple, it remains untouched
    except that it is always casted to a tuple (in order to be
    hashable and serve as a key)::

        sage: normalize_names(['u', 'v', 'w'], 3)
        ('u', 'v', 'w')

    Similarly, when ``names`` is ``None``, nothing is returned::

        sage: normalize_names(None, 3)

    If the number of names is not equal to ``rank``, an error
    is raised::

        sage: normalize_names(['u', 'v', 'w'], 2)
        Traceback (most recent call last):
        ...
        ValueError: the number of given names does not match the rank of the Ore module
    """

class OreModule(UniqueRepresentation, FreeModule_ambient):
    """
    Generic class for Ore modules.
    """
    Element = OreModuleElement
    def __classcall_private__(cls, mat, twist, names=None, category=None):
        """
        Normalize the input before passing it to the init function
        (useful to ensure the uniqueness assumption).

        INPUT:

        - ``mat`` -- the matrix defining the action of the Ore variable

        - ``twist`` -- the twisting morphism/derivation

        - ``names`` (default: ``None``) -- a string of a list of strings,
          the names of the vector of the canonical basis; if ``None``,
          elements are represented as vectors in `K^d`

        - ``category`` (default: ``None``) -- the category of this
          Ore module

        TESTS::

            sage: K.<z> = GF(5^3)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: P = X^2 + z

            sage: M1 = S.quotient_module(P)
            sage: M2 = S.quotient_module(P, names='e')
            sage: M3.<e0,e1> = S.quotient_module(P)

            sage: M1 is M2
            False
            sage: M2 is M3
            True
        """
    def __init__(self, mat, ore, names, category) -> None:
        """
        Initialize this Ore module.

        INPUT:

        - ``mat`` -- the matrix defining the action of the Ore variable

        - ``ore`` -- the underlying Ore polynomial ring

        - ``names`` -- a string of a list of strings,
          the names of the vector of the canonical basis; if ``None``,
          elements are represented as vectors in `K^d`

        - ``category`` -- the category of this Ore module

        TESTS::

            sage: K.<z> = GF(5^3)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: M = S.quotient_module(X^2 + z)  # indirect doctest
            sage: type(M)
            <class 'sage.modules.ore_module.OreModule_with_category'>

            sage: TestSuite(M).run()
        """
    def is_zero(self) -> bool:
        """
        Return ``True`` if this Ore module is reduced to zero.

        EXAMPLES::

            sage: K.<z> = GF(5^3)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: M = S.quotient_module(X^2 + z)
            sage: M
            Ore module of rank 2 over Finite Field in z of size 5^3 twisted by z |--> z^5
            sage: M.is_zero()
            False

            sage: Q = M.quo(M)
            sage: Q.is_zero()
            True
        """
    def rename_basis(self, names, coerce: bool = False):
        """
        Return the same Ore module with the given naming
        for the vectors in its distinguished basis.

        INPUT:

        - ``names`` -- a string or a list of strings, the
          new names

        - ``coerce`` (default: ``False``) -- a boolean; if
          ``True``, a coercion map from this Ore module to
          renamed version is set

        EXAMPLES::

            sage: K.<z> = GF(5^3)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: M = S.quotient_module(X^2 + z)
            sage: M
            Ore module of rank 2 over Finite Field in z of size 5^3 twisted by z |--> z^5

            sage: Me = M.rename_basis('e')
            sage: Me
            Ore module <e0, e1> over Finite Field in z of size 5^3 twisted by z |--> z^5

        Now compare how elements are displayed::

            sage: M.random_element()   # random
            (3*z^2 + 4*z + 2, 3*z^2 + z)
            sage: Me.random_element()  # random
            (2*z+4)*e0 + (z^2+4*z+4)*e1

        At this point, there is no coercion map between ``M``
        and ``Me``. Therefore, adding elements in both parents
        results in an error::

            sage: M.random_element() + Me.random_element()
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for +:
            'Ore module of rank 2 over Finite Field in z of size 5^3 twisted by z |--> z^5' and
            'Ore module <e0, e1> over Finite Field in z of size 5^3 twisted by z |--> z^5'

        In order to set this coercion, one should define ``Me``
        by passing the extra argument ``coerce=True``::

            sage: Me = M.rename_basis('e', coerce=True)
            sage: M.random_element() + Me.random_element()  # random
            2*z^2*e0 + (z^2+z+4)*e1

        .. WARNING::

            Use ``coerce=True`` with extreme caution. Indeed,
            setting inappropriate coercion maps may result in a
            circular path in the coercion graph which, in turn,
            could eventually break the coercion system.

        Note that the bracket construction also works::

            sage: M.<v,w> = M.rename_basis()
            sage: M
            Ore module <v, w> over Finite Field in z of size 5^3 twisted by z |--> z^5

        In this case, `v` and `w` are automatically defined::

            sage: v + w
            v + w
        """
    def pseudohom(self):
        """
        Return the pseudomorphism giving the action of the Ore
        variable on this Ore module.

        EXAMPLES::

            sage: K.<z> = GF(5^3)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: P = X^3 + z*X^2 - z^2*X + (z+2)
            sage: M = S.quotient_module(P)
            sage: M.pseudohom()
            Free module pseudomorphism (twisted by z |--> z^5) defined by the matrix
            [      0       1       0]
            [      0       0       1]
            [4*z + 3     z^2     4*z]
            Domain: Ore module of rank 3 over Finite Field in z of size 5^3 twisted by z |--> z^5
            Codomain: Ore module of rank 3 over Finite Field in z of size 5^3 twisted by z |--> z^5

        .. SEEALSO::

            :meth:`matrix`
        """
    def ore_ring(self, names: str = 'x', action: bool = True):
        """
        Return the underlying Ore polynomial ring.

        INPUT:

        - ``names`` (default: ``x``) -- a string, the name
          of the variable

        - ``action`` (default: ``True``) -- a boolean; if
          ``True``, an action of the Ore polynomial ring on
          the Ore module is set

        EXAMPLES::

            sage: K.<a> = GF(5^3)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: M.<e1,e2> = S.quotient_module(X^2 - a)
            sage: M.ore_ring()
            Ore Polynomial Ring in x over Finite Field in a of size 5^3 twisted by a |--> a^5

        We can use a different variable name::

            sage: M.ore_ring('Y')
            Ore Polynomial Ring in Y over Finite Field in a of size 5^3 twisted by a |--> a^5

        Alternatively, one can use the following shortcut::

            sage: T.<Z> = M.ore_ring()
            sage: T
            Ore Polynomial Ring in Z over Finite Field in a of size 5^3 twisted by a |--> a^5

        In all the above cases, an action of the returned Ore polynomial
        ring on `M` is registered::

            sage: Z*e1
            e2
            sage: Z*e2
            a*e1

        Specifying ``action=False`` prevents this to happen::

            sage: T.<U> = M.ore_ring(action=False)
            sage: U*e1
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
                'Ore Polynomial Ring in U over Finite Field in a of size 5^3 twisted by a |--> a^5' and
                'Ore module <e1, e2> over Finite Field in a of size 5^3 twisted by a |--> a^5'
        """
    def twisting_morphism(self):
        """
        Return the twisting morphism corresponding to this Ore module.

        EXAMPLES::

            sage: K.<z> = GF(5^3)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: M = S.quotient_module(X + z)
            sage: M.twisting_morphism()
            Frobenius endomorphism z |--> z^5 on Finite Field in z of size 5^3

        When the twisting morphism is trivial (that is, the identity),
        nothing is returned::

            sage: R.<t> = QQ[]
            sage: T.<Y> = OrePolynomialRing(R, R.derivation())
            sage: M = T.quotient_module(Y + t^2)
            sage: M.twisting_morphism()

        .. SEEALSO::

            :meth:`twisting_derivation`
        """
    def twisting_derivation(self):
        """
        Return the twisting derivation corresponding to this Ore module.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: T.<Y> = OrePolynomialRing(R, R.derivation())
            sage: M = T.quotient_module(Y + t^2)
            sage: M.twisting_derivation()
            d/dt

        When the twisting derivation in zero, nothing is returned::

            sage: K.<z> = GF(5^3)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: M = S.quotient_module(X + z)
            sage: M.twisting_derivation()

        .. SEEALSO::

            :meth:`twisting_morphism`
        """
    def matrix(self):
        """
        Return the matrix giving the action of the Ore variable
        on this Ore module.

        EXAMPLES::

            sage: K.<z> = GF(5^3)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: P = X^3 + z*X^2 - z^2*X + (z+2)
            sage: M = S.quotient_module(P)
            sage: M.matrix()
            [      0       1       0]
            [      0       0       1]
            [4*z + 3     z^2     4*z]

        We recognize the companion matrix attached to the Ore
        polynomial `P`. This is of course not a coincidence given
        that the pseudomorphism corresponds to the left multiplication

        .. SEEALSO::

            :meth:`pseudohom`
        """
    def basis(self) -> list:
        """
        Return the canonical basis of this Ore module.

        EXAMPLES::

            sage: K.<z> = GF(5^3)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: M = S.quotient_module(X^3 - z)
            sage: M.basis()
            [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
        """
    def gens(self) -> list:
        """
        Return the canonical basis of this Ore module.

        EXAMPLES::

            sage: K.<z> = GF(5^3)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: M = S.quotient_module(X^3 - z)
            sage: M.gens()
            [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
        """
    def gen(self, i):
        """
        Return the `i`-th vector of the canonical basis
        of this Ore module.

        EXAMPLES::

            sage: K.<z> = GF(5^3)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: M = S.quotient_module(X^3 - z)
            sage: M.gen(0)
            (1, 0, 0)
            sage: M.gen(1)
            (0, 1, 0)
            sage: M.gen(2)
            (0, 0, 1)
            sage: M.gen(3)
            Traceback (most recent call last):
            ...
            IndexError: generator is not defined
        """
    def random_element(self, *args, **kwds):
        """
        Return a random element in this Ore module.

        Extra arguments are passed to the random generator
        of the base ring.

        EXAMPLES::

            sage: A.<t> = QQ['t']
            sage: S.<X> = OrePolynomialRing(A, A.derivation())
            sage: M = S.quotient_module(X^3 - t, names='e')
            sage: M.random_element()   # random
            (-1/2*t^2 - 3/4*t + 3/2)*e0 + (-3/2*t^2 - 3*t + 4)*e1 + (-6*t + 2)*e2

            sage: M.random_element(degree=5)   # random
            (4*t^5 - 1/2*t^4 + 3/2*t^3 + 6*t^2 - t - 1/10)*e0 + (19/3*t^5 - t^3 - t^2 + 1)*e1 + (t^5 + 4*t^4 + 4*t^2 + 1/3*t - 33)*e2
        """
    def module(self):
        """
        Return the underlying free module of this Ore module.

        EXAMPLES::

            sage: A.<t> = QQ['t']
            sage: S.<X> = OrePolynomialRing(A, A.derivation())
            sage: M = S.quotient_module(X^3 - t)
            sage: M
            Ore module of rank 3 over Univariate Polynomial Ring in t over Rational Field twisted by d/dt

            sage: M.module()
            Ambient free module of rank 3 over the principal ideal domain Univariate Polynomial Ring in t over Rational Field
        """
    def hom(self, im_gens, codomain=None):
        """
        Return the morphism from this Ore module to ``codomain``
        defined by ``im_gens``.

        INPUT:

        - ``im_gens`` -- a datum defining the morphism to build;
          it could either a list, a tuple, a dictionary or a morphism
          of Ore modules

        - ``codomain`` (default: ``None``) -- a Ore module, the
          codomain of the morphism; if ``None``, it is inferred from
          ``im_gens``

        EXAMPLES::

            sage: K.<t> = Frac(GF(5)['t'])
            sage: S.<X> = OrePolynomialRing(K, K.derivation())
            sage: P = X^3 + 2*t*X^2 + (t^2 + 2)*X + t
            sage: Q = t*X^2 - X + 1

            sage: U = S.quotient_module(P, names='u')
            sage: U.inject_variables()
            Defining u0, u1, u2
            sage: V = S.quotient_module(P*Q, names='v')
            sage: V.inject_variables()
            Defining v0, v1, v2, v3, v4

        The first method for creating a morphism from `U` to `V` is
        to explicitly write down its matrix in the canonical bases::

            sage: mat = matrix(3, 5, [1, 4, t, 0, 0,
            ....:                     0, 1, 0, t, 0,
            ....:                     0, 0, 1, 1, t])
            sage: f = U.hom(mat, codomain=V)
            sage: f
            Ore module morphism:
              From: Ore module <u0, u1, u2> over Fraction Field of Univariate Polynomial Ring in t over Finite Field of size 5 twisted by d/dt
              To:   Ore module <v0, v1, v2, v3, v4> over Fraction Field of Univariate Polynomial Ring in t over Finite Field of size 5 twisted by d/dt

        This method is however not really convenient because it
        requires to compute beforehand all the entries of the
        defining matrix.
        Instead, we can pass the list of images of the generators::

            sage: g = U.hom([Q*v0, X*Q*v0, X^2*Q*v0])
            sage: g
            Ore module morphism:
              From: Ore module <u0, u1, u2> over Fraction Field of Univariate Polynomial Ring in t over Finite Field of size 5 twisted by d/dt
              To:   Ore module <v0, v1, v2, v3, v4> over Fraction Field of Univariate Polynomial Ring in t over Finite Field of size 5 twisted by d/dt
            sage: g.matrix()
            [1 4 t 0 0]
            [0 1 0 t 0]
            [0 0 1 1 t]

        One can even give the values of the morphism on a smaller
        set as soon as the latter generates the domain as Ore module.
        The syntax uses dictionaries as follows::

            sage: h = U.hom({u0: Q*v0})
            sage: h
            Ore module morphism:
              From: Ore module <u0, u1, u2> over Fraction Field of Univariate Polynomial Ring in t over Finite Field of size 5 twisted by d/dt
              To:   Ore module <v0, v1, v2, v3, v4> over Fraction Field of Univariate Polynomial Ring in t over Finite Field of size 5 twisted by d/dt
            sage: g == h
            True

        Finally ``im_gens`` can also be itself a Ore morphism, in which
        case SageMath tries to cast it into a morphism with the requested
        domains and codomains.
        As an example below, we restrict `g` to a subspace::

            sage: C.<c0,c1> = U.span((X + t)*u0)
            sage: gC = C.hom(g)
            sage: gC
            Ore module morphism:
              From: Ore module <c0, c1> over Fraction Field of Univariate Polynomial Ring in t over Finite Field of size 5 twisted by d/dt
              To:   Ore module <v0, v1, v2, v3, v4> over Fraction Field of Univariate Polynomial Ring in t over Finite Field of size 5 twisted by d/dt

            sage: g(c0) == gC(c0)
            True
            sage: g(c1) == gC(c1)
            True

        TESTS::

            sage: U.hom(0)
            Traceback (most recent call last):
            ...
            ValueError: im_gens must be a list, a tuple, a dictionary, a matrix or a Ore module morphism

            sage: U.hom([Q*v0])
            Traceback (most recent call last):
            ...
            ValueError: wrong number of generators

            sage: U.hom({u0: Q*v0, u1: Q*v0})
            Traceback (most recent call last):
            ...
            ValueError: does not define a morphism of Ore modules

            sage: U.hom({(X+t)*u0: (X+t)*Q*v0})
            Traceback (most recent call last):
            ...
            ValueError: does not define a morphism of Ore modules
        """
    def multiplication_map(self, P):
        """
        Return the multiplication by `P` acting on this Ore module.

        INPUT:

        - ``P`` -- a scalar in the base ring, or a Ore polynomial

        EXAMPLES::

            sage: K.<a> = GF(7^5)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: P = X^3 + a*X^2 + X - a^2
            sage: M = S.quotient_module(P)

        We define the scalar multiplication by an element in the base ring::

            sage: f = M.multiplication_map(3)
            sage: f
            Ore module endomorphism of Ore module of rank 3 over Finite Field in a of size 7^5 twisted by a |--> a^7
            sage: f.matrix()
            [3 0 0]
            [0 3 0]
            [0 0 3]

        Be careful that an element in the base ring defines a Ore morphism
        if and only if it is fixed by the twisting morphisms and killed by
        the derivation (otherwise the multiplication by this element does
        not commute with the Ore action).
        In SageMath, attempting to create the multiplication by an element
        which does not fulfill these requirements leads to an error::

            sage: M.multiplication_map(a)
            Traceback (most recent call last):
            ...
            ValueError: does not define a morphism of Ore modules

        As soon as it defines a Ore morphism, one can also build the left
        multiplication by an Ore polynomial::

            sage: g = M.multiplication_map(X^5)
            sage: g
            Ore module endomorphism of Ore module of rank 3 over Finite Field in a of size 7^5 twisted by a |--> a^7
            sage: g.matrix()
            [    3*a^4 + 3*a^3 + 6*a^2 + 5*a       4*a^4 + 5*a^3 + 2*a^2 + 6         6*a^4 + 6*a^3 + a^2 + 4]
            [                        a^2 + 3 5*a^4 + 5*a^3 + 6*a^2 + 4*a + 1                 a^3 + 5*a^2 + 4]
            [6*a^4 + 6*a^3 + 3*a^2 + 3*a + 1         4*a^4 + 2*a^3 + 3*a + 5 6*a^4 + 6*a^3 + 2*a^2 + 5*a + 2]

        We check that the characteristic polynomial of `g` is the reduced
        norm of the Ore polynomial `P` we started with (this is a classical
        property)::

            sage: g.charpoly()
            x^3 + 4*x^2 + 2*x + 5
            sage: P.reduced_norm(var='x')
            x^3 + 4*x^2 + 2*x + 5
        """
    def identity_morphism(self):
        """
        Return the identity morphism of this Ore module.

        EXAMPLES::

            sage: K.<a> = GF(7^5)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: M.<u,v> = S.quotient_module(X^2 + a*X + a^2)
            sage: id = M.identity_morphism()
            sage: id
            Ore module endomorphism of Ore module <u, v> over Finite Field in a of size 7^5 twisted by a |--> a^7

            sage: id(u)
            u
            sage: id(v)
            v
        """
    def span(self, gens, names=None):
        """
        Return the submodule of this Ore module generated (over the
        underlying Ore ring) by ``gens``.

        INPUT:

        - ``gens`` -- a list of vectors or submodules of this Ore module

        - ``names`` (default: ``None``) -- the name of the vectors in a
          basis of this submodule

        EXAMPLES::

            sage: K.<t> = Frac(GF(5)['t'])
            sage: S.<X> = OrePolynomialRing(K, K.derivation())
            sage: P = X^2 + t*X + 1
            sage: M = S.quotient_module(P^3, names='e')
            sage: M.inject_variables()
            Defining e0, e1, e2, e3, e4, e5

        We create the submodule `M P`::

            sage: MP = M.span([P*e0])
            sage: MP
            Ore module of rank 4 over Fraction Field of Univariate Polynomial Ring in t over Finite Field of size 5 twisted by d/dt
            sage: MP.basis()
            [e0 + (t^4+t^2+3)*e4 + t^3*e5,
             e1 + (4*t^3+2*t)*e4 + (4*t^2+3)*e5,
             e2 + (2*t^2+2)*e4 + 2*t*e5,
             e3 + 4*t*e4 + 4*e5]

        When there is only one generator, encapsulating it in a list is
        not necessary; one can equally write::

            sage: MP = M.span(P*e0)

        If one wants, one can give names to the basis of the submodule using
        the attribute ``names``::

            sage: MP2 = M.span(P^2*e0, names='u')
            sage: MP2.inject_variables()
            Defining u0, u1
            sage: MP2.basis()
            [u0, u1]

            sage: M(u0)
            e0 + (t^2+4)*e2 + 3*t^3*e3 + (t^2+1)*e4 + 3*t*e5

        Note that a coercion map from the submodule to the ambient module
        is automatically set::

            sage: M.has_coerce_map_from(MP2)
            True

        Therefore, combining elements of ``M`` and ``MP2`` in the same
        expression perfectly works::

            sage: t*u0 + e1
            t*e0 + e1 + (t^3+4*t)*e2 + 3*t^4*e3 + (t^3+t)*e4 + 3*t^2*e5

        Here is an example with multiple generators::

            sage: MM = M.span([MP2, P*e1])
            sage: MM.basis()
            [e0, e1, e2, e3, e4, e5]

        In this case, we obtain the whole space.

        Creating submodules of submodules is also allowed::

            sage: N = MP.span(P^2*e0)
            sage: N
            Ore module of rank 2 over Fraction Field of Univariate Polynomial Ring in t over Finite Field of size 5 twisted by d/dt
            sage: N.basis()
            [e0 + (t^2+4)*e2 + 3*t^3*e3 + (t^2+1)*e4 + 3*t*e5,
             e1 + (4*t^2+4)*e3 + 3*t*e4 + 4*e5]

        .. SEEALSO::

            :meth:`quotient`
        """
    def quotient(self, sub, names=None, check: bool = True):
        """
        Return the quotient of this Ore module by the submodule
        generated (over the underlying Ore ring) by ``gens``.

        INPUT:

        - ``gens`` -- a list of vectors or submodules of this Ore module

        - ``names`` (default: ``None``) -- the name of the vectors in a
          basis of the quotient

        - ``check`` (default: ``True``) -- a boolean, ignored

        EXAMPLES::

            sage: K.<t> = Frac(GF(5)['t'])
            sage: S.<X> = OrePolynomialRing(K, K.derivation())
            sage: P = X^2 + t*X + 1
            sage: M = S.quotient_module(P^3, names='e')
            sage: M.inject_variables()
            Defining e0, e1, e2, e3, e4, e5

        We create the quotient `M/MP`::

            sage: modP = M.quotient(P*e0)
            sage: modP
            Ore module of rank 2 over Fraction Field of Univariate Polynomial Ring in t over Finite Field of size 5 twisted by d/dt

        As a shortcut, we can write ``quo`` instead of ``quotient`` or even
        use the ``/`` operator::

            sage: modP = M / (P*e0)
            sage: modP
            Ore module of rank 2 over Fraction Field of Univariate Polynomial Ring in t over Finite Field of size 5 twisted by d/dt

        By default, the vectors in the quotient have the same names as their
        representatives in `M`::

            sage: modP.basis()
            [e4, e5]

        One can override this behavior by setting the attributes ``names``::

            sage: modP = M.quo(P*e0, names='u')
            sage: modP.inject_variables()
            Defining u0, u1
            sage: modP.basis()
            [u0, u1]

        Note that a coercion map from the initial Ore module to its quotient
        is automatically set. As a consequence, combining elements of ``M``
        and ``modP`` in the same formula works::

            sage: t*u0 + e1
            (t^3+4*t)*u0 + (t^2+2)*u1

        One can combine the construction of quotients and submodules without
        trouble. For instance, here we build the space `M P / M P^2`::

            sage: modP2 = M / (P^2*e0)
            sage: N = modP2.span(P*e0)
            sage: N
            Ore module of rank 2 over Fraction Field of Univariate Polynomial Ring in t over Finite Field of size 5 twisted by d/dt
            sage: N.basis()
            [e2 + (2*t^2+2)*e4 + 2*t*e5,
             e3 + 4*t*e4 + 4*e5]

        .. SEEALSO::

            :meth:`quo`, :meth:`span`
        """
    quo = quotient
    def __eq__(self, other) -> bool:
        """
        Return ``True`` if this Ore module is the same than ``other``.

        TESTS:

        Different names lead to different parents::

            sage: K.<a> = GF(7^5)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: M.<u,v> = S.quotient_module(X^2 + a*X + a^2)
            sage: N.<e0,e1> = S.quotient_module(X^2 + a*X + a^2)
            sage: M == N
            False

        However, different syntaxes resulting in the same names lead
        to the same parent::

            sage: N2 = S.quotient_module(X^2 + a*X + a^2, names='e')
            sage: N == N2
            True
        """
    def __hash__(self) -> int:
        """
        Return a hash of this Ore module.

        TESTS::

            sage: K.<z> = GF(5^3)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: M = S.quotient_module(X^3 - z)
            sage: hash(M)  # random
            128873304640624
        """

class OreSubmodule(OreModule):
    """
    Class for submodules of Ore modules.
    """
    def __classcall_private__(cls, ambient, gens, names):
        """
        Normalize the input before passing it to the init function
        (useful to ensure the uniqueness assupmtion).

        INPUT:

        - ``ambient`` -- a Ore module, the ambient module where
          this submodule sits

        - ``gens`` -- a list of generators (formatted as coordinates
          vectors) of this submodule

        - ``names`` -- the name of the vectors of the basis of
          the submodule, or ``None``

        TESTS::

            sage: K.<z> = GF(5^3)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: M.<v,w> = S.quotient_module((X + z)^2)
            sage: N1 = M.span((X + z)*v)
            sage: N2 = M.span((X + z^5)*w)
            sage: N1 is N2
            True

        ::

            sage: R.<t> = QQ[]
            sage: S.<X> = OrePolynomialRing(R, R.derivation())
            sage: M.<v,w> = S.quotient_module((X + t)^2)
            sage: M.span((X + t)*v)
            Traceback (most recent call last):
            ...
            NotImplementedError: Ore submodules are currently only implemented over fields
        """
    def __init__(self, ambient, basis, names) -> None:
        """
        Initialize this Ore submodule.

        INPUT:

        - ``ambient`` -- a Ore module, the ambient module where
          this submodule sits

        - ``basis`` -- the echelon basis of this submodule

        - ``names`` -- the name of the vectors of the basis of
          the submodule, or ``None``

        TESTS::

            sage: K.<z> = GF(5^3)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: M.<v,w> = S.quotient_module((X + z)^2)
            sage: N = M.span((X + z)*v)  # indirect doctest
            sage: type(N)
            <class 'sage.modules.ore_module.OreSubmodule_with_category'>

            sage: TestSuite(N).run()
        """
    def ambient(self):
        """
        Return the ambient Ore module in which this submodule lives.

        EXAMPLES::

            sage: K.<z> = GF(5^3)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: M.<v,w> = S.quotient_module((X + z)^2)
            sage: N = M.span((X + z)*v)
            sage: N.ambient()
            Ore module <v, w> over Finite Field in z of size 5^3 twisted by z |--> z^5
            sage: N.ambient() is M
            True
        """
    def rename_basis(self, names, coerce: bool = False):
        """
        Return the same Ore module with the given naming
        for the vectors in its distinguished basis.

        INPUT:

        - ``names`` -- a string or a list of strings, the
          new names

        - ``coerce`` (default: ``False``) -- a boolean; if
          ``True``, a coercion map from this Ore module to
          renamed version is set

        EXAMPLES::

            sage: K.<z> = GF(5^3)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: M = S.quotient_module(X^2 + z^2)
            sage: M
            Ore module of rank 2 over Finite Field in z of size 5^3 twisted by z |--> z^5

            sage: Me = M.rename_basis('e')
            sage: Me
            Ore module <e0, e1> over Finite Field in z of size 5^3 twisted by z |--> z^5

        Now compare how elements are displayed::

            sage: M.random_element()   # random
            (3*z^2 + 4*z + 2, 3*z^2 + z)
            sage: Me.random_element()  # random
            (2*z + 4)*e0 + (z^2 + 4*z + 4)*e1

        At this point, there is no coercion map between ``M``
        and ``Me``. Therefore, adding elements in both parents
        results in an error::

            sage: M.random_element() + Me.random_element()
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for +:
            'Ore module of rank 2 over Finite Field in z of size 5^3 twisted by z |--> z^5' and
            'Ore module <e0, e1> over Finite Field in z of size 5^3 twisted by z |--> z^5'

        In order to set this coercion, one should define ``Me``
        by passing the extra argument ``coerce=True``::

            sage: Me = M.rename_basis('e', coerce=True)
            sage: M.random_element() + Me.random_element()  # random
            2*z^2*e0 + (z^2 + z + 4)*e1

        .. WARNING::

            Use ``coerce=True`` with extreme caution. Indeed,
            setting inappropriate coercion maps may result in a
            circular path in the coercion graph which, in turn,
            could eventually break the coercion system.

        Note that the bracket construction also works::

            sage: M.<v,w> = M.rename_basis()
            sage: M
            Ore module <v, w> over Finite Field in z of size 5^3 twisted by z |--> z^5

        In this case, `v` and `w` are automatically defined::

            sage: v + w
            v + w

        TESTS::

            sage: K.<z> = GF(5^3)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: P = X + z
            sage: A.<v,w> = S.quotient_module(P^2)
            sage: M = A.span(P*v)
            sage: Me = M.rename_basis('e', coerce=True)
            sage: M.an_element() + Me.an_element()
            2*e0
        """
    def injection_morphism(self):
        """
        Return the inclusion of this submodule in the ambient space.

        EXAMPLES::

            sage: K.<z> = GF(5^3)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: M.<v,w> = S.quotient_module((X + z)^2)
            sage: N = M.span((X + z)*v)
            sage: N.injection_morphism()
            Ore module morphism:
              From: Ore module of rank 1 over Finite Field in z of size 5^3 twisted by z |--> z^5
              To:   Ore module <v, w> over Finite Field in z of size 5^3 twisted by z |--> z^5
        """
    def morphism_restriction(self, f):
        """
        Return the restriction of `f` to this submodule.

        EXAMPLES::

            sage: K.<z> = GF(5^3)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: M.<v,w> = S.quotient_module((X + z)^2)
            sage: N = M.span((X + z)*v)

            sage: f = M.multiplication_map(X^3)
            sage: f
            Ore module endomorphism of Ore module <v, w> over Finite Field in z of size 5^3 twisted by z |--> z^5

            sage: g = N.morphism_restriction(f)
            sage: g
            Ore module morphism:
              From: Ore module of rank 1 over Finite Field in z of size 5^3 twisted by z |--> z^5
              To:   Ore module <v, w> over Finite Field in z of size 5^3 twisted by z |--> z^5
            sage: g.matrix()
            [        3 4*z^2 + 2]

        TESTS::

            sage: N.morphism_restriction(g)
            Traceback (most recent call last):
            ...
            ValueError: the domain of the morphism must be the ambient space
        """
    def morphism_corestriction(self, f):
        """
        If the image of `f` is contained in this submodule,
        return the corresponding corestriction of `f`.

        EXAMPLES::

            sage: K.<z> = GF(5^3)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: P = X + z
            sage: M.<v,w> = S.quotient_module(P^2)
            sage: N = M.span(P*v)

            sage: f = M.hom({v: P*v})
            sage: f
            Ore module endomorphism of Ore module <v, w> over Finite Field in z of size 5^3 twisted by z |--> z^5

            sage: g = N.morphism_corestriction(f)
            sage: g
            Ore module morphism:
              From: Ore module <v, w> over Finite Field in z of size 5^3 twisted by z |--> z^5
              To:   Ore module of rank 1 over Finite Field in z of size 5^3 twisted by z |--> z^5
            sage: g.matrix()
            [    z]
            [4*z^2]

        When the image of the morphism is not contained in this submodule,
        an error is raised::

            sage: h = M.multiplication_map(X^3)
            sage: N.morphism_corestriction(h)
            Traceback (most recent call last):
            ...
            ValueError: the image of the morphism is not contained in this submodule

        TESTS::

            sage: N.morphism_corestriction(g)
            Traceback (most recent call last):
            ...
            ValueError: the codomain of the morphism must be the ambient space
        """

class OreQuotientModule(OreModule):
    """
    Class for quotients of Ore modules.
    """
    def __classcall_private__(cls, cover, gens, names):
        """
        Normalize the input before passing it to the init function
        (useful to ensure the uniqueness assumption).

        INPUT:

        - ``cover`` -- a Ore module, the cover module of this
          quotient

        - ``gens`` -- a list of generators (formatted as coordinates
          vectors) of the submodule by which we quotient out

        - ``names`` -- the name of the vectors of the basis of
          the quotient, or ``None``

        TESTS::

            sage: K.<t> = Frac(GF(5)['t'])
            sage: S.<X> = OrePolynomialRing(K, K.derivation())
            sage: M.<v,w> = S.quotient_module((X + t)^2)
            sage: Q1 = M.quo((X + t)*v)
            sage: Q2 = M.quo(v + (X + t)*w)
            sage: Q1 is Q2
            True

        ::

            sage: R.<t> = QQ[]
            sage: S.<X> = OrePolynomialRing(R, R.derivation())
            sage: M.<v,w> = S.quotient_module((X + t)^2)
            sage: M.quo((X + t)*v)
            Traceback (most recent call last):
            ...
            NotImplementedError: quotient of Ore modules are currently only implemented over fields
        """
    def __init__(self, cover, basis, names) -> None:
        """
        Initialize this Ore quotient.

        INPUT:

        - ``cover`` -- a Ore module, the cover module of this
          quotient

        - ``basis`` -- the echelon basis of the submodule
          defining the quotient

        - ``names`` -- the name of the vectors of the basis of
          the submodule, or ``None``

        TESTS::

            sage: K.<t> = Frac(GF(5)['t'])
            sage: S.<X> = OrePolynomialRing(K, K.derivation())
            sage: M.<v,w> = S.quotient_module((X + t)^2)
            sage: Q = M.quo((X + t)*v)  # indirect doctest
            sage: type(Q)
            <class 'sage.modules.ore_module.OreQuotientModule_with_category'>

            sage: TestSuite(N).run()
        """
    def cover(self):
        """
        If this quotient in `M/N`, return `M`.

        EXAMPLES::

            sage: K.<t> = Frac(GF(5)['t'])
            sage: S.<X> = OrePolynomialRing(K, K.derivation())
            sage: M.<v,w> = S.quotient_module((X + t)^2)
            sage: N = M.quo((X + t)*v)

            sage: N.cover()
            Ore module <v, w> over Fraction Field of Univariate Polynomial Ring in t over Finite Field of size 5 twisted by d/dt
            sage: N.cover() is M
            True

        .. SEEALSO::

            :meth:`relations`
        """
    def relations(self, names=None):
        """
        If this quotient in `M/N`, return `N`.

        INPUT:

        - ``names`` -- the names of the vectors of the basis
          of `N`, or ``None``

        EXAMPLES::

            sage: K.<t> = Frac(GF(5)['t'])
            sage: S.<X> = OrePolynomialRing(K, K.derivation())
            sage: M.<v,w> = S.quotient_module((X + t)^2)
            sage: Q = M.quo((X + t)*v)

            sage: N = Q.relations()
            sage: N
            Ore module of rank 1 over Fraction Field of Univariate Polynomial Ring in t over Finite Field of size 5 twisted by d/dt
            sage: (X + t)*v in N
            True
            sage: Q == M/N
            True

        It is also possible to define names for the basis elements
        of `N`::

            sage: N.<u> = Q.relations()
            sage: N
            Ore module <u> over Fraction Field of Univariate Polynomial Ring in t over Finite Field of size 5 twisted by d/dt
            sage: M(u)
            v + 1/t*w

        .. SEEALSO::

            :meth:`relations`
        """
    def rename_basis(self, names, coerce: bool = False):
        """
        Return the same Ore module with the given naming
        for the vectors in its distinguished basis.

        INPUT:

        - ``names`` -- a string or a list of strings, the
          new names

        - ``coerce`` (default: ``False``) -- a boolean; if
          ``True``, a coercion map from this Ore module to
          the renamed version is set

        EXAMPLES::

            sage: K.<z> = GF(5^3)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: M = S.quotient_module(X^2 + z*X + 1)
            sage: M
            Ore module of rank 2 over Finite Field in z of size 5^3 twisted by z |--> z^5

            sage: Me = M.rename_basis('e')
            sage: Me
            Ore module <e0, e1> over Finite Field in z of size 5^3 twisted by z |--> z^5

        Now compare how elements are displayed::

            sage: M.random_element()   # random
            (3*z^2 + 4*z + 2, 3*z^2 + z)
            sage: Me.random_element()  # random
            (2*z + 4)*e0 + (z^2 + 4*z + 4)*e1

        At this point, there is no coercion map between ``M``
        and ``Me``. Therefore, adding elements in both parents
        results in an error::

            sage: M.random_element() + Me.random_element()
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for +:
            'Ore module of rank 2 over Finite Field in z of size 5^3 twisted by z |--> z^5' and
            'Ore module <e0, e1> over Finite Field in z of size 5^3 twisted by z |--> z^5'

        In order to set this coercion, one should define ``Me``
        by passing the extra argument ``coerce=True``::

            sage: Me = M.rename_basis('e', coerce=True)
            sage: M.random_element() + Me.random_element()  # random
            2*z^2*e0 + (z^2 + z + 4)*e1

        .. WARNING::

            Use ``coerce=True`` with extreme caution. Indeed,
            setting inappropriate coercion maps may result in a
            circular path in the coercion graph which, in turn,
            could eventually break the coercion system.

        Note that the bracket construction also works::

            sage: M.<v,w> = M.rename_basis()
            sage: M
            Ore module <v, w> over Finite Field in z of size 5^3 twisted by z |--> z^5

        In this case, `v` and `w` are automatically defined::

            sage: v + w
            v + w

        TESTS::

            sage: K.<z> = GF(5^3)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: P = X + z
            sage: A.<v,w> = S.quotient_module(P^2)
            sage: M = A.quo(P*v)
            sage: Me = M.rename_basis('e', coerce=True)
            sage: M.an_element() + Me.an_element()
            2*e0

        """
    def projection_morphism(self):
        """
        Return the projection from the cover module to this quotient.

        EXAMPLES::

            sage: K.<t> = Frac(GF(5)['t'])
            sage: S.<X> = OrePolynomialRing(K, K.derivation())
            sage: M.<v,w> = S.quotient_module((X + t)^2)
            sage: Q = M.quo((X + t)*v)
            sage: Q.projection_morphism()
            Ore module morphism:
              From: Ore module <v, w> over Fraction Field of Univariate Polynomial Ring in t over Finite Field of size 5 twisted by d/dt
              To:   Ore module of rank 1 over Fraction Field of Univariate Polynomial Ring in t over Finite Field of size 5 twisted by d/dt
        """
    def morphism_quotient(self, f):
        """
        If this quotient in `M/N` and `f : M \\to X` is a morphism
        vanishing on `N`, return the induced map `M/N \\to X`.

        EXAMPLES::

            sage: K.<t> = Frac(GF(5)['t'])
            sage: S.<X> = OrePolynomialRing(K, K.derivation())
            sage: P = X + t
            sage: M.<v,w> = S.quotient_module(P^2)
            sage: Q.<wbar> = M.quo(P*v)

            sage: f = M.hom({v: P*v})
            sage: f
            Ore module endomorphism of Ore module <v, w> over Fraction Field of Univariate Polynomial Ring in t over Finite Field of size 5 twisted by d/dt
            sage: g = Q.morphism_quotient(f)
            sage: g
            Ore module morphism:
              From: Ore module <wbar> over Fraction Field of Univariate Polynomial Ring in t over Finite Field of size 5 twisted by d/dt
              To:   Ore module <v, w> over Fraction Field of Univariate Polynomial Ring in t over Finite Field of size 5 twisted by d/dt

        When the given morphism does not vanish on `N`, an error is raised::

            sage: h = M.multiplication_map(X^5)
            sage: h
            Ore module endomorphism of Ore module <v, w> over Fraction Field of Univariate Polynomial Ring in t over Finite Field of size 5 twisted by d/dt
            sage: Q.morphism_quotient(h)
            Traceback (most recent call last):
            ...
            ValueError: the morphism does not factor through this quotient

        TESTS::

            sage: Q.morphism_quotient(g)
            Traceback (most recent call last):
            ...
            ValueError: the domain of the morphism must be the cover ring
        """
    def morphism_modulo(self, f):
        """
        If this quotient in `M/N` and `f : X \\to M` is a morphism,
        return the induced map `X \\to M/N`.

        EXAMPLES::

            sage: K.<t> = Frac(GF(5)['t'])
            sage: S.<X> = OrePolynomialRing(K, K.derivation())
            sage: P = X + t
            sage: M.<v,w> = S.quotient_module(P^2)
            sage: Q.<wbar> = M.quo(P*v)

            sage: f = M.multiplication_map(X^5)
            sage: f
            Ore module endomorphism of Ore module <v, w> over Fraction Field of Univariate Polynomial Ring in t over Finite Field of size 5 twisted by d/dt
            sage: g = Q.morphism_modulo(f)
            sage: g
            Ore module morphism:
              From: Ore module <v, w> over Fraction Field of Univariate Polynomial Ring in t over Finite Field of size 5 twisted by d/dt
              To:   Ore module <wbar> over Fraction Field of Univariate Polynomial Ring in t over Finite Field of size 5 twisted by d/dt

        TESTS::

            sage: Q.morphism_modulo(g)
            Traceback (most recent call last):
            ...
            ValueError: the codomain of the morphism must be the cover ring
        """
