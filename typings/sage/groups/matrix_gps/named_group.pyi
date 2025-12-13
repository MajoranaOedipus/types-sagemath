from sage.groups.matrix_gps.matrix_group import MatrixGroup_generic as MatrixGroup_generic
from sage.structure.unique_representation import CachedRepresentation as CachedRepresentation

def normalize_args_vectorspace(*args, **kwds):
    """
    Normalize the arguments that relate to a vector space.

    INPUT:

    Something that defines an affine space. For example

    * An affine space itself:

      - ``A`` -- affine space

    * A vector space:

      - ``V`` -- a vector space

    * Degree and base ring:

      - ``degree`` -- integer; the degree of the affine group, that
        is, the dimension of the affine space the group is acting on

      - ``ring`` -- a ring or an integer. The base ring of the affine
        space. If an integer is given, it must be a prime power and
        the corresponding finite field is constructed.

      - ``var='a'`` -- (optional) keyword argument to specify the finite
        field generator name in the case where ``ring`` is a prime power

    OUTPUT: a pair ``(degree, ring)``

    TESTS::

        sage: from sage.groups.matrix_gps.named_group import normalize_args_vectorspace
        sage: A = AffineSpace(2, GF(4,'a'));  A                                         # needs sage.rings.finite_rings
        Affine Space of dimension 2 over Finite Field in a of size 2^2
        sage: normalize_args_vectorspace(A)                                             # needs sage.rings.finite_rings
        (2, Finite Field in a of size 2^2)

        sage: normalize_args_vectorspace(2,4)   # shorthand                             # needs sage.rings.finite_rings
        (2, Finite Field in a of size 2^2)

        sage: V = ZZ^3;  V
        Ambient free module of rank 3 over the principal ideal domain Integer Ring
        sage: normalize_args_vectorspace(V)
        (3, Integer Ring)

        sage: normalize_args_vectorspace(2, QQ)
        (2, Rational Field)
    """
def normalize_args_invariant_form(R, d, invariant_form):
    """
    Normalize the input of a user defined invariant bilinear form
    for orthogonal, unitary and symplectic groups.

    Further informations and examples can be found in the defining
    functions (:func:`GU`, :func:`SU`, :func:`Sp`, etc.) for unitary,
    symplectic groups, etc.

    INPUT:

    - ``R`` -- instance of the integral domain which should become
      the ``base_ring`` of the classical group

    - ``d`` -- integer giving the dimension of the module the classical
      group is operating on

    - ``invariant_form`` -- (optional) instances being accepted by
      the matrix-constructor that define a `d \\times d` square matrix
      over R describing the bilinear form to be kept invariant
      by the classical group

    OUTPUT:

    ``None`` if ``invariant_form`` was not specified (or ``None``).
    A matrix if the normalization was possible; otherwise an error
    is raised.

    TESTS::

        sage: from sage.groups.matrix_gps.named_group import normalize_args_invariant_form
        sage: CF3 = CyclotomicField(3)                                                  # needs sage.rings.number_field
        sage: m = normalize_args_invariant_form(CF3, 3, (1,2,3,0,2,0,0,2,1)); m         # needs sage.rings.number_field
        [1 2 3]
        [0 2 0]
        [0 2 1]
        sage: m.base_ring() == CF3                                                      # needs sage.rings.number_field
        True

        sage: normalize_args_invariant_form(ZZ, 3, (1,2,3,0,2,0,0,2))
        Traceback (most recent call last):
        ...
        ValueError: sequence too short (expected length 9, got 8)

        sage: normalize_args_invariant_form(QQ, 3, (1,2,3,0,2,0,0,2,0))
        Traceback (most recent call last):
        ...
        ValueError: invariant_form must be non-degenerate

    AUTHORS:

    - Sebastian Oehms (2018-8) (see :issue:`26028`)
    """

class NamedMatrixGroup_generic(CachedRepresentation, MatrixGroup_generic):
    def __init__(self, degree, base_ring, special, sage_name, latex_string, category=None, invariant_form=None) -> None:
        '''
        Base class for "named" matrix groups.

        INPUT:

        - ``degree`` -- integer; the degree (number of rows/columns of
          matrices)

        - ``base_ring`` -- ring; the base ring of the matrices

        - ``special`` -- boolean; whether the matrix group is special,
          that is, elements have determinant one

        - ``sage_name`` -- string; the name of the group

        - ``latex_string`` -- string; the latex representation

        - ``category`` -- (optional) a subcategory of
          :class:`sage.categories.groups.Groups` passed to
          the constructor of
          :class:`sage.groups.matrix_gps.matrix_group.MatrixGroup_generic`

        - ``invariant_form`` -- (optional) square-matrix of the given
          degree over the given base_ring describing a bilinear form
          to be kept invariant by the group

        EXAMPLES::

            sage: G = GL(2, QQ)
            sage: from sage.groups.matrix_gps.named_group import NamedMatrixGroup_generic
            sage: isinstance(G, NamedMatrixGroup_generic)
            True

        .. SEEALSO::

            See the examples for :func:`GU`, :func:`SU`, :func:`Sp`, etc.
            as well.
        '''
    def __richcmp__(self, other, op):
        """
        Override comparison.

        We need to override the comparison since the named groups
        derive from
        :class:`~sage.structure.unique_representation.UniqueRepresentation`,
        which compare by identity.

        EXAMPLES::

            sage: # needs sage.libs.gap
            sage: G = GL(2,3)
            sage: G == MatrixGroup(G.gens())
            True

            sage: # needs sage.libs.gap sage.rings.finite_rings
            sage: G = groups.matrix.GL(4,2)
            sage: H = MatrixGroup(G.gens())
            sage: G == H
            True
            sage: G != H
            False
        """
