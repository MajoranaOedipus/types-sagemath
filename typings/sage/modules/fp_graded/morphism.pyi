from sage.categories.homset import End as End, Hom as Hom
from sage.categories.morphism import Morphism as Morphism
from sage.misc.cachefunc import cached_function as cached_function, cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.rings.infinity import infinity as infinity

class FPModuleMorphism(Morphism):
    """
    Create a homomorphism between finitely presented graded modules.

    INPUT:

    - ``parent`` -- a homspace of finitely presented graded modules
    - ``values`` -- list of elements in the codomain; each element
      corresponds to a module generator in the domain
    - ``check`` -- boolean (default: ``True``); if ``True``, check
      that the morphism is well-defined

    TESTS::

        sage: from sage.modules.fp_graded.module import FPModule

    Trying to map the generators of a non-free module into a
    free module::

        sage: A = SteenrodAlgebra(2)
        sage: F = FPModule(A, [2,3])
        sage: Q = FPModule(A, [2,3], relations=[[Sq(6), Sq(5)]])
        sage: v1 = Q((Sq(1), 0))
        sage: v2 = Q((0, 1))
        sage: m = Hom(F, Q)( (v1, v2) )
        Traceback (most recent call last):
        ...
        ValueError: ill-defined homomorphism: degrees do not match

    Trying to map the generators of a non-free module into a
    free module::

        sage: w = Hom(Q, F)( (F((1, 0)), F((0, 1))) )
        Traceback (most recent call last):
        ...
        ValueError: relation Sq(6)*g[2] + Sq(5)*g[3] is not sent to zero
    """
    def __init__(self, parent, values, check: bool = True) -> None:
        """
        Create a homomorphism between finitely presented graded modules.

        OUTPUT:

        A module homomorphism defined by sending the generator
        with index `i` to the corresponding element in ``values``.

        TESTS::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A2 = SteenrodAlgebra(2, profile=(3,2,1))
            sage: A3 = SteenrodAlgebra(2, profile=(4,3,2,1))
            sage: M = FPModule(A2, [0], relations=[[Sq(1)]])
            sage: N = FPModule(A2, [0], relations=[[Sq(4)],[Sq(1)]])
            sage: f = Hom(M,N)([A2.Sq(3)*N.generator(0)])
            sage: TestSuite(f).run()
        """
    def change_ring(self, algebra):
        """
        Change the base ring of ``self``.

        INPUT:

        - ``algebra`` -- a graded algebra

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A2 = SteenrodAlgebra(2, profile=(3,2,1))
            sage: A3 = SteenrodAlgebra(2, profile=(4,3,2,1))
            sage: M = FPModule(A2, [0], relations=[[Sq(1)]])
            sage: N = FPModule(A2, [0], relations=[[Sq(4)],[Sq(1)]])

            sage: f = Hom(M,N)([A2.Sq(3)*N.generator(0)]); f
            Module morphism:
              From: Finitely presented left module on 1 generator and 1 relation over sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [3, 2, 1]
              To:   Finitely presented left module on 1 generator and 2 relations over sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [3, 2, 1]
              Defn: g[0] |--> Sq(3)*g[0]

            sage: f.base_ring()
            sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [3, 2, 1]

            sage: g = f.change_ring(A3)
            sage: g.base_ring()
            sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [4, 3, 2, 1]
        """
    def degree(self):
        """
        The degree of ``self``.

        OUTPUT: the integer degree of ``self``

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import *
            sage: A = SteenrodAlgebra(2)
            sage: M = FPModule(A, [0,1], [[Sq(2), Sq(1)]])
            sage: N = FPModule(A, [2], [[Sq(4)]])
            sage: homspace = Hom(M, N)

            sage: values = [Sq(5)*N.generator(0), Sq(3,1)*N.generator(0)]
            sage: f = homspace(values)
            sage: f.degree()
            7

        The trivial homomorphism has no degree::

            sage: homspace.zero().degree()
            Traceback (most recent call last):
            ...
            ValueError: the zero morphism does not have a well-defined degree

        TESTS::

            sage: M = FPModule(SteenrodAlgebra(p=2), [7])
            sage: N = FPModule(SteenrodAlgebra(p=2), [0], relations=[[Sq(1)]])
            sage: f = Hom(M,N)([Sq(1)*N.generator(0)])
            sage: f == Hom(M,N).zero()
            True
            sage: f.degree()
            Traceback (most recent call last):
            ...
            ValueError: the zero morphism does not have a well-defined degree
        """
    def values(self):
        """
        The values under ``self`` of the module generators of the domain module.

        OUTPUT: a sequence of module elements of the codomain

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A = SteenrodAlgebra(2)
            sage: M = FPModule(A, [0,1], [[Sq(2), Sq(1)]])
            sage: N = FPModule(A, [2], [[Sq(4)]])
            sage: homspace = Hom(M, N)

            sage: values = [Sq(5)*N.generator(0), Sq(3,1)*N.generator(0)]
            sage: f = homspace(values)

            sage: f.values()
            (Sq(5)*g[2], Sq(3,1)*g[2])

            sage: homspace.zero().values()
            (0, 0)

            sage: homspace = Hom(A.free_graded_module((0,1)), A.free_graded_module((2,)))
            sage: N = homspace.codomain()
            sage: values = [Sq(5)*N.generator(0), Sq(3,1)*N.generator(0)]
            sage: f = homspace(values)
            sage: f.values()
            (Sq(5)*g[2], Sq(3,1)*g[2])
            sage: homspace.zero().values()
            (0, 0)
        """
    def __add__(self, g):
        """
        The pointwise sum of ``self`` and ``g``.

        Pointwise addition of two homomorphisms `f` and `g` with the same domain
        and codomain is given by the formula `(f+g)(x) = f(x) + g(x)` for
        every `x` in the domain of `f`.

        INPUT:

        - ``g`` -- a homomorphism with the same domain and codomain as ``self``

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import *
            sage: A = SteenrodAlgebra(2)
            sage: M = FPModule(A, [0,1], [[Sq(2), Sq(1)]])
            sage: N = FPModule(A, [2], [[Sq(4)]])
            sage: v = N.generator(0)
            sage: homspace = Hom(M, N)
            sage: values = [Sq(5)*v, Sq(3,1)*v]
            sage: f = homspace(values)
            sage: ff = f + f
            sage: ff.is_zero()
            True
            sage: ff + f == f
            True

            sage: N = A.free_graded_module((2,))
            sage: v = N.generator(0)
            sage: homspace = Hom(A.free_graded_module((0,1)), N)
            sage: values = [Sq(5)*v, Sq(3,1)*v]
            sage: f = homspace(values)
            sage: ff = f + f
            sage: ff.is_zero()
            True
            sage: ff + f == f
            True
            sage: ff = f + f
            sage: ff.is_zero()
            True
        """
    def __neg__(self):
        """
        The additive inverse of ``self`` with respect to the group
        structure given by pointwise sum.

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A = SteenrodAlgebra(2)
            sage: M = FPModule(A, [0,1], [[Sq(2), Sq(1)]])
            sage: N = FPModule(A, [2], [[Sq(4)]])
            sage: v = N.generator(0)
            sage: homspace = Hom(M, N)
            sage: values = [Sq(5)*v, Sq(3,1)*v]
            sage: f = homspace(values)
            sage: f_neg = -f; f_neg
            Module morphism:
              From: Finitely presented left module on 2 generators and 1 relation over mod 2 Steenrod algebra, milnor basis
              To:   Finitely presented left module on 1 generator and 1 relation over mod 2 Steenrod algebra, milnor basis
              Defn: g[0] |--> Sq(5)*g[2]
                    g[1] |--> Sq(3,1)*g[2]
            sage: (f + f_neg).is_zero()
            True

            sage: N = A.free_graded_module((2,))
            sage: v = N.generator(0)
            sage: homspace = Hom(A.free_graded_module((0,1)), N)
            sage: N = homspace.codomain()
            sage: values = [Sq(5)*v, Sq(3,1)*v]
            sage: f = homspace(values)
            sage: f_neg = -f; f_neg
            Module morphism:
              From: Free graded left module on 2 generators over mod 2 Steenrod algebra, milnor basis
              To:   Free graded left module on 1 generator over mod 2 Steenrod algebra, milnor basis
              Defn: g[0] |--> Sq(5)*g[2]
                    g[1] |--> Sq(3,1)*g[2]
            sage: (f + f_neg).is_zero()
            True
        """
    def __sub__(self, g):
        """
        The difference between ``self`` and ``g`` with
        respect to the group structure given by pointwise sum.

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import *
            sage: A = SteenrodAlgebra(2)
            sage: M = FPModule(A, [0])
            sage: N = FPModule(A, [0], [[Sq(4)]])
            sage: f = Hom(M, N)( [Sq(3)*N.generator(0)] )
            sage: g = Hom(M, N)( [Sq(0,1)*N.generator(0)] )
            sage: f - g
            Module morphism:
              From: Free graded left module on 1 generator over mod 2 Steenrod algebra, milnor basis
              To:   Finitely presented left module on 1 generator and 1 relation over mod 2 Steenrod algebra, milnor basis
              Defn: g[0] |--> (Sq(0,1)+Sq(3))*g[0]

            sage: f = Hom(M, N)( [Sq(4)*N.generator(0)] ) # the zero map
            sage: g = Hom(M, N)( [Sq(1,1)*N.generator(0)] )
            sage: f - g
            Module morphism:
              From: Free graded left module on 1 generator over mod 2 Steenrod algebra, milnor basis
              To:   Finitely presented left module on 1 generator and 1 relation over mod 2 Steenrod algebra, milnor basis
              Defn: g[0] |--> Sq(1,1)*g[0]

            sage: N = A.free_graded_module((2,))
            sage: v = N.generator(0)
            sage: homspace = Hom(A.free_graded_module((0,1)), N)
            sage: values = [Sq(5)*v, Sq(3,1)*v]
            sage: f = homspace(values)
            sage: values2 = [Sq(5)*v, Sq(3,1)*v]
            sage: g = homspace(values2)
            sage: f - g == 0
            True
        """
    def __mul__(self, g):
        """
        The composition of ``g`` followed by ``self``.

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A = SteenrodAlgebra(2)
            sage: M = FPModule(A, [0], [[Sq(1,2)]])
            sage: N = FPModule(A, [0], [[Sq(2,2)]])
            sage: f = Hom(M, N)( [Sq(2)*N.generator(0)] )
            sage: g = Hom(N, M)( [Sq(2,2)*M.generator(0)] )
            sage: fg = f * g; fg
            Module endomorphism of Finitely presented left module on 1 generator and 1 relation over mod 2 Steenrod algebra, milnor basis
              Defn: g[0] |--> (Sq(0,1,1)+Sq(1,3)+Sq(3,0,1))*g[0]
            sage: fg.is_endomorphism()
            True

            sage: M = A.free_graded_module((0,1))
            sage: N = A.free_graded_module((2,))
            sage: v = N.generator(0)
            sage: values = [Sq(5)*v, Sq(3,1)*v]
            sage: f = Hom(M, N)(values)
            sage: values2 = [Sq(2)*M.generator(0)]
            sage: g = Hom(N, M)(values2)
            sage: fg = f * g; fg
            Module endomorphism of Free graded left module on 1 generator over mod 2 Steenrod algebra, milnor basis
              Defn: g[2] |--> (Sq(4,1)+Sq(7))*g[2]
            sage: fg.is_endomorphism()
            True

        TESTS::

            sage: from sage.modules.fp_graded.free_module import *
            sage: A = SteenrodAlgebra(2)
            sage: M = FPModule(A, (0,1))
            sage: values = [Sq(5)*N.generator(0), Sq(3,1)*N.generator(0)]
            sage: f = Hom(M, N)(values)
            sage: f * f
            Traceback (most recent call last):
            ...
            ValueError: morphisms not composable

            sage: M = A.free_graded_module((0,1))
            sage: N = A.free_graded_module((2,))
            sage: values = [Sq(5)*N.generator(0), Sq(3,1)*N.generator(0)]
            sage: f = Hom(M, N)(values)
            sage: f * f
            Traceback (most recent call last):
            ...
            ValueError: morphisms not composable
        """
    @cached_method
    def is_zero(self) -> bool:
        """
        Decide if ``self`` is the zero homomorphism.

        OUTPUT: the boolean value ``True`` if ``self`` is trivial and ``False`` otherwise

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A = SteenrodAlgebra(2)
            sage: M = FPModule(A, [0,1], [[Sq(2), Sq(1)]])
            sage: N = FPModule(A, [2], [[Sq(4)]])
            sage: values = [Sq(5)*N.generator(0), Sq(3,1)*N.generator(0)]

            sage: f = Hom(M, N)(values)
            sage: f.is_zero()
            False

            sage: (f-f).is_zero()
            True

            sage: M = A.free_graded_module((0,1))
            sage: N = A.free_graded_module((2,))
            sage: v = N.generator(0)
            sage: values = [Sq(5)*v, Sq(3,1)*v]
            sage: f = Hom(M, N)(values)
            sage: f.is_zero()
            False
            sage: (f-f).is_zero()
            True
        """
    __bool__ = is_zero
    @cached_method
    def is_identity(self) -> bool:
        """
        Decide if ``self`` is the identity endomorphism.

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import *
            sage: A = SteenrodAlgebra(2)
            sage: M = FPModule(A, [0,1], [[Sq(2), Sq(1)]])
            sage: N = FPModule(A, [2], [[Sq(4)]])
            sage: values = [Sq(5)*N.generator(0), Sq(3,1)*N.generator(0)]

            sage: f = Hom(M, N)(values)
            sage: f.is_identity()
            False

            sage: one = Hom(M, M)(M.generators()); one
            Module endomorphism of Finitely presented left module on 2 generators and 1 relation over mod 2 Steenrod algebra, milnor basis
              Defn: g[0] |--> g[0]
                    g[1] |--> g[1]

            sage: one.is_identity()
            True

            sage: M = A.free_graded_module((0,1))
            sage: N = A.free_graded_module((2,))
            sage: v = N.generator(0)
            sage: values = [Sq(5)*v, Sq(3,1)*v]
            sage: f = Hom(M, N)(values)
            sage: f.is_identity()
            False
            sage: one = Hom(M, M)(M.generators()); one
            Module endomorphism of Free graded left module on 2 generators over mod 2 Steenrod algebra, milnor basis
              Defn: g[0] |--> g[0]
                    g[1] |--> g[1]
            sage: one.is_identity()
            True
        """
    def __call__(self, x):
        """
        Evaluate the homomorphism at the given domain element ``x``.

        INPUT:

        - ``x`` -- an element of the domain of the homomorphism

        OUTPUT:

        The module element of the codomain which is the value of ``x``
        under this homomorphism.

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import *
            sage: A = SteenrodAlgebra(2)
            sage: M = FPModule(A, [0,1], [[Sq(2), Sq(1)]])
            sage: N = FPModule(A, [2], [[Sq(4)]])

            sage: values = [Sq(5)*N.generator(0), Sq(3,1)*N.generator(0)]
            sage: f = Hom(M, N)(values)

            sage: f.__call__(M.generator(0))
            Sq(5)*g[2]

            sage: f.__call__(M.generator(1))
            Sq(3,1)*g[2]
        """
    @cached_method
    def vector_presentation(self, n):
        """
        Return the restriction of ``self`` to the domain module elements
        of degree ``n``.

        The restriction of a nonzero module homomorphism to the free module
        of module elements of degree `n` is a linear function into the free
        module of elements of degree `n+d` belonging to the codomain.
        Here `d` is the degree of this homomorphism.

        When this homomorphism is zero, it has no well defined degree so the
        function cannot be presented since we do not know the degree of its
        codomain.  In this case, an error is raised.

        INPUT:

        - ``n`` -- integer degree

        OUTPUT:

        A linear function of finite dimensional free modules over the
        ground ring of the algebra for this module.  The domain is isomorphic
        to the free module of domain elements of degree ``n`` of ``self``
        via the choice of basis given by
        :meth:`~sage.modules.fp_graded.free_module.FreeGradedModule.basis_elements`.
        If the morphism is zero, an error is raised.

        .. SEEALSO::

            * :meth:`sage.modules.fp_graded.module.FPModule.vector_presentation`
            * :meth:`sage.modules.fp_graded.module.FPModule.basis_elements`
            * :meth:`sage.modules.fp_graded.free_module.FreeGradedModule.vector_presentation`
            * :meth:`sage.modules.fp_graded.free_module.FreeGradedModule.basis_elements`

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A = SteenrodAlgebra(2)
            sage: M = FPModule(A, [0,1], [[Sq(2), Sq(1)]])
            sage: N = FPModule(A, [2], [[Sq(4)]])
            sage: values = [Sq(5)*N.generator(0), Sq(3,1)*N.generator(0)]
            sage: f = Hom(M, N)(values)
            sage: f.vector_presentation(0)
            Vector space morphism represented by the matrix:
            [0]
            Domain: Vector space quotient V/W of dimension 1 over Finite Field of size 2 where
            V: Vector space of dimension 1 over Finite Field of size 2
            W: Vector space of degree 1 and dimension 0 over Finite Field of size 2
            Basis matrix:
            []
            Codomain: Vector space quotient V/W of dimension 1 over Finite Field of size 2 where
            V: Vector space of dimension 2 over Finite Field of size 2
            W: Vector space of degree 2 and dimension 1 over Finite Field of size 2
            Basis matrix:
            [0 1]
            sage: f.vector_presentation(1)
            Vector space morphism represented by the matrix:
            [0 0]
            [0 1]
            Domain: Vector space quotient V/W of dimension 2 over Finite Field of size 2 where
            V: Vector space of dimension 2 over Finite Field of size 2
            W: Vector space of degree 2 and dimension 0 over Finite Field of size 2
            Basis matrix:
            []
            Codomain: Vector space quotient V/W of dimension 2 over Finite Field of size 2 where
            V: Vector space of dimension 3 over Finite Field of size 2
            W: Vector space of degree 3 and dimension 1 over Finite Field of size 2
            Basis matrix:
            [0 1 1]
            sage: f.vector_presentation(2)
            Vector space morphism represented by the matrix:
            [0 0]
            Domain: Vector space quotient V/W of dimension 1 over Finite Field of size 2 where
            V: Vector space of dimension 2 over Finite Field of size 2
            W: Vector space of degree 2 and dimension 1 over Finite Field of size 2
            Basis matrix:
            [1 1]
            Codomain: Vector space quotient V/W of dimension 2 over Finite Field of size 2 where
            V: Vector space of dimension 4 over Finite Field of size 2
            W: Vector space of degree 4 and dimension 2 over Finite Field of size 2
            Basis matrix:
            [0 0 1 0]
            [0 0 0 1]

            sage: M = A.free_graded_module((0,1))
            sage: N = A.free_graded_module((2,))
            sage: v = N.generator(0)
            sage: values = [Sq(5)*v, Sq(3,1)*v]
            sage: f = Hom(M, N)(values)
            sage: f.vector_presentation(0)
            Vector space morphism represented by the matrix:
            [0 1]
            Domain: Vector space of dimension 1 over Finite Field of size 2
            Codomain: Vector space of dimension 2 over Finite Field of size 2
            sage: f.vector_presentation(1)
            Vector space morphism represented by the matrix:
            [0 0 0]
            [0 1 0]
            Domain: Vector space of dimension 2 over Finite Field of size 2
            Codomain: Vector space of dimension 3 over Finite Field of size 2
            sage: f.vector_presentation(2)
            Vector space morphism represented by the matrix:
            [0 0 1 1]
            [0 0 0 0]
            Domain: Vector space of dimension 2 over Finite Field of size 2
            Codomain: Vector space of dimension 4 over Finite Field of size 2

        TESTS::

            sage: F = FPModule(A, [0])
            sage: Q = FPModule(A, [0], [[Sq(2)]])
            sage: z = Hom(F, Q)([Sq(2)*Q.generator(0)])
            sage: z.is_zero()
            True
            sage: z.vector_presentation(0)
            Traceback (most recent call last):
            ...
            ValueError: the zero map has no vector presentation
        """
    def solve(self, x):
        """
        Return an element in the inverse image of ``x``.

        INPUT:

        - ``x`` -- an element of the codomain of this morphism

        OUTPUT:

        An element of the domain which maps to ``x`` under this morphism
        or ``None`` if ``x`` was not in the image of this morphism.

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A = SteenrodAlgebra(2)
            sage: M = FPModule(A, [0], [[Sq(3)]])
            sage: N = FPModule(A, [0], [[Sq(2,2)]])
            sage: f = Hom(M, N)( [Sq(2)*N.generator(0)] )
            sage: y = Sq(1,1)*N.generator(0); y
            Sq(1,1)*g[0]
            sage: x = f.solve(y); x
            Sq(2)*g[0]
            sage: y == f(x)
            True

        Trying to lift an element which is not in the image results
        in a ``None`` value::

            sage: z = f.solve(Sq(1)*N.generator(0))
            sage: z is None
            True

        TESTS::

            sage: f.solve(Sq(2,2)*M.generator(0))
            Traceback (most recent call last):
            ...
            ValueError: the given element is not in the codomain of this homomorphism
        """
    def lift(self, f, verbose: bool = False):
        """
        Return a lift of this homomorphism over the given homomorphism ``f``.

        INPUT:

        - ``f`` -- a homomorphism with codomain equal to the codomain of ``self``
        - ``verbose`` -- boolean (default: ``False``); enable progress messages

        OUTPUT:

        A homomorphism `g` with the property that ``self`` equals `f \\circ g`.
        If no lift exist, ``None`` is returned.

        ALGORITHM:

        Let `s` be this homomorphism with `L` the domain of `s`.
        Choose `x_1, \\ldots, x_N` such that `f(x_i) = s(g_i)`,
        where the `g_i`'s are the module generators of `L`.

        The linear function sending `g_i` to `x_i` for every `i` is well
        defined if and only if the vector `x = (x_1, \\ldots, x_N)` lies
        in the nullspace of the coefficient matrix `R = (r_{ij})` given
        by the relations of `L`.

        Let `k \\in \\ker(f)` solve the matrix equation:

        .. MATH::

            R \\cdot k = R \\cdot x.

        Define a module homomorphism by sending the generators of `L` to
        `x_1 - k_1, \\ldots, x_N - k_N`.  This is well defined, and is also a
        lift of this homomorphism over `f`.

        Note that it does not matter how we choose the initial elements `x_i`:
        If `x'` is another choice then `x' - x\\in \\ker(f)` and
        `R\\cdot k = R\\cdot x` if and only if `R\\cdot (k + x' - x) = R\\cdot x'`.

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A = SteenrodAlgebra(2)

        Lifting a map from a free module is always possible::

            sage: M = FPModule(A, [0], [[Sq(3)]])
            sage: N = FPModule(A, [0], [[Sq(2,2)]])
            sage: F = FPModule(A, [0])
            sage: f = Hom(M,N)([Sq(2)*N.generator(0)])
            sage: k = Hom(F,N)([Sq(1)*Sq(2)*N.generator(0)])
            sage: f_ = k.lift(f)
            sage: f*f_ == k
            True
            sage: f_
            Module morphism:
              From: Free graded left module on 1 generator over mod 2 Steenrod algebra, milnor basis
              To:   Finitely presented left module on 1 generator and 1 relation over mod 2 Steenrod algebra, milnor basis
              Defn: g[0] |--> Sq(1)*g[0]

        A split projection::

            sage: A_plus_HZ = FPModule(A, [0,0], [[0, Sq(1)]])
            sage: HZ = FPModule(A, [0], [[Sq(1)]])
            sage: q = Hom(A_plus_HZ, HZ)([HZ([1]), HZ([1])])
            sage: # We can construct a splitting of `q` manually:
            sage: split = Hom(HZ,A_plus_HZ)([A_plus_HZ.generator(1)])
            sage: (q*split).is_identity()
            True

        Thus, lifting the identity homomorphism over `q` should be possible::

            sage: one = Hom(HZ,HZ).identity()
            sage: j = one.lift(q); j
            Module morphism:
              From: Finitely presented left module on 1 generator and 1 relation over mod 2 Steenrod algebra, milnor basis
              To:   Finitely presented left module on 2 generators and 1 relation over mod 2 Steenrod algebra, milnor basis
              Defn: g[0] |--> g[0, 1]
            sage: q*j
            Module endomorphism of Finitely presented left module on 1 generator and 1 relation over mod 2 Steenrod algebra, milnor basis
              Defn: g[0] |--> g[0]

        Lifting over the inclusion of the image sub module::

            sage: A = SteenrodAlgebra(2)
            sage: M = FPModule(A, [0], relations=[[Sq(0,1)]])
            sage: f = Hom(M,M)([Sq(2)*M.generator(0)])
            sage: im = f.image(top_dim=10)
            sage: f.lift(im)
            Module morphism:
              From: Finitely presented left module on 1 generator and 1 relation over mod 2 Steenrod algebra, milnor basis
              To:   Finitely presented left module on 1 generator and 2 relations over mod 2 Steenrod algebra, milnor basis
              Defn: g[0] |--> g[2]

        When a lift cannot be found, the ``None`` value is returned.  By
        setting the verbose argument to ``True``, an explanation of why
        the lifting failed will be displayed::

            sage: F2 = FPModule(A, [0,0])
            sage: non_surjection = Hom(F2, F2)([F2([1, 0]), F2([0, 0])])
            sage: lift = Hom(F2, F2).identity().lift(non_surjection, verbose=True)
            The generators of the domain of this homomorphism do not map into
             the image of the homomorphism we are lifting over.
            sage: lift is None
            True

        TESTS::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A = SteenrodAlgebra(2)
            sage: # The trivial map often involved in corner cases..
            sage: trivial_map = Hom(FPModule(A, [0]), FPModule(A, [])).zero()
            sage: trivial_map.lift(trivial_map) == 0
            True

            sage: F = FPModule(A, [0])
            sage: HZ = FPModule(A, [0], relations=[[Sq(1)]])
            sage: f = Hom(F,HZ)(HZ.generators())
            sage: split = Hom(HZ, HZ).identity().lift(f, verbose=True)
            The homomorphism cannot be lifted in any way such that the relations
             of the domain are respected: matrix equation has no solutions
            sage: split is None
            True

            sage: Hom(F, F).identity().lift(f, verbose=true)
            Traceback (most recent call last):
            ...
            ValueError: the codomains of this homomorphism and the homomorphism
             we are lifting over are different

            sage: f.lift(Hom(HZ, HZ).zero(), verbose=True)
            This homomorphism cannot lift over a trivial homomorphism since
             it is non-trivial.

            sage: Ap = SteenrodAlgebra(p=2, profile=(2,2,2,1))
            sage: Hko = FPModule(Ap, [0], [[Sq(2)], [Sq(1)]])
            sage: f = Hom(Hko, Hko)([(Ap.Sq(0,0,3) + Ap.Sq(0,2,0,1))*Hko.generator(0)])
            sage: f*f == 0
            True
            sage: k = f.kernel_inclusion() # long time
            sage: f.lift(k) # long time
            Module morphism:
              From: Finitely presented left module on 1 generator and 2 relations over sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [2, 2, 2, 1]
              To:   Finitely presented left module on 3 generators and 12 relations over sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [2, 2, 2, 1]
              Defn: g[0] |--> Sq(1)*g[20]

        Corner cases involving trivial maps::

            sage: M = FPModule(A, [1])
            sage: M1 = FPModule(A, [0])
            sage: M2 = FPModule(A, [0], [[Sq(1)]])
            sage: q = Hom(M1, M2)([M2.generator(0)])
            sage: z = Hom(M, M2).zero()
            sage: lift = z.lift(q)
            sage: lift.domain() is M and lift.codomain() is M1
            True

        .. SEEALSO::

            :meth:`split`
        """
    def split(self, verbose: bool = False):
        """
        Return a split of ``self``.

        INPUT:

        - ``verbose`` -- boolean (default: ``False``); enable progress messages

        OUTPUT:

        A homomorphism with the property that the composite homomorphism
        `S \\circ f = id`, where `S` is ``self``, is The identity homomorphism
        If no such split exist, ``None`` is returned.

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A = SteenrodAlgebra(2)
            sage: M = FPModule(A, [0,0], [[0, Sq(1)]])
            sage: N = FPModule(A, [0], [[Sq(1)]])
            sage: p = Hom(M, N)([N.generator(0), N.generator(0)])
            sage: s = p.split(); s
            Module morphism:
              From: Finitely presented left module on 1 generator and 1 relation over mod 2 Steenrod algebra, milnor basis
              To:   Finitely presented left module on 2 generators and 1 relation over mod 2 Steenrod algebra, milnor basis
              Defn: g[0] |--> g[0, 1]
            sage: # Verify that `s` is a splitting:
            sage: p*s
            Module endomorphism of Finitely presented left module on 1 generator and 1 relation over mod 2 Steenrod algebra, milnor basis
              Defn: g[0] |--> g[0]

        TESTS::

            sage: F = FPModule(A, [0])
            sage: N = FPModule(A, [0], [[Sq(1)]])
            sage: p = Hom(F, N)([N.generator(0)])
            sage: p.split(verbose=True) is None
            The homomorphism cannot be lifted in any way such that the relations
             of the domain are respected: matrix equation has no solutions
            True

        .. SEEALSO::

            :meth:`lift`
        """
    def homology(self, f, top_dim=None, verbose: bool = False):
        """
        Compute the sub-quotient module of `H(self, f) =
        \\ker(self)/\\operatorname{im}(f)` in a range of degrees.

        For a pair of composable morphisms `f: M\\to N` and `g: N \\to Q` of
        finitely presented modules, the homology module is a finitely
        presented quotient of the kernel sub module `\\ker(g) \\subset N`.

        INPUT:

        - ``f`` -- a homomorphism with codomain equal to the domain of ``self``
          and image contained in the kernel of this homomorphism
        - ``top_dim`` -- integer (optional); used by this function to stop the
          computation at the given degree
        - ``verbose`` -- boolean (default: ``False``); enable progress messages

        OUTPUT:

        A quotient homomorphism `\\ker(self) \\to H`, where `H` is isomorphic
        to `H(self, f)` in degrees less than or equal to ``top_dim``.

        .. NOTE::

            If the algebra for this module is finite, then no ``top_dim`` needs
            to be specified in order to ensure that this function terminates.

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A = SteenrodAlgebra(2, profile=(3,2,1))
            sage: M = FPModule(A, [0], [[Sq(3)]])
            sage: N = FPModule(A, [0], [[Sq(2,2)]])
            sage: F = FPModule(A, [0])
            sage: f = Hom(M,N)([A.Sq(2)*N.generator(0)])
            sage: g = Hom(F, M)([A.Sq(4)*A.Sq(1,2)*M.generator(0)])
            sage: ho = f.homology(g)
            sage: ho.codomain()
            Finitely presented left module on 1 generator and 5 relations over
             sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [3, 2, 1]
            sage: ho.codomain().is_trivial()
            False
        """
    def suspension(self, t):
        """
        The suspension of this morphism by the given degree ``t``.

        INPUT:

        - ``t`` -- integer by which the morphism is suspended

        OUTPUT: the morphism which is the suspension of ``self`` by the degree ``t``

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A = SteenrodAlgebra(2)
            sage: F1 = FPModule(A, [4,5])
            sage: F2 = FPModule(A, [5])

            sage: f = Hom(F1, F2)( ( F2([Sq(4)]), F2([Sq(5)]) ) ); f
            Module morphism:
              From: Free graded left module on 2 generators over mod 2 Steenrod algebra, milnor basis
              To:   Free graded left module on 1 generator over mod 2 Steenrod algebra, milnor basis
              Defn: g[4] |--> Sq(4)*g[5]
                    g[5] |--> Sq(5)*g[5]

            sage: e1 = F1([1, 0])
            sage: e2 = F1([0, 1])
            sage: f(e1)
            Sq(4)*g[5]
            sage: f(e2)
            Sq(5)*g[5]

            sage: sf = f.suspension(4); sf
            Module morphism:
              From: Free graded left module on 2 generators over mod 2 Steenrod algebra, milnor basis
              To:   Free graded left module on 1 generator over mod 2 Steenrod algebra, milnor basis
              Defn: g[8] |--> Sq(4)*g[9]
                    g[9] |--> Sq(5)*g[9]

            sage: sf.domain() is f.domain().suspension(4)
            True

            sage: sf.codomain() is f.codomain().suspension(4)
            True
        """
    def cokernel_projection(self):
        """
        Return the map to the cokernel of ``self``.

        OUTPUT:

        The natural projection from the codomain of this homomorphism
        to its cokernel.

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A1 = SteenrodAlgebra(2, profile=(2,1))
            sage: M = FPModule(A1, [0], [[Sq(2)]])
            sage: F = FPModule(A1, [0])

            sage: r = Hom(F, M)([A1.Sq(1)*M.generator(0)])
            sage: co = r.cokernel_projection(); co
            Module morphism:
              From: Finitely presented left module on 1 generator and 1 relation over sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [2, 1]
              To:   Finitely presented left module on 1 generator and 2 relations over sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [2, 1]
              Defn: g[0] |--> g[0]

            sage: co.domain().is_trivial()
            False
        """
    def kernel_inclusion(self, top_dim=None, verbose: bool = False):
        """
        Return the kernel of ``self``.

        INPUT:

        - ``top_dim`` -- integer (optional); used by this function to stop the
          computation at the given degree
        - ``verbose`` -- boolean (default: ``False``); enable progress messages

        OUTPUT:

        A homomorphism into `\\ker(self)` which is an isomorphism in
        degrees less than or equal to ``top_dim``.

        .. NOTE::

            If the algebra for this module is finite, then no ``top_dim`` needs
            to be specified in order to ensure that this function terminates.

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A3 = SteenrodAlgebra(2, profile=(4,3,2,1))
            sage: F = FPModule(A3, [1,3]);
            sage: L = FPModule(A3, [2,3], [[Sq(2),Sq(1)], [0,Sq(2)]]);
            sage: H = Hom(F, L);

            sage: H([L((A3.Sq(1), 1)), L((0, A3.Sq(2)))]).kernel_inclusion() # long time
            Module morphism:
              From: Finitely presented left module on 2 generators and 1 relation over sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [4, 3, 2, 1]
              To:   Free graded left module on 2 generators over sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [4, 3, 2, 1]
              Defn: g[3] |--> g[3]
                    g[4] |--> Sq(0,1)*g[1]

            sage: M = FPModule(A3, [0,7], [[Sq(1), 0], [Sq(2), 0], [Sq(4), 0], [Sq(8), Sq(1)], [0, Sq(7)], [0, Sq(0,1,1)+Sq(4,2)]])
            sage: F2 = FPModule(A3, [0], [[Sq(1)], [Sq(2)], [Sq(4)], [Sq(8)], [Sq(15)]])
            sage: H = Hom(M, F2)
            sage: f = H([F2([1]), F2([0])])

            sage: K = f.kernel_inclusion(verbose=True, top_dim=17)
            1. Computing the generators of the kernel presentation:
            Resolving the kernel in the range of dimensions [0, 17]:
             0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17.
            2. Computing the relations of the kernel presentation:
            Computing using the profile:
            (4, 3, 2, 1)
            Resolving the kernel in the range of dimensions [7, 17]:
             7 8 9 10 11 12 13 14 15 16 17.

            sage: K.domain().generators()
            (g[7],)
            sage: K.domain().relations()
            ((Sq(0,1)+Sq(3))*g[7],
             (Sq(0,0,1)+Sq(1,2)+Sq(4,1))*g[7],
             Sq(9)*g[7],
             (Sq(0,1,1)+Sq(4,2))*g[7])

            sage: K
            Module morphism:
              From: Finitely presented left module on 1 generator and 4 relations over sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [4, 3, 2, 1]
              To:   Finitely presented left module on 2 generators and 6 relations over sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [4, 3, 2, 1]
              Defn: g[7] |--> g[7]
        """
    def image(self, top_dim=None, verbose: bool = False):
        """
        Compute the image of ``self``.

        INPUT:

        - ``top_dim`` -- integer (optional); used by this function to stop the
          computation at the given degree
        - ``verbose`` -- boolean (default: ``False``); enable progress messages

        OUTPUT:

        A homomorphism into `\\operatorname{im}(self)` that is an
        isomorphism in degrees less than or equal to ``top_dim``

        .. NOTE::

            If the algebra for this module is finite, then no ``top_dim``
            needs to be specified in order to ensure that this function
            terminates.

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A3 = SteenrodAlgebra(2, profile=(4,3,2,1))
            sage: F = FPModule(A3, [1,3]);
            sage: L = FPModule(A3, [2,3], [[Sq(2),Sq(1)], [0,Sq(2)]]);
            sage: H = Hom(F, L);

            sage: H([L((A3.Sq(1), 1)), L((0, A3.Sq(2)))]).image() # long time
            Module morphism:
              From: Finitely presented left module on 1 generator and 1 relation over sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [4, 3, 2, 1]
              To:   Finitely presented left module on 2 generators and 2 relations over sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [4, 3, 2, 1]
              Defn: g[3] |--> Sq(1)*g[2] + g[3]

            sage: M = FPModule(A3, [0,7], [[Sq(1), 0], [Sq(2), 0], [Sq(4), 0], [Sq(8), Sq(1)], [0, Sq(7)], [0, Sq(0,1,1)+Sq(4,2)]])
            sage: F2 = FPModule(A3, [0], [[Sq(1)], [Sq(2)], [Sq(4)], [Sq(8)], [Sq(15)]])
            sage: H = Hom(M, F2)
            sage: f = H([F2([1]), F2([0])])
            sage: K = f.image(verbose=True, top_dim=17)
            1. Computing the generators of the image presentation:
            Resolving the image in the range of dimensions [0, 17]:
             0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17.
            2. Computing the relations of the image presentation:
            Computing using the profile:
            (4, 3, 2, 1)
            Resolving the kernel in the range of dimensions [0, 17]:
             0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17.

            sage: K.is_injective()  # long time
            True
            sage: K.domain().generator_degrees()
            (0,)
            sage: K.domain().relations()
            (Sq(1)*g[0], Sq(2)*g[0], Sq(4)*g[0], Sq(8)*g[0])
            sage: K.domain().is_trivial()
            False
        """
    def is_injective(self, top_dim=None, verbose: bool = False) -> bool:
        """
        Return ``True`` if and only if ``self`` has a trivial kernel.

        INPUT:

        - ``top_dim`` -- integer (optional); used by this function to stop the
          computation at the given degree
        - ``verbose`` -- boolean (default: ``False``); enable progress messages

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A = SteenrodAlgebra(2)

            sage: K = FPModule(A, [2], [[Sq(2)]])
            sage: HZ = FPModule(A, [0], [[Sq(1)]])

            sage: f = Hom(K, HZ)([Sq(2)*HZ([1])])
            sage: f.is_injective(top_dim=23)
            True

        TESTS::

            sage: Z = FPModule(A, [])
            sage: Hom(Z, HZ).zero().is_injective(top_dim=8)
            True
        """
    def is_surjective(self) -> bool:
        """
        Return ``True`` if and only if ``self`` has a trivial cokernel.

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A = SteenrodAlgebra(2)
            sage: F = FPModule(A, [0])

            sage: f = Hom(F,F)([Sq(1)*F.generator(0)])
            sage: f.is_surjective()
            False

        TESTS::

            sage: Z = FPModule(A, [])
            sage: Hom(F, Z).zero().is_surjective()
            True
        """
    def fp_module(self):
        """
        Create a finitely presented module from ``self``.

        OUTPUT:

        The finitely presented module having presentation equal to ``self``
        as long as the domain and codomain are free.

        EXAMPLES:

        We construct examples with free modules that are presented
        with a redundant relation::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A = SteenrodAlgebra(2)
            sage: F1 = FPModule(A, (2,), [[0]])
            sage: F2 = FPModule(A, (0,), [[0]])
            sage: v = F2([Sq(2)])
            sage: pres = Hom(F1, F2)([v])
            sage: M = pres.fp_module(); M
            Finitely presented left module on 1 generator and 1 relation over
             mod 2 Steenrod algebra, milnor basis
            sage: M.generator_degrees()
            (0,)
            sage: M.relations()
            (Sq(2)*g[0],)

            sage: F2 = A.free_graded_module((0,))
            sage: v = F2([Sq(2)])
            sage: pres = Hom(F1, F2)([v])
            sage: M = pres.fp_module(); M
            Finitely presented left module on 1 generator and 1 relation over
             mod 2 Steenrod algebra, milnor basis
            sage: M.generator_degrees()
            (0,)
            sage: M.relations()
            (Sq(2)*g[0],)

            sage: F3 = FPModule(A, (0,), [[Sq(4)]])
            sage: v = F3([Sq(2)])
            sage: pres = Hom(F1, F3)([v])
            sage: pres.fp_module()
            Traceback (most recent call last):
            ...
            ValueError: this is not a morphism between free modules
        """
