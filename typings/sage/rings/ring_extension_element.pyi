import sage.structure.element
from sage.categories.category import ZZ as ZZ
from sage.categories.fields import Fields as Fields
from sage.cpython.getattr import dir_with_other_class as dir_with_other_class
from sage.misc.latex import latex as latex
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.structure.category_object import normalize_names as normalize_names
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

class RingExtensionElement(sage.structure.element.CommutativeAlgebraElement):
    """RingExtensionElement(RingExtension_generic parent, x, *args, **kwds)

    File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 42)

    Generic class for elements lying in ring extensions.

    TESTS::

        sage: K = GF(5^4).over()                                                        # needs sage.rings.finite_rings
        sage: x = K.random_element()                                                    # needs sage.rings.finite_rings
        sage: TestSuite(x).run()                                                        # needs sage.rings.finite_rings"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, RingExtension_genericparent, x, *args, **kwds) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 52)

                Initialize this element.

                INPUT:

                - ``parent`` -- the parent of this element

                - ``x`` -- some data to construct this element

                TESTS::

                    sage: Q = QQ.over(ZZ)
                    sage: x = Q(1/2)
                    sage: x
                    1/2
        """
    @overload
    def additive_order(self) -> Any:
        """RingExtensionElement.additive_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 540)

        Return the additive order of this element.

        EXAMPLES::

            sage: K.<a> = GF(5^4).over(GF(5^2))                                         # needs sage.rings.finite_rings
            sage: a.additive_order()                                                    # needs sage.rings.finite_rings
            5"""
    @overload
    def additive_order(self) -> Any:
        """RingExtensionElement.additive_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 540)

        Return the additive order of this element.

        EXAMPLES::

            sage: K.<a> = GF(5^4).over(GF(5^2))                                         # needs sage.rings.finite_rings
            sage: a.additive_order()                                                    # needs sage.rings.finite_rings
            5"""
    @overload
    def backend(self, force=...) -> Any:
        """RingExtensionElement.backend(self, force=False)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 313)

        Return the backend of this element.

        INPUT:

        - ``force`` -- boolean (default: ``False``); if ``False``,
          raise an error if the backend is not exposed

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5^2)
            sage: K.<z> = GF(5^4).over(F)
            sage: x = z^10
            sage: x
            (z2 + 2) + (3*z2 + 1)*z
            sage: y = x.backend()
            sage: y
            4*z4^3 + 2*z4^2 + 4*z4 + 4
            sage: y.parent()
            Finite Field in z4 of size 5^4"""
    @overload
    def backend(self) -> Any:
        """RingExtensionElement.backend(self, force=False)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 313)

        Return the backend of this element.

        INPUT:

        - ``force`` -- boolean (default: ``False``); if ``False``,
          raise an error if the backend is not exposed

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5^2)
            sage: K.<z> = GF(5^4).over(F)
            sage: x = z^10
            sage: x
            (z2 + 2) + (3*z2 + 1)*z
            sage: y = x.backend()
            sage: y
            4*z4^3 + 2*z4^2 + 4*z4 + 4
            sage: y.parent()
            Finite Field in z4 of size 5^4"""
    @overload
    def in_base(self) -> Any:
        """RingExtensionElement.in_base(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 340)

        Return this element as an element of the base.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5^2)
            sage: K.<z> = GF(5^4).over(F)
            sage: x = z^3 + z^2 + z + 4
            sage: y = x.in_base()
            sage: y
            z2 + 1
            sage: y.parent()
            Finite Field in z2 of size 5^2

        When the element is not in the base, an error is raised::

            sage: z.in_base()                                                           # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: z is not in the base

        ::

            sage: # needs sage.rings.finite_rings
            sage: S.<X> = F[]
            sage: E = S.over(F)
            sage: f = E(1)
            sage: g = f.in_base(); g
            1
            sage: g.parent()
            Finite Field in z2 of size 5^2

        TESTS:

        We check the case of a tower of extensions::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5^2)
            sage: K.<u> = GF(5^4).over(F)
            sage: L.<v> = GF(5^8).over(K)
            sage: x = 4*v^7 + v^6 + 3*v^4 + v^3 + v^2 + 4
            sage: x.in_base()
            u"""
    @overload
    def in_base(self) -> Any:
        """RingExtensionElement.in_base(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 340)

        Return this element as an element of the base.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5^2)
            sage: K.<z> = GF(5^4).over(F)
            sage: x = z^3 + z^2 + z + 4
            sage: y = x.in_base()
            sage: y
            z2 + 1
            sage: y.parent()
            Finite Field in z2 of size 5^2

        When the element is not in the base, an error is raised::

            sage: z.in_base()                                                           # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: z is not in the base

        ::

            sage: # needs sage.rings.finite_rings
            sage: S.<X> = F[]
            sage: E = S.over(F)
            sage: f = E(1)
            sage: g = f.in_base(); g
            1
            sage: g.parent()
            Finite Field in z2 of size 5^2

        TESTS:

        We check the case of a tower of extensions::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5^2)
            sage: K.<u> = GF(5^4).over(F)
            sage: L.<v> = GF(5^8).over(K)
            sage: x = 4*v^7 + v^6 + 3*v^4 + v^3 + v^2 + 4
            sage: x.in_base()
            u"""
    @overload
    def in_base(self) -> Any:
        """RingExtensionElement.in_base(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 340)

        Return this element as an element of the base.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5^2)
            sage: K.<z> = GF(5^4).over(F)
            sage: x = z^3 + z^2 + z + 4
            sage: y = x.in_base()
            sage: y
            z2 + 1
            sage: y.parent()
            Finite Field in z2 of size 5^2

        When the element is not in the base, an error is raised::

            sage: z.in_base()                                                           # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: z is not in the base

        ::

            sage: # needs sage.rings.finite_rings
            sage: S.<X> = F[]
            sage: E = S.over(F)
            sage: f = E(1)
            sage: g = f.in_base(); g
            1
            sage: g.parent()
            Finite Field in z2 of size 5^2

        TESTS:

        We check the case of a tower of extensions::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5^2)
            sage: K.<u> = GF(5^4).over(F)
            sage: L.<v> = GF(5^8).over(K)
            sage: x = 4*v^7 + v^6 + 3*v^4 + v^3 + v^2 + 4
            sage: x.in_base()
            u"""
    @overload
    def in_base(self) -> Any:
        """RingExtensionElement.in_base(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 340)

        Return this element as an element of the base.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5^2)
            sage: K.<z> = GF(5^4).over(F)
            sage: x = z^3 + z^2 + z + 4
            sage: y = x.in_base()
            sage: y
            z2 + 1
            sage: y.parent()
            Finite Field in z2 of size 5^2

        When the element is not in the base, an error is raised::

            sage: z.in_base()                                                           # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: z is not in the base

        ::

            sage: # needs sage.rings.finite_rings
            sage: S.<X> = F[]
            sage: E = S.over(F)
            sage: f = E(1)
            sage: g = f.in_base(); g
            1
            sage: g.parent()
            Finite Field in z2 of size 5^2

        TESTS:

        We check the case of a tower of extensions::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5^2)
            sage: K.<u> = GF(5^4).over(F)
            sage: L.<v> = GF(5^8).over(K)
            sage: x = 4*v^7 + v^6 + 3*v^4 + v^3 + v^2 + 4
            sage: x.in_base()
            u"""
    @overload
    def in_base(self) -> Any:
        """RingExtensionElement.in_base(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 340)

        Return this element as an element of the base.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5^2)
            sage: K.<z> = GF(5^4).over(F)
            sage: x = z^3 + z^2 + z + 4
            sage: y = x.in_base()
            sage: y
            z2 + 1
            sage: y.parent()
            Finite Field in z2 of size 5^2

        When the element is not in the base, an error is raised::

            sage: z.in_base()                                                           # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: z is not in the base

        ::

            sage: # needs sage.rings.finite_rings
            sage: S.<X> = F[]
            sage: E = S.over(F)
            sage: f = E(1)
            sage: g = f.in_base(); g
            1
            sage: g.parent()
            Finite Field in z2 of size 5^2

        TESTS:

        We check the case of a tower of extensions::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5^2)
            sage: K.<u> = GF(5^4).over(F)
            sage: L.<v> = GF(5^8).over(K)
            sage: x = 4*v^7 + v^6 + 3*v^4 + v^3 + v^2 + 4
            sage: x.in_base()
            u"""
    @overload
    def is_nilpotent(self) -> Any:
        """RingExtensionElement.is_nilpotent(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 579)

        Return whether if this element is nilpotent in this ring.

        EXAMPLES::

            sage: A.<x> = PolynomialRing(QQ)
            sage: E = A.over(QQ)
            sage: E(0).is_nilpotent()
            True
            sage: E(x).is_nilpotent()
            False"""
    @overload
    def is_nilpotent(self) -> Any:
        """RingExtensionElement.is_nilpotent(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 579)

        Return whether if this element is nilpotent in this ring.

        EXAMPLES::

            sage: A.<x> = PolynomialRing(QQ)
            sage: E = A.over(QQ)
            sage: E(0).is_nilpotent()
            True
            sage: E(x).is_nilpotent()
            False"""
    @overload
    def is_nilpotent(self) -> Any:
        """RingExtensionElement.is_nilpotent(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 579)

        Return whether if this element is nilpotent in this ring.

        EXAMPLES::

            sage: A.<x> = PolynomialRing(QQ)
            sage: E = A.over(QQ)
            sage: E(0).is_nilpotent()
            True
            sage: E(x).is_nilpotent()
            False"""
    @overload
    def is_prime(self) -> Any:
        """RingExtensionElement.is_prime(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 594)

        Return whether this element is a prime element in this ring.

        EXAMPLES::

            sage: A.<x> = PolynomialRing(QQ)
            sage: E = A.over(QQ)
            sage: E(x^2 + 1).is_prime()                                                 # needs sage.libs.pari
            True
            sage: E(x^2 - 1).is_prime()                                                 # needs sage.libs.pari
            False"""
    @overload
    def is_prime(self) -> Any:
        """RingExtensionElement.is_prime(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 594)

        Return whether this element is a prime element in this ring.

        EXAMPLES::

            sage: A.<x> = PolynomialRing(QQ)
            sage: E = A.over(QQ)
            sage: E(x^2 + 1).is_prime()                                                 # needs sage.libs.pari
            True
            sage: E(x^2 - 1).is_prime()                                                 # needs sage.libs.pari
            False"""
    @overload
    def is_prime(self) -> Any:
        """RingExtensionElement.is_prime(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 594)

        Return whether this element is a prime element in this ring.

        EXAMPLES::

            sage: A.<x> = PolynomialRing(QQ)
            sage: E = A.over(QQ)
            sage: E(x^2 + 1).is_prime()                                                 # needs sage.libs.pari
            True
            sage: E(x^2 - 1).is_prime()                                                 # needs sage.libs.pari
            False"""
    @overload
    def is_square(self, root=...) -> Any:
        """RingExtensionElement.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 609)

        Return whether this element is a square in this ring.

        INPUT:

        - ``root`` -- boolean (default: ``False``); if ``True``,
          return also a square root

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(5^3).over()
            sage: a.is_square()
            False
            sage: a.is_square(root=True)
            (False, None)
            sage: b = a + 1
            sage: b.is_square()
            True
            sage: b.is_square(root=True)
            (True, 2 + 3*a + a^2)"""
    @overload
    def is_square(self) -> Any:
        """RingExtensionElement.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 609)

        Return whether this element is a square in this ring.

        INPUT:

        - ``root`` -- boolean (default: ``False``); if ``True``,
          return also a square root

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(5^3).over()
            sage: a.is_square()
            False
            sage: a.is_square(root=True)
            (False, None)
            sage: b = a + 1
            sage: b.is_square()
            True
            sage: b.is_square(root=True)
            (True, 2 + 3*a + a^2)"""
    @overload
    def is_square(self, root=...) -> Any:
        """RingExtensionElement.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 609)

        Return whether this element is a square in this ring.

        INPUT:

        - ``root`` -- boolean (default: ``False``); if ``True``,
          return also a square root

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(5^3).over()
            sage: a.is_square()
            False
            sage: a.is_square(root=True)
            (False, None)
            sage: b = a + 1
            sage: b.is_square()
            True
            sage: b.is_square(root=True)
            (True, 2 + 3*a + a^2)"""
    @overload
    def is_square(self) -> Any:
        """RingExtensionElement.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 609)

        Return whether this element is a square in this ring.

        INPUT:

        - ``root`` -- boolean (default: ``False``); if ``True``,
          return also a square root

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(5^3).over()
            sage: a.is_square()
            False
            sage: a.is_square(root=True)
            (False, None)
            sage: b = a + 1
            sage: b.is_square()
            True
            sage: b.is_square(root=True)
            (True, 2 + 3*a + a^2)"""
    @overload
    def is_square(self, root=...) -> Any:
        """RingExtensionElement.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 609)

        Return whether this element is a square in this ring.

        INPUT:

        - ``root`` -- boolean (default: ``False``); if ``True``,
          return also a square root

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(5^3).over()
            sage: a.is_square()
            False
            sage: a.is_square(root=True)
            (False, None)
            sage: b = a + 1
            sage: b.is_square()
            True
            sage: b.is_square(root=True)
            (True, 2 + 3*a + a^2)"""
    @overload
    def is_unit(self) -> Any:
        """RingExtensionElement.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 564)

        Return whether if this element is a unit in this ring.

        EXAMPLES::

            sage: A.<x> = PolynomialRing(QQ)
            sage: E = A.over(QQ)
            sage: E(4).is_unit()
            True
            sage: E(x).is_unit()
            False"""
    @overload
    def is_unit(self) -> Any:
        """RingExtensionElement.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 564)

        Return whether if this element is a unit in this ring.

        EXAMPLES::

            sage: A.<x> = PolynomialRing(QQ)
            sage: E = A.over(QQ)
            sage: E(4).is_unit()
            True
            sage: E(x).is_unit()
            False"""
    @overload
    def is_unit(self) -> Any:
        """RingExtensionElement.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 564)

        Return whether if this element is a unit in this ring.

        EXAMPLES::

            sage: A.<x> = PolynomialRing(QQ)
            sage: E = A.over(QQ)
            sage: E(4).is_unit()
            True
            sage: E(x).is_unit()
            False"""
    @overload
    def multiplicative_order(self) -> Any:
        """RingExtensionElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 552)

        Return the multiplicite order of this element.

        EXAMPLES::

            sage: K.<a> = GF(5^4).over(GF(5^2))                                         # needs sage.rings.finite_rings
            sage: a.multiplicative_order()                                              # needs sage.rings.finite_rings
            624"""
    @overload
    def multiplicative_order(self) -> Any:
        """RingExtensionElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 552)

        Return the multiplicite order of this element.

        EXAMPLES::

            sage: K.<a> = GF(5^4).over(GF(5^2))                                         # needs sage.rings.finite_rings
            sage: a.multiplicative_order()                                              # needs sage.rings.finite_rings
            624"""
    @overload
    def sqrt(self, extend=..., all=..., name=...) -> Any:
        """RingExtensionElement.sqrt(self, extend=True, all=False, name=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 641)

        Return a square root or all square roots of this element.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``,
          return a square root in an extension ring, if necessary.
          Otherwise, raise a :exc:`ValueError` if the root is not in
          the ring.

        - ``all`` -- boolean (default: ``False``); if ``True``,
          return all square roots of this element, instead of just one

        - ``name`` -- required when ``extend=True`` and ``self`` is not a
          square; this will be the name of the generator extension

        .. NOTE::

            The option ``extend=True`` is often not implemented.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(5^3).over()
            sage: b = a + 1
            sage: b.sqrt()
            2 + 3*a + a^2
            sage: b.sqrt(all=True)
            [2 + 3*a + a^2, 3 + 2*a - a^2]"""
    @overload
    def sqrt(self) -> Any:
        """RingExtensionElement.sqrt(self, extend=True, all=False, name=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 641)

        Return a square root or all square roots of this element.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``,
          return a square root in an extension ring, if necessary.
          Otherwise, raise a :exc:`ValueError` if the root is not in
          the ring.

        - ``all`` -- boolean (default: ``False``); if ``True``,
          return all square roots of this element, instead of just one

        - ``name`` -- required when ``extend=True`` and ``self`` is not a
          square; this will be the name of the generator extension

        .. NOTE::

            The option ``extend=True`` is often not implemented.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(5^3).over()
            sage: b = a + 1
            sage: b.sqrt()
            2 + 3*a + a^2
            sage: b.sqrt(all=True)
            [2 + 3*a + a^2, 3 + 2*a - a^2]"""
    @overload
    def sqrt(self, all=...) -> Any:
        """RingExtensionElement.sqrt(self, extend=True, all=False, name=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 641)

        Return a square root or all square roots of this element.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``,
          return a square root in an extension ring, if necessary.
          Otherwise, raise a :exc:`ValueError` if the root is not in
          the ring.

        - ``all`` -- boolean (default: ``False``); if ``True``,
          return all square roots of this element, instead of just one

        - ``name`` -- required when ``extend=True`` and ``self`` is not a
          square; this will be the name of the generator extension

        .. NOTE::

            The option ``extend=True`` is often not implemented.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(5^3).over()
            sage: b = a + 1
            sage: b.sqrt()
            2 + 3*a + a^2
            sage: b.sqrt(all=True)
            [2 + 3*a + a^2, 3 + 2*a - a^2]"""
    def __call__(self, *args, **kwargs) -> Any:
        """RingExtensionElement.__call__(self, *args, **kwargs)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 154)

        Call this element.

        This methods calls the appropriate method of the backend if
        ``import_methods`` is set to ``True``

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: E = R.over()
            sage: P = E(x^2 + 2*x + 3)
            sage: P(1)
            6"""
    def __dir__(self) -> Any:
        """RingExtensionElement.__dir__(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 174)

        Return the list of all the attributes of this element;
        if the parent of this element was created with ``import_methods = True``,
        concatenate this list with the list of all the methods of the backend
        element.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: A.<a> = QQ.extension(x^2 - 2)
            sage: K.<a> = A.over()
            sage: dir(a)
            ['__abs__',
             '__add__',
             ...
             'complex_embeddings',
             'conjugate',
             'continued_fraction',
             'continued_fraction_list',
             ...
             'trace',
             'valuation',
             'vector',
             'xgcd']"""
    def __getitem__(self, i) -> Any:
        """RingExtensionElement.__getitem__(self, i)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 134)

        Return the `i`-th item of this element.

        This methods calls the appropriate method of the backend if
        ``import_methods`` is set to ``True``

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: E = R.over()
            sage: P = E(x^2 + 2*x + 3)
            sage: P[0]
            3"""
    def __hash__(self) -> Any:
        """RingExtensionElement.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 213)

        Return a hash of this element.

        EXAMPLES:

            sage: E.<a> = GF(5^3).over()                                                # needs sage.rings.finite_rings
            sage: hash(a)                                                               # needs sage.rings.finite_rings
            5"""
    def __reduce__(self) -> Any:
        """RingExtensionElement.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 83)

        Return a tuple of a function and data that can be used to unpickle this
        element.

        TESTS::

            sage: # needs sage.rings.finite_rings
            sage: K = GF(5^3).over()
            sage: x = K.random_element()
            sage: type(x)
            <class 'sage.rings.ring_extension_element.RingExtensionWithBasisElement'>
            sage: loads(dumps(x)) == x
            True"""

class RingExtensionFractionFieldElement(RingExtensionElement):
    """File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 696)

        A class for elements lying in fraction fields of ring extensions.

        TESTS::

            sage: Z = ZZ.over()
            sage: Q = Z.fraction_field()
            sage: x = Q.random_element()
            sage: type(x)
            <class 'sage.rings.ring_extension_element.RingExtensionFractionFieldElement'>
            sage: TestSuite(x).run()
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def denominator(self) -> Any:
        """RingExtensionFractionFieldElement.denominator(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 827)

        Return the denominator of this element.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x> = ZZ[]
            sage: A.<a> = ZZ.extension(x^2 - 2)
            sage: OK = A.over()  # over ZZ
            sage: K = OK.fraction_field(); K
            Fraction Field of
             Maximal Order generated by a in Number Field in a
             with defining polynomial x^2 - 2 over its base
            sage: x = K(1/a); x
            a/2
            sage: denom = x.denominator(); denom
            2

        The denominator is an element of the ring which was used
        to construct the fraction field::

            sage: denom.parent()                                                        # needs sage.rings.number_field
            Maximal Order generated by a in Number Field in a with defining polynomial x^2 - 2 over its base
            sage: denom.parent() is OK                                                  # needs sage.rings.number_field
            True

        TESTS::

            sage: # needs sage.rings.number_field
            sage: x = K.random_element()
            sage: x == x.numerator() / x.denominator()
            True"""
    @overload
    def denominator(self) -> Any:
        """RingExtensionFractionFieldElement.denominator(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 827)

        Return the denominator of this element.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x> = ZZ[]
            sage: A.<a> = ZZ.extension(x^2 - 2)
            sage: OK = A.over()  # over ZZ
            sage: K = OK.fraction_field(); K
            Fraction Field of
             Maximal Order generated by a in Number Field in a
             with defining polynomial x^2 - 2 over its base
            sage: x = K(1/a); x
            a/2
            sage: denom = x.denominator(); denom
            2

        The denominator is an element of the ring which was used
        to construct the fraction field::

            sage: denom.parent()                                                        # needs sage.rings.number_field
            Maximal Order generated by a in Number Field in a with defining polynomial x^2 - 2 over its base
            sage: denom.parent() is OK                                                  # needs sage.rings.number_field
            True

        TESTS::

            sage: # needs sage.rings.number_field
            sage: x = K.random_element()
            sage: x == x.numerator() / x.denominator()
            True"""
    @overload
    def denominator(self) -> Any:
        """RingExtensionFractionFieldElement.denominator(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 827)

        Return the denominator of this element.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x> = ZZ[]
            sage: A.<a> = ZZ.extension(x^2 - 2)
            sage: OK = A.over()  # over ZZ
            sage: K = OK.fraction_field(); K
            Fraction Field of
             Maximal Order generated by a in Number Field in a
             with defining polynomial x^2 - 2 over its base
            sage: x = K(1/a); x
            a/2
            sage: denom = x.denominator(); denom
            2

        The denominator is an element of the ring which was used
        to construct the fraction field::

            sage: denom.parent()                                                        # needs sage.rings.number_field
            Maximal Order generated by a in Number Field in a with defining polynomial x^2 - 2 over its base
            sage: denom.parent() is OK                                                  # needs sage.rings.number_field
            True

        TESTS::

            sage: # needs sage.rings.number_field
            sage: x = K.random_element()
            sage: x == x.numerator() / x.denominator()
            True"""
    @overload
    def numerator(self) -> Any:
        """RingExtensionFractionFieldElement.numerator(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 789)

        Return the numerator of this element.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: A.<a> = ZZ.extension(x^2 - 2)
            sage: OK = A.over()  # over ZZ
            sage: K = OK.fraction_field(); K
            Fraction Field of Maximal Order generated by a in Number Field in a
             with defining polynomial x^2 - 2 over its base
            sage: x = K(1/a); x
            a/2
            sage: num = x.numerator(); num
            a

        The numerator is an element of the ring which was used
        to construct the fraction field::

            sage: num.parent()                                                          # needs sage.rings.number_field
            Maximal Order generated by a in Number Field in a
             with defining polynomial x^2 - 2 over its base
            sage: num.parent() is OK                                                    # needs sage.rings.number_field
            True

        TESTS::

            sage: # needs sage.rings.number_field
            sage: x = K.random_element()
            sage: x == x.numerator() / x.denominator()
            True"""
    @overload
    def numerator(self) -> Any:
        """RingExtensionFractionFieldElement.numerator(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 789)

        Return the numerator of this element.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: A.<a> = ZZ.extension(x^2 - 2)
            sage: OK = A.over()  # over ZZ
            sage: K = OK.fraction_field(); K
            Fraction Field of Maximal Order generated by a in Number Field in a
             with defining polynomial x^2 - 2 over its base
            sage: x = K(1/a); x
            a/2
            sage: num = x.numerator(); num
            a

        The numerator is an element of the ring which was used
        to construct the fraction field::

            sage: num.parent()                                                          # needs sage.rings.number_field
            Maximal Order generated by a in Number Field in a
             with defining polynomial x^2 - 2 over its base
            sage: num.parent() is OK                                                    # needs sage.rings.number_field
            True

        TESTS::

            sage: # needs sage.rings.number_field
            sage: x = K.random_element()
            sage: x == x.numerator() / x.denominator()
            True"""
    @overload
    def numerator(self) -> Any:
        """RingExtensionFractionFieldElement.numerator(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 789)

        Return the numerator of this element.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: A.<a> = ZZ.extension(x^2 - 2)
            sage: OK = A.over()  # over ZZ
            sage: K = OK.fraction_field(); K
            Fraction Field of Maximal Order generated by a in Number Field in a
             with defining polynomial x^2 - 2 over its base
            sage: x = K(1/a); x
            a/2
            sage: num = x.numerator(); num
            a

        The numerator is an element of the ring which was used
        to construct the fraction field::

            sage: num.parent()                                                          # needs sage.rings.number_field
            Maximal Order generated by a in Number Field in a
             with defining polynomial x^2 - 2 over its base
            sage: num.parent() is OK                                                    # needs sage.rings.number_field
            True

        TESTS::

            sage: # needs sage.rings.number_field
            sage: x = K.random_element()
            sage: x == x.numerator() / x.denominator()
            True"""
    def __hash__(self) -> Any:
        """RingExtensionFractionFieldElement.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 709)

        Return a hash of this element.

        EXAMPLES:

            sage: E.<a> = GF(5^3).over()                                                # needs sage.rings.finite_rings
            sage: hash(a)                                                               # needs sage.rings.finite_rings
            5"""

class RingExtensionWithBasisElement(RingExtensionElement):
    """File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 869)

        A class for elements lying in finite free extensions.

        TESTS::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(5^3).over()
            sage: L.<b> = GF(5^9).over(K)
            sage: type(b)
            <class 'sage.rings.ring_extension_element.RingExtensionWithBasisElement'>
            sage: TestSuite(b).run()
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def charpoly(self, base=..., var=...) -> Any:
        """RingExtensionWithBasisElement.charpoly(self, base=None, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 1462)

        Return the characteristic polynomial of this element over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None``

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5)
            sage: K.<a> = GF(5^3).over(F)
            sage: L.<b> = GF(5^6).over(K)
            sage: u = a/(1+b)
            sage: chi = u.charpoly(K); chi
            x^2 + (1 + 2*a + 3*a^2)*x + 3 + 2*a^2

        We check that the charpoly has coefficients in the base ring::

            sage: chi.base_ring()                                                       # needs sage.rings.finite_rings
            Field in a with defining polynomial x^3 + 3*x + 3 over its base
            sage: chi.base_ring() is K                                                  # needs sage.rings.finite_rings
            True

        and that it annihilates u::

            sage: chi(u)                                                                # needs sage.rings.finite_rings
            0

        Similarly, one can compute the characteristic polynomial over F::

            sage: u.charpoly(F)                                                         # needs sage.rings.finite_rings
            x^6 + x^4 + 2*x^3 + 3*x + 4

        A different variable name can be specified::

            sage: u.charpoly(F, var='t')                                                # needs sage.rings.finite_rings
            t^6 + t^4 + 2*t^3 + 3*t + 4

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: u.charpoly()                                                          # needs sage.rings.finite_rings
            x^2 + (1 + 2*a + 3*a^2)*x + 3 + 2*a^2

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: u.charpoly(GF(5^2))                                                   # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z2 of size 5^2

        TESTS:

        We check that the characteristic polynomial of an element in the base
        ring is a power of a polynomial of degree 1::

            sage: S.<x> = K[]                                                           # needs sage.rings.finite_rings
            sage: u = K.random_element()                                                # needs sage.rings.finite_rings
            sage: L(u).charpoly() == (x - u)^2                                          # needs sage.rings.finite_rings
            True"""
    @overload
    def charpoly(self, K) -> Any:
        """RingExtensionWithBasisElement.charpoly(self, base=None, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 1462)

        Return the characteristic polynomial of this element over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None``

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5)
            sage: K.<a> = GF(5^3).over(F)
            sage: L.<b> = GF(5^6).over(K)
            sage: u = a/(1+b)
            sage: chi = u.charpoly(K); chi
            x^2 + (1 + 2*a + 3*a^2)*x + 3 + 2*a^2

        We check that the charpoly has coefficients in the base ring::

            sage: chi.base_ring()                                                       # needs sage.rings.finite_rings
            Field in a with defining polynomial x^3 + 3*x + 3 over its base
            sage: chi.base_ring() is K                                                  # needs sage.rings.finite_rings
            True

        and that it annihilates u::

            sage: chi(u)                                                                # needs sage.rings.finite_rings
            0

        Similarly, one can compute the characteristic polynomial over F::

            sage: u.charpoly(F)                                                         # needs sage.rings.finite_rings
            x^6 + x^4 + 2*x^3 + 3*x + 4

        A different variable name can be specified::

            sage: u.charpoly(F, var='t')                                                # needs sage.rings.finite_rings
            t^6 + t^4 + 2*t^3 + 3*t + 4

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: u.charpoly()                                                          # needs sage.rings.finite_rings
            x^2 + (1 + 2*a + 3*a^2)*x + 3 + 2*a^2

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: u.charpoly(GF(5^2))                                                   # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z2 of size 5^2

        TESTS:

        We check that the characteristic polynomial of an element in the base
        ring is a power of a polynomial of degree 1::

            sage: S.<x> = K[]                                                           # needs sage.rings.finite_rings
            sage: u = K.random_element()                                                # needs sage.rings.finite_rings
            sage: L(u).charpoly() == (x - u)^2                                          # needs sage.rings.finite_rings
            True"""
    @overload
    def charpoly(self, F) -> Any:
        """RingExtensionWithBasisElement.charpoly(self, base=None, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 1462)

        Return the characteristic polynomial of this element over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None``

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5)
            sage: K.<a> = GF(5^3).over(F)
            sage: L.<b> = GF(5^6).over(K)
            sage: u = a/(1+b)
            sage: chi = u.charpoly(K); chi
            x^2 + (1 + 2*a + 3*a^2)*x + 3 + 2*a^2

        We check that the charpoly has coefficients in the base ring::

            sage: chi.base_ring()                                                       # needs sage.rings.finite_rings
            Field in a with defining polynomial x^3 + 3*x + 3 over its base
            sage: chi.base_ring() is K                                                  # needs sage.rings.finite_rings
            True

        and that it annihilates u::

            sage: chi(u)                                                                # needs sage.rings.finite_rings
            0

        Similarly, one can compute the characteristic polynomial over F::

            sage: u.charpoly(F)                                                         # needs sage.rings.finite_rings
            x^6 + x^4 + 2*x^3 + 3*x + 4

        A different variable name can be specified::

            sage: u.charpoly(F, var='t')                                                # needs sage.rings.finite_rings
            t^6 + t^4 + 2*t^3 + 3*t + 4

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: u.charpoly()                                                          # needs sage.rings.finite_rings
            x^2 + (1 + 2*a + 3*a^2)*x + 3 + 2*a^2

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: u.charpoly(GF(5^2))                                                   # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z2 of size 5^2

        TESTS:

        We check that the characteristic polynomial of an element in the base
        ring is a power of a polynomial of degree 1::

            sage: S.<x> = K[]                                                           # needs sage.rings.finite_rings
            sage: u = K.random_element()                                                # needs sage.rings.finite_rings
            sage: L(u).charpoly() == (x - u)^2                                          # needs sage.rings.finite_rings
            True"""
    @overload
    def charpoly(self, F, var=...) -> Any:
        """RingExtensionWithBasisElement.charpoly(self, base=None, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 1462)

        Return the characteristic polynomial of this element over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None``

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5)
            sage: K.<a> = GF(5^3).over(F)
            sage: L.<b> = GF(5^6).over(K)
            sage: u = a/(1+b)
            sage: chi = u.charpoly(K); chi
            x^2 + (1 + 2*a + 3*a^2)*x + 3 + 2*a^2

        We check that the charpoly has coefficients in the base ring::

            sage: chi.base_ring()                                                       # needs sage.rings.finite_rings
            Field in a with defining polynomial x^3 + 3*x + 3 over its base
            sage: chi.base_ring() is K                                                  # needs sage.rings.finite_rings
            True

        and that it annihilates u::

            sage: chi(u)                                                                # needs sage.rings.finite_rings
            0

        Similarly, one can compute the characteristic polynomial over F::

            sage: u.charpoly(F)                                                         # needs sage.rings.finite_rings
            x^6 + x^4 + 2*x^3 + 3*x + 4

        A different variable name can be specified::

            sage: u.charpoly(F, var='t')                                                # needs sage.rings.finite_rings
            t^6 + t^4 + 2*t^3 + 3*t + 4

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: u.charpoly()                                                          # needs sage.rings.finite_rings
            x^2 + (1 + 2*a + 3*a^2)*x + 3 + 2*a^2

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: u.charpoly(GF(5^2))                                                   # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z2 of size 5^2

        TESTS:

        We check that the characteristic polynomial of an element in the base
        ring is a power of a polynomial of degree 1::

            sage: S.<x> = K[]                                                           # needs sage.rings.finite_rings
            sage: u = K.random_element()                                                # needs sage.rings.finite_rings
            sage: L(u).charpoly() == (x - u)^2                                          # needs sage.rings.finite_rings
            True"""
    @overload
    def charpoly(self) -> Any:
        """RingExtensionWithBasisElement.charpoly(self, base=None, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 1462)

        Return the characteristic polynomial of this element over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None``

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5)
            sage: K.<a> = GF(5^3).over(F)
            sage: L.<b> = GF(5^6).over(K)
            sage: u = a/(1+b)
            sage: chi = u.charpoly(K); chi
            x^2 + (1 + 2*a + 3*a^2)*x + 3 + 2*a^2

        We check that the charpoly has coefficients in the base ring::

            sage: chi.base_ring()                                                       # needs sage.rings.finite_rings
            Field in a with defining polynomial x^3 + 3*x + 3 over its base
            sage: chi.base_ring() is K                                                  # needs sage.rings.finite_rings
            True

        and that it annihilates u::

            sage: chi(u)                                                                # needs sage.rings.finite_rings
            0

        Similarly, one can compute the characteristic polynomial over F::

            sage: u.charpoly(F)                                                         # needs sage.rings.finite_rings
            x^6 + x^4 + 2*x^3 + 3*x + 4

        A different variable name can be specified::

            sage: u.charpoly(F, var='t')                                                # needs sage.rings.finite_rings
            t^6 + t^4 + 2*t^3 + 3*t + 4

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: u.charpoly()                                                          # needs sage.rings.finite_rings
            x^2 + (1 + 2*a + 3*a^2)*x + 3 + 2*a^2

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: u.charpoly(GF(5^2))                                                   # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z2 of size 5^2

        TESTS:

        We check that the characteristic polynomial of an element in the base
        ring is a power of a polynomial of degree 1::

            sage: S.<x> = K[]                                                           # needs sage.rings.finite_rings
            sage: u = K.random_element()                                                # needs sage.rings.finite_rings
            sage: L(u).charpoly() == (x - u)^2                                          # needs sage.rings.finite_rings
            True"""
    @overload
    def charpoly(self) -> Any:
        """RingExtensionWithBasisElement.charpoly(self, base=None, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 1462)

        Return the characteristic polynomial of this element over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None``

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5)
            sage: K.<a> = GF(5^3).over(F)
            sage: L.<b> = GF(5^6).over(K)
            sage: u = a/(1+b)
            sage: chi = u.charpoly(K); chi
            x^2 + (1 + 2*a + 3*a^2)*x + 3 + 2*a^2

        We check that the charpoly has coefficients in the base ring::

            sage: chi.base_ring()                                                       # needs sage.rings.finite_rings
            Field in a with defining polynomial x^3 + 3*x + 3 over its base
            sage: chi.base_ring() is K                                                  # needs sage.rings.finite_rings
            True

        and that it annihilates u::

            sage: chi(u)                                                                # needs sage.rings.finite_rings
            0

        Similarly, one can compute the characteristic polynomial over F::

            sage: u.charpoly(F)                                                         # needs sage.rings.finite_rings
            x^6 + x^4 + 2*x^3 + 3*x + 4

        A different variable name can be specified::

            sage: u.charpoly(F, var='t')                                                # needs sage.rings.finite_rings
            t^6 + t^4 + 2*t^3 + 3*t + 4

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: u.charpoly()                                                          # needs sage.rings.finite_rings
            x^2 + (1 + 2*a + 3*a^2)*x + 3 + 2*a^2

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: u.charpoly(GF(5^2))                                                   # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z2 of size 5^2

        TESTS:

        We check that the characteristic polynomial of an element in the base
        ring is a power of a polynomial of degree 1::

            sage: S.<x> = K[]                                                           # needs sage.rings.finite_rings
            sage: u = K.random_element()                                                # needs sage.rings.finite_rings
            sage: L(u).charpoly() == (x - u)^2                                          # needs sage.rings.finite_rings
            True"""
    @overload
    def matrix(self, base=...) -> Any:
        """RingExtensionWithBasisElement.matrix(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 1192)

        Return the matrix of the multiplication by this element (in
        the basis output by :meth:`basis_over`).

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None``

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(5^3).over()  # over GF(5)
            sage: L.<b> = GF(5^6).over(K)
            sage: u = a/(1+b)
            sage: u
            (2 + a + 3*a^2) + (3 + 3*a + a^2)*b
            sage: b*u
            (3 + 2*a^2) + (2 + 2*a - a^2)*b
            sage: u.matrix(K)
            [2 + a + 3*a^2 3 + 3*a + a^2]
            [    3 + 2*a^2 2 + 2*a - a^2]
            sage: u.matrix(GF(5))
            [2 1 3 3 3 1]
            [1 3 1 2 0 3]
            [2 3 3 1 3 0]
            [3 0 2 2 2 4]
            [4 2 0 3 0 2]
            [0 4 2 4 2 0]

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: u.matrix()                                                            # needs sage.rings.finite_rings
            [2 + a + 3*a^2 3 + 3*a + a^2]
            [    3 + 2*a^2 2 + 2*a - a^2]

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: u.matrix(GF(5^2))                                                     # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z2 of size 5^2"""
    @overload
    def matrix(self, K) -> Any:
        """RingExtensionWithBasisElement.matrix(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 1192)

        Return the matrix of the multiplication by this element (in
        the basis output by :meth:`basis_over`).

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None``

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(5^3).over()  # over GF(5)
            sage: L.<b> = GF(5^6).over(K)
            sage: u = a/(1+b)
            sage: u
            (2 + a + 3*a^2) + (3 + 3*a + a^2)*b
            sage: b*u
            (3 + 2*a^2) + (2 + 2*a - a^2)*b
            sage: u.matrix(K)
            [2 + a + 3*a^2 3 + 3*a + a^2]
            [    3 + 2*a^2 2 + 2*a - a^2]
            sage: u.matrix(GF(5))
            [2 1 3 3 3 1]
            [1 3 1 2 0 3]
            [2 3 3 1 3 0]
            [3 0 2 2 2 4]
            [4 2 0 3 0 2]
            [0 4 2 4 2 0]

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: u.matrix()                                                            # needs sage.rings.finite_rings
            [2 + a + 3*a^2 3 + 3*a + a^2]
            [    3 + 2*a^2 2 + 2*a - a^2]

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: u.matrix(GF(5^2))                                                     # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z2 of size 5^2"""
    @overload
    def matrix(self) -> Any:
        """RingExtensionWithBasisElement.matrix(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 1192)

        Return the matrix of the multiplication by this element (in
        the basis output by :meth:`basis_over`).

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None``

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(5^3).over()  # over GF(5)
            sage: L.<b> = GF(5^6).over(K)
            sage: u = a/(1+b)
            sage: u
            (2 + a + 3*a^2) + (3 + 3*a + a^2)*b
            sage: b*u
            (3 + 2*a^2) + (2 + 2*a - a^2)*b
            sage: u.matrix(K)
            [2 + a + 3*a^2 3 + 3*a + a^2]
            [    3 + 2*a^2 2 + 2*a - a^2]
            sage: u.matrix(GF(5))
            [2 1 3 3 3 1]
            [1 3 1 2 0 3]
            [2 3 3 1 3 0]
            [3 0 2 2 2 4]
            [4 2 0 3 0 2]
            [0 4 2 4 2 0]

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: u.matrix()                                                            # needs sage.rings.finite_rings
            [2 + a + 3*a^2 3 + 3*a + a^2]
            [    3 + 2*a^2 2 + 2*a - a^2]

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: u.matrix(GF(5^2))                                                     # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z2 of size 5^2"""
    @overload
    def minpoly(self, base=..., var=...) -> Any:
        """RingExtensionWithBasisElement.minpoly(self, base=None, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 1529)

        Return the minimal polynomial of this element over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None``

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5)
            sage: K.<a> = GF(5^3).over(F)
            sage: L.<b> = GF(5^6).over(K)
            sage: u = 1 / (a+b)
            sage: chi = u.minpoly(K); chi
            x^2 + (2*a + a^2)*x - 1 + a

        We check that the minimal polynomial has coefficients in the base ring::

            sage: chi.base_ring()                                                       # needs sage.rings.finite_rings
            Field in a with defining polynomial x^3 + 3*x + 3 over its base
            sage: chi.base_ring() is K                                                  # needs sage.rings.finite_rings
            True

        and that it annihilates u::

            sage: chi(u)                                                                # needs sage.rings.finite_rings
            0

        Similarly, one can compute the minimal polynomial over F::

            sage: u.minpoly(F)                                                          # needs sage.rings.finite_rings
            x^6 + 4*x^5 + x^4 + 2*x^2 + 3

        A different variable name can be specified::

            sage: u.minpoly(F, var='t')                                                 # needs sage.rings.finite_rings
            t^6 + 4*t^5 + t^4 + 2*t^2 + 3

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: u.minpoly()                                                           # needs sage.rings.finite_rings
            x^2 + (2*a + a^2)*x - 1 + a

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: u.minpoly(GF(5^2))                                                    # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z2 of size 5^2

        TESTS:

        We check that the minimal polynomial of an element in the base
        ring has degree 1::

            sage: S.<x> = K[]                                                           # needs sage.rings.finite_rings
            sage: u = K.random_element()                                                # needs sage.rings.finite_rings
            sage: L(u).minpoly() == x - u                                               # needs sage.rings.finite_rings
            True

        In a similar fashion, the minimal polynomial over `F` of an element
        of `K` should have degree 1 or 3::

            sage: L(u).minpoly(F).degree() in [ 1, 3 ]                                  # needs sage.rings.finite_rings
            True"""
    @overload
    def minpoly(self, K) -> Any:
        """RingExtensionWithBasisElement.minpoly(self, base=None, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 1529)

        Return the minimal polynomial of this element over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None``

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5)
            sage: K.<a> = GF(5^3).over(F)
            sage: L.<b> = GF(5^6).over(K)
            sage: u = 1 / (a+b)
            sage: chi = u.minpoly(K); chi
            x^2 + (2*a + a^2)*x - 1 + a

        We check that the minimal polynomial has coefficients in the base ring::

            sage: chi.base_ring()                                                       # needs sage.rings.finite_rings
            Field in a with defining polynomial x^3 + 3*x + 3 over its base
            sage: chi.base_ring() is K                                                  # needs sage.rings.finite_rings
            True

        and that it annihilates u::

            sage: chi(u)                                                                # needs sage.rings.finite_rings
            0

        Similarly, one can compute the minimal polynomial over F::

            sage: u.minpoly(F)                                                          # needs sage.rings.finite_rings
            x^6 + 4*x^5 + x^4 + 2*x^2 + 3

        A different variable name can be specified::

            sage: u.minpoly(F, var='t')                                                 # needs sage.rings.finite_rings
            t^6 + 4*t^5 + t^4 + 2*t^2 + 3

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: u.minpoly()                                                           # needs sage.rings.finite_rings
            x^2 + (2*a + a^2)*x - 1 + a

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: u.minpoly(GF(5^2))                                                    # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z2 of size 5^2

        TESTS:

        We check that the minimal polynomial of an element in the base
        ring has degree 1::

            sage: S.<x> = K[]                                                           # needs sage.rings.finite_rings
            sage: u = K.random_element()                                                # needs sage.rings.finite_rings
            sage: L(u).minpoly() == x - u                                               # needs sage.rings.finite_rings
            True

        In a similar fashion, the minimal polynomial over `F` of an element
        of `K` should have degree 1 or 3::

            sage: L(u).minpoly(F).degree() in [ 1, 3 ]                                  # needs sage.rings.finite_rings
            True"""
    @overload
    def minpoly(self, F) -> Any:
        """RingExtensionWithBasisElement.minpoly(self, base=None, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 1529)

        Return the minimal polynomial of this element over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None``

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5)
            sage: K.<a> = GF(5^3).over(F)
            sage: L.<b> = GF(5^6).over(K)
            sage: u = 1 / (a+b)
            sage: chi = u.minpoly(K); chi
            x^2 + (2*a + a^2)*x - 1 + a

        We check that the minimal polynomial has coefficients in the base ring::

            sage: chi.base_ring()                                                       # needs sage.rings.finite_rings
            Field in a with defining polynomial x^3 + 3*x + 3 over its base
            sage: chi.base_ring() is K                                                  # needs sage.rings.finite_rings
            True

        and that it annihilates u::

            sage: chi(u)                                                                # needs sage.rings.finite_rings
            0

        Similarly, one can compute the minimal polynomial over F::

            sage: u.minpoly(F)                                                          # needs sage.rings.finite_rings
            x^6 + 4*x^5 + x^4 + 2*x^2 + 3

        A different variable name can be specified::

            sage: u.minpoly(F, var='t')                                                 # needs sage.rings.finite_rings
            t^6 + 4*t^5 + t^4 + 2*t^2 + 3

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: u.minpoly()                                                           # needs sage.rings.finite_rings
            x^2 + (2*a + a^2)*x - 1 + a

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: u.minpoly(GF(5^2))                                                    # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z2 of size 5^2

        TESTS:

        We check that the minimal polynomial of an element in the base
        ring has degree 1::

            sage: S.<x> = K[]                                                           # needs sage.rings.finite_rings
            sage: u = K.random_element()                                                # needs sage.rings.finite_rings
            sage: L(u).minpoly() == x - u                                               # needs sage.rings.finite_rings
            True

        In a similar fashion, the minimal polynomial over `F` of an element
        of `K` should have degree 1 or 3::

            sage: L(u).minpoly(F).degree() in [ 1, 3 ]                                  # needs sage.rings.finite_rings
            True"""
    @overload
    def minpoly(self, F, var=...) -> Any:
        """RingExtensionWithBasisElement.minpoly(self, base=None, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 1529)

        Return the minimal polynomial of this element over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None``

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5)
            sage: K.<a> = GF(5^3).over(F)
            sage: L.<b> = GF(5^6).over(K)
            sage: u = 1 / (a+b)
            sage: chi = u.minpoly(K); chi
            x^2 + (2*a + a^2)*x - 1 + a

        We check that the minimal polynomial has coefficients in the base ring::

            sage: chi.base_ring()                                                       # needs sage.rings.finite_rings
            Field in a with defining polynomial x^3 + 3*x + 3 over its base
            sage: chi.base_ring() is K                                                  # needs sage.rings.finite_rings
            True

        and that it annihilates u::

            sage: chi(u)                                                                # needs sage.rings.finite_rings
            0

        Similarly, one can compute the minimal polynomial over F::

            sage: u.minpoly(F)                                                          # needs sage.rings.finite_rings
            x^6 + 4*x^5 + x^4 + 2*x^2 + 3

        A different variable name can be specified::

            sage: u.minpoly(F, var='t')                                                 # needs sage.rings.finite_rings
            t^6 + 4*t^5 + t^4 + 2*t^2 + 3

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: u.minpoly()                                                           # needs sage.rings.finite_rings
            x^2 + (2*a + a^2)*x - 1 + a

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: u.minpoly(GF(5^2))                                                    # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z2 of size 5^2

        TESTS:

        We check that the minimal polynomial of an element in the base
        ring has degree 1::

            sage: S.<x> = K[]                                                           # needs sage.rings.finite_rings
            sage: u = K.random_element()                                                # needs sage.rings.finite_rings
            sage: L(u).minpoly() == x - u                                               # needs sage.rings.finite_rings
            True

        In a similar fashion, the minimal polynomial over `F` of an element
        of `K` should have degree 1 or 3::

            sage: L(u).minpoly(F).degree() in [ 1, 3 ]                                  # needs sage.rings.finite_rings
            True"""
    @overload
    def minpoly(self) -> Any:
        """RingExtensionWithBasisElement.minpoly(self, base=None, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 1529)

        Return the minimal polynomial of this element over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None``

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5)
            sage: K.<a> = GF(5^3).over(F)
            sage: L.<b> = GF(5^6).over(K)
            sage: u = 1 / (a+b)
            sage: chi = u.minpoly(K); chi
            x^2 + (2*a + a^2)*x - 1 + a

        We check that the minimal polynomial has coefficients in the base ring::

            sage: chi.base_ring()                                                       # needs sage.rings.finite_rings
            Field in a with defining polynomial x^3 + 3*x + 3 over its base
            sage: chi.base_ring() is K                                                  # needs sage.rings.finite_rings
            True

        and that it annihilates u::

            sage: chi(u)                                                                # needs sage.rings.finite_rings
            0

        Similarly, one can compute the minimal polynomial over F::

            sage: u.minpoly(F)                                                          # needs sage.rings.finite_rings
            x^6 + 4*x^5 + x^4 + 2*x^2 + 3

        A different variable name can be specified::

            sage: u.minpoly(F, var='t')                                                 # needs sage.rings.finite_rings
            t^6 + 4*t^5 + t^4 + 2*t^2 + 3

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: u.minpoly()                                                           # needs sage.rings.finite_rings
            x^2 + (2*a + a^2)*x - 1 + a

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: u.minpoly(GF(5^2))                                                    # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z2 of size 5^2

        TESTS:

        We check that the minimal polynomial of an element in the base
        ring has degree 1::

            sage: S.<x> = K[]                                                           # needs sage.rings.finite_rings
            sage: u = K.random_element()                                                # needs sage.rings.finite_rings
            sage: L(u).minpoly() == x - u                                               # needs sage.rings.finite_rings
            True

        In a similar fashion, the minimal polynomial over `F` of an element
        of `K` should have degree 1 or 3::

            sage: L(u).minpoly(F).degree() in [ 1, 3 ]                                  # needs sage.rings.finite_rings
            True"""
    @overload
    def minpoly(self) -> Any:
        """RingExtensionWithBasisElement.minpoly(self, base=None, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 1529)

        Return the minimal polynomial of this element over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None``

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5)
            sage: K.<a> = GF(5^3).over(F)
            sage: L.<b> = GF(5^6).over(K)
            sage: u = 1 / (a+b)
            sage: chi = u.minpoly(K); chi
            x^2 + (2*a + a^2)*x - 1 + a

        We check that the minimal polynomial has coefficients in the base ring::

            sage: chi.base_ring()                                                       # needs sage.rings.finite_rings
            Field in a with defining polynomial x^3 + 3*x + 3 over its base
            sage: chi.base_ring() is K                                                  # needs sage.rings.finite_rings
            True

        and that it annihilates u::

            sage: chi(u)                                                                # needs sage.rings.finite_rings
            0

        Similarly, one can compute the minimal polynomial over F::

            sage: u.minpoly(F)                                                          # needs sage.rings.finite_rings
            x^6 + 4*x^5 + x^4 + 2*x^2 + 3

        A different variable name can be specified::

            sage: u.minpoly(F, var='t')                                                 # needs sage.rings.finite_rings
            t^6 + 4*t^5 + t^4 + 2*t^2 + 3

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: u.minpoly()                                                           # needs sage.rings.finite_rings
            x^2 + (2*a + a^2)*x - 1 + a

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: u.minpoly(GF(5^2))                                                    # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z2 of size 5^2

        TESTS:

        We check that the minimal polynomial of an element in the base
        ring has degree 1::

            sage: S.<x> = K[]                                                           # needs sage.rings.finite_rings
            sage: u = K.random_element()                                                # needs sage.rings.finite_rings
            sage: L(u).minpoly() == x - u                                               # needs sage.rings.finite_rings
            True

        In a similar fashion, the minimal polynomial over `F` of an element
        of `K` should have degree 1 or 3::

            sage: L(u).minpoly(F).degree() in [ 1, 3 ]                                  # needs sage.rings.finite_rings
            True"""
    @overload
    def minpoly(self, F) -> Any:
        """RingExtensionWithBasisElement.minpoly(self, base=None, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 1529)

        Return the minimal polynomial of this element over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None``

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5)
            sage: K.<a> = GF(5^3).over(F)
            sage: L.<b> = GF(5^6).over(K)
            sage: u = 1 / (a+b)
            sage: chi = u.minpoly(K); chi
            x^2 + (2*a + a^2)*x - 1 + a

        We check that the minimal polynomial has coefficients in the base ring::

            sage: chi.base_ring()                                                       # needs sage.rings.finite_rings
            Field in a with defining polynomial x^3 + 3*x + 3 over its base
            sage: chi.base_ring() is K                                                  # needs sage.rings.finite_rings
            True

        and that it annihilates u::

            sage: chi(u)                                                                # needs sage.rings.finite_rings
            0

        Similarly, one can compute the minimal polynomial over F::

            sage: u.minpoly(F)                                                          # needs sage.rings.finite_rings
            x^6 + 4*x^5 + x^4 + 2*x^2 + 3

        A different variable name can be specified::

            sage: u.minpoly(F, var='t')                                                 # needs sage.rings.finite_rings
            t^6 + 4*t^5 + t^4 + 2*t^2 + 3

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: u.minpoly()                                                           # needs sage.rings.finite_rings
            x^2 + (2*a + a^2)*x - 1 + a

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: u.minpoly(GF(5^2))                                                    # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z2 of size 5^2

        TESTS:

        We check that the minimal polynomial of an element in the base
        ring has degree 1::

            sage: S.<x> = K[]                                                           # needs sage.rings.finite_rings
            sage: u = K.random_element()                                                # needs sage.rings.finite_rings
            sage: L(u).minpoly() == x - u                                               # needs sage.rings.finite_rings
            True

        In a similar fashion, the minimal polynomial over `F` of an element
        of `K` should have degree 1 or 3::

            sage: L(u).minpoly(F).degree() in [ 1, 3 ]                                  # needs sage.rings.finite_rings
            True"""
    @overload
    def norm(self, base=...) -> Any:
        """RingExtensionWithBasisElement.norm(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 1369)

        Return the norm of this element over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None``

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5)
            sage: K.<a> = GF(5^3).over(F)
            sage: L.<b> = GF(5^6).over(K)
            sage: u = a/(1+b)
            sage: nr = u.norm(K); nr
            3 + 2*a^2

        We check that the norm lives in the base ring::

            sage: nr.parent()                                                           # needs sage.rings.finite_rings
            Field in a with defining polynomial x^3 + 3*x + 3 over its base
            sage: nr.parent() is K                                                      # needs sage.rings.finite_rings
            True

        Similarly, one can compute the norm over F::

            sage: u.norm(F)                                                             # needs sage.rings.finite_rings
            4

        We check the transitivity of the norm::

            sage: u.norm(F) == nr.norm(F)                                               # needs sage.rings.finite_rings
            True

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: u.norm()                                                              # needs sage.rings.finite_rings
            3 + 2*a^2

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: u.norm(GF(5^2))                                                       # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z2 of size 5^2"""
    @overload
    def norm(self, K) -> Any:
        """RingExtensionWithBasisElement.norm(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 1369)

        Return the norm of this element over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None``

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5)
            sage: K.<a> = GF(5^3).over(F)
            sage: L.<b> = GF(5^6).over(K)
            sage: u = a/(1+b)
            sage: nr = u.norm(K); nr
            3 + 2*a^2

        We check that the norm lives in the base ring::

            sage: nr.parent()                                                           # needs sage.rings.finite_rings
            Field in a with defining polynomial x^3 + 3*x + 3 over its base
            sage: nr.parent() is K                                                      # needs sage.rings.finite_rings
            True

        Similarly, one can compute the norm over F::

            sage: u.norm(F)                                                             # needs sage.rings.finite_rings
            4

        We check the transitivity of the norm::

            sage: u.norm(F) == nr.norm(F)                                               # needs sage.rings.finite_rings
            True

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: u.norm()                                                              # needs sage.rings.finite_rings
            3 + 2*a^2

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: u.norm(GF(5^2))                                                       # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z2 of size 5^2"""
    @overload
    def norm(self, F) -> Any:
        """RingExtensionWithBasisElement.norm(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 1369)

        Return the norm of this element over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None``

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5)
            sage: K.<a> = GF(5^3).over(F)
            sage: L.<b> = GF(5^6).over(K)
            sage: u = a/(1+b)
            sage: nr = u.norm(K); nr
            3 + 2*a^2

        We check that the norm lives in the base ring::

            sage: nr.parent()                                                           # needs sage.rings.finite_rings
            Field in a with defining polynomial x^3 + 3*x + 3 over its base
            sage: nr.parent() is K                                                      # needs sage.rings.finite_rings
            True

        Similarly, one can compute the norm over F::

            sage: u.norm(F)                                                             # needs sage.rings.finite_rings
            4

        We check the transitivity of the norm::

            sage: u.norm(F) == nr.norm(F)                                               # needs sage.rings.finite_rings
            True

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: u.norm()                                                              # needs sage.rings.finite_rings
            3 + 2*a^2

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: u.norm(GF(5^2))                                                       # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z2 of size 5^2"""
    @overload
    def norm(self) -> Any:
        """RingExtensionWithBasisElement.norm(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 1369)

        Return the norm of this element over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None``

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5)
            sage: K.<a> = GF(5^3).over(F)
            sage: L.<b> = GF(5^6).over(K)
            sage: u = a/(1+b)
            sage: nr = u.norm(K); nr
            3 + 2*a^2

        We check that the norm lives in the base ring::

            sage: nr.parent()                                                           # needs sage.rings.finite_rings
            Field in a with defining polynomial x^3 + 3*x + 3 over its base
            sage: nr.parent() is K                                                      # needs sage.rings.finite_rings
            True

        Similarly, one can compute the norm over F::

            sage: u.norm(F)                                                             # needs sage.rings.finite_rings
            4

        We check the transitivity of the norm::

            sage: u.norm(F) == nr.norm(F)                                               # needs sage.rings.finite_rings
            True

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: u.norm()                                                              # needs sage.rings.finite_rings
            3 + 2*a^2

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: u.norm(GF(5^2))                                                       # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z2 of size 5^2"""
    @overload
    def polynomial(self, base=..., var=...) -> Any:
        """RingExtensionWithBasisElement.polynomial(self, base=None, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 1102)

        Return a polynomial (in one or more variables) over ``base``
        whose evaluation at the generators of the parent equals this
        element.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None``

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF(5^2).over()  # over GF(5)
            sage: K.<b> = GF(5^4).over(F)
            sage: L.<c> = GF(5^12).over(K)
            sage: u = 1/(a + b + c); u
            (2 + (-1 - a)*b) + ((2 + 3*a) + (1 - a)*b)*c + ((-1 - a) - a*b)*c^2
            sage: P = u.polynomial(K); P
            ((-1 - a) - a*b)*x^2 + ((2 + 3*a) + (1 - a)*b)*x + 2 + (-1 - a)*b
            sage: P.base_ring() is K
            True
            sage: P(c) == u
            True

        When the base is `F`, we obtain a bivariate polynomial::

            sage: P = u.polynomial(F); P                                                # needs sage.rings.finite_rings
            (-a)*x0^2*x1 + (-1 - a)*x0^2 + (1 - a)*x0*x1 + (2 + 3*a)*x0 + (-1 - a)*x1 + 2

        We check that its value at the generators is the element we started with::

            sage: L.gens(F)                                                             # needs sage.rings.finite_rings
            (c, b)
            sage: P(c, b) == u                                                          # needs sage.rings.finite_rings
            True

        Similarly, when the base is ``GF(5)``, we get a trivariate polynomial:

            sage: P = u.polynomial(GF(5)); P                                            # needs sage.rings.finite_rings
            -x0^2*x1*x2 - x0^2*x2 - x0*x1*x2 - x0^2 + x0*x1 - 2*x0*x2 - x1*x2 + 2*x0 - x1 + 2
            sage: P(c, b, a) == u                                                       # needs sage.rings.finite_rings
            True

        Different variable names can be specified::

            sage: u.polynomial(GF(5), var='y')                                          # needs sage.rings.finite_rings
            -y0^2*y1*y2 - y0^2*y2 - y0*y1*y2 - y0^2 + y0*y1 - 2*y0*y2 - y1*y2 + 2*y0 - y1 + 2
            sage: u.polynomial(GF(5), var=['x','y','z'])                                # needs sage.rings.finite_rings
            -x^2*y*z - x^2*z - x*y*z - x^2 + x*y - 2*x*z - y*z + 2*x - y + 2

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: u.polynomial()                                                        # needs sage.rings.finite_rings
            ((-1 - a) - a*b)*x^2 + ((2 + 3*a) + (1 - a)*b)*x + 2 + (-1 - a)*b

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: u.polynomial(GF(5^3))                                                 # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z3 of size 5^3"""
    @overload
    def polynomial(self, inoneormorevariables) -> Any:
        """RingExtensionWithBasisElement.polynomial(self, base=None, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 1102)

        Return a polynomial (in one or more variables) over ``base``
        whose evaluation at the generators of the parent equals this
        element.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None``

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF(5^2).over()  # over GF(5)
            sage: K.<b> = GF(5^4).over(F)
            sage: L.<c> = GF(5^12).over(K)
            sage: u = 1/(a + b + c); u
            (2 + (-1 - a)*b) + ((2 + 3*a) + (1 - a)*b)*c + ((-1 - a) - a*b)*c^2
            sage: P = u.polynomial(K); P
            ((-1 - a) - a*b)*x^2 + ((2 + 3*a) + (1 - a)*b)*x + 2 + (-1 - a)*b
            sage: P.base_ring() is K
            True
            sage: P(c) == u
            True

        When the base is `F`, we obtain a bivariate polynomial::

            sage: P = u.polynomial(F); P                                                # needs sage.rings.finite_rings
            (-a)*x0^2*x1 + (-1 - a)*x0^2 + (1 - a)*x0*x1 + (2 + 3*a)*x0 + (-1 - a)*x1 + 2

        We check that its value at the generators is the element we started with::

            sage: L.gens(F)                                                             # needs sage.rings.finite_rings
            (c, b)
            sage: P(c, b) == u                                                          # needs sage.rings.finite_rings
            True

        Similarly, when the base is ``GF(5)``, we get a trivariate polynomial:

            sage: P = u.polynomial(GF(5)); P                                            # needs sage.rings.finite_rings
            -x0^2*x1*x2 - x0^2*x2 - x0*x1*x2 - x0^2 + x0*x1 - 2*x0*x2 - x1*x2 + 2*x0 - x1 + 2
            sage: P(c, b, a) == u                                                       # needs sage.rings.finite_rings
            True

        Different variable names can be specified::

            sage: u.polynomial(GF(5), var='y')                                          # needs sage.rings.finite_rings
            -y0^2*y1*y2 - y0^2*y2 - y0*y1*y2 - y0^2 + y0*y1 - 2*y0*y2 - y1*y2 + 2*y0 - y1 + 2
            sage: u.polynomial(GF(5), var=['x','y','z'])                                # needs sage.rings.finite_rings
            -x^2*y*z - x^2*z - x*y*z - x^2 + x*y - 2*x*z - y*z + 2*x - y + 2

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: u.polynomial()                                                        # needs sage.rings.finite_rings
            ((-1 - a) - a*b)*x^2 + ((2 + 3*a) + (1 - a)*b)*x + 2 + (-1 - a)*b

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: u.polynomial(GF(5^3))                                                 # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z3 of size 5^3"""
    @overload
    def polynomial(self, K) -> Any:
        """RingExtensionWithBasisElement.polynomial(self, base=None, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 1102)

        Return a polynomial (in one or more variables) over ``base``
        whose evaluation at the generators of the parent equals this
        element.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None``

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF(5^2).over()  # over GF(5)
            sage: K.<b> = GF(5^4).over(F)
            sage: L.<c> = GF(5^12).over(K)
            sage: u = 1/(a + b + c); u
            (2 + (-1 - a)*b) + ((2 + 3*a) + (1 - a)*b)*c + ((-1 - a) - a*b)*c^2
            sage: P = u.polynomial(K); P
            ((-1 - a) - a*b)*x^2 + ((2 + 3*a) + (1 - a)*b)*x + 2 + (-1 - a)*b
            sage: P.base_ring() is K
            True
            sage: P(c) == u
            True

        When the base is `F`, we obtain a bivariate polynomial::

            sage: P = u.polynomial(F); P                                                # needs sage.rings.finite_rings
            (-a)*x0^2*x1 + (-1 - a)*x0^2 + (1 - a)*x0*x1 + (2 + 3*a)*x0 + (-1 - a)*x1 + 2

        We check that its value at the generators is the element we started with::

            sage: L.gens(F)                                                             # needs sage.rings.finite_rings
            (c, b)
            sage: P(c, b) == u                                                          # needs sage.rings.finite_rings
            True

        Similarly, when the base is ``GF(5)``, we get a trivariate polynomial:

            sage: P = u.polynomial(GF(5)); P                                            # needs sage.rings.finite_rings
            -x0^2*x1*x2 - x0^2*x2 - x0*x1*x2 - x0^2 + x0*x1 - 2*x0*x2 - x1*x2 + 2*x0 - x1 + 2
            sage: P(c, b, a) == u                                                       # needs sage.rings.finite_rings
            True

        Different variable names can be specified::

            sage: u.polynomial(GF(5), var='y')                                          # needs sage.rings.finite_rings
            -y0^2*y1*y2 - y0^2*y2 - y0*y1*y2 - y0^2 + y0*y1 - 2*y0*y2 - y1*y2 + 2*y0 - y1 + 2
            sage: u.polynomial(GF(5), var=['x','y','z'])                                # needs sage.rings.finite_rings
            -x^2*y*z - x^2*z - x*y*z - x^2 + x*y - 2*x*z - y*z + 2*x - y + 2

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: u.polynomial()                                                        # needs sage.rings.finite_rings
            ((-1 - a) - a*b)*x^2 + ((2 + 3*a) + (1 - a)*b)*x + 2 + (-1 - a)*b

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: u.polynomial(GF(5^3))                                                 # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z3 of size 5^3"""
    @overload
    def polynomial(self, F) -> Any:
        """RingExtensionWithBasisElement.polynomial(self, base=None, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 1102)

        Return a polynomial (in one or more variables) over ``base``
        whose evaluation at the generators of the parent equals this
        element.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None``

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF(5^2).over()  # over GF(5)
            sage: K.<b> = GF(5^4).over(F)
            sage: L.<c> = GF(5^12).over(K)
            sage: u = 1/(a + b + c); u
            (2 + (-1 - a)*b) + ((2 + 3*a) + (1 - a)*b)*c + ((-1 - a) - a*b)*c^2
            sage: P = u.polynomial(K); P
            ((-1 - a) - a*b)*x^2 + ((2 + 3*a) + (1 - a)*b)*x + 2 + (-1 - a)*b
            sage: P.base_ring() is K
            True
            sage: P(c) == u
            True

        When the base is `F`, we obtain a bivariate polynomial::

            sage: P = u.polynomial(F); P                                                # needs sage.rings.finite_rings
            (-a)*x0^2*x1 + (-1 - a)*x0^2 + (1 - a)*x0*x1 + (2 + 3*a)*x0 + (-1 - a)*x1 + 2

        We check that its value at the generators is the element we started with::

            sage: L.gens(F)                                                             # needs sage.rings.finite_rings
            (c, b)
            sage: P(c, b) == u                                                          # needs sage.rings.finite_rings
            True

        Similarly, when the base is ``GF(5)``, we get a trivariate polynomial:

            sage: P = u.polynomial(GF(5)); P                                            # needs sage.rings.finite_rings
            -x0^2*x1*x2 - x0^2*x2 - x0*x1*x2 - x0^2 + x0*x1 - 2*x0*x2 - x1*x2 + 2*x0 - x1 + 2
            sage: P(c, b, a) == u                                                       # needs sage.rings.finite_rings
            True

        Different variable names can be specified::

            sage: u.polynomial(GF(5), var='y')                                          # needs sage.rings.finite_rings
            -y0^2*y1*y2 - y0^2*y2 - y0*y1*y2 - y0^2 + y0*y1 - 2*y0*y2 - y1*y2 + 2*y0 - y1 + 2
            sage: u.polynomial(GF(5), var=['x','y','z'])                                # needs sage.rings.finite_rings
            -x^2*y*z - x^2*z - x*y*z - x^2 + x*y - 2*x*z - y*z + 2*x - y + 2

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: u.polynomial()                                                        # needs sage.rings.finite_rings
            ((-1 - a) - a*b)*x^2 + ((2 + 3*a) + (1 - a)*b)*x + 2 + (-1 - a)*b

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: u.polynomial(GF(5^3))                                                 # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z3 of size 5^3"""
    @overload
    def polynomial(self) -> Any:
        """RingExtensionWithBasisElement.polynomial(self, base=None, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 1102)

        Return a polynomial (in one or more variables) over ``base``
        whose evaluation at the generators of the parent equals this
        element.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None``

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF(5^2).over()  # over GF(5)
            sage: K.<b> = GF(5^4).over(F)
            sage: L.<c> = GF(5^12).over(K)
            sage: u = 1/(a + b + c); u
            (2 + (-1 - a)*b) + ((2 + 3*a) + (1 - a)*b)*c + ((-1 - a) - a*b)*c^2
            sage: P = u.polynomial(K); P
            ((-1 - a) - a*b)*x^2 + ((2 + 3*a) + (1 - a)*b)*x + 2 + (-1 - a)*b
            sage: P.base_ring() is K
            True
            sage: P(c) == u
            True

        When the base is `F`, we obtain a bivariate polynomial::

            sage: P = u.polynomial(F); P                                                # needs sage.rings.finite_rings
            (-a)*x0^2*x1 + (-1 - a)*x0^2 + (1 - a)*x0*x1 + (2 + 3*a)*x0 + (-1 - a)*x1 + 2

        We check that its value at the generators is the element we started with::

            sage: L.gens(F)                                                             # needs sage.rings.finite_rings
            (c, b)
            sage: P(c, b) == u                                                          # needs sage.rings.finite_rings
            True

        Similarly, when the base is ``GF(5)``, we get a trivariate polynomial:

            sage: P = u.polynomial(GF(5)); P                                            # needs sage.rings.finite_rings
            -x0^2*x1*x2 - x0^2*x2 - x0*x1*x2 - x0^2 + x0*x1 - 2*x0*x2 - x1*x2 + 2*x0 - x1 + 2
            sage: P(c, b, a) == u                                                       # needs sage.rings.finite_rings
            True

        Different variable names can be specified::

            sage: u.polynomial(GF(5), var='y')                                          # needs sage.rings.finite_rings
            -y0^2*y1*y2 - y0^2*y2 - y0*y1*y2 - y0^2 + y0*y1 - 2*y0*y2 - y1*y2 + 2*y0 - y1 + 2
            sage: u.polynomial(GF(5), var=['x','y','z'])                                # needs sage.rings.finite_rings
            -x^2*y*z - x^2*z - x*y*z - x^2 + x*y - 2*x*z - y*z + 2*x - y + 2

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: u.polynomial()                                                        # needs sage.rings.finite_rings
            ((-1 - a) - a*b)*x^2 + ((2 + 3*a) + (1 - a)*b)*x + 2 + (-1 - a)*b

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: u.polynomial(GF(5^3))                                                 # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z3 of size 5^3"""
    @overload
    def trace(self, base=...) -> Any:
        """RingExtensionWithBasisElement.trace(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 1276)

        Return the trace of this element over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None``

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5)
            sage: K.<a> = GF(5^3).over(F)
            sage: L.<b> = GF(5^6).over(K)
            sage: u = a/(1+b)
            sage: tr = u.trace(K); tr
            -1 + 3*a + 2*a^2

        We check that the trace lives in the base ring::

            sage: tr.parent()                                                           # needs sage.rings.finite_rings
            Field in a with defining polynomial x^3 + 3*x + 3 over its base
            sage: tr.parent() is K                                                      # needs sage.rings.finite_rings
            True

        Similarly, one can compute the trace over F::

            sage: u.trace(F)                                                            # needs sage.rings.finite_rings
            0

        We check the transitivity of the trace::

            sage: u.trace(F) == tr.trace(F)                                             # needs sage.rings.finite_rings
            True

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: u.trace()                                                             # needs sage.rings.finite_rings
            -1 + 3*a + 2*a^2

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: u.trace(GF(5^2))                                                      # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z2 of size 5^2"""
    @overload
    def trace(self, K) -> Any:
        """RingExtensionWithBasisElement.trace(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 1276)

        Return the trace of this element over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None``

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5)
            sage: K.<a> = GF(5^3).over(F)
            sage: L.<b> = GF(5^6).over(K)
            sage: u = a/(1+b)
            sage: tr = u.trace(K); tr
            -1 + 3*a + 2*a^2

        We check that the trace lives in the base ring::

            sage: tr.parent()                                                           # needs sage.rings.finite_rings
            Field in a with defining polynomial x^3 + 3*x + 3 over its base
            sage: tr.parent() is K                                                      # needs sage.rings.finite_rings
            True

        Similarly, one can compute the trace over F::

            sage: u.trace(F)                                                            # needs sage.rings.finite_rings
            0

        We check the transitivity of the trace::

            sage: u.trace(F) == tr.trace(F)                                             # needs sage.rings.finite_rings
            True

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: u.trace()                                                             # needs sage.rings.finite_rings
            -1 + 3*a + 2*a^2

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: u.trace(GF(5^2))                                                      # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z2 of size 5^2"""
    @overload
    def trace(self, F) -> Any:
        """RingExtensionWithBasisElement.trace(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 1276)

        Return the trace of this element over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None``

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5)
            sage: K.<a> = GF(5^3).over(F)
            sage: L.<b> = GF(5^6).over(K)
            sage: u = a/(1+b)
            sage: tr = u.trace(K); tr
            -1 + 3*a + 2*a^2

        We check that the trace lives in the base ring::

            sage: tr.parent()                                                           # needs sage.rings.finite_rings
            Field in a with defining polynomial x^3 + 3*x + 3 over its base
            sage: tr.parent() is K                                                      # needs sage.rings.finite_rings
            True

        Similarly, one can compute the trace over F::

            sage: u.trace(F)                                                            # needs sage.rings.finite_rings
            0

        We check the transitivity of the trace::

            sage: u.trace(F) == tr.trace(F)                                             # needs sage.rings.finite_rings
            True

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: u.trace()                                                             # needs sage.rings.finite_rings
            -1 + 3*a + 2*a^2

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: u.trace(GF(5^2))                                                      # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z2 of size 5^2"""
    @overload
    def trace(self) -> Any:
        """RingExtensionWithBasisElement.trace(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 1276)

        Return the trace of this element over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None``

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5)
            sage: K.<a> = GF(5^3).over(F)
            sage: L.<b> = GF(5^6).over(K)
            sage: u = a/(1+b)
            sage: tr = u.trace(K); tr
            -1 + 3*a + 2*a^2

        We check that the trace lives in the base ring::

            sage: tr.parent()                                                           # needs sage.rings.finite_rings
            Field in a with defining polynomial x^3 + 3*x + 3 over its base
            sage: tr.parent() is K                                                      # needs sage.rings.finite_rings
            True

        Similarly, one can compute the trace over F::

            sage: u.trace(F)                                                            # needs sage.rings.finite_rings
            0

        We check the transitivity of the trace::

            sage: u.trace(F) == tr.trace(F)                                             # needs sage.rings.finite_rings
            True

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: u.trace()                                                             # needs sage.rings.finite_rings
            -1 + 3*a + 2*a^2

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: u.trace(GF(5^2))                                                      # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z2 of size 5^2"""
    @overload
    def vector(self, base=...) -> Any:
        """RingExtensionWithBasisElement.vector(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 1039)

        Return the vector of coordinates of this element over ``base``
        (in the basis output by the method :meth:`basis_over`).

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None``

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5)
            sage: K.<a> = GF(5^2).over()  # over F
            sage: L.<b> = GF(5^6).over(K)
            sage: x = (a+b)^4; x
            (-1 + a) + (3 + a)*b + (1 - a)*b^2
            sage: x.vector(K)                   # basis is (1, b, b^2)
            (-1 + a, 3 + a, 1 - a)
            sage: x.vector(F)                   # basis is (1, a, b, a*b, b^2, a*b^2)
            (4, 1, 3, 1, 1, 4)

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: x.vector()                                                            # needs sage.rings.finite_rings
            (-1 + a, 3 + a, 1 - a)

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: x.vector(GF(5^3))                                                     # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z3 of size 5^3"""
    @overload
    def vector(self, K) -> Any:
        """RingExtensionWithBasisElement.vector(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 1039)

        Return the vector of coordinates of this element over ``base``
        (in the basis output by the method :meth:`basis_over`).

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None``

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5)
            sage: K.<a> = GF(5^2).over()  # over F
            sage: L.<b> = GF(5^6).over(K)
            sage: x = (a+b)^4; x
            (-1 + a) + (3 + a)*b + (1 - a)*b^2
            sage: x.vector(K)                   # basis is (1, b, b^2)
            (-1 + a, 3 + a, 1 - a)
            sage: x.vector(F)                   # basis is (1, a, b, a*b, b^2, a*b^2)
            (4, 1, 3, 1, 1, 4)

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: x.vector()                                                            # needs sage.rings.finite_rings
            (-1 + a, 3 + a, 1 - a)

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: x.vector(GF(5^3))                                                     # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z3 of size 5^3"""
    @overload
    def vector(self, F) -> Any:
        """RingExtensionWithBasisElement.vector(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 1039)

        Return the vector of coordinates of this element over ``base``
        (in the basis output by the method :meth:`basis_over`).

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None``

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5)
            sage: K.<a> = GF(5^2).over()  # over F
            sage: L.<b> = GF(5^6).over(K)
            sage: x = (a+b)^4; x
            (-1 + a) + (3 + a)*b + (1 - a)*b^2
            sage: x.vector(K)                   # basis is (1, b, b^2)
            (-1 + a, 3 + a, 1 - a)
            sage: x.vector(F)                   # basis is (1, a, b, a*b, b^2, a*b^2)
            (4, 1, 3, 1, 1, 4)

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: x.vector()                                                            # needs sage.rings.finite_rings
            (-1 + a, 3 + a, 1 - a)

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: x.vector(GF(5^3))                                                     # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z3 of size 5^3"""
    @overload
    def vector(self) -> Any:
        """RingExtensionWithBasisElement.vector(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 1039)

        Return the vector of coordinates of this element over ``base``
        (in the basis output by the method :meth:`basis_over`).

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None``

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5)
            sage: K.<a> = GF(5^2).over()  # over F
            sage: L.<b> = GF(5^6).over(K)
            sage: x = (a+b)^4; x
            (-1 + a) + (3 + a)*b + (1 - a)*b^2
            sage: x.vector(K)                   # basis is (1, b, b^2)
            (-1 + a, 3 + a, 1 - a)
            sage: x.vector(F)                   # basis is (1, a, b, a*b, b^2, a*b^2)
            (4, 1, 3, 1, 1, 4)

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: x.vector()                                                            # needs sage.rings.finite_rings
            (-1 + a, 3 + a, 1 - a)

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: x.vector(GF(5^3))                                                     # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z3 of size 5^3"""
    def __hash__(self) -> Any:
        """RingExtensionWithBasisElement.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_element.pyx (starting at line 882)

        Return a hash of this element.

        EXAMPLES:

            sage: E.<a> = GF(5^3).over()                                                # needs sage.rings.finite_rings
            sage: hash(a)                                                               # needs sage.rings.finite_rings
            5"""
