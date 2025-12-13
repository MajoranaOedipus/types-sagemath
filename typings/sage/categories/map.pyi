import _cython_3_2_1
import sage.categories.homset as homset
import sage.structure.element
from sage.misc.constant_function import ConstantFunction as ConstantFunction
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

is_Map: _cython_3_2_1.cython_function_or_method
unpickle_map: _cython_3_2_1.cython_function_or_method

class FormalCompositeMap(Map):
    """FormalCompositeMap(parent, first, second=None)

    File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 1451)

    Formal composite maps.

    A formal composite map is formed by two maps, so that the codomain of the
    first map is contained in the domain of the second map.

    .. NOTE::

        When calling a composite with additional arguments, these arguments are
        *only* passed to the second underlying map.

    EXAMPLES::

        sage: R.<x> = QQ[]
        sage: S.<a> = QQ[]
        sage: from sage.categories.morphism import SetMorphism
        sage: f = SetMorphism(Hom(R, S, Rings()), lambda p: p[0]*a^p.degree())
        sage: g = S.hom([2*x])
        sage: f*g
        Composite map:
          From: Univariate Polynomial Ring in a over Rational Field
          To:   Univariate Polynomial Ring in a over Rational Field
          Defn:   Ring morphism:
                  From: Univariate Polynomial Ring in a over Rational Field
                  To:   Univariate Polynomial Ring in x over Rational Field
                  Defn: a |--> 2*x
                then
                  Generic morphism:
                  From: Univariate Polynomial Ring in x over Rational Field
                  To:   Univariate Polynomial Ring in a over Rational Field
        sage: g*f
        Composite map:
          From: Univariate Polynomial Ring in x over Rational Field
          To:   Univariate Polynomial Ring in x over Rational Field
          Defn:   Generic morphism:
                  From: Univariate Polynomial Ring in x over Rational Field
                  To:   Univariate Polynomial Ring in a over Rational Field
                then
                  Ring morphism:
                  From: Univariate Polynomial Ring in a over Rational Field
                  To:   Univariate Polynomial Ring in x over Rational Field
                  Defn: a |--> 2*x
        sage: (f*g)(2*a^2+5)
        5*a^2
        sage: (g*f)(2*x^2+5)
        20*x^2"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, *args, **kwargs) -> None:
        """File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 1500)

                INPUT:

                - ``parent`` -- a homset
                - ``first`` -- a map or a list of maps
                - ``second`` -- a map or None

                .. NOTE::

                    The intended use is of course that the codomain of the
                    first map is contained in the domain of the second map,
                    so that the two maps can be composed, and that the
                    composition belongs to ``parent``. However, none of
                    these conditions is verified in the init method.

                    The user is advised to compose two maps ``f`` and ``g``
                    in multiplicative notation, ``g*f``, since this will in
                    some cases return a more efficient map object than a
                    formal composite map.

                TESTS::

                    sage: R.<x,y> = QQ[]
                    sage: S.<a,b> = QQ[]
                    sage: f = R.hom([a+b, a-b])
                    sage: g = S.hom([x+y, x-y])
                    sage: H = Hom(R, R, Rings())
                    sage: from sage.categories.map import FormalCompositeMap
                    sage: m = FormalCompositeMap(H, f, g); m
                    Composite map:
                      From: Multivariate Polynomial Ring in x, y over Rational Field
                      To:   Multivariate Polynomial Ring in x, y over Rational Field
                      Defn:   Ring morphism:
                              From: Multivariate Polynomial Ring in x, y over Rational Field
                              To:   Multivariate Polynomial Ring in a, b over Rational Field
                              Defn: x |--> a + b
                                    y |--> a - b
                            then
                              Ring morphism:
                              From: Multivariate Polynomial Ring in a, b over Rational Field
                              To:   Multivariate Polynomial Ring in x, y over Rational Field
                              Defn: a |--> x + y
                                    b |--> x - y
                    sage: m(x), m(y)
                    (2*x, 2*y)
        """
    @overload
    def domains(self) -> Any:
        """FormalCompositeMap.domains(self)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 2033)

        Iterate over the domains of the factors of this map.

        (This is useful in particular to check for loops in coercion maps.)

        .. SEEALSO:: :meth:`Map.domains`

        EXAMPLES::

            sage: f = QQ.coerce_map_from(ZZ)
            sage: g = MatrixSpace(QQ, 2, 2).coerce_map_from(QQ)                         # needs sage.modules
            sage: list((g * f).domains())                                               # needs sage.modules
            [Integer Ring, Rational Field]"""
    @overload
    def domains(self) -> Any:
        """FormalCompositeMap.domains(self)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 2033)

        Iterate over the domains of the factors of this map.

        (This is useful in particular to check for loops in coercion maps.)

        .. SEEALSO:: :meth:`Map.domains`

        EXAMPLES::

            sage: f = QQ.coerce_map_from(ZZ)
            sage: g = MatrixSpace(QQ, 2, 2).coerce_map_from(QQ)                         # needs sage.modules
            sage: list((g * f).domains())                                               # needs sage.modules
            [Integer Ring, Rational Field]"""
    def first(self) -> Any:
        """FormalCompositeMap.first(self)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 1826)

        Return the first map in the formal composition.

        If ``self`` represents `f_n \\circ f_{n-1} \\circ \\cdots \\circ
        f_1 \\circ f_0`, then ``self.first()`` returns `f_0`.  We have
        ``self == self.then() * self.first()``.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: S.<a> = QQ[]
            sage: from sage.categories.morphism import SetMorphism
            sage: f = SetMorphism(Hom(R, S, Rings()), lambda p: p[0]*a^p.degree())
            sage: g = S.hom([2*x])
            sage: fg = f * g
            sage: fg.first() == g
            True
            sage: fg == fg.then() * fg.first()
            True"""
    @overload
    def is_injective(self) -> Any:
        """FormalCompositeMap.is_injective(self)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 1887)

        Tell whether ``self`` is injective.

        It raises :exc:`NotImplementedError` if it cannot be determined.

        EXAMPLES::

            sage: # needs sage.modules
            sage: V1 = QQ^2
            sage: V2 = QQ^3
            sage: phi1 = (QQ^1).hom(Matrix([[1, 1]]), V1)
            sage: phi2 = V1.hom(Matrix([[1, 2, 3], [4, 5, 6]]), V2)

        If both constituents are injective, the composition is injective::

            sage: from sage.categories.map import FormalCompositeMap
            sage: c1 = FormalCompositeMap(Hom(QQ^1, V2, phi1.category_for()),           # needs sage.modules
            ....:                         phi1, phi2)
            sage: c1.is_injective()                                                     # needs sage.modules
            True

        If it cannot be determined whether the composition is injective,
        an error is raised::

            sage: psi1 = V2.hom(Matrix([[1, 2], [3, 4], [5, 6]]), V1)                   # needs sage.modules
            sage: c2 = FormalCompositeMap(Hom(V1, V1, phi2.category_for()),             # needs sage.modules
            ....:                         phi2, psi1)
            sage: c2.is_injective()                                                     # needs sage.modules
            Traceback (most recent call last):
            ...
            NotImplementedError: not enough information to deduce injectivity

        If the first map is surjective and the second map is not injective,
        then the composition is not injective::

            sage: psi2 = V1.hom([[1], [1]], QQ^1)                                       # needs sage.modules
            sage: c3 = FormalCompositeMap(Hom(V2, QQ^1, phi2.category_for()),           # needs sage.modules
            ....:                         psi2, psi1)
            sage: c3.is_injective()                                                     # needs sage.modules
            False

        TESTS:

        Check that :issue:`23205` has been resolved::

            sage: f = QQ.hom(QQbar) * ZZ.hom(QQ)                                        # needs sage.rings.number_field
            sage: f.is_injective()                                                      # needs sage.rings.number_field
            True"""
    @overload
    def is_injective(self) -> Any:
        """FormalCompositeMap.is_injective(self)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 1887)

        Tell whether ``self`` is injective.

        It raises :exc:`NotImplementedError` if it cannot be determined.

        EXAMPLES::

            sage: # needs sage.modules
            sage: V1 = QQ^2
            sage: V2 = QQ^3
            sage: phi1 = (QQ^1).hom(Matrix([[1, 1]]), V1)
            sage: phi2 = V1.hom(Matrix([[1, 2, 3], [4, 5, 6]]), V2)

        If both constituents are injective, the composition is injective::

            sage: from sage.categories.map import FormalCompositeMap
            sage: c1 = FormalCompositeMap(Hom(QQ^1, V2, phi1.category_for()),           # needs sage.modules
            ....:                         phi1, phi2)
            sage: c1.is_injective()                                                     # needs sage.modules
            True

        If it cannot be determined whether the composition is injective,
        an error is raised::

            sage: psi1 = V2.hom(Matrix([[1, 2], [3, 4], [5, 6]]), V1)                   # needs sage.modules
            sage: c2 = FormalCompositeMap(Hom(V1, V1, phi2.category_for()),             # needs sage.modules
            ....:                         phi2, psi1)
            sage: c2.is_injective()                                                     # needs sage.modules
            Traceback (most recent call last):
            ...
            NotImplementedError: not enough information to deduce injectivity

        If the first map is surjective and the second map is not injective,
        then the composition is not injective::

            sage: psi2 = V1.hom([[1], [1]], QQ^1)                                       # needs sage.modules
            sage: c3 = FormalCompositeMap(Hom(V2, QQ^1, phi2.category_for()),           # needs sage.modules
            ....:                         psi2, psi1)
            sage: c3.is_injective()                                                     # needs sage.modules
            False

        TESTS:

        Check that :issue:`23205` has been resolved::

            sage: f = QQ.hom(QQbar) * ZZ.hom(QQ)                                        # needs sage.rings.number_field
            sage: f.is_injective()                                                      # needs sage.rings.number_field
            True"""
    @overload
    def is_injective(self) -> Any:
        """FormalCompositeMap.is_injective(self)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 1887)

        Tell whether ``self`` is injective.

        It raises :exc:`NotImplementedError` if it cannot be determined.

        EXAMPLES::

            sage: # needs sage.modules
            sage: V1 = QQ^2
            sage: V2 = QQ^3
            sage: phi1 = (QQ^1).hom(Matrix([[1, 1]]), V1)
            sage: phi2 = V1.hom(Matrix([[1, 2, 3], [4, 5, 6]]), V2)

        If both constituents are injective, the composition is injective::

            sage: from sage.categories.map import FormalCompositeMap
            sage: c1 = FormalCompositeMap(Hom(QQ^1, V2, phi1.category_for()),           # needs sage.modules
            ....:                         phi1, phi2)
            sage: c1.is_injective()                                                     # needs sage.modules
            True

        If it cannot be determined whether the composition is injective,
        an error is raised::

            sage: psi1 = V2.hom(Matrix([[1, 2], [3, 4], [5, 6]]), V1)                   # needs sage.modules
            sage: c2 = FormalCompositeMap(Hom(V1, V1, phi2.category_for()),             # needs sage.modules
            ....:                         phi2, psi1)
            sage: c2.is_injective()                                                     # needs sage.modules
            Traceback (most recent call last):
            ...
            NotImplementedError: not enough information to deduce injectivity

        If the first map is surjective and the second map is not injective,
        then the composition is not injective::

            sage: psi2 = V1.hom([[1], [1]], QQ^1)                                       # needs sage.modules
            sage: c3 = FormalCompositeMap(Hom(V2, QQ^1, phi2.category_for()),           # needs sage.modules
            ....:                         psi2, psi1)
            sage: c3.is_injective()                                                     # needs sage.modules
            False

        TESTS:

        Check that :issue:`23205` has been resolved::

            sage: f = QQ.hom(QQbar) * ZZ.hom(QQ)                                        # needs sage.rings.number_field
            sage: f.is_injective()                                                      # needs sage.rings.number_field
            True"""
    @overload
    def is_injective(self) -> Any:
        """FormalCompositeMap.is_injective(self)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 1887)

        Tell whether ``self`` is injective.

        It raises :exc:`NotImplementedError` if it cannot be determined.

        EXAMPLES::

            sage: # needs sage.modules
            sage: V1 = QQ^2
            sage: V2 = QQ^3
            sage: phi1 = (QQ^1).hom(Matrix([[1, 1]]), V1)
            sage: phi2 = V1.hom(Matrix([[1, 2, 3], [4, 5, 6]]), V2)

        If both constituents are injective, the composition is injective::

            sage: from sage.categories.map import FormalCompositeMap
            sage: c1 = FormalCompositeMap(Hom(QQ^1, V2, phi1.category_for()),           # needs sage.modules
            ....:                         phi1, phi2)
            sage: c1.is_injective()                                                     # needs sage.modules
            True

        If it cannot be determined whether the composition is injective,
        an error is raised::

            sage: psi1 = V2.hom(Matrix([[1, 2], [3, 4], [5, 6]]), V1)                   # needs sage.modules
            sage: c2 = FormalCompositeMap(Hom(V1, V1, phi2.category_for()),             # needs sage.modules
            ....:                         phi2, psi1)
            sage: c2.is_injective()                                                     # needs sage.modules
            Traceback (most recent call last):
            ...
            NotImplementedError: not enough information to deduce injectivity

        If the first map is surjective and the second map is not injective,
        then the composition is not injective::

            sage: psi2 = V1.hom([[1], [1]], QQ^1)                                       # needs sage.modules
            sage: c3 = FormalCompositeMap(Hom(V2, QQ^1, phi2.category_for()),           # needs sage.modules
            ....:                         psi2, psi1)
            sage: c3.is_injective()                                                     # needs sage.modules
            False

        TESTS:

        Check that :issue:`23205` has been resolved::

            sage: f = QQ.hom(QQbar) * ZZ.hom(QQ)                                        # needs sage.rings.number_field
            sage: f.is_injective()                                                      # needs sage.rings.number_field
            True"""
    @overload
    def is_injective(self) -> Any:
        """FormalCompositeMap.is_injective(self)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 1887)

        Tell whether ``self`` is injective.

        It raises :exc:`NotImplementedError` if it cannot be determined.

        EXAMPLES::

            sage: # needs sage.modules
            sage: V1 = QQ^2
            sage: V2 = QQ^3
            sage: phi1 = (QQ^1).hom(Matrix([[1, 1]]), V1)
            sage: phi2 = V1.hom(Matrix([[1, 2, 3], [4, 5, 6]]), V2)

        If both constituents are injective, the composition is injective::

            sage: from sage.categories.map import FormalCompositeMap
            sage: c1 = FormalCompositeMap(Hom(QQ^1, V2, phi1.category_for()),           # needs sage.modules
            ....:                         phi1, phi2)
            sage: c1.is_injective()                                                     # needs sage.modules
            True

        If it cannot be determined whether the composition is injective,
        an error is raised::

            sage: psi1 = V2.hom(Matrix([[1, 2], [3, 4], [5, 6]]), V1)                   # needs sage.modules
            sage: c2 = FormalCompositeMap(Hom(V1, V1, phi2.category_for()),             # needs sage.modules
            ....:                         phi2, psi1)
            sage: c2.is_injective()                                                     # needs sage.modules
            Traceback (most recent call last):
            ...
            NotImplementedError: not enough information to deduce injectivity

        If the first map is surjective and the second map is not injective,
        then the composition is not injective::

            sage: psi2 = V1.hom([[1], [1]], QQ^1)                                       # needs sage.modules
            sage: c3 = FormalCompositeMap(Hom(V2, QQ^1, phi2.category_for()),           # needs sage.modules
            ....:                         psi2, psi1)
            sage: c3.is_injective()                                                     # needs sage.modules
            False

        TESTS:

        Check that :issue:`23205` has been resolved::

            sage: f = QQ.hom(QQbar) * ZZ.hom(QQ)                                        # needs sage.rings.number_field
            sage: f.is_injective()                                                      # needs sage.rings.number_field
            True"""
    @overload
    def is_surjective(self) -> Any:
        """FormalCompositeMap.is_surjective(self)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 1961)

        Tell whether ``self`` is surjective.

        It raises :exc:`NotImplementedError` if it cannot be determined.

        EXAMPLES::

            sage: from sage.categories.map import FormalCompositeMap
            sage: V3 = QQ^3                                                             # needs sage.modules
            sage: V2 = QQ^2                                                             # needs sage.modules
            sage: V1 = QQ^1                                                             # needs sage.modules

        If both maps are surjective, the composition is surjective::

            sage: # needs sage.modules
            sage: phi32 = V3.hom(Matrix([[1, 2], [3, 4], [5, 6]]), V2)
            sage: phi21 = V2.hom(Matrix([[1], [1]]), V1)
            sage: c_phi = FormalCompositeMap(Hom(V3, V1, phi32.category_for()),
            ....:                            phi32, phi21)
            sage: c_phi.is_surjective()
            True

        If the second map is not surjective, the composition is not
        surjective::

            sage: FormalCompositeMap(Hom(V3, V1, phi32.category_for()),                 # needs sage.modules
            ....:                    phi32,
            ....:                    V2.hom(Matrix([[0], [0]]), V1)).is_surjective()
            False

        If the second map is an isomorphism and the first map is not
        surjective, then the composition is not surjective::

            sage: FormalCompositeMap(Hom(V2, V1, phi32.category_for()),                 # needs sage.modules
            ....:                    V2.hom(Matrix([[0], [0]]), V1),
            ....:                    V1.hom(Matrix([[1]]), V1)).is_surjective()
            False

        Otherwise, surjectivity of the composition cannot be determined::

            sage: FormalCompositeMap(Hom(V2, V1, phi32.category_for()),                 # needs sage.modules
            ....:     V2.hom(Matrix([[1, 1], [1, 1]]), V2),
            ....:     V2.hom(Matrix([[1], [1]]), V1)).is_surjective()
            Traceback (most recent call last):
            ...
            NotImplementedError: not enough information to deduce surjectivity"""
    @overload
    def is_surjective(self) -> Any:
        """FormalCompositeMap.is_surjective(self)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 1961)

        Tell whether ``self`` is surjective.

        It raises :exc:`NotImplementedError` if it cannot be determined.

        EXAMPLES::

            sage: from sage.categories.map import FormalCompositeMap
            sage: V3 = QQ^3                                                             # needs sage.modules
            sage: V2 = QQ^2                                                             # needs sage.modules
            sage: V1 = QQ^1                                                             # needs sage.modules

        If both maps are surjective, the composition is surjective::

            sage: # needs sage.modules
            sage: phi32 = V3.hom(Matrix([[1, 2], [3, 4], [5, 6]]), V2)
            sage: phi21 = V2.hom(Matrix([[1], [1]]), V1)
            sage: c_phi = FormalCompositeMap(Hom(V3, V1, phi32.category_for()),
            ....:                            phi32, phi21)
            sage: c_phi.is_surjective()
            True

        If the second map is not surjective, the composition is not
        surjective::

            sage: FormalCompositeMap(Hom(V3, V1, phi32.category_for()),                 # needs sage.modules
            ....:                    phi32,
            ....:                    V2.hom(Matrix([[0], [0]]), V1)).is_surjective()
            False

        If the second map is an isomorphism and the first map is not
        surjective, then the composition is not surjective::

            sage: FormalCompositeMap(Hom(V2, V1, phi32.category_for()),                 # needs sage.modules
            ....:                    V2.hom(Matrix([[0], [0]]), V1),
            ....:                    V1.hom(Matrix([[1]]), V1)).is_surjective()
            False

        Otherwise, surjectivity of the composition cannot be determined::

            sage: FormalCompositeMap(Hom(V2, V1, phi32.category_for()),                 # needs sage.modules
            ....:     V2.hom(Matrix([[1, 1], [1, 1]]), V2),
            ....:     V2.hom(Matrix([[1], [1]]), V1)).is_surjective()
            Traceback (most recent call last):
            ...
            NotImplementedError: not enough information to deduce surjectivity"""
    @overload
    def is_surjective(self) -> Any:
        """FormalCompositeMap.is_surjective(self)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 1961)

        Tell whether ``self`` is surjective.

        It raises :exc:`NotImplementedError` if it cannot be determined.

        EXAMPLES::

            sage: from sage.categories.map import FormalCompositeMap
            sage: V3 = QQ^3                                                             # needs sage.modules
            sage: V2 = QQ^2                                                             # needs sage.modules
            sage: V1 = QQ^1                                                             # needs sage.modules

        If both maps are surjective, the composition is surjective::

            sage: # needs sage.modules
            sage: phi32 = V3.hom(Matrix([[1, 2], [3, 4], [5, 6]]), V2)
            sage: phi21 = V2.hom(Matrix([[1], [1]]), V1)
            sage: c_phi = FormalCompositeMap(Hom(V3, V1, phi32.category_for()),
            ....:                            phi32, phi21)
            sage: c_phi.is_surjective()
            True

        If the second map is not surjective, the composition is not
        surjective::

            sage: FormalCompositeMap(Hom(V3, V1, phi32.category_for()),                 # needs sage.modules
            ....:                    phi32,
            ....:                    V2.hom(Matrix([[0], [0]]), V1)).is_surjective()
            False

        If the second map is an isomorphism and the first map is not
        surjective, then the composition is not surjective::

            sage: FormalCompositeMap(Hom(V2, V1, phi32.category_for()),                 # needs sage.modules
            ....:                    V2.hom(Matrix([[0], [0]]), V1),
            ....:                    V1.hom(Matrix([[1]]), V1)).is_surjective()
            False

        Otherwise, surjectivity of the composition cannot be determined::

            sage: FormalCompositeMap(Hom(V2, V1, phi32.category_for()),                 # needs sage.modules
            ....:     V2.hom(Matrix([[1, 1], [1, 1]]), V2),
            ....:     V2.hom(Matrix([[1], [1]]), V1)).is_surjective()
            Traceback (most recent call last):
            ...
            NotImplementedError: not enough information to deduce surjectivity"""
    @overload
    def is_surjective(self) -> Any:
        """FormalCompositeMap.is_surjective(self)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 1961)

        Tell whether ``self`` is surjective.

        It raises :exc:`NotImplementedError` if it cannot be determined.

        EXAMPLES::

            sage: from sage.categories.map import FormalCompositeMap
            sage: V3 = QQ^3                                                             # needs sage.modules
            sage: V2 = QQ^2                                                             # needs sage.modules
            sage: V1 = QQ^1                                                             # needs sage.modules

        If both maps are surjective, the composition is surjective::

            sage: # needs sage.modules
            sage: phi32 = V3.hom(Matrix([[1, 2], [3, 4], [5, 6]]), V2)
            sage: phi21 = V2.hom(Matrix([[1], [1]]), V1)
            sage: c_phi = FormalCompositeMap(Hom(V3, V1, phi32.category_for()),
            ....:                            phi32, phi21)
            sage: c_phi.is_surjective()
            True

        If the second map is not surjective, the composition is not
        surjective::

            sage: FormalCompositeMap(Hom(V3, V1, phi32.category_for()),                 # needs sage.modules
            ....:                    phi32,
            ....:                    V2.hom(Matrix([[0], [0]]), V1)).is_surjective()
            False

        If the second map is an isomorphism and the first map is not
        surjective, then the composition is not surjective::

            sage: FormalCompositeMap(Hom(V2, V1, phi32.category_for()),                 # needs sage.modules
            ....:                    V2.hom(Matrix([[0], [0]]), V1),
            ....:                    V1.hom(Matrix([[1]]), V1)).is_surjective()
            False

        Otherwise, surjectivity of the composition cannot be determined::

            sage: FormalCompositeMap(Hom(V2, V1, phi32.category_for()),                 # needs sage.modules
            ....:     V2.hom(Matrix([[1, 1], [1, 1]]), V2),
            ....:     V2.hom(Matrix([[1], [1]]), V1)).is_surjective()
            Traceback (most recent call last):
            ...
            NotImplementedError: not enough information to deduce surjectivity"""
    @overload
    def is_surjective(self) -> Any:
        """FormalCompositeMap.is_surjective(self)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 1961)

        Tell whether ``self`` is surjective.

        It raises :exc:`NotImplementedError` if it cannot be determined.

        EXAMPLES::

            sage: from sage.categories.map import FormalCompositeMap
            sage: V3 = QQ^3                                                             # needs sage.modules
            sage: V2 = QQ^2                                                             # needs sage.modules
            sage: V1 = QQ^1                                                             # needs sage.modules

        If both maps are surjective, the composition is surjective::

            sage: # needs sage.modules
            sage: phi32 = V3.hom(Matrix([[1, 2], [3, 4], [5, 6]]), V2)
            sage: phi21 = V2.hom(Matrix([[1], [1]]), V1)
            sage: c_phi = FormalCompositeMap(Hom(V3, V1, phi32.category_for()),
            ....:                            phi32, phi21)
            sage: c_phi.is_surjective()
            True

        If the second map is not surjective, the composition is not
        surjective::

            sage: FormalCompositeMap(Hom(V3, V1, phi32.category_for()),                 # needs sage.modules
            ....:                    phi32,
            ....:                    V2.hom(Matrix([[0], [0]]), V1)).is_surjective()
            False

        If the second map is an isomorphism and the first map is not
        surjective, then the composition is not surjective::

            sage: FormalCompositeMap(Hom(V2, V1, phi32.category_for()),                 # needs sage.modules
            ....:                    V2.hom(Matrix([[0], [0]]), V1),
            ....:                    V1.hom(Matrix([[1]]), V1)).is_surjective()
            False

        Otherwise, surjectivity of the composition cannot be determined::

            sage: FormalCompositeMap(Hom(V2, V1, phi32.category_for()),                 # needs sage.modules
            ....:     V2.hom(Matrix([[1, 1], [1, 1]]), V2),
            ....:     V2.hom(Matrix([[1], [1]]), V1)).is_surjective()
            Traceback (most recent call last):
            ...
            NotImplementedError: not enough information to deduce surjectivity"""
    def section(self, *args, **kwargs):
        """FormalCompositeMap.section(self)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 2051)

        Compute a section map from sections of the factors of
        ``self`` if they have been implemented.

        EXAMPLES::

            sage: P.<x> = QQ[]
            sage: incl = P.coerce_map_from(ZZ)
            sage: sect = incl.section(); sect
            Composite map:
              From: Univariate Polynomial Ring in x over Rational Field
              To:   Integer Ring
              Defn:   Generic map:
                      From: Univariate Polynomial Ring in x over Rational Field
                      To:   Rational Field
                    then
                      Generic map:
                      From: Rational Field
                      To:   Integer Ring
            sage: p = x + 5; q = x + 2
            sage: sect(p-q)
            3

        the following example has been attached to :meth:`_integer_`
        of :class:`sage.rings.polynomial.polynomial_element.Polynomial`
        before (see comment there)::

            sage: k = GF(47)
            sage: R.<x> = PolynomialRing(k)
            sage: R.coerce_map_from(ZZ).section()
            Composite map:
              From: Univariate Polynomial Ring in x over Finite Field of size 47
              To:   Integer Ring
              Defn:   Generic map:
                      From: Univariate Polynomial Ring in x over Finite Field of size 47
                      To:   Finite Field of size 47
                    then
                      Lifting map:
                      From: Finite Field of size 47
                      To:   Integer Ring
            sage: ZZ(R(45))                 # indirect doctest
            45
            sage: ZZ(3*x + 45)              # indirect doctest
            Traceback (most recent call last):
            ...
            TypeError: 3*x + 45 is not a constant polynomial"""
    def then(self) -> Any:
        """FormalCompositeMap.then(self)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 1849)

        Return the tail of the list of maps.

        If ``self`` represents `f_n \\circ f_{n-1} \\circ \\cdots \\circ
        f_1 \\circ f_0`, then ``self.first()`` returns `f_n \\circ
        f_{n-1} \\circ \\cdots \\circ f_1`.  We have ``self ==
        self.then() * self.first()``.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: S.<a> = QQ[]
            sage: from sage.categories.morphism import SetMorphism
            sage: f = SetMorphism(Hom(R, S, Rings()), lambda p: p[0]*a^p.degree())
            sage: g = S.hom([2*x])
            sage: (f*g).then() == f
            True

            sage: f = QQ.coerce_map_from(ZZ)
            sage: f = f.extend_domain(ZZ).extend_codomain(QQ)
            sage: f.then()
            Composite map:
            From: Integer Ring
            To:   Rational Field
            Defn:   Natural morphism:
            From: Integer Ring
            To:   Rational Field
            then
            Identity endomorphism of Rational Field"""
    def __copy__(self):
        """FormalCompositeMap.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 1566)

        Since :meth:`_extra_slots` would return the uncopied constituents
        of this composite map, we cannot rely on the default copying method
        of maps.

        TESTS::

            sage: copy(QQ['q,t'].coerce_map_from(int))   # indirect doctest
            Composite map:
              From: Set of Python objects of class 'int'
              To:   Multivariate Polynomial Ring in q, t over Rational Field
              Defn:   Native morphism:
                      From: Set of Python objects of class 'int'
                      To:   Rational Field
                    then
                      Polynomial base injection morphism:
                      From: Rational Field
                      To:   Multivariate Polynomial Ring in q, t over Rational Field"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __getitem__(self, i) -> Any:
        """FormalCompositeMap.__getitem__(self, i)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 1677)

        Return the `i`-th map of the formal composition.

        If ``self`` represents `f_n \\circ f_{n-1} \\circ \\cdots \\circ
        f_1 \\circ f_0`, then ``self[i]`` gives `f_i`.  Support
        negative indices as ``list.__getitem__``.  Raise an error if
        the index does not match, in the same way as
        ``list.__getitem__``.

        EXAMPLES::

            sage: from sage.categories.map import Map
            sage: f = Map(ZZ, QQ)
            sage: g = Map(QQ, ZZ)
            sage: (f*g)[0]
            Generic map:
              From: Rational Field
              To:   Integer Ring
            sage: (f*g)[1]
            Generic map:
              From: Integer Ring
              To:   Rational Field
            sage: (f*g)[-1]
            Generic map:
              From: Integer Ring
              To:   Rational Field
            sage: (f*g)[-2]
            Generic map:
              From: Rational Field
              To:   Integer Ring
            sage: (f*g)[-3]
            Traceback (most recent call last):
            ...
            IndexError: list index out of range
            sage: (f*g)[2]
            Traceback (most recent call last):
            ...
            IndexError: list index out of range"""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __hash__(self) -> Any:
        """FormalCompositeMap.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 1652)

        Return the hash of this map.

        TESTS::

            sage: R.<x,y> = QQ[]
            sage: S.<a,b> = QQ[]
            sage: f = R.hom([a+b, a-b])
            sage: g = S.hom([x+y, x-y])
            sage: from sage.categories.map import FormalCompositeMap
            sage: H = Hom(R, R, Rings())
            sage: m = FormalCompositeMap(H, f, g)
            sage: hash(m) == hash(m)
            True
            sage: {m: 1}[m]
            1
            sage: n = FormalCompositeMap(Hom(S, S, Rings()), g, f)
            sage: hash(m) == hash(n)
            False
            sage: len({m: 1, n: 2}.keys())
            2"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""

class Map(sage.structure.element.Element):
    """Map(parent, codomain=None)

    File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 76)

    Basic class for all maps.

    .. NOTE::

        The call method is of course not implemented in this base class. This must
        be done in the sub classes, by overloading ``_call_`` and possibly also
        ``_call_with_args``.

    EXAMPLES:

    Usually, instances of this class will not be constructed directly, but
    for example like this::

        sage: from sage.categories.morphism import SetMorphism
        sage: X.<x> = ZZ[]
        sage: Y = ZZ
        sage: phi = SetMorphism(Hom(X, Y, Rings()), lambda p: p[0])
        sage: phi(x^2+2*x-1)
        -1
        sage: R.<x,y> = QQ[]
        sage: f = R.hom([x+y, x-y], R)
        sage: f(x^2+2*x-1)
        x^2 + 2*x*y + y^2 + 2*x + 2*y - 1"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    codomain: codomain
    domain: domain
    def __init__(self, parent, codomain=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 103)

                INPUT:

                There can be one or two arguments of this init method. If it is one argument,
                it must be a hom space. If it is two arguments, it must be two parent structures
                that will be domain and codomain of the map-to-be-created.

                TESTS::

                    sage: from sage.categories.map import Map

                Using a hom space::

                    sage: Map(Hom(QQ, ZZ, Rings()))
                    Generic map:
                      From: Rational Field
                      To:   Integer Ring

                Using domain and codomain::

                    sage: Map(QQ['x'], SymmetricGroup(6))                                       # needs sage.groups
                    Generic map:
                      From: Univariate Polynomial Ring in x over Rational Field
                      To:   Symmetric group of order 6! as a permutation group
        """
    @overload
    def category_for(self) -> Any:
        """Map.category_for(self)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 635)

        Return the category ``self`` is a morphism for.

        .. NOTE::

            This is different from the category of maps to which this
            map belongs *as an object*.

        EXAMPLES::

            sage: from sage.categories.morphism import SetMorphism
            sage: X.<x> = ZZ[]
            sage: Y = ZZ
            sage: phi = SetMorphism(Hom(X, Y, Rings()), lambda p: p[0])
            sage: phi.category_for()
            Category of rings
            sage: phi.category()
            Category of homsets of unital magmas and additive unital additive magmas
            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x+y, x-y], R)
            sage: f.category_for()
            Join of Category of unique factorization domains
             and Category of algebras with basis over
              (number fields and quotient fields and metric spaces)
             and Category of commutative algebras over
              (number fields and quotient fields and metric spaces)
             and Category of infinite sets
            sage: f.category()
            Category of endsets of unital magmas
             and right modules over (number fields and quotient fields and metric spaces)
             and left modules over (number fields and quotient fields and metric spaces)


        FIXME: find a better name for this method"""
    @overload
    def category_for(self) -> Any:
        """Map.category_for(self)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 635)

        Return the category ``self`` is a morphism for.

        .. NOTE::

            This is different from the category of maps to which this
            map belongs *as an object*.

        EXAMPLES::

            sage: from sage.categories.morphism import SetMorphism
            sage: X.<x> = ZZ[]
            sage: Y = ZZ
            sage: phi = SetMorphism(Hom(X, Y, Rings()), lambda p: p[0])
            sage: phi.category_for()
            Category of rings
            sage: phi.category()
            Category of homsets of unital magmas and additive unital additive magmas
            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x+y, x-y], R)
            sage: f.category_for()
            Join of Category of unique factorization domains
             and Category of algebras with basis over
              (number fields and quotient fields and metric spaces)
             and Category of commutative algebras over
              (number fields and quotient fields and metric spaces)
             and Category of infinite sets
            sage: f.category()
            Category of endsets of unital magmas
             and right modules over (number fields and quotient fields and metric spaces)
             and left modules over (number fields and quotient fields and metric spaces)


        FIXME: find a better name for this method"""
    @overload
    def category_for(self) -> Any:
        """Map.category_for(self)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 635)

        Return the category ``self`` is a morphism for.

        .. NOTE::

            This is different from the category of maps to which this
            map belongs *as an object*.

        EXAMPLES::

            sage: from sage.categories.morphism import SetMorphism
            sage: X.<x> = ZZ[]
            sage: Y = ZZ
            sage: phi = SetMorphism(Hom(X, Y, Rings()), lambda p: p[0])
            sage: phi.category_for()
            Category of rings
            sage: phi.category()
            Category of homsets of unital magmas and additive unital additive magmas
            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x+y, x-y], R)
            sage: f.category_for()
            Join of Category of unique factorization domains
             and Category of algebras with basis over
              (number fields and quotient fields and metric spaces)
             and Category of commutative algebras over
              (number fields and quotient fields and metric spaces)
             and Category of infinite sets
            sage: f.category()
            Category of endsets of unital magmas
             and right modules over (number fields and quotient fields and metric spaces)
             and left modules over (number fields and quotient fields and metric spaces)


        FIXME: find a better name for this method"""
    @overload
    def domains(self) -> Any:
        """Map.domains(self)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 620)

        Iterate over the domains of the factors of a (composite) map.

        This default implementation simply yields the domain of this map.

        .. SEEALSO:: :meth:`FormalCompositeMap.domains`

        EXAMPLES::

            sage: list(QQ.coerce_map_from(ZZ).domains())
            [Integer Ring]"""
    @overload
    def domains(self) -> Any:
        """Map.domains(self)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 620)

        Iterate over the domains of the factors of a (composite) map.

        This default implementation simply yields the domain of this map.

        .. SEEALSO:: :meth:`FormalCompositeMap.domains`

        EXAMPLES::

            sage: list(QQ.coerce_map_from(ZZ).domains())
            [Integer Ring]"""
    def extend_codomain(self, new_codomain) -> Any:
        """Map.extend_codomain(self, new_codomain)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 1178)

        INPUT:

        - ``self`` -- a member of Hom(X, Y)
        - ``new_codomain`` -- an object Z such that there is a canonical coercion
          `\\phi` in Hom(Y, Z)

        OUTPUT:

        An element of Hom(X, Z) obtained by composing ``self`` with `\\phi`.  If
        no canonical `\\phi` exists, a :exc:`TypeError` is raised.

        EXAMPLES::

            sage: mor = QQ.coerce_map_from(ZZ)
            sage: mor.extend_codomain(RDF)
            Composite map:
              From: Integer Ring
              To:   Real Double Field
              Defn:   Natural morphism:
                      From: Integer Ring
                      To:   Rational Field
                    then
                      Native morphism:
                      From: Rational Field
                      To:   Real Double Field
            sage: mor.extend_codomain(GF(7))
            Traceback (most recent call last):
            ...
            TypeError: No coercion from Rational Field to Finite Field of size 7"""
    def extend_domain(self, new_domain) -> Any:
        """Map.extend_domain(self, new_domain)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 1133)

        INPUT:

        - ``self`` -- a member of Hom(Y, Z)
        - ``new_codomain`` -- an object X such that there is a canonical coercion
          `\\phi` in Hom(X, Y)

        OUTPUT:

        An element of Hom(X, Z) obtained by composing self with `\\phi`.  If
        no canonical `\\phi` exists, a :exc:`TypeError` is raised.

        EXAMPLES::

            sage: # needs sage.rings.complex_double
            sage: mor = CDF.coerce_map_from(RDF)
            sage: mor.extend_domain(QQ)
            Composite map:
              From: Rational Field
              To:   Complex Double Field
              Defn:   Native morphism:
                      From: Rational Field
                      To:   Real Double Field
                    then
                      Native morphism:
                      From: Real Double Field
                      To:   Complex Double Field
            sage: mor.extend_domain(ZZ['x'])
            Traceback (most recent call last):
            ...
            TypeError: No coercion from Univariate Polynomial Ring in x over Integer Ring
            to Real Double Field"""
    @overload
    def is_surjective(self) -> Any:
        """Map.is_surjective(self)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 1218)

        Tell whether the map is surjective (not implemented in the base class).

        TESTS::

            sage: from sage.categories.map import Map
            sage: f = Map(Hom(QQ, ZZ, Rings()))
            sage: f.is_surjective()
            Traceback (most recent call last):
            ...
            NotImplementedError: <class 'sage.categories.map.Map'>"""
    @overload
    def is_surjective(self) -> Any:
        """Map.is_surjective(self)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 1218)

        Tell whether the map is surjective (not implemented in the base class).

        TESTS::

            sage: from sage.categories.map import Map
            sage: f = Map(Hom(QQ, ZZ, Rings()))
            sage: f.is_surjective()
            Traceback (most recent call last):
            ...
            NotImplementedError: <class 'sage.categories.map.Map'>"""
    def parent(self, *args, **kwargs):
        """Map.parent(self)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 190)

        Return the homset containing this map.

        .. NOTE::

            The method :meth:`_make_weak_references`, that is used for the maps
            found by the coercion system, needs to remove the usual strong
            reference from the coercion map to the homset containing it. As long
            as the user keeps strong references to domain and codomain of the map,
            we will be able to reconstruct the homset. However, a strong reference
            to the coercion map does not prevent the domain from garbage collection!

        EXAMPLES::

            sage: Q = QuadraticField(-5)                                                # needs sage.rings.number_field
            sage: phi = CDF._internal_convert_map_from(Q)                               # needs sage.rings.number_field
            sage: print(phi.parent())                                                   # needs sage.rings.number_field
            Set of field embeddings
             from Number Field in a with defining polynomial x^2 + 5
                  with a = 2.236067977499790?*I
               to Complex Double Field

        We now demonstrate that the reference to the coercion map `\\phi` does
        not prevent `Q` from being garbage collected::

            sage: import gc
            sage: del Q                                                                 # needs sage.rings.number_field
            sage: _ = gc.collect()
            sage: phi.parent()                                                          # needs sage.rings.number_field
            Traceback (most recent call last):
            ...
            ValueError: This map is in an invalid state,
            the domain has been garbage collected

        You can still obtain copies of the maps used by the coercion system with
        strong references::

            sage: # needs sage.rings.number_field
            sage: Q = QuadraticField(-5)
            sage: phi = CDF.convert_map_from(Q)
            sage: print(phi.parent())
            Set of field embeddings
             from Number Field in a with defining polynomial x^2 + 5
                  with a = 2.236067977499790?*I
               to Complex Double Field
            sage: import gc
            sage: del Q
            sage: _ = gc.collect()
            sage: phi.parent()
            Set of field embeddings
             from Number Field in a with defining polynomial x^2 + 5
                  with a = 2.236067977499790?*I
               to Complex Double Field"""
    def post_compose(self, *args, **kwargs):
        """Map.post_compose(self, left)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 1096)

        INPUT:

        - ``self`` -- a Map in some ``Hom(X, Y, category_right)``
        - ``left`` -- a Map in some ``Hom(Y, Z, category_left)``

        Returns the composition of ``self`` followed by ``left`` as a
        morphism in ``Hom(X, Z, category)`` where ``category`` is the
        meet of ``category_left`` and ``category_right``.

        Caveat: see the current restrictions on :meth:`Category.meet`

        EXAMPLES::

            sage: from sage.categories.morphism import SetMorphism
            sage: X.<x> = ZZ[]
            sage: Y = ZZ
            sage: Z = QQ
            sage: phi_xy = SetMorphism(Hom(X, Y, Rings()), lambda p: p[0])
            sage: phi_yz = SetMorphism(Hom(Y, Z, Monoids()), lambda y: QQ(y**2))
            sage: phi_xz = phi_xy.post_compose(phi_yz); phi_xz
            Composite map:
              From: Univariate Polynomial Ring in x over Integer Ring
              To:   Rational Field
              Defn:   Generic morphism:
                      From: Univariate Polynomial Ring in x over Integer Ring
                      To:   Integer Ring
                    then
                      Generic morphism:
                      From: Integer Ring
                      To:   Rational Field
            sage: phi_xz.category_for()
            Category of monoids"""
    def pre_compose(self, *args, **kwargs):
        """Map.pre_compose(self, right)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 1058)

        INPUT:

        - ``self`` -- a Map in some ``Hom(Y, Z, category_left)``
        - ``left`` -- a Map in some ``Hom(X, Y, category_right)``

        Returns the composition of ``right`` followed by ``self`` as a
        morphism in ``Hom(X, Z, category)`` where ``category`` is the
        meet of ``category_left`` and ``category_right``.

        EXAMPLES::

            sage: from sage.categories.morphism import SetMorphism
            sage: X.<x> = ZZ[]
            sage: Y = ZZ
            sage: Z = QQ
            sage: phi_xy = SetMorphism(Hom(X, Y, Rings()), lambda p: p[0])
            sage: phi_yz = SetMorphism(Hom(Y, Z, Monoids()), lambda y: QQ(y**2))
            sage: phi_xz = phi_yz.pre_compose(phi_xy); phi_xz
            Composite map:
              From: Univariate Polynomial Ring in x over Integer Ring
              To:   Rational Field
              Defn:   Generic morphism:
                      From: Univariate Polynomial Ring in x over Integer Ring
                      To:   Integer Ring
                    then
                      Generic morphism:
                      From: Integer Ring
                      To:   Rational Field
            sage: phi_xz.category_for()
            Category of monoids"""
    @overload
    def section(self) -> Any:
        """Map.section(self)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 1281)

        Return a section of ``self``.

        .. NOTE::

            By default, it returns ``None``. You may override it in subclasses.

        TESTS::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x+y, x-y], R)
            sage: print(f.section())
            None

            sage: f = QQ.coerce_map_from(ZZ); f
            Natural morphism:
              From: Integer Ring
              To:   Rational Field
            sage: ff = f.section(); ff
            Generic map:
              From: Rational Field
              To:   Integer Ring
            sage: ff(4/2)
            2
            sage: parent(ff(4/2)) is ZZ
            True
            sage: ff(1/2)
            Traceback (most recent call last):
            ...
            TypeError: no conversion of this rational to integer"""
    @overload
    def section(self) -> Any:
        """Map.section(self)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 1281)

        Return a section of ``self``.

        .. NOTE::

            By default, it returns ``None``. You may override it in subclasses.

        TESTS::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x+y, x-y], R)
            sage: print(f.section())
            None

            sage: f = QQ.coerce_map_from(ZZ); f
            Natural morphism:
              From: Integer Ring
              To:   Rational Field
            sage: ff = f.section(); ff
            Generic map:
              From: Rational Field
              To:   Integer Ring
            sage: ff(4/2)
            2
            sage: parent(ff(4/2)) is ZZ
            True
            sage: ff(1/2)
            Traceback (most recent call last):
            ...
            TypeError: no conversion of this rational to integer"""
    @overload
    def section(self) -> Any:
        """Map.section(self)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 1281)

        Return a section of ``self``.

        .. NOTE::

            By default, it returns ``None``. You may override it in subclasses.

        TESTS::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x+y, x-y], R)
            sage: print(f.section())
            None

            sage: f = QQ.coerce_map_from(ZZ); f
            Natural morphism:
              From: Integer Ring
              To:   Rational Field
            sage: ff = f.section(); ff
            Generic map:
              From: Rational Field
              To:   Integer Ring
            sage: ff(4/2)
            2
            sage: parent(ff(4/2)) is ZZ
            True
            sage: ff(1/2)
            Traceback (most recent call last):
            ...
            TypeError: no conversion of this rational to integer"""
    def __call__(self, x, *args, **kwds) -> Any:
        '''Map.__call__(self, x, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 680)

        Apply this map to ``x``.

        IMPLEMENTATION:

        - To implement the call method in a subclass of Map, implement
          :meth:`_call_` and possibly also :meth:`_call_with_args` and
          :meth:`pushforward`.
        - If the parent of ``x`` cannot be coerced into the domain of
          ``self``, then the method ``pushforward`` is called with ``x``
          and the other given arguments, provided it is implemented.
          In that way, ``self`` could be applied to objects like ideals
          or sub-modules.
        - If there is no coercion and if ``pushforward`` is not implemented
          or fails, ``_call_`` is  called after conversion into the domain
          (which may be possible even when there is no coercion); if there
          are additional arguments (or keyword arguments),
          :meth:`_call_with_args` is called instead. Note that the
          positional arguments after ``x`` are passed as a tuple to
          :meth:`_call_with_args` and the named arguments are passed
          as a dictionary.

        INPUT:

        - ``x`` -- an element coercible to the domain of ``self``; also objects
          like ideals are supported in some cases

        OUTPUT:

        an element (or ideal, etc.)

        EXAMPLES::

            sage: R.<x,y> = QQ[]; phi = R.hom([y, x])
            sage: phi(y)          # indirect doctest
            x

        We take the image of an ideal::

            sage: I = ideal(x, y); I
            Ideal (x, y) of Multivariate Polynomial Ring in x, y over Rational Field
            sage: phi(I)
            Ideal (y, x) of Multivariate Polynomial Ring in x, y over Rational Field

        TESTS:

        We test that the map can be applied to something that converts
        (but not coerces) into the domain and can *not* be dealt with
        by :meth:`pushforward` (see :issue:`10496`)::

            sage: D = {(0, 2): -1, (0, 0): -1, (1, 1): 7, (2, 0): 1/3}
            sage: phi(D)
            -x^2 + 7*x*y + 1/3*y^2 - 1

        We test what happens if the argument can\'t be converted into
        the domain::

            sage: from sage.categories.map import Map
            sage: f = Map(Hom(ZZ, QQ, Rings()))
            sage: f(1/2)
            Traceback (most recent call last):
            ...
            TypeError: 1/2 fails to convert into the map\'s domain Integer Ring,
            but a `pushforward` method is not properly implemented

        We test that the default call method really works as described
        above (that was fixed in :issue:`10496`)::

            sage: class FOO(Map):
            ....:   def _call_(self, x):
            ....:       print("_call_ {}".format(parent(x)))
            ....:       return self.codomain()(x)
            ....:   def _call_with_args(self, x, args=(), kwds={}):
            ....:       print("_call_with_args {}".format(parent(x)))
            ....:       return self.codomain()(x)^kwds.get(\'exponent\', 1)
            ....:   def pushforward(self, x, exponent=1):
            ....:       print("pushforward {}".format(parent(x)))
            ....:       return self.codomain()(1/x)^exponent
            sage: f = FOO(ZZ, QQ)
            sage: f(1/1)   #indirect doctest
            pushforward Rational Field
            1

        ``_call_`` and ``_call_with_args_`` are used *after* coercion::

            sage: f(int(1))
            _call_ Integer Ring
            1
            sage: f(int(2), exponent=2)
            _call_with_args Integer Ring
            4

        ``pushforward`` is called without conversion::

            sage: f(1/2)
            pushforward Rational Field
            2
            sage: f(1/2, exponent=2)
            pushforward Rational Field
            4

        If the argument does not coerce into the domain, and if
        ``pushforward`` fails, ``_call_`` is tried after conversion::

            sage: g = FOO(QQ, ZZ)
            sage: g(SR(3))                                                              # needs sage.symbolic
            pushforward Symbolic Ring
            _call_ Rational Field
            3
            sage: g(SR(3), exponent=2)                                                  # needs sage.symbolic
            pushforward Symbolic Ring
            _call_with_args Rational Field
            9

        If conversion fails as well, an error is raised::

            sage: h = FOO(ZZ, ZZ)
            sage: h(2/3)
            Traceback (most recent call last):
            ...
            TypeError: 2/3 fails to convert into the map\'s domain Integer Ring,
            but a `pushforward` method is not properly implemented'''
    def __copy__(self):
        """Map.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 148)

        Return copy, with strong references to domain and codomain.

        .. NOTE::

            To implement copying on sub-classes, do not override this method, but
            implement cdef methods ``_extra_slots()`` returning a dictionary and
            ``_update_slots()`` using this dictionary to fill the cdef or cpdef
            slots of the subclass.

        EXAMPLES::

            sage: phi = QQ['x']._internal_coerce_map_from(ZZ)
            sage: phi.domain
            <weakref at ...; to 'sage.rings.integer_ring.IntegerRing_class' at ...>
            sage: type(phi)
            <class 'sage.categories.map.FormalCompositeMap'>
            sage: psi = copy(phi)   # indirect doctest
            sage: psi
            Composite map:
              From: Integer Ring
              To:   Univariate Polynomial Ring in x over Rational Field
              Defn:   Natural morphism:
                      From: Integer Ring
                      To:   Rational Field
                    then
                      Polynomial base injection morphism:
                      From: Rational Field
                      To:   Univariate Polynomial Ring in x over Rational Field
            sage: psi.domain
            The constant function (...) -> Integer Ring
            sage: psi(3)
            3"""
    def __hash__(self) -> Any:
        """Map.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 1315)

        Return the hash of this map.

        TESTS::

            sage: f = sage.rings.morphism.RingMap(ZZ.Hom(ZZ))
            sage: type(f)
            <class 'sage.rings.morphism.RingMap'>
            sage: hash(f) == hash(f)
            True
            sage: {f: 1}[f]
            1"""
    def __mul__(self, right) -> Any:
        """Map.__mul__(self, right)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 860)

        The multiplication * operator is operator composition.

        IMPLEMENTATION:

        If you want to change the behaviour of composition for
        derived classes, please overload :meth:`_composition_`
        (but not :meth:`_composition`!) of the left factor.

        INPUT:

        - ``self`` -- Map
        - ``right`` -- Map

        OUTPUT:

        The map `x \\mapsto self(right(x))`.

        EXAMPLES::

            sage: from sage.categories.morphism import SetMorphism
            sage: X.<x> = ZZ[]
            sage: Y = ZZ
            sage: Z = QQ
            sage: phi_xy = SetMorphism(Hom(X, Y, Rings()), lambda p: p[0])
            sage: phi_yz = SetMorphism(Hom(Y, Z, CommutativeAdditiveMonoids()), lambda y: QQ(y)/2)
            sage: phi_yz * phi_xy
            Composite map:
              From: Univariate Polynomial Ring in x over Integer Ring
              To:   Rational Field
              Defn:   Generic morphism:
                      From: Univariate Polynomial Ring in x over Integer Ring
                      To:   Integer Ring
                    then
                      Generic morphism:
                      From: Integer Ring
                      To:   Rational Field

        If ``right`` is a ring homomorphism given by the images of
        generators, then it is attempted to form the composition
        accordingly. Only if this fails, or if the result does not
        belong to the given homset, a formal composite map is
        returned (as above).
        ::

            sage: R.<x,y> = QQ[]
            sage: S.<a,b> = QQ[]
            sage: f = R.hom([x+y, x-y], R)
            sage: f = R.hom([a+b, a-b])
            sage: g = S.hom([x+y, x-y])
            sage: f*g
            Ring endomorphism of Multivariate Polynomial Ring in a, b over Rational Field
              Defn: a |--> 2*a
                    b |--> 2*b
            sage: h = SetMorphism(Hom(S, QQ, Rings()), lambda p: p.lc())
            sage: h*f
            Composite map:
              From: Multivariate Polynomial Ring in x, y over Rational Field
              To:   Rational Field
              Defn:   Ring morphism:
                      From: Multivariate Polynomial Ring in x, y over Rational Field
                      To:   Multivariate Polynomial Ring in a, b over Rational Field
                      Defn: x |--> a + b
                            y |--> a - b
                    then
                      Generic morphism:
                      From: Multivariate Polynomial Ring in a, b over Rational Field
                      To:   Rational Field"""
    def __reduce__(self) -> Any:
        """Map.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 486)

        TESTS::

            sage: from sage.categories.map import Map
            sage: f = Map(Hom(QQ, ZZ, Rings())); f
            Generic map:
              From: Rational Field
              To:   Integer Ring
            sage: loads(dumps(f))  # indirect doctest
            Generic map:
              From: Rational Field
              To:   Integer Ring"""
    def __rmul__(self, other):
        """Return value*self."""

class Section(Map):
    """Section(map)

    File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 1334)

    A formal section of a map.

    .. NOTE::

        Call methods are not implemented for the base class ``Section``.

    EXAMPLES::

        sage: from sage.categories.map import Section
        sage: R.<x,y> = ZZ[]
        sage: S.<a,b> = QQ[]
        sage: f = R.hom([a+b, a-b])
        sage: sf = Section(f); sf
        Section map:
          From: Multivariate Polynomial Ring in a, b over Rational Field
          To:   Multivariate Polynomial Ring in x, y over Integer Ring
        sage: sf(a)
        Traceback (most recent call last):
        ...
        NotImplementedError: <class 'sage.categories.map.Section'>"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @overload
    def __init__(self, map) -> Any:
        """File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 1358)

                INPUT:

                - ``map`` -- a map

                TESTS::

                    sage: from sage.categories.map import Section
                    sage: R.<x,y> = QQ[]
                    sage: f = R.hom([x+y, x-y], R)
                    sage: sf = Section(f); sf
                    Section map:
                      From: Multivariate Polynomial Ring in x, y over Rational Field
                      To:   Multivariate Polynomial Ring in x, y over Rational Field
        """
    @overload
    def __init__(self, f) -> Any:
        """File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 1358)

                INPUT:

                - ``map`` -- a map

                TESTS::

                    sage: from sage.categories.map import Section
                    sage: R.<x,y> = QQ[]
                    sage: f = R.hom([x+y, x-y], R)
                    sage: sf = Section(f); sf
                    Section map:
                      From: Multivariate Polynomial Ring in x, y over Rational Field
                      To:   Multivariate Polynomial Ring in x, y over Rational Field
        """
    @overload
    def inverse(self) -> Any:
        """Section.inverse(self)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 1433)

        Return inverse of ``self``.

        TESTS::

            sage: from sage.categories.map import Section
            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x+y, x-y], R)
            sage: sf = Section(f)
            sage: sf.inverse()
            Ring endomorphism of Multivariate Polynomial Ring in x, y over Rational Field
              Defn: x |--> x + y
                    y |--> x - y"""
    @overload
    def inverse(self) -> Any:
        """Section.inverse(self)

        File: /build/sagemath/src/sage/src/sage/categories/map.pyx (starting at line 1433)

        Return inverse of ``self``.

        TESTS::

            sage: from sage.categories.map import Section
            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x+y, x-y], R)
            sage: sf = Section(f)
            sage: sf.inverse()
            Ring endomorphism of Multivariate Polynomial Ring in x, y over Rational Field
              Defn: x |--> x + y
                    y |--> x - y"""
