from sage.graphs.graph import Graph as Graph

def dowker_to_gauss(code):
    """
    Convert from Dowker-Thistlethwaite code to signed Gauss code.

    EXAMPLES::

        sage: from sage.knots.gauss_code import dowker_to_gauss
        sage: dowker_to_gauss([6,-12,2,8,-4,-10])
        [-3, 1, 6, -2, -1, 3, -4, 4, 2, -5, 5, -6]
        sage: dowker_to_gauss([-4,-6,-2])
        [2, -1, 3, -2, 1, -3]

    TESTS::

        sage: dowker_to_gauss([])
        []
    """
def recover_orientations(gauss):
    """
    Create diagrammatic information from signed Gauss code.

    This method is an auxiliary method, used for two different
    goals. The first goal is to create a knot from the signed Gauss
    code. This requires choosing at every crossing a local
    orientation, in a compatible way. The second goal is to picture
    the knot diagram using unicode. This goes through the creation of
    a noncrossing matching diagram.

    INPUT:

    - signed Gauss code

    OUTPUT:

    - word, a permutation of the (unsigned) Gauss code
    - list of positive (upwards) couplings in this word
    - list of negative (downwards) couplings in this word
    - list of signs, local orientations at each crossing

    ALGORITHM:

    The algorithm comes from Section 3 of [Kauf1999]_.

    EXAMPLES::

        sage: from sage.knots.gauss_code import recover_orientations
        sage: G = [4,1,5,2,1,3,6,4,2,5,3,6]
        sage: recover_orientations(G)
        ([4, 2, 1, 4, 6, 3, 1, 5, 2, 5, 3, 6],
         [(1, 8), (2, 6)],
         [(0, 3), (4, 11), (5, 10), (7, 9)],
         [1, -1, 1, 1, -1, 1])

        sage: G = [1,2,3,1,2,3]
        sage: recover_orientations(G)
        ([1, 3, 2, 1, 2, 3], [(0, 3)], [(1, 5), (2, 4)], [1, 1, 1])

        sage: G = [1, 2, 4, 5, 8, 1, 3, 4, 6, 7, 2, 3, 5, 6, 7, 8]
        sage: recover_orientations(G)
        ([1, 8, 7, 6, 5, 4, 6, 7, 2, 4, 3, 2, 1, 3, 5, 8],
         [(0, 12), (2, 7), (3, 6), (8, 11)],
         [(1, 15), (4, 14), (5, 9), (10, 13)],
         [1, -1, 1, -1, 1, -1, -1, 1])

    TESTS::

        sage: recover_orientations([])
        ([], [], [], [])
    """
def rectangular_diagram(gauss):
    """
    Return a rectangular diagram and crossing coordinates.

    INPUT:

    - signed Gauss code

    OUTPUT:

    - graph whose vertices are the corners of the knot diagram

    - positions of the horizontal and vertical crossings

    EXAMPLES::

        sage: from sage.knots.gauss_code import rectangular_diagram
        sage: G = [4,1,5,2,1,3,6,4,2,5,3,6]
        sage: rectangular_diagram(G)
        (Graph on 18 vertices, ([(1, 3), (3, 7), (4, 6), (6, 2)],
         [(4, 3), (6, 5)]))

        sage: G = [1,2,3,1,2,3]
        sage: rectangular_diagram(G)
        (Graph on 10 vertices, ([(1, 3), (2, 2)], [(2, 1)]))

    TESTS::

        sage: rectangular_diagram([])
        (Graph on 4 vertices, ([], []))
    """
