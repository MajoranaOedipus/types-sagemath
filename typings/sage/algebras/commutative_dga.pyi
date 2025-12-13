from sage.algebras.free_algebra import FreeAlgebra as FreeAlgebra
from sage.categories.algebras import Algebras as Algebras
from sage.categories.chain_complexes import ChainComplexes as ChainComplexes
from sage.categories.homset import Hom as Hom
from sage.categories.modules import Modules as Modules
from sage.categories.morphism import Morphism as Morphism
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.combinat.integer_vector_weighted import WeightedIntegerVectors as WeightedIntegerVectors
from sage.groups.additive_abelian.additive_abelian_group import AdditiveAbelianGroup as AdditiveAbelianGroup
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_function as cached_function, cached_method as cached_method
from sage.misc.functional import is_even as is_even, is_odd as is_odd
from sage.misc.inherit_comparison import InheritComparisonClasscallMetaclass as InheritComparisonClasscallMetaclass
from sage.misc.misc_c import prod as prod
from sage.modules.free_module import VectorSpace as VectorSpace
from sage.modules.free_module_element import vector as vector
from sage.rings.homset import RingHomset_generic as RingHomset_generic
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.morphism import RingHomomorphism_im_gens as RingHomomorphism_im_gens
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.polynomial.term_order import TermOrder as TermOrder
from sage.rings.quotient_ring import QuotientRing_nc as QuotientRing_nc
from sage.rings.quotient_ring_element import QuotientRingElement as QuotientRingElement
from sage.structure.sage_object import SageObject as SageObject
from sage.structure.unique_representation import CachedRepresentation as CachedRepresentation, UniqueRepresentation as UniqueRepresentation

def sorting_keys(element):
    """
    Auxiliary function to sort the elements of a basis of a Cohomology group.

    It is needed to ensure that elements of a cohomology group are represented
    in a consistent way.

    INPUT:

    - ``element`` -- a CohomologyClass

    OUTPUT: its coordinates in the corresponding ``cohomology_raw`` quotient vector space

    EXAMPLES::

        sage: from sage.algebras.commutative_dga import sorting_keys
        sage: A.<e1,e2,e3,e4,e5> = GradedCommutativeAlgebra(QQ)
        sage: B = A.cdg_algebra({e5:e1*e2+e3*e4})
        sage: B.inject_variables()
        Defining e1, e2, e3, e4, e5
        sage: C = B.cohomology(3)
        sage: [sorting_keys(el) for el in C.basis().keys()]
        [[1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1]]
    """

class Differential(UniqueRepresentation, Morphism, metaclass=InheritComparisonClasscallMetaclass):
    """
    Differential of a commutative graded algebra.

    INPUT:

    - ``A`` -- algebra where the differential is defined
    - ``im_gens`` -- tuple containing the image of each generator

    EXAMPLES::

        sage: A.<x,y,z,t> = GradedCommutativeAlgebra(QQ, degrees=(1, 1, 2, 3))
        sage: B = A.cdg_algebra({x: x*y, y: -x*y , z: t})
        sage: B
        Commutative Differential Graded Algebra with generators ('x', 'y', 'z', 't')
         in degrees (1, 1, 2, 3) over Rational Field with differential:
            x --> x*y
            y --> -x*y
            z --> t
            t --> 0
        sage: B.differential()(x)
        x*y
    """
    @staticmethod
    def __classcall__(cls, A, im_gens):
        """
        Normalize input to ensure a unique representation.

        TESTS::

            sage: A.<x,y,z,t> = GradedCommutativeAlgebra(QQ, degrees=(1, 1, 2, 3))
            sage: d1 = A.cdg_algebra({x: x*y, y: -x*y, z: t}).differential()
            sage: d2 = A.cdg_algebra({x: x*y, z: t, y: -x*y, t: 0}).differential()
            sage: d1 is d2
            True

        Check that :issue:`34818` is solved::

            sage: A.<a,b,x,u> = GradedCommutativeAlgebra(QQ,degrees=(2,2,3,3))
            sage: A = A.quotient(A.ideal([a*u,b*u,x*u]))
            sage: A.cdg_algebra({x:a*b,a:u})
            Commutative Differential Graded Algebra with generators ('a', 'b', 'x', 'u')
             in degrees (2, 2, 3, 3) with relations [a*u, b*u, x*u] over Rational Field
             with differential:
               a --> u
               b --> 0
               x --> a*b
               u --> 0
            sage: A.cdg_algebra({x:a*b,a:u,u:a^2})
            Traceback (most recent call last):
            ...
            ValueError: the differential does not preserve the ideal
        """
    def __init__(self, A, im_gens) -> None:
        """
        Initialize ``self``.

        INPUT:

        - ``A`` -- algebra where the differential is defined

        - ``im_gens`` -- tuple containing the image of each generator

        EXAMPLES::

            sage: A.<x,y,z,t> = GradedCommutativeAlgebra(QQ)
            sage: B = A.cdg_algebra({x: x*y, y: x*y, z: z*t, t: t*z})
            sage: [B.cohomology(i).dimension() for i in range(6)]
            [1, 2, 1, 0, 0, 0]
            sage: d = B.differential()

        We skip the category test because homsets/morphisms aren't
        proper parents/elements yet::

            sage: TestSuite(d).run(skip='_test_category')

        An error is raised if the differential `d` does not have
        degree 1 or if `d \\circ d` is not zero::

            sage: A.<a,b,c> = GradedCommutativeAlgebra(QQ, degrees=(1,2,3))
            sage: A.cdg_algebra({a:b, b:c})
            Traceback (most recent call last):
            ...
            ValueError: the given dictionary does not determine a valid differential
        """
    @cached_method
    def differential_matrix(self, n):
        """
        The matrix that gives the differential in degree ``n``.

        INPUT:

        - ``n`` -- degree

        EXAMPLES::

            sage: A.<x,y,z,t> = GradedCommutativeAlgebra(GF(5), degrees=(2, 2, 3, 4))
            sage: d = A.differential({t: x*z, x: z, y: z})
            sage: d.differential_matrix(4)
            [2 0]
            [1 1]
            [0 2]
            [1 0]
            sage: A.inject_variables()
            Defining x, y, z, t
            sage: d(t)
            x*z
            sage: d(y^2)
            2*y*z
            sage: d(x*y)
            x*z + y*z
            sage: d(x^2)
            2*x*z
        """
    def coboundaries(self, n):
        """
        The ``n``-th coboundary group of the algebra.

        This is a vector space over the base field `F`, and it is
        returned as a subspace of the vector space `F^d`, where the
        ``n``-th homogeneous component has dimension `d`.

        INPUT:

        - ``n`` -- degree

        EXAMPLES::

            sage: A.<x,y,z> = GradedCommutativeAlgebra(QQ, degrees=(1, 1, 2))
            sage: d = A.differential({z: x*z})
            sage: d.coboundaries(2)
            Vector space of degree 2 and dimension 0 over Rational Field
            Basis matrix:
            []
            sage: d.coboundaries(3)
            Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix:
            [1 0]
            sage: d.coboundaries(1)
            Vector space of degree 2 and dimension 0 over Rational Field
            Basis matrix:
            []
        """
    def cocycles(self, n):
        """
        The ``n``-th cocycle group of the algebra.

        This is a vector space over the base field `F`, and it is
        returned as a subspace of the vector space `F^d`, where the
        ``n``-th homogeneous component has dimension `d`.

        INPUT:

        - ``n`` -- degree

        EXAMPLES::

            sage: A.<x,y,z> = GradedCommutativeAlgebra(QQ, degrees=(1, 1, 2))
            sage: d = A.differential({z: x*z})
            sage: d.cocycles(2)
            Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix:
            [1 0]
        """
    def cohomology_raw(self, n):
        """
        The ``n``-th cohomology group of ``self``.

        This is a vector space over the base ring, and it is returned
        as the quotient cocycles/coboundaries.

        INPUT:

        - ``n`` -- degree

        .. SEEALSO::

            :meth:`cohomology`

        EXAMPLES::

            sage: A.<x,y,z,t> = GradedCommutativeAlgebra(QQ, degrees=(2, 2, 3, 4))
            sage: d = A.differential({t: x*z, x: z, y: z})
            sage: d.cohomology_raw(4)
            Vector space quotient V/W of dimension 2 over Rational Field where
            V: Vector space of degree 4 and dimension 2 over Rational Field
            Basis matrix:
            [   1    0    0   -2]
            [   0    1 -1/2   -1]
            W: Vector space of degree 4 and dimension 0 over Rational Field
            Basis matrix:
            []

        Compare to :meth:`cohomology`::

            sage: d.cohomology(4)
            Free module generated by {[x^2 - 2*t], [x*y - 1/2*y^2 - t]} over Rational Field
        """
    def cohomology(self, n):
        """
        The ``n``-th cohomology group of ``self``.

        This is a vector space over the base ring, defined as the
        quotient cocycles/coboundaries. The elements of the quotient
        are lifted to the vector space of cocycles, and this is
        described in terms of those lifts.

        INPUT:

        - ``n`` -- degree

        .. SEEALSO::

            :meth:`cohomology_raw`

        EXAMPLES::

            sage: A.<a,b,c,d,e> = GradedCommutativeAlgebra(QQ, degrees=(1, 1, 1, 1, 1))
            sage: d = A.differential({d: a*b, e: b*c})
            sage: d.cohomology(2)
            Free module generated by {[a*c], [a*d], [b*d], [c*d - a*e], [b*e], [c*e]} over Rational Field

        Compare to :meth:`cohomology_raw`::

            sage: d.cohomology_raw(2)
            Vector space quotient V/W of dimension 6 over Rational Field where
            V: Vector space of degree 10 and dimension 8 over Rational Field
            Basis matrix:
            [ 1  0  0  0  0  0  0  0  0  0]
            [ 0  1  0  0  0  0  0  0  0  0]
            [ 0  0  1  0  0  0  0  0  0  0]
            [ 0  0  0  1  0  0  0  0  0  0]
            [ 0  0  0  0  1  0  0  0  0  0]
            [ 0  0  0  0  0  1 -1  0  0  0]
            [ 0  0  0  0  0  0  0  1  0  0]
            [ 0  0  0  0  0  0  0  0  1  0]
            W: Vector space of degree 10 and dimension 2 over Rational Field
            Basis matrix:
            [1 0 0 0 0 0 0 0 0 0]
            [0 0 1 0 0 0 0 0 0 0]
        """
    homology = cohomology

class Differential_multigraded(Differential):
    """
    Differential of a commutative multi-graded algebra.
    """
    def __init__(self, A, im_gens) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: A.<a,b,c> = GradedCommutativeAlgebra(QQ, degrees=((1, 0), (0, 1), (0, 2)))
            sage: d = A.differential({a: c})

        We skip the category test because homsets/morphisms aren't
        proper parents/elements yet::

            sage: TestSuite(d).run(skip='_test_category')
        """
    @cached_method
    def differential_matrix_multigraded(self, n, total: bool = False):
        """
        The matrix that gives the differential in degree ``n``.

        .. TODO::

            Rename this to ``differential_matrix`` once inheritance,
            overriding, and cached methods work together better. See
            :issue:`17201`.

        INPUT:

        - ``n`` -- degree
        - ``total`` -- boolean (default: ``False``); if ``True``,
          return the matrix corresponding to total degree `n`

        If `n` is an integer rather than a multi-index, then the
        total degree is used in that case as well.

        EXAMPLES::

            sage: A.<a,b,c> = GradedCommutativeAlgebra(QQ, degrees=((1, 0), (0, 1), (0, 2)))
            sage: d = A.differential({a: c})
            sage: d.differential_matrix_multigraded((1, 0))
            [1]
            sage: d.differential_matrix_multigraded(1, total=True)
            [0 1]
            [0 0]
            sage: d.differential_matrix_multigraded((1, 0), total=True)
            [0 1]
            [0 0]
            sage: d.differential_matrix_multigraded(1)
            [0 1]
            [0 0]
        """
    def coboundaries(self, n, total: bool = False):
        """
        The `n`-th coboundary group of the algebra.

        This is a vector space over the base field `F`, and it is
        returned as a subspace of the vector space `F^d`, where the
        `n`-th homogeneous component has dimension `d`.

        INPUT:

        - ``n`` -- degree
        - ``total`` -- boolean (default: ``False``); if ``True``, return the
          coboundaries in total degree `n`

        If `n` is an integer rather than a multi-index, then the
        total degree is used in that case as well.

        EXAMPLES::

            sage: A.<a,b,c> = GradedCommutativeAlgebra(QQ, degrees=((1, 0), (0, 1), (0, 2)))
            sage: d = A.differential({a: c})
            sage: d.coboundaries((0, 2))
            Vector space of degree 1 and dimension 1 over Rational Field
            Basis matrix:
            [1]
            sage: d.coboundaries(2)
            Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix:
            [0 1]
        """
    def cocycles(self, n, total: bool = False):
        """
        The `n`-th cocycle group of the algebra.

        This is a vector space over the base field `F`, and it is
        returned as a subspace of the vector space `F^d`, where the
        `n`-th homogeneous component has dimension `d`.

        INPUT:

        - ``n`` -- degree
        - ``total`` -- boolean (default: ``False``); if ``True``, return the
          cocycles in total degree `n`

        If `n` is an integer rather than a multi-index, then the
        total degree is used in that case as well.

        EXAMPLES::

            sage: A.<a,b,c> = GradedCommutativeAlgebra(QQ, degrees=((1, 0), (0, 1), (0, 2)))
            sage: d = A.differential({a: c})
            sage: d.cocycles((0, 1))
            Vector space of degree 1 and dimension 1 over Rational Field
            Basis matrix:
            [1]
            sage: d.cocycles((0, 1), total=True)
            Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix:
            [0 1]
        """
    def cohomology_raw(self, n, total: bool = False):
        """
        The `n`-th cohomology group of the algebra.

        This is a vector space over the base ring, and it is returned
        as the quotient cocycles/coboundaries.

        INPUT:

        - ``n`` -- degree
        - ``total`` -- boolean (default: ``False``); if ``True``, return the
          cohomology in total degree `n`

        If `n` is an integer rather than a multi-index, then the
        total degree is used in that case as well.

        .. SEEALSO::

            :meth:`cohomology`

        EXAMPLES::

            sage: A.<a,b,c> = GradedCommutativeAlgebra(QQ, degrees=((1, 0), (0, 1), (0, 2)))
            sage: d = A.differential({a: c})
            sage: d.cohomology_raw((0, 2))
            Vector space quotient V/W of dimension 0 over Rational Field where
            V: Vector space of degree 1 and dimension 1 over Rational Field
            Basis matrix:
            [1]
            W: Vector space of degree 1 and dimension 1 over Rational Field
            Basis matrix:
            [1]

            sage: d.cohomology_raw(1)
            Vector space quotient V/W of dimension 1 over Rational Field where
            V: Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix:
            [0 1]
            W: Vector space of degree 2 and dimension 0 over Rational Field
            Basis matrix:
            []
        """
    def cohomology(self, n, total: bool = False):
        """
        The `n`-th cohomology group of the algebra.

        This is a vector space over the base ring, defined as the
        quotient cocycles/coboundaries. The elements of the quotient
        are lifted to the vector space of cocycles, and this is
        described in terms of those lifts.

        INPUT:

        - ``n`` -- degree
        - ``total`` -- boolean (default: ``False``); if ``True``, return the
          cohomology in total degree `n`

        If `n` is an integer rather than a multi-index, then the
        total degree is used in that case as well.

        .. SEEALSO::

            :meth:`cohomology_raw`

        EXAMPLES::

            sage: A.<a,b,c> = GradedCommutativeAlgebra(QQ, degrees=((1, 0), (0, 1), (0, 2)))
            sage: d = A.differential({a: c})
            sage: d.cohomology((0, 2))
            Free module generated by {} over Rational Field

            sage: d.cohomology(1)
            Free module generated by {[b]} over Rational Field
        """
    homology = cohomology

class GCAlgebra(UniqueRepresentation, QuotientRing_nc):
    '''
    A graded commutative algebra.

    INPUT:

    - ``base`` -- the base field

    - ``names`` -- (optional) names of the generators: a list of
      strings or a single string with the names separated by
      commas. If not specified, the generators are named "x0", "x1",
      ...

    - ``degrees`` -- (optional) a tuple or list specifying the degrees
      of the generators; if omitted, each generator is given degree
      1, and if both ``names`` and ``degrees`` are omitted, an error is
      raised.

    - ``R`` -- (default: ``None``) the ring over which the
      algebra is defined: if this is specified, the algebra is defined
      to be ``R/I``.

    - ``I`` -- (default: ``None``) an ideal in `R`. It is
      should include, among other relations, the squares of the
      generators of odd degree

    As described in the module-level documentation, these are graded
    algebras for which oddly graded elements anticommute and evenly
    graded elements commute.

    The arguments ``R`` and ``I`` are primarily for use by the
    :meth:`quotient` method.

    These algebras should be graded over the integers; multi-graded
    algebras should be constructed using
    :class:`GCAlgebra_multigraded` instead.

    EXAMPLES::

        sage: A.<a,b> = GradedCommutativeAlgebra(QQ, degrees = (2, 3))
        sage: a.degree()
        2
        sage: B = A.quotient(A.ideal(a**2*b))
        sage: B
        Graded Commutative Algebra with generators (\'a\', \'b\') in degrees (2, 3)
         with relations [a^2*b] over Rational Field
        sage: A.basis(7)
        [a^2*b]
        sage: B.basis(7)
        []

    Note that the function :func:`GradedCommutativeAlgebra` can also be used to
    construct these algebras.
    '''
    @staticmethod
    def __classcall__(cls, base, names=None, degrees=None, R=None, I=None, category=None):
        """
        Normalize the input for the :meth:`__init__` method and the
        unique representation.

        INPUT:

        - ``base`` -- the base ring of the algebra

        - ``names`` -- the names of the variables; by default, set to ``x1``,
          ``x2``, etc.

        - ``degrees`` -- the degrees of the generators; by default, set to 1

        - ``R`` -- an underlying `g`-algebra; only meant to be used by the
          quotient method

        - ``I`` -- a two-sided ideal in ``R``, with the desired relations;
          Only meant to be used by the quotient method

        TESTS::

            sage: A1 = GradedCommutativeAlgebra(GF(2), 'x,y', (3, 6))
            sage: A2 = GradedCommutativeAlgebra(GF(2), ['x', 'y'], [3, 6])
            sage: A1 is A2
            True

        Testing the single generator case (:issue:`25276`)::

            sage: A3.<z> = GradedCommutativeAlgebra(QQ)
            sage: z**2 == 0
            True
            sage: A4.<z> = GradedCommutativeAlgebra(QQ, degrees=[4])
            sage: z**2 == 0
            False
            sage: A5.<z> = GradedCommutativeAlgebra(GF(2))
            sage: z**2 == 0
            False
        """
    def __init__(self, base, R=None, I=None, names=None, degrees=None, category=None) -> None:
        """
        Initialize ``self``.

        INPUT:

        - ``base`` -- the base field

        - ``R`` -- (optional) the ring over which the algebra is defined

        - ``I`` -- (optional) an ideal over the corresponding `g`-algebra;
          it is meant to include, among other relations, the squares of the
          generators of odd degree

        - ``names`` -- (optional) the names of the generators; if omitted,
          this uses the names ``x0``, ``x1``, ...

        - ``degrees`` -- (optional) the degrees of the generators; if
          omitted, they are given degree 1

        EXAMPLES::

            sage: A.<x,y,z,t> = GradedCommutativeAlgebra(QQ)
            sage: TestSuite(A).run()
            sage: A = GradedCommutativeAlgebra(QQ, ('x','y','z'), [2,3,4])
            sage: TestSuite(A).run()
            sage: A = GradedCommutativeAlgebra(QQ, ('x','y','z','t'), [1,2,3,4])
            sage: TestSuite(A).run()
        """
    def basis(self, n):
        """
        Return a basis of the `n`-th homogeneous component of ``self``.

        EXAMPLES::

            sage: A.<x,y,z,t> = GradedCommutativeAlgebra(QQ, degrees=(1, 2, 2, 3))
            sage: A.basis(2)
            [y, z]
            sage: A.basis(3)
            [x*y, x*z, t]
            sage: A.basis(4)
            [y^2, y*z, z^2, x*t]
            sage: A.basis(5)
            [x*y^2, x*y*z, x*z^2, y*t, z*t]
            sage: A.basis(6)
            [y^3, y^2*z, y*z^2, z^3, x*y*t, x*z*t]
        """
    def quotient(self, I, check: bool = True):
        """
        Create the quotient of this algebra by a two-sided ideal ``I``.

        INPUT:

        - ``I`` -- a two-sided homogeneous ideal of this algebra

        - ``check`` -- boolean (default: ``True``); if ``True``, check whether
          ``I`` is generated by homogeneous elements

        EXAMPLES::

            sage: A.<x,y,z,t> = GradedCommutativeAlgebra(GF(5), degrees=(2, 2, 3, 4))
            sage: I = A.ideal([x*t+z^2, x*y - t])
            sage: B = A.quotient(I); B
            Graded Commutative Algebra with generators ('x', 'y', 'z', 't')
             in degrees (2, 2, 3, 4) with relations [x*t, x*y - t]
             over Finite Field of size 5
            sage: B(x*t)
            0
            sage: B(x*y)
            t
            sage: A.basis(7)
            [x^2*z, x*y*z, y^2*z, z*t]
            sage: B.basis(7)
            [x^2*z, y^2*z, z*t]
        """
    def differential(self, diff):
        """
        Construct a differential on ``self``.

        INPUT:

        - ``diff`` -- dictionary defining a differential

        The keys of the dictionary are generators of the algebra, and
        the associated values are their targets under the
        differential. Any generators which are not specified are
        assumed to have zero differential.

        EXAMPLES::

            sage: A.<x,y,z> = GradedCommutativeAlgebra(QQ, degrees=(1, 1, 2))
            sage: A.differential({y:x*y, x: x*y})
            Differential of Graded Commutative Algebra with generators ('x', 'y', 'z')
             in degrees (1, 1, 2) over Rational Field
              Defn: x --> x*y
                    y --> x*y
                    z --> 0
            sage: B.<a,b,c> = GradedCommutativeAlgebra(QQ, degrees=(1, 2, 2))
            sage: d = B.differential({b:a*c, c:a*c})
            sage: d(b*c)
            a*b*c + a*c^2
        """
    def cdg_algebra(self, differential):
        """
        Construct a differential graded commutative algebra from ``self``
        by specifying a differential.

        INPUT:

        - ``differential`` -- dictionary defining a differential or
          a map defining a valid differential

        The keys of the dictionary are generators of the algebra, and
        the associated values are their targets under the
        differential. Any generators which are not specified are
        assumed to have zero differential. Alternatively, the
        differential can be defined using the :meth:`differential`
        method; see below for an example.

        .. SEEALSO::

            :meth:`differential`

        EXAMPLES::

            sage: A.<a,b,c> = GradedCommutativeAlgebra(QQ, degrees=(1, 1, 1))
            sage: B = A.cdg_algebra({a: b*c, b: a*c})
            sage: B
            Commutative Differential Graded Algebra with generators ('a', 'b', 'c')
             in degrees (1, 1, 1) over Rational Field with differential:
                a --> b*c
                b --> a*c
                c --> 0

        Note that ``differential`` can also be a map::

            sage: d = A.differential({a: b*c, b: a*c})
            sage: d
            Differential of Graded Commutative Algebra with generators ('a', 'b', 'c')
             in degrees (1, 1, 1) over Rational Field
              Defn: a --> b*c
                    b --> a*c
                    c --> 0
            sage: A.cdg_algebra(d) is B
            True
        """
    class Element(QuotientRingElement):
        """
        An element of a graded commutative algebra.
        """
        def __init__(self, A, rep) -> None:
            """
            Initialize ``self``.

            INPUT:

            - ``parent`` -- the graded commutative algebra in which
              this element lies, viewed as a quotient `R / I`

            - ``rep`` -- a representative of the element in `R`; this is used
              as the internal representation of the element

            EXAMPLES::

                sage: B.<x,y> = GradedCommutativeAlgebra(QQ, degrees=(2, 2))
                sage: a = B({(1,1): -3, (2,5): 1/2})
                sage: a
                1/2*x^2*y^5 - 3*x*y
                sage: TestSuite(a).run()

                sage: b = x^2*y^3+2
                sage: b
                x^2*y^3 + 2
            """
        def degree(self, total: bool = False):
            """
            The degree of this element.

            If the element is not homogeneous, this returns the
            maximum of the degrees of its monomials.

            INPUT:

            - ``total`` -- ignored, present for compatibility with the
              multi-graded case

            EXAMPLES::

                sage: A.<x,y,z,t> = GradedCommutativeAlgebra(QQ, degrees=(1, 2, 3, 3))
                sage: el = z*t+2*x*y-y^2*z
                sage: el.degree()
                7
                sage: el.monomials()
                [y^2*z, z*t, x*y]
                sage: [i.degree() for i in el.monomials()]
                [7, 6, 3]

                sage: A(0).degree()
                Traceback (most recent call last):
                ...
                ValueError: the zero element does not have a well-defined degree
            """
        def is_homogeneous(self, total: bool = False):
            """
            Return ``True`` if ``self`` is homogeneous and ``False`` otherwise.

            INPUT:

            - ``total`` -- boolean (default: ``False``); only used in the
              multi-graded case, in which case if ``True``, check to see
              if ``self`` is homogeneous with respect to total degree

            EXAMPLES::

                sage: A.<x,y,z,t> = GradedCommutativeAlgebra(QQ, degrees=(1, 2, 3, 3))
                sage: el = z*t + 2*x*y - y^2*z
                sage: el.degree()
                7
                sage: el.monomials()
                [y^2*z, z*t, x*y]
                sage: [i.degree() for i in el.monomials()]
                [7, 6, 3]
                sage: el.is_homogeneous()
                False
                sage: em = y^3 - 5*z*t + 3/2*x*y*t
                sage: em.is_homogeneous()
                True
                sage: em.monomials()
                [y^3, x*y*t, z*t]
                sage: [i.degree() for i in em.monomials()]
                [6, 6, 6]

            The element 0 is homogeneous, even though it doesn't have
            a well-defined degree::

                sage: A(0).is_homogeneous()
                True

            A multi-graded example::

                sage: B.<c,d> = GradedCommutativeAlgebra(QQ, degrees=((2, 0), (0, 4)))
                sage: (c^2 - 1/2 * d).is_homogeneous()
                False
                sage: (c^2 - 1/2 * d).is_homogeneous(total=True)
                True
            """
        def homogeneous_parts(self):
            """
            Return the homogeneous parts of the element. The result is given as
            a dictionary indexed by degree.

            EXAMPLES::

                sage: A.<e1,e2,e3,e4,e5> = GradedCommutativeAlgebra(QQ)
                sage: a = e1*e3*e5-3*e2*e3*e5 + e1*e2 -2*e3 + e5
                sage: a.homogeneous_parts()
                {1: -2*e3 + e5, 2: e1*e2, 3: e1*e3*e5 - 3*e2*e3*e5}
            """
        def monomial_coefficients(self, copy: bool = True):
            """
            A dictionary that determines the element.

            The keys of this dictionary are the tuples of exponents of each
            monomial, and the values are the corresponding coefficients.

            EXAMPLES::

                sage: A.<x,y,z,t> = GradedCommutativeAlgebra(QQ, degrees=(1, 2, 2, 3))
                sage: elt = x*y - 5*y*z + 7*x*y^2*z^3*t
                sage: sorted(elt.monomial_coefficients().items())
                [((0, 1, 1, 0), -5), ((1, 1, 0, 0), 1), ((1, 2, 3, 1), 7)]

            ``dict`` is an alias::

                sage: sorted(elt.dict().items())
                [((0, 1, 1, 0), -5), ((1, 1, 0, 0), 1), ((1, 2, 3, 1), 7)]
            """
        dict = monomial_coefficients
        def __call__(self, *values, **kwargs):
            """
            Evaluate the reduced expression of this element at ``x``, where ``x``
            is either the tuple of values to evaluate in, a dictionary indicating
            to which value is each generator evaluated, or keywords giving
            the value to which generators should be evaluated.

            INPUT:

            - ``values`` -- (optional) either the values in which the variables
              will be evaluated or a dictionary

            OUTPUT: this element evaluated at the given values

            EXAMPLES::

                sage: A.<x,y,z,t> = GradedCommutativeAlgebra(QQ, degrees=(1, 2, 2, 3))
                sage: f = x*y - 5*y*z + 7*x*y^2*z^3*t
                sage: f(3, y, x^2, x*z)
                3*y
                sage: f(x=3)
                21*y^2*z^3*t - 5*y*z + 3*y
                sage: f({x:3, z:x^2})
                3*y

            If the wrong number of values is provided, it results in an error::

                sage: f(3, 5, y)
                Traceback (most recent call last):
                ...
                ValueError: number of arguments does not match number of variables in parent

            It is also possible to use keywords like this::

                sage: A.<x,y,z,t> = GradedCommutativeAlgebra(QQ, degrees=(1, 2, 2, 3))
                sage: f = x*y - 5*y*z + 7*x*y^2*z^3*t
                sage: f(x=3)
                21*y^2*z^3*t - 5*y*z + 3*y
                sage: f(t=x,y=z)
                -5*z^2 + x*z

            If both a dictionary and keywords are used, only the dictionary is
            considered::

                sage: A.<x,y,z,t> = GradedCommutativeAlgebra(QQ, degrees=(1, 2, 2, 3))
                sage: f = x*y - 5*y*z + 7*x*y^2*z^3*t
                sage: f({x:1}, t=x,y=z)
                7*y^2*z^3*t - 5*y*z + y
            """
        def basis_coefficients(self, total: bool = False):
            """
            Return the coefficients of this homogeneous element with
            respect to the basis in its degree.

            For example, if this is the sum of the `0`-th and `2`-nd basis
            elements, return the list ``[1, 0, 1]``.

            Raise an error if the element is not homogeneous.

            INPUT:

            - ``total`` -- boolean (default: ``False``); this
              is only used in the multi-graded case, in which case if
              ``True``, it returns the coefficients with respect to
              the basis for the total degree of this element

            OUTPUT: list of elements of the base field

            EXAMPLES::

                sage: A.<x,y,z,t> = GradedCommutativeAlgebra(QQ, degrees=(1, 2, 2, 3))
                sage: A.basis(3)
                [x*y, x*z, t]
                sage: (t + 3*x*y).basis_coefficients()
                [3, 0, 1]
                sage: (t + x).basis_coefficients()
                Traceback (most recent call last):
                ...
                ValueError: this element is not homogeneous

                sage: B.<c,d> = GradedCommutativeAlgebra(QQ, degrees=((2,0), (0,4)))
                sage: B.basis(4)
                [c^2, d]
                sage: (c^2 - 1/2 * d).basis_coefficients(total=True)
                [1, -1/2]
                sage: (c^2 - 1/2 * d).basis_coefficients()
                Traceback (most recent call last):
                ...
                ValueError: this element is not homogeneous
            """

class GCAlgebra_multigraded(GCAlgebra):
    """
    A multi-graded commutative algebra.

    INPUT:

    - ``base`` -- the base field

    - ``degrees`` -- tuple or list specifying the degrees of the
      generators

    - ``names`` -- (optional) names of the generators: a list of
      strings or a single string with the names separated by
      commas; if not specified, the generators are named ``x0``,
      ``x1``, ...

    - ``R`` -- (optional) the ring over which the algebra is defined

    - ``I`` -- (optional) an ideal in ``R``; it should include, among
      other relations, the squares of the generators of odd degree

    When defining such an algebra, each entry of ``degrees`` should be
    a list, tuple, or element of an additive (free) abelian
    group. Regardless of how the user specifies the degrees, Sage
    converts them to group elements.

    The arguments ``R`` and ``I`` are primarily for use by the
    :meth:`GCAlgebra.quotient` method.

    EXAMPLES::

        sage: A.<a,b,c> = GradedCommutativeAlgebra(QQ, degrees=((1,0), (0,1), (1,1)))
        sage: A
        Graded Commutative Algebra with generators ('a', 'b', 'c')
         in degrees ((1, 0), (0, 1), (1, 1)) over Rational Field
        sage: a**2
        0
        sage: c.degree(total=True)
        2
        sage: c**2
        c^2
        sage: c.degree()
        (1, 1)

    Although the degree of ``c`` was defined using a Python tuple, it
    is returned as an element of an additive abelian group, and so it
    can be manipulated via arithmetic operations::

        sage: type(c.degree())
        <class 'sage.groups.additive_abelian.additive_abelian_group.AdditiveAbelianGroup_fixed_gens_with_category.element_class'>
        sage: 2 * c.degree()
        (2, 2)
        sage: (a*b).degree() == a.degree() + b.degree()
        True

    The :meth:`basis` method and the :meth:`Element.degree` method both accept
    the boolean keyword ``total``. If ``True``, use the total degree::

        sage: A.basis(2, total=True)
        [a*b, c]
        sage: c.degree(total=True)
        2
    """
    def __init__(self, base, degrees, names=None, R=None, I=None, category=None) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: A.<a,b,c> = GradedCommutativeAlgebra(QQ, degrees=((1,0), (0,1), (1,1)))
            sage: TestSuite(A).run()
            sage: B.<w> = GradedCommutativeAlgebra(GF(2), degrees=((3,2),))
            sage: TestSuite(B).run(skip=['_test_construction'])
            sage: C = GradedCommutativeAlgebra(GF(7), degrees=((3,2),))
            sage: TestSuite(C).run()
        """
    def quotient(self, I, check: bool = True):
        """
        Create the quotient of this algebra by a two-sided ideal ``I``.

        INPUT:

        - ``I`` -- a two-sided homogeneous ideal of this algebra

        - ``check`` -- boolean (default: ``True``); if ``True``, check whether
          ``I`` is generated by homogeneous elements

        EXAMPLES::

            sage: A.<x,y,z,t> = GradedCommutativeAlgebra(GF(5), degrees=(2, 2, 3, 4))
            sage: I = A.ideal([x*t+z^2, x*y - t])
            sage: B = A.quotient(I)
            sage: B
            Graded Commutative Algebra with generators ('x', 'y', 'z', 't')
             in degrees (2, 2, 3, 4) with relations [x*t, x*y - t]
             over Finite Field of size 5
            sage: B(x*t)
            0
            sage: B(x*y)
            t
            sage: A.basis(7)
            [x^2*z, x*y*z, y^2*z, z*t]
            sage: B.basis(7)
            [x^2*z, y^2*z, z*t]
        """
    def basis(self, n, total: bool = False):
        """
        Basis in degree `n`.

        - ``n`` -- degree or integer
        - ``total`` -- boolean (default: ``False``); if ``True``, return the
          basis in total degree `n`

        If `n` is an integer rather than a multi-index, then the
        total degree is used in that case as well.

        EXAMPLES::

            sage: A.<a,b,c> = GradedCommutativeAlgebra(GF(2), degrees=((1,0), (0,1), (1,1)))
            sage: A.basis((1,1))
            [a*b, c]
            sage: A.basis(2, total=True)
            [a^2, a*b, b^2, c]

        Since 2 is a not a multi-index, we don't need to specify that ``total``
        is ``True``::

            sage: A.basis(2)
            [a^2, a*b, b^2, c]

        If ``total`` is ``True``, then `n` can still be a tuple, list,
        etc., and its total degree is used instead::

            sage: A.basis((1,1), total=True)
            [a^2, a*b, b^2, c]
        """
    def differential(self, diff):
        """
        Construct a differential on ``self``.

        INPUT:

        - ``diff`` -- dictionary defining a differential

        The keys of the dictionary are generators of the algebra, and
        the associated values are their targets under the
        differential. Any generators which are not specified are
        assumed to have zero differential.

        EXAMPLES::

            sage: A.<a,b,c> = GradedCommutativeAlgebra(QQ, degrees=((1,0), (0, 1), (0,2)))
            sage: A.differential({a: c})
            Differential of Graded Commutative Algebra with generators ('a', 'b', 'c')
             in degrees ((1, 0), (0, 1), (0, 2)) over Rational Field
              Defn: a --> c
                    b --> 0
                    c --> 0
        """
    def cdg_algebra(self, differential):
        """
        Construct a differential graded commutative algebra from ``self``
        by specifying a differential.

        INPUT:

        - ``differential`` -- dictionary defining a differential or
          a map defining a valid differential

        The keys of the dictionary are generators of the algebra, and
        the associated values are their targets under the
        differential. Any generators which are not specified are
        assumed to have zero differential. Alternatively, the
        differential can be defined using the :meth:`differential`
        method; see below for an example.

        .. SEEALSO::

            :meth:`differential`

        EXAMPLES::

            sage: A.<a,b,c> = GradedCommutativeAlgebra(QQ, degrees=((1,0), (0, 1), (0,2)))
            sage: A.cdg_algebra({a: c})
            Commutative Differential Graded Algebra with generators ('a', 'b', 'c')
             in degrees ((1, 0), (0, 1), (0, 2)) over Rational Field with differential:
               a --> c
               b --> 0
               c --> 0
            sage: d = A.differential({a: c})
            sage: A.cdg_algebra(d)
            Commutative Differential Graded Algebra with generators ('a', 'b', 'c')
             in degrees ((1, 0), (0, 1), (0, 2)) over Rational Field with differential:
               a --> c
               b --> 0
               c --> 0
        """
    class Element(GCAlgebra.Element):
        def degree(self, total: bool = False):
            """
            Return the degree of this element.

            INPUT:

            - ``total`` -- if ``True``, return the total degree, an
              integer; otherwise, return the degree as an element of
              an additive free abelian group

            If not requesting the total degree, raise an error if the
            element is not homogeneous.

            EXAMPLES::

                sage: A.<a,b,c> = GradedCommutativeAlgebra(GF(2),
                ....:                                      degrees=((1,0), (0,1), (1,1)))
                sage: (a**2*b).degree()
                (2, 1)
                sage: (a**2*b).degree(total=True)
                3
                sage: (a**2*b + c).degree()
                Traceback (most recent call last):
                ...
                ValueError: this element is not homogeneous
                sage: (a**2*b + c).degree(total=True)
                3
                sage: A(0).degree()
                Traceback (most recent call last):
                ...
                ValueError: the zero element does not have a well-defined degree
            """

class DifferentialGCAlgebra(GCAlgebra):
    """
    A commutative differential graded algebra.

    INPUT:

    - ``A`` -- a graded commutative algebra; that is, an instance
      of :class:`GCAlgebra`

    - ``differential`` -- a differential

    As described in the module-level documentation, these are graded
    algebras for which oddly graded elements anticommute and evenly
    graded elements commute, and on which there is a graded
    differential of degree 1.

    These algebras should be graded over the integers; multi-graded
    algebras should be constructed using
    :class:`DifferentialGCAlgebra_multigraded` instead.

    Note that a natural way to construct these is to use the
    :func:`GradedCommutativeAlgebra` function and the
    :meth:`GCAlgebra.cdg_algebra` method.

    EXAMPLES::

        sage: A.<x,y,z,t> = GradedCommutativeAlgebra(QQ, degrees=(2, 2, 3, 3))
        sage: A.cdg_algebra({z: x*y})
        Commutative Differential Graded Algebra with generators ('x', 'y', 'z', 't')
         in degrees (2, 2, 3, 3) over Rational Field with differential:
            x --> 0
            y --> 0
            z --> x*y
            t --> 0

    Alternatively, starting with :func:`GradedCommutativeAlgebra`::

        sage: A.<x,y,z,t> = GradedCommutativeAlgebra(QQ, degrees=(2, 2, 3, 3))
        sage: A.cdg_algebra(differential={z: x*y})
        Commutative Differential Graded Algebra with generators ('x', 'y', 'z', 't')
         in degrees (2, 2, 3, 3) over Rational Field with differential:
            x --> 0
            y --> 0
            z --> x*y
            t --> 0

    See the function :func:`GradedCommutativeAlgebra` for more examples.
    """
    @staticmethod
    def __classcall__(cls, A, differential):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: A.<a,b,c> = GradedCommutativeAlgebra(QQ, degrees=(1,1,1))
            sage: D1 = A.cdg_algebra({a: b*c, b: a*c})
            sage: D2 = A.cdg_algebra(D1.differential())
            sage: D1 is D2
            True
            sage: from sage.algebras.commutative_dga import DifferentialGCAlgebra
            sage: D1 is DifferentialGCAlgebra(A, {a: b*c, b: a*c, c: 0})
            True
        """
    def __init__(self, A, differential) -> None:
        """
        Initialize ``self``.

        INPUT:

        - ``A`` -- a graded commutative algebra

        - ``differential`` -- a differential

        EXAMPLES::

            sage: A.<x,y,z,t> = GradedCommutativeAlgebra(QQ, degrees=(2, 2, 3, 3))
            sage: D = A.cdg_algebra({z: x*y})
            sage: TestSuite(D).run()

        The degree of the differential must be 1::

            sage: A.<a,b,c> = GradedCommutativeAlgebra(QQ, degrees=(1,1,1))
            sage: A.cdg_algebra({a: a*b*c})
            Traceback (most recent call last):
            ...
            ValueError: the given dictionary does not determine a degree 1 map

        The differential composed with itself must be zero::

            sage: A.<a,b,c> = GradedCommutativeAlgebra(QQ, degrees=(1,2,3))
            sage: A.cdg_algebra({a:b, b:c})
            Traceback (most recent call last):
            ...
            ValueError: the given dictionary does not determine a valid differential
        """
    def cdg_algebra(self, differential):
        """
        Construct a differential graded commutative algebra from the underlying
        graded commutative algebra by specifying a differential. This may be used
        to get a new differential over the same algebra structure.

        INPUT:

        - ``differential`` -- dictionary defining a differential or
          a map defining a valid differential

        The keys of the dictionary are generators of the algebra, and
        the associated values are their targets under the
        differential. Any generators which are not specified are
        assumed to have zero differential. Alternatively, the
        differential can be defined using the :meth:`differential`
        method; see below for an example.

        .. SEEALSO::

            :meth:`differential`

        EXAMPLES::

            sage: A.<x,y,z,t> = GradedCommutativeAlgebra(GF(5), degrees=(2, 3, 2, 4))
            sage: B = A.quotient(A.ideal(x^3-z*t))
            sage: C = B.cdg_algebra({y:t})
            sage: C
            Commutative Differential Graded Algebra with generators ('x', 'y', 'z', 't')
             in degrees (2, 3, 2, 4) with relations [x^3 - z*t]
             over Finite Field of size 5 with differential:
            x --> 0
            y --> t
            z --> 0
            t --> 0
            sage: C.cdg_algebra({})
            Commutative Differential Graded Algebra with generators ('x', 'y', 'z', 't')
             in degrees (2, 3, 2, 4) with relations [x^3 - z*t]
             over Finite Field of size 5 with differential:
            x --> 0
            y --> 0
            z --> 0
            t --> 0
        """
    def graded_commutative_algebra(self):
        """
        Return the base graded commutative algebra of ``self``.

        EXAMPLES::

            sage: A.<x,y,z,t> = GradedCommutativeAlgebra(QQ, degrees=(2, 2, 3, 3))
            sage: D = A.cdg_algebra({z: x*y})
            sage: D.graded_commutative_algebra() == A
            True
        """
    def quotient(self, I, check: bool = True):
        """
        Create the quotient of this algebra by a two-sided ideal ``I``.

        INPUT:

        - ``I`` -- a two-sided homogeneous ideal of this algebra

        - ``check`` -- boolean (default: ``True``); if ``True``, check whether
          ``I`` is generated by homogeneous elements

        EXAMPLES::

            sage: A.<x,y,z> = GradedCommutativeAlgebra(QQ, degrees=(1,1,2))
            sage: B = A.cdg_algebra({y:x*y, z:x*z})
            sage: B.inject_variables()
            Defining x, y, z
            sage: I = B.ideal([y*z])
            sage: C = B.quotient(I)
            sage: (y*z).differential()
            2*x*y*z
            sage: C((y*z).differential())
            0
            sage: C(y*z)
            0

        It is checked that the differential maps the ideal into itself, to make
        sure that the quotient inherits a differential structure::

            sage: A.<x,y,z> = GradedCommutativeAlgebra(QQ, degrees=(1,2,2))
            sage: B = A.cdg_algebra({x:y})
            sage: B.quotient(B.ideal(y*x))
            Traceback (most recent call last):
            ...
            ValueError: the differential does not preserve the ideal
            sage: B.quotient(B.ideal(x))
            Traceback (most recent call last):
            ...
            ValueError: the differential does not preserve the ideal
        """
    def differential(self, x=None):
        """
        The differential of ``self``.

        This returns a map, and so it may be evaluated on elements of
        this algebra.

        EXAMPLES::

            sage: A.<x,y,z> = GradedCommutativeAlgebra(QQ, degrees=(1,1,2))
            sage: B = A.cdg_algebra({y:x*y, x: y*x})
            sage: d = B.differential(); d
            Differential of Commutative Differential Graded Algebra
             with generators ('x', 'y', 'z') in degrees (1, 1, 2) over Rational Field
              Defn: x --> -x*y
                    y --> x*y
                    z --> 0
            sage: d(y)
            x*y
        """
    def coboundaries(self, n):
        """
        The `n`-th coboundary group of the algebra.

        This is a vector space over the base field `F`, and it is
        returned as a subspace of the vector space `F^d`, where the
        `n`-th homogeneous component has dimension `d`.

        INPUT:

        - ``n`` -- degree

        EXAMPLES::

            sage: A.<x,y,z> = GradedCommutativeAlgebra(QQ, degrees=(1,1,2))
            sage: B = A.cdg_algebra(differential={z: x*z})
            sage: B.coboundaries(2)
            Vector space of degree 2 and dimension 0 over Rational Field
            Basis matrix:
            []
            sage: B.coboundaries(3)
            Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix:
            [1 0]
            sage: B.basis(3)
            [x*z, y*z]
        """
    def cocycles(self, n):
        """
        The `n`-th cocycle group of the algebra.

        This is a vector space over the base field `F`, and it is
        returned as a subspace of the vector space `F^d`, where the
        `n`-th homogeneous component has dimension `d`.

        INPUT:

        - ``n`` -- degree

        EXAMPLES::

            sage: A.<x,y,z> = GradedCommutativeAlgebra(QQ, degrees=(1,1,2))
            sage: B = A.cdg_algebra(differential={z: x*z})
            sage: B.cocycles(2)
            Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix:
            [1 0]
            sage: B.basis(2)
            [x*y, z]
        """
    def cohomology_raw(self, n):
        """
        The `n`-th cohomology group of ``self``.

        This is a vector space over the base ring, and it is returned
        as the quotient cocycles/coboundaries.

        INPUT:

        - ``n`` -- degree

        EXAMPLES::

            sage: A.<x,y,z,t> = GradedCommutativeAlgebra(QQ, degrees = (2,2,3,4))
            sage: B = A.cdg_algebra({t: x*z, x: z, y: z})
            sage: B.cohomology_raw(4)
            Vector space quotient V/W of dimension 2 over Rational Field where
            V: Vector space of degree 4 and dimension 2 over Rational Field
            Basis matrix:
            [   1    0    0   -2]
            [   0    1 -1/2   -1]
            W: Vector space of degree 4 and dimension 0 over Rational Field
            Basis matrix:
            []

        Compare to :meth:`cohomology`::

            sage: B.cohomology(4)
            Free module generated by {[x^2 - 2*t], [x*y - 1/2*y^2 - t]} over Rational Field
        """
    def cohomology(self, n):
        """
        The `n`-th cohomology group of ``self``.

        This is a vector space over the base ring, defined as the
        quotient cocycles/coboundaries. The elements of the quotient
        are lifted to the vector space of cocycles, and this is
        described in terms of those lifts.

        INPUT:

        - ``n`` -- degree

        EXAMPLES::

            sage: A.<a,b,c,d,e> = GradedCommutativeAlgebra(QQ, degrees=(1,1,1,1,1))
            sage: B = A.cdg_algebra({d: a*b, e: b*c})
            sage: B.cohomology(2)
            Free module generated by {[a*c], [a*d], [b*d], [c*d - a*e], [b*e], [c*e]}
             over Rational Field

        Compare to :meth:`cohomology_raw`::

            sage: B.cohomology_raw(2)
            Vector space quotient V/W of dimension 6 over Rational Field where
            V: Vector space of degree 10 and dimension 8 over Rational Field
            Basis matrix:
            [ 1  0  0  0  0  0  0  0  0  0]
            [ 0  1  0  0  0  0  0  0  0  0]
            [ 0  0  1  0  0  0  0  0  0  0]
            [ 0  0  0  1  0  0  0  0  0  0]
            [ 0  0  0  0  1  0  0  0  0  0]
            [ 0  0  0  0  0  1 -1  0  0  0]
            [ 0  0  0  0  0  0  0  1  0  0]
            [ 0  0  0  0  0  0  0  0  1  0]
            W: Vector space of degree 10 and dimension 2 over Rational Field
            Basis matrix:
            [1 0 0 0 0 0 0 0 0 0]
            [0 0 1 0 0 0 0 0 0 0]

        TESTS:

        Check that the issue discovered in :issue:`28155` is solved::

            sage: A.<e1,e2,e3,e4,e5> = GradedCommutativeAlgebra(QQ)
            sage: B = A.cdg_algebra({e5:e1*e2+e3*e4})
            sage: B.cohomology(3) is B.cohomology(3)
            True
        """
    homology = cohomology
    def cohomology_generators(self, max_degree):
        """
        Return lifts of algebra generators for cohomology in degrees at
        most ``max_degree``.

        INPUT:

        - ``max_degree`` -- integer

        OUTPUT:

        A dictionary keyed by degree, where the corresponding
        value is a list of cohomology generators in that degree.
        Actually, the elements are lifts of cohomology generators,
        which means that they lie in this differential graded
        algebra. It also means that they are only well-defined up to
        cohomology, not on the nose.

        ALGORITHM:

        Reduce a basis of the `n`-th cohomology modulo all the degree `n`
        products of the lower degree cohomologies.

        EXAMPLES::

            sage: A.<a,x,y> = GradedCommutativeAlgebra(QQ, degrees=(1,2,2))
            sage: B = A.cdg_algebra(differential={y: a*x})
            sage: B.cohomology_generators(3)
            {1: [a], 2: [x], 3: [a*y]}

        The previous example has infinitely generated cohomology:
        `a y^n` is a cohomology generator for each `n`::

            sage: B.cohomology_generators(10)
            {1: [a], 2: [x], 3: [a*y], 5: [a*y^2], 7: [a*y^3], 9: [a*y^4]}

        In contrast, the corresponding algebra in characteristic `p`
        has finitely generated cohomology::

            sage: A3.<a,x,y> = GradedCommutativeAlgebra(GF(3), degrees=(1,2,2))
            sage: B3 = A3.cdg_algebra(differential={y: a*x})
            sage: B3.cohomology_generators(16)
            {1: [a], 2: [x], 3: [a*y], 5: [a*y^2], 6: [y^3]}

        This method works with both singly graded and multi-graded algebras::

            sage: Cs.<a,b,c,d> = GradedCommutativeAlgebra(GF(2), degrees=(1,2,2,3))
            sage: Ds = Cs.cdg_algebra({a:c, b:d})
            sage: Ds.cohomology_generators(10)
            {2: [a^2], 4: [b^2]}

            sage: Cm.<a,b,c,d> = GradedCommutativeAlgebra(GF(2),
            ....:                                         degrees=((1,0), (1,1),
            ....:                                                  (0,2), (0,3)))
            sage: Dm = Cm.cdg_algebra({a:c, b:d})
            sage: Dm.cohomology_generators(10)
            {2: [a^2], 4: [b^2]}

        TESTS:

        Test that coboundaries do not appear as cohomology generators::

            sage: X.<x,y> = GradedCommutativeAlgebra(QQ, degrees=(1,2))
            sage: acyclic = X.cdg_algebra({x: y})
            sage: acyclic.cohomology_generators(3)
            {}

        Test that redundant generators are eliminated::

            sage: A.<e1,e2,e3,e4> = GradedCommutativeAlgebra(QQ)
            sage: d = A.differential({e1:e4*e3,e2:e4*e3})
            sage: B = A.cdg_algebra(d)
            sage: B.cohomology_generators(3)
            {1: [e1 - e2, e3, e4], 2: [e1*e3, e1*e4]}
        """
    def minimal_model(self, i: int = 3, max_iterations: int = 3, partial_result: bool = False):
        """
        Try to compute a map from a `i`-minimal gcda that is a
        `i`-quasi-isomorphism to ``self``.

        INPUT:

        - ``i`` -- integer (default: `3`); degree to which the result is
          required to induce an isomorphism in cohomology, and the domain is
          required to be minimal

        - ``max_iterations`` -- integer (default: `3`); the number of
          iterations of the method at each degree. If the algorithm does not
          finish in this many iterations at each degree, an error is raised,
          or the partial result computed up to that point is returned, deppending
          on the ``partial_result`` flag.

        - ``partial_result`` -- boolean (default: ``False``); whether to return
          the partial result if the ``max_iterations`` limit is reached

        OUTPUT:

        A morphism from a minimal Sullivan (up to degree ``i``) CDGA's to self,
        that induces an isomorphism in cohomology up to degree ``i``, and a
        monomorphism in degree ``i+1``.

        EXAMPLES::

            sage: S.<x, y, z> = GradedCommutativeAlgebra(QQ, degrees = (1, 1, 2))
            sage: d = S.differential({x:x*y, y:x*y})
            sage: R = S.cdg_algebra(d)
            sage: p = R.minimal_model()
            sage: T = p.domain()
            sage: p
            Commutative Differential Graded Algebra morphism:
              From: Commutative Differential Graded Algebra
                    with generators ('x1_0', 'x2_0') in degrees (1, 2)
                    over Rational Field with differential:
                      x1_0 --> 0
                      x2_0 --> 0
              To:   Commutative Differential Graded Algebra
                    with generators ('x', 'y', 'z') in degrees (1, 1, 2)
                    over Rational Field with differential:
                      x --> x*y
                      y --> x*y
                      z --> 0
              Defn: (x1_0, x2_0) --> (x - y, z)
            sage: R.cohomology(1)
            Free module generated by {[x - y]} over Rational Field
            sage: T.cohomology(1)
            Free module generated by {[x1_0]} over Rational Field
            sage: [p(g.representative()) for g in T.cohomology(1).basis().keys()]
            [x - y]
            sage: R.cohomology(2)
            Free module generated by {[z]} over Rational Field
            sage: T.cohomology(2)
            Free module generated by {[x2_0]} over Rational Field
            sage: [p(g.representative()) for g in T.cohomology(2).basis().keys()]
            [z]


            sage: A.<e1, e2, e3, e4, e5, e6, e7> = GradedCommutativeAlgebra(QQ)
            sage: d = A.differential({e1:e1*e7, e2:e2*e7, e3:-e3*e7, e4:-e4*e7})
            sage: B = A.cdg_algebra(d)
            sage: phi = B.minimal_model(i=3)
            sage: M = phi.domain()
            sage: M
            Commutative Differential Graded Algebra with generators
             ('x1_0', 'x1_1', 'x1_2', 'x2_0', 'x2_1', 'x2_2', 'x2_3',
              'y3_0', 'y3_1', 'y3_2', 'y3_3', 'y3_4', 'y3_5', 'y3_6', 'y3_7', 'y3_8')
             in degrees (1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3)
             over Rational Field with differential:
               x1_0 --> 0
               x1_1 --> 0
               x1_2 --> 0
               x2_0 --> 0
               x2_1 --> 0
               x2_2 --> 0
               x2_3 --> 0
               y3_0 --> x2_0^2
               y3_1 --> x2_0*x2_1
               y3_2 --> x2_1^2
               y3_3 --> x2_0*x2_2
               y3_4 --> x2_1*x2_2 + x2_0*x2_3
               y3_5 --> x2_2^2
               y3_6 --> x2_1*x2_3
               y3_7 --> x2_2*x2_3
               y3_8 --> x2_3^2

            sage: phi
            Commutative Differential Graded Algebra morphism:
              From: Commutative Differential Graded Algebra with generators
                    ('x1_0', 'x1_1', 'x1_2', 'x2_0', 'x2_1', 'x2_2', 'x2_3',
                     'y3_0', 'y3_1', 'y3_2', 'y3_3', 'y3_4', 'y3_5', 'y3_6', 'y3_7', 'y3_8')
                    in degrees (1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3)
                    over Rational Field with differential:
                      x1_0 --> 0
                      x1_1 --> 0
                      x1_2 --> 0
                      x2_0 --> 0
                      x2_1 --> 0
                      x2_2 --> 0
                      x2_3 --> 0
                      y3_0 --> x2_0^2
                      y3_1 --> x2_0*x2_1
                      y3_2 --> x2_1^2
                      y3_3 --> x2_0*x2_2
                      y3_4 --> x2_1*x2_2 + x2_0*x2_3
                      y3_5 --> x2_2^2
                      y3_6 --> x2_1*x2_3
                      y3_7 --> x2_2*x2_3
                      y3_8 --> x2_3^2
              To:   Commutative Differential Graded Algebra with generators
                    ('e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7')
                    in degrees (1, 1, 1, 1, 1, 1, 1) over Rational Field with differential:
                      e1 --> e1*e7
                      e2 --> e2*e7
                      e3 --> -e3*e7
                      e4 --> -e4*e7
                      e5 --> 0
                      e6 --> 0
                      e7 --> 0
              Defn: (x1_0, x1_1, x1_2, x2_0, x2_1, x2_2, x2_3,
                     y3_0, y3_1, y3_2, y3_3, y3_4, y3_5, y3_6, y3_7, y3_8)
                    --> (e5, e6, e7, e1*e3, e2*e3, e1*e4, e2*e4, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            sage: [B.cohomology(i).dimension() for i in [1..3]]
            [3, 7, 13]
            sage: [M.cohomology(i).dimension() for i in [1..3]]
            [3, 7, 13]

        ALGORITHM:

        We follow the algorithm described in [Man2019]_. It consists in
        constructing the minimal Sullivan algebra ``S`` by iteratively adding
        generators to it. Start with one closed generator of degree 1 for each
        element in the basis of the first cohomology of the algebra. Then
        proceed degree by degree. At each degree `d`, we keep adding generators
        of degree `d-1` whose differential kills the elements in the kernel of
        the map `H^d(S)\\to H^d(self)`. Once this map is made injective, we add
        the needed closed generators in degree `d` to make it surjective.

        .. WARNING::

            The method is not granted to finish (it can't, since the minimal
            model could be infinitely generated in some degrees).
            The parameter ``max_iterations`` controls how many iterations of
            the method are attempted at each degree. In case they are not
            enough, an exception is raised. If you think that the result will
            be finitely generated, you can try to run it again with a higher
            value for ``max_iterations``.

        .. SEEALSO::

            :wikipedia:`Rational_homotopy_theory#Sullivan_algebras`

        TESTS::

            sage: A.<x, y, z, t> = GradedCommutativeAlgebra(QQ,degrees = (1, 2, 3, 3))
            sage: d = A.differential({x:y})
            sage: B = A.cdg_algebra(d)
            sage: B.minimal_model(i=3)
            Commutative Differential Graded Algebra morphism:
              From: Commutative Differential Graded Algebra with generators ('x3_0', 'x3_1') in degrees (3, 3) over Rational Field with differential:
               x3_0 --> 0
               x3_1 --> 0
              To:   Commutative Differential Graded Algebra with generators ('x', 'y', 'z', 't') in degrees (1, 2, 3, 3) over Rational Field with differential:
               x --> y
               y --> 0
               z --> 0
               t --> 0
              Defn: (x3_0, x3_1) --> (z, t)

        ::

            sage: A.<a,b,c> = GradedCommutativeAlgebra(QQ)
            sage: I = A.ideal([a*b-a*c+b*c])
            sage: B = A.quotient(I)
            sage: S = B.cdg_algebra({})
            sage: S.minimal_model()
            Traceback (most recent call last):
            ...
            ValueError: could not cover all relations in max iterations in degree 2
            sage: S.minimal_model(partial_result=True)
            Commutative Differential Graded Algebra morphism:
              From: Commutative Differential Graded Algebra with generators
               ('x1_0', 'x1_1', 'x1_2', 'y1_0', 'y1_1', 'y1_2') in degrees (1, 1, 1, 1, 1, 1)
                over Rational Field with differential:
               x1_0 --> 0
               x1_1 --> 0
               x1_2 --> 0
               y1_0 --> x1_0*x1_1 - x1_0*x1_2 + x1_1*x1_2
               y1_1 --> x1_0*y1_0 - x1_2*y1_0
               y1_2 --> x1_1*y1_0 - x1_2*y1_0
              To:   Commutative Differential Graded Algebra with generators ('a', 'b', 'c')
               in degrees (1, 1, 1) with relations [a*b - a*c + b*c] over Rational Field with differential:
               a --> 0
               b --> 0
               c --> 0
              Defn: (x1_0, x1_1, x1_2, y1_0, y1_1, y1_2) --> (a, b, c, 0, 0, 0)

        REFERENCES:

        - [Fel2001]_

        - [Man2019]_
        """
    def cohomology_algebra(self, max_degree: int = 3):
        """
        Compute a CDGA with trivial differential, that is isomorphic to the cohomology of
        ``self`` up to``max_degree``

        INPUT:

        - ``max_degree`` -- integer (default: `3`); degree to which the result is required to
          be isomorphic to ``self``'s cohomology

        EXAMPLES::

            sage: A.<e1, e2, e3, e4, e5, e6, e7> = GradedCommutativeAlgebra(QQ)
            sage: d = A.differential({e1:-e1*e6, e2:-e2*e6, e3:-e3*e6, e4:-e5*e6, e5:e4*e6})
            sage: B = A.cdg_algebra(d)
            sage: M = B.cohomology_algebra()
            sage: M
            Commutative Differential Graded Algebra with generators ('x0', 'x1', 'x2')
             in degrees (1, 1, 2) over Rational Field with differential:
               x0 --> 0
               x1 --> 0
               x2 --> 0
            sage: M.cohomology(1)
            Free module generated by {[x0], [x1]} over Rational Field
            sage: B.cohomology(1)
            Free module generated by {[e6], [e7]} over Rational Field
            sage: M.cohomology(2)
            Free module generated by {[x0*x1], [x2]} over Rational Field
            sage: B.cohomology(2)
            Free module generated by {[e4*e5], [e6*e7]} over Rational Field
            sage: M.cohomology(3)
            Free module generated by {[x0*x2], [x1*x2]} over Rational Field
            sage: B.cohomology(3)
            Free module generated by {[e4*e5*e6], [e4*e5*e7]} over Rational Field
        """
    def numerical_invariants(self, max_degree: int = 3, max_iterations: int = 3):
        """
        Return the numerical invariants of the algebra, up to degree ``d``. The
        numerical invariants reflect the number of generators added at each step
        of the construction of the minimal model.

        The numerical invariants are the dimensions of the subsequent Hirsch
        extensions used at each degree to compute the minimal model.

        INPUT:

        - ``max_degree`` -- integer (default: `3`); the degree up to which the
          numerical invariants are computed

        - ``max_iterations`` -- integer (default: `3`); the maximum number of iterations
          used to compute the minimal model, if it is not already cached

        EXAMPLES::

            sage: A.<e1, e2, e3> = GradedCommutativeAlgebra(QQ)
            sage: B = A.cdg_algebra({e3 : e1*e2})
            sage: B.minimal_model(4)
            Commutative Differential Graded Algebra morphism:
            From: Commutative Differential Graded Algebra with
                  generators ('x1_0', 'x1_1', 'y1_0') in degrees (1, 1, 1)
                  over Rational Field with differential:
                    x1_0 --> 0
                    x1_1 --> 0
                    y1_0 --> x1_0*x1_1
            To:   Commutative Differential Graded Algebra with
                  generators ('e1', 'e2', 'e3') in degrees (1, 1, 1)
                  over Rational Field with differential:
                    e1 --> 0
                    e2 --> 0
                    e3 --> e1*e2
            Defn: (x1_0, x1_1, y1_0) --> (e1, e2, e3)
            sage: B.numerical_invariants(2)
            {1: [2, 1, 0], 2: [0, 0]}

        ALGORITHM:

        The numerical invariants are stored as the minimal model is constructed.

        .. WARNING::

            The method is not granted to finish (it can't, since the minimal
            model could be infinitely generated in some degrees).
            The parameter ``max_iterations`` controls how many iterations of
            the method are attempted at each degree. In case they are not
            enough, an exception is raised. If you think that the result will
            be finitely generated, you can try to run it again with a higher
            value for ``max_iterations``.

        REFERENCES:

        For a precise definition and properties, see [Man2019]_ .
        """
    def is_formal(self, i, max_iterations: int = 3):
        """
        Check if the algebra is ``i``-formal. That is, if it is ``i``-quasi-isomorphic
        to its cohomology algebra.

        INPUT:

        - ``i`` -- integer; the degree up to which the formality is checked

        - ``max_iterations`` -- integer (default: `3`); the maximum number of
          iterations used in the computation of the minimal model

        .. WARNING::

            The method is not granted to finish (it can't, since the minimal
            model could be infinitely generated in some degrees).
            The parameter ``max_iterations`` controls how many iterations of
            the method are attempted at each degree. In case they are not
            enough, an exception is raised. If you think that the result will
            be finitely generated, you can try to run it again with a higher
            value for ``max_iterations``.

            Moreover, the method uses criteria that are often enough to conclude
            that the algebra is either formal or non-formal. However, it could
            happen that the used criteria can not determine the formality. In
            that case, an error is raised.

        EXAMPLES::

            sage: A.<e1, e2, e3, e4, e5> = GradedCommutativeAlgebra(QQ)
            sage: B = A.cdg_algebra({e5: e1*e2 + e3*e4})
            sage: B.is_formal(1)
            True
            sage: B.is_formal(2)
            False

        ALGORITHM:

        Apply the criteria in [Man2019]_ . Both the `i`-minimal model of the
        algebra and its cohomology algebra are computed. If the numerical
        invariants are different, the algebra is not `i`-formal.

        If the numerical invariants match, the `\\psi` condition is checked.
        """
    class Element(GCAlgebra.Element):
        def differential(self):
            """
            The differential on this element.

            EXAMPLES::

                sage: A.<x,y,z,t> = GradedCommutativeAlgebra(QQ, degrees=(2, 2, 3, 4))
                sage: B = A.cdg_algebra({t: x*z, x: z, y: z})
                sage: B.inject_variables()
                Defining x, y, z, t
                sage: x.differential()
                z
                sage: (-1/2 * x^2 + t).differential()
                0
            """
        def is_coboundary(self):
            """
            Return ``True`` if ``self`` is a coboundary and ``False``
            otherwise.

            This raises an error if the element is not homogeneous.

            EXAMPLES::

                sage: A.<a,b,c> = GradedCommutativeAlgebra(QQ, degrees=(1,2,2))
                sage: B = A.cdg_algebra(differential={b: a*c})
                sage: x,y,z = B.gens()
                sage: x.is_coboundary()
                False
                sage: (x*z).is_coboundary()
                True
                sage: (x*z + x*y).is_coboundary()
                False
                sage: (x*z + y**2).is_coboundary()
                Traceback (most recent call last):
                ...
                ValueError: this element is not homogeneous
            """
        def is_cohomologous_to(self, other):
            """
            Return ``True`` if ``self`` is cohomologous to ``other``
            and ``False`` otherwise.

            INPUT:

            - ``other`` -- another element of this algebra

            EXAMPLES::

                sage: A.<a,b,c,d> = GradedCommutativeAlgebra(QQ, degrees=(1,1,1,1))
                sage: B = A.cdg_algebra(differential={a: b*c-c*d})
                sage: w, x, y, z = B.gens()
                sage: (x*y).is_cohomologous_to(y*z)
                True
                sage: (x*y).is_cohomologous_to(x*z)
                False
                sage: (x*y).is_cohomologous_to(x*y)
                True

            Two elements whose difference is not homogeneous are
            cohomologous if and only if they are both coboundaries::

                sage: w.is_cohomologous_to(y*z)
                False
                sage: (x*y-y*z).is_cohomologous_to(x*y*z)
                True
                sage: (x*y*z).is_cohomologous_to(0)  # make sure 0 works
                True
            """
        def cohomology_class(self):
            """
            Return the cohomology class of a homogeneous cycle, as an element
            of the corresponding cohomology group.

            EXAMPLES::

                sage: A.<e1,e2,e3,e4,e5> = GradedCommutativeAlgebra(QQ)
                sage: B = A.cdg_algebra({e5: e1*e2+e3*e4})
                sage: B.inject_variables()
                Defining e1, e2, e3, e4, e5
                sage: a = e1*e3*e5 - 3*e2*e3*e5
                sage: a.cohomology_class()
                B[[e1*e3*e5]] - 3*B[[e2*e3*e5]]

            TESTS::

                sage: A.<a,b,c> = GradedCommutativeAlgebra(QQ, degrees=(1, 2, 3))
                sage: B = A.cdg_algebra({a: b})
                sage: B.inject_variables()
                Defining a, b, c
                sage: b.cohomology_class()
                0
                sage: b.cohomology_class().parent()
                Free module generated by {} over Rational Field

            Check that the issue detected in :issue:`28155` is solved::

                sage: A.<e1,e2,e3,e4,e5> = GradedCommutativeAlgebra(QQ)
                sage: B = A.cdg_algebra({e5: e1*e2+e3*e4})
                sage: B.inject_variables()
                Defining e1, e2, e3, e4, e5
                sage: a = e1*e3*e5 - 3*e2*e3*e5
                sage: ca = a.cohomology_class()
                sage: C = B.cohomology(3)
                sage: ca in C
                True
            """

class DifferentialGCAlgebra_multigraded(DifferentialGCAlgebra, GCAlgebra_multigraded):
    """
    A commutative differential multi-graded algebras.

    INPUT:

    - ``A`` -- a commutative multi-graded algebra

    - ``differential`` -- a differential

    EXAMPLES::

        sage: A.<a,b,c> = GradedCommutativeAlgebra(QQ, degrees=((1,0), (0, 1), (0,2)))
        sage: B = A.cdg_algebra(differential={a: c})
        sage: B.basis((1,0))
        [a]
        sage: B.basis(1, total=True)
        [a, b]
        sage: B.cohomology((1, 0))
        Free module generated by {} over Rational Field
        sage: B.cohomology(1, total=True)
        Free module generated by {[b]} over Rational Field
    """
    def __init__(self, A, differential) -> None:
        """
        Initialize ``self``.

        INPUT:

        - ``A`` -- a multi-graded commutative algebra
        - ``differential`` -- a differential

        EXAMPLES::

            sage: A.<a,b,c> = GradedCommutativeAlgebra(QQ, degrees=((1,0), (0, 1), (0,2)))
            sage: B = A.cdg_algebra(differential={a: c})

        Trying to define a differential which is not multi-graded::

            sage: A.<t,x,y,z> = GradedCommutativeAlgebra(QQ, degrees=((1,0),(1,0),(2,0),(0,2)))
            sage: B = A.cdg_algebra(differential={x:y}) # good
            sage: B = A.cdg_algebra(differential={t:z}) # good
            sage: B = A.cdg_algebra(differential={x:y, t:z}) # bad
            Traceback (most recent call last):
            ...
            ValueError: the differential does not have a well-defined degree
        """
    def coboundaries(self, n, total: bool = False):
        """
        The `n`-th coboundary group of the algebra.

        This is a vector space over the base field `F`, and it is
        returned as a subspace of the vector space `F^d`, where the
        `n`-th homogeneous component has dimension `d`.

        INPUT:

        - ``n`` -- degree
        - ``total`` -- boolean (default: ``False``); if ``True``, return the
          coboundaries in total degree `n`

        If `n` is an integer rather than a multi-index, then the
        total degree is used in that case as well.

        EXAMPLES::

            sage: A.<a,b,c> = GradedCommutativeAlgebra(QQ, degrees=((1,0), (0, 1), (0,2)))
            sage: B = A.cdg_algebra(differential={a: c})
            sage: B.coboundaries((0,2))
            Vector space of degree 1 and dimension 1 over Rational Field
            Basis matrix:
            [1]
            sage: B.coboundaries(2)
            Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix:
            [0 1]
        """
    def cocycles(self, n, total: bool = False):
        """
        The `n`-th cocycle group of the algebra.

        This is a vector space over the base field `F`, and it is
        returned as a subspace of the vector space `F^d`, where the
        `n`-th homogeneous component has dimension `d`.

        INPUT:

        - ``n`` -- degree
        - ``total`` -- boolean (default: ``False``); if ``True``, return the
          cocycles in total degree `n`

        If `n` is an integer rather than a multi-index, then the
        total degree is used in that case as well.

        EXAMPLES::

            sage: A.<a,b,c> = GradedCommutativeAlgebra(QQ, degrees=((1,0), (0, 1), (0,2)))
            sage: B = A.cdg_algebra(differential={a: c})
            sage: B.cocycles((0,1))
            Vector space of degree 1 and dimension 1 over Rational Field
            Basis matrix:
            [1]
            sage: B.cocycles((0,1), total=True)
            Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix:
            [0 1]
        """
    def cohomology_raw(self, n, total: bool = False):
        """
        The `n`-th cohomology group of the algebra.

        This is a vector space over the base ring, and it is returned
        as the quotient cocycles/coboundaries.

        Compare to :meth:`cohomology`.

        INPUT:

        - ``n`` -- degree
        - ``total`` -- boolean (default: ``False``); if ``True``, return the
          cohomology in total degree `n`

        If `n` is an integer rather than a multi-index, then the
        total degree is used in that case as well.

        EXAMPLES::

            sage: A.<a,b,c> = GradedCommutativeAlgebra(QQ, degrees=((1,0), (0, 1), (0,2)))
            sage: B = A.cdg_algebra(differential={a: c})
            sage: B.cohomology_raw((0,2))
            Vector space quotient V/W of dimension 0 over Rational Field where
            V: Vector space of degree 1 and dimension 1 over Rational Field
            Basis matrix:
            [1]
            W: Vector space of degree 1 and dimension 1 over Rational Field
            Basis matrix:
            [1]

            sage: B.cohomology_raw(1)
            Vector space quotient V/W of dimension 1 over Rational Field where
            V: Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix:
            [0 1]
            W: Vector space of degree 2 and dimension 0 over Rational Field
            Basis matrix:
            []
        """
    def cohomology(self, n, total: bool = False):
        """
        The `n`-th cohomology group of the algebra.

        This is a vector space over the base ring, defined as the
        quotient cocycles/coboundaries. The elements of the quotient
        are lifted to the vector space of cocycles, and this is
        described in terms of those lifts.

        Compare to :meth:`cohomology_raw`.

        INPUT:

        - ``n`` -- degree
        - ``total`` -- boolean (default: ``False``); if ``True``, return the
          cohomology in total degree `n`

        If `n` is an integer rather than a multi-index, then the
        total degree is used in that case as well.

        EXAMPLES::

            sage: A.<a,b,c> = GradedCommutativeAlgebra(QQ, degrees=((1,0), (0, 1), (0,2)))
            sage: B = A.cdg_algebra(differential={a: c})
            sage: B.cohomology((0,2))
            Free module generated by {} over Rational Field

            sage: B.cohomology(1)
            Free module generated by {[b]} over Rational Field
        """
    homology = cohomology
    class Element(GCAlgebra_multigraded.Element, DifferentialGCAlgebra.Element):
        """
        Element class of a commutative differential multi-graded algebra.
        """

def GradedCommutativeAlgebra(ring, names=None, degrees=None, max_degree=None, **kwargs):
    '''
    A graded commutative algebra.

    INPUT:

    There are two ways to call this. The first way defines a free
    graded commutative algebra:

    - ``ring`` -- the base field over which to work

    - ``names`` -- names of the generators. You may also use Sage\'s
      ``A.<x,y,...> = ...`` syntax to define the names. If no names
      are specified, the generators are named ``x0``, ``x1``, ...

    - ``degrees`` -- degrees of the generators; if this is omitted,
      the degree of each generator is 1, and if both ``names`` and
      ``degrees`` are omitted, an error is raised

    - ``max_degree`` -- the maximal degree of the graded algebra. If omitted,
      no maximal degree is assumed and an instance of :class:`GCAlgebra` is
      returned. Otherwise, an instance of
      :class:`sage.algebras.commutative_graded_algebra.GradedCommutativeAlgebraWithMaxDeg`
      is created.

    Once such an algebra has been defined, one can use its associated
    methods to take a quotient, impose a differential, etc. See the
    examples below.

    The second way takes a graded commutative algebra and imposes
    relations:

    - ``ring`` -- a graded commutative algebra

    - ``relations`` -- list or tuple of elements of ``ring``

    EXAMPLES:

    Defining a graded commutative algebra::

        sage: GradedCommutativeAlgebra(QQ, \'x, y, z\')
        Graded Commutative Algebra with generators (\'x\', \'y\', \'z\')
         in degrees (1, 1, 1) over Rational Field
        sage: GradedCommutativeAlgebra(QQ, degrees=(2, 3, 4))
        Graded Commutative Algebra with generators (\'x0\', \'x1\', \'x2\')
         in degrees (2, 3, 4) over Rational Field

    As usual in Sage, the ``A.<...>`` notation defines both the
    algebra and the generator names::

        sage: A.<x,y,z> = GradedCommutativeAlgebra(QQ, degrees=(1, 1, 2))
        sage: x^2
        0
        sage: y*x #  Odd classes anticommute.
        -x*y
        sage: z*y  # z is central since it is in degree 2.
        y*z
        sage: (x*y*z**3).degree()
        8
        sage: A.basis(3)  # basis of homogeneous degree 3 elements
        [x*z, y*z]

    Defining a quotient::

        sage: I = A.ideal(x*z)
        sage: AQ = A.quotient(I); AQ
        Graded Commutative Algebra with generators (\'x\', \'y\', \'z\')
         in degrees (1, 1, 2) with relations [x*z] over Rational Field
        sage: AQ.basis(3)
        [y*z]

    Note that ``AQ`` has no specified differential. This is reflected in
    its print representation: ``AQ`` is described as a "graded commutative
    algebra" -- the word "differential" is missing. Also, it has no
    default ``differential``::

        sage: AQ.differential()
        Traceback (most recent call last):
        ...
        TypeError: ...differential() missing 1 required positional argument:
        \'diff\'

    Now we add a differential to ``AQ``::

        sage: B = AQ.cdg_algebra({z: y*z}); B
        Commutative Differential Graded Algebra with generators (\'x\', \'y\', \'z\')
         in degrees (1, 1, 2) with relations [x*z] over Rational Field with differential:
            x --> 0
            y --> 0
            z --> y*z
        sage: B.differential()
        Differential of Commutative Differential Graded Algebra with generators
         (\'x\', \'y\', \'z\') in degrees (1, 1, 2) with relations [x*z] over Rational Field
          Defn: x --> 0
                y --> 0
                z --> y*z
        sage: B.cohomology(1)
        Free module generated by {[x], [y]} over Rational Field
        sage: B.cohomology(2)
        Free module generated by {[x*y]} over Rational Field

    We compute algebra generators for cohomology in a range of
    degrees. This cohomology algebra appears to be finitely
    generated::

        sage: B.cohomology_generators(15)
        {1: [x, y]}

    We can construct multi-graded rings as well. We work in characteristic 2
    for a change, so the algebras here are honestly commutative::

        sage: C.<a,b,c,d> = GradedCommutativeAlgebra(GF(2),
        ....:                                        degrees=((1,0), (1,1), (0,2), (0,3)))
        sage: D = C.cdg_algebra(differential={a: c, b: d}); D
        Commutative Differential Graded Algebra with generators (\'a\', \'b\', \'c\', \'d\')
         in degrees ((1, 0), (1, 1), (0, 2), (0, 3)) over Finite Field of size 2
         with differential:
            a --> c
            b --> d
            c --> 0
            d --> 0

    We can examine ``D`` using both total degrees and multidegrees.
    Use tuples, lists, vectors, or elements of additive
    abelian groups to specify degrees::

        sage: D.basis(3)      # basis in total degree 3
        [a^3, a*b, a*c, d]
        sage: D.basis((1,2))  # basis in degree (1,2)
        [a*c]
        sage: D.basis([1,2])
        [a*c]
        sage: D.basis(vector([1,2]))
        [a*c]
        sage: G = AdditiveAbelianGroup([0,0]); G
        Additive abelian group isomorphic to Z + Z
        sage: D.basis(G(vector([1,2])))
        [a*c]

    At this point, ``a``, for example, is an element of ``C``. We can
    redefine it so that it is instead an element of ``D`` in several
    ways, for instance using :meth:`gens` method::

        sage: a, b, c, d = D.gens()
        sage: a.differential()
        c

    Or the :meth:`inject_variables` method::

        sage: D.inject_variables()
        Defining a, b, c, d
        sage: (a*b).differential()
        b*c + a*d
        sage: (a*b*c**2).degree()
        (2, 5)

    Degrees are returned as elements of additive abelian groups::

        sage: (a*b*c**2).degree() in G
        True

        sage: (a*b*c**2).degree(total=True)  # total degree
        7
        sage: D.cohomology(4)
        Free module generated by {[a^4], [b^2]} over Finite Field of size 2
        sage: D.cohomology((2,2))
        Free module generated by {[b^2]} over Finite Field of size 2

    Graded algebra with maximal degree::

        sage: A.<p,e> = GradedCommutativeAlgebra(QQ, degrees=(4,2), max_degree=6); A
        Graded commutative algebra with generators (\'p\', \'e\') in degrees (4, 2)
         with maximal degree 6
        sage: p^2
        0

    TESTS:

    We need to specify either name or degrees::

        sage: GradedCommutativeAlgebra(QQ)
        Traceback (most recent call last):
        ...
        ValueError: you must specify names or degrees
    '''

class GCAlgebraMorphism(RingHomomorphism_im_gens):
    """
    Create a morphism between two :class:`graded commutative algebras <GCAlgebra>`.

    INPUT:

    - ``parent`` -- the parent homset

    - ``im_gens`` -- the images, in the codomain, of the generators of
      the domain

    - ``check`` -- boolean (default: ``True``); check whether the
      proposed map is actually an algebra map; if the domain and
      codomain have differentials, also check that the map respects
      those.

    EXAMPLES::

        sage: A.<x,y> = GradedCommutativeAlgebra(QQ)
        sage: H = Hom(A,A)
        sage: f = H([y,x])
        sage: f
        Graded Commutative Algebra endomorphism of Graded Commutative Algebra
         with generators ('x', 'y') in degrees (1, 1) over Rational Field
          Defn: (x, y) --> (y, x)
        sage: f(x*y)
        -x*y
    """
    def __init__(self, parent, im_gens, check: bool = True) -> None:
        '''
        TESTS:

        The entries in ``im_gens`` must lie in the codomain::

            sage: A.<x,y> = GradedCommutativeAlgebra(QQ, degrees=(1,2))
            sage: B.<a,b> = GradedCommutativeAlgebra(QQ, degrees=(1,2))
            sage: H = Hom(A,A)
            sage: H([x,b])
            Traceback (most recent call last):
            ...
            ValueError: not all elements of im_gens are in the codomain

        Note that morphisms do not need to respect the grading;
        whether they do can be tested with the method
        :meth:`is_graded`::

            sage: A.<x,y> = GradedCommutativeAlgebra(QQ, degrees=(1,2))
            sage: H = Hom(A,A)
            sage: f = H([x,x])
            sage: f
            Graded Commutative Algebra endomorphism of Graded Commutative Algebra
             with generators (\'x\', \'y\') in degrees (1, 2) over Rational Field
              Defn: (x, y) --> (x, x)
            sage: f.is_graded()
            False
            sage: TestSuite(f).run(skip=\'_test_category\')

        Since `x^2=0` but `y^2 \\neq 0`, the following does not define a valid morphism::

            sage: H([y,y])
            Traceback (most recent call last):
            ...
            ValueError: the proposed morphism does not respect the relations

        This is okay in characteristic two since then `x^2 \\neq 0`::

            sage: A2.<x,y> = GradedCommutativeAlgebra(GF(2), degrees=(1,2))
            sage: H2 = Hom(A2,A2)
            sage: H2([y,y])
            Graded Commutative Algebra endomorphism of Graded Commutative Algebra
             with generators (\'x\', \'y\') in degrees (1, 2) over Finite Field of size 2
              Defn: (x, y) --> (y, y)

        The "nc-relations" `a*b = -b*a`, for `a` and `b` in odd
        degree, are checked first, and we can see this when using more
        generators::

            sage: A.<x,y,z> = GradedCommutativeAlgebra(QQ, degrees=(1,1,2))
            sage: Hom(A,A)([x,z,z])
            Traceback (most recent call last):
            ...
            ValueError: the proposed morphism does not respect the nc-relations

        Other relations::

            sage: B.<x,y,z> = GradedCommutativeAlgebra(QQ, degrees=(1,1,1))
            sage: D = B.quotient(B.ideal(x*y))
            sage: H = Hom(D,D)
            sage: D.inject_variables()
            Defining x, y, z
            sage: H([x,z,z])
            Traceback (most recent call last):
            ...
            ValueError: the proposed morphism does not respect the relations

        The morphisms must respect the differentials, when present::

            sage: B.<x,y,z> = GradedCommutativeAlgebra(QQ, degrees=(1,1,1))
            sage: C = B.cdg_algebra({z: x*y})
            sage: C.inject_variables()
            Defining x, y, z
            sage: H = Hom(C,C)
            sage: H([x,z,z])
            Traceback (most recent call last):
            ...
            ValueError: the proposed morphism does not respect the differentials

        In the case of only one generator, the cover ring is a polynomial ring,
        hence the noncommutativity relations should not be checked::

            sage: A.<e1> = GradedCommutativeAlgebra(QQ)
            sage: A.cover_ring()
            Multivariate Polynomial Ring in e1 over Rational Field
            sage: A.hom([2*e1])
            Graded Commutative Algebra endomorphism of Graded Commutative Algebra
             with generators (\'e1\',) in degrees (1,) over Rational Field
              Defn: (e1,) --> (2*e1,)
        '''
    def is_graded(self, total: bool = False):
        """
        Return ``True`` if this morphism is graded.

        That is, return ``True`` if `f(x)` is zero, or if `f(x)` is
        homogeneous and has the same degree as `x`, for each generator
        `x`.

        INPUT:

        - ``total`` -- boolean (default: ``False``); if ``True``, use
          the total degree to determine whether the morphism is graded
          (relevant only in the multigraded case)

        EXAMPLES::

            sage: C.<a,b,c> = GradedCommutativeAlgebra(QQ, degrees=(1,1,2))
            sage: H = Hom(C,C)
            sage: H([a, b, a*b + 2*a]).is_graded()
            False
            sage: H([a, b, a*b]).is_graded()
            True

            sage: A.<w,x> = GradedCommutativeAlgebra(QQ, degrees=((1,0), (1,0)))
            sage: B.<y,z> = GradedCommutativeAlgebra(QQ, degrees=((1,0), (0,1)))
            sage: H = Hom(A,B)
            sage: H([y,0]).is_graded()
            True
            sage: H([z,z]).is_graded()
            False
            sage: H([z,z]).is_graded(total=True)
            True
        """

class GCAlgebraHomset(RingHomset_generic):
    """
    Set of morphisms between two graded commutative algebras.

    .. NOTE::

        Homsets (and thus morphisms) have only been implemented when
        the base fields are the same for the domain and codomain.

    EXAMPLES::

        sage: A.<x,y> = GradedCommutativeAlgebra(QQ, degrees=(1,2))
        sage: H = Hom(A,A)
        sage: H([x,y]) == H.identity()
        True
        sage: H([x,x]) == H.identity()
        False

        sage: A.<w,x> = GradedCommutativeAlgebra(QQ, degrees=(1,2))
        sage: B.<y,z> = GradedCommutativeAlgebra(QQ, degrees=(1,1))
        sage: H = Hom(A,B)
        sage: H([y,0])
        Graded Commutative Algebra morphism:
          From: Graded Commutative Algebra with generators ('w', 'x')
                in degrees (1, 2) over Rational Field
          To:   Graded Commutative Algebra with generators ('y', 'z')
                in degrees (1, 1) over Rational Field
          Defn: (w, x) --> (y, 0)
        sage: H([y,y*z])
        Graded Commutative Algebra morphism:
          From: Graded Commutative Algebra with generators ('w', 'x')
                in degrees (1, 2) over Rational Field
          To:   Graded Commutative Algebra with generators ('y', 'z')
                in degrees (1, 1) over Rational Field
          Defn: (w, x) --> (y, y*z)
    """
    @cached_method
    def zero(self):
        '''
        Construct the "zero" morphism of this homset: the map sending each
        generator to zero.

        EXAMPLES::

            sage: A.<x,y> = GradedCommutativeAlgebra(QQ, degrees=(1,2))
            sage: B.<a,b,c> = GradedCommutativeAlgebra(QQ, degrees=(1,1,1))
            sage: zero = Hom(A,B).zero()
            sage: zero(x) == zero(y) == 0
            True
        '''
    @cached_method
    def identity(self):
        """
        Construct the identity morphism of this homset.

        EXAMPLES::

            sage: A.<x,y> = GradedCommutativeAlgebra(QQ, degrees=(1,2))
            sage: H = Hom(A,A)
            sage: H([x,y]) == H.identity()
            True
            sage: H([x,x]) == H.identity()
            False
        """
    def __call__(self, im_gens, check: bool = True):
        """
        Create a homomorphism.

        INPUT:

        - ``im_gens`` -- the images of the generators of the domain

        EXAMPLES::

            sage: A.<w,x> = GradedCommutativeAlgebra(QQ, degrees=(1,2))
            sage: B.<y,z> = GradedCommutativeAlgebra(QQ, degrees=(1,1))
            sage: H = Hom(A,B)
            sage: H([y,0])
            Graded Commutative Algebra morphism:
              From: Graded Commutative Algebra with generators ('w', 'x') in degrees (1, 2) over Rational Field
              To:   Graded Commutative Algebra with generators ('y', 'z') in degrees (1, 1) over Rational Field
              Defn: (w, x) --> (y, 0)
            sage: H([y,y*z])
            Graded Commutative Algebra morphism:
              From: Graded Commutative Algebra with generators ('w', 'x') in degrees (1, 2) over Rational Field
              To:   Graded Commutative Algebra with generators ('y', 'z') in degrees (1, 1) over Rational Field
              Defn: (w, x) --> (y, y*z)
        """

class CohomologyClass(SageObject, CachedRepresentation):
    """
    A class for representing cohomology classes.

    This just has ``_repr_`` and ``_latex_`` methods which put
    brackets around the object's name.

    EXAMPLES::

        sage: from sage.algebras.commutative_dga import CohomologyClass
        sage: CohomologyClass(3)
        [3]
        sage: A.<x,y,z,t> = GradedCommutativeAlgebra(QQ, degrees=(2,2,3,3))
        sage: CohomologyClass(x^2 + 2*y*z, A)
        [2*y*z + x^2]

    TESTS:

    In order for the cache to not confuse objects with the same representation,
    we can pass the parent of the representative as a parameter::

        sage: A.<e1,e2,e3,e4,e5,e6> = GradedCommutativeAlgebra(QQ)
        sage: B1 = A.cdg_algebra({e5:e1*e2,e6:e3*e4})
        sage: B2 = A.cdg_algebra({e5:e1*e2,e6:e1*e2+e3*e4})
        sage: B1.minimal_model()
        Commutative Differential Graded Algebra morphism:
          From: Commutative Differential Graded Algebra with generators ('x1_0', 'x1_1', 'x1_2', 'x1_3', 'y1_0', 'y1_1') in degrees (1, 1, 1, 1, 1, 1) over Rational Field with differential:
           x1_0 --> 0
           x1_1 --> 0
           x1_2 --> 0
           x1_3 --> 0
           y1_0 --> x1_0*x1_1
           y1_1 --> x1_2*x1_3
          To:   Commutative Differential Graded Algebra with generators ('e1', 'e2', 'e3', 'e4', 'e5', 'e6') in degrees (1, 1, 1, 1, 1, 1) over Rational Field with differential:
           e1 --> 0
           e2 --> 0
           e3 --> 0
           e4 --> 0
           e5 --> e1*e2
           e6 --> e3*e4
          Defn: (x1_0, x1_1, x1_2, x1_3, y1_0, y1_1) --> (e1, e2, e3, e4, e5, e6)
        sage: B2.minimal_model()
        Commutative Differential Graded Algebra morphism:
          From: Commutative Differential Graded Algebra with generators ('x1_0', 'x1_1', 'x1_2', 'x1_3', 'y1_0', 'y1_1') in degrees (1, 1, 1, 1, 1, 1) over Rational Field with differential:
           x1_0 --> 0
           x1_1 --> 0
           x1_2 --> 0
           x1_3 --> 0
           y1_0 --> x1_0*x1_1
           y1_1 --> x1_2*x1_3
          To:   Commutative Differential Graded Algebra with generators ('e1', 'e2', 'e3', 'e4', 'e5', 'e6') in degrees (1, 1, 1, 1, 1, 1) over Rational Field with differential:
           e1 --> 0
           e2 --> 0
           e3 --> 0
           e4 --> 0
           e5 --> e1*e2
           e6 --> e1*e2 + e3*e4
          Defn: (x1_0, x1_1, x1_2, x1_3, y1_0, y1_1) --> (e1, e2, e3, e4, e5, -e5 + e6)
    """
    def __init__(self, x, cdga=None) -> None:
        """
        EXAMPLES::

            sage: from sage.algebras.commutative_dga import CohomologyClass
            sage: CohomologyClass(x - 2)                                                # needs sage.symbolic
            [x - 2]
        """
    def __hash__(self):
        """
        TESTS::

            sage: from sage.algebras.commutative_dga import CohomologyClass
            sage: hash(CohomologyClass(sin)) == hash(sin)                               # needs sage.symbolic
            True
        """
    def representative(self):
        """
        Return the representative of ``self``.

        EXAMPLES::

            sage: from sage.algebras.commutative_dga import CohomologyClass
            sage: x = CohomologyClass(sin)                                              # needs sage.symbolic
            sage: x.representative() == sin                                             # needs sage.symbolic
            True
        """

@cached_function
def exterior_algebra_basis(n, degrees):
    """
    Basis of an exterior algebra in degree ``n``, where the
    generators are in degrees ``degrees``.

    INPUT:

    - ``n`` -- integer
    - ``degrees`` -- iterable of integers

    Return list of lists, each list representing exponents for the
    corresponding generators. (So each list consists of 0s and 1s.)

    EXAMPLES::

        sage: from sage.algebras.commutative_dga import exterior_algebra_basis
        sage: exterior_algebra_basis(1, (1,3,1))
        [[0, 0, 1], [1, 0, 0]]
        sage: exterior_algebra_basis(4, (1,3,1))
        [[0, 1, 1], [1, 1, 0]]
        sage: exterior_algebra_basis(10, (1,5,1,1))
        []
    """
def total_degree(deg):
    """
    Total degree of ``deg``.

    INPUT:

    - ``deg`` -- an element of a free abelian group

    In fact, ``deg`` could be an integer, a Python int, a list, a
    tuple, a vector, etc. This function returns the sum of the
    components of ``deg``.

    EXAMPLES::

        sage: from sage.algebras.commutative_dga import total_degree
        sage: total_degree(12)
        12
        sage: total_degree(range(5))
        10
        sage: total_degree(vector(range(5)))
        10
        sage: G = AdditiveAbelianGroup((0,0))
        sage: x = G.gen(0); y = G.gen(1)
        sage: 3*x+4*y
        (3, 4)
        sage: total_degree(3*x+4*y)
        7
    """
