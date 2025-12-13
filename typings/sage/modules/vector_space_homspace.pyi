import sage.modules.free_module_homspace
from sage.matrix.constructor import matrix as matrix

def is_VectorSpaceHomspace(x):
    """
    Return ``True`` if ``x`` is a vector space homspace.

    INPUT:

    - ``x`` -- anything

    EXAMPLES:

    To be a vector space morphism, the domain and codomain must both be
    vector spaces, in other words, modules over fields.  If either
    set is just a module, then the ``Hom()`` constructor will build a
    space of free module morphisms.  ::

        sage: H = Hom(QQ^3, QQ^2)
        sage: type(H)
        <class 'sage.modules.vector_space_homspace.VectorSpaceHomspace_with_category'>
        sage: sage.modules.vector_space_homspace.is_VectorSpaceHomspace(H)
        doctest:warning...
        DeprecationWarning: the function is_VectorSpaceHomspace is deprecated;
        use 'isinstance(..., VectorSpaceHomspace)' instead
        See https://github.com/sagemath/sage/issues/37924 for details.
        True

        sage: K = Hom(QQ^3, ZZ^2)
        sage: type(K)
        <class 'sage.modules.free_module_homspace.FreeModuleHomspace_with_category'>
        sage: sage.modules.vector_space_homspace.is_VectorSpaceHomspace(K)
        False

        sage: L = Hom(ZZ^3, QQ^2)
        sage: type(L)
        <class 'sage.modules.free_module_homspace.FreeModuleHomspace_with_category'>
        sage: sage.modules.vector_space_homspace.is_VectorSpaceHomspace(L)
        False

        sage: sage.modules.vector_space_homspace.is_VectorSpaceHomspace('junk')
        False
    """

class VectorSpaceHomspace(sage.modules.free_module_homspace.FreeModuleHomspace):
    def __call__(self, A, check: bool = True, **kwds):
        """
        INPUT:

        - ``A`` -- one of several possible inputs representing
          a morphism from this vector space homspace:

          - a vector space morphism in this homspace
          - a matrix representation relative to the bases of the vector spaces,
            which acts on a vector placed to the left of the matrix
          - a list or tuple containing images of the domain's basis vectors
          - a function from the domain to the codomain

        - ``check`` -- boolean (default: ``True``); required for compatibility
          with calls from :meth:`sage.structure.parent.Parent.hom`

        - the keyword ``side`` can be assigned the values ``'left'`` or
          ``'right'``; it corresponds to the side of vectors relative to the
          matrix

        EXAMPLES::

            sage: V = (QQ^3).span_of_basis([[1,1,0],[1,0,2]])
            sage: H = V.Hom(V)
            sage: H
            Set of Morphisms (Linear Transformations) from
            Vector space of degree 3 and dimension 2 over Rational Field
            User basis matrix:
            [1 1 0]
            [1 0 2]
            to
            Vector space of degree 3 and dimension 2 over Rational Field
            User basis matrix:
            [1 1 0]
            [1 0 2]

        Coercing a matrix::

            sage: A = matrix(QQ, [[0, 1], [1, 0]])
            sage: rho = H(A)          # indirect doctest
            sage: rho
            Vector space morphism represented by the matrix:
            [0 1]
            [1 0]
            Domain: Vector space of degree 3 and dimension 2 over Rational Field
            User basis matrix:
            [1 1 0]
            [1 0 2]
            Codomain: Vector space of degree 3 and dimension 2 over Rational Field
            User basis matrix:
            [1 1 0]
            [1 0 2]

        Coercing a list of images::

            sage: phi = H([V.1, V.0])
            sage: phi(V.1) == V.0
            True
            sage: phi(V.0) == V.1
            True
            sage: phi
            Vector space morphism represented by the matrix:
            [0 1]
            [1 0]
            Domain: Vector space of degree 3 and dimension 2 over Rational Field
            User basis matrix:
            [1 1 0]
            [1 0 2]
            Codomain: Vector space of degree 3 and dimension 2 over Rational Field
            User basis matrix:
            [1 1 0]
            [1 0 2]

        Coercing a lambda function::

            sage: f = lambda x: vector(QQ, [x[0], (1/2)*x[2], 2*x[1]])
            sage: zeta = H(f)
            sage: zeta
            Vector space morphism represented by the matrix:
            [0 1]
            [1 0]
            Domain: Vector space of degree 3 and dimension 2 over Rational Field
            User basis matrix:
            [1 1 0]
            [1 0 2]
            Codomain: Vector space of degree 3 and dimension 2 over Rational Field
            User basis matrix:
            [1 1 0]
            [1 0 2]

        Coercing a vector space morphism into the parent of a second vector
        space morphism will unify their parents::

            sage: U = FreeModule(QQ,3, sparse=True ); V = QQ^4
            sage: W = FreeModule(QQ,3, sparse=False); X = QQ^4
            sage: H = Hom(U, V)
            sage: K = Hom(W, X)
            sage: H is K, H == K
            (False, True)

            sage: A = matrix(QQ, 3, 4, [0]*12)
            sage: f = H(A)
            sage: B = matrix(QQ, 3, 4, range(12))
            sage: g = K(B)
            sage: f.parent() is H and g.parent() is K
            True

            sage: h = H(g)
            sage: f.parent() is h.parent()
            True

        See other examples in the module-level documentation.

        TESTS::

            sage: V = GF(3)^0
            sage: W = GF(3)^1
            sage: H = V.Hom(W)
            sage: H.zero().is_zero()
            True

        Previously the above code resulted in a :exc:`TypeError` because the
        dimensions of the matrix were incorrect.
        """
