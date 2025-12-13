from sage.categories.hopf_algebras import HopfAlgebras as HopfAlgebras
from sage.categories.rings import Rings as Rings
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.combinat.rooted_tree import LabelledRootedTree as LabelledRootedTree, LabelledRootedTrees as LabelledRootedTrees, RootedTree as RootedTree, RootedTrees as RootedTrees
from sage.combinat.words.alphabet import Alphabet as Alphabet
from sage.rings.integer_ring import ZZ as ZZ
from sage.sets.family import Family as Family

ROOT: str

class GrossmanLarsonAlgebra(CombinatorialFreeModule):
    '''
    The Grossman-Larson Hopf Algebra.

    The Grossman-Larson Hopf Algebras are Hopf algebras with a basis
    indexed by forests of decorated rooted trees. They are the
    universal enveloping algebras of free pre-Lie algebras, seen
    as Lie algebras.

    The Grossman-Larson Hopf algebra on a given set `E` has an
    explicit description using rooted forests. The underlying vector
    space has a basis indexed by finite rooted forests endowed with a
    map from their vertices to `E` (called the "labeling").
    In this basis, the product of two
    (decorated) rooted forests `S * T` is a sum over all maps from
    the set of roots of `T` to the union of a singleton `\\{\\#\\}` and
    the set of vertices of `S`. Given such a map, one defines a new
    forest as follows. Starting from the disjoint union of all rooted trees
    of `S` and `T`, one adds an edge from every root of `T` to its
    image when this image is not the fake vertex labelled ``#``.
    The coproduct sends a rooted forest `T` to the sum of all tensors
    `T_1 \\otimes T_2` obtained by splitting the connected components
    of `T` into two subsets and letting `T_1` be the forest formed
    by the first subset and `T_2` the forest formed by the second.
    This yields a connected graded Hopf algebra (the degree of a
    forest is its number of vertices).

    See [Pana2002]_ (Section 2) and [GroLar1]_.
    (Note that both references use rooted trees rather than rooted
    forests, so think of each rooted forest grafted onto a new root.
    Also, the product is reversed, so they are defining the opposite
    algebra structure.)

    .. WARNING::

        For technical reasons, instead of using forests as labels for
        the basis, we use rooted trees. Their root vertex should be
        considered as a fake vertex. This fake root vertex is labelled
        ``\'#\'`` when labels are present.

    EXAMPLES::

        sage: G = algebras.GrossmanLarson(QQ, \'xy\')
        sage: x, y = G.single_vertex_all()
        sage: ascii_art(x*y)
        B  + B
         #      #_
         |     / /
         x    x y
         |
         y

        sage: ascii_art(x*x*x)
        B  + B     + 3*B     + B
         #      #         #_      _#__
         |      |        / /     / / /
         x      x_      x x     x x x
         |     / /        |
         x    x x         x
         |
         x

    The Grossman-Larson algebra is associative::

        sage: z = x * y
        sage: x * (y * z) == (x * y) * z
        True

    It is not commutative::

        sage: x * y == y * x
        False

    When ``None`` is given as input, unlabelled forests are used instead;
    this corresponds to a `1`-element set `E`::

        sage: G = algebras.GrossmanLarson(QQ, None)
        sage: x = G.single_vertex_all()[0]
        sage: ascii_art(x*x)
        B  + B
         o      o_
         |     / /
         o    o o
         |
         o

    .. NOTE::

        Variables names can be ``None``, a list of strings, a string
        or an integer. When ``None`` is given, unlabelled rooted
        forests are used. When a single string is given, each letter is taken
        as a variable. See
        :func:`sage.combinat.words.alphabet.build_alphabet`.

    .. WARNING::

        Beware that the underlying combinatorial free module is based
        either on ``RootedTrees`` or on ``LabelledRootedTrees``, with no
        restriction on the labellings. This means that all code calling
        the :meth:`basis` method would not give meaningful results, since
        :meth:`basis` returns many "chaff" elements that do not belong to
        the algebra.

    REFERENCES:

    - [Pana2002]_

    - [GroLar1]_
    '''
    @staticmethod
    def __classcall_private__(cls, R, names=None):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: F1 = algebras.GrossmanLarson(QQ, 'xyz')
            sage: F2 = algebras.GrossmanLarson(QQ, ['x','y','z'])
            sage: F3 = algebras.GrossmanLarson(QQ, Alphabet('xyz'))
            sage: F1 is F2 and F1 is F3
            True
        """
    def __init__(self, R, names=None) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: A = algebras.GrossmanLarson(QQ, '@'); A
            Grossman-Larson Hopf algebra on one generator ['@']
            over Rational Field
            sage: TestSuite(A).run() # long time

            sage: F = algebras.GrossmanLarson(QQ, 'xy')
            sage: TestSuite(F).run() # long time

            sage: A = algebras.GrossmanLarson(QQ, None); A
            Grossman-Larson Hopf algebra on one generator ['o'] over
            Rational Field

            sage: F = algebras.GrossmanLarson(QQ, ['x','y']); F
            Grossman-Larson Hopf algebra on 2 generators ['x', 'y']
            over Rational Field

            sage: A = algebras.GrossmanLarson(QQ, []); A
            Grossman-Larson Hopf algebra on 0 generators [] over
            Rational Field
        """
    def variable_names(self):
        """
        Return the names of the variables.

        This returns the set `E` (as a family).

        EXAMPLES::

            sage: R = algebras.GrossmanLarson(QQ, 'xy')
            sage: R.variable_names()
            {'x', 'y'}

            sage: R = algebras.GrossmanLarson(QQ, ['a','b'])
            sage: R.variable_names()
            {'a', 'b'}

            sage: R = algebras.GrossmanLarson(QQ, 2)
            sage: R.variable_names()
            {0, 1}

            sage: R = algebras.GrossmanLarson(QQ, None)
            sage: R.variable_names()
            {'o'}
        """
    def single_vertex(self, i):
        """
        Return the ``i``-th rooted forest with one vertex.

        This is the rooted forest with just one vertex, labelled by the
        ``i``-th element of the label list.

        .. SEEALSO:: :meth:`single_vertex_all`.

        INPUT:

        - ``i`` -- nonnegative integer

        EXAMPLES::

            sage: F = algebras.GrossmanLarson(ZZ, 'xyz')
            sage: F.single_vertex(0)
            B[#[x[]]]

            sage: F.single_vertex(4)
            Traceback (most recent call last):
            ...
            IndexError: argument i (= 4) must be between 0 and 2
        """
    def single_vertex_all(self):
        """
        Return the rooted forests with one vertex in ``self``.

        They freely generate the Lie algebra of primitive elements
        as a pre-Lie algebra.

        .. SEEALSO:: :meth:`single_vertex`.

        EXAMPLES::

            sage: A = algebras.GrossmanLarson(ZZ, 'fgh')
            sage: A.single_vertex_all()
            (B[#[f[]]], B[#[g[]]], B[#[h[]]])

            sage: A = algebras.GrossmanLarson(QQ, ['x1','x2'])
            sage: A.single_vertex_all()
            (B[#[x1[]]], B[#[x2[]]])

            sage: A = algebras.GrossmanLarson(ZZ, None)
            sage: A.single_vertex_all()
            (B[[[]]],)
        """
    def change_ring(self, R):
        """
        Return the Grossman-Larson algebra in the same variables over `R`.

        INPUT:

        - ``R`` -- a ring

        EXAMPLES::

            sage: A = algebras.GrossmanLarson(ZZ, 'fgh')
            sage: A.change_ring(QQ)
            Grossman-Larson Hopf algebra on 3 generators ['f', 'g', 'h']
            over Rational Field
        """
    def degree_on_basis(self, t):
        """
        Return the degree of a rooted forest in the Grossman-Larson algebra.

        This is the total number of vertices of the forest.

        EXAMPLES::

            sage: A = algebras.GrossmanLarson(QQ, '@')
            sage: RT = A.basis().keys()
            sage: A.degree_on_basis(RT([RT([])]))
            1
        """
    def some_elements(self):
        """
        Return some elements of the Grossman-Larson Hopf algebra.

        EXAMPLES::

            sage: A = algebras.GrossmanLarson(QQ, None)
            sage: A.some_elements()
            [B[[[]]], B[[]] + B[[[[]]]] + B[[[], []]],
            4*B[[[[]]]] + 4*B[[[], []]]]

        With several generators::

            sage: A = algebras.GrossmanLarson(QQ, 'xy')
            sage: A.some_elements()
            [B[#[x[]]],
             B[#[]] + B[#[x[x[]]]] + B[#[x[], x[]]],
             B[#[x[x[]]]] + 3*B[#[x[y[]]]] + B[#[x[], x[]]] + 3*B[#[x[], y[]]]]
        """
    def product_on_basis(self, x, y):
        """
        Return the product of two forests `x` and `y`.

        This is the sum over all possible ways for the components
        of the forest `y` to either fall side-by-side with components
        of `x` or be grafted on a vertex of `x`.

        EXAMPLES::

            sage: A = algebras.GrossmanLarson(QQ, None)
            sage: RT = A.basis().keys()
            sage: x = RT([RT([])])
            sage: A.product_on_basis(x, x)
            B[[[[]]]] + B[[[], []]]

        Check that the product is the correct one::

            sage: A = algebras.GrossmanLarson(QQ, 'uv')
            sage: RT = A.basis().keys()
            sage: Tu = RT([RT([],'u')],'#')
            sage: Tv = RT([RT([],'v')],'#')
            sage: A.product_on_basis(Tu, Tv)
            B[#[u[v[]]]] + B[#[u[], v[]]]
        """
    def one_basis(self):
        """
        Return the empty rooted forest.

        EXAMPLES::

            sage: A = algebras.GrossmanLarson(QQ, 'ab')
            sage: A.one_basis()
            #[]

            sage: A = algebras.GrossmanLarson(QQ, None)
            sage: A.one_basis()
            []
        """
    def coproduct_on_basis(self, x):
        """
        Return the coproduct of a forest.

        EXAMPLES::

            sage: G = algebras.GrossmanLarson(QQ,2)
            sage: x, y = G.single_vertex_all()
            sage: ascii_art(G.coproduct(x))  # indirect doctest
            1 # B  + B  # 1
                 #    #
                 |    |
                 0    0

            sage: Delta_xy = G.coproduct(y*x)
            sage: ascii_art(Delta_xy)  # random indirect doctest
            1 # B     + 1 # B  + B  # B  + B     # 1 + B  # B  + B  # 1
                   #_        #    #    #      #_        #    #    #
                  / /        |    |    |     / /        |    |    |
                 0 1         1    0    1    0 1         1    0    1
                             |                                    |
                             0                                    0

        TESTS::

            sage: Delta_xy.coefficients()
            [1, 1, 1, 1, 1, 1]
            sage: sortkey = G.print_options()['sorting_key']
            sage: doublekey = lambda tt: (sortkey(tt[0]), sortkey(tt[1]))
            sage: sorted(Delta_xy.monomial_coefficients(), key=doublekey)
            [(#[], #[1[0[]]]),
             (#[], #[0[], 1[]]),
             (#[0[]], #[1[]]),
             (#[1[]], #[0[]]),
             (#[1[0[]]], #[]),
             (#[0[], 1[]], #[])]
        """
    def counit_on_basis(self, x):
        """
        Return the counit on a basis element.

        This is zero unless the forest `x` is empty.

        EXAMPLES::

            sage: A = algebras.GrossmanLarson(QQ, 'xy')
            sage: RT = A.basis().keys()
            sage: x = RT([RT([],'x')],'#')
            sage: A.counit_on_basis(x)
            0
            sage: A.counit_on_basis(RT([],'#'))
            1
        """
    def antipode_on_basis(self, x):
        """
        Return the antipode of a forest.

        EXAMPLES::

            sage: G = algebras.GrossmanLarson(QQ,2)
            sage: x, y = G.single_vertex_all()
            sage: G.antipode(x)  # indirect doctest
            -B[#[0[]]]

            sage: G.antipode(y*x)  # indirect doctest
            B[#[0[1[]]]] + B[#[0[], 1[]]]
        """
