from sage.categories.homset import Hom as Hom
from sage.categories.modules_with_basis import ModulesWithBasis as ModulesWithBasis
from sage.categories.tensor import tensor as tensor
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.sets.family import Family as Family

class SteenrodAlgebra_generic(CombinatorialFreeModule):
    """
    The mod `p` Steenrod algebra.

    Users should not call this, but use the function
    :func:`SteenrodAlgebra` instead. See that function for
    extensive documentation.

    EXAMPLES::

        sage: sage.algebras.steenrod.steenrod_algebra.SteenrodAlgebra_generic()
        mod 2 Steenrod algebra, milnor basis
        sage: sage.algebras.steenrod.steenrod_algebra.SteenrodAlgebra_generic(5)
        mod 5 Steenrod algebra, milnor basis
        sage: sage.algebras.steenrod.steenrod_algebra.SteenrodAlgebra_generic(5, 'adem')
        mod 5 Steenrod algebra, serre-cartan basis
    """
    @staticmethod
    def __classcall__(self, p: int = 2, basis: str = 'milnor', **kwds):
        """
        This normalizes the basis name and the profile, to make unique
        representation work properly.

        EXAMPLES::

            sage: SteenrodAlgebra(basis='adem') is SteenrodAlgebra(basis='serre-cartan')
            True
            sage: SteenrodAlgebra(profile=[3,2,1,0]) is SteenrodAlgebra(profile=lambda n: max(4-n,0), truncation_type=0)
            True
            sage: SteenrodAlgebra(p=5) is SteenrodAlgebra(p=5, generic=True)
            True
        """
    def __init__(self, p: int = 2, basis: str = 'milnor', **kwds) -> None:
        """
        INPUT:

        - ``p`` -- positive prime integer (default: 2)
        - ``basis`` -- string (default: ``'milnor'``)
        - ``profile`` -- profile function (default: ``None``)
        - ``truncation_type`` -- (default: ``'auto'``)
        - ``precision`` -- (default: ``None``)
        - ``generic`` -- (default: ``'auto'``)

        OUTPUT:

        mod `p` Steenrod algebra with basis, or a sub-Hopf
        algebra of the mod `p` Steenrod algebra defined by the given
        profile function.

        See :func:`SteenrodAlgebra` for full documentation.

        EXAMPLES::

            sage: SteenrodAlgebra()   # 2 is the default prime
            mod 2 Steenrod algebra, milnor basis
            sage: SteenrodAlgebra(5)
            mod 5 Steenrod algebra, milnor basis
            sage: SteenrodAlgebra(2, 'milnor').Sq(0,1)
            Sq(0,1)
            sage: SteenrodAlgebra(2, 'adem').Sq(0,1)
            Sq^2 Sq^1 + Sq^3

        TESTS::

            sage: TestSuite(SteenrodAlgebra()).run()
            sage: TestSuite(SteenrodAlgebra(profile=[4,3,2,2,1])).run()
            sage: TestSuite(SteenrodAlgebra(basis='adem')).run()
            sage: TestSuite(SteenrodAlgebra(basis='wall')).run()
            sage: TestSuite(SteenrodAlgebra(basis='arnonc')).run()  # long time
            sage: TestSuite(SteenrodAlgebra(basis='woody')).run()   # long time
            sage: A3 = SteenrodAlgebra(3)
            sage: A3.category()
            Category of supercocommutative super Hopf algebras
             with basis over Finite Field of size 3
            sage: TestSuite(A3).run()  # long time
            sage: TestSuite(SteenrodAlgebra(basis='adem', p=3)).run()
            sage: TestSuite(SteenrodAlgebra(basis='pst_llex', p=7)).run()  # long time
            sage: TestSuite(SteenrodAlgebra(basis='comm_deg', p=5)).run()  # long time
            sage: TestSuite(SteenrodAlgebra(p=2, generic=True)).run()      # long time

        Two Steenrod algebras are equal iff their associated primes,
        bases, and profile functions (if present) are equal.  Because
        this class inherits from :class:`UniqueRepresentation`, this
        means that they are equal if and only they are identical: ``A
        == B`` is True if and only if ``A is B`` is ``True``::

            sage: A = SteenrodAlgebra(2)
            sage: B = SteenrodAlgebra(2, 'adem')
            sage: A == B
            False
            sage: C = SteenrodAlgebra(17)
            sage: A == C
            False

            sage: A1 = SteenrodAlgebra(2, profile=[2,1])
            sage: A1 == A
            False
            sage: A1 == SteenrodAlgebra(2, profile=[2,1,0])
            True
            sage: A1 == SteenrodAlgebra(2, profile=[2,1], basis='pst')
            False
        """
    def prime(self):
        """
        The prime associated to ``self``.

        EXAMPLES::

            sage: SteenrodAlgebra(p=2, profile=[1,1]).prime()
            2
            sage: SteenrodAlgebra(p=7).prime()
            7
        """
    def basis_name(self) -> str:
        """
        The basis name associated to ``self``.

        EXAMPLES::

            sage: SteenrodAlgebra(p=2, profile=[1,1]).basis_name()
            'milnor'
            sage: SteenrodAlgebra(basis='serre-cartan').basis_name()
            'serre-cartan'
            sage: SteenrodAlgebra(basis='adem').basis_name()
            'serre-cartan'
        """
    def profile(self, i, component: int = 0):
        """
        Profile function for this algebra.

        INPUT:

        - ``i`` -- integer
        - ``component`` -- either 0 or 1 (default: 0)

        OUTPUT: integer or `\\infty`

        See the documentation for
        :mod:`sage.algebras.steenrod.steenrod_algebra` and
        :func:`SteenrodAlgebra` for information on profile functions.

        This applies the profile function to the integer `i`.  Thus
        when `p=2`, `i` must be a positive integer.  When `p` is odd,
        there are two profile functions, `e` and `k` (in the notation
        of the aforementioned documentation), corresponding,
        respectively to ``component=0`` and ``component=1``.  So when
        `p` is odd and ``component`` is 0, `i` must be positive, while
        when ``component`` is 1, `i` must be nonnegative.

        EXAMPLES::

            sage: SteenrodAlgebra().profile(3)
            +Infinity
            sage: SteenrodAlgebra(profile=[3,2,1]).profile(1)
            3
            sage: SteenrodAlgebra(profile=[3,2,1]).profile(2)
            2

        When the profile is specified by a list, the default behavior
        is to return zero values outside the range of the list.  This
        can be overridden if the algebra is created with an infinite
        ``truncation_type``::

            sage: SteenrodAlgebra(profile=[3,2,1]).profile(9)
            0
            sage: SteenrodAlgebra(profile=[3,2,1], truncation_type=Infinity).profile(9)
            +Infinity

            sage: B = SteenrodAlgebra(p=3, profile=(lambda n: n, lambda n: 1))
            sage: B.profile(3)
            3
            sage: B.profile(3, component=1)
            1

            sage: EA = SteenrodAlgebra(generic=True, profile=(lambda n: n, lambda n: 1))
            sage: EA.profile(4)
            4
            sage: EA.profile(2, component=1)
            1
        """
    def homogeneous_component(self, n):
        """
        Return the `n`-th homogeneous piece of the Steenrod algebra.

        INPUT:

        - ``n`` -- integer

        OUTPUT: a vector space spanned by the basis for this algebra in dimension `n`

        EXAMPLES::

            sage: A = SteenrodAlgebra()
            sage: A.homogeneous_component(4)
            Vector space spanned by (Sq(1,1), Sq(4)) over Finite Field of size 2
            sage: SteenrodAlgebra(profile=[2,1,0]).homogeneous_component(4)
            Vector space spanned by (Sq(1,1),) over Finite Field of size 2

        The notation A[n] may also be used::

            sage: A[5]
            Vector space spanned by (Sq(2,1), Sq(5)) over Finite Field of size 2
            sage: SteenrodAlgebra(basis='wall')[4]
            Vector space spanned by (Q^1_0 Q^0_0, Q^2_2) over Finite Field of size 2
            sage: SteenrodAlgebra(p=5)[17]
            Vector space spanned by (Q_1 P(1), Q_0 P(2)) over Finite Field of size 5

        Note that A[n] is just a vector space, not a Hopf algebra, so
        its elements don't have products, coproducts, or antipodes
        defined on them.  If you want to use operations like this on
        elements of some A[n], then convert them back to elements of A::

            sage: sorted(A[5].basis())
            [milnor[(2, 1)], milnor[(5,)]]
            sage: a = list(A[5].basis())[1]
            sage: a  # not in A, doesn't print like an element of A
            milnor[(5,)]
            sage: A(a) # in A
            Sq(5)
            sage: A(a) * A(a)
            Sq(7,1)
            sage: a * A(a) # only need to convert one factor
            Sq(7,1)
            sage: a.antipode() # not defined
            Traceback (most recent call last):
            ...
            AttributeError: 'CombinatorialFreeModule_with_category.element_class' object has no attribute 'antipode'...
            sage: A(a).antipode() # convert to elt of A, then compute antipode
            Sq(2,1) + Sq(5)

            sage: G = SteenrodAlgebra(p=5, profile=[[2,1], [2,2,2]], basis='pst')

        TESTS:

        The following sort of thing is also tested by the function
        :func:`steenrod_basis_error_check
        <sage.algebras.steenrod.steenrod_algebra_bases.steenrod_basis_error_check>`::

            sage: H = SteenrodAlgebra(p=5, profile=[[2,1], [2,2,2]])
            sage: G = SteenrodAlgebra(p=5, profile=[[2,1], [2,2,2]], basis='pst')
            sage: max([H[n].dimension() - G[n].dimension() for n in range(100)])
            0
        """
    __getitem__ = homogeneous_component
    def one_basis(self):
        """
        The index of the element 1 in the basis for the Steenrod algebra.

        EXAMPLES::

            sage: SteenrodAlgebra(p=2).one_basis()
            ()
            sage: SteenrodAlgebra(p=7).one_basis()
            ((), ())
        """
    def product_on_basis(self, t1, t2):
        """
        The product of two basis elements of this algebra.

        INPUT:

        - ``t1``, ``t2`` -- tuples, the indices of two basis elements of self

        OUTPUT:

        the product of the two corresponding basis elements,
        as an element of self

        ALGORITHM: If the two elements are represented in the Milnor
        basis, use Milnor multiplication as implemented in
        :mod:`sage.algebras.steenrod.steenrod_algebra_mult`.  If the two
        elements are represented in the Serre-Cartan basis, then
        multiply them using Adem relations (also implemented in
        :mod:`sage.algebras.steenrod.steenrod_algebra_mult`).  This
        provides a good way of checking work -- multiply Milnor
        elements, then convert them to Adem elements and multiply
        those, and see if the answers correspond.

        If the two elements are represented in some other basis, then
        convert them both to the Milnor basis and multiply.

        EXAMPLES::

            sage: Milnor = SteenrodAlgebra()
            sage: Milnor.product_on_basis((2,), (2,))
            Sq(1,1)
            sage: Adem = SteenrodAlgebra(basis='adem')
            sage: Adem.Sq(2) * Adem.Sq(2) # indirect doctest
            Sq^3 Sq^1

        When multiplying elements from different bases, the left-hand
        factor determines the form of the output::

            sage: Adem.Sq(2) * Milnor.Sq(2)
            Sq^3 Sq^1
            sage: Milnor.Sq(2) * Adem.Sq(2)
            Sq(1,1)

        TESTS::

            sage: all(Adem(Milnor.Sq(n) ** 3)._repr_() == (Adem.Sq(n) ** 3)._repr_() for n in range(10))
            True
            sage: Wall = SteenrodAlgebra(basis='wall')
            sage: Wall(Adem.Sq(4,4) * Milnor.Sq(4)) == Adem(Wall.Sq(4,4) * Milnor.Sq(4))
            True

            sage: A3 = SteenrodAlgebra(p=3, basis='adem')
            sage: M3 = SteenrodAlgebra(p=3, basis='milnor')
            sage: all(A3(M3.P(n) * M3.Q(0) * M3.P(n))._repr_() == (A3.P(n) * A3.Q(0) * A3.P(n))._repr_() for n in range(5))
            True

            sage: EA = SteenrodAlgebra(generic=True)
            sage: EA.product_on_basis(((1, 3), (2, 1)), ((2, ), (0, 0, 1)))
            Q_1 Q_2 Q_3 P(2,1,1)

            sage: EA2 = SteenrodAlgebra(basis='serre-cartan', generic=True)
            sage: EA2.product_on_basis((1, 2, 0, 1, 0), (1, 2, 0, 1, 0))
            beta P^4 P^2 beta + beta P^5 beta P^1
        """
    def coproduct_on_basis(self, t, algorithm=None):
        """
        The coproduct of a basis element of this algebra.

        INPUT:

        - ``t`` -- tuple, the index of a basis element of self

        - ``algorithm`` -- ``None`` or a string, either 'milnor' or
          'serre-cartan' (or anything which will be converted to one
          of these by the function :func:`get_basis_name
          <sage.algebras.steenrod.steenrod_algebra_misc.get_basis_name>`.
          If ``None``, default to 'milnor' unless current basis is
          'serre-cartan', in which case use 'serre-cartan'.

        ALGORITHM: The coproduct on a Milnor basis element `P(n_1,
        n_2, ...)` is `\\sum P(i_1, i_2, ...) \\otimes P(j_1, j_2,
        ...)`, summed over all `i_k + j_k = n_k` for each `k`.  At odd
        primes, each element `Q_n` is primitive: its coproduct is `Q_n
        \\otimes 1 + 1 \\otimes Q_n`.

        One can deduce a coproduct formula for the Serre-Cartan basis
        from this: the coproduct on each `P^n` is `\\sum P^i \\otimes
        P^{n-i}` and at odd primes `\\beta` is primitive.  Since the
        coproduct is an algebra map, one can then compute the
        coproduct on any Serre-Cartan basis element.

        Which of these methods is used is controlled by whether
        ``algorithm`` is 'milnor' or 'serre-cartan'.

        OUTPUT:

        the coproduct of the corresponding basis element,
        as an element of ``self`` tensor ``self``.

        EXAMPLES::

            sage: A = SteenrodAlgebra()
            sage: A.coproduct_on_basis((3,))
            1 # Sq(3) + Sq(1) # Sq(2) + Sq(2) # Sq(1) + Sq(3) # 1

        TESTS::

            sage: all(A.coproduct_on_basis((n,1), algorithm='milnor') == A.coproduct_on_basis((n,1), algorithm='adem') for n in range(9)) # long time
            True
            sage: A7 = SteenrodAlgebra(p=7, basis='adem')
            sage: all(A7.coproduct_on_basis((0,n,1), algorithm='milnor') == A7.coproduct_on_basis((0,n,1), algorithm='adem') for n in range(9)) # long time
            True
        """
    def coproduct(self, x, algorithm: str = 'milnor'):
        """
        Return the coproduct of an element ``x`` of this algebra.

        INPUT:

        - ``x`` -- element of ``self``

        - ``algorithm`` -- ``None`` or a string, either ``'milnor'`` or
          ``'serre-cartan'`` (or anything which will be converted to one
          of these by the function :func:`get_basis_name
          <sage.algebras.steenrod.steenrod_algebra_misc.get_basis_name>`.
          If ``None``, default to ``'serre-cartan'`` if current basis is
          ``'serre-cartan'``; otherwise use ``'milnor'``.

        This calls :meth:`coproduct_on_basis` on the summands of ``x``
        and extends linearly.

        EXAMPLES::

            sage: SteenrodAlgebra().Sq(3).coproduct()
            1 # Sq(3) + Sq(1) # Sq(2) + Sq(2) # Sq(1) + Sq(3) # 1

        The element `\\text{Sq}(0,1)` is primitive::

            sage: SteenrodAlgebra(basis='adem').Sq(0,1).coproduct()
            1 # Sq^2 Sq^1 + 1 # Sq^3 + Sq^2 Sq^1 # 1 + Sq^3 # 1
            sage: SteenrodAlgebra(basis='pst').Sq(0,1).coproduct()
            1 # P^0_2 + P^0_2 # 1

            sage: SteenrodAlgebra(p=3).P(4).coproduct()
            1 # P(4) + P(1) # P(3) + P(2) # P(2) + P(3) # P(1) + P(4) # 1
            sage: SteenrodAlgebra(p=3).P(4).coproduct(algorithm='serre-cartan')
            1 # P(4) + P(1) # P(3) + P(2) # P(2) + P(3) # P(1) + P(4) # 1
            sage: SteenrodAlgebra(p=3, basis='serre-cartan').P(4).coproduct()
            1 # P^4 + P^1 # P^3 + P^2 # P^2 + P^3 # P^1 + P^4 # 1
            sage: SteenrodAlgebra(p=11, profile=((), (2,1,2))).Q(0,2).coproduct()
            1 # Q_0 Q_2 + Q_0 # Q_2 + Q_0 Q_2 # 1 + 10*Q_2 # Q_0
        """
    def antipode_on_basis(self, t):
        """
        The antipode of a basis element of this algebra.

        INPUT:

        - ``t`` -- tuple, the index of a basis element of ``self``

        OUTPUT:

        the antipode of the corresponding basis element,
        as an element of ``self``.

        ALGORITHM: according to a result of Milnor's, the antipode of
        `\\text{Sq}(n)` is the sum of all of the Milnor basis elements
        in dimension `n`. So: convert the element to the Serre-Cartan
        basis, thus writing it as a sum of products of elements
        `\\text{Sq}(n)`, and use Milnor's formula for the antipode of
        `\\text{Sq}(n)`, together with the fact that the antipode is an
        antihomomorphism: if we call the antipode `c`, then `c(ab) =
        c(b) c(a)`.

        At odd primes, a similar method is used: the antipode of
        `P(n)` is the sum of the Milnor P basis elements in dimension
        `n*2(p-1)`, multiplied by `(-1)^n`, and the antipode of `\\beta
        = Q_0` is `-Q_0`. So convert to the Serre-Cartan basis, as in
        the `p = 2` case. Note that in the odd prime case, there is a
        sign in the antihomomorphism formula:
        `c(ab) = (-1)^{\\deg a \\deg b} c(b) c(a)`.

        EXAMPLES::

            sage: A = SteenrodAlgebra()
            sage: A.antipode_on_basis((4,))
            Sq(1,1) + Sq(4)
            sage: A.Sq(4).antipode()
            Sq(1,1) + Sq(4)
            sage: Adem = SteenrodAlgebra(basis='adem')
            sage: Adem.Sq(4).antipode()
            Sq^3 Sq^1 + Sq^4
            sage: SteenrodAlgebra(basis='pst').Sq(3).antipode()
            P^0_1 P^1_1 + P^0_2
            sage: a = SteenrodAlgebra(basis='wall_long').Sq(10)
            sage: a.antipode()
            Sq^1 Sq^2 Sq^4 Sq^1 Sq^2 + Sq^2 Sq^4 Sq^1 Sq^2 Sq^1 + Sq^8 Sq^2
            sage: a.antipode().antipode() == a
            True

            sage: SteenrodAlgebra(p=3).P(6).antipode()
            P(2,1) + P(6)
            sage: SteenrodAlgebra(p=3).P(6).antipode().antipode()
            P(6)

        TESTS::

            sage: Milnor = SteenrodAlgebra()
            sage: all(x.antipode().antipode() == x for x in Milnor.basis(11))  # long time
            True
            sage: A5 = SteenrodAlgebra(p=5, basis='adem')
            sage: all(x.antipode().antipode() == x for x in A5.basis(25))
            True
            sage: H = SteenrodAlgebra(profile=[2,2,1])
            sage: H.Sq(1,2).antipode() in H
            True

            sage: Q = A5.Q
            sage: (Q(0) * Q(1)).antipode() == - Q(1).antipode() * Q(0).antipode()
            True
        """
    def counit_on_basis(self, t):
        """
        The counit sends all elements of positive degree to zero.

        INPUT:

        - ``t`` -- tuple, the index of a basis element of ``self``

        EXAMPLES::

            sage: A2 = SteenrodAlgebra(p=2)
            sage: A2.counit_on_basis(())
            1
            sage: A2.counit_on_basis((0,0,1))
            0
            sage: parent(A2.counit_on_basis((0,0,1)))
            Finite Field of size 2
            sage: A3 = SteenrodAlgebra(p=3)
            sage: A3.counit_on_basis(((1,2,3), (1,1,1)))
            0
            sage: A3.counit_on_basis(((), ()))
            1
            sage: A3.counit(A3.P(10,5))
            0
            sage: A3.counit(A3.P(0))
            1
        """
    @lazy_attribute
    def milnor(self):
        """
        Convert an element of this algebra to the Milnor basis.

        INPUT:

        - ``x`` -- an element of this algebra

        OUTPUT: x converted to the Milnor basis

        ALGORITHM: use the method ``_milnor_on_basis`` and linearity.

        EXAMPLES::

            sage: Adem = SteenrodAlgebra(basis='adem')
            sage: a = Adem.Sq(2) * Adem.Sq(1)
            sage: Adem.milnor(a)
            Sq(0,1) + Sq(3)
        """
    def degree_on_basis(self, t):
        """
        The degree of the monomial specified by the tuple ``t``.

        INPUT:

        - ``t`` -- tuple, representing basis element in the current basis

        OUTPUT: integer, the degree of the corresponding element

        The degree of `\\text{Sq}(i_1,i_2,i_3,...)` is

        .. MATH::

            i_1 + 3i_2 + 7i_3 + ... + (2^k - 1) i_k + ....

        At an odd prime `p`, the degree of `Q_k` is `2p^k - 1` and the
        degree of `\\mathcal{P}(i_1, i_2, ...)` is

        .. MATH::

            \\sum_{k \\geq 0} 2(p^k - 1) i_k.

        ALGORITHM: Each basis element is represented in terms relevant
        to the particular basis: 'milnor' basis elements (at the prime
        2) are given by tuples ``(a,b,c,...)`` corresponding to the
        element `\\text{Sq}(a,b,c,...)`, while 'pst' basis elements are
        given by tuples of pairs ``((a, b), (c, d), ...)``,
        corresponding to the product `P^a_b P^c_d ...`.  The other
        bases have similar descriptions.  The degree of each basis
        element is computed from this data, rather than converting the
        element to the Milnor basis, for example, and then computing
        the degree.

        EXAMPLES::

            sage: SteenrodAlgebra().degree_on_basis((0,0,1))
            7
            sage: Sq(7).degree()
            7

            sage: A11 = SteenrodAlgebra(p=11)
            sage: A11.degree_on_basis(((), (1,1)))
            260
            sage: A11.degree_on_basis(((2,), ()))
            241
        """
    def __contains__(self, x) -> bool:
        """
        Return ``True`` if ``self`` contains `x`.

        EXAMPLES::

            sage: Sq(3,1,1) in SteenrodAlgebra()
            True
            sage: Sq(3,1,1) in SteenrodAlgebra(p=5)
            False

            sage: A1 = SteenrodAlgebra(profile=[2,1])
            sage: Sq(3) in A1
            True
            sage: Sq(4) in A1
            False
            sage: Sq(0,2) in A1
            False

            sage: Sq(3) in SteenrodAlgebra(generic=True)
            False

            sage: A_3 = SteenrodAlgebra(p=3)
            sage: B_3 = SteenrodAlgebra(p=3, profile=([1], [2,2,1,1]))
            sage: A_3.P(2) in B_3
            True
            sage: A_3.P(3) in B_3
            False
            sage: A_3.Q(1) in B_3
            True
            sage: A_3.P(1) * A_3.Q(2) in B_3
            False
        """
    def basis(self, d=None):
        '''
        Return basis for ``self``, either the whole basis or the basis in
        degree `d`.

        INPUT:

        - ``d`` -- integer or ``None`` (default: ``None``)

        OUTPUT:

        If `d` is ``None``, then return a basis of the algebra.
        Otherwise, return the basis in degree `d`.

        EXAMPLES::

            sage: A3 = SteenrodAlgebra(3)
            sage: A3.basis(13)
            Family (Q_1 P(2), Q_0 P(3))
            sage: SteenrodAlgebra(2, \'adem\').basis(12)
            Family (Sq^12, Sq^11 Sq^1, Sq^9 Sq^2 Sq^1, Sq^8 Sq^3 Sq^1, Sq^10 Sq^2, Sq^9 Sq^3, Sq^8 Sq^4)

            sage: A = SteenrodAlgebra(profile=[1,2,1])
            sage: A.basis(2)
            Family ()
            sage: A.basis(3)
            Family (Sq(0,1),)
            sage: SteenrodAlgebra().basis(3)
            Family (Sq(0,1), Sq(3))
            sage: A_pst = SteenrodAlgebra(profile=[1,2,1], basis=\'pst\')
            sage: A_pst.basis(3)
            Family (P^0_2,)

            sage: A7 = SteenrodAlgebra(p=7)
            sage: B = SteenrodAlgebra(p=7, profile=([1,2,1], [1]))
            sage: A7.basis(84)
            Family (P(7),)
            sage: B.basis(84)
            Family ()
            sage: C = SteenrodAlgebra(p=7, profile=([1], [2,2]))
            sage: A7.Q(0,1) in C.basis(14)
            True
            sage: A7.Q(2) in A7.basis(97)
            True
            sage: A7.Q(2) in C.basis(97)
            False

        With no arguments, return the basis of the whole algebra.
        This does not print in a very helpful way, unfortunately::

            sage: A7.basis()
            Lazy family (Term map from basis key family of mod 7 Steenrod algebra, milnor basis
             to mod 7 Steenrod algebra, milnor basis(i))_{i in basis key family
             of mod 7 Steenrod algebra, milnor basis}
            sage: for (idx,a) in zip((1,..,9),A7.basis()):
            ....:      print("{} {}".format(idx, a))
            1 1
            2 Q_0
            3 P(1)
            4 Q_1
            5 Q_0 P(1)
            6 Q_0 Q_1
            7 P(2)
            8 Q_1 P(1)
            9 Q_0 P(2)
            sage: D = SteenrodAlgebra(p=3, profile=([1], [2,2]))
            sage: sorted(D.basis())
            [1, P(1), P(2), Q_0, Q_0 P(1), Q_0 P(2), Q_0 Q_1,
             Q_0 Q_1 P(1), Q_0 Q_1 P(2), Q_1, Q_1 P(1), Q_1 P(2)]
        '''
    def P(self, *nums):
        """
        The element `P(a, b, c, \\ldots)`.

        INPUT:

        - ``a``, ``b``, ``c``, ... -- nonnegative integers

        OUTPUT:

        element of the Steenrod algebra given by the Milnor
        single basis element `P(a, b, c, ...)`

        Note that at the prime 2, this is the same element as
        `\\text{Sq}(a, b, c, ...)`.

        EXAMPLES::

            sage: A = SteenrodAlgebra(2)
            sage: A.P(5)
            Sq(5)
            sage: B = SteenrodAlgebra(3)
            sage: B.P(5,1,1)
            P(5,1,1)
            sage: B.P(1,1,-12,1)
            Traceback (most recent call last):
            ...
            TypeError: entries must be nonnegative integers

            sage: SteenrodAlgebra(basis='serre-cartan').P(0,1)
            Sq^2 Sq^1 + Sq^3
            sage: SteenrodAlgebra(generic=True).P(2,0,1)
            P(2,0,1)
        """
    def Q_exp(self, *nums):
        """
        The element `Q_0^{e_0} Q_1^{e_1} ...` , given by
        specifying the exponents.

        INPUT:

        - ``e0``, ``e1``, ... -- sequence of 0s and 1s

        OUTPUT: the element `Q_0^{e_0} Q_1^{e_1} ...`

        Note that at the prime 2, `Q_n` is the element
        `\\text{Sq}(0,0,...,1)` , where the 1 is in the
        `(n+1)^{st}` position.

        Compare this to the method :meth:`Q`, which defines a similar
        element, but by specifying the tuple of subscripts of terms
        with exponent 1.

        EXAMPLES::

            sage: A2 = SteenrodAlgebra(2)
            sage: A5 = SteenrodAlgebra(5)
            sage: A2.Q_exp(0,0,1,1,0)
            Sq(0,0,1,1)
            sage: A5.Q_exp(0,0,1,1,0)
            Q_2 Q_3
            sage: A5.Q(2,3)
            Q_2 Q_3
            sage: A5.Q_exp(0,0,1,1,0) == A5.Q(2,3)
            True
            sage: SteenrodAlgebra(2,generic=True).Q_exp(1,0,1)
            Q_0 Q_2
        """
    def Q(self, *nums):
        """
        The element `Q_{n0} Q_{n1} ...` , given by specifying the
        subscripts.

        INPUT:

        - ``n0``, ``n1``, ... -- nonnegative integers

        OUTPUT: the element `Q_{n0} Q_{n1} ...`

        Note that at the prime 2, `Q_n` is the element
        `\\text{Sq}(0,0,...,1)` , where the 1 is in the
        `(n+1)^{st}` position.

        Compare this to the method :meth:`Q_exp`, which defines a
        similar element, but by specifying the tuple of exponents.

        EXAMPLES::

            sage: A2 = SteenrodAlgebra(2)
            sage: A2.Q(2,3)
            Sq(0,0,1,1)
            sage: A5 = SteenrodAlgebra(5)
            sage: A5.Q(1,4)
            Q_1 Q_4
            sage: A5.Q(1,4) == A5.Q_exp(0,1,0,0,1)
            True
            sage: H = SteenrodAlgebra(p=5, profile=[[2,1], [2,2,2]])
            sage: H.Q(2)
            Q_2
            sage: H.Q(4)
            Traceback (most recent call last):
            ...
            ValueError: element not in this algebra
        """
    def pst(self, s, t):
        """
        The Margolis element `P^s_t`.

        INPUT:

        - ``s`` -- nonnegative integer

        - ``t`` -- positive integer

        - ``p`` -- positive prime number

        OUTPUT: element of the Steenrod algebra

        This returns the Margolis element `P^s_t` of the mod
        `p` Steenrod algebra: the element equal to
        `P(0,0,...,0,p^s)`, where the `p^s` is in position
        `t`.

        EXAMPLES::

            sage: A2 = SteenrodAlgebra(2)
            sage: A2.pst(3,5)
            Sq(0,0,0,0,8)
            sage: A2.pst(1,2) == Sq(4)*Sq(2) + Sq(2)*Sq(4)
            True
            sage: SteenrodAlgebra(5).pst(3,5)
            P(0,0,0,0,125)
        """
    def ngens(self):
        """
        Number of generators of ``self``.

        OUTPUT: number or Infinity

        The Steenrod algebra is infinitely generated.  A sub-Hopf
        algebra may be finitely or infinitely generated; in general,
        it is not clear what a minimal generating set is, nor the
        cardinality of that set.  So: if the algebra is
        infinite-dimensional, this returns Infinity.  If the algebra
        is finite-dimensional and is equal to one of the sub-Hopf
        algebras `A(n)`, then their minimal generating set is known,
        and this returns the cardinality of that set.  Otherwise, any
        sub-Hopf algebra is (not necessarily minimally) generated by
        the `P^s_t`'s that it contains (along with the `Q_n`'s it
        contains, at odd primes), so this returns the number of
        `P^s_t`'s and `Q_n`'s in the algebra.

        EXAMPLES::

            sage: A = SteenrodAlgebra(3)
            sage: A.ngens()
            +Infinity
            sage: SteenrodAlgebra(profile=lambda n: n).ngens()
            +Infinity
            sage: SteenrodAlgebra(profile=[3,2,1]).ngens() # A(2)
            3
            sage: SteenrodAlgebra(profile=[3,2,1], basis='pst').ngens()
            3
            sage: SteenrodAlgebra(p=3, profile=[[3,2,1], [2,2,2,2]]).ngens()  # A(3) at p=3
            4
            sage: SteenrodAlgebra(profile=[1,2,1,1]).ngens()
            5
        """
    def gens(self) -> Family:
        """
        Family of generators for this algebra.

        OUTPUT: family of elements of this algebra

        At the prime 2, the Steenrod algebra is generated by the
        elements `\\text{Sq}^{2^i}` for `i \\geq 0`.  At odd primes, it
        is generated by the elements `Q_0` and `\\mathcal{P}^{p^i}` for
        `i \\geq 0`.  So if this algebra is the entire Steenrod
        algebra, return an infinite family made up of these elements.

        For sub-Hopf algebras of the Steenrod algebra, it is not
        always clear what a minimal generating set is.  The sub-Hopf
        algebra `A(n)` is minimally generated by the elements
        `\\text{Sq}^{2^i}` for `0 \\leq i \\leq n` at the prime 2.  At
        odd primes, `A(n)` is minimally generated by `Q_0` along with
        `\\mathcal{P}^{p^i}` for `0 \\leq i \\leq n-1`.  So if this
        algebra is `A(n)`, return the appropriate list of generators.

        For other sub-Hopf algebras: return a non-minimal generating
        set: the family of `P^s_t`'s and `Q_n`'s contained in the
        algebra.

        EXAMPLES::

            sage: A3 = SteenrodAlgebra(3, 'adem')
            sage: A3.gens()
            Lazy family (<bound method SteenrodAlgebra_generic.gen of mod 3 Steenrod algebra,
             serre-cartan basis>(i))_{i in Non negative integers}
            sage: A3.gens()[0]
            beta
            sage: A3.gens()[1]
            P^1
            sage: A3.gens()[2]
            P^3
            sage: SteenrodAlgebra(profile=[3,2,1]).gens()
            Family (Sq(1), Sq(2), Sq(4))

        In the following case, return a non-minimal generating set.
        (It is not minimal because `\\text{Sq}(0,0,1)` is the
        commutator of `\\text{Sq}(1)` and `\\text{Sq}(0,2)`.) ::

            sage: SteenrodAlgebra(profile=[1,2,1]).gens()
            Family (Sq(1), Sq(0,1), Sq(0,2), Sq(0,0,1))
            sage: SteenrodAlgebra(p=5, profile=[[2,1], [2,2,2]]).gens()
            Family (Q_0, P(1), P(5))
            sage: SteenrodAlgebra(profile=lambda n: n).gens()
            Lazy family (<bound method SteenrodAlgebra_generic.gen of sub-Hopf algebra
             of mod 2 Steenrod algebra, milnor basis, profile function [1, 2, 3, ...,
             98, 99, +Infinity, +Infinity, +Infinity, ...]>(i))_{i in Non negative integers}

        You may also use ``algebra_generators`` instead of ``gens``::

            sage: SteenrodAlgebra(p=5, profile=[[2,1], [2,2,2]]).algebra_generators()
            Family (Q_0, P(1), P(5))
        """
    algebra_generators = gens
    def gen(self, i: int = 0):
        """
        The `i`-th generator of this algebra.

        INPUT:

        - ``i`` -- nonnegative integer

        OUTPUT: the `i`-th generator of this algebra

        For the full Steenrod algebra, the `i`-th generator is
        `\\text{Sq}(2^i)` at the prime 2; when `p` is odd, the `0`-th generator
        is `\\beta = Q(0)`, and for `i>0`, the `i`-th generator is
        `P(p^{i-1})`.

        For sub-Hopf algebras of the Steenrod algebra, it is not
        always clear what a minimal generating set is.  The sub-Hopf
        algebra `A(n)` is minimally generated by the elements
        `\\text{Sq}^{2^i}` for `0 \\leq i \\leq n` at the prime 2.  At
        odd primes, `A(n)` is minimally generated by `Q_0` along with
        `\\mathcal{P}^{p^i}` for `0 \\leq i \\leq n-1`.  So if this
        algebra is `A(n)`, return the appropriate generator.

        For other sub-Hopf algebras: they are generated (but not
        necessarily minimally) by the `P^s_t`'s (and `Q_n`'s, if `p`
        is odd) that they contain.  So order the `P^s_t`'s (and
        `Q_n`'s) in the algebra by degree and return the `i`-th one.

        EXAMPLES::

            sage: A = SteenrodAlgebra(2)
            sage: A.gen(4)
            Sq(16)
            sage: A.gen(200)
            Sq(1606938044258990275541962092341162602522202993782792835301376)
            sage: SteenrodAlgebra(2, basis='adem').gen(2)
            Sq^4
            sage: SteenrodAlgebra(2, basis='pst').gen(2)
            P^2_1
            sage: B = SteenrodAlgebra(5)
            sage: B.gen(0)
            Q_0
            sage: B.gen(2)
            P(5)

            sage: SteenrodAlgebra(profile=[2,1]).gen(1)
            Sq(2)
            sage: SteenrodAlgebra(profile=[1,2,1]).gen(1)
            Sq(0,1)
            sage: SteenrodAlgebra(profile=[1,2,1]).gen(5)
            Traceback (most recent call last):
            ...
            ValueError: this algebra only has 4 generators, so call gen(i) with 0 <= i < 4

            sage: D = SteenrodAlgebra(profile=lambda n: n)
            sage: [D.gen(n) for n in range(5)]
            [Sq(1), Sq(0,1), Sq(0,2), Sq(0,0,1), Sq(0,0,2)]
            sage: D3 = SteenrodAlgebra(p=3, profile=(lambda n: n, lambda n: 2))
            sage: [D3.gen(n) for n in range(9)]
            [Q_0, P(1), Q_1, P(0,1), Q_2, P(0,3), P(0,0,1), Q_3, P(0,0,3)]
            sage: D3 = SteenrodAlgebra(p=3, profile=(lambda n: n, lambda n: 1 if n<1 else 2))
            sage: [D3.gen(n) for n in range(9)]
            [P(1), Q_1, P(0,1), Q_2, P(0,3), P(0,0,1), Q_3, P(0,0,3), P(0,0,0,1)]
            sage: SteenrodAlgebra(p=5, profile=[[2,1], [2,2,2]], basis='pst').gen(2)
            P^1_1
        """
    def is_commutative(self) -> bool:
        """
        Return ``True`` if ``self`` is graded commutative, as determined by the
        profile function.

        In particular, a sub-Hopf algebra of the
        mod 2 Steenrod algebra is commutative if and only if there is
        an integer `n>0` so that its profile function `e` satisfies

        - `e(i) = 0` for `i < n`,
        - `e(i) \\leq n` for `i \\geq n`.

        When `p` is odd, there must be an integer `n \\geq 0` so that
        the profile functions `e` and `k` satisfy

        - `e(i) = 0` for `i < n`,
        - `e(i) \\leq n` for `i \\geq n`.
        - `k(i) = 1` for `i < n`.

        EXAMPLES::

            sage: A = SteenrodAlgebra(p=3)
            sage: A.is_commutative()
            False
            sage: SteenrodAlgebra(profile=[2,1]).is_commutative()
            False
            sage: SteenrodAlgebra(profile=[0,2,2,1]).is_commutative()
            True

        Note that if the profile function is specified by a function,
        then by default it has infinite truncation type: the profile
        function is assumed to be infinite after the 100th term.  ::

            sage: SteenrodAlgebra(profile=lambda n: 1).is_commutative()
            False
            sage: SteenrodAlgebra(profile=lambda n: 1, truncation_type=0).is_commutative()
            True

            sage: SteenrodAlgebra(p=5, profile=([0,2,2,1], [])).is_commutative()
            True
            sage: SteenrodAlgebra(p=5, profile=([0,2,2,1], [1,1,2])).is_commutative()
            True
            sage: SteenrodAlgebra(p=5, profile=([0,2,1], [1,2,2,2])).is_commutative()
            False
        """
    def is_finite(self):
        """
        Return ``True`` if this algebra is finite-dimensional.

        Therefore true if the profile function is finite, and in
        particular the ``truncation_type`` must be finite.

        EXAMPLES::

            sage: A = SteenrodAlgebra(p=3)
            sage: A.is_finite()
            False
            sage: SteenrodAlgebra(profile=[3,2,1]).is_finite()
            True
            sage: SteenrodAlgebra(profile=lambda n: n).is_finite()
            False
        """
    def dimension(self):
        """
        The dimension of this algebra as a vector space over `\\GF{p}`.

        If the algebra is infinite, return ``+Infinity``.  Otherwise,
        the profile function must be finite.  In this case, at the
        prime 2, its dimension is `2^s`, where `s` is the sum of the
        entries in the profile function.  At odd primes, the dimension
        is `p^s * 2^t` where `s` is the sum of the `e` component of
        the profile function and `t` is the number of 2's in the `k`
        component of the profile function.

        EXAMPLES::

            sage: SteenrodAlgebra(p=7).dimension()
            +Infinity
            sage: SteenrodAlgebra(profile=[3,2,1]).dimension()
            64
            sage: SteenrodAlgebra(p=3, profile=([1,1], [])).dimension()
            9
            sage: SteenrodAlgebra(p=5, profile=([1], [2,2])).dimension()
            20
        """
    @cached_method
    def top_class(self):
        """
        Highest dimensional basis element. This is only defined if the algebra is finite.

        EXAMPLES::

            sage: SteenrodAlgebra(2, profile=(3,2,1)).top_class()
            Sq(7,3,1)
            sage: SteenrodAlgebra(3, profile=((2,2,1),(1,2,2,2,2))).top_class()
            Q_1 Q_2 Q_3 Q_4 P(8,8,2)

        TESTS::

            sage: SteenrodAlgebra(2, profile=(3,2,1), basis='pst').top_class()
            P^0_1 P^0_2 P^1_1 P^0_3 P^1_2 P^2_1
            sage: SteenrodAlgebra(5, profile=((0,),(2,1,2,2))).top_class()
            Q_0 Q_2 Q_3
            sage: SteenrodAlgebra(5).top_class()
            Traceback (most recent call last):
            ...
            ValueError: the algebra is not finite dimensional

        Currently, we create the top class in the Milnor basis version and transform
        this result back into the requested basis. This approach is easy to implement
        but far from optimal for the 'pst' basis.  Occasionally, it also gives an awkward
        leading coefficient::

            sage: SteenrodAlgebra(3, profile=((2,1),(1,2,2)), basis='pst').top_class()
            2 Q_1 Q_2 (P^0_1)^2 (P^0_2)^2 (P^1_1)^2

        TESTS::

            sage: A = SteenrodAlgebra(2, profile=(3,2,1), basis='pst')
            sage: A.top_class().parent() is A
            True
        """
    def order(self):
        """
        The order of this algebra.

        This is computed by computing its vector space dimension `d`
        and then returning `p^d`.

        EXAMPLES::

            sage: SteenrodAlgebra(p=7).order()
            +Infinity
            sage: SteenrodAlgebra(profile=[2,1]).dimension()
            8
            sage: SteenrodAlgebra(profile=[2,1]).order()
            256
            sage: SteenrodAlgebra(p=3, profile=([1], [])).dimension()
            3
            sage: SteenrodAlgebra(p=3, profile=([1], [])).order()
            27
            sage: SteenrodAlgebra(p=5, profile=([], [2, 2])).dimension()
            4
            sage: SteenrodAlgebra(p=5, profile=([], [2, 2])).order() == 5**4
            True
        """
    def is_division_algebra(self):
        """
        The only way this algebra can be a division algebra is if it
        is the ground field `\\GF{p}`.

        EXAMPLES::

            sage: SteenrodAlgebra(11).is_division_algebra()
            False
            sage: SteenrodAlgebra(profile=lambda n: 0, truncation_type=0).is_division_algebra()
            True
        """
    def is_field(self, proof: bool = True):
        """
        The only way this algebra can be a field is if it is the
        ground field `\\GF{p}`.

        EXAMPLES::

            sage: SteenrodAlgebra(11).is_field()
            False
            sage: SteenrodAlgebra(profile=lambda n: 0, truncation_type=0).is_field()
            True
        """
    def is_integral_domain(self, proof: bool = True):
        """
        The only way this algebra can be an integral domain is if it
        is the ground field `\\GF{p}`.

        EXAMPLES::

            sage: SteenrodAlgebra(11).is_integral_domain()
            False
            sage: SteenrodAlgebra(profile=lambda n: 0, truncation_type=0).is_integral_domain()
            True
        """
    def is_noetherian(self) -> bool:
        """
        This algebra is Noetherian if and only if it is finite.

        EXAMPLES::

            sage: SteenrodAlgebra(3).is_noetherian()
            False
            sage: SteenrodAlgebra(profile=[1,2,1]).is_noetherian()
            True
            sage: SteenrodAlgebra(profile=lambda n: n+2).is_noetherian()
            False
        """
    def is_generic(self):
        """
        The algebra is generic if it is based on the odd-primary relations,
        i.e. if its dual is a quotient of

        .. MATH::

            A_* = \\GF{p} [\\xi_1, \\xi_2, \\xi_3, ...] \\otimes \\Lambda (\\tau_0, \\tau_1, ...)

        Sage also allows this for `p=2`. Only the usual Steenrod algebra at the prime `2` and
        its sub algebras are non-generic.

        EXAMPLES::

            sage: SteenrodAlgebra(3).is_generic()
            True
            sage: SteenrodAlgebra(2).is_generic()
            False
            sage: SteenrodAlgebra(2, generic=True).is_generic()
            True
        """
    class Element(CombinatorialFreeModule.Element):
        """
        Class for elements of the Steenrod algebra.  Since the
        Steenrod algebra class is based on
        :class:`CombinatorialFreeModule
        <sage.combinat.free_module.CombinatorialFreeModule>`, this is
        based on :class:`IndexedFreeModuleElement
        <sage.modules.with_basis.indexed_element.IndexedFreeModuleElement>`.
        It has new methods reflecting its role, like :meth:`degree`
        for computing the degree of an element.

        EXAMPLES:

        Since this class inherits from
        :class:`IndexedFreeModuleElement
        <sage.modules.with_basis.indexed_element.IndexedFreeModuleElement>`,
        elements can be used as iterators, and there are other useful
        methods::

            sage: c = Sq(5).antipode(); c
            Sq(2,1) + Sq(5)
            sage: for mono, coeff in c: print((coeff, mono))
            (1, (5,))
            (1, (2, 1))
            sage: c.monomial_coefficients() == {(2, 1): 1, (5,): 1}
            True
            sage: sorted(c.monomials(), key=lambda x: tuple(x.support()))
            [Sq(2,1), Sq(5)]
            sage: sorted(c.support())
            [(2, 1), (5,)]

        See the documentation for this module (type
        ``sage.algebras.steenrod.steenrod_algebra?``) for more
        information about elements of the Steenrod algebra.
        """
        def prime(self):
            """
            The prime associated to ``self``.

            EXAMPLES::

                sage: a = SteenrodAlgebra().Sq(3,2,1)
                sage: a.prime()
                2
                sage: a.change_basis('adem').prime()
                2
                sage: b = SteenrodAlgebra(p=7).basis(36)[0]
                sage: b.prime()
                7
                sage: SteenrodAlgebra(p=3, basis='adem').one().prime()
                3
            """
        def basis_name(self):
            """
            The basis name associated to ``self``.

            EXAMPLES::

                sage: a = SteenrodAlgebra().Sq(3,2,1)
                sage: a.basis_name()
                'milnor'
                sage: a.change_basis('adem').basis_name()
                'serre-cartan'
                sage: a.change_basis('wood____y').basis_name()
                'woody'
                sage: b = SteenrodAlgebra(p=7).basis(36)[0]
                sage: b.basis_name()
                'milnor'
                sage: a.change_basis('adem').basis_name()
                'serre-cartan'
            """
        def is_homogeneous(self):
            """
            Return ``True`` iff this element is homogeneous.

            EXAMPLES::

                sage: (Sq(0,0,1) + Sq(7)).is_homogeneous()
                True
                sage: (Sq(0,0,1) + Sq(2)).is_homogeneous()
                False
            """
        def degree(self):
            """
            The degree of ``self``.

            The degree of `\\text{Sq}(i_1,i_2,i_3,...)` is

            .. MATH::

                i_1 + 3i_2 + 7i_3 + ... + (2^k - 1) i_k + ....

            At an odd prime `p`, the degree of `Q_k` is `2p^k - 1` and the
            degree of `\\mathcal{P}(i_1, i_2, ...)` is

            .. MATH::

                \\sum_{k \\geq 0} 2(p^k - 1) i_k.

            ALGORITHM: If :meth:`is_homogeneous` returns True, call
            :meth:`SteenrodAlgebra_generic.degree_on_basis` on the leading
            summand.

            EXAMPLES::

                sage: Sq(0,0,1).degree()
                7
                sage: (Sq(0,0,1) + Sq(7)).degree()
                7
                sage: (Sq(0,0,1) + Sq(2)).degree()
                Traceback (most recent call last):
                ...
                ValueError: element is not homogeneous

                sage: A11 = SteenrodAlgebra(p=11)
                sage: A11.P(1).degree()
                20
                sage: A11.P(1,1).degree()
                260
                sage: A11.Q(2).degree()
                241

            TESTS::

                sage: all(x.degree() == 10 for x in SteenrodAlgebra(basis='woody').basis(10))
                True
                sage: all(x.degree() == 11 for x in SteenrodAlgebra(basis='woodz').basis(11))
                True
                sage: all(x.degree() == x.milnor().degree() for x in SteenrodAlgebra(basis='wall').basis(11))
                True
                sage: a = SteenrodAlgebra(basis='pst').basis(10)[0]
                sage: a.degree() == a.change_basis('arnonc').degree()
                True
                sage: b = SteenrodAlgebra(basis='comm').basis(12)[1]
                sage: b.degree() == b.change_basis('adem').change_basis('arnona').degree()
                True
                sage: all(x.degree() == 9 for x in SteenrodAlgebra(basis='comm').basis(9))
                True
                sage: all(x.degree() == 8 for x in SteenrodAlgebra(basis='adem').basis(8))
                True
                sage: all(x.degree() == 7 for x in SteenrodAlgebra(basis='milnor').basis(7))
                True
                sage: all(x.degree() == 24 for x in SteenrodAlgebra(p=3).basis(24))
                True
                sage: all(x.degree() == 40 for x in SteenrodAlgebra(p=5, basis='serre-cartan').basis(40))
                True
            """
        def milnor(self):
            """
            Return this element in the Milnor basis; that is, as an
            element of the appropriate Steenrod algebra.

            This just calls the method
            :meth:`SteenrodAlgebra_generic.milnor`.

            EXAMPLES::

                sage: Adem = SteenrodAlgebra(basis='adem')
                sage: a = Adem.basis(4)[1]; a
                Sq^3 Sq^1
                sage: a.milnor()
                Sq(1,1)
            """
        def change_basis(self, basis: str = 'milnor'):
            """
            Representation of element with respect to basis.

            INPUT:

            - ``basis`` -- string; basis in which to work

            OUTPUT: representation of ``self`` in given basis

            The choices for ``basis`` are:

            - 'milnor' for the Milnor basis.
            - 'serre-cartan', 'serre_cartan', 'sc', 'adem', 'admissible'
              for the Serre-Cartan basis.
            - 'wood_y' for Wood's Y basis.
            - 'wood_z' for Wood's Z basis.
            - 'wall' for Wall's basis.
            - 'wall_long' for Wall's basis, alternate representation
            - 'arnon_a' for Arnon's A basis.
            - 'arnon_a_long' for Arnon's A basis, alternate representation.
            - 'arnon_c' for Arnon's C basis.
            - 'pst', 'pst_rlex', 'pst_llex', 'pst_deg', 'pst_revz' for
              various `P^s_t`-bases.
            - 'comm', 'comm_rlex', 'comm_llex', 'comm_deg', 'comm_revz'
              for various commutator bases.
            - 'comm_long', 'comm_rlex_long', etc., for commutator bases,
              alternate representations.

            See documentation for this module (by browsing the
            reference manual or by typing
            ``sage.algebras.steenrod.steenrod_algebra?``) for
            descriptions of the different bases.

            EXAMPLES::

                sage: c = Sq(2) * Sq(1)
                sage: c.change_basis('milnor')
                Sq(0,1) + Sq(3)
                sage: c.change_basis('serre-cartan')
                Sq^2 Sq^1
                sage: d = Sq(0,0,1)
                sage: d.change_basis('arnonc')
                Sq^2 Sq^5 + Sq^4 Sq^2 Sq^1 + Sq^4 Sq^3 + Sq^7
            """
        def coproduct(self, algorithm: str = 'milnor'):
            """
            The coproduct of this element.

            INPUT:

            - ``algorithm`` -- ``None`` or a string, either 'milnor' or
              'serre-cartan' (or anything which will be converted to
              one of these by the function :func:`get_basis_name
              <sage.algebras.steenrod.steenrod_algebra_misc.get_basis_name>`).
              If ``None``, default to 'serre-cartan' if current basis is
              'serre-cartan'; otherwise use 'milnor'.

            See :meth:`SteenrodAlgebra_generic.coproduct_on_basis` for
            more information on computing the coproduct.

            EXAMPLES::

                sage: a = Sq(2)
                sage: a.coproduct()
                1 # Sq(2) + Sq(1) # Sq(1) + Sq(2) # 1
                sage: b = Sq(4)
                sage: (a*b).coproduct() == (a.coproduct()) * (b.coproduct())
                True

                sage: c = a.change_basis('adem'); c.coproduct(algorithm='milnor')
                1 # Sq^2 + Sq^1 # Sq^1 + Sq^2 # 1
                sage: c = a.change_basis('adem'); c.coproduct(algorithm='adem')
                1 # Sq^2 + Sq^1 # Sq^1 + Sq^2 # 1

                sage: d = a.change_basis('comm_long'); d.coproduct()
                1 # s_2 + s_1 # s_1 + s_2 # 1

                sage: A7 = SteenrodAlgebra(p=7)
                sage: a = A7.Q(1) * A7.P(1); a
                Q_1 P(1)
                sage: a.coproduct()
                1 # Q_1 P(1) + P(1) # Q_1 + Q_1 # P(1) + Q_1 P(1) # 1
                sage: a.coproduct(algorithm='adem')
                1 # Q_1 P(1) + P(1) # Q_1 + Q_1 # P(1) + Q_1 P(1) # 1

            Once you have an element of the tensor product, you may
            want to extract the tensor factors of its summands. ::

                sage: b = Sq(2).coproduct()
                sage: b
                1 # Sq(2) + Sq(1) # Sq(1) + Sq(2) # 1
                sage: supp = sorted(b.support()); supp
                [((), (2,)), ((1,), (1,)), ((2,), ())]
                sage: Sq(*supp[0][0])
                1
                sage: Sq(*supp[0][1])
                Sq(2)
                sage: [(Sq(*x), Sq(*y)) for (x,y) in supp]
                [(1, Sq(2)), (Sq(1), Sq(1)), (Sq(2), 1)]

            The ``support`` of an element does not include the
            coefficients, so at odd primes it may be better to use
            ``monomial_coefficients``::

                sage: A3 = SteenrodAlgebra(p=3)
                sage: b = (A3.P(1)**2).coproduct()
                sage: b
                2*1 # P(2) + 2*P(1) # P(1) + 2*P(2) # 1
                sage: sorted(b.support())
                [(((), ()), ((), (2,))), (((), (1,)), ((), (1,))), (((), (2,)), ((), ()))]
                sage: b.monomial_coefficients()
                {(((), ()), ((), (2,))): 2,
                 (((), (1,)), ((), (1,))): 2,
                 (((), (2,)), ((), ())): 2}
                sage: mc = b.monomial_coefficients()
                sage: sorted([(A3.monomial(x), A3.monomial(y), mc[x,y]) for (x,y) in mc])
                [(1, P(2), 2), (P(1), P(1), 2), (P(2), 1, 2)]
            """
        def excess(self):
            """
            Excess of element.

            OUTPUT: ``excess`` -- nonnegative integer

            The excess of a Milnor basis element `\\text{Sq}(a,b,c,...)` is
            `a + b + c + \\cdots`. When `p` is odd, the excess of `Q_{0}^{e_0}
            Q_{1}^{e_1} \\cdots P(r_1, r_2, ...)` is `\\sum e_i + 2 \\sum r_i`.
            The excess of a linear combination of Milnor basis elements is
            the minimum of the excesses of those basis elements.

            See [Kr1971]_ for the proofs of these assertions.

            EXAMPLES::

                sage: a = Sq(1,2,3)
                sage: a.excess()
                6
                sage: (Sq(0,0,1) + Sq(4,1) + Sq(7)).excess()
                1
                sage: elt = Sq(0,0,1) + Sq(4,1) + Sq(7)
                sage: M = sorted(elt.monomials(), key=lambda x: tuple(x.support()))
                sage: [m.excess() for m in M]
                [1, 5, 7]
                sage: [m for m in M]
                [Sq(0,0,1), Sq(4,1), Sq(7)]
                sage: B = SteenrodAlgebra(7)
                sage: a = B.Q(1,2,5)
                sage: b = B.P(2,2,3)
                sage: a.excess()
                3
                sage: b.excess()
                14
                sage: (a + b).excess()
                3
                sage: (a * b).excess()
                17
            """
        def is_unit(self):
            """
            Return ``True`` if element has a nonzero scalar multiple of
            `P(0)` as a summand, ``False`` otherwise.

            EXAMPLES::

                sage: z = Sq(4,2) + Sq(7,1) + Sq(3,0,1)
                sage: z.is_unit()
                False
                sage: u = Sq(0) + Sq(3,1)
                sage: u == 1 + Sq(3,1)
                True
                sage: u.is_unit()
                True
                sage: A5 = SteenrodAlgebra(5)
                sage: v = A5.P(0)
                sage: (v + v + v).is_unit()
                True
            """
        def is_nilpotent(self):
            """
            Return ``True`` if element is not a unit, ``False`` otherwise.

            EXAMPLES::

                sage: z = Sq(4,2) + Sq(7,1) + Sq(3,0,1)
                sage: z.is_nilpotent()
                True
                sage: u = 1 + Sq(3,1)
                sage: u == 1 + Sq(3,1)
                True
                sage: u.is_nilpotent()
                False
            """
        def may_weight(self):
            """
            May's 'weight' of element.

            OUTPUT: ``weight`` -- nonnegative integer

            If we let `F_* (A)` be the May filtration of the Steenrod
            algebra, the weight of an element `x` is the integer `k` so
            that `x` is in `F_k(A)` and not in `F_{k+1}(A)`. According to
            Theorem 2.6 in May's thesis [May1964]_, the weight of a Milnor
            basis element is computed as follows: first, to compute the
            weight of `P(r_1,r_2, ...)`, write each `r_i` in base `p` as
            `r_i = \\sum_j p^j r_{ij}`. Then each nonzero binary digit
            `r_{ij}` contributes `i` to the weight: the weight is
            `\\sum_{i,j} i r_{ij}`. When `p` is odd, the weight of `Q_i` is
            `i+1`, so the weight of a product `Q_{i_1} Q_{i_2} ...` equals
            `(i_1+1) + (i_2+1) + ...`. Then the weight of `Q_{i_1} Q_{i_2}
            ...P(r_1,r_2, ...)` is the sum of `(i_1+1) + (i_2+1) + ...`
            and `\\sum_{i,j} i r_{ij}`.

            The weight of a sum of Milnor basis elements is the minimum of
            the weights of the summands.

            When `p=2`, we compute the weight on Milnor basis elements by
            adding up the terms in their 'height' - see
            :meth:`wall_height` for documentation. (When `p` is odd, the
            height of an element is not defined.)

            EXAMPLES::

                sage: Sq(0).may_weight()
                0
                sage: a = Sq(4)
                sage: a.may_weight()
                1
                sage: b = Sq(4)*Sq(8) + Sq(8)*Sq(4)
                sage: b.may_weight()
                2
                sage: Sq(2,1,5).wall_height()
                [2, 3, 2, 1, 1]
                sage: Sq(2,1,5).may_weight()
                9
                sage: A5 = SteenrodAlgebra(5)
                sage: a = A5.Q(1,2,4)
                sage: b = A5.P(1,2,1)
                sage: a.may_weight()
                10
                sage: b.may_weight()
                8
                sage: (a * b).may_weight()
                18
                sage: A5.P(0,0,1).may_weight()
                3
            """
        def is_decomposable(self):
            """
            Return ``True`` if element is decomposable, ``False`` otherwise.

            That is, if element is in the square of the augmentation ideal,
            return ``True``; otherwise, return ``False``.

            OUTPUT: boolean

            EXAMPLES::

                sage: a = Sq(6)
                sage: a.is_decomposable()
                True
                sage: for i in range(9):
                ....:     if not Sq(i).is_decomposable():
                ....:         print(Sq(i))
                1
                Sq(1)
                Sq(2)
                Sq(4)
                Sq(8)
                sage: A3 = SteenrodAlgebra(p=3, basis='adem')
                sage: [A3.P(n) for n in range(30) if not A3.P(n).is_decomposable()]
                [1, P^1, P^3, P^9, P^27]

            TESTS:

            These all test changing bases and printing in various bases::

                sage: A = SteenrodAlgebra(basis='milnor')
                sage: [A.Sq(n) for n in range(9) if not A.Sq(n).is_decomposable()]
                [1, Sq(1), Sq(2), Sq(4), Sq(8)]
                sage: A = SteenrodAlgebra(basis='wall_long')
                sage: [A.Sq(n) for n in range(9) if not A.Sq(n).is_decomposable()]
                [1, Sq^1, Sq^2, Sq^4, Sq^8]
                sage: A = SteenrodAlgebra(basis='arnona_long')
                sage: [A.Sq(n) for n in range(9) if not A.Sq(n).is_decomposable()]
                [1, Sq^1, Sq^2, Sq^4, Sq^8]
                sage: A = SteenrodAlgebra(basis='woodz')
                sage: [A.Sq(n) for n in range(20) if not A.Sq(n).is_decomposable()] # long time
                [1, Sq^1, Sq^2, Sq^4, Sq^8, Sq^16]
                sage: A = SteenrodAlgebra(basis='comm_long')
                sage: [A.Sq(n) for n in range(25) if not A.Sq(n).is_decomposable()] # long time
                [1, s_1, s_2, s_4, s_8, s_16]
            """
        def wall_height(self):
            """
            Wall's 'height' of element.

            OUTPUT: list of nonnegative integers

            The height of an element of the mod 2 Steenrod algebra is a
            list of nonnegative integers, defined as follows: if the
            element is a monomial in the generators `\\text{Sq}(2^i)`, then
            the `i`-th entry in the list is the number of times
            `\\text{Sq}(2^i)` appears. For an arbitrary element, write it
            as a sum of such monomials; then its height is the maximum,
            ordered right-lexicographically, of the heights of those
            monomials.

            When `p` is odd, the height of an element is not defined.

            According to Theorem 3 in [Wal1960]_, the height of the Milnor
            basis element `\\text{Sq}(r_1, r_2, ...)` is obtained as
            follows: write each `r_i` in binary as `r_i = \\sum_j 2^j
            r_{ij}`. Then each nonzero binary digit `r_{ij}` contributes 1
            to the `k`-th entry in the height, for `j \\leq k \\leq
            i+j-1`.

            EXAMPLES::

                sage: Sq(0).wall_height()
                []
                sage: a = Sq(4)
                sage: a.wall_height()
                [0, 0, 1]
                sage: b = Sq(4)*Sq(8) + Sq(8)*Sq(4)
                sage: b.wall_height()
                [0, 0, 1, 1]
                sage: Sq(0,0,3).wall_height()
                [1, 2, 2, 1]
            """
        def additive_order(self):
            """
            The additive order of any nonzero element of the mod p
            Steenrod algebra is p.

            OUTPUT: 1 (for the zero element) or p (for anything else)

            EXAMPLES::

                sage: z = Sq(4) + Sq(6) + 1
                sage: z.additive_order()
                2
                sage: (Sq(3) + Sq(3)).additive_order()
                1
            """

class SteenrodAlgebra_mod_two(SteenrodAlgebra_generic):
    """
    The mod 2 Steenrod algebra.

    Users should not call this, but use the function
    :func:`SteenrodAlgebra` instead. See that function for extensive
    documentation. (This differs from :class:`SteenrodAlgebra_generic`
    only in that it has a method :meth:`Sq` for defining elements.)
    """
    def Sq(self, *nums):
        """
        Milnor element `\\text{Sq}(a,b,c,...)`.

        INPUT:

        - ``a``, ``b``, ``c``, ... -- nonnegative integers

        OUTPUT: element of the Steenrod algebra

        This returns the Milnor basis element
        `\\text{Sq}(a, b, c, ...)`.

        EXAMPLES::

            sage: A = SteenrodAlgebra(2)
            sage: A.Sq(5)
            Sq(5)
            sage: A.Sq(5,0,2)
            Sq(5,0,2)

        Entries must be nonnegative integers; otherwise, an error
        results.
        """

def SteenrodAlgebra(p: int = 2, basis: str = 'milnor', generic: str = 'auto', **kwds):
    '''
    The mod `p` Steenrod algebra.

    INPUT:

    - ``p`` -- positive prime integer (default: 2)
    - ``basis`` -- string (default: ``\'milnor\'``)
    - ``profile`` -- a profile function in form specified below (default: ``None``)
    - ``truncation_type`` -- 0 or `\\infty` or \'auto\' (default: ``\'auto\'``)
    - ``precision`` -- integer or ``None`` (default: ``None``)
    - ``generic`` -- (default: ``\'auto\'``)

    OUTPUT:

    mod `p` Steenrod algebra or one of its sub-Hopf algebras,
    elements of which are printed using ``basis``

    See below for information about ``basis``, ``profile``, etc.

    EXAMPLES:

    Some properties of the Steenrod algebra are available::

        sage: A = SteenrodAlgebra(2)
        sage: A.order()
        +Infinity
        sage: A.is_finite()
        False
        sage: A.is_commutative()
        False
        sage: A.is_noetherian()
        False
        sage: A.is_integral_domain()
        False
        sage: A.is_field()
        False
        sage: A.is_division_algebra()
        False
        sage: A.category()
        Category of supercocommutative super Hopf algebras
         with basis over Finite Field of size 2

    There are methods for constructing elements of the Steenrod
    algebra::

        sage: A2 = SteenrodAlgebra(2); A2
        mod 2 Steenrod algebra, milnor basis
        sage: A2.Sq(1,2,6)
        Sq(1,2,6)
        sage: A2.Q(3,4)  # product of Milnor primitives Q_3 and Q_4
        Sq(0,0,0,1,1)
        sage: A2.pst(2,3)  # Margolis pst element
        Sq(0,0,4)
        sage: A5 = SteenrodAlgebra(5); A5
        mod 5 Steenrod algebra, milnor basis
        sage: A5.P(1,2,6)
        P(1,2,6)
        sage: A5.Q(3,4)
        Q_3 Q_4
        sage: A5.Q(3,4) * A5.P(1,2,6)
        Q_3 Q_4 P(1,2,6)
        sage: A5.pst(2,3)
        P(0,0,25)

    You can test whether elements are contained in the Steenrod
    algebra::

        sage: w = Sq(2) * Sq(4)
        sage: w in SteenrodAlgebra(2)
        True
        sage: w in SteenrodAlgebra(17)
        False

    .. rubric:: Different bases for the Steenrod algebra:

    There are two standard vector space bases for the mod `p` Steenrod
    algebra: the Milnor basis and the Serre-Cartan basis. When `p=2`,
    there are also several other, less well-known, bases. See the
    documentation for this module (type
    ``sage.algebras.steenrod.steenrod_algebra?``) and the function
    :func:`steenrod_algebra_basis
    <sage.algebras.steenrod.steenrod_algebra_bases.steenrod_algebra_basis_>`
    for full descriptions of each of the implemented bases.

    This module implements the following bases at all primes:

    - \'milnor\': Milnor basis.

    - \'serre-cartan\' or \'adem\' or \'admissible\': Serre-Cartan basis.

    - \'pst\', \'pst_rlex\', \'pst_llex\', \'pst_deg\', \'pst_revz\': various
      `P^s_t`-bases.

    - \'comm\', \'comm_rlex\', \'comm_llex\', \'comm_deg\', \'comm_revz\', or
      these with \'_long\' appended: various commutator bases.

    It implements the following bases when `p=2`:

    - \'wood_y\': Wood\'s Y basis.

    - \'wood_z\': Wood\'s Z basis.

    - \'wall\', \'wall_long\': Wall\'s basis.

    - \'arnon_a\', \'arnon_a_long\': Arnon\'s A basis.

    - \'arnon_c\': Arnon\'s C basis.

    When defining a Steenrod algebra, you can specify a basis. Then
    elements of that Steenrod algebra are printed in that basis::

        sage: adem = SteenrodAlgebra(2, \'adem\')
        sage: x = adem.Sq(2,1)  # Sq(-) always means a Milnor basis element
        sage: x
        Sq^4 Sq^1 + Sq^5
        sage: y = Sq(0,1)    # unadorned Sq defines elements w.r.t. Milnor basis
        sage: y
        Sq(0,1)
        sage: adem(y)
        Sq^2 Sq^1 + Sq^3
        sage: adem5 = SteenrodAlgebra(5, \'serre-cartan\')
        sage: adem5.P(0,2)
        P^10 P^2 + 4 P^11 P^1 + P^12

    If you add or multiply elements defined using different bases, the
    left-hand factor determines the form of the output::

        sage: SteenrodAlgebra(basis=\'adem\').Sq(3) + SteenrodAlgebra(basis=\'pst\').Sq(0,1)
        Sq^2 Sq^1
        sage: SteenrodAlgebra(basis=\'pst\').Sq(3) + SteenrodAlgebra(basis=\'milnor\').Sq(0,1)
        P^0_1 P^1_1 + P^0_2
        sage: SteenrodAlgebra(basis=\'milnor\').Sq(2) * SteenrodAlgebra(basis=\'arnonc\').Sq(2)
        Sq(1,1)

    You can get a list of basis elements in a given dimension::

        sage: A3 = SteenrodAlgebra(3, \'milnor\')
        sage: A3.basis(13)
        Family (Q_1 P(2), Q_0 P(3))

    Algebras defined over different bases are not equal::

        sage: SteenrodAlgebra(basis=\'milnor\') == SteenrodAlgebra(basis=\'pst\')
        False

    Bases have various synonyms, and in general Sage tries to figure
    out what basis you meant::

        sage: SteenrodAlgebra(basis=\'MiLNOr\')
        mod 2 Steenrod algebra, milnor basis
        sage: SteenrodAlgebra(basis=\'MiLNOr\') == SteenrodAlgebra(basis=\'milnor\')
        True
        sage: SteenrodAlgebra(basis=\'adem\')
        mod 2 Steenrod algebra, serre-cartan basis
        sage: SteenrodAlgebra(basis=\'adem\').basis_name()
        \'serre-cartan\'
        sage: SteenrodAlgebra(basis=\'wood---z---\').basis_name()
        \'woodz\'

    As noted above, several of the bases (\'arnon_a\', \'wall\', \'comm\')
    have alternate, sometimes longer, representations. These provide
    ways of expressing elements of the Steenrod algebra in terms of
    the `\\text{Sq}^{2^n}`.

    ::

        sage: A_long = SteenrodAlgebra(2, \'arnon_a_long\')
        sage: A_long(Sq(6))
        Sq^1 Sq^2 Sq^1 Sq^2 + Sq^2 Sq^4
        sage: SteenrodAlgebra(2, \'wall_long\')(Sq(6))
        Sq^2 Sq^1 Sq^2 Sq^1 + Sq^2 Sq^4
        sage: SteenrodAlgebra(2, \'comm_deg_long\')(Sq(6))
        s_1 s_2 s_12 + s_2 s_4

    .. rubric:: Sub-Hopf algebras of the Steenrod algebra:

    These are specified using the argument ``profile``, along with,
    optionally, ``truncation_type`` and ``precision``.  The
    ``profile`` argument specifies the profile function for this
    algebra.  Any sub-Hopf algebra of the Steenrod algebra is
    determined by its *profile function*.  When `p=2`, this is a map `e`
    from the positive integers to the set of nonnegative integers,
    plus `\\infty`, corresponding to the sub-Hopf algebra dual to this
    quotient of the dual Steenrod algebra:

    .. MATH::

        \\GF{2} [\\xi_1, \\xi_2, \\xi_3, ...] / (\\xi_1^{2^{e(1)}}, \\xi_2^{2^{e(2)}}, \\xi_3^{2^{e(3)}}, ...).

    The profile function `e` must satisfy the condition

    - `e(r) \\geq \\min( e(r-i) - i, e(i))` for all `0 < i < r`.

    This is specified via ``profile``, and optionally ``precision``
    and ``truncation_type``.  First, ``profile`` must have one of the
    following forms:

    - a list or tuple, e.g., ``[3,2,1]``, corresponding to the
      function sending 1 to 3, 2 to 2, 3 to 1, and all other integers
      to the value of ``truncation_type``.
    - a function from positive integers to nonnegative integers (and
      `\\infty`), e.g., ``lambda n: n+2``.
    - ``None`` or ``Infinity`` -- use this for the profile function for
      the whole Steenrod algebra

    In the first and third cases, ``precision`` is ignored.  In the
    second case, this function is converted to a tuple of length one
    less than ``precision``, which has default value 100.  The
    function is truncated at this point, and all remaining values are
    set to the value of ``truncation_type``.

    ``truncation_type`` may be 0, `\\infty`, or \'auto\'.  If it\'s
    \'auto\', then it gets converted to 0 in the first case above (when
    ``profile`` is a list), and otherwise (when ``profile`` is a
    function, ``None``, or ``Infinity``) it gets converted to `\\infty`.

    For example, the sub-Hopf algebra `A(2)` has profile function
    ``[3,2,1,0,0,0,...]``, so it can be defined by any of the
    following::

        sage: A2 = SteenrodAlgebra(profile=[3,2,1])
        sage: B2 = SteenrodAlgebra(profile=[3,2,1,0,0]) # trailing 0s ignored
        sage: A2 == B2
        True
        sage: C2 = SteenrodAlgebra(profile=lambda n: max(4-n, 0), truncation_type=0)
        sage: A2 == C2
        True

    In the following case, the profile function is specified by a
    function and ``truncation_type`` isn\'t specified, so it defaults
    to `\\infty`; therefore this gives a different sub-Hopf algebra::

        sage: D2 = SteenrodAlgebra(profile=lambda n: max(4-n, 0))
        sage: A2 == D2
        False
        sage: D2.is_finite()
        False
        sage: E2 = SteenrodAlgebra(profile=lambda n: max(4-n, 0), truncation_type=Infinity)
        sage: D2 == E2
        True

    The argument ``precision`` only needs to be specified if the
    profile function is defined by a function and you want to control
    when the profile switches from the given function to the
    truncation type.  For example::

        sage: D3 = SteenrodAlgebra(profile=lambda n: n, precision=3)
        sage: D3
        sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [1, 2, +Infinity, +Infinity, +Infinity, ...]
        sage: D4 = SteenrodAlgebra(profile=lambda n: n, precision=4); D4
        sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [1, 2, 3, +Infinity, +Infinity, +Infinity, ...]
        sage: D3 == D4
        False

    When `p` is odd, ``profile`` is a pair of functions `e` and `k`,
    corresponding to the quotient

    .. MATH::

        \\GF{p} [\\xi_1, \\xi_2, \\xi_3, ...] \\otimes \\Lambda (\\tau_0,
        \\tau_1, ...) / (\\xi_1^{p^{e_1}}, \\xi_2^{p^{e_2}}, ...;
        \\tau_0^{k_0}, \\tau_1^{k_1}, ...).

    Together, the functions `e` and `k` must satisfy the conditions

    - `e(r) \\geq \\min( e(r-i) - i, e(i))` for all `0 < i < r`,

    - if `k(i+j) = 1`, then either `e(i) \\leq j` or `k(j) = 1` for all `i
      \\geq 1`, `j \\geq 0`.

    Therefore ``profile`` must have one of the following forms:

    - a pair of lists or tuples, the second of which takes values in
      the set `\\{1,2\\}`, e.g., ``([3,2,1,1], [1,1,2,2,1])``.

    - a pair of functions, one from the positive integers to
      nonnegative integers (and `\\infty`), one from the nonnegative
      integers to the set `\\{1,2\\}`, e.g., ``(lambda n: n+2, lambda n:
      1 if n<3 else 2)``.

    - ``None`` or ``Infinity`` -- use this for the profile function for
      the whole Steenrod algebra

    You can also mix and match the first two, passing a pair with
    first entry a list and second entry a function, for instance.  The
    values of ``precision`` and ``truncation_type`` are determined by
    the first entry.

    More examples::

        sage: E = SteenrodAlgebra(profile=lambda n: 0 if n<3 else 3, truncation_type=0)
        sage: E.is_commutative()
        True

        sage: A2 = SteenrodAlgebra(profile=[3,2,1]) # the algebra A(2)
        sage: Sq(7,3,1) in A2
        True
        sage: Sq(8) in A2
        False
        sage: Sq(8) in SteenrodAlgebra().basis(8)
        True
        sage: Sq(8) in A2.basis(8)
        False
        sage: A2.basis(8)
        Family (Sq(1,0,1), Sq(2,2), Sq(5,1))

        sage: A5 = SteenrodAlgebra(p=5)
        sage: A51 = SteenrodAlgebra(p=5, profile=([1], [2,2]))
        sage: A5.Q(0,1) * A5.P(4) in A51
        True
        sage: A5.Q(2) in A51
        False
        sage: A5.P(5) in A51
        False

    For sub-Hopf algebras of the Steenrod algebra, only the Milnor
    basis or the various `P^s_t`-bases may be used. ::

        sage: SteenrodAlgebra(profile=[1,2,1,1], basis=\'adem\')
        Traceback (most recent call last):
        ...
        NotImplementedError: for sub-Hopf algebras of the Steenrod algebra, only the Milnor basis and the pst bases are implemented

    .. rubric:: The generic Steenrod algebra at the prime `2`:

    The structure formulas for the Steenrod algebra at odd primes `p` also make sense
    when `p` is set to `2`. We refer to the resulting algebra as the "generic Steenrod algebra" for
    the prime `2`. The dual Hopf algebra is given by

        .. MATH::

            A_* = \\GF{2} [\\xi_1, \\xi_2, \\xi_3, ...] \\otimes \\Lambda (\\tau_0, \\tau_1, ...)

    The degree of `\\xi_k` is `2^{k+1}-2` and the degree of `\\tau_k` is `2^{k+1}-1`.

    The generic Steenrod algebra is an associated graded algebra of the usual Steenrod algebra
    that is occasionally useful. Its cohomology, for example, is the `E_2`-term of a spectral sequence
    that computes the `E_2`-term of the Novikov spectral sequence. It can also be obtained as a
    specialisation of Voevodsky\'s "motivic Steenrod algebra": in the notation of [Voe2003]_, Remark 12.12,
    it corresponds to setting `\\rho = \\tau = 0`. The usual Steenrod algebra is given by `\\rho = 0`
    and `\\tau = 1`.

    In Sage this algebra is constructed using the \'generic\' keyword.

    Example::

        sage: EA = SteenrodAlgebra(p=2,generic=True) ; EA
        generic mod 2 Steenrod algebra, milnor basis
        sage: EA[8]
        Vector space spanned by (Q_0 Q_2, Q_0 Q_1 P(2), P(1,1), P(4))
         over Finite Field of size 2

    TESTS:

    Testing unique parents::

        sage: S0 = SteenrodAlgebra(2)
        sage: S1 = SteenrodAlgebra(2)
        sage: S0 is S1
        True
        sage: S2 = SteenrodAlgebra(2, basis=\'adem\')
        sage: S0 is S2
        False
        sage: S0 == S2
        False
        sage: A1 = SteenrodAlgebra(profile=[2,1])
        sage: B1 = SteenrodAlgebra(profile=[2,1,0,0])
        sage: A1 is B1
        True
    '''
def AA(n=None, p: int = 2):
    """
    This returns the Steenrod algebra `A` or its sub-Hopf algebra `A(n)`.

    INPUT:

    - ``n`` -- nonnegative integer (default: ``None``)
    - ``p`` -- prime number (default: 2)

    OUTPUT:

    If `n` is ``None``, then return the full Steenrod algebra.
    Otherwise, return `A(n)`.

    When `p=2`, `A(n)` is the sub-Hopf algebra generated by the
    elements `\\text{Sq}^i` for `i \\leq 2^n`.  Its profile function is
    `(n+1, n, n-1, ...)`.  When `p` is odd, `A(n)` is the sub-Hopf
    algebra generated by the elements `Q_0` and `\\mathcal{P}^i` for `i
    \\leq p^{n-1}`.  Its profile function is `e=(n, n-1, n-2, ...)`
    and `k=(2, 2, ..., 2)` (length `n+1`).

    EXAMPLES::

        sage: from sage.algebras.steenrod.steenrod_algebra import AA as A
        sage: A()
        mod 2 Steenrod algebra, milnor basis
        sage: A(2)
        sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis,
         profile function [3, 2, 1]
        sage: A(2, p=5)
        sub-Hopf algebra of mod 5 Steenrod algebra, milnor basis,
         profile function ([2, 1], [2, 2, 2])
    """
def Sq(*nums):
    """
    Milnor element Sq(a,b,c,...).

    INPUT:

    - ``a``, ``b``, ``c``, ... -- nonnegative integers

    OUTPUT: element of the Steenrod algebra

    This returns the Milnor basis element `\\text{Sq}(a, b, c, ...)`.

    EXAMPLES::

        sage: Sq(5)
        Sq(5)
        sage: Sq(5) + Sq(2,1) + Sq(5)  # addition is mod 2:
        Sq(2,1)
        sage: (Sq(4,3) + Sq(7,2)).degree()
        13

    Entries must be nonnegative integers; otherwise, an error
    results.

    This function is a good way to define elements of the Steenrod
    algebra.
    """
