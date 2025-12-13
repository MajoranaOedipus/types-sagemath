import sage.structure.element
import sage.structure.parent
import sage.structure.unique_representation
from sage.categories.magmatic_algebras import MagmaticAlgebras as MagmaticAlgebras
from sage.categories.metric_spaces import MetricSpaces as MetricSpaces
from sage.categories.rings import Rings as Rings
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.functional import sqrt as sqrt
from sage.modules.free_module import FreeModule as FreeModule
from sage.structure.category_object import normalize_names as normalize_names
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation
from typing import Any, ClassVar, overload

class Octonion(Octonion_generic):
    """File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 535)

        An octonion.

        This is an element of the octonion algebra with parameters
        `a = b = c = -1`, which is a classical octonion number.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def norm(self) -> Any:
        """Octonion.norm(self)

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 561)

        Return the norm of ``self``.

        The norm of an octonion `x` is `\\lVert x \\rVert = \\sqrt{x x^*}`,
        where `x^*` is the :meth:`conjugate` of `x`.

        .. SEEALSO::

            This is the square root of :meth:`quadratic_form()`.

        EXAMPLES::

            sage: O = OctonionAlgebra(QQ)
            sage: elt = sum(i * b for i, b in enumerate(O.basis(), start=2))
            sage: elt.norm()                                                            # needs sage.symbolic
            2*sqrt(71)
            sage: elt = sum(O.basis())
            sage: elt.norm()                                                            # needs sage.symbolic
            2*sqrt(2)"""
    @overload
    def quadratic_form(self) -> Any:
        """Octonion.quadratic_form(self)

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 542)

        Return the quadratic form of ``self``.

        The octonion algebra has a distinguished quadratic form given
        by `N(x) = x x^*`, where `x^*` is the :meth:`conjugate` of `x`.

        EXAMPLES::

            sage: O = OctonionAlgebra(QQ)
            sage: elt = sum(O.basis()); elt
            1 + i + j + k + l + li + lj + lk
            sage: elt.quadratic_form()
            8
            sage: elt * elt.conjugate()
            8"""
    @overload
    def quadratic_form(self) -> Any:
        """Octonion.quadratic_form(self)

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 542)

        Return the quadratic form of ``self``.

        The octonion algebra has a distinguished quadratic form given
        by `N(x) = x x^*`, where `x^*` is the :meth:`conjugate` of `x`.

        EXAMPLES::

            sage: O = OctonionAlgebra(QQ)
            sage: elt = sum(O.basis()); elt
            1 + i + j + k + l + li + lj + lk
            sage: elt.quadratic_form()
            8
            sage: elt * elt.conjugate()
            8"""

class OctonionAlgebra(sage.structure.unique_representation.UniqueRepresentation, sage.structure.parent.Parent):
    """File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 585)

        The octonion algebra.

        Let `R` be a commutative ring of characteristic not equal to `2`. The
        *octonion algebra* with parameters `a, b, c` is a non-associative
        non-commutative unital 8-dimensional `R`-algebra that is a deformation
        of the usual octonions, which are when `a = b = c = -1`. The octonions
        were originally constructed by Graves and independently discovered by
        Cayley (due to being published first, these are sometimes called
        the Cayley numbers) and can also be built from the Cayley-Dickson
        construction with the :class:`quaternions <QuaternionAlgebra>`.

        We use the multiplication table from [Scha1996]_. The octonion
        algebra `\\mathbf{O}_{a,b,c}(R)` is a composition (Hurwitz) algebra,
        which means it is also an alternative algebra as it satisfies
        `x^2 y = (x x) y = x (x y)` and  `y x^2 = y (x x) = (y x) x`
        for all `x, y \\in \\mathbf{O}_{a,b,c}`.

        EXAMPLES:

        We first create the classical octonions and perform some basic
        computations::

            sage: O = OctonionAlgebra(QQ)
            sage: O
            Octonion algebra over Rational Field
            sage: i, j, k, l = O.gens()
            sage: i * j * k
            1
            sage: k * j * i
            -1
            sage: (i * k) * l
            -lj
            sage: i * (k * l)
            lj
            sage: elt = sum(O.basis())
            sage: elt^2
            -6 + 2*i + 2*j + 2*k + 2*l + 2*li + 2*lj + 2*lk
            sage: prod(O.basis())
            1
            sage: (i + l)^2
            -2
            sage: (1 + l) * (1 + l).conjugate()
            2
            sage: S = O.some_elements()
            sage: B = O.basis()
            sage: S.extend(x * (i + j/2 - 5*k/3) for x in O.some_elements())
            sage: all((x * x) * y == (x * (x * y)) for x in S for y in S)
            True
            sage: all(y * (x * x) == (y * x) * x for x in S for y in S)
            True
            sage: all((x + x.conjugate()) / 2 == x.real_part() for x in S)
            True
            sage: all((x - x.conjugate()) / 2 == x.imag_part() for x in S)
            True
            sage: all(sum((b*x)*b for b in B) == -6 * x.conjugate() for x in S)
            True

        We construct the (rescaled) `E_8` lattice as the integral octonions,
        which we verify by constructing `240` shortest length elements in
        the lattice (see also :wikipedia:`E8_lattice#Integral_octonions`)::

            sage: m = (i + j + k + l) / 2
            sage: basis = [i, j, i*j, i^2, m, i * m, j * m, (i * j) * m]
            sage: basis
            [i,
             j,
             -k,
             -1,
             1/2*i + 1/2*j + 1/2*k + 1/2*l,
             -1/2 + 1/2*j - 1/2*k - 1/2*li,
             -1/2 - 1/2*i + 1/2*k - 1/2*lj,
             1/2 - 1/2*i + 1/2*j + 1/2*lk]
            sage: matrix([vector(b) for b in basis]).rank()
            8
            sage: [b.norm() for b in basis]
            [1, 1, 1, 1, 1, 1, 1, 1]
            sage: roots = set(basis)
            sage: roots.update(-b for b in basis)
            sage: new_roots = set(roots)  # make a copy
            sage: while new_roots:
            ....:     prev_roots = new_roots
            ....:     new_roots = set()
            ....:     for a in prev_roots:
            ....:         for b in roots:
            ....:             c = a + b
            ....:             if c.quadratic_form() != 1 or c in roots:
            ....:                 continue
            ....:             new_roots.update([c, -c])
            ....:         roots.update(new_roots)
            sage: len(roots)
            240

        A classical construction of the Lie algebra of type `G_2` is
        the Lie algebra of all derivations of `\\mathbf{O}` (as the
        automorphism group is the Lie group of type `G_2`). We verify
        that the derivations have the correct dimension::

            sage: len(O.derivations_basis())
            14

        We can construct the split octonions by taking the parameter `c = 1`::

            sage: SO = OctonionAlgebra(QQ, c=1)
            sage: SO
            Octonion algebra over Rational Field with parameters (-1, -1, 1)
            sage: i, j, k, l = SO.gens()
            sage: i^2 == j^2 == k^2 == -1
            True
            sage: l^2
            1
            sage: (i + l)^2
            0
            sage: (1 + l) * (1 + l).conjugate()
            0

        REFERENCES:

        - [Scha1996]_
        - :wikipedia:`octonion`
        - :wikipedia:`Split-octonion`
        - :wikipedia:`Hurwitz's_theorem_(composition_algebras)`
    """

    class Element(sage.structure.element.AlgebraElement):
        """Octonion_generic(parent, v)

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 32)

        An octonion with generic parameters."""
        __pyx_vtable__: ClassVar[PyCapsule] = ...
        def __init__(self, *args, **kwargs) -> None:
            """File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 36)

                    Initialize ``self``.

                    EXAMPLES::

                        sage: O = OctonionAlgebra(QQ, 1, 3, 7)
                        sage: elt = sum(i * b for i, b in enumerate(O.basis(), start=2))
                        sage: TestSuite(elt).run()
                        sage: elt = sum(O.basis())
                        sage: TestSuite(elt).run()
                        sage: TestSuite(O.zero()).run()

                        sage: O = OctonionAlgebra(Zmod(8), 1, 3, 7)
                        sage: elt = sum(i * b for i, b in enumerate(O.basis(), start=2))
                        sage: TestSuite(elt).run()
                        sage: elt = sum(O.basis())
                        sage: TestSuite(elt).run()
                        sage: TestSuite(O.zero()).run()
        """
        def abs(self) -> Any:
            """Octonion_generic.abs(self)

            File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 427)

            Return the absolute value of ``self``.

            This is equal to the :meth:`norm`.

            .. WARNING::

                If any of the parameters `a, b, c \\not> 0`, then this does
                not define a metric.

            EXAMPLES::

                sage: O = OctonionAlgebra(QQ, 1, 3, 7)
                sage: elt = sum(i * b for i, b in enumerate(O.basis(), start=2))
                sage: elt.abs()                                                             # needs sage.symbolic
                2*sqrt(-61)
                sage: elt = sum(O.basis())
                sage: elt.abs()
                0"""
        @overload
        def conjugate(self) -> Octonion_generic:
            """Octonion_generic.conjugate(self) -> Octonion_generic

            File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 360)

            Return the conjugate of ``self``.

            EXAMPLES::

                sage: O = OctonionAlgebra(QQ)
                sage: elt = sum(O.basis()); elt
                1 + i + j + k + l + li + lj + lk
                sage: elt.conjugate()
                1 - i - j - k - l - li - lj - lk"""
        @overload
        def conjugate(self) -> Any:
            """Octonion_generic.conjugate(self) -> Octonion_generic

            File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 360)

            Return the conjugate of ``self``.

            EXAMPLES::

                sage: O = OctonionAlgebra(QQ)
                sage: elt = sum(O.basis()); elt
                1 + i + j + k + l + li + lj + lk
                sage: elt.conjugate()
                1 - i - j - k - l - li - lj - lk"""
        def dict(self, *args, **kwargs):
            """Octonion_generic.monomial_coefficients(self, copy=False)

            File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 513)

            Return ``self`` as a ``dict`` with keys being indices
            for the basis and the values being the corresponding
            nonzero coefficients.

            INPUT:

            - ``copy`` -- ignored

            EXAMPLES::

                sage: O = OctonionAlgebra(QQ)
                sage: x = O([2/7, 0, 0, 0, 2/3, 0, -5, 0])
                sage: x.monomial_coefficients()
                {0: 2/7, 4: 2/3, 6: -5}"""
        @overload
        def imag_part(self) -> Octonion_generic:
            """Octonion_generic.imag_part(self) -> Octonion_generic

            File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 468)

            Return the imginary part of ``self``.

            OUTPUT: the imaginary part of ``self`` as an element in the octonion algebra

            EXAMPLES::

                sage: O = OctonionAlgebra(QQ)
                sage: elt = sum(i * b for i, b in enumerate(O.basis(), start=2)); elt
                2 + 3*i + 4*j + 5*k + 6*l + 7*li + 8*lj + 9*lk
                sage: elt.imag_part()
                3*i + 4*j + 5*k + 6*l + 7*li + 8*lj + 9*lk

            TESTS::

                sage: O = OctonionAlgebra(QQ)
                sage: elt = sum(i * b for i, b in enumerate(O.basis(), start=2))
                sage: elt.imag_part()
                3*i + 4*j + 5*k + 6*l + 7*li + 8*lj + 9*lk
                sage: elt
                2 + 3*i + 4*j + 5*k + 6*l + 7*li + 8*lj + 9*lk"""
        @overload
        def imag_part(self) -> Any:
            """Octonion_generic.imag_part(self) -> Octonion_generic

            File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 468)

            Return the imginary part of ``self``.

            OUTPUT: the imaginary part of ``self`` as an element in the octonion algebra

            EXAMPLES::

                sage: O = OctonionAlgebra(QQ)
                sage: elt = sum(i * b for i, b in enumerate(O.basis(), start=2)); elt
                2 + 3*i + 4*j + 5*k + 6*l + 7*li + 8*lj + 9*lk
                sage: elt.imag_part()
                3*i + 4*j + 5*k + 6*l + 7*li + 8*lj + 9*lk

            TESTS::

                sage: O = OctonionAlgebra(QQ)
                sage: elt = sum(i * b for i, b in enumerate(O.basis(), start=2))
                sage: elt.imag_part()
                3*i + 4*j + 5*k + 6*l + 7*li + 8*lj + 9*lk
                sage: elt
                2 + 3*i + 4*j + 5*k + 6*l + 7*li + 8*lj + 9*lk"""
        @overload
        def imag_part(self) -> Any:
            """Octonion_generic.imag_part(self) -> Octonion_generic

            File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 468)

            Return the imginary part of ``self``.

            OUTPUT: the imaginary part of ``self`` as an element in the octonion algebra

            EXAMPLES::

                sage: O = OctonionAlgebra(QQ)
                sage: elt = sum(i * b for i, b in enumerate(O.basis(), start=2)); elt
                2 + 3*i + 4*j + 5*k + 6*l + 7*li + 8*lj + 9*lk
                sage: elt.imag_part()
                3*i + 4*j + 5*k + 6*l + 7*li + 8*lj + 9*lk

            TESTS::

                sage: O = OctonionAlgebra(QQ)
                sage: elt = sum(i * b for i, b in enumerate(O.basis(), start=2))
                sage: elt.imag_part()
                3*i + 4*j + 5*k + 6*l + 7*li + 8*lj + 9*lk
                sage: elt
                2 + 3*i + 4*j + 5*k + 6*l + 7*li + 8*lj + 9*lk"""
        @overload
        def is_unit(self) -> Any:
            """Octonion_generic.is_unit(self)

            File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 291)

            Return if ``self`` is a unit or not.

            EXAMPLES::

                sage: O = OctonionAlgebra(ZZ)
                sage: x = O([1, 0, 1, 0, 0, 0, 0, 0])
                sage: x.quadratic_form()
                2
                sage: x.is_unit()
                False
                sage: O([1, 0, -1, 0, 0, 0, 0, 0]).is_unit()
                False
                sage: x = O([1, 0, 0, 0, 1, 0, 0, 0])
                sage: x.quadratic_form()
                2
                sage: x.is_unit()
                False
                sage: x = O([0, 0, 0, 0, 1, 0, 0, 0])
                sage: x.quadratic_form()
                1
                sage: x.is_unit()
                True

                sage: O = OctonionAlgebra(ZZ, -1, 1, 2)
                sage: x = O([1, 0, 1, 0, 0, 0, 0, 0])
                sage: x.quadratic_form()
                0
                sage: x.is_unit()
                False
                sage: O([1, 0, -1, 0, 0, 0, 0, 0]).is_unit()
                False
                sage: x = O([1, 0, 0, 0, 1, 0, 0, 0])
                sage: x.quadratic_form()
                -1
                sage: x.is_unit()
                True
                sage: x = O([0, 0, 0, 0, 1, 0, 0, 0])
                sage: x.quadratic_form()
                -2
                sage: x.is_unit()
                False"""
        @overload
        def is_unit(self) -> Any:
            """Octonion_generic.is_unit(self)

            File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 291)

            Return if ``self`` is a unit or not.

            EXAMPLES::

                sage: O = OctonionAlgebra(ZZ)
                sage: x = O([1, 0, 1, 0, 0, 0, 0, 0])
                sage: x.quadratic_form()
                2
                sage: x.is_unit()
                False
                sage: O([1, 0, -1, 0, 0, 0, 0, 0]).is_unit()
                False
                sage: x = O([1, 0, 0, 0, 1, 0, 0, 0])
                sage: x.quadratic_form()
                2
                sage: x.is_unit()
                False
                sage: x = O([0, 0, 0, 0, 1, 0, 0, 0])
                sage: x.quadratic_form()
                1
                sage: x.is_unit()
                True

                sage: O = OctonionAlgebra(ZZ, -1, 1, 2)
                sage: x = O([1, 0, 1, 0, 0, 0, 0, 0])
                sage: x.quadratic_form()
                0
                sage: x.is_unit()
                False
                sage: O([1, 0, -1, 0, 0, 0, 0, 0]).is_unit()
                False
                sage: x = O([1, 0, 0, 0, 1, 0, 0, 0])
                sage: x.quadratic_form()
                -1
                sage: x.is_unit()
                True
                sage: x = O([0, 0, 0, 0, 1, 0, 0, 0])
                sage: x.quadratic_form()
                -2
                sage: x.is_unit()
                False"""
        @overload
        def is_unit(self) -> Any:
            """Octonion_generic.is_unit(self)

            File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 291)

            Return if ``self`` is a unit or not.

            EXAMPLES::

                sage: O = OctonionAlgebra(ZZ)
                sage: x = O([1, 0, 1, 0, 0, 0, 0, 0])
                sage: x.quadratic_form()
                2
                sage: x.is_unit()
                False
                sage: O([1, 0, -1, 0, 0, 0, 0, 0]).is_unit()
                False
                sage: x = O([1, 0, 0, 0, 1, 0, 0, 0])
                sage: x.quadratic_form()
                2
                sage: x.is_unit()
                False
                sage: x = O([0, 0, 0, 0, 1, 0, 0, 0])
                sage: x.quadratic_form()
                1
                sage: x.is_unit()
                True

                sage: O = OctonionAlgebra(ZZ, -1, 1, 2)
                sage: x = O([1, 0, 1, 0, 0, 0, 0, 0])
                sage: x.quadratic_form()
                0
                sage: x.is_unit()
                False
                sage: O([1, 0, -1, 0, 0, 0, 0, 0]).is_unit()
                False
                sage: x = O([1, 0, 0, 0, 1, 0, 0, 0])
                sage: x.quadratic_form()
                -1
                sage: x.is_unit()
                True
                sage: x = O([0, 0, 0, 0, 1, 0, 0, 0])
                sage: x.quadratic_form()
                -2
                sage: x.is_unit()
                False"""
        @overload
        def is_unit(self) -> Any:
            """Octonion_generic.is_unit(self)

            File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 291)

            Return if ``self`` is a unit or not.

            EXAMPLES::

                sage: O = OctonionAlgebra(ZZ)
                sage: x = O([1, 0, 1, 0, 0, 0, 0, 0])
                sage: x.quadratic_form()
                2
                sage: x.is_unit()
                False
                sage: O([1, 0, -1, 0, 0, 0, 0, 0]).is_unit()
                False
                sage: x = O([1, 0, 0, 0, 1, 0, 0, 0])
                sage: x.quadratic_form()
                2
                sage: x.is_unit()
                False
                sage: x = O([0, 0, 0, 0, 1, 0, 0, 0])
                sage: x.quadratic_form()
                1
                sage: x.is_unit()
                True

                sage: O = OctonionAlgebra(ZZ, -1, 1, 2)
                sage: x = O([1, 0, 1, 0, 0, 0, 0, 0])
                sage: x.quadratic_form()
                0
                sage: x.is_unit()
                False
                sage: O([1, 0, -1, 0, 0, 0, 0, 0]).is_unit()
                False
                sage: x = O([1, 0, 0, 0, 1, 0, 0, 0])
                sage: x.quadratic_form()
                -1
                sage: x.is_unit()
                True
                sage: x = O([0, 0, 0, 0, 1, 0, 0, 0])
                sage: x.quadratic_form()
                -2
                sage: x.is_unit()
                False"""
        @overload
        def is_unit(self) -> Any:
            """Octonion_generic.is_unit(self)

            File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 291)

            Return if ``self`` is a unit or not.

            EXAMPLES::

                sage: O = OctonionAlgebra(ZZ)
                sage: x = O([1, 0, 1, 0, 0, 0, 0, 0])
                sage: x.quadratic_form()
                2
                sage: x.is_unit()
                False
                sage: O([1, 0, -1, 0, 0, 0, 0, 0]).is_unit()
                False
                sage: x = O([1, 0, 0, 0, 1, 0, 0, 0])
                sage: x.quadratic_form()
                2
                sage: x.is_unit()
                False
                sage: x = O([0, 0, 0, 0, 1, 0, 0, 0])
                sage: x.quadratic_form()
                1
                sage: x.is_unit()
                True

                sage: O = OctonionAlgebra(ZZ, -1, 1, 2)
                sage: x = O([1, 0, 1, 0, 0, 0, 0, 0])
                sage: x.quadratic_form()
                0
                sage: x.is_unit()
                False
                sage: O([1, 0, -1, 0, 0, 0, 0, 0]).is_unit()
                False
                sage: x = O([1, 0, 0, 0, 1, 0, 0, 0])
                sage: x.quadratic_form()
                -1
                sage: x.is_unit()
                True
                sage: x = O([0, 0, 0, 0, 1, 0, 0, 0])
                sage: x.quadratic_form()
                -2
                sage: x.is_unit()
                False"""
        @overload
        def is_unit(self) -> Any:
            """Octonion_generic.is_unit(self)

            File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 291)

            Return if ``self`` is a unit or not.

            EXAMPLES::

                sage: O = OctonionAlgebra(ZZ)
                sage: x = O([1, 0, 1, 0, 0, 0, 0, 0])
                sage: x.quadratic_form()
                2
                sage: x.is_unit()
                False
                sage: O([1, 0, -1, 0, 0, 0, 0, 0]).is_unit()
                False
                sage: x = O([1, 0, 0, 0, 1, 0, 0, 0])
                sage: x.quadratic_form()
                2
                sage: x.is_unit()
                False
                sage: x = O([0, 0, 0, 0, 1, 0, 0, 0])
                sage: x.quadratic_form()
                1
                sage: x.is_unit()
                True

                sage: O = OctonionAlgebra(ZZ, -1, 1, 2)
                sage: x = O([1, 0, 1, 0, 0, 0, 0, 0])
                sage: x.quadratic_form()
                0
                sage: x.is_unit()
                False
                sage: O([1, 0, -1, 0, 0, 0, 0, 0]).is_unit()
                False
                sage: x = O([1, 0, 0, 0, 1, 0, 0, 0])
                sage: x.quadratic_form()
                -1
                sage: x.is_unit()
                True
                sage: x = O([0, 0, 0, 0, 1, 0, 0, 0])
                sage: x.quadratic_form()
                -2
                sage: x.is_unit()
                False"""
        @overload
        def is_unit(self) -> Any:
            """Octonion_generic.is_unit(self)

            File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 291)

            Return if ``self`` is a unit or not.

            EXAMPLES::

                sage: O = OctonionAlgebra(ZZ)
                sage: x = O([1, 0, 1, 0, 0, 0, 0, 0])
                sage: x.quadratic_form()
                2
                sage: x.is_unit()
                False
                sage: O([1, 0, -1, 0, 0, 0, 0, 0]).is_unit()
                False
                sage: x = O([1, 0, 0, 0, 1, 0, 0, 0])
                sage: x.quadratic_form()
                2
                sage: x.is_unit()
                False
                sage: x = O([0, 0, 0, 0, 1, 0, 0, 0])
                sage: x.quadratic_form()
                1
                sage: x.is_unit()
                True

                sage: O = OctonionAlgebra(ZZ, -1, 1, 2)
                sage: x = O([1, 0, 1, 0, 0, 0, 0, 0])
                sage: x.quadratic_form()
                0
                sage: x.is_unit()
                False
                sage: O([1, 0, -1, 0, 0, 0, 0, 0]).is_unit()
                False
                sage: x = O([1, 0, 0, 0, 1, 0, 0, 0])
                sage: x.quadratic_form()
                -1
                sage: x.is_unit()
                True
                sage: x = O([0, 0, 0, 0, 1, 0, 0, 0])
                sage: x.quadratic_form()
                -2
                sage: x.is_unit()
                False"""
        @overload
        def is_unit(self) -> Any:
            """Octonion_generic.is_unit(self)

            File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 291)

            Return if ``self`` is a unit or not.

            EXAMPLES::

                sage: O = OctonionAlgebra(ZZ)
                sage: x = O([1, 0, 1, 0, 0, 0, 0, 0])
                sage: x.quadratic_form()
                2
                sage: x.is_unit()
                False
                sage: O([1, 0, -1, 0, 0, 0, 0, 0]).is_unit()
                False
                sage: x = O([1, 0, 0, 0, 1, 0, 0, 0])
                sage: x.quadratic_form()
                2
                sage: x.is_unit()
                False
                sage: x = O([0, 0, 0, 0, 1, 0, 0, 0])
                sage: x.quadratic_form()
                1
                sage: x.is_unit()
                True

                sage: O = OctonionAlgebra(ZZ, -1, 1, 2)
                sage: x = O([1, 0, 1, 0, 0, 0, 0, 0])
                sage: x.quadratic_form()
                0
                sage: x.is_unit()
                False
                sage: O([1, 0, -1, 0, 0, 0, 0, 0]).is_unit()
                False
                sage: x = O([1, 0, 0, 0, 1, 0, 0, 0])
                sage: x.quadratic_form()
                -1
                sage: x.is_unit()
                True
                sage: x = O([0, 0, 0, 0, 1, 0, 0, 0])
                sage: x.quadratic_form()
                -2
                sage: x.is_unit()
                False"""
        @overload
        def is_unit(self) -> Any:
            """Octonion_generic.is_unit(self)

            File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 291)

            Return if ``self`` is a unit or not.

            EXAMPLES::

                sage: O = OctonionAlgebra(ZZ)
                sage: x = O([1, 0, 1, 0, 0, 0, 0, 0])
                sage: x.quadratic_form()
                2
                sage: x.is_unit()
                False
                sage: O([1, 0, -1, 0, 0, 0, 0, 0]).is_unit()
                False
                sage: x = O([1, 0, 0, 0, 1, 0, 0, 0])
                sage: x.quadratic_form()
                2
                sage: x.is_unit()
                False
                sage: x = O([0, 0, 0, 0, 1, 0, 0, 0])
                sage: x.quadratic_form()
                1
                sage: x.is_unit()
                True

                sage: O = OctonionAlgebra(ZZ, -1, 1, 2)
                sage: x = O([1, 0, 1, 0, 0, 0, 0, 0])
                sage: x.quadratic_form()
                0
                sage: x.is_unit()
                False
                sage: O([1, 0, -1, 0, 0, 0, 0, 0]).is_unit()
                False
                sage: x = O([1, 0, 0, 0, 1, 0, 0, 0])
                sage: x.quadratic_form()
                -1
                sage: x.is_unit()
                True
                sage: x = O([0, 0, 0, 0, 1, 0, 0, 0])
                sage: x.quadratic_form()
                -2
                sage: x.is_unit()
                False"""
        @overload
        def monomial_coefficients(self, copy=...) -> Any:
            """Octonion_generic.monomial_coefficients(self, copy=False)

            File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 513)

            Return ``self`` as a ``dict`` with keys being indices
            for the basis and the values being the corresponding
            nonzero coefficients.

            INPUT:

            - ``copy`` -- ignored

            EXAMPLES::

                sage: O = OctonionAlgebra(QQ)
                sage: x = O([2/7, 0, 0, 0, 2/3, 0, -5, 0])
                sage: x.monomial_coefficients()
                {0: 2/7, 4: 2/3, 6: -5}"""
        @overload
        def monomial_coefficients(self) -> Any:
            """Octonion_generic.monomial_coefficients(self, copy=False)

            File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 513)

            Return ``self`` as a ``dict`` with keys being indices
            for the basis and the values being the corresponding
            nonzero coefficients.

            INPUT:

            - ``copy`` -- ignored

            EXAMPLES::

                sage: O = OctonionAlgebra(QQ)
                sage: x = O([2/7, 0, 0, 0, 2/3, 0, -5, 0])
                sage: x.monomial_coefficients()
                {0: 2/7, 4: 2/3, 6: -5}"""
        def norm(self) -> Any:
            """Octonion_generic.norm(self)

            File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 399)

            Return the norm of ``self``.

            The norm of an octonion `x` is `\\lVert x \\rVert = \\sqrt{x x^*}`,
            where `x^*` is the :meth:`conjugate` of `x`.

            .. SEEALSO::

                This is the square root of :meth:`quadratic_form()`.

            .. WARNING::

                If any of the parameters `a, b, c \\not> 0`, then this is not
                an actual norm.

            EXAMPLES::

                sage: O = OctonionAlgebra(QQ, 1, 3, 7)
                sage: elt = sum(i * b for i, b in enumerate(O.basis(), start=2))
                sage: elt.norm()                                                            # needs sage.symbolic
                2*sqrt(-61)
                sage: elt = sum(O.basis())
                sage: elt.norm()
                0"""
        @overload
        def quadratic_form(self) -> Any:
            """Octonion_generic.quadratic_form(self)

            File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 376)

            Return the quadratic form of ``self``.

            The octonion algebra has a distinguished quadratic form given
            by `N(x) = x x^*`, where `x^*` is the :meth:`conjugate` of `x`.

            EXAMPLES::

                sage: O = OctonionAlgebra(QQ, 1, 3, 7)
                sage: elt = sum(O.basis())
                sage: elt.quadratic_form()
                0
                sage: elt * elt.conjugate()
                0"""
        @overload
        def quadratic_form(self) -> Any:
            """Octonion_generic.quadratic_form(self)

            File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 376)

            Return the quadratic form of ``self``.

            The octonion algebra has a distinguished quadratic form given
            by `N(x) = x x^*`, where `x^*` is the :meth:`conjugate` of `x`.

            EXAMPLES::

                sage: O = OctonionAlgebra(QQ, 1, 3, 7)
                sage: elt = sum(O.basis())
                sage: elt.quadratic_form()
                0
                sage: elt * elt.conjugate()
                0"""
        @overload
        def real_part(self) -> Any:
            """Octonion_generic.real_part(self)

            File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 450)

            Return the real part of ``self``.

            OUTPUT: the real part of ``self`` as an element in the base ring

            EXAMPLES::

                sage: O = OctonionAlgebra(QQ)
                sage: elt = sum(i * b for i, b in enumerate(O.basis(), start=2)); elt
                2 + 3*i + 4*j + 5*k + 6*l + 7*li + 8*lj + 9*lk
                sage: r = elt.real_part(); r
                2
                sage: r.parent() is QQ
                True"""
        @overload
        def real_part(self) -> Any:
            """Octonion_generic.real_part(self)

            File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 450)

            Return the real part of ``self``.

            OUTPUT: the real part of ``self`` as an element in the base ring

            EXAMPLES::

                sage: O = OctonionAlgebra(QQ)
                sage: elt = sum(i * b for i, b in enumerate(O.basis(), start=2)); elt
                2 + 3*i + 4*j + 5*k + 6*l + 7*li + 8*lj + 9*lk
                sage: r = elt.real_part(); r
                2
                sage: r.parent() is QQ
                True"""
        def vector(self) -> Any:
            """Octonion_generic._vector_(self, new_base_ring=None)

            File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 495)

            Return ``self`` as a vector in `R^8`, where `R` is the base
            ring of ``self``.

            EXAMPLES::

                sage: O = OctonionAlgebra(QQ)
                sage: elt = sum(i * b for i, b in enumerate(O.basis(), start=2))
                sage: elt.vector()
                (2, 3, 4, 5, 6, 7, 8, 9)"""
        def __bool__(self) -> bool:
            """True if self else False"""
        def __hash__(self) -> Any:
            """Octonion_generic.__hash__(self)

            File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 138)

            Return a hash of ``self``.

            EXAMPLES::

                sage: O = OctonionAlgebra(QQ, 1, 3, 7)
                sage: elt = sum(i * b for i, b in enumerate(O.basis(), start=2))
                sage: hash(elt) == hash(elt.vector())
                True"""
        def __invert__(self) -> Any:
            """Octonion_generic.__invert__(self)

            File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 337)

            Return the (multiplicative) inverse of ``self``.

            EXAMPLES::

                sage: O137 = OctonionAlgebra(QQ, 1, 3, 7)
                sage: elt = sum(O137.basis())
                sage: elt.quadratic_form()
                0
                sage: ~elt
                Traceback (most recent call last):
                ...
                ZeroDivisionError: rational division by zero
                sage: ~O137.zero()
                Traceback (most recent call last):
                ...
                ZeroDivisionError"""
        def __neg__(self) -> Any:
            """Octonion_generic.__neg__(self)

            File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 179)

            Return the negative of ``self``.

            EXAMPLES::

                sage: O = OctonionAlgebra(QQ, 1, 3, 7)
                sage: x = sum(i * b for i, b in enumerate(O.basis(), start=2))
                sage: -x
                -2 - 3*i - 4*j - 5*k - 6*l - 7*li - 8*lj - 9*lk
                sage: y = sum(O.basis())
                sage: -y
                -1 - i - j - k - l - li - lj - lk"""
        @overload
        def __reduce__(self) -> Any:
            """Octonion_generic.__reduce__(self)

            File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 105)

            For pickling.

            EXAMPLES::

                sage: O = OctonionAlgebra(QQ, 1, 3, 7)
                sage: x = sum(i * b for i, b in enumerate(O.basis(), start=2))
                sage: x.__reduce__()
                (<class 'sage.algebras.octonion_algebra.Octonion_generic'>,
                 (Octonion algebra over Rational Field with parameters (1, 3, 7),
                  (2, 3, 4, 5, 6, 7, 8, 9)))"""
        @overload
        def __reduce__(self) -> Any:
            """Octonion_generic.__reduce__(self)

            File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 105)

            For pickling.

            EXAMPLES::

                sage: O = OctonionAlgebra(QQ, 1, 3, 7)
                sage: x = sum(i * b for i, b in enumerate(O.basis(), start=2))
                sage: x.__reduce__()
                (<class 'sage.algebras.octonion_algebra.Octonion_generic'>,
                 (Octonion algebra over Rational Field with parameters (1, 3, 7),
                  (2, 3, 4, 5, 6, 7, 8, 9)))"""
    def __init__(self, R, a, b, c, names) -> Any:
        """OctonionAlgebra.__init__(self, R, a, b, c, names)

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 743)

        Initialize ``self``.

        EXAMPLES::

            sage: O = OctonionAlgebra(QQ)
            sage: TestSuite(O).run()                                                    # needs sage.symbolic

            sage: O = OctonionAlgebra(QQ, 1, 3, 7)
            sage: TestSuite(O).run()

            sage: O = OctonionAlgebra(GF(3), 1, 2, 2)
            sage: TestSuite(O).run()

            sage: O = OctonionAlgebra(Zmod(6), -1, 2, 3)
            sage: TestSuite(O).run()

            sage: R.<a, b, c> = QQ[]
            sage: O = OctonionAlgebra(R, a, b, c)
            sage: TestSuite(O).run()"""
    @overload
    def basis(self) -> Any:
        """OctonionAlgebra.basis(self)

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 968)

        Return the basis of ``self``.

        EXAMPLES::

            sage: O = OctonionAlgebra(ZZ)
            sage: O.basis()
            Family (1, i, j, k, l, li, lj, lk)"""
    @overload
    def basis(self) -> Any:
        """OctonionAlgebra.basis(self)

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 968)

        Return the basis of ``self``.

        EXAMPLES::

            sage: O = OctonionAlgebra(ZZ)
            sage: O.basis()
            Family (1, i, j, k, l, li, lj, lk)"""
    @overload
    def gens(self) -> tuple:
        """OctonionAlgebra.gens(self) -> tuple

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 954)

        Return the generators of ``self``.

        EXAMPLES::

            sage: O = OctonionAlgebra(ZZ)
            sage: O.gens()
            (i, j, k, l)"""
    @overload
    def gens(self) -> Any:
        """OctonionAlgebra.gens(self) -> tuple

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 954)

        Return the generators of ``self``.

        EXAMPLES::

            sage: O = OctonionAlgebra(ZZ)
            sage: O.gens()
            (i, j, k, l)"""
    @overload
    def one_basis(self) -> Any:
        """OctonionAlgebra.one_basis(self)

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 941)

        Return the index for the basis element of `1`.

        EXAMPLES::

            sage: O = OctonionAlgebra(ZZ)
            sage: O.one_basis()
            0"""
    @overload
    def one_basis(self) -> Any:
        """OctonionAlgebra.one_basis(self)

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 941)

        Return the index for the basis element of `1`.

        EXAMPLES::

            sage: O = OctonionAlgebra(ZZ)
            sage: O.one_basis()
            0"""
    @overload
    def some_elements(self) -> Any:
        """OctonionAlgebra.some_elements(self)

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 913)

        Return some elements of ``self``.

        EXAMPLES::

            sage: O = OctonionAlgebra(ZZ)
            sage: O.some_elements()
            [2, 1, i, j, k, l, li, lj, lk,
             2 + 3*i + 4*j + 5*k + 6*l + 7*li + 8*lj + 9*lk,
             -2*j + 3*k - li - lj,
             8 - 7*i + 2*j + 13*k - 18*l + 45*li - 40*lj + 5*lk]
            sage: O = OctonionAlgebra(Zmod(6))
            sage: O.some_elements()
            [2, 1, i, j, k, l, li, lj, lk,
             2 + 3*i + 4*j + 5*k + li + 2*lj + 3*lk,
             4*j + 3*k + 5*li + 5*lj,
             2 + 5*i + 2*j + k + 3*li + 2*lj + 5*lk]"""
    @overload
    def some_elements(self) -> Any:
        """OctonionAlgebra.some_elements(self)

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 913)

        Return some elements of ``self``.

        EXAMPLES::

            sage: O = OctonionAlgebra(ZZ)
            sage: O.some_elements()
            [2, 1, i, j, k, l, li, lj, lk,
             2 + 3*i + 4*j + 5*k + 6*l + 7*li + 8*lj + 9*lk,
             -2*j + 3*k - li - lj,
             8 - 7*i + 2*j + 13*k - 18*l + 45*li - 40*lj + 5*lk]
            sage: O = OctonionAlgebra(Zmod(6))
            sage: O.some_elements()
            [2, 1, i, j, k, l, li, lj, lk,
             2 + 3*i + 4*j + 5*k + li + 2*lj + 3*lk,
             4*j + 3*k + 5*li + 5*lj,
             2 + 5*i + 2*j + k + 3*li + 2*lj + 5*lk]"""
    @overload
    def some_elements(self) -> Any:
        """OctonionAlgebra.some_elements(self)

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 913)

        Return some elements of ``self``.

        EXAMPLES::

            sage: O = OctonionAlgebra(ZZ)
            sage: O.some_elements()
            [2, 1, i, j, k, l, li, lj, lk,
             2 + 3*i + 4*j + 5*k + 6*l + 7*li + 8*lj + 9*lk,
             -2*j + 3*k - li - lj,
             8 - 7*i + 2*j + 13*k - 18*l + 45*li - 40*lj + 5*lk]
            sage: O = OctonionAlgebra(Zmod(6))
            sage: O.some_elements()
            [2, 1, i, j, k, l, li, lj, lk,
             2 + 3*i + 4*j + 5*k + li + 2*lj + 3*lk,
             4*j + 3*k + 5*li + 5*lj,
             2 + 5*i + 2*j + k + 3*li + 2*lj + 5*lk]"""
    @staticmethod
    def __classcall_private__(cls, R, a=..., b=..., c=..., names=...) -> Any:
        """OctonionAlgebra.__classcall_private__(cls, R, a=-1, b=-1, c=-1, names=('i', 'j', 'k', 'l'))

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 709)

        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: O1 = OctonionAlgebra(QQ, 1)
            sage: O2 = OctonionAlgebra(QQ, QQ.one(), -1, QQ['x'](-1))
            sage: O3 = algebras.Octonion(QQ, QQ.one(), c=int(-1), names='ijkl')
            sage: O1 is O2
            True
            sage: O1 is O3
            True

            sage: OctonionAlgebra(ExteriorAlgebra(QQ, 3))
            Traceback (most recent call last):
            ...
            ValueError: the base ring must be a commutative ring
            sage: OctonionAlgebra(GF(2)['x','y','z'])
            Traceback (most recent call last):
            ...
            ValueError: the characteristic must not be 2"""

class Octonion_generic(sage.structure.element.AlgebraElement):
    """Octonion_generic(parent, v)

    File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 32)

    An octonion with generic parameters."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, v) -> Any:
        """File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 36)

                Initialize ``self``.

                EXAMPLES::

                    sage: O = OctonionAlgebra(QQ, 1, 3, 7)
                    sage: elt = sum(i * b for i, b in enumerate(O.basis(), start=2))
                    sage: TestSuite(elt).run()
                    sage: elt = sum(O.basis())
                    sage: TestSuite(elt).run()
                    sage: TestSuite(O.zero()).run()

                    sage: O = OctonionAlgebra(Zmod(8), 1, 3, 7)
                    sage: elt = sum(i * b for i, b in enumerate(O.basis(), start=2))
                    sage: TestSuite(elt).run()
                    sage: elt = sum(O.basis())
                    sage: TestSuite(elt).run()
                    sage: TestSuite(O.zero()).run()
        """
    def abs(self) -> Any:
        """Octonion_generic.abs(self)

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 427)

        Return the absolute value of ``self``.

        This is equal to the :meth:`norm`.

        .. WARNING::

            If any of the parameters `a, b, c \\not> 0`, then this does
            not define a metric.

        EXAMPLES::

            sage: O = OctonionAlgebra(QQ, 1, 3, 7)
            sage: elt = sum(i * b for i, b in enumerate(O.basis(), start=2))
            sage: elt.abs()                                                             # needs sage.symbolic
            2*sqrt(-61)
            sage: elt = sum(O.basis())
            sage: elt.abs()
            0"""
    @overload
    def conjugate(self) -> Octonion_generic:
        """Octonion_generic.conjugate(self) -> Octonion_generic

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 360)

        Return the conjugate of ``self``.

        EXAMPLES::

            sage: O = OctonionAlgebra(QQ)
            sage: elt = sum(O.basis()); elt
            1 + i + j + k + l + li + lj + lk
            sage: elt.conjugate()
            1 - i - j - k - l - li - lj - lk"""
    @overload
    def conjugate(self) -> Any:
        """Octonion_generic.conjugate(self) -> Octonion_generic

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 360)

        Return the conjugate of ``self``.

        EXAMPLES::

            sage: O = OctonionAlgebra(QQ)
            sage: elt = sum(O.basis()); elt
            1 + i + j + k + l + li + lj + lk
            sage: elt.conjugate()
            1 - i - j - k - l - li - lj - lk"""
    def dict(self, *args, **kwargs):
        """Octonion_generic.monomial_coefficients(self, copy=False)

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 513)

        Return ``self`` as a ``dict`` with keys being indices
        for the basis and the values being the corresponding
        nonzero coefficients.

        INPUT:

        - ``copy`` -- ignored

        EXAMPLES::

            sage: O = OctonionAlgebra(QQ)
            sage: x = O([2/7, 0, 0, 0, 2/3, 0, -5, 0])
            sage: x.monomial_coefficients()
            {0: 2/7, 4: 2/3, 6: -5}"""
    @overload
    def imag_part(self) -> Octonion_generic:
        """Octonion_generic.imag_part(self) -> Octonion_generic

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 468)

        Return the imginary part of ``self``.

        OUTPUT: the imaginary part of ``self`` as an element in the octonion algebra

        EXAMPLES::

            sage: O = OctonionAlgebra(QQ)
            sage: elt = sum(i * b for i, b in enumerate(O.basis(), start=2)); elt
            2 + 3*i + 4*j + 5*k + 6*l + 7*li + 8*lj + 9*lk
            sage: elt.imag_part()
            3*i + 4*j + 5*k + 6*l + 7*li + 8*lj + 9*lk

        TESTS::

            sage: O = OctonionAlgebra(QQ)
            sage: elt = sum(i * b for i, b in enumerate(O.basis(), start=2))
            sage: elt.imag_part()
            3*i + 4*j + 5*k + 6*l + 7*li + 8*lj + 9*lk
            sage: elt
            2 + 3*i + 4*j + 5*k + 6*l + 7*li + 8*lj + 9*lk"""
    @overload
    def imag_part(self) -> Any:
        """Octonion_generic.imag_part(self) -> Octonion_generic

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 468)

        Return the imginary part of ``self``.

        OUTPUT: the imaginary part of ``self`` as an element in the octonion algebra

        EXAMPLES::

            sage: O = OctonionAlgebra(QQ)
            sage: elt = sum(i * b for i, b in enumerate(O.basis(), start=2)); elt
            2 + 3*i + 4*j + 5*k + 6*l + 7*li + 8*lj + 9*lk
            sage: elt.imag_part()
            3*i + 4*j + 5*k + 6*l + 7*li + 8*lj + 9*lk

        TESTS::

            sage: O = OctonionAlgebra(QQ)
            sage: elt = sum(i * b for i, b in enumerate(O.basis(), start=2))
            sage: elt.imag_part()
            3*i + 4*j + 5*k + 6*l + 7*li + 8*lj + 9*lk
            sage: elt
            2 + 3*i + 4*j + 5*k + 6*l + 7*li + 8*lj + 9*lk"""
    @overload
    def imag_part(self) -> Any:
        """Octonion_generic.imag_part(self) -> Octonion_generic

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 468)

        Return the imginary part of ``self``.

        OUTPUT: the imaginary part of ``self`` as an element in the octonion algebra

        EXAMPLES::

            sage: O = OctonionAlgebra(QQ)
            sage: elt = sum(i * b for i, b in enumerate(O.basis(), start=2)); elt
            2 + 3*i + 4*j + 5*k + 6*l + 7*li + 8*lj + 9*lk
            sage: elt.imag_part()
            3*i + 4*j + 5*k + 6*l + 7*li + 8*lj + 9*lk

        TESTS::

            sage: O = OctonionAlgebra(QQ)
            sage: elt = sum(i * b for i, b in enumerate(O.basis(), start=2))
            sage: elt.imag_part()
            3*i + 4*j + 5*k + 6*l + 7*li + 8*lj + 9*lk
            sage: elt
            2 + 3*i + 4*j + 5*k + 6*l + 7*li + 8*lj + 9*lk"""
    @overload
    def is_unit(self) -> Any:
        """Octonion_generic.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 291)

        Return if ``self`` is a unit or not.

        EXAMPLES::

            sage: O = OctonionAlgebra(ZZ)
            sage: x = O([1, 0, 1, 0, 0, 0, 0, 0])
            sage: x.quadratic_form()
            2
            sage: x.is_unit()
            False
            sage: O([1, 0, -1, 0, 0, 0, 0, 0]).is_unit()
            False
            sage: x = O([1, 0, 0, 0, 1, 0, 0, 0])
            sage: x.quadratic_form()
            2
            sage: x.is_unit()
            False
            sage: x = O([0, 0, 0, 0, 1, 0, 0, 0])
            sage: x.quadratic_form()
            1
            sage: x.is_unit()
            True

            sage: O = OctonionAlgebra(ZZ, -1, 1, 2)
            sage: x = O([1, 0, 1, 0, 0, 0, 0, 0])
            sage: x.quadratic_form()
            0
            sage: x.is_unit()
            False
            sage: O([1, 0, -1, 0, 0, 0, 0, 0]).is_unit()
            False
            sage: x = O([1, 0, 0, 0, 1, 0, 0, 0])
            sage: x.quadratic_form()
            -1
            sage: x.is_unit()
            True
            sage: x = O([0, 0, 0, 0, 1, 0, 0, 0])
            sage: x.quadratic_form()
            -2
            sage: x.is_unit()
            False"""
    @overload
    def is_unit(self) -> Any:
        """Octonion_generic.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 291)

        Return if ``self`` is a unit or not.

        EXAMPLES::

            sage: O = OctonionAlgebra(ZZ)
            sage: x = O([1, 0, 1, 0, 0, 0, 0, 0])
            sage: x.quadratic_form()
            2
            sage: x.is_unit()
            False
            sage: O([1, 0, -1, 0, 0, 0, 0, 0]).is_unit()
            False
            sage: x = O([1, 0, 0, 0, 1, 0, 0, 0])
            sage: x.quadratic_form()
            2
            sage: x.is_unit()
            False
            sage: x = O([0, 0, 0, 0, 1, 0, 0, 0])
            sage: x.quadratic_form()
            1
            sage: x.is_unit()
            True

            sage: O = OctonionAlgebra(ZZ, -1, 1, 2)
            sage: x = O([1, 0, 1, 0, 0, 0, 0, 0])
            sage: x.quadratic_form()
            0
            sage: x.is_unit()
            False
            sage: O([1, 0, -1, 0, 0, 0, 0, 0]).is_unit()
            False
            sage: x = O([1, 0, 0, 0, 1, 0, 0, 0])
            sage: x.quadratic_form()
            -1
            sage: x.is_unit()
            True
            sage: x = O([0, 0, 0, 0, 1, 0, 0, 0])
            sage: x.quadratic_form()
            -2
            sage: x.is_unit()
            False"""
    @overload
    def is_unit(self) -> Any:
        """Octonion_generic.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 291)

        Return if ``self`` is a unit or not.

        EXAMPLES::

            sage: O = OctonionAlgebra(ZZ)
            sage: x = O([1, 0, 1, 0, 0, 0, 0, 0])
            sage: x.quadratic_form()
            2
            sage: x.is_unit()
            False
            sage: O([1, 0, -1, 0, 0, 0, 0, 0]).is_unit()
            False
            sage: x = O([1, 0, 0, 0, 1, 0, 0, 0])
            sage: x.quadratic_form()
            2
            sage: x.is_unit()
            False
            sage: x = O([0, 0, 0, 0, 1, 0, 0, 0])
            sage: x.quadratic_form()
            1
            sage: x.is_unit()
            True

            sage: O = OctonionAlgebra(ZZ, -1, 1, 2)
            sage: x = O([1, 0, 1, 0, 0, 0, 0, 0])
            sage: x.quadratic_form()
            0
            sage: x.is_unit()
            False
            sage: O([1, 0, -1, 0, 0, 0, 0, 0]).is_unit()
            False
            sage: x = O([1, 0, 0, 0, 1, 0, 0, 0])
            sage: x.quadratic_form()
            -1
            sage: x.is_unit()
            True
            sage: x = O([0, 0, 0, 0, 1, 0, 0, 0])
            sage: x.quadratic_form()
            -2
            sage: x.is_unit()
            False"""
    @overload
    def is_unit(self) -> Any:
        """Octonion_generic.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 291)

        Return if ``self`` is a unit or not.

        EXAMPLES::

            sage: O = OctonionAlgebra(ZZ)
            sage: x = O([1, 0, 1, 0, 0, 0, 0, 0])
            sage: x.quadratic_form()
            2
            sage: x.is_unit()
            False
            sage: O([1, 0, -1, 0, 0, 0, 0, 0]).is_unit()
            False
            sage: x = O([1, 0, 0, 0, 1, 0, 0, 0])
            sage: x.quadratic_form()
            2
            sage: x.is_unit()
            False
            sage: x = O([0, 0, 0, 0, 1, 0, 0, 0])
            sage: x.quadratic_form()
            1
            sage: x.is_unit()
            True

            sage: O = OctonionAlgebra(ZZ, -1, 1, 2)
            sage: x = O([1, 0, 1, 0, 0, 0, 0, 0])
            sage: x.quadratic_form()
            0
            sage: x.is_unit()
            False
            sage: O([1, 0, -1, 0, 0, 0, 0, 0]).is_unit()
            False
            sage: x = O([1, 0, 0, 0, 1, 0, 0, 0])
            sage: x.quadratic_form()
            -1
            sage: x.is_unit()
            True
            sage: x = O([0, 0, 0, 0, 1, 0, 0, 0])
            sage: x.quadratic_form()
            -2
            sage: x.is_unit()
            False"""
    @overload
    def is_unit(self) -> Any:
        """Octonion_generic.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 291)

        Return if ``self`` is a unit or not.

        EXAMPLES::

            sage: O = OctonionAlgebra(ZZ)
            sage: x = O([1, 0, 1, 0, 0, 0, 0, 0])
            sage: x.quadratic_form()
            2
            sage: x.is_unit()
            False
            sage: O([1, 0, -1, 0, 0, 0, 0, 0]).is_unit()
            False
            sage: x = O([1, 0, 0, 0, 1, 0, 0, 0])
            sage: x.quadratic_form()
            2
            sage: x.is_unit()
            False
            sage: x = O([0, 0, 0, 0, 1, 0, 0, 0])
            sage: x.quadratic_form()
            1
            sage: x.is_unit()
            True

            sage: O = OctonionAlgebra(ZZ, -1, 1, 2)
            sage: x = O([1, 0, 1, 0, 0, 0, 0, 0])
            sage: x.quadratic_form()
            0
            sage: x.is_unit()
            False
            sage: O([1, 0, -1, 0, 0, 0, 0, 0]).is_unit()
            False
            sage: x = O([1, 0, 0, 0, 1, 0, 0, 0])
            sage: x.quadratic_form()
            -1
            sage: x.is_unit()
            True
            sage: x = O([0, 0, 0, 0, 1, 0, 0, 0])
            sage: x.quadratic_form()
            -2
            sage: x.is_unit()
            False"""
    @overload
    def is_unit(self) -> Any:
        """Octonion_generic.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 291)

        Return if ``self`` is a unit or not.

        EXAMPLES::

            sage: O = OctonionAlgebra(ZZ)
            sage: x = O([1, 0, 1, 0, 0, 0, 0, 0])
            sage: x.quadratic_form()
            2
            sage: x.is_unit()
            False
            sage: O([1, 0, -1, 0, 0, 0, 0, 0]).is_unit()
            False
            sage: x = O([1, 0, 0, 0, 1, 0, 0, 0])
            sage: x.quadratic_form()
            2
            sage: x.is_unit()
            False
            sage: x = O([0, 0, 0, 0, 1, 0, 0, 0])
            sage: x.quadratic_form()
            1
            sage: x.is_unit()
            True

            sage: O = OctonionAlgebra(ZZ, -1, 1, 2)
            sage: x = O([1, 0, 1, 0, 0, 0, 0, 0])
            sage: x.quadratic_form()
            0
            sage: x.is_unit()
            False
            sage: O([1, 0, -1, 0, 0, 0, 0, 0]).is_unit()
            False
            sage: x = O([1, 0, 0, 0, 1, 0, 0, 0])
            sage: x.quadratic_form()
            -1
            sage: x.is_unit()
            True
            sage: x = O([0, 0, 0, 0, 1, 0, 0, 0])
            sage: x.quadratic_form()
            -2
            sage: x.is_unit()
            False"""
    @overload
    def is_unit(self) -> Any:
        """Octonion_generic.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 291)

        Return if ``self`` is a unit or not.

        EXAMPLES::

            sage: O = OctonionAlgebra(ZZ)
            sage: x = O([1, 0, 1, 0, 0, 0, 0, 0])
            sage: x.quadratic_form()
            2
            sage: x.is_unit()
            False
            sage: O([1, 0, -1, 0, 0, 0, 0, 0]).is_unit()
            False
            sage: x = O([1, 0, 0, 0, 1, 0, 0, 0])
            sage: x.quadratic_form()
            2
            sage: x.is_unit()
            False
            sage: x = O([0, 0, 0, 0, 1, 0, 0, 0])
            sage: x.quadratic_form()
            1
            sage: x.is_unit()
            True

            sage: O = OctonionAlgebra(ZZ, -1, 1, 2)
            sage: x = O([1, 0, 1, 0, 0, 0, 0, 0])
            sage: x.quadratic_form()
            0
            sage: x.is_unit()
            False
            sage: O([1, 0, -1, 0, 0, 0, 0, 0]).is_unit()
            False
            sage: x = O([1, 0, 0, 0, 1, 0, 0, 0])
            sage: x.quadratic_form()
            -1
            sage: x.is_unit()
            True
            sage: x = O([0, 0, 0, 0, 1, 0, 0, 0])
            sage: x.quadratic_form()
            -2
            sage: x.is_unit()
            False"""
    @overload
    def is_unit(self) -> Any:
        """Octonion_generic.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 291)

        Return if ``self`` is a unit or not.

        EXAMPLES::

            sage: O = OctonionAlgebra(ZZ)
            sage: x = O([1, 0, 1, 0, 0, 0, 0, 0])
            sage: x.quadratic_form()
            2
            sage: x.is_unit()
            False
            sage: O([1, 0, -1, 0, 0, 0, 0, 0]).is_unit()
            False
            sage: x = O([1, 0, 0, 0, 1, 0, 0, 0])
            sage: x.quadratic_form()
            2
            sage: x.is_unit()
            False
            sage: x = O([0, 0, 0, 0, 1, 0, 0, 0])
            sage: x.quadratic_form()
            1
            sage: x.is_unit()
            True

            sage: O = OctonionAlgebra(ZZ, -1, 1, 2)
            sage: x = O([1, 0, 1, 0, 0, 0, 0, 0])
            sage: x.quadratic_form()
            0
            sage: x.is_unit()
            False
            sage: O([1, 0, -1, 0, 0, 0, 0, 0]).is_unit()
            False
            sage: x = O([1, 0, 0, 0, 1, 0, 0, 0])
            sage: x.quadratic_form()
            -1
            sage: x.is_unit()
            True
            sage: x = O([0, 0, 0, 0, 1, 0, 0, 0])
            sage: x.quadratic_form()
            -2
            sage: x.is_unit()
            False"""
    @overload
    def is_unit(self) -> Any:
        """Octonion_generic.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 291)

        Return if ``self`` is a unit or not.

        EXAMPLES::

            sage: O = OctonionAlgebra(ZZ)
            sage: x = O([1, 0, 1, 0, 0, 0, 0, 0])
            sage: x.quadratic_form()
            2
            sage: x.is_unit()
            False
            sage: O([1, 0, -1, 0, 0, 0, 0, 0]).is_unit()
            False
            sage: x = O([1, 0, 0, 0, 1, 0, 0, 0])
            sage: x.quadratic_form()
            2
            sage: x.is_unit()
            False
            sage: x = O([0, 0, 0, 0, 1, 0, 0, 0])
            sage: x.quadratic_form()
            1
            sage: x.is_unit()
            True

            sage: O = OctonionAlgebra(ZZ, -1, 1, 2)
            sage: x = O([1, 0, 1, 0, 0, 0, 0, 0])
            sage: x.quadratic_form()
            0
            sage: x.is_unit()
            False
            sage: O([1, 0, -1, 0, 0, 0, 0, 0]).is_unit()
            False
            sage: x = O([1, 0, 0, 0, 1, 0, 0, 0])
            sage: x.quadratic_form()
            -1
            sage: x.is_unit()
            True
            sage: x = O([0, 0, 0, 0, 1, 0, 0, 0])
            sage: x.quadratic_form()
            -2
            sage: x.is_unit()
            False"""
    @overload
    def monomial_coefficients(self, copy=...) -> Any:
        """Octonion_generic.monomial_coefficients(self, copy=False)

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 513)

        Return ``self`` as a ``dict`` with keys being indices
        for the basis and the values being the corresponding
        nonzero coefficients.

        INPUT:

        - ``copy`` -- ignored

        EXAMPLES::

            sage: O = OctonionAlgebra(QQ)
            sage: x = O([2/7, 0, 0, 0, 2/3, 0, -5, 0])
            sage: x.monomial_coefficients()
            {0: 2/7, 4: 2/3, 6: -5}"""
    @overload
    def monomial_coefficients(self) -> Any:
        """Octonion_generic.monomial_coefficients(self, copy=False)

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 513)

        Return ``self`` as a ``dict`` with keys being indices
        for the basis and the values being the corresponding
        nonzero coefficients.

        INPUT:

        - ``copy`` -- ignored

        EXAMPLES::

            sage: O = OctonionAlgebra(QQ)
            sage: x = O([2/7, 0, 0, 0, 2/3, 0, -5, 0])
            sage: x.monomial_coefficients()
            {0: 2/7, 4: 2/3, 6: -5}"""
    def norm(self) -> Any:
        """Octonion_generic.norm(self)

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 399)

        Return the norm of ``self``.

        The norm of an octonion `x` is `\\lVert x \\rVert = \\sqrt{x x^*}`,
        where `x^*` is the :meth:`conjugate` of `x`.

        .. SEEALSO::

            This is the square root of :meth:`quadratic_form()`.

        .. WARNING::

            If any of the parameters `a, b, c \\not> 0`, then this is not
            an actual norm.

        EXAMPLES::

            sage: O = OctonionAlgebra(QQ, 1, 3, 7)
            sage: elt = sum(i * b for i, b in enumerate(O.basis(), start=2))
            sage: elt.norm()                                                            # needs sage.symbolic
            2*sqrt(-61)
            sage: elt = sum(O.basis())
            sage: elt.norm()
            0"""
    @overload
    def quadratic_form(self) -> Any:
        """Octonion_generic.quadratic_form(self)

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 376)

        Return the quadratic form of ``self``.

        The octonion algebra has a distinguished quadratic form given
        by `N(x) = x x^*`, where `x^*` is the :meth:`conjugate` of `x`.

        EXAMPLES::

            sage: O = OctonionAlgebra(QQ, 1, 3, 7)
            sage: elt = sum(O.basis())
            sage: elt.quadratic_form()
            0
            sage: elt * elt.conjugate()
            0"""
    @overload
    def quadratic_form(self) -> Any:
        """Octonion_generic.quadratic_form(self)

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 376)

        Return the quadratic form of ``self``.

        The octonion algebra has a distinguished quadratic form given
        by `N(x) = x x^*`, where `x^*` is the :meth:`conjugate` of `x`.

        EXAMPLES::

            sage: O = OctonionAlgebra(QQ, 1, 3, 7)
            sage: elt = sum(O.basis())
            sage: elt.quadratic_form()
            0
            sage: elt * elt.conjugate()
            0"""
    @overload
    def real_part(self) -> Any:
        """Octonion_generic.real_part(self)

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 450)

        Return the real part of ``self``.

        OUTPUT: the real part of ``self`` as an element in the base ring

        EXAMPLES::

            sage: O = OctonionAlgebra(QQ)
            sage: elt = sum(i * b for i, b in enumerate(O.basis(), start=2)); elt
            2 + 3*i + 4*j + 5*k + 6*l + 7*li + 8*lj + 9*lk
            sage: r = elt.real_part(); r
            2
            sage: r.parent() is QQ
            True"""
    @overload
    def real_part(self) -> Any:
        """Octonion_generic.real_part(self)

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 450)

        Return the real part of ``self``.

        OUTPUT: the real part of ``self`` as an element in the base ring

        EXAMPLES::

            sage: O = OctonionAlgebra(QQ)
            sage: elt = sum(i * b for i, b in enumerate(O.basis(), start=2)); elt
            2 + 3*i + 4*j + 5*k + 6*l + 7*li + 8*lj + 9*lk
            sage: r = elt.real_part(); r
            2
            sage: r.parent() is QQ
            True"""
    def vector(self) -> Any:
        """Octonion_generic._vector_(self, new_base_ring=None)

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 495)

        Return ``self`` as a vector in `R^8`, where `R` is the base
        ring of ``self``.

        EXAMPLES::

            sage: O = OctonionAlgebra(QQ)
            sage: elt = sum(i * b for i, b in enumerate(O.basis(), start=2))
            sage: elt.vector()
            (2, 3, 4, 5, 6, 7, 8, 9)"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __hash__(self) -> Any:
        """Octonion_generic.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 138)

        Return a hash of ``self``.

        EXAMPLES::

            sage: O = OctonionAlgebra(QQ, 1, 3, 7)
            sage: elt = sum(i * b for i, b in enumerate(O.basis(), start=2))
            sage: hash(elt) == hash(elt.vector())
            True"""
    def __invert__(self) -> Any:
        """Octonion_generic.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 337)

        Return the (multiplicative) inverse of ``self``.

        EXAMPLES::

            sage: O137 = OctonionAlgebra(QQ, 1, 3, 7)
            sage: elt = sum(O137.basis())
            sage: elt.quadratic_form()
            0
            sage: ~elt
            Traceback (most recent call last):
            ...
            ZeroDivisionError: rational division by zero
            sage: ~O137.zero()
            Traceback (most recent call last):
            ...
            ZeroDivisionError"""
    def __neg__(self) -> Any:
        """Octonion_generic.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 179)

        Return the negative of ``self``.

        EXAMPLES::

            sage: O = OctonionAlgebra(QQ, 1, 3, 7)
            sage: x = sum(i * b for i, b in enumerate(O.basis(), start=2))
            sage: -x
            -2 - 3*i - 4*j - 5*k - 6*l - 7*li - 8*lj - 9*lk
            sage: y = sum(O.basis())
            sage: -y
            -1 - i - j - k - l - li - lj - lk"""
    @overload
    def __reduce__(self) -> Any:
        """Octonion_generic.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 105)

        For pickling.

        EXAMPLES::

            sage: O = OctonionAlgebra(QQ, 1, 3, 7)
            sage: x = sum(i * b for i, b in enumerate(O.basis(), start=2))
            sage: x.__reduce__()
            (<class 'sage.algebras.octonion_algebra.Octonion_generic'>,
             (Octonion algebra over Rational Field with parameters (1, 3, 7),
              (2, 3, 4, 5, 6, 7, 8, 9)))"""
    @overload
    def __reduce__(self) -> Any:
        """Octonion_generic.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/algebras/octonion_algebra.pyx (starting at line 105)

        For pickling.

        EXAMPLES::

            sage: O = OctonionAlgebra(QQ, 1, 3, 7)
            sage: x = sum(i * b for i, b in enumerate(O.basis(), start=2))
            sage: x.__reduce__()
            (<class 'sage.algebras.octonion_algebra.Octonion_generic'>,
             (Octonion algebra over Rational Field with parameters (1, 3, 7),
              (2, 3, 4, 5, 6, 7, 8, 9)))"""
