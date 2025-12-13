from sage.matrix.constructor import matrix as matrix
from sage.modules.free_module_element import vector as vector
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ

def find_primitive_p_divisible_vector__random(self, p):
    """
    Find a random `p`-primitive vector in `L/pL` whose value is `p`-divisible.

    .. NOTE::

        Since there are about `p^{(n-2)}` of these lines, we have a `1/p`
        chance of randomly finding an appropriate vector.

    EXAMPLES::

        sage: Q = QuadraticForm(ZZ, 2, [10,1,4])
        sage: v = Q.find_primitive_p_divisible_vector__random(5)
        sage: tuple(v) in ((1, 0), (1, 1), (2, 0), (2, 2), (3, 0), (3, 3), (4, 0), (4, 4))
        True
        sage: 5.divides(Q(v))
        True
        sage: Q = QuadraticForm(QQ, matrix.diagonal([1,1,1,1]))
        sage: v = Q.find_primitive_p_divisible_vector__random(2)
        sage: Q(v)
        2
    """
def find_primitive_p_divisible_vector__next(self, p, v=None):
    """
    Find the next `p`-primitive vector (up to scaling) in `L/pL` whose
    value is `p`-divisible, where the last vector returned was `v`.  For
    an initial call, no `v` needs to be passed.

    Return vectors whose last nonzero entry is normalized to 0 or 1 (so no
    lines are counted repeatedly).  The ordering is by increasing the
    first non-normalized entry.  If we have tested all (lines of)
    vectors, then return None.

    OUTPUT: vector or None

    EXAMPLES::

        sage: Q = QuadraticForm(ZZ, 2, [10,1,4])
        sage: v = Q.find_primitive_p_divisible_vector__next(5); v
        (1, 1)
        sage: v = Q.find_primitive_p_divisible_vector__next(5, v); v
        (1, 0)
        sage: v = Q.find_primitive_p_divisible_vector__next(5, v); v
        sage: v = Q.find_primitive_p_divisible_vector__next(2) ; v
        (0, 1)
        sage: v = Q.find_primitive_p_divisible_vector__next(2, v) ; v
        (1, 0)
        sage: Q = QuadraticForm(QQ, matrix.diagonal([1,1,1,1]))
        sage: v = Q.find_primitive_p_divisible_vector__next(2)
        sage: Q(v)
        2
    """
def find_p_neighbor_from_vec(self, p, y, return_matrix: bool = False):
    """
    Return the `p`-neighbor of ``self`` defined by ``y``.

    Let `(L,q)` be a lattice with `b(L,L) \\subseteq \\ZZ` which is maximal at `p`.
    Let `y \\in L` with `b(y,y) \\in p^2\\ZZ` then the `p`-neighbor of
    `L` at `y` is given by
    `\\ZZ y/p + L_y` where `L_y = \\{x \\in L | b(x,y) \\in p \\ZZ \\}`
    and `b(x,y) = q(x+y)-q(x)-q(y)` is the bilinear form associated to `q`.

    INPUT:

    - ``p`` -- a prime number
    - ``y`` -- a vector with `q(y) \\in p \\ZZ`
    - ``odd`` -- boolean (default: ``False``); if `p=2`, return also odd neighbors
    - ``return_matrix`` -- boolean (default: ``False``); return
      the transformation matrix instead of the quadratic form

    EXAMPLES::

        sage: # needs sage.libs.pari
        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1,1])
        sage: v = vector([0,2,1,1])
        sage: X = Q.find_p_neighbor_from_vec(3, v); X
        Quadratic form in 4 variables over Integer Ring with coefficients:
        [ 1 0 0 0 ]
        [ * 1 4 4 ]
        [ * * 5 12 ]
        [ * * * 9 ]
        sage: B = Q.find_p_neighbor_from_vec(3, v, return_matrix=True)
        sage: Q(B) == X
        True

    Since the base ring and the domain are not yet separate,
    for rational, half integral forms we just pretend
    the base ring is `\\ZZ`::

        sage: # needs sage.libs.pari
        sage: Q = QuadraticForm(QQ, matrix.diagonal([1,1,1,1]))
        sage: v = vector([1,1,1,1])
        sage: Q.find_p_neighbor_from_vec(2, v)
        Quadratic form in 4 variables over Rational Field with coefficients:
        [ 1/2 1 1 1 ]
        [ * 1 1 2 ]
        [ * * 1 2 ]
        [ * * * 2 ]
    """
def neighbor_iteration(seeds, p, mass=None, max_classes=None, algorithm=None, max_neighbors: int = 1000, verbose: bool = False):
    """
    Return all classes in the `p`-neighbor graph of ``self``.

    Starting from the given seeds, this function successively
    finds `p`-neighbors until no new quadratic form (class) is obtained.

    INPUT:

    - ``seeds`` -- list of quadratic forms in the same genus

    - ``p`` -- a prime number

    - ``mass`` -- (optional) a rational number; the mass of this genus

    - ``max_classes`` -- (default: ``1000``) break the computation when ``max_classes`` are found

    - ``algorithm`` -- (optional) one of ``'orbits'``, ``'random'``, ``'exhaustion'``

    - ``max_random_trys`` -- (default: ``1000``) the maximum number of neighbors
      computed for a single lattice

    OUTPUT: list of quadratic forms

    EXAMPLES::

        sage: from sage.quadratic_forms.quadratic_form__neighbors import neighbor_iteration
        sage: Q = QuadraticForm(ZZ, 3, [1, 0, 0, 2, 1, 3])
        sage: Q.det()
        46

        sage: # needs sage.symbolic
        sage: mass = Q.conway_mass()
        sage: g1 = neighbor_iteration([Q], 3,   # long time
        ....:                         mass=mass, algorithm='random')
        sage: g2 = neighbor_iteration([Q], 3, algorithm='exhaustion')   # long time
        sage: g3 = neighbor_iteration([Q], 3, algorithm='orbits')                       # needs sage.libs.gap
        sage: mass == sum(1/q.number_of_automorphisms() for q in g1)    # long time
        True
        sage: mass == sum(1/q.number_of_automorphisms() for q in g2)    # long time
        True
        sage: mass == sum(1/q.number_of_automorphisms() for q in g3)                    # needs sage.libs.gap
        True

    TESTS::

        sage: from sage.quadratic_forms.quadratic_form__neighbors import neighbor_iteration
        sage: Q = QuadraticForm(ZZ, 3, [1, 0, 0, 2, 1, 3])
        sage: g = neighbor_iteration([Q], 3, mass=Q.conway_mass(), max_classes=2)       # needs sage.symbolic
        ...
        UserWarning: reached the maximum number of isometry classes=2.
        Increase the optional argument max_classes to obtain more.
        Warning: not all classes in the genus were found
        sage: neighbor_iteration([Q], 3,                                                # needs sage.symbolic
        ....:                    mass=Q.conway_mass(), max_neighbors=0, algorithm='random')
        Warning: not all classes in the genus were found
        []
    """
def orbits_lines_mod_p(self, p):
    """
    Let `(L, q)` be a lattice. This returns representatives of the
    orbits of lines in `L/pL` under the orthogonal group of `q`.

    INPUT:

    - ``p`` -- a prime number

    OUTPUT: list of vectors over ``GF(p)``

    EXAMPLES::

        sage: from sage.quadratic_forms.quadratic_form__neighbors import orbits_lines_mod_p
        sage: Q = QuadraticForm(ZZ, 3, [1, 0, 0, 2, 1, 3])
        sage: Q.orbits_lines_mod_p(2)                                                   # needs sage.libs.gap sage.libs.pari
        [(0, 0, 1),
         (0, 1, 0),
         (0, 1, 1),
         (1, 0, 0),
         (1, 0, 1),
         (1, 1, 0),
         (1, 1, 1)]
    """
