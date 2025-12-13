import sage.modules.free_module_morphism as free_module_morphism
from sage.modules import vector_space_homspace as vector_space_homspace
from sage.structure.element import Matrix as Matrix

def linear_transformation(arg0, arg1=None, arg2=None, side: str = 'left'):
    '''
    Create a linear transformation from a variety of possible inputs.

    FORMATS:

    In the following, ``D`` and ``C`` are vector spaces over
    the same field that are the domain and codomain
    (respectively) of the linear transformation.

    ``side`` is a keyword that is either ``\'left\'`` or ``\'right\'``.
    When a matrix is used to specify a linear transformation,
    as in the first two call formats below, you may specify
    if the function is given by matrix multiplication with
    the vector on the left, or the vector on the right.
    The default is \'left\'. The matrix
    representation may be obtained as either version, no matter
    how it is created.

    - ``linear_transformation(A, side=\'left\')``

      Where ``A`` is a matrix.  The domain and codomain are inferred
      from the dimension of the matrix and the base ring of the matrix.
      The base ring must be a field, or have its fraction field implemented
      in Sage.

    - ``linear_transformation(D, C, A, side=\'left\')``

      ``A`` is a matrix that behaves as above.  However, now the domain
      and codomain are given explicitly. The matrix is checked for
      compatibility with the domain and codomain.  Additionally, the
      domain and codomain may be supplied with alternate ("user") bases
      and the matrix is interpreted as being a representation relative
      to those bases.

    - ``linear_transformation(D, C, f)``

      ``f`` is any function that can be applied to the basis elements of the
      domain and that produces elements of the codomain.  The linear
      transformation returned is the unique linear transformation that
      extends this mapping on the basis elements.  ``f`` may come from a
      function defined by a Python ``def`` statement, or may be defined as a
      ``lambda`` function.

      Alternatively, ``f`` may be specified by a callable symbolic function,
      see the examples below for a demonstration.

    - ``linear_transformation(D, C, images)``

      ``images`` is a list, or tuple, of codomain elements, equal in number
      to the size of the basis of the domain.  Each basis element of the domain
      is mapped to the corresponding element of the ``images`` list, and the
      linear transformation returned is the unique linear transformation that
      extends this mapping.

    OUTPUT:

    A linear transformation described by the input.  This is a
    "vector space morphism", an object of the class
    :class:`sage.modules.vector_space_morphism`.

    EXAMPLES:

    We can define a linear transformation with just a matrix, understood to
    act on a vector placed on one side or the other.  The field for the
    vector spaces used as domain and codomain is obtained from the base
    ring of the matrix, possibly promoting to a fraction field.  ::

        sage: A = matrix(ZZ, [[1, -1, 4], [2, 0, 5]])
        sage: phi = linear_transformation(A)
        sage: phi
        Vector space morphism represented by the matrix:
        [ 1 -1  4]
        [ 2  0  5]
        Domain: Vector space of dimension 2 over Rational Field
        Codomain: Vector space of dimension 3 over Rational Field
        sage: phi([1/2, 5])
        (21/2, -1/2, 27)

        sage: B = matrix(Integers(7), [[1, 2, 1], [3, 5, 6]])
        sage: rho = linear_transformation(B, side=\'right\')
        sage: rho
        Vector space morphism represented by the matrix:
        [1 3]
        [2 5]
        [1 6]
        Domain: Vector space of dimension 3 over Ring of integers modulo 7
        Codomain: Vector space of dimension 2 over Ring of integers modulo 7
        sage: rho([2, 4, 6])
        (2, 6)

    We can define a linear transformation with a matrix, while explicitly
    giving the domain and codomain.  Matrix entries will be coerced into the
    common field of scalars for the vector spaces.  ::

        sage: D = QQ^3
        sage: C = QQ^2
        sage: A = matrix([[1, 7], [2, -1], [0, 5]])
        sage: A.parent()
        Full MatrixSpace of 3 by 2 dense matrices over Integer Ring
        sage: zeta = linear_transformation(D, C, A)
        sage: zeta.matrix().parent()
        Full MatrixSpace of 3 by 2 dense matrices over Rational Field
        sage: zeta
        Vector space morphism represented by the matrix:
        [ 1  7]
        [ 2 -1]
        [ 0  5]
        Domain: Vector space of dimension 3 over Rational Field
        Codomain: Vector space of dimension 2 over Rational Field

    Matrix representations are relative to the bases for the domain
    and codomain.  ::

        sage: u = vector(QQ, [1, -1])
        sage: v = vector(QQ, [2, 3])
        sage: D = (QQ^2).subspace_with_basis([u, v])
        sage: x = vector(QQ, [2, 1])
        sage: y = vector(QQ, [-1, 4])
        sage: C = (QQ^2).subspace_with_basis([x, y])
        sage: A = matrix(QQ, [[2, 5], [3, 7]])
        sage: psi = linear_transformation(D, C, A)
        sage: psi
        Vector space morphism represented by the matrix:
        [2 5]
        [3 7]
        Domain: Vector space of degree 2 and dimension 2 over Rational Field
        User basis matrix:
        [ 1 -1]
        [ 2  3]
        Codomain: Vector space of degree 2 and dimension 2 over Rational Field
        User basis matrix:
        [ 2  1]
        [-1  4]
        sage: psi(u) == 2*x + 5*y
        True
        sage: psi(v) == 3*x + 7*y
        True

    Functions that act on the domain may be used to compute images of
    the domain\'s basis elements, and this mapping can be extended to
    a unique linear transformation.  The function may be a Python
    function (via ``def`` or ``lambda``) or a Sage symbolic function.  ::

        sage: def g(x):
        ....:     return vector(QQ, [2*x[0]+x[2], 5*x[1]])
        sage: phi = linear_transformation(QQ^3, QQ^2, g)
        sage: phi
        Vector space morphism represented by the matrix:
        [2 0]
        [0 5]
        [1 0]
        Domain: Vector space of dimension 3 over Rational Field
        Codomain: Vector space of dimension 2 over Rational Field

        sage: f = lambda x: vector(QQ, [2*x[0]+x[2], 5*x[1]])
        sage: rho = linear_transformation(QQ^3, QQ^2, f)
        sage: rho
        Vector space morphism represented by the matrix:
        [2 0]
        [0 5]
        [1 0]
        Domain: Vector space of dimension 3 over Rational Field
        Codomain: Vector space of dimension 2 over Rational Field

        sage: # needs sage.symbolic
        sage: x, y, z = var(\'x y z\')
        sage: h(x, y, z) = [2*x + z, 5*y]
        sage: zeta = linear_transformation(QQ^3, QQ^2, h)
        sage: zeta
        Vector space morphism represented by the matrix:
        [2 0]
        [0 5]
        [1 0]
        Domain:   Vector space of dimension 3 over Rational Field
        Codomain: Vector space of dimension 2 over Rational Field

        sage: phi == rho
        True
        sage: rho == zeta                                                               # needs sage.symbolic
        True


    We create a linear transformation relative to non-standard bases,
    and capture its representation relative to standard bases.  With this, we
    can build functions that create the same linear transformation relative
    to the nonstandard bases.  ::

        sage: u = vector(QQ, [1, -1])
        sage: v = vector(QQ, [2, 3])
        sage: D = (QQ^2).subspace_with_basis([u, v])
        sage: x = vector(QQ, [2, 1])
        sage: y = vector(QQ, [-1, 4])
        sage: C = (QQ^2).subspace_with_basis([x, y])
        sage: A = matrix(QQ, [[2, 5], [3, 7]])
        sage: psi = linear_transformation(D, C, A)
        sage: rho = psi.restrict_codomain(QQ^2).restrict_domain(QQ^2)
        sage: rho.matrix()
        [ -4/5  97/5]
        [  1/5 -13/5]

        sage: f = lambda x: vector(QQ, [(-4/5)*x[0] + (1/5)*x[1], (97/5)*x[0] + (-13/5)*x[1]])
        sage: psi = linear_transformation(D, C, f)
        sage: psi.matrix()
        [2 5]
        [3 7]

        sage: # needs sage.symbolic
        sage: s, t = var(\'s t\')
        sage: h(s, t) = [(-4/5)*s + (1/5)*t, (97/5)*s + (-13/5)*t]
        sage: zeta = linear_transformation(D, C, h)
        sage: zeta.matrix()
        [2 5]
        [3 7]

    Finally, we can give an explicit list of images for the basis
    elements of the domain.  ::

        sage: # needs sage.rings.number_field
        sage: x = polygen(QQ)
        sage: F.<a> = NumberField(x^3 + x + 1)
        sage: u = vector(F, [1, a, a^2])
        sage: v = vector(F, [a, a^2, 2])
        sage: w = u + v
        sage: D = F^3
        sage: C = F^3
        sage: rho = linear_transformation(D, C, [u, v, w])
        sage: rho.matrix()
        [      1       a     a^2]
        [      a     a^2       2]
        [  a + 1 a^2 + a a^2 + 2]
        sage: C = (F^3).subspace_with_basis([u, v])
        sage: D = (F^3).subspace_with_basis([u, v])
        sage: psi = linear_transformation(C, D, [u+v, u-v])
        sage: psi.matrix()
        [ 1  1]
        [ 1 -1]

    TESTS:

    We test some bad inputs.  First, the wrong things in the wrong places.  ::

        sage: linear_transformation(\'junk\')
        Traceback (most recent call last):
        ...
        TypeError: first argument must be a matrix or a vector space, not junk

        sage: linear_transformation(QQ^2, QQ^3, \'stuff\')
        Traceback (most recent call last):
        ...
        TypeError: third argument must be a matrix, function, or list of images, not stuff

        sage: linear_transformation(QQ^2, \'garbage\')
        Traceback (most recent call last):
        ...
        TypeError: if first argument is a vector space, then second argument must be a vector space, not garbage

        sage: linear_transformation(QQ^2, Integers(7)^2)
        Traceback (most recent call last):
        ...
        TypeError: vector spaces must have the same field of scalars, not Rational Field and Ring of integers modulo 7

    Matrices must be over a field (or a ring that can be promoted to a field),
    and of the right size.  ::

        sage: linear_transformation(matrix(Integers(6), [[2, 3],[4, 5]]))
        Traceback (most recent call last):
        ...
        TypeError: matrix must have entries from a field, or a ring with a fraction field, not Ring of integers modulo 6

        sage: A = matrix(QQ, 3, 4, range(12))
        sage: linear_transformation(QQ^4, QQ^4, A)
        Traceback (most recent call last):
        ...
        TypeError: domain dimension is incompatible with matrix size

        sage: linear_transformation(QQ^3, QQ^3, A, side=\'right\')
        Traceback (most recent call last):
        ...
        TypeError: domain dimension is incompatible with matrix size

        sage: linear_transformation(QQ^3, QQ^3, A)
        Traceback (most recent call last):
        ...
        TypeError: codomain dimension is incompatible with matrix size

        sage: linear_transformation(QQ^4, QQ^4, A, side=\'right\')
        Traceback (most recent call last):
        ...
        TypeError: codomain dimension is incompatible with matrix size

    Lists of images can be of the wrong number, or not really
    elements of the codomain.  ::

        sage: linear_transformation(QQ^3, QQ^2, [vector(QQ, [1,2])])
        Traceback (most recent call last):
        ...
        ValueError: number of images should equal the size of the domain\'s basis (=3), not 1

        sage: C = (QQ^2).subspace_with_basis([vector(QQ, [1,1])])
        sage: linear_transformation(QQ^1, C, [vector(QQ, [1,2])])
        Traceback (most recent call last):
        ...
        ArithmeticError: some proposed image is not in the codomain, because
        element [1, 2] is not in free module


    Functions may not apply properly to domain elements,
    or return values outside the codomain.  ::

        sage: f = lambda x: vector(QQ, [x[0], x[4]])
        sage: linear_transformation(QQ^3, QQ^2, f)
        Traceback (most recent call last):
        ...
        ValueError: function cannot be applied properly to some basis element because
        vector index out of range

        sage: f = lambda x: vector(QQ, [x[0], x[1]])
        sage: C = (QQ^2).span([vector(QQ, [1, 1])])
        sage: linear_transformation(QQ^2, C, f)
        Traceback (most recent call last):
        ...
        ArithmeticError: some image of the function is not in the codomain, because
        element [1, 0] is not in free module

    A Sage symbolic function can come in a variety of forms that are
    not representative of a linear transformation. ::

        sage: x, y = var(\'x, y\')                                                        # needs sage.symbolic
        sage: f(x, y) = [y, x, y]                                                       # needs sage.symbolic
        sage: linear_transformation(QQ^3, QQ^3, f)                                      # needs sage.symbolic
        Traceback (most recent call last):
        ...
        ValueError: symbolic function has the wrong number of inputs for domain

        sage: linear_transformation(QQ^2, QQ^2, f)                                      # needs sage.symbolic
        Traceback (most recent call last):
        ...
        ValueError: symbolic function has the wrong number of outputs for codomain

        sage: x, y = var(\'x y\')                                                         # needs sage.symbolic
        sage: f(x, y) = [y, x*y]                                                        # needs sage.symbolic
        sage: linear_transformation(QQ^2, QQ^2, f)                                      # needs sage.symbolic
        Traceback (most recent call last):
        ...
        ValueError: symbolic function must be linear in all the inputs:
        unable to convert y to a rational

        sage: # needs sage.symbolic
        sage: x, y = var(\'x y\')
        sage: f(x, y) = [x, 2*y]
        sage: C = (QQ^2).span([vector(QQ, [1, 1])])
        sage: linear_transformation(QQ^2, C, f)
        Traceback (most recent call last):
        ...
        ArithmeticError: some image of the function is not in the codomain, because
        element [1, 0] is not in free module
    '''
def is_VectorSpaceMorphism(x) -> bool:
    """
    Return ``True`` if ``x`` is a vector space morphism (a linear transformation).

    This function is deprecated.

    INPUT:

    - ``x`` -- anything

    OUTPUT:

    ``True`` only if ``x`` is an instance of a vector space morphism,
    which are also known as linear transformations.

    EXAMPLES::

        sage: V = QQ^2; f = V.hom([V.1,-2*V.0])
        sage: sage.modules.vector_space_morphism.is_VectorSpaceMorphism(f)
        doctest:warning...
        DeprecationWarning: is_VectorSpaceMorphism is deprecated;
        use isinstance(..., VectorSpaceMorphism) or categories instead
        See https://github.com/sagemath/sage/issues/37731 for details.
        True
        sage: sage.modules.vector_space_morphism.is_VectorSpaceMorphism('junk')
        False
    """

class VectorSpaceMorphism(free_module_morphism.FreeModuleMorphism):
    def __init__(self, homspace, A, side: str = 'left') -> None:
        """
        Create a linear transformation, a morphism between vector spaces.

        INPUT:

        - ``homspace`` -- a homspace (of vector spaces) to serve
          as a parent for the linear transformation and a home for
          the domain and codomain of the morphism
        - ``A`` -- a matrix representing the linear transformation,
          which will act on vectors placed to the left of the matrix

        EXAMPLES:

        Nominally, we require a homspace to hold the domain
        and codomain and a matrix representation of the morphism
        (linear transformation).  ::

            sage: from sage.modules.vector_space_homspace import VectorSpaceHomspace
            sage: from sage.modules.vector_space_morphism import VectorSpaceMorphism
            sage: H = VectorSpaceHomspace(QQ^3, QQ^2)
            sage: A = matrix(QQ, 3, 2, range(6))
            sage: zeta = VectorSpaceMorphism(H, A)
            sage: zeta
            Vector space morphism represented by the matrix:
            [0 1]
            [2 3]
            [4 5]
            Domain:   Vector space of dimension 3 over Rational Field
            Codomain: Vector space of dimension 2 over Rational Field

        See the constructor,
        :func:`sage.modules.vector_space_morphism.linear_transformation`
        for another way to create linear transformations.

        The ``.hom()`` method of a vector space will create a vector
        space morphism. ::

            sage: V = QQ^3; W = V.subspace_with_basis([[1,2,3], [-1,2,5/3], [0,1,-1]])
            sage: phi = V.hom(matrix(QQ, 3, range(9)), codomain=W) # indirect doctest
            sage: type(phi)
            <class 'sage.modules.vector_space_morphism.VectorSpaceMorphism'>

        A matrix may be coerced into a vector space homspace to
        create a vector space morphism.  ::

            sage: from sage.modules.vector_space_homspace import VectorSpaceHomspace
            sage: H = VectorSpaceHomspace(QQ^3, QQ^2)
            sage: A = matrix(QQ, 3, 2, range(6))
            sage: rho = H(A)  # indirect doctest
            sage: type(rho)
            <class 'sage.modules.vector_space_morphism.VectorSpaceMorphism'>
        """
    def is_invertible(self) -> bool:
        """
        Determine if the vector space morphism has an inverse.

        OUTPUT:

        ``True`` if the vector space morphism is invertible, otherwise
        ``False``.

        EXAMPLES:

        If the dimension of the domain does not match the dimension
        of the codomain, then the morphism cannot be invertible.  ::

            sage: V = QQ^3
            sage: U = V.subspace_with_basis([V.0 + V.1, 2*V.1 + 3*V.2])
            sage: phi = V.hom([U.0, U.0 + U.1, U.0 - U.1], U)
            sage: phi.is_invertible()
            False

        An invertible linear transformation. ::

            sage: A = matrix(QQ, 3, [[-3, 5, -5], [4, -7, 7], [6, -8, 10]])
            sage: A.determinant()
            2
            sage: H = Hom(QQ^3, QQ^3)
            sage: rho = H(A)
            sage: rho.is_invertible()
            True

        A non-invertible linear transformation, an endomorphism of
        a vector space over a finite field.  ::

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF(11^2)
            sage: A = matrix(F, [[6*a + 3,   8*a +  2, 10*a + 3],
            ....:                [2*a + 7,   4*a +  3,  2*a + 3],
            ....:                [9*a + 2,  10*a + 10,  3*a + 3]])
            sage: A.nullity()
            1
            sage: E = End(F^3)
            sage: zeta = E(A)
            sage: zeta.is_invertible()
            False
        """
