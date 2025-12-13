from sage.categories.magmatic_algebras import MagmaticAlgebras as MagmaticAlgebras
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.modules.free_module import FreeModule as FreeModule
from sage.sets.family import Family as Family
from sage.structure.element import AlgebraElement as AlgebraElement, Matrix as Matrix
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp as richcmp
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class JordanAlgebra(UniqueRepresentation, Parent):
    """
    A Jordan algebra.

    A *Jordan algebra* is a magmatic algebra (over a commutative ring
    `R`) whose multiplication satisfies the following axioms:

    - `xy = yx`, and
    - `(xy)(xx) = x(y(xx))` (the Jordan identity).

    See [Ja1971]_, [Ch2012]_, and [McC1978]_, for example.

    These axioms imply that a Jordan algebra is power-associative and the
    following generalization of Jordan's identity holds [Al1947]_:
    `(x^m y) x^n = x^m (y x^n)` for all `m, n \\in \\ZZ_{>0}`.

    Let `A` be an associative algebra over a ring `R` in which `2` is
    invertible. We construct a Jordan algebra `A^+` with ground set `A`
    by defining the multiplication as

    .. MATH::

        x \\circ y = \\frac{xy + yx}{2}.

    Often the multiplication is written as `x \\circ y` to avoid confusion
    with the product in the associative algebra `A`. We note that if `A` is
    commutative then this reduces to the usual multiplication in `A`.

    Jordan algebras constructed in this fashion, or their subalgebras,
    are called *special*. All other Jordan algebras are called *exceptional*.

    Jordan algebras can also be constructed from a module `M` over `R` with
    a symmetric bilinear form `(\\cdot, \\cdot) : M \\times M \\to R`.
    We begin with the module `M^* = R \\oplus M` and define multiplication
    in `M^*` by

    .. MATH::

        (\\alpha + x) \\circ (\\beta + y) =
        \\underbrace{\\alpha \\beta + (x,y)}_{\\in R}
        + \\underbrace{\\beta x + \\alpha y}_{\\in M},

    where `\\alpha, \\beta \\in R` and `x,y \\in M`.

    INPUT:

    Can be either an associative algebra `A` or a symmetric bilinear
    form given as a matrix (possibly followed by, or preceded by, a base
    ring argument).

    EXAMPLES:

    We let the base algebra `A` be the free algebra on 3 generators::

        sage: F.<x,y,z> = FreeAlgebra(QQ)
        sage: J = JordanAlgebra(F); J
        Jordan algebra of Free Algebra on 3 generators (x, y, z) over Rational Field
        sage: a,b,c = map(J, F.gens())
        sage: a*b
        1/2*x*y + 1/2*y*x
        sage: b*a
        1/2*x*y + 1/2*y*x

    Jordan algebras are typically non-associative::

        sage: (a*b)*c
        1/4*x*y*z + 1/4*y*x*z + 1/4*z*x*y + 1/4*z*y*x
        sage: a*(b*c)
        1/4*x*y*z + 1/4*x*z*y + 1/4*y*z*x + 1/4*z*y*x

    We check the Jordan identity::

        sage: (a*b)*(a*a) == a*(b*(a*a))
        True
        sage: x = a + c
        sage: y = b - 2*a
        sage: (x*y)*(x*x) == x*(y*(x*x))
        True

    Next we construct a Jordan algebra from a symmetric bilinear form::

        sage: m = matrix([[-2,3],[3,4]])
        sage: J.<a,b,c> = JordanAlgebra(m); J
        Jordan algebra over Integer Ring given by the symmetric bilinear form:
        [-2  3]
        [ 3  4]
        sage: a
        1 + (0, 0)
        sage: b
        0 + (1, 0)
        sage: x = 3*a - 2*b + c; x
        3 + (-2, 1)

    We again show that Jordan algebras are usually non-associative::

        sage: (x*b)*b
        -6 + (7, 0)
        sage: x*(b*b)
        -6 + (4, -2)

    We verify the Jordan identity::

        sage: y = -a + 4*b - c
        sage: (x*y)*(x*x) == x*(y*(x*x))
        True

    The base ring, while normally inferred from the matrix, can also
    be explicitly specified::

        sage: J.<a,b,c> = JordanAlgebra(m, QQ); J
        Jordan algebra over Rational Field given by the symmetric bilinear form:
        [-2  3]
        [ 3  4]
        sage: J.<a,b,c> = JordanAlgebra(QQ, m); J # either order work
        Jordan algebra over Rational Field given by the symmetric bilinear form:
        [-2  3]
        [ 3  4]

    REFERENCES:

    - :wikipedia:`Jordan_algebra`
    - [Ja1971]_
    - [Ch2012]_
    - [McC1978]_
    - [Al1947]_
    """
    @staticmethod
    def __classcall_private__(self, arg0, arg1=None, names=None):
        """
        Choose the correct parent based upon input.

        TESTS:

        We check arguments with passing in an associative algebra::

            sage: cat = Algebras(QQ).WithBasis().FiniteDimensional()
            sage: C = CombinatorialFreeModule(QQ, ['x','y','z'], category=cat)
            sage: J1 = JordanAlgebra(C, names=['a','b','c'])
            sage: J2.<a,b,c> = JordanAlgebra(C)
            sage: J1 is J2
            True

        We check with passing in a symmetric bilinear form::

            sage: m = matrix([[0,1],[1,1]])
            sage: J1 = JordanAlgebra(m)
            sage: J2 = JordanAlgebra(QQ, m)
            sage: J3 = JordanAlgebra(m, QQ)
            sage: J1 is J2
            False
            sage: J2 is J3
            True
            sage: J4 = JordanAlgebra(ZZ, m)
            sage: J1 is J4
            True
            sage: m = matrix(QQ, [[0,1],[1,1]])
            sage: J1 = JordanAlgebra(m)
            sage: J1 is J2
            True
        """

class SpecialJordanAlgebra(JordanAlgebra):
    """
    A (special) Jordan algebra `A^+` from an associative algebra `A`.
    """
    def __init__(self, A, names=None) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: F.<x,y,z> = FreeAlgebra(QQ)
            sage: J = JordanAlgebra(F)
            sage: TestSuite(J).run()
            sage: J.category()
            Category of commutative unital algebras with basis over Rational Field
        """
    @cached_method
    def basis(self):
        """
        Return the basis of ``self``.

        EXAMPLES::

            sage: F.<x,y,z> = FreeAlgebra(QQ)
            sage: J = JordanAlgebra(F)
            sage: J.basis()
            Lazy family (Term map(i))_{i in Free monoid on 3 generators (x, y, z)}
        """
    algebra_generators = basis
    def gens(self) -> tuple:
        """
        Return the generators of ``self``.

        EXAMPLES::

            sage: cat = Algebras(QQ).WithBasis().FiniteDimensional()
            sage: C = CombinatorialFreeModule(QQ, ['x','y','z'], category=cat)
            sage: J = JordanAlgebra(C)
            sage: J.gens()
            (B['x'], B['y'], B['z'])

            sage: F.<x,y,z> = FreeAlgebra(QQ)
            sage: J = JordanAlgebra(F)
            sage: J.gens()
            Traceback (most recent call last):
            ...
            NotImplementedError: infinite set
        """
    @cached_method
    def zero(self):
        """
        Return the element `0`.

        EXAMPLES::

            sage: F.<x,y,z> = FreeAlgebra(QQ)
            sage: J = JordanAlgebra(F)
            sage: J.zero()
            0
        """
    @cached_method
    def one(self):
        """
        Return the element `1` if it exists.

        EXAMPLES::

            sage: F.<x,y,z> = FreeAlgebra(QQ)
            sage: J = JordanAlgebra(F)
            sage: J.one()
            1
        """
    class Element(AlgebraElement):
        """
        An element of a special Jordan algebra.
        """
        def __init__(self, parent, x) -> None:
            """
            Initialize ``self``.

            EXAMPLES::

                sage: F.<x,y,z> = FreeAlgebra(QQ)
                sage: J = JordanAlgebra(F)
                sage: a,b,c = map(J, F.gens())
                sage: TestSuite(a + 2*b - c).run()
            """
        def __bool__(self) -> bool:
            """
            Return if ``self`` is nonzero.

            EXAMPLES::

                sage: F.<x,y,z> = FreeAlgebra(QQ)
                sage: J = JordanAlgebra(F)
                sage: a,b,c = map(J, F.gens())
                sage: bool(a + 2*b - c)
                True
            """
        def __eq__(self, other):
            """
            Check equality.

            EXAMPLES::

                sage: F.<x,y,z> = FreeAlgebra(QQ)
                sage: J = JordanAlgebra(F)
                sage: a,b,c = map(J, F.gens())
                sage: elt = a + 2*b - c
                sage: elt == elt
                True
                sage: elt == x
                False
                sage: elt == 2*b
                False
            """
        def __ne__(self, other):
            """
            Check inequality.

            EXAMPLES::

                sage: F.<x,y,z> = FreeAlgebra(QQ)
                sage: J = JordanAlgebra(F)
                sage: a,b,c = map(J, F.gens())
                sage: elt = a + 2*b - c
                sage: elt != elt
                False
                sage: elt != x
                True
                sage: elt != 2*b
                True
            """
        def monomial_coefficients(self, copy: bool = True):
            """
            Return a dictionary whose keys are indices of basis elements in
            the support of ``self`` and whose values are the corresponding
            coefficients.

            INPUT:

            - ``copy`` -- boolean (default: ``True``); if ``self`` is
              internally represented by a dictionary ``d``, then make a copy of
              ``d``; if ``False``, then this can cause undesired behavior by
              mutating ``d``

            EXAMPLES::

                sage: F.<x,y,z> = FreeAlgebra(QQ)
                sage: J = JordanAlgebra(F)
                sage: a,b,c = map(J, F.gens())
                sage: elt = a + 2*b - c
                sage: elt.monomial_coefficients()
                {x: 1, y: 2, z: -1}
            """

class JordanAlgebraSymmetricBilinear(JordanAlgebra):
    """
    A Jordan algebra given by a symmetric bilinear form `m`.
    """
    def __init__(self, R, form, names=None) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: m = matrix([[-2,3],[3,4]])
            sage: J = JordanAlgebra(m)
            sage: TestSuite(J).run()
        """
    @cached_method
    def basis(self):
        """
        Return a basis of ``self``.

        The basis returned begins with the unity of `R` and continues with
        the standard basis of `M`.

        EXAMPLES::

            sage: m = matrix([[0,1],[1,1]])
            sage: J = JordanAlgebra(m)
            sage: J.basis()
            Family (1 + (0, 0), 0 + (1, 0), 0 + (0, 1))
        """
    algebra_generators = basis
    def gens(self) -> tuple:
        """
        Return the generators of ``self``.

        EXAMPLES::

            sage: m = matrix([[0,1],[1,1]])
            sage: J = JordanAlgebra(m)
            sage: J.gens()
            (1 + (0, 0), 0 + (1, 0), 0 + (0, 1))
        """
    @cached_method
    def zero(self):
        """
        Return the element 0.

        EXAMPLES::

            sage: m = matrix([[0,1],[1,1]])
            sage: J = JordanAlgebra(m)
            sage: J.zero()
            0 + (0, 0)
        """
    @cached_method
    def one(self):
        """
        Return the element 1 if it exists.

        EXAMPLES::

            sage: m = matrix([[0,1],[1,1]])
            sage: J = JordanAlgebra(m)
            sage: J.one()
            1 + (0, 0)
        """
    class Element(AlgebraElement):
        """
        An element of a Jordan algebra defined by a symmetric bilinear form.
        """
        def __init__(self, parent, s, v) -> None:
            """
            Initialize ``self``.

            TESTS::

                sage: m = matrix([[0,1],[1,1]])
                sage: J.<a,b,c> = JordanAlgebra(m)
                sage: TestSuite(a + 2*b - c).run()
            """
        def __bool__(self) -> bool:
            """
            Return if ``self`` is nonzero.

            TESTS::

                sage: m = matrix([[0,1],[1,1]])
                sage: J.<a,b,c> = JordanAlgebra(m)
                sage: bool(1)
                True
                sage: bool(b)
                True
                sage: bool(a + 2*b - c)
                True
            """
        def __eq__(self, other):
            """
            Check equality.

            EXAMPLES::

                sage: m = matrix([[0,1],[1,1]])
                sage: J.<a,b,c> = JordanAlgebra(m)
                sage: x = 4*a - b + 3*c
                sage: x == J((4, (-1, 3)))
                True
                sage: a == x
                False

                sage: m = matrix([[-2,3],[3,4]])
                sage: J.<a,b,c> = JordanAlgebra(m)
                sage: 4*a - b + 3*c == x
                False
            """
        def __ne__(self, other):
            """
            Check inequality.

            EXAMPLES::

                sage: m = matrix([[0,1],[1,1]])
                sage: J.<a,b,c> = JordanAlgebra(m)
                sage: x = 4*a - b + 3*c
                sage: x != J((4, (-1, 3)))
                False
                sage: a != x
                True

                sage: m = matrix([[-2,3],[3,4]])
                sage: J.<a,b,c> = JordanAlgebra(m)
                sage: 4*a - b + 3*c != x
                True
            """
        def monomial_coefficients(self, copy: bool = True):
            """
            Return a dictionary whose keys are indices of basis elements in
            the support of ``self`` and whose values are the corresponding
            coefficients.

            INPUT:

            - ``copy`` -- ignored

            EXAMPLES::

                sage: m = matrix([[0,1],[1,1]])
                sage: J.<a,b,c> = JordanAlgebra(m)
                sage: elt = a + 2*b - c
                sage: elt.monomial_coefficients()
                {0: 1, 1: 2, 2: -1}
            """
        def trace(self):
            """
            Return the trace of ``self``.

            The trace of an element `\\alpha + x \\in M^*` is given by
            `t(\\alpha + x) = 2 \\alpha`.

            EXAMPLES::

                sage: m = matrix([[0,1],[1,1]])
                sage: J.<a,b,c> = JordanAlgebra(m)
                sage: x = 4*a - b + 3*c
                sage: x.trace()
                8
            """
        def norm(self):
            """
            Return the norm of ``self``.

            The norm of an element `\\alpha + x \\in M^*` is given by
            `n(\\alpha + x) = \\alpha^2 - (x, x)`.

            EXAMPLES::

                sage: m = matrix([[0,1],[1,1]])
                sage: J.<a,b,c> = JordanAlgebra(m)
                sage: x = 4*a - b + 3*c; x
                4 + (-1, 3)
                sage: x.norm()
                13
            """
        def bar(self):
            """
            Return the result of the bar involution of ``self``.

            The bar involution `\\bar{\\cdot}` is the `R`-linear
            endomorphism of `M^*` defined by `\\bar{1} = 1` and
            `\\bar{x} = -x` for `x \\in M`.

            EXAMPLES::

                sage: m = matrix([[0,1],[1,1]])
                sage: J.<a,b,c> = JordanAlgebra(m)
                sage: x = 4*a - b + 3*c
                sage: x.bar()
                4 + (1, -3)

            We check that it is an algebra morphism::

                sage: y = 2*a + 2*b - c
                sage: x.bar() * y.bar() == (x*y).bar()
                True
            """

class ExceptionalJordanAlgebra(JordanAlgebra):
    """
    The exceptional `27` dimensional Jordan algebra as self-adjoint
    `3 \\times 3` matrix over an octonion algebra.

    Let `\\mathbf{O}` be the :class:`OctonionAlgebra` over a commutative
    ring `R` of characteristic not equal to `2`. The *exceptional Jordan
    algebra* `\\mathfrak{h}_3(\\mathbf{O})` is a `27` dimensional free
    `R`-module spanned by the matrices

    .. MATH::

        \\begin{bmatrix}
        \\alpha & x & y \\\\\n        x^* & \\beta & z \\\\\n        y^* & z^* & \\gamma
        \\end{bmatrix}

    for `\\alpha, \\beta, \\gamma \\in R` and `x, y, z \\in \\mathbf{O}`,
    with multiplication given by the usual symmetrizer operation
    `X \\circ Y = \\frac{1}{2}(XY + YX)`.

    These are also known as *Albert algebras* due to the work of
    Abraham Adrian Albert on these algebras over `\\RR`.

    EXAMPLES:

    We construct an exceptional Jordan algebra over `\\QQ` and perform
    some basic computations::

        sage: O = OctonionAlgebra(QQ)
        sage: J = JordanAlgebra(O)
        sage: gens = J.gens()
        sage: gens[1]
        [0 0 0]
        [0 1 0]
        [0 0 0]
        sage: gens[3]
        [0 1 0]
        [1 0 0]
        [0 0 0]
        sage: gens[1] * gens[3]
        [  0 1/2   0]
        [1/2   0   0]
        [  0   0   0]

    The Lie algebra of derivations of the exceptional Jordan algebra
    is isomorphic to the simple Lie algebra of type `F_4`. We verify
    that we the derivation module has the correct dimension::

        sage: len(J.derivations_basis())  # long time
        52
        sage: LieAlgebra(QQ, cartan_type='F4').dimension()
        52

    REFERENCES:

    - :wikipedia:`Albert_algebra`
    - :wikipedia:`Jordan_algebra#Examples`
    - :wikipedia:`Hurwitz's_theorem_(composition_algebras)#Applications_to_Jordan_algebras`
    - `<https://math.ucr.edu/home/baez/octonions/octonions.pdf>`_
    """
    def __init__(self, O) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: O = OctonionAlgebra(QQ)
            sage: J = JordanAlgebra(O)
            sage: TestSuite(J).run()  # long time

            sage: O = OctonionAlgebra(QQ, 1, -2, 9)
            sage: J = JordanAlgebra(O)
            sage: TestSuite(J).run()  # long time

            sage: R.<x, y> = GF(11)[]
            sage: O = OctonionAlgebra(R, 1, x + y, 9)
            sage: J = JordanAlgebra(O)
            sage: TestSuite(J).run()  # long time

            sage: O = OctonionAlgebra(ZZ)
            sage: J = JordanAlgebra(O)
            Traceback (most recent call last):
            ...
            ValueError: 2 must be invertible
        """
    @cached_method
    def basis(self):
        """
        Return a basis of ``self``.

        EXAMPLES::

            sage: O = OctonionAlgebra(QQ)
            sage: J = JordanAlgebra(O)
            sage: B = J.basis()
            sage: B[::6]
            ([1 0 0]
             [0 0 0]
             [0 0 0],
             [ 0  k  0]
             [-k  0  0]
             [ 0  0  0],
             [ 0  0  i]
             [ 0  0  0]
             [-i  0  0],
             [  0   0  lk]
             [  0   0   0]
             [-lk   0   0],
             [  0   0   0]
             [  0   0  li]
             [  0 -li   0])
            sage: len(B)
            27
        """
    algebra_generators = basis
    def gens(self) -> tuple:
        """
        Return the generators of ``self``.

        EXAMPLES::

            sage: O = OctonionAlgebra(QQ)
            sage: J = JordanAlgebra(O)
            sage: G = J.gens()
            sage: G[0]
            [1 0 0]
            [0 0 0]
            [0 0 0]
            sage: G[5]
            [ 0  j  0]
            [-j  0  0]
            [ 0  0  0]
            sage: G[22]
            [ 0  0  0]
            [ 0  0  k]
            [ 0 -k  0]
        """
    @cached_method
    def zero(self):
        """
        Return the additive identity.

        EXAMPLES::

            sage: O = OctonionAlgebra(QQ)
            sage: J = JordanAlgebra(O)
            sage: J.zero()
            [0 0 0]
            [0 0 0]
            [0 0 0]
        """
    @cached_method
    def one(self):
        """
        Return multiplicative identity.

        EXAMPLES::

            sage: O = OctonionAlgebra(QQ)
            sage: J = JordanAlgebra(O)
            sage: J.one()
            [1 0 0]
            [0 1 0]
            [0 0 1]
            sage: all(J.one() * b == b for b in J.basis())
            True
        """
    def some_elements(self):
        """
        Return some elements of ``self``.

        EXAMPLES::

            sage: O = OctonionAlgebra(QQ)
            sage: J = JordanAlgebra(O)
            sage: J.some_elements()
            [[6/5   0   0]
             [  0 6/5   0]
             [  0   0 6/5],
             [1 0 0]
             [0 1 0]
             [0 0 1],
             [0 0 0]
             [0 0 0]
             [0 0 0],
             [0 0 0]
             [0 1 0]
             [0 0 0],
             [ 0  j  0]
             [-j  0  0]
             [ 0  0  0],
             [  0   0  lj]
             [  0   0   0]
             [-lj   0   0],
             [      0       0       0]
             [      0       1  1/2*lj]
             [      0 -1/2*lj       0],
             [        1         0  j + 2*li]
             [        0         1         0]
             [-j - 2*li         0         1],
             [      1  j + lk       l]
             [-j - lk       0  i + lj]
             [     -l -i - lj       0],
             [     1  3/2*l    2*k]
             [-3/2*l      0  5/2*j]
             [  -2*k -5/2*j      0]]

            sage: O = OctonionAlgebra(GF(3))
            sage: J = JordanAlgebra(O)
            sage: J.some_elements()
            [[-1  0  0]
             [ 0 -1  0]
             [ 0  0 -1],
             [1 0 0]
             [0 1 0]
             [0 0 1],
             [0 0 0]
             [0 0 0]
             [0 0 0],
             [0 0 0]
             [0 1 0]
             [0 0 0],
             [ 0  j  0]
             [-j  0  0]
             [ 0  0  0],
             [  0   0  lj]
             [  0   0   0]
             [-lj   0   0],
             [  0   0   0]
             [  0   1 -lj]
             [  0  lj   0],
             [      1       0  j - li]
             [      0       1       0]
             [-j + li       0       1],
             [      1  j + lk       l]
             [-j - lk       0  i + lj]
             [     -l -i - lj       0],
             [ 1  0 -k]
             [ 0  0  j]
             [ k -j  0]]
        """
    class Element(AlgebraElement):
        """
        An element of an exceptional Jordan algebra.
        """
        def __init__(self, parent, data) -> None:
            """
            Initialize ``self``.

            TESTS::

                sage: O = OctonionAlgebra(QQ)
                sage: J = JordanAlgebra(O)
                sage: elt = sum(J.basis())
                sage: TestSuite(elt).run()
            """
        def __bool__(self) -> bool:
            """
            Return if ``self`` is nonzero.

            TESTS::

                sage: O = OctonionAlgebra(QQ)
                sage: J = JordanAlgebra(O)
                sage: all(bool(b) for b in J.basis())
                True
                sage: bool(J.zero())
                False
            """
        def monomial_coefficients(self, copy: bool = True):
            """
            Return a dictionary whose keys are indices of basis elements in
            the support of ``self`` and whose values are the corresponding
            coefficients.

            INPUT:

            - ``copy`` -- ignored

            EXAMPLES::

                sage: O = OctonionAlgebra(QQ)
                sage: J = JordanAlgebra(O)
                sage: elt = sum(~QQ(ind) * b for ind, b in enumerate(J.basis()[::6], start=1)); elt
                [              1           1/2*k  1/3*i + 1/4*lk]
                [         -1/2*k               0          1/5*li]
                [-1/3*i - 1/4*lk         -1/5*li               0]
                sage: elt.monomial_coefficients()
                {0: 1, 6: 1/2, 12: 1/3, 18: 1/4, 24: 1/5}

            TESTS::

                sage: O = OctonionAlgebra(QQ)
                sage: J = JordanAlgebra(O)
                sage: all(b.monomial_coefficients() == {i: 1} for i,b in enumerate(J.basis()))
                True
            """
