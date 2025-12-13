from sage.categories.fields import Fields as Fields
from sage.categories.groups import Groups as Groups
from sage.groups.matrix_gps.named_group import NamedMatrixGroup_generic as NamedMatrixGroup_generic, normalize_args_vectorspace as normalize_args_vectorspace
from sage.misc.latex import latex as latex
from sage.misc.misc_c import prod as prod
from sage.rings.finite_rings.integer_mod_ring import Integers as Integers
from sage.rings.infinity import Infinity as Infinity
from sage.rings.integer_ring import ZZ as ZZ

def GL(n, R, var: str = 'a'):
    """
    Return the general linear group.

    The general linear group `GL( d, R )` consists of all `d \\times d`
    matrices that are invertible over the ring `R`.

    .. NOTE::

        This group is also available via ``groups.matrix.GL()``.

    INPUT:

    - ``n`` -- positive integer

    - ``R`` -- ring or an integer; if an integer is specified, the
      corresponding finite field is used

    - ``var`` -- variable used to represent generator of the finite
      field, if needed

    EXAMPLES::

        sage: G = GL(6, GF(5))
        sage: G.base_ring()
        Finite Field of size 5
        sage: G.category()
        Category of finite groups

        sage: # needs sage.libs.gap
        sage: G.order()
        11064475422000000000000000
        sage: TestSuite(G).run()

        sage: G = GL(6, QQ)
        sage: G.category()
        Category of infinite groups

        sage: # needs sage.libs.gap
        sage: TestSuite(G).run()

    Here is the Cayley graph of (relatively small) finite General Linear Group::

        sage: # needs sage.graphs sage.libs.gap
        sage: g = GL(2,3)
        sage: d = g.cayley_graph(); d
        Digraph on 48 vertices
        sage: d.plot(color_by_label=True, vertex_size=0.03,     # long time             # needs sage.plot
        ....:        vertex_labels=False)
        Graphics object consisting of 144 graphics primitives
        sage: d.plot3d(color_by_label=True)                     # long time             # needs sage.plot
        Graphics3d Object

    ::

        sage: # needs sage.libs.gap
        sage: F = GF(3); MS = MatrixSpace(F, 2, 2)
        sage: gens = [MS([[2,0], [0,1]]), MS([[2,1], [2,0]])]
        sage: G = MatrixGroup(gens)
        sage: G.order()
        48
        sage: G.cardinality()
        48
        sage: H = GL(2,F)
        sage: H.order()
        48
        sage: H == G
        True
        sage: H.gens() == G.gens()
        True
        sage: H.as_matrix_group() == H
        True
        sage: H.gens()
        (
        [2 0]  [2 1]
        [0 1], [2 0]
        )

    TESTS::

        sage: groups.matrix.GL(2, 3)
        General Linear Group of degree 2 over Finite Field of size 3
        sage: groups.matrix.GL(1, ZZ).category()
        Category of groups
        sage: groups.matrix.GL(1, QQ).category()
        Category of infinite groups
    """
def SL(n, R, var: str = 'a'):
    """
    Return the special linear group.

    The special linear group `SL( d, R )` consists of all `d \\times d`
    matrices that are invertible over the ring `R` with determinant
    one.

    .. NOTE::

        This group is also available via ``groups.matrix.SL()``.

    INPUT:

    - ``n`` -- positive integer

    - ``R`` -- ring or integer; if an integer is specified, the
      corresponding finite field is used

    - ``var`` -- variable used to represent generator of the finite
      field, if needed

    EXAMPLES::

        sage: SL(3, GF(2))
        Special Linear Group of degree 3 over Finite Field of size 2
        sage: G = SL(15, GF(7)); G
        Special Linear Group of degree 15 over Finite Field of size 7
        sage: G.category()
        Category of finite groups

        sage: # needs sage.libs.gap
        sage: G.order()
        1956712595698146962015219062429586341124018007182049478916067369638713066737882363393519966343657677430907011270206265834819092046250232049187967718149558134226774650845658791865745408000000
        sage: len(G.gens())
        2

        sage: G = SL(2, ZZ); G
        Special Linear Group of degree 2 over Integer Ring
        sage: G.category()
        Category of infinite groups
        sage: G.gens()
        (
        [ 0  1]  [1 1]
        [-1  0], [0 1]
        )

    Next we compute generators for `\\mathrm{SL}_3(\\ZZ)` ::

        sage: G = SL(3, ZZ); G
        Special Linear Group of degree 3 over Integer Ring

        sage: # needs sage.libs.gap
        sage: G.gens()
        (
        [0 1 0]  [ 0  1  0]  [1 1 0]
        [0 0 1]  [-1  0  0]  [0 1 0]
        [1 0 0], [ 0  0  1], [0 0 1]
        )
        sage: TestSuite(G).run()

    TESTS::

        sage: groups.matrix.SL(2, 3)
        Special Linear Group of degree 2 over Finite Field of size 3
    """

class LinearMatrixGroup_generic(NamedMatrixGroup_generic):
    def order(self):
        """
        Return the order of ``self``.

        EXAMPLES::

            sage: G = SL(3, GF(5))
            sage: G.order()
            372000

        The order computation also works over the base rings `\\ZZ/n\\ZZ`::

            sage: GL(4, Integers(15)).order()
            2815842631680000000

            sage: SL(4, Integers(15)).order()
            351980328960000000

            sage: G = GL(2, Integers(6))
            sage: G.order() == len(list(G))
            True

            sage: H = SL(2, Integers(6))
            sage: H.order() == len(list(H))
            True

        Arbitrary base rings are currently not fully supported::

            sage: R.<x> = PolynomialRing(GF(7))
            sage: S = R.quotient(x^2 + 5)
            sage: GL(2, S).order()
            Traceback (most recent call last):
            ...
            NotImplementedError: order computation of linear groups not fully supported for arbitrary base rings

        TESTS:

        Check if :issue:`36876` is fixed::

            sage: SL(1, QQ).order()
            1
            sage: SL(2, ZZ).cardinality()
            +Infinity

        Check if :issue:`35490` is fixed::

            sage: q = 7
            sage: FqT.<T> = GF(q)[]
            sage: N = T^2+1
            sage: FqTN = QuotientRing(FqT, N*FqT)
            sage: S = SL(2, FqTN)
            sage: S.is_finite()
            True
            sage: S.order()
            117600

        Check if :issue:`37934` is fixed::

            sage: GL(2, Integers(4)).order()
            96

            sage: GL(2, Integers(1)).order()
            1

            sage: GL(1, ZZ).order()
            2
        """
    cardinality = order
