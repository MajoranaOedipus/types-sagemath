import sage.rings.padics.padic_generic_element
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

class pAdicExtElement(sage.rings.padics.padic_generic_element.pAdicGenericElement):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def frobenius(self, arithmetic=...) -> Any:
        """pAdicExtElement.frobenius(self, arithmetic=True)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ext_element.pyx (starting at line 335)

        Return the image of this element under the Frobenius automorphism
        applied to its parent.

        INPUT:

        - ``arithmetic`` -- whether to apply the arithmetic Frobenius (acting
          by raising to the `p`-th power on the residue field). If ``False`` is
          provided, the image of geometric Frobenius (raising to the `(1/p)`-th
          power on the residue field) will be returned instead.

        EXAMPLES::

            sage: R.<a> = Zq(5^4,3)
            sage: a.frobenius()
            (a^3 + a^2 + 3*a) + (3*a + 1)*5 + (2*a^3 + 2*a^2 + 2*a)*5^2 + O(5^3)
            sage: f = R.defining_polynomial()
            sage: f(a)
            O(5^3)
            sage: f(a.frobenius())
            O(5^3)
            sage: for i in range(4): a = a.frobenius()
            sage: a
            a + O(5^3)

            sage: K.<a> = Qq(7^3,4)
            sage: b = (a+1)/7
            sage: c = b.frobenius(); c
            (3*a^2 + 5*a + 1)*7^-1 + (6*a^2 + 6*a + 6) + (4*a^2 + 3*a + 4)*7 + (6*a^2 + a + 6)*7^2 + O(7^3)
            sage: c.frobenius().frobenius()
            (a + 1)*7^-1 + O(7^3)

        An error will be raised if the parent of ``self`` is a ramified extension::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = Qp(5).extension(x^2 - 5)
            sage: a.frobenius()
            Traceback (most recent call last):
            ...
            NotImplementedError: Frobenius automorphism only implemented for unramified extensions"""
    @overload
    def frobenius(self) -> Any:
        """pAdicExtElement.frobenius(self, arithmetic=True)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ext_element.pyx (starting at line 335)

        Return the image of this element under the Frobenius automorphism
        applied to its parent.

        INPUT:

        - ``arithmetic`` -- whether to apply the arithmetic Frobenius (acting
          by raising to the `p`-th power on the residue field). If ``False`` is
          provided, the image of geometric Frobenius (raising to the `(1/p)`-th
          power on the residue field) will be returned instead.

        EXAMPLES::

            sage: R.<a> = Zq(5^4,3)
            sage: a.frobenius()
            (a^3 + a^2 + 3*a) + (3*a + 1)*5 + (2*a^3 + 2*a^2 + 2*a)*5^2 + O(5^3)
            sage: f = R.defining_polynomial()
            sage: f(a)
            O(5^3)
            sage: f(a.frobenius())
            O(5^3)
            sage: for i in range(4): a = a.frobenius()
            sage: a
            a + O(5^3)

            sage: K.<a> = Qq(7^3,4)
            sage: b = (a+1)/7
            sage: c = b.frobenius(); c
            (3*a^2 + 5*a + 1)*7^-1 + (6*a^2 + 6*a + 6) + (4*a^2 + 3*a + 4)*7 + (6*a^2 + a + 6)*7^2 + O(7^3)
            sage: c.frobenius().frobenius()
            (a + 1)*7^-1 + O(7^3)

        An error will be raised if the parent of ``self`` is a ramified extension::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = Qp(5).extension(x^2 - 5)
            sage: a.frobenius()
            Traceback (most recent call last):
            ...
            NotImplementedError: Frobenius automorphism only implemented for unramified extensions"""
    @overload
    def frobenius(self) -> Any:
        """pAdicExtElement.frobenius(self, arithmetic=True)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ext_element.pyx (starting at line 335)

        Return the image of this element under the Frobenius automorphism
        applied to its parent.

        INPUT:

        - ``arithmetic`` -- whether to apply the arithmetic Frobenius (acting
          by raising to the `p`-th power on the residue field). If ``False`` is
          provided, the image of geometric Frobenius (raising to the `(1/p)`-th
          power on the residue field) will be returned instead.

        EXAMPLES::

            sage: R.<a> = Zq(5^4,3)
            sage: a.frobenius()
            (a^3 + a^2 + 3*a) + (3*a + 1)*5 + (2*a^3 + 2*a^2 + 2*a)*5^2 + O(5^3)
            sage: f = R.defining_polynomial()
            sage: f(a)
            O(5^3)
            sage: f(a.frobenius())
            O(5^3)
            sage: for i in range(4): a = a.frobenius()
            sage: a
            a + O(5^3)

            sage: K.<a> = Qq(7^3,4)
            sage: b = (a+1)/7
            sage: c = b.frobenius(); c
            (3*a^2 + 5*a + 1)*7^-1 + (6*a^2 + 6*a + 6) + (4*a^2 + 3*a + 4)*7 + (6*a^2 + a + 6)*7^2 + O(7^3)
            sage: c.frobenius().frobenius()
            (a + 1)*7^-1 + O(7^3)

        An error will be raised if the parent of ``self`` is a ramified extension::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = Qp(5).extension(x^2 - 5)
            sage: a.frobenius()
            Traceback (most recent call last):
            ...
            NotImplementedError: Frobenius automorphism only implemented for unramified extensions"""
    @overload
    def frobenius(self) -> Any:
        """pAdicExtElement.frobenius(self, arithmetic=True)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ext_element.pyx (starting at line 335)

        Return the image of this element under the Frobenius automorphism
        applied to its parent.

        INPUT:

        - ``arithmetic`` -- whether to apply the arithmetic Frobenius (acting
          by raising to the `p`-th power on the residue field). If ``False`` is
          provided, the image of geometric Frobenius (raising to the `(1/p)`-th
          power on the residue field) will be returned instead.

        EXAMPLES::

            sage: R.<a> = Zq(5^4,3)
            sage: a.frobenius()
            (a^3 + a^2 + 3*a) + (3*a + 1)*5 + (2*a^3 + 2*a^2 + 2*a)*5^2 + O(5^3)
            sage: f = R.defining_polynomial()
            sage: f(a)
            O(5^3)
            sage: f(a.frobenius())
            O(5^3)
            sage: for i in range(4): a = a.frobenius()
            sage: a
            a + O(5^3)

            sage: K.<a> = Qq(7^3,4)
            sage: b = (a+1)/7
            sage: c = b.frobenius(); c
            (3*a^2 + 5*a + 1)*7^-1 + (6*a^2 + 6*a + 6) + (4*a^2 + 3*a + 4)*7 + (6*a^2 + a + 6)*7^2 + O(7^3)
            sage: c.frobenius().frobenius()
            (a + 1)*7^-1 + O(7^3)

        An error will be raised if the parent of ``self`` is a ramified extension::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = Qp(5).extension(x^2 - 5)
            sage: a.frobenius()
            Traceback (most recent call last):
            ...
            NotImplementedError: Frobenius automorphism only implemented for unramified extensions"""
    @overload
    def frobenius(self) -> Any:
        """pAdicExtElement.frobenius(self, arithmetic=True)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ext_element.pyx (starting at line 335)

        Return the image of this element under the Frobenius automorphism
        applied to its parent.

        INPUT:

        - ``arithmetic`` -- whether to apply the arithmetic Frobenius (acting
          by raising to the `p`-th power on the residue field). If ``False`` is
          provided, the image of geometric Frobenius (raising to the `(1/p)`-th
          power on the residue field) will be returned instead.

        EXAMPLES::

            sage: R.<a> = Zq(5^4,3)
            sage: a.frobenius()
            (a^3 + a^2 + 3*a) + (3*a + 1)*5 + (2*a^3 + 2*a^2 + 2*a)*5^2 + O(5^3)
            sage: f = R.defining_polynomial()
            sage: f(a)
            O(5^3)
            sage: f(a.frobenius())
            O(5^3)
            sage: for i in range(4): a = a.frobenius()
            sage: a
            a + O(5^3)

            sage: K.<a> = Qq(7^3,4)
            sage: b = (a+1)/7
            sage: c = b.frobenius(); c
            (3*a^2 + 5*a + 1)*7^-1 + (6*a^2 + 6*a + 6) + (4*a^2 + 3*a + 4)*7 + (6*a^2 + a + 6)*7^2 + O(7^3)
            sage: c.frobenius().frobenius()
            (a + 1)*7^-1 + O(7^3)

        An error will be raised if the parent of ``self`` is a ramified extension::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = Qp(5).extension(x^2 - 5)
            sage: a.frobenius()
            Traceback (most recent call last):
            ...
            NotImplementedError: Frobenius automorphism only implemented for unramified extensions"""
    @overload
    def frobenius(self) -> Any:
        """pAdicExtElement.frobenius(self, arithmetic=True)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ext_element.pyx (starting at line 335)

        Return the image of this element under the Frobenius automorphism
        applied to its parent.

        INPUT:

        - ``arithmetic`` -- whether to apply the arithmetic Frobenius (acting
          by raising to the `p`-th power on the residue field). If ``False`` is
          provided, the image of geometric Frobenius (raising to the `(1/p)`-th
          power on the residue field) will be returned instead.

        EXAMPLES::

            sage: R.<a> = Zq(5^4,3)
            sage: a.frobenius()
            (a^3 + a^2 + 3*a) + (3*a + 1)*5 + (2*a^3 + 2*a^2 + 2*a)*5^2 + O(5^3)
            sage: f = R.defining_polynomial()
            sage: f(a)
            O(5^3)
            sage: f(a.frobenius())
            O(5^3)
            sage: for i in range(4): a = a.frobenius()
            sage: a
            a + O(5^3)

            sage: K.<a> = Qq(7^3,4)
            sage: b = (a+1)/7
            sage: c = b.frobenius(); c
            (3*a^2 + 5*a + 1)*7^-1 + (6*a^2 + 6*a + 6) + (4*a^2 + 3*a + 4)*7 + (6*a^2 + a + 6)*7^2 + O(7^3)
            sage: c.frobenius().frobenius()
            (a + 1)*7^-1 + O(7^3)

        An error will be raised if the parent of ``self`` is a ramified extension::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = Qp(5).extension(x^2 - 5)
            sage: a.frobenius()
            Traceback (most recent call last):
            ...
            NotImplementedError: Frobenius automorphism only implemented for unramified extensions"""
    @overload
    def frobenius(self) -> Any:
        """pAdicExtElement.frobenius(self, arithmetic=True)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ext_element.pyx (starting at line 335)

        Return the image of this element under the Frobenius automorphism
        applied to its parent.

        INPUT:

        - ``arithmetic`` -- whether to apply the arithmetic Frobenius (acting
          by raising to the `p`-th power on the residue field). If ``False`` is
          provided, the image of geometric Frobenius (raising to the `(1/p)`-th
          power on the residue field) will be returned instead.

        EXAMPLES::

            sage: R.<a> = Zq(5^4,3)
            sage: a.frobenius()
            (a^3 + a^2 + 3*a) + (3*a + 1)*5 + (2*a^3 + 2*a^2 + 2*a)*5^2 + O(5^3)
            sage: f = R.defining_polynomial()
            sage: f(a)
            O(5^3)
            sage: f(a.frobenius())
            O(5^3)
            sage: for i in range(4): a = a.frobenius()
            sage: a
            a + O(5^3)

            sage: K.<a> = Qq(7^3,4)
            sage: b = (a+1)/7
            sage: c = b.frobenius(); c
            (3*a^2 + 5*a + 1)*7^-1 + (6*a^2 + 6*a + 6) + (4*a^2 + 3*a + 4)*7 + (6*a^2 + a + 6)*7^2 + O(7^3)
            sage: c.frobenius().frobenius()
            (a + 1)*7^-1 + O(7^3)

        An error will be raised if the parent of ``self`` is a ramified extension::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = Qp(5).extension(x^2 - 5)
            sage: a.frobenius()
            Traceback (most recent call last):
            ...
            NotImplementedError: Frobenius automorphism only implemented for unramified extensions"""
    def residue(self, absprec=..., field=..., check_prec=...) -> Any:
        """pAdicExtElement.residue(self, absprec=1, field=None, check_prec=True)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ext_element.pyx (starting at line 411)

        Reduces this element modulo `\\pi^\\mathrm{absprec}`.

        INPUT:

        - ``absprec`` -- nonnegative integer (default: 1)

        - ``field`` -- boolean (default: ``None``); for precision 1, whether to return
          an element of the residue field or a residue ring.  Currently unused.

        - ``check_prec`` -- boolean (default: ``True``); whether to raise an error if this
          element has insufficient precision to determine the reduction.  Errors are never
          raised for fixed-mod or floating-point types.

        OUTPUT: this element reduced modulo `\\pi^\\mathrm{absprec}`

        If ``absprec`` is zero, then as an element of `\\ZZ/(1)`.

        If ``absprec`` is one, then as an element of the residue field.

        .. NOTE::

            Only implemented for ``absprec`` less than or equal to one.

        AUTHORS:

        - Julian Rueth (2012-10-18): initial version

        EXAMPLES:

        Unramified case::

            sage: # needs sage.libs.flint
            sage: R = ZpCA(3,5)
            sage: S.<a> = R[]
            sage: W.<a> = R.extension(a^2 + 9*a + 1)
            sage: (a + 1).residue(1)
            a0 + 1
            sage: a.residue(2)
            Traceback (most recent call last):
            ...
            NotImplementedError: reduction modulo p^n with n>1

        Eisenstein case::

            sage: R = ZpCA(3,5)
            sage: S.<a> = R[]
            sage: W.<a> = R.extension(a^2 + 9*a + 3)
            sage: (a + 1).residue(1)
            1
            sage: a.residue(2)
            Traceback (most recent call last):
            ...
            NotImplementedError: residue() not implemented in extensions for absprec larger than one

        TESTS::

            sage: # needs sage.libs.flint
            sage: K = Qp(3,5)
            sage: S.<a> = R[]
            sage: W.<a> = R.extension(a^2 + 9*a + 1)
            sage: (a/3).residue(0)
            Traceback (most recent call last):
            ...
            ValueError: element must have nonnegative valuation in order to compute residue

            sage: # needs sage.libs.flint
            sage: R = ZpFM(3,5)
            sage: S.<a> = R[]
            sage: W.<a> = R.extension(a^2 + 3)
            sage: W.one().residue(0)
            0
            sage: a.residue(-1)
            Traceback (most recent call last):
            ...
            ValueError: cannot reduce modulo a negative power of the uniformizer
            sage: a.residue(16)
            Traceback (most recent call last):
            ...
            NotImplementedError: residue() not implemented in extensions for absprec larger than one"""
