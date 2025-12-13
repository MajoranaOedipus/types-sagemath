from sage.categories.super_modules import SuperModulesCategory as SuperModulesCategory

class SuperModulesWithBasis(SuperModulesCategory):
    """
    The category of super modules with a distinguished basis.

    An `R`-*super module with a distinguished basis* is an
    `R`-super module equipped with an `R`-module basis whose elements are
    homogeneous.

    EXAMPLES::

        sage: C = GradedModulesWithBasis(QQ); C
        Category of graded vector spaces with basis over Rational Field
        sage: sorted(C.super_categories(), key=str)
        [Category of filtered vector spaces with basis over Rational Field,
         Category of graded modules with basis over Rational Field,
         Category of graded vector spaces over Rational Field]
        sage: C is ModulesWithBasis(QQ).Graded()
        True

    TESTS::

        sage: TestSuite(C).run()
    """
    class ParentMethods: ...
    class ElementMethods:
        def is_super_homogeneous(self):
            """
            Return whether this element is homogeneous, in the sense
            of a super module (i.e., is even or odd).

            EXAMPLES::

                sage: # needs sage.modules
                sage: Q = QuadraticForm(QQ, 2, [1,2,3])
                sage: C.<x,y> = CliffordAlgebra(Q)
                sage: a = x + y
                sage: a.is_super_homogeneous()
                True
                sage: a = x*y + 4
                sage: a.is_super_homogeneous()
                True
                sage: a = x*y + x - 3*y + 4
                sage: a.is_super_homogeneous()
                False

            The exterior algebra has a `\\ZZ` grading, which induces the
            `\\ZZ / 2\\ZZ` grading. However the definition of homogeneous
            elements differs because of the different gradings::

                sage: # needs sage.combinat sage.modules
                sage: E.<x,y> = ExteriorAlgebra(QQ)
                sage: a = x*y + 4
                sage: a.is_super_homogeneous()
                True
                sage: a.is_homogeneous()
                False
            """
        def is_even_odd(self):
            """
            Return ``0`` if ``self`` is an even element and ``1`` if
            ``self`` is an odd element.

            EXAMPLES::

                sage: # needs sage.modules
                sage: Q = QuadraticForm(QQ, 2, [1,2,3])
                sage: C.<x,y> = CliffordAlgebra(Q)
                sage: a = x + y
                sage: a.is_even_odd()
                1
                sage: a = x*y + 4
                sage: a.is_even_odd()
                0
                sage: a = x + 4
                sage: a.is_even_odd()
                Traceback (most recent call last):
                ...
                ValueError: element is not homogeneous

                sage: E.<x,y> = ExteriorAlgebra(QQ)                                     # needs sage.modules
                sage: (x*y).is_even_odd()                                               # needs sage.modules
                0
            """
        def even_component(self):
            """
            Return the even component of ``self``.

            EXAMPLES::

                sage: # needs sage.modules
                sage: Q = QuadraticForm(QQ, 2, [1,2,3])
                sage: C.<x,y> = CliffordAlgebra(Q)
                sage: a = x*y + x - 3*y + 4
                sage: a.even_component()
                x*y + 4

            TESTS:

            Check that this really return ``A.zero()`` and not a plain ``0``::

                sage: a = x + y                                                         # needs sage.modules
                sage: a.even_component().parent() is C                                  # needs sage.modules
                True
            """
        def odd_component(self):
            """
            Return the odd component of ``self``.

            EXAMPLES::

                sage: # needs sage.modules
                sage: Q = QuadraticForm(QQ, 2, [1,2,3])
                sage: C.<x,y> = CliffordAlgebra(Q)
                sage: a = x*y + x - 3*y + 4
                sage: a.odd_component()
                x - 3*y

            TESTS:

            Check that this really return ``A.zero()`` and not a plain ``0``::

                sage: a = x*y                                                           # needs sage.modules
                sage: a.odd_component().parent() is C                                   # needs sage.modules
                True
            """
