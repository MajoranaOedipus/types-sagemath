import sage.matroids.basis_exchange_matroid
from sage.categories.category import ZZ as ZZ
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.matrix.constructor import matrix as matrix
from sage.matroids.utilities import lift_cross_ratios as lift_cross_ratios, newlabel as newlabel, spanning_forest as spanning_forest, spanning_stars as spanning_stars
from sage.rings.finite_rings.finite_field_constructor import GF as GF
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

class BinaryMatroid(LinearMatroid):
    """BinaryMatroid(matrix=None, groundset=None, reduced_matrix=None, ring=None, keep_initial_representation=True, basis=None)

    File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 3011)

    Binary matroids.

    A binary matroid is a linear matroid represented over the finite field
    with two elements. See :class:`LinearMatroid` for a definition.

    The simplest way to create a ``BinaryMatroid`` is by giving only a matrix
    `A`. Then, the groundset defaults to ``range(A.ncols())``. Any iterable
    object `E` can be given as a groundset. If `E` is a list, then ``E[i]``
    will label the `i`-th column of `A`. Another possibility is to specify a
    *reduced* matrix `B`, to create the matroid induced by `A = [ I B ]`.

    INPUT:

    - ``matrix`` -- (default: ``None``) a matrix whose column vectors
      represent the matroid.
    - ``reduced_matrix`` -- (default: ``None``) a matrix `B` such that
      `[I\\ \\ B]` represents the matroid, where `I` is an identity matrix with
      the same number of rows as `B`. Only one of ``matrix`` and
      ``reduced_matrix`` should be provided.
    - ``groundset`` -- (default: ``None``) an iterable containing the element
      labels. When provided, must have the correct number of elements: the
      number of columns of ``matrix`` or the number of rows plus the number
      of columns of ``reduced_matrix``.
    - ``ring`` -- (default: ``None``) ignored
    - ``keep_initial_representation`` -- boolean (default: ``True``); whether
      or not an internal copy of the input matrix should be preserved. This
      can help to see the structure of the matroid (e.g. in the case of
      graphic matroids), and makes it easier to look at extensions. However,
      the input matrix may have redundant rows, and sometimes it is desirable
      to store only a row-reduced copy.
    - ``basis`` -- (default: ``None``) when provided, this is an ordered
      subset of ``groundset``, such that the submatrix of ``matrix`` indexed
      by ``basis`` is an identity matrix. In this case, no row reduction takes
      place in the initialization phase.

    OUTPUT: a :class:`BinaryMatroid` instance based on the data above

    .. NOTE::

        An indirect way to generate a binary matroid is through the
        :func:`Matroid() <sage.matroids.constructor.Matroid>` function. This
        is usually the preferred way, since it automatically chooses between
        :class:`BinaryMatroid` and other classes. For direct access to the
        ``BinaryMatroid`` constructor, run::

            sage: from sage.matroids.advanced import *

    EXAMPLES::

        sage: A = Matrix(GF(2), 2, 4, [[1, 0, 1, 1], [0, 1, 1, 1]])
        sage: M = Matroid(A)
        sage: M
        Binary matroid of rank 2 on 4 elements, type (0, 6)
        sage: sorted(M.groundset())
        [0, 1, 2, 3]
        sage: Matrix(M)
        [1 0 1 1]
        [0 1 1 1]
        sage: M = Matroid(matrix=A, groundset='abcd')
        sage: sorted(M.groundset())
        ['a', 'b', 'c', 'd']
        sage: B = Matrix(GF(2), 2, 2, [[1, 1], [1, 1]])
        sage: N = Matroid(reduced_matrix=B, groundset='abcd')
        sage: M == N
        True"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, matrix=..., groundset=..., reduced_matrix=..., ring=..., keep_initial_representation=..., basis=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 3079)

                See the class definition for full documentation.

                .. NOTE::

                    The extra argument ``basis``, when provided, is an ordered list of
                    elements of the groundset, ordered such that they index a standard
                    identity matrix within ``matrix``.

                EXAMPLES::

                    sage: from sage.matroids.advanced import *
                    sage: BinaryMatroid(matrix=Matrix(GF(5), [[1, 0, 1, 1, 1],      # indirect doctest
                    ....:                                     [0, 1, 1, 2, 3]]))
                    Binary matroid of rank 2 on 5 elements, type (1, 7)
        """
    def base_ring(self) -> Any:
        """BinaryMatroid.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 3150)

        Return the base ring of the matrix representing the matroid,
        in this case `\\GF{2}`.

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: M.base_ring()
            Finite Field of size 2"""
    def bicycle_dimension(self) -> Any:
        """BinaryMatroid.bicycle_dimension(self)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 3562)

        Return the bicycle dimension of the binary matroid.

        The *bicycle dimension* of a linear subspace `V` is
        `\\dim(V\\cap V^\\perp)`. The bicycle dimension of a matroid equals the
        bicycle dimension of its cocycle-space, and is an invariant for binary
        matroids. See [Pen2012]_, [GR2001]_ for more information.

        OUTPUT: integer

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: M.bicycle_dimension()
            3"""
    @overload
    def binary_matroid(self, randomized_tests=..., verify=...) -> Any:
        """BinaryMatroid.binary_matroid(self, randomized_tests=1, verify=True)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 3895)

        Return a binary matroid representing ``self``.

        INPUT:

        - ``randomized_tests`` -- ignored
        - ``verify`` -- ignored

        OUTPUT: a binary matroid

        ALGORITHM:

        ``self`` is a binary matroid, so just return ``self``.

        .. SEEALSO::

            :meth:`M.binary_matroid()
            <sage.matroids.matroid.Matroid.binary_matroid>`

        EXAMPLES::

            sage: N = matroids.catalog.Fano()
            sage: N.binary_matroid() is N
            True"""
    @overload
    def binary_matroid(self) -> Any:
        """BinaryMatroid.binary_matroid(self, randomized_tests=1, verify=True)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 3895)

        Return a binary matroid representing ``self``.

        INPUT:

        - ``randomized_tests`` -- ignored
        - ``verify`` -- ignored

        OUTPUT: a binary matroid

        ALGORITHM:

        ``self`` is a binary matroid, so just return ``self``.

        .. SEEALSO::

            :meth:`M.binary_matroid()
            <sage.matroids.matroid.Matroid.binary_matroid>`

        EXAMPLES::

            sage: N = matroids.catalog.Fano()
            sage: N.binary_matroid() is N
            True"""
    @overload
    def binary_matroid(self) -> Any:
        """BinaryMatroid.binary_matroid(self, randomized_tests=1, verify=True)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 3895)

        Return a binary matroid representing ``self``.

        INPUT:

        - ``randomized_tests`` -- ignored
        - ``verify`` -- ignored

        OUTPUT: a binary matroid

        ALGORITHM:

        ``self`` is a binary matroid, so just return ``self``.

        .. SEEALSO::

            :meth:`M.binary_matroid()
            <sage.matroids.matroid.Matroid.binary_matroid>`

        EXAMPLES::

            sage: N = matroids.catalog.Fano()
            sage: N.binary_matroid() is N
            True"""
    def brown_invariant(self) -> Any:
        """BinaryMatroid.brown_invariant(self)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 3583)

        Return the value of Brown's invariant for the binary matroid.

        For a binary space `V`, consider the sum
        `B(V):=\\sum_{v\\in V} i^{|v|}`, where `|v|` denotes the number of
        nonzero entries of a binary vector `v`. The value of the Tutte
        Polynomial in the point `(-i, i)` can be expressed in terms of
        `B(V)`, see [Pen2012]_. If `|v|` equals `2` modulo 4 for some
        `v\\in V\\cap V^\\perp`, then `B(V)=0`. In this case, Browns invariant is
        not defined. Otherwise, `B(V)=\\sqrt{2}^k \\exp(\\sigma \\pi i/4)` for
        some integers `k, \\sigma`. In that case, `k` equals the bycycle
        dimension of `V`, and Browns invariant for `V` is defined as `\\sigma`
        modulo `8`.

        The Brown invariant of a binary matroid equals the Brown invariant of
        its cocycle-space.

        OUTPUT: integer

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: M.brown_invariant()
            0
            sage: M = Matroid(Matrix(GF(2), 3, 8, [[1, 0, 0, 1, 1, 1, 1, 1],
            ....:                                  [0, 1, 0, 1, 1, 0, 0, 0],
            ....:                                  [0, 0, 1, 0, 0, 1, 1, 0]]))
            sage: M.brown_invariant() is None
            True"""
    @overload
    def characteristic(self) -> Any:
        """BinaryMatroid.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 3164)

        Return the characteristic of the base ring of the matrix representing
        the matroid, in this case `2`.

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: M.characteristic()
            2"""
    @overload
    def characteristic(self) -> Any:
        """BinaryMatroid.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 3164)

        Return the characteristic of the base ring of the matrix representing
        the matroid, in this case `2`.

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: M.characteristic()
            2"""
    @overload
    def is_binary(self, randomized_tests=...) -> Any:
        """BinaryMatroid.is_binary(self, randomized_tests=1)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 3923)

        Decide if ``self`` is a binary matroid.

        INPUT:

        - ``randomized_tests`` -- ignored

        OUTPUT: boolean

        ALGORITHM:

        ``self`` is a binary matroid, so just return ``True``.

        .. SEEALSO::

            :meth:`M.is_binary() <sage.matroids.matroid.Matroid.is_binary>`

        EXAMPLES::

            sage: N = matroids.catalog.Fano()
            sage: N.is_binary()
            True"""
    @overload
    def is_binary(self) -> Any:
        """BinaryMatroid.is_binary(self, randomized_tests=1)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 3923)

        Decide if ``self`` is a binary matroid.

        INPUT:

        - ``randomized_tests`` -- ignored

        OUTPUT: boolean

        ALGORITHM:

        ``self`` is a binary matroid, so just return ``True``.

        .. SEEALSO::

            :meth:`M.is_binary() <sage.matroids.matroid.Matroid.is_binary>`

        EXAMPLES::

            sage: N = matroids.catalog.Fano()
            sage: N.is_binary()
            True"""
    @overload
    def is_binary(self) -> Any:
        """BinaryMatroid.is_binary(self, randomized_tests=1)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 3923)

        Decide if ``self`` is a binary matroid.

        INPUT:

        - ``randomized_tests`` -- ignored

        OUTPUT: boolean

        ALGORITHM:

        ``self`` is a binary matroid, so just return ``True``.

        .. SEEALSO::

            :meth:`M.is_binary() <sage.matroids.matroid.Matroid.is_binary>`

        EXAMPLES::

            sage: N = matroids.catalog.Fano()
            sage: N.is_binary()
            True"""
    @overload
    def is_graphic(self) -> bool:
        """BinaryMatroid.is_graphic(self) -> bool

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 3802)

        Test if the binary matroid is graphic.

        A matroid is *graphic* if there exists a graph whose edge set equals
        the groundset of the matroid, such that a subset of elements of the
        matroid is independent if and only if the corresponding subgraph is
        acyclic.

        OUTPUT: boolean

        EXAMPLES::

            sage: R10 = matroids.catalog.R10()
            sage: M = Matroid(ring=GF(2), reduced_matrix=R10.representation(
            ....:                                 reduced=True, labels=False))
            sage: M.is_graphic()
            False
            sage: K5 = Matroid(graphs.CompleteGraph(5), regular=True)                   # needs sage.graphs
            sage: M = Matroid(ring=GF(2), reduced_matrix=K5.representation(             # needs sage.graphs sage.rings.finite_rings
            ....:                                 reduced=True, labels=False))
            sage: M.is_graphic()                                                        # needs sage.graphs sage.rings.finite_rings
            True
            sage: M.dual().is_graphic()                                                 # needs sage.graphs
            False

        ALGORITHM:

        In a recent paper, Geelen and Gerards [GG2012]_ reduced the problem to
        testing if a system of linear equations has a solution. While not the
        fastest method, and not necessarily constructive (in the presence of
        2-separations especially), it is easy to implement."""
    @overload
    def is_graphic(self) -> Any:
        """BinaryMatroid.is_graphic(self) -> bool

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 3802)

        Test if the binary matroid is graphic.

        A matroid is *graphic* if there exists a graph whose edge set equals
        the groundset of the matroid, such that a subset of elements of the
        matroid is independent if and only if the corresponding subgraph is
        acyclic.

        OUTPUT: boolean

        EXAMPLES::

            sage: R10 = matroids.catalog.R10()
            sage: M = Matroid(ring=GF(2), reduced_matrix=R10.representation(
            ....:                                 reduced=True, labels=False))
            sage: M.is_graphic()
            False
            sage: K5 = Matroid(graphs.CompleteGraph(5), regular=True)                   # needs sage.graphs
            sage: M = Matroid(ring=GF(2), reduced_matrix=K5.representation(             # needs sage.graphs sage.rings.finite_rings
            ....:                                 reduced=True, labels=False))
            sage: M.is_graphic()                                                        # needs sage.graphs sage.rings.finite_rings
            True
            sage: M.dual().is_graphic()                                                 # needs sage.graphs
            False

        ALGORITHM:

        In a recent paper, Geelen and Gerards [GG2012]_ reduced the problem to
        testing if a system of linear equations has a solution. While not the
        fastest method, and not necessarily constructive (in the presence of
        2-separations especially), it is easy to implement."""
    @overload
    def is_graphic(self) -> Any:
        """BinaryMatroid.is_graphic(self) -> bool

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 3802)

        Test if the binary matroid is graphic.

        A matroid is *graphic* if there exists a graph whose edge set equals
        the groundset of the matroid, such that a subset of elements of the
        matroid is independent if and only if the corresponding subgraph is
        acyclic.

        OUTPUT: boolean

        EXAMPLES::

            sage: R10 = matroids.catalog.R10()
            sage: M = Matroid(ring=GF(2), reduced_matrix=R10.representation(
            ....:                                 reduced=True, labels=False))
            sage: M.is_graphic()
            False
            sage: K5 = Matroid(graphs.CompleteGraph(5), regular=True)                   # needs sage.graphs
            sage: M = Matroid(ring=GF(2), reduced_matrix=K5.representation(             # needs sage.graphs sage.rings.finite_rings
            ....:                                 reduced=True, labels=False))
            sage: M.is_graphic()                                                        # needs sage.graphs sage.rings.finite_rings
            True
            sage: M.dual().is_graphic()                                                 # needs sage.graphs
            False

        ALGORITHM:

        In a recent paper, Geelen and Gerards [GG2012]_ reduced the problem to
        testing if a system of linear equations has a solution. While not the
        fastest method, and not necessarily constructive (in the presence of
        2-separations especially), it is easy to implement."""
    @overload
    def is_graphic(self) -> Any:
        """BinaryMatroid.is_graphic(self) -> bool

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 3802)

        Test if the binary matroid is graphic.

        A matroid is *graphic* if there exists a graph whose edge set equals
        the groundset of the matroid, such that a subset of elements of the
        matroid is independent if and only if the corresponding subgraph is
        acyclic.

        OUTPUT: boolean

        EXAMPLES::

            sage: R10 = matroids.catalog.R10()
            sage: M = Matroid(ring=GF(2), reduced_matrix=R10.representation(
            ....:                                 reduced=True, labels=False))
            sage: M.is_graphic()
            False
            sage: K5 = Matroid(graphs.CompleteGraph(5), regular=True)                   # needs sage.graphs
            sage: M = Matroid(ring=GF(2), reduced_matrix=K5.representation(             # needs sage.graphs sage.rings.finite_rings
            ....:                                 reduced=True, labels=False))
            sage: M.is_graphic()                                                        # needs sage.graphs sage.rings.finite_rings
            True
            sage: M.dual().is_graphic()                                                 # needs sage.graphs
            False

        ALGORITHM:

        In a recent paper, Geelen and Gerards [GG2012]_ reduced the problem to
        testing if a system of linear equations has a solution. While not the
        fastest method, and not necessarily constructive (in the presence of
        2-separations especially), it is easy to implement."""
    def is_valid(self, certificate=...) -> Any:
        """BinaryMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 3872)

        Test if the data obey the matroid axioms.

        Since this is a linear matroid over the field `\\GF{2}`, this is always
        the case.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: ``True``, or ``(True, {})``

        EXAMPLES::

            sage: M = Matroid(Matrix(GF(2), [[]]))
            sage: M.is_valid()
            True"""
    @overload
    def relabel(self, mapping) -> Any:
        """BinaryMatroid.relabel(self, mapping)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 4007)

        Return an isomorphic matroid with relabeled groundset.

        The output is obtained by relabeling each element `e` by
        ``mapping[e]``, where ``mapping`` is a given injective map. If
        ``mapping[e]`` is not defined, then the identity map is assumed.

        INPUT:

        - ``mapping`` -- a Python object such that ``mapping[e]`` is the new
          label of `e`

        OUTPUT: matroid

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: sorted(M.groundset())
            ['a', 'b', 'c', 'd', 'e', 'f', 'g']
            sage: N = M.relabel({'g': 'x'})
            sage: sorted(N.groundset())
            ['a', 'b', 'c', 'd', 'e', 'f', 'x']

        TESTS::

            sage: M = matroids.catalog.Fano()
            sage: f = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}
            sage: N = M.relabel(f)
            sage: for S in powerset(M.groundset()):
            ....:     assert M.rank(S) == N.rank([f[x] for x in S])"""
    @overload
    def relabel(self, f) -> Any:
        """BinaryMatroid.relabel(self, mapping)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 4007)

        Return an isomorphic matroid with relabeled groundset.

        The output is obtained by relabeling each element `e` by
        ``mapping[e]``, where ``mapping`` is a given injective map. If
        ``mapping[e]`` is not defined, then the identity map is assumed.

        INPUT:

        - ``mapping`` -- a Python object such that ``mapping[e]`` is the new
          label of `e`

        OUTPUT: matroid

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: sorted(M.groundset())
            ['a', 'b', 'c', 'd', 'e', 'f', 'g']
            sage: N = M.relabel({'g': 'x'})
            sage: sorted(N.groundset())
            ['a', 'b', 'c', 'd', 'e', 'f', 'x']

        TESTS::

            sage: M = matroids.catalog.Fano()
            sage: f = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}
            sage: N = M.relabel(f)
            sage: for S in powerset(M.groundset()):
            ....:     assert M.rank(S) == N.rank([f[x] for x in S])"""
    def __reduce__(self) -> Any:
        """BinaryMatroid.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 3949)

        Save the matroid for later reloading.

        OUTPUT:

        A tuple ``(unpickle_binary_matroid, (version, data))``, where
        ``unpickle_binary_matroid`` is the name of a function that, when
        called with ``(version, data)``, produces a matroid isomorphic to
        ``self``. ``version`` is an integer (currently 0) and ``data`` is a
        tuple ``(A, E, B, name)`` where ``A`` is the representation
        matrix, ``E`` is the groundset of the matroid, ``B`` is the currently
        displayed basis, and ``name`` is a custom name.

        .. WARNING::

            Users should never call this function directly.

        EXAMPLES::

            sage: M = Matroid(Matrix(GF(2), [[1, 0, 0, 1], [0, 1, 0, 1],
            ....:        [0, 0, 1, 1]]))
            sage: M == loads(dumps(M))  # indirect doctest
            True
            sage: M.rename('U34')
            sage: loads(dumps(M))
            U34
            sage: M = Matroid(Matrix(GF(2), [[1, 0, 1], [1, 0, 1]]))
            sage: loads(dumps(M)).representation()
            [1 0 1]
            [1 0 1]

        TESTS:

        Check that :issue:`23437` is fixed::

            sage: M = matroids.catalog.Fano().dual()
            sage: B = list(M.bases())
            sage: N = loads(dumps(M))
            sage: N.closure(frozenset({'d'}))
            frozenset({'d'})
            sage: N.is_isomorphic(M)
            True"""

class LinearMatroid(sage.matroids.basis_exchange_matroid.BasisExchangeMatroid):
    """LinearMatroid(matrix=None, groundset=None, reduced_matrix=None, ring=None, keep_initial_representation=True)

    File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 189)

    Linear matroids.

    When `A` is an `r` times `E` matrix, the linear matroid `M[A]` has ground
    set `E` and set of independent sets

        `I(A) =\\{F \\subseteq E :` the columns of `A` indexed by `F` are linearly independent `\\}`

    The simplest way to create a LinearMatroid is by giving only a matrix `A`.
    Then, the groundset defaults to ``range(A.ncols())``. Any iterable object
    ``E`` can be given as a groundset. If ``E`` is a list, then ``E[i]`` will
    label the `i`-th column of `A`. Another possibility is to specify a
    *reduced* matrix `B`, to create the matroid induced by `A = [ I B ]`.

    INPUT:

    - ``matrix`` -- (default: ``None``) a matrix whose column vectors
      represent the matroid
    - ``reduced_matrix`` -- (default: ``None``) a matrix `B` such that
      `[I\\ \\ B]` represents the matroid, where `I` is an identity matrix with
      the same number of rows as `B`. Only one of ``matrix`` and
      ``reduced_matrix`` should be provided.
    - ``groundset`` -- (default: ``None``) an iterable containing the element
      labels. When provided, must have the correct number of elements: the
      number of columns of ``matrix`` or the number of rows plus the number
      of columns of ``reduced_matrix``.
    - ``ring`` -- (default: ``None``) the desired base ring of the matrix. If
      the base ring is different, an attempt will be made to create a new
      matrix with the correct base ring.
    - ``keep_initial_representation`` -- boolean (default: ``True``); whether
      or not an internal copy of the input matrix should be preserved. This
      can help to see the structure of the matroid (e.g. in the case of
      graphic matroids), and makes it easier to look at extensions. However,
      the input matrix may have redundant rows, and sometimes it is desirable
      to store only a row-reduced copy.

    OUTPUT: a ``LinearMatroid`` instance based on the data above

    .. NOTE::

        The recommended way to generate a linear matroid is through the
        :func:`Matroid() <sage.matroids.constructor.Matroid>` function. It
        will automatically choose more optimized classes when present
        (currently :class:`BinaryMatroid`, :class:`TernaryMatroid`,
        :class:`QuaternaryMatroid`, :class:`RegularMatroid`). For direct
        access to the ``LinearMatroid`` constructor, run::

            sage: from sage.matroids.advanced import *

    EXAMPLES::

        sage: from sage.matroids.advanced import *
        sage: A = Matrix(GF(3), 2, 4, [[1, 0, 1, 1], [0, 1, 1, 2]])
        sage: M = LinearMatroid(A)
        sage: M
        Linear matroid of rank 2 on 4 elements represented over the Finite
        Field of size 3
        sage: sorted(M.groundset())
        [0, 1, 2, 3]
        sage: Matrix(M)
        [1 0 1 1]
        [0 1 1 2]
        sage: M = LinearMatroid(A, 'abcd')
        sage: sorted(M.groundset())
        ['a', 'b', 'c', 'd']
        sage: B = Matrix(GF(3), 2, 2, [[1, 1], [1, 2]])
        sage: N = LinearMatroid(reduced_matrix=B, groundset='abcd')
        sage: M == N
        True"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, matrix=..., groundset=..., reduced_matrix=..., ring=..., keep_initial_representation=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 260)

                See the class definition for full documentation.

                EXAMPLES::

                    sage: from sage.matroids.advanced import *
                    sage: LinearMatroid(matrix=Matrix(GF(5), [[1, 0, 1, 1, 1],        # indirect doctest
                    ....:                                     [0, 1, 1, 2, 3]]))
                    Linear matroid of rank 2 on 5 elements represented over the Finite
                    Field of size 5
        """
    @overload
    def base_ring(self) -> Any:
        """LinearMatroid.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 365)

        Return the base ring of the matrix representing the matroid.

        EXAMPLES::

            sage: M = Matroid(matrix=Matrix(GF(5), [[1, 0, 1, 1, 1],
            ....:                                   [0, 1, 1, 2, 3]]))
            sage: M.base_ring()
            Finite Field of size 5"""
    @overload
    def base_ring(self) -> Any:
        """LinearMatroid.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 365)

        Return the base ring of the matrix representing the matroid.

        EXAMPLES::

            sage: M = Matroid(matrix=Matrix(GF(5), [[1, 0, 1, 1, 1],
            ....:                                   [0, 1, 1, 2, 3]]))
            sage: M.base_ring()
            Finite Field of size 5"""
    @overload
    def characteristic(self) -> Any:
        """LinearMatroid.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 378)

        Return the characteristic of the base ring of the matrix representing
        the matroid.

        EXAMPLES::

            sage: M = Matroid(matrix=Matrix(GF(5), [[1, 0, 1, 1, 1],
            ....:                                   [0, 1, 1, 2, 3]]))
            sage: M.characteristic()
            5"""
    @overload
    def characteristic(self) -> Any:
        """LinearMatroid.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 378)

        Return the characteristic of the base ring of the matrix representing
        the matroid.

        EXAMPLES::

            sage: M = Matroid(matrix=Matrix(GF(5), [[1, 0, 1, 1, 1],
            ....:                                   [0, 1, 1, 2, 3]]))
            sage: M.characteristic()
            5"""
    def cross_ratio(self, F, a, b, c, d) -> Any:
        """LinearMatroid.cross_ratio(self, F, a, b, c, d)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 1745)

        Return the cross ratio of the four ordered points ``a, b, c, d``
        after contracting a flat ``F`` of codimension 2.

        Consider the following matrix with columns labeled by
        `\\{a, b, c, d\\}`.

        .. MATH::

            \\begin{bmatrix}
              1 & 0 & 1 & 1\\\\\n              0 & 1 & x & 1
            \\end{bmatrix}

        The cross ratio of the ordered tuple `(a, b, c, d)` equals `x`. This
        method looks at such minors where ``F`` is a flat to be contracted,
        and all remaining elements other than ``a, b, c, d`` are deleted.

        INPUT:

        - ``F`` -- a flat of codimension 2
        - ``a``, ``b``, ``c``, ``d`` -- elements of the groundset

        OUTPUT:

        The cross ratio of the four points on the line obtained by
        contracting ``F``.

        EXAMPLES::

            sage: M = Matroid(Matrix(GF(7), [[1, 0, 0, 1, 1, 1],
            ....:                            [0, 1, 0, 1, 2, 4],
            ....:                            [0, 0, 1, 3, 2, 6]]))
            sage: M.cross_ratio([0], 1, 2, 3, 5)
            4

            sage: M = Matroid(ring=GF(7), matrix=[[1, 0, 1, 1], [0, 1, 1, 1]])
            sage: M.cross_ratio(set(), 0, 1, 2, 3)
            Traceback (most recent call last):
            ...
            ValueError: points a, b, c, d do not form a 4-point line in M/F"""
    def cross_ratios(self, hyperlines=...) -> Any:
        """LinearMatroid.cross_ratios(self, hyperlines=None)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 1687)

        Return the set of cross ratios that occur in this linear matroid.

        Consider the following matrix with columns labeled by
        `\\{a, b, c, d\\}`.

        .. MATH::

            \\begin{matrix}
              1 & 0 & 1 & 1\\\\\n              0 & 1 & x & 1
            \\end{matrix}

        The cross ratio of the ordered tuple `(a, b, c, d)` equals `x`. The
        set of all cross ratios of a matroid is the set of cross ratios of all
        such minors.

        INPUT:

        - ``hyperlines`` -- (optional) a set of flats of the matroid, of rank
          `r - 2`, where `r` is the rank of the matroid. If not given, then
          ``hyperlines`` defaults to all such flats.

        OUTPUT:

        A list of all cross ratios of this linearly represented matroid that
        occur in rank-2 minors that arise by contracting a flat ``F`` in
        ``hyperlines`` (so by default, those are all cross ratios).

        .. SEEALSO::

            :meth:`M.cross_ratio() <LinearMatroid.cross_ratio>`

        EXAMPLES::

            sage: M = Matroid(Matrix(GF(7), [[1, 0, 0, 1, 1, 1],
            ....:                            [0, 1, 0, 1, 2, 4],
            ....:                            [0, 0, 1, 3, 2, 5]]))
            sage: sorted(M.cross_ratios())
            [2, 3, 4, 5, 6]
            sage: M = Matroid(graphs.CompleteGraph(5), regular=True)                    # needs sage.graphs
            sage: M.cross_ratios()                                                      # needs sage.graphs
            set()"""
    def dual(self) -> Any:
        """LinearMatroid.dual(self)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 1350)

        Return the dual of the matroid.

        Let `M` be a matroid with groundset `E`. If `B` is the set of bases
        of `M`, then the set `\\{E - b : b \\in B\\}` is the set of bases of
        another matroid, the *dual* of `M`.

        If the matroid is represented by `[I_1\\ \\ A]`, then the dual is
        represented by `[-A^T\\ \\ I_2]` for appropriately sized identity
        matrices `I_1, I_2`.

        OUTPUT: the dual matroid

        EXAMPLES::

            sage: A = Matrix(GF(7), [[1, 1, 0, 1],
            ....:                    [1, 0, 1, 1],
            ....:                    [0, 1, 1, 1]])
            sage: B = - A.transpose()
            sage: Matroid(reduced_matrix=A).dual() == Matroid(
            ....:                             reduced_matrix=B,
            ....:                             groundset=[3, 4, 5, 6, 0, 1, 2])
            True"""
    def fundamental_cocycle(self, B, e) -> Any:
        """LinearMatroid.fundamental_cocycle(self, B, e)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 1562)

        Return the fundamental cycle, relative to ``B``, containing element
        ``e``.

        This is the
        :meth:`fundamental cocircuit <sage.matroids.matroid.Matroid.fundamental_cocircuit>`
        together with an appropriate signing from the field, such that `Av=0`,
        where `A` is a representation matrix of the dual, and `v` the vector
        corresponding to the output.

        INPUT:

        - ``B`` -- a basis of the matroid
        - ``e`` -- an element of the basis

        OUTPUT:

        A dictionary mapping elements of ``M.fundamental_cocircuit(B, e)`` to
        elements of the ring.

        .. SEEALSO::

            :meth:`M.fundamental_cocircuit() <sage.matroids.matroid.Matroid.fundamental_cocircuit>`

        EXAMPLES::

            sage: M = Matroid(Matrix(GF(7), [[1, 0, 1, 1], [0, 1, 1, 4]]))
            sage: v = M.fundamental_cocycle([0, 1], 0)
            sage: [v[0], v[2], v[3]]
            [1, 1, 1]
            sage: frozenset(v.keys()) == M.fundamental_cocircuit([0, 1], 0)
            True"""
    def fundamental_cycle(self, B, e) -> Any:
        """LinearMatroid.fundamental_cycle(self, B, e)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 1515)

        Return the fundamental cycle, relative to ``B``, containing element
        ``e``.

        This is the
        :meth:`fundamental circuit <sage.matroids.matroid.Matroid.fundamental_circuit>`
        together with an appropriate signing from the field, such that `Av=0`,
        where `A` is the representation matrix, and `v` the vector
        corresponding to the output.

        INPUT:

        - ``B`` -- a basis of the matroid
        - ``e`` -- an element outside the basis

        OUTPUT:

        A dictionary mapping elements of ``M.fundamental_circuit(B, e)`` to
        elements of the ring.

        .. SEEALSO::

            :meth:`M.fundamental_circuit() <sage.matroids.matroid.Matroid.fundamental_circuit>`

        EXAMPLES::

            sage: M = Matroid(Matrix(GF(7), [[1, 0, 1, 1], [0, 1, 1, 4]]))
            sage: v = M.fundamental_cycle([0, 1], 3)
            sage: [v[0], v[1], v[3]]
            [6, 3, 1]
            sage: frozenset(v.keys()) == M.fundamental_circuit([0, 1], 3)
            True"""
    @overload
    def has_field_minor(self, N) -> Any:
        """LinearMatroid.has_field_minor(self, N)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 1431)

        Check if ``self`` has a minor field isomorphic to ``N``.

        INPUT:

        - ``N`` -- matroid

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.minor() <sage.matroids.matroid.Matroid.minor>`,
            :meth:`M.is_field_isomorphic() <LinearMatroid.is_field_isomorphic>`

        .. TODO::

            This important method can (and should) be optimized considerably.
            See [Hli2006]_ p.1219 for hints to that end.

        EXAMPLES::

            sage: M = matroids.Whirl(3)
            sage: matroids.catalog.Fano().has_field_minor(M)
            False
            sage: matroids.catalog.NonFano().has_field_minor(M)
            True"""
    @overload
    def has_field_minor(self, M) -> Any:
        """LinearMatroid.has_field_minor(self, N)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 1431)

        Check if ``self`` has a minor field isomorphic to ``N``.

        INPUT:

        - ``N`` -- matroid

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.minor() <sage.matroids.matroid.Matroid.minor>`,
            :meth:`M.is_field_isomorphic() <LinearMatroid.is_field_isomorphic>`

        .. TODO::

            This important method can (and should) be optimized considerably.
            See [Hli2006]_ p.1219 for hints to that end.

        EXAMPLES::

            sage: M = matroids.Whirl(3)
            sage: matroids.catalog.Fano().has_field_minor(M)
            False
            sage: matroids.catalog.NonFano().has_field_minor(M)
            True"""
    @overload
    def has_field_minor(self, M) -> Any:
        """LinearMatroid.has_field_minor(self, N)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 1431)

        Check if ``self`` has a minor field isomorphic to ``N``.

        INPUT:

        - ``N`` -- matroid

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.minor() <sage.matroids.matroid.Matroid.minor>`,
            :meth:`M.is_field_isomorphic() <LinearMatroid.is_field_isomorphic>`

        .. TODO::

            This important method can (and should) be optimized considerably.
            See [Hli2006]_ p.1219 for hints to that end.

        EXAMPLES::

            sage: M = matroids.Whirl(3)
            sage: matroids.catalog.Fano().has_field_minor(M)
            False
            sage: matroids.catalog.NonFano().has_field_minor(M)
            True"""
    def has_line_minor(self, k, hyperlines=..., certificate=...) -> Any:
        """LinearMatroid.has_line_minor(self, k, hyperlines=None, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 1379)

        Test if the matroid has a `U_{2, k}`-minor.

        The matroid `U_{2, k}` is a matroid on `k` elements in which every
        subset of at most 2 elements is independent, and every subset of more
        than two elements is dependent.

        The optional argument ``hyperlines`` restricts the search space: this
        method returns ``True`` if `si(M/F)` is isomorphic to `U_{2, l}` with
        `l \\geq k` for some `F` in ``hyperlines``, and ``False`` otherwise.

        INPUT:

        - ``k`` -- the length of the line minor
        - ``hyperlines`` -- (default: ``None``) a set of flats of codimension
          2. Defaults to the set of all flats of codimension 2.
        - ``certificate`` -- (default: ``False``) if ``True`` returns
          ``True, F``, where ``F`` is a flat and ``self.minor(contractions=F)``
          has a `U_{2,k}` restriction or ``False, None``

        OUTPUT: boolean or tuple

        EXAMPLES::

            sage: M = matroids.catalog.N1()
            sage: M.has_line_minor(4)
            True
            sage: M.has_line_minor(5)
            False
            sage: M.has_line_minor(k=4, hyperlines=[['a', 'b', 'c']])
            False
            sage: M.has_line_minor(k=4, hyperlines=[['a', 'b', 'c'],
            ....:                                   ['a', 'b', 'd' ]])
            True
            sage: M.has_line_minor(4, certificate=True)
            (True, frozenset({'a', 'b', 'd'}))
            sage: M.has_line_minor(5, certificate=True)
            (False, None)
            sage: M.has_line_minor(k=4, hyperlines=[['a', 'b', 'c'],
            ....:                                   ['a', 'b', 'd' ]], certificate=True)
            (True, frozenset({'a', 'b', 'd'}))"""
    @overload
    def is_field_equivalent(self, other) -> Any:
        """LinearMatroid.is_field_equivalent(self, other)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 917)

        Test for matroid representation equality.

        Two linear matroids `M` and `N` with representation matrices `A` and
        `B` are *field equivalent* if they have the same groundset, and the
        identity map between the groundsets is an isomorphism between the
        representations `A` and `B`. That is, one can be turned into the other
        using only row operations and column scaling.

        INPUT:

        - ``other`` -- matroid

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.equals() <sage.matroids.matroid.Matroid.equals>`,
            :meth:`M.is_field_isomorphism() <LinearMatroid.is_field_isomorphism>`,
            :meth:`M.is_field_isomorphic() <LinearMatroid.is_field_isomorphic>`

        EXAMPLES:

        A :class:`BinaryMatroid` and
        :class:`LinearMatroid` use different
        representations of the matroid internally, so `` == ``
        yields ``False``, even if the matroids are equal::

            sage: from sage.matroids.advanced import *
            sage: M = matroids.catalog.Fano()
            sage: M1 = LinearMatroid(Matrix(M), groundset=M.groundset_list())
            sage: M2 = Matroid(groundset='abcdefg',
            ....:              reduced_matrix=[[0, 1, 1, 1],
            ....:                              [1, 0, 1, 1],
            ....:                              [1, 1, 0, 1]], field=GF(2))
            sage: M.equals(M1)
            True
            sage: M.equals(M2)
            True
            sage: M.is_field_equivalent(M1)
            True
            sage: M.is_field_equivalent(M2)
            True
            sage: M == M1
            False
            sage: M == M2
            True

        ``LinearMatroid`` instances ``M`` and ``N`` satisfy ``M == N`` if the
        representations are equivalent up to row operations and column
        scaling::

            sage: M1 = Matroid(groundset='abcd',
            ....:          matrix=Matrix(GF(7), [[1, 0, 1, 1], [0, 1, 1, 2]]))
            sage: M2 = Matroid(groundset='abcd',
            ....:          matrix=Matrix(GF(7), [[1, 0, 1, 1], [0, 1, 1, 3]]))
            sage: M3 = Matroid(groundset='abcd',
            ....:          matrix=Matrix(GF(7), [[2, 6, 1, 0], [6, 1, 0, 1]]))
            sage: M1.equals(M2)
            True
            sage: M1.equals(M3)
            True
            sage: M1 == M2
            False
            sage: M1 == M3
            True
            sage: M1.is_field_equivalent(M2)
            False
            sage: M1.is_field_equivalent(M3)
            True
            sage: M1.is_field_equivalent(M1)
            True"""
    @overload
    def is_field_equivalent(self, M1) -> Any:
        """LinearMatroid.is_field_equivalent(self, other)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 917)

        Test for matroid representation equality.

        Two linear matroids `M` and `N` with representation matrices `A` and
        `B` are *field equivalent* if they have the same groundset, and the
        identity map between the groundsets is an isomorphism between the
        representations `A` and `B`. That is, one can be turned into the other
        using only row operations and column scaling.

        INPUT:

        - ``other`` -- matroid

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.equals() <sage.matroids.matroid.Matroid.equals>`,
            :meth:`M.is_field_isomorphism() <LinearMatroid.is_field_isomorphism>`,
            :meth:`M.is_field_isomorphic() <LinearMatroid.is_field_isomorphic>`

        EXAMPLES:

        A :class:`BinaryMatroid` and
        :class:`LinearMatroid` use different
        representations of the matroid internally, so `` == ``
        yields ``False``, even if the matroids are equal::

            sage: from sage.matroids.advanced import *
            sage: M = matroids.catalog.Fano()
            sage: M1 = LinearMatroid(Matrix(M), groundset=M.groundset_list())
            sage: M2 = Matroid(groundset='abcdefg',
            ....:              reduced_matrix=[[0, 1, 1, 1],
            ....:                              [1, 0, 1, 1],
            ....:                              [1, 1, 0, 1]], field=GF(2))
            sage: M.equals(M1)
            True
            sage: M.equals(M2)
            True
            sage: M.is_field_equivalent(M1)
            True
            sage: M.is_field_equivalent(M2)
            True
            sage: M == M1
            False
            sage: M == M2
            True

        ``LinearMatroid`` instances ``M`` and ``N`` satisfy ``M == N`` if the
        representations are equivalent up to row operations and column
        scaling::

            sage: M1 = Matroid(groundset='abcd',
            ....:          matrix=Matrix(GF(7), [[1, 0, 1, 1], [0, 1, 1, 2]]))
            sage: M2 = Matroid(groundset='abcd',
            ....:          matrix=Matrix(GF(7), [[1, 0, 1, 1], [0, 1, 1, 3]]))
            sage: M3 = Matroid(groundset='abcd',
            ....:          matrix=Matrix(GF(7), [[2, 6, 1, 0], [6, 1, 0, 1]]))
            sage: M1.equals(M2)
            True
            sage: M1.equals(M3)
            True
            sage: M1 == M2
            False
            sage: M1 == M3
            True
            sage: M1.is_field_equivalent(M2)
            False
            sage: M1.is_field_equivalent(M3)
            True
            sage: M1.is_field_equivalent(M1)
            True"""
    @overload
    def is_field_equivalent(self, M2) -> Any:
        """LinearMatroid.is_field_equivalent(self, other)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 917)

        Test for matroid representation equality.

        Two linear matroids `M` and `N` with representation matrices `A` and
        `B` are *field equivalent* if they have the same groundset, and the
        identity map between the groundsets is an isomorphism between the
        representations `A` and `B`. That is, one can be turned into the other
        using only row operations and column scaling.

        INPUT:

        - ``other`` -- matroid

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.equals() <sage.matroids.matroid.Matroid.equals>`,
            :meth:`M.is_field_isomorphism() <LinearMatroid.is_field_isomorphism>`,
            :meth:`M.is_field_isomorphic() <LinearMatroid.is_field_isomorphic>`

        EXAMPLES:

        A :class:`BinaryMatroid` and
        :class:`LinearMatroid` use different
        representations of the matroid internally, so `` == ``
        yields ``False``, even if the matroids are equal::

            sage: from sage.matroids.advanced import *
            sage: M = matroids.catalog.Fano()
            sage: M1 = LinearMatroid(Matrix(M), groundset=M.groundset_list())
            sage: M2 = Matroid(groundset='abcdefg',
            ....:              reduced_matrix=[[0, 1, 1, 1],
            ....:                              [1, 0, 1, 1],
            ....:                              [1, 1, 0, 1]], field=GF(2))
            sage: M.equals(M1)
            True
            sage: M.equals(M2)
            True
            sage: M.is_field_equivalent(M1)
            True
            sage: M.is_field_equivalent(M2)
            True
            sage: M == M1
            False
            sage: M == M2
            True

        ``LinearMatroid`` instances ``M`` and ``N`` satisfy ``M == N`` if the
        representations are equivalent up to row operations and column
        scaling::

            sage: M1 = Matroid(groundset='abcd',
            ....:          matrix=Matrix(GF(7), [[1, 0, 1, 1], [0, 1, 1, 2]]))
            sage: M2 = Matroid(groundset='abcd',
            ....:          matrix=Matrix(GF(7), [[1, 0, 1, 1], [0, 1, 1, 3]]))
            sage: M3 = Matroid(groundset='abcd',
            ....:          matrix=Matrix(GF(7), [[2, 6, 1, 0], [6, 1, 0, 1]]))
            sage: M1.equals(M2)
            True
            sage: M1.equals(M3)
            True
            sage: M1 == M2
            False
            sage: M1 == M3
            True
            sage: M1.is_field_equivalent(M2)
            False
            sage: M1.is_field_equivalent(M3)
            True
            sage: M1.is_field_equivalent(M1)
            True"""
    @overload
    def is_field_equivalent(self, M2) -> Any:
        """LinearMatroid.is_field_equivalent(self, other)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 917)

        Test for matroid representation equality.

        Two linear matroids `M` and `N` with representation matrices `A` and
        `B` are *field equivalent* if they have the same groundset, and the
        identity map between the groundsets is an isomorphism between the
        representations `A` and `B`. That is, one can be turned into the other
        using only row operations and column scaling.

        INPUT:

        - ``other`` -- matroid

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.equals() <sage.matroids.matroid.Matroid.equals>`,
            :meth:`M.is_field_isomorphism() <LinearMatroid.is_field_isomorphism>`,
            :meth:`M.is_field_isomorphic() <LinearMatroid.is_field_isomorphic>`

        EXAMPLES:

        A :class:`BinaryMatroid` and
        :class:`LinearMatroid` use different
        representations of the matroid internally, so `` == ``
        yields ``False``, even if the matroids are equal::

            sage: from sage.matroids.advanced import *
            sage: M = matroids.catalog.Fano()
            sage: M1 = LinearMatroid(Matrix(M), groundset=M.groundset_list())
            sage: M2 = Matroid(groundset='abcdefg',
            ....:              reduced_matrix=[[0, 1, 1, 1],
            ....:                              [1, 0, 1, 1],
            ....:                              [1, 1, 0, 1]], field=GF(2))
            sage: M.equals(M1)
            True
            sage: M.equals(M2)
            True
            sage: M.is_field_equivalent(M1)
            True
            sage: M.is_field_equivalent(M2)
            True
            sage: M == M1
            False
            sage: M == M2
            True

        ``LinearMatroid`` instances ``M`` and ``N`` satisfy ``M == N`` if the
        representations are equivalent up to row operations and column
        scaling::

            sage: M1 = Matroid(groundset='abcd',
            ....:          matrix=Matrix(GF(7), [[1, 0, 1, 1], [0, 1, 1, 2]]))
            sage: M2 = Matroid(groundset='abcd',
            ....:          matrix=Matrix(GF(7), [[1, 0, 1, 1], [0, 1, 1, 3]]))
            sage: M3 = Matroid(groundset='abcd',
            ....:          matrix=Matrix(GF(7), [[2, 6, 1, 0], [6, 1, 0, 1]]))
            sage: M1.equals(M2)
            True
            sage: M1.equals(M3)
            True
            sage: M1 == M2
            False
            sage: M1 == M3
            True
            sage: M1.is_field_equivalent(M2)
            False
            sage: M1.is_field_equivalent(M3)
            True
            sage: M1.is_field_equivalent(M1)
            True"""
    @overload
    def is_field_equivalent(self, M3) -> Any:
        """LinearMatroid.is_field_equivalent(self, other)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 917)

        Test for matroid representation equality.

        Two linear matroids `M` and `N` with representation matrices `A` and
        `B` are *field equivalent* if they have the same groundset, and the
        identity map between the groundsets is an isomorphism between the
        representations `A` and `B`. That is, one can be turned into the other
        using only row operations and column scaling.

        INPUT:

        - ``other`` -- matroid

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.equals() <sage.matroids.matroid.Matroid.equals>`,
            :meth:`M.is_field_isomorphism() <LinearMatroid.is_field_isomorphism>`,
            :meth:`M.is_field_isomorphic() <LinearMatroid.is_field_isomorphic>`

        EXAMPLES:

        A :class:`BinaryMatroid` and
        :class:`LinearMatroid` use different
        representations of the matroid internally, so `` == ``
        yields ``False``, even if the matroids are equal::

            sage: from sage.matroids.advanced import *
            sage: M = matroids.catalog.Fano()
            sage: M1 = LinearMatroid(Matrix(M), groundset=M.groundset_list())
            sage: M2 = Matroid(groundset='abcdefg',
            ....:              reduced_matrix=[[0, 1, 1, 1],
            ....:                              [1, 0, 1, 1],
            ....:                              [1, 1, 0, 1]], field=GF(2))
            sage: M.equals(M1)
            True
            sage: M.equals(M2)
            True
            sage: M.is_field_equivalent(M1)
            True
            sage: M.is_field_equivalent(M2)
            True
            sage: M == M1
            False
            sage: M == M2
            True

        ``LinearMatroid`` instances ``M`` and ``N`` satisfy ``M == N`` if the
        representations are equivalent up to row operations and column
        scaling::

            sage: M1 = Matroid(groundset='abcd',
            ....:          matrix=Matrix(GF(7), [[1, 0, 1, 1], [0, 1, 1, 2]]))
            sage: M2 = Matroid(groundset='abcd',
            ....:          matrix=Matrix(GF(7), [[1, 0, 1, 1], [0, 1, 1, 3]]))
            sage: M3 = Matroid(groundset='abcd',
            ....:          matrix=Matrix(GF(7), [[2, 6, 1, 0], [6, 1, 0, 1]]))
            sage: M1.equals(M2)
            True
            sage: M1.equals(M3)
            True
            sage: M1 == M2
            False
            sage: M1 == M3
            True
            sage: M1.is_field_equivalent(M2)
            False
            sage: M1.is_field_equivalent(M3)
            True
            sage: M1.is_field_equivalent(M1)
            True"""
    @overload
    def is_field_equivalent(self, M1) -> Any:
        """LinearMatroid.is_field_equivalent(self, other)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 917)

        Test for matroid representation equality.

        Two linear matroids `M` and `N` with representation matrices `A` and
        `B` are *field equivalent* if they have the same groundset, and the
        identity map between the groundsets is an isomorphism between the
        representations `A` and `B`. That is, one can be turned into the other
        using only row operations and column scaling.

        INPUT:

        - ``other`` -- matroid

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.equals() <sage.matroids.matroid.Matroid.equals>`,
            :meth:`M.is_field_isomorphism() <LinearMatroid.is_field_isomorphism>`,
            :meth:`M.is_field_isomorphic() <LinearMatroid.is_field_isomorphic>`

        EXAMPLES:

        A :class:`BinaryMatroid` and
        :class:`LinearMatroid` use different
        representations of the matroid internally, so `` == ``
        yields ``False``, even if the matroids are equal::

            sage: from sage.matroids.advanced import *
            sage: M = matroids.catalog.Fano()
            sage: M1 = LinearMatroid(Matrix(M), groundset=M.groundset_list())
            sage: M2 = Matroid(groundset='abcdefg',
            ....:              reduced_matrix=[[0, 1, 1, 1],
            ....:                              [1, 0, 1, 1],
            ....:                              [1, 1, 0, 1]], field=GF(2))
            sage: M.equals(M1)
            True
            sage: M.equals(M2)
            True
            sage: M.is_field_equivalent(M1)
            True
            sage: M.is_field_equivalent(M2)
            True
            sage: M == M1
            False
            sage: M == M2
            True

        ``LinearMatroid`` instances ``M`` and ``N`` satisfy ``M == N`` if the
        representations are equivalent up to row operations and column
        scaling::

            sage: M1 = Matroid(groundset='abcd',
            ....:          matrix=Matrix(GF(7), [[1, 0, 1, 1], [0, 1, 1, 2]]))
            sage: M2 = Matroid(groundset='abcd',
            ....:          matrix=Matrix(GF(7), [[1, 0, 1, 1], [0, 1, 1, 3]]))
            sage: M3 = Matroid(groundset='abcd',
            ....:          matrix=Matrix(GF(7), [[2, 6, 1, 0], [6, 1, 0, 1]]))
            sage: M1.equals(M2)
            True
            sage: M1.equals(M3)
            True
            sage: M1 == M2
            False
            sage: M1 == M3
            True
            sage: M1.is_field_equivalent(M2)
            False
            sage: M1.is_field_equivalent(M3)
            True
            sage: M1.is_field_equivalent(M1)
            True"""
    @overload
    def is_field_isomorphic(self, other) -> Any:
        """LinearMatroid.is_field_isomorphic(self, other)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 1131)

        Test isomorphism between matroid representations.

        Two represented matroids are *field isomorphic* if there is a
        bijection between their groundsets that induces a field equivalence
        between their representation matrices: the matrices are equal up to
        row operations and column scaling. This implies that the matroids are
        isomorphic, but the converse is false: two isomorphic matroids can be
        represented by matrices that are not field equivalent.

        INPUT:

        - ``other`` -- matroid

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.is_isomorphic() <sage.matroids.matroid.Matroid.is_isomorphic>`,
            :meth:`M.is_field_isomorphism() <LinearMatroid.is_field_isomorphism>`,
            :meth:`M.is_field_equivalent() <LinearMatroid.is_field_equivalent>`

        EXAMPLES::

            sage: M1 = matroids.Wheel(3)
            sage: M2 = Matroid(graphs.CompleteGraph(4), regular=True)                   # needs sage.graphs
            sage: M1.is_field_isomorphic(M2)                                            # needs sage.graphs
            True
            sage: M3 = Matroid(bases=M1.bases())
            sage: M1.is_field_isomorphic(M3)
            Traceback (most recent call last):
            ...
            AttributeError: 'sage.matroids.basis_matroid.BasisMatroid' object
            has no attribute 'base_ring'...
            sage: from sage.matroids.advanced import *
            sage: M4 = BinaryMatroid(Matrix(M1))
            sage: M5 = LinearMatroid(reduced_matrix=Matrix(GF(2), [[-1, 0, 1],
            ....:                                    [1, -1, 0], [0, 1, -1]]))
            sage: M4.is_field_isomorphic(M5)
            True

            sage: M1 = Matroid(groundset=[0, 1, 2, 3], matrix=Matrix(GF(7),
            ....:                               [[1, 0, 1, 1], [0, 1, 1, 2]]))
            sage: M2 = Matroid(groundset=[0, 1, 2, 3], matrix=Matrix(GF(7),
            ....:                               [[1, 0, 1, 1], [0, 1, 2, 1]]))
            sage: M1.is_field_isomorphic(M2)
            True
            sage: M1.is_field_equivalent(M2)
            False"""
    @overload
    def is_field_isomorphic(self, M2) -> Any:
        """LinearMatroid.is_field_isomorphic(self, other)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 1131)

        Test isomorphism between matroid representations.

        Two represented matroids are *field isomorphic* if there is a
        bijection between their groundsets that induces a field equivalence
        between their representation matrices: the matrices are equal up to
        row operations and column scaling. This implies that the matroids are
        isomorphic, but the converse is false: two isomorphic matroids can be
        represented by matrices that are not field equivalent.

        INPUT:

        - ``other`` -- matroid

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.is_isomorphic() <sage.matroids.matroid.Matroid.is_isomorphic>`,
            :meth:`M.is_field_isomorphism() <LinearMatroid.is_field_isomorphism>`,
            :meth:`M.is_field_equivalent() <LinearMatroid.is_field_equivalent>`

        EXAMPLES::

            sage: M1 = matroids.Wheel(3)
            sage: M2 = Matroid(graphs.CompleteGraph(4), regular=True)                   # needs sage.graphs
            sage: M1.is_field_isomorphic(M2)                                            # needs sage.graphs
            True
            sage: M3 = Matroid(bases=M1.bases())
            sage: M1.is_field_isomorphic(M3)
            Traceback (most recent call last):
            ...
            AttributeError: 'sage.matroids.basis_matroid.BasisMatroid' object
            has no attribute 'base_ring'...
            sage: from sage.matroids.advanced import *
            sage: M4 = BinaryMatroid(Matrix(M1))
            sage: M5 = LinearMatroid(reduced_matrix=Matrix(GF(2), [[-1, 0, 1],
            ....:                                    [1, -1, 0], [0, 1, -1]]))
            sage: M4.is_field_isomorphic(M5)
            True

            sage: M1 = Matroid(groundset=[0, 1, 2, 3], matrix=Matrix(GF(7),
            ....:                               [[1, 0, 1, 1], [0, 1, 1, 2]]))
            sage: M2 = Matroid(groundset=[0, 1, 2, 3], matrix=Matrix(GF(7),
            ....:                               [[1, 0, 1, 1], [0, 1, 2, 1]]))
            sage: M1.is_field_isomorphic(M2)
            True
            sage: M1.is_field_equivalent(M2)
            False"""
    @overload
    def is_field_isomorphic(self, M3) -> Any:
        """LinearMatroid.is_field_isomorphic(self, other)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 1131)

        Test isomorphism between matroid representations.

        Two represented matroids are *field isomorphic* if there is a
        bijection between their groundsets that induces a field equivalence
        between their representation matrices: the matrices are equal up to
        row operations and column scaling. This implies that the matroids are
        isomorphic, but the converse is false: two isomorphic matroids can be
        represented by matrices that are not field equivalent.

        INPUT:

        - ``other`` -- matroid

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.is_isomorphic() <sage.matroids.matroid.Matroid.is_isomorphic>`,
            :meth:`M.is_field_isomorphism() <LinearMatroid.is_field_isomorphism>`,
            :meth:`M.is_field_equivalent() <LinearMatroid.is_field_equivalent>`

        EXAMPLES::

            sage: M1 = matroids.Wheel(3)
            sage: M2 = Matroid(graphs.CompleteGraph(4), regular=True)                   # needs sage.graphs
            sage: M1.is_field_isomorphic(M2)                                            # needs sage.graphs
            True
            sage: M3 = Matroid(bases=M1.bases())
            sage: M1.is_field_isomorphic(M3)
            Traceback (most recent call last):
            ...
            AttributeError: 'sage.matroids.basis_matroid.BasisMatroid' object
            has no attribute 'base_ring'...
            sage: from sage.matroids.advanced import *
            sage: M4 = BinaryMatroid(Matrix(M1))
            sage: M5 = LinearMatroid(reduced_matrix=Matrix(GF(2), [[-1, 0, 1],
            ....:                                    [1, -1, 0], [0, 1, -1]]))
            sage: M4.is_field_isomorphic(M5)
            True

            sage: M1 = Matroid(groundset=[0, 1, 2, 3], matrix=Matrix(GF(7),
            ....:                               [[1, 0, 1, 1], [0, 1, 1, 2]]))
            sage: M2 = Matroid(groundset=[0, 1, 2, 3], matrix=Matrix(GF(7),
            ....:                               [[1, 0, 1, 1], [0, 1, 2, 1]]))
            sage: M1.is_field_isomorphic(M2)
            True
            sage: M1.is_field_equivalent(M2)
            False"""
    @overload
    def is_field_isomorphic(self, M5) -> Any:
        """LinearMatroid.is_field_isomorphic(self, other)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 1131)

        Test isomorphism between matroid representations.

        Two represented matroids are *field isomorphic* if there is a
        bijection between their groundsets that induces a field equivalence
        between their representation matrices: the matrices are equal up to
        row operations and column scaling. This implies that the matroids are
        isomorphic, but the converse is false: two isomorphic matroids can be
        represented by matrices that are not field equivalent.

        INPUT:

        - ``other`` -- matroid

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.is_isomorphic() <sage.matroids.matroid.Matroid.is_isomorphic>`,
            :meth:`M.is_field_isomorphism() <LinearMatroid.is_field_isomorphism>`,
            :meth:`M.is_field_equivalent() <LinearMatroid.is_field_equivalent>`

        EXAMPLES::

            sage: M1 = matroids.Wheel(3)
            sage: M2 = Matroid(graphs.CompleteGraph(4), regular=True)                   # needs sage.graphs
            sage: M1.is_field_isomorphic(M2)                                            # needs sage.graphs
            True
            sage: M3 = Matroid(bases=M1.bases())
            sage: M1.is_field_isomorphic(M3)
            Traceback (most recent call last):
            ...
            AttributeError: 'sage.matroids.basis_matroid.BasisMatroid' object
            has no attribute 'base_ring'...
            sage: from sage.matroids.advanced import *
            sage: M4 = BinaryMatroid(Matrix(M1))
            sage: M5 = LinearMatroid(reduced_matrix=Matrix(GF(2), [[-1, 0, 1],
            ....:                                    [1, -1, 0], [0, 1, -1]]))
            sage: M4.is_field_isomorphic(M5)
            True

            sage: M1 = Matroid(groundset=[0, 1, 2, 3], matrix=Matrix(GF(7),
            ....:                               [[1, 0, 1, 1], [0, 1, 1, 2]]))
            sage: M2 = Matroid(groundset=[0, 1, 2, 3], matrix=Matrix(GF(7),
            ....:                               [[1, 0, 1, 1], [0, 1, 2, 1]]))
            sage: M1.is_field_isomorphic(M2)
            True
            sage: M1.is_field_equivalent(M2)
            False"""
    @overload
    def is_field_isomorphic(self, M2) -> Any:
        """LinearMatroid.is_field_isomorphic(self, other)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 1131)

        Test isomorphism between matroid representations.

        Two represented matroids are *field isomorphic* if there is a
        bijection between their groundsets that induces a field equivalence
        between their representation matrices: the matrices are equal up to
        row operations and column scaling. This implies that the matroids are
        isomorphic, but the converse is false: two isomorphic matroids can be
        represented by matrices that are not field equivalent.

        INPUT:

        - ``other`` -- matroid

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.is_isomorphic() <sage.matroids.matroid.Matroid.is_isomorphic>`,
            :meth:`M.is_field_isomorphism() <LinearMatroid.is_field_isomorphism>`,
            :meth:`M.is_field_equivalent() <LinearMatroid.is_field_equivalent>`

        EXAMPLES::

            sage: M1 = matroids.Wheel(3)
            sage: M2 = Matroid(graphs.CompleteGraph(4), regular=True)                   # needs sage.graphs
            sage: M1.is_field_isomorphic(M2)                                            # needs sage.graphs
            True
            sage: M3 = Matroid(bases=M1.bases())
            sage: M1.is_field_isomorphic(M3)
            Traceback (most recent call last):
            ...
            AttributeError: 'sage.matroids.basis_matroid.BasisMatroid' object
            has no attribute 'base_ring'...
            sage: from sage.matroids.advanced import *
            sage: M4 = BinaryMatroid(Matrix(M1))
            sage: M5 = LinearMatroid(reduced_matrix=Matrix(GF(2), [[-1, 0, 1],
            ....:                                    [1, -1, 0], [0, 1, -1]]))
            sage: M4.is_field_isomorphic(M5)
            True

            sage: M1 = Matroid(groundset=[0, 1, 2, 3], matrix=Matrix(GF(7),
            ....:                               [[1, 0, 1, 1], [0, 1, 1, 2]]))
            sage: M2 = Matroid(groundset=[0, 1, 2, 3], matrix=Matrix(GF(7),
            ....:                               [[1, 0, 1, 1], [0, 1, 2, 1]]))
            sage: M1.is_field_isomorphic(M2)
            True
            sage: M1.is_field_equivalent(M2)
            False"""
    @overload
    def is_field_isomorphism(self, other, morphism) -> Any:
        """LinearMatroid.is_field_isomorphism(self, other, morphism)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 1002)

        Test if a provided morphism induces a bijection between represented
        matroids.

        Two represented matroids are *field isomorphic* if the bijection
        ``morphism`` between them induces a field equivalence between their
        representation matrices: the matrices are equal up to row operations
        and column scaling. This implies that the matroids are isomorphic, but
        the converse is false: two isomorphic matroids can be represented by
        matrices that are not field equivalent.

        INPUT:

        - ``other`` -- matroid
        - ``morphism`` -- a map from the groundset of ``self`` to the
          groundset of ``other``. See documentation of the
          :meth:`M.is_isomorphism() <sage.matroids.matroid.Matroid.is_isomorphism>`
          method for more on what is accepted as input.

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.is_isomorphism() <sage.matroids.matroid.Matroid.is_isomorphism>`,
            :meth:`M.is_field_equivalent() <LinearMatroid.is_field_equivalent>`,
            :meth:`M.is_field_isomorphic() <LinearMatroid.is_field_isomorphic>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: N = matroids.catalog.NonFano()
            sage: N.is_field_isomorphism(M, {e:e for e in M.groundset()})
            False

            sage: from sage.matroids.advanced import *
            sage: M = matroids.catalog.Fano().delete(['g'])
            sage: N = LinearMatroid(reduced_matrix=Matrix(GF(2),
            ....:                       [[-1, 0, 1], [1, -1, 0], [0, 1, -1]]))
            sage: morphism = {'a':0, 'b':1, 'c': 2, 'd':4, 'e':5, 'f':3}
            sage: M.is_field_isomorphism(N, morphism)
            True

            sage: M1 = Matroid(groundset=[0, 1, 2, 3], matrix=Matrix(GF(7),
            ....:                               [[1, 0, 1, 1], [0, 1, 1, 2]]))
            sage: M2 = Matroid(groundset=[0, 1, 2, 3], matrix=Matrix(GF(7),
            ....:                               [[1, 0, 1, 1], [0, 1, 2, 1]]))
            sage: mf1 = {0:0, 1:1, 2:2, 3:3}
            sage: mf2 = {0:0, 1:1, 2:3, 3:2}
            sage: M1.is_field_isomorphism(M2, mf1)
            False
            sage: M1.is_field_isomorphism(M2, mf2)
            True"""
    @overload
    def is_field_isomorphism(self, N, morphism) -> Any:
        """LinearMatroid.is_field_isomorphism(self, other, morphism)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 1002)

        Test if a provided morphism induces a bijection between represented
        matroids.

        Two represented matroids are *field isomorphic* if the bijection
        ``morphism`` between them induces a field equivalence between their
        representation matrices: the matrices are equal up to row operations
        and column scaling. This implies that the matroids are isomorphic, but
        the converse is false: two isomorphic matroids can be represented by
        matrices that are not field equivalent.

        INPUT:

        - ``other`` -- matroid
        - ``morphism`` -- a map from the groundset of ``self`` to the
          groundset of ``other``. See documentation of the
          :meth:`M.is_isomorphism() <sage.matroids.matroid.Matroid.is_isomorphism>`
          method for more on what is accepted as input.

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.is_isomorphism() <sage.matroids.matroid.Matroid.is_isomorphism>`,
            :meth:`M.is_field_equivalent() <LinearMatroid.is_field_equivalent>`,
            :meth:`M.is_field_isomorphic() <LinearMatroid.is_field_isomorphic>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: N = matroids.catalog.NonFano()
            sage: N.is_field_isomorphism(M, {e:e for e in M.groundset()})
            False

            sage: from sage.matroids.advanced import *
            sage: M = matroids.catalog.Fano().delete(['g'])
            sage: N = LinearMatroid(reduced_matrix=Matrix(GF(2),
            ....:                       [[-1, 0, 1], [1, -1, 0], [0, 1, -1]]))
            sage: morphism = {'a':0, 'b':1, 'c': 2, 'd':4, 'e':5, 'f':3}
            sage: M.is_field_isomorphism(N, morphism)
            True

            sage: M1 = Matroid(groundset=[0, 1, 2, 3], matrix=Matrix(GF(7),
            ....:                               [[1, 0, 1, 1], [0, 1, 1, 2]]))
            sage: M2 = Matroid(groundset=[0, 1, 2, 3], matrix=Matrix(GF(7),
            ....:                               [[1, 0, 1, 1], [0, 1, 2, 1]]))
            sage: mf1 = {0:0, 1:1, 2:2, 3:3}
            sage: mf2 = {0:0, 1:1, 2:3, 3:2}
            sage: M1.is_field_isomorphism(M2, mf1)
            False
            sage: M1.is_field_isomorphism(M2, mf2)
            True"""
    @overload
    def is_field_isomorphism(self, M2, mf1) -> Any:
        """LinearMatroid.is_field_isomorphism(self, other, morphism)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 1002)

        Test if a provided morphism induces a bijection between represented
        matroids.

        Two represented matroids are *field isomorphic* if the bijection
        ``morphism`` between them induces a field equivalence between their
        representation matrices: the matrices are equal up to row operations
        and column scaling. This implies that the matroids are isomorphic, but
        the converse is false: two isomorphic matroids can be represented by
        matrices that are not field equivalent.

        INPUT:

        - ``other`` -- matroid
        - ``morphism`` -- a map from the groundset of ``self`` to the
          groundset of ``other``. See documentation of the
          :meth:`M.is_isomorphism() <sage.matroids.matroid.Matroid.is_isomorphism>`
          method for more on what is accepted as input.

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.is_isomorphism() <sage.matroids.matroid.Matroid.is_isomorphism>`,
            :meth:`M.is_field_equivalent() <LinearMatroid.is_field_equivalent>`,
            :meth:`M.is_field_isomorphic() <LinearMatroid.is_field_isomorphic>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: N = matroids.catalog.NonFano()
            sage: N.is_field_isomorphism(M, {e:e for e in M.groundset()})
            False

            sage: from sage.matroids.advanced import *
            sage: M = matroids.catalog.Fano().delete(['g'])
            sage: N = LinearMatroid(reduced_matrix=Matrix(GF(2),
            ....:                       [[-1, 0, 1], [1, -1, 0], [0, 1, -1]]))
            sage: morphism = {'a':0, 'b':1, 'c': 2, 'd':4, 'e':5, 'f':3}
            sage: M.is_field_isomorphism(N, morphism)
            True

            sage: M1 = Matroid(groundset=[0, 1, 2, 3], matrix=Matrix(GF(7),
            ....:                               [[1, 0, 1, 1], [0, 1, 1, 2]]))
            sage: M2 = Matroid(groundset=[0, 1, 2, 3], matrix=Matrix(GF(7),
            ....:                               [[1, 0, 1, 1], [0, 1, 2, 1]]))
            sage: mf1 = {0:0, 1:1, 2:2, 3:3}
            sage: mf2 = {0:0, 1:1, 2:3, 3:2}
            sage: M1.is_field_isomorphism(M2, mf1)
            False
            sage: M1.is_field_isomorphism(M2, mf2)
            True"""
    @overload
    def is_field_isomorphism(self, M2, mf2) -> Any:
        """LinearMatroid.is_field_isomorphism(self, other, morphism)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 1002)

        Test if a provided morphism induces a bijection between represented
        matroids.

        Two represented matroids are *field isomorphic* if the bijection
        ``morphism`` between them induces a field equivalence between their
        representation matrices: the matrices are equal up to row operations
        and column scaling. This implies that the matroids are isomorphic, but
        the converse is false: two isomorphic matroids can be represented by
        matrices that are not field equivalent.

        INPUT:

        - ``other`` -- matroid
        - ``morphism`` -- a map from the groundset of ``self`` to the
          groundset of ``other``. See documentation of the
          :meth:`M.is_isomorphism() <sage.matroids.matroid.Matroid.is_isomorphism>`
          method for more on what is accepted as input.

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.is_isomorphism() <sage.matroids.matroid.Matroid.is_isomorphism>`,
            :meth:`M.is_field_equivalent() <LinearMatroid.is_field_equivalent>`,
            :meth:`M.is_field_isomorphic() <LinearMatroid.is_field_isomorphic>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: N = matroids.catalog.NonFano()
            sage: N.is_field_isomorphism(M, {e:e for e in M.groundset()})
            False

            sage: from sage.matroids.advanced import *
            sage: M = matroids.catalog.Fano().delete(['g'])
            sage: N = LinearMatroid(reduced_matrix=Matrix(GF(2),
            ....:                       [[-1, 0, 1], [1, -1, 0], [0, 1, -1]]))
            sage: morphism = {'a':0, 'b':1, 'c': 2, 'd':4, 'e':5, 'f':3}
            sage: M.is_field_isomorphism(N, morphism)
            True

            sage: M1 = Matroid(groundset=[0, 1, 2, 3], matrix=Matrix(GF(7),
            ....:                               [[1, 0, 1, 1], [0, 1, 1, 2]]))
            sage: M2 = Matroid(groundset=[0, 1, 2, 3], matrix=Matrix(GF(7),
            ....:                               [[1, 0, 1, 1], [0, 1, 2, 1]]))
            sage: mf1 = {0:0, 1:1, 2:2, 3:3}
            sage: mf2 = {0:0, 1:1, 2:3, 3:2}
            sage: M1.is_field_isomorphism(M2, mf1)
            False
            sage: M1.is_field_isomorphism(M2, mf2)
            True"""
    @overload
    def is_valid(self, certificate=...) -> Any:
        """LinearMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 2617)

        Test if the data represent an actual matroid.

        Since this matroid is linear, we test the representation matrix.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, or (boolean, dictionary)

        The boolean output value is:

        - ``True`` if the matrix is over a field.
        - ``True`` if the matrix is over a ring and all cross ratios are
          invertible.
        - ``False`` otherwise.

        .. NOTE::

            This function does NOT test if the cross ratios are contained in
            the appropriate set of fundamentals. To that end, use

            ``M.cross_ratios().issubset(F)``

            where ``F`` is the set of fundamentals.

        .. SEEALSO::

            :meth:`M.cross_ratios() <LinearMatroid.cross_ratios>`

        EXAMPLES::

            sage: M = Matroid(ring=QQ, reduced_matrix=Matrix(ZZ,
            ....:                          [[1, 0, 1], [1, 1, 0], [0, 1, 1]]))
            sage: M.is_valid()
            True
            sage: from sage.matroids.advanced import *  # LinearMatroid
            sage: M = LinearMatroid(ring=ZZ, reduced_matrix=Matrix(ZZ,
            ....:                          [[1, 0, 1], [1, 1, 0], [0, 1, 1]]))
            sage: M.is_valid(certificate=True)
            (False, {'error': 'not all cross ratios are invertible'})"""
    @overload
    def is_valid(self) -> Any:
        """LinearMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 2617)

        Test if the data represent an actual matroid.

        Since this matroid is linear, we test the representation matrix.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, or (boolean, dictionary)

        The boolean output value is:

        - ``True`` if the matrix is over a field.
        - ``True`` if the matrix is over a ring and all cross ratios are
          invertible.
        - ``False`` otherwise.

        .. NOTE::

            This function does NOT test if the cross ratios are contained in
            the appropriate set of fundamentals. To that end, use

            ``M.cross_ratios().issubset(F)``

            where ``F`` is the set of fundamentals.

        .. SEEALSO::

            :meth:`M.cross_ratios() <LinearMatroid.cross_ratios>`

        EXAMPLES::

            sage: M = Matroid(ring=QQ, reduced_matrix=Matrix(ZZ,
            ....:                          [[1, 0, 1], [1, 1, 0], [0, 1, 1]]))
            sage: M.is_valid()
            True
            sage: from sage.matroids.advanced import *  # LinearMatroid
            sage: M = LinearMatroid(ring=ZZ, reduced_matrix=Matrix(ZZ,
            ....:                          [[1, 0, 1], [1, 1, 0], [0, 1, 1]]))
            sage: M.is_valid(certificate=True)
            (False, {'error': 'not all cross ratios are invertible'})"""
    @overload
    def is_valid(self, certificate=...) -> Any:
        """LinearMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 2617)

        Test if the data represent an actual matroid.

        Since this matroid is linear, we test the representation matrix.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, or (boolean, dictionary)

        The boolean output value is:

        - ``True`` if the matrix is over a field.
        - ``True`` if the matrix is over a ring and all cross ratios are
          invertible.
        - ``False`` otherwise.

        .. NOTE::

            This function does NOT test if the cross ratios are contained in
            the appropriate set of fundamentals. To that end, use

            ``M.cross_ratios().issubset(F)``

            where ``F`` is the set of fundamentals.

        .. SEEALSO::

            :meth:`M.cross_ratios() <LinearMatroid.cross_ratios>`

        EXAMPLES::

            sage: M = Matroid(ring=QQ, reduced_matrix=Matrix(ZZ,
            ....:                          [[1, 0, 1], [1, 1, 0], [0, 1, 1]]))
            sage: M.is_valid()
            True
            sage: from sage.matroids.advanced import *  # LinearMatroid
            sage: M = LinearMatroid(ring=ZZ, reduced_matrix=Matrix(ZZ,
            ....:                          [[1, 0, 1], [1, 1, 0], [0, 1, 1]]))
            sage: M.is_valid(certificate=True)
            (False, {'error': 'not all cross ratios are invertible'})"""
    def linear_coextension(self, element, cochain=..., row=...) -> Any:
        """LinearMatroid.linear_coextension(self, element, cochain=None, row=None)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 1976)

        Return a linear coextension of this matroid.

        A *linear coextension* of the represented matroid `M` by element `e`
        is a matroid represented by

        .. MATH::

            \\begin{bmatrix}
                A  & 0\\\\\n                -c & 1
            \\end{bmatrix},

        where `A` is a representation matrix of `M`, `c` is a new row, and the
        last column is labeled by `e`.

        This is the dual method of
        :meth:`M.linear_extension() <LinearMatroid.linear_extension>`.

        INPUT:

        - ``element`` -- the name of the new element
        - ``row`` -- (default: ``None``) a row to be appended to
          ``self.representation()``; can be any iterable
        - ``cochain`` -- (default: ``None``) a dictionary that maps elements
          of the groundset to elements of the base ring

        OUTPUT:

        A linear matroid `N = M([A 0; -c 1])`, where `A` is a matrix such that
        the current matroid is `M[A]`, and `c` is either given by ``row``
        (relative to ``self.representation()``) or has nonzero entries given
        by ``cochain``.

        .. NOTE::

            The minus sign is to ensure this method commutes with dualizing.
            See the last example.

        .. SEEALSO::

            :meth:`M.coextension() <sage.matroids.matroid.Matroid.coextension>`,
            :meth:`M.linear_extension() <LinearMatroid.linear_extension>`,
            :meth:`M.dual() <LinearMatroid.dual>`

        EXAMPLES::

            sage: M = Matroid(ring=GF(2), matrix=[[1, 1, 0, 1, 0, 0],
            ....:                                 [1, 0, 1, 0, 1, 0],
            ....:                                 [0, 1, 1, 0, 0, 1],
            ....:                                 [0, 0, 0, 1, 1, 1]])
            sage: M.linear_coextension(6, {0:1, 5: 1}).representation()
            [1 1 0 1 0 0 0]
            [1 0 1 0 1 0 0]
            [0 1 1 0 0 1 0]
            [0 0 0 1 1 1 0]
            [1 0 0 0 0 1 1]
            sage: M.linear_coextension(6, row=[0,1,1,1,0,1]).representation()
            [1 1 0 1 0 0 0]
            [1 0 1 0 1 0 0]
            [0 1 1 0 0 1 0]
            [0 0 0 1 1 1 0]
            [0 1 1 1 0 1 1]

        Coextending commutes with dualizing::

            sage: M = matroids.catalog.NonFano()
            sage: chain = {'a': 1, 'b': -1, 'f': 1}
            sage: M1 = M.linear_coextension('x', chain)
            sage: M2 = M.dual().linear_extension('x', chain)
            sage: M1 == M2.dual()
            True"""
    @overload
    def linear_coextension_cochains(self, F=..., cosimple=..., fundamentals=...) -> Any:
        """LinearMatroid.linear_coextension_cochains(self, F=None, cosimple=False, fundamentals=None)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 2412)

        Create a list of cochains that determine the single-element
        coextensions of this linear matroid representation.

        A cochain is a dictionary, mapping elements from the groundset to
        elements of the base ring. If `A` represents the current matroid, then
        the coextension is given by `N = M([A 0; -c 1])`, with the entries of
        `c` given by the cochain. Note that the matroid does not change when
        row operations are carried out on `A`.

        INPUT:

        - ``F`` -- (default: ``self.groundset()``) a subset of the groundset

        - ``cosimple`` -- boolean (default: ``False``)

        - ``fundamentals`` -- (default: ``None``) a set elements of the base
          ring

        OUTPUT:

        A list of cochains, so each single-element coextension of this linear
        matroid representation is given by one of these cochains.

        If one or more of the above inputs is given, the list is restricted to
        chains

        - so that the support of each cochain lies in ``F``, if given
        - so that the cochain does not generate a series extension or coloop,
          if ``cosimple = True``
        - so that in the coextension generated by this cochain, the cross
          ratios are restricted to ``fundamentals``, if given.

        .. SEEALSO::

            :meth:`M.linear_coextension() <LinearMatroid.linear_coextension>`,
            :meth:`M.linear_coextensions() <LinearMatroid.linear_coextensions>`,
            :meth:`M.cross_ratios() <LinearMatroid.cross_ratios>`

        EXAMPLES::

            sage: M = Matroid(reduced_matrix=Matrix(GF(2),
            ....:                          [[1, 1, 0], [1, 0, 1], [0, 1, 1]]))
            sage: len(M.linear_coextension_cochains())
            8
            sage: len(M.linear_coextension_cochains(F=[0, 1]))
            4
            sage: len(M.linear_coextension_cochains(F=[0, 1], cosimple=True))
            0
            sage: M.linear_coextension_cochains(F=[3, 4, 5], cosimple=True)
            [{3: 1, 4: 1, 5: 1}]
            sage: N = Matroid(ring=QQ,
            ....:         reduced_matrix=[[-1, -1, 0], [1, 0, -1], [0, 1, 1]])
            sage: N.linear_coextension_cochains(F=[0, 1], cosimple=True,
            ....:                           fundamentals=set([1, -1, 1/2, 2]))
            [{0: 2, 1: 1}, {0: -1, 1: 1}, {0: 1/2, 1: 1}]"""
    @overload
    def linear_coextension_cochains(self) -> Any:
        """LinearMatroid.linear_coextension_cochains(self, F=None, cosimple=False, fundamentals=None)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 2412)

        Create a list of cochains that determine the single-element
        coextensions of this linear matroid representation.

        A cochain is a dictionary, mapping elements from the groundset to
        elements of the base ring. If `A` represents the current matroid, then
        the coextension is given by `N = M([A 0; -c 1])`, with the entries of
        `c` given by the cochain. Note that the matroid does not change when
        row operations are carried out on `A`.

        INPUT:

        - ``F`` -- (default: ``self.groundset()``) a subset of the groundset

        - ``cosimple`` -- boolean (default: ``False``)

        - ``fundamentals`` -- (default: ``None``) a set elements of the base
          ring

        OUTPUT:

        A list of cochains, so each single-element coextension of this linear
        matroid representation is given by one of these cochains.

        If one or more of the above inputs is given, the list is restricted to
        chains

        - so that the support of each cochain lies in ``F``, if given
        - so that the cochain does not generate a series extension or coloop,
          if ``cosimple = True``
        - so that in the coextension generated by this cochain, the cross
          ratios are restricted to ``fundamentals``, if given.

        .. SEEALSO::

            :meth:`M.linear_coextension() <LinearMatroid.linear_coextension>`,
            :meth:`M.linear_coextensions() <LinearMatroid.linear_coextensions>`,
            :meth:`M.cross_ratios() <LinearMatroid.cross_ratios>`

        EXAMPLES::

            sage: M = Matroid(reduced_matrix=Matrix(GF(2),
            ....:                          [[1, 1, 0], [1, 0, 1], [0, 1, 1]]))
            sage: len(M.linear_coextension_cochains())
            8
            sage: len(M.linear_coextension_cochains(F=[0, 1]))
            4
            sage: len(M.linear_coextension_cochains(F=[0, 1], cosimple=True))
            0
            sage: M.linear_coextension_cochains(F=[3, 4, 5], cosimple=True)
            [{3: 1, 4: 1, 5: 1}]
            sage: N = Matroid(ring=QQ,
            ....:         reduced_matrix=[[-1, -1, 0], [1, 0, -1], [0, 1, 1]])
            sage: N.linear_coextension_cochains(F=[0, 1], cosimple=True,
            ....:                           fundamentals=set([1, -1, 1/2, 2]))
            [{0: 2, 1: 1}, {0: -1, 1: 1}, {0: 1/2, 1: 1}]"""
    @overload
    def linear_coextension_cochains(self, F=...) -> Any:
        """LinearMatroid.linear_coextension_cochains(self, F=None, cosimple=False, fundamentals=None)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 2412)

        Create a list of cochains that determine the single-element
        coextensions of this linear matroid representation.

        A cochain is a dictionary, mapping elements from the groundset to
        elements of the base ring. If `A` represents the current matroid, then
        the coextension is given by `N = M([A 0; -c 1])`, with the entries of
        `c` given by the cochain. Note that the matroid does not change when
        row operations are carried out on `A`.

        INPUT:

        - ``F`` -- (default: ``self.groundset()``) a subset of the groundset

        - ``cosimple`` -- boolean (default: ``False``)

        - ``fundamentals`` -- (default: ``None``) a set elements of the base
          ring

        OUTPUT:

        A list of cochains, so each single-element coextension of this linear
        matroid representation is given by one of these cochains.

        If one or more of the above inputs is given, the list is restricted to
        chains

        - so that the support of each cochain lies in ``F``, if given
        - so that the cochain does not generate a series extension or coloop,
          if ``cosimple = True``
        - so that in the coextension generated by this cochain, the cross
          ratios are restricted to ``fundamentals``, if given.

        .. SEEALSO::

            :meth:`M.linear_coextension() <LinearMatroid.linear_coextension>`,
            :meth:`M.linear_coextensions() <LinearMatroid.linear_coextensions>`,
            :meth:`M.cross_ratios() <LinearMatroid.cross_ratios>`

        EXAMPLES::

            sage: M = Matroid(reduced_matrix=Matrix(GF(2),
            ....:                          [[1, 1, 0], [1, 0, 1], [0, 1, 1]]))
            sage: len(M.linear_coextension_cochains())
            8
            sage: len(M.linear_coextension_cochains(F=[0, 1]))
            4
            sage: len(M.linear_coextension_cochains(F=[0, 1], cosimple=True))
            0
            sage: M.linear_coextension_cochains(F=[3, 4, 5], cosimple=True)
            [{3: 1, 4: 1, 5: 1}]
            sage: N = Matroid(ring=QQ,
            ....:         reduced_matrix=[[-1, -1, 0], [1, 0, -1], [0, 1, 1]])
            sage: N.linear_coextension_cochains(F=[0, 1], cosimple=True,
            ....:                           fundamentals=set([1, -1, 1/2, 2]))
            [{0: 2, 1: 1}, {0: -1, 1: 1}, {0: 1/2, 1: 1}]"""
    @overload
    def linear_coextension_cochains(self, F=..., cosimple=...) -> Any:
        """LinearMatroid.linear_coextension_cochains(self, F=None, cosimple=False, fundamentals=None)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 2412)

        Create a list of cochains that determine the single-element
        coextensions of this linear matroid representation.

        A cochain is a dictionary, mapping elements from the groundset to
        elements of the base ring. If `A` represents the current matroid, then
        the coextension is given by `N = M([A 0; -c 1])`, with the entries of
        `c` given by the cochain. Note that the matroid does not change when
        row operations are carried out on `A`.

        INPUT:

        - ``F`` -- (default: ``self.groundset()``) a subset of the groundset

        - ``cosimple`` -- boolean (default: ``False``)

        - ``fundamentals`` -- (default: ``None``) a set elements of the base
          ring

        OUTPUT:

        A list of cochains, so each single-element coextension of this linear
        matroid representation is given by one of these cochains.

        If one or more of the above inputs is given, the list is restricted to
        chains

        - so that the support of each cochain lies in ``F``, if given
        - so that the cochain does not generate a series extension or coloop,
          if ``cosimple = True``
        - so that in the coextension generated by this cochain, the cross
          ratios are restricted to ``fundamentals``, if given.

        .. SEEALSO::

            :meth:`M.linear_coextension() <LinearMatroid.linear_coextension>`,
            :meth:`M.linear_coextensions() <LinearMatroid.linear_coextensions>`,
            :meth:`M.cross_ratios() <LinearMatroid.cross_ratios>`

        EXAMPLES::

            sage: M = Matroid(reduced_matrix=Matrix(GF(2),
            ....:                          [[1, 1, 0], [1, 0, 1], [0, 1, 1]]))
            sage: len(M.linear_coextension_cochains())
            8
            sage: len(M.linear_coextension_cochains(F=[0, 1]))
            4
            sage: len(M.linear_coextension_cochains(F=[0, 1], cosimple=True))
            0
            sage: M.linear_coextension_cochains(F=[3, 4, 5], cosimple=True)
            [{3: 1, 4: 1, 5: 1}]
            sage: N = Matroid(ring=QQ,
            ....:         reduced_matrix=[[-1, -1, 0], [1, 0, -1], [0, 1, 1]])
            sage: N.linear_coextension_cochains(F=[0, 1], cosimple=True,
            ....:                           fundamentals=set([1, -1, 1/2, 2]))
            [{0: 2, 1: 1}, {0: -1, 1: 1}, {0: 1/2, 1: 1}]"""
    @overload
    def linear_coextension_cochains(self, F=..., cosimple=...) -> Any:
        """LinearMatroid.linear_coextension_cochains(self, F=None, cosimple=False, fundamentals=None)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 2412)

        Create a list of cochains that determine the single-element
        coextensions of this linear matroid representation.

        A cochain is a dictionary, mapping elements from the groundset to
        elements of the base ring. If `A` represents the current matroid, then
        the coextension is given by `N = M([A 0; -c 1])`, with the entries of
        `c` given by the cochain. Note that the matroid does not change when
        row operations are carried out on `A`.

        INPUT:

        - ``F`` -- (default: ``self.groundset()``) a subset of the groundset

        - ``cosimple`` -- boolean (default: ``False``)

        - ``fundamentals`` -- (default: ``None``) a set elements of the base
          ring

        OUTPUT:

        A list of cochains, so each single-element coextension of this linear
        matroid representation is given by one of these cochains.

        If one or more of the above inputs is given, the list is restricted to
        chains

        - so that the support of each cochain lies in ``F``, if given
        - so that the cochain does not generate a series extension or coloop,
          if ``cosimple = True``
        - so that in the coextension generated by this cochain, the cross
          ratios are restricted to ``fundamentals``, if given.

        .. SEEALSO::

            :meth:`M.linear_coextension() <LinearMatroid.linear_coextension>`,
            :meth:`M.linear_coextensions() <LinearMatroid.linear_coextensions>`,
            :meth:`M.cross_ratios() <LinearMatroid.cross_ratios>`

        EXAMPLES::

            sage: M = Matroid(reduced_matrix=Matrix(GF(2),
            ....:                          [[1, 1, 0], [1, 0, 1], [0, 1, 1]]))
            sage: len(M.linear_coextension_cochains())
            8
            sage: len(M.linear_coextension_cochains(F=[0, 1]))
            4
            sage: len(M.linear_coextension_cochains(F=[0, 1], cosimple=True))
            0
            sage: M.linear_coextension_cochains(F=[3, 4, 5], cosimple=True)
            [{3: 1, 4: 1, 5: 1}]
            sage: N = Matroid(ring=QQ,
            ....:         reduced_matrix=[[-1, -1, 0], [1, 0, -1], [0, 1, 1]])
            sage: N.linear_coextension_cochains(F=[0, 1], cosimple=True,
            ....:                           fundamentals=set([1, -1, 1/2, 2]))
            [{0: 2, 1: 1}, {0: -1, 1: 1}, {0: 1/2, 1: 1}]"""
    @overload
    def linear_coextension_cochains(self, F=..., cosimple=..., 
....: fundamentals = ...) -> Any:
        """LinearMatroid.linear_coextension_cochains(self, F=None, cosimple=False, fundamentals=None)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 2412)

        Create a list of cochains that determine the single-element
        coextensions of this linear matroid representation.

        A cochain is a dictionary, mapping elements from the groundset to
        elements of the base ring. If `A` represents the current matroid, then
        the coextension is given by `N = M([A 0; -c 1])`, with the entries of
        `c` given by the cochain. Note that the matroid does not change when
        row operations are carried out on `A`.

        INPUT:

        - ``F`` -- (default: ``self.groundset()``) a subset of the groundset

        - ``cosimple`` -- boolean (default: ``False``)

        - ``fundamentals`` -- (default: ``None``) a set elements of the base
          ring

        OUTPUT:

        A list of cochains, so each single-element coextension of this linear
        matroid representation is given by one of these cochains.

        If one or more of the above inputs is given, the list is restricted to
        chains

        - so that the support of each cochain lies in ``F``, if given
        - so that the cochain does not generate a series extension or coloop,
          if ``cosimple = True``
        - so that in the coextension generated by this cochain, the cross
          ratios are restricted to ``fundamentals``, if given.

        .. SEEALSO::

            :meth:`M.linear_coextension() <LinearMatroid.linear_coextension>`,
            :meth:`M.linear_coextensions() <LinearMatroid.linear_coextensions>`,
            :meth:`M.cross_ratios() <LinearMatroid.cross_ratios>`

        EXAMPLES::

            sage: M = Matroid(reduced_matrix=Matrix(GF(2),
            ....:                          [[1, 1, 0], [1, 0, 1], [0, 1, 1]]))
            sage: len(M.linear_coextension_cochains())
            8
            sage: len(M.linear_coextension_cochains(F=[0, 1]))
            4
            sage: len(M.linear_coextension_cochains(F=[0, 1], cosimple=True))
            0
            sage: M.linear_coextension_cochains(F=[3, 4, 5], cosimple=True)
            [{3: 1, 4: 1, 5: 1}]
            sage: N = Matroid(ring=QQ,
            ....:         reduced_matrix=[[-1, -1, 0], [1, 0, -1], [0, 1, 1]])
            sage: N.linear_coextension_cochains(F=[0, 1], cosimple=True,
            ....:                           fundamentals=set([1, -1, 1/2, 2]))
            [{0: 2, 1: 1}, {0: -1, 1: 1}, {0: 1/2, 1: 1}]"""
    @overload
    def linear_coextensions(self, element=..., F=..., cosimple=..., fundamentals=...) -> Any:
        """LinearMatroid.linear_coextensions(self, element=None, F=None, cosimple=False, fundamentals=None)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 2543)

        Create a list of linear matroids represented by corank-preserving single-element
        coextensions of this linear matroid representation.

        INPUT:

        - ``element`` -- (default: ``None``) the name of the new element of
          the groundset

        - ``F`` -- (default: ``None``) a subset of the groundset

        - ``cosimple`` -- boolean (default: ``False``)

        - ``fundamentals`` -- (default: ``None``) a set elements of the base
          ring

        OUTPUT:

        A list of linear matroids represented by corank-preserving single-element
        coextensions of this linear matroid representation. In particular, the coextension
        by a loop is not generated.

        If one or more of the above inputs is given, the list is restricted to
        coextensions

        - so that the new element lies in the cospan of ``F``, if given.
        - so that the new element is no coloop and is not in series with
          another element, if ``cosimple = True``.
        - so that in the representation of the coextension, the cross ratios
          are restricted to ``fundamentals``, if given. Note that it is
          assumed that the cross ratios of the input matroid already satisfy
          this condition.

        .. SEEALSO::

            :meth:`M.linear_coextension() <LinearMatroid.linear_coextension>`,
            :meth:`M.linear_coextension_cochains() <LinearMatroid.linear_coextension_cochains>`,
            :meth:`M.cross_ratios() <LinearMatroid.cross_ratios>`

        EXAMPLES::

            sage: M = Matroid(ring=GF(2),
            ....:         reduced_matrix=[[-1, 0, 1], [1, -1, 0], [0, 1, -1]])
            sage: len(M.linear_coextensions())
            8
            sage: S = M.linear_coextensions(cosimple=True)
            sage: S
            [Binary matroid of rank 4 on 7 elements, type (3, 7)]
            sage: F7 = matroids.catalog.Fano()
            sage: S[0].is_field_isomorphic(F7.dual())
            True
            sage: M = Matroid(ring=QQ,
            ....:            reduced_matrix=[[1, 0, 1], [1, 1, 0], [0, 1, 1]])
            sage: S = M.linear_coextensions(cosimple=True,
            ....:                           fundamentals=[1, -1, 1/2, 2])
            sage: len(S)
            7
            sage: NF7 = matroids.catalog.NonFano()
            sage: any(N.is_isomorphic(NF7.dual()) for N in S)
            True
            sage: len(M.linear_coextensions(cosimple=True,
            ....:                           fundamentals=[1, -1, 1/2, 2],
            ....:                           F=[3, 4]))
            1"""
    @overload
    def linear_coextensions(self) -> Any:
        """LinearMatroid.linear_coextensions(self, element=None, F=None, cosimple=False, fundamentals=None)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 2543)

        Create a list of linear matroids represented by corank-preserving single-element
        coextensions of this linear matroid representation.

        INPUT:

        - ``element`` -- (default: ``None``) the name of the new element of
          the groundset

        - ``F`` -- (default: ``None``) a subset of the groundset

        - ``cosimple`` -- boolean (default: ``False``)

        - ``fundamentals`` -- (default: ``None``) a set elements of the base
          ring

        OUTPUT:

        A list of linear matroids represented by corank-preserving single-element
        coextensions of this linear matroid representation. In particular, the coextension
        by a loop is not generated.

        If one or more of the above inputs is given, the list is restricted to
        coextensions

        - so that the new element lies in the cospan of ``F``, if given.
        - so that the new element is no coloop and is not in series with
          another element, if ``cosimple = True``.
        - so that in the representation of the coextension, the cross ratios
          are restricted to ``fundamentals``, if given. Note that it is
          assumed that the cross ratios of the input matroid already satisfy
          this condition.

        .. SEEALSO::

            :meth:`M.linear_coextension() <LinearMatroid.linear_coextension>`,
            :meth:`M.linear_coextension_cochains() <LinearMatroid.linear_coextension_cochains>`,
            :meth:`M.cross_ratios() <LinearMatroid.cross_ratios>`

        EXAMPLES::

            sage: M = Matroid(ring=GF(2),
            ....:         reduced_matrix=[[-1, 0, 1], [1, -1, 0], [0, 1, -1]])
            sage: len(M.linear_coextensions())
            8
            sage: S = M.linear_coextensions(cosimple=True)
            sage: S
            [Binary matroid of rank 4 on 7 elements, type (3, 7)]
            sage: F7 = matroids.catalog.Fano()
            sage: S[0].is_field_isomorphic(F7.dual())
            True
            sage: M = Matroid(ring=QQ,
            ....:            reduced_matrix=[[1, 0, 1], [1, 1, 0], [0, 1, 1]])
            sage: S = M.linear_coextensions(cosimple=True,
            ....:                           fundamentals=[1, -1, 1/2, 2])
            sage: len(S)
            7
            sage: NF7 = matroids.catalog.NonFano()
            sage: any(N.is_isomorphic(NF7.dual()) for N in S)
            True
            sage: len(M.linear_coextensions(cosimple=True,
            ....:                           fundamentals=[1, -1, 1/2, 2],
            ....:                           F=[3, 4]))
            1"""
    @overload
    def linear_coextensions(self, cosimple=...) -> Any:
        """LinearMatroid.linear_coextensions(self, element=None, F=None, cosimple=False, fundamentals=None)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 2543)

        Create a list of linear matroids represented by corank-preserving single-element
        coextensions of this linear matroid representation.

        INPUT:

        - ``element`` -- (default: ``None``) the name of the new element of
          the groundset

        - ``F`` -- (default: ``None``) a subset of the groundset

        - ``cosimple`` -- boolean (default: ``False``)

        - ``fundamentals`` -- (default: ``None``) a set elements of the base
          ring

        OUTPUT:

        A list of linear matroids represented by corank-preserving single-element
        coextensions of this linear matroid representation. In particular, the coextension
        by a loop is not generated.

        If one or more of the above inputs is given, the list is restricted to
        coextensions

        - so that the new element lies in the cospan of ``F``, if given.
        - so that the new element is no coloop and is not in series with
          another element, if ``cosimple = True``.
        - so that in the representation of the coextension, the cross ratios
          are restricted to ``fundamentals``, if given. Note that it is
          assumed that the cross ratios of the input matroid already satisfy
          this condition.

        .. SEEALSO::

            :meth:`M.linear_coextension() <LinearMatroid.linear_coextension>`,
            :meth:`M.linear_coextension_cochains() <LinearMatroid.linear_coextension_cochains>`,
            :meth:`M.cross_ratios() <LinearMatroid.cross_ratios>`

        EXAMPLES::

            sage: M = Matroid(ring=GF(2),
            ....:         reduced_matrix=[[-1, 0, 1], [1, -1, 0], [0, 1, -1]])
            sage: len(M.linear_coextensions())
            8
            sage: S = M.linear_coextensions(cosimple=True)
            sage: S
            [Binary matroid of rank 4 on 7 elements, type (3, 7)]
            sage: F7 = matroids.catalog.Fano()
            sage: S[0].is_field_isomorphic(F7.dual())
            True
            sage: M = Matroid(ring=QQ,
            ....:            reduced_matrix=[[1, 0, 1], [1, 1, 0], [0, 1, 1]])
            sage: S = M.linear_coextensions(cosimple=True,
            ....:                           fundamentals=[1, -1, 1/2, 2])
            sage: len(S)
            7
            sage: NF7 = matroids.catalog.NonFano()
            sage: any(N.is_isomorphic(NF7.dual()) for N in S)
            True
            sage: len(M.linear_coextensions(cosimple=True,
            ....:                           fundamentals=[1, -1, 1/2, 2],
            ....:                           F=[3, 4]))
            1"""
    @overload
    def linear_coextensions(self, cosimple=..., 
....: fundamentals = ...) -> Any:
        """LinearMatroid.linear_coextensions(self, element=None, F=None, cosimple=False, fundamentals=None)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 2543)

        Create a list of linear matroids represented by corank-preserving single-element
        coextensions of this linear matroid representation.

        INPUT:

        - ``element`` -- (default: ``None``) the name of the new element of
          the groundset

        - ``F`` -- (default: ``None``) a subset of the groundset

        - ``cosimple`` -- boolean (default: ``False``)

        - ``fundamentals`` -- (default: ``None``) a set elements of the base
          ring

        OUTPUT:

        A list of linear matroids represented by corank-preserving single-element
        coextensions of this linear matroid representation. In particular, the coextension
        by a loop is not generated.

        If one or more of the above inputs is given, the list is restricted to
        coextensions

        - so that the new element lies in the cospan of ``F``, if given.
        - so that the new element is no coloop and is not in series with
          another element, if ``cosimple = True``.
        - so that in the representation of the coextension, the cross ratios
          are restricted to ``fundamentals``, if given. Note that it is
          assumed that the cross ratios of the input matroid already satisfy
          this condition.

        .. SEEALSO::

            :meth:`M.linear_coextension() <LinearMatroid.linear_coextension>`,
            :meth:`M.linear_coextension_cochains() <LinearMatroid.linear_coextension_cochains>`,
            :meth:`M.cross_ratios() <LinearMatroid.cross_ratios>`

        EXAMPLES::

            sage: M = Matroid(ring=GF(2),
            ....:         reduced_matrix=[[-1, 0, 1], [1, -1, 0], [0, 1, -1]])
            sage: len(M.linear_coextensions())
            8
            sage: S = M.linear_coextensions(cosimple=True)
            sage: S
            [Binary matroid of rank 4 on 7 elements, type (3, 7)]
            sage: F7 = matroids.catalog.Fano()
            sage: S[0].is_field_isomorphic(F7.dual())
            True
            sage: M = Matroid(ring=QQ,
            ....:            reduced_matrix=[[1, 0, 1], [1, 1, 0], [0, 1, 1]])
            sage: S = M.linear_coextensions(cosimple=True,
            ....:                           fundamentals=[1, -1, 1/2, 2])
            sage: len(S)
            7
            sage: NF7 = matroids.catalog.NonFano()
            sage: any(N.is_isomorphic(NF7.dual()) for N in S)
            True
            sage: len(M.linear_coextensions(cosimple=True,
            ....:                           fundamentals=[1, -1, 1/2, 2],
            ....:                           F=[3, 4]))
            1"""
    def linear_extension(self, element, chain=..., col=...) -> Any:
        """LinearMatroid.linear_extension(self, element, chain=None, col=None)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 1908)

        Return a linear extension of this matroid.

        A *linear extension* of the represented matroid `M` by element `e` is
        a matroid represented by `[A\\ \\ b]`, where `A` is a representation
        matrix of `M` and `b` is a new column labeled by `e`.

        INPUT:

        - ``element`` -- the name of the new element
        - ``col`` -- (default: ``None``) a column to be appended to
          ``self.representation()``; can be any iterable
        - ``chain`` -- (default: ``None``) a dictionary that maps elements of
          the groundset to elements of the base ring

        OUTPUT:

        A linear matroid `N = M([A\\ \\ b])`, where `A` is a matrix such that
        the current matroid is `M[A]`, and `b` is either given by ``col`` or
        is a weighted combination of columns of `A`, the weights being given
        by ``chain``.

        .. SEEALSO::

            :meth:`M.extension() <sage.matroids.matroid.Matroid.extension>`.

        EXAMPLES::

            sage: M = Matroid(ring=GF(2), matrix=[[1, 1, 0, 1, 0, 0],
            ....:                                 [1, 0, 1, 0, 1, 0],
            ....:                                 [0, 1, 1, 0, 0, 1],
            ....:                                 [0, 0, 0, 1, 1, 1]])
            sage: M.linear_extension(6, {0:1, 5: 1}).representation()
            [1 1 0 1 0 0 1]
            [1 0 1 0 1 0 1]
            [0 1 1 0 0 1 1]
            [0 0 0 1 1 1 1]
            sage: M.linear_extension(6, col=[0, 1, 1, 1]).representation()
            [1 1 0 1 0 0 0]
            [1 0 1 0 1 0 1]
            [0 1 1 0 0 1 1]
            [0 0 0 1 1 1 1]"""
    @overload
    def linear_extension_chains(self, F=..., simple=..., fundamentals=...) -> Any:
        """LinearMatroid.linear_extension_chains(self, F=None, simple=False, fundamentals=None)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 2311)

        Create a list of chains that determine the single-element extensions
        of this linear matroid representation.

        A *chain* is a dictionary, mapping elements from the groundset to
        elements of the base ring, indicating a linear combination of columns
        to form the new column. Think of chains as vectors, only independent
        of representation.

        INPUT:

        - ``F`` -- (default: ``self.groundset()``) a subset of the groundset

        - ``simple`` -- boolean (default: ``False``)

        - ``fundamentals`` -- (default: ``None``) a set elements of the base
          ring

        OUTPUT:

        A list of chains, so each single-element extension of this linear
        matroid representation is given by one of these chains.

        If one or more of the above inputs is given, the list is restricted to
        chains

        - so that the support of each chain lies in ``F``, if given
        - so that the chain does not generate a parallel extension or loop, if
          ``simple = True``
        - so that in the extension generated by this chain, the cross ratios
          are restricted to ``fundamentals``, if given.

        .. SEEALSO::

            :meth:`M.linear_extension() <LinearMatroid.linear_extension>`,
            :meth:`M.linear_extensions() <LinearMatroid.linear_extensions>`,
            :meth:`M.cross_ratios() <LinearMatroid.cross_ratios>`

        EXAMPLES::

            sage: M = Matroid(reduced_matrix=Matrix(GF(2),
            ....:                          [[1, 1, 0], [1, 0, 1], [0, 1, 1]]))
            sage: len(M.linear_extension_chains())
            8
            sage: len(M.linear_extension_chains(F=[0, 1]))
            4
            sage: len(M.linear_extension_chains(F=[0, 1], simple=True))
            0
            sage: M.linear_extension_chains(F=[0, 1, 2], simple=True)
            [{0: 1, 1: 1, 2: 1}]
            sage: N = Matroid(ring=QQ,
            ....:         reduced_matrix=[[-1, -1, 0], [1, 0, -1], [0, 1, 1]])
            sage: L = N.linear_extension_chains(F=[0, 1], simple=True,
            ....:                           fundamentals=set([1, -1, 1/2, 2]))
            sage: result = [{0: 1, 1: 1}, {0: -1/2, 1: 1}, {0: -2, 1: 1}]
            sage: all(D in L for D in result)
            True"""
    @overload
    def linear_extension_chains(self) -> Any:
        """LinearMatroid.linear_extension_chains(self, F=None, simple=False, fundamentals=None)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 2311)

        Create a list of chains that determine the single-element extensions
        of this linear matroid representation.

        A *chain* is a dictionary, mapping elements from the groundset to
        elements of the base ring, indicating a linear combination of columns
        to form the new column. Think of chains as vectors, only independent
        of representation.

        INPUT:

        - ``F`` -- (default: ``self.groundset()``) a subset of the groundset

        - ``simple`` -- boolean (default: ``False``)

        - ``fundamentals`` -- (default: ``None``) a set elements of the base
          ring

        OUTPUT:

        A list of chains, so each single-element extension of this linear
        matroid representation is given by one of these chains.

        If one or more of the above inputs is given, the list is restricted to
        chains

        - so that the support of each chain lies in ``F``, if given
        - so that the chain does not generate a parallel extension or loop, if
          ``simple = True``
        - so that in the extension generated by this chain, the cross ratios
          are restricted to ``fundamentals``, if given.

        .. SEEALSO::

            :meth:`M.linear_extension() <LinearMatroid.linear_extension>`,
            :meth:`M.linear_extensions() <LinearMatroid.linear_extensions>`,
            :meth:`M.cross_ratios() <LinearMatroid.cross_ratios>`

        EXAMPLES::

            sage: M = Matroid(reduced_matrix=Matrix(GF(2),
            ....:                          [[1, 1, 0], [1, 0, 1], [0, 1, 1]]))
            sage: len(M.linear_extension_chains())
            8
            sage: len(M.linear_extension_chains(F=[0, 1]))
            4
            sage: len(M.linear_extension_chains(F=[0, 1], simple=True))
            0
            sage: M.linear_extension_chains(F=[0, 1, 2], simple=True)
            [{0: 1, 1: 1, 2: 1}]
            sage: N = Matroid(ring=QQ,
            ....:         reduced_matrix=[[-1, -1, 0], [1, 0, -1], [0, 1, 1]])
            sage: L = N.linear_extension_chains(F=[0, 1], simple=True,
            ....:                           fundamentals=set([1, -1, 1/2, 2]))
            sage: result = [{0: 1, 1: 1}, {0: -1/2, 1: 1}, {0: -2, 1: 1}]
            sage: all(D in L for D in result)
            True"""
    @overload
    def linear_extension_chains(self, F=...) -> Any:
        """LinearMatroid.linear_extension_chains(self, F=None, simple=False, fundamentals=None)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 2311)

        Create a list of chains that determine the single-element extensions
        of this linear matroid representation.

        A *chain* is a dictionary, mapping elements from the groundset to
        elements of the base ring, indicating a linear combination of columns
        to form the new column. Think of chains as vectors, only independent
        of representation.

        INPUT:

        - ``F`` -- (default: ``self.groundset()``) a subset of the groundset

        - ``simple`` -- boolean (default: ``False``)

        - ``fundamentals`` -- (default: ``None``) a set elements of the base
          ring

        OUTPUT:

        A list of chains, so each single-element extension of this linear
        matroid representation is given by one of these chains.

        If one or more of the above inputs is given, the list is restricted to
        chains

        - so that the support of each chain lies in ``F``, if given
        - so that the chain does not generate a parallel extension or loop, if
          ``simple = True``
        - so that in the extension generated by this chain, the cross ratios
          are restricted to ``fundamentals``, if given.

        .. SEEALSO::

            :meth:`M.linear_extension() <LinearMatroid.linear_extension>`,
            :meth:`M.linear_extensions() <LinearMatroid.linear_extensions>`,
            :meth:`M.cross_ratios() <LinearMatroid.cross_ratios>`

        EXAMPLES::

            sage: M = Matroid(reduced_matrix=Matrix(GF(2),
            ....:                          [[1, 1, 0], [1, 0, 1], [0, 1, 1]]))
            sage: len(M.linear_extension_chains())
            8
            sage: len(M.linear_extension_chains(F=[0, 1]))
            4
            sage: len(M.linear_extension_chains(F=[0, 1], simple=True))
            0
            sage: M.linear_extension_chains(F=[0, 1, 2], simple=True)
            [{0: 1, 1: 1, 2: 1}]
            sage: N = Matroid(ring=QQ,
            ....:         reduced_matrix=[[-1, -1, 0], [1, 0, -1], [0, 1, 1]])
            sage: L = N.linear_extension_chains(F=[0, 1], simple=True,
            ....:                           fundamentals=set([1, -1, 1/2, 2]))
            sage: result = [{0: 1, 1: 1}, {0: -1/2, 1: 1}, {0: -2, 1: 1}]
            sage: all(D in L for D in result)
            True"""
    @overload
    def linear_extension_chains(self, F=..., simple=...) -> Any:
        """LinearMatroid.linear_extension_chains(self, F=None, simple=False, fundamentals=None)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 2311)

        Create a list of chains that determine the single-element extensions
        of this linear matroid representation.

        A *chain* is a dictionary, mapping elements from the groundset to
        elements of the base ring, indicating a linear combination of columns
        to form the new column. Think of chains as vectors, only independent
        of representation.

        INPUT:

        - ``F`` -- (default: ``self.groundset()``) a subset of the groundset

        - ``simple`` -- boolean (default: ``False``)

        - ``fundamentals`` -- (default: ``None``) a set elements of the base
          ring

        OUTPUT:

        A list of chains, so each single-element extension of this linear
        matroid representation is given by one of these chains.

        If one or more of the above inputs is given, the list is restricted to
        chains

        - so that the support of each chain lies in ``F``, if given
        - so that the chain does not generate a parallel extension or loop, if
          ``simple = True``
        - so that in the extension generated by this chain, the cross ratios
          are restricted to ``fundamentals``, if given.

        .. SEEALSO::

            :meth:`M.linear_extension() <LinearMatroid.linear_extension>`,
            :meth:`M.linear_extensions() <LinearMatroid.linear_extensions>`,
            :meth:`M.cross_ratios() <LinearMatroid.cross_ratios>`

        EXAMPLES::

            sage: M = Matroid(reduced_matrix=Matrix(GF(2),
            ....:                          [[1, 1, 0], [1, 0, 1], [0, 1, 1]]))
            sage: len(M.linear_extension_chains())
            8
            sage: len(M.linear_extension_chains(F=[0, 1]))
            4
            sage: len(M.linear_extension_chains(F=[0, 1], simple=True))
            0
            sage: M.linear_extension_chains(F=[0, 1, 2], simple=True)
            [{0: 1, 1: 1, 2: 1}]
            sage: N = Matroid(ring=QQ,
            ....:         reduced_matrix=[[-1, -1, 0], [1, 0, -1], [0, 1, 1]])
            sage: L = N.linear_extension_chains(F=[0, 1], simple=True,
            ....:                           fundamentals=set([1, -1, 1/2, 2]))
            sage: result = [{0: 1, 1: 1}, {0: -1/2, 1: 1}, {0: -2, 1: 1}]
            sage: all(D in L for D in result)
            True"""
    @overload
    def linear_extension_chains(self, F=..., simple=...) -> Any:
        """LinearMatroid.linear_extension_chains(self, F=None, simple=False, fundamentals=None)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 2311)

        Create a list of chains that determine the single-element extensions
        of this linear matroid representation.

        A *chain* is a dictionary, mapping elements from the groundset to
        elements of the base ring, indicating a linear combination of columns
        to form the new column. Think of chains as vectors, only independent
        of representation.

        INPUT:

        - ``F`` -- (default: ``self.groundset()``) a subset of the groundset

        - ``simple`` -- boolean (default: ``False``)

        - ``fundamentals`` -- (default: ``None``) a set elements of the base
          ring

        OUTPUT:

        A list of chains, so each single-element extension of this linear
        matroid representation is given by one of these chains.

        If one or more of the above inputs is given, the list is restricted to
        chains

        - so that the support of each chain lies in ``F``, if given
        - so that the chain does not generate a parallel extension or loop, if
          ``simple = True``
        - so that in the extension generated by this chain, the cross ratios
          are restricted to ``fundamentals``, if given.

        .. SEEALSO::

            :meth:`M.linear_extension() <LinearMatroid.linear_extension>`,
            :meth:`M.linear_extensions() <LinearMatroid.linear_extensions>`,
            :meth:`M.cross_ratios() <LinearMatroid.cross_ratios>`

        EXAMPLES::

            sage: M = Matroid(reduced_matrix=Matrix(GF(2),
            ....:                          [[1, 1, 0], [1, 0, 1], [0, 1, 1]]))
            sage: len(M.linear_extension_chains())
            8
            sage: len(M.linear_extension_chains(F=[0, 1]))
            4
            sage: len(M.linear_extension_chains(F=[0, 1], simple=True))
            0
            sage: M.linear_extension_chains(F=[0, 1, 2], simple=True)
            [{0: 1, 1: 1, 2: 1}]
            sage: N = Matroid(ring=QQ,
            ....:         reduced_matrix=[[-1, -1, 0], [1, 0, -1], [0, 1, 1]])
            sage: L = N.linear_extension_chains(F=[0, 1], simple=True,
            ....:                           fundamentals=set([1, -1, 1/2, 2]))
            sage: result = [{0: 1, 1: 1}, {0: -1/2, 1: 1}, {0: -2, 1: 1}]
            sage: all(D in L for D in result)
            True"""
    @overload
    def linear_extension_chains(self, F=..., simple=..., 
....: fundamentals = ...) -> Any:
        """LinearMatroid.linear_extension_chains(self, F=None, simple=False, fundamentals=None)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 2311)

        Create a list of chains that determine the single-element extensions
        of this linear matroid representation.

        A *chain* is a dictionary, mapping elements from the groundset to
        elements of the base ring, indicating a linear combination of columns
        to form the new column. Think of chains as vectors, only independent
        of representation.

        INPUT:

        - ``F`` -- (default: ``self.groundset()``) a subset of the groundset

        - ``simple`` -- boolean (default: ``False``)

        - ``fundamentals`` -- (default: ``None``) a set elements of the base
          ring

        OUTPUT:

        A list of chains, so each single-element extension of this linear
        matroid representation is given by one of these chains.

        If one or more of the above inputs is given, the list is restricted to
        chains

        - so that the support of each chain lies in ``F``, if given
        - so that the chain does not generate a parallel extension or loop, if
          ``simple = True``
        - so that in the extension generated by this chain, the cross ratios
          are restricted to ``fundamentals``, if given.

        .. SEEALSO::

            :meth:`M.linear_extension() <LinearMatroid.linear_extension>`,
            :meth:`M.linear_extensions() <LinearMatroid.linear_extensions>`,
            :meth:`M.cross_ratios() <LinearMatroid.cross_ratios>`

        EXAMPLES::

            sage: M = Matroid(reduced_matrix=Matrix(GF(2),
            ....:                          [[1, 1, 0], [1, 0, 1], [0, 1, 1]]))
            sage: len(M.linear_extension_chains())
            8
            sage: len(M.linear_extension_chains(F=[0, 1]))
            4
            sage: len(M.linear_extension_chains(F=[0, 1], simple=True))
            0
            sage: M.linear_extension_chains(F=[0, 1, 2], simple=True)
            [{0: 1, 1: 1, 2: 1}]
            sage: N = Matroid(ring=QQ,
            ....:         reduced_matrix=[[-1, -1, 0], [1, 0, -1], [0, 1, 1]])
            sage: L = N.linear_extension_chains(F=[0, 1], simple=True,
            ....:                           fundamentals=set([1, -1, 1/2, 2]))
            sage: result = [{0: 1, 1: 1}, {0: -1/2, 1: 1}, {0: -2, 1: 1}]
            sage: all(D in L for D in result)
            True"""
    @overload
    def linear_extensions(self, element=..., F=..., simple=..., fundamentals=...) -> Any:
        """LinearMatroid.linear_extensions(self, element=None, F=None, simple=False, fundamentals=None)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 2472)

        Create a list of linear matroids represented by rank-preserving single-element
        extensions of this linear matroid representation.

        INPUT:

        - ``element`` -- (default: ``None``) the name of the new element of
          the groundset

        - ``F`` -- (default: ``None``) a subset of the groundset

        - ``simple`` -- boolean (default: ``False``)

        - ``fundamentals`` -- (default: ``None``) a set elements of the base
          ring

        OUTPUT:

        A list of linear matroids represented by rank-preserving single-element extensions of
        this linear matroid representation. In particular, the extension by a coloop is not
        generated.

        If one or more of the above inputs is given, the list is restricted to
        matroids

        - so that the new element is spanned by ``F``, if given
        - so that the new element is not a loop or in a parallel pair, if
          ``simple=True``
        - so that in the representation of the extension, the cross ratios are
          restricted to ``fundamentals``, if given. Note that it is assumed
          that the cross ratios of the input matroid already satisfy this
          condition.

        .. SEEALSO::

            :meth:`M.linear_extension() <LinearMatroid.linear_extension>`,
            :meth:`M.linear_extension_chains() <LinearMatroid.linear_extension_chains>`,
            :meth:`M.cross_ratios() <LinearMatroid.cross_ratios>`

        EXAMPLES::

            sage: M = Matroid(ring=GF(2),
            ....:             reduced_matrix=[[-1, 0, 1], [1, -1, 0], [0, 1, -1]])
            sage: len(M.linear_extensions())
            8
            sage: S = M.linear_extensions(simple=True); S
            [Binary matroid of rank 3 on 7 elements, type (3, 0)]
            sage: S[0].is_field_isomorphic(matroids.catalog.Fano())
            True
            sage: M = Matroid(ring=QQ,
            ....:             reduced_matrix=[[1, 0, 1], [1, 1, 0], [0, 1, 1]])
            sage: S = M.linear_extensions(simple=True,
            ....:                         fundamentals=[1, -1, 1/2, 2])
            sage: len(S)
            7
            sage: any(N.is_isomorphic(matroids.catalog.NonFano())
            ....:     for N in S)
            True
            sage: len(M.linear_extensions(simple=True,
            ....:                         fundamentals=[1, -1, 1/2, 2], F=[0, 1]))
            1"""
    @overload
    def linear_extensions(self) -> Any:
        """LinearMatroid.linear_extensions(self, element=None, F=None, simple=False, fundamentals=None)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 2472)

        Create a list of linear matroids represented by rank-preserving single-element
        extensions of this linear matroid representation.

        INPUT:

        - ``element`` -- (default: ``None``) the name of the new element of
          the groundset

        - ``F`` -- (default: ``None``) a subset of the groundset

        - ``simple`` -- boolean (default: ``False``)

        - ``fundamentals`` -- (default: ``None``) a set elements of the base
          ring

        OUTPUT:

        A list of linear matroids represented by rank-preserving single-element extensions of
        this linear matroid representation. In particular, the extension by a coloop is not
        generated.

        If one or more of the above inputs is given, the list is restricted to
        matroids

        - so that the new element is spanned by ``F``, if given
        - so that the new element is not a loop or in a parallel pair, if
          ``simple=True``
        - so that in the representation of the extension, the cross ratios are
          restricted to ``fundamentals``, if given. Note that it is assumed
          that the cross ratios of the input matroid already satisfy this
          condition.

        .. SEEALSO::

            :meth:`M.linear_extension() <LinearMatroid.linear_extension>`,
            :meth:`M.linear_extension_chains() <LinearMatroid.linear_extension_chains>`,
            :meth:`M.cross_ratios() <LinearMatroid.cross_ratios>`

        EXAMPLES::

            sage: M = Matroid(ring=GF(2),
            ....:             reduced_matrix=[[-1, 0, 1], [1, -1, 0], [0, 1, -1]])
            sage: len(M.linear_extensions())
            8
            sage: S = M.linear_extensions(simple=True); S
            [Binary matroid of rank 3 on 7 elements, type (3, 0)]
            sage: S[0].is_field_isomorphic(matroids.catalog.Fano())
            True
            sage: M = Matroid(ring=QQ,
            ....:             reduced_matrix=[[1, 0, 1], [1, 1, 0], [0, 1, 1]])
            sage: S = M.linear_extensions(simple=True,
            ....:                         fundamentals=[1, -1, 1/2, 2])
            sage: len(S)
            7
            sage: any(N.is_isomorphic(matroids.catalog.NonFano())
            ....:     for N in S)
            True
            sage: len(M.linear_extensions(simple=True,
            ....:                         fundamentals=[1, -1, 1/2, 2], F=[0, 1]))
            1"""
    @overload
    def linear_extensions(self, simple=...) -> Any:
        """LinearMatroid.linear_extensions(self, element=None, F=None, simple=False, fundamentals=None)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 2472)

        Create a list of linear matroids represented by rank-preserving single-element
        extensions of this linear matroid representation.

        INPUT:

        - ``element`` -- (default: ``None``) the name of the new element of
          the groundset

        - ``F`` -- (default: ``None``) a subset of the groundset

        - ``simple`` -- boolean (default: ``False``)

        - ``fundamentals`` -- (default: ``None``) a set elements of the base
          ring

        OUTPUT:

        A list of linear matroids represented by rank-preserving single-element extensions of
        this linear matroid representation. In particular, the extension by a coloop is not
        generated.

        If one or more of the above inputs is given, the list is restricted to
        matroids

        - so that the new element is spanned by ``F``, if given
        - so that the new element is not a loop or in a parallel pair, if
          ``simple=True``
        - so that in the representation of the extension, the cross ratios are
          restricted to ``fundamentals``, if given. Note that it is assumed
          that the cross ratios of the input matroid already satisfy this
          condition.

        .. SEEALSO::

            :meth:`M.linear_extension() <LinearMatroid.linear_extension>`,
            :meth:`M.linear_extension_chains() <LinearMatroid.linear_extension_chains>`,
            :meth:`M.cross_ratios() <LinearMatroid.cross_ratios>`

        EXAMPLES::

            sage: M = Matroid(ring=GF(2),
            ....:             reduced_matrix=[[-1, 0, 1], [1, -1, 0], [0, 1, -1]])
            sage: len(M.linear_extensions())
            8
            sage: S = M.linear_extensions(simple=True); S
            [Binary matroid of rank 3 on 7 elements, type (3, 0)]
            sage: S[0].is_field_isomorphic(matroids.catalog.Fano())
            True
            sage: M = Matroid(ring=QQ,
            ....:             reduced_matrix=[[1, 0, 1], [1, 1, 0], [0, 1, 1]])
            sage: S = M.linear_extensions(simple=True,
            ....:                         fundamentals=[1, -1, 1/2, 2])
            sage: len(S)
            7
            sage: any(N.is_isomorphic(matroids.catalog.NonFano())
            ....:     for N in S)
            True
            sage: len(M.linear_extensions(simple=True,
            ....:                         fundamentals=[1, -1, 1/2, 2], F=[0, 1]))
            1"""
    @overload
    def linear_extensions(self, simple=..., 
....: fundamentals = ...) -> Any:
        """LinearMatroid.linear_extensions(self, element=None, F=None, simple=False, fundamentals=None)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 2472)

        Create a list of linear matroids represented by rank-preserving single-element
        extensions of this linear matroid representation.

        INPUT:

        - ``element`` -- (default: ``None``) the name of the new element of
          the groundset

        - ``F`` -- (default: ``None``) a subset of the groundset

        - ``simple`` -- boolean (default: ``False``)

        - ``fundamentals`` -- (default: ``None``) a set elements of the base
          ring

        OUTPUT:

        A list of linear matroids represented by rank-preserving single-element extensions of
        this linear matroid representation. In particular, the extension by a coloop is not
        generated.

        If one or more of the above inputs is given, the list is restricted to
        matroids

        - so that the new element is spanned by ``F``, if given
        - so that the new element is not a loop or in a parallel pair, if
          ``simple=True``
        - so that in the representation of the extension, the cross ratios are
          restricted to ``fundamentals``, if given. Note that it is assumed
          that the cross ratios of the input matroid already satisfy this
          condition.

        .. SEEALSO::

            :meth:`M.linear_extension() <LinearMatroid.linear_extension>`,
            :meth:`M.linear_extension_chains() <LinearMatroid.linear_extension_chains>`,
            :meth:`M.cross_ratios() <LinearMatroid.cross_ratios>`

        EXAMPLES::

            sage: M = Matroid(ring=GF(2),
            ....:             reduced_matrix=[[-1, 0, 1], [1, -1, 0], [0, 1, -1]])
            sage: len(M.linear_extensions())
            8
            sage: S = M.linear_extensions(simple=True); S
            [Binary matroid of rank 3 on 7 elements, type (3, 0)]
            sage: S[0].is_field_isomorphic(matroids.catalog.Fano())
            True
            sage: M = Matroid(ring=QQ,
            ....:             reduced_matrix=[[1, 0, 1], [1, 1, 0], [0, 1, 1]])
            sage: S = M.linear_extensions(simple=True,
            ....:                         fundamentals=[1, -1, 1/2, 2])
            sage: len(S)
            7
            sage: any(N.is_isomorphic(matroids.catalog.NonFano())
            ....:     for N in S)
            True
            sage: len(M.linear_extensions(simple=True,
            ....:                         fundamentals=[1, -1, 1/2, 2], F=[0, 1]))
            1"""
    @overload
    def linear_extensions(self, simple=..., 
....: fundamentals = ..., F=...) -> Any:
        """LinearMatroid.linear_extensions(self, element=None, F=None, simple=False, fundamentals=None)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 2472)

        Create a list of linear matroids represented by rank-preserving single-element
        extensions of this linear matroid representation.

        INPUT:

        - ``element`` -- (default: ``None``) the name of the new element of
          the groundset

        - ``F`` -- (default: ``None``) a subset of the groundset

        - ``simple`` -- boolean (default: ``False``)

        - ``fundamentals`` -- (default: ``None``) a set elements of the base
          ring

        OUTPUT:

        A list of linear matroids represented by rank-preserving single-element extensions of
        this linear matroid representation. In particular, the extension by a coloop is not
        generated.

        If one or more of the above inputs is given, the list is restricted to
        matroids

        - so that the new element is spanned by ``F``, if given
        - so that the new element is not a loop or in a parallel pair, if
          ``simple=True``
        - so that in the representation of the extension, the cross ratios are
          restricted to ``fundamentals``, if given. Note that it is assumed
          that the cross ratios of the input matroid already satisfy this
          condition.

        .. SEEALSO::

            :meth:`M.linear_extension() <LinearMatroid.linear_extension>`,
            :meth:`M.linear_extension_chains() <LinearMatroid.linear_extension_chains>`,
            :meth:`M.cross_ratios() <LinearMatroid.cross_ratios>`

        EXAMPLES::

            sage: M = Matroid(ring=GF(2),
            ....:             reduced_matrix=[[-1, 0, 1], [1, -1, 0], [0, 1, -1]])
            sage: len(M.linear_extensions())
            8
            sage: S = M.linear_extensions(simple=True); S
            [Binary matroid of rank 3 on 7 elements, type (3, 0)]
            sage: S[0].is_field_isomorphic(matroids.catalog.Fano())
            True
            sage: M = Matroid(ring=QQ,
            ....:             reduced_matrix=[[1, 0, 1], [1, 1, 0], [0, 1, 1]])
            sage: S = M.linear_extensions(simple=True,
            ....:                         fundamentals=[1, -1, 1/2, 2])
            sage: len(S)
            7
            sage: any(N.is_isomorphic(matroids.catalog.NonFano())
            ....:     for N in S)
            True
            sage: len(M.linear_extensions(simple=True,
            ....:                         fundamentals=[1, -1, 1/2, 2], F=[0, 1]))
            1"""
    @overload
    def orlik_terao_algebra(self, R=..., ordering=..., **kwargs) -> Any:
        """LinearMatroid.orlik_terao_algebra(self, R=None, ordering=None, **kwargs)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 2861)

        Return the Orlik-Terao algebra of ``self``.

        INPUT:

        - ``R`` -- (default: the base ring of ``self``) the base ring
        - ``ordering`` -- (optional) an ordering of the groundset

        .. SEEALSO::

            :class:`~sage.algebras.orlik_terao.OrlikTeraoAlgebra`

        EXAMPLES::

            sage: M = matroids.Wheel(3)
            sage: OS = M.orlik_terao_algebra(); OS
            Orlik-Terao algebra of Wheel(3):
             Regular matroid of rank 3 on 6 elements with 16 bases
             over Integer Ring
            sage: OS.base_ring()
            Integer Ring
            sage: M.orlik_terao_algebra(QQ).base_ring()
            Rational Field

            sage: G = SymmetricGroup(3);                                                # needs sage.groups
            sage: OTG = M.orlik_terao_algebra(QQ, invariant=G)                          # needs sage.groups

            sage: # needs sage.groups
            sage: G = SymmetricGroup(4)
            sage: action = lambda g, x: g(x + 1) - 1
            sage: OTG1 = M.orlik_terao_algebra(QQ, invariant=(G, action))
            sage: OTG2 = M.orlik_terao_algebra(QQ, invariant=(action, G))
            sage: OTG1 is OTG2
            True"""
    @overload
    def orlik_terao_algebra(self) -> Any:
        """LinearMatroid.orlik_terao_algebra(self, R=None, ordering=None, **kwargs)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 2861)

        Return the Orlik-Terao algebra of ``self``.

        INPUT:

        - ``R`` -- (default: the base ring of ``self``) the base ring
        - ``ordering`` -- (optional) an ordering of the groundset

        .. SEEALSO::

            :class:`~sage.algebras.orlik_terao.OrlikTeraoAlgebra`

        EXAMPLES::

            sage: M = matroids.Wheel(3)
            sage: OS = M.orlik_terao_algebra(); OS
            Orlik-Terao algebra of Wheel(3):
             Regular matroid of rank 3 on 6 elements with 16 bases
             over Integer Ring
            sage: OS.base_ring()
            Integer Ring
            sage: M.orlik_terao_algebra(QQ).base_ring()
            Rational Field

            sage: G = SymmetricGroup(3);                                                # needs sage.groups
            sage: OTG = M.orlik_terao_algebra(QQ, invariant=G)                          # needs sage.groups

            sage: # needs sage.groups
            sage: G = SymmetricGroup(4)
            sage: action = lambda g, x: g(x + 1) - 1
            sage: OTG1 = M.orlik_terao_algebra(QQ, invariant=(G, action))
            sage: OTG2 = M.orlik_terao_algebra(QQ, invariant=(action, G))
            sage: OTG1 is OTG2
            True"""
    @overload
    def orlik_terao_algebra(self, QQ) -> Any:
        """LinearMatroid.orlik_terao_algebra(self, R=None, ordering=None, **kwargs)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 2861)

        Return the Orlik-Terao algebra of ``self``.

        INPUT:

        - ``R`` -- (default: the base ring of ``self``) the base ring
        - ``ordering`` -- (optional) an ordering of the groundset

        .. SEEALSO::

            :class:`~sage.algebras.orlik_terao.OrlikTeraoAlgebra`

        EXAMPLES::

            sage: M = matroids.Wheel(3)
            sage: OS = M.orlik_terao_algebra(); OS
            Orlik-Terao algebra of Wheel(3):
             Regular matroid of rank 3 on 6 elements with 16 bases
             over Integer Ring
            sage: OS.base_ring()
            Integer Ring
            sage: M.orlik_terao_algebra(QQ).base_ring()
            Rational Field

            sage: G = SymmetricGroup(3);                                                # needs sage.groups
            sage: OTG = M.orlik_terao_algebra(QQ, invariant=G)                          # needs sage.groups

            sage: # needs sage.groups
            sage: G = SymmetricGroup(4)
            sage: action = lambda g, x: g(x + 1) - 1
            sage: OTG1 = M.orlik_terao_algebra(QQ, invariant=(G, action))
            sage: OTG2 = M.orlik_terao_algebra(QQ, invariant=(action, G))
            sage: OTG1 is OTG2
            True"""
    @overload
    def orlik_terao_algebra(self, QQ, invariant=...) -> Any:
        """LinearMatroid.orlik_terao_algebra(self, R=None, ordering=None, **kwargs)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 2861)

        Return the Orlik-Terao algebra of ``self``.

        INPUT:

        - ``R`` -- (default: the base ring of ``self``) the base ring
        - ``ordering`` -- (optional) an ordering of the groundset

        .. SEEALSO::

            :class:`~sage.algebras.orlik_terao.OrlikTeraoAlgebra`

        EXAMPLES::

            sage: M = matroids.Wheel(3)
            sage: OS = M.orlik_terao_algebra(); OS
            Orlik-Terao algebra of Wheel(3):
             Regular matroid of rank 3 on 6 elements with 16 bases
             over Integer Ring
            sage: OS.base_ring()
            Integer Ring
            sage: M.orlik_terao_algebra(QQ).base_ring()
            Rational Field

            sage: G = SymmetricGroup(3);                                                # needs sage.groups
            sage: OTG = M.orlik_terao_algebra(QQ, invariant=G)                          # needs sage.groups

            sage: # needs sage.groups
            sage: G = SymmetricGroup(4)
            sage: action = lambda g, x: g(x + 1) - 1
            sage: OTG1 = M.orlik_terao_algebra(QQ, invariant=(G, action))
            sage: OTG2 = M.orlik_terao_algebra(QQ, invariant=(action, G))
            sage: OTG1 is OTG2
            True"""
    @overload
    def orlik_terao_algebra(self, QQ, invariant=...) -> Any:
        """LinearMatroid.orlik_terao_algebra(self, R=None, ordering=None, **kwargs)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 2861)

        Return the Orlik-Terao algebra of ``self``.

        INPUT:

        - ``R`` -- (default: the base ring of ``self``) the base ring
        - ``ordering`` -- (optional) an ordering of the groundset

        .. SEEALSO::

            :class:`~sage.algebras.orlik_terao.OrlikTeraoAlgebra`

        EXAMPLES::

            sage: M = matroids.Wheel(3)
            sage: OS = M.orlik_terao_algebra(); OS
            Orlik-Terao algebra of Wheel(3):
             Regular matroid of rank 3 on 6 elements with 16 bases
             over Integer Ring
            sage: OS.base_ring()
            Integer Ring
            sage: M.orlik_terao_algebra(QQ).base_ring()
            Rational Field

            sage: G = SymmetricGroup(3);                                                # needs sage.groups
            sage: OTG = M.orlik_terao_algebra(QQ, invariant=G)                          # needs sage.groups

            sage: # needs sage.groups
            sage: G = SymmetricGroup(4)
            sage: action = lambda g, x: g(x + 1) - 1
            sage: OTG1 = M.orlik_terao_algebra(QQ, invariant=(G, action))
            sage: OTG2 = M.orlik_terao_algebra(QQ, invariant=(action, G))
            sage: OTG1 is OTG2
            True"""
    @overload
    def orlik_terao_algebra(self, QQ, invariant=...) -> Any:
        """LinearMatroid.orlik_terao_algebra(self, R=None, ordering=None, **kwargs)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 2861)

        Return the Orlik-Terao algebra of ``self``.

        INPUT:

        - ``R`` -- (default: the base ring of ``self``) the base ring
        - ``ordering`` -- (optional) an ordering of the groundset

        .. SEEALSO::

            :class:`~sage.algebras.orlik_terao.OrlikTeraoAlgebra`

        EXAMPLES::

            sage: M = matroids.Wheel(3)
            sage: OS = M.orlik_terao_algebra(); OS
            Orlik-Terao algebra of Wheel(3):
             Regular matroid of rank 3 on 6 elements with 16 bases
             over Integer Ring
            sage: OS.base_ring()
            Integer Ring
            sage: M.orlik_terao_algebra(QQ).base_ring()
            Rational Field

            sage: G = SymmetricGroup(3);                                                # needs sage.groups
            sage: OTG = M.orlik_terao_algebra(QQ, invariant=G)                          # needs sage.groups

            sage: # needs sage.groups
            sage: G = SymmetricGroup(4)
            sage: action = lambda g, x: g(x + 1) - 1
            sage: OTG1 = M.orlik_terao_algebra(QQ, invariant=(G, action))
            sage: OTG2 = M.orlik_terao_algebra(QQ, invariant=(action, G))
            sage: OTG1 is OTG2
            True"""
    @overload
    def relabel(self, mapping) -> Any:
        """LinearMatroid.relabel(self, mapping)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 2972)

        Return an isomorphic matroid with relabeled groundset.

        The output is obtained by relabeling each element `e` by
        ``mapping[e]``, where ``mapping`` is a given injective map. If
        ``mapping[e]`` is not defined, then the identity map is assumed.

        INPUT:

        - ``mapping`` -- a Python object such that ``mapping[e]`` is the new
          label of `e`

        OUTPUT: matroid

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: sorted(M.groundset())
            ['a', 'b', 'c', 'd', 'e', 'f', 'g']
            sage: N = M.relabel({'g': 'x'})
            sage: sorted(N.groundset())
            ['a', 'b', 'c', 'd', 'e', 'f', 'x']

        TESTS::

            sage: M = matroids.catalog.Fano()
            sage: f = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}
            sage: N = M.relabel(f)
            sage: for S in powerset(M.groundset()):
            ....:     assert M.rank(S) == N.rank([f[x] for x in S])"""
    @overload
    def relabel(self, f) -> Any:
        """LinearMatroid.relabel(self, mapping)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 2972)

        Return an isomorphic matroid with relabeled groundset.

        The output is obtained by relabeling each element `e` by
        ``mapping[e]``, where ``mapping`` is a given injective map. If
        ``mapping[e]`` is not defined, then the identity map is assumed.

        INPUT:

        - ``mapping`` -- a Python object such that ``mapping[e]`` is the new
          label of `e`

        OUTPUT: matroid

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: sorted(M.groundset())
            ['a', 'b', 'c', 'd', 'e', 'f', 'g']
            sage: N = M.relabel({'g': 'x'})
            sage: sorted(N.groundset())
            ['a', 'b', 'c', 'd', 'e', 'f', 'x']

        TESTS::

            sage: M = matroids.catalog.Fano()
            sage: f = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}
            sage: N = M.relabel(f)
            sage: for S in powerset(M.groundset()):
            ....:     assert M.rank(S) == N.rank([f[x] for x in S])"""
    def representation(self, B=..., reduced=..., labels=..., order=..., lift_map=...) -> Any:
        """LinearMatroid.representation(self, B=None, reduced=False, labels=None, order=None, lift_map=None)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 471)

        Return a matrix representing the matroid.

        Let `M` be a matroid on `n` elements with rank `r`. Let `E` be an
        ordering of the groundset, as output by
        :func:`M.groundset_list() <sage.matroids.basis_exchange_matroid.BasisExchangeMatroid.groundset_list>`.
        A *representation* of the matroid is an `r \\times n` matrix with the
        following property. Consider column `i` to be labeled by `E[i]`,
        and denote by `A[F]` the submatrix formed by the columns labeled by
        the subset `F \\subseteq E`. Then for all `F \\subseteq E`, the columns
        of `A[F]` are linearly independent if and only if `F` is an
        independent set in the matroid.

        A *reduced representation* is a matrix `D` such that `[I\\ \\ D]` is a
        representation of the matroid, where `I` is an `r \\times r` identity
        matrix. In this case, the rows of `D` are considered to be labeled by
        the first `r` elements of the list ``E``, and the columns by the
        remaining `n - r` elements.

        INPUT:

        - ``B`` -- (default: ``None``) a subset of elements. When provided,
          the representation is such that a basis `B'` that maximally
          intersects `B` is an identity matrix.

        - ``reduced`` -- boolean (default: ``False``); when ``True``, return a
          reduced matrix `D` (so `[I\\ \\  D]` is a representation of the
          matroid). Otherwise return a full representation matrix.

        - ``labels`` -- (default: ``None``) when ``True``, return additionally
          a list of column labels (if ``reduced=False``) or a list of row
          labels and a list of column labels (if ``reduced=True``).
          The default setting, ``None``, will not return the labels for a full
          matrix, but will return the labels for a reduced matrix.

        - ``order`` -- sequence or ``None`` or ``True`` (default: ``None``)

          - when a sequence, it should be an ordering of the groundset
            elements, and the columns (and, in case of a reduced
            representation, rows) will be presented in the given order,
          - when ``None``, use the same ordering that :meth:`groundset_list`
            uses,
          - when ``True``, return a morphism of free modules instead of a matrix.

        - ``lift_map`` -- (default: ``None``) a dictionary containing the cross
          ratios of the representing matrix in its domain. If provided, the
          representation will be transformed by mapping its cross ratios according
          to ``lift_map``.

        OUTPUT:

        - ``A`` -- a full or reduced representation matrix of ``self``; or
        - ``(A, E)`` -- a full representation matrix ``A`` and a list ``E``
          of column labels; or
        - ``(A, R, C)`` -- a reduced representation matrix and a list ``R`` of
          row labels and a list ``C`` of column labels

        If ``B == None`` and ``reduced == False`` and ``order == None`` then
        this method will always output the same matrix (except when
        ``M._forget()`` is called): either the matrix used as input to create
        the matroid, or a matrix in which the lexicographically least basis
        corresponds to an identity. If only ``order`` is not ``None``, the
        columns of this matrix will be permuted accordingly.

        If a ``lift_map`` is provided, then the resulting matrix will be lifted
        using the method
        :func:`lift_cross_ratios() <sage.matroids.utilities.lift_cross_ratios>`
        See the docstring of this method for further details.

        .. NOTE::

            A shortcut for ``M.representation()`` is ``Matrix(M)``.

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: M.representation()
            [1 0 0 0 1 1 1]
            [0 1 0 1 0 1 1]
            [0 0 1 1 1 0 1]
            sage: Matrix(M) == M.representation()
            True
            sage: M.representation(labels=True)
            (
            [1 0 0 0 1 1 1]
            [0 1 0 1 0 1 1]
            [0 0 1 1 1 0 1], ['a', 'b', 'c', 'd', 'e', 'f', 'g']
            )
            sage: M.representation(B='efg')
            [1 1 0 1 1 0 0]
            [1 0 1 1 0 1 0]
            [1 1 1 0 0 0 1]
            sage: M.representation(B='efg', order='efgabcd')
            [1 0 0 1 1 0 1]
            [0 1 0 1 0 1 1]
            [0 0 1 1 1 1 0]
            sage: M.representation(B='abc', reduced=True)
            (
            [0 1 1 1]
            [1 0 1 1]
            [1 1 0 1], ['a', 'b', 'c'], ['d', 'e', 'f', 'g']
            )
            sage: M.representation(B='efg', reduced=True, labels=False,
            ....:                  order='gfeabcd')
            [1 1 1 0]
            [1 0 1 1]
            [1 1 0 1]

            sage: from sage.matroids.advanced import lift_cross_ratios, lift_map, LinearMatroid
            sage: R = GF(7)
            sage: A = Matrix(R, [[1, 0, 6, 1, 2],[6, 1, 0, 0, 1],[0, 6, 3, 6, 0]])
            sage: M = LinearMatroid(reduced_matrix=A)
            sage: M.representation(lift_map=lift_map('sru'))                            # needs sage.rings.finite_rings
            [     1      0      0      1      0      1      1      1]
            [     0      1      0 -z + 1      1      0      0      1]
            [     0      0      1      0      1      -1 z - 1      0]

        As morphisms::

            sage: M = matroids.catalog.Fano()
            sage: A = M.representation(order=True); A
            Generic morphism:
             From: Free module generated by {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
                   over Finite Field of size 2
             To:   Free module generated by {0, 1, 2} over Finite Field of size 2
            sage: print(A._unicode_art_matrix())
              a b c d e f g
            0⎛1 0 0 0 1 1 1⎞
            1⎜0 1 0 1 0 1 1⎟
            2⎝0 0 1 1 1 0 1⎠
            sage: A = M.representation(B='efg', order=True); A
            Generic morphism:
             From: Free module generated by {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
                   over Finite Field of size 2
             To:   Free module generated by {0, 1, 2} over Finite Field of size 2
            sage: print(A._unicode_art_matrix())
              a b c d e f g
            0⎛1 1 0 1 1 0 0⎞
            1⎜1 0 1 1 0 1 0⎟
            2⎝1 1 1 0 0 0 1⎠
            sage: A = M.representation(B='abc', order=True, reduced=True); A
            Generic morphism:
             From: Free module generated by {'d', 'e', 'f', 'g'}
                   over Finite Field of size 2
             To:   Free module generated by {'a', 'b', 'c'} over Finite Field of size 2
            sage: print(A._unicode_art_matrix())
              d e f g
            a⎛0 1 1 1⎞
            b⎜1 0 1 1⎟
            c⎝1 1 0 1⎠"""
    @overload
    def representation_vectors(self) -> Any:
        """LinearMatroid.representation_vectors(self)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 778)

        Return a dictionary that associates a column vector with each element
        of the matroid.

        .. SEEALSO::

            :meth:`M.representation() <LinearMatroid.representation>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: E = M.groundset_list()
            sage: [M.representation_vectors()[e] for e in E]
            [(1, 0, 0), (0, 1, 0), (0, 0, 1), (0, 1, 1), (1, 0, 1), (1, 1, 0),
             (1, 1, 1)]"""
    @overload
    def representation_vectors(self) -> Any:
        """LinearMatroid.representation_vectors(self)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 778)

        Return a dictionary that associates a column vector with each element
        of the matroid.

        .. SEEALSO::

            :meth:`M.representation() <LinearMatroid.representation>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: E = M.groundset_list()
            sage: [M.representation_vectors()[e] for e in E]
            [(1, 0, 0), (0, 1, 0), (0, 0, 1), (0, 1, 1), (1, 0, 1), (1, 1, 0),
             (1, 1, 1)]"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __hash__(self) -> Any:
        """LinearMatroid.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 1278)

        Return an invariant of the matroid.

        This function is called when matroids are added to a set. It is very
        desirable to override it so it can distinguish matroids on the same
        groundset, which is a very typical use case!

        .. WARNING::

            This method is linked to ``__richcmp__`` (in Cython) and ``__cmp__``
            or ``__eq__``/``__ne__`` (in Python). If you override one, you
            should (and, in Cython, \\emph{must}) override the other!

        EXAMPLES::

            sage: M1 = Matroid(groundset='abcde', matrix=Matrix(GF(7),
            ....:                         [[1, 0, 1, 1, 1], [0, 1, 1, 2, 3]]))
            sage: M2 = Matroid(groundset='abcde', matrix=Matrix(GF(7),
            ....:                         [[0, 1, 1, 2, 3], [1, 0, 1, 1, 1]]))
            sage: hash(M1) == hash(M2)
            True
            sage: M2 = M1.dual()
            sage: hash(M1) == hash(M2)
            False"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __reduce__(self) -> Any:
        """LinearMatroid.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 2923)

        Save the matroid for later reloading.

        OUTPUT:

        A tuple ``(unpickle_lean_linear_matroid, (version, data))``, where
        ``unpickle_lean_linear_matroid`` is the name of a function that, when
        called with ``(version, data)``, produces a matroid isomorphic to
        ``self``. ``version`` is an integer (currently 0) and ``data`` is a
        tuple ``(A, E, reduced, name)`` where ``A`` is the representation
        matrix, ``E`` is the groundset of the matroid, ``reduced`` is a
        boolean indicating whether ``A`` is a reduced matrix, and ``name`` is
        a custom name.

        .. WARNING::

            Users should never call this function directly.

        EXAMPLES::

            sage: M = Matroid(Matrix(GF(7), [[1, 0, 0, 1, 1], [0, 1, 0, 1, 2],
            ....:                                           [0, 0, 1, 1, 3]]))
            sage: M == loads(dumps(M))  # indirect doctest
            True
            sage: M.rename('U35')
            sage: loads(dumps(M))
            U35
            sage: M = Matroid(Matrix(GF(7), [[1, 0, 1], [1, 0, 1]]))
            sage: N = loads(dumps(M))
            sage: N.representation()
            [1 0 1]
            [1 0 1]"""

class QuaternaryMatroid(LinearMatroid):
    """QuaternaryMatroid(matrix=None, groundset=None, reduced_matrix=None, ring=None, keep_initial_representation=True, basis=None)

    File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 4916)

    Quaternary matroids.

    A quaternary matroid is a linear matroid represented over the finite field
    with four elements. See :class:`LinearMatroid` for a definition.

    The simplest way to create a ``QuaternaryMatroid`` is by giving only a
    matrix `A`. Then, the groundset defaults to ``range(A.ncols())``. Any
    iterable object `E` can be given as a groundset. If `E` is a list, then
    ``E[i]`` will label the `i`-th column of `A`. Another possibility is to
    specify a 'reduced' matrix `B`, to create the matroid induced by
    `A = [I\\ \\ B]`.

    INPUT:

    - ``matrix`` -- (default: ``None``) a matrix whose column vectors
      represent the matroid.
    - ``reduced_matrix`` -- (default: ``None``) a matrix `B` such that
      `[I\\ \\ B]` represents the matroid, where `I` is an identity matrix with
      the same number of rows as `B`. Only one of ``matrix`` and
      ``reduced_matrix`` should be provided.
    - ``groundset`` -- (default: ``None``) an iterable containing the element
      labels. When provided, must have the correct number of elements:
      the number of columns of ``matrix`` or the number of rows plus the
      number of columns of ``reduced_matrix``.
    - ``ring`` -- (default: ``None``) must be a copy of `\\GF{4}`
    - ``keep_initial_representation`` -- boolean (default: ``True``); decides
      whether or not an internal copy of the input matrix should be preserved.
      This can help to see the structure of the matroid (e.g. in the case of
      graphic matroids), and makes it easier to look at extensions. However,
      the input matrix may have redundant rows, and sometimes it is desirable
      to store only a row-reduced copy.
    - ``basis`` -- (default: ``None``) when provided, this is an ordered
      subset of ``groundset``, such that the submatrix of ``matrix`` indexed
      by ``basis`` is an identity matrix. In this case, no row reduction takes
      place in the initialization phase.

    OUTPUT: a ``QuaternaryMatroid`` instance based on the data above

    .. NOTE::

        The recommended way to generate a quaternary matroid is through the
        :func:`Matroid() <sage.matroids.constructor.Matroid>` function. This
        is usually the preferred way, since it automatically chooses between
        ``QuaternaryMatroid`` and other classes. For direct access to the
        ``QuaternaryMatroid`` constructor, run::

            sage: from sage.matroids.advanced import *

    EXAMPLES::

        sage: # needs sage.rings.finite_rings
        sage: GF4 = GF(4, 'x')
        sage: x = GF4.gens()[0]
        sage: A = Matrix(GF4, 2, 4, [[1, 0, 1, 1], [0, 1, 1, x]])
        sage: M = Matroid(A)
        sage: M
        Quaternary matroid of rank 2 on 4 elements
        sage: sorted(M.groundset())
        [0, 1, 2, 3]
        sage: Matrix(M)
        [1 0 1 1]
        [0 1 1 x]
        sage: M = Matroid(matrix=A, groundset='abcd')
        sage: sorted(M.groundset())
        ['a', 'b', 'c', 'd']
        sage: GF4p = GF(4, 'y')
        sage: y = GF4p.gens()[0]
        sage: B = Matrix(GF4p, 2, 2, [[1, 1], [1, y]])
        sage: N = Matroid(reduced_matrix=B, groundset='abcd')
        sage: M == N
        False"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, matrix=..., groundset=..., reduced_matrix=..., ring=..., keep_initial_representation=..., basis=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 4990)

                See the class definition for full documentation.

                .. NOTE::

                    The extra argument ``basis``, when provided, is an ordered list of
                    elements of the groundset, ordered such that they index a standard
                    identity matrix within ``matrix``.

                EXAMPLES::

                    sage: from sage.matroids.advanced import *
                    sage: QuaternaryMatroid(matrix=Matrix(GF(4, 'x'),         # indirect doctest            # needs sage.rings.finite_rings
                    ....:                                 [[1, 0, 1, 1, 1],
                    ....:                                  [0, 1, 1, 1, 1]]))
                    Quaternary matroid of rank 2 on 5 elements
        """
    def base_ring(self) -> Any:
        """QuaternaryMatroid.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 5058)

        Return the base ring of the matrix representing the matroid, in this
        case `\\GF{4}`.

        EXAMPLES::

            sage: M = Matroid(ring=GF(4, 'y'), reduced_matrix=[[1, 0, 1],               # needs sage.rings.finite_rings
            ....:                                              [0, 1, 1]])
            sage: M.base_ring()                                                         # needs sage.rings.finite_rings
            Finite Field in y of size 2^2"""
    def bicycle_dimension(self) -> Any:
        """QuaternaryMatroid.bicycle_dimension(self)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 5373)

        Return the bicycle dimension of the quaternary matroid.

        The bicycle dimension of a linear subspace `V` is
        `\\dim(V\\cap V^\\perp)`. We use the inner product
        `< v, w >=v_1 w_1^* + ... + v_n w_n^*`, where `w_i^*` is obtained from
        `w_i` by applying the unique nontrivial field automorphism of
        `\\GF{4}`.

        The bicycle dimension of a matroid equals the bicycle dimension of its
        rowspace, and is a matroid invariant. See [Pen2012]_.

        OUTPUT: integer

        EXAMPLES::

            sage: M = matroids.catalog.Q10()                                            # needs sage.rings.finite_rings
            sage: M.bicycle_dimension()                                                 # needs sage.rings.finite_rings
            0"""
    @overload
    def characteristic(self) -> Any:
        """QuaternaryMatroid.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 5072)

        Return the characteristic of the base ring of the matrix representing
        the matroid, in this case `2`.

        EXAMPLES::

            sage: M = Matroid(ring=GF(4, 'y'), reduced_matrix=[[1, 0, 1],               # needs sage.rings.finite_rings
            ....:                                              [0, 1, 1]])
            sage: M.characteristic()                                                    # needs sage.rings.finite_rings
            2"""
    @overload
    def characteristic(self) -> Any:
        """QuaternaryMatroid.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 5072)

        Return the characteristic of the base ring of the matrix representing
        the matroid, in this case `2`.

        EXAMPLES::

            sage: M = Matroid(ring=GF(4, 'y'), reduced_matrix=[[1, 0, 1],               # needs sage.rings.finite_rings
            ....:                                              [0, 1, 1]])
            sage: M.characteristic()                                                    # needs sage.rings.finite_rings
            2"""
    def is_valid(self, certificate=...) -> Any:
        """QuaternaryMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 5506)

        Test if the data obey the matroid axioms.

        Since this is a linear matroid over the field `\\GF{4}`, this is always
        the case.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: ``True``, or ``(True, {})``

        EXAMPLES::

            sage: M = Matroid(Matrix(GF(4, 'x'), [[]]))                                 # needs sage.rings.finite_rings
            sage: M.is_valid()                                                          # needs sage.rings.finite_rings
            True"""
    @overload
    def relabel(self, mapping) -> Any:
        '''QuaternaryMatroid.relabel(self, mapping)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 5585)

        Return an isomorphic matroid with relabeled groundset.

        The output is obtained by relabeling each element `e` by
        ``mapping[e]``, where ``mapping`` is a given injective map. If
        ``mapping[e]`` is not defined, then the identity map is assumed.

        INPUT:

        - ``mapping`` -- a Python object such that ``mapping[e]`` is the new
          label of `e`

        OUTPUT: matroid

        EXAMPLES::

            sage: M = matroids.catalog.RelaxedNonFano("abcdefg")
            sage: sorted(M.groundset())
            [\'a\', \'b\', \'c\', \'d\', \'e\', \'f\', \'g\']
            sage: N = M.relabel({\'g\':\'x\'})
            sage: sorted(N.groundset())
            [\'a\', \'b\', \'c\', \'d\', \'e\', \'f\', \'x\']

        TESTS::

            sage: M = matroids.catalog.RelaxedNonFano("abcdefg")
            sage: f = {\'a\': 1, \'b\': 2, \'c\': 3, \'d\': 4, \'e\': 5, \'f\': 6, \'g\': 7}
            sage: N = M.relabel(f)
            sage: for S in powerset(M.groundset()):
            ....:     assert M.rank(S) == N.rank([f[x] for x in S])'''
    @overload
    def relabel(self, f) -> Any:
        '''QuaternaryMatroid.relabel(self, mapping)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 5585)

        Return an isomorphic matroid with relabeled groundset.

        The output is obtained by relabeling each element `e` by
        ``mapping[e]``, where ``mapping`` is a given injective map. If
        ``mapping[e]`` is not defined, then the identity map is assumed.

        INPUT:

        - ``mapping`` -- a Python object such that ``mapping[e]`` is the new
          label of `e`

        OUTPUT: matroid

        EXAMPLES::

            sage: M = matroids.catalog.RelaxedNonFano("abcdefg")
            sage: sorted(M.groundset())
            [\'a\', \'b\', \'c\', \'d\', \'e\', \'f\', \'g\']
            sage: N = M.relabel({\'g\':\'x\'})
            sage: sorted(N.groundset())
            [\'a\', \'b\', \'c\', \'d\', \'e\', \'f\', \'x\']

        TESTS::

            sage: M = matroids.catalog.RelaxedNonFano("abcdefg")
            sage: f = {\'a\': 1, \'b\': 2, \'c\': 3, \'d\': 4, \'e\': 5, \'f\': 6, \'g\': 7}
            sage: N = M.relabel(f)
            sage: for S in powerset(M.groundset()):
            ....:     assert M.rank(S) == N.rank([f[x] for x in S])'''
    def __reduce__(self) -> Any:
        """QuaternaryMatroid.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 5527)

        Save the matroid for later reloading.

        OUTPUT:

        A tuple ``(unpickle_quaternary_matroid, (version, data))``, where
        ``unpickle_quaternary_matroid`` is the name of a function that,
        when called with ``(version, data)``, produces a matroid isomorphic to
        ``self``. ``version`` is an integer (currently 0) and ``data`` is a
        tuple ``(A, E, B, name)`` where ``A`` is the representation
        matrix, ``E`` is the groundset of the matroid, ``B`` is the currently
        displayed basis, and ``name`` is a custom name.

        .. WARNING::

            Users should never call this function directly.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: M = Matroid(Matrix(GF(4, 'x'), [[1, 0, 0, 1], [0, 1, 0, 1],
            ....:            [0, 0, 1, 1]]))
            sage: M == loads(dumps(M))  # indirect doctest
            True
            sage: M.rename('U34')
            sage: loads(dumps(M))
            U34

        TESTS:

        Check that :issue:`23437` is fixed::

            sage: from sage.matroids.advanced import QuaternaryMatroid
            sage: X_bin = matroids.catalog.Fano().representation()
            sage: X = Matrix(GF(4), X_bin)                                              # needs sage.rings.finite_rings
            sage: M = QuaternaryMatroid(matrix=X).dual()                                # needs sage.rings.finite_rings
            sage: B = list(M.bases())                                                   # needs sage.rings.finite_rings
            sage: N = loads(dumps(M))                                                   # needs sage.rings.finite_rings
            sage: N.closure(frozenset({3}))                                             # needs sage.rings.finite_rings
            frozenset({3})
            sage: N.is_isomorphic(M)                                                    # needs sage.rings.finite_rings
            True"""

class RegularMatroid(LinearMatroid):
    """RegularMatroid(matrix=None, groundset=None, reduced_matrix=None, ring=None, keep_initial_representation=True)

    File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 5624)

    Regular matroids.

    A regular matroid is a linear matroid represented over the integers by a
    totally unimodular matrix.

    The simplest way to create a ``RegularMatroid`` is by giving only a matrix
    `A`. Then, the groundset defaults to ``range(A.ncols())``.
    Any iterable object `E` can be given as a groundset. If `E` is a list, then ``E[i]`` will label the `i`-th column of `A`.
    Another possibility is to specify a 'reduced' matrix `B`, to create the matroid induced by `A = [ I B ]`.

    INPUT:

    - ``matrix`` -- (default: ``None``) a matrix whose column vectors
      represent the matroid.
    - ``reduced_matrix`` -- (default: ``None``) a matrix `B` such that
      `[I\\ \\ B]` represents the matroid, where `I` is an identity matrix with
      the same number of rows as `B`. Only one of ``matrix`` and
      ``reduced_matrix`` should be provided.
    - ``groundset`` -- (default: ``None``) an iterable containing the element
      labels. When provided, must have the correct number of elements: the
      number of columns of ``matrix`` or the number of rows plus the number of
      columns of ``reduced_matrix``.
    - ``ring`` -- (default: ``None``) ignored
    - ``keep_initial_representation`` -- boolean (default: ``True``); decides
      whether or not an internal copy of the input matrix should be preserved.
      This can help to see the structure of the matroid (e.g. in the case of
      graphic matroids), and makes it easier to look at extensions. However,
      the input matrix may have redundant rows, and sometimes it is desirable
      to store only a row-reduced copy.
    - ``basis`` -- (default: ``None``) when provided, this is an ordered
      subset of ``groundset``, such that the submatrix of ``matrix`` indexed
      by ``basis`` is an identity matrix. In this case, no row reduction takes
      place in the initialization phase.

    OUTPUT: a ``RegularMatroid`` instance based on the data above

    .. NOTE::

        The recommended way to generate a regular matroid is through the
        :func:`Matroid() <sage.matroids.constructor.Matroid>` function. This
        is usually the preferred way, since it automatically chooses between
        ``RegularMatroid`` and other classes. Moreover, it will test whether
        the input actually yields a regular matroid, unlike this class.
        For direct access to the ``RegularMatroid`` constructor, run::

            sage: from sage.matroids.advanced import *

    .. WARNING::

        No checks are performed to ensure the input data form an actual regular
        matroid! If not, the behavior is unpredictable, and the internal
        representation can get corrupted. If in doubt, run
        :meth:`self.is_valid() <RegularMatroid.is_valid>` to ensure the data
        are as desired.

    EXAMPLES::

        sage: A = Matrix(ZZ, 2, 4, [[1, 0, 1, 1], [0, 1, 1, 1]])
        sage: M = Matroid(A, regular=True); M                                           # needs sage.graphs
        Regular matroid of rank 2 on 4 elements with 5 bases
        sage: sorted(M.groundset())                                                     # needs sage.graphs
        [0, 1, 2, 3]
        sage: Matrix(M)                                                                 # needs sage.graphs
        [1 0 1 1]
        [0 1 1 1]
        sage: M = Matroid(matrix=A, groundset='abcd', regular=True)                     # needs sage.graphs
        sage: sorted(M.groundset())                                                     # needs sage.graphs
        ['a', 'b', 'c', 'd']"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, matrix=..., groundset=..., reduced_matrix=..., ring=..., keep_initial_representation=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 5695)

                See the class definition for full documentation.

                .. NOTE::

                    The extra argument ``basis``, when provided, is an ordered list of
                    elements of the groundset, ordered such that they index a standard
                    identity matrix within ``matrix``.

                EXAMPLES::

                    sage: from sage.matroids.advanced import *
                    sage: RegularMatroid(matrix=Matrix(ZZ, [[1, 0, 1, 1, 1],    # indirect doctest          # needs sage.graphs
                    ....:                                   [0, 1, 1, 1, 1]]))
                    Regular matroid of rank 2 on 5 elements with 7 bases
        """
    def base_ring(self) -> Any:
        """RegularMatroid.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 5757)

        Return the base ring of the matrix representing the matroid, in this
        case `\\ZZ`.

        EXAMPLES::

            sage: M = matroids.catalog.R10()
            sage: M.base_ring()
            Integer Ring"""
    @overload
    def bases_count(self) -> Any:
        """RegularMatroid.bases_count(self)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 5840)

        Count the number of bases.

        EXAMPLES::

            sage: M = Matroid(graphs.CompleteGraph(5), regular=True)                    # needs sage.graphs
            sage: M.bases_count()                                                       # needs sage.graphs
            125

        ALGORITHM:

        Since the matroid is regular, we use Kirchhoff's Matrix-Tree Theorem.
        See also :wikipedia:`Kirchhoff%27s_theorem`."""
    @overload
    def bases_count(self) -> Any:
        """RegularMatroid.bases_count(self)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 5840)

        Count the number of bases.

        EXAMPLES::

            sage: M = Matroid(graphs.CompleteGraph(5), regular=True)                    # needs sage.graphs
            sage: M.bases_count()                                                       # needs sage.graphs
            125

        ALGORITHM:

        Since the matroid is regular, we use Kirchhoff's Matrix-Tree Theorem.
        See also :wikipedia:`Kirchhoff%27s_theorem`."""
    @overload
    def binary_matroid(self, randomized_tests=..., verify=...) -> Any:
        """RegularMatroid.binary_matroid(self, randomized_tests=1, verify=True)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 6342)

        Return a binary matroid representing ``self``.

        INPUT:

        - ``randomized_tests`` -- ignored
        - ``verify`` -- ignored

        OUTPUT: a binary matroid

        ALGORITHM:

        ``self`` is a regular matroid, so just cast ``self`` to a BinaryMatroid.

        .. SEEALSO::

            :meth:`M.binary_matroid()
            <sage.matroids.matroid.Matroid.binary_matroid>`

        EXAMPLES::

            sage: N = matroids.catalog.R10()
            sage: N.binary_matroid()
            Binary matroid of rank 5 on 10 elements, type (1, None)"""
    @overload
    def binary_matroid(self) -> Any:
        """RegularMatroid.binary_matroid(self, randomized_tests=1, verify=True)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 6342)

        Return a binary matroid representing ``self``.

        INPUT:

        - ``randomized_tests`` -- ignored
        - ``verify`` -- ignored

        OUTPUT: a binary matroid

        ALGORITHM:

        ``self`` is a regular matroid, so just cast ``self`` to a BinaryMatroid.

        .. SEEALSO::

            :meth:`M.binary_matroid()
            <sage.matroids.matroid.Matroid.binary_matroid>`

        EXAMPLES::

            sage: N = matroids.catalog.R10()
            sage: N.binary_matroid()
            Binary matroid of rank 5 on 10 elements, type (1, None)"""
    @overload
    def binary_matroid(self) -> Any:
        """RegularMatroid.binary_matroid(self, randomized_tests=1, verify=True)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 6342)

        Return a binary matroid representing ``self``.

        INPUT:

        - ``randomized_tests`` -- ignored
        - ``verify`` -- ignored

        OUTPUT: a binary matroid

        ALGORITHM:

        ``self`` is a regular matroid, so just cast ``self`` to a BinaryMatroid.

        .. SEEALSO::

            :meth:`M.binary_matroid()
            <sage.matroids.matroid.Matroid.binary_matroid>`

        EXAMPLES::

            sage: N = matroids.catalog.R10()
            sage: N.binary_matroid()
            Binary matroid of rank 5 on 10 elements, type (1, None)"""
    @overload
    def characteristic(self) -> Any:
        """RegularMatroid.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 5770)

        Return the characteristic of the base ring of the matrix representing
        the matroid, in this case `0`.

        EXAMPLES::

            sage: M = matroids.catalog.R10()
            sage: M.characteristic()
            0"""
    @overload
    def characteristic(self) -> Any:
        """RegularMatroid.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 5770)

        Return the characteristic of the base ring of the matrix representing
        the matroid, in this case `0`.

        EXAMPLES::

            sage: M = matroids.catalog.R10()
            sage: M.characteristic()
            0"""
    def has_line_minor(self, k, hyperlines=..., certificate=...) -> Any:
        """RegularMatroid.has_line_minor(self, k, hyperlines=None, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 6174)

        Test if the matroid has a `U_{2, k}`-minor.

        The matroid `U_{2, k}` is a matroid on `k` elements in which every
        subset of at most 2 elements is independent, and every subset of more
        than two elements is dependent.

        The optional argument ``hyperlines`` restricts the search space: this
        method returns ``True`` if `si(M/F)` is isomorphic to `U_{2, l}` with
        `l \\geq k` for some `F` in ``hyperlines``, and ``False`` otherwise.

        INPUT:

        - ``k`` -- the length of the line minor
        - ``hyperlines`` -- (default: ``None``) a set of flats of codimension
          2. Defaults to the set of all flats of codimension 2.
        - ``certificate`` -- (default: ``False``) if ``True`` returns
          ``True, F``, where ``F`` is a flat and ``self.minor(contractions=F)``
          has a `U_{2,k}` restriction or ``False, None``

        OUTPUT: boolean or tuple

        .. SEEALSO::

            :meth:`Matroid.has_minor() <sage.matroids.matroid.Matroid.has_minor>`

        EXAMPLES::

            sage: M = matroids.catalog.R10()
            sage: M.has_line_minor(4)
            False
            sage: M.has_line_minor(4, certificate=True)
            (False, None)
            sage: M.has_line_minor(3)
            True
            sage: M.has_line_minor(3, certificate=True)
            (True, frozenset({'a', 'b', 'c', 'g'}))
            sage: M.has_line_minor(k=3, hyperlines=[['a', 'b', 'c'],
            ....:                                   ['a', 'b', 'd' ]])
            True
            sage: M.has_line_minor(k=3, hyperlines=[['a', 'b', 'c'],
            ....:                                   ['a', 'b', 'd' ]], certificate=True)
            (True, frozenset({'a', 'b', 'c'}))"""
    @overload
    def is_binary(self, randomized_tests=...) -> Any:
        """RegularMatroid.is_binary(self, randomized_tests=1)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 6371)

        Decide if ``self`` is a binary matroid.

        INPUT:

        - ``randomized_tests`` -- ignored

        OUTPUT: boolean

        ALGORITHM:

        ``self`` is a regular matroid, so just return ``True``.

        .. SEEALSO::

            :meth:`M.is_binary() <sage.matroids.matroid.Matroid.is_binary>`

        EXAMPLES::

            sage: N = matroids.catalog.R10()
            sage: N.is_binary()
            True"""
    @overload
    def is_binary(self) -> Any:
        """RegularMatroid.is_binary(self, randomized_tests=1)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 6371)

        Decide if ``self`` is a binary matroid.

        INPUT:

        - ``randomized_tests`` -- ignored

        OUTPUT: boolean

        ALGORITHM:

        ``self`` is a regular matroid, so just return ``True``.

        .. SEEALSO::

            :meth:`M.is_binary() <sage.matroids.matroid.Matroid.is_binary>`

        EXAMPLES::

            sage: N = matroids.catalog.R10()
            sage: N.is_binary()
            True"""
    @overload
    def is_binary(self) -> Any:
        """RegularMatroid.is_binary(self, randomized_tests=1)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 6371)

        Decide if ``self`` is a binary matroid.

        INPUT:

        - ``randomized_tests`` -- ignored

        OUTPUT: boolean

        ALGORITHM:

        ``self`` is a regular matroid, so just return ``True``.

        .. SEEALSO::

            :meth:`M.is_binary() <sage.matroids.matroid.Matroid.is_binary>`

        EXAMPLES::

            sage: N = matroids.catalog.R10()
            sage: N.is_binary()
            True"""
    @overload
    def is_graphic(self) -> bool:
        """RegularMatroid.is_graphic(self) -> bool

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 6262)

        Test if the regular matroid is graphic.

        A matroid is *graphic* if there exists a graph whose edge set equals
        the groundset of the matroid, such that a subset of elements of the
        matroid is independent if and only if the corresponding subgraph is
        acyclic.

        OUTPUT: boolean

        EXAMPLES::

            sage: M = matroids.catalog.R10()
            sage: M.is_graphic()
            False
            sage: M = Matroid(graphs.CompleteGraph(5), regular=True)                    # needs sage.graphs
            sage: M.is_graphic()                                                        # needs sage.graphs sage.rings.finite_rings
            True
            sage: M.dual().is_graphic()                                                 # needs sage.graphs
            False

        ALGORITHM:

        In a recent paper, Geelen and Gerards [GG2012]_ reduced the problem to
        testing if a system of linear equations has a solution. While not the
        fastest method, and not necessarily constructive (in the presence of
        2-separations especially), it is easy to implement."""
    @overload
    def is_graphic(self) -> Any:
        """RegularMatroid.is_graphic(self) -> bool

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 6262)

        Test if the regular matroid is graphic.

        A matroid is *graphic* if there exists a graph whose edge set equals
        the groundset of the matroid, such that a subset of elements of the
        matroid is independent if and only if the corresponding subgraph is
        acyclic.

        OUTPUT: boolean

        EXAMPLES::

            sage: M = matroids.catalog.R10()
            sage: M.is_graphic()
            False
            sage: M = Matroid(graphs.CompleteGraph(5), regular=True)                    # needs sage.graphs
            sage: M.is_graphic()                                                        # needs sage.graphs sage.rings.finite_rings
            True
            sage: M.dual().is_graphic()                                                 # needs sage.graphs
            False

        ALGORITHM:

        In a recent paper, Geelen and Gerards [GG2012]_ reduced the problem to
        testing if a system of linear equations has a solution. While not the
        fastest method, and not necessarily constructive (in the presence of
        2-separations especially), it is easy to implement."""
    @overload
    def is_graphic(self) -> Any:
        """RegularMatroid.is_graphic(self) -> bool

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 6262)

        Test if the regular matroid is graphic.

        A matroid is *graphic* if there exists a graph whose edge set equals
        the groundset of the matroid, such that a subset of elements of the
        matroid is independent if and only if the corresponding subgraph is
        acyclic.

        OUTPUT: boolean

        EXAMPLES::

            sage: M = matroids.catalog.R10()
            sage: M.is_graphic()
            False
            sage: M = Matroid(graphs.CompleteGraph(5), regular=True)                    # needs sage.graphs
            sage: M.is_graphic()                                                        # needs sage.graphs sage.rings.finite_rings
            True
            sage: M.dual().is_graphic()                                                 # needs sage.graphs
            False

        ALGORITHM:

        In a recent paper, Geelen and Gerards [GG2012]_ reduced the problem to
        testing if a system of linear equations has a solution. While not the
        fastest method, and not necessarily constructive (in the presence of
        2-separations especially), it is easy to implement."""
    @overload
    def is_graphic(self) -> Any:
        """RegularMatroid.is_graphic(self) -> bool

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 6262)

        Test if the regular matroid is graphic.

        A matroid is *graphic* if there exists a graph whose edge set equals
        the groundset of the matroid, such that a subset of elements of the
        matroid is independent if and only if the corresponding subgraph is
        acyclic.

        OUTPUT: boolean

        EXAMPLES::

            sage: M = matroids.catalog.R10()
            sage: M.is_graphic()
            False
            sage: M = Matroid(graphs.CompleteGraph(5), regular=True)                    # needs sage.graphs
            sage: M.is_graphic()                                                        # needs sage.graphs sage.rings.finite_rings
            True
            sage: M.dual().is_graphic()                                                 # needs sage.graphs
            False

        ALGORITHM:

        In a recent paper, Geelen and Gerards [GG2012]_ reduced the problem to
        testing if a system of linear equations has a solution. While not the
        fastest method, and not necessarily constructive (in the presence of
        2-separations especially), it is easy to implement."""
    @overload
    def is_regular(self) -> bool:
        """RegularMatroid.is_regular(self) -> bool

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 6328)

        Return if ``self`` is regular.

        This is trivially ``True`` for a :class:`RegularMatroid`.

        EXAMPLES::

            sage: M = matroids.catalog.R10()
            sage: M.is_regular()
            True"""
    @overload
    def is_regular(self) -> Any:
        """RegularMatroid.is_regular(self) -> bool

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 6328)

        Return if ``self`` is regular.

        This is trivially ``True`` for a :class:`RegularMatroid`.

        EXAMPLES::

            sage: M = matroids.catalog.R10()
            sage: M.is_regular()
            True"""
    @overload
    def is_ternary(self, randomized_tests=...) -> Any:
        """RegularMatroid.is_ternary(self, randomized_tests=1)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 6426)

        Decide if ``self`` is a ternary matroid.

        INPUT:

        - ``randomized_tests`` -- ignored

        OUTPUT: boolean

        ALGORITHM:

        ``self`` is a regular matroid, so just return ``True``.

        .. SEEALSO::

            :meth:`M.is_ternary() <sage.matroids.matroid.Matroid.is_ternary>`

        EXAMPLES::

            sage: N = matroids.catalog.R10()
            sage: N.is_ternary()
            True"""
    @overload
    def is_ternary(self) -> Any:
        """RegularMatroid.is_ternary(self, randomized_tests=1)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 6426)

        Decide if ``self`` is a ternary matroid.

        INPUT:

        - ``randomized_tests`` -- ignored

        OUTPUT: boolean

        ALGORITHM:

        ``self`` is a regular matroid, so just return ``True``.

        .. SEEALSO::

            :meth:`M.is_ternary() <sage.matroids.matroid.Matroid.is_ternary>`

        EXAMPLES::

            sage: N = matroids.catalog.R10()
            sage: N.is_ternary()
            True"""
    @overload
    def is_ternary(self) -> Any:
        """RegularMatroid.is_ternary(self, randomized_tests=1)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 6426)

        Decide if ``self`` is a ternary matroid.

        INPUT:

        - ``randomized_tests`` -- ignored

        OUTPUT: boolean

        ALGORITHM:

        ``self`` is a regular matroid, so just return ``True``.

        .. SEEALSO::

            :meth:`M.is_ternary() <sage.matroids.matroid.Matroid.is_ternary>`

        EXAMPLES::

            sage: N = matroids.catalog.R10()
            sage: N.is_ternary()
            True"""
    def is_valid(self, certificate=...) -> Any:
        """RegularMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 6293)

        Test if the data obey the matroid axioms.

        Since this is a regular matroid, this function tests if the
        representation matrix is *totally unimodular*, i.e. if all square
        submatrices have determinant in `\\{-1, 0, 1\\}`.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, or (boolean, dictionary)

        EXAMPLES::

            sage: # needs sage.graphs
            sage: M = Matroid(Matrix(ZZ, [[1, 0, 0, 1, 1, 0, 1],
            ....:                         [0, 1, 0, 1, 0, 1, 1],
            ....:                         [0, 0, 1, 0, 1, 1, 1]]),
            ....:             regular=True, check=False)
            sage: M.is_valid(certificate=True)
            (False, {'error': 'the representation matrix is not totally unimodular'})
            sage: M = Matroid(graphs.PetersenGraph())
            sage: M.is_valid()
            True"""
    @overload
    def relabel(self, mapping) -> Any:
        """RegularMatroid.relabel(self, mapping)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 6503)

        Return an isomorphic matroid with relabeled groundset.

        The output is obtained by relabeling each element `e` by
        ``mapping[e]``, where ``mapping`` is a given injective map. If
        ``mapping[e]`` is not defined, then the identity map is assumed.

        INPUT:

        - ``mapping`` -- a Python object such that ``mapping[e]`` is the new
          label of `e`

        OUTPUT: matroid

        EXAMPLES::

            sage: M = matroids.catalog.R10()
            sage: sorted(M.groundset())
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
            sage: N = M.relabel({'g': 'x'})
            sage: sorted(N.groundset())
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', 'i', 'j', 'x']

        TESTS::

            sage: M = matroids.catalog.R10()
            sage: f = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}
            sage: N = M.relabel(f)
            sage: for S in powerset(M.groundset()):
            ....:     assert M.rank(S) == N.rank([M._relabel_map(f)[x] for x in S])"""
    @overload
    def relabel(self, f) -> Any:
        """RegularMatroid.relabel(self, mapping)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 6503)

        Return an isomorphic matroid with relabeled groundset.

        The output is obtained by relabeling each element `e` by
        ``mapping[e]``, where ``mapping`` is a given injective map. If
        ``mapping[e]`` is not defined, then the identity map is assumed.

        INPUT:

        - ``mapping`` -- a Python object such that ``mapping[e]`` is the new
          label of `e`

        OUTPUT: matroid

        EXAMPLES::

            sage: M = matroids.catalog.R10()
            sage: sorted(M.groundset())
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
            sage: N = M.relabel({'g': 'x'})
            sage: sorted(N.groundset())
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', 'i', 'j', 'x']

        TESTS::

            sage: M = matroids.catalog.R10()
            sage: f = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}
            sage: N = M.relabel(f)
            sage: for S in powerset(M.groundset()):
            ....:     assert M.rank(S) == N.rank([M._relabel_map(f)[x] for x in S])"""
    @overload
    def ternary_matroid(self, randomized_tests=..., verify=...) -> Any:
        """RegularMatroid.ternary_matroid(self, randomized_tests=1, verify=True)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 6397)

        Return a ternary matroid representing ``self``.

        INPUT:

        - ``randomized_tests`` -- ignored
        - ``verify`` -- ignored

        OUTPUT: a ternary matroid

        ALGORITHM:

        ``self`` is a regular matroid, so just cast ``self`` to a TernaryMatroid.

        .. SEEALSO::

            :meth:`M.ternary_matroid()
            <sage.matroids.matroid.Matroid.ternary_matroid>`

        EXAMPLES::

            sage: N = matroids.catalog.R10()
            sage: N.ternary_matroid()
            Ternary matroid of rank 5 on 10 elements, type 4+"""
    @overload
    def ternary_matroid(self) -> Any:
        """RegularMatroid.ternary_matroid(self, randomized_tests=1, verify=True)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 6397)

        Return a ternary matroid representing ``self``.

        INPUT:

        - ``randomized_tests`` -- ignored
        - ``verify`` -- ignored

        OUTPUT: a ternary matroid

        ALGORITHM:

        ``self`` is a regular matroid, so just cast ``self`` to a TernaryMatroid.

        .. SEEALSO::

            :meth:`M.ternary_matroid()
            <sage.matroids.matroid.Matroid.ternary_matroid>`

        EXAMPLES::

            sage: N = matroids.catalog.R10()
            sage: N.ternary_matroid()
            Ternary matroid of rank 5 on 10 elements, type 4+"""
    @overload
    def ternary_matroid(self) -> Any:
        """RegularMatroid.ternary_matroid(self, randomized_tests=1, verify=True)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 6397)

        Return a ternary matroid representing ``self``.

        INPUT:

        - ``randomized_tests`` -- ignored
        - ``verify`` -- ignored

        OUTPUT: a ternary matroid

        ALGORITHM:

        ``self`` is a regular matroid, so just cast ``self`` to a TernaryMatroid.

        .. SEEALSO::

            :meth:`M.ternary_matroid()
            <sage.matroids.matroid.Matroid.ternary_matroid>`

        EXAMPLES::

            sage: N = matroids.catalog.R10()
            sage: N.ternary_matroid()
            Ternary matroid of rank 5 on 10 elements, type 4+"""
    def __reduce__(self) -> Any:
        """RegularMatroid.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 6454)

        Save the matroid for later reloading.

        OUTPUT:

        A tuple ``(unpickle_regular_matroid, (version, data))``, where
        ``unpickle_regular_matroid`` is the name of a function that, when
        called with ``(version, data)``, produces a matroid isomorphic to
        ``self``. ``version`` is an integer (currently 0) and ``data`` is a
        tuple ``(A, E, reduced, name)`` where ``A`` is the representation
        matrix, ``E`` is the groundset of the matroid, ``reduced`` is a
        boolean indicating whether ``A`` is a reduced matrix, and ``name`` is
        a custom name.

        .. WARNING::

            Users should never call this function directly.

        EXAMPLES::

            sage: from sage.matroids.advanced import *
            sage: M = matroids.catalog.R12()
            sage: M == loads(dumps(M))  # indirect doctest
            True
            sage: M.rename('R_{12}')
            sage: loads(dumps(M))
            R_{12}
            sage: M = RegularMatroid(Matrix(QQ, [[1, 0, 1], [1, 0, 1]]))
            sage: N = loads(dumps(M))
            sage: N.representation()
            [1 0 1]
            [1 0 1]"""

class TernaryMatroid(LinearMatroid):
    """TernaryMatroid(matrix=None, groundset=None, reduced_matrix=None, ring=None, keep_initial_representation=True, basis=None)

    File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 4044)

    Ternary matroids.

    A ternary matroid is a linear matroid represented over the finite field
    with three elements. See :class:`LinearMatroid` for a definition.

    The simplest way to create a ``TernaryMatroid`` is by giving only a
    matrix `A`. Then, the groundset defaults to ``range(A.ncols())``. Any
    iterable object `E` can be given as a groundset. If `E` is a list, then
    ``E[i]`` will label the `i`-th column of `A`. Another possibility is to
    specify a 'reduced' matrix `B`, to create the matroid induced by
    `A = [I\\ \\ B]`.

    INPUT:

    - ``matrix`` -- (default: ``None``) a matrix whose column vectors
      represent the matroid.
    - ``reduced_matrix`` -- (default: ``None``) a matrix `B` such that
      `[I\\ \\ B]` represents the matroid, where `I` is an identity matrix with
      the same number of rows as `B`. Only one of ``matrix`` and
      ``reduced_matrix`` should be provided.
    - ``groundset`` -- (default: ``None``) an iterable containing the element
      labels. When provided, must have the correct number of elements: the
      number of columns of ``matrix`` or the number of rows plus the number
      of columns of ``reduced_matrix``.
    - ``ring`` -- (default: ``None``) ignored
    - ``keep_initial_representation`` -- boolean (default: ``True``); decides
      whether or not an internal copy of the input matrix should be preserved.
      This can help to see the structure of the matroid (e.g. in the case of
      graphic matroids), and makes it easier to look at extensions. However,
      the input matrix may have redundant rows, and sometimes it is desirable
      to store only a row-reduced copy.
    - ``basis`` -- (default: ``None``) when provided, this is an ordered
      subset of ``groundset``, such that the submatrix of ``matrix`` indexed
      by ``basis`` is an identity matrix. In this case, no row reduction takes
      place in the initialization phase.

    OUTPUT: a ``TernaryMatroid`` instance based on the data above

    .. NOTE::

        The recommended way to generate a ternary matroid is through the
        :func:`Matroid() <sage.matroids.constructor.Matroid>` function. This
        is usually the preferred way, since it automatically chooses between
        ``TernaryMatroid`` and other classes. For direct access to the
        ``TernaryMatroid`` constructor, run::

            sage: from sage.matroids.advanced import *

    EXAMPLES::

        sage: A = Matrix(GF(3), 2, 4, [[1, 0, 1, 1], [0, 1, 1, 1]])
        sage: M = Matroid(A); M
        Ternary matroid of rank 2 on 4 elements, type 0-
        sage: sorted(M.groundset())
        [0, 1, 2, 3]
        sage: Matrix(M)
        [1 0 1 1]
        [0 1 1 1]
        sage: M = Matroid(matrix=A, groundset='abcd')
        sage: sorted(M.groundset())
        ['a', 'b', 'c', 'd']
        sage: B = Matrix(GF(2), 2, 2, [[1, 1], [1, 1]])
        sage: N = Matroid(ring=GF(3), reduced_matrix=B, groundset='abcd')               # needs sage.rings.finite_rings
        sage: M == N                                                                    # needs sage.rings.finite_rings
        True"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, matrix=..., groundset=..., reduced_matrix=..., ring=..., keep_initial_representation=..., basis=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 4112)

                See the class definition for full documentation.

                .. NOTE::

                    The extra argument ``basis``, when provided, is an ordered list of
                    elements of the groundset, ordered such that they index a standard
                    identity matrix within ``matrix``.

                EXAMPLES::

                    sage: from sage.matroids.advanced import *
                    sage: TernaryMatroid(matrix=Matrix(GF(5), [[1, 0, 1, 1, 1],       # indirect doctest
                    ....:                                      [0, 1, 1, 2, 3]]))
                    Ternary matroid of rank 2 on 5 elements, type 1+
        """
    def base_ring(self) -> Any:
        """TernaryMatroid.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 4185)

        Return the base ring of the matrix representing the matroid, in this
        case `\\GF{3}`.

        EXAMPLES::

            sage: M = matroids.catalog.NonFano()
            sage: M.base_ring()
            Finite Field of size 3"""
    def bicycle_dimension(self) -> Any:
        """TernaryMatroid.bicycle_dimension(self)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 4548)

        Return the bicycle dimension of the ternary matroid.

        The bicycle dimension of a linear subspace `V` is
        `\\dim(V\\cap V^\\perp)`. The bicycle dimension of a matroid equals the
        bicycle dimension of its rowspace, and is a matroid invariant.
        See [Pen2012]_.

        OUTPUT: integer

        EXAMPLES::

            sage: M = matroids.catalog.NonFano()
            sage: M.bicycle_dimension()
            0"""
    def character(self) -> Any:
        """TernaryMatroid.character(self)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 4569)

        Return the character of the ternary matroid.

        For a linear subspace `V` over `GF(3)` with orthogonal basis
        `q_1, \\ldots, q_k` the character equals the product of `|q_i|`
        modulo 3, where the product ranges over the `i` such that `|q_i|`
        is not divisible by 3. The character does not depend on the choice of
        the orthogonal basis. The character of a ternary matroid equals the
        character of its cocycle-space, and is an invariant for ternary
        matroids. See [Pen2012]_.

        OUTPUT: integer

        EXAMPLES::

            sage: M = matroids.catalog.NonFano()
            sage: M.character()
            2"""
    @overload
    def characteristic(self) -> Any:
        """TernaryMatroid.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 4199)

        Return the characteristic of the base ring of the matrix representing
        the matroid, in this case `3`.

        EXAMPLES::

            sage: M = matroids.catalog.NonFano()
            sage: M.characteristic()
            3"""
    @overload
    def characteristic(self) -> Any:
        """TernaryMatroid.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 4199)

        Return the characteristic of the base ring of the matrix representing
        the matroid, in this case `3`.

        EXAMPLES::

            sage: M = matroids.catalog.NonFano()
            sage: M.characteristic()
            3"""
    @overload
    def is_ternary(self, randomized_tests=...) -> Any:
        """TernaryMatroid.is_ternary(self, randomized_tests=1)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 4789)

        Decide if ``self`` is a binary matroid.

        INPUT:

        - ``randomized_tests`` -- ignored

        OUTPUT: boolean

        ALGORITHM:

        ``self`` is a ternary matroid, so just return ``True``.

        .. SEEALSO::

            :meth:`M.is_ternary() <sage.matroids.matroid.Matroid.is_ternary>`

        EXAMPLES::

            sage: N = matroids.catalog.NonFano()
            sage: N.is_ternary()
            True"""
    @overload
    def is_ternary(self) -> Any:
        """TernaryMatroid.is_ternary(self, randomized_tests=1)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 4789)

        Decide if ``self`` is a binary matroid.

        INPUT:

        - ``randomized_tests`` -- ignored

        OUTPUT: boolean

        ALGORITHM:

        ``self`` is a ternary matroid, so just return ``True``.

        .. SEEALSO::

            :meth:`M.is_ternary() <sage.matroids.matroid.Matroid.is_ternary>`

        EXAMPLES::

            sage: N = matroids.catalog.NonFano()
            sage: N.is_ternary()
            True"""
    @overload
    def is_ternary(self) -> Any:
        """TernaryMatroid.is_ternary(self, randomized_tests=1)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 4789)

        Decide if ``self`` is a binary matroid.

        INPUT:

        - ``randomized_tests`` -- ignored

        OUTPUT: boolean

        ALGORITHM:

        ``self`` is a ternary matroid, so just return ``True``.

        .. SEEALSO::

            :meth:`M.is_ternary() <sage.matroids.matroid.Matroid.is_ternary>`

        EXAMPLES::

            sage: N = matroids.catalog.NonFano()
            sage: N.is_ternary()
            True"""
    def is_valid(self, certificate=...) -> Any:
        """TernaryMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 4738)

        Test if the data obey the matroid axioms.

        Since this is a linear matroid over the field `\\GF{3}`, this is always
        the case.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: ``True``, or ``(True, {})``

        EXAMPLES::

            sage: M = Matroid(Matrix(GF(3), [[]]))
            sage: M.is_valid()
            True"""
    @overload
    def relabel(self, mapping) -> Any:
        """TernaryMatroid.relabel(self, mapping)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 4877)

        Return an isomorphic matroid with relabeled groundset.

        The output is obtained by relabeling each element `e` by
        ``mapping[e]``, where ``mapping`` is a given injective map. If
        ``mapping[e]`` is not defined, then the identity map is assumed.

        INPUT:

        - ``mapping`` -- a Python object such that ``mapping[e]`` is the new
          label of `e`

        OUTPUT: matroid

        EXAMPLES::

            sage: M = matroids.catalog.NonFano()
            sage: sorted(M.groundset())
            ['a', 'b', 'c', 'd', 'e', 'f', 'g']
            sage: N = M.relabel({'g': 'x'})
            sage: sorted(N.groundset())
            ['a', 'b', 'c', 'd', 'e', 'f', 'x']

        TESTS::

            sage: M = matroids.catalog.NonFano()
            sage: f = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}
            sage: N = M.relabel(f)
            sage: for S in powerset(M.groundset()):
            ....:     assert M.rank(S) == N.rank([f[x] for x in S])"""
    @overload
    def relabel(self, f) -> Any:
        """TernaryMatroid.relabel(self, mapping)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 4877)

        Return an isomorphic matroid with relabeled groundset.

        The output is obtained by relabeling each element `e` by
        ``mapping[e]``, where ``mapping`` is a given injective map. If
        ``mapping[e]`` is not defined, then the identity map is assumed.

        INPUT:

        - ``mapping`` -- a Python object such that ``mapping[e]`` is the new
          label of `e`

        OUTPUT: matroid

        EXAMPLES::

            sage: M = matroids.catalog.NonFano()
            sage: sorted(M.groundset())
            ['a', 'b', 'c', 'd', 'e', 'f', 'g']
            sage: N = M.relabel({'g': 'x'})
            sage: sorted(N.groundset())
            ['a', 'b', 'c', 'd', 'e', 'f', 'x']

        TESTS::

            sage: M = matroids.catalog.NonFano()
            sage: f = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}
            sage: N = M.relabel(f)
            sage: for S in powerset(M.groundset()):
            ....:     assert M.rank(S) == N.rank([f[x] for x in S])"""
    @overload
    def ternary_matroid(self, randomized_tests=..., verify=...) -> Any:
        """TernaryMatroid.ternary_matroid(self, randomized_tests=1, verify=True)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 4761)

        Return a ternary matroid representing ``self``.

        INPUT:

        - ``randomized_tests`` -- ignored
        - ``verify`` -- ignored

        OUTPUT: a binary matroid

        ALGORITHM:

        ``self`` is a ternary matroid, so just return ``self``.

        .. SEEALSO::

            :meth:`M.ternary_matroid()
            <sage.matroids.matroid.Matroid.ternary_matroid>`

        EXAMPLES::

            sage: N = matroids.catalog.NonFano()
            sage: N.ternary_matroid() is N
            True"""
    @overload
    def ternary_matroid(self) -> Any:
        """TernaryMatroid.ternary_matroid(self, randomized_tests=1, verify=True)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 4761)

        Return a ternary matroid representing ``self``.

        INPUT:

        - ``randomized_tests`` -- ignored
        - ``verify`` -- ignored

        OUTPUT: a binary matroid

        ALGORITHM:

        ``self`` is a ternary matroid, so just return ``self``.

        .. SEEALSO::

            :meth:`M.ternary_matroid()
            <sage.matroids.matroid.Matroid.ternary_matroid>`

        EXAMPLES::

            sage: N = matroids.catalog.NonFano()
            sage: N.ternary_matroid() is N
            True"""
    @overload
    def ternary_matroid(self) -> Any:
        """TernaryMatroid.ternary_matroid(self, randomized_tests=1, verify=True)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 4761)

        Return a ternary matroid representing ``self``.

        INPUT:

        - ``randomized_tests`` -- ignored
        - ``verify`` -- ignored

        OUTPUT: a binary matroid

        ALGORITHM:

        ``self`` is a ternary matroid, so just return ``self``.

        .. SEEALSO::

            :meth:`M.ternary_matroid()
            <sage.matroids.matroid.Matroid.ternary_matroid>`

        EXAMPLES::

            sage: N = matroids.catalog.NonFano()
            sage: N.ternary_matroid() is N
            True"""
    def __reduce__(self) -> Any:
        """TernaryMatroid.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/linear_matroid.pyx (starting at line 4815)

        Save the matroid for later reloading.

        OUTPUT:

        A tuple ``(unpickle_ternary_matroid, (version, data))``, where
        ``unpickle_ternary_matroid`` is the name of a function that, when
        called with ``(version, data)``, produces a matroid isomorphic to
        ``self``. ``version`` is an integer (currently 0) and ``data`` is a
        tuple ``(A, E, B, name)`` where ``A`` is the representation
        matrix, ``E`` is the groundset of the matroid, ``B`` is the currently
        displayed basis, and ``name`` is a custom name.

        .. WARNING::

            Users should never call this function directly.

        EXAMPLES::

            sage: from sage.matroids.advanced import *
            sage: M = TernaryMatroid(Matrix(GF(3), [[1, 0, 0, 1],
            ....:              [0, 1, 0, 1], [0, 0, 1, 1]]))
            sage: M == loads(dumps(M))  # indirect doctest
            True
            sage: M.rename('U34')
            sage: loads(dumps(M))
            U34
            sage: M = TernaryMatroid(Matrix(GF(3), [[1, 0, 1], [1, 0, 1]]))
            sage: loads(dumps(M)).representation()
            [1 0 1]
            [1 0 1]

        TESTS:

        Check that :issue:`23437` is fixed::

            sage: from sage.matroids.advanced import *
            sage: X_bin = matroids.catalog.Fano().representation()
            sage: X = Matrix(GF(3), X_bin)                                              # needs sage.rings.finite_rings
            sage: M = TernaryMatroid(matrix=X).dual()                                   # needs sage.rings.finite_rings
            sage: B = list(M.bases())
            sage: N = loads(dumps(M))
            sage: N.closure(frozenset({3}))                                             # needs sage.rings.finite_rings
            frozenset({3})
            sage: N.is_isomorphic(M)
            True"""
