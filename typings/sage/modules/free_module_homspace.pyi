import sage.categories.homset
from sage.matrix.constructor import identity_matrix as identity_matrix, matrix as matrix
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.misc.cachefunc import cached_method as cached_method
from sage.structure.element import Matrix as Matrix

def is_FreeModuleHomspace(x):
    """
    Return ``True`` if ``x`` is a free module homspace.

    Notice that every vector space is a free module, but when we construct
    a set of morphisms between two vector spaces, it is a
    ``VectorSpaceHomspace``, which qualifies as a ``FreeModuleHomspace``,
    since the former is special case of the latter.

    EXAMPLES::

        sage: H = Hom(ZZ^3, ZZ^2)
        sage: type(H)
        <class 'sage.modules.free_module_homspace.FreeModuleHomspace_with_category'>
        sage: sage.modules.free_module_homspace.is_FreeModuleHomspace(H)
        doctest:warning...
        DeprecationWarning: the function is_FreeModuleHomspace is deprecated;
        use 'isinstance(..., FreeModuleHomspace)' instead
        See https://github.com/sagemath/sage/issues/37924 for details.
        True

        sage: K = Hom(QQ^3, ZZ^2)
        sage: type(K)
        <class 'sage.modules.free_module_homspace.FreeModuleHomspace_with_category'>
        sage: sage.modules.free_module_homspace.is_FreeModuleHomspace(K)
        True

        sage: L = Hom(ZZ^3, QQ^2)
        sage: type(L)
        <class 'sage.modules.free_module_homspace.FreeModuleHomspace_with_category'>
        sage: sage.modules.free_module_homspace.is_FreeModuleHomspace(L)
        True

        sage: P = Hom(QQ^3, QQ^2)
        sage: type(P)
        <class 'sage.modules.vector_space_homspace.VectorSpaceHomspace_with_category'>
        sage: sage.modules.free_module_homspace.is_FreeModuleHomspace(P)
        True

        sage: sage.modules.free_module_homspace.is_FreeModuleHomspace('junk')
        False
    """

class FreeModuleHomspace(sage.categories.homset.HomsetWithBase):
    def __call__(self, A, **kwds):
        """
        INPUT:

        - ``A`` -- either a matrix or a list/tuple of images of generators,
          or a function returning elements of the codomain for elements of the domain
        - ``check`` -- boolean (default: ``True``)
        - the keyword ``side`` can be assigned the values ``'left'`` or
          ``'right'``. It corresponds to the side of vectors relative to the matrix.

        If A is a matrix, then it is the matrix of this linear
        transformation, with respect to the basis for the domain and
        codomain.  Thus the identity matrix always defines the
        identity morphism.

        EXAMPLES::

            sage: V = (ZZ^3).span_of_basis([[1,1,0],[1,0,2]])
            sage: H = V.Hom(V); H
            Set of Morphisms from ...
            sage: H([V.0,V.1])                    # indirect doctest
            Free module morphism defined by the matrix
            [1 0]
            [0 1]...
            sage: phi = H([V.1,V.0]); phi
            Free module morphism defined by the matrix
            [0 1]
            [1 0]...
            sage: phi(V.1) == V.0
            True
            sage: phi(V.0) == V.1
            True

        The following tests against a bug that was fixed in
        :issue:`9944`. The method ``zero()`` calls this hom space with
        a function, not with a matrix, and that case had previously
        not been taken care of::

            sage: V = span([[1/2,1,1],[3/2,2,1],[0,0,1]],ZZ)
            sage: V.Hom(V).zero()   # indirect doctest
            Free module morphism defined by the matrix
            [0 0 0]
            [0 0 0]
            [0 0 0]
            Domain:   Free module of degree 3 and rank 3 over Integer Ring
                      Echelon ...
            Codomain: Free module of degree 3 and rank 3 over Integer Ring
                      Echelon ...

        The following tests the bug fixed in :issue:`31818`. If there is no
        coercion between base rings, one can only define the zero morphism,
        as morphism of additive groups. Before one could for example use an
        integer matrix to define a morphism from the rational numbers to the
        integers. ::

            sage: V = QQ^2; W = ZZ^2; m = identity_matrix(2)
            sage: H = V.Hom(W); H(m)
            Traceback (most recent call last):
            ...
            TypeError: nontrivial morphisms require a coercion map from the base ring of the domain to the base ring of the codomain
            sage: n = zero_matrix(2);
            sage: h = H(n); h
            Free module morphism defined by the matrix
            [0 0]
            [0 0]
            Domain:   Vector space of dimension 2 over Rational Field
            Codomain: Ambient free module of rank 2 over the principal ideal domain Integer Ring
            sage: [h(v) for v in V.gens()]
            [(0, 0), (0, 0)]
        """
    @cached_method
    def zero(self, side: str = 'left'):
        '''
        INPUT:

        - ``side`` -- side of the vectors acted on by the matrix
          (default: ``\'left\'``)

        EXAMPLES::

            sage: E = ZZ^2
            sage: F = ZZ^3
            sage: H = Hom(E, F)
            sage: f = H.zero()
            sage: f
            Free module morphism defined by the matrix
            [0 0 0]
            [0 0 0]
            Domain:   Ambient free module of rank 2 over the principal ideal domain Integer Ring
            Codomain: Ambient free module of rank 3 over the principal ideal domain Integer Ring
            sage: f(E.an_element())
            (0, 0, 0)
            sage: f(E.an_element()) == F.zero()
            True
            sage: H.zero("right")
            Free module morphism defined as left-multiplication by the matrix
            [0 0]
            [0 0]
            [0 0]
            Domain:   Ambient free module of rank 2 over the principal ideal domain Integer Ring
            Codomain: Ambient free module of rank 3 over the principal ideal domain Integer Ring


        TESTS:

        We check that ``H.zero()`` is picklable::

            sage: loads(dumps(f.parent().zero()))
            Free module morphism defined by the matrix
            [0 0 0]
            [0 0 0]
            Domain:   Ambient free module of rank 2 over the principal ideal domain Integer Ring
            Codomain: Ambient free module of rank 3 over the principal ideal domain Integer Ring
        '''
    @cached_method
    def basis(self, side: str = 'left'):
        '''
        Return a basis for this space of free module homomorphisms.

        INPUT:

        - ``side`` -- side of the vectors acted on by the matrix
          (default: ``\'left\'``)

        OUTPUT: tuple

        EXAMPLES::

            sage: H = Hom(ZZ^2, ZZ^1)
            sage: H.basis()
            (Free module morphism defined by the matrix
              [1]
              [0]
              Domain:   Ambient free module of rank 2 over the principal ideal domain ...
              Codomain: Ambient free module of rank 1 over the principal ideal domain ...,
             Free module morphism defined by the matrix
              [0]
              [1]
              Domain:   Ambient free module of rank 2 over the principal ideal domain ...
              Codomain: Ambient free module of rank 1 over the principal ideal domain ...)
            sage: H.basis("right")
            (Free module morphism defined as left-multiplication by the matrix
              [1 0]
              Domain:   Ambient free module of rank 2 over the principal ideal domain ...
              Codomain: Ambient free module of rank 1 over the principal ideal domain ...,
             Free module morphism defined as left-multiplication by the matrix
              [0 1]
              Domain:   Ambient free module of rank 2 over the principal ideal domain ...
              Codomain: Ambient free module of rank 1 over the principal ideal domain ...)
        '''
    def identity(self, side: str = 'left'):
        """
        Return identity morphism in an endomorphism ring.

        INPUT:

        - ``side`` -- side of the vectors acted on by the matrix
          (default: ``'left'``)

        EXAMPLES::

            sage: V = FreeModule(ZZ,5)
            sage: H = V.Hom(V)
            sage: H.identity()
            Free module morphism defined by the matrix
            [1 0 0 0 0]
            [0 1 0 0 0]
            [0 0 1 0 0]
            [0 0 0 1 0]
            [0 0 0 0 1]
            Domain:   Ambient free module of rank 5 over the principal ideal domain ...
            Codomain: Ambient free module of rank 5 over the principal ideal domain ...
        """
