from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from typing import Any, ClassVar, overload

class CutNode:
    """File: /build/sagemath/src/sage/src/sage/matroids/extension.pyx (starting at line 36)

        An internal class used for creating linear subclasses of a matroids in a
        depth-first manner.

        A linear subclass is a set of hyperplanes `mc` with the property that
        certain sets of hyperplanes must either be fully contained in `mc` or
        intersect `mc` in at most 1 element. The way we generate them is by a
        depth-first search. This class represents a node in the search tree.

        It contains the set of hyperplanes selected so far, as well as a
        collection of hyperplanes whose insertion has been explored elsewhere in
        the search tree.

        The class has methods for selecting a hyperplane to insert, for inserting
        hyperplanes and closing the set to become a linear subclass again, and for
        adding a hyperplane to the set of *forbidden* hyperplanes, and similarly
        closing that set.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class LinearSubclasses:
    """LinearSubclasses(M, line_length=None, subsets=None, splice=None)

    File: /build/sagemath/src/sage/src/sage/matroids/extension.pyx (starting at line 251)

    An iterable set of linear subclasses of a matroid.

    Enumerate linear subclasses of a given matroid. A *linear subclass* is a
    collection of hyperplanes (flats of rank `r - 1` where `r` is the rank of
    the matroid) with the property that no modular triple of hyperplanes has
    exactly two members in the linear subclass. A triple of hyperplanes in a
    matroid of rank `r` is *modular* if its intersection has rank `r - 2`.

    INPUT:

    - ``M`` -- matroid
    - ``line_length`` -- integer (default: ``None``)
    - ``subsets`` -- (default: ``None``) a set of subsets of the groundset of
      ``M``
    - ``splice`` -- (default: ``None``) a matroid `N` such that for some
      `e \\in E(N)` and some `f \\in E(M)`, we have
      `N\\setminus e= M\\setminus f`

    OUTPUT: an enumerator for the linear subclasses of M

    If ``line_length`` is not ``None``, the enumeration is restricted to
    linear subclasses ``mc`` so containing at least one of each set of
    ``line_length`` hyperplanes which have a common intersection of
    rank `r - 2`.

    If ``subsets`` is not ``None``, the enumeration is restricted to linear
    subclasses ``mc`` containing all hyperplanes which fully contain some set
    from ``subsets``.

    If ``splice`` is not ``None``, then the enumeration is restricted to
    linear subclasses `mc` such that if `M'` is the extension of `M` by `e`
    that arises from `mc`, then `M'\\setminus f = N`.

    EXAMPLES::

        sage: from sage.matroids.extension import LinearSubclasses
        sage: M = matroids.Uniform(3, 6)
        sage: len([mc for mc in LinearSubclasses(M)])
        83
        sage: len([mc for mc in LinearSubclasses(M, line_length=5)])
        22
        sage: for mc in LinearSubclasses(M, subsets=[[0, 1], [2, 3], [4, 5]]):
        ....:     print(len(mc))
        3
        15

    Note that this class is intended for runtime, internal use, so no
    loads/dumps mechanism was implemented."""
    def __init__(self, M, line_length=..., subsets=..., splice=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matroids/extension.pyx (starting at line 302)

                See the class docstring for full documentation.

                EXAMPLES::

                    sage: from sage.matroids.advanced import *  # LinearSubclasses, BasisMatroid
                    sage: M = matroids.Uniform(3, 6)
                    sage: len([mc for mc in LinearSubclasses(M)])
                    83
                    sage: len([mc for mc in LinearSubclasses(M, line_length=5)])
                    22
                    sage: for mc in LinearSubclasses(M,
                    ....:                           subsets=[[0, 1], [2, 3], [4, 5]]):
                    ....:     print(len(mc))
                    3
                    15
                    sage: M = BasisMatroid(matroids.catalog.BetsyRoss()); M
                    Matroid of rank 3 on 11 elements with 140 bases
                    sage: e = 'k'; f = 'h'; Me = M.delete(e); Mf=M.delete(f)
                    sage: for mc in LinearSubclasses(Mf, splice=Me):
                    ....:     print(Mf.extension(f, mc))
                    Matroid of rank 3 on 11 elements with 141 bases
                    Matroid of rank 3 on 11 elements with 140 bases
                    sage: for mc in LinearSubclasses(Me, splice=Mf):
                    ....:     print(Me.extension(e, mc))
                    Matroid of rank 3 on 11 elements with 141 bases
                    Matroid of rank 3 on 11 elements with 140 bases
        """
    def __getitem__(self, CutNodenode) -> Any:
        """LinearSubclasses.__getitem__(self, CutNode node)

        File: /build/sagemath/src/sage/src/sage/matroids/extension.pyx (starting at line 396)

        Return a linear subclass stored in a given CutNode.

        Internal function.

        EXAMPLES::

            sage: from sage.matroids.extension import LinearSubclasses
            sage: M = matroids.Uniform(3, 6)
            sage: len([mc for mc in LinearSubclasses(M)])
            83"""
    def __iter__(self) -> Any:
        """LinearSubclasses.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/extension.pyx (starting at line 381)

        Return an iterator for the linear subclasses.

        EXAMPLES::

            sage: from sage.matroids.extension import LinearSubclasses
            sage: M = matroids.Uniform(3, 6)
            sage: for mc in LinearSubclasses(M, subsets=[[0, 1], [2, 3], [4, 5]]):
            ....:     print(len(mc))
            3
            15"""

class LinearSubclassesIter:
    """LinearSubclassesIter(MC)

    File: /build/sagemath/src/sage/src/sage/matroids/extension.pyx (starting at line 177)

    An iterator for a set of linear subclass."""
    def __init__(self, MC) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matroids/extension.pyx (starting at line 181)

                Create a linear subclass iterator.

                Auxiliary to class LinearSubclasses.

                INPUT:

                - ``MC`` -- a member of class LinearSubclasses

                EXAMPLES::

                    sage: from sage.matroids.extension import LinearSubclasses
                    sage: M = matroids.Uniform(3, 6)
                    sage: type(LinearSubclasses(M).__iter__())
                    <... 'sage.matroids.extension.LinearSubclassesIter'>
        """
    def __iter__(self) -> Any:
        """LinearSubclassesIter.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/extension.pyx (starting at line 214)"""
    @overload
    def __next__(self) -> Any:
        """LinearSubclassesIter.__next__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/extension.pyx (starting at line 217)

        Return the next linear subclass.

        EXAMPLES::

            sage: from sage.matroids.advanced import *
            sage: from sage.matroids.extension import LinearSubclasses
            sage: M = BasisMatroid(matroids.Uniform(3, 6))
            sage: I = LinearSubclasses(M).__iter__()
            sage: M.extension('x', I.__next__())
            Matroid of rank 3 on 7 elements with 35 bases
            sage: M.extension('x', I.__next__())
            Matroid of rank 3 on 7 elements with 34 bases"""
    @overload
    def __next__(self) -> Any:
        """LinearSubclassesIter.__next__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/extension.pyx (starting at line 217)

        Return the next linear subclass.

        EXAMPLES::

            sage: from sage.matroids.advanced import *
            sage: from sage.matroids.extension import LinearSubclasses
            sage: M = BasisMatroid(matroids.Uniform(3, 6))
            sage: I = LinearSubclasses(M).__iter__()
            sage: M.extension('x', I.__next__())
            Matroid of rank 3 on 7 elements with 35 bases
            sage: M.extension('x', I.__next__())
            Matroid of rank 3 on 7 elements with 34 bases"""
    @overload
    def __next__(self) -> Any:
        """LinearSubclassesIter.__next__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/extension.pyx (starting at line 217)

        Return the next linear subclass.

        EXAMPLES::

            sage: from sage.matroids.advanced import *
            sage: from sage.matroids.extension import LinearSubclasses
            sage: M = BasisMatroid(matroids.Uniform(3, 6))
            sage: I = LinearSubclasses(M).__iter__()
            sage: M.extension('x', I.__next__())
            Matroid of rank 3 on 7 elements with 35 bases
            sage: M.extension('x', I.__next__())
            Matroid of rank 3 on 7 elements with 34 bases"""

class MatroidExtensions(LinearSubclasses):
    """MatroidExtensions(M, e, line_length=None, subsets=None, splice=None, orderly=False)

    File: /build/sagemath/src/sage/src/sage/matroids/extension.pyx (starting at line 413)

    An iterable set of single-element extensions of a given matroid.

    INPUT:

    - ``M`` -- matroid
    - ``e`` -- an element
    - ``line_length`` -- integer (default: ``None``)
    - ``subsets`` -- (default: ``None``) a set of subsets of the groundset of
      ``M``
    - ``splice`` -- a matroid `N` such that for some `f \\in E(M)`, we have
      `N\\setminus e= M\\setminus f`

    OUTPUT:

    An enumerator for the extensions of ``M`` to a matroid ``N`` so that
    `N\\setminus e = M`. If ``line_length`` is not ``None``, the enumeration
    is restricted to extensions `N` without `U(2, k)`-minors, where
    ``k > line_length``.

    If ``subsets`` is not ``None``, the enumeration is restricted to
    extensions `N` of `M` by element `e` so that all hyperplanes of `M`
    which fully contain some set from ``subsets``, will also span `e`.

    If ``splice`` is not ``None``, then the enumeration is restricted to
    extensions `M'` such that `M'\\setminus f = N`, where
    `E(M)\\setminus E(N)=\\{f\\}`.

    EXAMPLES::

        sage: from sage.matroids.advanced import *
        sage: M = matroids.Uniform(3, 6)
        sage: len([N for N in MatroidExtensions(M, 'x')])
        83
        sage: len([N for N in MatroidExtensions(M, 'x', line_length=5)])
        22
        sage: for N in MatroidExtensions(M, 'x', subsets=[[0, 1], [2, 3],
        ....:                                             [4, 5]]): print(N)
        Matroid of rank 3 on 7 elements with 32 bases
        Matroid of rank 3 on 7 elements with 20 bases
        sage: M = BasisMatroid(matroids.catalog.BetsyRoss()); M
        Matroid of rank 3 on 11 elements with 140 bases
        sage: e = 'k'; f = 'h'; Me = M.delete(e); Mf=M.delete(f)
        sage: for N in MatroidExtensions(Mf, f, splice=Me): print(N)
        Matroid of rank 3 on 11 elements with 141 bases
        Matroid of rank 3 on 11 elements with 140 bases
        sage: for N in MatroidExtensions(Me, e, splice=Mf): print(N)
        Matroid of rank 3 on 11 elements with 141 bases
        Matroid of rank 3 on 11 elements with 140 bases

    Note that this class is intended for runtime, internal use, so no
    loads/dumps mechanism was implemented."""
    def __init__(self, M, e, line_length=..., subsets=..., splice=..., orderly=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matroids/extension.pyx (starting at line 467)

                See the class docstring for full documentation.

                EXAMPLES::

                    sage: from sage.matroids.advanced import *
                    sage: M = matroids.Uniform(3, 6)
                    sage: len([N for N in MatroidExtensions(M, 'x')])
                    83
                    sage: len([N for N in MatroidExtensions(M, 'x', line_length=5)])
                    22
                    sage: for N in MatroidExtensions(M, 'x', subsets=[[0, 1], [2, 3],
                    ....:                                            [4, 5]]): print(N)
                    Matroid of rank 3 on 7 elements with 32 bases
                    Matroid of rank 3 on 7 elements with 20 bases
        """
    def __getitem__(self, CutNodenode) -> Any:
        """MatroidExtensions.__getitem__(self, CutNode node)

        File: /build/sagemath/src/sage/src/sage/matroids/extension.pyx (starting at line 496)

        Return a single-element extension determined by a given CutNode.

        Internal function.

        EXAMPLES::

            sage: from sage.matroids.advanced import *
            sage: M = matroids.Uniform(3, 6)
            sage: len([N for N in MatroidExtensions(M, 'x')])
            83"""
