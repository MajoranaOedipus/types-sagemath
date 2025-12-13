from sage.categories.graded_modules import GradedModules as GradedModules
from sage.categories.homset import Hom as Hom
from sage.categories.principal_ideal_domains import PrincipalIdealDomains as PrincipalIdealDomains
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.misc.cachefunc import cached_method as cached_method
from sage.modules.fp_graded.free_element import FreeGradedModuleElement as FreeGradedModuleElement
from sage.modules.free_module import FreeModule as FreeModule
from sage.rings.infinity import infinity as infinity

class FreeGradedModule(CombinatorialFreeModule):
    """
    Create a finitely generated free graded module over a connected
    graded algebra, with generators in specified degrees.

    INPUT:

    - ``algebra`` -- the graded connected algebra over which the module is
      defined; this algebra must be equipped with a graded basis

    - ``generator_degrees`` -- tuple of integers defining the number
      of generators of the module, and their degrees

    - ``names`` -- (optional) the names of the generators. If ``names``
      is a comma-separated string like ``'a, b, c'``, then those will
      be the names. Otherwise, for example if ``names`` is ``abc``,
      then the names will be ``abc(d,i)``.

    By default, if all generators are in distinct degrees, then the
    ``names`` of the generators will have the form ``g_{d}`` where
    ``d`` is the degree of the generator. If the degrees are not
    distinct, then the generators will be called ``g_{d,i}`` where
    ``d`` is the degree and ``i`` is its index in the list of
    generators in that degree.

    EXAMPLES::

        sage: from sage.modules.fp_graded.free_module import FreeGradedModule
        sage: E.<x,y,z> = ExteriorAlgebra(QQ)
        sage: M = FreeGradedModule(E, (-1,3))
        sage: M
        Free graded left module on 2 generators over
         The exterior algebra of rank 3 over Rational Field
        sage: M.generator_degrees()
        (-1, 3)
        sage: a, b = M.generators()
        sage: (x*y*b).degree()
        5

    ``names`` of generators::

        sage: M.generators()
        (g[-1], g[3])
        sage: FreeGradedModule(E, (0, 0, 2)).generators()
        (g[0, 0], g[0, 1], g[2, 0])
        sage: FreeGradedModule(E, (0, 0, 2), names='x, y, z').generators()
        (x, y, z)
        sage: FreeGradedModule(E, (0, 0, 2), names='xyz').generators()
        (xyz[0, 0], xyz[0, 1], xyz[2, 0])

    ``names`` can also be defined implicitly using Sage's ``M.<...>`` syntax::

        sage: A = SteenrodAlgebra(2)
        sage: M.<x,y,z> = FreeGradedModule(A, (-2,2,4))
        sage: M
        Free graded left module on 3 generators over
         mod 2 Steenrod algebra, milnor basis
        sage: M.gens()
        (x, y, z)
    """
    def __classcall__(cls, algebra, generator_degrees, category=None, names=None, prefix=None, **kwds):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: E.<x,y> = ExteriorAlgebra(QQ)
            sage: from sage.modules.fp_graded.free_module import FreeGradedModule
            sage: M1 = FreeGradedModule(E, [1, 0, 2], names='a,b,c')
            sage: M2.<a,b,c> = FreeGradedModule(E, (1, 0, 2))
            sage: M1 is M2
            True
        """
    def __init__(self, algebra, generator_degrees, category, names=None, **kwds) -> None:
        """
        Create a finitely generated free graded module over a connected graded
        algebra.

        TESTS::

            sage: from sage.modules.fp_graded.free_module import FreeGradedModule
            sage: A = SteenrodAlgebra(2)
            sage: TestSuite(FreeGradedModule(A, (-2,2,4))).run()
        """
    Element = FreeGradedModuleElement
    def change_ring(self, algebra):
        """
        Change the base ring of ``self``.

        INPUT:

        - ``algebra`` -- a connected graded algebra

        OUTPUT:

        The free graded module over ``algebra`` defined with the same
        number of generators of the same degrees as ``self``.

        EXAMPLES::

            sage: from sage.modules.fp_graded.free_module import FreeGradedModule
            sage: A = SteenrodAlgebra(2)
            sage: A2 = SteenrodAlgebra(2, profile=(3,2,1))

            sage: M = FreeGradedModule(A, [0,1])
            sage: N = M.change_ring(A2); N
            Free graded left module on 2 generators over sub-Hopf algebra of
             mod 2 Steenrod algebra, milnor basis, profile function [3, 2, 1]

        Changing back yields the original module::

            sage: N.change_ring(A) is M
            True
        """
    def generator_degrees(self):
        """
        The degrees of the module generators.

        OUTPUT:

        A tuple containing the degrees of the generators for this
        module, in the order that the generators were given when
        ``self`` was constructed.

        EXAMPLES::

            sage: from sage.modules.fp_graded.free_module import FreeGradedModule
            sage: A = SteenrodAlgebra(2)
            sage: M = FreeGradedModule(A, (-2,2,4))
            sage: M.generator_degrees()
            (-2, 2, 4)
        """
    def is_trivial(self) -> bool:
        """
        Return ``True`` if this module is trivial and ``False`` otherwise.

        EXAMPLES::

            sage: from sage.modules.fp_graded.free_module import FreeGradedModule
            sage: A = SteenrodAlgebra(2)
            sage: FreeGradedModule(A, (-2,2,4)).is_trivial()
            False
            sage: FreeGradedModule(A, ()).is_trivial()
            True
        """
    def connectivity(self):
        """
        The connectivity of ``self``.

        OUTPUT:

        An integer equal to the minimal degree of all the generators, if
        this module is non-trivial.  Otherwise, `+\\infty`.

        EXAMPLES::

            sage: from sage.modules.fp_graded.free_module import FreeGradedModule
            sage: A = SteenrodAlgebra(2)
            sage: M = FreeGradedModule(A, (-2,2,4))
            sage: M.connectivity()
            -2

        TESTS::

            sage: M = FreeGradedModule(A, ())
            sage: M.is_trivial()
            True
            sage: M.connectivity()
            +Infinity
        """
    def an_element(self, n=None):
        """
        Return an element of ``self``.

        This function chooses deterministically an element of the module
        in the given degree.

        INPUT:

        - ``n`` -- (optional) the degree of the element to construct

        OUTPUT:

        An element (of the given degree if specified).

        EXAMPLES::

            sage: from sage.modules.fp_graded.free_module import FreeGradedModule
            sage: A = SteenrodAlgebra(2)
            sage: M = FreeGradedModule(A, (0,2,4))
            sage: M.an_element(172)
            Sq(0,0,2,0,1,0,1)*g[0] + Sq(0,4,0,0,1,0,1)*g[2] + Sq(7,1,0,0,1,0,1)*g[4]

        Zero is the only element in the trivial module::

            sage: FreeGradedModule(A, ()).an_element()
            0
        """
    def basis_elements(self, n):
        """
        Return a basis for the free module of degree ``n`` module elements.

        .. NOTE::

            Suppose ``self`` is a module over the graded algebra `A` with
            base ring `R`. This returns a basis as a free module over `R`,
            not a basis as a free module over `A`.

        INPUT:

        - ``n`` -- integer

        OUTPUT:

        A sequence of homogeneous module elements of degree ``n``, which
        is a basis for the free module of all degree ``n`` module elements.

        .. SEEALSO::

            :meth:`vector_presentation`, :meth:`element_from_coordinates`

        EXAMPLES::

            sage: A = SteenrodAlgebra(2)
            sage: M.<m0, m2, m4> = A.free_graded_module((0,2,4))
            sage: M.basis_elements(8)
            (Sq(1,0,1)*m0,
             Sq(2,2)*m0,
             Sq(5,1)*m0,
             Sq(8)*m0,
             Sq(0,2)*m2,
             Sq(3,1)*m2,
             Sq(6)*m2,
             Sq(1,1)*m4,
             Sq(4)*m4)
        """
    @cached_method
    def element_from_coordinates(self, coordinates, n):
        """
        The module element of degree ``n`` having the given coordinates
        with respect to the basis of module elements given by
        :meth:`basis_elements`.

        INPUT:

        - ``coordinates`` -- a sequence of elements of the ground ring
        - ``n`` -- integer

        OUTPUT: a module element of degree ``n``

        .. SEEALSO::

            :meth:`vector_presentation`, and :meth:`basis_elements`.

        EXAMPLES::

            sage: A = SteenrodAlgebra(2)
            sage: M = A.free_graded_module((0,1))
            sage: x = M.element_from_coordinates((0,1,0,1), 5); x
            Sq(5)*g[0] + Sq(4)*g[1]
            sage: basis = M.basis_elements(5)
            sage: y = 0*basis[0] + 1*basis[1] + 0*basis[2] + 1*basis[3]
            sage: x == y
            True

            sage: M.element_from_coordinates((0,0,0,0), 5)
            0
        """
    @cached_method
    def vector_presentation(self, n):
        """
        Return a free module over the ground ring of the module algebra
        isomorphic to the degree ``n`` elements of ``self``.

        Let `\\mathcal{k}` be the ground ring of the algebra over this module
        is defined, and let `M_n` be the free module of module elements of
        degree ``n``.

        The return value of this function is the free module
        `\\mathcal{k}^{r}` where `r = dim(M_n)`.

        The isomorphism between `k^{r}` and `M_n` is given by the
        bijection taking the standard basis element `e_i` to the `i`-th
        element of the array returned by :meth:`basis_elements`.

        INPUT:

        - ``n`` -- integer degree

        OUTPUT:

        A free module over the ground ring of the algebra over which
        ``self`` is defined, isomorphic to the free module of module
        elements of degree ``n``.

        .. SEEALSO::

            :meth:`basis_elements`, :meth:`element_from_coordinates`

        EXAMPLES::

            sage: A1 = SteenrodAlgebra(2, profile=[2,1])
            sage: M.<x> = A1.free_graded_module((0,))
            sage: M.vector_presentation(3)
            Vector space of dimension 2 over Finite Field of size 2
            sage: M.basis_elements(3)
            (Sq(0,1)*x, Sq(3)*x)
            sage: [M.vector_presentation(i).dimension() for i in range(-2, 9)]
            [0, 0, 1, 1, 1, 2, 1, 1, 1, 0, 0]

        TESTS::

            sage: A = SteenrodAlgebra(2)
            sage: M = A.free_graded_module((0,2,4))
            sage: V = M[4]; V
            Vector space of dimension 4 over Finite Field of size 2
            sage: V.dimension()
            4
        """
    __getitem__ = vector_presentation
    def generator(self, index):
        """
        Return the module generator with the given index.

        EXAMPLES::

            sage: from sage.modules.fp_graded.free_module import FreeGradedModule
            sage: A = SteenrodAlgebra(2)
            sage: M = FreeGradedModule(A, (0,2,4))
            sage: M.generator(0)
            g[0]
            sage: M.generator(1)
            g[2]
            sage: M.generator(2)
            g[4]
        """
    gen = generator
    def generators(self):
        """
        Return all the module generators.

        EXAMPLES::

            sage: from sage.modules.fp_graded.free_module import FreeGradedModule
            sage: A = SteenrodAlgebra(2)
            sage: M = FreeGradedModule(A, (-2,1))
            sage: M.generators()
            (g[-2], g[1])
        """
    def suspension(self, t):
        """
        Suspend ``self`` by the given degree ``t``.

        INPUT:

        - ``t`` -- integer

        OUTPUT:

        A module which is isomorphic to this module by a shift
        of degrees by the integer ``t``.

        EXAMPLES::

            sage: from sage.modules.fp_graded.free_module import FreeGradedModule
            sage: A = SteenrodAlgebra(2)
            sage: M = FreeGradedModule(A, (0,2,4))
            sage: M.suspension(4).generator_degrees()
            (4, 6, 8)
            sage: M.suspension(-4).generator_degrees()
            (-4, -2, 0)
        """
    def has_relations(self) -> bool:
        """
        Return ``False`` as this has no relations.

        This is for compatibility with
        :class:`~sage.modules.fp_graded.module.FPModule`.

        EXAMPLES::

            sage: from sage.modules.fp_graded.free_module import FreeGradedModule
            sage: A = SteenrodAlgebra(2)
            sage: F = FreeGradedModule(A, (-2,2,4))
            sage: F.has_relations()
            False
        """
    def relations(self):
        """
        Return the relations of ``self``, which is ``()``.

        This is for compatibility with
        :class:`~sage.modules.fp_graded.module.FPModule`.

        EXAMPLES::

            sage: from sage.modules.fp_graded.free_module import FreeGradedModule
            sage: A = SteenrodAlgebra(2)
            sage: F = FreeGradedModule(A, (-2,2,4))
            sage: F.relations()
            ()
        """
    def resolution(self, k, top_dim=None, verbose: bool = False):
        """
        Return a free resolution of ``self`` of length ``k``.

        Since ``self`` is free, the initial map in the resolution will
        be the identity, and the rest of the maps will be zero.

        INPUT:

        - ``k`` -- nonnegative integer
        - ``top_dim`` -- stop the computation at this degree. Ignored,
          for compatibility with
          :meth:`sage.modules.fp_graded.module.FPModule.resolution`.
        - ``verbose`` -- boolean (default: ``False``); controls whether log
          messages should be emitted

        OUTPUT:

        A list of homomorphisms `[1_M, 0, 0, \\ldots, 0]` consisting of
        the identity map on this module followed by zero maps. Other
        than this module, the other modules in the resolution will be
        zero.

        EXAMPLES::

            sage: E.<x,y,z> = ExteriorAlgebra(QQ)
            sage: M = E.free_graded_module((1,2))
            sage: M.resolution(0)
            [Module endomorphism of Free graded left module on 2 generators over The exterior algebra of rank 3 over Rational Field
               Defn: g[1] |--> g[1]
                     g[2] |--> g[2]]
            sage: M.resolution(1)
            [Module endomorphism of Free graded left module on 2 generators over The exterior algebra of rank 3 over Rational Field
               Defn: g[1] |--> g[1]
                     g[2] |--> g[2],
             Module morphism:
               From: Free graded left module on 0 generators over The exterior algebra of rank 3 over Rational Field
               To:   Free graded left module on 2 generators over The exterior algebra of rank 3 over Rational Field]
            sage: M.resolution(4)
            [Module endomorphism of Free graded left module on 2 generators over The exterior algebra of rank 3 over Rational Field
               Defn: g[1] |--> g[1]
                     g[2] |--> g[2],
             Module morphism:
               From: Free graded left module on 0 generators over The exterior algebra of rank 3 over Rational Field
               To:   Free graded left module on 2 generators over The exterior algebra of rank 3 over Rational Field,
             Module endomorphism of Free graded left module on 0 generators over The exterior algebra of rank 3 over Rational Field,
             Module endomorphism of Free graded left module on 0 generators over The exterior algebra of rank 3 over Rational Field,
             Module endomorphism of Free graded left module on 0 generators over The exterior algebra of rank 3 over Rational Field]
        """
    def minimal_presentation(self, top_dim=None, verbose: bool = False):
        """
        Return a minimal presentation of ``self``.

        OUTPUT: the identity morphism as ``self`` is free

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A2 = SteenrodAlgebra(2)

            sage: M = A2.free_graded_module([0,1])
            sage: M.minimal_presentation().is_identity()
            True
        """
