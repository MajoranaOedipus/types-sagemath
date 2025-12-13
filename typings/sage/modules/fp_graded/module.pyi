from sage.categories.graded_modules import GradedModules as GradedModules
from sage.categories.homset import Hom as Hom
from sage.categories.morphism import Morphism as Morphism
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.modules.fp_graded.element import FPElement as FPElement
from sage.modules.fp_graded.free_element import FreeGradedModuleElement as FreeGradedModuleElement
from sage.modules.fp_graded.free_module import FreeGradedModule as FreeGradedModule
from sage.modules.module import Module as Module
from sage.rings.infinity import infinity as infinity
from sage.structure.element import parent as parent
from sage.structure.indexed_generators import IndexedGenerators as IndexedGenerators
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class FPModule(UniqueRepresentation, IndexedGenerators, Module):
    """
    A finitely presented module over a connected graded algebra.

    INPUT:

    One of the following:

    - ``arg0`` -- a morphism such that the module is the cokernel, or
      a free graded module, in which case the output is the same
      module, viewed as finitely presented

    Otherwise:

    - ``arg0`` -- the graded connected algebra over which the module is
      defined; this algebra must be equipped with a graded basis

    - ``generator_degrees`` -- tuple of integer degrees

    - ``relations`` -- tuple of relations; a relation is a tuple of
      coefficients `(c_1, \\ldots, c_n)`, ordered so that they
      correspond to the module generators, that is, such a tuple
      corresponds to the relation

      .. MATH::

          c_1 g_1 + \\ldots + c_n g_n = 0

      if the generators are `(g_1, \\ldots, g_n)`

    EXAMPLES::

        sage: from sage.modules.fp_graded.module import FPModule

        sage: E.<x,y> = ExteriorAlgebra(QQ)
        sage: M = FPModule(E, [0, 1], [[x, 1]])
        sage: a, b = M.generators()
        sage: x*a + b == 0
        True
        sage: (x*a + b).normalize()
        0

        sage: A3 = SteenrodAlgebra(2, profile=(4,3,2,1))
        sage: M = FPModule(A3, [0, 1], [[Sq(2), Sq(1)]])
        sage: M.generators()
        (g[0], g[1])
        sage: M.relations()
        (Sq(2)*g[0] + Sq(1)*g[1],)
        sage: M.is_trivial()
        False

        sage: Z = FPModule(A3, [])
        sage: Z.generators()
        ()
        sage: Z.relations()
        ()
        sage: Z.is_trivial()
        True

        sage: from sage.modules.fp_graded.free_module import FreeGradedModule
        sage: F = FreeGradedModule(E, [0, 1])
        sage: one = Hom(F, F).identity()
        sage: Z = FPModule(one)
        sage: Z.is_trivial()
        True

        sage: FPModule(E.free_graded_module([0, 1]))
        Free graded left module on 2 generators over The exterior algebra of rank 2 over Rational Field
    """
    @staticmethod
    def __classcall__(cls, arg0, generator_degrees=None, relations=(), names=None):
        """
        Normalize input to ensure a unique representation.

        TESTS::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A3 = SteenrodAlgebra(2, profile=(4,3,2,1))
            sage: M1.<m0,m1> = FPModule(A3, [0, 1], [[Sq(2), Sq(1)]])
            sage: M2 = FPModule(A3, (0, 1), [[Sq(2), Sq(1)]], names='m0,m1')
            sage: M1 is M2
            True
        """
    def __init__(self, j, names) -> None:
        """
        Create a finitely presented module over a connected graded algebra.

        TESTS::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A3 = SteenrodAlgebra(2, profile=(4,3,2,1))
            sage: M = FPModule(A3, [0, 1], [[Sq(2), Sq(1)]])
            sage: TestSuite(M).run()

        Checking containment::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: M = FPModule(SteenrodAlgebra(2), [0,1], [[Sq(4), Sq(3)]])
            sage: x = M([Sq(1), 1])
            sage: x in M
            True
            sage: N = FPModule(SteenrodAlgebra(2), [0], [[Sq(2)]])
            sage: y = Sq(2) * N.generator(0)
            sage: y in M
            False
        """
    Element = FPElement
    def defining_homomorphism(self):
        """
        Return the homomorphism defining ``self``.

        ``self`` is a finitely presented module defined as the
        cokernel of a map `j: F_0 \to F_1` of free modules, and this
        returns that map.

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: E.<x,y> = ExteriorAlgebra(QQ)
            sage: M = FPModule(E, [0, 1], [[x, 1]])
            sage: M.defining_homomorphism()
            Module morphism:
              From: Free graded left module on 1 generator over The exterior algebra of rank 2 over Rational Field
              To:   Free graded left module on 2 generators over The exterior algebra of rank 2 over Rational Field
              Defn: g[1] |--> x*g[0] + g[1]
        """
    def change_ring(self, algebra):
        """
        Change the base ring of ``self``.

        INPUT:

        - ``algebra`` -- a connected graded algebra

        OUTPUT:

        The finitely presented module over ``algebra`` defined with the
        exact same number of generators of the same degrees and relations
        as ``self``.

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A = SteenrodAlgebra(2)
            sage: A2 = SteenrodAlgebra(2, profile=(3,2,1))

            sage: M = FPModule(A, [0,1], [[Sq(2), Sq(1)]])
            sage: N = M.change_ring(A2); N
            Finitely presented left module on 2 generators and 1 relation over
             sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [3, 2, 1]

        Changing back yields the original module::

            sage: N.change_ring(A) is M
            True

        TESTS:

        Subclasses preserve their type::

            sage: from sage.modules.fp_graded.steenrod.module import SteenrodFPModule
            sage: A = SteenrodAlgebra(2)
            sage: A1 = SteenrodAlgebra(2, profile=(2,1))

            sage: M = SteenrodFPModule(A, [0,1], [[Sq(2), Sq(1)]])
            sage: N = M.change_ring(A1)
            sage: isinstance(N, SteenrodFPModule)
            True

        Changing back yields the original module::

            sage: N.change_ring(A) is M
            True
        """
    @lazy_attribute
    def monomial(self):
        """
        Return the basis element indexed by ``i``.

        INPUT:

        - ``i`` -- an element of the index set

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: M = FPModule(SteenrodAlgebra(2), [0,1], [[Sq(4), Sq(3)]])
            sage: M.monomial(0)
            g[0]
            sage: M.monomial(1)
            g[1]
        """
    @cached_method
    def zero(self):
        """
        Return the zero element.

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: M = FPModule(SteenrodAlgebra(2), [0,1], [[Sq(4), Sq(3)]])
            sage: M.zero()
            0
        """
    def connectivity(self):
        """
        The connectivity of ``self``.

        Since a finitely presented module over a connected algebra is in
        particular bounded below, the connectivity is an integer when the
        module is non-trivial, and `+\\infty` when the module is trivial.

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A = SteenrodAlgebra(2)

            sage: M = FPModule(A, [0,2,4], [[0, Sq(5), Sq(3)], [Sq(7), 0, Sq(2)*Sq(1)]])
            sage: M.connectivity()
            0

            sage: G = FPModule(A, [0,2], [[1,0]])
            sage: G.connectivity()
            2

        TESTS::

            sage: C = FPModule(SteenrodAlgebra(2, profile=(3,2,1)), [0], relations=[[Sq(1)], [0]])
            sage: C.connectivity()
            0

            sage: F = FPModule(A, [-1])
            sage: F.connectivity()
            -1

            sage: F = FPModule(A, [])
            sage: F.connectivity()
            +Infinity

            sage: F = FPModule(A, [0], [[1]])
            sage: F.connectivity()
            +Infinity
        """
    def is_trivial(self) -> bool:
        """
        Return ``True`` if ``self`` is isomorphic to the trivial module
        and ``False`` otherwise.

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A = SteenrodAlgebra(2)
            sage: A2 = SteenrodAlgebra(2, profile=(3,2,1))

            sage: M = FPModule(A2, [])
            sage: M.is_trivial()
            True

            sage: N = FPModule(A, [1,2])
            sage: N.is_trivial()
            False

            sage: P = FPModule(A, [1,2], [[1,0], [0,1]])
            sage: P.is_trivial()
            True

        TESTS::

            sage: C = FPModule(SteenrodAlgebra(2, profile=(3,2,1)), [0], [[Sq(1)], [0]])
            sage: C.is_trivial()
            False

            sage: C = FPModule(SteenrodAlgebra(2), [0], [[Sq(1)], [1]])
            sage: C.is_trivial()
            True
        """
    def has_relations(self) -> bool:
        """
        Return ``True`` if no relations are defined, and ``False``
        otherwise.

        .. NOTE::

            This module is free if this function returns ``False``, but a free
            module can have (redundant) relations.

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A2 = SteenrodAlgebra(2, profile=(3,2,1))

            sage: F = FPModule(A2, [1,2])
            sage: F.has_relations()
            False

            sage: M = FPModule(A2, [1,2], [[Sq(2), Sq(1)]])
            sage: M.has_relations()
            True

        A free module constructed with a redundant generator and relation::

            sage: N = FPModule(A2, [0, 0], [[0, 1]])
            sage: N.has_relations()
            True
            sage: # Computing a minimal presentation reveals an
            ....: # isomorphic module with no relations.
            sage: N_min = N.minimal_presentation().domain()
            sage: N_min.has_relations()
            False
        """
    def an_element(self, n=None):
        """
        An element of this module.

        This function chooses deterministically an element, i.e. the output
        depends only on the module and its input ``n``.

        INPUT:

        - ``n`` -- (optional) the degree of the element to construct

        OUTPUT: a module element of the given degree

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A2 = SteenrodAlgebra(2, profile=(3,2,1))
            sage: M = FPModule(A2, [0,2,4], [[0, Sq(5), Sq(3)], [Sq(7), 0, Sq(2)*Sq(1)]])

            sage: [M.an_element(i) for i in range(10)]
            [g[0],
             Sq(1)*g[0],
             Sq(2)*g[0] + g[2],
             Sq(0,1)*g[0] + Sq(1)*g[2],
             Sq(1,1)*g[0] + Sq(2)*g[2] + g[4],
             Sq(2,1)*g[0] + Sq(0,1)*g[2] + Sq(1)*g[4],
             Sq(0,2)*g[0] + Sq(1,1)*g[2] + Sq(2)*g[4],
             Sq(0,0,1)*g[0] + Sq(2,1)*g[2] + Sq(0,1)*g[4],
             Sq(1,0,1)*g[0] + Sq(6)*g[2] + Sq(1,1)*g[4],
             Sq(2,0,1)*g[0] + Sq(4,1)*g[2] + Sq(2,1)*g[4]]
        """
    @cached_method
    def basis_elements(self, n, verbose: bool = False):
        """
        Return a basis for the free module of degree ``n`` module elements.

        .. NOTE::

            Suppose ``self`` is a module over the graded algebra `A` with
            base ring `R`. This returns a basis as a free module over `R`.

        INPUT:

        - ``n`` -- integer
        - ``verbose`` -- boolean (default: ``False``); controls whether log
          messages should be emitted

        OUTPUT:

        A list of homogeneous module elements of degree ``n`` which is
        a basis for the free module of all degree ``n`` module elements.

        .. SEEALSO::

            :meth:`vector_presentation`, :meth:`element_from_coordinates`

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A2 = SteenrodAlgebra(2, profile=(3,2,1))
            sage: M.<m0,m2> = FPModule(A2, [0,2], [[Sq(4), Sq(2)], [0, Sq(6)]])

            sage: M.basis_elements(4)
            (Sq(1,1)*m0, Sq(4)*m0)

            sage: M.basis_elements(5)
            (Sq(2,1)*m0, Sq(5)*m0, Sq(0,1)*m2)

            sage: M.basis_elements(25)
            ()

            sage: M.basis_elements(0)
            (m0,)

            sage: M.basis_elements(2)
            (Sq(2)*m0, m2)

        TESTS::

            sage: Z0 = FPModule(A2, [])
            sage: Z0.basis_elements(n=10)
            ()

            sage: Z1 = FPModule(A2, [1], [[1]])
            sage: Z1.basis_elements(n=10)
            ()
        """
    @cached_method
    def element_from_coordinates(self, coordinates, n):
        """
        Return the module element in degree ``n`` having the given coordinates
        with respect to the basis returned by :meth:`basis_elements`.

        This function is inverse to
        :meth:`sage.modules.fp_graded.element.FPElement.vector_presentation`.

        INPUT:

        - ``coordinates`` -- a vector of coordinates
        - ``n`` -- the degree of the element to construct

        OUTPUT:

        A module element of degree ``n`` having the given coordinates
        with respect to the basis returned by :meth:`basis_elements`.

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A = SteenrodAlgebra(2)
            sage: M = FPModule(A, [0], [[Sq(4)], [Sq(7)], [Sq(4)*Sq(9)]])

            sage: M.vector_presentation(12).dimension()
            3
            sage: x = M.element_from_coordinates((0,1,0), 12); x
            Sq(0,4)*g[0]

        Applying the inverse function brings us back to the coordinate form::

            sage: x.vector_presentation()
            (0, 1, 0)

        TESTS::

            sage: M.element_from_coordinates((0,1,0,0), 12)
            Traceback (most recent call last):
             ...
            ValueError: the given coordinate vector has incorrect length (4);
             it should have length 3

        .. SEEALSO::

            :meth:`sage.modules.fp_graded.module.FPModule.vector_presentation`
        """
    @cached_method
    def vector_presentation(self, n, verbose: bool = False):
        """
        Return a free module isomorphic to the free module of module
        elements of degree ``n``.

        INPUT:

        - ``n`` -- the degree of the presentation

        OUTPUT: a vector space

        .. SEEALSO::

            :meth:`basis_elements`, :meth:`element_from_coordinates`

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A = SteenrodAlgebra(2)
            sage: M = FPModule(A, [0,2,4], [[Sq(4),Sq(2),0]])

            sage: V = M.vector_presentation(4)
            sage: V.dimension()
            3

            sage: len(M.basis_elements(4))
            3

        TESTS::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A = SteenrodAlgebra(2)
            sage: M = FPModule(A, [0,2,4], [[Sq(4),Sq(2),0]])
            sage: M[4].dimension()
            3
        """
    __getitem__ = vector_presentation
    def generator_degrees(self):
        """
        Return the degrees of the generators for ``self``.

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A4 = SteenrodAlgebra(2, profile=(4,3,2,1))
            sage: N = FPModule(A4, [0, 1], [[Sq(2), Sq(1)]])

            sage: N.generator_degrees()
            (0, 1)
        """
    def generators(self):
        """
        Return the generators of ``self``.

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A4 = SteenrodAlgebra(2, profile=(4,3,2,1))

            sage: M = FPModule(A4, [0,0,2,3])
            sage: M.generators()
            (g[0, 0], g[0, 1], g[2, 0], g[3, 0])

            sage: N = FPModule(A4, [0, 1], [[Sq(2), Sq(1)]], names='h')
            sage: N.generators()
            (h[0], h[1])

            sage: Z = FPModule(A4, [])
            sage: Z.generators()
            ()
        """
    gens = generators
    def generator(self, index):
        """
        Return the module generator with the given index.

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A4 = SteenrodAlgebra(2, profile=(4,3,2,1))

            sage: M = FPModule(A4, [0,2,3])
            sage: M.generator(0)
            g[0]

            sage: N = FPModule(A4, [0, 1], [[Sq(2), Sq(1)]], names='h')
            sage: N.generator(1)
            h[1]
        """
    gen = generator
    def relations(self):
        """
        Return the relations of ``self``.

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A4 = SteenrodAlgebra(2, profile=(4,3,2,1))

            sage: M = FPModule(A4, [0,2,3])
            sage: M.relations()
            ()

            sage: N = FPModule(A4, [0, 1], [[Sq(2), Sq(1)]])
            sage: N.relations()
            (Sq(2)*g[0] + Sq(1)*g[1],)

            sage: Z = FPModule(A4, [])
            sage: Z.relations()
            ()
        """
    def relation(self, index):
        """
        Return the module relation of the given index.

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A4 = SteenrodAlgebra(2, profile=(4,3,2,1))
            sage: N = FPModule(A4, [0, 1], [[Sq(2), Sq(1)]])
            sage: N.relation(0)
            Sq(2)*g[0] + Sq(1)*g[1]
        """
    def minimal_presentation(self, top_dim=None, verbose: bool = False):
        """
        Return a minimal presentation of ``self``.

        OUTPUT:

        An isomorphism `M \\to S`, where `M` has minimal presentation
        and `S` is ``self``.

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A2 = SteenrodAlgebra(2, profile=(3,2,1))

            sage: M = FPModule(A2, [0,1], [[Sq(2),Sq(1)],[0,Sq(2)],[Sq(3),0]])
            sage: i = M.minimal_presentation()
            sage: M_min = i.domain()

        ``i`` is an isomorphism between ``M_min`` and ``M``::

            sage: i.codomain() is M
            True
            sage: i.is_injective()
            True
            sage: i.is_surjective()
            True

        There are more relations in ``M`` than in ``M_min``::

            sage: M.relations()
            (Sq(2)*g[0] + Sq(1)*g[1], Sq(2)*g[1], Sq(3)*g[0])
            sage: M_min.relations()
            (Sq(2)*g[0] + Sq(1)*g[1], Sq(2)*g[1])

        TESTS::

            sage: T = FPModule(A2, [0], [[1]])
            sage: T_min = T.minimal_presentation().domain()
            sage: T_min.is_trivial()
            True
            sage: T_min
            Free graded left module on 0 generators over ...

        Similar example but using
        :class:`sage.modules.fp_graded.steenrod.module.SteenrodFPModule`::

            sage: from sage.modules.fp_graded.steenrod.module import SteenrodFPModule
            sage: A = SteenrodAlgebra(2)
            sage: M = SteenrodFPModule(A, [0,1], [[Sq(2),Sq(1)],[0,Sq(2)],[Sq(3),0]])

            sage: i = M.minimal_presentation()
            sage: i.codomain() is M
            True

            sage: i.is_injective()
            True
            sage: i.is_surjective()
            True

            sage: i.domain().relations()
            (Sq(2)*g[0] + Sq(1)*g[1], Sq(2)*g[1])

            sage: i.codomain().relations()
            (Sq(2)*g[0] + Sq(1)*g[1], Sq(2)*g[1], Sq(3)*g[0])
        """
    def suspension(self, t):
        """
        Return the suspension of ``self`` by degree ``t``.

        INPUT:

        - ``t`` -- integer degree by which the module is suspended

        OUTPUT:

        A module which is identical to this module by a shift of
        degrees by the integer ``t``.

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A = SteenrodAlgebra(2)
            sage: A2 = SteenrodAlgebra(2, profile=(3,2,1))

            sage: Y = FPModule(A2, [0], [[Sq(1)]])
            sage: X = Y.suspension(4)
            sage: X.generator_degrees()
            (4,)
            sage: X.relations()
            (Sq(1)*g[4],)

            sage: M = FPModule(A, [2,3], [[Sq(2), Sq(1)], [0, Sq(2)]])
            sage: Q = M.suspension(1)
            sage: Q.generator_degrees()
            (3, 4)
            sage: Q.relations()
            (Sq(2)*g[3] + Sq(1)*g[4], Sq(2)*g[4])
            sage: Q = M.suspension(-3)
            sage: Q.generator_degrees()
            (-1, 0)
            sage: Q = M.suspension(0)
            sage: Q.generator_degrees()
            (2, 3)
        """
    def submodule_inclusion(self, spanning_elements):
        """
        Return the inclusion morphism of the submodule of ``self`` spanned
        by the given elements.

        INPUT:

        - ``spanning_elements`` -- an iterable of elements

        OUTPUT: the inclusion of the submodule into this module

        Because a submodule of a finitely presented module need not be
        finitely presented, this method will only work if the
        underlying algebra is finite-dimensional. Indeed, the current
        implementation only works if the algebra has a ``top_class``
        method, which gets used in
        :meth:`sage.modules.fp_graded.morphism._resolve_kernel`.

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A2 = SteenrodAlgebra(2, profile=(3,2,1))

            sage: M = FPModule(A2, [0,1], [[Sq(2),Sq(1)]])
            sage: i = M.submodule_inclusion([M.generator(0)])
            sage: i.codomain() is M
            True
            sage: i.is_injective()
            True
            sage: i.domain().generator_degrees()
            (0,)
            sage: i.domain().relations()
            (Sq(3)*g[0],)
        """
    def resolution(self, k, top_dim=None, verbose: bool = False):
        """
        Return a free resolution of this module of length ``k``.

        INPUT:

        - ``k`` -- nonnegative integer
        - ``top_dim`` -- stop the computation at this degree
          (default: ``None``, but required if the algebra is
          not finite-dimensional)
        - ``verbose`` -- boolean (default: ``False``); control if
          log messages should be emitted

        OUTPUT: list of homomorphisms `[\\epsilon, f_1, \\ldots, f_k]` such that

        .. MATH::

            f_i: F_i \\to F_{i-1} \\text{ for } 1 < i \\leq k,
            \\qquad
            \\epsilon: F_0 \\to M,

        where each `F_i` is a finitely generated free module, and the
        sequence

        .. MATH::

            F_k \\xrightarrow{\\mathit{f_k}} F_{k-1}
            \\xrightarrow{\\mathit{f_{k-1}}} \\ldots \\rightarrow F_0
            \\xrightarrow{\\epsilon} M \\rightarrow 0

        is exact. Note that the 0th element in this list is the map
        `\\epsilon`, and the rest of the maps are between free
        modules.

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule

            sage: E.<x,y> = ExteriorAlgebra(QQ)
            sage: M = FPModule(E, [0], [[x], [y]])
            sage: res = M.resolution(3); res
            [Module morphism:
               From: Free graded left module on 1 generator over The exterior algebra of rank 2 over Rational Field
               To:   Finitely presented left module on 1 generator and 2 relations over The exterior algebra of rank 2 over Rational Field
               Defn: g[0] |--> g[0],
             Module morphism:
               From: Free graded left module on 2 generators over The exterior algebra of rank 2 over Rational Field
               To:   Free graded left module on 1 generator over The exterior algebra of rank 2 over Rational Field
               Defn: g[1, 0] |--> x*g[0]
                     g[1, 1] |--> y*g[0],
             Module morphism:
               From: Free graded left module on 3 generators over The exterior algebra of rank 2 over Rational Field
               To:   Free graded left module on 2 generators over The exterior algebra of rank 2 over Rational Field
               Defn: g[2, 0] |--> x*g[1, 0]
                     g[2, 1] |--> y*g[1, 0] + x*g[1, 1]
                     g[2, 2] |--> y*g[1, 1],
             Module morphism:
               From: Free graded left module on 4 generators over The exterior algebra of rank 2 over Rational Field
               To:   Free graded left module on 3 generators over The exterior algebra of rank 2 over Rational Field
               Defn: g[3, 0] |--> x*g[2, 0]
                     g[3, 1] |--> y*g[2, 0] + x*g[2, 1]
                     g[3, 2] |--> y*g[2, 1] + x*g[2, 2]
                     g[3, 3] |--> y*g[2, 2]]
            sage: all((res[i] * res[i+1]).is_zero() for i in range(len(res)-1))
            True

            sage: e = SymmetricFunctions(QQ).e()
            sage: M = FPModule(e, [0], [[e[2]+e[1,1]], [e[1,1]]])
            sage: res = M.resolution(3, top_dim=10)
            sage: all((res[i] * res[i+1]).is_zero() for i in range(2))
            True
            sage: res[-1].domain().is_trivial()
            True
            sage: M = FPModule(e, [0,2], [[e[2]+e[1,1], 0], [e[2,1], e[1]], [0, e[1,1]]])
            sage: res = M.resolution(3, top_dim=10)
            sage: all((res[i] * res[i+1]).is_zero() for i in range(2))
            True
            sage: res[-1].domain().is_trivial()
            True

            sage: A2 = SteenrodAlgebra(2, profile=(3,2,1))
            sage: M = FPModule(A2, [0,1], [[Sq(2), Sq(1)]])
            sage: M.resolution(0)
            [Module morphism:
               From: Free graded left module on 2 generators over sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [3, 2, 1]
               To:   Finitely presented left module on 2 generators and 1 relation over sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [3, 2, 1]
               Defn: g[0] |--> g[0]
                     g[1] |--> g[1]]
            sage: res = M.resolution(4, verbose=True)
            Computing f_1 (1/4)
            Computing f_2 (2/4)
            Computing using the profile:
            (2, 1)
            Resolving the kernel in the range of dimensions [2, 8]: 2 3 4 5 6 7 8.
            Computing f_3 (3/4)
            Computing using the profile:
            (2, 1)
            Resolving the kernel in the range of dimensions [8, 14]: 8 9 10 11 12 13 14.
            Computing f_4 (4/4)
            Computing using the profile:
            (2, 1)
            Resolving the kernel in the range of dimensions [9, 16]: 9 10 11 12 13 14 15 16.
            sage: len(res)
            5
            sage: res
            [Module morphism:
               From: Free graded left module on 2 generators over sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [3, 2, 1]
               To:   Finitely presented left module on 2 generators and 1 relation over sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [3, 2, 1]
               Defn: g[0] |--> g[0]
                     g[1] |--> g[1],
             Module morphism:
               From: Free graded left module on 1 generator over sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [3, 2, 1]
               To:   Free graded left module on 2 generators over sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [3, 2, 1]
               Defn: g[2] |--> Sq(2)*g[0] + Sq(1)*g[1],
             Module morphism:
               From: Free graded left module on 1 generator over sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [3, 2, 1]
               To:   Free graded left module on 1 generator over sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [3, 2, 1]
               Defn: g[8] |--> Sq(3,1)*g[2],
             Module morphism:
               From: Free graded left module on 2 generators over sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [3, 2, 1]
               To:   Free graded left module on 1 generator over sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [3, 2, 1]
               Defn: g[9] |--> Sq(1)*g[8]
                     g[10] |--> Sq(2)*g[8],
             Module morphism:
               From: Free graded left module on 2 generators over sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [3, 2, 1]
               To:   Free graded left module on 2 generators over sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [3, 2, 1]
               Defn: g[10] |--> Sq(1)*g[9]
                     g[12] |--> Sq(0,1)*g[9] + Sq(2)*g[10]]
            sage: for i in range(len(res)-1):
            ....:     assert (res[i] * res[i+1]).is_zero(), 'the result is not a complex'

        We construct `\\GF{3}` as a `\\ZZ`-module (with trivial grading
        concentrated in degree 0) and compute its resolution::

            sage: E = ExteriorAlgebra(ZZ, 0)
            sage: M = FPModule(E, [0], [[3]])
            sage: res = M.resolution(3)
            sage: res
            [Module morphism:
               From: Free graded left module on 1 generator over The exterior algebra of rank 0 over Integer Ring
               To:   Finitely presented left module on 1 generator and 1 relation over The exterior algebra of rank 0 over Integer Ring
               Defn: g[0] |--> g[0],
             Module endomorphism of Free graded left module on 1 generator over The exterior algebra of rank 0 over Integer Ring
               Defn: g[0] |--> 3*g[0],
             Module morphism:
               From: Free graded left module on 0 generators over The exterior algebra of rank 0 over Integer Ring
               To:   Free graded left module on 1 generator over The exterior algebra of rank 0 over Integer Ring,
             Module endomorphism of Free graded left module on 0 generators over The exterior algebra of rank 0 over Integer Ring]

        TESTS::

            sage: A2 = SteenrodAlgebra(2, profile=(3,2,1))
            sage: M = FPModule(A2, [0,1], [[Sq(2), Sq(1)]])
            sage: res2 = M.resolution(2)
            sage: [type(f) for f in res2]
            [<class '...SteenrodFreeModuleHomspace...'>,
             <class '...SteenrodFreeModuleHomspace...'>,
             <class '...SteenrodFreeModuleHomspace...'>]
        """
