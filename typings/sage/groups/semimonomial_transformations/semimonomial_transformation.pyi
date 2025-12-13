import sage.structure.element
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

class SemimonomialTransformation(sage.structure.element.MultiplicativeGroupElement):
    """SemimonomialTransformation(parent, v, perm, alpha)

    File: /build/sagemath/src/sage/src/sage/groups/semimonomial_transformations/semimonomial_transformation.pyx (starting at line 94)

    An element in the semimonomial group over a ring `R`. See
    :class:`~sage.groups.semimonomial_transformations.semimonomial_transformation_group.SemimonomialTransformationGroup`
    for the details on the multiplication of two elements.

    The init method should never be called directly. Use the call via the
    parent
    :class:`~sage.groups.semimonomial_transformations.semimonomial_transformation_group.SemimonomialTransformationGroup`.
    instead.

    EXAMPLES::

        sage: F.<a> = GF(9)
        sage: S = SemimonomialTransformationGroup(F, 4)
        sage: g = S(v = [2, a, 1, 2])
        sage: h = S(perm = Permutation('(1,2,3,4)'), autom=F.hom([a**3]))
        sage: g*h
        ((2, a, 1, 2); (1,2,3,4), Ring endomorphism of Finite Field in a of size 3^2 Defn: a |--> 2*a + 1)
        sage: h*g
        ((2*a + 1, 1, 2, 2); (1,2,3,4), Ring endomorphism of Finite Field in a of size 3^2 Defn: a |--> 2*a + 1)
        sage: S(g)
        ((2, a, 1, 2); (), Ring endomorphism of Finite Field in a of size 3^2 Defn: a |--> a)
        sage: S(1)  # the one element in the group
        ((1, 1, 1, 1); (), Ring endomorphism of Finite Field in a of size 3^2 Defn: a |--> a)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, v, perm, alpha) -> Any:
        """File: /build/sagemath/src/sage/src/sage/groups/semimonomial_transformations/semimonomial_transformation.pyx (starting at line 120)

                The init method should never be called directly. Use the call via the
                parent instead. See
                :meth:`sage.groups.semimonomial_transformations.semimonomial_transformation.SemimonomialTransformation.__call__`.

                EXAMPLES::

                    sage: F.<a> = GF(9)
                    sage: S = SemimonomialTransformationGroup(F, 4)
                    sage: g = S(v = [2, a, 1, 2])  #indirect doctest
        """
    @overload
    def get_autom(self) -> Any:
        """SemimonomialTransformation.get_autom(self)

        File: /build/sagemath/src/sage/src/sage/groups/semimonomial_transformations/semimonomial_transformation.pyx (starting at line 318)

        Return the component corresponding to `Aut(R)` of ``self``.

        EXAMPLES::

            sage: F.<a> = GF(9)
            sage: SemimonomialTransformationGroup(F, 4).an_element().get_autom()
            Ring endomorphism of Finite Field in a of size 3^2 Defn: a |--> 2*a + 1"""
    @overload
    def get_autom(self) -> Any:
        """SemimonomialTransformation.get_autom(self)

        File: /build/sagemath/src/sage/src/sage/groups/semimonomial_transformations/semimonomial_transformation.pyx (starting at line 318)

        Return the component corresponding to `Aut(R)` of ``self``.

        EXAMPLES::

            sage: F.<a> = GF(9)
            sage: SemimonomialTransformationGroup(F, 4).an_element().get_autom()
            Ring endomorphism of Finite Field in a of size 3^2 Defn: a |--> 2*a + 1"""
    @overload
    def get_perm(self) -> Any:
        """SemimonomialTransformation.get_perm(self)

        File: /build/sagemath/src/sage/src/sage/groups/semimonomial_transformations/semimonomial_transformation.pyx (starting at line 306)

        Return the component corresponding to `S_n` of ``self``.

        EXAMPLES::

            sage: F.<a> = GF(9)
            sage: SemimonomialTransformationGroup(F, 4).an_element().get_perm()
            [4, 1, 2, 3]"""
    @overload
    def get_perm(self) -> Any:
        """SemimonomialTransformation.get_perm(self)

        File: /build/sagemath/src/sage/src/sage/groups/semimonomial_transformations/semimonomial_transformation.pyx (starting at line 306)

        Return the component corresponding to `S_n` of ``self``.

        EXAMPLES::

            sage: F.<a> = GF(9)
            sage: SemimonomialTransformationGroup(F, 4).an_element().get_perm()
            [4, 1, 2, 3]"""
    @overload
    def get_v(self) -> Any:
        """SemimonomialTransformation.get_v(self)

        File: /build/sagemath/src/sage/src/sage/groups/semimonomial_transformations/semimonomial_transformation.pyx (starting at line 281)

        Return the component corresponding to `{R^{     imes}}^n` of ``self``.

        EXAMPLES::

            sage: F.<a> = GF(9)
            sage: SemimonomialTransformationGroup(F, 4).an_element().get_v()
            (a, 1, 1, 1)"""
    @overload
    def get_v(self) -> Any:
        """SemimonomialTransformation.get_v(self)

        File: /build/sagemath/src/sage/src/sage/groups/semimonomial_transformations/semimonomial_transformation.pyx (starting at line 281)

        Return the component corresponding to `{R^{     imes}}^n` of ``self``.

        EXAMPLES::

            sage: F.<a> = GF(9)
            sage: SemimonomialTransformationGroup(F, 4).an_element().get_v()
            (a, 1, 1, 1)"""
    @overload
    def get_v_inverse(self) -> Any:
        """SemimonomialTransformation.get_v_inverse(self)

        File: /build/sagemath/src/sage/src/sage/groups/semimonomial_transformations/semimonomial_transformation.pyx (starting at line 293)

        Return the (elementwise) inverse of the component corresponding to
        `{R^{   imes}}^n` of ``self``.

        EXAMPLES::

            sage: F.<a> = GF(9)
            sage: SemimonomialTransformationGroup(F, 4).an_element().get_v_inverse()
            (a + 2, 1, 1, 1)"""
    @overload
    def get_v_inverse(self) -> Any:
        """SemimonomialTransformation.get_v_inverse(self)

        File: /build/sagemath/src/sage/src/sage/groups/semimonomial_transformations/semimonomial_transformation.pyx (starting at line 293)

        Return the (elementwise) inverse of the component corresponding to
        `{R^{   imes}}^n` of ``self``.

        EXAMPLES::

            sage: F.<a> = GF(9)
            sage: SemimonomialTransformationGroup(F, 4).an_element().get_v_inverse()
            (a + 2, 1, 1, 1)"""
    @overload
    def invert_v(self) -> Any:
        """SemimonomialTransformation.invert_v(self)

        File: /build/sagemath/src/sage/src/sage/groups/semimonomial_transformations/semimonomial_transformation.pyx (starting at line 330)

        Elementwisely invert all entries of ``self`` which
        correspond to the component `{R^{       imes}}^n`.

        The other components of ``self`` keep unchanged.

        EXAMPLES::

            sage: F.<a> = GF(9)
            sage: x = copy(SemimonomialTransformationGroup(F, 4).an_element())
            sage: x.invert_v()
            sage: x.get_v() == SemimonomialTransformationGroup(F, 4).an_element().get_v_inverse()
            True"""
    @overload
    def invert_v(self) -> Any:
        """SemimonomialTransformation.invert_v(self)

        File: /build/sagemath/src/sage/src/sage/groups/semimonomial_transformations/semimonomial_transformation.pyx (starting at line 330)

        Elementwisely invert all entries of ``self`` which
        correspond to the component `{R^{       imes}}^n`.

        The other components of ``self`` keep unchanged.

        EXAMPLES::

            sage: F.<a> = GF(9)
            sage: x = copy(SemimonomialTransformationGroup(F, 4).an_element())
            sage: x.invert_v()
            sage: x.get_v() == SemimonomialTransformationGroup(F, 4).an_element().get_v_inverse()
            True"""
    def __copy__(self) -> Any:
        """SemimonomialTransformation.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/groups/semimonomial_transformations/semimonomial_transformation.pyx (starting at line 147)

        Return a copy of ``self``.

        EXAMPLES::

            sage: F.<a> = GF(9)
            sage: s = SemimonomialTransformationGroup(F, 4).an_element()
            sage: t = copy(s)  # indirect doctest
            sage: t is s
            False
            sage: t == s
            True"""
    def __hash__(self) -> Any:
        """SemimonomialTransformation.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/groups/semimonomial_transformations/semimonomial_transformation.pyx (starting at line 163)

        Return hash of this element.

        EXAMPLES::

            sage: F.<a> = GF(9)
            sage: hash( SemimonomialTransformationGroup(F, 4).an_element() )  #random #indirect doctest
            6279637968393375107"""
    def __invert__(self) -> Any:
        """SemimonomialTransformation.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/groups/semimonomial_transformations/semimonomial_transformation.pyx (starting at line 217)

        Return the inverse of ``self``.

        EXAMPLES::

            sage: F.<a> = GF(9)
            sage: S = SemimonomialTransformationGroup(F, 4)
            sage: s = S.an_element()
            sage: s*s**(-1) == S(1)  # indirect doctest
            True"""
    @overload
    def __reduce__(self) -> Any:
        """SemimonomialTransformation.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/groups/semimonomial_transformations/semimonomial_transformation.pyx (starting at line 267)

        Return a function and its arguments needed to create this
        semimonomial group element. This is used in pickling.

        EXAMPLES::

            sage: F.<a> = GF(9)
            sage: SemimonomialTransformationGroup(F, 4).an_element().__reduce__()
            (Semimonomial transformation group over Finite Field in a of size 3^2 of degree 4, (0, (a, 1, 1, 1), [4, 1, 2, 3], Ring endomorphism of Finite Field in a of size 3^2
              Defn: a |--> 2*a + 1))"""
    @overload
    def __reduce__(self) -> Any:
        """SemimonomialTransformation.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/groups/semimonomial_transformations/semimonomial_transformation.pyx (starting at line 267)

        Return a function and its arguments needed to create this
        semimonomial group element. This is used in pickling.

        EXAMPLES::

            sage: F.<a> = GF(9)
            sage: SemimonomialTransformationGroup(F, 4).an_element().__reduce__()
            (Semimonomial transformation group over Finite Field in a of size 3^2 of degree 4, (0, (a, 1, 1, 1), [4, 1, 2, 3], Ring endomorphism of Finite Field in a of size 3^2
              Defn: a |--> 2*a + 1))"""
