import sage.structure.element
from sage.categories.category import ZZ as ZZ
from sage.matrix.matrix_space import M2Z as M2Z, MatrixSpace as MatrixSpace
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

class ArithmeticSubgroupElement(sage.structure.element.MultiplicativeGroupElement):
    """ArithmeticSubgroupElement(parent, x, check=True)

    File: /build/sagemath/src/sage/src/sage/modular/arithgroup/arithgroup_element.pyx (starting at line 26)

    An element of the group `\\SL_2(\\ZZ)`, i.e. a 2x2 integer matrix of
    determinant 1."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, x, check=...) -> Any:
        '''File: /build/sagemath/src/sage/src/sage/modular/arithgroup/arithgroup_element.pyx (starting at line 34)

                Create an element of an arithmetic subgroup.

                INPUT:

                - ``parent`` -- an arithmetic subgroup

                - ``x`` -- data defining a 2x2 matrix over ZZ
                  which lives in ``parent``

                - ``check`` -- if ``True``, check that parent is an arithmetic
                  subgroup, and that `x` defines a matrix of determinant `1`

                We tend not to create elements of arithmetic subgroups that are not
                SL2Z, in order to avoid coercion issues (that is, the other arithmetic
                subgroups are "facade parents").

                EXAMPLES::

                    sage: G = Gamma0(27)
                    sage: sage.modular.arithgroup.arithgroup_element.ArithmeticSubgroupElement(G, [4,1,27,7])
                    [ 4  1]
                    [27  7]
                    sage: sage.modular.arithgroup.arithgroup_element.ArithmeticSubgroupElement(Integers(3), [4,1,27,7])
                    Traceback (most recent call last):
                    ...
                    TypeError: parent (= Ring of integers modulo 3) must be an arithmetic subgroup
                    sage: sage.modular.arithgroup.arithgroup_element.ArithmeticSubgroupElement(G, [2,0,0,2])
                    Traceback (most recent call last):
                    ...
                    TypeError: matrix must have determinant 1
                    sage: sage.modular.arithgroup.arithgroup_element.ArithmeticSubgroupElement(G, [2,0,0,2], check=False)
                    [2 0]
                    [0 2]
                    sage: x = Gamma0(11)([2,1,11,6])
                    sage: TestSuite(x).run()

                    sage: x = Gamma0(5).0
                    sage: SL2Z(x)
                    [1 1]
                    [0 1]
                    sage: x in SL2Z
                    True
        '''
    @overload
    def a(self) -> Any:
        """ArithmeticSubgroupElement.a(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/arithgroup_element.pyx (starting at line 280)

        Return the upper left entry of ``self``.

        EXAMPLES::

            sage: Gamma0(13)([7,1,13,2]).a()
            7"""
    @overload
    def a(self) -> Any:
        """ArithmeticSubgroupElement.a(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/arithgroup_element.pyx (starting at line 280)

        Return the upper left entry of ``self``.

        EXAMPLES::

            sage: Gamma0(13)([7,1,13,2]).a()
            7"""
    @overload
    def acton(self, z) -> Any:
        """ArithmeticSubgroupElement.acton(self, z)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/arithgroup_element.pyx (starting at line 324)

        Return the result of the action of ``self`` on z as a fractional linear
        transformation.

        EXAMPLES::

            sage: G = Gamma0(15)
            sage: g = G([1, 2, 15, 31])

        An example of g acting on a symbolic variable::

            sage: z = var('z')                                                          # needs sage.symbolic
            sage: g.acton(z)                                                            # needs sage.symbolic
            (z + 2)/(15*z + 31)

        An example involving the Gaussian numbers::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: K.<i> = NumberField(x^2 + 1)
            sage: g.acton(i)
            1/1186*i + 77/1186

        An example with complex numbers::

            sage: C.<i> = ComplexField()
            sage: g.acton(i)
            0.0649241146711636 + 0.000843170320404721*I

        An example with the cusp infinity::

            sage: g.acton(infinity)
            1/15

        An example which maps a finite cusp to infinity::

            sage: g.acton(-31/15)
            +Infinity

        Note that when acting on instances of cusps the return value
        is still a rational number or infinity (Note the presence of
        '+', which does not show up for cusp instances)::

            sage: g.acton(Cusp(-31/15))
            +Infinity

        TESTS:

        We cover the remaining case, i.e., infinity mapped to infinity::

            sage: G([1, 4, 0, 1]).acton(infinity)
            +Infinity"""
    @overload
    def acton(self, z) -> Any:
        """ArithmeticSubgroupElement.acton(self, z)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/arithgroup_element.pyx (starting at line 324)

        Return the result of the action of ``self`` on z as a fractional linear
        transformation.

        EXAMPLES::

            sage: G = Gamma0(15)
            sage: g = G([1, 2, 15, 31])

        An example of g acting on a symbolic variable::

            sage: z = var('z')                                                          # needs sage.symbolic
            sage: g.acton(z)                                                            # needs sage.symbolic
            (z + 2)/(15*z + 31)

        An example involving the Gaussian numbers::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: K.<i> = NumberField(x^2 + 1)
            sage: g.acton(i)
            1/1186*i + 77/1186

        An example with complex numbers::

            sage: C.<i> = ComplexField()
            sage: g.acton(i)
            0.0649241146711636 + 0.000843170320404721*I

        An example with the cusp infinity::

            sage: g.acton(infinity)
            1/15

        An example which maps a finite cusp to infinity::

            sage: g.acton(-31/15)
            +Infinity

        Note that when acting on instances of cusps the return value
        is still a rational number or infinity (Note the presence of
        '+', which does not show up for cusp instances)::

            sage: g.acton(Cusp(-31/15))
            +Infinity

        TESTS:

        We cover the remaining case, i.e., infinity mapped to infinity::

            sage: G([1, 4, 0, 1]).acton(infinity)
            +Infinity"""
    @overload
    def acton(self, i) -> Any:
        """ArithmeticSubgroupElement.acton(self, z)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/arithgroup_element.pyx (starting at line 324)

        Return the result of the action of ``self`` on z as a fractional linear
        transformation.

        EXAMPLES::

            sage: G = Gamma0(15)
            sage: g = G([1, 2, 15, 31])

        An example of g acting on a symbolic variable::

            sage: z = var('z')                                                          # needs sage.symbolic
            sage: g.acton(z)                                                            # needs sage.symbolic
            (z + 2)/(15*z + 31)

        An example involving the Gaussian numbers::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: K.<i> = NumberField(x^2 + 1)
            sage: g.acton(i)
            1/1186*i + 77/1186

        An example with complex numbers::

            sage: C.<i> = ComplexField()
            sage: g.acton(i)
            0.0649241146711636 + 0.000843170320404721*I

        An example with the cusp infinity::

            sage: g.acton(infinity)
            1/15

        An example which maps a finite cusp to infinity::

            sage: g.acton(-31/15)
            +Infinity

        Note that when acting on instances of cusps the return value
        is still a rational number or infinity (Note the presence of
        '+', which does not show up for cusp instances)::

            sage: g.acton(Cusp(-31/15))
            +Infinity

        TESTS:

        We cover the remaining case, i.e., infinity mapped to infinity::

            sage: G([1, 4, 0, 1]).acton(infinity)
            +Infinity"""
    @overload
    def acton(self, i) -> Any:
        """ArithmeticSubgroupElement.acton(self, z)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/arithgroup_element.pyx (starting at line 324)

        Return the result of the action of ``self`` on z as a fractional linear
        transformation.

        EXAMPLES::

            sage: G = Gamma0(15)
            sage: g = G([1, 2, 15, 31])

        An example of g acting on a symbolic variable::

            sage: z = var('z')                                                          # needs sage.symbolic
            sage: g.acton(z)                                                            # needs sage.symbolic
            (z + 2)/(15*z + 31)

        An example involving the Gaussian numbers::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: K.<i> = NumberField(x^2 + 1)
            sage: g.acton(i)
            1/1186*i + 77/1186

        An example with complex numbers::

            sage: C.<i> = ComplexField()
            sage: g.acton(i)
            0.0649241146711636 + 0.000843170320404721*I

        An example with the cusp infinity::

            sage: g.acton(infinity)
            1/15

        An example which maps a finite cusp to infinity::

            sage: g.acton(-31/15)
            +Infinity

        Note that when acting on instances of cusps the return value
        is still a rational number or infinity (Note the presence of
        '+', which does not show up for cusp instances)::

            sage: g.acton(Cusp(-31/15))
            +Infinity

        TESTS:

        We cover the remaining case, i.e., infinity mapped to infinity::

            sage: G([1, 4, 0, 1]).acton(infinity)
            +Infinity"""
    @overload
    def acton(self, infinity) -> Any:
        """ArithmeticSubgroupElement.acton(self, z)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/arithgroup_element.pyx (starting at line 324)

        Return the result of the action of ``self`` on z as a fractional linear
        transformation.

        EXAMPLES::

            sage: G = Gamma0(15)
            sage: g = G([1, 2, 15, 31])

        An example of g acting on a symbolic variable::

            sage: z = var('z')                                                          # needs sage.symbolic
            sage: g.acton(z)                                                            # needs sage.symbolic
            (z + 2)/(15*z + 31)

        An example involving the Gaussian numbers::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: K.<i> = NumberField(x^2 + 1)
            sage: g.acton(i)
            1/1186*i + 77/1186

        An example with complex numbers::

            sage: C.<i> = ComplexField()
            sage: g.acton(i)
            0.0649241146711636 + 0.000843170320404721*I

        An example with the cusp infinity::

            sage: g.acton(infinity)
            1/15

        An example which maps a finite cusp to infinity::

            sage: g.acton(-31/15)
            +Infinity

        Note that when acting on instances of cusps the return value
        is still a rational number or infinity (Note the presence of
        '+', which does not show up for cusp instances)::

            sage: g.acton(Cusp(-31/15))
            +Infinity

        TESTS:

        We cover the remaining case, i.e., infinity mapped to infinity::

            sage: G([1, 4, 0, 1]).acton(infinity)
            +Infinity"""
    @overload
    def acton(self, infinity) -> Any:
        """ArithmeticSubgroupElement.acton(self, z)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/arithgroup_element.pyx (starting at line 324)

        Return the result of the action of ``self`` on z as a fractional linear
        transformation.

        EXAMPLES::

            sage: G = Gamma0(15)
            sage: g = G([1, 2, 15, 31])

        An example of g acting on a symbolic variable::

            sage: z = var('z')                                                          # needs sage.symbolic
            sage: g.acton(z)                                                            # needs sage.symbolic
            (z + 2)/(15*z + 31)

        An example involving the Gaussian numbers::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: K.<i> = NumberField(x^2 + 1)
            sage: g.acton(i)
            1/1186*i + 77/1186

        An example with complex numbers::

            sage: C.<i> = ComplexField()
            sage: g.acton(i)
            0.0649241146711636 + 0.000843170320404721*I

        An example with the cusp infinity::

            sage: g.acton(infinity)
            1/15

        An example which maps a finite cusp to infinity::

            sage: g.acton(-31/15)
            +Infinity

        Note that when acting on instances of cusps the return value
        is still a rational number or infinity (Note the presence of
        '+', which does not show up for cusp instances)::

            sage: g.acton(Cusp(-31/15))
            +Infinity

        TESTS:

        We cover the remaining case, i.e., infinity mapped to infinity::

            sage: G([1, 4, 0, 1]).acton(infinity)
            +Infinity"""
    @overload
    def b(self) -> Any:
        """ArithmeticSubgroupElement.b(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/arithgroup_element.pyx (starting at line 291)

        Return the upper right entry of ``self``.

        EXAMPLES::

            sage: Gamma0(13)([7,1,13,2]).b()
            1"""
    @overload
    def b(self) -> Any:
        """ArithmeticSubgroupElement.b(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/arithgroup_element.pyx (starting at line 291)

        Return the upper right entry of ``self``.

        EXAMPLES::

            sage: Gamma0(13)([7,1,13,2]).b()
            1"""
    @overload
    def c(self) -> Any:
        """ArithmeticSubgroupElement.c(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/arithgroup_element.pyx (starting at line 302)

        Return the lower left entry of ``self``.

        EXAMPLES::

            sage: Gamma0(13)([7,1,13,2]).c()
            13"""
    @overload
    def c(self) -> Any:
        """ArithmeticSubgroupElement.c(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/arithgroup_element.pyx (starting at line 302)

        Return the lower left entry of ``self``.

        EXAMPLES::

            sage: Gamma0(13)([7,1,13,2]).c()
            13"""
    @overload
    def d(self) -> Any:
        """ArithmeticSubgroupElement.d(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/arithgroup_element.pyx (starting at line 313)

        Return the lower right entry of ``self``.

        EXAMPLES::

            sage: Gamma0(13)([7,1,13,2]).d()
            2"""
    @overload
    def d(self) -> Any:
        """ArithmeticSubgroupElement.d(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/arithgroup_element.pyx (starting at line 313)

        Return the lower right entry of ``self``.

        EXAMPLES::

            sage: Gamma0(13)([7,1,13,2]).d()
            2"""
    @overload
    def det(self) -> Any:
        """ArithmeticSubgroupElement.det(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/arithgroup_element.pyx (starting at line 269)

        Return the determinant of ``self``, which is always 1.

        EXAMPLES::

            sage: Gamma1(11)([12,11,-11,-10]).det()
            1"""
    @overload
    def det(self) -> Any:
        """ArithmeticSubgroupElement.det(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/arithgroup_element.pyx (starting at line 269)

        Return the determinant of ``self``, which is always 1.

        EXAMPLES::

            sage: Gamma1(11)([12,11,-11,-10]).det()
            1"""
    @overload
    def determinant(self) -> Any:
        """ArithmeticSubgroupElement.determinant(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/arithgroup_element.pyx (starting at line 258)

        Return the determinant of ``self``, which is always 1.

        EXAMPLES::

            sage: Gamma0(691)([1,0,691,1]).determinant()
            1"""
    @overload
    def determinant(self) -> Any:
        """ArithmeticSubgroupElement.determinant(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/arithgroup_element.pyx (starting at line 258)

        Return the determinant of ``self``, which is always 1.

        EXAMPLES::

            sage: Gamma0(691)([1,0,691,1]).determinant()
            1"""
    @overload
    def matrix(self) -> Any:
        """ArithmeticSubgroupElement.matrix(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/arithgroup_element.pyx (starting at line 241)

        Return the matrix corresponding to ``self``.

        EXAMPLES::

            sage: x = Gamma1(3)([4,5,3,4]) ; x
            [4 5]
            [3 4]
            sage: x.matrix()
            [4 5]
            [3 4]
            sage: type(x.matrix())
            <class 'sage.matrix.matrix_integer_dense.Matrix_integer_dense'>"""
    @overload
    def matrix(self) -> Any:
        """ArithmeticSubgroupElement.matrix(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/arithgroup_element.pyx (starting at line 241)

        Return the matrix corresponding to ``self``.

        EXAMPLES::

            sage: x = Gamma1(3)([4,5,3,4]) ; x
            [4 5]
            [3 4]
            sage: x.matrix()
            [4 5]
            [3 4]
            sage: type(x.matrix())
            <class 'sage.matrix.matrix_integer_dense.Matrix_integer_dense'>"""
    @overload
    def matrix(self) -> Any:
        """ArithmeticSubgroupElement.matrix(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/arithgroup_element.pyx (starting at line 241)

        Return the matrix corresponding to ``self``.

        EXAMPLES::

            sage: x = Gamma1(3)([4,5,3,4]) ; x
            [4 5]
            [3 4]
            sage: x.matrix()
            [4 5]
            [3 4]
            sage: type(x.matrix())
            <class 'sage.matrix.matrix_integer_dense.Matrix_integer_dense'>"""
    @overload
    def multiplicative_order(self) -> Any:
        """ArithmeticSubgroupElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/arithgroup_element.pyx (starting at line 433)

        Return the multiplicative order of this element.

        EXAMPLES::

            sage: SL2Z.one().multiplicative_order()
            1
            sage: SL2Z([-1,0,0,-1]).multiplicative_order()
            2
            sage: s,t = SL2Z.gens()
            sage: ((t^3*s*t^2) * s * ~(t^3*s*t^2)).multiplicative_order()
            4
            sage: (t^3 * s * t * t^-3).multiplicative_order()
            6
            sage: (t^3 * s * t * s * t^-2).multiplicative_order()
            3
            sage: SL2Z([2,1,1,1]).multiplicative_order()
            +Infinity
            sage: SL2Z([-2,1,1,-1]).multiplicative_order()
            +Infinity"""
    @overload
    def multiplicative_order(self) -> Any:
        """ArithmeticSubgroupElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/arithgroup_element.pyx (starting at line 433)

        Return the multiplicative order of this element.

        EXAMPLES::

            sage: SL2Z.one().multiplicative_order()
            1
            sage: SL2Z([-1,0,0,-1]).multiplicative_order()
            2
            sage: s,t = SL2Z.gens()
            sage: ((t^3*s*t^2) * s * ~(t^3*s*t^2)).multiplicative_order()
            4
            sage: (t^3 * s * t * t^-3).multiplicative_order()
            6
            sage: (t^3 * s * t * s * t^-2).multiplicative_order()
            3
            sage: SL2Z([2,1,1,1]).multiplicative_order()
            +Infinity
            sage: SL2Z([-2,1,1,-1]).multiplicative_order()
            +Infinity"""
    @overload
    def multiplicative_order(self) -> Any:
        """ArithmeticSubgroupElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/arithgroup_element.pyx (starting at line 433)

        Return the multiplicative order of this element.

        EXAMPLES::

            sage: SL2Z.one().multiplicative_order()
            1
            sage: SL2Z([-1,0,0,-1]).multiplicative_order()
            2
            sage: s,t = SL2Z.gens()
            sage: ((t^3*s*t^2) * s * ~(t^3*s*t^2)).multiplicative_order()
            4
            sage: (t^3 * s * t * t^-3).multiplicative_order()
            6
            sage: (t^3 * s * t * s * t^-2).multiplicative_order()
            3
            sage: SL2Z([2,1,1,1]).multiplicative_order()
            +Infinity
            sage: SL2Z([-2,1,1,-1]).multiplicative_order()
            +Infinity"""
    @overload
    def multiplicative_order(self) -> Any:
        """ArithmeticSubgroupElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/arithgroup_element.pyx (starting at line 433)

        Return the multiplicative order of this element.

        EXAMPLES::

            sage: SL2Z.one().multiplicative_order()
            1
            sage: SL2Z([-1,0,0,-1]).multiplicative_order()
            2
            sage: s,t = SL2Z.gens()
            sage: ((t^3*s*t^2) * s * ~(t^3*s*t^2)).multiplicative_order()
            4
            sage: (t^3 * s * t * t^-3).multiplicative_order()
            6
            sage: (t^3 * s * t * s * t^-2).multiplicative_order()
            3
            sage: SL2Z([2,1,1,1]).multiplicative_order()
            +Infinity
            sage: SL2Z([-2,1,1,-1]).multiplicative_order()
            +Infinity"""
    @overload
    def multiplicative_order(self) -> Any:
        """ArithmeticSubgroupElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/arithgroup_element.pyx (starting at line 433)

        Return the multiplicative order of this element.

        EXAMPLES::

            sage: SL2Z.one().multiplicative_order()
            1
            sage: SL2Z([-1,0,0,-1]).multiplicative_order()
            2
            sage: s,t = SL2Z.gens()
            sage: ((t^3*s*t^2) * s * ~(t^3*s*t^2)).multiplicative_order()
            4
            sage: (t^3 * s * t * t^-3).multiplicative_order()
            6
            sage: (t^3 * s * t * s * t^-2).multiplicative_order()
            3
            sage: SL2Z([2,1,1,1]).multiplicative_order()
            +Infinity
            sage: SL2Z([-2,1,1,-1]).multiplicative_order()
            +Infinity"""
    @overload
    def multiplicative_order(self) -> Any:
        """ArithmeticSubgroupElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/arithgroup_element.pyx (starting at line 433)

        Return the multiplicative order of this element.

        EXAMPLES::

            sage: SL2Z.one().multiplicative_order()
            1
            sage: SL2Z([-1,0,0,-1]).multiplicative_order()
            2
            sage: s,t = SL2Z.gens()
            sage: ((t^3*s*t^2) * s * ~(t^3*s*t^2)).multiplicative_order()
            4
            sage: (t^3 * s * t * t^-3).multiplicative_order()
            6
            sage: (t^3 * s * t * s * t^-2).multiplicative_order()
            3
            sage: SL2Z([2,1,1,1]).multiplicative_order()
            +Infinity
            sage: SL2Z([-2,1,1,-1]).multiplicative_order()
            +Infinity"""
    @overload
    def multiplicative_order(self) -> Any:
        """ArithmeticSubgroupElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/arithgroup_element.pyx (starting at line 433)

        Return the multiplicative order of this element.

        EXAMPLES::

            sage: SL2Z.one().multiplicative_order()
            1
            sage: SL2Z([-1,0,0,-1]).multiplicative_order()
            2
            sage: s,t = SL2Z.gens()
            sage: ((t^3*s*t^2) * s * ~(t^3*s*t^2)).multiplicative_order()
            4
            sage: (t^3 * s * t * t^-3).multiplicative_order()
            6
            sage: (t^3 * s * t * s * t^-2).multiplicative_order()
            3
            sage: SL2Z([2,1,1,1]).multiplicative_order()
            +Infinity
            sage: SL2Z([-2,1,1,-1]).multiplicative_order()
            +Infinity"""
    @overload
    def multiplicative_order(self) -> Any:
        """ArithmeticSubgroupElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/arithgroup_element.pyx (starting at line 433)

        Return the multiplicative order of this element.

        EXAMPLES::

            sage: SL2Z.one().multiplicative_order()
            1
            sage: SL2Z([-1,0,0,-1]).multiplicative_order()
            2
            sage: s,t = SL2Z.gens()
            sage: ((t^3*s*t^2) * s * ~(t^3*s*t^2)).multiplicative_order()
            4
            sage: (t^3 * s * t * t^-3).multiplicative_order()
            6
            sage: (t^3 * s * t * s * t^-2).multiplicative_order()
            3
            sage: SL2Z([2,1,1,1]).multiplicative_order()
            +Infinity
            sage: SL2Z([-2,1,1,-1]).multiplicative_order()
            +Infinity"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __getitem__(self, q) -> Any:
        """ArithmeticSubgroupElement.__getitem__(self, q)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/arithgroup_element.pyx (starting at line 395)

        Fetch entries by direct indexing.

        EXAMPLES::

            sage: SL2Z([3,2,1,1])[0,0]
            3"""
    def __hash__(self) -> Any:
        """ArithmeticSubgroupElement.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/arithgroup_element.pyx (starting at line 406)

        Return a hash value.

        EXAMPLES::

            sage: hash(SL2Z.0)
            -8192788425652673914  # 64-bit
            -1995808122           # 32-bit"""
    @overload
    def __invert__(self) -> Any:
        """ArithmeticSubgroupElement.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/arithgroup_element.pyx (starting at line 226)

        Return the inverse of ``self``.

        EXAMPLES::

            sage: Gamma0(11)([1,-1,0,1]).__invert__()
            [1 1]
            [0 1]"""
    @overload
    def __invert__(self) -> Any:
        """ArithmeticSubgroupElement.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/arithgroup_element.pyx (starting at line 226)

        Return the inverse of ``self``.

        EXAMPLES::

            sage: Gamma0(11)([1,-1,0,1]).__invert__()
            [1 1]
            [0 1]"""
    def __iter__(self) -> Any:
        """ArithmeticSubgroupElement.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/arithgroup_element.pyx (starting at line 118)

        EXAMPLES::

            sage: Gamma0(2).0
            [1 1]
            [0 1]
            sage: list(Gamma0(2).0)
            [1, 1, 0, 1]

        Warning: this is different from the iteration on the matrix::

            sage: list(Gamma0(2).0.matrix())
            [(1, 1), (0, 1)]"""
    @overload
    def __reduce__(self) -> Any:
        """ArithmeticSubgroupElement.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/arithgroup_element.pyx (starting at line 418)

        Used for pickling.

        EXAMPLES::

            sage: (SL2Z.1).__reduce__()
            (Modular Group SL(2,Z), (
            [1 1]
            [0 1]
            ))"""
    @overload
    def __reduce__(self) -> Any:
        """ArithmeticSubgroupElement.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/arithgroup_element.pyx (starting at line 418)

        Used for pickling.

        EXAMPLES::

            sage: (SL2Z.1).__reduce__()
            (Modular Group SL(2,Z), (
            [1 1]
            [0 1]
            ))"""
