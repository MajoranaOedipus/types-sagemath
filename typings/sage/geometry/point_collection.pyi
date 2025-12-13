import _cython_3_2_1
import sage.structure.sage_object
from sage.geometry.toric_lattice import ToricLattice as ToricLattice
from sage.matrix.constructor import matrix as matrix
from sage.misc.latex import latex as latex
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, overload

is_PointCollection: _cython_3_2_1.cython_function_or_method
read_palp_point_collection: _cython_3_2_1.cython_function_or_method

class PointCollection(sage.structure.sage_object.SageObject):
    """PointCollection(points, module=None)

    File: /build/sagemath/src/sage/src/sage/geometry/point_collection.pyx (starting at line 116)

    Create a point collection.

    .. WARNING::

        No correctness check or normalization is performed on the input data.
        This class is designed for internal operations and you probably should
        not use it directly.

    Point collections are immutable, but cache most of the returned values.

    INPUT:

    - ``points`` -- an iterable structure of immutable elements of ``module``,
      if ``points`` are already accessible to you as a :class:`tuple`, it is
      preferable to use it for speed and memory consumption reasons;

    - ``module`` -- an ambient module for ``points``. If ``None`` (the default),
      it will be determined as :func:`parent` of the first point. Of course, this
      cannot be done if there are no points, so in this case you must give an
      appropriate ``module`` directly.

    OUTPUT:

    - a point collection."""
    def __init__(self, points, module=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/geometry/point_collection.pyx (starting at line 152)

                See :class:`PointCollection` for documentation.

                TESTS::

                    sage: from sage.geometry.point_collection import PointCollection
                    sage: v = vector([1,0])
                    sage: v.set_immutable()
                    sage: c = PointCollection([v], ZZ^2)
                    sage: c.module()
                    Ambient free module of rank 2
                    over the principal ideal domain Integer Ring
                    sage: c = PointCollection([v], None)
                    sage: c.module()  # Determined automatically
                    Ambient free module of rank 2
                    over the principal ideal domain Integer Ring
                    sage: TestSuite(c).run()
        """
    def basis(self) -> Any:
        """PointCollection.basis(self)

        File: /build/sagemath/src/sage/src/sage/geometry/point_collection.pyx (starting at line 575)

        Return a linearly independent subset of points of ``self``.

        OUTPUT:

        - a :class:`point collection <PointCollection>` giving a random (but
          fixed) choice of an `\\RR`-basis for the vector space spanned by the
          points of ``self``.

        EXAMPLES::

            sage: c = Cone([(0,0,1), (1,0,1), (0,1,1), (1,1,1)]).rays()
            sage: c.basis()
            N(0, 0, 1),
            N(1, 0, 1),
            N(0, 1, 1)
            in 3-d lattice N

        Calling this method twice will always return *exactly the same* point
        collection::

            sage: c.basis().basis() is c.basis()
            True"""
    @overload
    def cardinality(self) -> Any:
        """PointCollection.cardinality(self)

        File: /build/sagemath/src/sage/src/sage/geometry/point_collection.pyx (starting at line 604)

        Return the number of points in ``self``.

        OUTPUT: integer

        EXAMPLES::

            sage: c = Cone([(0,0,1), (1,0,1), (0,1,1), (1,1,1)]).rays()
            sage: c.cardinality()
            4"""
    @overload
    def cardinality(self) -> Any:
        """PointCollection.cardinality(self)

        File: /build/sagemath/src/sage/src/sage/geometry/point_collection.pyx (starting at line 604)

        Return the number of points in ``self``.

        OUTPUT: integer

        EXAMPLES::

            sage: c = Cone([(0,0,1), (1,0,1), (0,1,1), (1,1,1)]).rays()
            sage: c.cardinality()
            4"""
    @overload
    def cartesian_product(self, other, module=...) -> Any:
        """PointCollection.cartesian_product(self, other, module=None)

        File: /build/sagemath/src/sage/src/sage/geometry/point_collection.pyx (starting at line 618)

        Return the Cartesian product of ``self`` with ``other``.

        INPUT:

        - ``other`` -- a :class:`point collection <PointCollection>`;

        - ``module`` -- (optional) the ambient module for the result. By
          default, the direct sum of the ambient modules of ``self`` and
          ``other`` is constructed.

        OUTPUT: a :class:`point collection <PointCollection>`

        EXAMPLES::

            sage: c = Cone([(0,0,1), (1,1,1)]).rays()
            sage: c.cartesian_product(c)
            N+N(0, 0, 1, 0, 0, 1),
            N+N(1, 1, 1, 0, 0, 1),
            N+N(0, 0, 1, 1, 1, 1),
            N+N(1, 1, 1, 1, 1, 1)
            in 6-d lattice N+N"""
    @overload
    def cartesian_product(self, c) -> Any:
        """PointCollection.cartesian_product(self, other, module=None)

        File: /build/sagemath/src/sage/src/sage/geometry/point_collection.pyx (starting at line 618)

        Return the Cartesian product of ``self`` with ``other``.

        INPUT:

        - ``other`` -- a :class:`point collection <PointCollection>`;

        - ``module`` -- (optional) the ambient module for the result. By
          default, the direct sum of the ambient modules of ``self`` and
          ``other`` is constructed.

        OUTPUT: a :class:`point collection <PointCollection>`

        EXAMPLES::

            sage: c = Cone([(0,0,1), (1,1,1)]).rays()
            sage: c.cartesian_product(c)
            N+N(0, 0, 1, 0, 0, 1),
            N+N(1, 1, 1, 0, 0, 1),
            N+N(0, 0, 1, 1, 1, 1),
            N+N(1, 1, 1, 1, 1, 1)
            in 6-d lattice N+N"""
    @overload
    def column_matrix(self) -> Any:
        """PointCollection.column_matrix(self)

        File: /build/sagemath/src/sage/src/sage/geometry/point_collection.pyx (starting at line 652)

        Return a matrix whose columns are points of ``self``.

        OUTPUT: a :class:`matrix <Matrix>`

        EXAMPLES::

            sage: c = Cone([(0,0,1), (1,0,1), (0,1,1), (1,1,1)]).rays()
            sage: c.column_matrix()
            [0 1 0 1]
            [0 0 1 1]
            [1 1 1 1]"""
    @overload
    def column_matrix(self) -> Any:
        """PointCollection.column_matrix(self)

        File: /build/sagemath/src/sage/src/sage/geometry/point_collection.pyx (starting at line 652)

        Return a matrix whose columns are points of ``self``.

        OUTPUT: a :class:`matrix <Matrix>`

        EXAMPLES::

            sage: c = Cone([(0,0,1), (1,0,1), (0,1,1), (1,1,1)]).rays()
            sage: c.column_matrix()
            [0 1 0 1]
            [0 0 1 1]
            [1 1 1 1]"""
    def dim(self) -> Any:
        """PointCollection.dimension(self)

        File: /build/sagemath/src/sage/src/sage/geometry/point_collection.pyx (starting at line 668)

        Return the dimension of the space spanned by points of ``self``.

        .. NOTE:: You can use either :meth:`dim` or :meth:`dimension`.

        OUTPUT: integer

        EXAMPLES::

            sage: c = Cone([(0,0,1), (1,1,1)]).rays()
            sage: c.dimension()
            2
            sage: c.dim()
            2"""
    @overload
    def dimension(self) -> Any:
        """PointCollection.dimension(self)

        File: /build/sagemath/src/sage/src/sage/geometry/point_collection.pyx (starting at line 668)

        Return the dimension of the space spanned by points of ``self``.

        .. NOTE:: You can use either :meth:`dim` or :meth:`dimension`.

        OUTPUT: integer

        EXAMPLES::

            sage: c = Cone([(0,0,1), (1,1,1)]).rays()
            sage: c.dimension()
            2
            sage: c.dim()
            2"""
    @overload
    def dimension(self) -> Any:
        """PointCollection.dimension(self)

        File: /build/sagemath/src/sage/src/sage/geometry/point_collection.pyx (starting at line 668)

        Return the dimension of the space spanned by points of ``self``.

        .. NOTE:: You can use either :meth:`dim` or :meth:`dimension`.

        OUTPUT: integer

        EXAMPLES::

            sage: c = Cone([(0,0,1), (1,1,1)]).rays()
            sage: c.dimension()
            2
            sage: c.dim()
            2"""
    @overload
    def dual_module(self) -> Any:
        """PointCollection.dual_module(self)

        File: /build/sagemath/src/sage/src/sage/geometry/point_collection.pyx (starting at line 688)

        Return the dual of the ambient module of ``self``.

        OUTPUT:

        - a :class:`module <FreeModule_generic>`. If possible (that is, if the
          ambient :meth:`module` `M` of ``self`` has a ``dual()`` method), the
          dual module is returned. Otherwise, `R^n` is returned, where `n` is
          the dimension of `M` and `R` is its base ring.

        EXAMPLES::

            sage: c = Cone([(0,0,1), (1,0,1), (0,1,1), (1,1,1)]).rays()
            sage: c.dual_module()
            3-d lattice M"""
    @overload
    def dual_module(self) -> Any:
        """PointCollection.dual_module(self)

        File: /build/sagemath/src/sage/src/sage/geometry/point_collection.pyx (starting at line 688)

        Return the dual of the ambient module of ``self``.

        OUTPUT:

        - a :class:`module <FreeModule_generic>`. If possible (that is, if the
          ambient :meth:`module` `M` of ``self`` has a ``dual()`` method), the
          dual module is returned. Otherwise, `R^n` is returned, where `n` is
          the dimension of `M` and `R` is its base ring.

        EXAMPLES::

            sage: c = Cone([(0,0,1), (1,0,1), (0,1,1), (1,1,1)]).rays()
            sage: c.dual_module()
            3-d lattice M"""
    @overload
    def index(self, *args) -> Any:
        """PointCollection.index(self, *args)

        File: /build/sagemath/src/sage/src/sage/geometry/point_collection.pyx (starting at line 712)

        Return the index of the first occurrence of ``point`` in ``self``.

        INPUT:

        - ``point`` -- a point of ``self``

        - ``start`` -- (optional) an integer, if given, the search will start
          at this position

        - ``stop`` -- (optional) an integer, if given, the search will stop
          at this position

        OUTPUT: an integer if ``point`` is in ``self[start:stop]``, otherwise a
        :exc:`ValueError` exception is raised

        EXAMPLES::

            sage: c = Cone([(0,0,1), (1,0,1), (0,1,1), (1,1,1)]).rays()
            sage: c.index((0,1,1))
            Traceback (most recent call last):
            ...
            ValueError: tuple.index(x): x not in tuple

        Note that this was not a mistake: the *tuple* ``(0,1,1)`` is *not* a
        point of ``c``! We need to pass actual element of the ambient module of
        ``c`` to get their indices::

            sage: N = c.module()
            sage: c.index(N(0,1,1))
            2
            sage: c[2]
            N(0, 1, 1)"""
    @overload
    def index(self, x) -> Any:
        """PointCollection.index(self, *args)

        File: /build/sagemath/src/sage/src/sage/geometry/point_collection.pyx (starting at line 712)

        Return the index of the first occurrence of ``point`` in ``self``.

        INPUT:

        - ``point`` -- a point of ``self``

        - ``start`` -- (optional) an integer, if given, the search will start
          at this position

        - ``stop`` -- (optional) an integer, if given, the search will stop
          at this position

        OUTPUT: an integer if ``point`` is in ``self[start:stop]``, otherwise a
        :exc:`ValueError` exception is raised

        EXAMPLES::

            sage: c = Cone([(0,0,1), (1,0,1), (0,1,1), (1,1,1)]).rays()
            sage: c.index((0,1,1))
            Traceback (most recent call last):
            ...
            ValueError: tuple.index(x): x not in tuple

        Note that this was not a mistake: the *tuple* ``(0,1,1)`` is *not* a
        point of ``c``! We need to pass actual element of the ambient module of
        ``c`` to get their indices::

            sage: N = c.module()
            sage: c.index(N(0,1,1))
            2
            sage: c[2]
            N(0, 1, 1)"""
    @overload
    def matrix(self) -> Any:
        """PointCollection.matrix(self)

        File: /build/sagemath/src/sage/src/sage/geometry/point_collection.pyx (starting at line 749)

        Return a matrix whose rows are points of ``self``.

        OUTPUT: a :class:`matrix <Matrix>`

        EXAMPLES::

            sage: c = Cone([(0,0,1), (1,0,1), (0,1,1), (1,1,1)]).rays()
            sage: c.matrix()
            [0 0 1]
            [1 0 1]
            [0 1 1]
            [1 1 1]"""
    @overload
    def matrix(self) -> Any:
        """PointCollection.matrix(self)

        File: /build/sagemath/src/sage/src/sage/geometry/point_collection.pyx (starting at line 749)

        Return a matrix whose rows are points of ``self``.

        OUTPUT: a :class:`matrix <Matrix>`

        EXAMPLES::

            sage: c = Cone([(0,0,1), (1,0,1), (0,1,1), (1,1,1)]).rays()
            sage: c.matrix()
            [0 0 1]
            [1 0 1]
            [0 1 1]
            [1 1 1]"""
    @overload
    def module(self) -> Any:
        """PointCollection.module(self)

        File: /build/sagemath/src/sage/src/sage/geometry/point_collection.pyx (starting at line 771)

        Return the ambient module of ``self``.

        OUTPUT: a :class:`module <FreeModule_generic>`

        EXAMPLES::

            sage: c = Cone([(0,0,1), (1,0,1), (0,1,1), (1,1,1)]).rays()
            sage: c.module()
            3-d lattice N"""
    @overload
    def module(self) -> Any:
        """PointCollection.module(self)

        File: /build/sagemath/src/sage/src/sage/geometry/point_collection.pyx (starting at line 771)

        Return the ambient module of ``self``.

        OUTPUT: a :class:`module <FreeModule_generic>`

        EXAMPLES::

            sage: c = Cone([(0,0,1), (1,0,1), (0,1,1), (1,1,1)]).rays()
            sage: c.module()
            3-d lattice N"""
    @overload
    @staticmethod
    def output_format(format=...) -> Any:
        '''PointCollection.output_format(format=None)

        File: /build/sagemath/src/sage/src/sage/geometry/point_collection.pyx (starting at line 785)

        Return or set the output format for **ALL** point collections.

        INPUT:

        - ``format`` -- (optional) if given, must be one of the strings
            * "default" -- output one point per line with vertical alignment of
              coordinates in text mode, same as "tuple" for LaTeX;
            * "tuple" -- output ``tuple(self)`` with lattice information;
            * "matrix" -- output :meth:`matrix` with lattice information;
            * "column matrix" -- output :meth:`column_matrix` with lattice
              information;
            * "separated column matrix" -- same as "column matrix" for text
              mode, for LaTeX separate columns by lines (not shown by jsMath).

        OUTPUT:

        - a string with the current format (only if ``format`` was omitted).

        This function affects both regular and LaTeX output.

        EXAMPLES::

            sage: c = Cone([(0,0,1), (1,0,1), (0,1,1), (1,1,1)]).rays()
            sage: c
            N(0, 0, 1),
            N(1, 0, 1),
            N(0, 1, 1),
            N(1, 1, 1)
            in 3-d lattice N
            sage: c.output_format()
            \'default\'
            sage: c.output_format("tuple")
            sage: c
            (N(0, 0, 1), N(1, 0, 1), N(0, 1, 1), N(1, 1, 1))
            in 3-d lattice N
            sage: c.output_format("matrix")
            sage: c
            [0 0 1]
            [1 0 1]
            [0 1 1]
            [1 1 1]
            in 3-d lattice N
            sage: c.output_format("column matrix")
            sage: c
            [0 1 0 1]
            [0 0 1 1]
            [1 1 1 1]
            in 3-d lattice N
            sage: c.output_format("separated column matrix")
            sage: c
            [0 1 0 1]
            [0 0 1 1]
            [1 1 1 1]
            in 3-d lattice N

        Note that the last two outputs are identical, separators are only
        inserted in the LaTeX mode::

            sage: latex(c)
            \\left(\\begin{array}{r|r|r|r}
            0 & 1 & 0 & 1 \\\\\n            0 & 0 & 1 & 1 \\\\\n            1 & 1 & 1 & 1
            \\end{array}\\right)_{N}

        Since this is a static method, you can call it for the class directly::

            sage: from sage.geometry.point_collection import PointCollection
            sage: PointCollection.output_format("default")
            sage: c
            N(0, 0, 1),
            N(1, 0, 1),
            N(0, 1, 1),
            N(1, 1, 1)
            in 3-d lattice N'''
    @overload
    @staticmethod
    def output_format() -> Any:
        '''PointCollection.output_format(format=None)

        File: /build/sagemath/src/sage/src/sage/geometry/point_collection.pyx (starting at line 785)

        Return or set the output format for **ALL** point collections.

        INPUT:

        - ``format`` -- (optional) if given, must be one of the strings
            * "default" -- output one point per line with vertical alignment of
              coordinates in text mode, same as "tuple" for LaTeX;
            * "tuple" -- output ``tuple(self)`` with lattice information;
            * "matrix" -- output :meth:`matrix` with lattice information;
            * "column matrix" -- output :meth:`column_matrix` with lattice
              information;
            * "separated column matrix" -- same as "column matrix" for text
              mode, for LaTeX separate columns by lines (not shown by jsMath).

        OUTPUT:

        - a string with the current format (only if ``format`` was omitted).

        This function affects both regular and LaTeX output.

        EXAMPLES::

            sage: c = Cone([(0,0,1), (1,0,1), (0,1,1), (1,1,1)]).rays()
            sage: c
            N(0, 0, 1),
            N(1, 0, 1),
            N(0, 1, 1),
            N(1, 1, 1)
            in 3-d lattice N
            sage: c.output_format()
            \'default\'
            sage: c.output_format("tuple")
            sage: c
            (N(0, 0, 1), N(1, 0, 1), N(0, 1, 1), N(1, 1, 1))
            in 3-d lattice N
            sage: c.output_format("matrix")
            sage: c
            [0 0 1]
            [1 0 1]
            [0 1 1]
            [1 1 1]
            in 3-d lattice N
            sage: c.output_format("column matrix")
            sage: c
            [0 1 0 1]
            [0 0 1 1]
            [1 1 1 1]
            in 3-d lattice N
            sage: c.output_format("separated column matrix")
            sage: c
            [0 1 0 1]
            [0 0 1 1]
            [1 1 1 1]
            in 3-d lattice N

        Note that the last two outputs are identical, separators are only
        inserted in the LaTeX mode::

            sage: latex(c)
            \\left(\\begin{array}{r|r|r|r}
            0 & 1 & 0 & 1 \\\\\n            0 & 0 & 1 & 1 \\\\\n            1 & 1 & 1 & 1
            \\end{array}\\right)_{N}

        Since this is a static method, you can call it for the class directly::

            sage: from sage.geometry.point_collection import PointCollection
            sage: PointCollection.output_format("default")
            sage: c
            N(0, 0, 1),
            N(1, 0, 1),
            N(0, 1, 1),
            N(1, 1, 1)
            in 3-d lattice N'''
    @overload
    def set(self) -> Any:
        """PointCollection.set(self)

        File: /build/sagemath/src/sage/src/sage/geometry/point_collection.pyx (starting at line 871)

        Return points of ``self`` as a :class:`frozenset`.

        OUTPUT: a :class:`frozenset`

        EXAMPLES::

            sage: c = Cone([(0,0,1), (1,0,1), (0,1,1), (1,1,1)]).rays()
            sage: c.set()
            frozenset({N(0, 0, 1), N(0, 1, 1), N(1, 0, 1), N(1, 1, 1)})"""
    @overload
    def set(self) -> Any:
        """PointCollection.set(self)

        File: /build/sagemath/src/sage/src/sage/geometry/point_collection.pyx (starting at line 871)

        Return points of ``self`` as a :class:`frozenset`.

        OUTPUT: a :class:`frozenset`

        EXAMPLES::

            sage: c = Cone([(0,0,1), (1,0,1), (0,1,1), (1,1,1)]).rays()
            sage: c.set()
            frozenset({N(0, 0, 1), N(0, 1, 1), N(1, 0, 1), N(1, 1, 1)})"""
    @overload
    def write_for_palp(self, f) -> Any:
        """PointCollection.write_for_palp(self, f)

        File: /build/sagemath/src/sage/src/sage/geometry/point_collection.pyx (starting at line 887)

        Write ``self`` into an open file ``f`` in PALP format.

        INPUT:

        - ``f`` -- a file opened for writing

        EXAMPLES::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: from io import StringIO
            sage: f = StringIO()
            sage: o.vertices().write_for_palp(f)
            sage: print(f.getvalue())
            6 3
            1 0 0
            0 1 0
            0 0 1
            -1 0 0
            0 -1 0
            0 0 -1"""
    @overload
    def write_for_palp(self, f) -> Any:
        """PointCollection.write_for_palp(self, f)

        File: /build/sagemath/src/sage/src/sage/geometry/point_collection.pyx (starting at line 887)

        Write ``self`` into an open file ``f`` in PALP format.

        INPUT:

        - ``f`` -- a file opened for writing

        EXAMPLES::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: from io import StringIO
            sage: f = StringIO()
            sage: o.vertices().write_for_palp(f)
            sage: print(f.getvalue())
            6 3
            1 0 0
            0 1 0
            0 0 1
            -1 0 0
            0 -1 0
            0 0 -1"""
    def __add__(self, left, right) -> Any:
        """PointCollection.__add__(left, right)

        File: /build/sagemath/src/sage/src/sage/geometry/point_collection.pyx (starting at line 198)

        Return the joint point collection.

        INPUT:

        - ``left`` -- a :class:`PointCollection`;

        - ``right`` -- a :class:`PointCollection`

        OUTPUT: a :class:`PointCollection`

        TESTS::

            sage: c = Cone([(0,0,1), (1,0,1), (0,1,1), (1,1,1)]).rays()
            sage: c + c
            N(0, 0, 1),
            N(1, 0, 1),
            N(0, 1, 1),
            N(1, 1, 1),
            N(0, 0, 1),
            N(1, 0, 1),
            N(0, 1, 1),
            N(1, 1, 1)
            in 3-d lattice N"""
    def __call__(self, *args) -> Any:
        """PointCollection.__call__(self, *args)

        File: /build/sagemath/src/sage/src/sage/geometry/point_collection.pyx (starting at line 234)

        Return a subcollection of ``self``.

        INPUT:

        - a list of integers (as a single or many arguments).

        OUTPUT: a :class:`point collection <PointCollection>`

        TESTS::

            sage: c = Cone([(0,0,1), (1,0,1), (0,1,1), (1,1,1)]).rays()
            sage: c()
            Empty collection
            in 3-d lattice N
            sage: c(2,1)
            N(0, 1, 1),
            N(1, 0, 1)
            in 3-d lattice N
            sage: c(range(4)) == c
            True"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __getitem__(self, n) -> Any:
        """PointCollection.__getitem__(self, n)

        File: /build/sagemath/src/sage/src/sage/geometry/point_collection.pyx (starting at line 303)

        Return the ``n``-th point of ``self``.

        INPUT:

        - ``n`` -- integer

        OUTPUT: a point, an element of the ambient :meth:`module` of ``self``

        EXAMPLES::

            sage: c = Cone([(0,0,1), (1,0,1), (0,1,1), (1,1,1)]).rays()
            sage: c[0]
            N(0, 0, 1)"""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __hash__(self) -> Any:
        """PointCollection.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/geometry/point_collection.pyx (starting at line 321)

        Return the hash of ``self``.

        OUTPUT: integer

        TESTS::

            sage: c = Cone([(0,0,1), (1,0,1), (0,1,1), (1,1,1)]).rays()
            sage: hash(c) == hash(c)
            True"""
    def __iter__(self) -> Any:
        """PointCollection.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/geometry/point_collection.pyx (starting at line 335)

        Return an iterator over points of ``self``.

        OUTPUT: an iterator

        TESTS::

            sage: c = Cone([(0,0,1), (1,0,1), (0,1,1), (1,1,1)]).rays()
            sage: for point in c: print(point)
            N(0, 0, 1)
            N(1, 0, 1)
            N(0, 1, 1)
            N(1, 1, 1)"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __len__(self) -> Any:
        """PointCollection.__len__(self)

        File: /build/sagemath/src/sage/src/sage/geometry/point_collection.pyx (starting at line 352)

        Return the number of points in ``self``.

        OUTPUT: integer

        EXAMPLES::

            sage: c = Cone([(0,0,1), (1,0,1), (0,1,1), (1,1,1)]).rays()
            sage: len(c)
            4"""
    def __list__(self) -> Any:
        """PointCollection.__list__(self)

        File: /build/sagemath/src/sage/src/sage/geometry/point_collection.pyx (starting at line 366)

        Return a list of points of ``self``.

        OUTPUT: list

        TESTS::

            sage: c = Cone([(0,0,1), (1,0,1), (0,1,1), (1,1,1)]).rays()
            sage: list(c)
            [N(0, 0, 1), N(1, 0, 1), N(0, 1, 1), N(1, 1, 1)]"""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __mul__(self, left, right) -> Any:
        """PointCollection.__mul__(left, right)

        File: /build/sagemath/src/sage/src/sage/geometry/point_collection.pyx (starting at line 380)

        Return the product ``left * right``.

        INPUT:

        - a :class:`point collection <PointCollection>` and something that can
          act both on ``self.module().zero()`` and either ``self.matrix()`` from
          the right or ``self.column_matrix()`` from the left.

        OUTPUT:

        - the result of ``self.matrix() * right``, provided that
          ``self.module().zero() * right`` can be computed.

        The idea of this method is to provide a shortcut for matrix
        multiplication with appropriate type checks, in particular, it is not
        possible to multiply by a point of the same toric lattice as elements of
        ``self``.

        TESTS::

            sage: c = Cone([(0,0,1), (1,0,1), (0,1,1), (1,1,1)]).rays()
            sage: c.matrix()
            [0 0 1]
            [1 0 1]
            [0 1 1]
            [1 1 1]
            sage: c * c[0]
            Traceback (most recent call last):
            ...
            TypeError: elements of the same toric lattice cannot be multiplied!

        If you really need such a product, state it explicitly::

            sage: c.matrix() * c[0]
            (1, 1, 1, 1)

        Multiplication by matrices works as well::

            sage: c * c.column_matrix()
            [1 1 1 1]
            [1 2 1 2]
            [1 1 2 2]
            [1 2 2 3]"""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __radd__(self, other):
        """Return value+self."""
    def __reduce__(self) -> Any:
        """PointCollection.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/geometry/point_collection.pyx (starting at line 439)

        Prepare ``self`` for pickling.

        OUTPUT:

        - a tuple, currently the class name and a tuple consisting of points
          and the ambient module.

        TESTS::

            sage: c = Cone([(0,0,1), (1,0,1), (0,1,1), (1,1,1)]).rays()
            sage: loads(dumps(c))
            N(0, 0, 1),
            N(1, 0, 1),
            N(0, 1, 1),
            N(1, 1, 1)
            in 3-d lattice N
            sage: loads(dumps(c)) == c
            True"""
    def __rmul__(self, other):
        """Return value*self."""
    def __tuple__(self) -> Any:
        """PointCollection.__tuple__(self)

        File: /build/sagemath/src/sage/src/sage/geometry/point_collection.pyx (starting at line 462)

        Return the tuple of points of ``self``.

        OUTPUT: a tuple

        TESTS::

            sage: c = Cone([(0,0,1), (1,0,1), (0,1,1), (1,1,1)]).rays()
            sage: tuple(c)
            (N(0, 0, 1), N(1, 0, 1), N(0, 1, 1), N(1, 1, 1))"""
