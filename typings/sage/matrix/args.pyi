import _cython_3_2_1
import sage.categories.monoids as monoids
from sage.categories.category import ZZ as ZZ
from sage.categories.monoids import CommutativeMonoids as CommutativeMonoids
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.misc.misc_c import sized_iter as sized_iter
from sage.misc.superseded import deprecation_cython as deprecation_cython
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

MatrixArgs_init: _cython_3_2_1.cython_function_or_method
__pyx_capi__: dict

class MatrixArgs:
    '''MatrixArgs(base_ring=None, *args, nrows=None, ncols=None, entries=None, sparse=None, row_keys=None, column_keys=None, space=None, **kwds)

    File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 119)

    Collect arguments for constructing a matrix.

    This class is meant to pass around arguments, for example from the
    global :func:`matrix` constructor to the matrix space or to the
    element class constructor.

    A typical use case is first creating a ``MatrixArgs`` instance,
    possibly adjusting the attributes. This instance can then be passed
    around and a matrix can be constructed from it using the
    :meth:`matrix` method. Also, a flat list can be constructed using
    :meth:`list` or a sparse dict using :meth:`dict`. It is safe to
    construct multiple objects (of the same or a different kind) from
    the same ``MatrixArgs`` instance.

    ``MatrixArgs`` also supports iteration using the :meth:`iter`
    method. This is a more low-level interface.

    When ``MatrixArgs`` produces output, it is first *finalized*. This
    means that all missing attributes are derived or guessed. After
    finalization, you should no longer change the attributes or it will
    end up in an inconsistent state. You can also finalize explicitly by
    calling the :meth:`finalized` method.

    A ``MatrixArgs`` can contain invalid input. This is not checked when
    constructing the ``MatrixArgs`` instance, but it is checked either
    when finalizing or when constructing an object from it.

    .. WARNING::

        Instances of this class should only be temporary, they are not
        meant to be stored long-term.

    EXAMPLES::

        sage: from sage.matrix.args import MatrixArgs
        sage: ma = MatrixArgs(2, 2, (x for x in range(4))); ma
        <MatrixArgs for None; typ=UNKNOWN; entries=<generator ...>>
        sage: ma.finalized()
        <MatrixArgs for Full MatrixSpace of 2 by 2 dense matrices
         over Integer Ring; typ=SEQ_FLAT; entries=[0, 1, 2, 3]>

    Many types of input are possible::

        sage: ma = MatrixArgs(2, 2, entries=None); ma.finalized()
        <MatrixArgs for Full MatrixSpace of 2 by 2 dense matrices
         over Integer Ring; typ=ZERO; entries=None>
        sage: ma.matrix()
        [0 0]
        [0 0]
        sage: ma = MatrixArgs(2, 2, entries={}); ma.finalized()
        <MatrixArgs for Full MatrixSpace of 2 by 2 sparse matrices
         over Integer Ring; typ=SEQ_SPARSE; entries=[]>
        sage: ma.matrix()
        [0 0]
        [0 0]
        sage: ma = MatrixArgs(2, 2, entries=[1,2,3,4]); ma.finalized()
        <MatrixArgs for Full MatrixSpace of 2 by 2 dense matrices
         over Integer Ring; typ=SEQ_FLAT; entries=[1, 2, 3, 4]>
        sage: ma.matrix()
        [1 2]
        [3 4]
        sage: ma = MatrixArgs(2, 2, entries=math.pi); ma.finalized()
        <MatrixArgs for Full MatrixSpace of 2 by 2 dense matrices
         over Real Double Field; typ=SCALAR; entries=3.141592653589793>
        sage: ma.matrix()
        [3.141592653589793               0.0]
        [              0.0 3.141592653589793]
        sage: ma = MatrixArgs(2, 2, entries=pi); ma.finalized()                         # needs sage.symbolic
        <MatrixArgs for Full MatrixSpace of 2 by 2 dense matrices
         over Symbolic Ring; typ=SCALAR; entries=pi>
        sage: ma.matrix()                                                               # needs sage.symbolic
        [pi  0]
        [ 0 pi]
        sage: ma = MatrixArgs(ZZ, 2, 2, entries={(0,0): 7}); ma.finalized()
        <MatrixArgs for Full MatrixSpace of 2 by 2 sparse matrices
         over Integer Ring; typ=SEQ_SPARSE; entries=[SparseEntry(0, 0, 7)]>
        sage: ma.matrix()
        [7 0]
        [0 0]
        sage: ma = MatrixArgs(ZZ, 2, 2, entries=((1,2), (3,4))); ma.finalized()
        <MatrixArgs for Full MatrixSpace of 2 by 2 dense matrices
         over Integer Ring; typ=SEQ_SEQ; entries=((1, 2), (3, 4))>
        sage: ma.matrix()
        [1 2]
        [3 4]
        sage: ma = MatrixArgs(ZZ, 2, 2, entries=(1,2,3,4)); ma.finalized()
        <MatrixArgs for Full MatrixSpace of 2 by 2 dense matrices
         over Integer Ring; typ=SEQ_FLAT; entries=(1, 2, 3, 4)>
        sage: ma.matrix()
        [1 2]
        [3 4]

        sage: # needs sage.libs.pari
        sage: ma = MatrixArgs(QQ, entries=pari("[1,2;3,4]")); ma.finalized()
        <MatrixArgs for Full MatrixSpace of 2 by 2 dense matrices
         over Rational Field; typ=SEQ_FLAT; entries=[1, 2, 3, 4]>
        sage: ma.matrix()
        [1 2]
        [3 4]
        sage: ma = MatrixArgs(QQ, 2, 2, entries=pari("[1,2,3,4]")); ma.finalized()
        <MatrixArgs for Full MatrixSpace of 2 by 2 dense matrices
         over Rational Field; typ=SEQ_FLAT; entries=[1, 2, 3, 4]>
        sage: ma.matrix()
        [1 2]
        [3 4]
        sage: ma = MatrixArgs(QQ, 2, 2, entries=pari("3/5")); ma.finalized()
        <MatrixArgs for Full MatrixSpace of 2 by 2 dense matrices
         over Rational Field; typ=SCALAR; entries=3/5>
        sage: ma.matrix()
        [3/5   0]
        [  0 3/5]

        sage: ma = MatrixArgs(entries=matrix(2,2)); ma.finalized()
        <MatrixArgs for Full MatrixSpace of 2 by 2 dense matrices
         over Integer Ring; typ=MATRIX; entries=[0 0]
                                                [0 0]>
        sage: ma.matrix()
        [0 0]
        [0 0]
        sage: ma = MatrixArgs(2, 2, entries=lambda i,j: 1+2*i+j); ma.finalized()
        <MatrixArgs for Full MatrixSpace of 2 by 2 dense matrices
         over Integer Ring; typ=SEQ_FLAT; entries=[1, 2, 3, 4]>
        sage: ma.matrix()
        [1 2]
        [3 4]
        sage: ma = MatrixArgs(ZZ, 2, 2, entries=lambda i,j: 1+2*i+j); ma.finalized()
        <MatrixArgs for Full MatrixSpace of 2 by 2 dense matrices
         over Integer Ring; typ=CALLABLE; entries=<function ...>>
        sage: ma.matrix()
        [1 2]
        [3 4]

        sage: # needs numpy
        sage: from numpy import array
        sage: ma = MatrixArgs(array([[1,2],[3,4]])); ma.finalized()
        <MatrixArgs for Full MatrixSpace of 2 by 2 dense matrices
         over Integer Ring; typ=SEQ_SEQ; entries=array([[1, 2], [3, 4]])>
        sage: ma.matrix()
        [1 2]
        [3 4]
        sage: ma = MatrixArgs(array([[1.,2.],[3.,4.]])); ma.finalized()
        <MatrixArgs for Full MatrixSpace of 2 by 2 dense matrices
         over Real Double Field; typ=MATRIX; entries=[1.0 2.0]
                                                     [3.0 4.0]>
        sage: ma.matrix()
        [1.0 2.0]
        [3.0 4.0]
        sage: ma = MatrixArgs(RealField(20), array([[1.,2.],[3.,4.]])); ma.finalized()
        <MatrixArgs for Full MatrixSpace of 2 by 2 dense matrices over Real Field
         with 20 bits of precision; typ=MATRIX; entries=[1.0 2.0]
                                                        [3.0 4.0]>
        sage: ma.matrix()
        [1.0000 2.0000]
        [3.0000 4.0000]

        sage: # needs sage.graphs
        sage: ma = MatrixArgs(graphs.CycleGraph(3)); ma.finalized()
        <MatrixArgs for Full MatrixSpace of 3 by 3 dense matrices
         over Integer Ring; typ=MATRIX; entries=[0 1 1]
                                                [1 0 1]
                                                [1 1 0]>
        sage: ma.matrix()
        [0 1 1]
        [1 0 1]
        [1 1 0]

        sage: ma = MatrixArgs([vector([0,1], sparse=True),
        ....:                  vector([0,0], sparse=True)], sparse=True)
        sage: ma.finalized()
        <MatrixArgs for Full MatrixSpace of 2 by 2 sparse matrices over
         Integer Ring; typ=SEQ_SPARSE; entries=[SparseEntry(0, 1, 1)]>
        sage: ma.matrix()
        [0 1]
        [0 0]

    Test invalid input::

        sage: MatrixArgs(ZZ, 2, 2, entries=\'abcd\').finalized()
        <MatrixArgs for Full MatrixSpace of 2 by 2 dense matrices
        over Integer Ring; typ=SCALAR; entries=\'abcd\'>
        sage: matrix(ZZ, 2, 2, entries=\'abcd\')
        Traceback (most recent call last):
        ...
        TypeError: unable to convert \'abcd\' to an integer
        sage: MatrixArgs(ZZ, 2, 2, entries=MatrixArgs()).finalized()
        Traceback (most recent call last):
        ...
        TypeError: unable to convert <MatrixArgs for None; typ=UNKNOWN; entries=None> to a matrix'''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    base: base
    column_keys: column_keys
    entries: entries
    kwds: kwds
    ncols: ncols
    nrows: nrows
    row_keys: row_keys
    space: space
    sparse: sparse
    @overload
    def __init__(self, base_ring=..., *args, nrows=..., ncols=..., entries=..., sparse=..., row_keys=..., column_keys=..., space=..., **kwds) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 318)

                Parse arguments for creating a new matrix.

                See :func:`matrix` for documentation.

                This typically does not raise errors for invalid input, except
                when the arguments cannot be parsed.

                EXAMPLES::

                    sage: from sage.matrix.args import MatrixArgs
                    sage: MatrixArgs().finalized()
                    <MatrixArgs for Full MatrixSpace of 0 by 0 dense matrices over
                     Integer Ring; typ=ZERO; entries=None>
                    sage: MatrixArgs(1).finalized()
                    <MatrixArgs for Full MatrixSpace of 1 by 1 dense matrices over
                     Integer Ring; typ=ZERO; entries=None>
                    sage: MatrixArgs(1, 1, 3).finalized()
                    <MatrixArgs for Full MatrixSpace of 1 by 1 dense matrices over
                     Integer Ring; typ=SCALAR; entries=3>
                    sage: MatrixArgs(1, 1, 1, 1).finalized()
                    Traceback (most recent call last):
                    ...
                    TypeError: too many arguments in matrix constructor
                    sage: MatrixArgs(3, nrows=1, ncols=1).finalized()
                    <MatrixArgs for Full MatrixSpace of 1 by 1 dense matrices over
                     Integer Ring; typ=SCALAR; entries=3>
                    sage: MatrixArgs(3, nrows=1).finalized()
                    <MatrixArgs for Full MatrixSpace of 1 by 1 dense matrices over
                     Integer Ring; typ=SCALAR; entries=3>
                    sage: MatrixArgs(3, ncols=1).finalized()
                    <MatrixArgs for Full MatrixSpace of 1 by 1 dense matrices over
                     Integer Ring; typ=SCALAR; entries=3>
        """
    @overload
    def __init__(self, QQ, entries=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 318)

                Parse arguments for creating a new matrix.

                See :func:`matrix` for documentation.

                This typically does not raise errors for invalid input, except
                when the arguments cannot be parsed.

                EXAMPLES::

                    sage: from sage.matrix.args import MatrixArgs
                    sage: MatrixArgs().finalized()
                    <MatrixArgs for Full MatrixSpace of 0 by 0 dense matrices over
                     Integer Ring; typ=ZERO; entries=None>
                    sage: MatrixArgs(1).finalized()
                    <MatrixArgs for Full MatrixSpace of 1 by 1 dense matrices over
                     Integer Ring; typ=ZERO; entries=None>
                    sage: MatrixArgs(1, 1, 3).finalized()
                    <MatrixArgs for Full MatrixSpace of 1 by 1 dense matrices over
                     Integer Ring; typ=SCALAR; entries=3>
                    sage: MatrixArgs(1, 1, 1, 1).finalized()
                    Traceback (most recent call last):
                    ...
                    TypeError: too many arguments in matrix constructor
                    sage: MatrixArgs(3, nrows=1, ncols=1).finalized()
                    <MatrixArgs for Full MatrixSpace of 1 by 1 dense matrices over
                     Integer Ring; typ=SCALAR; entries=3>
                    sage: MatrixArgs(3, nrows=1).finalized()
                    <MatrixArgs for Full MatrixSpace of 1 by 1 dense matrices over
                     Integer Ring; typ=SCALAR; entries=3>
                    sage: MatrixArgs(3, ncols=1).finalized()
                    <MatrixArgs for Full MatrixSpace of 1 by 1 dense matrices over
                     Integer Ring; typ=SCALAR; entries=3>
        """
    @overload
    def __init__(self, entries=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 318)

                Parse arguments for creating a new matrix.

                See :func:`matrix` for documentation.

                This typically does not raise errors for invalid input, except
                when the arguments cannot be parsed.

                EXAMPLES::

                    sage: from sage.matrix.args import MatrixArgs
                    sage: MatrixArgs().finalized()
                    <MatrixArgs for Full MatrixSpace of 0 by 0 dense matrices over
                     Integer Ring; typ=ZERO; entries=None>
                    sage: MatrixArgs(1).finalized()
                    <MatrixArgs for Full MatrixSpace of 1 by 1 dense matrices over
                     Integer Ring; typ=ZERO; entries=None>
                    sage: MatrixArgs(1, 1, 3).finalized()
                    <MatrixArgs for Full MatrixSpace of 1 by 1 dense matrices over
                     Integer Ring; typ=SCALAR; entries=3>
                    sage: MatrixArgs(1, 1, 1, 1).finalized()
                    Traceback (most recent call last):
                    ...
                    TypeError: too many arguments in matrix constructor
                    sage: MatrixArgs(3, nrows=1, ncols=1).finalized()
                    <MatrixArgs for Full MatrixSpace of 1 by 1 dense matrices over
                     Integer Ring; typ=SCALAR; entries=3>
                    sage: MatrixArgs(3, nrows=1).finalized()
                    <MatrixArgs for Full MatrixSpace of 1 by 1 dense matrices over
                     Integer Ring; typ=SCALAR; entries=3>
                    sage: MatrixArgs(3, ncols=1).finalized()
                    <MatrixArgs for Full MatrixSpace of 1 by 1 dense matrices over
                     Integer Ring; typ=SCALAR; entries=3>
        """
    @overload
    def __init__(self) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 318)

                Parse arguments for creating a new matrix.

                See :func:`matrix` for documentation.

                This typically does not raise errors for invalid input, except
                when the arguments cannot be parsed.

                EXAMPLES::

                    sage: from sage.matrix.args import MatrixArgs
                    sage: MatrixArgs().finalized()
                    <MatrixArgs for Full MatrixSpace of 0 by 0 dense matrices over
                     Integer Ring; typ=ZERO; entries=None>
                    sage: MatrixArgs(1).finalized()
                    <MatrixArgs for Full MatrixSpace of 1 by 1 dense matrices over
                     Integer Ring; typ=ZERO; entries=None>
                    sage: MatrixArgs(1, 1, 3).finalized()
                    <MatrixArgs for Full MatrixSpace of 1 by 1 dense matrices over
                     Integer Ring; typ=SCALAR; entries=3>
                    sage: MatrixArgs(1, 1, 1, 1).finalized()
                    Traceback (most recent call last):
                    ...
                    TypeError: too many arguments in matrix constructor
                    sage: MatrixArgs(3, nrows=1, ncols=1).finalized()
                    <MatrixArgs for Full MatrixSpace of 1 by 1 dense matrices over
                     Integer Ring; typ=SCALAR; entries=3>
                    sage: MatrixArgs(3, nrows=1).finalized()
                    <MatrixArgs for Full MatrixSpace of 1 by 1 dense matrices over
                     Integer Ring; typ=SCALAR; entries=3>
                    sage: MatrixArgs(3, ncols=1).finalized()
                    <MatrixArgs for Full MatrixSpace of 1 by 1 dense matrices over
                     Integer Ring; typ=SCALAR; entries=3>
        """
    @overload
    def dict(self, boolconvert=...) -> dict:
        """MatrixArgs.dict(self, bool convert=True) -> dict

        File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 883)

        Return the entries of the matrix as a :class:`dict`.

        The keys of this :class:`dict` are the nonzero positions ``(i,j)``. The
        corresponding value is the entry at that position. Zero values are skipped.

        If ``convert`` is ``True``, the entries are converted to the base
        ring. Otherwise, the entries are returned as given.

        EXAMPLES::

            sage: from sage.matrix.args import MatrixArgs
            sage: L = list(range(6))
            sage: MatrixArgs(2, 3, L).dict()
            {(0, 1): 1, (0, 2): 2, (1, 0): 3, (1, 1): 4, (1, 2): 5}

        ::

            sage: ma = MatrixArgs(GF(2), 2, 3, L)
            sage: ma.dict(convert=False)
            {(0, 1): 1, (0, 2): 2, (1, 0): 3, (1, 1): 4, (1, 2): 5}
            sage: ma.dict()
            {(0, 1): 1, (1, 0): 1, (1, 2): 1}"""
    @overload
    def dict(self) -> Any:
        """MatrixArgs.dict(self, bool convert=True) -> dict

        File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 883)

        Return the entries of the matrix as a :class:`dict`.

        The keys of this :class:`dict` are the nonzero positions ``(i,j)``. The
        corresponding value is the entry at that position. Zero values are skipped.

        If ``convert`` is ``True``, the entries are converted to the base
        ring. Otherwise, the entries are returned as given.

        EXAMPLES::

            sage: from sage.matrix.args import MatrixArgs
            sage: L = list(range(6))
            sage: MatrixArgs(2, 3, L).dict()
            {(0, 1): 1, (0, 2): 2, (1, 0): 3, (1, 1): 4, (1, 2): 5}

        ::

            sage: ma = MatrixArgs(GF(2), 2, 3, L)
            sage: ma.dict(convert=False)
            {(0, 1): 1, (0, 2): 2, (1, 0): 3, (1, 1): 4, (1, 2): 5}
            sage: ma.dict()
            {(0, 1): 1, (1, 0): 1, (1, 2): 1}"""
    @overload
    def dict(self, convert=...) -> Any:
        """MatrixArgs.dict(self, bool convert=True) -> dict

        File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 883)

        Return the entries of the matrix as a :class:`dict`.

        The keys of this :class:`dict` are the nonzero positions ``(i,j)``. The
        corresponding value is the entry at that position. Zero values are skipped.

        If ``convert`` is ``True``, the entries are converted to the base
        ring. Otherwise, the entries are returned as given.

        EXAMPLES::

            sage: from sage.matrix.args import MatrixArgs
            sage: L = list(range(6))
            sage: MatrixArgs(2, 3, L).dict()
            {(0, 1): 1, (0, 2): 2, (1, 0): 3, (1, 1): 4, (1, 2): 5}

        ::

            sage: ma = MatrixArgs(GF(2), 2, 3, L)
            sage: ma.dict(convert=False)
            {(0, 1): 1, (0, 2): 2, (1, 0): 3, (1, 1): 4, (1, 2): 5}
            sage: ma.dict()
            {(0, 1): 1, (1, 0): 1, (1, 2): 1}"""
    @overload
    def dict(self) -> Any:
        """MatrixArgs.dict(self, bool convert=True) -> dict

        File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 883)

        Return the entries of the matrix as a :class:`dict`.

        The keys of this :class:`dict` are the nonzero positions ``(i,j)``. The
        corresponding value is the entry at that position. Zero values are skipped.

        If ``convert`` is ``True``, the entries are converted to the base
        ring. Otherwise, the entries are returned as given.

        EXAMPLES::

            sage: from sage.matrix.args import MatrixArgs
            sage: L = list(range(6))
            sage: MatrixArgs(2, 3, L).dict()
            {(0, 1): 1, (0, 2): 2, (1, 0): 3, (1, 1): 4, (1, 2): 5}

        ::

            sage: ma = MatrixArgs(GF(2), 2, 3, L)
            sage: ma.dict(convert=False)
            {(0, 1): 1, (0, 2): 2, (1, 0): 3, (1, 1): 4, (1, 2): 5}
            sage: ma.dict()
            {(0, 1): 1, (1, 0): 1, (1, 2): 1}"""
    def element(self, *args, **kwargs):
        """MatrixArgs.element(self, bool immutable=False)

        File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 765)

        Return the matrix or morphism.

        INPUT:

        - ``immutable`` -- boolean; if ``True``, the result will be immutable

        OUTPUT: an element of ``self.space``

        .. NOTE::

            This may change ``self.entries``, making it unsafe to access the
            ``self.entries`` attribute after calling this method.

        EXAMPLES::

            sage: from sage.matrix.args import MatrixArgs
            sage: M = matrix(2, 3, range(6), sparse=True)
            sage: ma = MatrixArgs(M); ma.finalized()
            <MatrixArgs for
              Full MatrixSpace of 2 by 3 sparse matrices over Integer Ring;
             typ=MATRIX; entries=[0 1 2]
                                 [3 4 5]>
            sage: M2 = ma.element(immutable=True); M2.parent()
            Full MatrixSpace of 2 by 3 sparse matrices over Integer Ring
            sage: M2.is_immutable()
            True

            sage: ma = MatrixArgs(M, row_keys=['u','v'], column_keys=['a','b','c'])
            sage: ma.finalized()
            <MatrixArgs for
              Set of Morphisms
               from Free module generated by {'a', 'b', 'c'} over Integer Ring
                 to Free module generated by {'u', 'v'} over Integer Ring
                 in Category of finite dimensional modules with basis over Integer Ring;
             typ=MATRIX; entries=[0 1 2]
                                 [3 4 5]>
            sage: phi = ma.element(); phi
            Generic morphism:
            From: Free module generated by {'a', 'b', 'c'} over Integer Ring
            To:   Free module generated by {'u', 'v'} over Integer Ring"""
    @overload
    def finalized(self) -> Any:
        """MatrixArgs.finalized(self)

        File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 1046)

        Determine all missing values.

        Depending on the input, this might be a non-trivial operation.
        In some cases, this will do most of the work of constructing the
        matrix. That is actually not a problem since we eventually want
        to construct the matrix anyway. However, care is taken to avoid
        double work or needless checking or copying.

        OUTPUT: ``self``

        EXAMPLES::

            sage: from sage.matrix.args import MatrixArgs
            sage: MatrixArgs(pi).finalized()                                            # needs sage.symbolic
            Traceback (most recent call last):
            ...
            TypeError: the dimensions of the matrix must be specified
            sage: MatrixArgs(RR, pi).finalized()                                        # needs sage.symbolic
            Traceback (most recent call last):
            ...
            TypeError: the dimensions of the matrix must be specified
            sage: MatrixArgs(2, 3, 0.0).finalized()
            <MatrixArgs for Full MatrixSpace of 2 by 3 dense matrices over Real
             Field with 53 bits of precision; typ=ZERO; entries=0.000000000000000>
            sage: MatrixArgs(RR, 2, 3, 1.0).finalized()
            Traceback (most recent call last):
            ...
            TypeError: nonzero scalar matrix must be square

        Check :issue:`19134`::

            sage: matrix(2, 3, [])
            Traceback (most recent call last):
            ...
            ValueError: sequence too short (expected length 6, got 0)
            sage: matrix(ZZ, 2, 3, [])
            Traceback (most recent call last):
            ...
            ValueError: sequence too short (expected length 6, got 0)
            sage: matrix(2, 3, [1])
            Traceback (most recent call last):
            ...
            ValueError: sequence too short (expected length 6, got 1)

        Check github issue #36065:

            sage: # needs sage.rings.number_field
            sage: class MyAlgebraicNumber(sage.rings.qqbar.AlgebraicNumber):
            ....:     def __bool__(self):
            ....:         raise ValueError
            sage: matrix(1, 1, MyAlgebraicNumber(0))
            [0]
            sage: matrix(1, 1, MyAlgebraicNumber(3))
            [3]
            sage: matrix(1, 2, MyAlgebraicNumber(0))
            Traceback (most recent call last):
            ...
            TypeError: scalar matrix must be square if the value cannot be determined to be zero
            sage: matrix(1, 2, MyAlgebraicNumber(3))
            Traceback (most recent call last):
            ...
            TypeError: scalar matrix must be square if the value cannot be determined to be zero"""
    @overload
    def finalized(self) -> Any:
        """MatrixArgs.finalized(self)

        File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 1046)

        Determine all missing values.

        Depending on the input, this might be a non-trivial operation.
        In some cases, this will do most of the work of constructing the
        matrix. That is actually not a problem since we eventually want
        to construct the matrix anyway. However, care is taken to avoid
        double work or needless checking or copying.

        OUTPUT: ``self``

        EXAMPLES::

            sage: from sage.matrix.args import MatrixArgs
            sage: MatrixArgs(pi).finalized()                                            # needs sage.symbolic
            Traceback (most recent call last):
            ...
            TypeError: the dimensions of the matrix must be specified
            sage: MatrixArgs(RR, pi).finalized()                                        # needs sage.symbolic
            Traceback (most recent call last):
            ...
            TypeError: the dimensions of the matrix must be specified
            sage: MatrixArgs(2, 3, 0.0).finalized()
            <MatrixArgs for Full MatrixSpace of 2 by 3 dense matrices over Real
             Field with 53 bits of precision; typ=ZERO; entries=0.000000000000000>
            sage: MatrixArgs(RR, 2, 3, 1.0).finalized()
            Traceback (most recent call last):
            ...
            TypeError: nonzero scalar matrix must be square

        Check :issue:`19134`::

            sage: matrix(2, 3, [])
            Traceback (most recent call last):
            ...
            ValueError: sequence too short (expected length 6, got 0)
            sage: matrix(ZZ, 2, 3, [])
            Traceback (most recent call last):
            ...
            ValueError: sequence too short (expected length 6, got 0)
            sage: matrix(2, 3, [1])
            Traceback (most recent call last):
            ...
            ValueError: sequence too short (expected length 6, got 1)

        Check github issue #36065:

            sage: # needs sage.rings.number_field
            sage: class MyAlgebraicNumber(sage.rings.qqbar.AlgebraicNumber):
            ....:     def __bool__(self):
            ....:         raise ValueError
            sage: matrix(1, 1, MyAlgebraicNumber(0))
            [0]
            sage: matrix(1, 1, MyAlgebraicNumber(3))
            [3]
            sage: matrix(1, 2, MyAlgebraicNumber(0))
            Traceback (most recent call last):
            ...
            TypeError: scalar matrix must be square if the value cannot be determined to be zero
            sage: matrix(1, 2, MyAlgebraicNumber(3))
            Traceback (most recent call last):
            ...
            TypeError: scalar matrix must be square if the value cannot be determined to be zero"""
    @overload
    def finalized(self) -> Any:
        """MatrixArgs.finalized(self)

        File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 1046)

        Determine all missing values.

        Depending on the input, this might be a non-trivial operation.
        In some cases, this will do most of the work of constructing the
        matrix. That is actually not a problem since we eventually want
        to construct the matrix anyway. However, care is taken to avoid
        double work or needless checking or copying.

        OUTPUT: ``self``

        EXAMPLES::

            sage: from sage.matrix.args import MatrixArgs
            sage: MatrixArgs(pi).finalized()                                            # needs sage.symbolic
            Traceback (most recent call last):
            ...
            TypeError: the dimensions of the matrix must be specified
            sage: MatrixArgs(RR, pi).finalized()                                        # needs sage.symbolic
            Traceback (most recent call last):
            ...
            TypeError: the dimensions of the matrix must be specified
            sage: MatrixArgs(2, 3, 0.0).finalized()
            <MatrixArgs for Full MatrixSpace of 2 by 3 dense matrices over Real
             Field with 53 bits of precision; typ=ZERO; entries=0.000000000000000>
            sage: MatrixArgs(RR, 2, 3, 1.0).finalized()
            Traceback (most recent call last):
            ...
            TypeError: nonzero scalar matrix must be square

        Check :issue:`19134`::

            sage: matrix(2, 3, [])
            Traceback (most recent call last):
            ...
            ValueError: sequence too short (expected length 6, got 0)
            sage: matrix(ZZ, 2, 3, [])
            Traceback (most recent call last):
            ...
            ValueError: sequence too short (expected length 6, got 0)
            sage: matrix(2, 3, [1])
            Traceback (most recent call last):
            ...
            ValueError: sequence too short (expected length 6, got 1)

        Check github issue #36065:

            sage: # needs sage.rings.number_field
            sage: class MyAlgebraicNumber(sage.rings.qqbar.AlgebraicNumber):
            ....:     def __bool__(self):
            ....:         raise ValueError
            sage: matrix(1, 1, MyAlgebraicNumber(0))
            [0]
            sage: matrix(1, 1, MyAlgebraicNumber(3))
            [3]
            sage: matrix(1, 2, MyAlgebraicNumber(0))
            Traceback (most recent call last):
            ...
            TypeError: scalar matrix must be square if the value cannot be determined to be zero
            sage: matrix(1, 2, MyAlgebraicNumber(3))
            Traceback (most recent call last):
            ...
            TypeError: scalar matrix must be square if the value cannot be determined to be zero"""
    @overload
    def finalized(self) -> Any:
        """MatrixArgs.finalized(self)

        File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 1046)

        Determine all missing values.

        Depending on the input, this might be a non-trivial operation.
        In some cases, this will do most of the work of constructing the
        matrix. That is actually not a problem since we eventually want
        to construct the matrix anyway. However, care is taken to avoid
        double work or needless checking or copying.

        OUTPUT: ``self``

        EXAMPLES::

            sage: from sage.matrix.args import MatrixArgs
            sage: MatrixArgs(pi).finalized()                                            # needs sage.symbolic
            Traceback (most recent call last):
            ...
            TypeError: the dimensions of the matrix must be specified
            sage: MatrixArgs(RR, pi).finalized()                                        # needs sage.symbolic
            Traceback (most recent call last):
            ...
            TypeError: the dimensions of the matrix must be specified
            sage: MatrixArgs(2, 3, 0.0).finalized()
            <MatrixArgs for Full MatrixSpace of 2 by 3 dense matrices over Real
             Field with 53 bits of precision; typ=ZERO; entries=0.000000000000000>
            sage: MatrixArgs(RR, 2, 3, 1.0).finalized()
            Traceback (most recent call last):
            ...
            TypeError: nonzero scalar matrix must be square

        Check :issue:`19134`::

            sage: matrix(2, 3, [])
            Traceback (most recent call last):
            ...
            ValueError: sequence too short (expected length 6, got 0)
            sage: matrix(ZZ, 2, 3, [])
            Traceback (most recent call last):
            ...
            ValueError: sequence too short (expected length 6, got 0)
            sage: matrix(2, 3, [1])
            Traceback (most recent call last):
            ...
            ValueError: sequence too short (expected length 6, got 1)

        Check github issue #36065:

            sage: # needs sage.rings.number_field
            sage: class MyAlgebraicNumber(sage.rings.qqbar.AlgebraicNumber):
            ....:     def __bool__(self):
            ....:         raise ValueError
            sage: matrix(1, 1, MyAlgebraicNumber(0))
            [0]
            sage: matrix(1, 1, MyAlgebraicNumber(3))
            [3]
            sage: matrix(1, 2, MyAlgebraicNumber(0))
            Traceback (most recent call last):
            ...
            TypeError: scalar matrix must be square if the value cannot be determined to be zero
            sage: matrix(1, 2, MyAlgebraicNumber(3))
            Traceback (most recent call last):
            ...
            TypeError: scalar matrix must be square if the value cannot be determined to be zero"""
    @overload
    def finalized(self) -> Any:
        """MatrixArgs.finalized(self)

        File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 1046)

        Determine all missing values.

        Depending on the input, this might be a non-trivial operation.
        In some cases, this will do most of the work of constructing the
        matrix. That is actually not a problem since we eventually want
        to construct the matrix anyway. However, care is taken to avoid
        double work or needless checking or copying.

        OUTPUT: ``self``

        EXAMPLES::

            sage: from sage.matrix.args import MatrixArgs
            sage: MatrixArgs(pi).finalized()                                            # needs sage.symbolic
            Traceback (most recent call last):
            ...
            TypeError: the dimensions of the matrix must be specified
            sage: MatrixArgs(RR, pi).finalized()                                        # needs sage.symbolic
            Traceback (most recent call last):
            ...
            TypeError: the dimensions of the matrix must be specified
            sage: MatrixArgs(2, 3, 0.0).finalized()
            <MatrixArgs for Full MatrixSpace of 2 by 3 dense matrices over Real
             Field with 53 bits of precision; typ=ZERO; entries=0.000000000000000>
            sage: MatrixArgs(RR, 2, 3, 1.0).finalized()
            Traceback (most recent call last):
            ...
            TypeError: nonzero scalar matrix must be square

        Check :issue:`19134`::

            sage: matrix(2, 3, [])
            Traceback (most recent call last):
            ...
            ValueError: sequence too short (expected length 6, got 0)
            sage: matrix(ZZ, 2, 3, [])
            Traceback (most recent call last):
            ...
            ValueError: sequence too short (expected length 6, got 0)
            sage: matrix(2, 3, [1])
            Traceback (most recent call last):
            ...
            ValueError: sequence too short (expected length 6, got 1)

        Check github issue #36065:

            sage: # needs sage.rings.number_field
            sage: class MyAlgebraicNumber(sage.rings.qqbar.AlgebraicNumber):
            ....:     def __bool__(self):
            ....:         raise ValueError
            sage: matrix(1, 1, MyAlgebraicNumber(0))
            [0]
            sage: matrix(1, 1, MyAlgebraicNumber(3))
            [3]
            sage: matrix(1, 2, MyAlgebraicNumber(0))
            Traceback (most recent call last):
            ...
            TypeError: scalar matrix must be square if the value cannot be determined to be zero
            sage: matrix(1, 2, MyAlgebraicNumber(3))
            Traceback (most recent call last):
            ...
            TypeError: scalar matrix must be square if the value cannot be determined to be zero"""
    @overload
    def iter(self, boolconvert=..., boolsparse=...) -> Any:
        """MatrixArgs.iter(self, bool convert=True, bool sparse=False)

        File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 490)

        Iteration over the entries in the matrix.

        INPUT:

        - ``convert`` -- if ``True``, the entries are converted to the
          base right; if ``False``, the entries are returned as given

        - ``sparse`` -- see OUTPUT below

        OUTPUT: iterator

        - If ``sparse`` is False: yield all entries of the matrix in
          the following order::

            [1 2 3]
            [4 5 6]

        - If ``sparse`` is True: yield instances of
          :class:`SparseEntry`. The indices ``(i, j)`` are guaranteed to
          lie within the matrix. Zero entries in the input are *not*
          skipped.

        .. WARNING::

            If an iterator is given as input to :class:`MatrixArgs`, it
            may be exhausted breaking any further usage. Otherwise, it
            is safe to iterate multiple times.

        EXAMPLES::

            sage: from sage.matrix.args import SparseEntry, MatrixArgs
            sage: ma = MatrixArgs(ZZ, 2, 3, iter(range(6)))
            sage: list(ma.iter())
            [0, 1, 2, 3, 4, 5]
            sage: ma = MatrixArgs(ZZ, 3, 3, [SparseEntry(0, 0, 0)])
            sage: list(ma.iter())
            Traceback (most recent call last):
            ...
            TypeError: dense iteration is not supported for sparse input

        Sparse examples::

            sage: ma = MatrixArgs(3, 3, pi)                                             # needs sage.symbolic
            sage: list(ma.iter(sparse=True))                                            # needs sage.symbolic
            [SparseEntry(0, 0, pi), SparseEntry(1, 1, pi), SparseEntry(2, 2, pi)]
            sage: ma = MatrixArgs(2, 3)
            sage: list(ma.iter(sparse=True))
            []
            sage: ma = MatrixArgs(2, 2, lambda i, j: i > j)
            sage: list(ma.iter(convert=False, sparse=True))
            [SparseEntry(0, 0, False),
             SparseEntry(0, 1, False),
             SparseEntry(1, 0, True),
             SparseEntry(1, 1, False)]
            sage: ma = MatrixArgs(2, 2, {(1,0):88, (0,1):89})
            sage: sorted(tuple(x) for x in ma.iter(sparse=True))
            [(0, 1, 89), (1, 0, 88)]
            sage: ma = MatrixArgs(QQ, 2, 1, {(1,0):88, (0,1):89})
            sage: ma.finalized()
            Traceback (most recent call last):
            ...
            IndexError: invalid column index 1
            sage: ma = MatrixArgs(QQ, 1, 2, {(1,0):88, (0,1):89})
            sage: ma.finalized()
            Traceback (most recent call last):
            ...
            IndexError: invalid row index 1"""
    @overload
    def iter(self) -> Any:
        """MatrixArgs.iter(self, bool convert=True, bool sparse=False)

        File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 490)

        Iteration over the entries in the matrix.

        INPUT:

        - ``convert`` -- if ``True``, the entries are converted to the
          base right; if ``False``, the entries are returned as given

        - ``sparse`` -- see OUTPUT below

        OUTPUT: iterator

        - If ``sparse`` is False: yield all entries of the matrix in
          the following order::

            [1 2 3]
            [4 5 6]

        - If ``sparse`` is True: yield instances of
          :class:`SparseEntry`. The indices ``(i, j)`` are guaranteed to
          lie within the matrix. Zero entries in the input are *not*
          skipped.

        .. WARNING::

            If an iterator is given as input to :class:`MatrixArgs`, it
            may be exhausted breaking any further usage. Otherwise, it
            is safe to iterate multiple times.

        EXAMPLES::

            sage: from sage.matrix.args import SparseEntry, MatrixArgs
            sage: ma = MatrixArgs(ZZ, 2, 3, iter(range(6)))
            sage: list(ma.iter())
            [0, 1, 2, 3, 4, 5]
            sage: ma = MatrixArgs(ZZ, 3, 3, [SparseEntry(0, 0, 0)])
            sage: list(ma.iter())
            Traceback (most recent call last):
            ...
            TypeError: dense iteration is not supported for sparse input

        Sparse examples::

            sage: ma = MatrixArgs(3, 3, pi)                                             # needs sage.symbolic
            sage: list(ma.iter(sparse=True))                                            # needs sage.symbolic
            [SparseEntry(0, 0, pi), SparseEntry(1, 1, pi), SparseEntry(2, 2, pi)]
            sage: ma = MatrixArgs(2, 3)
            sage: list(ma.iter(sparse=True))
            []
            sage: ma = MatrixArgs(2, 2, lambda i, j: i > j)
            sage: list(ma.iter(convert=False, sparse=True))
            [SparseEntry(0, 0, False),
             SparseEntry(0, 1, False),
             SparseEntry(1, 0, True),
             SparseEntry(1, 1, False)]
            sage: ma = MatrixArgs(2, 2, {(1,0):88, (0,1):89})
            sage: sorted(tuple(x) for x in ma.iter(sparse=True))
            [(0, 1, 89), (1, 0, 88)]
            sage: ma = MatrixArgs(QQ, 2, 1, {(1,0):88, (0,1):89})
            sage: ma.finalized()
            Traceback (most recent call last):
            ...
            IndexError: invalid column index 1
            sage: ma = MatrixArgs(QQ, 1, 2, {(1,0):88, (0,1):89})
            sage: ma.finalized()
            Traceback (most recent call last):
            ...
            IndexError: invalid row index 1"""
    @overload
    def iter(self) -> Any:
        """MatrixArgs.iter(self, bool convert=True, bool sparse=False)

        File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 490)

        Iteration over the entries in the matrix.

        INPUT:

        - ``convert`` -- if ``True``, the entries are converted to the
          base right; if ``False``, the entries are returned as given

        - ``sparse`` -- see OUTPUT below

        OUTPUT: iterator

        - If ``sparse`` is False: yield all entries of the matrix in
          the following order::

            [1 2 3]
            [4 5 6]

        - If ``sparse`` is True: yield instances of
          :class:`SparseEntry`. The indices ``(i, j)`` are guaranteed to
          lie within the matrix. Zero entries in the input are *not*
          skipped.

        .. WARNING::

            If an iterator is given as input to :class:`MatrixArgs`, it
            may be exhausted breaking any further usage. Otherwise, it
            is safe to iterate multiple times.

        EXAMPLES::

            sage: from sage.matrix.args import SparseEntry, MatrixArgs
            sage: ma = MatrixArgs(ZZ, 2, 3, iter(range(6)))
            sage: list(ma.iter())
            [0, 1, 2, 3, 4, 5]
            sage: ma = MatrixArgs(ZZ, 3, 3, [SparseEntry(0, 0, 0)])
            sage: list(ma.iter())
            Traceback (most recent call last):
            ...
            TypeError: dense iteration is not supported for sparse input

        Sparse examples::

            sage: ma = MatrixArgs(3, 3, pi)                                             # needs sage.symbolic
            sage: list(ma.iter(sparse=True))                                            # needs sage.symbolic
            [SparseEntry(0, 0, pi), SparseEntry(1, 1, pi), SparseEntry(2, 2, pi)]
            sage: ma = MatrixArgs(2, 3)
            sage: list(ma.iter(sparse=True))
            []
            sage: ma = MatrixArgs(2, 2, lambda i, j: i > j)
            sage: list(ma.iter(convert=False, sparse=True))
            [SparseEntry(0, 0, False),
             SparseEntry(0, 1, False),
             SparseEntry(1, 0, True),
             SparseEntry(1, 1, False)]
            sage: ma = MatrixArgs(2, 2, {(1,0):88, (0,1):89})
            sage: sorted(tuple(x) for x in ma.iter(sparse=True))
            [(0, 1, 89), (1, 0, 88)]
            sage: ma = MatrixArgs(QQ, 2, 1, {(1,0):88, (0,1):89})
            sage: ma.finalized()
            Traceback (most recent call last):
            ...
            IndexError: invalid column index 1
            sage: ma = MatrixArgs(QQ, 1, 2, {(1,0):88, (0,1):89})
            sage: ma.finalized()
            Traceback (most recent call last):
            ...
            IndexError: invalid row index 1"""
    @overload
    def iter(self, sparse=...) -> Any:
        """MatrixArgs.iter(self, bool convert=True, bool sparse=False)

        File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 490)

        Iteration over the entries in the matrix.

        INPUT:

        - ``convert`` -- if ``True``, the entries are converted to the
          base right; if ``False``, the entries are returned as given

        - ``sparse`` -- see OUTPUT below

        OUTPUT: iterator

        - If ``sparse`` is False: yield all entries of the matrix in
          the following order::

            [1 2 3]
            [4 5 6]

        - If ``sparse`` is True: yield instances of
          :class:`SparseEntry`. The indices ``(i, j)`` are guaranteed to
          lie within the matrix. Zero entries in the input are *not*
          skipped.

        .. WARNING::

            If an iterator is given as input to :class:`MatrixArgs`, it
            may be exhausted breaking any further usage. Otherwise, it
            is safe to iterate multiple times.

        EXAMPLES::

            sage: from sage.matrix.args import SparseEntry, MatrixArgs
            sage: ma = MatrixArgs(ZZ, 2, 3, iter(range(6)))
            sage: list(ma.iter())
            [0, 1, 2, 3, 4, 5]
            sage: ma = MatrixArgs(ZZ, 3, 3, [SparseEntry(0, 0, 0)])
            sage: list(ma.iter())
            Traceback (most recent call last):
            ...
            TypeError: dense iteration is not supported for sparse input

        Sparse examples::

            sage: ma = MatrixArgs(3, 3, pi)                                             # needs sage.symbolic
            sage: list(ma.iter(sparse=True))                                            # needs sage.symbolic
            [SparseEntry(0, 0, pi), SparseEntry(1, 1, pi), SparseEntry(2, 2, pi)]
            sage: ma = MatrixArgs(2, 3)
            sage: list(ma.iter(sparse=True))
            []
            sage: ma = MatrixArgs(2, 2, lambda i, j: i > j)
            sage: list(ma.iter(convert=False, sparse=True))
            [SparseEntry(0, 0, False),
             SparseEntry(0, 1, False),
             SparseEntry(1, 0, True),
             SparseEntry(1, 1, False)]
            sage: ma = MatrixArgs(2, 2, {(1,0):88, (0,1):89})
            sage: sorted(tuple(x) for x in ma.iter(sparse=True))
            [(0, 1, 89), (1, 0, 88)]
            sage: ma = MatrixArgs(QQ, 2, 1, {(1,0):88, (0,1):89})
            sage: ma.finalized()
            Traceback (most recent call last):
            ...
            IndexError: invalid column index 1
            sage: ma = MatrixArgs(QQ, 1, 2, {(1,0):88, (0,1):89})
            sage: ma.finalized()
            Traceback (most recent call last):
            ...
            IndexError: invalid row index 1"""
    @overload
    def iter(self, sparse=...) -> Any:
        """MatrixArgs.iter(self, bool convert=True, bool sparse=False)

        File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 490)

        Iteration over the entries in the matrix.

        INPUT:

        - ``convert`` -- if ``True``, the entries are converted to the
          base right; if ``False``, the entries are returned as given

        - ``sparse`` -- see OUTPUT below

        OUTPUT: iterator

        - If ``sparse`` is False: yield all entries of the matrix in
          the following order::

            [1 2 3]
            [4 5 6]

        - If ``sparse`` is True: yield instances of
          :class:`SparseEntry`. The indices ``(i, j)`` are guaranteed to
          lie within the matrix. Zero entries in the input are *not*
          skipped.

        .. WARNING::

            If an iterator is given as input to :class:`MatrixArgs`, it
            may be exhausted breaking any further usage. Otherwise, it
            is safe to iterate multiple times.

        EXAMPLES::

            sage: from sage.matrix.args import SparseEntry, MatrixArgs
            sage: ma = MatrixArgs(ZZ, 2, 3, iter(range(6)))
            sage: list(ma.iter())
            [0, 1, 2, 3, 4, 5]
            sage: ma = MatrixArgs(ZZ, 3, 3, [SparseEntry(0, 0, 0)])
            sage: list(ma.iter())
            Traceback (most recent call last):
            ...
            TypeError: dense iteration is not supported for sparse input

        Sparse examples::

            sage: ma = MatrixArgs(3, 3, pi)                                             # needs sage.symbolic
            sage: list(ma.iter(sparse=True))                                            # needs sage.symbolic
            [SparseEntry(0, 0, pi), SparseEntry(1, 1, pi), SparseEntry(2, 2, pi)]
            sage: ma = MatrixArgs(2, 3)
            sage: list(ma.iter(sparse=True))
            []
            sage: ma = MatrixArgs(2, 2, lambda i, j: i > j)
            sage: list(ma.iter(convert=False, sparse=True))
            [SparseEntry(0, 0, False),
             SparseEntry(0, 1, False),
             SparseEntry(1, 0, True),
             SparseEntry(1, 1, False)]
            sage: ma = MatrixArgs(2, 2, {(1,0):88, (0,1):89})
            sage: sorted(tuple(x) for x in ma.iter(sparse=True))
            [(0, 1, 89), (1, 0, 88)]
            sage: ma = MatrixArgs(QQ, 2, 1, {(1,0):88, (0,1):89})
            sage: ma.finalized()
            Traceback (most recent call last):
            ...
            IndexError: invalid column index 1
            sage: ma = MatrixArgs(QQ, 1, 2, {(1,0):88, (0,1):89})
            sage: ma.finalized()
            Traceback (most recent call last):
            ...
            IndexError: invalid row index 1"""
    @overload
    def iter(self, convert=..., sparse=...) -> Any:
        """MatrixArgs.iter(self, bool convert=True, bool sparse=False)

        File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 490)

        Iteration over the entries in the matrix.

        INPUT:

        - ``convert`` -- if ``True``, the entries are converted to the
          base right; if ``False``, the entries are returned as given

        - ``sparse`` -- see OUTPUT below

        OUTPUT: iterator

        - If ``sparse`` is False: yield all entries of the matrix in
          the following order::

            [1 2 3]
            [4 5 6]

        - If ``sparse`` is True: yield instances of
          :class:`SparseEntry`. The indices ``(i, j)`` are guaranteed to
          lie within the matrix. Zero entries in the input are *not*
          skipped.

        .. WARNING::

            If an iterator is given as input to :class:`MatrixArgs`, it
            may be exhausted breaking any further usage. Otherwise, it
            is safe to iterate multiple times.

        EXAMPLES::

            sage: from sage.matrix.args import SparseEntry, MatrixArgs
            sage: ma = MatrixArgs(ZZ, 2, 3, iter(range(6)))
            sage: list(ma.iter())
            [0, 1, 2, 3, 4, 5]
            sage: ma = MatrixArgs(ZZ, 3, 3, [SparseEntry(0, 0, 0)])
            sage: list(ma.iter())
            Traceback (most recent call last):
            ...
            TypeError: dense iteration is not supported for sparse input

        Sparse examples::

            sage: ma = MatrixArgs(3, 3, pi)                                             # needs sage.symbolic
            sage: list(ma.iter(sparse=True))                                            # needs sage.symbolic
            [SparseEntry(0, 0, pi), SparseEntry(1, 1, pi), SparseEntry(2, 2, pi)]
            sage: ma = MatrixArgs(2, 3)
            sage: list(ma.iter(sparse=True))
            []
            sage: ma = MatrixArgs(2, 2, lambda i, j: i > j)
            sage: list(ma.iter(convert=False, sparse=True))
            [SparseEntry(0, 0, False),
             SparseEntry(0, 1, False),
             SparseEntry(1, 0, True),
             SparseEntry(1, 1, False)]
            sage: ma = MatrixArgs(2, 2, {(1,0):88, (0,1):89})
            sage: sorted(tuple(x) for x in ma.iter(sparse=True))
            [(0, 1, 89), (1, 0, 88)]
            sage: ma = MatrixArgs(QQ, 2, 1, {(1,0):88, (0,1):89})
            sage: ma.finalized()
            Traceback (most recent call last):
            ...
            IndexError: invalid column index 1
            sage: ma = MatrixArgs(QQ, 1, 2, {(1,0):88, (0,1):89})
            sage: ma.finalized()
            Traceback (most recent call last):
            ...
            IndexError: invalid row index 1"""
    @overload
    def iter(self, sparse=...) -> Any:
        """MatrixArgs.iter(self, bool convert=True, bool sparse=False)

        File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 490)

        Iteration over the entries in the matrix.

        INPUT:

        - ``convert`` -- if ``True``, the entries are converted to the
          base right; if ``False``, the entries are returned as given

        - ``sparse`` -- see OUTPUT below

        OUTPUT: iterator

        - If ``sparse`` is False: yield all entries of the matrix in
          the following order::

            [1 2 3]
            [4 5 6]

        - If ``sparse`` is True: yield instances of
          :class:`SparseEntry`. The indices ``(i, j)`` are guaranteed to
          lie within the matrix. Zero entries in the input are *not*
          skipped.

        .. WARNING::

            If an iterator is given as input to :class:`MatrixArgs`, it
            may be exhausted breaking any further usage. Otherwise, it
            is safe to iterate multiple times.

        EXAMPLES::

            sage: from sage.matrix.args import SparseEntry, MatrixArgs
            sage: ma = MatrixArgs(ZZ, 2, 3, iter(range(6)))
            sage: list(ma.iter())
            [0, 1, 2, 3, 4, 5]
            sage: ma = MatrixArgs(ZZ, 3, 3, [SparseEntry(0, 0, 0)])
            sage: list(ma.iter())
            Traceback (most recent call last):
            ...
            TypeError: dense iteration is not supported for sparse input

        Sparse examples::

            sage: ma = MatrixArgs(3, 3, pi)                                             # needs sage.symbolic
            sage: list(ma.iter(sparse=True))                                            # needs sage.symbolic
            [SparseEntry(0, 0, pi), SparseEntry(1, 1, pi), SparseEntry(2, 2, pi)]
            sage: ma = MatrixArgs(2, 3)
            sage: list(ma.iter(sparse=True))
            []
            sage: ma = MatrixArgs(2, 2, lambda i, j: i > j)
            sage: list(ma.iter(convert=False, sparse=True))
            [SparseEntry(0, 0, False),
             SparseEntry(0, 1, False),
             SparseEntry(1, 0, True),
             SparseEntry(1, 1, False)]
            sage: ma = MatrixArgs(2, 2, {(1,0):88, (0,1):89})
            sage: sorted(tuple(x) for x in ma.iter(sparse=True))
            [(0, 1, 89), (1, 0, 88)]
            sage: ma = MatrixArgs(QQ, 2, 1, {(1,0):88, (0,1):89})
            sage: ma.finalized()
            Traceback (most recent call last):
            ...
            IndexError: invalid column index 1
            sage: ma = MatrixArgs(QQ, 1, 2, {(1,0):88, (0,1):89})
            sage: ma.finalized()
            Traceback (most recent call last):
            ...
            IndexError: invalid row index 1"""
    @overload
    def list(self, boolconvert=...) -> list:
        """MatrixArgs.list(self, bool convert=True) -> list

        File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 816)

        Return the entries of the matrix as a flat list of scalars.

        If possible and ``convert=False``, this returns a direct
        reference to ``self.entries`` without copying.

        INPUT:

        - ``convert`` -- if ``True``, the entries are converted to the base
          ring; otherwise, the entries are returned as given

        .. NOTE::

            This changes ``self.entries`` to the returned list. This
            means that it is unsafe to access the ``self.entries``
            attribute after calling this method.

        EXAMPLES::

            sage: from sage.matrix.args import MatrixArgs
            sage: L = list(range(6))
            sage: MatrixArgs(2, 3, L).list()
            [0, 1, 2, 3, 4, 5]

        ::

            sage: ma = MatrixArgs(RDF, 2, 3, L)
            sage: ma.list(convert=False)
            [0, 1, 2, 3, 4, 5]
            sage: ma.list()
            [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]

        If we remove our reference to the input ``L`` and
        ``convert=False``, no copy is made::

            sage: idL = id(L)
            sage: ma = MatrixArgs(2, 3, L)
            sage: del L
            sage: L = ma.list(convert=False)
            sage: id(L) == idL
            True"""
    @overload
    def list(self) -> Any:
        """MatrixArgs.list(self, bool convert=True) -> list

        File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 816)

        Return the entries of the matrix as a flat list of scalars.

        If possible and ``convert=False``, this returns a direct
        reference to ``self.entries`` without copying.

        INPUT:

        - ``convert`` -- if ``True``, the entries are converted to the base
          ring; otherwise, the entries are returned as given

        .. NOTE::

            This changes ``self.entries`` to the returned list. This
            means that it is unsafe to access the ``self.entries``
            attribute after calling this method.

        EXAMPLES::

            sage: from sage.matrix.args import MatrixArgs
            sage: L = list(range(6))
            sage: MatrixArgs(2, 3, L).list()
            [0, 1, 2, 3, 4, 5]

        ::

            sage: ma = MatrixArgs(RDF, 2, 3, L)
            sage: ma.list(convert=False)
            [0, 1, 2, 3, 4, 5]
            sage: ma.list()
            [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]

        If we remove our reference to the input ``L`` and
        ``convert=False``, no copy is made::

            sage: idL = id(L)
            sage: ma = MatrixArgs(2, 3, L)
            sage: del L
            sage: L = ma.list(convert=False)
            sage: id(L) == idL
            True"""
    @overload
    def list(self, convert=...) -> Any:
        """MatrixArgs.list(self, bool convert=True) -> list

        File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 816)

        Return the entries of the matrix as a flat list of scalars.

        If possible and ``convert=False``, this returns a direct
        reference to ``self.entries`` without copying.

        INPUT:

        - ``convert`` -- if ``True``, the entries are converted to the base
          ring; otherwise, the entries are returned as given

        .. NOTE::

            This changes ``self.entries`` to the returned list. This
            means that it is unsafe to access the ``self.entries``
            attribute after calling this method.

        EXAMPLES::

            sage: from sage.matrix.args import MatrixArgs
            sage: L = list(range(6))
            sage: MatrixArgs(2, 3, L).list()
            [0, 1, 2, 3, 4, 5]

        ::

            sage: ma = MatrixArgs(RDF, 2, 3, L)
            sage: ma.list(convert=False)
            [0, 1, 2, 3, 4, 5]
            sage: ma.list()
            [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]

        If we remove our reference to the input ``L`` and
        ``convert=False``, no copy is made::

            sage: idL = id(L)
            sage: ma = MatrixArgs(2, 3, L)
            sage: del L
            sage: L = ma.list(convert=False)
            sage: id(L) == idL
            True"""
    @overload
    def list(self) -> Any:
        """MatrixArgs.list(self, bool convert=True) -> list

        File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 816)

        Return the entries of the matrix as a flat list of scalars.

        If possible and ``convert=False``, this returns a direct
        reference to ``self.entries`` without copying.

        INPUT:

        - ``convert`` -- if ``True``, the entries are converted to the base
          ring; otherwise, the entries are returned as given

        .. NOTE::

            This changes ``self.entries`` to the returned list. This
            means that it is unsafe to access the ``self.entries``
            attribute after calling this method.

        EXAMPLES::

            sage: from sage.matrix.args import MatrixArgs
            sage: L = list(range(6))
            sage: MatrixArgs(2, 3, L).list()
            [0, 1, 2, 3, 4, 5]

        ::

            sage: ma = MatrixArgs(RDF, 2, 3, L)
            sage: ma.list(convert=False)
            [0, 1, 2, 3, 4, 5]
            sage: ma.list()
            [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]

        If we remove our reference to the input ``L`` and
        ``convert=False``, no copy is made::

            sage: idL = id(L)
            sage: ma = MatrixArgs(2, 3, L)
            sage: del L
            sage: L = ma.list(convert=False)
            sage: id(L) == idL
            True"""
    @overload
    def list(self, convert=...) -> Any:
        """MatrixArgs.list(self, bool convert=True) -> list

        File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 816)

        Return the entries of the matrix as a flat list of scalars.

        If possible and ``convert=False``, this returns a direct
        reference to ``self.entries`` without copying.

        INPUT:

        - ``convert`` -- if ``True``, the entries are converted to the base
          ring; otherwise, the entries are returned as given

        .. NOTE::

            This changes ``self.entries`` to the returned list. This
            means that it is unsafe to access the ``self.entries``
            attribute after calling this method.

        EXAMPLES::

            sage: from sage.matrix.args import MatrixArgs
            sage: L = list(range(6))
            sage: MatrixArgs(2, 3, L).list()
            [0, 1, 2, 3, 4, 5]

        ::

            sage: ma = MatrixArgs(RDF, 2, 3, L)
            sage: ma.list(convert=False)
            [0, 1, 2, 3, 4, 5]
            sage: ma.list()
            [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]

        If we remove our reference to the input ``L`` and
        ``convert=False``, no copy is made::

            sage: idL = id(L)
            sage: ma = MatrixArgs(2, 3, L)
            sage: del L
            sage: L = ma.list(convert=False)
            sage: id(L) == idL
            True"""
    @overload
    def matrix(self, boolconvert=...) -> Matrix:
        """MatrixArgs.matrix(self, bool convert=True) -> Matrix

        File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 671)

        Return the entries of the matrix as a Sage Matrix.

        If possible, this returns a direct reference to
        ``self.entries`` without copying.

        INPUT:

        - ``convert`` -- if ``True``, the matrix is guaranteed to have
          the correct parent matrix space. If ``False``, the input matrix
          may be returned even if it lies in the wrong space.

        .. NOTE::

            This changes ``self.entries`` to the returned matrix. This
            means that it is unsafe to access the ``self.entries``
            attribute after calling this method.

        EXAMPLES::

            sage: from sage.matrix.args import MatrixArgs
            sage: M = matrix(2, 3, range(6), sparse=True)

        ::

            sage: ma = MatrixArgs(M); ma.finalized()
            <MatrixArgs for Full MatrixSpace of 2 by 3 sparse matrices
             over Integer Ring; typ=MATRIX; entries=[0 1 2]
            [3 4 5]>
            sage: ma.matrix()
            [0 1 2]
            [3 4 5]

        ::

            sage: ma = MatrixArgs(M, sparse=False); ma.finalized()
            <MatrixArgs for Full MatrixSpace of 2 by 3 dense matrices
             over Integer Ring; typ=MATRIX; entries=[0 1 2]
                                                    [3 4 5]>
            sage: ma.matrix()
            [0 1 2]
            [3 4 5]

        ::

            sage: ma = MatrixArgs(RDF, M); ma.finalized()
            <MatrixArgs for Full MatrixSpace of 2 by 3 sparse matrices
             over Real Double Field; typ=MATRIX; entries=[0 1 2]
                                                         [3 4 5]>
            sage: ma.matrix(convert=False)
            [0 1 2]
            [3 4 5]
            sage: ma.matrix()
            [0.0 1.0 2.0]
            [3.0 4.0 5.0]

        If we remove our reference to the input ``M``, no copy is made::

            sage: idM = id(M)
            sage: ma = MatrixArgs(M)
            sage: del M
            sage: M = ma.matrix()
            sage: id(M) == idM
            True

        Immutable matrices are never copied::

            sage: M.set_immutable()
            sage: matrix(M) is M
            True"""
    @overload
    def matrix(self) -> Any:
        """MatrixArgs.matrix(self, bool convert=True) -> Matrix

        File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 671)

        Return the entries of the matrix as a Sage Matrix.

        If possible, this returns a direct reference to
        ``self.entries`` without copying.

        INPUT:

        - ``convert`` -- if ``True``, the matrix is guaranteed to have
          the correct parent matrix space. If ``False``, the input matrix
          may be returned even if it lies in the wrong space.

        .. NOTE::

            This changes ``self.entries`` to the returned matrix. This
            means that it is unsafe to access the ``self.entries``
            attribute after calling this method.

        EXAMPLES::

            sage: from sage.matrix.args import MatrixArgs
            sage: M = matrix(2, 3, range(6), sparse=True)

        ::

            sage: ma = MatrixArgs(M); ma.finalized()
            <MatrixArgs for Full MatrixSpace of 2 by 3 sparse matrices
             over Integer Ring; typ=MATRIX; entries=[0 1 2]
            [3 4 5]>
            sage: ma.matrix()
            [0 1 2]
            [3 4 5]

        ::

            sage: ma = MatrixArgs(M, sparse=False); ma.finalized()
            <MatrixArgs for Full MatrixSpace of 2 by 3 dense matrices
             over Integer Ring; typ=MATRIX; entries=[0 1 2]
                                                    [3 4 5]>
            sage: ma.matrix()
            [0 1 2]
            [3 4 5]

        ::

            sage: ma = MatrixArgs(RDF, M); ma.finalized()
            <MatrixArgs for Full MatrixSpace of 2 by 3 sparse matrices
             over Real Double Field; typ=MATRIX; entries=[0 1 2]
                                                         [3 4 5]>
            sage: ma.matrix(convert=False)
            [0 1 2]
            [3 4 5]
            sage: ma.matrix()
            [0.0 1.0 2.0]
            [3.0 4.0 5.0]

        If we remove our reference to the input ``M``, no copy is made::

            sage: idM = id(M)
            sage: ma = MatrixArgs(M)
            sage: del M
            sage: M = ma.matrix()
            sage: id(M) == idM
            True

        Immutable matrices are never copied::

            sage: M.set_immutable()
            sage: matrix(M) is M
            True"""
    @overload
    def matrix(self) -> Any:
        """MatrixArgs.matrix(self, bool convert=True) -> Matrix

        File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 671)

        Return the entries of the matrix as a Sage Matrix.

        If possible, this returns a direct reference to
        ``self.entries`` without copying.

        INPUT:

        - ``convert`` -- if ``True``, the matrix is guaranteed to have
          the correct parent matrix space. If ``False``, the input matrix
          may be returned even if it lies in the wrong space.

        .. NOTE::

            This changes ``self.entries`` to the returned matrix. This
            means that it is unsafe to access the ``self.entries``
            attribute after calling this method.

        EXAMPLES::

            sage: from sage.matrix.args import MatrixArgs
            sage: M = matrix(2, 3, range(6), sparse=True)

        ::

            sage: ma = MatrixArgs(M); ma.finalized()
            <MatrixArgs for Full MatrixSpace of 2 by 3 sparse matrices
             over Integer Ring; typ=MATRIX; entries=[0 1 2]
            [3 4 5]>
            sage: ma.matrix()
            [0 1 2]
            [3 4 5]

        ::

            sage: ma = MatrixArgs(M, sparse=False); ma.finalized()
            <MatrixArgs for Full MatrixSpace of 2 by 3 dense matrices
             over Integer Ring; typ=MATRIX; entries=[0 1 2]
                                                    [3 4 5]>
            sage: ma.matrix()
            [0 1 2]
            [3 4 5]

        ::

            sage: ma = MatrixArgs(RDF, M); ma.finalized()
            <MatrixArgs for Full MatrixSpace of 2 by 3 sparse matrices
             over Real Double Field; typ=MATRIX; entries=[0 1 2]
                                                         [3 4 5]>
            sage: ma.matrix(convert=False)
            [0 1 2]
            [3 4 5]
            sage: ma.matrix()
            [0.0 1.0 2.0]
            [3.0 4.0 5.0]

        If we remove our reference to the input ``M``, no copy is made::

            sage: idM = id(M)
            sage: ma = MatrixArgs(M)
            sage: del M
            sage: M = ma.matrix()
            sage: id(M) == idM
            True

        Immutable matrices are never copied::

            sage: M.set_immutable()
            sage: matrix(M) is M
            True"""
    @overload
    def matrix(self, convert=...) -> Any:
        """MatrixArgs.matrix(self, bool convert=True) -> Matrix

        File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 671)

        Return the entries of the matrix as a Sage Matrix.

        If possible, this returns a direct reference to
        ``self.entries`` without copying.

        INPUT:

        - ``convert`` -- if ``True``, the matrix is guaranteed to have
          the correct parent matrix space. If ``False``, the input matrix
          may be returned even if it lies in the wrong space.

        .. NOTE::

            This changes ``self.entries`` to the returned matrix. This
            means that it is unsafe to access the ``self.entries``
            attribute after calling this method.

        EXAMPLES::

            sage: from sage.matrix.args import MatrixArgs
            sage: M = matrix(2, 3, range(6), sparse=True)

        ::

            sage: ma = MatrixArgs(M); ma.finalized()
            <MatrixArgs for Full MatrixSpace of 2 by 3 sparse matrices
             over Integer Ring; typ=MATRIX; entries=[0 1 2]
            [3 4 5]>
            sage: ma.matrix()
            [0 1 2]
            [3 4 5]

        ::

            sage: ma = MatrixArgs(M, sparse=False); ma.finalized()
            <MatrixArgs for Full MatrixSpace of 2 by 3 dense matrices
             over Integer Ring; typ=MATRIX; entries=[0 1 2]
                                                    [3 4 5]>
            sage: ma.matrix()
            [0 1 2]
            [3 4 5]

        ::

            sage: ma = MatrixArgs(RDF, M); ma.finalized()
            <MatrixArgs for Full MatrixSpace of 2 by 3 sparse matrices
             over Real Double Field; typ=MATRIX; entries=[0 1 2]
                                                         [3 4 5]>
            sage: ma.matrix(convert=False)
            [0 1 2]
            [3 4 5]
            sage: ma.matrix()
            [0.0 1.0 2.0]
            [3.0 4.0 5.0]

        If we remove our reference to the input ``M``, no copy is made::

            sage: idM = id(M)
            sage: ma = MatrixArgs(M)
            sage: del M
            sage: M = ma.matrix()
            sage: id(M) == idM
            True

        Immutable matrices are never copied::

            sage: M.set_immutable()
            sage: matrix(M) is M
            True"""
    @overload
    def matrix(self) -> Any:
        """MatrixArgs.matrix(self, bool convert=True) -> Matrix

        File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 671)

        Return the entries of the matrix as a Sage Matrix.

        If possible, this returns a direct reference to
        ``self.entries`` without copying.

        INPUT:

        - ``convert`` -- if ``True``, the matrix is guaranteed to have
          the correct parent matrix space. If ``False``, the input matrix
          may be returned even if it lies in the wrong space.

        .. NOTE::

            This changes ``self.entries`` to the returned matrix. This
            means that it is unsafe to access the ``self.entries``
            attribute after calling this method.

        EXAMPLES::

            sage: from sage.matrix.args import MatrixArgs
            sage: M = matrix(2, 3, range(6), sparse=True)

        ::

            sage: ma = MatrixArgs(M); ma.finalized()
            <MatrixArgs for Full MatrixSpace of 2 by 3 sparse matrices
             over Integer Ring; typ=MATRIX; entries=[0 1 2]
            [3 4 5]>
            sage: ma.matrix()
            [0 1 2]
            [3 4 5]

        ::

            sage: ma = MatrixArgs(M, sparse=False); ma.finalized()
            <MatrixArgs for Full MatrixSpace of 2 by 3 dense matrices
             over Integer Ring; typ=MATRIX; entries=[0 1 2]
                                                    [3 4 5]>
            sage: ma.matrix()
            [0 1 2]
            [3 4 5]

        ::

            sage: ma = MatrixArgs(RDF, M); ma.finalized()
            <MatrixArgs for Full MatrixSpace of 2 by 3 sparse matrices
             over Real Double Field; typ=MATRIX; entries=[0 1 2]
                                                         [3 4 5]>
            sage: ma.matrix(convert=False)
            [0 1 2]
            [3 4 5]
            sage: ma.matrix()
            [0.0 1.0 2.0]
            [3.0 4.0 5.0]

        If we remove our reference to the input ``M``, no copy is made::

            sage: idM = id(M)
            sage: ma = MatrixArgs(M)
            sage: del M
            sage: M = ma.matrix()
            sage: id(M) == idM
            True

        Immutable matrices are never copied::

            sage: M.set_immutable()
            sage: matrix(M) is M
            True"""
    @overload
    def matrix(self) -> Any:
        """MatrixArgs.matrix(self, bool convert=True) -> Matrix

        File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 671)

        Return the entries of the matrix as a Sage Matrix.

        If possible, this returns a direct reference to
        ``self.entries`` without copying.

        INPUT:

        - ``convert`` -- if ``True``, the matrix is guaranteed to have
          the correct parent matrix space. If ``False``, the input matrix
          may be returned even if it lies in the wrong space.

        .. NOTE::

            This changes ``self.entries`` to the returned matrix. This
            means that it is unsafe to access the ``self.entries``
            attribute after calling this method.

        EXAMPLES::

            sage: from sage.matrix.args import MatrixArgs
            sage: M = matrix(2, 3, range(6), sparse=True)

        ::

            sage: ma = MatrixArgs(M); ma.finalized()
            <MatrixArgs for Full MatrixSpace of 2 by 3 sparse matrices
             over Integer Ring; typ=MATRIX; entries=[0 1 2]
            [3 4 5]>
            sage: ma.matrix()
            [0 1 2]
            [3 4 5]

        ::

            sage: ma = MatrixArgs(M, sparse=False); ma.finalized()
            <MatrixArgs for Full MatrixSpace of 2 by 3 dense matrices
             over Integer Ring; typ=MATRIX; entries=[0 1 2]
                                                    [3 4 5]>
            sage: ma.matrix()
            [0 1 2]
            [3 4 5]

        ::

            sage: ma = MatrixArgs(RDF, M); ma.finalized()
            <MatrixArgs for Full MatrixSpace of 2 by 3 sparse matrices
             over Real Double Field; typ=MATRIX; entries=[0 1 2]
                                                         [3 4 5]>
            sage: ma.matrix(convert=False)
            [0 1 2]
            [3 4 5]
            sage: ma.matrix()
            [0.0 1.0 2.0]
            [3.0 4.0 5.0]

        If we remove our reference to the input ``M``, no copy is made::

            sage: idM = id(M)
            sage: ma = MatrixArgs(M)
            sage: del M
            sage: M = ma.matrix()
            sage: id(M) == idM
            True

        Immutable matrices are never copied::

            sage: M.set_immutable()
            sage: matrix(M) is M
            True"""
    @overload
    def matrix(self, M) -> Any:
        """MatrixArgs.matrix(self, bool convert=True) -> Matrix

        File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 671)

        Return the entries of the matrix as a Sage Matrix.

        If possible, this returns a direct reference to
        ``self.entries`` without copying.

        INPUT:

        - ``convert`` -- if ``True``, the matrix is guaranteed to have
          the correct parent matrix space. If ``False``, the input matrix
          may be returned even if it lies in the wrong space.

        .. NOTE::

            This changes ``self.entries`` to the returned matrix. This
            means that it is unsafe to access the ``self.entries``
            attribute after calling this method.

        EXAMPLES::

            sage: from sage.matrix.args import MatrixArgs
            sage: M = matrix(2, 3, range(6), sparse=True)

        ::

            sage: ma = MatrixArgs(M); ma.finalized()
            <MatrixArgs for Full MatrixSpace of 2 by 3 sparse matrices
             over Integer Ring; typ=MATRIX; entries=[0 1 2]
            [3 4 5]>
            sage: ma.matrix()
            [0 1 2]
            [3 4 5]

        ::

            sage: ma = MatrixArgs(M, sparse=False); ma.finalized()
            <MatrixArgs for Full MatrixSpace of 2 by 3 dense matrices
             over Integer Ring; typ=MATRIX; entries=[0 1 2]
                                                    [3 4 5]>
            sage: ma.matrix()
            [0 1 2]
            [3 4 5]

        ::

            sage: ma = MatrixArgs(RDF, M); ma.finalized()
            <MatrixArgs for Full MatrixSpace of 2 by 3 sparse matrices
             over Real Double Field; typ=MATRIX; entries=[0 1 2]
                                                         [3 4 5]>
            sage: ma.matrix(convert=False)
            [0 1 2]
            [3 4 5]
            sage: ma.matrix()
            [0.0 1.0 2.0]
            [3.0 4.0 5.0]

        If we remove our reference to the input ``M``, no copy is made::

            sage: idM = id(M)
            sage: ma = MatrixArgs(M)
            sage: del M
            sage: M = ma.matrix()
            sage: id(M) == idM
            True

        Immutable matrices are never copied::

            sage: M.set_immutable()
            sage: matrix(M) is M
            True"""
    def set_column_keys(self, *args, **kwargs):
        """MatrixArgs.set_column_keys(self, column_keys) -> int

        File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 918)

        Set the column keys with consistency checking.

        If the value was previously set, it must remain the same.

        EXAMPLES::

            sage: from sage.matrix.args import MatrixArgs
            sage: ma = MatrixArgs(2, 4)
            sage: ma.set_column_keys('xyz')
            Traceback (most recent call last):
            ...
            ValueError: inconsistent column keys: should be of cardinality 4 but got xyz
            sage: ma.set_column_keys('abcd')
            0
            sage: ma.finalized()
            <MatrixArgs for
              Set of Morphisms
               from Free module generated by {'a', 'b', 'c', 'd'} over Integer Ring
                 to Ambient free module of rank 2 over the principal ideal domain
                    Integer Ring
                 in Category of finite dimensional modules with basis over
                    (Dedekind domains and euclidean domains
                     and noetherian rings and infinite enumerated sets
                     and metric spaces);
             typ=ZERO; entries=None>"""
    def set_row_keys(self, *args, **kwargs):
        """MatrixArgs.set_row_keys(self, row_keys) -> int

        File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 955)

        Set the row keys with consistency checking.

        If the value was previously set, it must remain the same.

        EXAMPLES::

            sage: from sage.matrix.args import MatrixArgs
            sage: ma = MatrixArgs(2, 4)
            sage: ma.set_row_keys('xyz')
            Traceback (most recent call last):
            ...
            ValueError: inconsistent row keys: should be of cardinality 2 but got xyz
            sage: ma.set_row_keys(['u', 'v'])
            0
            sage: ma.finalized()
            <MatrixArgs for
              Set of Morphisms
               from Ambient free module of rank 4 over the principal ideal domain
                    Integer Ring
                 to Free module generated by {'u', 'v'} over Integer Ring
                 in Category of finite dimensional modules with basis over
                    (Dedekind domains and euclidean domains
                     and noetherian rings and infinite enumerated sets
                     and metric spaces);
             typ=ZERO; entries=None>"""
    @overload
    def set_space(self, space) -> int:
        """MatrixArgs.set_space(self, space) -> int

        File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 991)

        Set inputs from a given matrix space.

        INPUT:

        - ``space`` -- a :class:`MatrixSpace` or a homset of modules with basis

        EXAMPLES::

            sage: from sage.matrix.args import MatrixArgs
            sage: ma = MatrixArgs()
            sage: S = MatrixSpace(QQ, 3, 2, sparse=True)
            sage: _ = ma.set_space(S)
            sage: ma.finalized()
            <MatrixArgs for Full MatrixSpace of 3 by 2 sparse matrices
             over Rational Field; typ=ZERO; entries=None>
            sage: M = ma.matrix(); M
            [0 0]
            [0 0]
            [0 0]
            sage: M.parent() is S
            True

        From a homset::

            sage: C = CombinatorialFreeModule(ZZ, ['a', 'b', 'c'])
            sage: R = CombinatorialFreeModule(ZZ, ['u', 'v'])
            sage: S = Hom(C, R); S
            Set of Morphisms
             from Free module generated by {'a', 'b', 'c'} over Integer Ring
               to Free module generated by {'u', 'v'} over Integer Ring
               in Category of finite dimensional modules with basis over Integer Ring
            sage: ma = MatrixArgs()
            sage: _ = ma.set_space(S)
            sage: ma.finalized()
            <MatrixArgs for Set of Morphisms
             from Free module generated by {'a', 'b', 'c'} over Integer Ring
               to Free module generated by {'u', 'v'} over Integer Ring
               in Category of finite dimensional modules with basis over Integer Ring;
             typ=ZERO; entries=None>"""
    @overload
    def set_space(self, S) -> Any:
        """MatrixArgs.set_space(self, space) -> int

        File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 991)

        Set inputs from a given matrix space.

        INPUT:

        - ``space`` -- a :class:`MatrixSpace` or a homset of modules with basis

        EXAMPLES::

            sage: from sage.matrix.args import MatrixArgs
            sage: ma = MatrixArgs()
            sage: S = MatrixSpace(QQ, 3, 2, sparse=True)
            sage: _ = ma.set_space(S)
            sage: ma.finalized()
            <MatrixArgs for Full MatrixSpace of 3 by 2 sparse matrices
             over Rational Field; typ=ZERO; entries=None>
            sage: M = ma.matrix(); M
            [0 0]
            [0 0]
            [0 0]
            sage: M.parent() is S
            True

        From a homset::

            sage: C = CombinatorialFreeModule(ZZ, ['a', 'b', 'c'])
            sage: R = CombinatorialFreeModule(ZZ, ['u', 'v'])
            sage: S = Hom(C, R); S
            Set of Morphisms
             from Free module generated by {'a', 'b', 'c'} over Integer Ring
               to Free module generated by {'u', 'v'} over Integer Ring
               in Category of finite dimensional modules with basis over Integer Ring
            sage: ma = MatrixArgs()
            sage: _ = ma.set_space(S)
            sage: ma.finalized()
            <MatrixArgs for Set of Morphisms
             from Free module generated by {'a', 'b', 'c'} over Integer Ring
               to Free module generated by {'u', 'v'} over Integer Ring
               in Category of finite dimensional modules with basis over Integer Ring;
             typ=ZERO; entries=None>"""
    @overload
    def set_space(self, S) -> Any:
        """MatrixArgs.set_space(self, space) -> int

        File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 991)

        Set inputs from a given matrix space.

        INPUT:

        - ``space`` -- a :class:`MatrixSpace` or a homset of modules with basis

        EXAMPLES::

            sage: from sage.matrix.args import MatrixArgs
            sage: ma = MatrixArgs()
            sage: S = MatrixSpace(QQ, 3, 2, sparse=True)
            sage: _ = ma.set_space(S)
            sage: ma.finalized()
            <MatrixArgs for Full MatrixSpace of 3 by 2 sparse matrices
             over Rational Field; typ=ZERO; entries=None>
            sage: M = ma.matrix(); M
            [0 0]
            [0 0]
            [0 0]
            sage: M.parent() is S
            True

        From a homset::

            sage: C = CombinatorialFreeModule(ZZ, ['a', 'b', 'c'])
            sage: R = CombinatorialFreeModule(ZZ, ['u', 'v'])
            sage: S = Hom(C, R); S
            Set of Morphisms
             from Free module generated by {'a', 'b', 'c'} over Integer Ring
               to Free module generated by {'u', 'v'} over Integer Ring
               in Category of finite dimensional modules with basis over Integer Ring
            sage: ma = MatrixArgs()
            sage: _ = ma.set_space(S)
            sage: ma.finalized()
            <MatrixArgs for Set of Morphisms
             from Free module generated by {'a', 'b', 'c'} over Integer Ring
               to Free module generated by {'u', 'v'} over Integer Ring
               in Category of finite dimensional modules with basis over Integer Ring;
             typ=ZERO; entries=None>"""
    def __iter__(self) -> Any:
        """MatrixArgs.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 477)

        Default iteration (dense with conversion).

        EXAMPLES::

            sage: from sage.matrix.args import SparseEntry, MatrixArgs
            sage: ma = MatrixArgs(ZZ, 2, 3, iter(range(6)))
            sage: list(ma)
            [0, 1, 2, 3, 4, 5]"""
    def __len__(self) -> Any:
        """MatrixArgs.__len__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 659)

        EXAMPLES::

            sage: from sage.matrix.args import MatrixArgs
            sage: len(MatrixArgs(3, 14))
            42"""
    def __reduce__(self) -> Any:
        """MatrixArgs.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 458)

        We intentionally do not support pickling because there should
        not be any use case for it.

        TESTS::

            sage: from sage.matrix.args import MatrixArgs
            sage: dumps(MatrixArgs())
            Traceback (most recent call last):
            ...
            RuntimeError: pickling MatrixArgs instances is not allowed
            sage: copy(MatrixArgs())
            Traceback (most recent call last):
            ...
            RuntimeError: pickling MatrixArgs instances is not allowed"""

class SparseEntry:
    '''SparseEntry(i, j, entry)

    File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 59)

    Specialized class for dealing with sparse input in
    :class:`MatrixArgs`. An instance of ``SparseEntry`` represents
    one position in a matrix to be constructed. To construct a sparse
    matrix, one would typically make a list of such.

    Previous versions of Sage used a ``dict`` as data structure for
    sparse input, but that is not so suitable because the keys are not
    guaranteed to be of the correct format. There is also the
    performance cost of creating tuples of Python integers.

    Users of this class are expected to know what they are doing, so
    the indices are not checked when constructing a matrix.

    INPUT:

    - ``i``, ``j`` -- row and column index

    - ``entry`` -- value to be put at position `(i,j)`

    EXAMPLES::

        sage: from sage.matrix.args import SparseEntry
        sage: SparseEntry(123, 456, "abc")
        SparseEntry(123, 456, \'abc\')
        sage: SparseEntry(1/3, 2/3, x)                                                  # needs sage.symbolic
        Traceback (most recent call last):
        ...
        TypeError: unable to convert rational 1/3 to an integer'''
    entry: entry
    i: i
    j: j
    def __init__(self, i, j, entry) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 93)"""
    def __iter__(self) -> Any:
        '''SparseEntry.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/args.pyx (starting at line 98)

        Iteration for convenience, such as converting to a tuple.

        EXAMPLES::

            sage: from sage.matrix.args import SparseEntry
            sage: e = SparseEntry(123, 456, "abc")
            sage: tuple(e)
            (123, 456, \'abc\')'''
