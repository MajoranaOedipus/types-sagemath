from _typeshed import Incomplete
from sage.groups.perm_gps.permgroup import PermutationGroup_generic as PermutationGroup_generic
from sage.groups.perm_gps.permgroup_element import PermutationGroupElement as PermutationGroupElement
from sage.libs.gap.libgap import libgap as libgap
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.rational_field import QQ as QQ
from sage.rings.real_double import RDF as RDF
from sage.structure.richcmp import richcmp as richcmp, richcmp_method as richcmp_method
from sage.structure.sage_object import SageObject as SageObject

pi: Incomplete
named_colors: Incomplete

def xproj(x, y, z, r):
    """
    Return the `x`-projection of `(x,y,z)` rotated by `r`.

    EXAMPLES::

        sage: from sage.groups.perm_gps.cubegroup import rotation_list, xproj
        sage: rot = rotation_list(30, 45)
        sage: xproj(1,2,3,rot)
        0.6123724356957945
    """
def yproj(x, y, z, r):
    """
    Return the `y`-projection of `(x,y,z)` rotated by `r`.

    EXAMPLES::

        sage: from sage.groups.perm_gps.cubegroup import rotation_list, yproj
        sage: rot = rotation_list(30, 45)
        sage: yproj(1,2,3,rot)
        1.378497416975604
    """
def rotation_list(tilt, turn):
    """
    Return a list `[\\sin(\\theta), \\sin(\\phi), \\cos(\\theta), \\cos(\\phi)]` of
    rotations where `\\theta` is ``tilt`` and `\\phi` is ``turn``.

    EXAMPLES::

        sage: from sage.groups.perm_gps.cubegroup import rotation_list
        sage: rotation_list(30, 45)
        [0.49999999999999994, 0.7071067811865475, 0.8660254037844387, 0.7071067811865476]
    """
def polygon_plot3d(points, tilt: int = 30, turn: int = 30, **kwargs):
    '''
    Plot a polygon viewed from an angle determined by ``tilt``, ``turn``, and
    vertices ``points``.

    .. WARNING::

       The ordering of the points is important to get "correct"
       and if you add several of these plots together, the one added first
       is also drawn first (ie, addition of Graphics objects is not
       commutative).

    The following example produced a green-colored square with vertices
    at the points indicated.

    EXAMPLES::

        sage: from sage.groups.perm_gps.cubegroup import polygon_plot3d,green
        sage: P = polygon_plot3d([[1,3,1],[2,3,1],[2,3,2],[1,3,2],[1,3,1]],             # needs sage.plot
        ....:                    rgbcolor=green)
    '''
def inv_list(lst):
    """
    Input a list of ints `1, \\ldots, m` (in any order), outputs inverse
    perm.

    EXAMPLES::

        sage: from sage.groups.perm_gps.cubegroup import inv_list
        sage: L = [2,3,1]
        sage: inv_list(L)
        [3, 1, 2]
    """

face_polys: Incomplete

def create_poly(face, color):
    """
    Create the polygon given by ``face`` with color ``color``.

    EXAMPLES::

        sage: from sage.groups.perm_gps.cubegroup import create_poly, red
        sage: create_poly('ur', red)                                                    # needs sage.plot
        Graphics object consisting of 1 graphics primitive
    """

singmaster_indices: Incomplete

def index2singmaster(facet):
    """
    Translate index used (eg, 43) to Singmaster facet notation (eg,
    fdr).

    EXAMPLES::

        sage: from sage.groups.perm_gps.cubegroup import index2singmaster
        sage: index2singmaster(41)
        'dlf'
    """
def color_of_square(facet, colors=['lpurple', 'yellow', 'red', 'green', 'orange', 'blue']):
    """
    Return the color the facet has in the solved state.

    EXAMPLES::

        sage: from sage.groups.perm_gps.cubegroup import color_of_square
        sage: color_of_square(41)
        'blue'
    """

cubie_center_list: Incomplete

def cubie_centers(label):
    """
    Return the cubie center list element given by ``label``.

    EXAMPLES::

        sage: from sage.groups.perm_gps.cubegroup import cubie_centers
        sage: cubie_centers(3)
        [0, 2, 2]
    """
def cubie_colors(label, state0):
    '''
    Return the color of the cubie given by ``label`` at ``state0``.

    EXAMPLES::

        sage: from sage.groups.perm_gps.cubegroup import cubie_colors
        sage: G = CubeGroup()
        sage: g = G.parse("R*U")
        sage: cubie_colors(3, G.facets(g))
        [(1, 1, 1), (1, 0.63, 1), (1, 0.6, 0.3)]
    '''
def plot3d_cubie(cnt, clrs):
    """
    Plot the front, up and right face of a cubie centered at cnt and
    rgbcolors given by clrs (in the order FUR).

    Type ``P.show()`` to view.

    EXAMPLES::

        sage: from sage.groups.perm_gps.cubegroup import plot3d_cubie, blue, red, green
        sage: clrF = blue; clrU = red; clrR = green
        sage: P = plot3d_cubie([1/2,1/2,1/2],[clrF,clrU,clrR])                          # needs sage.plot
    """

class CubeGroup(PermutationGroup_generic):
    '''
    A python class to help compute Rubik\'s cube group actions.

    .. NOTE::

        This group is also available via ``groups.permutation.RubiksCube()``.

    EXAMPLES:

    If G denotes the cube group then it may be regarded as a
    subgroup of ``SymmetricGroup(48)``, where the 48 facets are labeled as
    follows.

    ::

        sage: rubik = CubeGroup()
        sage: rubik.display2d("")
                     ┌──────────────┐
                     │  1    2    3 │
                     │  4   top   5 │
                     │  6    7    8 │
        ┌────────────┼──────────────┼─────────────┬────────────┐
        │  9  10  11 │ 17   18   19 │ 25   26  27 │ 33  34  35 │
        │ 12 left 13 │ 20  front 21 │ 28 right 29 │ 36 rear 37 │
        │ 14  15  16 │ 22   23   24 │ 30   31  32 │ 38  39  40 │
        └────────────┼──────────────┼─────────────┴────────────┘
                     │ 41   42   43 │
                     │ 44 bottom 45 │
                     │ 46   47   48 │
                     └──────────────┘

    ::

        sage: rubik
        The Rubik\'s cube group with generators R,L,F,B,U,D in SymmetricGroup(48).

        TESTS::

            sage: groups.permutation.RubiksCube()
            The Rubik\'s cube group with generators R,L,F,B,U,D in SymmetricGroup(48).
    '''
    def __init__(self) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: rubik = CubeGroup()
            sage: TestSuite(rubik).run(skip='_test_enumerated_set_contains') # because the group is very large

        TESTS:

        Check that :issue:`11360` is fixed::

            sage: rubik = CubeGroup()
            sage: rubik.order()
            43252003274489856000
        """
    def gen_names(self):
        """
        Return the names of the generators.

        EXAMPLES::

            sage: rubik = CubeGroup()
            sage: rubik.gen_names()
            ['B', 'D', 'F', 'L', 'R', 'U']
        """
    def B(self):
        """
        Return the generator `B` in Singmaster notation.

        EXAMPLES::

            sage: rubik = CubeGroup()
            sage: rubik.B()
            (1,14,48,27)(2,12,47,29)(3,9,46,32)(33,35,40,38)(34,37,39,36)
        """
    def D(self):
        """
        Return the generator `D` in Singmaster notation.

        EXAMPLES::

            sage: rubik = CubeGroup()
            sage: rubik.D()
            (14,22,30,38)(15,23,31,39)(16,24,32,40)(41,43,48,46)(42,45,47,44)
        """
    def F(self):
        """
        Return the generator `F` in Singmaster notation.

        EXAMPLES::

            sage: rubik = CubeGroup()
            sage: rubik.F()
            (6,25,43,16)(7,28,42,13)(8,30,41,11)(17,19,24,22)(18,21,23,20)
        """
    def L(self):
        """
        Return the generator `L` in Singmaster notation.

        EXAMPLES::

            sage: rubik = CubeGroup()
            sage: rubik.L()
            (1,17,41,40)(4,20,44,37)(6,22,46,35)(9,11,16,14)(10,13,15,12)
        """
    def R(self):
        """
        Return the generator `R` in Singmaster notation.

        EXAMPLES::

            sage: rubik = CubeGroup()
            sage: rubik.R()
            (3,38,43,19)(5,36,45,21)(8,33,48,24)(25,27,32,30)(26,29,31,28)
        """
    def U(self):
        """
        Return the generator `U` in Singmaster notation.

        EXAMPLES::

            sage: rubik = CubeGroup()
            sage: rubik.U()
            (1,3,8,6)(2,5,7,4)(9,33,25,17)(10,34,26,18)(11,35,27,19)
        """
    def parse(self, mv, check: bool = True):
        '''
        This function allows one to create the permutation group element
        from a variety of formats.

        INPUT:

        - ``mv`` -- can one of the following:

          - ``list`` -- list of facets (as returned by
            self.facets())

          - ``dict`` -- list of faces (as returned by
            ``self.faces()``)

          - ``str`` -- either cycle notation (passed to GAP) or
            a product of generators or Singmaster notation

          - ``perm_group element`` -- returned as an element of ``self``

        - ``check`` -- check if the input is valid

        EXAMPLES::

            sage: C = CubeGroup()
            sage: C.parse(list(range(1,49)))
            ()
            sage: g = C.parse("L"); g
            (1,17,41,40)(4,20,44,37)(6,22,46,35)(9,11,16,14)(10,13,15,12)
            sage: C.parse(str(g)) == g
            True
            sage: facets = C.facets(g); facets
            [17, 2, 3, 20, 5, 22, 7, 8, 11, 13, 16, 10, 15, 9, 12, 14, 41, 18, 19, 44, 21, 46, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 6, 36, 4, 38, 39, 1, 40, 42, 43, 37, 45, 35, 47, 48]
            sage: C.parse(facets)
            (1,17,41,40)(4,20,44,37)(6,22,46,35)(9,11,16,14)(10,13,15,12)
            sage: C.parse(facets) == g
            True
            sage: faces = C.faces("L"); faces
            {\'back\': [[33, 34, 6], [36, 0, 4], [38, 39, 1]],
             \'down\': [[40, 42, 43], [37, 0, 45], [35, 47, 48]],
             \'front\': [[41, 18, 19], [44, 0, 21], [46, 23, 24]],
             \'left\': [[11, 13, 16], [10, 0, 15], [9, 12, 14]],
             \'right\': [[25, 26, 27], [28, 0, 29], [30, 31, 32]],
             \'up\': [[17, 2, 3], [20, 0, 5], [22, 7, 8]]}
            sage: C.parse(faces) == C.parse("L")
            True
            sage: C.parse("L\' R2") == C.parse("L^(-1)*R^2")
            True
            sage: C.parse("L\' R2")
            (1,40,41,17)(3,43)(4,37,44,20)(5,45)(6,35,46,22)(8,48)(9,14,16,11)(10,12,15,13)(19,38)(21,36)(24,33)(25,32)(26,31)(27,30)(28,29)
            sage: C.parse("L^4")
            ()
            sage: C.parse("L^(-1)*R")
            (1,40,41,17)(3,38,43,19)(4,37,44,20)(5,36,45,21)(6,35,46,22)(8,33,48,24)(9,14,16,11)(10,12,15,13)(25,27,32,30)(26,29,31,28)
        '''
    __call__ = parse
    def facets(self, g=None):
        '''
        Return the set of facets on which the group acts. This function is
        a "constant".

        EXAMPLES::

            sage: rubik = CubeGroup()
            sage: rubik.facets() == list(range(1,49))
            True
        '''
    def faces(self, mv):
        '''
        Return the dictionary of faces created by the effect of the move
        mv, which is a string of the form `X^a*Y^b*...`, where
        `X, Y, \\ldots` are in `\\{R,L,F,B,U,D\\}` and
        `a, b, \\ldots` are integers. We call this ordering of the faces
        the "BDFLRU, L2R, T2B ordering".

        EXAMPLES::

            sage: rubik = CubeGroup()

        Here is the dictionary of the solved state::

            sage: sorted(rubik.faces("").items())
            [(\'back\', [[33, 34, 35], [36, 0, 37], [38, 39, 40]]),
             (\'down\', [[41, 42, 43], [44, 0, 45], [46, 47, 48]]),
             (\'front\', [[17, 18, 19], [20, 0, 21], [22, 23, 24]]),
             (\'left\', [[9, 10, 11], [12, 0, 13], [14, 15, 16]]),
             (\'right\', [[25, 26, 27], [28, 0, 29], [30, 31, 32]]),
             (\'up\', [[1, 2, 3], [4, 0, 5], [6, 7, 8]])]

        Now the dictionary of the state obtained after making the move `R`
        followed by `L`::

            sage: sorted(rubik.faces("R*U").items())
            [(\'back\', [[48, 26, 27], [45, 0, 37], [43, 39, 40]]),
             (\'down\', [[41, 42, 11], [44, 0, 21], [46, 47, 24]]),
             (\'front\', [[9, 10, 8], [20, 0, 7], [22, 23, 6]]),
             (\'left\', [[33, 34, 35], [12, 0, 13], [14, 15, 16]]),
             (\'right\', [[19, 29, 32], [18, 0, 31], [17, 28, 30]]),
             (\'up\', [[3, 5, 38], [2, 0, 36], [1, 4, 25]])]
        '''
    def move(self, mv):
        '''
        Return the group element and the reordered list of facets, as
        moved by the list ``mv`` (read left-to-right)

        INPUT:

        - ``mv`` -- string of the form ``Xa*Yb*...``,
          where ``X``, ``Y``, ... are in ``R``, ``L``, ``F``, ``B``, ``U``,
          ``D`` and ``a``, ``b``, ... are integers

        EXAMPLES::

            sage: rubik = CubeGroup()
            sage: rubik.move("")[0]
            ()
            sage: rubik.move("R")[0]
            (3,38,43,19)(5,36,45,21)(8,33,48,24)(25,27,32,30)(26,29,31,28)
            sage: rubik.R()
            (3,38,43,19)(5,36,45,21)(8,33,48,24)(25,27,32,30)(26,29,31,28)
        '''
    def display2d(self, mv) -> None:
        '''
        Print the 2d representation of ``self``.

        EXAMPLES::

            sage: rubik = CubeGroup()
            sage: rubik.display2d("R")
                         ┌──────────────┐
                         │  1    2   38 │
                         │  4   top  36 │
                         │  6    7   33 │
            ┌────────────┼──────────────┼─────────────┬────────────┐
            │  9  10  11 │ 17   18    3 │ 27   29  32 │ 48  34  35 │
            │ 12 left 13 │ 20  front  5 │ 26 right 31 │ 45 rear 37 │
            │ 14  15  16 │ 22   23    8 │ 25   28  30 │ 43  39  40 │
            └────────────┼──────────────┼─────────────┴────────────┘
                         │ 41   42   19 │
                         │ 44 bottom 21 │
                         │ 46   47   24 │
                         └──────────────┘
        '''
    def repr2d(self, mv):
        '''
        Displays a 2D map of the Rubik\'s cube after the move mv has been
        made. Nothing is returned.

        EXAMPLES::

            sage: rubik = CubeGroup()
            sage: print(rubik.repr2d(""))
                         ┌──────────────┐
                         │  1    2    3 │
                         │  4   top   5 │
                         │  6    7    8 │
            ┌────────────┼──────────────┼─────────────┬────────────┐
            │  9  10  11 │ 17   18   19 │ 25   26  27 │ 33  34  35 │
            │ 12 left 13 │ 20  front 21 │ 28 right 29 │ 36 rear 37 │
            │ 14  15  16 │ 22   23   24 │ 30   31  32 │ 38  39  40 │
            └────────────┼──────────────┼─────────────┴────────────┘
                         │ 41   42   43 │
                         │ 44 bottom 45 │
                         │ 46   47   48 │
                         └──────────────┘

        ::

            sage: print(rubik.repr2d("R"))
                         ┌──────────────┐
                         │  1    2   38 │
                         │  4   top  36 │
                         │  6    7   33 │
            ┌────────────┼──────────────┼─────────────┬────────────┐
            │  9  10  11 │ 17   18    3 │ 27   29  32 │ 48  34  35 │
            │ 12 left 13 │ 20  front  5 │ 26 right 31 │ 45 rear 37 │
            │ 14  15  16 │ 22   23    8 │ 25   28  30 │ 43  39  40 │
            └────────────┼──────────────┼─────────────┴────────────┘
                         │ 41   42   19 │
                         │ 44 bottom 21 │
                         │ 46   47   24 │
                         └──────────────┘

        You can see the right face has been rotated but not the left face.
        '''
    def plot_cube(self, mv, title: bool = True, colors=...):
        '''
        Input the move mv, as a string in the Singmaster notation, and
        output the 2D plot of the cube in that state.

        Type ``P.show()`` to display any of the plots below.

        EXAMPLES::

            sage: rubik = CubeGroup()
            sage: P = rubik.plot_cube("R^2*U^2*R^2*U^2*R^2*U^2", title=False)           # needs sage.plot
            sage: # (R^2U^2)^3  permutes 2 pairs of edges (uf,ub)(fr,br)
            sage: P = rubik.plot_cube("R*L*D^2*B^3*L^2*F^2*R^2*U^3*D*R^3*D^2*F^3*B^3*D^3*F^2*D^3*R^2*U^3*F^2*D^3")      # needs sage.plot
            sage: # the superflip (in 20f* moves)
            sage: P = rubik.plot_cube("U^2*F*U^2*L*R^(-1)*F^2*U*F^3*B^3*R*L*U^2*R*D^3*U*L^3*R*D*R^3*L^3*D^2")           # needs sage.plot
            sage: # "superflip+4 spot" (in 26q* moves)
        '''
    def plot3d_cube(self, mv, title: bool = True):
        '''
        Displays `F,U,R` faces of the cube after the given move ``mv``. Mostly
        included for the purpose of drawing pictures and checking moves.

        INPUT:

        - ``mv`` -- string in the Singmaster notation
        - ``title`` -- boolean (default: ``True``); display the title information

        The first one below is "superflip+4 spot" (in 26q\\* moves) and the
        second one is the superflip (in 20f\\* moves). Type show(P) to view
        them.

        EXAMPLES::

            sage: rubik = CubeGroup()
            sage: P = rubik.plot3d_cube("U^2*F*U^2*L*R^(-1)*F^2*U*F^3*B^3*R*L*U^2*R*D^3*U*L^3*R*D*R^3*L^3*D^2")         # needs sage.plot
            sage: P = rubik.plot3d_cube("R*L*D^2*B^3*L^2*F^2*R^2*U^3*D*R^3*D^2*F^3*B^3*D^3*F^2*D^3*R^2*U^3*F^2*D^3")    # needs sage.plot
        '''
    def legal(self, state, mode: str = 'quiet'):
        '''
        Return 1 (true) if the dictionary ``state`` (in the
        same format as returned by the faces method) represents a legal
        position (or state) of the Rubik\'s cube or 0 (false)
        otherwise.

        EXAMPLES::

            sage: rubik = CubeGroup()
            sage: r0 = rubik.faces("")
            sage: r1 = {\'back\': [[33, 34, 35], [36, 0, 37], [38, 39, 40]], \'down\': [[41, 42, 43], [44, 0, 45], [46, 47, 48]],\'front\': [[17, 18, 19], [20, 0, 21], [22, 23, 24]],\'left\': [[9, 10, 11], [12, 0, 13], [14, 15, 16]],\'right\': [[25, 26, 27], [28, 0, 29], [30, 31, 32]],\'up\': [[1, 2, 3], [4, 0, 5], [6, 8, 7]]}
            sage: rubik.legal(r0)
            1
            sage: rubik.legal(r0,"verbose")
            (1, ())
            sage: rubik.legal(r1)
            0
        '''
    def solve(self, state, algorithm: str = 'default'):
        '''
        Solve the cube in the ``state``, given as a dictionary
        as in ``legal``. See the ``solve`` method
        of the RubiksCube class for more details.

        This may use GAP\'s ``EpimorphismFromFreeGroup`` and
        ``PreImagesRepresentative`` as explained below, if
        \'gap\' is passed in as the algorithm.

        This algorithm


        #. constructs the free group on 6 generators then computes a
           reasonable set of relations which they satisfy

        #. computes a homomorphism from the cube group to this free group
           quotient

        #. takes the cube position, regarded as a group element, and maps
           it over to the free group quotient

        #. using those relations and tricks from combinatorial group theory
           (stabilizer chains), solves the "word problem" for that element.

        #. uses python string parsing to rewrite that in cube notation.


        The Rubik\'s cube group has about `4.3 \\times 10^{19}`
        elements, so this process is time-consuming. See
        https://www.gap-system.org/Doc/Examples/rubik.html for an
        interesting discussion of some GAP code analyzing the Rubik\'s
        cube.

        EXAMPLES::

            sage: rubik = CubeGroup()
            sage: state = rubik.faces("R")
            sage: rubik.solve(state)
            \'R\'
            sage: state = rubik.faces("R*U")
            sage: rubik.solve(state, algorithm=\'gap\')       # long time
            \'R*U\'

        You can also check this another (but similar) way using the
        ``word_problem`` method (eg, G = rubik.group(); g =
        G("(3,38,43,19)(5,36,45,21)(8,33,48,24)(25,27,32,30)(26,29,31,28)");
        g.word_problem([b,d,f,l,r,u]), though the output will be less
        intuitive).
        '''

def cubie_faces():
    """
    This provides a map from the 6 faces of the 27 cubies to the 48
    facets of the larger cube.

    -1,-1,-1 is left, top, front

    EXAMPLES::

        sage: from sage.groups.perm_gps.cubegroup import cubie_faces
        sage: sorted(cubie_faces().items())
        [((-1, -1, -1), [6, 17, 11, 0, 0, 0]),
         ((-1, -1, 0), [4, 0, 10, 0, 0, 0]),
         ((-1, -1, 1), [1, 0, 9, 0, 35, 0]),
         ((-1, 0, -1), [0, 20, 13, 0, 0, 0]),
         ((-1, 0, 0), [0, 0, -5, 0, 0, 0]),
         ((-1, 0, 1), [0, 0, 12, 0, 37, 0]),
         ((-1, 1, -1), [0, 22, 16, 41, 0, 0]),
         ((-1, 1, 0), [0, 0, 15, 44, 0, 0]),
         ((-1, 1, 1), [0, 0, 14, 46, 40, 0]),
         ((0, -1, -1), [7, 18, 0, 0, 0, 0]),
         ((0, -1, 0), [-6, 0, 0, 0, 0, 0]),
         ((0, -1, 1), [2, 0, 0, 0, 34, 0]),
         ((0, 0, -1), [0, -4, 0, 0, 0, 0]),
         ((0, 0, 0), [0, 0, 0, 0, 0, 0]),
         ((0, 0, 1), [0, 0, 0, 0, -2, 0]),
         ((0, 1, -1), [0, 23, 0, 42, 0, 0]),
         ((0, 1, 0), [0, 0, 0, -1, 0, 0]),
         ((0, 1, 1), [0, 0, 0, 47, 39, 0]),
         ((1, -1, -1), [8, 19, 0, 0, 0, 25]),
         ((1, -1, 0), [5, 0, 0, 0, 0, 26]),
         ((1, -1, 1), [3, 0, 0, 0, 33, 27]),
         ((1, 0, -1), [0, 21, 0, 0, 0, 28]),
         ((1, 0, 0), [0, 0, 0, 0, 0, -3]),
         ((1, 0, 1), [0, 0, 0, 0, 36, 29]),
         ((1, 1, -1), [0, 24, 0, 43, 0, 30]),
         ((1, 1, 0), [0, 0, 0, 45, 0, 31]),
         ((1, 1, 1), [0, 0, 0, 48, 38, 32])]
    """

cubie_face_list: Incomplete
rand_colors: Incomplete

class RubiksCube(SageObject):
    '''
    The Rubik\'s cube (in a given state).

    EXAMPLES::

        sage: C = RubiksCube().move("R U R\'")
        sage: C.show3d()                                                                # needs sage.plot

    ::

        sage: C = RubiksCube("R*L"); C
                     ┌──────────────┐
                     │ 17    2   38 │
                     │ 20   top  36 │
                     │ 22    7   33 │
        ┌────────────┼──────────────┼─────────────┬────────────┐
        │ 11  13  16 │ 41   18    3 │ 27   29  32 │ 48  34   6 │
        │ 10 left 15 │ 44  front  5 │ 26 right 31 │ 45 rear  4 │
        │  9  12  14 │ 46   23    8 │ 25   28  30 │ 43  39   1 │
        └────────────┼──────────────┼─────────────┴────────────┘
                     │ 40   42   19 │
                     │ 37 bottom 21 │
                     │ 35   47   24 │
                     └──────────────┘
        sage: C.show()                                                                  # needs sage.plot
        sage: C.solve(algorithm=\'gap\')  # long time
        \'L*R\'
        sage: C == RubiksCube("L*R")
        True
    '''
    colors: Incomplete
    def __init__(self, state=None, history=[], colors=...) -> None:
        '''
        Initialize ``self``.

        EXAMPLES::

            sage: C = RubiksCube().move("R*U")
            sage: TestSuite(C).run()
        '''
    def move(self, g):
        '''
        Move the Rubik\'s cube by ``g``.

        EXAMPLES::

            sage: RubiksCube().move("R*U") == RubiksCube("R*U")
            True
        '''
    def undo(self):
        '''
        Undo the last move of the Rubik\'s cube.

        EXAMPLES::

            sage: C = RubiksCube()
            sage: D = C.move("R*U")
            sage: D.undo() == C
            True
        '''
    def facets(self):
        '''
        Return the facets of ``self``.

        EXAMPLES::

            sage: C = RubiksCube("R*U")
            sage: C.facets()
            [3, 5, 38, 2, 36, 1, 4, 25, 33, 34, 35, 12, 13, 14, 15, 16, 9, 10,
             8, 20, 7, 22, 23, 6, 19, 29, 32, 18, 31, 17, 28, 30, 48, 26, 27,
             45, 37, 43, 39, 40, 41, 42, 11, 44, 21, 46, 47, 24]
        '''
    def plot(self):
        '''
        Return a plot of ``self``.

        EXAMPLES::

            sage: C = RubiksCube("R*U")
            sage: C.plot()                                                              # needs sage.plot
            Graphics object consisting of 55 graphics primitives
        '''
    def show(self) -> None:
        '''
        Show a plot of ``self``.

        EXAMPLES::

            sage: C = RubiksCube("R*U")
            sage: C.show()                                                              # needs sage.plot
        '''
    def cubie(self, size, gap, x, y, z, colors, stickers: bool = True):
        '''
        Return the cubie at `(x,y,z)`.

        INPUT:

        - ``size`` -- the size of the cubie
        - ``gap`` -- the gap between cubies
        - ``x``, ``y``, ``z`` -- the position of the cubie
        - ``colors`` -- the list of colors
        - ``stickers`` -- boolean (default: ``True``); whether to display stickers

        EXAMPLES::

            sage: C = RubiksCube("R*U")
            sage: C.cubie(0.15, 0.025, 0,0,0, C.colors*3)                               # needs sage.plot
            Graphics3d Object
        '''
    def plot3d(self, stickers: bool = True):
        '''
        Return a 3D plot of ``self``.

        EXAMPLES::

            sage: C = RubiksCube("R*U")
            sage: C.plot3d()                                                            # needs sage.plot
            Graphics3d Object
        '''
    def show3d(self):
        '''
        Show a 3D plot of ``self``.

        EXAMPLES::

            sage: C = RubiksCube("R*U")
            sage: C.show3d()                                                            # needs sage.plot
        '''
    def __richcmp__(self, other, op):
        '''
        Comparison.

        INPUT:

        - ``other`` -- anything

        - ``op`` -- comparison operator

        EXAMPLES::

            sage: C = RubiksCube()
            sage: D = RubiksCube("R*U")
            sage: C < D
            True
            sage: C > D
            False
            sage: C == C
            True
            sage: C != D
            True
        '''
    def solve(self, algorithm: str = 'default', timeout: int = 15):
        '''
        Solve the Rubik\'s cube.

        INPUT:

        - ``algorithm`` -- must be one of the following:

          - ``hybrid`` -- (default) try ``kociemba`` for timeout seconds, then ``dietz``
          - ``kociemba`` -- use Dik T. Winter\'s program (reasonable speed, few moves)
          - ``dietz`` -- use Eric Dietz\'s cubex program (fast but lots of moves)
          - ``optimal`` -- use Michael Reid\'s optimal program (may take a long time)
          - ``gap`` -- use GAP word solution (can be slow)

        Any choice other than ``gap`` requires the optional package ``rubiks``.
        If the package is not installed, the ``gap`` algorithm is used by default.

        EXAMPLES::

            sage: C = RubiksCube("R U F L B D")
            sage: C.solve()           # optional - rubiks
            \'R U F L B D\'

        Dietz\'s program is much faster, but may give highly non-optimal
        solutions::

            sage: s = C.solve(\'dietz\'); s   # optional - rubiks
            "U\' L\' L\' U L U\' L U D L L D\' L\' D L\' D\' L D L\' U\' L D\' L\' U L\' B\'
             U\' L\' U B L D L D\' U\' L\' U L B L B\' L\' U L U\' L\' F\' L\' F L\' F L F\'
             L\' D\' L\' D D L D\' B L B\' L B\' L B F\' L F F B\' L F\' B D\' D\' L D B\'
             B\' L\' D\' B U\' U\' L\' B\' D\' F\' F\' L D F\'"
            sage: C2 = RubiksCube(s)  # optional - rubiks
            sage: C == C2             # optional - rubiks
            True
        '''
    def scramble(self, moves: int = 30):
        """
        Scramble the Rubik's cube.

        EXAMPLES::

            sage: C = RubiksCube()
            sage: C.scramble() # random
                         ┌──────────────┐
                         │  3    5   38 │
                         │  2   top  36 │
                         │  1    4   25 │
            ┌────────────┼──────────────┼─────────────┬────────────┐
            │ 33  34  35 │  9   10    8 │ 19   29  32 │ 48  26  27 │
            │ 12 left 13 │ 20  front  7 │ 18 right 31 │ 45 rear 37 │
            │ 14  15  16 │ 22   23    6 │ 17   28  30 │ 43  39  40 │
            └────────────┼──────────────┼─────────────┴────────────┘
                         │ 41   42   11 │
                         │ 44 bottom 21 │
                         │ 46   47   24 │
                         └──────────────┘
        """
