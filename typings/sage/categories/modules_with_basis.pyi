from _typeshed import Incomplete
from sage.categories.cartesian_product import CartesianProductsCategory as CartesianProductsCategory
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring as CategoryWithAxiom_over_base_ring
from sage.categories.dual import DualObjectsCategory as DualObjectsCategory
from sage.categories.fields import Fields as Fields
from sage.categories.homsets import HomsetsCategory as HomsetsCategory
from sage.categories.map import Map as Map
from sage.categories.modules import Modules as Modules
from sage.categories.poor_man_map import PoorManMap as PoorManMap
from sage.categories.tensor import TensorProductsCategory as TensorProductsCategory, tensor as tensor
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.lazy_import import LazyImport as LazyImport, lazy_import as lazy_import
from sage.structure.element import Element as Element, parent as parent

class ModulesWithBasis(CategoryWithAxiom_over_base_ring):
    """
    The category of modules with a distinguished basis.

    The elements are represented by expanding them in the distinguished basis.
    The morphisms are not required to respect the distinguished basis.

    EXAMPLES::

        sage: ModulesWithBasis(ZZ)
        Category of modules with basis over Integer Ring
        sage: ModulesWithBasis(ZZ).super_categories()
        [Category of modules over Integer Ring]

    If the base ring is actually a field, this constructs instead the
    category of vector spaces with basis::

        sage: ModulesWithBasis(QQ)
        Category of vector spaces with basis over Rational Field

        sage: ModulesWithBasis(QQ).super_categories()
        [Category of modules with basis over Rational Field,
         Category of vector spaces over Rational Field]

    Let `X` and `Y` be two modules with basis. We can build `Hom(X,Y)`::

        sage: X = CombinatorialFreeModule(QQ, [1,2]); X.rename('X')                     # needs sage.modules
        sage: Y = CombinatorialFreeModule(QQ, [3,4]); Y.rename('Y')                     # needs sage.modules
        sage: H = Hom(X, Y); H                                                          # needs sage.modules
        Set of Morphisms from X to Y
         in Category of finite dimensional vector spaces with basis over Rational Field

    The simplest morphism is the zero map::

        sage: H.zero()     # todo: move this test into module once we have an example   # needs sage.modules
        Generic morphism:
          From: X
          To:   Y

    which we can apply to elements of `X`::

        sage: x = X.monomial(1) + 3 * X.monomial(2)                                     # needs sage.modules
        sage: H.zero()(x)                                                               # needs sage.modules
        0

    EXAMPLES:

    We now construct a more interesting morphism by extending a
    function by linearity::

        sage: phi = H(on_basis=lambda i: Y.monomial(i + 2)); phi                        # needs sage.modules
        Generic morphism:
          From: X
          To:   Y
        sage: phi(x)                                                                    # needs sage.modules
        B[3] + 3*B[4]

    We can retrieve the function acting on indices of the basis::

        sage: f = phi.on_basis()                                                        # needs sage.modules
        sage: f(1), f(2)                                                                # needs sage.modules
        (B[3], B[4])

    `Hom(X,Y)` has a natural module structure (except for the zero,
    the operations are not yet implemented though). However since the
    dimension is not necessarily finite, it is not a module with
    basis; but see :class:`FiniteDimensionalModulesWithBasis` and
    :class:`GradedModulesWithBasis`::

        sage: H in ModulesWithBasis(QQ), H in Modules(QQ)                               # needs sage.modules
        (False, True)

    Some more playing around with categories and higher order homsets::

        sage: H.category()                                                              # needs sage.modules
        Category of homsets of finite dimensional modules with basis over Rational Field
        sage: Hom(H, H).category()                                                      # needs sage.modules
        Category of endsets of
         homsets of finite dimensional modules with basis over Rational Field

    .. TODO:: ``End(X)`` is an algebra.

    .. NOTE::

        This category currently requires an implementation of an
        element method ``support``. Once :issue:`18066` is merged, an
        implementation of an ``items`` method will be required.

    TESTS::

        sage: f = H.zero().on_basis()                                                   # needs sage.modules
        sage: f(1)                                                                      # needs sage.modules
        0
        sage: f(2)                                                                      # needs sage.modules
        0

        sage: TestSuite(ModulesWithBasis(ZZ)).run()
    """
    def is_abelian(self):
        """
        Return whether this category is abelian.

        This is the case if and only if the base ring is a field.

        EXAMPLES::

            sage: ModulesWithBasis(QQ).is_abelian()
            True
            sage: ModulesWithBasis(ZZ).is_abelian()
            False
        """
    FiniteDimensional: Incomplete
    Filtered: Incomplete
    Graded: Incomplete
    Super: Incomplete
    class ParentMethods:
        @cached_method
        def basis(self):
            """
            Return the basis of ``self``.

            EXAMPLES::

                sage: F = CombinatorialFreeModule(QQ, ['a', 'b', 'c'])                  # needs sage.modules
                sage: F.basis()                                                         # needs sage.modules
                Finite family {'a': B['a'], 'b': B['b'], 'c': B['c']}

            ::

                sage: QS3 = SymmetricGroupAlgebra(QQ, 3)                                # needs sage.combinat sage.groups sage.modules
                sage: list(QS3.basis())                                                 # needs sage.combinat sage.groups sage.modules
                [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
            """
        def module_morphism(self, on_basis=None, matrix=None, function=None, diagonal=None, triangular=None, unitriangular: bool = False, **keywords):
            '''
            Construct a module morphism from ``self`` to ``codomain``.

            Let ``self`` be a module `X` with a basis indexed by `I`.
            This constructs a morphism `f: X \\to Y` by linearity from
            a map `I \\to Y` which is to be its restriction to the
            basis `(x_i)_{i \\in I}` of `X`. Some variants are possible
            too.

            INPUT:

            - ``self`` -- a parent `X` in ``ModulesWithBasis(R)`` with
              basis `x=(x_i)_{i\\in I}`

            Exactly one of the four following options must be
            specified in order to define the morphism:

            - ``on_basis`` -- a function `f` from `I` to `Y`
            - ``diagonal`` -- a function `d` from `I` to `R`
            - ``function`` -- a function `f` from `X` to `Y`
            - ``matrix`` -- a matrix of size `\\dim Y \\times \\dim X`
              (if the keyword ``side`` is set to ``\'left\'``) or
              `\\dim Y \\times \\dim X` (if this keyword is ``\'right\'``)

            Further options include:

            - ``codomain`` -- the codomain `Y` of the morphism (default:
              ``f.codomain()`` if it\'s defined; otherwise it must be specified)

            - ``category`` -- a category or ``None`` (default: ``None``)

            - ``zero`` -- the zero of the codomain (default: ``codomain.zero()``);
              can be used (with care) to define affine maps.
              Only meaningful with ``on_basis``.

            - ``position`` -- nonnegative integer specifying which
              positional argument is used as the input of the function `f`
              (default: 0); this is currently only used with ``on_basis``.

            - ``triangular`` -- (default: ``None``) ``\'upper\'`` or
              ``\'lower\'`` or ``None``:

              * ``\'upper\'`` -- if the
                :meth:`~ModulesWithBasis.ElementMethods.leading_support`
                of the image of the basis vector `x_i` is `i`, or

              * ``\'lower\'`` -- if the
                :meth:`~ModulesWithBasis.ElementMethods.trailing_support`
                of the image of the basis vector `x_i` is `i`.

            - ``unitriangular`` -- boolean (default: ``False``);
              only meaningful for a triangular morphism.
              As a shorthand, one may use ``unitriangular="lower"``
              for ``triangular=\'lower\', unitriangular=True``.

            - ``side`` -- ``\'left\'`` or ``\'right\'`` (default: ``\'left\'``);
              only meaningful for a morphism built from a matrix

            EXAMPLES:

            With the ``on_basis`` option, this returns a function `g`
            obtained by extending `f` by linearity on the
            ``position``-th positional argument. For example, for
            ``position == 1`` and a ternary function `f`, one has:

            .. MATH::

                g\\left( a,\\ \\sum_i \\lambda_i x_i,\\ c \\right)
                = \\sum_i \\lambda_i f(a, i, c).

            ::

                sage: # needs sage.modules
                sage: X = CombinatorialFreeModule(QQ, [1,2,3]);   X.rename(\'X\')
                sage: Y = CombinatorialFreeModule(QQ, [1,2,3,4]); Y.rename(\'Y\')
                sage: def f(i):
                ....:     return Y.monomial(i) + 2*Y.monomial(i+1)
                sage: phi = X.module_morphism(f, codomain=Y)
                sage: x = X.basis(); y = Y.basis()
                sage: phi(x[1] + x[3])
                B[1] + 2*B[2] + B[3] + 2*B[4]
                sage: phi
                Generic morphism:
                From: X
                To:   Y

            By default, the category is the first of
            ``Modules(R).WithBasis().FiniteDimensional()``,
            ``Modules(R).WithBasis()``, ``Modules(R)``, and
            ``CommutativeAdditiveMonoids()`` that contains both the
            domain and the codomain::

                sage: phi.category_for()                                                # needs sage.modules
                Category of finite dimensional vector spaces with basis
                 over Rational Field

            With the ``zero`` argument, one can define affine morphisms::

                sage: def f(i):
                ....:     return Y.monomial(i) + 2*Y.monomial(i+1)
                sage: phi = X.module_morphism(f, codomain=Y, zero=10*y[1])              # needs sage.modules
                sage: phi(x[1] + x[3])                                                  # needs sage.modules
                11*B[1] + 2*B[2] + B[3] + 2*B[4]

            In this special case, the default category is ``Sets()``::

                sage: phi.category_for()                                                # needs sage.modules
                Category of sets

            One can construct morphisms with the base ring as codomain::

                sage: # needs sage.modules
                sage: X = CombinatorialFreeModule(ZZ, [1, -1])
                sage: phi = X.module_morphism(on_basis=lambda i: i, codomain=ZZ)
                sage: phi(2 * X.monomial(1) + 3 * X.monomial(-1))
                -1
                sage: phi.category_for()
                Category of commutative additive semigroups
                sage: phi.category_for()        # not implemented
                Category of modules over Integer Ring

            Or more generally any ring admitting a coercion map from
            the base ring::

                sage: # needs sage.modules
                sage: phi = X.module_morphism(on_basis=lambda i: i, codomain=RR)
                sage: phi(2 * X.monomial(1) + 3 * X.monomial(-1))
                -1.00000000000000
                sage: phi.category_for()
                Category of commutative additive semigroups
                sage: phi.category_for()        # not implemented
                Category of modules over Integer Ring

                sage: phi = X.module_morphism(on_basis=lambda i: i, codomain=Zmod(4))   # needs sage.modules
                sage: phi(2 * X.monomial(1) + 3 * X.monomial(-1))                       # needs sage.modules
                3

                sage: phi = Y.module_morphism(on_basis=lambda i: i, codomain=Zmod(4))   # needs sage.modules
                Traceback (most recent call last):
                ...
                ValueError: codomain(=Ring of integers modulo 4) should be a module
                over the base ring of the domain(=Y)

            On can also define module morphisms between free modules
            over different base rings; here we implement the natural
            map from `X = \\RR^2` to `Y = \\CC`::

                sage: # needs sage.modules
                sage: X = CombinatorialFreeModule(RR, [\'x\', \'y\'])
                sage: Y = CombinatorialFreeModule(CC, [\'z\'])
                sage: x = X.monomial(\'x\')
                sage: y = X.monomial(\'y\')
                sage: z = Y.monomial(\'z\')
                sage: def on_basis(a):
                ....:     if a == \'x\':
                ....:         return CC(1) * z
                ....:     elif a == \'y\':
                ....:         return CC(I) * z
                sage: phi = X.module_morphism(on_basis=on_basis, codomain=Y)
                sage: v = 3 * x + 2 * y; v
                3.00000000000000*B[\'x\'] + 2.00000000000000*B[\'y\']
                sage: phi(v)                                                            # needs sage.symbolic
                (3.00000000000000+2.00000000000000*I)*B[\'z\']
                sage: phi.category_for()
                Category of commutative additive semigroups
                sage: phi.category_for()        # not implemented
                Category of vector spaces over Real Field with 53 bits of precision

                sage: # needs sage.modules
                sage: Y = CombinatorialFreeModule(CC[\'q\'], [\'z\'])
                sage: z = Y.monomial(\'z\')
                sage: phi = X.module_morphism(on_basis=on_basis, codomain=Y)
                sage: phi(v)                                                            # needs sage.symbolic
                (3.00000000000000+2.00000000000000*I)*B[\'z\']

            Of course, there should be a coercion between the
            respective base rings of the domain and the codomain for
            this to be meaningful::

                sage: Y = CombinatorialFreeModule(QQ, [\'z\'])                            # needs sage.modules
                sage: phi = X.module_morphism(on_basis=on_basis, codomain=Y)            # needs sage.modules
                Traceback (most recent call last):
                ...
                ValueError: codomain(=Free module generated by {\'z\'} over Rational Field)
                should be a module over the base ring of the domain(=Free module
                generated by {\'x\', \'y\'} over Real Field with 53 bits of precision)

                sage: Y = CombinatorialFreeModule(RR[\'q\'], [\'z\'])                       # needs sage.modules
                sage: phi = Y.module_morphism(on_basis=on_basis, codomain=X)            # needs sage.modules
                Traceback (most recent call last):
                ...
                ValueError: codomain(=Free module generated by {\'x\', \'y\'}
                over Real Field with 53 bits of precision) should be a module over
                the base ring of the domain(=Free module generated by {\'z\'} over
                Univariate Polynomial Ring in q over Real Field with 53 bits of precision)


            With the ``diagonal=d`` argument, this constructs the
            module morphism `g` such that

            .. MATH::

                `g(x_i) = d(i) y_i`.

            This assumes that the respective bases `x` and `y` of `X`
            and `Y` have the same index set `I`::

                sage: # needs sage.modules
                sage: X = CombinatorialFreeModule(ZZ, [1, 2, 3]); X.rename(\'X\')
                sage: from sage.arith.misc import factorial
                sage: phi = X.module_morphism(diagonal=factorial, codomain=X)
                sage: x = X.basis()
                sage: phi(x[1]), phi(x[2]), phi(x[3])
                (B[1], 2*B[2], 6*B[3])

            See also: :class:`sage.modules.with_basis.morphism.DiagonalModuleMorphism`.

            With the ``matrix=m`` argument, this constructs the module
            morphism whose matrix in the distinguished basis of `X`
            and `Y` is `m`::

                sage: # needs sage.modules
                sage: X = CombinatorialFreeModule(ZZ, [1,2,3]); X.rename(\'X\')
                sage: x = X.basis()
                sage: Y = CombinatorialFreeModule(ZZ, [3,4]); Y.rename(\'Y\')
                sage: y = Y.basis()
                sage: m = matrix([[0,1,2], [3,5,0]])
                sage: phi = X.module_morphism(matrix=m, codomain=Y)
                sage: phi(x[1])
                3*B[4]
                sage: phi(x[2])
                B[3] + 5*B[4]


            See also: :class:`sage.modules.with_basis.morphism.ModuleMorphismFromMatrix`.

            With ``triangular="upper"``, the constructed module morphism is
            assumed to be upper triangular; that is its matrix in the
            distinguished basis of `X` and `Y` would be upper triangular with
            invertible elements on its diagonal. This is used to compute
            preimages and to invert the morphism::

                sage: # needs sage.modules
                sage: I = list(range(1, 200))
                sage: X = CombinatorialFreeModule(QQ, I); X.rename(\'X\'); x = X.basis()
                sage: Y = CombinatorialFreeModule(QQ, I); Y.rename(\'Y\'); y = Y.basis()
                sage: f = Y.sum_of_monomials * divisors
                sage: phi = X.module_morphism(f, triangular=\'upper\', codomain=Y)
                sage: phi(x[2])
                B[1] + B[2]
                sage: phi(x[6])
                B[1] + B[2] + B[3] + B[6]
                sage: phi(x[30])
                B[1] + B[2] + B[3] + B[5] + B[6] + B[10] + B[15] + B[30]
                sage: phi.preimage(y[2])
                -B[1] + B[2]
                sage: phi.preimage(y[6])
                B[1] - B[2] - B[3] + B[6]
                sage: phi.preimage(y[30])
                -B[1] + B[2] + B[3] + B[5] - B[6] - B[10] - B[15] + B[30]
                sage: (phi^-1)(y[30])
                -B[1] + B[2] + B[3] + B[5] - B[6] - B[10] - B[15] + B[30]

            Since :issue:`8678`, one can also define a triangular
            morphism from a function::

                sage: # needs sage.modules
                sage: X = CombinatorialFreeModule(QQ, [0,1,2,3,4]); x = X.basis()
                sage: from sage.modules.with_basis.morphism import TriangularModuleMorphismFromFunction
                sage: def f(x): return x + X.term(0, sum(x.coefficients()))
                sage: phi = X.module_morphism(function=f, codomain=X,
                ....:                         triangular=\'upper\')
                sage: phi(x[2] + 3*x[4])
                4*B[0] + B[2] + 3*B[4]
                sage: phi.preimage(_)
                B[2] + 3*B[4]

            For details and further optional arguments, see
            :class:`sage.modules.with_basis.morphism.TriangularModuleMorphism`.

            .. WARNING::

                As a temporary measure, until multivariate morphisms
                are implemented, the constructed morphism is in
                ``Hom(codomain, domain, category)``. This is only
                correct for unary functions.

            .. TODO::

               - Should codomain be ``self`` by default in the
                 diagonal, triangular, and matrix cases?

               - Support for diagonal morphisms between modules not
                 sharing the same index set

            TESTS::

                sage: X = CombinatorialFreeModule(ZZ, [1,2,3]); X.rename(\'X\')           # needs sage.modules
                sage: phi = X.module_morphism(codomain=X)                               # needs sage.modules
                Traceback (most recent call last):
                ...
                ValueError: module_morphism() takes exactly one option
                out of `matrix`, `on_basis`, `function`, `diagonal`

            ::

                sage: X = CombinatorialFreeModule(ZZ, [1,2,3]); X.rename(\'X\')           # needs sage.modules
                sage: phi = X.module_morphism(diagonal=factorial, matrix=matrix(),      # needs sage.modules
                ....:                         codomain=X)
                Traceback (most recent call last):
                ...
                ValueError: module_morphism() takes exactly one option
                out of `matrix`, `on_basis`, `function`, `diagonal`

            ::

                sage: X = CombinatorialFreeModule(ZZ, [1,2,3]); X.rename(\'X\')           # needs sage.modules
                sage: phi = X.module_morphism(matrix=factorial, codomain=X)             # needs sage.modules
                Traceback (most recent call last):
                ...
                ValueError: matrix (=...factorial...) should be a matrix

            ::

                sage: X = CombinatorialFreeModule(ZZ, [1,2,3]); X.rename(\'X\')           # needs sage.modules
                sage: phi = X.module_morphism(diagonal=3, codomain=X)                   # needs sage.modules
                Traceback (most recent call last):
                ...
                ValueError: diagonal (=3) should be a function
            '''
        def echelon_form(self, elements, row_reduced: bool = False, order=None):
            """
            Return a basis in echelon form of the subspace spanned by
            a finite set of elements.

            INPUT:

            - ``elements`` -- list or finite iterable of elements of ``self``
            - ``row_reduced`` -- boolean (default: ``False``); whether to
              compute the basis for the row reduced echelon form
            - ``order`` -- (optional) either something that can
              be converted into a tuple or a key function

            OUTPUT:

            A list of elements of ``self`` whose expressions as vectors
            form a matrix in echelon form. If ``base_ring`` is specified,
            then the calculation is achieved in this base ring.

            EXAMPLES::

                sage: R.<x,y> = QQ[]
                sage: C = CombinatorialFreeModule(R, ZZ, prefix='z')                    # needs sage.modules
                sage: z = C.basis()                                                     # needs sage.modules
                sage: C.echelon_form([z[0] - z[1], 2*z[1] - 2*z[2], z[0] - z[2]])       # needs sage.libs.singular sage.modules
                [z[0] - z[2], z[1] - z[2]]

            TESTS:

            We convert the input elements to ``self``::

                sage: s = SymmetricFunctions(QQ).s()                                    # needs sage.combinat sage.modules
                sage: s.echelon_form([1, s[1] + 5])                                     # needs sage.combinat sage.modules
                [s[], s[1]]
            """
        def submodule(self, gens, check: bool = True, already_echelonized: bool = False, unitriangular: bool = False, support_order=None, category=None, submodule_class=None, *args, **opts):
            """
            The submodule spanned by a finite set of elements.

            INPUT:

            - ``gens`` -- list or family of elements of ``self``
            - ``check`` -- boolean (default: ``True``); whether to verify that
              the elements of ``gens`` are in ``self``
            - ``already_echelonized`` -- boolean (default: ``False``); whether
               the elements of ``gens`` are already in (not necessarily
               reduced) echelon form
            - ``unitriangular`` -- boolean (default: ``False``); whether
              the lift morphism is unitriangular
            - ``support_order`` -- (optional) either something that can
              be converted into a tuple or a key function
            - ``category`` -- (optional) the category of the submodule
            - ``submodule_class`` -- (optional) the class of the submodule
              to return

            If ``already_echelonized`` is ``False``, then the
            generators are put in reduced echelon form using
            :meth:`echelonize`, and reindexed by `0,1,...`.

            .. WARNING::

                At this point, this method only works for finite
                dimensional submodules and if matrices can be
                echelonized over the base ring.

            If in addition ``unitriangular`` is ``True``, then
            the generators are made such that the coefficients of
            the pivots are 1, so that lifting map is unitriangular.

            The basis of the submodule uses the same index set as the
            generators, and the lifting map sends `y_i` to `gens[i]`.

            .. SEEALSO::

                 - :meth:`ModulesWithBasis.FiniteDimensional.ParentMethods.quotient_module`
                 - :class:`sage.modules.with_basis.subquotient.SubmoduleWithBasis`

            EXAMPLES:

            We construct a submodule of the free `\\QQ`-module generated by
            `x_0, x_1, x_2`. The submodule is spanned by `y_0 = x_0 - x_1` and
            `y_1 - x_1 - x_2`, and its basis elements are indexed by `0` and `1`::

                sage: # needs sage.modules
                sage: X = CombinatorialFreeModule(QQ, range(3), prefix='x')
                sage: x = X.basis()
                sage: gens = [x[0] - x[1], x[1] - x[2]]; gens
                [x[0] - x[1], x[1] - x[2]]
                sage: Y = X.submodule(gens, already_echelonized=True)
                sage: Y.print_options(prefix='y'); Y
                Free module generated by {0, 1} over Rational Field
                sage: y = Y.basis()
                sage: y[1]
                y[1]
                sage: y[1].lift()
                x[1] - x[2]
                sage: Y.retract(x[0] - x[2])
                y[0] + y[1]
                sage: Y.retract(x[0])
                Traceback (most recent call last):
                ...
                ValueError: x[0] is not in the image

            By using a family to specify a basis of the submodule, we obtain a
            submodule whose index set coincides with the index set of the family::

                sage: # needs sage.modules
                sage: X = CombinatorialFreeModule(QQ, range(3), prefix='x')
                sage: x = X.basis()
                sage: gens = Family({1: x[0] - x[1], 3: x[1] - x[2]}); gens
                Finite family {1: x[0] - x[1], 3: x[1] - x[2]}
                sage: Y = X.submodule(gens, already_echelonized=True)
                sage: Y.print_options(prefix='y'); Y
                Free module generated by {1, 3} over Rational Field
                sage: y = Y.basis()
                sage: y[1]
                y[1]
                sage: y[1].lift()
                x[0] - x[1]
                sage: y[3].lift()
                x[1] - x[2]
                sage: Y.retract(x[0] - x[2])
                y[1] + y[3]
                sage: Y.retract(x[0])
                Traceback (most recent call last):
                ...
                ValueError: x[0] is not in the image

            It is not necessary that the generators of the submodule form
            a basis (an explicit basis will be computed)::

                sage: # needs sage.modules
                sage: X = CombinatorialFreeModule(QQ, range(3), prefix='x')
                sage: x = X.basis()
                sage: gens = [x[0] - x[1], 2*x[1] - 2*x[2], x[0] - x[2]]; gens
                [x[0] - x[1], 2*x[1] - 2*x[2], x[0] - x[2]]
                sage: Y = X.submodule(gens, already_echelonized=False)
                sage: Y.print_options(prefix='y')
                sage: Y
                Free module generated by {0, 1} over Rational Field
                sage: [b.lift() for b in Y.basis()]
                [x[0] - x[2], x[1] - x[2]]

            We now implement by hand the center of the algebra of the
            symmetric group `S_3`::

                sage: # needs sage.combinat sage.groups sage.modules
                sage: S3 = SymmetricGroup(3)
                sage: S3A = S3.algebra(QQ)
                sage: basis = S3A.annihilator_basis(S3A.algebra_generators(),
                ....:                               S3A.bracket)
                sage: basis
                ((), (1,2,3) + (1,3,2), (2,3) + (1,2) + (1,3))
                sage: center = S3A.submodule(basis,
                ....:     category=AlgebrasWithBasis(QQ).Subobjects(),
                ....:     already_echelonized=True)
                sage: center
                Free module generated by {0, 1, 2} over Rational Field
                sage: center in Algebras
                True
                sage: center.print_options(prefix='c')
                sage: c = center.basis()
                sage: c[1].lift()
                (1,2,3) + (1,3,2)
                sage: c[0]^2
                c[0]
                sage: e = 1/6 * (c[0]+c[1]+c[2])
                sage: e.is_idempotent()
                True

            Of course, this center is best constructed using::

                sage: center = S3A.center()                                             # needs sage.combinat sage.groups sage.modules

            We can also automatically construct a basis such that
            the lift morphism is (lower) unitriangular::

                sage: # needs sage.modules
                sage: R.<a,b> = QQ[]
                sage: C = CombinatorialFreeModule(R, range(3), prefix='x')
                sage: x = C.basis()
                sage: gens = [x[0] - x[1], 2*x[1] - 2*x[2], x[0] - x[2]]
                sage: Y = C.submodule(gens, unitriangular=True)
                sage: Y.lift.matrix()
                [ 1  0]
                [ 0  1]
                [-1 -1]

            We now construct a (finite-dimensional) submodule of an
            infinite dimensional free module::

                sage: # needs sage.modules
                sage: C = CombinatorialFreeModule(QQ, ZZ, prefix='z')
                sage: z = C.basis()
                sage: gens = [z[0] - z[1], 2*z[1] - 2*z[2], z[0] - z[2]]
                sage: Y = C.submodule(gens)
                sage: [Y.lift(b) for b in Y.basis()]
                [z[0] - z[2], z[1] - z[2]]

            TESTS::

                sage: TestSuite(Y).run()                                                # needs sage.modules
                sage: TestSuite(center).run()                                           # needs sage.combinat sage.groups sage.modules
            """
        def quotient_module(self, submodule, check: bool = True, already_echelonized: bool = False, category=None):
            """
            Construct the quotient module ``self`` / ``submodule``.

            INPUT:

            - ``submodule`` -- a submodule with basis of ``self``, or
              something that can be turned into one via
              ``self.submodule(submodule)``

            - ``check``, ``already_echelonized`` -- passed down to
              :meth:`ModulesWithBasis.ParentMethods.submodule`

            .. WARNING::

                At this point, this only supports quotients by free
                submodules admitting a basis in unitriangular echelon
                form. In this case, the quotient is also a free
                module, with a basis consisting of the retract of a
                subset of the basis of ``self``.

            EXAMPLES::

                sage: # needs sage.modules
                sage: X = CombinatorialFreeModule(QQ, range(3), prefix='x')
                sage: x = X.basis()
                sage: Y = X.quotient_module([x[0] - x[1], x[1] - x[2]],
                ....:                       already_echelonized=True)
                sage: Y.print_options(prefix='y'); Y
                Free module generated by {2} over Rational Field
                sage: y = Y.basis()
                sage: y[2]
                y[2]
                sage: y[2].lift()
                x[2]
                sage: Y.retract(x[0] + 2*x[1])
                3*y[2]

                sage: # needs sage.modules
                sage: R.<a,b> = QQ[]
                sage: C = CombinatorialFreeModule(R, range(3), prefix='x')
                sage: x = C.basis()
                sage: gens = [x[0] - x[1], 2*x[1] - 2*x[2], x[0] - x[2]]
                sage: Y = C.quotient_module(gens)

            .. SEEALSO::

                 - :meth:`Modules.WithBasis.ParentMethods.submodule`
                 - :meth:`Rings.ParentMethods.quotient`
                 - :class:`sage.modules.with_basis.subquotient.QuotientModuleWithBasis`
            """
        def tensor(*parents, **kwargs):
            """
            Return the tensor product of the parents.

            EXAMPLES::

                sage: C = AlgebrasWithBasis(QQ)
                sage: A = C.example(); A.rename('A')                                    # needs sage.combinat sage.modules
                sage: A.tensor(A, A)                                                    # needs sage.combinat sage.modules
                A # A # A
                sage: A.rename(None)                                                    # needs sage.combinat sage.modules
            """
        def intersection(self, other):
            """
            Return the intersection of ``self`` with ``other``.

            EXAMPLES::

                sage: X = CombinatorialFreeModule(QQ, range(4)); x = X.basis()
                sage: U = X.submodule([x[0]-x[1], x[1]-x[2], x[2]-x[3]])
                sage: F = CombinatorialFreeModule(QQ, ['a','b','c','d'])
                sage: G = F.submodule([F.basis()['a']])
                sage: X.intersection(X) is X
                True
                sage: X.intersection(U) is U
                True
                sage: X.intersection(F)
                Traceback (most recent call last):
                ...
                TypeError: other must be a submodule
                sage: X.intersection(G)
                Traceback (most recent call last):
                ...
                ArithmeticError: this module must be the ambient
            """
        def cardinality(self):
            """
            Return the cardinality of ``self``.

            EXAMPLES::

                sage: # needs sage.groups sage.modules
                sage: S = SymmetricGroupAlgebra(QQ, 4)
                sage: S.cardinality()
                +Infinity
                sage: S = SymmetricGroupAlgebra(GF(2), 4)
                sage: S.cardinality()
                16777216
                sage: S.cardinality().factor()
                2^24

                sage: # needs sage.modules
                sage: E.<x,y> = ExteriorAlgebra(QQ)
                sage: E.cardinality()
                +Infinity
                sage: E.<x,y> = ExteriorAlgebra(GF(3))
                sage: E.cardinality()
                81

                sage: s = SymmetricFunctions(GF(2)).s()                                 # needs sage.combinat sage.modules
                sage: s.cardinality()                                                   # needs sage.combinat sage.modules
                +Infinity

                sage: M = CombinatorialFreeModule(QQ, [])
                sage: M.dimension()
                0
                sage: M.cardinality()
                1
            """
        def is_finite(self):
            """
            Return whether ``self`` is finite.

            This is true if and only if ``self.basis().keys()`` and
            ``self.base_ring()`` are both finite.

            EXAMPLES::

                sage: GroupAlgebra(SymmetricGroup(2), IntegerModRing(10)).is_finite()   # needs sage.combinat sage.groups sage.modules
                True
                sage: GroupAlgebra(SymmetricGroup(2)).is_finite()                       # needs sage.combinat sage.groups sage.modules
                False
                sage: GroupAlgebra(AbelianGroup(1), IntegerModRing(10)).is_finite()     # needs sage.groups sage.modules
                False
            """
        def monomial(self, i):
            """
            Return the basis element indexed by ``i``.

            INPUT:

            - ``i`` -- an element of the index set

            EXAMPLES::

                sage: F = CombinatorialFreeModule(QQ, ['a', 'b', 'c'])                  # needs sage.modules
                sage: F.monomial('a')                                                   # needs sage.modules
                B['a']

            ``F.monomial`` is in fact (almost) a map::

                sage: F.monomial                                                        # needs sage.modules
                Term map from {'a', 'b', 'c'}
                 to Free module generated by {'a', 'b', 'c'} over Rational Field
            """
        @lazy_attribute
        def sum_of_monomials(self):
            """
            Return the sum of the basis elements with indices in
            ``indices``.

            INPUT:

            - ``indices`` -- list (or iterable) of indices of basis
              elements

            EXAMPLES::

                sage: F = CombinatorialFreeModule(QQ, ['a', 'b', 'c'])                  # needs sage.modules
                sage: F.sum_of_monomials(['a', 'b'])                                    # needs sage.modules
                B['a'] + B['b']

                sage: F.sum_of_monomials(['a', 'b', 'a'])                               # needs sage.modules
                2*B['a'] + B['b']

            ``F.sum_of_monomials`` is in fact (almost) a map::

                sage: F.sum_of_monomials                                                # needs sage.modules
                A map to Free module generated by {'a', 'b', 'c'} over Rational Field
            """
        def monomial_or_zero_if_none(self, i):
            """
            EXAMPLES::

                sage: F = CombinatorialFreeModule(QQ, ['a', 'b', 'c'])                  # needs sage.modules
                sage: F.monomial_or_zero_if_none('a')                                   # needs sage.modules
                B['a']
                sage: F.monomial_or_zero_if_none(None)                                  # needs sage.modules
                0
            """
        def term(self, index, coeff=None):
            """
            Construct a term in ``self``.

            INPUT:

            - ``index`` -- the index of a basis element
            - ``coeff`` -- an element of the coefficient ring (default: one)

            OUTPUT: ``coeff * B[index]``, where ``B`` is the basis of ``self``

            EXAMPLES::

                sage: m = matrix([[0,1], [1,1]])                                        # needs sage.modules
                sage: J.<a,b,c> = JordanAlgebra(m)                                      # needs sage.combinat sage.modules
                sage: J.term(1, -2)                                                     # needs sage.combinat sage.modules
                0 + (-2, 0)

            Design: should this do coercion on the coefficient ring?
            """
        def sum_of_terms(self, terms):
            """
            Construct a sum of terms of ``self``.

            INPUT:

            - ``terms`` -- list (or iterable) of pairs ``(index, coeff)``

            OUTPUT:

            Sum of ``coeff * B[index]`` over all ``(index, coeff)`` in
            ``terms``, where ``B`` is the basis of ``self``.

            EXAMPLES::

                sage: m = matrix([[0,1], [1,1]])                                        # needs sage.modules
                sage: J.<a,b,c> = JordanAlgebra(m)                                      # needs sage.combinat sage.modules
                sage: J.sum_of_terms([(0, 2), (2, -3)])                                 # needs sage.combinat sage.modules
                2 + (0, -3)
            """
        def dimension(self):
            """
            Return the dimension of ``self``.

            EXAMPLES::

                sage: A.<x,y> = algebras.DifferentialWeyl(QQ)                           # needs sage.modules
                sage: A.dimension()                                                     # needs sage.modules
                +Infinity
            """
        def rank(self):
            """
            Return the rank of ``self``.

            Since there is a (distinguished) basis, the rank of ``self``
            is equal to the cardinality of the basis (which equals
            the :meth:`dimension` of ``self``).

            EXAMPLES::

                sage: A.<x,y> = algebras.DifferentialWeyl(QQ)                           # needs sage.modules
                sage: A.rank()                                                          # needs sage.modules
                +Infinity

                sage: R.<x,y> = QQ[]
                sage: R.rank()
                +Infinity

                sage: F = CombinatorialFreeModule(QQ, ['a','b','c'])
                sage: F.rank()
                3
            """
        def random_element(self, n: int = 2):
            """
            Return a 'random' element of ``self``.

            INPUT:

            - ``n`` -- integer (default: 2); number of summands

            ALGORITHM:

            Return a sum of `n` terms, each of which is formed by
            multiplying a random element of the base ring by a random
            element of the group.

            EXAMPLES::

                sage: x = DihedralGroup(6).algebra(QQ).random_element()                 # needs sage.groups sage.modules
                sage: x.parent() is DihedralGroup(6).algebra(QQ)                        # needs sage.groups sage.modules
                True

            Note, this result can depend on the PRNG state in libgap in a way
            that depends on which packages are loaded, so we must re-seed GAP
            to ensure a consistent result for this example::

                sage: libgap.set_seed(0)                                                # needs sage.libs.gap
                0
                sage: m = SU(2, 13).algebra(QQ).random_element(1)                       # needs sage.groups sage.libs.pari sage.modules
                sage: m.parent() is SU(2, 13).algebra(QQ)                               # needs sage.groups sage.libs.pari sage.modules
                True
                sage: p = CombinatorialFreeModule(ZZ, Partitions(4)).random_element()   # needs sage.combinat sage.modules
                sage: p.parent() is CombinatorialFreeModule(ZZ, Partitions(4))          # needs sage.combinat sage.modules
                True

            TESTS:

            Ensure that the two issues reported in :issue:`28327` are
            fixed; that we don't rely unnecessarily on being able to
            coerce the base ring's zero into the algebra, and that
            we can find a random element in a trivial module::

                sage: class Foo(CombinatorialFreeModule):                               # needs sage.modules
                ....:     def _element_constructor_(self, x):
                ....:         if x in self:
                ....:             return x
                ....:         else:
                ....:             raise ValueError
                sage: from sage.categories.magmatic_algebras import MagmaticAlgebras
                sage: C = MagmaticAlgebras(QQ).WithBasis().Unital()
                sage: F = Foo(QQ, tuple(), category=C)                                  # needs sage.modules
                sage: F.random_element() == F.zero()                                    # needs sage.modules
                True
            """
    class ElementMethods:
        @abstract_method
        def monomial_coefficients(self, copy: bool = True) -> None:
            """
            Return a dictionary whose keys are indices of basis elements
            in the support of ``self`` and whose values are the
            corresponding coefficients.

            INPUT:

            - ``copy`` -- boolean (default: ``True``); if ``self`` is
              internally represented by a dictionary ``d``, then make a copy of
              ``d``; if ``False``, then this can cause undesired behavior by
              mutating ``d``

            EXAMPLES::

                sage: # needs sage.modules
                sage: F = CombinatorialFreeModule(QQ, ['a','b','c'])
                sage: B = F.basis()
                sage: f = B['a'] + 3*B['c']
                sage: d = f.monomial_coefficients()
                sage: d['a']
                1
                sage: d['c']
                3

            TESTS:

            We check that we make a copy of the coefficient dictionary::

                sage: # needs sage.modules
                sage: F = CombinatorialFreeModule(ZZ, ['a','b','c'])
                sage: B = F.basis()
                sage: f = B['a'] + 3*B['c']
                sage: d = f.monomial_coefficients()
                sage: d['a'] = 5
                sage: f
                B['a'] + 3*B['c']
            """
        def __getitem__(self, m):
            """
            Return the coefficient of ``m`` in ``self``.

            EXAMPLES::

                sage: W.<x,y,z> = DifferentialWeylAlgebra(QQ)                           # needs sage.modules
                sage: x[((0,0,0), (0,0,0))]                                             # needs sage.modules
                0
                sage: x[((1,0,0), (0,0,0))]                                             # needs sage.modules
                1
            """
        def coefficient(self, m):
            '''
            Return the coefficient of ``m`` in ``self`` and raise an error
            if ``m`` is not in the basis indexing set.

            INPUT:

            - ``m`` -- a basis index of the parent of ``self``

            OUTPUT:

            The ``B[m]``-coordinate of ``self`` with respect to the basis
            ``B``. Here, ``B`` denotes the given basis of the parent of
            ``self``.

            EXAMPLES::

                sage: # needs sage.combinat sage.modules
                sage: s = CombinatorialFreeModule(QQ, Partitions())
                sage: z = s([4]) - 2*s([2,1]) + s([1,1,1]) + s([1])
                sage: z.coefficient([4])
                1
                sage: z.coefficient([2,1])
                -2
                sage: z.coefficient(Partition([2,1]))
                -2
                sage: z.coefficient([1,2])
                Traceback (most recent call last):
                ...
                AssertionError: [1, 2] should be an element of Partitions
                sage: z.coefficient(Composition([2,1]))
                Traceback (most recent call last):
                ...
                AssertionError: [2, 1] should be an element of Partitions

            Test that ``coefficient`` also works for those parents that do
            not have an ``element_class``::

                sage: # needs sage.modules sage.rings.padics
                sage: H = pAdicWeightSpace(3)
                sage: F = CombinatorialFreeModule(QQ, H)
                sage: hasattr(H, "element_class")
                False
                sage: h = H.an_element()
                sage: (2*F.monomial(h)).coefficient(h)
                2
            '''
        def items(self):
            """
            Return a list of pairs ``(i, c)``, where ``c`` is the
            ``i``-th coefficient of ``i`` in the standard basis.


            EXAMPLES::

                sage: # needs sage.algebras
                sage: B = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0], [0,1]]),
                ....:                                   Matrix([[0,1], [-1,0]])])
                sage: elt = B(Matrix([[1,2], [-2,1]]))
                sage: elt.items()
                dict_items([(0, 1), (1, 2)])

            ::

                sage: # needs sage.combinat sage.modules
                sage: h = SymmetricFunctions(QQ).h()
                sage: (h[2]+3*h[3]).items()
                dict_items([([2], 1), ([3], 3)])
            """
        def is_zero(self):
            """
            Return ``True`` if and only if ``self == 0``.

            EXAMPLES::

                sage: # needs sage.modules
                sage: F = CombinatorialFreeModule(QQ, ['a','b','c'])
                sage: B = F.basis()
                sage: f = B['a'] - 3*B['c']
                sage: f.is_zero()
                False
                sage: F.zero().is_zero()
                True

            ::

                sage: # needs sage.combinat sage.modules
                sage: s = SymmetricFunctions(QQ).schur()
                sage: s([2,1]).is_zero()
                False
                sage: s(0).is_zero()
                True
                sage: (s([2,1]) - s([2,1])).is_zero()
                True
            """
        def __len__(self) -> int:
            """
            Return the number of basis elements whose coefficients in
            ``self`` are nonzero.

            EXAMPLES::

                sage: # needs sage.modules
                sage: F = CombinatorialFreeModule(QQ, ['a','b','c'])
                sage: B = F.basis()
                sage: f = B['a'] - 3*B['c']
                sage: len(f)
                2

            ::

                sage: s = SymmetricFunctions(QQ).schur()                                # needs sage.combinat sage.modules
                sage: z = s([4]) + s([2,1]) + s([1,1,1]) + s([1])                       # needs sage.combinat sage.modules
                sage: len(z)                                                            # needs sage.combinat sage.modules
                4
            """
        def length(self):
            """
            Return the number of basis elements whose coefficients in
            ``self`` are nonzero.

            EXAMPLES::

                sage: # needs sage.modules
                sage: F = CombinatorialFreeModule(QQ, ['a','b','c'])
                sage: B = F.basis()
                sage: f = B['a'] - 3*B['c']
                sage: f.length()
                2

            ::

                sage: s = SymmetricFunctions(QQ).schur()                                # needs sage.combinat sage.modules
                sage: z = s([4]) + s([2,1]) + s([1,1,1]) + s([1])                       # needs sage.combinat sage.modules
                sage: z.length()                                                        # needs sage.combinat sage.modules
                4
            """
        def support(self):
            """
            Return an iterable of the objects indexing the basis of
            ``self.parent()`` whose corresponding coefficients of
            ``self`` are nonzero.

            This method returns these objects in an arbitrary order.

            EXAMPLES::

                sage: # needs sage.modules
                sage: F = CombinatorialFreeModule(QQ, ['a','b','c'])
                sage: B = F.basis()
                sage: f = B['a'] - 3*B['c']
                sage: sorted(f.support())
                ['a', 'c']

            ::

                sage: s = SymmetricFunctions(QQ).schur()                                # needs sage.combinat sage.modules
                sage: z = s([4]) + s([2,1]) + s([1,1,1]) + s([1])                       # needs sage.combinat sage.modules
                sage: sorted(z.support())                                               # needs sage.combinat sage.modules
                [[1], [1, 1, 1], [2, 1], [4]]
            """
        def monomials(self):
            """
            Return a list of the monomials of ``self`` (in an arbitrary
            order).

            The monomials of an element `a` are defined to be the basis
            elements whose corresponding coefficients of `a` are
            nonzero.

            EXAMPLES::

                sage: # needs sage.modules
                sage: F = CombinatorialFreeModule(QQ, ['a','b','c'])
                sage: B = F.basis()
                sage: f = B['a'] + 2*B['c']
                sage: f.monomials()
                [B['a'], B['c']]

                sage: (F.zero()).monomials()                                            # needs sage.modules
                []
            """
        def terms(self):
            """
            Return a list of the (nonzero) terms of ``self`` (in an
            arbitrary order).

            .. SEEALSO:: :meth:`monomials`

            EXAMPLES::

                sage: # needs sage.modules
                sage: F = CombinatorialFreeModule(QQ, ['a','b','c'])
                sage: B = F.basis()
                sage: f = B['a'] + 2*B['c']
                sage: f.terms()
                [B['a'], 2*B['c']]
            """
        def coefficients(self, sort: bool = True):
            """
            Return a list of the (nonzero) coefficients appearing on
            the basis elements in ``self`` (in an arbitrary order).

            INPUT:

            - ``sort`` -- boolean (default: ``True``); to sort the coefficients
              based upon the default ordering of the indexing set

            .. SEEALSO::

                :meth:`~sage.categories.finite_dimensional_modules_with_basis.FiniteDimensionalModulesWithBasis.ElementMethods.dense_coefficient_list`

            EXAMPLES::

                sage: # needs sage.modules
                sage: F = CombinatorialFreeModule(QQ, ['a','b','c'])
                sage: B = F.basis()
                sage: f = B['a'] - 3*B['c']
                sage: f.coefficients()
                [1, -3]
                sage: f = B['c'] - 3*B['a']
                sage: f.coefficients()
                [-3, 1]

            ::

                sage: s = SymmetricFunctions(QQ).schur()                                # needs sage.combinat sage.modules
                sage: z = s([4]) + s([2,1]) + s([1,1,1]) + s([1])                       # needs sage.combinat sage.modules
                sage: z.coefficients()                                                  # needs sage.combinat sage.modules
                [1, 1, 1, 1]
            """
        def support_of_term(self):
            """
            Return the support of ``self``, where ``self`` is a monomial
            (possibly with coefficient).

            EXAMPLES::

                sage: X = CombinatorialFreeModule(QQ, [1,2,3,4]); X.rename('X')         # needs sage.modules
                sage: X.monomial(2).support_of_term()                                   # needs sage.modules
                2
                sage: X.term(3, 2).support_of_term()                                    # needs sage.modules
                3

            An exception is raised if ``self`` has more than one term::

                sage: (X.monomial(2) + X.monomial(3)).support_of_term()                 # needs sage.modules
                Traceback (most recent call last):
                ...
                ValueError: B[2] + B[3] is not a single term
            """
        def leading_support(self, *args, **kwds):
            """
            Return the maximal element of the support of ``self``.

            Note that this may not be the term which actually appears
            first when ``self`` is printed.

            If the default ordering of the basis elements is not what is
            desired, a comparison key, ``key(x)``, can be provided.

            EXAMPLES::

                sage: # needs sage.modules
                sage: X = CombinatorialFreeModule(QQ, [1, 2, 3])
                sage: X.rename('X'); x = X.basis()
                sage: x = 3*X.monomial(1) + 2*X.monomial(2) + 4*X.monomial(3)
                sage: x.leading_support()
                3
                sage: def key(x): return -x
                sage: x.leading_support(key=key)
                1

                sage: s = SymmetricFunctions(QQ).schur()                                # needs sage.combinat sage.modules
                sage: f = 2*s[1] + 3*s[2,1] - 5*s[3]                                    # needs sage.combinat sage.modules
                sage: f.leading_support()                                               # needs sage.combinat sage.modules
                [3]
            """
        def leading_item(self, *args, **kwds):
            """
            Return the pair ``(k, c)`` where

            .. MATH::

                c \\cdot (\\mbox{the basis element indexed by } k)

            is the leading term of ``self``.

            Here 'leading term' means that the corresponding basis element is
            maximal.  Note that this may not be the term which actually appears
            first when ``self`` is printed.

            If the default term ordering is not what is desired, a
            comparison function, ``key(x)``, can be provided.

            EXAMPLES::

                sage: # needs sage.modules
                sage: X = CombinatorialFreeModule(QQ, [1, 2, 3]); X.rename('X')
                sage: x = 3*X.monomial(1) + 2*X.monomial(2) + 4*X.monomial(3)
                sage: x.leading_item()
                (3, 4)
                sage: def key(x): return -x
                sage: x.leading_item(key=key)
                (1, 3)

                sage: s = SymmetricFunctions(QQ).schur()                                # needs sage.combinat sage.modules
                sage: f = 2*s[1] + 3*s[2,1] - 5*s[3]                                    # needs sage.combinat sage.modules
                sage: f.leading_item()                                                  # needs sage.combinat sage.modules
                ([3], -5)

            The term ordering of polynomial rings is taken into account::

                sage: R.<x,y,z> = QQ[]
                sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).leading_item()
                ((0, 4, 0), 1)
                sage: R.<x,y,z> = PolynomialRing(QQ, order='lex')
                sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).leading_item()
                ((1, 2, 0), 3)
                sage: R.<x,y,z> = PolynomialRing(QQ, order='invlex')
                sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).leading_item()
                ((0, 1, 3), 2)
            """
        def leading_monomial(self, *args, **kwds):
            """
            Return the leading monomial of ``self``.

            This is the monomial whose corresponding basis element is
            maximal. Note that this may not be the term which actually appears
            first when ``self`` is printed.

            If the default term ordering is not
            what is desired, a comparison key, ``key(x)``, can be provided.

            EXAMPLES::

                sage: # needs sage.modules
                sage: X = CombinatorialFreeModule(QQ, [1, 2, 3]); X.rename('X')
                sage: x = 3*X.monomial(1) + 2*X.monomial(2) + X.monomial(3)
                sage: x.leading_monomial()
                B[3]
                sage: def key(x): return -x
                sage: x.leading_monomial(key=key)
                B[1]

                sage: s = SymmetricFunctions(QQ).schur()                                # needs sage.combinat sage.modules
                sage: f = 2*s[1] + 3*s[2,1] - 5*s[3]                                    # needs sage.combinat sage.modules
                sage: f.leading_monomial()                                              # needs sage.combinat sage.modules
                s[3]

            The term ordering of polynomial rings is taken into account::

                sage: R.<x,y,z> = QQ[]
                sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).leading_monomial()
                y^4
                sage: R.<x,y,z> = PolynomialRing(QQ, order='lex')
                sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).leading_monomial()
                x*y^2
                sage: R.<x,y,z> = PolynomialRing(QQ, order='invlex')
                sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).leading_monomial()
                y*z^3
            """
        def leading_coefficient(self, *args, **kwds):
            """
            Return the leading coefficient of ``self``.

            This is the coefficient of the term whose corresponding basis element is
            maximal. Note that this may not be the term which actually appears
            first when ``self`` is printed.

            If the default term ordering is not
            what is desired, a comparison key, ``key(x,y)``, can be provided.

            EXAMPLES::

                sage: # needs sage.modules
                sage: X = CombinatorialFreeModule(QQ, [1, 2, 3]); X.rename('X')
                sage: x = 3*X.monomial(1) + 2*X.monomial(2) + X.monomial(3)
                sage: x.leading_coefficient()
                1
                sage: def key(x): return -x
                sage: x.leading_coefficient(key=key)
                3

                sage: s = SymmetricFunctions(QQ).schur()                                # needs sage.combinat sage.modules
                sage: f = 2*s[1] + 3*s[2,1] - 5*s[3]                                    # needs sage.combinat sage.modules
                sage: f.leading_coefficient()                                           # needs sage.combinat sage.modules
                -5

            The term ordering of polynomial rings is taken into account::

                sage: R.<x,y,z> = QQ[]
                sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).leading_coefficient()
                1
                sage: R.<x,y,z> = PolynomialRing(QQ, order='lex')
                sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).leading_coefficient()
                3
                sage: R.<x,y,z> = PolynomialRing(QQ, order='invlex')
                sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).leading_coefficient()
                2
            """
        def leading_term(self, *args, **kwds):
            """
            Return the leading term of ``self``.

            This is the term whose corresponding basis element is
            maximal. Note that this may not be the term which actually appears
            first when ``self`` is printed.

            If the default term ordering is not
            what is desired, a comparison key, ``key(x)``, can be provided.

            EXAMPLES::

                sage: # needs sage.modules
                sage: X = CombinatorialFreeModule(QQ, [1, 2, 3]); X.rename('X')
                sage: x = 3*X.monomial(1) + 2*X.monomial(2) + X.monomial(3)
                sage: x.leading_term()
                B[3]
                sage: def key(x): return -x
                sage: x.leading_term(key=key)
                3*B[1]

                sage: s = SymmetricFunctions(QQ).schur()                                # needs sage.combinat sage.modules
                sage: f = 2*s[1] + 3*s[2,1] - 5*s[3]                                    # needs sage.combinat sage.modules
                sage: f.leading_term()                                                  # needs sage.combinat sage.modules
                -5*s[3]

            The term ordering of polynomial rings is taken into account::

                sage: R.<x,y,z> = QQ[]
                sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).leading_term()
                y^4
                sage: R.<x,y,z> = PolynomialRing(QQ, order='lex')
                sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).leading_term()
                3*x*y^2
                sage: R.<x,y,z> = PolynomialRing(QQ, order='invlex')
                sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).leading_term()
                2*y*z^3
            """
        def trailing_support(self, *args, **kwds):
            """
            Return the minimal element of the support of ``self``. Note
            that this may not be the term which actually appears last when
            ``self`` is printed.

            If the default ordering of the basis elements is not what is
            desired, a comparison key, ``key(x)``, can be provided.

            EXAMPLES::

                sage: X = CombinatorialFreeModule(QQ, [1, 2, 3]); X.rename('X')         # needs sage.modules
                sage: x = 3*X.monomial(1) + 2*X.monomial(2) + 4*X.monomial(3)           # needs sage.modules
                sage: x.trailing_support()                                              # needs sage.modules
                1

                sage: def key(x): return -x
                sage: x.trailing_support(key=key)                                       # needs sage.modules
                3

                sage: s = SymmetricFunctions(QQ).schur()                                # needs sage.combinat sage.modules
                sage: f = 2*s[1] + 3*s[2,1] - 5*s[3]                                    # needs sage.combinat sage.modules
                sage: f.trailing_support()                                              # needs sage.combinat sage.modules
                [1]
            """
        def trailing_item(self, *args, **kwds):
            """
            Return the pair ``(c, k)`` where ``c*self.parent().monomial(k)``
            is the trailing term of ``self``.

            This is the monomial whose corresponding basis element is
            minimal. Note that this may not be the term which actually appears
            last when ``self`` is printed.

            If the default term ordering is not
            what is desired, a comparison key ``key(x)``, can be provided.

            EXAMPLES::

                sage: # needs sage.modules
                sage: X = CombinatorialFreeModule(QQ, [1, 2, 3]); X.rename('X')
                sage: x = 3*X.monomial(1) + 2*X.monomial(2) + X.monomial(3)
                sage: x.trailing_item()
                (1, 3)
                sage: def key(x): return -x
                sage: x.trailing_item(key=key)
                (3, 1)

                sage: s = SymmetricFunctions(QQ).schur()                                # needs sage.combinat sage.modules
                sage: f = 2*s[1] + 3*s[2,1] - 5*s[3]                                    # needs sage.combinat sage.modules
                sage: f.trailing_item()                                                 # needs sage.combinat sage.modules
                ([1], 2)

            The term ordering of polynomial rings is taken into account::

                sage: R.<x,y,z> = QQ[]
                sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).trailing_item()
                ((1, 1, 1), 4)
                sage: R.<x,y,z> = PolynomialRing(QQ, order='lex')
                sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).trailing_item()
                ((0, 1, 3), 2)
                sage: R.<x,y,z> = PolynomialRing(QQ, order='invlex')
                sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).trailing_item()
                ((1, 2, 0), 3)
            """
        def trailing_monomial(self, *args, **kwds):
            """
            Return the trailing monomial of ``self``.

            This is the monomial whose corresponding basis element is
            minimal. Note that this may not be the term which actually appears
            last when ``self`` is printed.

            If the default term ordering is not
            what is desired, a comparison key ``key(x)``, can be provided.

            EXAMPLES::

                sage: # needs sage.modules
                sage: X = CombinatorialFreeModule(QQ, [1, 2, 3]); X.rename('X')
                sage: x = 3*X.monomial(1) + 2*X.monomial(2) + X.monomial(3)
                sage: x.trailing_monomial()
                B[1]
                sage: def key(x): return -x
                sage: x.trailing_monomial(key=key)
                B[3]

                sage: s = SymmetricFunctions(QQ).schur()                                # needs sage.combinat sage.modules
                sage: f = 2*s[1] + 3*s[2,1] - 5*s[3]                                    # needs sage.combinat sage.modules
                sage: f.trailing_monomial()                                             # needs sage.combinat sage.modules
                s[1]

            The term ordering of polynomial rings is taken into account::

                sage: R.<x,y,z> = QQ[]
                sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).trailing_monomial()
                x*y*z
                sage: R.<x,y,z> = PolynomialRing(QQ, order='lex')
                sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).trailing_monomial()
                y*z^3
                sage: R.<x,y,z> = PolynomialRing(QQ, order='invlex')
                sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).trailing_monomial()
                x*y^2
            """
        def trailing_coefficient(self, *args, **kwds):
            """
            Return the trailing coefficient of ``self``.

            This is the coefficient of the monomial whose corresponding basis element is
            minimal. Note that this may not be the term which actually appears
            last when ``self`` is printed.

            If the default term ordering is not
            what is desired, a comparison key ``key(x)``, can be provided.

            EXAMPLES::

                sage: # needs sage.modules
                sage: X = CombinatorialFreeModule(QQ, [1, 2, 3]); X.rename('X')
                sage: x = 3*X.monomial(1) + 2*X.monomial(2) + X.monomial(3)
                sage: x.trailing_coefficient()
                3
                sage: def key(x): return -x
                sage: x.trailing_coefficient(key=key)
                1

                sage: s = SymmetricFunctions(QQ).schur()                                # needs sage.combinat sage.modules
                sage: f = 2*s[1] + 3*s[2,1] - 5*s[3]                                    # needs sage.combinat sage.modules
                sage: f.trailing_coefficient()                                          # needs sage.combinat sage.modules
                2

            The term ordering of polynomial rings is taken into account::

                sage: R.<x,y,z> = QQ[]
                sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).trailing_coefficient()
                4
                sage: R.<x,y,z> = PolynomialRing(QQ, order='lex')
                sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).trailing_coefficient()
                2
                sage: R.<x,y,z> = PolynomialRing(QQ, order='invlex')
                sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).trailing_coefficient()
                3
            """
        def trailing_term(self, *args, **kwds):
            """
            Return the trailing term of ``self``.

            This is the term whose corresponding basis element is
            minimal. Note that this may not be the term which actually appears
            last when ``self`` is printed.

            If the default term ordering is not
            what is desired, a comparison key ``key(x)``, can be provided.

            EXAMPLES::

                sage: # needs sage.modules
                sage: X = CombinatorialFreeModule(QQ, [1, 2, 3]); X.rename('X')
                sage: x = 3*X.monomial(1) + 2*X.monomial(2) + X.monomial(3)
                sage: x.trailing_term()
                3*B[1]
                sage: def key(x): return -x
                sage: x.trailing_term(key=key)
                B[3]

                sage: s = SymmetricFunctions(QQ).schur()                                # needs sage.combinat sage.modules
                sage: f = 2*s[1] + 3*s[2,1] - 5*s[3]                                    # needs sage.combinat sage.modules
                sage: f.trailing_term()                                                 # needs sage.combinat sage.modules
                2*s[1]

            The term ordering of polynomial rings is taken into account::

                sage: R.<x,y,z> = QQ[]
                sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).trailing_term()
                4*x*y*z
                sage: R.<x,y,z> = PolynomialRing(QQ, order='lex')
                sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).trailing_term()
                2*y*z^3
                sage: R.<x,y,z> = PolynomialRing(QQ, order='invlex')
                sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).trailing_term()
                3*x*y^2
            """
        def map_coefficients(self, f, new_base_ring=None):
            """
            Return the element obtained by applying ``f`` to the nonzero
            coefficients of ``self``.

            If ``f`` is a :class:`sage.categories.map.Map`, then the resulting
            polynomial will be defined over the codomain of ``f``. Otherwise, the
            resulting polynomial will be over the same ring as ``self``. Set
            ``new_base_ring`` to override this behaviour.

            An error is raised if the coefficients cannot be
            converted to the new base ring.

            INPUT:

            - ``f`` -- a callable that will be applied to the
              coefficients of ``self``

            - ``new_base_ring`` -- (optional) if given, the resulting element
              will be defined over this ring

            EXAMPLES::

                sage: # needs sage.modules
                sage: F = CombinatorialFreeModule(QQ, ['a','b','c'])
                sage: B = F.basis()
                sage: f = B['a'] - 3*B['c']
                sage: f.map_coefficients(lambda x: x + 5)
                6*B['a'] + 2*B['c']

            Killed coefficients are handled properly::

                sage: f.map_coefficients(lambda x: 0)                                   # needs sage.modules
                0
                sage: list(f.map_coefficients(lambda x: 0))                             # needs sage.modules
                []

            ::

                sage: s = SymmetricFunctions(QQ).schur()                                # needs sage.combinat sage.modules
                sage: a = s([2,1]) + 2*s([3,2])                                         # needs sage.combinat sage.modules
                sage: a.map_coefficients(lambda x: x * 2)                               # needs sage.combinat sage.modules
                2*s[2, 1] + 4*s[3, 2]

            We can map into a different base ring::

                sage: F = CombinatorialFreeModule(QQ, ['a','b','c'])
                sage: B = F.basis()
                sage: a = 1/2*(B['a'] + 3*B['c']); a
                1/2*B['a'] + 3/2*B['c']
                sage: b = a.map_coefficients(lambda c: 2*c, ZZ); b
                B['a'] + 3*B['c']
                sage: b.parent()
                Free module generated by {'a', 'b', 'c'} over Integer Ring
                sage: b.map_coefficients(lambda c: 1/2*c, ZZ)
                Traceback (most recent call last):
                ...
                TypeError: no conversion of this rational to integer

            Coefficients are converted to the new base ring after
            applying the map::

                sage: B['a'].map_coefficients(lambda c: 2*c, GF(2))
                0
                sage: B['a'].map_coefficients(lambda c: GF(2)(c), QQ)
                B['a']
            """
        def map_support(self, f):
            """
            Mapping a function on the support.

            INPUT:

            - ``f`` -- an endofunction on the indices of the free module

            Return a new element of ``self.parent()`` obtained by
            applying the function ``f`` to all of the objects indexing
            the basis elements.

            EXAMPLES::

                sage: B = CombinatorialFreeModule(ZZ, [-1, 0, 1])                       # needs sage.modules
                sage: x = B.an_element(); x                                             # needs sage.modules
                2*B[-1] + 2*B[0] + 3*B[1]
                sage: x.map_support(lambda i: -i)                                       # needs sage.modules
                3*B[-1] + 2*B[0] + 2*B[1]

            ``f`` needs not be injective::

                sage: x.map_support(lambda i: 1)                                        # needs sage.modules
                7*B[1]

                sage: s = SymmetricFunctions(QQ).schur()                                # needs sage.combinat sage.modules
                sage: a = s([2,1]) + 2*s([3,2])                                         # needs sage.combinat sage.modules
                sage: a.map_support(lambda x: x.conjugate())                            # needs sage.combinat sage.modules
                s[2, 1] + 2*s[2, 2, 1]

            TESTS::

                sage: B.zero()      # This actually failed at some point!!! See #8890   # needs sage.modules
                0

                sage: y = B.zero().map_support(lambda i: i/0); y                        # needs sage.modules
                0
                sage: y.parent() is B                                                   # needs sage.modules
                True
            """
        def map_support_skip_none(self, f):
            """
            Mapping a function on the support.

            INPUT:

            - ``f`` -- an endofunction on the indices of the free module

            Returns a new element of ``self.parent()`` obtained by
            applying the function `f` to all of the objects indexing
            the basis elements.

            EXAMPLES::

                sage: B = CombinatorialFreeModule(ZZ, [-1, 0, 1])                       # needs sage.modules
                sage: x = B.an_element(); x                                             # needs sage.modules
                2*B[-1] + 2*B[0] + 3*B[1]
                sage: x.map_support_skip_none(lambda i: -i if i else None)              # needs sage.modules
                3*B[-1] + 2*B[1]

            ``f`` needs not be injective::

                sage: x.map_support_skip_none(lambda i: 1 if i else None)               # needs sage.modules
                5*B[1]

            TESTS::

                sage: y = x.map_support_skip_none(lambda i: None); y                    # needs sage.modules
                0
                sage: y.parent() is B                                                   # needs sage.modules
                True
            """
        def map_item(self, f):
            """
            Mapping a function on items.

            INPUT:

            - ``f`` -- a function mapping pairs ``(index, coeff)`` to
              other such pairs

            Return a new element of ``self.parent()`` obtained by
            applying the function `f` to all items ``(index, coeff)`` of
            ``self``.

            EXAMPLES::

                sage: B = CombinatorialFreeModule(ZZ, [-1, 0, 1])                       # needs sage.modules
                sage: x = B.an_element(); x                                             # needs sage.modules
                2*B[-1] + 2*B[0] + 3*B[1]
                sage: x.map_item(lambda i, c: (-i, 2*c))                                # needs sage.modules
                6*B[-1] + 4*B[0] + 4*B[1]

            ``f`` needs not be injective::

                sage: x.map_item(lambda i, c: (1, 2*c))                                 # needs sage.modules
                14*B[1]

                sage: s = SymmetricFunctions(QQ).schur()                                # needs sage.combinat sage.modules
                sage: f = lambda m, c: (m.conjugate(), 2 * c)
                sage: a = s([2,1]) + s([1,1,1])                                         # needs sage.combinat sage.modules
                sage: a.map_item(f)                                                     # needs sage.combinat sage.modules
                2*s[2, 1] + 2*s[3]
            """
        def tensor(*elements):
            """
            Return the tensor product of its arguments, as an element of
            the tensor product of the parents of those elements.

            EXAMPLES::

                sage: C = AlgebrasWithBasis(QQ)
                sage: A = C.example()                                                   # needs sage.combinat sage.modules
                sage: a, b, c = A.algebra_generators()                                  # needs sage.combinat sage.modules
                sage: a.tensor(b, c)                                                    # needs sage.combinat sage.modules
                B[word: a] # B[word: b] # B[word: c]

            FIXME: is this a policy that we want to enforce on all parents?
            """
    class Homsets(HomsetsCategory):
        class ParentMethods:
            def __call_on_basis__(self, **options):
                """
                Construct a morphism in this homset from a function defined
                on the basis.

                INPUT:

                - ``on_basis`` -- a function from the indices of the
                  basis of the domain of ``self`` to the codomain of
                  ``self``

                This method simply delegates the work to
                :meth:`ModulesWithBasis.ParentMethods.module_morphism`. It
                is used by :meth:`Homset.__call__` to handle the
                ``on_basis`` argument, and will disappear as soon as
                the logic will be generalized.

                EXAMPLES::

                    sage: # needs sage.modules
                    sage: X = CombinatorialFreeModule(QQ, [1,2,3]);   X.rename('X')
                    sage: Y = CombinatorialFreeModule(QQ, [1,2,3,4]); Y.rename('Y')
                    sage: H = Hom(X, Y)
                    sage: x = X.basis()
                    sage: def on_basis(i):
                    ....:     return Y.monomial(i) + 2*Y.monomial(i + 1)
                    sage: phi = H(on_basis=on_basis)  # indirect doctest
                    sage: phi
                    Generic morphism:
                      From: X
                      To:   Y
                    sage: phi(x[1] + x[3])
                    B[1] + 2*B[2] + B[3] + 2*B[4]

                Diagonal functions can be constructed using the ``diagonal`` option::

                    sage: # needs sage.modules
                    sage: X = CombinatorialFreeModule(QQ, [1,2,3,4]); X.rename('X')
                    sage: Y = CombinatorialFreeModule(QQ, [1,2,3,4],
                    ....:                             key='Y'); Y.rename('Y')
                    sage: H = Hom(X, Y)
                    sage: x = X.basis()
                    sage: phi = H(diagonal=lambda x: x^2)
                    sage: phi(x[1] + x[2] + x[3])
                    B[1] + 4*B[2] + 9*B[3]

                TESTS:

                As for usual homsets, the argument can be a Python function::

                    sage: phi = H(lambda x: Y.zero()); phi                              # needs sage.modules
                    Generic morphism:
                      From: X
                      To:   Y
                    sage: phi(x[1] + x[3])                                              # needs sage.modules
                    0

                We check that the homset category is properly set up::

                    sage: # needs sage.modules
                    sage: X = CombinatorialFreeModule(QQ, [1,2,3]);   X.rename('X')
                    sage: Y = CombinatorialFreeModule(QQ, [1,2,3,4]); Y.rename('Y')
                    sage: H = Hom(X, Y)
                    sage: H.zero().category_for()
                    Category of finite dimensional vector spaces with basis over Rational Field
                """
    class MorphismMethods:
        @cached_method
        def on_basis(self):
            """
            Return the action of this morphism on basis elements.

            OUTPUT:

            - a function from the indices of the basis of the domain to
              the codomain

            EXAMPLES::

                sage: # needs sage.modules
                sage: X = CombinatorialFreeModule(QQ, [1,2,3]);   X.rename('X')
                sage: Y = CombinatorialFreeModule(QQ, [1,2,3,4]); Y.rename('Y')
                sage: H = Hom(X, Y)
                sage: x = X.basis()
                sage: f = H(lambda x: Y.zero()).on_basis()
                sage: f(2)
                0
                sage: f = lambda i: Y.monomial(i) + 2*Y.monomial(i+1)
                sage: g = H(on_basis=f).on_basis()
                sage: g(2)
                B[2] + 2*B[3]
                sage: g == f
                True
            """
    class CartesianProducts(CartesianProductsCategory):
        """
        The category of modules with basis constructed by Cartesian products
        of modules with basis.
        """
        @cached_method
        def extra_super_categories(self):
            """
            EXAMPLES::

                sage: ModulesWithBasis(QQ).CartesianProducts().extra_super_categories()
                [Category of vector spaces with basis over Rational Field]
                sage: ModulesWithBasis(QQ).CartesianProducts().super_categories()
                [Category of Cartesian products of modules with basis over Rational Field,
                 Category of vector spaces with basis over Rational Field,
                 Category of Cartesian products of vector spaces over Rational Field]
            """
        class ParentMethods: ...
    class TensorProducts(TensorProductsCategory):
        """
        The category of modules with basis constructed by tensor product of
        modules with basis.
        """
        @cached_method
        def extra_super_categories(self):
            """
            EXAMPLES::

                sage: ModulesWithBasis(QQ).TensorProducts().extra_super_categories()
                [Category of vector spaces with basis over Rational Field]
                sage: ModulesWithBasis(QQ).TensorProducts().super_categories()
                [Category of tensor products of modules with basis over Rational Field,
                 Category of vector spaces with basis over Rational Field,
                 Category of tensor products of vector spaces over Rational Field]
            """
        class ParentMethods:
            """
            Implement operations on tensor products of modules with basis.
            """
        class ElementMethods:
            """
            Implement operations on elements of tensor products of modules
            with basis.
            """
            def apply_multilinear_morphism(self, f, codomain=None):
                """
                Return the result of applying the morphism induced by ``f``
                to ``self``.

                INPUT:

                - ``f`` -- a multilinear morphism from the component
                  modules of the parent tensor product to any module

                - ``codomain`` -- the codomain of ``f`` (optional)

                By the universal property of the tensor product, ``f``
                induces a linear morphism from `self.parent()` to the
                target module. Returns the result of applying that
                morphism to ``self``.

                The codomain is used for optimizations purposes
                only. If it's not provided, it's recovered by calling
                ``f`` on the zero input.

                EXAMPLES:

                We start with simple (admittedly not so interesting)
                examples, with two modules `A` and `B`::

                    sage: # needs sage.modules
                    sage: A = CombinatorialFreeModule(ZZ, [1,2], prefix='A')
                    sage: A.rename('A')
                    sage: B = CombinatorialFreeModule(ZZ, [3,4], prefix='B')
                    sage: B.rename('B')

                and `f` the bilinear morphism `(a,b) \\mapsto b \\otimes a`
                from `A \\times B` to `B \\otimes A`::

                    sage: def f(a, b):
                    ....:     return tensor([b,a])

                Now, calling applying `f` on `a \\otimes b` returns the same
                as `f(a,b)`::

                    sage: # needs sage.modules
                    sage: a = A.monomial(1) + 2 * A.monomial(2); a
                    A[1] + 2*A[2]
                    sage: b = B.monomial(3) - 2 * B.monomial(4); b
                    B[3] - 2*B[4]
                    sage: f(a, b)
                    B[3] # A[1] + 2*B[3] # A[2] - 2*B[4] # A[1] - 4*B[4] # A[2]
                    sage: tensor([a, b]).apply_multilinear_morphism(f)
                    B[3] # A[1] + 2*B[3] # A[2] - 2*B[4] # A[1] - 4*B[4] # A[2]

                `f` may be a bilinear morphism to any module over the
                base ring of `A` and `B`. Here the codomain is `\\ZZ`::

                    sage: def f(a, b):
                    ....:     return sum(a.coefficients(), 0) * sum(b.coefficients(), 0)
                    sage: f(a, b)                                                       # needs sage.modules
                    -3
                    sage: tensor([a, b]).apply_multilinear_morphism(f)                  # needs sage.modules
                    -3

                Mind the `0` in the sums above; otherwise `f` would
                not return `0` in `\\ZZ`::

                    sage: def f(a, b):
                    ....:     return sum(a.coefficients()) * sum(b.coefficients())
                    sage: type(f(A.zero(), B.zero()))                                   # needs sage.modules
                    <... 'int'>

                Which would be wrong and break this method::

                    sage: tensor([a, b]).apply_multilinear_morphism(f)                  # needs sage.modules
                    Traceback (most recent call last):
                    ...
                    AttributeError: 'int' object has no attribute 'parent'...

                Here we consider an example where the codomain is a
                module with basis with a different base ring::

                    sage: # needs sage.modules
                    sage: C = CombinatorialFreeModule(QQ, [(1,3),(2,4)], prefix='C')
                    sage: C.rename('C')
                    sage: def f(a, b):
                    ....:     return C.sum_of_terms([((1,3), QQ(a[1]*b[3])),
                    ....:                            ((2,4), QQ(a[2]*b[4]))])
                    sage: f(a,b)
                    C[(1, 3)] - 4*C[(2, 4)]
                    sage: tensor([a, b]).apply_multilinear_morphism(f)
                    C[(1, 3)] - 4*C[(2, 4)]

                 We conclude with a real life application, where we
                 check that the antipode of the Hopf algebra of
                 Symmetric functions on the Schur basis satisfies its
                 defining formula::

                    sage: # needs lrcalc_python sage.combinat sage.modules
                    sage: Sym = SymmetricFunctions(QQ)
                    sage: s = Sym.schur()
                    sage: def f(a, b): return a * b.antipode()
                    sage: x = 4 * s.an_element(); x
                    8*s[] + 8*s[1] + 12*s[2]
                    sage: x.coproduct().apply_multilinear_morphism(f)
                    8*s[]
                    sage: x.coproduct().apply_multilinear_morphism(f) == x.counit()
                    True

                We recover the constant term of `x`, as desired.

                .. TODO::

                    Extract a method to linearize a multilinear
                    morphism, and delegate the work there.
                """
    class DualObjects(DualObjectsCategory):
        @cached_method
        def extra_super_categories(self):
            """
            EXAMPLES::

                sage: ModulesWithBasis(ZZ).DualObjects().extra_super_categories()
                [Category of modules over Integer Ring]
                sage: ModulesWithBasis(QQ).DualObjects().super_categories()
                [Category of duals of vector spaces over Rational Field,
                 Category of duals of modules with basis over Rational Field]
            """

FreeModules = ModulesWithBasis