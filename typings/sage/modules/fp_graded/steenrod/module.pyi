from .profile import enveloping_profile_elements as enveloping_profile_elements
from sage.algebras.steenrod.steenrod_algebra import SteenrodAlgebra_generic as SteenrodAlgebra_generic
from sage.modules.fp_graded.free_module import FreeGradedModule as FreeGradedModule
from sage.modules.fp_graded.module import FPModule as FPModule
from sage.rings.infinity import infinity as infinity

class SteenrodModuleMixin:
    """
    Mixin class for common methods of the Steenrod algebra modules.
    """
    def profile(self):
        """
        Return a finite profile over which ``self`` can be defined.

        Any finitely presented module over the Steenrod algebra can be
        defined over a finite-dimensional sub-Hopf algebra, and this
        method identifies such a sub-Hopf algebra and returns its
        profile function.

        .. NOTE::

            The profile produced by this function is reasonably small
            but is not guaranteed to be minimal.

        EXAMPLES::

            sage: from sage.modules.fp_graded.steenrod.module import SteenrodFPModule
            sage: A = SteenrodAlgebra(2)
            sage: M = SteenrodFPModule(A, [0,1], [[Sq(2),Sq(1)],[0,Sq(2)],[Sq(3),0]])
            sage: M.profile()
            (2, 1)

        TESTS::

            sage: from sage.modules.fp_graded.steenrod.module import SteenrodFPModule
            sage: A = SteenrodAlgebra(2)
            sage: X = SteenrodFPModule(A, [0])
            sage: X.profile()
            (0,)
        """
    def export_module_definition(self, powers_of_two_only: bool = True):
        """
        Return the module to the input
        `format used by R. Bruner's Ext software
        <http://www.math.wayne.edu/~rrb/cohom/modfmt.html>`_ as a string.

        INPUT:

        - ``powers_of_two_only`` -- boolean (default: ``True``); if the
          output should contain the action of all Steenrod squaring operations
          (restricted by the profile), or only the action of the operations
          of degree equal to a power of two

        EXAMPLES::

            sage: from sage.modules.fp_graded.steenrod.module import SteenrodFPModule
            sage: A1 = algebra=SteenrodAlgebra(p=2, profile=[2,1])
            sage: M = SteenrodFPModule(A1, [0])
            sage: print(M.export_module_definition())
            8 0 1 2 3 3 4 5 6
            0 1 1 1
            2 1 1 4
            3 1 1 5
            6 1 1 7
            0 2 1 2
            1 2 2 3 4
            2 2 1 5
            3 2 1 6
            4 2 1 6
            5 2 1 7
            sage: N = SteenrodFPModule(A1, [0], [[Sq(1)]])
            sage: print(N.export_module_definition())
            4 0 2 3 5
            1 1 1 2
            0 2 1 1
            2 2 1 3
            sage: print(N.export_module_definition(powers_of_two_only=False))
            4 0 2 3 5
            1 1 1 2
            0 2 1 1
            2 2 1 3
            0 3 1 2
            sage: A2 = SteenrodAlgebra(p=2, profile=[3,2,1])
            sage: Hko = SteenrodFPModule(A2, [0], [[Sq(1)], [Sq(2)]])
            sage: print(Hko.export_module_definition())
            8 0 4 6 7 10 11 13 17
            2 1 1 3
            4 1 1 5
            1 2 1 2
            5 2 1 6
            0 4 1 1
            2 4 1 4
            3 4 1 5
            6 4 1 7

        TESTS::

            sage: A = SteenrodAlgebra()
            sage: M = A.free_graded_module([])
            sage: M.export_module_definition()
            Traceback (most recent call last):
            ...
            ValueError: this module is not defined over a finite algebra
            sage: A1 = SteenrodAlgebra(profile=[2,1])
            sage: M1 = A1.free_graded_module([])
            sage: s = M1.export_module_definition()
            The module connectivity is infinite, so there is nothing to export.
            sage: s
            ''
            sage: P1 = SteenrodAlgebra(p=5, profile=[[], [2,1]])
            sage: N = P1.free_graded_module([])
            sage: N.export_module_definition()
            Traceback (most recent call last):
            ...
            ValueError: this function is not implemented for odd primes
        """

class SteenrodFPModule(FPModule, SteenrodModuleMixin):
    """
    Create a finitely presented module over the Steenrod algebra.

    .. SEEALSO::

        The thematic tutorial on `Steenrod algebra modules
        <../../../../../../thematic_tutorials/steenrod_algebra_modules.html>`_.

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

    TESTS::

        sage: from sage.modules.fp_graded.steenrod.module import SteenrodFPModule
        sage: SteenrodFPModule(SteenrodAlgebra(2), (0,))
        Free graded left module on 1 generator over mod 2 Steenrod algebra, milnor basis
    """
    def resolution(self, k, top_dim=None, verbose: bool = False):
        """
        A free resolution of ``self`` of the given length.

        INPUT:

        - ``k`` -- nonnegative integer
        - ``top_dim`` -- (optional) stop the computation at this degree
        - ``verbose`` -- boolean (default: ``False``); whether log messages are
          printed

        OUTPUT: list of homomorphisms `[\\epsilon, f_1, \\ldots, f_k]` such that

        .. MATH::

            \\begin{gathered}
            f_i: F_i \\to F_{i-1} \\text{ for } 1\\leq i\\leq k, \\\\\n            \\epsilon: F_0\\to M,
            \\end{gathered}

        where each `F_i` is a finitely generated free module, and the
        sequence

        .. MATH::

            F_k \\xrightarrow{f_k} F_{k-1} \\xrightarrow{f_{k-1}} \\ldots
            \\rightarrow F_0 \\xrightarrow{\\epsilon} M \\rightarrow 0

        is exact. Note that the 0th element in this list is the map
        `\\epsilon`, and the rest of the maps are between free
        modules.

        EXAMPLES::

            sage: from sage.modules.fp_graded.steenrod.module import SteenrodFPModule
            sage: A = SteenrodAlgebra(2)
            sage: Hko = SteenrodFPModule(A, [0], [[Sq(1)], [Sq(2)]])

            sage: res = Hko.resolution(5, verbose=True)
            Computing f_1 (1/5)
            Computing f_2 (2/5)
            Computing using the profile:
            (2, 1)
            Resolving the kernel in the range of dimensions [1, 8]: 1 2 3 4 5 6 7 8.
            Computing f_3 (3/5)
            Computing using the profile:
            (2, 1)
            Resolving the kernel in the range of dimensions [2, 10]: 2 3 4 5 6 7 8 9 10.
            Computing f_4 (4/5)
            Computing using the profile:
            (2, 1)
            Resolving the kernel in the range of dimensions [3, 13]: 3 4 5 6 7 8 9 10 11 12 13.
            Computing f_5 (5/5)
            Computing using the profile:
            (2, 1)
            Resolving the kernel in the range of dimensions [4, 18]: 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18.
            sage: [x.domain() for x in res]
            [Free graded left module on 1 generator over mod 2 Steenrod algebra, milnor basis,
             Free graded left module on 2 generators over mod 2 Steenrod algebra, milnor basis,
             Free graded left module on 2 generators over mod 2 Steenrod algebra, milnor basis,
             Free graded left module on 2 generators over mod 2 Steenrod algebra, milnor basis,
             Free graded left module on 3 generators over mod 2 Steenrod algebra, milnor basis,
             Free graded left module on 4 generators over mod 2 Steenrod algebra, milnor basis]

        When there are no relations, the resolution is trivial::

            sage: M = SteenrodFPModule(A, [0])
            sage: M.resolution(4)
            [Module endomorphism of Free graded left module on 1 generator over mod 2 Steenrod algebra, milnor basis
               Defn: g[0] |--> g[0],
             Module morphism:
               From: Free graded left module on 0 generators over mod 2 Steenrod algebra, milnor basis
               To:   Free graded left module on 1 generator over mod 2 Steenrod algebra, milnor basis,
             Module endomorphism of Free graded left module on 0 generators over mod 2 Steenrod algebra, milnor basis,
             Module endomorphism of Free graded left module on 0 generators over mod 2 Steenrod algebra, milnor basis,
             Module endomorphism of Free graded left module on 0 generators over mod 2 Steenrod algebra, milnor basis]
        """

class SteenrodFreeModule(FreeGradedModule, SteenrodModuleMixin): ...
