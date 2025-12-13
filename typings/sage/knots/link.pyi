from sage.graphs.digraph import DiGraph as DiGraph
from sage.graphs.graph import Graph as Graph
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.flatten import flatten as flatten
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.laurent_polynomial_ring import LaurentPolynomialRing as LaurentPolynomialRing
from sage.structure.sage_object import SageObject as SageObject

class Link(SageObject):
    '''
    A link.

    A link is an embedding of one or more copies of `\\mathbb{S}^1` in
    `\\mathbb{S}^3`, considered up to ambient isotopy. That is, a link
    represents the idea of one or more tied ropes. Every knot is a link,
    but not every link is a knot.

    A link can be created by using one of the conventions mentioned below:

    Braid:

    - The closure of a braid is a link::

        sage: B = BraidGroup(8)
        sage: L = Link(B([-1, -1, -1, -2, 1, -2, 3, -2, 3])); L
        Link with 1 component represented by 9 crossings
        sage: L = Link(B([1, 2, 1, -2, -1])); L
        Link with 2 components represented by 5 crossings

      .. NOTE::

          The strands of the braid that have no crossings at all
          are removed.

    - Oriented Gauss Code:

      Label the crossings from `1` to `n` (where `n` is the number of
      crossings) and start moving along the link. Trace every component of
      the link, by starting at a particular point on one component of the
      link and writing down each of the crossings that you encounter until
      returning to the starting point. The crossings are written with sign
      depending on whether we cross them as over or undercrossing. Each
      component is then represented as a list whose elements are the
      crossing numbers. A second list of `+1` and `-1`\'s keeps track of
      the orientation of each crossing::

        sage: L = Link([[[-1, 2, 3, -4, 5, -6, 7, 8, -2, -5, 6, 1, -8, -3, 4, -7]],
        ....:           [-1, -1, -1, -1, 1, 1, -1, 1]])
        sage: L
        Link with 1 component represented by 8 crossings

      For links there may be more than one component and the input is
      as follows::

        sage: L = Link([[[-1, 2], [-3, 4], [1, 3, -4, -2]], [-1, -1, 1, 1]])
        sage: L
        Link with 3 components represented by 4 crossings

    - Planar Diagram (PD) Code:

      The diagram of the link is formed by segments that are adjacent to
      the crossings. Label each one of this segments with a positive number,
      and for each crossing, write down the four incident segments. The
      order of these segments is anti-clockwise, starting with the incoming
      undercrossing.

      There is no particular distinction between knots and links for
      this input.

    EXAMPLES:

    One of the representations of the trefoil knot::

        sage: L = Link([[1, 5, 2, 4], [5, 3, 6, 2], [3, 1, 4, 6]])
        sage: L
        Link with 1 component represented by 3 crossings

    .. PLOT::
        :width: 300 px

        L = Link([[1, 5, 2, 4], [5, 3, 6, 2], [3, 1, 4, 6]])
        sphinx_plot(L.plot())

    One of the representations of the Hopf link::

        sage: L = Link([[1, 4, 2, 3], [4, 1, 3, 2]])
        sage: L
        Link with 2 components represented by 2 crossings

    .. PLOT::
        :width: 300 px

        L = Link([[1, 4, 2, 3], [4, 1, 3, 2]])
        sphinx_plot(L.plot())

    We can construct links from the braid group::

        sage: B = BraidGroup(4)
        sage: L = Link(B([-1, -1, -1, -2, 1, -2, 3, -2])); L
        Link with 2 components represented by 8 crossings

    .. PLOT::
        :width: 300 px

        B = BraidGroup(4)
        L = Link(B([-1, -1, -1, -2, 1, -2, 3, -2]))
        sphinx_plot(L.plot())

    ::

        sage: L = Link(B([1, 2, 1, 3])); L
        Link with 2 components represented by 4 crossings

    .. PLOT::
        :width: 300 px

        B = BraidGroup(4)
        L = Link(B([1, 2, 1, 3]))
        sphinx_plot(L.plot())

    We construct the "monster" unknot using a planar code, and
    then construct the oriented Gauss code and braid representation::

        sage: L = Link([[3,4,2,1], [8,7,1,9], [5,3,7,6], [4,5,6,18],
        ....:           [17,18,8,19], [9,14,11,10], [10,11,13,12],
        ....:           [12,13,15,19], [20,15,14,16], [16,2,17,20]])
        sage: L.oriented_gauss_code()
        [[[1, -4, 3, -1, 10, -9, 6, -7, 8, 5, 4, -3, 2, -6, 7, -8, 9, -10, -5, -2]],
         [1, -1, 1, 1, 1, -1, -1, -1, -1, -1]]
        sage: L.braid()
        s0*s1^-3*s2^-1*s1*s3*s2^2*s1^-1*s0^-1*s2*s1^-1*s3^-1*s2*s1^-1

    .. PLOT::
        :width: 300 px

        L = Link([[3,4,2,1], [8,7,1,9], [5,3,7,6], [4,5,6,18],
                  [17,18,8,19], [9,14,11,10], [10,11,13,12],
                  [12,13,15,19], [20,15,14,16], [16,2,17,20]])
        sphinx_plot(L.plot())

    We construct the Ochiai unknot by using an oriented Gauss code::

        sage: L = Link([[[1,-2,-3,-8,-12,13,-14,15,-7,-1,2,-4,10,11,-13,12,
        ....:             -11,-16,4,3,-5,6,-9,7,-15,14,16,-10,8,9,-6,5]],
        ....:           [-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,-1,-1,-1]])
        sage: L.pd_code()
        [[10, 1, 11, 2], [2, 11, 3, 12], [3, 21, 4, 20], [12, 20, 13, 19],
         [21, 1, 22, 32], [31, 23, 32, 22], [9, 24, 10, 25], [4, 30, 5, 29],
         [23, 31, 24, 30], [28, 13, 29, 14], [17, 15, 18, 14], [5, 16, 6, 17],
         [15, 6, 16, 7], [7, 26, 8, 27], [25, 8, 26, 9], [18, 27, 19, 28]]

    .. PLOT::
        :width: 300 px

        L = Link([[[1,-2,-3,-8,-12,13,-14,15,-7,-1,2,-4,10,11,-13,12,
                    -11,-16,4,3,-5,6,-9,7,-15,14,16,-10,8,9,-6,5]],
                  [-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,-1,-1,-1]])
        sphinx_plot(L.plot())

    We construct the knot `7_1` and compute some invariants::

        sage: B = BraidGroup(2)
        sage: L = Link(B([1]*7))

    .. PLOT::
        :width: 300 px

        B = BraidGroup(2)
        L = Link(B([1]*7))
        sphinx_plot(L.plot())

    ::

        sage: L.alexander_polynomial()
        t^-3 - t^-2 + t^-1 - 1 + t - t^2 + t^3
        sage: L.jones_polynomial()
        -t^10 + t^9 - t^8 + t^7 - t^6 + t^5 + t^3
        sage: L.determinant()
        7
        sage: L.signature()
        -6

    The links here have removed components in which no strand is used::

        sage: B = BraidGroup(8)
        sage: b = B([1])
        sage: L = Link(b)
        sage: b.components_in_closure()
        7
        sage: L.number_of_components()
        1
        sage: L.braid().components_in_closure()
        1
        sage: L.braid().parent()
        Braid group on 2 strands

    .. WARNING::

        Equality of knots is done by comparing the corresponding braids,
        which may give false negatives.

    .. NOTE::

        The behavior of removing unused strands from an element of a
        braid group may change without notice in the future. Do not
        rely on this feature.

    .. TODO::

        Implement methods to creating new links from previously created links.
    '''
    def __init__(self, data) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: B = BraidGroup(8)
            sage: L = Link(B([-1, -1, -1, -2,1, -2, 3, -2]))
            sage: TestSuite(L).run()
            sage: L = Link(B([1, 2, 1]))
            sage: TestSuite(L).run()
            sage: L = Link(B.one())

            sage: L = Link([[1, 1, 2, 2]])
            sage: TestSuite(L).run()
            sage: L = Link([])
            sage: L = Link([[], []])

            sage: Link([[[-1, 2, -1, 2]],  [1, 1, 1, 1]])
            Traceback (most recent call last):
            ...
            ValueError: invalid input: data is not a valid oriented Gauss code

            sage: Link([[[-1, 2, 3, 4]]])
            Traceback (most recent call last):
            ...
            ValueError: invalid PD code: crossings must be represented by four segments

            sage: L = Link([[1, 5, 2, 4], [5, 3, 6, 2], [3, 1, 4, 3]])
            Traceback (most recent call last):
            ...
            ValueError: invalid PD code: each segment must appear twice

        Segments in PD code must be labelled by positive integers::

            sage: code = [(2, 5, 3, 0), (4, 1, 5, 2), (0, 3, 1, 4)]
            sage: Knot(code)
            Traceback (most recent call last):
            ...
            ValueError: invalid PD code: segment label 0 not allowed

            sage: L = Link(5)
            Traceback (most recent call last):
            ...
            ValueError: invalid input: data must be either a list or a braid

        Verify that :issue:`29692` is fixed::

            sage: B = BraidGroup(5)
            sage: L = Link(B([3,4,3,-4])); L
            Link with 1 component represented by 4 crossings
            sage: L.braid()
            s0*s1*s0*s1^-1

        PD code can be a list of 4-tuples::

            sage: code = [(2, 5, 3, 6), (4, 1, 5, 2), (6, 3, 1, 4)]
            sage: K = Knot(code); K.alexander_polynomial()
            t^-1 - 1 + t
        """
    def arcs(self, presentation: str = 'pd'):
        """
        Return the arcs of ``self``.

        Arcs are the connected components of the planar diagram.

        INPUT:

        - ``presentation`` -- one of the following:

          * ``'pd'`` -- the arcs are returned as lists of parts in the PD code
          * ``'gauss_code'`` -- the arcs are returned as pieces of the Gauss
            code that start with a negative number, and end with the
            following negative one; of there exist a closed arc,
            it is returned as a list of positive numbers only

        OUTPUT: list of lists representing the arcs based upon ``presentation``

        EXAMPLES::

            sage: K = Knot([[[1,-2,3,-1,2,-3]],[1,1,1]])
            sage: K.arcs()
            [[1, 2], [3, 4], [5, 6]]
            sage: K.arcs(presentation='gauss_code')
            [[-3, 1, -2], [-2, 3, -1], [-1, 2, -3]]

        ::

            sage: L = Link([[1, 2, 3, 4], [3, 2, 1, 4]])
            sage: L.arcs()
            [[2, 4], [1], [3]]
            sage: L.arcs(presentation='gauss_code')
            [[-2, -1], [-1, -2], [2, 1]]
            sage: L.gauss_code()
            [[-1, -2], [2, 1]]
        """
    def fundamental_group(self, presentation: str = 'wirtinger'):
        """
        Return the fundamental group of the complement of ``self``.

        INPUT:

        - ``presentation`` -- string; one of the following:

          * ``'wirtinger'`` -- (default) the Wirtinger presentation
            (see :wikipedia:`Link_group`)
          * ``'braid'`` -- the presentation is given by the braid action
            on the free group (see chapter 2 of [Bir1975]_)

        OUTPUT: a finitely presented group

        EXAMPLES::

            sage: L = Link([[1, 4, 3, 2], [3, 4, 1, 2]])
            sage: L.fundamental_group()
            Finitely presented group < x0, x1, x2 | x1*x0^-1*x2^-1*x0, x2*x0*x1^-1*x0^-1 >
            sage: L.fundamental_group('braid')
            Finitely presented group < x0, x1 | 1, 1 >

        We can see, for instance, that the  two presentations of the group
        of the figure eight knot correspond to isomorphic groups::

            sage: K8 = Knot([[[1, -2, 4, -3, 2, -1, 3, -4]], [1, 1, -1, -1]])
            sage: GA = K8.fundamental_group(); GA
            Finitely presented group < x0, x1, x2, x3 |
             x2*x0*x3^-1*x0^-1, x0*x2*x1^-1*x2^-1,
             x1*x3^-1*x2^-1*x3, x3*x1^-1*x0^-1*x1 >
            sage: GB = K8.fundamental_group(presentation='braid'); GB
            Finitely presented group
             < x0, x1, x2 | x1*x2^-1*x1^-1*x0*x1*x2*x1*x2^-1*x1^-1*x0^-1*x1*x2*x1^-1*x0^-1,
                            x1*x2^-1*x1^-1*x0*x1*x2*x1^-1*x2^-1*x1^-1*x0^-1*x1*x2*x1^-1*x0*x1*x2*x1*x2^-1*x1^-1*x0^-1*x1*x2*x1^-2,
                            x1*x2^-1*x1^-1*x0*x1*x2*x1^-1*x2^-1 >
            sage: GA.simplified()
            Finitely presented group
             < x0, x1 | x1^-1*x0*x1*x0^-1*x1*x0*x1^-1*x0^-1*x1*x0^-1 >
            sage: GB.simplified()
            Finitely presented group
             < x0, x2 | x2^-1*x0*x2^-1*x0^-1*x2*x0*x2^-1*x0*x2*x0^-1 >
        """
    def __eq__(self, other):
        """
        Check equality.

        TESTS::

            sage: B = BraidGroup(8)
            sage: L1 = Link(B([-1, -1, -1, -2, 1, -2, 3, -2, 5, 4]))
            sage: L2 = Link(B([-1, -1, -1, -2, 1, -2, 3, -2, 5, 4]))
            sage: L1 == L2
            True
            sage: L3 = Link(B([-1, -1, -1, -2, 1, -2, 3, -2]))
            sage: L1 == L3
            False
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: B = BraidGroup(8)
            sage: L1 = Link(B([-1, -1, -1, -2, 1, -2, 3, -2, 5, 4]))
            sage: H = hash(L1)
        """
    def __ne__(self, other):
        """
        Check inequality.

        TESTS::

            sage: B = BraidGroup(8)
            sage: L1 = Link(B([-1, -1, -1, -2, 1, -2, 3, -2, 5, 4]))
            sage: L2 = Link(B([-1, -1, -1, -2, 1, -2, 3, -2, 5, 4]))
            sage: L1 != L2
            False
            sage: L3 = Link(B([-1, -1, -1, -2, 1, -2, 3, -2]))
            sage: L1 != L3
            True
        """
    def braid(self, remove_loops: bool = False):
        """
        Return a braid representation of ``self``.

        INPUT:

        - ``remove_loops`` -- boolean (default: ``False``); if set to ``True``
          loops will be removed first. This can reduce the number of strands
          needed for an ambient isotopic braid closure. However, this can lead
          to a loss of the regular isotopy.

        OUTPUT: an element in the braid group

        .. WARNING::

            For the unknot with no crossings, this returns the identity
            of the braid group with 2 strands because this disregards
            strands with no crossings.

        EXAMPLES::

            sage: L = Link([[2, 4, 1, 3], [4, 2, 3, 1]])
            sage: L.braid()
            s^2
            sage: L = Link([[[-1, 2, -3, 1, -2, 3]], [-1, -1, -1]])
            sage: L.braid()
            s^-3
            sage: L = Link([[1,7,2,8], [8,5,9,4], [3,10,4,9], [10,6,7,1], [5,2,6,3]])
            sage: L.braid()
            (s0*s1^-1)^2*s1^-1

        using ``remove_loops=True``::

            sage: L = Link([[2, 7, 1, 1], [7, 3, 9, 2], [4, 11, 3, 9], [11, 5, 5, 4]])
            sage: L.braid()
            s0*s1^-1*s2*s3^-1
            sage: L.braid(remove_loops=True)
            1

        TESTS::

            sage: L = Link([])
            sage: L.braid()
            1
            sage: L = Link([[], []])
            sage: L.braid()
            1

        Check that :issue:`25050` is solved::

            sage: A = Link([[[1, 2, -2, -1, -3, -4, 4, 3]], [1, 1, 1, 1]])
            sage: A.braid()
            s0*s1*s2*s3

        Check that :issue:`36884` is solved::

            sage: L = Link([[1, 7, 2, 6], [3, 1, 4, 8], [5, 5, 6, 4], [7, 3, 8, 2]])
            sage: L.braid()
            s0^3*s1*s0*s1^-1
            sage: L.braid(remove_loops=True)
            s^3
        """
    def khovanov_homology(self, ring=..., height=None, degree=None):
        """
        Return the Khovanov homology of the link.

        INPUT:

        - ``ring`` -- (default: ``ZZ``) the coefficient ring

        - ``height`` -- the height of the homology to compute,
          if not specified, all the heights are computed

        - ``degree`` -- the degree of the homology to compute,
          if not specified, all the degrees are computed

        OUTPUT:

        The Khovanov homology of the Link. It is given as a dictionary
        whose keys are the different heights. For each height, the
        homology is given as another dictionary whose keys are the degrees.

        EXAMPLES::

            sage: K = Link([[[1, -2, 3, -1, 2, -3]],[-1, -1, -1]])
            sage: K.khovanov_homology()                                                 # needs sage.modules
            {-9: {-3: Z},
             -7: {-3: 0, -2: C2},
             -5: {-3: 0, -2: Z, -1: 0, 0: 0},
             -3: {-3: 0, -2: 0, -1: 0, 0: Z},
             -1: {0: Z}}

        The figure eight knot::

            sage: L = Link([[1, 6, 2, 7], [5, 2, 6, 3], [3, 1, 4, 8], [7, 5, 8, 4]])
            sage: L.khovanov_homology(height=-1)                                        # needs sage.modules
            {-1: {-2: 0, -1: Z, 0: Z, 1: 0, 2: 0}}

        The Hopf link::

            sage: # needs sage.modules
            sage: B = BraidGroup(2)
            sage: b = B([1, 1])
            sage: K = Link(b)
            sage: K.khovanov_homology(degree=2)
            {2: {2: 0}, 4: {2: Z}, 6: {2: Z}}

        TESTS:

        Check that :issue:`31001` is fixed::

            sage: # needs sage.modules
            sage: L = Link([])
            sage: L.khovanov_homology()
            {-1: {0: Z}, 1: {0: Z}}
            sage: L.khovanov_homology(height=-1)
            {-1: {0: Z}}
            sage: L.khovanov_homology(height=0)
            {}
            sage: L.khovanov_homology(QQ, height=1)
            {1: {0: Vector space of dimension 1 over Rational Field}}
            sage: L.khovanov_homology(GF(2), degree=0)
            {-1: {0: Vector space of dimension 1 over Finite Field of size 2},
             1: {0: Vector space of dimension 1 over Finite Field of size 2}}
            sage: L.khovanov_homology(degree=1)
            {}
            sage: L.khovanov_homology(degree=0, height=1)
            {1: {0: Z}}
            sage: L.khovanov_homology(degree=1, height=1)
            {}
        """
    def oriented_gauss_code(self):
        """
        Return the oriented Gauss code of ``self``.

        The oriented Gauss code has two parts:

        a. the Gauss code

        b. the orientation of each crossing

        The following orientation was taken into consideration for
        construction of knots:

        From the outgoing of the overcrossing if we move in the clockwise
        direction to reach the outgoing of the undercrossing then we label
        that crossing as `-1`.

        From the outgoing of the overcrossing if we move in the anticlockwise
        direction to reach the outgoing of the undercrossing then we label
        that crossing as `+1`.

        One more consideration we take in while constructing the orientation
        is the order of the orientation is same as the ordering of the
        crossings in the Gauss code.

        .. NOTE::

            Convention: under is denoted by `-1`, and over by `+1` in the
            crossing info.

        EXAMPLES::

            sage: L = Link([[1, 10, 2, 11], [6, 3, 7, 2], [3, 9, 4, 12],
            ....:           [9, 6, 10, 5], [8, 4, 5, 1], [11, 7, 12, 8]])
            sage: L.oriented_gauss_code()
            [[[-1, 2, -3, 5], [4, -2, 6, -5], [-4, 1, -6, 3]], [-1, 1, 1, 1, -1, -1]]
            sage: L = Link([[1, 3, 2, 4], [6, 2, 3, 1], [7, 5, 8, 4], [5, 7, 6, 8]])
            sage: L.oriented_gauss_code()
            [[[-1, 2], [-3, 4], [1, 3, -4, -2]], [-1, -1, 1, 1]]

            sage: B = BraidGroup(8)
            sage: b = B([1, 1, 1, 1, 1])
            sage: L = Link(b)
            sage: L.oriented_gauss_code()
            [[[1, -2, 3, -4, 5, -1, 2, -3, 4, -5]], [1, 1, 1, 1, 1]]

        TESTS::

            sage: L = Link([])
            sage: L.oriented_gauss_code()
            [[], []]

            sage: L = Link(BraidGroup(2).one())
            sage: L.oriented_gauss_code()
            [[], []]
        """
    def pd_code(self):
        """
        Return the planar diagram code of ``self``.

        The planar diagram is returned in the following format.

        We construct the crossing by starting with the entering component
        of the undercrossing, move in the anti-clockwise direction (see the
        note below) and then generate the list. If the crossing is given by
        `[a, b, c, d]`, then we interpret this information as:

        1. `a` is the entering component of the undercrossing;
        2. `b, d` are the components of the overcrossing;
        3. `c` is the leaving component of the undercrossing.

        .. NOTE::

            Until version 10.0 the convention to read the ``PD`` code has been
            to list the components in clockwise direction. As of version 10.1
            the convention has changed, since it was opposite to the usage in
            most other places.

            Thus, if you use ``PD`` codes from former Sage releases with this
            version you should check for the correct mirror type.

        EXAMPLES::

            sage: L = Link([[[1, -2, 3, -4, 2, -1, 4, -3]], [1, 1, -1, -1]])
            sage: L.pd_code()
            [[6, 2, 7, 1], [2, 6, 3, 5], [8, 3, 1, 4], [4, 7, 5, 8]]

            sage: B = BraidGroup(2)
            sage: b = B([1, 1, 1, 1, 1])
            sage: L = Link(b)
            sage: L.pd_code()
            [[2, 4, 3, 1], [4, 6, 5, 3], [6, 8, 7, 5], [8, 10, 9, 7], [10, 2, 1, 9]]
            sage: L = Link([[[2, -1], [1, -2]], [1, 1]])
            sage: L.pd_code()
            [[2, 4, 1, 3], [4, 2, 3, 1]]
            sage: L = Link([[1, 2, 3, 3], [2, 4, 5, 5], [4, 1, 7, 7]])
            sage: L.pd_code()
            [[1, 2, 3, 3], [2, 4, 5, 5], [4, 1, 7, 7]]

        TESTS::

            sage: L = Link([[], []])
            sage: L.pd_code()
            []

            sage: L = Link(BraidGroup(2).one())
            sage: L.pd_code()
            []
        """
    def gauss_code(self):
        """
        Return the Gauss code of ``self``.

        The Gauss code is generated by the following procedure:

        a. Number the crossings from `1` to `n`.
        b. Select a point on the knot and start moving along the component.
        c. At each crossing, take the number of the crossing, along with
           sign, which is `-` if it is an undercrossing and `+` if it is a
           overcrossing.

        EXAMPLES::

            sage: L = Link([[1, 4, 2, 3], [4, 1, 3, 2]])
            sage: L.gauss_code()
            [[-1, 2], [1, -2]]

            sage: B = BraidGroup(8)
            sage: L = Link(B([1, -2, 1, -2, -2]))
            sage: L.gauss_code()
            [[-1, 3, -4, 5], [1, -2, 4, -5, 2, -3]]

            sage: L = Link([[[-1, 2], [-3, 4], [1, 3, -4, -2]], [-1, -1, 1, 1]])
            sage: L.gauss_code()
            [[-1, 2], [-3, 4], [1, 3, -4, -2]]
        """
    def dowker_notation(self):
        """
        Return the Dowker notation of ``self``.

        Similar to the PD code we number the components, so every crossing
        is represented by four numbers. We focus on the incoming entities
        of the under and the overcrossing. It is the pair of incoming
        undercrossing and the incoming overcrossing. This information at
        every crossing gives the Dowker notation.

        OUTPUT:

        A list containing the pair of incoming under cross and the incoming
        over cross.

        EXAMPLES::

            sage: L = Link([[[-1, 2, -3, 4, 5, 1, -2, 6, 7, 3, -4, -7, -6,-5]],
            ....:           [-1, -1, -1, -1, 1, -1, 1]])
            sage: L.dowker_notation()
            [(1, 6), (7, 2), (3, 10), (11, 4), (14, 5), (13, 8), (12, 9)]

            sage: B = BraidGroup(4)
            sage: L = Link(B([1, 2, 1, 2]))
            sage: L.dowker_notation()
            [(2, 1), (3, 5), (6, 4), (7, 9)]
            sage: L = Link([[1, 4, 2, 3], [4, 1, 3, 2]])
            sage: L.dowker_notation()
            [(1, 3), (4, 2)]
        """
    @cached_method
    def seifert_matrix(self):
        """
        Return the Seifert matrix associated with ``self``.

        ALGORITHM:

        This is the algorithm presented in Section 3.3 of [Col2013]_.

        OUTPUT:

        The intersection matrix of a (not necessarily minimal) Seifert surface.

        EXAMPLES::

            sage: # needs sage.modules
            sage: B = BraidGroup(4)
            sage: L = Link(B([-1, 3, 1, 3]))
            sage: L.seifert_matrix()
            [ 0  0]
            [ 0 -1]
            sage: B = BraidGroup(8)
            sage: L = Link(B([-1, 3, 1, 5, 1, 7, 1, 6]))
            sage: L.seifert_matrix()
            [ 0  0  0]
            [ 1 -1  0]
            [ 0  1 -1]
            sage: L = Link(B([-2, 4, 1, 6, 1, 4]))
            sage: L.seifert_matrix()
            [-1  0]
            [ 0 -1]
        """
    @cached_method
    def number_of_components(self):
        """
        Return the number of connected components of ``self``.

        OUTPUT: number of connected components

        EXAMPLES::

            sage: B = BraidGroup(4)
            sage: L = Link(B([-1, 3, 1, 3]))
            sage: L.number_of_components()
            4
            sage: B = BraidGroup(8)
            sage: L = Link(B([-2, 4, 1, 6, 1, 4]))
            sage: L.number_of_components()
            5
            sage: L = Link(B([1, 2, 1, 2]))
            sage: L.number_of_components()
            1
            sage: L = Link(B.one())
            sage: L.number_of_components()
            1
        """
    def is_knot(self) -> bool:
        """
        Return ``True`` if ``self`` is a knot.

        Every knot is a link but the converse is not true.

        EXAMPLES::

            sage: B = BraidGroup(4)
            sage: L = Link(B([1, 3, 1, -3]))
            sage: L.is_knot()
            False
            sage: B = BraidGroup(8)
            sage: L = Link(B([1, 2, 3, 4, 5, 6]))
            sage: L.is_knot()
            True
        """
    def genus(self):
        """
        Return the genus of ``self``.

        EXAMPLES::

            sage: B = BraidGroup(4)
            sage: L = Link(B([-1, 3, 1, 3]))
            sage: L.genus()
            0
            sage: L = Link(B([1,3]))
            sage: L.genus()
            0
            sage: B = BraidGroup(8)
            sage: L = Link(B([-2, 4, 1, 6, 1, 4]))
            sage: L.genus()
            0
            sage: L = Link(B([1, 2, 1, 2]))
            sage: L.genus()
            1
        """
    def signature(self):
        """
        Return the signature of ``self``.

        This is defined as the signature of the symmetric matrix

        .. MATH::

             V + V^{t},

        where `V` is the :meth:`Seifert matrix <seifert_matrix>`.

        .. SEEALSO:: :meth:`omega_signature`, :meth:`seifert_matrix`

        EXAMPLES::

            sage: # needs sage.modules
            sage: B = BraidGroup(4)
            sage: L = Link(B([-1, 3, 1, 3]))
            sage: L.signature()
            -1
            sage: B = BraidGroup(8)
            sage: L = Link(B([-2, 4, 1, 6, 1, 4]))
            sage: L.signature()
            -2
            sage: L = Link(B([1, 2, 1, 2]))
            sage: L.signature()
            -2
        """
    def omega_signature(self, omega):
        """
        Compute the `\\omega`-signature of ``self``.

        INPUT:

        - `\\omega` -- a complex number of modulus 1; this is assumed to be
          coercible to ``QQbar``

        This is defined as the signature of the Hermitian matrix

        .. MATH::

             (1 - \\omega) V + (1 - \\omega^{-1}) V^{t},

        where `V` is the :meth:`Seifert matrix <seifert_matrix>`,
        as explained on page 122 of [Liv1993]_.

        According to [Con2018]_, this is also known as the
        Levine-Tristram signature, the equivariant signature or the
        Tristram-Levine signature.

        .. SEEALSO:: :meth:`signature`, :meth:`seifert_matrix`

        EXAMPLES::

            sage: # needs sage.modules sage.rings.number_field
            sage: B = BraidGroup(4)
            sage: K = Knot(B([1,1,1,2,-1,2,-3,2,-3]))
            sage: omega = QQbar.zeta(3)
            sage: K.omega_signature(omega)
            -2
        """
    def alexander_polynomial(self, var: str = 't'):
        '''
        Return the Alexander polynomial of ``self``.

        INPUT:

        - ``var`` -- (default: ``\'t\'``) the variable in the polynomial

        EXAMPLES:

        We begin by computing the Alexander polynomial for the
        figure-eight knot::

            sage: # needs sage.modules
            sage: B = BraidGroup(3)
            sage: L = Link(B([1, -2, 1, -2]))
            sage: L.alexander_polynomial()
            -t^-1 + 3 - t

        The "monster" unknot::

            sage: L = Link([[3,1,2,4],[8,9,1,7],[5,6,7,3],[4,18,6,5],
            ....:           [17,19,8,18],[9,10,11,14],[10,12,13,11],
            ....:           [12,19,15,13],[20,16,14,15],[16,20,17,2]])
            sage: L.alexander_polynomial()                                              # needs sage.modules
            1

        Some additional examples::

            sage: # needs sage.modules
            sage: B = BraidGroup(2)
            sage: L = Link(B([1]))
            sage: L.alexander_polynomial()
            1
            sage: L = Link(B.one())
            sage: L.alexander_polynomial()
            1
            sage: B = BraidGroup(3)
            sage: L = Link(B([1, 2, 1, 2]))
            sage: L.alexander_polynomial()
            t^-1 - 1 + t

        When the Seifert surface is disconnected, the Alexander
        polynomial is defined to be `0`::

            sage: # needs sage.modules
            sage: B = BraidGroup(4)
            sage: L = Link(B([1,3]))
            sage: L.alexander_polynomial()
            0

        TESTS::

            sage: # needs sage.modules
            sage: B = BraidGroup(4)
            sage: L = Link(B([-1, 3, 1, 3]))
            sage: L.alexander_polynomial()
            0
            sage: L = Link(B([1,3,1,1,3,3]))
            sage: L.alexander_polynomial()
            0
            sage: B = BraidGroup(8)
            sage: L = Link(B([-2, 4, 1, 6, 1, 4]))
            sage: L.alexander_polynomial()
            0

        .. SEEALSO:: :meth:`conway_polynomial`
        '''
    def conway_polynomial(self):
        """
        Return the Conway polynomial of ``self``.

        This is closely related to the Alexander polynomial.

        See :wikipedia:`Alexander_polynomial` for the definition.

        EXAMPLES::

            sage: # needs sage.modules
            sage: B = BraidGroup(3)
            sage: L = Link(B([1, -2, 1, -2]))
            sage: L.conway_polynomial()
            -t^2 + 1
            sage: Link([[1, 5, 2, 4], [3, 9, 4, 8], [5, 1, 6, 10],
            ....:       [7, 3, 8, 2], [9, 7, 10, 6]])
            Link with 1 component represented by 5 crossings
            sage: _.conway_polynomial()
            2*t^2 + 1
            sage: B = BraidGroup(4)
            sage: L = Link(B([1,3]))
            sage: L.conway_polynomial()
            0

        .. SEEALSO:: :meth:`alexander_polynomial`
        """
    def khovanov_polynomial(self, var1: str = 'q', var2: str = 't', torsion: str = 'T', ring=..., base_ring=None):
        """
        Return the Khovanov polynomial of ``self``.

        This is the Poincaré polynomial of the Khovanov homology.

        INPUT:

        - ``var1`` -- (default: ``'q'``) the first variable. Its exponents
          correspond to the height of Khovanov homology
        - ``var2`` -- (default: ``'t'``) the second variable. Its exponents
          correspond to the degree of Khovanov homology
        - ``torsion`` -- (default: ``'T'``) additional variable to indicate
          the torsion of the integral homology group corresponding to the
          monomial; monomials without it correspond to torsion free ``ring``
          modules; if it appears its exponents stands for the modulus of
          the torsion
        - ``ring`` -- (default: ``ZZ``) the ring of the homology. This will
          be transferred to :meth:`khovanov_homology`

        Here we follow the conventions used in
        `KnotInfo <https://knotinfo.math.indiana.edu/descriptions/khovanov_unreduced_integral_polynomial.html>`__

        OUTPUT:

        A two or three (for integral homology) variate Laurent polynomial over
        ``ZZ``, more precisely an instance of
        :class:`~sage.rings.polynomial.laurent_polynomial.LaurentPolynomial_mpair`.

        EXAMPLES::

            sage: K = Link([[[1, -2, 3, -1, 2, -3]],[-1, -1, -1]])
            sage: K.khovanov_polynomial()                                               # needs sage.modules
            q^-1 + q^-3 + q^-5*t^-2 + q^-7*t^-2*T^2 + q^-9*t^-3
            sage: K.khovanov_polynomial(ring=GF(2))                                     # needs sage.modules
            q^-1 + q^-3 + q^-5*t^-2 + q^-7*t^-2 + q^-7*t^-3 + q^-9*t^-3

        The figure eight knot::

            sage: L = Link([[1, 6, 2, 7], [5, 2, 6, 3], [3, 1, 4, 8], [7, 5, 8, 4]])
            sage: L.khovanov_polynomial(var1='p')                                       # needs sage.modules
            p^5*t^2 + p^3*t^2*T^2 + p*t + p + p^-1 + p^-1*t^-1
              + p^-3*t^-1*T^2 + p^-5*t^-2
            sage: L.khovanov_polynomial(var1='p', var2='s', ring=GF(4))                 # needs sage.modules sage.rings.finite_rings
            p^5*s^2 + p^3*s^2 + p^3*s + p*s + p + p^-1 + p^-1*s^-1
              + p^-3*s^-1 + p^-3*s^-2 + p^-5*s^-2

        The Hopf link::

            sage: B = BraidGroup(2)
            sage: b = B([1, 1])
            sage: K = Link(b)
            sage: K.khovanov_polynomial()                                               # needs sage.modules
            q^6*t^2 + q^4*t^2 + q^2 + 1

        .. SEEALSO:: :meth:`khovanov_homology`
        """
    def determinant(self):
        """
        Return the determinant of ``self``.

        EXAMPLES::

            sage: # needs sage.modules
            sage: B = BraidGroup(4)
            sage: L = Link(B([-1, 2, 1, 2]))
            sage: L.determinant()
            1
            sage: B = BraidGroup(8)
            sage: L = Link(B([2, 4, 2, 3, 1, 2]))
            sage: L.determinant()
            3
            sage: L = Link(B([1]*16 + [2,1,2,1,2,2,2,2,2,2,2,1,2,1,2,-1,2,-2]))
            sage: L.determinant()
            65
            sage: B = BraidGroup(3)
            sage: Link(B([1, 2, 1, 1, 2])).determinant()
            4

        TESTS::

            sage: # needs sage.modules
            sage: B = BraidGroup(3)
            sage: Link(B([1, 2, 1, -2, -1])).determinant()
            0

        REFERENCES:

        - Definition 6.6.3 in [Cro2004]_
        """
    def is_alternating(self) -> bool:
        """
        Return whether the given knot diagram is alternating.

        Alternating diagram implies every overcross is followed by an
        undercross or the vice-versa.

        We look at the Gauss code if the sign is alternating, ``True``
        is returned else the knot is not alternating ``False`` is returned.

        .. WARNING::

            This does not check if a knot admits an alternating diagram
            or not. Thus, this term is used differently than in some of
            the literature, such as in Hoste-Thistlethwaite table.

        .. NOTE::

            Links with more than one component are considered to not
            be alternating (knots) even when such a diagram exists.

        EXAMPLES::

            sage: B = BraidGroup(4)
            sage: L = Link(B([-1, -1, -1, -1]))
            sage: L.is_alternating()
            False
            sage: L = Link(B([1, -2, -1, 2]))
            sage: L.is_alternating()
            False
            sage: L = Link(B([-1, 3, 1, 3, 2]))
            sage: L.is_alternating()
            False
            sage: L = Link(B([1]*16 + [2,1,2,1,2,2,2,2,2,2,2,1,2,1,2,-1,2,-2]))
            sage: L.is_alternating()
            False
            sage: L = Link(B([-1,2,-1,2]))
            sage: L.is_alternating()
            True

        We give the `5_2` knot with an alternating diagram and a
        non-alternating diagram::

            sage: K5_2 = Link([[1, 4, 2, 5], [3, 8, 4, 9], [5, 10, 6, 1],
            ....:              [7, 2, 8, 3], [9, 6, 10, 7]])
            sage: K5_2.is_alternating()
            True

            sage: K5_2b = Link(K5_2.braid())
            sage: K5_2b.is_alternating()
            False

        TESTS:

        Check that :issue:`31001` is fixed::

            sage: L = Knot([])
            sage: L.is_alternating()
            True
        """
    def orientation(self):
        """
        Return the orientation of the crossings of the link diagram
        of ``self``.

        EXAMPLES::

            sage: L = Link([[1, 2, 5, 4], [3, 7, 6, 5], [4, 6, 9, 8], [7, 11, 10, 9],
            ....:           [8, 10, 13, 1], [11, 3, 2, 13]])
            sage: L.orientation()
            [-1, 1, -1, 1, -1, 1]
            sage: L = Link([[1, 6, 2, 7], [7, 2, 8, 3], [3, 10, 4, 11], [11, 4, 12, 5],
            ....:           [14, 6, 1, 5], [13, 8, 14, 9], [12, 10, 13, 9]])
            sage: L.orientation()
            [-1, -1, -1, -1, 1, -1, 1]
            sage: L = Link([[1, 3, 3, 2], [2, 5, 5, 4], [4, 7, 7, 1]])
            sage: L.orientation()
            [-1, -1, -1]
        """
    def seifert_circles(self):
        """
        Return the Seifert circles from the link diagram of ``self``.

        Seifert circles are the circles obtained by smoothing all crossings
        respecting the orientation of the segments.

        Each Seifert circle is represented as a list of the segments
        that form it.

        EXAMPLES::

            sage: L = Link([[[1, -2, 3, -4, 2, -1, 4, -3]], [1, 1, -1, -1]])
            sage: L.seifert_circles()
            [[1, 7, 5, 3], [2, 6], [4, 8]]
            sage: L = Link([[[-1, 2, 3, -4, 5, -6, 7, 8, -2, -5, 6, 1, -8, -3, 4, -7]],
            ....:           [-1, -1, -1, -1, 1, 1, -1, 1]])
            sage: L.seifert_circles()
            [[1, 13, 9, 3, 15, 5, 11, 7], [2, 10, 6, 12], [4, 16, 8, 14]]
            sage: L = Link([[[-1, 2, -3, 4, 5, 1, -2, 6, 7, 3, -4, -7, -6, -5]],
            ....:           [-1, -1, -1, -1, 1, -1, 1]])
            sage: L.seifert_circles()
            [[1, 7, 3, 11, 5], [2, 8, 14, 6], [4, 12, 10], [9, 13]]
            sage: L = Link([[1, 7, 2, 6], [7, 3, 8, 2], [3, 11, 4, 10], [11, 5, 12, 4],
            ....:           [14, 5, 1, 6], [13, 9, 14, 8], [12, 9, 13, 10]])
            sage: L.seifert_circles()
            [[1, 7, 3, 11, 5], [2, 8, 14, 6], [4, 12, 10], [9, 13]]
            sage: L = Link([[[-1, 2, -3, 5], [4, -2, 6, -5], [-4, 1, -6, 3]],
            ....:           [-1, 1, 1, 1, -1, -1]])
            sage: L.seifert_circles()
            [[1, 11, 8], [2, 7, 12, 4, 5, 10], [3, 9, 6]]

            sage: B = BraidGroup(2)
            sage: L = Link(B([1, 1, 1]))
            sage: L.seifert_circles()
            [[1, 3, 5], [2, 4, 6]]

        TESTS:

        Check that :issue:`25050` is solved::

            sage: A = Link([[[1, 2, -2, -1, -3, -4, 4, 3]], [1, 1, 1, 1]])
            sage: A.seifert_circles()
            [[3], [7], [1, 5], [2, 4], [6, 8]]
        """
    def regions(self):
        """
        Return the regions from the link diagram of ``self``.

        Regions are obtained always turning left at each crossing.

        Then the regions are represented as a list with the segments that form
        its boundary, with a sign depending on the orientation of the segment
        as part of the boundary.

        EXAMPLES::

            sage: L = Link([[[-1, +2, -3, 4, +5, +1, -2, +6, +7, 3, -4, -7, -6,-5]],
            ....:           [-1, -1, -1, -1, 1, -1, 1]])
            sage: L.regions()
            [[14, -5, 12, -9], [13, 9], [11, 5, 1, 7, 3], [10, -3, 8, -13],
             [6, -1], [4, -11], [2, -7], [-2, -6, -14, -8], [-4, -10, -12]]
            sage: L = Link([[[1, -2, 3, -4, 2, -1, 4, -3]],[1, 1, -1, -1]])
            sage: L.regions()
            [[8, 4], [7, -4, 1], [6, -1, -3], [5, 3, -8], [2, -5, -7], [-2, -6]]
            sage: L = Link([[[-1, +2, 3, -4, 5, -6, 7, 8, -2, -5, +6, +1, -8, -3, 4, -7]],
            ....:           [-1, -1, -1, -1, 1, 1, -1, 1]])
            sage: L.regions()
            [[16, 8, 14, 4], [15, -4], [13, -8, 1], [12, -1, -7], [11, 7, -16, 5],
             [10, -5, -15, -3], [9, 3, -14], [6, -11], [2, -9, -13], [-2, -12, -6, -10]]

            sage: B = BraidGroup(2)
            sage: L = Link(B([-1, -1, -1]))
            sage: L.regions()
            [[6, -5], [5, 1, 3], [4, -3], [2, -1], [-2, -6, -4]]
            sage: L = Link([[[1, -2, 3, -4], [-1, 5, -3, 2, -5, 4]],
            ....:           [-1, 1, 1, -1, -1]])
            sage: L.regions()
            [[10, -4, -7], [9, 7, -3], [8, 3], [6, -9, -2], [5, 2, -8, 4],
             [1, -5], [-1, -10, -6]]
            sage: L = Link([[1, 3, 3, 2], [2, 4, 4, 5], [5, 6, 6, 7], [7, 8, 8, 1]])
            sage: L.regions()
            [[-3], [-4], [-6], [-8], [7, 1, 2, 5], [-1, 8, -7, 6, -5, 4, -2, 3]]

        .. NOTE::

            The link diagram is assumed to have only one completely isolated
            component. This is because otherwise some regions would have
            disconnected boundary.

        TESTS::

            sage: B = BraidGroup(6)
            sage: L = Link(B([1, 3, 5]))
            sage: L.regions()
            Traceback (most recent call last):
            ...
            NotImplementedError: can only have one isolated component
        """
    def remove_loops(self):
        """
        Return an ambient isotopic link in which all loops are removed.

        EXAMPLES::

            sage: b = BraidGroup(4)((3, 2, -1, -1))
            sage: L = Link(b)
            sage: L.remove_loops()
            Link with 2 components represented by 2 crossings
            sage: K4 = Link([[1, 7, 2, 6], [3, 1, 4, 8], [5, 5, 6, 4], [7, 3, 8, 2]])
            sage: K3 = K4.remove_loops()
            sage: K3.pd_code()
            [[1, 7, 2, 4], [3, 1, 4, 8], [7, 3, 8, 2]]
            sage: U = Link([[1, 2, 2, 1]])
            sage: U.remove_loops()
            Link with 1 component represented by 0 crossings
        """
    @cached_method
    def mirror_image(self):
        """
        Return the mirror image of ``self``.

        EXAMPLES::

            sage: g = BraidGroup(2).gen(0)
            sage: K = Link(g^3)
            sage: K2 = K.mirror_image(); K2
            Link with 1 component represented by 3 crossings
            sage: K2.braid()
            s^-3

        .. PLOT::
            :width: 300 px

            g = BraidGroup(2).gen(0)
            K = Link(g**3)
            sphinx_plot(K.plot())

        .. PLOT::
            :width: 300 px

            g = BraidGroup(2).gen(0)
            K = Link(g**3)
            sphinx_plot(K.mirror_image().plot())

        ::

            sage: K = Knot([[[1, -2, 3, -1, 2, -3]], [1, 1, 1]])
            sage: K2 = K.mirror_image(); K2
            Knot represented by 3 crossings
            sage: K.pd_code()
            [[4, 2, 5, 1], [2, 6, 3, 5], [6, 4, 1, 3]]
            sage: K2.pd_code()
            [[4, 1, 5, 2], [2, 5, 3, 6], [6, 3, 1, 4]]

        .. PLOT::
            :width: 300 px

            K = Link([[[1,-2,3,-1,2,-3]],[1,1,1]])
            sphinx_plot(K.plot())

        .. PLOT::
            :width: 300 px

            K = Link([[[1,-2,3,-1,2,-3]],[1,1,1]])
            K2 = K.mirror_image()
            sphinx_plot(K2.plot())

        TESTS:

        check that :issue:`30997` is fixed::

            sage: L = Link([[6, 2, 7, 1], [5, 13, 6, 12], [8, 3, 9, 4],
            ....:           [2, 13, 3, 14], [14, 8, 15, 7], [11, 17, 12, 16],
            ....:           [9, 18, 10, 11], [17, 10, 18, 5], [4, 16, 1, 15]]) # L9n25{0}{0} from KnotInfo
            sage: Lmm = L.mirror_image().mirror_image()
            sage: L == Lmm
            True
        """
    def reverse(self):
        """
        Return the reverse of ``self``. This is the link obtained from ``self``
        by reverting the orientation on all components.

        EXAMPLES::

            sage: K3 = Knot([[5, 2, 4, 1], [3, 6, 2, 5], [1, 4, 6, 3]])
            sage: K3r = K3.reverse(); K3r.pd_code()
            [[4, 1, 5, 2], [2, 5, 3, 6], [6, 3, 1, 4]]
            sage: K3 == K3r
            True

        a non reversable knot::

            sage: K8_17 = Knot([[6, 1, 7, 2], [14, 7, 15, 8], [8, 4, 9, 3],
            ....:               [2, 14, 3, 13], [12, 6, 13, 5], [4, 10, 5, 9],
            ....:               [16, 11, 1, 12], [10, 15, 11, 16]])
            sage: K8_17r = K8_17.reverse()
            sage: b = K8_17.braid(); b
            s0^2*s1^-1*(s1^-1*s0)^2*s1^-1
            sage: br = K8_17r.braid(); br
            s0^-1*s1*s0^-2*s1^2*s0^-1*s1
            sage: b.is_conjugated(br)
            False
            sage: b == br.reverse()
            False
            sage: b.is_conjugated(br.reverse())
            True
            sage: K8_17b = Link(b)
            sage: K8_17br = K8_17b.reverse()
            sage: bbr = K8_17br.braid(); bbr
            (s1^-1*s0)^2*s1^-2*s0^2
            sage: br == bbr
            False
            sage: br.is_conjugated(bbr)
            True
        """
    def writhe(self):
        """
        Return the writhe of ``self``.

        EXAMPLES::

            sage: L = Link([[[1, -2, 3, -4, 2, -1, 4, -3]],[1, 1, -1, -1]])
            sage: L.writhe()
            0
            sage: L = Link([[[-1, 2, -3, 4, 5, 1, -2, 6, 7, 3, -4, -7, -6,-5]],
            ....:            [-1, -1, -1, -1, 1, -1, 1]])
            sage: L.writhe()
            -3
            sage: L = Link([[[-1, 2, 3, -4, 5, -6, 7, 8, -2, -5, 6, 1, -8, -3, 4, -7]],
            ....:            [-1, -1, -1, -1, 1, 1, -1, 1]])
            sage: L.writhe()
            -2
        """
    def jones_polynomial(self, variab=None, skein_normalization: bool = False, algorithm: str = 'jonesrep'):
        '''
        Return the Jones polynomial of ``self``.

        The normalization is so that the unknot has Jones polynomial `1`.
        If ``skein_normalization`` is ``True``, the variable of the result
        is replaced by a itself to the power of `4`, so that the result
        agrees with the conventions of [Lic1997]_ (which in particular differs
        slightly from the conventions used otherwise in this class), had
        one used the conventional Kauffman bracket variable notation directly.

        If ``variab`` is ``None`` return a polynomial in the variable `A`
        or `t`, depending on the value ``skein_normalization``. In
        particular, if ``skein_normalization`` is ``False``, return the
        result in terms of the variable `t`, also used in [Lic1997]_.

        ALGORITHM:

        The calculation goes through one of two possible algorithms,
        depending on the value of ``algorithm``. Possible values are
        ``\'jonesrep\'`` which uses the Jones representation of a braid
        representation of ``self`` to compute the polynomial of the
        trace closure of the braid, and ``statesum`` which recursively
        computes the Kauffman bracket of ``self``. Depending on how the
        link is given, there might be significant time gains in using
        one over the other. When the trace closure of the braid is
        ``self``, the algorithms give the same result.

        INPUT:

        - ``variab`` -- variable (default: ``None``); the variable in the
          resulting polynomial; if unspecified, use either a default variable
          in `\\ZZ[A,A^{-1}]` or the variable `t` in the symbolic ring

        - ``skein_normalization`` -- boolean (default: ``False``); determines
          the variable of the resulting polynomial

        - ``algorithm`` -- string (default: ``\'jonesrep\'``); algorithm to use
          and can be one of the following:

          * ``\'jonesrep\'`` -- use the Jones representation of the braid
            representation

          * ``\'statesum\'`` -- recursively computes the Kauffman bracket

        OUTPUT:

        If ``skein_normalization`` if ``False``, this returns an element
        in the symbolic ring as the Jones polynomial of the link might
        have fractional powers when the link is not a knot. Otherwise the
        result is a Laurent polynomial in ``variab``.

        EXAMPLES:

        The unknot::

            sage: B = BraidGroup(9)
            sage: b = B([1, 2, 3, 4, 5, 6, 7, 8])
            sage: Link(b).jones_polynomial()
            1

        The "monster" unknot::

            sage: L = Link([[3,1,2,4],[8,9,1,7],[5,6,7,3],[4,18,6,5],
            ....:           [17,19,8,18],[9,10,11,14],[10,12,13,11],
            ....:           [12,19,15,13],[20,16,14,15],[16,20,17,2]])
            sage: L.jones_polynomial()                                                  # needs sage.symbolic
            1

        The Ochiai unknot::

            sage: L = Link([[[1,-2,-3,-8,-12,13,-14,15,-7,-1,2,-4,10,11,-13,12,
            ....:             -11,-16,4,3,-5,6,-9,7,-15,14,16,-10,8,9,-6,5]],
            ....:           [-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,-1,-1,-1]])
            sage: L.jones_polynomial()          # long time                             # needs sage.symbolic
            1

        Two unlinked unknots::

            sage: B = BraidGroup(4)
            sage: b = B([1, 3])
            sage: Link(b).jones_polynomial()                                            # needs sage.symbolic
            -sqrt(t) - 1/sqrt(t)

        The Hopf link::

            sage: B = BraidGroup(2)
            sage: b = B([-1,-1])
            sage: Link(b).jones_polynomial()                                            # needs sage.symbolic
            -1/sqrt(t) - 1/t^(5/2)

        Different representations of the trefoil and one of its mirror::

            sage: B = BraidGroup(2)
            sage: b = B([-1, -1, -1])
            sage: Link(b).jones_polynomial(skein_normalization=True)
            -A^-16 + A^-12 + A^-4
            sage: Link(b).jones_polynomial()
            1/t + 1/t^3 - 1/t^4
            sage: B = BraidGroup(3)
            sage: b = B([-1, -2, -1, -2])
            sage: Link(b).jones_polynomial(skein_normalization=True)
            -A^-16 + A^-12 + A^-4
            sage: R.<x> = LaurentPolynomialRing(GF(2))
            sage: Link(b).jones_polynomial(skein_normalization=True, variab=x)
            x^-16 + x^-12 + x^-4
            sage: B = BraidGroup(3)
            sage: b = B([1, 2, 1, 2])
            sage: Link(b).jones_polynomial(skein_normalization=True)
            A^4 + A^12 - A^16

        `K11n42` (the mirror of the "Kinoshita-Terasaka" knot) and `K11n34`
        (the mirror of the "Conway" knot) in [KnotAtlas]_::

            sage: B = BraidGroup(4)
            sage: K11n42 = Link(B([1, -2, 3, -2, 3, -2, -2, -1, 2, -3, -3, 2, 2]))
            sage: K11n34 = Link(B([1, 1, 2, -3, 2, -3, 1, -2, -2, -3, -3]))
            sage: bool(K11n42.jones_polynomial() == K11n34.jones_polynomial())          # needs sage.symbolic
            True

        The two algorithms for computation give the same result when the
        trace closure of the braid representation is the link itself::

            sage: # needs sage.symbolic
            sage: L = Link([[[-1, 2, -3, 4, 5, 1, -2, 6, 7, 3, -4, -7, -6, -5]],
            ....:           [-1, -1, -1, -1, 1, -1, 1]])
            sage: jonesrep = L.jones_polynomial(algorithm=\'jonesrep\')
            sage: statesum = L.jones_polynomial(algorithm=\'statesum\')
            sage: bool(jonesrep == statesum)
            True

        When we have thrown away unknots so that the trace closure of the
        braid is not necessarily the link itself, this is only true up to a
        power of the Jones polynomial of the unknot::

            sage: B = BraidGroup(3)
            sage: b = B([1])
            sage: L = Link(b)
            sage: b.components_in_closure()
            2
            sage: L.number_of_components()
            1
            sage: b.jones_polynomial()                                                  # needs sage.symbolic
            -sqrt(t) - 1/sqrt(t)
            sage: L.jones_polynomial()                                                  # needs sage.symbolic
            1
            sage: L.jones_polynomial(algorithm=\'statesum\')                              # needs sage.symbolic
            1

        TESTS::

            sage: L = Link([])
            sage: L.jones_polynomial(algorithm=\'statesum\')                              # needs sage.symbolic
            1

            sage: L.jones_polynomial(algorithm=\'other\')
            Traceback (most recent call last):
            ...
            ValueError: bad value of algorithm

        Check that :issue:`31001` is fixed::

            sage: L.jones_polynomial()
            1
        '''
    @cached_method
    def homfly_polynomial(self, var1=None, var2=None, normalization: str = 'lm'):
        '''
        Return the HOMFLY polynomial of ``self``.

        The HOMFLY polynomial `P(K)` of a link `K` is a Laurent polynomial
        in two variables defined using skein relations and for the unknot
        `U`, we have `P(U) = 1`.

        INPUT:

        - ``var1`` -- (default: ``\'L\'``) the first variable. If ``normalization``
          is set to ``az`` resp. ``vz`` the default is ``a`` resp. ``v``
        - ``var2`` -- (default: ``\'M\'``) the second variable. If ``normalization``
          is set to ``az`` resp. ``vz`` the default is ``z``
        - ``normalization`` -- (default: ``lm``) the system of coordinates
          and can be one of the following:

          * ``\'lm\'`` -- corresponding to the Skein relation
            `L\\cdot P(K _+) + L^{-1}\\cdot P(K _-) + M\\cdot P(K _0) = 0`

          * ``\'az\'`` -- corresponding to the Skein relation
            `a\\cdot P(K _+) - a^{-1}\\cdot P(K _-) = z  \\cdot P(K _0)`

          * ``\'vz\'`` -- corresponding to the Skein relation
            `v^{-1}\\cdot P(K _+) - v\\cdot P(K _-) = z  \\cdot P(K _0)`

          where `P(K _+)`, `P(K _-)` and `P(K _0)` represent the HOMFLY
          polynomials of three links that vary only in one crossing;
          that is the positive, negative, or smoothed links respectively

        OUTPUT: a Laurent polynomial over the integers

        .. NOTE::

            Use the ``\'az\'`` normalization to agree with the data
            in [KnotAtlas]_

            Use the ``\'vz\'`` normalization to agree with the data
            `KnotInfo <http://www.indiana.edu/~knotinfo/>`__.

        EXAMPLES:

        We give some examples::

            sage: g = BraidGroup(2).gen(0)
            sage: K = Knot(g^5)
            sage: K.homfly_polynomial()                                                 # needs sage.libs.homfly
            L^-4*M^4 - 4*L^-4*M^2 + 3*L^-4 - L^-6*M^2 + 2*L^-6

        The Hopf link::

            sage: L = Link([[1,4,2,3],[4,1,3,2]])
            sage: L.homfly_polynomial(\'x\', \'y\')                                         # needs sage.libs.homfly
            -x^-1*y + x^-1*y^-1 + x^-3*y^-1

        Another version of the Hopf link where the orientation
        has been changed. Therefore we substitute `x \\mapsto L^{-1}`
        and `y \\mapsto M`::

            sage: L = Link([[1,3,2,4], [4,2,3,1]])
            sage: L.homfly_polynomial()                                                 # needs sage.libs.homfly
            L^3*M^-1 - L*M + L*M^-1
            sage: L = Link([[1,3,2,4], [4,2,3,1]])
            sage: L.homfly_polynomial(normalization=\'az\')                               # needs sage.libs.homfly
            a^3*z^-1 - a*z - a*z^-1

        The figure-eight knot::

            sage: L = Link([[2,5,4,1], [5,3,7,6], [6,9,1,4], [9,7,3,2]])
            sage: L.homfly_polynomial()                                                 # needs sage.libs.homfly
            -L^2 + M^2 - 1 - L^-2
            sage: L.homfly_polynomial(\'a\', \'z\', \'az\')                                   # needs sage.libs.homfly
            a^2 - z^2 - 1 + a^-2

        The "monster" unknot::

            sage: L = Link([[3,1,2,4], [8,9,1,7], [5,6,7,3], [4,18,6,5],
            ....:           [17,19,8,18], [9,10,11,14], [10,12,13,11],
            ....:           [12,19,15,13], [20,16,14,15], [16,20,17,2]])
            sage: L.homfly_polynomial()                                                 # needs sage.libs.homfly
            1

        Comparison with KnotInfo::

            sage: # needs sage.libs.homfly
            sage: KI =  K.get_knotinfo(mirror_version=False); KI
             <KnotInfo.K5_1: \'5_1\'>
            sage: K.homfly_polynomial(normalization=\'vz\') == KI.homfly_polynomial()
            True

        The knot `9_6`::

            sage: # needs sage.libs.homfly
            sage: B = BraidGroup(3)
            sage: K = Knot(B([-1,-1,-1,-1,-1,-1,-2,1,-2,-2]))
            sage: K.homfly_polynomial()
            L^10*M^4 - L^8*M^6 - 3*L^10*M^2 + 4*L^8*M^4 + L^6*M^6 + L^10
             - 3*L^8*M^2 - 5*L^6*M^4 - L^8 + 7*L^6*M^2 - 3*L^6
            sage: K.homfly_polynomial(\'a\', \'z\', normalization=\'az\')
            -a^10*z^4 + a^8*z^6 - 3*a^10*z^2 + 4*a^8*z^4 + a^6*z^6 - a^10
             + 3*a^8*z^2 + 5*a^6*z^4 - a^8 + 7*a^6*z^2 + 3*a^6

        TESTS:

        This works with isolated components::

            sage: # needs sage.libs.homfly
            sage: L = Link([[[1, -1], [2, -2]], [1, 1]])
            sage: L2 = Link([[1, 4, 2, 3], [2, 4, 1, 3]])
            sage: L2.homfly_polynomial()  # not tested (:issue:`39544`)
            -L*M^-1 - L^-1*M^-1
            sage: L.homfly_polynomial()
            -L*M^-1 - L^-1*M^-1
            sage: L.homfly_polynomial(normalization=\'az\')
            a*z^-1 - a^-1*z^-1
            sage: L2.homfly_polynomial(\'α\', \'ζ\', \'az\')
            α*ζ^-1 - α^-1*ζ^-1
            sage: L.homfly_polynomial(normalization=\'vz\')
            -v*z^-1 + v^-1*z^-1
            sage: L2.homfly_polynomial(\'ν\', \'ζ\', \'vz\')
            -ν*ζ^-1 + ν^-1*ζ^-1

        Check that :issue:`30346` is fixed::

            sage: L = Link([])
            sage: L.homfly_polynomial()                                                 # needs sage.libs.homfly
            1

        REFERENCES:

        - :wikipedia:`HOMFLY_polynomial`
        - http://mathworld.wolfram.com/HOMFLYPolynomial.html
        '''
    def links_gould_polynomial(self, varnames: str = 't0, t1'):
        """
        Return the Links-Gould polynomial of ``self``. See [MW2012]_, section 3
        and references given there. See also the docstring of
        :meth:`~sage.groups.braid.Braid.links_gould_polynomial`.

        INPUT:

        - ``varnames`` -- string (default: ``'t0, t1'``)

        OUTPUT: a Laurent polynomial in the given variable names

        EXAMPLES::

            sage: Hopf = Link([[1, 3, 2, 4], [4, 2, 3, 1]])
            sage: Hopf.links_gould_polynomial()
            -1 + t1^-1 + t0^-1 - t0^-1*t1^-1
        """
    def is_colorable(self, n=None) -> bool:
        """
        Return whether the link is ``n``-colorable.

        A link is ``n``-colorable if its arcs can be painted with
        ``n`` colours, labeled from ``0`` to ``n - 1``, in such a way
        that at any crossing, the average of the indices of the
        undercrossings equals twice the index of the overcrossing.

        INPUT:

        - ``n`` -- the number of colors to consider (if omitted the
          value of the determinant of ``self`` will be taken)

        EXAMPLES:

        We show that the trefoil knot is 3-colorable::

            sage: K = Link([[[1, -2, 3, -1, 2, -3]], [1, 1, 1]])
            sage: K.is_colorable(3)                                                     # needs sage.libs.pari sage.modules
            True

        But the figure eight knot is not::

            sage: K8 = Link([[[1, -2, 4, -3, 2, -1, 3, -4]], [1, 1, -1, -1]])
            sage: K8.is_colorable(3)                                                    # needs sage.libs.pari sage.modules
            False

        But it is colorable with respect to the value of its determinant::

            sage: K8.determinant()
            5
            sage: K8.is_colorable()
            True

        An examples with non prime determinant::

            sage: K = Knots().from_table(6, 1)
            sage: K.determinant()
            9
            sage: K.is_colorable()
            True

        REFERENCES:

        - :wikipedia:`Fox_n-coloring`

        - Chapter 3 of [Liv1993]_

        .. SEEALSO:: :meth:`colorings` and :meth:`coloring_maps`
        """
    def colorings(self, n=None):
        """
        Return the ``n``-colorings of ``self``.

        INPUT:

        - ``n`` -- the number of colors to consider (if omitted the value
          of the determinant of ``self`` will be taken). Note that there
          are no colorings if n is coprime to the determinant of ``self``

        OUTPUT:

        a list with the colorings. Each coloring is represented as
        a dictionary that maps a tuple of the edges forming each arc
        (as in the PD code) to the index of the corresponding color.

        EXAMPLES::

            sage: K = Link([[[1, -2, 3, -1, 2, -3]], [1, 1, 1]])
            sage: K.colorings(3)                                                        # needs sage.libs.pari sage.modules
            [{(1, 2): 0, (3, 4): 1, (5, 6): 2},
             {(1, 2): 0, (3, 4): 2, (5, 6): 1},
             {(1, 2): 1, (3, 4): 0, (5, 6): 2},
             {(1, 2): 1, (3, 4): 2, (5, 6): 0},
             {(1, 2): 2, (3, 4): 0, (5, 6): 1},
             {(1, 2): 2, (3, 4): 1, (5, 6): 0}]
            sage: K.pd_code()
            [[4, 2, 5, 1], [2, 6, 3, 5], [6, 4, 1, 3]]
            sage: K.arcs('pd')
            [[1, 2], [3, 4], [5, 6]]

        Note that ``n`` is not the number of different colors to be used. It
        can be looked upon the size of the color palette::

            sage: K = Knots().from_table(9, 15)
            sage: cols = K.colorings(13); len(cols)
            156
            sage: max(cols[0].values())
            12
            sage: max(cols[13].values())
            9

        REFERENCES:

        - :wikipedia:`Fox_n-coloring`

        - Chapter 3 of [Liv1993]_

        .. SEEALSO:: :meth:`is_colorable` and :meth:`coloring_maps`
        """
    def coloring_maps(self, n=None, finitely_presented: bool = False):
        """
        Return the `n`-coloring maps of ``self``.

        These are group homomorphisms from the fundamental group of
        ``self`` to the `n`-th dihedral group.

        INPUT:

        - ``n`` -- the number of colors to consider (if omitted the value
          of the determinant of ``self`` will be taken). Note that there
          are no coloring maps if n is coprime to the determinant of ``self``

        - ``finitely_presented`` -- boolean (default: ``False``); whether to
          choose the dihedral groups as finitely presented groups. If not set
          to ``True`` they are represented as permutation groups.

        OUTPUT:

        a list of group homomporhisms from the fundamental group of ``self``
        to the `n`-th dihedral group (represented according to the key
        argument ``finitely_presented``).

        EXAMPLES::

          sage: L5a1_1 = Link([[8, 2, 9, 1], [10, 7, 5, 8], [4, 10, 1, 9],
          ....:                [2, 5, 3, 6], [6, 3, 7, 4]])
          sage: L5a1_1.determinant()
          8
          sage: L5a1_1.coloring_maps(2)
          [Group morphism:
             From: Finitely presented group < x0, x1, x2, x3, x4 | x4*x1*x0^-1*x1^-1, x0*x4^-1*x3^-1*x4, x2*x0*x1^-1*x0^-1, x1*x3^-1*x2^-1*x3, x3*x2^-1*x4^-1*x2 >
             To:   Dihedral group of order 4 as a permutation group,
           Group morphism:
             From: Finitely presented group < x0, x1, x2, x3, x4 | x4*x1*x0^-1*x1^-1, x0*x4^-1*x3^-1*x4, x2*x0*x1^-1*x0^-1, x1*x3^-1*x2^-1*x3, x3*x2^-1*x4^-1*x2 >
             To:   Dihedral group of order 4 as a permutation group]
          sage: col_maps = L5a1_1.coloring_maps(4); len(col_maps)
          12
          sage: col_maps = L5a1_1.coloring_maps(5); len(col_maps)
          0
          sage: col_maps = L5a1_1.coloring_maps(12); len(col_maps)
          36
          sage: col_maps = L5a1_1.coloring_maps(); len(col_maps)
          56

        applying the map::

          sage: cm1 = col_maps[0]
          sage: gs = L5a1_1.fundamental_group().gens()
          sage: d = cm1(gs[0]); d
          (1,8)(2,7)(3,6)(4,5)
          sage: d.parent()
          Dihedral group of order 16 as a permutation group

        using the finitely presented dihedral group::

          sage: col_maps = L5a1_1.coloring_maps(2, finitely_presented=True)
          sage: d = col_maps[0](gs[1]); d
          b*a
          sage: d.parent()
          Finitely presented group < a, b | a^2, b^2, (a*b)^2 >

        REFERENCES:

        - :wikipedia:`Fox_n-coloring`

        - Chapter 3 of [Liv1993]_

        .. SEEALSO:: :meth:`is_colorable` and :meth:`colorings`
        """
    def plot(self, gap: float = 0.1, component_gap: float = 0.5, solver=None, color: str = 'blue', **kwargs):
        '''
        Plot ``self``.

        INPUT:

        - ``gap`` -- (default: 0.1) the size of the blank gap left for
          the crossings

        - ``component_gap`` -- (default: 0.5) the gap between isolated
          components

        - ``solver`` -- the linear solver to use, see
          :class:`~sage.numerical.mip.MixedIntegerLinearProgram`

        - ``color`` -- string (default: ``\'blue\'``); a color or a coloring (as
          returned by :meth:`colorings`

        The usual keywords for plots can be used here too.

        EXAMPLES:

        We construct the simplest version of the unknot::

            sage: L = Link([[2, 1, 1, 2]])
            sage: L.plot()                                                              # needs sage.plot
            Graphics object consisting of ... graphics primitives

        .. PLOT::
            :width: 300 px

            B = BraidGroup(2)
            L = Link([[2, 1, 1, 2]])
            sphinx_plot(L.plot())

        We construct a more interesting example of the unknot::

            sage: L = Link([[2, 1, 4, 5], [3, 5, 6, 7], [4, 1, 9, 6], [9, 2, 3, 7]])
            sage: L.plot()                                                              # needs sage.plot
            Graphics object consisting of ... graphics primitives

        .. PLOT::
            :width: 300 px

            L = Link([[2,1,4,5], [3,5,6,7], [4,1,9,6], [9,2,3,7]])
            sphinx_plot(L.plot())

        The "monster" unknot::

            sage: L = Link([[3,1,2,4], [8,9,1,7], [5,6,7,3], [4,18,6,5],
            ....:           [17,19,8,18], [9,10,11,14], [10,12,13,11],
            ....:           [12,19,15,13], [20,16,14,15], [16,20,17,2]])
            sage: L.plot()                                                              # needs sage.plot
            Graphics object consisting of ... graphics primitives

        .. PLOT::
            :width: 300 px

            L = Link([[3,1,2,4],[8,9,1,7],[5,6,7,3],[4,18,6,5],
                      [17,19,8,18],[9,10,11,14],[10,12,13,11],
                      [12,19,15,13],[20,16,14,15],[16,20,17,2]])
            sphinx_plot(L.plot())

        The Ochiai unknot::

            sage: L = Link([[[1,-2,-3,-8,-12,13,-14,15,-7,-1,2,-4,10,11,-13,12,
            ....:             -11,-16,4,3,-5,6,-9,7,-15,14,16,-10,8,9,-6,5]],
            ....:           [-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,-1,-1,-1]])
            sage: L.plot()                                                              # needs sage.plot
            Graphics object consisting of ... graphics primitives

        .. PLOT::
            :width: 300 px

            L = Link([[[1,-2,-3,-8,-12,13,-14,15,-7,-1,2,-4,10,11,-13,12,
                        -11,-16,4,3,-5,6,-9,7,-15,14,16,-10,8,9,-6,5]],
                      [-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,-1,-1,-1]])
            sphinx_plot(L.plot())

        One of the representations of the trefoil knot::

            sage: L = Link([[1, 5, 2, 4], [5, 3, 6, 2], [3, 1, 4, 6]])
            sage: L.plot()                                                              # needs sage.plot
            Graphics object consisting of 14 graphics primitives

        .. PLOT::
            :width: 300 px

            L = Link([[1, 5, 2, 4], [5, 3, 6, 2], [3, 1, 4, 6]])
            sphinx_plot(L.plot())

        The figure-eight knot::

            sage: L = Link([[2, 1, 4, 5], [5, 6, 7, 3], [6, 4, 1, 9], [9, 2, 3, 7]])
            sage: L.plot()                                                              # needs sage.plot
            Graphics object consisting of ... graphics primitives

        .. PLOT::
            :width: 300 px

            L = Link([[2,1,4,5], [5,6,7,3], [6,4,1,9], [9,2,3,7]])
            sphinx_plot(L.plot())

        The knot `K11n121` in [KnotAtlas]_::

            sage: L = Link([[4,2,5,1], [10,3,11,4], [5,16,6,17], [7,12,8,13],
            ....:           [18,9,19,10], [2,11,3,12], [13,20,14,21], [15,6,16,7],
            ....:           [22,18,1,17], [8,19,9,20], [21,14,22,15]])
            sage: L.plot()                                                              # needs sage.plot
            Graphics object consisting of ... graphics primitives

        .. PLOT::
            :width: 300 px

            L = Link([[4,2,5,1], [10,3,11,4], [5,16,6,17], [7,12,8,13],
                      [18,9,19,10], [2,11,3,12], [13,20,14,21], [15,6,16,7],
                      [22,18,1,17], [8,19,9,20], [21,14,22,15]])
            sphinx_plot(L.plot())

        One of the representations of the Hopf link::

            sage: L = Link([[1, 4, 2, 3], [4, 1, 3, 2]])
            sage: L.plot()                                                              # needs sage.plot
            Graphics object consisting of ... graphics primitives

        .. PLOT::
            :width: 300 px

            L = Link([[1, 4, 2, 3], [4, 1, 3, 2]])
            sphinx_plot(L.plot())

        Plotting links with multiple isolated components::

            sage: L = Link([[[-1, 2, -3, 1, -2, 3], [4, -5, 6, -4, 5, -6]],
            ....:            [1, 1, 1, 1, 1, 1]])
            sage: L.plot()                                                              # needs sage.plot
            Graphics object consisting of ... graphics primitives

        .. PLOT::
            :width: 300 px

            L = Link([[[-1,2,-3,1,-2,3], [4,-5,6,-4,5,-6]], [1,1,1,1,1,1]])
            sphinx_plot(L.plot())

        If a coloring is passed, the different arcs are plotted with
        the corresponding colors (see :meth:`colorings`)::

            sage: B = BraidGroup(4)
            sage: b = B([1,2,3,1,2,-1,-3,2,3])
            sage: L = Link(b)
            sage: L.plot(color=L.colorings()[0])                                        # needs sage.plot
            Graphics object consisting of ... graphics primitives

        .. PLOT::
            :width: 300 px

            B = BraidGroup(4)
            b = B([1, 2, 3, 1, 2, -1, -3, 2, 3])
            L = Link(b)
            sphinx_plot(L.plot(color=L.colorings()[0]))

        TESTS:

        Check that :issue:`20315` is fixed::

            sage: # needs sage.plot
            sage: L = Link([[2,1,4,5], [5,6,7,3], [6,4,1,9], [9,2,3,7]])
            sage: L.plot(solver=\'GLPK\')
            Graphics object consisting of ... graphics primitives
            sage: L.plot(solver=\'Coin\')    # optional - sage_numerical_backends_coin
            Graphics object consisting of ... graphics primitives
            sage: L.plot(solver=\'CPLEX\')   # optional - CPLEX
            Graphics object consisting of ... graphics primitives
            sage: L.plot(solver=\'Gurobi\')  # optional - Gurobi
            Graphics object consisting of ... graphics primitives
        '''
    def get_knotinfo(self, mirror_version: bool = True, unique: bool = True):
        """
        Identify this link as an item of the KnotInfo database (if possible).

        INPUT:

        - ``mirror_version`` -- boolean (default: ``True``); if set to ``False``
          the result of the method will be just the instance of :class:`~sage.knots.knotinfo.KnotInfoBase`
          (by default the result is a tuple of the instance and an enum, see
          explanation of the output below)

        - ``unique`` -- boolean (default: ``True``); this only affects the case
          where a unique identification is not possible. If set to ``False`` you
          can obtain a matching list (see explanation of the output below).

        OUTPUT:

        If ``self`` is a knot, then an element of the free monoid over prime
        knots constructed from the KnotInfo database is returned. More explicitly
        this is an element of :class:`~sage.knots.free_knotinfo_monoid.FreeKnotInfoMonoidElement`.
        Else a tuple ``(K, m)`` is returned where ``K`` is an instance of
        :class:`~sage.knots.knotinfo.KnotInfoBase` and ``m`` an instance of
        :class:`~sage.knots.knotinfo.SymmetryMutant` (for chiral links) specifying
        the symmetry mutant of ``K`` to which ``self`` is isotopic. The value of
        ``m`` is ``unknown`` if it cannot be determined uniquely and the keyword
        option ``unique=False`` is given.

        For proper links, if the orientation mutant cannot be uniquely determined,
        K will be a series of links gathering all links having the same unoriented
        name, that is an instance of :class:`~sage.knots.knotinfo.KnotInfoSeries`.

        If ``mirror_version`` is set to ``False`` then the result is just ``K``
        (that is: ``m`` is suppressed).

        If it is not possible to determine a unique result
        a :exc:`NotImplementedError`
        will be raised. To avoid this you can set ``unique`` to ``False``. You
        will get a list of matching candidates instead.

        .. NOTE::

            The identification of proper links may fail to be unique due to the
            following fact: In opposite to the database for knots, there are pairs
            of oriented mutants of an unoriented link which are isotopic to each
            other. For example ``L5a1_0`` and ``L5a1_1`` is such a pair.

            This is because all combinatorial possible oriented mutants are
            listed with individual names regardless whether they are pairwise
            non isotopic or not. In such a case the identification is not
            unique and therefore a series of the links will be returned which
            gathers all having the same unoriented name.

            To obtain the individual oriented links being isotopic to ``self``
            use the keyword ``unique`` (see the examples for ``L2a1_1`` and
            ``L5a1_0`` below).

        EXAMPLES::

            sage: # optional - database_knotinfo
            sage: L = Link([[4,1,5,2], [10,4,11,3], [5,17,6,16], [7,13,8,12],
            ....:           [18,10,19,9], [2,12,3,11], [13,21,14,20], [15,7,16,6],
            ....:           [22,17,1,18], [8,20,9,19], [21,15,22,14]])
            sage: L.get_knotinfo()
            KnotInfo['K11n_121m']
            sage: K = KnotInfo.K10_25
            sage: l = K.link()
            sage: l.get_knotinfo()
            KnotInfo['K10_25']
            sage: k11  = KnotInfo.K11n_82.link()
            sage: k11m = k11.mirror_image()
            sage: k11mr = k11m.reverse()
            sage: k11mr.get_knotinfo()
            KnotInfo['K11n_82m']
            sage: k11r = k11.reverse()
            sage: k11r.get_knotinfo()
            KnotInfo['K11n_82']
            sage: k11rm = k11r.mirror_image()
            sage: k11rm.get_knotinfo()
            KnotInfo['K11n_82m']

        Knots with more than 13 and multi-component links having more than 11
        crossings cannot be identified. In addition non prime multi-component
        links or even links whose HOMFLY-PT polynomial is not irreducible cannot
        be identified::

            sage: b, = BraidGroup(2).gens()
            sage: Link(b**13).get_knotinfo()    # optional - database_knotinfo
            KnotInfo['K13a_4878']
            sage: Link(b**14).get_knotinfo()
            Traceback (most recent call last):
            ...
            NotImplementedError: this link having more than 11 crossings cannot be determined

            sage: Link([[1, 4, 2, 5], [3, 8, 4, 1], [5, 2, 6, 3],
            ....:       [6, 10, 7, 9], [10, 8, 9, 7]])
            Link with 2 components represented by 5 crossings
            sage: _.get_knotinfo()                                                      # needs sage.libs.homfly
            Traceback (most recent call last):
            ...
            NotImplementedError: this (possibly non prime) link cannot be determined

        Lets identify the monster unknot::

            sage: L = Link([[3,1,2,4], [8,9,1,7], [5,6,7,3], [4,18,6,5],
            ....:           [17,19,8,18], [9,10,11,14], [10,12,13,11],
            ....:           [12,19,15,13], [20,16,14,15], [16,20,17,2]])
            sage: L.get_knotinfo()
            KnotInfo['K0_1']

        Usage of option ``mirror_version``::

            sage: L.get_knotinfo(mirror_version=False) == KnotInfo.K0_1
            True

        Usage of option ``unique``::

            sage: # optional - database_knotinfo
            sage: l = K.link(K.items.gauss_notation)
            sage: l.get_knotinfo()
            Traceback (most recent call last):
            ...
            NotImplementedError: this link cannot be uniquely determined
            use keyword argument `unique` to obtain more details
            sage: l.get_knotinfo(unique=False)
            [KnotInfo['K10_25'], KnotInfo['K10_56']]
            sage: t = (1, -2, 1, 1, -2, 1, -2, -2)
            sage: l8 = Link(BraidGroup(3)(t))
            sage: l8.get_knotinfo()
            Traceback (most recent call last):
            ...
            NotImplementedError: this link cannot be uniquely determined
            use keyword argument `unique` to obtain more details
            sage: l8.get_knotinfo(unique=False)
            [(<KnotInfo.L8a19_0_0: 'L8a19{0,0}'>, <SymmetryMutant.itself: 's'>),
             (<KnotInfo.L8a19_1_1: 'L8a19{1,1}'>, <SymmetryMutant.itself: 's'>)]
            sage: t = (2, -3, -3, -2, 3, 3, -2, 3, 1, -2, -2, 1)
            sage: l12 = Link(BraidGroup(5)(t))
            sage: l12.get_knotinfo()
            Traceback (most recent call last):
            ...
            NotImplementedError: this link having more than 11 crossings
            cannot be uniquely determined
            use keyword argument `unique` to obtain more details
            sage: l12.get_knotinfo(unique=False)
            [(<KnotInfo.L10n36_0: 'L10n36{0}'>, <SymmetryMutant.unknown: '?'>),
             (<KnotInfo.L10n36_1: 'L10n36{1}'>, <SymmetryMutant.unknown: '?'>),
             (<KnotInfo.L10n59_0: 'L10n59{0}'>, <SymmetryMutant.itself: 's'>),
             (<KnotInfo.L10n59_1: 'L10n59{1}'>, <SymmetryMutant.itself: 's'>)]

        Furthermore, if the result is a complete  series of oriented links having
        the same unoriented name (according to the note above) the option can be
        used to achieve more detailed information::

            sage: L2a1 = Link(b**2)
            sage: L2a1.get_knotinfo()
            (Series of links L2a1, <SymmetryMutant.mixed: 'x'>)
            sage: L2a1.get_knotinfo(unique=False)
            [(<KnotInfo.L2a1_0: 'L2a1{0}'>, <SymmetryMutant.mirror_image: 'm'>),
             (<KnotInfo.L2a1_1: 'L2a1{1}'>, <SymmetryMutant.itself: 's'>)]

            sage: KnotInfo.L5a1_0.inject()
            Defining L5a1_0
            sage: l5 = Link(L5a1_0.braid())
            sage: l5.get_knotinfo()
            (Series of links L5a1, <SymmetryMutant.itself: 's'>)
            sage: _[0].inject()
            Defining L5a1
            sage: list(L5a1)
            [<KnotInfo.L5a1_0: 'L5a1{0}'>, <KnotInfo.L5a1_1: 'L5a1{1}'>]
            sage: l5.get_knotinfo(unique=False)
            [(<KnotInfo.L5a1_0: 'L5a1{0}'>, <SymmetryMutant.itself: 's'>),
             (<KnotInfo.L5a1_1: 'L5a1{1}'>, <SymmetryMutant.itself: 's'>)]

        Clarifying the series around the Perko pair (:wikipedia:`Perko_pair`)::

            sage: for i in range(160, 166):           # optional - database_knotinfo
            ....:     K = Knots().from_table(10, i)
            ....:     print('%s_%s' %(10, i), '--->', K.get_knotinfo())
            10_160 ---> KnotInfo['K10_160']
            10_161 ---> KnotInfo['K10_161m']
            10_162 ---> KnotInfo['K10_162']
            10_163 ---> KnotInfo['K10_163']
            10_164 ---> KnotInfo['K10_164']
            10_165 ---> KnotInfo['K10_165m']

        Clarifying ther Perko series against `SnapPy
        <https://snappy.math.uic.edu/index.html>`__::

            sage: import snappy                    # optional - snappy
            ...

            sage: # optional - database_knotinfo snappy
            sage: from sage.knots.knotinfo import KnotInfoSeries
            sage: KnotInfoSeries(10, True, True)
            Series of knots K10
            sage: _.inject()
            Defining K10
            sage: for i in range(160, 166):
            ....:     K = K10(i)
            ....:     k = K.link(K.items.name, snappy=True)
            ....:     print(k, '--->', k.sage_link().get_knotinfo())
            <Link 10_160: 1 comp; 10 cross> ---> KnotInfo['K10_160']
            <Link 10_161: 1 comp; 10 cross> ---> KnotInfo['K10_161m']
            <Link 10_162: 1 comp; 10 cross> ---> KnotInfo['K10_161']
            <Link 10_163: 1 comp; 10 cross> ---> KnotInfo['K10_162']
            <Link 10_164: 1 comp; 10 cross> ---> KnotInfo['K10_163']
            <Link 10_165: 1 comp; 10 cross> ---> KnotInfo['K10_164']
            sage: snappy.Link('10_166')
            <Link 10_166: 1 comp; 10 cross>
            sage: _.sage_link().get_knotinfo()
            KnotInfo['K10_165m']

        Another pair of confusion (see the corresponding `Warning
        <http://katlas.math.toronto.edu/wiki/10_86>`__)::

            sage: # optional - database_knotinfo snappy
            sage: Ks10_86 = snappy.Link('10_86')
            sage: Ks10_83 = snappy.Link('10_83')
            sage: Ks10_86.sage_link().get_knotinfo(unique=False)
            [KnotInfo['K10_83c'], KnotInfo['K10_83m']]
            sage: Ks10_83.sage_link().get_knotinfo(unique=False)
            [KnotInfo['K10_86'], KnotInfo['K10_86r']]

        Non prime knots can be detected, as well::

            sage: b = BraidGroup(4)((1, 2, 2, 2, -1, 2, 2, 2, -3, -3, -3))
            sage: Kb = Knot(b)
            sage: Kb.get_knotinfo()
            KnotInfo['K3_1']^2*KnotInfo['K3_1m']

            sage: K = Link([[4, 2, 5, 1], [8, 6, 9, 5], [6, 3, 7, 4], [2, 7, 3, 8],
            ....:  [10, 15, 11, 16], [12, 21, 13, 22], [14, 11, 15, 12], [16, 9, 17, 10],
            ....:  [18, 25, 19, 26], [20, 23, 21, 24], [22, 13, 23, 14], [24, 19, 25, 20],
            ....:  [26, 17, 1, 18]])
            sage: K.get_knotinfo()    # optional - database_knotinfo, long time
            KnotInfo['K4_1']*KnotInfo['K9_2m']

        TESTS::

            sage: # optional - database_knotinfo
            sage: L = KnotInfo.L10a171_1_1_0
            sage: l = L.link(L.items.braid_notation)
            sage: l.get_knotinfo(unique=False)
            [(<KnotInfo.L10a171_0_1_0: 'L10a171{0,1,0}'>, <SymmetryMutant.unknown: '?'>),
             (<KnotInfo.L10a171_1_0_1: 'L10a171{1,0,1}'>, <SymmetryMutant.unknown: '?'>),
             (<KnotInfo.L10a171_1_1_0: 'L10a171{1,1,0}'>, <SymmetryMutant.unknown: '?'>),
             (<KnotInfo.L10a171_1_1_1: 'L10a171{1,1,1}'>, <SymmetryMutant.unknown: '?'>)]
            sage: KnotInfo.L10a151_0_0.link().get_knotinfo()
            Traceback (most recent call last):
            ...
            NotImplementedError: this link cannot be uniquely determined (unknown chirality)
            use keyword argument `unique` to obtain more details
            sage: KnotInfo.L10a151_0_0.link().get_knotinfo(unique=False)
            [(<KnotInfo.L10a151_0_0: 'L10a151{0,0}'>, <SymmetryMutant.unknown: '?'>),
             (<KnotInfo.L10a151_0_1: 'L10a151{0,1}'>, <SymmetryMutant.unknown: '?'>),
             (<KnotInfo.L10a151_1_0: 'L10a151{1,0}'>, <SymmetryMutant.unknown: '?'>),
             (<KnotInfo.L10a151_1_1: 'L10a151{1,1}'>, <SymmetryMutant.unknown: '?'>)]

            sage: L = KnotInfo.L6a2_0
            sage: L1 = L.link()
            sage: L2 = L.link(L.items.braid_notation)
            sage: L1.get_knotinfo() == L2.get_knotinfo()
            True
        """
    def is_isotopic(self, other) -> bool:
        """
        Check whether ``self`` is isotopic to ``other``.

        INPUT:

        - ``other`` -- another instance of :class:`Link`

        EXAMPLES::

            sage: l1 = Link([[2, 9, 3, 10], [4, 13, 5, 14], [6, 11, 7, 12],
            ....:            [8, 1, 9, 2], [10, 7, 11, 8], [12, 5, 13, 6],
            ....:            [14, 3, 1, 4]])
            sage: l2 = Link([[1, 8, 2, 9], [9, 2, 10, 3], [3, 14, 4, 1],
            ....:            [13, 4, 14, 5], [5, 12, 6, 13], [11, 6, 12, 7],
            ....:            [7, 10, 8, 11]])
            sage: l1.is_isotopic(l2)
            True

            sage: l3 = l2.mirror_image()
            sage: l1.is_isotopic(l3)
            False

            sage: # optional - database_knotinfo
            sage: L = KnotInfo.L7a7_0_0
            sage: L.series(oriented=True).inject()
            Defining L7a7
            sage: L == L7a7(0)
            True
            sage: l = L.link()
            sage: l.is_isotopic(L7a7(1).link())
            Traceback (most recent call last):
            ...
            NotImplementedError: comparison not possible!
            sage: l.is_isotopic(L7a7(2).link())
            True
            sage: l.is_isotopic(L7a7(3).link())
            False

        Using verbosity::

            sage: set_verbose(1)
            sage: l1.is_isotopic(l2)
            verbose 1 (... link.py, is_isotopic) identified by KnotInfo (KnotInfo.K7_2, SymmetryMutant.mirror_image)
            True
            sage: l1.is_isotopic(l3)
            verbose 1 (... link.py, is_isotopic) different Homfly-PT polynomials
            False
            sage: set_verbose(0)

        TESTS:

        Check that :issue:`37668` is fixed::

            sage: L = KnotInfo.L6a2_0
            sage: L1 = L.link()
            sage: L2 = L.link(L.items.braid_notation)
            sage: set_verbose(1)
            sage: L1.is_isotopic(L2)
            verbose 1 (... link.py, is_isotopic) identified by KnotInfo uniquely (KnotInfo.L6a2_0, SymmetryMutant.itself)
            True
            sage: KnotInfo.K0_1.link().is_isotopic(KnotInfo.L2a1_0.link())
            verbose 1 (... link.py, is_isotopic) different number of components
            False

            sage: # optional - database_knotinfo
            sage: K = KnotInfo.K10_67
            sage: K1 = K.link()
            sage: K1r = K.link().reverse()
            sage: K1.is_isotopic(K1r)
            verbose 1 (... link.py, is_isotopic) unidentified by KnotInfo ([<KnotInfo.K10_67: '10_67'>], SymmetryMutant.itself != [<KnotInfo.K10_67: '10_67'>], SymmetryMutant.reverse)
            False
            sage: KnotInfo.K10_25.link().is_isotopic(KnotInfo.K10_56.link())
            verbose 1 (... link.py, is_isotopic) unidentified by KnotInfo ([<KnotInfo.K10_25: '10_25'>] != [<KnotInfo.K10_56: '10_56'>], SymmetryMutant.itself)
            False
            sage: KnotInfo.L8n2_0.link().is_isotopic(KnotInfo.L8n2_1.link())
            verbose 1 (... link.py, is_isotopic) identified by KnotInfoSeries ([<KnotInfo.L8n2_0: 'L8n2{0}'>, <KnotInfo.L8n2_1: 'L8n2{1}'>], SymmetryMutant.reverse)
            True
            sage: set_verbose(0)
        """
