from .profile import enveloping_profile_elements as enveloping_profile_elements
from sage.algebras.steenrod.steenrod_algebra import SteenrodAlgebra_generic as SteenrodAlgebra_generic
from sage.categories.homset import Hom as Hom
from sage.modules.fp_graded.free_morphism import FreeGradedModuleMorphism as FreeGradedModuleMorphism
from sage.modules.fp_graded.morphism import FPModuleMorphism as FPModuleMorphism

class SteenrodFPModuleMorphism(FPModuleMorphism):
    def profile(self):
        '''
        Return a finite profile over which ``self`` can be defined.

        This is in some ways the key method for these morphisms. As
        discussed in the "Theoretical background" section of
        :mod:`sage.modules.fp_graded.steenrod.module`, any
        homomorphism of finitely presented modules over the Steenrod
        algebra can be defined over a finite-dimensional sub-Hopf
        algebra, and this method identifies such a sub-Hopf algebra
        and returns its profile function.

        EXAMPLES::

            sage: from sage.modules.fp_graded.steenrod.module import SteenrodFPModule
            sage: A = SteenrodAlgebra(2)
            sage: M = SteenrodFPModule(A, [0,1], [[Sq(2),Sq(1)], [0,Sq(2)]])
            sage: one = Hom(M,M).identity()
            sage: one.profile()
            (2, 1)
            sage: zero = Hom(M,M).zero()
            sage: zero.profile()
            (2, 1)
            sage: A_fin = SteenrodAlgebra(2, profile=(2,1))
            sage: M_fin = M.change_ring(A_fin)

        Change the ring of the module ``M``::

            sage: M_fin.change_ring(A) is M
            True

        We can change rings to the finite sub-Hopf algebra defined by
        the profile we just computed::

            sage: one_fin = one.change_ring(A_fin)
            sage: one_fin.domain()
            Finitely presented left module on 2 generators and 2 relations over
             sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [2, 1]

        If we change back to the full Steenrod algebra, we are back where
        we started::

            sage: one_fin.change_ring(A) == one
            True
        '''
    def is_injective(self, top_dim=None, verbose: bool = False) -> bool:
        """
        Return ``True`` if ``self`` is injective.

        INPUT:

        - ``top_dim`` -- (optional) stop the computation at this degree; if
          not specified, this is determined using :meth:`profile`
        - ``verbose`` -- boolean (default: ``False``); whether log messages are
          printed

        EXAMPLES::

            sage: from sage.modules.fp_graded.steenrod.module import SteenrodFPModule
            sage: A = SteenrodAlgebra(2)
            sage: M = SteenrodFPModule(A, [0,1], [[Sq(2),Sq(1)], [0,Sq(2)]])
            sage: S = SteenrodFPModule(A, [0], [[Sq(2)]])
            sage: f = Hom(S, M)([M([0,1])])
            sage: f.is_injective()
            True
            sage: g = Hom(S, M).zero()
            sage: g.is_injective()
            False
            sage: z = Hom(SteenrodFPModule(A, []), M).zero()
            sage: z.is_injective()
            True
            sage: z.is_zero()
            True
        """
    def kernel_inclusion(self, top_dim=None, verbose: bool = False):
        """
        Return the kernel of ``self`` as a morphism.

        INPUT:

        - ``top_dim`` -- (optional) stop the computation at this degree; if
          not specified, this is determined using :meth:`profile`
        - ``verbose`` -- boolean (default: ``False``); whether log messages are
          printed

        OUTPUT: an injective homomorphism into the domain ``self`` which is
        onto the kernel of this homomorphism.

        EXAMPLES::

            sage: from sage.modules.fp_graded.steenrod.module import SteenrodFPModule
            sage: A = SteenrodAlgebra(2)
            sage: M = SteenrodFPModule(A, [0,1], [[Sq(2),Sq(1)], [0,Sq(2)]])
            sage: S = SteenrodFPModule(A, [0], [[Sq(2)]])
            sage: f = Hom(S, M)([M([0,1])])
            sage: f.is_injective()
            True
            sage: k = f.kernel_inclusion()
            sage: k == 0
            True

        Since k is both trivial and injective, its domain should
        be the zero module::

            sage: k.domain().is_trivial()
            True

            sage: g = Hom(S, M)([M([Sq(3),Sq(2)])])
            sage: h = g.kernel_inclusion()
            sage: h.is_identity()
            True
            sage: ker = h.domain();
            sage: ker is S
            True

        So `g` had to be trivial::

            sage: g.is_zero()
            True
        """
    def cokernel_projection(self, verbose: bool = False):
        """
        Compute the map to the cokernel of ``self``.

        INPUT:

        - ``verbose`` -- boolean (default: ``False``); whether log messages are
          printed

        OUTPUT:

        The natural projection from the codomain of this homomorphism
        to its cokernel.

        EXAMPLES::

            sage: from sage.modules.fp_graded.steenrod.module import SteenrodFPModule
            sage: A1 = SteenrodAlgebra(2, profile=(2,1))
            sage: M = SteenrodFPModule(A1, [0], [[Sq(2)]])
            sage: F = SteenrodFPModule(A1, [0])

            sage: r = Hom(F, M)([A1.Sq(1)*M.generator(0)])
            sage: co = r.cokernel_projection(); co
            Module morphism:
              From: Finitely presented left module on 1 generator and 1 relation over sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [2, 1]
              To:   Finitely presented left module on 1 generator and 2 relations over sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [2, 1]
              Defn: g[0] |--> g[0]

            sage: co.domain().is_trivial()
            False
        """
    def image(self, top_dim=None, verbose: bool = False):
        """
        Return the image of ``self``.

        INPUT:

        - ``top_dim`` -- integer (optional); used by this function to stop the
          computation at the given degree
        - ``verbose`` -- boolean (default: ``False``); whether log messages are
          printed

        OUTPUT:

        An injective homomorphism into the codomain of ``self`` which is
        onto the image of ``self``.

        EXAMPLES::

            sage: from sage.modules.fp_graded.steenrod.module import SteenrodFPModule
            sage: A = SteenrodAlgebra(2)
            sage: M = SteenrodFPModule(A, [0,1], [[Sq(2),Sq(1)], [0,Sq(2)]])
            sage: S = SteenrodFPModule(A, [0], [[Sq(2)]])
            sage: f = Hom(S, M)([M([0,1])])
            sage: f.is_injective()
            True
            sage: i = f.image(); i
            Module morphism:
              From: Finitely presented left module on 1 generator and 1 relation over mod 2 Steenrod algebra, milnor basis
              To:   Finitely presented left module on 2 generators and 2 relations over mod 2 Steenrod algebra, milnor basis
              Defn: g[1] |--> g[1]
            sage: i.codomain() is M
            True

        Lift the map ``f`` over the inclusion ``i``::

            sage: f_ = f.lift(i)
            sage: f_.is_injective()
            True
            sage: f_.is_surjective()
            True

            sage: g = Hom(S, M)([M([Sq(3),Sq(2)])])
            sage: j = g.image(); j
            Module morphism:
              From: Free graded left module on 0 generators over mod 2 Steenrod algebra, milnor basis
              To:   Finitely presented left module on 2 generators and 2 relations over mod 2 Steenrod algebra, milnor basis

        So ``g`` had to be trivial::

            sage: g.is_zero()
            True
        """

class SteenrodFreeModuleMorphism(FreeGradedModuleMorphism, SteenrodFPModuleMorphism): ...
