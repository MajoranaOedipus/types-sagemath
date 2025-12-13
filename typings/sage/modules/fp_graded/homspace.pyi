from sage.categories.homset import Homset as Homset

class FPModuleHomspace(Homset):
    def an_element(self, n: int = 0):
        """
        Create a homomorphism belonging to ``self``.

        INPUT:

        - ``n`` -- (default: 0) an integer degree

        OUTPUT: a module homomorphism of degree ``n``

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A = SteenrodAlgebra(2)
            sage: HZ = FPModule(A, [0], relations=[[Sq(1)]])

            sage: Hom(HZ, HZ).an_element(3)
            Module endomorphism of Finitely presented left module on 1 generator and 1 relation over mod 2 Steenrod algebra, milnor basis
              Defn: g[0] |--> Sq(0,1)*g[0]

        TESTS::

            sage: K = FPModule(A, [0, 0], [[Sq(2), 0]]) # Using a zero coefficient in the relations.
            sage: Hom(K, K).an_element(4)
            Module endomorphism of Finitely presented left module on 2 generators and 1 relation over mod 2 Steenrod algebra, milnor basis
              Defn: g[0, 0] |--> 0
                    g[0, 1] |--> Sq(4)*g[0, 0]

            sage: K = FPModule(A, [0, 0], [[Sq(2), 0], [0,0], [Sq(4), Sq(2)*Sq(2)]])
            sage: Hom(K, K).an_element(n=3)
            Module endomorphism of Finitely presented left module on 2 generators and 2 relations over mod 2 Steenrod algebra, milnor basis
              Defn: g[0, 0] |--> 0
                    g[0, 1] |--> Sq(0,1)*g[0, 0]

        An example involving free modules::

            sage: A2 = SteenrodAlgebra(2, profile=(3,2,1))
            sage: F = A2.free_graded_module((1,3))
            sage: L = A2.free_graded_module((1,2))
            sage: H = Hom(F, L)
            sage: H.an_element()
            Module morphism:
              From: Free graded left module on 2 generators over sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [3, 2, 1]
              To:   Free graded left module on 2 generators over sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [3, 2, 1]
              Defn: g[1] |--> g[1]
                    g[3] |--> 0
        """
    def basis_elements(self, n):
        """
        Return a basis for the free module of degree ``n`` morphisms.

        INPUT:

        - ``n`` -- integer degree

        OUTPUT: a basis for the set of all module homomorphisms of degree ``n``

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A = SteenrodAlgebra(2)
            sage: Hko = FPModule(A, [0], relations=[[Sq(2)], [Sq(1)]])

            sage: Hom(Hko, Hko).basis_elements(21)
            [Module endomorphism of Finitely presented left module on 1 generator and 2 relations over mod 2 Steenrod algebra, milnor basis
               Defn: g[0] |--> (Sq(0,0,3)+Sq(0,2,0,1))*g[0],
             Module endomorphism of Finitely presented left module on 1 generator and 2 relations over mod 2 Steenrod algebra, milnor basis
               Defn: g[0] |--> Sq(8,2,1)*g[0]]
        """
    def zero(self):
        """
        Create the trivial homomorphism in ``self``.

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A2 = SteenrodAlgebra(2, profile=(3,2,1))
            sage: F = FPModule(A2, [1,3])
            sage: L = FPModule(A2, [2,3], [[Sq(2),Sq(1)], [0,Sq(2)]])

            sage: z = Hom(F, L).zero()
            sage: z(F.an_element(5))
            0
            sage: z(F.an_element(23))
            0

        Example with free modules::

            sage: A2 = SteenrodAlgebra(2, profile=(3,2,1))
            sage: F = A2.free_graded_module((1,3))
            sage: L = A2.free_graded_module((2,3))
            sage: H = Hom(F, L)
            sage: H.zero()
            Module morphism:
              From: Free graded left module on 2 generators over sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [3, 2, 1]
              To:   Free graded left module on 2 generators over sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [3, 2, 1]
              Defn: g[1] |--> 0
                    g[3] |--> 0
        """
    def identity(self):
        """
        Return the identity homomorphism.

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A2 = SteenrodAlgebra(2, profile=(3,2,1))
            sage: L = FPModule(A2, [2,3], [[Sq(2),Sq(1)], [0,Sq(2)]])

            sage: one = Hom(L, L).identity(); one
            Module endomorphism of Finitely presented left module on 2 generators and 2 relations over sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [3, 2, 1]
              Defn: g[2] |--> g[2]
                    g[3] |--> g[3]

            sage: e = L.an_element(5)
            sage: e == one(e)
            True

        It is an error to call this function when the homset is not a
        set of endomorphisms::

            sage: F = FPModule(A2, [1,3])
            sage: Hom(F,L).identity()
            Traceback (most recent call last):
            ...
            TypeError: this homspace does not consist of endomorphisms

        An example with free graded modules::

            sage: A2 = SteenrodAlgebra(2, profile=(3,2,1))
            sage: L = A2.free_graded_module((2,3))
            sage: H = Hom(L, L)
            sage: H.identity()
            Module endomorphism of Free graded left module on 2 generators
             over sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [3, 2, 1]
              Defn: g[2] |--> g[2]
                    g[3] |--> g[3]

        TESTS::

            sage: A2 = SteenrodAlgebra(2, profile=(3,2,1))
            sage: L = A2.free_graded_module((2,3))
            sage: F = A2.free_graded_module((1,3))
            sage: H = Hom(F, L)
            sage: H.identity()
            Traceback (most recent call last):
            ...
            TypeError: this homspace does not consist of endomorphisms
        """
