import _cython_3_2_1
import sage.categories.map
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar

__pyx_capi__: dict
test_CCallableConvertMap: _cython_3_2_1.cython_function_or_method

class CCallableConvertMap_class(sage.categories.map.Map):
    """CCallableConvertMap_class(domain, codomain, name)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, domain, codomain, name) -> Any:
        """File: /build/sagemath/src/sage/src/sage/structure/coerce_maps.pyx (starting at line 492)"""

class CallableConvertMap(sage.categories.map.Map):
    """CallableConvertMap(domain, codomain, func, parent_as_first_arg=None)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, domain, codomain, func, parent_as_first_arg=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/structure/coerce_maps.pyx (starting at line 320)

                This lets one easily create maps from any callable object.

                This is especially useful to create maps from bound methods.

                EXAMPLES::

                    sage: from sage.structure.coerce_maps import CallableConvertMap
                    sage: def foo(P, x): return x/2
                    sage: f = CallableConvertMap(ZZ, QQ, foo)
                    sage: f(3)
                    3/2
                    sage: f
                    Conversion via foo map:
                      From: Integer Ring
                      To:   Rational Field

                Create a homomorphism from `\\RR` to `\\RR^+` viewed as additive groups.

                ::

                    sage: # needs sage.symbolic
                    sage: f = CallableConvertMap(RR, RR, exp, parent_as_first_arg=False)
                    sage: f(0)
                    1.00000000000000
                    sage: f(1)
                    2.71828182845905
                    sage: f(-3)
                    0.0497870683678639
        """

class DefaultConvertMap(sage.categories.map.Map):
    """DefaultConvertMap(domain, codomain, category=None)

    File: /build/sagemath/src/sage/src/sage/structure/coerce_maps.pyx (starting at line 17)

    This morphism simply calls the codomain's element_constructor method,
    passing in the codomain as the first argument.

    EXAMPLES::

        sage: QQ[['x']].coerce_map_from(QQ)
        Coercion map:
          From: Rational Field
          To:   Power Series Ring in x over Rational Field"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, domain, codomain, category=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/structure/coerce_maps.pyx (starting at line 29)

                TESTS:

                Maps of this type are morphisms in the category of sets with
                partial maps (see :issue:`15618`)::

                    sage: f = GF(11).convert_map_from(GF(7)); f                                 # needs sage.rings.finite_rings
                    Conversion map:
                      From: Finite Field of size 7
                      To:   Finite Field of size 11
                    sage: f.parent()                                                            # needs sage.rings.finite_rings
                    Set of Morphisms
                     from Finite Field of size 7
                     to Finite Field of size 11
                     in Category of sets with partial maps

                Test that :issue:`23211` is resolved::

                    sage: f._is_coercion                                                        # needs sage.rings.finite_rings
                    False
                    sage: QQ[['x']].coerce_map_from(QQ)._is_coercion
                    True

                This class is deprecated when used directly::

                    sage: from sage.structure.coerce_maps import DefaultConvertMap
                    sage: DefaultConvertMap(ZZ, ZZ)
                    doctest:...: DeprecationWarning: DefaultConvertMap is deprecated, use DefaultConvertMap_unique instead.
                    This probably means that _element_constructor_ should be a method and not some other kind of callable
                    See https://github.com/sagemath/sage/issues/26879 for details.
                    Conversion map:
                      From: Integer Ring
                      To:   Integer Ring
        """

class DefaultConvertMap_unique(DefaultConvertMap):
    """File: /build/sagemath/src/sage/src/sage/structure/coerce_maps.pyx (starting at line 144)

        This morphism simply defers action to the codomain's
        element_constructor method, WITHOUT passing in the codomain as the
        first argument.

        This is used for creating elements that don't take a parent as the
        first argument to their __init__ method, for example, Integers,
        Rationals, Algebraic Reals... all have a unique parent. It is also
        used when the element_constructor is a bound method (whose self
        argument is assumed to be bound to the codomain).
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class ListMorphism(sage.categories.map.Map):
    """ListMorphism(domain, Map real_morphism)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, domain, Mapreal_morphism) -> Any:
        """File: /build/sagemath/src/sage/src/sage/structure/coerce_maps.pyx (starting at line 584)"""

class NamedConvertMap(sage.categories.map.Map):
    """NamedConvertMap(domain, codomain, method_name)

    File: /build/sagemath/src/sage/src/sage/structure/coerce_maps.pyx (starting at line 186)

    This is used for creating elements via the _xxx_ methods.

    For example, many elements implement an _integer_ method to
    convert to ZZ, or a _rational_ method to convert to QQ."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    method_name: File
    def __init__(self, domain, codomain, method_name) -> Any:
        """File: /build/sagemath/src/sage/src/sage/structure/coerce_maps.pyx (starting at line 194)

                EXAMPLES::

                    sage: # needs sage.symbolic
                    sage: from sage.structure.coerce_maps import NamedConvertMap
                    sage: var('t')
                    t
                    sage: mor = NamedConvertMap(SR, QQ['t'], '_polynomial_')
                    sage: mor(t^2/4 + 1)
                    1/4*t^2 + 1
                    sage: mor = NamedConvertMap(SR, GF(7)[['t']], '_polynomial_')
                    sage: mor(t^2/4 + 1)
                    1 + 2*t^2
        """

class TryMap(sage.categories.map.Map):
    """TryMap(Map morphism_preferred, Map morphism_backup, error_types=None)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, Mapmorphism_preferred, Mapmorphism_backup, error_types=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/structure/coerce_maps.pyx (starting at line 617)

                TESTS::

                    sage: sage.structure.coerce_maps.TryMap(RDF.coerce_map_from(QQ), RDF.coerce_map_from(ZZ))
                    Traceback (most recent call last):
                    ...
                    TypeError: incorrectly matching parent
        """
