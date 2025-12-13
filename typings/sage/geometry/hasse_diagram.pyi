from sage.combinat.posets.lattices import FiniteLatticePoset as FiniteLatticePoset
from sage.graphs.digraph import DiGraph as DiGraph

def lattice_from_incidences(atom_to_coatoms, coatom_to_atoms, face_constructor=None, required_atoms=None, key=None, **kwds):
    '''
    Compute an atomic and coatomic lattice from the incidence between
    atoms and coatoms.

    INPUT:

    - ``atom_to_coatoms`` -- list; ``atom_to_coatom[i]`` should list all
      coatoms over the ``i``-th atom

    - ``coatom_to_atoms`` -- list; ``coatom_to_atom[i]`` should list all
      atoms under the ``i``-th coatom

    - ``face_constructor`` -- function or class taking as the first two
      arguments sorted :class:`tuple` of integers and any keyword arguments.
      It will be called to construct a face over atoms passed as the first
      argument and under coatoms passed as the second argument. Default
      implementation will just return these two tuples as a tuple;

    - ``required_atoms`` -- list of atoms (default: ``None``); each
      non-empty "face" requires at least one of the specified atoms
      present. Used to ensure that each face has a vertex.

    - ``key`` -- any hashable value (default: ``None``); it is passed down
      to :class:`~sage.combinat.posets.posets.FinitePoset`

    - all other keyword arguments will be passed to ``face_constructor`` on
      each call

    OUTPUT:

    - :class:`finite poset <sage.combinat.posets.posets.FinitePoset>` with
      elements constructed by ``face_constructor``.

    .. NOTE::

        In addition to the specified partial order, finite posets in Sage have
        internal total linear order of elements which extends the partial one.
        This function will try to make this internal order to start with the
        bottom and atoms in the order corresponding to ``atom_to_coatoms`` and
        to finish with coatoms in the order corresponding to
        ``coatom_to_atoms`` and the top. This may not be possible if atoms and
        coatoms are the same, in which case the preference is given to the
        first list.

    ALGORITHM:

    The detailed description of the used algorithm is given in [KP2002]_.

    The code of this function follows the pseudo-code description in the
    section 2.5 of the paper, although it is mostly based on frozen sets
    instead of sorted lists - this makes the implementation easier and should
    not cost a big performance penalty. (If one wants to make this function
    faster, it should be probably written in Cython.)

    While the title of the paper mentions only polytopes, the algorithm (and
    the implementation provided here) is applicable to any atomic and coatomic
    lattice if both incidences are given, see Section 3.4.

    In particular, this function can be used for strictly convex cones and
    complete fans.

    REFERENCES: [KP2002]_

    AUTHORS:

    - Andrey Novoseltsev (2010-05-13) with thanks to Marshall Hampton for the
      reference.

    EXAMPLES:

    Let us construct the lattice of subsets of {0, 1, 2}.
    Our atoms are {0}, {1}, and {2}, while our coatoms are {0,1}, {0,2}, and
    {1,2}. Then incidences are ::

        sage: atom_to_coatoms = [(0,1), (0,2), (1,2)]
        sage: coatom_to_atoms = [(0,1), (0,2), (1,2)]

    and we can compute the lattice as ::

        sage: from sage.geometry.cone import lattice_from_incidences
        sage: L = lattice_from_incidences(atom_to_coatoms, coatom_to_atoms); L          # needs sage.graphs
        Finite lattice containing 8 elements with distinguished linear extension
        sage: for level in L.level_sets(): print(level)                                 # needs sage.graphs
        [((), (0, 1, 2))]
        [((0,), (0, 1)), ((1,), (0, 2)), ((2,), (1, 2))]
        [((0, 1), (0,)), ((0, 2), (1,)), ((1, 2), (2,))]
        [((0, 1, 2), ())]

    For more involved examples see the *source code* of
    :meth:`sage.geometry.cone.ConvexRationalPolyhedralCone.face_lattice` and
    :meth:`sage.geometry.fan.RationalPolyhedralFan._compute_cone_lattice`.
    '''
