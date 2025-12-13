import sage.rings.finite_rings.hom_finite_field
from sage.categories.homset import Hom as Hom
from sage.rings.finite_rings.finite_field_constructor import FiniteField as FiniteField
from sage.rings.finite_rings.finite_field_givaro import FiniteField_givaro as FiniteField_givaro
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

class FiniteFieldHomomorphism_givaro(sage.rings.finite_rings.hom_finite_field.FiniteFieldHomomorphism_generic):
    """FiniteFieldHomomorphism_givaro(parent, im_gens=None, check=False)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, im_gens=..., check=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_finite_field_givaro.pyx (starting at line 139)

                TESTS::

                    sage: from sage.rings.finite_rings.hom_finite_field_givaro import FiniteFieldHomomorphism_givaro
                    sage: k.<t> = GF(3^2)
                    sage: K.<T> = GF(3^4)
                    sage: f = FiniteFieldHomomorphism_givaro(Hom(k, K)); f # random
                    Ring morphism:
                      From: Finite Field in t of size 3^2
                      To:   Finite Field in T of size 3^4
                      Defn: t |--> 2*T^3 + 2*T^2 + 1
                    sage: a = k.random_element()
                    sage: b = k.random_element()
                    sage: f(a) + f(b) == f(a + b)
                    True

                    sage: k.<t> = GF(3^10)
                    sage: K.<T> = GF(3^20)
                    sage: f = FiniteFieldHomomorphism_givaro(Hom(k, K)); f
                    Traceback (most recent call last):
                    ...
                    TypeError: The codomain is not an instance of FiniteField_givaro
        """

class FrobeniusEndomorphism_givaro(sage.rings.finite_rings.hom_finite_field.FrobeniusEndomorphism_finite_field):
    """FrobeniusEndomorphism_givaro(domain, power=1)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, domain, power=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_finite_field_givaro.pyx (starting at line 209)

                TESTS::

                    sage: k.<t> = GF(5^3)
                    sage: Frob = k.frobenius_endomorphism(); Frob
                    Frobenius endomorphism t |--> t^5 on Finite Field in t of size 5^3
                    sage: type(Frob)
                    <class 'sage.rings.finite_rings.hom_finite_field_givaro.FrobeniusEndomorphism_givaro'>

                    sage: k.<t> = GF(5^20)
                    sage: Frob = k.frobenius_endomorphism(); Frob
                    Frobenius endomorphism t |--> t^5 on Finite Field in t of size 5^20
                    sage: type(Frob)
                    <class 'sage.rings.finite_rings.hom_finite_field.FrobeniusEndomorphism_finite_field'>
        """
    @overload
    def fixed_field(self) -> Any:
        """FrobeniusEndomorphism_givaro.fixed_field(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_finite_field_givaro.pyx (starting at line 229)

        Return the fixed field of ``self``.

        OUTPUT:

        - a tuple `(K, e)`, where `K` is the subfield of the domain
          consisting of elements fixed by ``self`` and `e` is an
          embedding of `K` into the domain.

        .. NOTE::

            The name of the variable used for the subfield (if it
            is not a prime subfield) is suffixed by ``_fixed``.

        EXAMPLES::

            sage: k.<t> = GF(5^6)
            sage: f = k.frobenius_endomorphism(2)
            sage: kfixed, embed = f.fixed_field()
            sage: kfixed
            Finite Field in t_fixed of size 5^2
            sage: embed # random
            Ring morphism:
              From: Finite Field in t_fixed of size 5^2
              To:   Finite Field in t of size 5^6
              Defn: t_fixed |--> 4*t^5 + 2*t^4 + 4*t^2 + t

            sage: tfixed = kfixed.gen()
            sage: embed(tfixed) # random
            4*t^5 + 2*t^4 + 4*t^2 + t"""
    @overload
    def fixed_field(self) -> Any:
        """FrobeniusEndomorphism_givaro.fixed_field(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_finite_field_givaro.pyx (starting at line 229)

        Return the fixed field of ``self``.

        OUTPUT:

        - a tuple `(K, e)`, where `K` is the subfield of the domain
          consisting of elements fixed by ``self`` and `e` is an
          embedding of `K` into the domain.

        .. NOTE::

            The name of the variable used for the subfield (if it
            is not a prime subfield) is suffixed by ``_fixed``.

        EXAMPLES::

            sage: k.<t> = GF(5^6)
            sage: f = k.frobenius_endomorphism(2)
            sage: kfixed, embed = f.fixed_field()
            sage: kfixed
            Finite Field in t_fixed of size 5^2
            sage: embed # random
            Ring morphism:
              From: Finite Field in t_fixed of size 5^2
              To:   Finite Field in t of size 5^6
              Defn: t_fixed |--> 4*t^5 + 2*t^4 + 4*t^2 + t

            sage: tfixed = kfixed.gen()
            sage: embed(tfixed) # random
            4*t^5 + 2*t^4 + 4*t^2 + t"""

class SectionFiniteFieldHomomorphism_givaro(sage.rings.finite_rings.hom_finite_field.SectionFiniteFieldHomomorphism_generic):
    """SectionFiniteFieldHomomorphism_givaro(inverse)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, inverse) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_finite_field_givaro.pyx (starting at line 54)

                TESTS::

                    sage: from sage.rings.finite_rings.hom_finite_field_givaro import FiniteFieldHomomorphism_givaro
                    sage: k.<t> = GF(3^2)
                    sage: K.<T> = GF(3^4)
                    sage: f = FiniteFieldHomomorphism_givaro(Hom(k, K))
                    sage: g = f.section(); g # random
                    Section of Ring morphism:
                      From: Finite Field in t of size 3^2
                      To:   Finite Field in T of size 3^4
                      Defn: t |--> 2*T^3 + 2*T^2 + 1
                    sage: a = k.random_element()
                    sage: b = k.random_element()
                    sage: g(f(a) + f(b)) == g(f(a)) + g(f(b)) == a + b
                    True
        """
