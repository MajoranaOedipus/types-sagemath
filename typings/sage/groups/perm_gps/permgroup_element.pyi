import _cython_3_2_1
import sage as sage
import sage.structure.element
from sage.categories.category import ZZ as ZZ
from sage.interfaces.abc import GpElement as GpElement
from sage.libs.gap.libgap import libgap as libgap
from sage.rings.integer import Integer as Integer
from sage.rings.polynomial.multi_polynomial import MPolynomial as MPolynomial
from sage.rings.polynomial.polynomial_element import Polynomial as Polynomial
from sage.sets.finite_enumerated_set import FiniteEnumeratedSet as FiniteEnumeratedSet
from sage.structure.element import Matrix as Matrix, have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

is_PermutationGroupElement: _cython_3_2_1.cython_function_or_method
make_permgroup_element: _cython_3_2_1.cython_function_or_method
make_permgroup_element_v2: _cython_3_2_1.cython_function_or_method

class PermutationGroupElement(sage.structure.element.MultiplicativeGroupElement):
    '''PermutationGroupElement(g, parent, check=True)

    File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 227)

    An element of a permutation group.

    EXAMPLES::

        sage: G = PermutationGroup([\'(1,2,3)(4,5)\']); G
        Permutation Group with generators [(1,2,3)(4,5)]
        sage: g = G.random_element()
        sage: g in G
        True
        sage: g = G.gen(0); g
        (1,2,3)(4,5)
        sage: print(g)
        (1,2,3)(4,5)
        sage: g*g
        (1,3,2)
        sage: g**(-1)
        (1,3,2)(4,5)
        sage: g**2
        (1,3,2)
        sage: G = PermutationGroup([(1,2,3)])
        sage: g = G.gen(0); g
        (1,2,3)
        sage: g.order()
        3

    This example illustrates how permutations act on multivariate
    polynomials.

    ::

        sage: R = PolynomialRing(RationalField(), 5, ["x","y","z","u","v"])
        sage: x, y, z, u, v = R.gens()
        sage: f = x**2 - y**2 + 3*z**2
        sage: G = PermutationGroup([\'(1,2,3)(4,5)\', \'(1,2,3,4,5)\'])
        sage: sigma = G.gen(0)
        sage: f * sigma
        3*x^2 + y^2 - z^2'''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, g, parent, check=...) -> Any:
        '''File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 271)

                Create element of a permutation group.

                There are several ways to define a permutation group element:

                -  Define a permutation group `G`, then use
                   ``G.gens()`` and multiplication ``*`` to construct
                   elements.

                -  Define a permutation group `G`, then use, e.g.,
                   ``G([(1,2),(3,4,5)])`` to construct an element of the
                   group. You could also use ``G(\'(1,2)(3,4,5)\')``

                -  Use, e.g., ``PermutationGroupElement([(1,2),(3,4,5)])`` or
                   ``PermutationGroupElement(\'(1,2)(3,4,5)\')`` to make a
                   permutation group element with parent `S_5`.

                INPUT:

                - ``g`` -- defines element

                - ``parent`` -- defines parent group (``g`` must be in
                  parent if specified, or a :exc:`TypeError` is raised)

                - ``check`` -- boolean (default: ``True``); if ``False`` assumes ``g``
                  is a gap element in parent (if specified)

                EXAMPLES:

                We illustrate construction of permutation using several
                different methods.

                First we construct elements by multiplying together generators for
                a group.

                ::

                    sage: G = PermutationGroup([\'(1,2)(3,4)\', \'(3,4,5,6)\'], canonicalize=False)
                    sage: s = G.gens()
                    sage: s[0]
                    (1,2)(3,4)
                    sage: s[1]
                    (3,4,5,6)
                    sage: s[0]*s[1]
                    (1,2)(3,5,6)
                    sage: (s[0]*s[1]).parent()
                    Permutation Group with generators [(1,2)(3,4), (3,4,5,6)]

                Next we illustrate creation of a permutation using coercion into an
                already-created group.

                ::

                    sage: g = G([(1,2),(3,5,6)]); g
                    (1,2)(3,5,6)
                    sage: g.parent()
                    Permutation Group with generators [(1,2)(3,4), (3,4,5,6)]
                    sage: g == s[0]*s[1]
                    True

                We can also use a string instead of a list to specify the
                permutation.

                ::

                    sage: h = G(\'(1,2)(3,5,6)\')
                    sage: g == h
                    True

                We can also make a permutation group element directly using the
                :class:`PermutationGroupElement` command. Note that the
                parent is then the full symmetric group `S_n`, where
                `n` is the largest integer that is moved by the
                permutation.

                ::

                    sage: k = PermutationGroupElement(\'(1,2)(3,5,6)\'); k
                    (1,2)(3,5,6)
                    sage: k.parent()
                    Symmetric group of order 6! as a permutation group

                Note the comparison of permutations doesn\'t require that the parent
                groups are the same.

                ::

                    sage: k == g
                    True

                Arithmetic with permutations having different parents is also
                defined::

                    sage: k*g
                    (3,6,5)
                    sage: (k*g).parent()
                    Symmetric group of order 6! as a permutation group

                ::

                    sage: G = PermutationGroup([[(1,2,3),(4,5)],[(3,4)]])
                    sage: loads(dumps(G.0)) == G.0
                    True

                Initialization from gap or pari objects::

                    sage: S = SymmetricGroup(5)
                    sage: S(Permutation([5,1,4,3,2]))
                    (1,5,2)(3,4)
                    sage: S(gp.Vecsmall([5,1,4,3,2]))                                           # needs sage.libs.pari
                    (1,5,2)(3,4)
                    sage: S(gap.PermList([5,1,4,3,2]))
                    (1,5,2)(3,4)
                    sage: S(pari.Vecsmall([5,1,4,3,2]))                                         # needs sage.libs.pari
                    (1,5,2)(3,4)
                    sage: S(libgap.PermList([5,1,4,3,2]))
                    (1,5,2)(3,4)
                    sage: S(libgap([3,1,4,2,5]))
                    (1,3,4,2)
                    sage: S(libgap("(1,2,4)(3,5)"))
                    (1,2,4)(3,5)

                Note that the conversion from gap permutations is agnostic to domains::

                    sage: S = SymmetricGroup([\'a\', \'b\', \'c\'])
                    sage: S(libgap.eval("(1,3)"))
                    (\'a\',\'c\')
                    sage: S(gap("(1,3)"))
                    (\'a\',\'c\')

                Though not for gap list or string::

                    sage: S(libgap([1, 3, 2]))
                    Traceback (most recent call last):
                    ...
                    KeyError: 1
                    sage: S(libgap([\'a\', \'c\', \'b\']))
                    (\'b\',\'c\')

                    sage: S(libgap("(1,2)"))
                    Traceback (most recent call last):
                    ...
                    KeyError: 1
                    sage: S(libgap("(\'a\',\'c\')"))
                    (\'a\',\'c\')

                EXAMPLES::

                    sage: k = PermutationGroupElement(\'(1,2)(3,5,6)\')
                    sage: k._gap_()
                    (1,2)(3,5,6)
                    sage: k._gap_().parent()
                    C library interface to GAP

                List notation::

                    sage: PermutationGroupElement([1,2,4,3,5])
                    (3,4)

                TESTS::

                    sage: PermutationGroupElement(())
                    ()
                    sage: PermutationGroupElement([()])
                    ()

                We check that :issue:`16678` is fixed::

                    sage: Permutations.options.display=\'cycle\'
                    sage: p = Permutation((1,2))
                    sage: PermutationGroupElement(p)
                    (1,2)

                Bad input::

                    sage: S5 = SymmetricGroup(5)
                    sage: S5((3,-1,5))
                    Traceback (most recent call last):
                    ...
                    ValueError: invalid list of cycles to initialize a permutation
                    sage: S5((1,2,6,3))
                    Traceback (most recent call last):
                    ...
                    ValueError: invalid list of cycles to initialize a permutation

                    sage: P = PermutationGroup([\'(1,2,3)\'])
                    sage: P(\'(1,2)\')
                    Traceback (most recent call last):
                    ...
                    ValueError: permutation (1,2) not in Permutation Group with generators [(1,2,3)]
        '''
    @overload
    def cycle_string(self, singletons=...) -> Any:
        """PermutationGroupElement.cycle_string(self, singletons=False)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1862)

        Return string representation of this permutation.

        EXAMPLES::

            sage: g = PermutationGroupElement([(1,2,3),(4,5)])
            sage: g.cycle_string()
            '(1,2,3)(4,5)'

            sage: g = PermutationGroupElement([3,2,1])
            sage: g.cycle_string(singletons=True)
            '(1,3)(2)'"""
    @overload
    def cycle_string(self) -> Any:
        """PermutationGroupElement.cycle_string(self, singletons=False)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1862)

        Return string representation of this permutation.

        EXAMPLES::

            sage: g = PermutationGroupElement([(1,2,3),(4,5)])
            sage: g.cycle_string()
            '(1,2,3)(4,5)'

            sage: g = PermutationGroupElement([3,2,1])
            sage: g.cycle_string(singletons=True)
            '(1,3)(2)'"""
    @overload
    def cycle_string(self, singletons=...) -> Any:
        """PermutationGroupElement.cycle_string(self, singletons=False)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1862)

        Return string representation of this permutation.

        EXAMPLES::

            sage: g = PermutationGroupElement([(1,2,3),(4,5)])
            sage: g.cycle_string()
            '(1,2,3)(4,5)'

            sage: g = PermutationGroupElement([3,2,1])
            sage: g.cycle_string(singletons=True)
            '(1,3)(2)'"""
    @overload
    def cycle_tuples(self, singletons=...) -> Any:
        """PermutationGroupElement.cycle_tuples(self, singletons=False)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1803)

        Return ``self`` as a list of disjoint cycles, represented as tuples
        rather than permutation group elements.

        INPUT:

        - ``singletons`` -- boolean (default: ``False``); whether or not consider the
          cycle that correspond to fixed point

        EXAMPLES::

            sage: p = PermutationGroupElement('(2,6)(4,5,1)')
            sage: p.cycle_tuples()
            [(1, 4, 5), (2, 6)]
            sage: p.cycle_tuples(singletons=True)
            [(1, 4, 5), (2, 6), (3,)]

        EXAMPLES::

            sage: S = SymmetricGroup(4)
            sage: S.gen(0).cycle_tuples()
            [(1, 2, 3, 4)]

        ::

            sage: S = SymmetricGroup(['a','b','c','d'])
            sage: S.gen(0).cycle_tuples()
            [('a', 'b', 'c', 'd')]
            sage: S([('a', 'b'), ('c', 'd')]).cycle_tuples()
            [('a', 'b'), ('c', 'd')]"""
    @overload
    def cycle_tuples(self) -> Any:
        """PermutationGroupElement.cycle_tuples(self, singletons=False)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1803)

        Return ``self`` as a list of disjoint cycles, represented as tuples
        rather than permutation group elements.

        INPUT:

        - ``singletons`` -- boolean (default: ``False``); whether or not consider the
          cycle that correspond to fixed point

        EXAMPLES::

            sage: p = PermutationGroupElement('(2,6)(4,5,1)')
            sage: p.cycle_tuples()
            [(1, 4, 5), (2, 6)]
            sage: p.cycle_tuples(singletons=True)
            [(1, 4, 5), (2, 6), (3,)]

        EXAMPLES::

            sage: S = SymmetricGroup(4)
            sage: S.gen(0).cycle_tuples()
            [(1, 2, 3, 4)]

        ::

            sage: S = SymmetricGroup(['a','b','c','d'])
            sage: S.gen(0).cycle_tuples()
            [('a', 'b', 'c', 'd')]
            sage: S([('a', 'b'), ('c', 'd')]).cycle_tuples()
            [('a', 'b'), ('c', 'd')]"""
    @overload
    def cycle_tuples(self, singletons=...) -> Any:
        """PermutationGroupElement.cycle_tuples(self, singletons=False)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1803)

        Return ``self`` as a list of disjoint cycles, represented as tuples
        rather than permutation group elements.

        INPUT:

        - ``singletons`` -- boolean (default: ``False``); whether or not consider the
          cycle that correspond to fixed point

        EXAMPLES::

            sage: p = PermutationGroupElement('(2,6)(4,5,1)')
            sage: p.cycle_tuples()
            [(1, 4, 5), (2, 6)]
            sage: p.cycle_tuples(singletons=True)
            [(1, 4, 5), (2, 6), (3,)]

        EXAMPLES::

            sage: S = SymmetricGroup(4)
            sage: S.gen(0).cycle_tuples()
            [(1, 2, 3, 4)]

        ::

            sage: S = SymmetricGroup(['a','b','c','d'])
            sage: S.gen(0).cycle_tuples()
            [('a', 'b', 'c', 'd')]
            sage: S([('a', 'b'), ('c', 'd')]).cycle_tuples()
            [('a', 'b'), ('c', 'd')]"""
    @overload
    def cycle_tuples(self) -> Any:
        """PermutationGroupElement.cycle_tuples(self, singletons=False)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1803)

        Return ``self`` as a list of disjoint cycles, represented as tuples
        rather than permutation group elements.

        INPUT:

        - ``singletons`` -- boolean (default: ``False``); whether or not consider the
          cycle that correspond to fixed point

        EXAMPLES::

            sage: p = PermutationGroupElement('(2,6)(4,5,1)')
            sage: p.cycle_tuples()
            [(1, 4, 5), (2, 6)]
            sage: p.cycle_tuples(singletons=True)
            [(1, 4, 5), (2, 6), (3,)]

        EXAMPLES::

            sage: S = SymmetricGroup(4)
            sage: S.gen(0).cycle_tuples()
            [(1, 2, 3, 4)]

        ::

            sage: S = SymmetricGroup(['a','b','c','d'])
            sage: S.gen(0).cycle_tuples()
            [('a', 'b', 'c', 'd')]
            sage: S([('a', 'b'), ('c', 'd')]).cycle_tuples()
            [('a', 'b'), ('c', 'd')]"""
    @overload
    def cycle_tuples(self) -> Any:
        """PermutationGroupElement.cycle_tuples(self, singletons=False)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1803)

        Return ``self`` as a list of disjoint cycles, represented as tuples
        rather than permutation group elements.

        INPUT:

        - ``singletons`` -- boolean (default: ``False``); whether or not consider the
          cycle that correspond to fixed point

        EXAMPLES::

            sage: p = PermutationGroupElement('(2,6)(4,5,1)')
            sage: p.cycle_tuples()
            [(1, 4, 5), (2, 6)]
            sage: p.cycle_tuples(singletons=True)
            [(1, 4, 5), (2, 6), (3,)]

        EXAMPLES::

            sage: S = SymmetricGroup(4)
            sage: S.gen(0).cycle_tuples()
            [(1, 2, 3, 4)]

        ::

            sage: S = SymmetricGroup(['a','b','c','d'])
            sage: S.gen(0).cycle_tuples()
            [('a', 'b', 'c', 'd')]
            sage: S([('a', 'b'), ('c', 'd')]).cycle_tuples()
            [('a', 'b'), ('c', 'd')]"""
    @overload
    def cycle_tuples(self) -> Any:
        """PermutationGroupElement.cycle_tuples(self, singletons=False)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1803)

        Return ``self`` as a list of disjoint cycles, represented as tuples
        rather than permutation group elements.

        INPUT:

        - ``singletons`` -- boolean (default: ``False``); whether or not consider the
          cycle that correspond to fixed point

        EXAMPLES::

            sage: p = PermutationGroupElement('(2,6)(4,5,1)')
            sage: p.cycle_tuples()
            [(1, 4, 5), (2, 6)]
            sage: p.cycle_tuples(singletons=True)
            [(1, 4, 5), (2, 6), (3,)]

        EXAMPLES::

            sage: S = SymmetricGroup(4)
            sage: S.gen(0).cycle_tuples()
            [(1, 2, 3, 4)]

        ::

            sage: S = SymmetricGroup(['a','b','c','d'])
            sage: S.gen(0).cycle_tuples()
            [('a', 'b', 'c', 'd')]
            sage: S([('a', 'b'), ('c', 'd')]).cycle_tuples()
            [('a', 'b'), ('c', 'd')]"""
    @overload
    def cycle_type(self, singletons=..., as_list=...) -> Any:
        """PermutationGroupElement.cycle_type(self, singletons=True, as_list=False)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1882)

        Return the partition that gives the cycle type of ``self`` as an element of
        its parent.

        INPUT:

        - ``g`` -- an element of the permutation group ``self.parent()``

        - ``singletons`` -- boolean depending on whether or not
          trivial cycles should be counted (default: ``True``)

        - ``as_list`` -- boolean depending on whether the cycle
          type should be returned as a :class:`list` or as a :class:`Partition`
          (default: ``False``)

        OUTPUT: a :class:`Partition`, or :class:`list` if ``is_list`` is
        ``True``, giving the cycle type of ``self``

        If speed is a concern, then ``as_list=True`` should be used.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: G = DihedralGroup(3)
            sage: [g.cycle_type() for g in G]
            [[1, 1, 1], [3], [3], [2, 1], [2, 1], [2, 1]]
            sage: PermutationGroupElement('(1,2,3)(4,5)(6,7,8)').cycle_type()
            [3, 3, 2]
            sage: G = SymmetricGroup(3); G('(1,2)').cycle_type()
            [2, 1]
            sage: G = SymmetricGroup(4); G('(1,2)').cycle_type()
            [2, 1, 1]
            sage: G = SymmetricGroup(4); G('(1,2)').cycle_type(singletons=False)
            [2]
            sage: G = SymmetricGroup(4); G('(1,2)').cycle_type(as_list=False)
            [2, 1, 1]"""
    @overload
    def cycle_type(self) -> Any:
        """PermutationGroupElement.cycle_type(self, singletons=True, as_list=False)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1882)

        Return the partition that gives the cycle type of ``self`` as an element of
        its parent.

        INPUT:

        - ``g`` -- an element of the permutation group ``self.parent()``

        - ``singletons`` -- boolean depending on whether or not
          trivial cycles should be counted (default: ``True``)

        - ``as_list`` -- boolean depending on whether the cycle
          type should be returned as a :class:`list` or as a :class:`Partition`
          (default: ``False``)

        OUTPUT: a :class:`Partition`, or :class:`list` if ``is_list`` is
        ``True``, giving the cycle type of ``self``

        If speed is a concern, then ``as_list=True`` should be used.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: G = DihedralGroup(3)
            sage: [g.cycle_type() for g in G]
            [[1, 1, 1], [3], [3], [2, 1], [2, 1], [2, 1]]
            sage: PermutationGroupElement('(1,2,3)(4,5)(6,7,8)').cycle_type()
            [3, 3, 2]
            sage: G = SymmetricGroup(3); G('(1,2)').cycle_type()
            [2, 1]
            sage: G = SymmetricGroup(4); G('(1,2)').cycle_type()
            [2, 1, 1]
            sage: G = SymmetricGroup(4); G('(1,2)').cycle_type(singletons=False)
            [2]
            sage: G = SymmetricGroup(4); G('(1,2)').cycle_type(as_list=False)
            [2, 1, 1]"""
    @overload
    def cycle_type(self) -> Any:
        """PermutationGroupElement.cycle_type(self, singletons=True, as_list=False)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1882)

        Return the partition that gives the cycle type of ``self`` as an element of
        its parent.

        INPUT:

        - ``g`` -- an element of the permutation group ``self.parent()``

        - ``singletons`` -- boolean depending on whether or not
          trivial cycles should be counted (default: ``True``)

        - ``as_list`` -- boolean depending on whether the cycle
          type should be returned as a :class:`list` or as a :class:`Partition`
          (default: ``False``)

        OUTPUT: a :class:`Partition`, or :class:`list` if ``is_list`` is
        ``True``, giving the cycle type of ``self``

        If speed is a concern, then ``as_list=True`` should be used.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: G = DihedralGroup(3)
            sage: [g.cycle_type() for g in G]
            [[1, 1, 1], [3], [3], [2, 1], [2, 1], [2, 1]]
            sage: PermutationGroupElement('(1,2,3)(4,5)(6,7,8)').cycle_type()
            [3, 3, 2]
            sage: G = SymmetricGroup(3); G('(1,2)').cycle_type()
            [2, 1]
            sage: G = SymmetricGroup(4); G('(1,2)').cycle_type()
            [2, 1, 1]
            sage: G = SymmetricGroup(4); G('(1,2)').cycle_type(singletons=False)
            [2]
            sage: G = SymmetricGroup(4); G('(1,2)').cycle_type(as_list=False)
            [2, 1, 1]"""
    @overload
    def cycle_type(self) -> Any:
        """PermutationGroupElement.cycle_type(self, singletons=True, as_list=False)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1882)

        Return the partition that gives the cycle type of ``self`` as an element of
        its parent.

        INPUT:

        - ``g`` -- an element of the permutation group ``self.parent()``

        - ``singletons`` -- boolean depending on whether or not
          trivial cycles should be counted (default: ``True``)

        - ``as_list`` -- boolean depending on whether the cycle
          type should be returned as a :class:`list` or as a :class:`Partition`
          (default: ``False``)

        OUTPUT: a :class:`Partition`, or :class:`list` if ``is_list`` is
        ``True``, giving the cycle type of ``self``

        If speed is a concern, then ``as_list=True`` should be used.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: G = DihedralGroup(3)
            sage: [g.cycle_type() for g in G]
            [[1, 1, 1], [3], [3], [2, 1], [2, 1], [2, 1]]
            sage: PermutationGroupElement('(1,2,3)(4,5)(6,7,8)').cycle_type()
            [3, 3, 2]
            sage: G = SymmetricGroup(3); G('(1,2)').cycle_type()
            [2, 1]
            sage: G = SymmetricGroup(4); G('(1,2)').cycle_type()
            [2, 1, 1]
            sage: G = SymmetricGroup(4); G('(1,2)').cycle_type(singletons=False)
            [2]
            sage: G = SymmetricGroup(4); G('(1,2)').cycle_type(as_list=False)
            [2, 1, 1]"""
    @overload
    def cycle_type(self) -> Any:
        """PermutationGroupElement.cycle_type(self, singletons=True, as_list=False)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1882)

        Return the partition that gives the cycle type of ``self`` as an element of
        its parent.

        INPUT:

        - ``g`` -- an element of the permutation group ``self.parent()``

        - ``singletons`` -- boolean depending on whether or not
          trivial cycles should be counted (default: ``True``)

        - ``as_list`` -- boolean depending on whether the cycle
          type should be returned as a :class:`list` or as a :class:`Partition`
          (default: ``False``)

        OUTPUT: a :class:`Partition`, or :class:`list` if ``is_list`` is
        ``True``, giving the cycle type of ``self``

        If speed is a concern, then ``as_list=True`` should be used.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: G = DihedralGroup(3)
            sage: [g.cycle_type() for g in G]
            [[1, 1, 1], [3], [3], [2, 1], [2, 1], [2, 1]]
            sage: PermutationGroupElement('(1,2,3)(4,5)(6,7,8)').cycle_type()
            [3, 3, 2]
            sage: G = SymmetricGroup(3); G('(1,2)').cycle_type()
            [2, 1]
            sage: G = SymmetricGroup(4); G('(1,2)').cycle_type()
            [2, 1, 1]
            sage: G = SymmetricGroup(4); G('(1,2)').cycle_type(singletons=False)
            [2]
            sage: G = SymmetricGroup(4); G('(1,2)').cycle_type(as_list=False)
            [2, 1, 1]"""
    @overload
    def cycle_type(self, singletons=...) -> Any:
        """PermutationGroupElement.cycle_type(self, singletons=True, as_list=False)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1882)

        Return the partition that gives the cycle type of ``self`` as an element of
        its parent.

        INPUT:

        - ``g`` -- an element of the permutation group ``self.parent()``

        - ``singletons`` -- boolean depending on whether or not
          trivial cycles should be counted (default: ``True``)

        - ``as_list`` -- boolean depending on whether the cycle
          type should be returned as a :class:`list` or as a :class:`Partition`
          (default: ``False``)

        OUTPUT: a :class:`Partition`, or :class:`list` if ``is_list`` is
        ``True``, giving the cycle type of ``self``

        If speed is a concern, then ``as_list=True`` should be used.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: G = DihedralGroup(3)
            sage: [g.cycle_type() for g in G]
            [[1, 1, 1], [3], [3], [2, 1], [2, 1], [2, 1]]
            sage: PermutationGroupElement('(1,2,3)(4,5)(6,7,8)').cycle_type()
            [3, 3, 2]
            sage: G = SymmetricGroup(3); G('(1,2)').cycle_type()
            [2, 1]
            sage: G = SymmetricGroup(4); G('(1,2)').cycle_type()
            [2, 1, 1]
            sage: G = SymmetricGroup(4); G('(1,2)').cycle_type(singletons=False)
            [2]
            sage: G = SymmetricGroup(4); G('(1,2)').cycle_type(as_list=False)
            [2, 1, 1]"""
    @overload
    def cycle_type(self, as_list=...) -> Any:
        """PermutationGroupElement.cycle_type(self, singletons=True, as_list=False)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1882)

        Return the partition that gives the cycle type of ``self`` as an element of
        its parent.

        INPUT:

        - ``g`` -- an element of the permutation group ``self.parent()``

        - ``singletons`` -- boolean depending on whether or not
          trivial cycles should be counted (default: ``True``)

        - ``as_list`` -- boolean depending on whether the cycle
          type should be returned as a :class:`list` or as a :class:`Partition`
          (default: ``False``)

        OUTPUT: a :class:`Partition`, or :class:`list` if ``is_list`` is
        ``True``, giving the cycle type of ``self``

        If speed is a concern, then ``as_list=True`` should be used.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: G = DihedralGroup(3)
            sage: [g.cycle_type() for g in G]
            [[1, 1, 1], [3], [3], [2, 1], [2, 1], [2, 1]]
            sage: PermutationGroupElement('(1,2,3)(4,5)(6,7,8)').cycle_type()
            [3, 3, 2]
            sage: G = SymmetricGroup(3); G('(1,2)').cycle_type()
            [2, 1]
            sage: G = SymmetricGroup(4); G('(1,2)').cycle_type()
            [2, 1, 1]
            sage: G = SymmetricGroup(4); G('(1,2)').cycle_type(singletons=False)
            [2]
            sage: G = SymmetricGroup(4); G('(1,2)').cycle_type(as_list=False)
            [2, 1, 1]"""
    @overload
    def cycles(self) -> Any:
        """PermutationGroupElement.cycles(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1768)

        Return ``self`` as a list of disjoint cycles.

        EXAMPLES::

            sage: G = PermutationGroup(['(1,2,3)(4,5,6,7)'])
            sage: g = G.0
            sage: g.cycles()
            [(1,2,3), (4,5,6,7)]
            sage: a, b = g.cycles()
            sage: a(1), b(1)
            (2, 1)"""
    @overload
    def cycles(self) -> Any:
        """PermutationGroupElement.cycles(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1768)

        Return ``self`` as a list of disjoint cycles.

        EXAMPLES::

            sage: G = PermutationGroup(['(1,2,3)(4,5,6,7)'])
            sage: g = G.0
            sage: g.cycles()
            [(1,2,3), (4,5,6,7)]
            sage: a, b = g.cycles()
            sage: a(1), b(1)
            (2, 1)"""
    @overload
    def cycles(self) -> Any:
        """PermutationGroupElement.cycles(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1768)

        Return ``self`` as a list of disjoint cycles.

        EXAMPLES::

            sage: G = PermutationGroup(['(1,2,3)(4,5,6,7)'])
            sage: g = G.0
            sage: g.cycles()
            [(1,2,3), (4,5,6,7)]
            sage: a, b = g.cycles()
            sage: a(1), b(1)
            (2, 1)"""
    @overload
    def dict(self) -> Any:
        """PermutationGroupElement.dict(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1580)

        Return a dictionary associating each element of the domain with its
        image.

        EXAMPLES::

            sage: G = SymmetricGroup(4)
            sage: g = G((1,2,3,4)); g
            (1,2,3,4)
            sage: v = g.dict(); v
            {1: 2, 2: 3, 3: 4, 4: 1}
            sage: type(v[1])
            <... 'int'>
            sage: x = G([2,1]); x
            (1,2)
            sage: x.dict()
            {1: 2, 2: 1, 3: 3, 4: 4}"""
    @overload
    def dict(self) -> Any:
        """PermutationGroupElement.dict(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1580)

        Return a dictionary associating each element of the domain with its
        image.

        EXAMPLES::

            sage: G = SymmetricGroup(4)
            sage: g = G((1,2,3,4)); g
            (1,2,3,4)
            sage: v = g.dict(); v
            {1: 2, 2: 3, 3: 4, 4: 1}
            sage: type(v[1])
            <... 'int'>
            sage: x = G([2,1]); x
            (1,2)
            sage: x.dict()
            {1: 2, 2: 1, 3: 3, 4: 4}"""
    @overload
    def dict(self) -> Any:
        """PermutationGroupElement.dict(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1580)

        Return a dictionary associating each element of the domain with its
        image.

        EXAMPLES::

            sage: G = SymmetricGroup(4)
            sage: g = G((1,2,3,4)); g
            (1,2,3,4)
            sage: v = g.dict(); v
            {1: 2, 2: 3, 3: 4, 4: 1}
            sage: type(v[1])
            <... 'int'>
            sage: x = G([2,1]); x
            (1,2)
            sage: x.dict()
            {1: 2, 2: 1, 3: 3, 4: 4}"""
    @overload
    def domain(self) -> Any:
        """PermutationGroupElement.domain(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1496)

        Return the domain of ``self``.

        EXAMPLES::

            sage: G = SymmetricGroup(4)
            sage: x = G([2,1,4,3]); x
            (1,2)(3,4)
            sage: v = x.domain(); v
            [2, 1, 4, 3]
            sage: type(v[0])
            <... 'int'>
            sage: x = G([2,1]); x
            (1,2)
            sage: x.domain()
            [2, 1, 3, 4]

        TESTS::

            sage: S = SymmetricGroup(0)
            sage: x = S.one(); x
            ()
            sage: x.domain()
            []"""
    @overload
    def domain(self) -> Any:
        """PermutationGroupElement.domain(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1496)

        Return the domain of ``self``.

        EXAMPLES::

            sage: G = SymmetricGroup(4)
            sage: x = G([2,1,4,3]); x
            (1,2)(3,4)
            sage: v = x.domain(); v
            [2, 1, 4, 3]
            sage: type(v[0])
            <... 'int'>
            sage: x = G([2,1]); x
            (1,2)
            sage: x.domain()
            [2, 1, 3, 4]

        TESTS::

            sage: S = SymmetricGroup(0)
            sage: x = S.one(); x
            ()
            sage: x.domain()
            []"""
    @overload
    def domain(self) -> Any:
        """PermutationGroupElement.domain(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1496)

        Return the domain of ``self``.

        EXAMPLES::

            sage: G = SymmetricGroup(4)
            sage: x = G([2,1,4,3]); x
            (1,2)(3,4)
            sage: v = x.domain(); v
            [2, 1, 4, 3]
            sage: type(v[0])
            <... 'int'>
            sage: x = G([2,1]); x
            (1,2)
            sage: x.domain()
            [2, 1, 3, 4]

        TESTS::

            sage: S = SymmetricGroup(0)
            sage: x = S.one(); x
            ()
            sage: x.domain()
            []"""
    @overload
    def domain(self) -> Any:
        """PermutationGroupElement.domain(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1496)

        Return the domain of ``self``.

        EXAMPLES::

            sage: G = SymmetricGroup(4)
            sage: x = G([2,1,4,3]); x
            (1,2)(3,4)
            sage: v = x.domain(); v
            [2, 1, 4, 3]
            sage: type(v[0])
            <... 'int'>
            sage: x = G([2,1]); x
            (1,2)
            sage: x.domain()
            [2, 1, 3, 4]

        TESTS::

            sage: S = SymmetricGroup(0)
            sage: x = S.one(); x
            ()
            sage: x.domain()
            []"""
    @overload
    def gap(self) -> Any:
        """PermutationGroupElement._libgap_(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 850)

        Return ``self`` as a libgap element.

        EXAMPLES::

            sage: S = SymmetricGroup(4)
            sage: p = S('(2,4)')
            sage: p_libgap = libgap(p)
            sage: p_libgap.Order()
            2
            sage: S(p_libgap) == p
            True

            sage: # needs sage.rings.finite_rings
            sage: P = PGU(8,2)
            sage: p, q = P.gens()
            sage: p_libgap  = p.gap()

        TESTS::

            sage: # needs sage.rings.finite_rings
            sage: P = PGU(8,2)
            sage: p, q = P.gens()
            sage: p_pexpect = gap(p)
            sage: p_libgap == p_pexpect
            True
            sage: type(p_libgap) == type(p_pexpect)
            True

        If the permutation element is built from a libgap element, it is cached
        and returned by this function::

            sage: S = SymmetricGroup(4)
            sage: p = libgap.eval('(1,3)')
            sage: libgap(S(p)) is p
            True

        Test the empty permutation::

            sage: p = SymmetricGroup(0).an_element()
            sage: p._libgap_()
            ()

        A minimal test that we handle permutations of degree larger than 2^16 :issue:`39998`::

            sage: SymmetricGroup(2**16+1)((2**16,2**16+1))._libgap_() # long time (100 mb)
            (65536,65537)"""
    @overload
    def gap(self, p) -> Any:
        """PermutationGroupElement._libgap_(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 850)

        Return ``self`` as a libgap element.

        EXAMPLES::

            sage: S = SymmetricGroup(4)
            sage: p = S('(2,4)')
            sage: p_libgap = libgap(p)
            sage: p_libgap.Order()
            2
            sage: S(p_libgap) == p
            True

            sage: # needs sage.rings.finite_rings
            sage: P = PGU(8,2)
            sage: p, q = P.gens()
            sage: p_libgap  = p.gap()

        TESTS::

            sage: # needs sage.rings.finite_rings
            sage: P = PGU(8,2)
            sage: p, q = P.gens()
            sage: p_pexpect = gap(p)
            sage: p_libgap == p_pexpect
            True
            sage: type(p_libgap) == type(p_pexpect)
            True

        If the permutation element is built from a libgap element, it is cached
        and returned by this function::

            sage: S = SymmetricGroup(4)
            sage: p = libgap.eval('(1,3)')
            sage: libgap(S(p)) is p
            True

        Test the empty permutation::

            sage: p = SymmetricGroup(0).an_element()
            sage: p._libgap_()
            ()

        A minimal test that we handle permutations of degree larger than 2^16 :issue:`39998`::

            sage: SymmetricGroup(2**16+1)((2**16,2**16+1))._libgap_() # long time (100 mb)
            (65536,65537)"""
    def has_descent(self, i, side=..., positive=...) -> bool:
        """PermutationGroupElement.has_descent(self, i, side='right', positive=False) -> bool

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1928)

        Return whether ``self`` has a left (resp. right) descent at
        position ``i``. If ``positive`` is ``True``, then test for a non
        descent instead.

        Beware that, since permutations are acting on the right, the
        meaning of descents is the reverse of the usual
        convention. Hence, ``self`` has a left descent at position
        ``i`` if ``self(i) > self(i+1)``.

        INPUT:

        - ``i`` -- an element of the index set
        - ``side`` -- ``'left'`` or ``'right'`` (default: ``'right'``)
        - ``positive`` -- boolean (default: ``False``)

        EXAMPLES::

            sage: S = SymmetricGroup([1,2,3])
            sage: S.one().has_descent(1)
            False
            sage: S.one().has_descent(2)
            False
            sage: s = S.simple_reflections()
            sage: x = s[1]*s[2]
            sage: x.has_descent(1, side='right')
            False
            sage: x.has_descent(2, side='right')
            True
            sage: x.has_descent(1, side='left')
            True
            sage: x.has_descent(2, side='left')
            False
            sage: S._test_has_descent()

        The symmetric group acting on a set not of the form
        `(1,\\dots,n)` is also supported::

            sage: S = SymmetricGroup([2,4,1])
            sage: s = S.simple_reflections()
            sage: x = s[2]*s[4]
            sage: x.has_descent(4)
            True
            sage: S._test_has_descent()"""
    @overload
    def inverse(self) -> Any:
        '''PermutationGroupElement.inverse(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1656)

        Return the inverse permutation.

        OUTPUT:

        For an element of a permutation group, this method returns the inverse
        element, which is both the inverse function and the inverse as an
        element of a group.

        EXAMPLES::

            sage: s = PermutationGroupElement("(1,2,3)(4,5)")
            sage: s.inverse()
            (1,3,2)(4,5)

            sage: A = AlternatingGroup(4)
            sage: t = A("(1,2,3)")
            sage: t.inverse()
            (1,3,2)

        There are several ways (syntactically) to get an inverse
        of a permutation group element.  ::

            sage: s = PermutationGroupElement("(1,2,3,4)(6,7,8)")
            sage: s.inverse() == s^-1
            True
            sage: s.inverse() == ~s
            True'''
    @overload
    def inverse(self) -> Any:
        '''PermutationGroupElement.inverse(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1656)

        Return the inverse permutation.

        OUTPUT:

        For an element of a permutation group, this method returns the inverse
        element, which is both the inverse function and the inverse as an
        element of a group.

        EXAMPLES::

            sage: s = PermutationGroupElement("(1,2,3)(4,5)")
            sage: s.inverse()
            (1,3,2)(4,5)

            sage: A = AlternatingGroup(4)
            sage: t = A("(1,2,3)")
            sage: t.inverse()
            (1,3,2)

        There are several ways (syntactically) to get an inverse
        of a permutation group element.  ::

            sage: s = PermutationGroupElement("(1,2,3,4)(6,7,8)")
            sage: s.inverse() == s^-1
            True
            sage: s.inverse() == ~s
            True'''
    @overload
    def inverse(self) -> Any:
        '''PermutationGroupElement.inverse(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1656)

        Return the inverse permutation.

        OUTPUT:

        For an element of a permutation group, this method returns the inverse
        element, which is both the inverse function and the inverse as an
        element of a group.

        EXAMPLES::

            sage: s = PermutationGroupElement("(1,2,3)(4,5)")
            sage: s.inverse()
            (1,3,2)(4,5)

            sage: A = AlternatingGroup(4)
            sage: t = A("(1,2,3)")
            sage: t.inverse()
            (1,3,2)

        There are several ways (syntactically) to get an inverse
        of a permutation group element.  ::

            sage: s = PermutationGroupElement("(1,2,3,4)(6,7,8)")
            sage: s.inverse() == s^-1
            True
            sage: s.inverse() == ~s
            True'''
    @overload
    def inverse(self) -> Any:
        '''PermutationGroupElement.inverse(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1656)

        Return the inverse permutation.

        OUTPUT:

        For an element of a permutation group, this method returns the inverse
        element, which is both the inverse function and the inverse as an
        element of a group.

        EXAMPLES::

            sage: s = PermutationGroupElement("(1,2,3)(4,5)")
            sage: s.inverse()
            (1,3,2)(4,5)

            sage: A = AlternatingGroup(4)
            sage: t = A("(1,2,3)")
            sage: t.inverse()
            (1,3,2)

        There are several ways (syntactically) to get an inverse
        of a permutation group element.  ::

            sage: s = PermutationGroupElement("(1,2,3,4)(6,7,8)")
            sage: s.inverse() == s^-1
            True
            sage: s.inverse() == ~s
            True'''
    @overload
    def inverse(self) -> Any:
        '''PermutationGroupElement.inverse(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1656)

        Return the inverse permutation.

        OUTPUT:

        For an element of a permutation group, this method returns the inverse
        element, which is both the inverse function and the inverse as an
        element of a group.

        EXAMPLES::

            sage: s = PermutationGroupElement("(1,2,3)(4,5)")
            sage: s.inverse()
            (1,3,2)(4,5)

            sage: A = AlternatingGroup(4)
            sage: t = A("(1,2,3)")
            sage: t.inverse()
            (1,3,2)

        There are several ways (syntactically) to get an inverse
        of a permutation group element.  ::

            sage: s = PermutationGroupElement("(1,2,3,4)(6,7,8)")
            sage: s.inverse() == s^-1
            True
            sage: s.inverse() == ~s
            True'''
    def matrix(self) -> Any:
        """PermutationGroupElement.matrix(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1986)

        Return a deg `\\times` deg permutation matrix associated to the permutation
        ``self``.

        EXAMPLES::

            sage: G = PermutationGroup(['(1,2,3)(4,5)'])
            sage: g = G.gen(0)
            sage: g.matrix()
            [0 1 0 0 0]
            [0 0 1 0 0]
            [1 0 0 0 0]
            [0 0 0 0 1]
            [0 0 0 1 0]"""
    @overload
    def multiplicative_order(self) -> Any:
        """PermutationGroupElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1604)

        Return the order of this group element, which is the smallest
        positive integer `n` for which `g^n = 1`.

        EXAMPLES::

            sage: s = PermutationGroupElement('(1,2)(3,5,6)')
            sage: s.multiplicative_order()
            6

        :meth:`order` is just an alias for :meth:`multiplicative_order`::

            sage: s.order()
            6

        TESTS::

            sage: # needs sage.libs.pari
            sage: prod(primes(150))
            1492182350939279320058875736615841068547583863326864530410
            sage: L = [tuple(range(sum(primes(p))+1, sum(primes(p))+1+p)) for p in primes(150)]
            sage: t = PermutationGroupElement(L).multiplicative_order(); t
            1492182350939279320058875736615841068547583863326864530410
            sage: type(t)
            <class 'sage.rings.integer.Integer'>"""
    @overload
    def multiplicative_order(self) -> Any:
        """PermutationGroupElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1604)

        Return the order of this group element, which is the smallest
        positive integer `n` for which `g^n = 1`.

        EXAMPLES::

            sage: s = PermutationGroupElement('(1,2)(3,5,6)')
            sage: s.multiplicative_order()
            6

        :meth:`order` is just an alias for :meth:`multiplicative_order`::

            sage: s.order()
            6

        TESTS::

            sage: # needs sage.libs.pari
            sage: prod(primes(150))
            1492182350939279320058875736615841068547583863326864530410
            sage: L = [tuple(range(sum(primes(p))+1, sum(primes(p))+1+p)) for p in primes(150)]
            sage: t = PermutationGroupElement(L).multiplicative_order(); t
            1492182350939279320058875736615841068547583863326864530410
            sage: type(t)
            <class 'sage.rings.integer.Integer'>"""
    @overload
    def multiplicative_order(self) -> Any:
        """PermutationGroupElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1604)

        Return the order of this group element, which is the smallest
        positive integer `n` for which `g^n = 1`.

        EXAMPLES::

            sage: s = PermutationGroupElement('(1,2)(3,5,6)')
            sage: s.multiplicative_order()
            6

        :meth:`order` is just an alias for :meth:`multiplicative_order`::

            sage: s.order()
            6

        TESTS::

            sage: # needs sage.libs.pari
            sage: prod(primes(150))
            1492182350939279320058875736615841068547583863326864530410
            sage: L = [tuple(range(sum(primes(p))+1, sum(primes(p))+1+p)) for p in primes(150)]
            sage: t = PermutationGroupElement(L).multiplicative_order(); t
            1492182350939279320058875736615841068547583863326864530410
            sage: type(t)
            <class 'sage.rings.integer.Integer'>"""
    def orbit(self, n, boolsorted=...) -> Any:
        """PermutationGroupElement.orbit(self, n, bool sorted=True)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1724)

        Return the orbit of the integer `n` under this group
        element, as a sorted list.

        EXAMPLES::

            sage: G = PermutationGroup(['(1,2,3)(4,5)'])
            sage: g = G.gen(0)
            sage: g.orbit(4)
            [4, 5]
            sage: g.orbit(3)
            [1, 2, 3]
            sage: g.orbit(10)
            [10]

        ::

            sage: s = SymmetricGroup(['a', 'b']).gen(0); s
            ('a','b')
            sage: s.orbit('a')
            ['a', 'b']"""
    @overload
    def sign(self) -> Any:
        """PermutationGroupElement.sign(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1688)

        Return the sign of ``self``, which is `(-1)^{s}`, where
        `s` is the number of swaps.

        EXAMPLES::

            sage: s = PermutationGroupElement('(1,2)(3,5,6)')
            sage: s.sign()
            -1

        ALGORITHM: Only even cycles contribute to the sign, thus

        .. MATH::

            sign(sigma) = (-1)^{\\sum_c len(c)-1}


        where the sum is over cycles in ``self``."""
    @overload
    def sign(self) -> Any:
        """PermutationGroupElement.sign(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1688)

        Return the sign of ``self``, which is `(-1)^{s}`, where
        `s` is the number of swaps.

        EXAMPLES::

            sage: s = PermutationGroupElement('(1,2)(3,5,6)')
            sage: s.sign()
            -1

        ALGORITHM: Only even cycles contribute to the sign, thus

        .. MATH::

            sign(sigma) = (-1)^{\\sum_c len(c)-1}


        where the sum is over cycles in ``self``."""
    @overload
    def tuple(self) -> Any:
        """PermutationGroupElement.tuple(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1558)

        Return tuple of images of the domain under ``self``.

        EXAMPLES::

            sage: G = SymmetricGroup(5)
            sage: s = G([2,1,5,3,4])
            sage: s.tuple()
            (2, 1, 5, 3, 4)

            sage: S = SymmetricGroup(['a', 'b'])
            sage: S.gen().tuple()
            ('b', 'a')"""
    @overload
    def tuple(self) -> Any:
        """PermutationGroupElement.tuple(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1558)

        Return tuple of images of the domain under ``self``.

        EXAMPLES::

            sage: G = SymmetricGroup(5)
            sage: s = G([2,1,5,3,4])
            sage: s.tuple()
            (2, 1, 5, 3, 4)

            sage: S = SymmetricGroup(['a', 'b'])
            sage: S.gen().tuple()
            ('b', 'a')"""
    @overload
    def tuple(self) -> Any:
        """PermutationGroupElement.tuple(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1558)

        Return tuple of images of the domain under ``self``.

        EXAMPLES::

            sage: G = SymmetricGroup(5)
            sage: s = G([2,1,5,3,4])
            sage: s.tuple()
            (2, 1, 5, 3, 4)

            sage: S = SymmetricGroup(['a', 'b'])
            sage: S.gen().tuple()
            ('b', 'a')"""
    def word_problem(self, words, display=..., as_list=...) -> Any:
        """PermutationGroupElement.word_problem(self, words, display=True, as_list=False)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 2010)

        Try to solve the word problem for ``self``.

        INPUT:

        - ``words`` -- list of elements of the ambient group, generating
          a subgroup

        - ``display`` -- boolean (default: ``True``); whether to display
          additional information

        - ``as_list`` -- boolean (default: ``False``); whether to return
          the result as a list of pairs (generator, exponent)

        OUTPUT:

        - a pair of strings, both representing the same word

        or

        - a list of pairs representing the word, each pair being
          (generator as a string, exponent as an integer)

        Let `G` be the ambient permutation group, containing the given
        element `g`. Let `H` be the subgroup of `G` generated by the list
        ``words`` of elements of `G`. If `g` is in `H`, this function
        returns an expression for `g` as a word in the elements of
        ``words`` and their inverses.

        This function does not solve the word problem in Sage. Rather it
        pushes it over to GAP, which has optimized algorithms for the word
        problem. Essentially, this function is a wrapper for the GAP
        functions ``EpimorphismFromFreeGroup`` and
        ``PreImagesRepresentative``.

        EXAMPLES::

            sage: G = PermutationGroup([[(1,2,3),(4,5)],[(3,4)]], canonicalize=False)
            sage: g1, g2 = G.gens()
            sage: h = g1^2*g2*g1
            sage: h.word_problem([g1,g2], False)
            ('x1^2*x2^-1*x1', '(1,2,3)(4,5)^2*(3,4)^-1*(1,2,3)(4,5)')

            sage: h.word_problem([g1,g2])
               x1^2*x2^-1*x1
               [['(1,2,3)(4,5)', 2], ['(3,4)', -1], ['(1,2,3)(4,5)', 1]]
            ('x1^2*x2^-1*x1', '(1,2,3)(4,5)^2*(3,4)^-1*(1,2,3)(4,5)')

            sage: h.word_problem([g1,g2], False, as_list=True)
            [['(1,2,3)(4,5)', 2], ['(3,4)', -1], ['(1,2,3)(4,5)', 1]]

        TESTS:

        Check for :issue:`28556`::

            sage: G = SymmetricGroup(6)
            sage: g = G('(1,2,3)')
            sage: g.word_problem([g], False)
            ('x1', '(1,2,3)')"""
    def __call__(self, i) -> Any:
        """PermutationGroupElement.__call__(self, i)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1055)

        Return the image of the integer `i` under this permutation.
        Alternately, if `i` is a list, tuple or string, returns the result of
        ``self`` acting on `i`.

        EXAMPLES::

            sage: G = PermutationGroup(['(1,2,3)(4,5)'])
            sage: G
            Permutation Group with generators [(1,2,3)(4,5)]
            sage: g = G.gen(0)
            sage: g(5)
            4
            sage: g('abcde')
            'bcaed'
            sage: g([0,1,2,3,4])
            [1, 2, 0, 4, 3]
            sage: g(('who','what','when','where','why'))
            ('what', 'when', 'who', 'why', 'where')

        ::

            sage: g(x)                                                                  # needs sage.symbolic
            Traceback (most recent call last):
            ...
            ValueError: must be in the domain or a list, tuple or string
            sage: g(3/2)
            Traceback (most recent call last):
            ...
            ValueError: must be in the domain or a list, tuple or string"""
    def __getitem__(self, i) -> Any:
        """PermutationGroupElement.__getitem__(self, i)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 987)

        Return the ``i``-th permutation cycle in the disjoint cycle
        representation of ``self``.

        INPUT:

        - ``i`` -- integer

        OUTPUT: a permutation group element

        EXAMPLES::

            sage: G = PermutationGroup([[(1,2,3),(4,5)]])
            sage: g = G.gen(0)
            sage: g[0]
            (1,2,3)
            sage: g[1]
            (4,5)"""
    def __hash__(self) -> Any:
        """PermutationGroupElement.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1529)

        Return a hash for this permutation.

        EXAMPLES::

            sage: G = SymmetricGroup(5)
            sage: hash(G([2,1,5,3,4]))
            -1203337681           # 32-bit
            -1527414595000039889  # 64-bit

        Check that the hash looks reasonable::

            sage: s = set()
            sage: s.update(map(hash,SymmetricGroup(0)))
            sage: s.update(map(hash,SymmetricGroup(1)))
            sage: s.update(map(hash,SymmetricGroup(2)))
            sage: s.update(map(hash,SymmetricGroup(3)))
            sage: s.update(map(hash,SymmetricGroup(4)))
            sage: s.update(map(hash,SymmetricGroup(5)))
            sage: len(s) == 1 + 1 + 2 + 6 + 24 + 120
            True"""
    def __invert__(self) -> Any:
        """PermutationGroupElement.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1430)

        Return the inverse of this permutation.

        EXAMPLES::

            sage: g = PermutationGroupElement('(1,2,3)(4,5)')
            sage: ~g
            (1,3,2)(4,5)
            sage: (~g) * g
            ()"""
    def __mul__(self, left, right) -> Any:
        """PermutationGroupElement.__mul__(left, right)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 1281)

        TESTS::

            sage: S = SymmetricGroup(5)
            sage: P = PermutationGroup([(1,2,3),(4,5)])
            sage: Q = PermutationGroup([(1,2),(2,3),(4,5)])
            sage: prod = S('(1,2,3)(4,5)')
            sage: for P1 in [S, P,Q]:
            ....:     for P2 in [S, P,Q]:
            ....:         prod = P1('(1,2,3)') * P2('(4,5)')
            ....:         assert prod.parent() == coercion_model.common_parent(P1, P2)
            ....:         assert prod == S('(1,2,3)(4,5)')"""
    @overload
    def __reduce__(self) -> Any:
        """PermutationGroupElement.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 805)

        Return a function and its arguments needed to create this
        permutation group element.  This is used in pickling.

        EXAMPLES::

           sage: g = PermutationGroupElement([(1,2,3),(4,5)]); g
           (1,2,3)(4,5)
           sage: func, args = g.__reduce__()
           sage: func(*args)
           (1,2,3)(4,5)"""
    @overload
    def __reduce__(self) -> Any:
        """PermutationGroupElement.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 805)

        Return a function and its arguments needed to create this
        permutation group element.  This is used in pickling.

        EXAMPLES::

           sage: g = PermutationGroupElement([(1,2,3),(4,5)]); g
           (1,2,3)(4,5)
           sage: func, args = g.__reduce__()
           sage: func(*args)
           (1,2,3)(4,5)"""
    def __rmul__(self, other):
        """Return value*self."""

class SymmetricGroupElement(PermutationGroupElement):
    """File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 2108)

        An element of the symmetric group.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def absolute_length(self) -> Any:
        """SymmetricGroupElement.absolute_length(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 2112)

        Return the absolute length of ``self``.

        The absolute length is the size minus the number of its disjoint
        cycles. Alternatively, it is the length of the shortest
        expression of the element as a product of reflections.

        .. SEEALSO::

            :meth:`absolute_le`

        EXAMPLES::

            sage: S = SymmetricGroup(3)
            sage: [x.absolute_length() for x in S]                                      # needs sage.combinat
            [0, 2, 2, 1, 1, 1]"""
    @overload
    def absolute_length(self) -> Any:
        """SymmetricGroupElement.absolute_length(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 2112)

        Return the absolute length of ``self``.

        The absolute length is the size minus the number of its disjoint
        cycles. Alternatively, it is the length of the shortest
        expression of the element as a product of reflections.

        .. SEEALSO::

            :meth:`absolute_le`

        EXAMPLES::

            sage: S = SymmetricGroup(3)
            sage: [x.absolute_length() for x in S]                                      # needs sage.combinat
            [0, 2, 2, 1, 1, 1]"""
    @overload
    def has_left_descent(self, i) -> bool:
        """SymmetricGroupElement.has_left_descent(self, i) -> bool

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 2133)

        Return whether `i` is a left descent of ``self``.

        EXAMPLES::

            sage: W = SymmetricGroup(4)
            sage: w = W.from_reduced_word([1,3,2,1])
            sage: [i for i in W.index_set() if w.has_left_descent(i)]
            [1, 3]"""
    @overload
    def has_left_descent(self, i) -> Any:
        """SymmetricGroupElement.has_left_descent(self, i) -> bool

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/permgroup_element.pyx (starting at line 2133)

        Return whether `i` is a left descent of ``self``.

        EXAMPLES::

            sage: W = SymmetricGroup(4)
            sage: w = W.from_reduced_word([1,3,2,1])
            sage: [i for i in W.index_set() if w.has_left_descent(i)]
            [1, 3]"""
