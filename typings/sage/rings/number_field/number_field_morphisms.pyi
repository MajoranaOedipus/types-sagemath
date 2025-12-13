import _cython_3_2_1
import sage.categories.map
import sage.categories.morphism
from sage.categories.category import CDF as CDF
from sage.categories.pushout import pushout as pushout
from sage.rings.real_lazy import CLF as CLF, LazyAlgebraic as LazyAlgebraic, LazyField as LazyField, RLF as RLF
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

closest: _cython_3_2_1.cython_function_or_method
create_embedding_from_approx: _cython_3_2_1.cython_function_or_method
matching_root: _cython_3_2_1.cython_function_or_method
root_from_approx: _cython_3_2_1.cython_function_or_method

class CyclotomicFieldConversion(sage.categories.map.Map):
    """CyclotomicFieldConversion(K, L)

    File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_morphisms.pyx (starting at line 711)

    This allows one to cast one cyclotomic field in another consistently.

    EXAMPLES::

        sage: from sage.rings.number_field.number_field_morphisms import CyclotomicFieldConversion
        sage: K1.<z1> = CyclotomicField(12)
        sage: K2.<z2> = CyclotomicField(18)
        sage: f = CyclotomicFieldConversion(K1, K2)
        sage: f(z1^2)
        z2^3
        sage: f(z1)
        Traceback (most recent call last):
        ...
        ValueError: Element z1 has no image in the codomain

    Tests from :issue:`29511`::

        sage: K.<z> = CyclotomicField(12)
        sage: K1.<z1> = CyclotomicField(3)
        sage: K(2) in K1 # indirect doctest
        True
        sage: K1(K(2)) # indirect doctest
        2"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @overload
    def __init__(self, K, L) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_morphisms.pyx (starting at line 740)

                Construct a conversion map between cyclotomic fields.

                EXAMPLES::

                    sage: from sage.rings.number_field.number_field_morphisms import CyclotomicFieldEmbedding
                    sage: K.<a> = CyclotomicField(7)
                    sage: L.<b> = CyclotomicField(21)
                    sage: K(b^3) # indirect doctest
                    a
        """
    @overload
    def __init__(self, K1, K2) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_morphisms.pyx (starting at line 740)

                Construct a conversion map between cyclotomic fields.

                EXAMPLES::

                    sage: from sage.rings.number_field.number_field_morphisms import CyclotomicFieldEmbedding
                    sage: K.<a> = CyclotomicField(7)
                    sage: L.<b> = CyclotomicField(21)
                    sage: K(b^3) # indirect doctest
                    a
        """

class CyclotomicFieldEmbedding(NumberFieldEmbedding):
    """CyclotomicFieldEmbedding(K, L)

    File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_morphisms.pyx (starting at line 561)

    Specialized class for converting cyclotomic field elements into a
    cyclotomic field of higher order. All the real work is done by
    :meth:`_lift_cyclotomic_element`."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, K, L) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_morphisms.pyx (starting at line 570)

                Check and cache the parameters.

                EXAMPLES::

                    sage: from sage.rings.number_field.number_field_morphisms import CyclotomicFieldEmbedding
                    sage: CyclotomicFieldEmbedding(CyclotomicField(7), CyclotomicField(21))
                    Generic morphism:
                      From: Cyclotomic Field of order 7 and degree 6
                      To:   Cyclotomic Field of order 21 and degree 12
                      Defn: zeta7 -> zeta21^3

                Note that this only handles the easy case of cyclotomic fields where
                the order of the smaller dividing the order of the larger, regardless
                of whether or not there is an actual coercion::

                    sage: CyclotomicFieldEmbedding(CyclotomicField(3), QuadraticField(-3, 'a'))
                    Traceback (most recent call last):
                    ...
                    TypeError: CyclotomicFieldEmbedding only valid for cyclotomic fields.
                    sage: CyclotomicFieldEmbedding(CyclotomicField(14), CyclotomicField(21))
                    Traceback (most recent call last):
                    ...
                    TypeError: The zeta_order of the new field must be a multiple of the zeta_order of the original.

                Check that :issue:`13765` is fixed::

                    sage: z3=(CC(-1)^(1/3))^2
                    sage: Ka.<a>=CyclotomicField(3,embedding=z3)
                    sage: Kb.<b>=CyclotomicField(3,embedding=z3^2)
                    sage: CyclotomicFieldEmbedding(Ka, Kb)
                    Generic morphism:
                      From: Cyclotomic Field of order 3 and degree 2
                      To:   Cyclotomic Field of order 3 and degree 2
                      Defn: a -> -b - 1
                    sage: Ka(b)
                    -a - 1
                    sage: a + b
                    -1
                    sage: b + a
                    -1
        """
    @overload
    def section(self) -> Any:
        """CyclotomicFieldEmbedding.section(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_morphisms.pyx (starting at line 695)

        Return the section of ``self``.

        EXAMPLES::

            sage: from sage.rings.number_field.number_field_morphisms import CyclotomicFieldEmbedding
            sage: K = CyclotomicField(7)
            sage: L = CyclotomicField(21)
            sage: f = CyclotomicFieldEmbedding(K, L)
            sage: h = f.section()
            sage: h(f(K.gen())) # indirect doctest
            zeta7"""
    @overload
    def section(self) -> Any:
        """CyclotomicFieldEmbedding.section(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_morphisms.pyx (starting at line 695)

        Return the section of ``self``.

        EXAMPLES::

            sage: from sage.rings.number_field.number_field_morphisms import CyclotomicFieldEmbedding
            sage: K = CyclotomicField(7)
            sage: L = CyclotomicField(21)
            sage: f = CyclotomicFieldEmbedding(K, L)
            sage: h = f.section()
            sage: h(f(K.gen())) # indirect doctest
            zeta7"""

class EmbeddedNumberFieldConversion(sage.categories.map.Map):
    """EmbeddedNumberFieldConversion(K, L, ambient_field=None)

    File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_morphisms.pyx (starting at line 286)

    This allows one to cast one number field in another consistently,
    assuming they both have specified embeddings into an ambient field
    (by default it looks for an embedding into `\\CC`).

    This is done by factoring the minimal polynomial of the input
    in the number field of the codomain. This may fail if the element is
    not actually in the given field."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    ambient_field: File
    def __init__(self, K, L, ambient_field=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_morphisms.pyx (starting at line 299)

                EXAMPLES::

                    sage: from sage.rings.number_field.number_field_morphisms import EmbeddedNumberFieldConversion
                    sage: x = polygen(ZZ, 'x')
                    sage: K.<a> = NumberField(x^2 - 17, embedding=4.1)
                    sage: L.<b> = NumberField(x^4 - 17, embedding=2.0)
                    sage: f = EmbeddedNumberFieldConversion(K, L)
                    sage: f(a)
                    b^2
                    sage: f(K(b^2/2-11))
                    1/2*b^2 - 11
        """

class EmbeddedNumberFieldMorphism(NumberFieldEmbedding):
    """EmbeddedNumberFieldMorphism(K, L, ambient_field=None)

    File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_morphisms.pyx (starting at line 160)

    This allows one to go from one number field in another consistently,
    assuming they both have specified embeddings into an ambient field.

    If no ambient field is supplied, then the following ambient fields are
    tried:

    * the pushout of the fields where the number fields are embedded;

    * the algebraic closure of the previous pushout;

    * `\\CC`.

    EXAMPLES::

        sage: x = polygen(ZZ, 'x')
        sage: K.<i> = NumberField(x^2 + 1, embedding=QQbar(I))
        sage: L.<i> = NumberField(x^2 + 1, embedding=-QQbar(I))
        sage: from sage.rings.number_field.number_field_morphisms import EmbeddedNumberFieldMorphism
        sage: EmbeddedNumberFieldMorphism(K, L, CDF)
        Generic morphism:
          From: Number Field in i with defining polynomial x^2 + 1 with i = I
          To:   Number Field in i with defining polynomial x^2 + 1 with i = -I
          Defn: i -> -i
        sage: EmbeddedNumberFieldMorphism(K, L, QQbar)
        Generic morphism:
          From: Number Field in i with defining polynomial x^2 + 1 with i = I
          To:   Number Field in i with defining polynomial x^2 + 1 with i = -I
          Defn: i -> -i"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    ambient_field: File
    def __init__(self, K, L, ambient_field=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_morphisms.pyx (starting at line 193)

                EXAMPLES::

                    sage: from sage.rings.number_field.number_field_morphisms import EmbeddedNumberFieldMorphism
                    sage: x = polygen(ZZ, 'x')
                    sage: K.<a> = NumberField(x^2 - 17, embedding=4.1)
                    sage: L.<b> = NumberField(x^4 - 17, embedding=2.0)
                    sage: f = EmbeddedNumberFieldMorphism(K, L)
                    sage: f(a)
                    b^2

                    sage: K.<zeta12> = CyclotomicField(12)
                    sage: L.<zeta36> = CyclotomicField(36)
                    sage: f = EmbeddedNumberFieldMorphism(K, L)
                    sage: f(zeta12)
                    zeta36^3
                    sage: f(zeta12^5-zeta12+1)
                    zeta36^9 - 2*zeta36^3 + 1
                    sage: f
                    Generic morphism:
                      From: Cyclotomic Field of order 12 and degree 4
                      To:   Cyclotomic Field of order 36 and degree 12
                      Defn: zeta12 -> zeta36^3

                The embeddings must be compatible::

                    sage: F1 = NumberField(x^3 + 2, 'a', embedding=2)
                    sage: F2 = NumberField(x^3 + 2, 'a', embedding=CC.0)
                    sage: F1.gen() + F2.gen()
                    Traceback (most recent call last):
                    ...
                    TypeError: unsupported operand parent(s) for +:
                    'Number Field in a with defining polynomial x^3 + 2 with a = -1.259921049894873?' and
                    'Number Field in a with defining polynomial x^3 + 2 with a = 0.6299605249474365? + 1.091123635971722?*I'

                The following was fixed to raise a :exc:`TypeError` in :issue:`15331`::

                    sage: L.<i> = NumberField(x^2 + 1)
                    sage: K = NumberField(L(i/2+3).minpoly(), names=('i0',), embedding=L(i/2+3))
                    sage: EmbeddedNumberFieldMorphism(K, L)
                    Traceback (most recent call last):
                    ...
                    TypeError: No embedding available for Number Field in i with defining polynomial x^2 + 1
        """
    @overload
    def section(self) -> Any:
        """EmbeddedNumberFieldMorphism.section(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_morphisms.pyx (starting at line 268)

        EXAMPLES::

            sage: from sage.rings.number_field.number_field_morphisms import EmbeddedNumberFieldMorphism
            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 700, embedding=25)
            sage: L.<b> = NumberField(x^6 - 700, embedding=3)
            sage: f = EmbeddedNumberFieldMorphism(K, L)
            sage: f(2*a - 1)
            2*b^3 - 1
            sage: g = f.section()
            sage: g(2*b^3 - 1)
            2*a - 1"""
    @overload
    def section(self) -> Any:
        """EmbeddedNumberFieldMorphism.section(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_morphisms.pyx (starting at line 268)

        EXAMPLES::

            sage: from sage.rings.number_field.number_field_morphisms import EmbeddedNumberFieldMorphism
            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 700, embedding=25)
            sage: L.<b> = NumberField(x^6 - 700, embedding=3)
            sage: f = EmbeddedNumberFieldMorphism(K, L)
            sage: f(2*a - 1)
            2*b^3 - 1
            sage: g = f.section()
            sage: g(2*b^3 - 1)
            2*a - 1"""

class NumberFieldEmbedding(sage.categories.morphism.Morphism):
    """NumberFieldEmbedding(K, R, gen_embedding)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, K, R, gen_embedding) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_morphisms.pyx (starting at line 35)

                If R is a lazy field, the closest root to gen_embedding will be chosen.

                EXAMPLES::

                    sage: x = polygen(QQ)
                    sage: from sage.rings.number_field.number_field_morphisms import NumberFieldEmbedding
                    sage: K.<a> = NumberField(x^3-2)
                    sage: f = NumberFieldEmbedding(K, RLF, 1)
                    sage: f(a)^3
                    2.00000000000000?
                    sage: RealField(200)(f(a)^3)
                    2.0000000000000000000000000000000000000000000000000000000000

                    sage: sigma_a = K.polynomial().change_ring(CC).roots()[1][0]; sigma_a
                    -0.62996052494743... - 1.09112363597172*I
                    sage: g = NumberFieldEmbedding(K, CC, sigma_a)
                    sage: g(a+1)
                    0.37003947505256... - 1.09112363597172*I
        """
    @overload
    def gen_image(self) -> Any:
        """NumberFieldEmbedding.gen_image(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_morphisms.pyx (starting at line 147)

        Return the image of the generator under this embedding.

        EXAMPLES::

            sage: f = QuadraticField(7, 'a', embedding=2).coerce_embedding()
            sage: f.gen_image()
            2.645751311064591?"""
    @overload
    def gen_image(self) -> Any:
        """NumberFieldEmbedding.gen_image(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_morphisms.pyx (starting at line 147)

        Return the image of the generator under this embedding.

        EXAMPLES::

            sage: f = QuadraticField(7, 'a', embedding=2).coerce_embedding()
            sage: f.gen_image()
            2.645751311064591?"""
