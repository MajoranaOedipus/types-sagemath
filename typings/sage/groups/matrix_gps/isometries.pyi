from sage.categories.action import Action as Action
from sage.groups.matrix_gps.finitely_generated_gap import FinitelyGeneratedMatrixGroup_gap as FinitelyGeneratedMatrixGroup_gap

class GroupOfIsometries(FinitelyGeneratedMatrixGroup_gap):
    """
    A base class for Orthogonal matrix groups with a gap backend.

    Main difference to :class:`~sage.groups.matrix_gps.orthogonal.OrthogonalMatrixGroup_gap`
    is that we can specify generators and a bilinear form. Following GAP, the group action is
    from the right.

    INPUT:

    - ``degree`` -- integer; the degree (matrix size) of the matrix
    - ``base_ring`` -- ring, the base ring of the matrices
    - ``gens`` -- list of matrices over the base ring
    - ``invariant_bilinear_form`` -- a symmetric matrix
    - ``category`` -- (default: ``None``) a category of groups
    - ``check`` -- boolean (default: ``True``); check if the generators
      preserve the bilinear form
    - ``invariant_submodule`` -- a submodule preserved by the group action
      (default: ``None``); registers an action on this submodule
    - ``invariant_quotient_module`` -- a quotient module preserved by
      the group action (default: ``None``)
      registers an action on this quotient module

    EXAMPLES::

        sage: from sage.groups.matrix_gps.isometries import GroupOfIsometries
        sage: bil = Matrix(ZZ, 2, [3,2,2,3])
        sage: gens = [-Matrix(ZZ, 2, [0,1,1,0])]
        sage: O = GroupOfIsometries(2, ZZ, gens, bil)
        sage: O
        Group of isometries with 1 generator (
        [ 0 -1]
        [-1  0]
        )
        sage: O.order()
        2

    Infinite groups are O.K. too::

        sage: bil = Matrix(ZZ,4,[0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0])
        sage: f = Matrix(ZZ,4,[0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, -1, 1, 1, 1])
        sage: O = GroupOfIsometries(2, ZZ, [f], bil)
        sage: O.cardinality()
        +Infinity
    """
    def __init__(self, degree, base_ring, gens, invariant_bilinear_form, category=None, check: bool = True, invariant_submodule=None, invariant_quotient_module=None) -> None:
        """
        Create this orthogonal group from the input.

        TESTS::

            sage: from sage.groups.matrix_gps.isometries import GroupOfIsometries
            sage: bil = Matrix(ZZ,2,[3,2,2,3])
            sage: gens = [-Matrix(ZZ,2,[0,1,1,0])]
            sage: cat = Groups().Finite()
            sage: O = GroupOfIsometries(2, ZZ, gens, bil, category=cat)
            sage: TestSuite(O).run()
        """
    def __reduce__(self):
        """
        Implement pickling.

        EXAMPLES::

            sage: from sage.groups.matrix_gps.isometries import GroupOfIsometries
            sage: bil = Matrix(ZZ,2,[3,2,2,3])
            sage: gens = [-Matrix(ZZ,2,[0,1,1,0])]
            sage: cat = Groups().Finite()
            sage: O = GroupOfIsometries(2, ZZ, gens, bil, category=cat)
            sage: loads(dumps(O)) == O
            True
        """
    def invariant_bilinear_form(self):
        """
        Return the symmetric bilinear form preserved by the orthogonal group.

        OUTPUT: the matrix defining the bilinear form

        EXAMPLES::

            sage: from sage.groups.matrix_gps.isometries import GroupOfIsometries
            sage: bil = Matrix(ZZ,2,[3,2,2,3])
            sage: gens = [-Matrix(ZZ,2,[0,1,1,0])]
            sage: O = GroupOfIsometries(2,ZZ,gens,bil)
            sage: O.invariant_bilinear_form()
            [3 2]
            [2 3]
        """

class GroupActionOnSubmodule(Action):
    """
    Matrix group action on a submodule from the right.

    INPUT:

    - ``MatrixGroup`` -- an instance of :class:`GroupOfIsometries`
    - ``submodule`` -- an invariant submodule
    - ``is_left`` -- boolean (default: ``False``)

    EXAMPLES::

        sage: from sage.groups.matrix_gps.isometries import GroupOfIsometries
        sage: S = span(ZZ, [[0,1]])
        sage: g = Matrix(QQ, 2, [1,0,0,-1])
        sage: G = GroupOfIsometries(2, ZZ, [g],
        ....:                       invariant_bilinear_form=matrix.identity(2),
        ....:                       invariant_submodule=S)
        sage: g = G.an_element()
        sage: x = S.an_element()
        sage: x*g
        (0, -1)
        sage: (x*g).parent()
        Free module of degree 2 and rank 1 over Integer Ring
        Echelon basis matrix:
        [0 1]
    """
    def __init__(self, MatrixGroup, submodule, is_left: bool = False) -> None:
        """
        Initialize the action.

        TESTS::

            sage: from sage.groups.matrix_gps.isometries import GroupOfIsometries, GroupActionOnSubmodule
            sage: S = span(ZZ, [[0,1]])
            sage: g = Matrix(QQ, 2, [1,0,0,-1])
            sage: e = Matrix.identity(2)
            sage: G = GroupOfIsometries(2, ZZ, [g], e)
            sage: GroupActionOnSubmodule(G, S)
            Right action by Group of isometries with 1 generator (
            [ 1  0]
            [ 0 -1]
            ) on Free module of degree 2 and rank 1 over Integer Ring
            Echelon basis matrix:
            [0 1]
        """

class GroupActionOnQuotientModule(Action):
    """
    Matrix group action on a quotient module from the right.

    INPUT:

    - ``MatrixGroup`` -- the group acting
      :class:`GroupOfIsometries`
    - ``submodule`` -- an invariant quotient module
    - ``is_left`` -- boolean (default: ``False``)

    EXAMPLES::

        sage: from sage.groups.matrix_gps.isometries import GroupOfIsometries
        sage: S = span(ZZ,[[0,1]])
        sage: Q = S/(6*S)
        sage: g = Matrix(QQ,2,[1,0,0,-1])
        sage: G = GroupOfIsometries(2, ZZ, [g], invariant_bilinear_form=matrix.identity(2), invariant_quotient_module=Q)
        sage: g = G.an_element()
        sage: x = Q.an_element()
        sage: x*g
        (5)
        sage: (x*g).parent()
        Finitely generated module V/W over Integer Ring with invariants (6)
    """
    def __init__(self, MatrixGroup, quotient_module, is_left: bool = False) -> None:
        """
        Initialize the action.

        TESTS::

            sage: from sage.groups.matrix_gps.isometries import GroupOfIsometries
            sage: S = span(ZZ,[[0,1]])
            sage: Q = S/(6*S)
            sage: g = Matrix(QQ,2,[1,0,0,-1])
            sage: G = GroupOfIsometries(2, ZZ, [g], invariant_bilinear_form=matrix.identity(2), invariant_quotient_module=Q)
            sage: g = G.an_element()
            sage: x = Q.an_element()
            sage: x, x*g
            ((1), (5))
        """
