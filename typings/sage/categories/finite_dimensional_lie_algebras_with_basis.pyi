from _typeshed import Incomplete
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring as CategoryWithAxiom_over_base_ring
from sage.categories.lie_algebras import LieAlgebras as LieAlgebras
from sage.categories.subobjects import SubobjectsCategory as SubobjectsCategory
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.lazy_import import LazyImport as LazyImport
from sage.rings.integer import Integer as Integer
from sage.sets.family import Family as Family

class FiniteDimensionalLieAlgebrasWithBasis(CategoryWithAxiom_over_base_ring):
    """
    Category of finite dimensional Lie algebras with a basis.

    .. TODO::

        Many of these tests should use non-abelian Lie algebras and need to
        be added after :issue:`16820`.
    """
    def example(self, n: int = 3):
        """
        Return an example of a finite dimensional Lie algebra with basis as per
        :meth:`Category.example <sage.categories.category.Category.example>`.

        EXAMPLES::

            sage: C = LieAlgebras(QQ).FiniteDimensional().WithBasis()
            sage: C.example()                                                           # needs sage.modules
            An example of a finite dimensional Lie algebra with basis:
             the 3-dimensional abelian Lie algebra over Rational Field

        Other dimensions can be specified as an optional argument::

            sage: C.example(5)                                                          # needs sage.modules
            An example of a finite dimensional Lie algebra with basis:
             the 5-dimensional abelian Lie algebra over Rational Field
        """
    Nilpotent: Incomplete
    class ParentMethods:
        module: Incomplete
        def from_vector(self, v, order=None):
            """
            Return the element of ``self`` corresponding to the
            vector ``v`` in ``self.module()``.

            Implement this if you implement :meth:`module`; see the
            documentation of
            :meth:`sage.categories.lie_algebras.LieAlgebras.module`
            for how this is to be done.

            EXAMPLES::

                sage: L = LieAlgebras(QQ).FiniteDimensional().WithBasis().example()     # needs sage.modules
                sage: u = L.from_vector(vector(QQ, (1, 0, 0))); u                       # needs sage.modules
                (1, 0, 0)
                sage: parent(u) is L                                                    # needs sage.modules
                True
            """
        def killing_matrix(self, x, y):
            """
            Return the Killing matrix of ``x`` and ``y``, where ``x``
            and ``y`` are two elements of ``self``.

            The Killing matrix is defined as the matrix corresponding
            to the action of
            `\\operatorname{ad}_x \\circ \\operatorname{ad}_y` in the
            basis of ``self``.

            EXAMPLES::

                sage: L = LieAlgebras(QQ).FiniteDimensional().WithBasis().example()     # needs sage.modules
                sage: a, b, c = L.lie_algebra_generators()                              # needs sage.modules
                sage: L.killing_matrix(a, b)                                            # needs sage.modules
                [0 0 0]
                [0 0 0]
                [0 0 0]

            ::

                sage: L.<x,y> = LieAlgebra(QQ, {('x','y'): {'x':1}})                    # needs sage.combinat sage.modules
                sage: L.killing_matrix(y, x)                                            # needs sage.combinat sage.modules
                [ 0 -1]
                [ 0  0]
            """
        def killing_form(self, x, y):
            """
            Return the Killing form on ``x`` and ``y``, where ``x``
            and ``y`` are two elements of ``self``.

            The Killing form is defined as

            .. MATH::

                \\langle x \\mid y \\rangle
                = \\operatorname{tr}\\left( \\operatorname{ad}_x
                \\circ \\operatorname{ad}_y \\right).

            EXAMPLES::

                sage: L = LieAlgebras(QQ).FiniteDimensional().WithBasis().example()     # needs sage.modules
                sage: a, b, c = L.lie_algebra_generators()                              # needs sage.modules
                sage: L.killing_form(a, b)                                              # needs sage.modules
                0
            """
        @cached_method
        def killing_form_matrix(self):
            """
            Return the matrix of the Killing form of ``self``.

            The rows and the columns of this matrix are indexed by the
            elements of the basis of ``self`` (in the order provided by
            :meth:`basis`).

            EXAMPLES::

                sage: # needs sage.modules
                sage: L = LieAlgebras(QQ).FiniteDimensional().WithBasis().example()
                sage: L.killing_form_matrix()
                [0 0 0]
                [0 0 0]
                [0 0 0]
                sage: L = LieAlgebras(QQ).FiniteDimensional().WithBasis().example(0)
                sage: m = L.killing_form_matrix(); m
                []
                sage: parent(m)
                Full MatrixSpace of 0 by 0 dense matrices over Rational Field
            """
        @cached_method
        def structure_coefficients(self, include_zeros: bool = False):
            """
            Return the structure coefficients of ``self``.

            INPUT:

            - ``include_zeros`` -- boolean (default: ``False``); if ``True``,
              then include the `[x, y] = 0` pairs in the output

            OUTPUT:

            A dictionary whose keys are pairs of basis indices `(i, j)`
            with `i < j`, and whose values are the corresponding
            *elements* `[b_i, b_j]` in the Lie algebra.

            EXAMPLES::

                sage: L = LieAlgebras(QQ).FiniteDimensional().WithBasis().example()     # needs sage.modules
                sage: L.structure_coefficients()                                        # needs sage.modules
                Finite family {}
                sage: L.structure_coefficients(True)                                    # needs sage.modules
                Finite family {(0, 1): (0, 0, 0), (0, 2): (0, 0, 0), (1, 2): (0, 0, 0)}

            ::

                sage: # needs sage.combinat sage.groups sage.modules
                sage: G = SymmetricGroup(3)
                sage: S = GroupAlgebra(G, QQ)
                sage: L = LieAlgebra(associative=S)
                sage: L.structure_coefficients()
                Finite family {((2,3), (1,2)): (1,2,3) - (1,3,2),
                               ((2,3), (1,3)): -(1,2,3) + (1,3,2),
                               ((1,2,3), (2,3)): -(1,2) + (1,3),
                               ((1,2,3), (1,2)): (2,3) - (1,3),
                               ((1,2,3), (1,3)): -(2,3) + (1,2),
                               ((1,3,2), (2,3)): (1,2) - (1,3),
                               ((1,3,2), (1,2)): -(2,3) + (1,3),
                               ((1,3,2), (1,3)): (2,3) - (1,2),
                               ((1,3), (1,2)): -(1,2,3) + (1,3,2)}
            """
        def centralizer_basis(self, S):
            """
            Return a basis of the centralizer of ``S`` in ``self``.

            INPUT:

            - ``S`` -- a subalgebra of ``self`` or a list of elements that
              represent generators for a subalgebra

            .. SEEALSO::

                :meth:`centralizer`

            EXAMPLES::

                sage: # needs sage.combinat sage.modules
                sage: L = LieAlgebras(QQ).FiniteDimensional().WithBasis().example()
                sage: a, b, c = L.lie_algebra_generators()
                sage: L.centralizer_basis([a + b, 2*a + c])
                [(1, 0, 0), (0, 1, 0), (0, 0, 1)]

                sage: # needs sage.combinat sage.modules
                sage: H = lie_algebras.Heisenberg(QQ, 2)
                sage: H.centralizer_basis(H)
                [z]

                sage: # needs sage.combinat sage.groups sage.modules
                sage: D = DescentAlgebra(QQ, 4).D()
                sage: L = LieAlgebra(associative=D)
                sage: L.centralizer_basis(L)
                [D{},
                 D{1} + D{1, 2} + D{2, 3} + D{3},
                 D{1, 2, 3} + D{1, 3} + D{2}]
                sage: D.center_basis()
                (D{},
                 D{1} + D{1, 2} + D{2, 3} + D{3},
                 D{1, 2, 3} + D{1, 3} + D{2})

                sage: scoeffs = {('a','d'): {'a':1}, ('a','e'): {'b':-1},
                ....:            ('b','d'): {'b':1}, ('b','e'): {'a':1},
                ....:            ('d','e'): {'c':1}}
                sage: L.<a,b,c,d,e> = LieAlgebra(QQ, scoeffs)
                sage: L.centralizer_basis([a, c])
                [a, b, c]
                sage: L.centralizer_basis([a, e])
                [c]
            """
        def centralizer(self, S):
            """
            Return the centralizer of ``S`` in ``self``.

            INPUT:

            - ``S`` -- a subalgebra of ``self`` or a list of elements that
              represent generators for a subalgebra

            .. SEEALSO::

                :meth:`centralizer_basis`

            EXAMPLES::

                sage: # needs sage.combinat sage.modules
                sage: L = LieAlgebras(QQ).FiniteDimensional().WithBasis().example()
                sage: a, b, c = L.lie_algebra_generators()
                sage: S = L.centralizer([a + b, 2*a + c]); S
                An example of a finite dimensional Lie algebra with basis:
                 the 3-dimensional abelian Lie algebra over Rational Field
                sage: S.basis_matrix()
                [1 0 0]
                [0 1 0]
                [0 0 1]
            """
        @cached_method
        def center(self):
            """
            Return the center of ``self``.

            EXAMPLES::

                sage: # needs sage.combinat sage.modules
                sage: L = LieAlgebras(QQ).FiniteDimensional().WithBasis().example()
                sage: Z = L.center(); Z
                An example of a finite dimensional Lie algebra with basis: the
                 3-dimensional abelian Lie algebra over Rational Field
                sage: Z.basis_matrix()
                [1 0 0]
                [0 1 0]
                [0 0 1]
            """
        def normalizer_basis(self, S):
            """
            Return a basis of the normalizer of ``S`` in ``self``.

            INPUT:

            - ``S`` -- a subalgebra of ``self`` or a list of elements that
              represent generators for a subalgebra

            .. SEEALSO::

                :meth:`normalizer`

            EXAMPLES::

                sage: scoeffs = {('a','d'): {'a':1}, ('a','e'): {'b':-1},
                ....:            ('b','d'): {'b':1}, ('b','e'): {'a':1},
                ....:            ('d','e'): {'c':1}}
                sage: L.<a,b,c,d,e> = LieAlgebra(QQ, scoeffs)
                sage: L.normalizer_basis([a, e])
                [b, c]

                sage: S = L.subalgebra([a, e])
                sage: L.normalizer_basis(S)
                [a, b, c, e]

            When the subalgebra is the ambient Lie algebra, we return the
            basis of the ambient Lie algebra::

                sage: L.normalizer_basis(L)
                Finite family {'a': a, 'b': b, 'c': c, 'd': d, 'e': e}
                sage: L.normalizer_basis([a, b, c, a, d + e, a + e])
                Finite family {'a': a, 'b': b, 'c': c, 'd': d, 'e': e}
            """
        def normalizer(self, S):
            """
            Return the normalizer of ``S`` in ``self``.

            INPUT:

            - ``S`` -- a subalgebra of ``self`` or a list of elements that
              represent generators for a subalgebra

            .. SEEALSO::

                :meth:`normalizer_basis`

            EXAMPLES::

                sage: scoeffs = {('a','d'): {'a':1}, ('a','e'): {'b':-1},
                ....:            ('b','d'): {'b':1}, ('b','e'): {'a':1},
                ....:            ('d','e'): {'c':1}}
                sage: L.<a,b,c,d,e> = LieAlgebra(QQ, scoeffs)
                sage: L.normalizer([a, e])
                Subalgebra generated by (b, c) of Lie algebra on
                 5 generators (a, b, c, d, e) over Rational Field
                sage: L.normalizer([a, c, e])
                Subalgebra generated by (b, c, d) of Lie algebra on
                 5 generators (a, b, c, d, e) over Rational Field
            """
        @cached_method
        def derivations_basis(self):
            """
            Return a basis for the Lie algebra of derivations
            of ``self`` as matrices.

            A derivation `D` of an algebra is an endomorphism of `A`
            such that

            .. MATH::

                D([a, b]) = [D(a), b] + [a, D(b)]

            for all `a, b \\in A`. The set of all derivations
            form a Lie algebra.

            EXAMPLES:

            We construct the derivations of the Heisenberg Lie algebra::

                sage: # needs sage.combinat sage.modules
                sage: H = lie_algebras.Heisenberg(QQ, 1)
                sage: H.derivations_basis()
                (
                [1 0 0]  [0 1 0]  [0 0 0]  [0 0 0]  [0 0 0]  [0 0 0]
                [0 0 0]  [0 0 0]  [1 0 0]  [0 1 0]  [0 0 0]  [0 0 0]
                [0 0 1], [0 0 0], [0 0 0], [0 0 1], [1 0 0], [0 1 0]
                )

            We construct the derivations of `\\mathfrak{sl}_2`::

                sage: # needs sage.combinat sage.modules
                sage: sl2 = lie_algebras.sl(QQ, 2)
                sage: sl2.derivations_basis()
                (
                [ 1  0  0]  [   0    1    0]  [ 0  0  0]
                [ 0  0  0]  [   0    0 -1/2]  [ 1  0  0]
                [ 0  0 -1], [   0    0    0], [ 0 -2  0]
                )

            We verify these are derivations::

                sage: # needs sage.combinat sage.modules
                sage: D = [sl2.module_morphism(matrix=M, codomain=sl2)
                ....:      for M in sl2.derivations_basis()]
                sage: all(d(a.bracket(b)) == d(a).bracket(b) + a.bracket(d(b))
                ....:     for a in sl2.basis() for b in sl2.basis() for d in D)
                True

            REFERENCES:

            :wikipedia:`Derivation_(differential_algebra)`
            """
        @cached_method
        def inner_derivations_basis(self):
            """
            Return a basis for the Lie algebra of inner derivations
            of ``self`` as matrices.

            EXAMPLES::

                sage: # needs sage.combinat sage.modules
                sage: H = lie_algebras.Heisenberg(QQ, 1)
                sage: H.inner_derivations_basis()
                (
                [0 0 0]  [0 0 0]
                [0 0 0]  [0 0 0]
                [1 0 0], [0 1 0]
                )
            """
        @cached_method
        def nilradical_basis(self):
            """
            Return a basis of the nilradical of ``self``.

            .. SEEALSO::

                :meth:`nilradical`

            EXAMPLES::

                sage: scoeffs = {('a','d'): {'a':1}, ('a','e'): {'b':-1},
                ....:            ('b','d'): {'b':1}, ('b','e'): {'a':1},
                ....:            ('d','e'): {'c':1}}
                sage: L.<a,b,c,d,e> = LieAlgebra(QQ, scoeffs)
                sage: L.nilradical_basis()
                (a, b, c)
                sage: L.is_nilpotent()
                False

                sage: sl3 = LieAlgebra(QQ, cartan_type=['A',2])
                sage: sl3.nilradical_basis()
                ()

                sage: scoeffs = {('a','e'): {'a':1}, ('b','e'): {'a':1,'b':1},
                ....:            ('c','d'): {'a':1}, ('c','e'): {'c':1}}
                sage: L.<a,b,c,d,e> = LieAlgebra(QQ, scoeffs)
                sage: L.nilradical_basis()
                (a, b, c, d)
                sage: L.is_solvable()
                True
                sage: L.is_nilpotent()
                False

                sage: K1 = L.quotient([a])
                sage: K1.nilradical_basis()
                (b, c, d)

                sage: SL = L.subalgebra([a,b,c,d]); SL
                Subalgebra generated by (a, b, c, d) of
                 Lie algebra on 5 generators (a, b, c, d, e) over Rational Field
                sage: SL.nilradical_basis()
                (a, b, c, d)

                sage: scoeffs = {('x','z'): {'x':1, 'y':1}, ('y','z'): {'y':1}}
                sage: L.<x,y,z> = LieAlgebra(GF(3), scoeffs)
                sage: L.nilradical_basis()
                (x, y)

            We check against the generic algorithm::

                sage: L.<x,y,z> = LieAlgebra(QQ, {('x','z'): {'x':1,'y':1}, ('y','z'): {'y':1}})
                sage: L.nilradical_basis()
                (x, y)

                sage: dim = L.dimension()
                sage: MS = MatrixSpace(L.base_ring(), dim)
                sage: gens = [b.adjoint_matrix() for b in L.basis()]
                sage: A = MS.subalgebra(gens)
                sage: RB = A.radical_basis()
                sage: mat = matrix(L.base_ring(),
                ....:              [g._vector_() for g in gens]
                ....:              + [A.lift(r)._vector_() for r in RB])
                sage: tuple([L.from_vector(w) for v in mat.right_kernel().basis()
                ....:               if (w := v[:dim])])
                (x, y)

            A positive characteristic example::

                sage: scoeffs = {('x','z'): {'x':1,'y':1}, ('y','z'): {'y':1}}
                sage: L.<x,y,z> = LieAlgebra(GF(3), scoeffs)
                sage: L.nilradical_basis()
                (x, y)
            """
        def nilradical(self):
            """
            Return the nilradical of ``self``.

            The *nilradical* of a Lie algebra `L` is the largest
            nilpotent ideal of `L`.

            .. SEEALSO::

                :meth:`nilradical_basis`

            EXAMPLES::

                sage: scoeffs = {('a','d'): {'a':1}, ('a','e'): {'b':-1},
                ....:            ('b','d'): {'b':1}, ('b','e'): {'a':1},
                ....:            ('d','e'): {'c':1}}
                sage: L.<a,b,c,d,e> = LieAlgebra(QQ, scoeffs)
                sage: L.solvable_radical()
                Ideal (a, b, c, d, e) of
                 Lie algebra on 5 generators (a, b, c, d, e) over Rational Field
            """
        @cached_method
        def solvable_radical_basis(self):
            """
            Return a basis of the solvable radical of ``self``.

            .. SEEALSO::

                :meth:`solvable_radical`

            EXAMPLES::

                sage: scoeffs = {('a','d'): {'a':1}, ('a','e'): {'b':-1},
                ....:            ('b','d'): {'b':1}, ('b','e'): {'a':1},
                ....:            ('d','e'): {'c':1}}
                sage: L.<a,b,c,d,e> = LieAlgebra(QQ, scoeffs)
                sage: L.solvable_radical_basis()
                (a, b, c, d, e)
                sage: L.is_solvable()
                True

                sage: sl3 = LieAlgebra(QQ, cartan_type=['A',2])
                sage: sl3.solvable_radical_basis()
                ()

                sage: L.<x,y,z> = LieAlgebra(QQ, {('x','z'): {'x':1,'y':1}, ('y','z'): {'y':1}})
                sage: S = L.subalgebra([x, y])
                sage: S.solvable_radical_basis()
                (x, y)
                sage: S.is_solvable()
                True

            Positive characteristic examples::

                sage: scoeffs = {('x','z'): {'x':1,'y':1}, ('y','z'): {'y':1}}
                sage: L.<x,y,z> = LieAlgebra(GF(3), scoeffs)
                sage: L.solvable_radical_basis()
                (x, y, z)
                sage: sl3 = LieAlgebra(GF(3), cartan_type=['A',2])
                sage: sl3.solvable_radical_basis()
                (2*h1 + h2,)
            """
        def solvable_radical(self):
            """
            Return the solvable radical of ``self``.

            The *solvable radical* of a Lie algebra `L` is the largest
            solvable ideal of `L`.

            .. SEEALSO::

                :meth:`solvable_radical_basis`

            EXAMPLES::

                sage: scoeffs = {('a','d'): {'a':1}, ('a','e'): {'b':-1},
                ....:            ('b','d'): {'b':1}, ('b','e'): {'a':1},
                ....:            ('d','e'): {'c':1}}
                sage: L.<a,b,c,d,e> = LieAlgebra(QQ, scoeffs)
                sage: L.solvable_radical()
                Ideal (a, b, c, d, e) of Lie algebra on 5 generators (a, b, c, d, e) over Rational Field
            """
        def subalgebra(self, *gens, **kwds):
            """
            Return the subalgebra of ``self`` generated by ``gens``.

            INPUT:

            - ``gens`` -- list of generators of the subalgebra
            - ``category`` -- (optional) a subcategory of subobjects of finite
              dimensional Lie algebras with basis

            EXAMPLES::

                sage: # needs sage.combinat sage.modules
                sage: H = lie_algebras.Heisenberg(QQ, 2)
                sage: p1,p2,q1,q2,z = H.basis()
                sage: S = H.subalgebra([p1, q1])
                sage: S.basis().list()
                [p1, q1, z]
                sage: S.basis_matrix()
                [1 0 0 0 0]
                [0 0 1 0 0]
                [0 0 0 0 1]

            Passing an extra category to a subalgebra::

                sage: # needs sage.combinat sage.modules
                sage: L = LieAlgebra(QQ, 3, step=2)
                sage: x,y,z = L.homogeneous_component_basis(1)
                sage: C = LieAlgebras(QQ).FiniteDimensional().WithBasis()
                sage: C = C.Subobjects().Graded().Stratified()
                sage: S = L.subalgebra([x, y], category=C)
                sage: S.homogeneous_component_basis(2).list()
                [X_12]
            """
        def ideal(self, *gens, **kwds):
            """
            Return the ideal of ``self`` generated by ``gens``.

            INPUT:

            - ``gens`` -- list of generators of the ideal
            - ``category`` -- (optional) a subcategory of subobjects of finite
              dimensional Lie algebras with basis

            EXAMPLES::

                sage: # needs sage.combinat sage.modules
                sage: H = lie_algebras.Heisenberg(QQ, 2)
                sage: p1,p2,q1,q2,z = H.basis()
                sage: I = H.ideal([p1 - p2, q1 - q2])
                sage: I.basis().list()
                [-p1 + p2, -q1 + q2, z]
                sage: I.reduce(p1 + p2 + q1 + q2 + z)
                2*p1 + 2*q1

            Passing an extra category to an ideal::

                sage: # needs sage.combinat sage.modules
                sage: L.<x,y,z> = LieAlgebra(QQ, abelian=True)
                sage: C = LieAlgebras(QQ).FiniteDimensional().WithBasis()
                sage: C = C.Subobjects().Graded().Stratified()
                sage: I = L.ideal(x, y, category=C)
                sage: I.homogeneous_component_basis(1).list()
                [x, y]
            """
        @cached_method
        def is_ideal(self, A):
            """
            Return if ``self`` is an ideal of ``A``.

            EXAMPLES::

                sage: # needs sage.combinat sage.modules
                sage: L = LieAlgebras(QQ).FiniteDimensional().WithBasis().example()
                sage: a, b, c = L.lie_algebra_generators()
                sage: I = L.ideal([2*a - c, b + c])
                sage: I.is_ideal(L)
                True

                sage: L.<x,y> = LieAlgebra(QQ, {('x','y'):{'x':1}})                     # needs sage.combinat sage.modules
                sage: L.is_ideal(L)                                                     # needs sage.combinat sage.modules
                True

                sage: F = LieAlgebra(QQ, 'F', representation='polynomial')              # needs sage.combinat sage.modules
                sage: L.is_ideal(F)                                                     # needs sage.combinat sage.modules
                Traceback (most recent call last):
                ...
                NotImplementedError: A must be a finite dimensional Lie algebra
                 with basis
            """
        def quotient(self, I, names=None, category=None):
            """
            Return the quotient of ``self`` by the ideal ``I``.

            A quotient Lie algebra.

            INPUT:

            - ``I`` -- an ideal or a list of generators of the ideal
            - ``names`` -- (optional) string or list of strings;
              names for the basis elements of the quotient. If ``names`` is a
              string, the basis will be named ``names_1``,...,``names_n``.

            EXAMPLES:

            The Engel Lie algebra as a quotient of the free nilpotent Lie algebra
            of step 3 with 2 generators::

                sage: # needs sage.combinat sage.modules
                sage: L.<X,Y,Z,W,U> = LieAlgebra(QQ, 2, step=3)
                sage: E = L.quotient(U); E
                Lie algebra quotient L/I of dimension 4 over Rational Field where
                 L: Free Nilpotent Lie algebra on 5 generators (X, Y, Z, W, U)
                    over Rational Field
                 I: Ideal (U)
                sage: E.basis().list()
                [X, Y, Z, W]
                sage: E(X).bracket(E(Y))
                Z
                sage: Y.bracket(Z)
                -U
                sage: E(Y).bracket(E(Z))
                0
                sage: E(U)
                0

            Quotients when the base ring is not a field are not implemented::

                sage: # needs sage.combinat sage.modules
                sage: L = lie_algebras.Heisenberg(ZZ, 1)
                sage: L.quotient(L.an_element())
                Traceback (most recent call last):
                ...
                NotImplementedError: quotients over non-fields not implemented
            """
        def product_space(self, L, submodule: bool = False):
            """
            Return the product space ``[self, L]``.

            INPUT:

            - ``L`` -- a Lie subalgebra of ``self``
            - ``submodule`` -- boolean (default: ``False``); if ``True``, then
              the result is forced to be a submodule of ``self``

            EXAMPLES::

                sage: # needs sage.combinat sage.modules
                sage: L = LieAlgebras(QQ).FiniteDimensional().WithBasis().example()
                sage: a,b,c = L.lie_algebra_generators()
                sage: X = L.subalgebra([a, b + c])
                sage: L.product_space(X)
                An example of a finite dimensional Lie algebra with basis:
                 the 0-dimensional abelian Lie algebra over Rational Field
                  with basis matrix: []
                sage: Y = L.subalgebra([a, 2*b - c])
                sage: X.product_space(Y)
                An example of a finite dimensional Lie algebra with basis:
                 the 0-dimensional abelian Lie algebra over Rational Field
                  with basis matrix: []

            ::

                sage: # needs sage.combinat sage.modules
                sage: H = lie_algebras.Heisenberg(ZZ, 4)
                sage: Hp = H.product_space(H, submodule=True).basis()
                sage: [H.from_vector(v) for v in Hp]
                [z]

            ::

                sage: # needs sage.combinat sage.modules
                sage: L.<x,y> = LieAlgebra(QQ, {('x','y'):{'x':1}})
                sage: Lp = L.product_space(L)   # not implemented
                sage: Lp                        # not implemented
                Subalgebra generated of
                 Lie algebra on 2 generators (x, y) over Rational Field
                 with basis: (x,)
                sage: Lp.product_space(L)       # not implemented
                Subalgebra generated of
                 Lie algebra on 2 generators (x, y) over Rational Field
                 with basis: (x,)
                sage: L.product_space(Lp)       # not implemented
                Subalgebra generated of
                 Lie algebra on 2 generators (x, y) over Rational Field
                 with basis: (x,)
                sage: Lp.product_space(Lp)      # not implemented
                Subalgebra generated of
                 Lie algebra on 2 generators (x, y) over Rational Field
                 with basis: ()
            """
        @cached_method
        def derived_subalgebra(self):
            """
            Return the derived subalgebra of ``self``.

            EXAMPLES::

                sage: # needs sage.combinat sage.modules
                sage: L = LieAlgebras(QQ).FiniteDimensional().WithBasis().example()
                sage: L.derived_subalgebra()
                An example of a finite dimensional Lie algebra with basis:
                 the 0-dimensional abelian Lie algebra over Rational Field
                 with basis matrix:
                []

            If ``self`` is semisimple, then the derived subalgebra is ``self``::

                sage: # needs sage.combinat sage.modules
                sage: sl3 = LieAlgebra(QQ, cartan_type=['A', 2])
                sage: sl3.derived_subalgebra()
                Lie algebra of ['A', 2] in the Chevalley basis
                sage: sl3 is sl3.derived_subalgebra()
                True
            """
        @cached_method
        def derived_series(self):
            """
            Return the derived series `(\\mathfrak{g}^{(i)})_i` of ``self``
            where the rightmost
            `\\mathfrak{g}^{(k)} = \\mathfrak{g}^{(k+1)} = \\cdots`.

            We define the derived series of a Lie algebra `\\mathfrak{g}`
            recursively by `\\mathfrak{g}^{(0)} := \\mathfrak{g}` and

            .. MATH::

                \\mathfrak{g}^{(k+1)} =
                [\\mathfrak{g}^{(k)}, \\mathfrak{g}^{(k)}]

            and recall that
            `\\mathfrak{g}^{(k)} \\supseteq \\mathfrak{g}^{(k+1)}`.
            Alternatively we can express this as

            .. MATH::

                \\mathfrak{g} \\supseteq [\\mathfrak{g}, \\mathfrak{g}] \\supseteq
                \\bigl[ [\\mathfrak{g}, \\mathfrak{g}], [\\mathfrak{g},
                \\mathfrak{g}] \\bigr] \\supseteq
                \\biggl[ \\bigl[ [\\mathfrak{g}, \\mathfrak{g}], [\\mathfrak{g},
                \\mathfrak{g}] \\bigr], \\bigl[ [\\mathfrak{g}, \\mathfrak{g}],
                [\\mathfrak{g}, \\mathfrak{g}] \\bigr] \\biggr] \\supseteq \\cdots.

            EXAMPLES::

                sage: # needs sage.combinat sage.modules
                sage: L = LieAlgebras(QQ).FiniteDimensional().WithBasis().example()
                sage: L.derived_series()
                (An example of a finite dimensional Lie algebra with basis:
                    the 3-dimensional abelian Lie algebra over Rational Field,
                 An example of a finite dimensional Lie algebra with basis:
                    the 0-dimensional abelian Lie algebra over Rational Field
                    with basis matrix: [])

            ::

                sage: # needs sage.combinat sage.modules
                sage: L.<x,y> = LieAlgebra(QQ, {('x','y'): {'x':1}})
                sage: L.derived_series()
                (Lie algebra on 2 generators (x, y) over Rational Field,
                 Ideal (x) of Lie algebra on 2 generators (x, y) over Rational Field,
                 Ideal () of Lie algebra on 2 generators (x, y) over Rational Field)

                sage: scoeffs = {('a','d'): {'a':1}, ('a','e'): {'b':-1},
                ....:            ('b','d'): {'b':1}, ('b','e'): {'a':1},
                ....:            ('d','e'): {'c':1}}
                sage: L.<a,b,c,d,e> = LieAlgebra(QQ, scoeffs)
                sage: L.derived_series()
                (Lie algebra on 5 generators (a, b, c, d, e) over Rational Field,
                 Ideal (a, b, c) of Lie algebra on 5 generators (a, b, c, d, e) over Rational Field,
                 Ideal () of Lie algebra on 5 generators (a, b, c, d, e) over Rational Field)
            """
        @cached_method
        def lower_central_series(self, submodule: bool = False):
            """
            Return the lower central series `(\\mathfrak{g}_{i})_i`
            of ``self`` where the rightmost
            `\\mathfrak{g}_k = \\mathfrak{g}_{k+1} = \\cdots`.

            INPUT:

            - ``submodule`` -- boolean (default: ``False``); if ``True``, then
              the result is given as submodules of ``self``

            We define the lower central series of a Lie algebra `\\mathfrak{g}`
            recursively by `\\mathfrak{g}_0 := \\mathfrak{g}` and

            .. MATH::

                \\mathfrak{g}_{k+1} = [\\mathfrak{g}, \\mathfrak{g}_{k}]

            and recall that `\\mathfrak{g}_{k} \\supseteq \\mathfrak{g}_{k+1}`.
            Alternatively we can express this as

            .. MATH::

                \\mathfrak{g} \\supseteq [\\mathfrak{g}, \\mathfrak{g}] \\supseteq
                \\bigl[ [\\mathfrak{g}, \\mathfrak{g}], \\mathfrak{g} \\bigr]
                \\supseteq \\Bigl[\\bigl[ [\\mathfrak{g}, \\mathfrak{g}],
                \\mathfrak{g} \\bigr], \\mathfrak{g}\\Bigr] \\supseteq \\cdots.

            EXAMPLES::

                sage: # needs sage.combinat sage.modules
                sage: L = LieAlgebras(QQ).FiniteDimensional().WithBasis().example()
                sage: L.derived_series()
                (An example of a finite dimensional Lie algebra with basis:
                  the 3-dimensional abelian Lie algebra over Rational Field,
                 An example of a finite dimensional Lie algebra with basis:
                  the 0-dimensional abelian Lie algebra over Rational Field
                   with basis matrix: [])

            The lower central series as submodules::

                sage: # needs sage.combinat sage.modules
                sage: L.<x,y> = LieAlgebra(QQ, {('x','y'): {'x':1}})
                sage: L.lower_central_series(submodule=True)
                (Sparse vector space of dimension 2 over Rational Field,
                 Vector space of degree 2 and dimension 1 over Rational Field
                  Basis matrix: [1 0])

            ::

                sage: # needs sage.combinat sage.modules
                sage: L.<x,y> = LieAlgebra(QQ, {('x','y'): {'x':1}})
                sage: L.lower_central_series()
                (Lie algebra on 2 generators (x, y) over Rational Field,
                 Ideal (x) of Lie algebra on 2 generators (x, y) over Rational Field)

                sage: scoeffs = {('a','d'): {'a':1}, ('a','e'): {'b':-1},
                ....:            ('b','d'): {'b':1}, ('b','e'): {'a':1},
                ....:            ('d','e'): {'c':1}}
                sage: L.<a,b,c,d,e> = LieAlgebra(QQ, scoeffs)
                sage: L.lower_central_series()
                (Lie algebra on 5 generators (a, b, c, d, e) over Rational Field,
                 Ideal (a, b, c) of Lie algebra on 5 generators (a, b, c, d, e) over Rational Field,
                 Ideal (a, b) of Lie algebra on 5 generators (a, b, c, d, e) over Rational Field)
            """
        @cached_method
        def upper_central_series(self):
            """
            Return the upper central series `(Z_i(\\mathfrak{g}))_i`
            of ``self`` where the rightmost
            `Z_k(\\mathfrak{g}) = Z_{k+1}(\\mathfrak{g}) = \\cdots`.

            The *upper central series* of a Lie algebra `\\mathfrak{g}` is
            defined recursively by `Z_0(\\mathfrak{g}) := Z(\\mathfrak{g})` and

            .. MATH::

                Z_{k+1}(\\mathfrak{g}) / Z_k(\\mathfrak{g})
                = Z(\\mathfrak{g} / Z_k(\\mathfrak{g}),

            and recall that `Z(\\mathfrak{g})` is the :meth:`center`
            of `\\mathfrak{g}`.

            EXAMPLES::

                sage: L = LieAlgebras(QQ).FiniteDimensional().WithBasis().example()
                sage: L.upper_central_series()
                [An example of a finite dimensional Lie algebra with basis:
                 the 3-dimensional abelian Lie algebra over Rational Field]

                sage: L.<x,y> = LieAlgebra(QQ, {('x','y'): {'x':1}})
                sage: L.upper_central_series()
                [Ideal () of Lie algebra on 2 generators (x, y) over Rational Field]

                sage: scoeffs = {('a','d'): {'a':1}, ('a','e'): {'b':-1},
                ....:            ('b','d'): {'b':1}, ('b','e'): {'a':1},
                ....:            ('d','e'): {'c':1}}
                sage: L.<a,b,c,d,e> = LieAlgebra(QQ, scoeffs)
                sage: L.upper_central_series()
                [Ideal (c) of Lie algebra on 5 generators (a, b, c, d, e) over Rational Field]

                sage: L = lie_algebras.Heisenberg(QQ, 3)
                sage: L.upper_central_series()
                [Ideal (z) of Heisenberg algebra of rank 3 over Rational Field,
                 Heisenberg algebra of rank 3 over Rational Field]
            """
        def hypercenter(self):
            """
            Return the hypercenter of ``self``.

            EXAMPLES::

                sage: SGA3 = SymmetricGroup(3).algebra(QQ)
                sage: L = LieAlgebra(associative=SGA3)
                sage: L.hypercenter()
                Ideal ((), (1,2,3) + (1,3,2), (2,3) + (1,2) + (1,3)) of
                 Lie algebra of Symmetric group algebra of order 3
                 over Rational Field

                sage: L = lie_algebras.Heisenberg(QQ, 3)
                sage: L.hypercenter()
                Heisenberg algebra of rank 3 over Rational Field
            """
        def is_abelian(self):
            """
            Return if ``self`` is an abelian Lie algebra.

            EXAMPLES::

                sage: # needs sage.combinat sage.modules
                sage: L = LieAlgebras(QQ).FiniteDimensional().WithBasis().example()
                sage: L.is_abelian()
                True

            ::

                sage: # needs sage.combinat sage.modules
                sage: L.<x,y> = LieAlgebra(QQ, {('x','y'): {'x':1}})
                sage: L.is_abelian()
                False
            """
        def is_solvable(self):
            """
            Return if ``self`` is a solvable Lie algebra.

            A Lie algebra is solvable if the derived series eventually
            becomes `0`.

            EXAMPLES::

                sage: # needs sage.combinat sage.modules
                sage: L = LieAlgebras(QQ).FiniteDimensional().WithBasis().example()
                sage: L.is_solvable()
                True

            ::

                sage: # needs sage.combinat sage.modules
                sage: L.<x,y> = LieAlgebra(QQ, {('x','y'): {'x':1}})
                sage: L.is_solvable()           # not implemented
                False
            """
        def is_nilpotent(self):
            """
            Return if ``self`` is a nilpotent Lie algebra.

            A Lie algebra is nilpotent if the lower central series eventually
            becomes `0`.

            EXAMPLES::

                sage: # needs sage.combinat sage.modules
                sage: L = LieAlgebras(QQ).FiniteDimensional().WithBasis().example()
                sage: L.is_nilpotent()
                True
            """
        def is_semisimple(self):
            """
            Return if ``self`` if a semisimple Lie algebra.

            A Lie algebra is semisimple if the solvable radical is zero. In
            characteristic 0, this is equivalent to saying the Killing form
            is non-degenerate.

            EXAMPLES::

                sage: # needs sage.combinat sage.modules
                sage: L = LieAlgebras(QQ).FiniteDimensional().WithBasis().example()
                sage: L.is_semisimple()
                False

            Positive characteristic examples::

                sage: L.<x,y,z> = LieAlgebra(GF(3), {('x','z'): {'x':1, 'y':1}, ('y','z'): {'y':1}})
                sage: L.is_semisimple()
                False

                sage: sp4 = LieAlgebra(GF(3), cartan_type=['C',2])
                sage: sp4.killing_form_matrix().det()
                0
                sage: sp4.solvable_radical_basis()  # long time
                ()
                sage: sp4.is_semisimple()  # long time
                True
            """
        def chevalley_eilenberg_complex(self, M=None, dual: bool = False, sparse: bool = True, ncpus=None):
            """
            Return the Chevalley-Eilenberg complex of ``self``.

            Let `\\mathfrak{g}` be a Lie algebra and `M` be a right
            `\\mathfrak{g}`-module. The *Chevalley-Eilenberg complex*
            is the chain complex on

            .. MATH::

                C_{\\bullet}(\\mathfrak{g}, M) =
                M \\otimes \\bigwedge\\nolimits^{\\bullet} \\mathfrak{g},

            where the differential is given by

            .. MATH::

                d(m \\otimes g_1 \\wedge \\cdots \\wedge g_p) =
                \\sum_{i=1}^p (-1)^{i+1}
                  (m g_i) \\otimes g_1 \\wedge \\cdots \\wedge
                  \\hat{g}_i \\wedge \\cdots \\wedge g_p +
                \\sum_{1 \\leq i < j \\leq p} (-1)^{i+j}
                  m \\otimes [g_i, g_j] \\wedge
                  g_1 \\wedge \\cdots \\wedge \\hat{g}_i
                  \\wedge \\cdots \\wedge \\hat{g}_j
                  \\wedge \\cdots \\wedge g_p.

            INPUT:

            - ``M`` -- (default: the trivial 1-dimensional module)
              one of the following:

              * a module `M` with an action of ``self``
              * a dictionary whose keys are basis elements and values
                are matrices representing a Lie algebra homomorphism
                defining the representation

            - ``dual`` -- boolean (default: ``False``); if ``True``, causes
              the dual of the complex to be computed
            - ``sparse`` -- boolean (default: ``True``); whether to use sparse
              or dense matrices
            - ``ncpus`` -- (optional) how many cpus to use

            EXAMPLES::

                sage: # needs sage.combinat sage.modules
                sage: L = lie_algebras.sl(ZZ, 2)
                sage: C = L.chevalley_eilenberg_complex(); C
                Chain complex with at most 4 nonzero terms over Integer Ring
                sage: ascii_art(C)
                                          [-2  0  0]       [0]
                                          [ 0  1  0]       [0]
                            [0 0 0]       [ 0  0 -2]       [0]
                 0 <-- C_0 <-------- C_1 <----------- C_2 <---- C_3 <-- 0

                sage: # needs sage.combinat sage.modules
                sage: L = LieAlgebra(QQ, cartan_type=['C',2])
                sage: C = L.chevalley_eilenberg_complex()  # long time
                sage: [C.free_module_rank(i) for i in range(11)]  # long time
                [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]

                sage: # needs sage.combinat sage.modules
                sage: g = lie_algebras.sl(QQ, 2)
                sage: E, F, H = g.basis()
                sage: n = g.subalgebra([F, H])
                sage: ascii_art(n.chevalley_eilenberg_complex())
                                        [ 0]
                            [0 0]       [-2]
                 0 <-- C_0 <------ C_1 <----- C_2 <-- 0

                sage: L.<x,y> = LieAlgebra(QQ, {('x','y'): {'y':1}})
                sage: f = ({x: Matrix([[1,0],[0,0]]), y: Matrix([[0,1],[0,0]])})
                sage: C = L.chevalley_eilenberg_complex(f); C
                Chain complex with at most 3 nonzero terms over Rational Field
                sage: ascii_art(C)
                                            [ 0 -1]
                                            [ 2  0]
                            [1 0 0 1]       [ 0  0]
                            [0 0 0 0]       [ 0  1]
                 0 <-- C_0 <---------- C_1 <-------- C_2 <-- 0

                sage: ascii_art(L.chevalley_eilenberg_complex(f, sparse=False))
                                            [ 0 -1]
                                            [ 2  0]
                            [1 0 0 1]       [ 0  0]
                            [0 0 0 0]       [ 0  1]
                 0 <-- C_0 <---------- C_1 <-------- C_2 <-- 0

            REFERENCES:

            - :wikipedia:`Lie_algebra_cohomology#Chevalley-Eilenberg_complex`
            - [Wei1994]_ Chapter 7
            """
        def homology(self, deg=None, M=None, sparse: bool = True, ncpus=None):
            """
            Return the Lie algebra homology of ``self``.

            The Lie algebra homology is the homology of the
            Chevalley-Eilenberg chain complex.

            INPUT:

            - ``deg`` -- the degree of the homology (optional)
            - ``M`` -- (default: the trivial module) a right module
              of ``self``
            - ``sparse`` -- boolean (default: ``True``); whether to use sparse
              matrices for the Chevalley-Eilenberg chain complex
            - ``ncpus`` -- (optional) how many cpus to use when
              computing the Chevalley-Eilenberg chain complex

            EXAMPLES::

                sage: # needs sage.combinat sage.modules
                sage: L = lie_algebras.cross_product(QQ)
                sage: L.homology()
                {0: Vector space of dimension 1 over Rational Field,
                 1: Vector space of dimension 0 over Rational Field,
                 2: Vector space of dimension 0 over Rational Field,
                 3: Vector space of dimension 1 over Rational Field}

                sage: # needs sage.combinat sage.modules
                sage: L = lie_algebras.pwitt(GF(5), 5)
                sage: L.homology()
                {0: Vector space of dimension 1 over Finite Field of size 5,
                 1: Vector space of dimension 0 over Finite Field of size 5,
                 2: Vector space of dimension 1 over Finite Field of size 5,
                 3: Vector space of dimension 1 over Finite Field of size 5,
                 4: Vector space of dimension 0 over Finite Field of size 5,
                 5: Vector space of dimension 1 over Finite Field of size 5}

                sage: # needs sage.combinat sage.modules
                sage: d = {('x', 'y'): {'y': 2}}
                sage: L.<x,y> = LieAlgebra(ZZ, d)
                sage: L.homology()
                {0: Z, 1: Z x C2, 2: 0}

            .. SEEALSO::

                :meth:`chevalley_eilenberg_complex`
            """
        def cohomology(self, deg=None, M=None, sparse: bool = True, ncpus=None):
            """
            Return the Lie algebra cohomology of ``self``.

            The Lie algebra cohomology is the cohomology of the
            Chevalley-Eilenberg cochain complex (which is the dual
            of the Chevalley-Eilenberg chain complex).

            Let `\\mathfrak{g}` be a Lie algebra and `M` a left
            `\\mathfrak{g}`-module. It is known that `H^0(\\mathfrak{g}; M)`
            is the subspace of `\\mathfrak{g}`-invariants of `M`:

            .. MATH::

                H^0(\\mathfrak{g}; M) = M^{\\mathfrak{g}}
                = \\{ m \\in M \\mid g m = 0
                    \\text{ for all } g \\in \\mathfrak{g} \\}.

            Additionally, `H^1(\\mathfrak{g}; M)` is the space of
            derivations `\\mathfrak{g} \\to M`
            modulo the space of inner derivations, and
            `H^2(\\mathfrak{g}; M)` is the space of equivalence classes
            of Lie algebra extensions of `\\mathfrak{g}` by `M`.

            INPUT:

            - ``deg`` -- the degree of the homology (optional)
            - ``M`` -- (default: the trivial module) a right module
              of ``self``
            - ``sparse`` -- boolean (default: ``True``); whether to use sparse
              matrices for the Chevalley-Eilenberg chain complex
            - ``ncpus`` -- (optional) how many cpus to use when
              computing the Chevalley-Eilenberg chain complex

            EXAMPLES::

                sage: # needs sage.combinat sage.modules
                sage: L = lie_algebras.so(QQ, 4)
                sage: L.cohomology()
                {0: Vector space of dimension 1 over Rational Field,
                 1: Vector space of dimension 0 over Rational Field,
                 2: Vector space of dimension 0 over Rational Field,
                 3: Vector space of dimension 2 over Rational Field,
                 4: Vector space of dimension 0 over Rational Field,
                 5: Vector space of dimension 0 over Rational Field,
                 6: Vector space of dimension 1 over Rational Field}

                sage: # needs sage.combinat sage.modules
                sage: L = lie_algebras.Heisenberg(QQ, 2)
                sage: L.cohomology()
                {0: Vector space of dimension 1 over Rational Field,
                 1: Vector space of dimension 4 over Rational Field,
                 2: Vector space of dimension 5 over Rational Field,
                 3: Vector space of dimension 5 over Rational Field,
                 4: Vector space of dimension 4 over Rational Field,
                 5: Vector space of dimension 1 over Rational Field}

                sage: # needs sage.combinat sage.modules
                sage: d = {('x', 'y'): {'y': 2}}
                sage: L.<x,y> = LieAlgebra(ZZ, d)
                sage: L.cohomology()
                {0: Z, 1: Z, 2: C2}

            .. SEEALSO::

                :meth:`chevalley_eilenberg_complex`

            REFERENCES:

            - :wikipedia:`Lie_algebra_cohomology`
            """
        def as_finite_dimensional_algebra(self):
            """
            Return ``self`` as a :class:`FiniteDimensionalAlgebra`.

            EXAMPLES::

                sage: # needs sage.combinat sage.modules
                sage: L = lie_algebras.cross_product(QQ)
                sage: x, y, z = L.basis()
                sage: F = L.as_finite_dimensional_algebra()
                sage: X, Y, Z = F.basis()
                sage: x.bracket(y)
                Z
                sage: X * Y
                Z
            """
        def morphism(self, on_generators, codomain=None, base_map=None, check: bool = True):
            """
            Return a Lie algebra morphism defined by images of a Lie
            generating subset of ``self``.

            INPUT:

            - ``on_generators`` -- dictionary ``{X: Y}`` of the images `Y`
              in ``codomain`` of elements `X` of ``domain``
            - ``codomain`` -- a Lie algebra (optional); this is inferred
              from the values of ``on_generators`` if not given
            - ``base_map`` -- a homomorphism from the base ring to something
              coercing into the codomain
            - ``check`` -- boolean (default: ``True``); if ``False`` the
              values  on the Lie brackets implied by ``on_generators`` will
              not be checked for contradictory values

            .. NOTE::

                The keys of ``on_generators`` need to generate ``domain``
                as a Lie algebra.

            .. SEEALSO::

                :class:`sage.algebras.lie_algebras.morphism.LieAlgebraMorphism_from_generators`

            EXAMPLES:

            A quotient type Lie algebra morphism ::

                sage: # needs sage.combinat sage.modules
                sage: L.<X,Y,Z,W> = LieAlgebra(QQ, {('X','Y'): {'Z': 1},
                ....:                               ('X','Z'): {'W': 1}})
                sage: K.<A,B> = LieAlgebra(QQ, abelian=True)
                sage: L.morphism({X: A, Y: B})
                Lie algebra morphism:
                  From: Lie algebra on 4 generators (X, Y, Z, W) over Rational Field
                  To:   Abelian Lie algebra on 2 generators (A, B) over Rational Field
                  Defn: X |--> A
                        Y |--> B
                        Z |--> 0
                        W |--> 0

            The reverse map `A \\mapsto X`, `B \\mapsto Y` does not define a Lie
            algebra morphism, since `[A,B] = 0`, but `[X,Y] \\neq 0`::

                sage: # needs sage.combinat sage.modules
                sage: K.morphism({A:X, B: Y})
                Traceback (most recent call last):
                ...
                ValueError: this does not define a Lie algebra morphism;
                 contradictory values for brackets of length 2

            However, it is still possible to create a morphism that acts nontrivially
            on the coefficients, even though it's not a Lie algebra morphism
            (since it isn't linear)::

                sage: # needs sage.combinat sage.modules sage.rings.number_fields
                sage: R.<x> = ZZ[]
                sage: K.<i> = NumberField(x^2 + 1)
                sage: cc = K.hom([-i])
                sage: L.<X,Y,Z,W> = LieAlgebra(K, {('X','Y'): {'Z': 1},
                ....:                              ('X','Z'): {'W': 1}})
                sage: M.<A,B> = LieAlgebra(K, abelian=True)
                sage: phi = L.morphism({X: A, Y: B}, base_map=cc)
                sage: phi(X)
                A
                sage: phi(i*X)
                -i*A
            """
        @cached_method
        def universal_polynomials(self):
            """
            Return the family of universal polynomials of ``self``.

            The *universal polynomials* of a Lie algebra `L` with
            basis `\\{e_i\\}_{i \\in I}` and structure coefficients
            `[e_i, e_j] = \\tau_{ij}^a e_a` is given by

            .. MATH::

                P_{aij} = \\sum_{u \\in I} \\tau_{ij}^u X_{au}
                - \\sum_{s,t \\in I} \\tau_{st}^a X_{si} X_{tj},

            where `a,i,j \\in I`.

            REFERENCES:

            - [AM2020]_

            EXAMPLES::

                sage: # needs sage.combinat sage.modules
                sage: L.<x,y> = LieAlgebra(QQ, {('x','y'): {'x':1}})
                sage: L.universal_polynomials()
                Finite family {('x', 'x', 'y'): X01*X10 - X00*X11 + X00,
                               ('y', 'x', 'y'): X10}

                sage: # needs sage.combinat sage.modules
                sage: L = LieAlgebra(QQ, cartan_type=['A',1])
                sage: list(L.universal_polynomials())
                [-2*X01*X10 + 2*X00*X11 - 2*X00,
                 -2*X02*X10 + 2*X00*X12 + X01,
                 -2*X02*X11 + 2*X01*X12 - 2*X02,
                 X01*X20 - X00*X21 - 2*X10,
                 X02*X20 - X00*X22 + X11,
                 X02*X21 - X01*X22 - 2*X12,
                 -2*X11*X20 + 2*X10*X21 - 2*X20,
                 -2*X12*X20 + 2*X10*X22 + X21,
                 -2*X12*X21 + 2*X11*X22 - 2*X22]

                sage: # long time, needs sage.combinat sage.modules
                sage: L = LieAlgebra(QQ, cartan_type=['B', 2])
                sage: al = RootSystem(['B', 2]).root_lattice().simple_roots()
                sage: k = list(L.basis().keys())[0]
                sage: UP = L.universal_polynomials()
                sage: len(UP)
                450
                sage: UP[al[2], al[1], -al[1]]
                X0_7*X4_1 - X0_1*X4_7 - 2*X0_7*X5_1 + 2*X0_1*X5_7 + X2_7*X7_1
                 - X2_1*X7_7 - X3_7*X8_1 + X3_1*X8_7 + X0_4
            """
        @cached_method
        def universal_commutative_algebra(self):
            """
            Return the universal commutative algebra associated to ``self``.

            Let `I` be the index set of the basis of ``self``. Let
            `\\mathcal{P} = \\{P_{a,i,j}\\}_{a,i,j \\in I}` denote the
            universal polynomials of a Lie algebra `L`. The *universal
            commutative algebra* associated to `L` is the quotient
            ring `R[X_{ij}]_{i,j \\in I} / (\\mathcal{P})`.

            EXAMPLES::

                sage: # needs sage.combinat sage.modules
                sage: L.<x,y> = LieAlgebra(QQ, {('x','y'): {'x':1}})
                sage: A = L.universal_commutative_algebra()
                sage: a, b, c, d = A.gens()
                sage: a, b, c, d
                (X00bar, X01bar, 0, X11bar)
                sage: a*d - a
                0
            """
        def casimir_element(self, order: int = 2, UEA=None, force_generic: bool = False, basis: bool = False):
            """
            Return a Casimir element of order ``order`` in the universal
            enveloping algebra of ``self``.

            A *Casimir element* of order `k` is a distinguished basis element
            for the center of `U(\\mathfrak{g})` of homogeneous degree `k`
            (that is, it is an element of `U_k \\setminus U_{k-1}`, where
            `\\{U_i\\}_{i=0}^{\\infty}` is the natural filtration of
            `U(\\mathfrak{g})`). When `\\mathfrak{g}` is a simple Lie algebra,
            then this spans `Z(U(\\mathfrak{g}))_k`.

            INPUT:

            - ``order`` -- (default: ``2``) the order of the Casimir element
            - ``UEA`` -- (optional) the universal enveloping algebra
              implementation to return the result in
            - ``force_generic`` -- boolean (default: ``False``); if ``True``
              for the quadratic order, then this uses the default algorithm
              (otherwise this is ignored)
            - ``basis`` -- boolean (default: ``False``); if ``True``, this
              returns a basis of all Casimir elements of order ``order`` as a
              list

            ALGORITHM:

            For the quadratic order (i.e., ``order=2``), then this uses
            `K^{ij}`, the inverse of the Killing form matrix, to compute
            `C_{(2)} = \\sum_{i,j} K^{ij} X_i \\cdots X_j`, where `\\{X_1, \\ldots,
            X_n\\}` is a basis for `\\mathfrak{g}`. Otherwise this solves the
            system of equations

            .. MATH::

                f_{aj}^b \\kappa^{jc\\cdots d} + f_{aj}^c \\kappa^{cj\\cdots d}
                \\cdots + f_{aj}^d \\kappa^{bc \\cdots j}

            for the symmetric tensor `\\kappa^{i_1 \\cdots i_k}`, where `k` is
            the ``order``. This system comes from `[X_i, C_{(k)}] = 0` with

            .. MATH::

                C_{(k)} = \\sum_{i_1, \\ldots, i_k}^n
                \\kappa^{i_1 \\cdots i_k} X_{i_1} \\cdots X_{i_k}.

            EXAMPLES::

                sage: # needs sage.combinat sage.modules
                sage: L = LieAlgebra(QQ, cartan_type=['A', 1])
                sage: C = L.casimir_element(); C
                1/8*b1^2 + 1/2*b0*b2 - 1/4*b1
                sage: U = L.universal_enveloping_algebra()
                sage: all(g * C == C * g for g in U.gens())
                True
                sage: U = L.pbw_basis()
                sage: C = L.casimir_element(UEA=U); C
                1/2*PBW[alpha[1]]*PBW[-alpha[1]] + 1/8*PBW[alphacheck[1]]^2
                 - 1/4*PBW[alphacheck[1]]
                sage: all(g * C == C * g for g in U.algebra_generators())
                True

                sage: # needs sage.combinat sage.modules
                sage: L = LieAlgebra(QQ, cartan_type=['B', 2])
                sage: U = L.pbw_basis()
                sage: C = L.casimir_element(UEA=U)
                sage: all(g * C == C * g for g in U.algebra_generators())
                True

                sage: # needs sage.combinat sage.modules
                sage: L = LieAlgebra(QQ, cartan_type=['C', 3])
                sage: U = L.pbw_basis()
                sage: C = L.casimir_element(UEA=U)
                sage: all(g * C == C * g for g in U.algebra_generators())
                True

                sage: # needs sage.combinat sage.modules
                sage: L = LieAlgebra(QQ, cartan_type=['A', 1])
                sage: C4 = L.casimir_element(order=4, UEA=L.pbw_basis()); C4
                4*PBW[alpha[1]]^2*PBW[-alpha[1]]^2
                 + 2*PBW[alpha[1]]*PBW[alphacheck[1]]^2*PBW[-alpha[1]]
                 + 1/4*PBW[alphacheck[1]]^4 - PBW[alphacheck[1]]^3
                 - 4*PBW[alpha[1]]*PBW[-alpha[1]] + 2*PBW[alphacheck[1]]
                sage: all(g * C4 == C4 * g for g in L.pbw_basis().algebra_generators())
                True

                sage: # needs sage.combinat sage.modules
                sage: L = lie_algebras.Heisenberg(QQ, 2)
                sage: L.casimir_element()
                0

                sage: # needs sage.combinat sage.modules
                sage: g = LieAlgebra(QQ, cartan_type=['D',2])
                sage: U = g.pbw_basis()
                sage: U.casimir_element(2, basis=True)
                [2*PBW[alpha[2]]*PBW[-alpha[2]] + 1/2*PBW[alphacheck[2]]^2 - PBW[alphacheck[2]],
                 2*PBW[alpha[1]]*PBW[-alpha[1]] + 1/2*PBW[alphacheck[1]]^2 - PBW[alphacheck[1]]]

            TESTS::

                sage: # needs sage.combinat sage.modules
                sage: L = LieAlgebra(QQ, cartan_type=['A', 1])
                sage: L.casimir_element(1)
                Traceback (most recent call last):
                ...
                ValueError: invalid order
                sage: 4 * L.casimir_element() == L.casimir_element(force_generic=True)
                True

            .. TODO::

                Use the symmetry of the tensor to reduce the number of
                equations and/or variables to solve.
            """
        def faithful_representation(self, algorithm=None):
            """
            Return a faithful representation of ``self``.

            By Ado's and Iwasawa's theorems, every finite dimensional
            Lie algebra has a faithful finite dimensional representation.

            INPUT:

            - ``algorithm`` -- one of the following depending on the
              classification of the Lie algebra:

              Nilpotent:

              * ``'regular'`` -- use the universal enveloping algebra quotient
                :class:`~sage.algebras.lie_algebras.representation.FaithfulRepresentationNilpotentPBW`
              * ``'minimal'`` -- construct the minimal representation (for
                precise details, see the documentation of
                :class:`~sage.algebras.lie_algebras.representation.FaithfulRepresentationNilpotentPBW`)

              Solvable:

              * Not implemented

              Semisimple:

              * Not implemented

              General case

              * ``'generic'`` -- generic algorithm (only implemented currently
                for positive characteristic)

            Note that the algorithm for any more generic cases can be used
            in the specialized cases. For instance, using ``'generic'`` for
            any Lie algebra (e.g., even if nilpotent) will use the generic
            implementation.

            EXAMPLES::

                sage: H2 = lie_algebras.Heisenberg(QQ, 2)
                sage: H2.is_nilpotent()
                True
                sage: F = H2.faithful_representation(); F
                Faithful 16 dimensional representation of
                 Heisenberg algebra of rank 2 over Rational Field
                sage: M = H2.faithful_representation(algorithm='minimal'); M
                Minimal faithful representation of
                 Heisenberg algebra of rank 2 over Rational Field
                sage: M.dimension()
                4
                sage: H2.faithful_representation(algorithm='invalid')
                Traceback (most recent call last):
                ...
                ValueError: invalid algorithm 'invalid'

                sage: scoeffs = {('a','d'): {'a':1}, ('a','e'): {'b':-1},
                ....:            ('b','d'): {'b':1}, ('b','e'): {'a':1},
                ....:            ('d','e'): {'c':1}}
                sage: L.<a,b,c,d,e> = LieAlgebra(QQ, scoeffs)
                sage: L.is_nilpotent()
                False
                sage: L.is_solvable()
                True
                sage: L.faithful_representation()
                Traceback (most recent call last):
                ...
                NotImplementedError: only implemented for nilpotent Lie algebras

                sage: sl3 = LieAlgebra(QQ, cartan_type=['A', 2])
                sage: sl3.is_semisimple()
                True
                sage: sl3.faithful_representation()
                Traceback (most recent call last):
                ...
                NotImplementedError: only implemented for nilpotent Lie algebras
            """
    class ElementMethods:
        def adjoint_matrix(self, sparse: bool = False):
            """
            Return the matrix of the adjoint action of ``self``.

            EXAMPLES::

                sage: # needs sage.combinat sage.modules
                sage: L = LieAlgebras(QQ).FiniteDimensional().WithBasis().example()
                sage: L.an_element().adjoint_matrix()
                [0 0 0]
                [0 0 0]
                [0 0 0]
                sage: L.an_element().adjoint_matrix(sparse=True).is_sparse()
                True

            ::

                sage: # needs sage.combinat sage.modules
                sage: L.<x,y> = LieAlgebra(QQ, {('x','y'): {'x':1}})
                sage: x.adjoint_matrix()
                [0 1]
                [0 0]
                sage: y.adjoint_matrix()
                [-1  0]
                [ 0  0]

            We verify that this forms a representation::

                sage: # needs sage.combinat sage.modules
                sage: sl3 = lie_algebras.sl(QQ, 3)
                sage: e1, e2 = sl3.e(1), sl3.e(2)
                sage: e12 = e1.bracket(e2)
                sage: E1, E2 = e1.adjoint_matrix(), e2.adjoint_matrix()
                sage: E1 * E2 - E2 * E1 == e12.adjoint_matrix()
                True

            TESTS::

                sage: scoeffs = {('a','d'): {'a':1}, ('a','e'): {'b':-1},
                ....:            ('b','d'): {'b':1}, ('b','e'): {'a':1},
                ....:            ('d','e'): {'c':1}}
                sage: L.<a,b,c,d,e> = LieAlgebra(QQ, scoeffs)
                sage: S = L.solvable_radical()
                sage: elt = S.derived_subalgebra().an_element()
                sage: elt.adjoint_matrix()
                [0 0 0]
                [0 0 0]
                [0 0 0]
            """
        def to_vector(self, sparse: bool = False, order=None):
            """
            Return the vector in ``g.module()`` corresponding to the
            element ``self`` of ``g`` (where ``g`` is the parent of
            ``self``).

            Implement this if you implement ``g.module()``.
            See :meth:`sage.categories.lie_algebras.LieAlgebras.module`
            for how this is to be done.

            EXAMPLES::

                sage: # needs sage.combinat sage.modules
                sage: L = LieAlgebras(QQ).FiniteDimensional().WithBasis().example()
                sage: L.an_element().to_vector()
                (0, 0, 0)
                sage: L.an_element().to_vector(sparse=True)
                (0, 0, 0)

                sage: # needs sage.combinat sage.groupssage.modules
                sage: D = DescentAlgebra(QQ, 4).D()
                sage: L = LieAlgebra(associative=D)
                sage: L.an_element().to_vector()
                (1, 1, 1, 1, 1, 1, 1, 1)

            TESTS:

            Check that the error raised agrees with the one
            from ``monomial_coefficients()`` (see :issue:`25007`)::

                sage: # needs sage.combinat sage.modules
                sage: L = lie_algebras.sp(QQ, 4, representation='matrix')
                sage: x = L.an_element()
                sage: x.monomial_coefficients()
                Traceback (most recent call last):
                ...
                NotImplementedError: the basis is not defined
                sage: x.to_vector()
                Traceback (most recent call last):
                ...
                NotImplementedError: the basis is not defined
            """
    class Subobjects(SubobjectsCategory):
        """
        A category for subalgebras of a finite dimensional Lie algebra
        with basis.
        """
        class ParentMethods:
            @abstract_method
            def ambient(self) -> None:
                """
                Return the ambient Lie algebra of ``self``.

                EXAMPLES::

                    sage: # needs sage.combinat sage.modules
                    sage: C = LieAlgebras(QQ).FiniteDimensional().WithBasis()
                    sage: L = C.example()
                    sage: a, b, c = L.lie_algebra_generators()
                    sage: S = L.subalgebra([2*a + b, b + c])
                    sage: S.ambient() == L
                    True
                """
            @abstract_method
            def basis_matrix(self) -> None:
                """
                Return the basis matrix of ``self``.

                EXAMPLES::

                    sage: # needs sage.combinat sage.modules
                    sage: C = LieAlgebras(QQ).FiniteDimensional().WithBasis()
                    sage: L = C.example()
                    sage: a, b, c = L.lie_algebra_generators()
                    sage: S = L.subalgebra([2*a + b, b + c])
                    sage: S.basis_matrix()
                    [   1    0 -1/2]
                    [   0    1    1]
                """
            def reduce(self, X):
                """
                Reduce an element of the ambient Lie algebra modulo the
                ideal ``self``.

                INPUT:

                - ``X`` -- an element of the ambient Lie algebra

                OUTPUT:

                An element `Y` of the ambient Lie algebra that is contained
                in a fixed complementary submodule `V` to ``self`` such that
                `X = Y` mod ``self``.

                When the base ring of ``self`` is a field, the complementary
                submodule `V` is spanned by the elements of the basis that
                are not the leading supports of the basis of ``self``.

                EXAMPLES:

                An example reduction in a 6 dimensional Lie algebra::

                    sage: sc = {('a','b'): {'d': 1}, ('a','c'): {'e': 1},
                    ....:       ('b','c'): {'f': 1}}
                    sage: L.<a,b,c,d,e,f> = LieAlgebra(QQ, sc)
                    sage: I = L.ideal(c)
                    sage: I.reduce(a + b + c + d + e + f)
                    a + b + d

                The reduction of an element is zero if and only if the
                element belongs to the subalgebra::

                    sage: I.reduce(c + e)
                    0
                    sage: c + e in I
                    True

                Over non-fields, the complementary submodule may not be spanned
                by a subset of the basis of the ambient Lie algebra::

                    sage: L.<X,Y,Z> = LieAlgebra(ZZ, {('X','Y'): {'Z': 3}})
                    sage: I = L.ideal(Y)
                    sage: I.basis()
                    Finite family {'Y': Y, 'Z': 3*Z}
                    sage: I.reduce(3*Z)
                    0
                    sage: I.reduce(Y + 14*Z)
                    2*Z

                We can reduce elements of a subalgebra `A` by an ideal `B`
                (:issue:`40137`)::

                    sage: L.<a,b,c,d> = LieAlgebra(QQ, {('a','b'): {'c': 1, 'd':1}, ('a','c'): {'b':1}})
                    sage: A = L.ideal([b, c, d])
                    sage: B = L.ideal([c+d])
                    sage: [B.reduce(v) for v in A.basis()]
                    [0, c, -c]
                    sage: A.basis()
                    Finite family {'b': b, 'c': c, 'd': d}
                    sage: B.basis()
                    Finite family {'b': b, 'd': c + d}
                    sage: all(B.reduce(v).parent() is A for v in A.basis())
                    True
                """
