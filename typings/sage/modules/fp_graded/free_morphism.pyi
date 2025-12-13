from sage.modules.fp_graded.morphism import FPModuleMorphism as FPModuleMorphism

class FreeGradedModuleMorphism(FPModuleMorphism):
    """
    Create a homomorphism from a finitely generated free graded module
    to a graded module.

    INPUT:

    - ``parent`` -- a homspace in the category of finitely generated free
      modules

    - ``values`` -- list of elements in the codomain; each element
      corresponds (by their ordering) to a module generator in the domain

    EXAMPLES::

        sage: from sage.modules.fp_graded.free_module import FreeGradedModule
        sage: A = SteenrodAlgebra(2)
        sage: F1 = FreeGradedModule(A, (4,5), names='b')
        sage: F2 = FreeGradedModule(A, (3,4), names='c')
        sage: F3 = FreeGradedModule(A, (2,3), names='d')
        sage: H1 = Hom(F1, F2)
        sage: H2 = Hom(F2, F3)
        sage: f = H1((F2((Sq(4), 0)), F2((0, Sq(4)))))
        sage: g = H2((F3((Sq(2), 0)), F3((Sq(3), Sq(2)))))
        sage: g*f
        Module morphism:
          From: Free graded left module on 2 generators over mod 2 Steenrod algebra, milnor basis
          To:   Free graded left module on 2 generators over mod 2 Steenrod algebra, milnor basis
          Defn: b[4] |--> (Sq(0,2)+Sq(3,1)+Sq(6))*d[2]
                b[5] |--> (Sq(1,2)+Sq(7))*d[2] + (Sq(0,2)+Sq(3,1)+Sq(6))*d[3]

    TESTS:

    A non-example because the degree is not well-defined::

        sage: M = FreeGradedModule(A, (0, 0))
        sage: N = FreeGradedModule(A, (0,))
        sage: H = Hom(M, N)
        sage: g = N.generator(0)
        sage: H([Sq(1)*g, Sq(2)*g])
        Traceback (most recent call last):
        ...
        ValueError: ill-defined homomorphism: degrees do not match
    """
    def __init__(self, parent, values) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: from sage.modules.fp_graded.free_module import FreeGradedModule
            sage: A = SteenrodAlgebra(2)
            sage: M = FreeGradedModule(A, (0, 0))
            sage: N = FreeGradedModule(A, (0,))
            sage: H = Hom(M, N)
            sage: g = N.generator(0)
            sage: TestSuite(H).run()
            sage: TestSuite(g).run()
        """
    def degree(self):
        """
        The degree of ``self``.

        OUTPUT:

        The degree of this homomorphism. Raise an error if this is
        the trivial homomorphism.

        EXAMPLES::

            sage: from sage.modules.fp_graded.free_module import FreeGradedModule
            sage: A = SteenrodAlgebra(2)
            sage: homspace = Hom(FreeGradedModule(A, (0,1)), FreeGradedModule(A, (0,)))
            sage: N = homspace.codomain()
            sage: values = [Sq(5)*N.generator(0), Sq(3,1)*N.generator(0)]
            sage: f = homspace(values)
            sage: f.degree()
            5

        The zero homomorphism has no degree::

            sage: homspace.zero().degree()
            Traceback (most recent call last):
            ...
            ValueError: the zero morphism does not have a well-defined degree
        """
    def __call__(self, x):
        """
        Evaluate the homomorphism at the given domain element ``x``.

        INPUT:

        - ``x`` -- an element of the domain of this morphism

        OUTPUT:

        The module element of the codomain which is the value of ``x``
        under this homomorphism.

        EXAMPLES::

            sage: from sage.modules.fp_graded.free_module import FreeGradedModule
            sage: A = SteenrodAlgebra(2)
            sage: M = FreeGradedModule(A, (0,1))
            sage: N = FreeGradedModule(A, (2,))
            sage: values = [Sq(5)*N.generator(0), Sq(3,1)*N.generator(0)]
            sage: f = Hom(M, N)(values)
            sage: f.__call__(M.generator(0))
            Sq(5)*g[2]
            sage: f.__call__(M.generator(1))
            Sq(3,1)*g[2]
        """
    def fp_module(self):
        """
        Create a finitely presented module from ``self``.

        OUTPUT: the finitely presented module with presentation equal to ``self``

        EXAMPLES::

            sage: A = SteenrodAlgebra(2)
            sage: F1 = A.free_graded_module([2])
            sage: F2 = A.free_graded_module([0])
            sage: v = F2([Sq(2)])
            sage: pres = Hom(F1, F2)([v])
            sage: M = pres.fp_module(); M
            Finitely presented left module on 1 generator and 1 relation over
             mod 2 Steenrod algebra, milnor basis
            sage: M.generator_degrees()
            (0,)
            sage: M.relations()
            (Sq(2)*g[0],)

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A = SteenrodAlgebra(2)
            sage: F1 = A.free_graded_module((2,))
            sage: F2 = FPModule(A, (0,), [[Sq(4)]])
            sage: v = F2([Sq(2)])
            sage: pres = Hom(F1, F2)([v])
            sage: pres.fp_module()
            Traceback (most recent call last):
            ...
            ValueError: this is not a morphism between free modules
        """
