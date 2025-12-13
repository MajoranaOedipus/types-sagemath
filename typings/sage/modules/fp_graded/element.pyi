from sage.misc.cachefunc import cached_method as cached_method
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement as IndexedFreeModuleElement

class FPElement(IndexedFreeModuleElement):
    """
    A module element of a finitely presented graded module over
    a connected graded algebra.

    TESTS::

        sage: from sage.modules.fp_graded.module import FPModule
        sage: FPModule(SteenrodAlgebra(2), [0])([Sq(2)])
        Sq(2)*g[0]
    """
    def lift_to_free(self):
        """
        Return the lift of ``self`` to the free module ``F``,
        where ``self`` is in a quotient of ``F``.

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: M = FPModule(SteenrodAlgebra(2), [0,1], [[Sq(4), Sq(3)]])
            sage: x = M([Sq(1), 1])
            sage: x
            Sq(1)*g[0] + g[1]
            sage: x.parent()
            Finitely presented left module on 2 generators and 1 relation over mod 2 Steenrod algebra, milnor basis
            sage: x.lift_to_free()
            Sq(1)*g[0] + g[1]
            sage: x.lift_to_free().parent()
            Free graded left module on 2 generators over mod 2 Steenrod algebra, milnor basis
        """
    @cached_method
    def degree(self):
        """
        The degree of ``self``.

        OUTPUT: the integer degree of ``self`` or raise an error if the zero element

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: M = FPModule(SteenrodAlgebra(2), [0,1], [[Sq(4), Sq(3)]])
            sage: x = M.an_element(7)

            sage: x
            Sq(0,0,1)*g[0] + Sq(3,1)*g[1]
            sage: x.degree()
            7

        The zero element has no degree::

            sage: (x-x).degree()
            Traceback (most recent call last):
            ...
            ValueError: the zero element does not have a well-defined degree

        TESTS::

            sage: N = FPModule(SteenrodAlgebra(2), [0], [[Sq(2)]])
            sage: y = Sq(2)*N.generator(0)
            sage: y == 0
            True
            sage: y.degree()
            Traceback (most recent call last):
            ...
            ValueError: the zero element does not have a well-defined degree

        Testing that the order of the coefficients agrees with the
        order of the generators::

            sage: F.<x,y> = FPModule(SteenrodAlgebra(), (2, 0))
            sage: x.degree()
            2
            sage: y.degree()
            0
        """
    def dense_coefficient_list(self, order=None):
        """
        Return a list of all coefficients of ``self``.

        INPUT:

        - ``order`` -- (optional) an ordering of the basis indexing set

        Note that this includes *all* of the coefficients, not just
        the nonzero ones. By default they appear in the same order as
        the module generators.

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A = SteenrodAlgebra()
            sage: M = FPModule(SteenrodAlgebra(2), [0,1], [[Sq(4), Sq(3)]])
            sage: x = M([Sq(1), 1])
            sage: x.dense_coefficient_list()
            [Sq(1), 1]
            sage: y = Sq(2) * M.generator(1)
            sage: y.dense_coefficient_list()
            [0, Sq(2)]
        """
    def vector_presentation(self):
        """
        A coordinate vector representing ``self`` when it is nonzero.

        These are coordinates with respect to the basis chosen by
        :meth:`~sage.modules.fp_graded.module.FPModule.basis_elements`.
        When the element is zero, it has no well defined degree, and this
        function returns ``None``.

        OUTPUT:

        A vector of elements in the ground ring of the algebra for
        this module when this element is nonzero.  Otherwise, the
        value ``None``.

        .. SEEALSO::

            * :meth:`sage.modules.fp_graded.module.FPModule.vector_presentation`
            * :meth:`sage.modules.fp_graded.module.FPModule.basis_elements`
            * :meth:`sage.modules.fp_graded.module.FPModule.element_from_coordinates`

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: A2 = SteenrodAlgebra(2, profile=(3,2,1))
            sage: M.<m0,m1> = FPModule(A2, (0,1))

            sage: x = M.an_element(7)
            sage: v = x.vector_presentation(); v
            (1, 0, 0, 0, 0, 1, 0)
            sage: type(v)
            <class 'sage.modules.vector_mod2_dense.Vector_mod2_dense'>

            sage: V = M.vector_presentation(7)
            sage: v in V
            True

            sage: M.element_from_coordinates(v, 7) == x
            True

        We can use the basis for the module elements in the degree of `x`,
        together with the coefficients `v` to recreate the element `x`::

            sage: basis = M.basis_elements(7)
            sage: x_ = sum( [c*b for (c,b) in zip(v, basis)] ); x_
            Sq(0,0,1)*m0 + Sq(3,1)*m1
            sage: x__ = M.linear_combination(zip(basis, v)); x__
            Sq(0,0,1)*m0 + Sq(3,1)*m1
            sage: x == x_ == x__
            True

        TESTS::

            sage: M.zero().vector_presentation() is None
            True
        """
    def __bool__(self) -> bool:
        """
        Determine if this element is nonzero.

        OUTPUT:

        The boolean value ``True`` if this element is nonzero
        and ``False`` otherwise.

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: M = FPModule(SteenrodAlgebra(2), [0,2,4], [[Sq(4),Sq(2),0]])
            sage: M(0) != 0
            False
            sage: M((Sq(6), 0, Sq(2))) == 0
            False
            sage: a = M((Sq(1)*Sq(2)*Sq(1)*Sq(4), 0, 0))
            sage: b = M((0, Sq(2)*Sq(2)*Sq(2), 0))
            sage: a != 0
            True
            sage: bool(b)
            True
            sage: bool(a + b)
            False
        """
    def __eq__(self, other):
        """
        ``True`` iff ``self`` and ``other`` are equal.

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: M = FPModule(SteenrodAlgebra(2), [0,1], [[Sq(4), Sq(3)]])
            sage: x = M([Sq(1), 1])
            sage: x
            Sq(1)*g[0] + g[1]
            sage: x == x
            True
            sage: x == M.zero()
            False
            sage: x-x == M.zero()
            True
            sage: x != x
            False

        Comparing elements in different modules::

            sage: x = Sq(2) * M.generator(0)
            sage: N = FPModule(SteenrodAlgebra(2), [0], [[Sq(2)]])
            sage: y = Sq(2) * N.generator(0)
            sage: x == y
            False
            sage: x != y
            True
        """
    def normalize(self):
        """
        A normalized form of ``self``.

        OUTPUT:

        An instance representing the same module element as ``self`` in
        normalized form.

        EXAMPLES::

            sage: from sage.modules.fp_graded.module import FPModule
            sage: M.<a0,b2,c4> = FPModule(SteenrodAlgebra(2), [0,2,4], [[Sq(4),Sq(2),0]])

            sage: m = M((Sq(6), 0, Sq(2))); m
            Sq(6)*a0 + Sq(2)*c4
            sage: m.normalize()
            Sq(6)*a0 + Sq(2)*c4
            sage: m == m.normalize()
            True

            sage: n = M((Sq(4), Sq(2), 0)); n
            Sq(4)*a0 + Sq(2)*b2
            sage: n.normalize()
            0
            sage: n == n.normalize()
            True
        """
