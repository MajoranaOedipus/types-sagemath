from sage.matroids.advanced import newlabel as newlabel
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.sets.set import Set as Set

def it(M, B1, nB1, lps) -> tuple[dict, list, list, list]:
    """
    Return points on and off the triangle and lines to be drawn for a rank 3
    matroid.

    INPUT:

    - ``M`` -- matroid
    - ``B1`` -- list of groundset elements of ``M`` that corresponds to a
      basis of matroid ``M``
    - ``nB1`` -- list of elements in the ground set of M that corresponds to
      ``M.simplify.groundset() \\ B1``
    - ``lps`` -- list of elements in the ground set of matroid M that are loops

    OUTPUT: a tuple containing 4 elements in this order:

    1. A dictionary containing 2-tuple (x,y) coordinates with
       ``M.simplify.groundset()`` elements that can be placed on the sides of
       the triangle as keys.
    2. A list of 3 lists of elements of ``M.simplify.groundset()`` that can
       be placed on the 3 sides of the triangle.
    3. A list of elements of ``M.simplify.groundset()`` that cane be placed
       inside the triangle in the geometric representation.
    4. A list of lists of elements of ``M.simplify.groundset()`` that
       correspond to lines in the geometric representation other than the sides
       of the triangle.

    EXAMPLES::

        sage: from sage.matroids import matroids_plot_helpers as mph
        sage: M = Matroid(ring=GF(2), matrix=[[1, 0, 0, 0, 1, 1, 1,0],
        ....: [0, 1, 0, 1, 0, 1, 1,0],[0, 0, 1, 1, 1, 0, 1,0]])
        sage: N = M.simplify()
        sage: B1 = list(N.basis())
        sage: nB1 = list(set(M.simplify().groundset())-set(B1))
        sage: pts,trilines,nontripts,curvedlines = mph.it(M,
        ....: B1,nB1,M.loops())
        sage: pts
        {1: (1.0, 0.0), 2: (1.5, 1.0), 3: (0.5, 1.0),
         4: (0, 0), 5: (1, 2), 6: (2, 0)}
        sage: trilines
        [[3, 4, 5], [2, 5, 6], [1, 4, 6]]
        sage: nontripts
        [0]
        sage: curvedlines
        [[0, 1, 5], [0, 2, 4], [0, 3, 6], [1, 2, 3], [1, 4, 6], [2, 5, 6],
         [3, 4, 5]]

    .. NOTE::

        This method does NOT do any checks.
    """
def trigrid(tripts) -> list[list]:
    """
    Return a grid of 4 points inside given 3 points as a list.

    INPUT:

    - ``tripts`` -- list of 3 lists of the form [x,y] where x and y are the
      Cartesian coordinates of a point

    OUTPUT: list of lists containing 4 points in following order:

    - 1. Barycenter of 3 input points.
    - 2,3,4. Barycenters of 1. with 3 different 2-subsets of input points
      respectively.

    EXAMPLES::

        sage: from sage.matroids import matroids_plot_helpers
        sage: points = matroids_plot_helpers.trigrid([[2,1],[4,5],[5,2]])
        sage: points
        [[3.6666666666666665, 2.6666666666666665],
         [3.222222222222222, 2.888888888888889],
         [4.222222222222222, 3.222222222222222],
         [3.5555555555555554, 1.8888888888888886]]

    .. NOTE::

        This method does NOT do any checks.
    """
def addnontripts(tripts_labels, nontripts_labels, ptsdict) -> dict:
    """
    Return modified ``ptsdict`` with additional keys and values corresponding
    to ``nontripts``.

    INPUT:

    - ``tripts`` -- list of 3 ground set elements that are to be placed on
      vertices of the triangle
    - ``ptsdict`` -- dictionary (at least) containing ground set elements in
      ``tripts`` as keys and their (x,y) position as values
    - ``nontripts`` -- list of ground set elements whose corresponding points
      are to be placed inside the triangle

    OUTPUT:

    A dictionary containing ground set elements in ``tripts`` as keys and
    their (x,y) position as values along with all keys and respective values
    in ``ptsdict``.

    EXAMPLES::

        sage: from sage.matroids import matroids_plot_helpers
        sage: from sage.matroids.advanced import setprint
        sage: ptsdict={'a':(0,0),'b':(1,2),'c':(2,0)}
        sage: ptsdict_1=matroids_plot_helpers.addnontripts(['a','b','c'],
        ....:         ['d','e','f'],ptsdict)
        sage: setprint(ptsdict_1)
        {'a': [0, 0], 'b': [1, 2], 'c': [0, 2], 'd': [0.6666666666666666, 1.0],
        'e': [0.6666666666666666, 0.8888888888888888],
        'f': [0.8888888888888888, 1.3333333333333333]}
        sage: ptsdict_2=matroids_plot_helpers.addnontripts(['a','b','c'],
        ....:         ['d','e','f','g','h'],ptsdict)
        sage: setprint(ptsdict_2)
        {'a': [0, 0], 'b': [1, 2], 'c': [0, 2], 'd': [0.6666666666666666, 1.0],
        'e': [0.6666666666666666, 0.8888888888888888],
        'f': [0.8888888888888888, 1.3333333333333333],
        'g': [0.2222222222222222, 1.0],
        'h': [0.5185185185185185, 0.5555555555555555]}

    .. NOTE::

        This method does NOT do any checks.
    """
def createline(ptsdict, ll, lineorders2=None) -> tuple[list, list, list, list]:
    """
    Return ordered lists of coordinates of points to be traversed to draw a
    2D line.

    INPUT:

    - ``ptsdict`` -- dictionary containing keys and their (x,y) position as
      values
    - ``ll`` -- list of keys in ``ptsdict`` through which a line is to be
      drawn
    - ``lineorders2`` -- (optional) list of ordered lists of keys in
      ``ptsdict`` such that if ll is setwise same as any of these then points
      corresponding to values of the keys will be traversed in that order thus
      overriding internal order deciding heuristic

    OUTPUT: a tuple containing 4 elements in this order:

    1. Ordered list of x-coordinates of values of keys in ``ll`` specified in
       ptsdict.
    2. Ordered list of y-coordinates of values of keys in ``ll`` specified
       in ptsdict.
    3. Ordered list of interpolated x-coordinates of points through which a
       line can be drawn.
    4. Ordered list of interpolated y-coordinates of points through which a
       line can be drawn.

    EXAMPLES::

        sage: from sage.matroids import matroids_plot_helpers
        sage: ptsdict = {'a':(1,3),'b':(2,1),'c':(4,5),'d':(5,2)}
        sage: x,y,x_i,y_i = matroids_plot_helpers.createline(ptsdict,
        ....: ['a','b','c','d'])
        sage: [len(x), len(y), len(x_i), len(y_i)]
        [4, 4, 100, 100]
        sage: G = line(zip(x_i, y_i), color='black', thickness=3, zorder=1)             # needs sage.plot
        sage: G += points(zip(x, y), color='black', size=300, zorder=2)                 # needs sage.plot
        sage: G.show()                                                                  # needs sage.plot
        sage: x,y,x_i,y_i = matroids_plot_helpers.createline(ptsdict,
        ....: ['a','b','c','d'],lineorders2=[['b','a','c','d'],
        ....: ['p','q','r','s']])
        sage: [len(x), len(y), len(x_i), len(y_i)]
        [4, 4, 100, 100]
        sage: G = line(zip(x_i, y_i), color='black', thickness=3, zorder=1)             # needs sage.plot
        sage: G += points(zip(x, y), color='black', size=300, zorder=2)                 # needs sage.plot
        sage: G.show()                                                                  # needs sage.plot

    .. NOTE::

        This method does NOT do any checks.
    """
def slp(M1, pos_dict=None, B=None) -> tuple:
    """
    Return simple matroid, loops and parallel elements of given matroid.

    INPUT:

    - ``M1`` -- matroid
    - ``pos_dict`` -- (optional) dictionary containing non loopy elements of
      ``M`` as keys and their (x,y) positions as keys. While simplifying the
      matroid, all except one element in a parallel class that is also
      specified in ``pos_dict`` will be retained.
    - ``B`` -- (optional) a basis of M1 that has been chosen for placement on
      vertices of triangle

    OUTPUT: a tuple containing 3 elements in this order:

    1. Simple matroid corresponding to ``M1``.
    2. Loops of matroid ``M1``.
    3. Elements that are in `M1.groundset()` but not in ground set of 1 or
       in 2

    EXAMPLES::

        sage: from sage.matroids import matroids_plot_helpers
        sage: from sage.matroids.advanced import setprint
        sage: M1 = Matroid(ring=GF(2), matrix=[[1, 0, 0, 0, 1, 1, 1,0,1,0,1],
        ....:                                  [0, 1, 0, 1, 0, 1, 1,0,0,1,0],
        ....:                                  [0, 0, 1, 1, 1, 0, 1,0,0,0,0]])
        sage: M, L, P = matroids_plot_helpers.slp(M1)                                   # needs sage.rings.finite_rings
        sage: M.is_simple()                                                             # needs sage.rings.finite_rings
        True
        sage: setprint([L,P])                                                           # needs sage.rings.finite_rings
        [{10, 8, 9}, {7}]
        sage: M1 = Matroid(ring=GF(2), matrix=[[1, 0, 0, 0, 1, 1, 1,0,1,0,1],
        ....:                                  [0, 1, 0, 1, 0, 1, 1,0,0,1,0],
        ....:                                  [0, 0, 1, 1, 1, 0, 1,0,0,0,0]])
        sage: posdict = {8: (0, 0),  1: (2, 0),  2: (1, 2),  3: (1.5, 1.0),
        ....:            4: (0.5, 1.0),  5: (1.0, 0.0), 6: (1.0, 0.6666666666666666)}
        sage: M, L, P = matroids_plot_helpers.slp(M1, pos_dict=posdict)                 # needs sage.rings.finite_rings
        sage: M.is_simple()                                                             # needs sage.rings.finite_rings
        True
        sage: setprint([L,P])                                                           # needs sage.rings.finite_rings
        [{0, 10, 9}, {7}]

    .. NOTE::

        This method does NOT do any checks.
    """
def addlp(M, M1, L, P, ptsdict, G=None, limits=None) -> tuple:
    """
    Return a graphics object containing loops (in inset) and parallel elements
    of matroid.

    INPUT:

    - ``M`` -- matroid
    - ``M1`` -- a simple matroid corresponding to ``M``
    - ``L`` -- list of elements in ``M.groundset()`` that are loops of matroid
      ``M``
    - ``P`` -- list of elements in ``M.groundset()`` not in
      ``M.simplify.groundset()`` or ``L``
    - ``ptsdict`` -- dictionary containing elements in ``M.groundset()`` not
      necessarily containing elements of ``L``
    - ``G`` -- (optional) a sage graphics object to which loops and parallel
      elements of matroid `M` added
    - ``limits`` -- (optional) current axes limits [xmin,xmax,ymin,ymax]

    OUTPUT: a 2-tuple containing:

    1. A sage graphics object containing loops and parallel elements of
       matroid ``M``
    2. axes limits array

    EXAMPLES::

        sage: from sage.matroids import matroids_plot_helpers
        sage: M = Matroid(ring=GF(2), matrix=[[1, 0, 0, 0, 1, 1, 1,0,1],
        ....:                                 [0, 1, 0, 1, 0, 1, 1,0,0],
        ....:                                 [0, 0, 1, 1, 1, 0, 1,0,0]])
        sage: M1, L, P = matroids_plot_helpers.slp(M)                                   # needs sage.rings.finite_rings
        sage: G, lims = matroids_plot_helpers.addlp(M,M1,L,P,{0:(0,0)})                 # needs sage.plot sage.rings.finite_rings
        sage: G.show(axes=False)                                                        # needs sage.plot sage.rings.finite_rings

    .. NOTE::

        This method does NOT do any checks.
    """
def line_hasorder(l, lodrs=None) -> tuple[bool, list]:
    """
    Determine if an order is specified for a line.

    INPUT:

    - ``l`` -- a line specified as a list of ground set elements
    - ``lordrs`` -- (optional) list of lists each specifying an order on
      a subset of ground set elements that may or may not correspond to a
      line in geometric representation

    OUTPUT: a tuple containing 2 elements in this order:

    1. A boolean indicating whether there is any list in ``lordrs`` that is
       setwise equal to ``l``.
    2. A list specifying an order on ``set(l)`` if 1. is True, otherwise
       an empty list.

    EXAMPLES::

        sage: from sage.matroids import matroids_plot_helpers
        sage: matroids_plot_helpers.line_hasorder(['a','b','c','d'],
        ....: [['a','c','d','b'],['p','q','r']])
        (True, ['a', 'c', 'd', 'b'])
        sage: matroids_plot_helpers.line_hasorder(['a','b','c','d'],
        ....: [['p','q','r'],['l','m','n','o']])
        (False, [])

    .. NOTE::

        This method does NOT do any checks.
    """
def lineorders_union(lineorders1, lineorders2) -> list:
    """
    Return a list of ordered lists of ground set elements that corresponds to
    union of two sets of ordered lists of ground set elements in a sense.

    INPUT:

    - ``lineorders1`` -- list of ordered lists specifying orders on subsets
      of ground set
    - ``lineorders2`` -- list of ordered lists specifying orders subsets of
      ground set

    OUTPUT:

    A list of ordered lists of ground set elements that are (setwise) in only
    one of ``lineorders1`` or ``lineorders2`` along with the ones in
    lineorder2 that are setwise equal to any list in lineorders1.

    EXAMPLES::

        sage: from sage.matroids import matroids_plot_helpers
        sage: matroids_plot_helpers.lineorders_union([['a','b','c'],
        ....: ['p','q','r'],['i','j','k','l']],[['r','p','q']])
        [['a', 'b', 'c'], ['p', 'q', 'r'], ['i', 'j', 'k', 'l']]
    """
def posdict_is_sane(M1, pos_dict) -> bool:
    """
    Return a boolean establishing sanity of ``posdict`` wrt matroid ``M``.

    INPUT:

    - ``M1`` -- matroid
    - ``posdict`` -- dictionary mapping ground set elements to (x,y)
      positions

    OUTPUT:

    A boolean that is ``True`` if posdict indeed has all the required elements
    to plot the geometric elements, otherwise ``False``.

    EXAMPLES::

        sage: from sage.matroids import matroids_plot_helpers
        sage: M1 = Matroid(ring=GF(2), matrix=[[1, 0, 0, 0, 1, 1, 1,0,1,0,1],
        ....:                                  [0, 1, 0, 1, 0, 1, 1,0,0,1,0],
        ....:                                  [0, 0, 1, 1, 1, 0, 1,0,0,0,0]])
        sage: pos_dict = {0: (0, 0),  1: (2, 0),  2: (1, 2),  3: (1.5, 1.0),
        ....: 4: (0.5, 1.0),  5: (1.0, 0.0), 6: (1.0, 0.6666666666666666)}
        sage: matroids_plot_helpers.posdict_is_sane(M1,pos_dict)                        # needs sage.rings.finite_rings
        True
        sage: pos_dict = {1: (2, 0),  2: (1, 2),  3: (1.5, 1.0),
        ....:             4: (0.5, 1.0), 5: (1.0, 0.0), 6: (1.0, 0.6666666666666666)}
        sage: matroids_plot_helpers.posdict_is_sane(M1,pos_dict)                        # needs sage.rings.finite_rings
        False

    .. NOTE::

        This method does NOT do any checks. ``M1`` is assumed to be a
        matroid and ``posdict`` is assumed to be a dictionary.
    """
def tracklims(lims, x_i=[], y_i=[]) -> list:
    """
    Return modified limits list.

    INPUT:

    - ``lims`` -- list with 4 elements ``[xmin,xmax,ymin,ymax]``
    - ``x_i`` -- new x values to track
    - ``y_i`` -- new y values to track

    OUTPUT: list with 4 elements ``[xmin,xmax,ymin,ymax]``

    EXAMPLES::

        sage: from sage.matroids import matroids_plot_helpers
        sage: matroids_plot_helpers.tracklims([0,5,-1,7],[1,2,3,6,-1],
        ....: [-1,2,3,6])
        [-1, 6, -1, 7]

    .. NOTE::

        This method does NOT do any checks.
    """
def geomrep(M1, B1=None, lineorders1=None, pd=None, sp: bool = False):
    """
    Return a sage graphics object containing geometric representation of
    matroid M1.

    INPUT:

    - ``M1`` -- matroid
    - ``B1`` -- (optional) list of elements in ``M1.groundset()`` that
      correspond to a basis of ``M1`` and will be placed as vertices of the
      triangle in the geometric representation of ``M1``
    - ``lineorders1`` -- (optional) list of ordered lists of elements of
      ``M1.groundset()`` such that if a line in geometric representation is
      setwise same as any of these then points contained will be traversed in
      that order thus overriding internal order deciding heuristic
    - ``pd`` -- (optional) dictionary mapping ground set elements to their
      (x,y) positions
    - ``sp`` -- (optional) if ``True``, a positioning dictionary and line orders
      will be placed in ``M._cached_info``

    OUTPUT:

    A sage graphics object of type <class 'sage.plot.graphics.Graphics'> that
    corresponds to the geometric representation of the matroid.

    EXAMPLES::

        sage: from sage.matroids import matroids_plot_helpers
        sage: M = matroids.catalog.P7()
        sage: G = matroids_plot_helpers.geomrep(M)                                      # needs sage.plot
        sage: G.show(xmin=-2, xmax=3, ymin=-2, ymax=3)                                  # needs sage.plot
        sage: M = matroids.catalog.P7()
        sage: G = matroids_plot_helpers.geomrep(M, lineorders1=[['f','e','d']])         # needs sage.plot
        sage: G.show(xmin=-2, xmax=3, ymin=-2, ymax=3)                                  # needs sage.plot

    .. NOTE::

        This method does NOT do any checks.
    """
