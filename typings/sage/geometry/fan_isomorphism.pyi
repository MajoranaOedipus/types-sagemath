from _typeshed import Incomplete
from collections.abc import Generator
from sage.geometry.cone import Cone as Cone
from sage.matrix.constructor import column_matrix as column_matrix, matrix as matrix
from sage.rings.integer_ring import ZZ as ZZ

class FanNotIsomorphicError(Exception):
    """
    Exception to return if there is no fan isomorphism
    """

def fan_isomorphic_necessary_conditions(fan1, fan2):
    """
    Check necessary (but not sufficient) conditions for the fans to be isomorphic.

    INPUT:

    - ``fan1``, ``fan2`` -- two fans

    OUTPUT: boolean; ``False`` if the two fans cannot be isomorphic. ``True``
    if the two fans may be isomorphic.

    EXAMPLES::

        sage: fan1 = toric_varieties.P2().fan()                                         # needs palp sage.graphs
        sage: fan2 = toric_varieties.dP8().fan()                                        # needs palp sage.graphs
        sage: from sage.geometry.fan_isomorphism import fan_isomorphic_necessary_conditions
        sage: fan_isomorphic_necessary_conditions(fan1, fan2)                           # needs palp sage.graphs
        False
    """
def fan_isomorphism_generator(fan1, fan2) -> Generator[Incomplete]:
    """
    Iterate over the isomorphisms from ``fan1`` to ``fan2``.

    ALGORITHM:

    The :meth:`sage.geometry.fan.Fan.vertex_graph` of the two fans is
    compared. For each graph isomorphism, we attempt to lift it to an
    actual isomorphism of fans.

    INPUT:

    - ``fan1``, ``fan2`` -- two fans

    OUTPUT:

    Yields the fan isomorphisms as matrices acting from the right on
    rays.

    EXAMPLES::

        sage: fan = toric_varieties.P2().fan()                                          # needs palp sage.graphs
        sage: from sage.geometry.fan_isomorphism import fan_isomorphism_generator
        sage: sorted(fan_isomorphism_generator(fan, fan))                               # needs palp sage.graphs
        [
        [-1 -1]  [-1 -1]  [ 0  1]  [0 1]  [ 1  0]  [1 0]
        [ 0  1], [ 1  0], [-1 -1], [1 0], [-1 -1], [0 1]
        ]
        sage: m1 = matrix([(1, 0), (0, -5), (-3, 4)])
        sage: m2 = matrix([(3, 0), (1, 0), (-2, 1)])
        sage: m1.elementary_divisors() == m2.elementary_divisors() == [1,1,0]
        True
        sage: fan1 = Fan([Cone([m1*vector([23, 14]), m1*vector([   3,100])]),
        ....:             Cone([m1*vector([-1,-14]), m1*vector([-100, -5])])])
        sage: fan2 = Fan([Cone([m2*vector([23, 14]), m2*vector([   3,100])]),
        ....:             Cone([m2*vector([-1,-14]), m2*vector([-100, -5])])])
        sage: sorted(fan_isomorphism_generator(fan1, fan2))                             # needs sage.graphs
        [
        [-12  1 -5]
        [ -4  0 -1]
        [ -5  0 -1]
        ]

        sage: m0 = identity_matrix(ZZ, 2)
        sage: m1 = matrix([(1, 0), (0, -5), (-3, 4)])
        sage: m2 = matrix([(3, 0), (1, 0), (-2, 1)])
        sage: m1.elementary_divisors() == m2.elementary_divisors() == [1,1,0]
        True
        sage: fan0 = Fan([Cone([m0*vector([1,0]), m0*vector([1,1])]),
        ....:             Cone([m0*vector([1,1]), m0*vector([0,1])])])
        sage: fan1 = Fan([Cone([m1*vector([1,0]), m1*vector([1,1])]),
        ....:             Cone([m1*vector([1,1]), m1*vector([0,1])])])
        sage: fan2 = Fan([Cone([m2*vector([1,0]), m2*vector([1,1])]),
        ....:             Cone([m2*vector([1,1]), m2*vector([0,1])])])
        sage: sorted(fan_isomorphism_generator(fan0, fan0))                             # needs sage.graphs
        [
        [0 1]  [1 0]
        [1 0], [0 1]
        ]
        sage: sorted(fan_isomorphism_generator(fan1, fan1))                             # needs sage.graphs
        [
        [ -3 -20  28]  [1 0 0]
        [ -1  -4   7]  [0 1 0]
        [ -1  -5   8], [0 0 1]
        ]
        sage: sorted(fan_isomorphism_generator(fan1, fan2))                             # needs sage.graphs
        [
        [-24  -3   7]  [-12   1  -5]
        [ -7  -1   2]  [ -4   0  -1]
        [ -8  -1   2], [ -5   0  -1]
        ]
        sage: sorted(fan_isomorphism_generator(fan2, fan1))                             # needs sage.graphs
        [
        [  0   1  -1]  [ 0  1 -1]
        [  1 -13   8]  [ 2 -8  1]
        [  0  -5   4], [ 1  0 -3]
        ]
    """
def find_isomorphism(fan1, fan2, check: bool = False):
    """
    Find an isomorphism of the two fans.

    INPUT:

    - ``fan1``, ``fan2`` -- two fans

    - ``check`` -- boolean (default: ``False``); passed to the fan
      morphism constructor, see
      :func:`~sage.geometry.fan_morphism.FanMorphism`

    OUTPUT:

    A fan isomorphism. If the fans are not isomorphic, a
    :exc:`FanNotIsomorphicError` is raised.

    EXAMPLES::

        sage: rays = ((1, 1), (0, 1), (-1, -1), (3, 1))
        sage: cones = [(0,1), (1,2), (2,3), (3,0)]
        sage: fan1 = Fan(cones, rays)

        sage: m = matrix([[-2,3],[1,-1]])
        sage: m.det() == -1
        True
        sage: fan2 = Fan(cones, [vector(r)*m for r in rays])

        sage: from sage.geometry.fan_isomorphism import find_isomorphism
        sage: find_isomorphism(fan1, fan2, check=True)                                  # needs sage.graphs
        Fan morphism defined by the matrix
        [-2  3]
        [ 1 -1]
        Domain fan: Rational polyhedral fan in 2-d lattice N
        Codomain fan: Rational polyhedral fan in 2-d lattice N

        sage: find_isomorphism(fan1, toric_varieties.P2().fan())                        # needs palp sage.graphs
        Traceback (most recent call last):
        ...
        FanNotIsomorphicError

        sage: fan1 = Fan(cones=[[1,3,4,5],[0,1,2,3],[2,3,4],[0,1,5]],
        ....:            rays=[(-1,-1,0),(-1,-1,3),(-1,1,-1),(-1,3,-1),(0,2,-1),(1,-1,1)])
        sage: fan2 = Fan(cones=[[0,2,3,5],[0,1,4,5],[0,1,2],[3,4,5]],
        ....:            rays=[(-1,-1,-1),(-1,-1,0),(-1,1,-1),(0,2,-1),(1,-1,1),(3,-1,-1)])
        sage: fan1.is_isomorphic(fan2)                                                  # needs sage.graphs
        True
    """
def fan_2d_cyclically_ordered_rays(fan):
    """
    Return the rays of a 2-dimensional ``fan`` in cyclic order.

    INPUT:

    - ``fan`` -- a 2-dimensional fan

    OUTPUT:

    A :class:`~sage.geometry.point_collection.PointCollection`
    containing the rays in one particular cyclic order.

    EXAMPLES::

        sage: rays = ((1, 1), (-1, -1), (-1, 1), (1, -1))
        sage: cones = [(0,2), (2,1), (1,3), (3,0)]
        sage: fan = Fan(cones, rays)
        sage: fan.rays()
        N( 1,  1),
        N(-1, -1),
        N(-1,  1),
        N( 1, -1)
        in 2-d lattice N
        sage: from sage.geometry.fan_isomorphism import fan_2d_cyclically_ordered_rays
        sage: fan_2d_cyclically_ordered_rays(fan)
        N(-1, -1),
        N(-1,  1),
        N( 1,  1),
        N( 1, -1)
        in 2-d lattice N

    TESTS::

        sage: fan = Fan(cones=[], rays=[], lattice=ZZ^2)
        sage: from sage.geometry.fan_isomorphism import fan_2d_cyclically_ordered_rays
        sage: fan_2d_cyclically_ordered_rays(fan)
        Empty collection
        in Ambient free module of rank 2 over the principal ideal domain Integer Ring
    """
def fan_2d_echelon_forms(fan):
    """
    Return echelon forms of all cyclically ordered ray matrices.

    Note that the echelon form of the ordered ray matrices are unique
    up to different cyclic orderings.

    INPUT:

    - ``fan`` -- a fan

    OUTPUT:

    A set of matrices. The set of all echelon forms for all different
    cyclic orderings.

    EXAMPLES::

        sage: fan = toric_varieties.P2().fan()                                          # needs palp sage.graphs
        sage: from sage.geometry.fan_isomorphism import fan_2d_echelon_forms
        sage: fan_2d_echelon_forms(fan)                                                 # needs palp sage.graphs
        frozenset({[ 1  0 -1]
                   [ 0  1 -1]})

        sage: fan = toric_varieties.dP7().fan()                                         # needs palp sage.graphs
        sage: sorted(fan_2d_echelon_forms(fan))                                         # needs palp sage.graphs
        [
        [ 1  0 -1 -1  0]  [ 1  0 -1 -1  0]  [ 1  0 -1 -1  1]  [ 1  0 -1  0  1]
        [ 0  1  0 -1 -1], [ 0  1  1  0 -1], [ 0  1  1  0 -1], [ 0  1  0 -1 -1],
        <BLANKLINE>
        [ 1  0 -1  0  1]
        [ 0  1  1 -1 -1]
        ]

    TESTS::

        sage: rays = [(1, 1), (-1, -1), (-1, 1), (1, -1)]
        sage: cones = [(0,2), (2,1), (1,3), (3,0)]
        sage: fan1 = Fan(cones, rays)
        sage: from sage.geometry.fan_isomorphism import fan_2d_echelon_form, fan_2d_echelon_forms
        sage: echelon_forms = fan_2d_echelon_forms(fan1)
        sage: S4 = CyclicPermutationGroup(4)                                            # needs sage.groups
        sage: rays.reverse()
        sage: cones = [(3,1), (1,2), (2,0), (0,3)]
        sage: for i in range(100):                                                      # needs sage.groups
        ....:     m = random_matrix(ZZ,2,2)
        ....:     if abs(det(m)) != 1: continue
        ....:     perm = S4.random_element()
        ....:     perm_cones = [ (perm(c[0]+1)-1, perm(c[1]+1)-1) for c in cones ]
        ....:     perm_rays = [ rays[perm(i+1)-1] for i in range(len(rays)) ]
        ....:     fan2 = Fan(perm_cones, rays=[m*vector(r) for r in perm_rays])
        ....:     assert fan_2d_echelon_form(fan2) in echelon_forms

    The trivial case was fixed in :issue:`18613`::

        sage: fan = Fan([], lattice=ToricLattice(2))
        sage: fan_2d_echelon_forms(fan)
        frozenset({[]})
        sage: parent(list(_)[0])
        Full MatrixSpace of 2 by 0 dense matrices over Integer Ring
    """
def fan_2d_echelon_form(fan):
    """
    Return echelon form of a cyclically ordered ray matrix.

    INPUT:

    - ``fan`` -- a fan

    OUTPUT:

    A matrix. The echelon form of the rays in one particular cyclic
    order.

    EXAMPLES::

        sage: fan = toric_varieties.P2().fan()                                          # needs palp sage.graphs
        sage: from sage.geometry.fan_isomorphism import fan_2d_echelon_form
        sage: fan_2d_echelon_form(fan)                                                  # needs palp sage.graphs
        [ 1  0 -1]
        [ 0  1 -1]
    """
