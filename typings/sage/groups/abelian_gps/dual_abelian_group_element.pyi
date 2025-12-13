from sage.groups.abelian_gps.element_base import AbelianGroupElementBase as AbelianGroupElementBase

def is_DualAbelianGroupElement(x) -> bool:
    '''
    Test whether ``x`` is a dual Abelian group element.

    INPUT:

    - ``x`` -- anything

    OUTPUT: boolean

    EXAMPLES::

        sage: from sage.groups.abelian_gps.dual_abelian_group import is_DualAbelianGroupElement
        sage: F = AbelianGroup(5, [5,5,7,8,9], names=list("abcde")).dual_group()
        sage: is_DualAbelianGroupElement(F)
        doctest:warning...
        DeprecationWarning: The function is_DualAbelianGroupElement is deprecated;
        use \'isinstance(..., DualAbelianGroupElement)\' instead.
        See https://github.com/sagemath/sage/issues/38184 for details.
        False
        sage: is_DualAbelianGroupElement(F.an_element())
        True
    '''

class DualAbelianGroupElement(AbelianGroupElementBase):
    """
    Base class for abelian group elements
    """
    def __call__(self, g):
        """
        Evaluate ``self`` on a group element ``g``.

        OUTPUT: an element in
        :meth:`~sage.groups.abelian_gps.dual_abelian_group.DualAbelianGroup_class.base_ring`

        EXAMPLES::

            sage: F = AbelianGroup(5, [2,3,5,7,8], names='abcde')
            sage: a,b,c,d,e = F.gens()
            sage: Fd = F.dual_group(names='ABCDE')
            sage: A,B,C,D,E = Fd.gens()
            sage: A*B^2*D^7
            A*B^2
            sage: A(a)
            -1
            sage: B(b)
            zeta840^140 - 1
            sage: CC(B(b))    # abs tol 1e-8
            -0.499999999999995 + 0.866025403784447*I
            sage: A(a*b)
            -1

        TESTS::

            sage: F = AbelianGroup(1, [7], names='a')
            sage: a, = F.gens()
            sage: Fd = F.dual_group(names='A', base_ring=GF(29))
            sage: A, = Fd.gens()
            sage: A(a)                                                                  # needs sage.libs.pari
            16
        """
    def word_problem(self, words):
        '''
        This is a rather hackish method and is included for completeness.

        The word problem for an instance of DualAbelianGroup as it can
        for an AbelianGroup. The reason why is that word problem
        for an instance of AbelianGroup simply calls GAP (which
        has abelian groups implemented) and invokes "EpimorphismFromFreeGroup"
        and "PreImagesRepresentative". GAP does not have duals of
        abelian groups implemented. So, by using the same name
        for the generators, the method below converts the problem for
        the dual group to the corresponding problem on the group
        itself and uses GAP to solve that.

        EXAMPLES::

            sage: G = AbelianGroup(5,[3, 5, 5, 7, 8], names=\'abcde\')
            sage: Gd = G.dual_group(names=\'abcde\')
            sage: a,b,c,d,e = Gd.gens()
            sage: u = a^3*b*c*d^2*e^5
            sage: v = a^2*b*c^2*d^3*e^3
            sage: w = a^7*b^3*c^5*d^4*e^4
            sage: x = a^3*b^2*c^2*d^3*e^5
            sage: y = a^2*b^4*c^2*d^4*e^5
            sage: e.word_problem([u,v,w,x,y])                                           # needs sage.libs.gap
            [[b^2*c^2*d^3*e^5, 245]]
        '''
