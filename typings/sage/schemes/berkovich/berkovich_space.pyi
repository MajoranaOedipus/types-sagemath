from sage.categories.number_fields import NumberFields as NumberFields
from sage.categories.topological_spaces import TopologicalSpaces as TopologicalSpaces
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.schemes.affine.affine_space import AffineSpace_generic as AffineSpace_generic
from sage.schemes.berkovich.berkovich_cp_element import Berkovich_Element_Cp_Affine as Berkovich_Element_Cp_Affine, Berkovich_Element_Cp_Projective as Berkovich_Element_Cp_Projective
from sage.schemes.projective.projective_space import ProjectiveSpace as ProjectiveSpace, ProjectiveSpace_ring as ProjectiveSpace_ring
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

def is_Berkovich(space) -> bool:
    """
    Check if ``space`` is a Berkovich space.

    OUTPUT:

    - ``True`` if ``space`` is a Berkovich space.
    - ``False`` otherwise.

    EXAMPLES::

        sage: B = Berkovich_Cp_Projective(3)
        sage: from sage.schemes.berkovich.berkovich_space import is_Berkovich
        sage: is_Berkovich(B)
        doctest:warning...
        DeprecationWarning: The function is_Berkovich is deprecated; use 'isinstance(..., Berkovich)' instead.
        See https://github.com/sagemath/sage/issues/38022 for details.
        True
    """
def is_Berkovich_Cp(space) -> bool:
    """
    Check if ``space`` is a Berkovich space over ``Cp``.

    OUTPUT:

    - ``True`` if ``space`` is a Berkovich space over ``Cp``.
    - ``False`` otherwise.

    EXAMPLES::

        sage: B = Berkovich_Cp_Projective(3)
        sage: from sage.schemes.berkovich.berkovich_space import is_Berkovich_Cp
        sage: is_Berkovich_Cp(B)
        doctest:warning...
        DeprecationWarning: The function is_Berkovich_Cp is deprecated; use 'isinstance(..., Berkovich_Cp)' instead.
        See https://github.com/sagemath/sage/issues/38022 for details.
        True
    """

class Berkovich(UniqueRepresentation, Parent):
    """
    The parent class for any Berkovich space
    """

class Berkovich_Cp(Berkovich):
    """
    Abstract parent class for Berkovich space over ``Cp``.
    """
    def residue_characteristic(self):
        """
        The residue characteristic of the ``base``.

        EXAMPLES::

            sage: B = Berkovich_Cp_Projective(3)
            sage: B.prime()
            3

        ::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: A.<a> = NumberField(x^3 + 20)
            sage: ideal = A.ideal(-1/2*a^2 + a - 3)
            sage: B = Berkovich_Cp_Affine(A, ideal)
            sage: B.residue_characteristic()
            7
        """
    prime = residue_characteristic
    def is_padic_base(self):
        """
        Return ``True`` if this Berkovich space is backed by a `p`-adic field.

        OUTPUT:

        - ``True`` if this Berkovich space was created with a `p`-adic field.
        - ``False`` otherwise.

        EXAMPLES::

            sage: B = Berkovich_Cp_Affine(Qp(3))
            sage: B.is_padic_base()
            True

        ::

            sage: B = Berkovich_Cp_Affine(QQ, 3)
            sage: B.is_padic_base()
            False
        """
    def is_number_field_base(self):
        """
        Return ``True`` if this Berkovich space is backed by a number field.

        OUTPUT:

        - ``True`` if this Berkovich space was created with a number field.
        - ``False`` otherwise.

        EXAMPLES::

            sage: B = Berkovich_Cp_Affine(Qp(3))
            sage: B.is_number_field_base()
            False

        ::

            sage: B = Berkovich_Cp_Affine(QQ, 3)
            sage: B.is_number_field_base()
            True
        """
    def ideal(self):
        """
        The ideal which defines an embedding of the ``base_ring`` into `\\CC_p`.

        If this Berkovich space is backed by a `p`-adic field, then an embedding is
        already specified, and this returns ``None``.

        OUTPUT:

        - An ideal of a ``base_ring`` if ``base_ring`` is a number field.

        - A prime of `\\QQ` if ``base_ring`` is `\\QQ`.

        - ``None`` if ``base_ring`` is a `p`-adic field.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<z> = QQ[]
            sage: A.<a> = NumberField(z^2 + 1)
            sage: ideal = A.prime_above(5)
            sage: B = Berkovich_Cp_Projective(A, ideal)
            sage: B.ideal()
            Fractional ideal (2*a - 1)

        ::

            sage: B = Berkovich_Cp_Projective(QQ, 3)
            sage: B.ideal()
            3

        ::

            sage: B = Berkovich_Cp_Projective(Qp(3))
            sage: B.ideal() is None
            True
        """
    def __eq__(self, right):
        """
        Equality operator.

        EXAMPLES::

            sage: B = Berkovich_Cp_Affine(3)
            sage: A.<x> = Qq(27)
            sage: C = Berkovich_Cp_Affine(A)
            sage: B == C
            True

        ::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: A.<a> = NumberField(x^2 + 1)
            sage: A_ideal = A.prime_above(2)
            sage: B.<b> = NumberField(x^4 + 1)
            sage: B_ideal = B.prime_above(2)
            sage: C = Berkovich_Cp_Projective(A, A_ideal)
            sage: D = Berkovich_Cp_Projective(B, B_ideal)
            sage: C == D
            False

        ::

            sage: C = Berkovich_Cp_Affine(A, A_ideal)                                   # needs sage.rings.number_field
            sage: D = Berkovich_Cp_Affine(B, B_ideal)                                   # needs sage.rings.number_field
            sage: C == D                                                                # needs sage.rings.number_field
            False

        ::

            sage: A_ideal_2 = A.prime_above(5)                                          # needs sage.rings.number_field
            sage: E = Berkovich_Cp_Affine(A, A_ideal_2)                                 # needs sage.rings.number_field
            sage: C == E                                                                # needs sage.rings.number_field
            False
        """
    def __ne__(self, right):
        """
        Inequality operator.

        EXAMPLES::

            sage: B = Berkovich_Cp_Affine(5)
            sage: A.<x> = Qq(25)
            sage: C = Berkovich_Cp_Affine(A)
            sage: B != C
            False
        """
    def __hash__(self):
        """
        Hash function.

        EXAMPLES::

            sage: hash(Berkovich_Cp_Projective(3))
            3

        ::

            sage: # needs sage.rings.number_field
            sage: R.<z> = QQ[]
            sage: A.<a> = NumberField(z^2 + 1)
            sage: B = Berkovich_Cp_Projective(A, A.primes_above(5)[0])
            sage: C = Berkovich_Cp_Projective(A, A.primes_above(5)[1])
            sage: hash(B) != hash(C)
            True
        """

class Berkovich_Cp_Affine(Berkovich_Cp):
    """
    The Berkovich affine line over `\\CC_p`.

    The Berkovich affine line is the set of seminorms on `\\CC_p[x]`,
    with the weakest topology such that the map `| \\cdot | \\to |f|` is continuous
    for all `f \\in \\CC_p[x]`.

    We can represent the Berkovich affine line in two separate ways:
    either using a `p`-adic field to represent elements or using
    a number field to represent elements while storing an ideal
    of the ring of integers of the number field, which specifies
    an embedding of the number field into `\\CC_p`. See the examples.

    INPUT:

    - ``base`` -- three cases:

      * a prime number `p`. Centers of elements are then represented
        as points of `\\QQ_p`.

      * `\\QQ_p` or a finite extension of `\\QQ_p`. Centers of elements
        are then represented as points of ``base``.

      * A number field `K`. Centers of elements are then represented
        as points of `K`.

    - ``ideal`` -- (optional) a prime ideal of ``base``. Must be
      specified if a number field is passed to ``base``, otherwise
      it is ignored.

    EXAMPLES::

        sage: B = Berkovich_Cp_Affine(3); B
        Affine Berkovich line over Cp(3) of precision 20

    We can create elements::

        sage: B(-2)
        Type I point centered at 1 + 2*3 + 2*3^2 + 2*3^3 + 2*3^4 + 2*3^5
        + 2*3^6 + 2*3^7 + 2*3^8 + 2*3^9 + 2*3^10 + 2*3^11 + 2*3^12 + 2*3^13
        + 2*3^14 + 2*3^15 + 2*3^16 + 2*3^17 + 2*3^18 + 2*3^19 + O(3^20)

    ::

        sage: B(1, 2)
        Type III point centered at 1 + O(3^20) of radius 2.00000000000000

    For details on element creation, see the documentation
    of :class:`Berkovich_Element_Cp_Affine`. Initializing by
    passing in `\\QQ_p` looks the same::

        sage: B = Berkovich_Cp_Affine(Qp(3)); B
        Affine Berkovich line over Cp(3) of precision 20

    However, this method allows for more control over behind-the-scenes conversion::

        sage: B = Berkovich_Cp_Affine(Qp(3, 1)); B
        Affine Berkovich line over Cp(3) of precision 1

        sage: B(1/2)
        Type I point centered at 2 + O(3)

    Note that this point has very low precision, as ``B`` was initialized
    with a `p`-adic field of capped-relative precision one. For high precision,
    pass in a high precision `p`-adic field::

        sage: B = Berkovich_Cp_Affine(Qp(3, 1000)); B
        Affine Berkovich line over Cp(3) of precision 1000

    Points of Berkovich space can be created from points of
    extensions of `\\QQ_p`::

        sage: B = Berkovich_Cp_Affine(3)
        sage: A.<a> = Qp(3).extension(x^3 - 3)
        sage: B(a)
        Type I point centered at a + O(a^61)

    For exact computation, a number field can be used::

        sage: R.<x> = QQ[]
        sage: A.<a> = NumberField(x^3 + 20)                                             # needs sage.rings.number_field
        sage: ideal = A.prime_above(3)                                                  # needs sage.rings.number_field
        sage: B = Berkovich_Cp_Affine(A, ideal); B                                      # needs sage.rings.number_field
        Affine Berkovich line over Cp(3), with base
         Number Field in a with defining polynomial x^3 + 20

    Number fields have a major advantage of exact computation.

    Number fields also have added functionality. Arbitrary extensions of
    `\\QQ` are supported, while there is currently limited functionality
    for extensions of `\\QQ_p`. As seen above, constructing a Berkovich
    space backed by a number field requires specifying an ideal of the
    ring of integers of the number field. Specifying the ideal uniquely
    specifies an embedding of the number field into `\\CC_p`.

    Unlike in the case where Berkovich space is backed by a `p`-adic
    field, any point of a Berkovich space backed by a number field
    must be centered at a point of that number field::

        sage: # needs sage.rings.number_field
        sage: R.<x> = QQ[]
        sage: A.<a> = NumberField(x^3 + 20)
        sage: ideal = A.prime_above(3)
        sage: B = Berkovich_Cp_Affine(A, ideal)
        sage: C.<c> = NumberField(x^2 + 1)
        sage: B(c)
        Traceback (most recent call last):
        ...
        ValueError: could not convert c to Number Field in a
        with defining polynomial x^3 + 20

    TESTS::

        sage: A.<x> = AffineSpace(Qp(3), 1)
        sage: Berkovich_Cp_Affine(A)
        Affine Berkovich line over Cp(3) of precision 20

    ::

        sage: B = Berkovich_Cp_Projective(3)
        sage: TestSuite(B).run()
    """
    Element = Berkovich_Element_Cp_Affine
    def __init__(self, base, ideal=None) -> None:
        """
        The Python constructor.

        EXAMPLES::

            sage: Berkovich_Cp_Affine(3)
            Affine Berkovich line over Cp(3) of precision 20
        """

class Berkovich_Cp_Projective(Berkovich_Cp):
    """
    The Berkovich projective line over `\\CC_p`.

    The Berkovich projective line is the one-point compactification
    of the Berkovich affine line.

    We can represent the Berkovich projective line in two separate ways:
    either using a `p`-adic field to represent elements or using
    a number field to represent elements while storing an ideal
    of the ring of integers of the number field, which specifies
    an embedding of the number field into `\\CC_p`. See the examples.

    INPUT:

    - ``base`` -- three cases:

      * a prime number `p`. Centers of elements are then represented
        as points of projective space of dimension 1 over `\\QQ_p`.

      * `\\QQ_p` or a finite extension of `\\QQ_p`. Centers of elements
        are then represented as points of projective space of dimension 1
        over ``base``.

      * A number field `K`. Centers of elements are then represented
        as points of projective space of dimension 1 over ``base``.

    - ``ideal`` -- (optional) a prime ideal of ``base``. Must be
      specified if a number field is passed to ``base``, otherwise
      it is ignored.

    EXAMPLES::

        sage: B = Berkovich_Cp_Projective(3); B
        Projective Berkovich line over Cp(3) of precision 20

    Elements can be constructed::

        sage: B(1/2)
        Type I point centered at (2 + 3 + 3^2 + 3^3 + 3^4 + 3^5
        + 3^6 + 3^7 + 3^8 + 3^9 + 3^10 + 3^11 + 3^12 + 3^13 + 3^14
        + 3^15 + 3^16 + 3^17 + 3^18 + 3^19 + O(3^20) : 1 + O(3^20))

    ::

        sage: B(2, 1)
        Type II point centered at (2 + O(3^20) : 1 + O(3^20)) of radius 3^0

    For details about element construction, see the documentation of
    :class:`Berkovich_Element_Cp_Projective`. Initializing a Berkovich projective
    line by passing in a `p`-adic space looks the same::

        sage: B = Berkovich_Cp_Projective(Qp(3)); B
        Projective Berkovich line over Cp(3) of precision 20

    However, this method allows for more control over
    behind-the-scenes conversion::

        sage: S = Qp(3, 1)
        sage: B = Berkovich_Cp_Projective(S); B
        Projective Berkovich line over Cp(3) of precision 1

        sage: Q1 = B(1/2); Q1
        Type I point centered at (2 + O(3) : 1 + O(3))

    Note that this point has very low precision, as S has low
    precision cap. Berkovich space can also be created over
    a number field, as long as an ideal is specified::

        sage: R.<x> = QQ[]
        sage: A.<a> = NumberField(x^2 + 1)                                              # needs sage.rings.number_field
        sage: ideal = A.prime_above(2)                                                  # needs sage.rings.number_field
        sage: B = Berkovich_Cp_Projective(A, ideal); B                                  # needs sage.rings.number_field
        Projective Berkovich line over Cp(2), with base
         Number Field in a with defining polynomial x^2 + 1

    Number fields have the benefit that computation is exact,
    but lack support for all of `\\CC_p`.

    Number fields also have the advantage of added functionality,
    as arbitrary extensions of `\\QQ` can be constructed while
    there is currently limited functionality for extensions of `\\QQ_p`.
    As seen above, constructing a Berkovich space backed by a number
    field requires specifying an ideal of the ring of integers
    of the number field. Specifying the ideal uniquely specifies
    an embedding of the number field into `\\CC_p`.

    Unlike in the case where Berkovich space is backed by a `p`-adic
    field, any point of a Berkovich space backed by a number field
    must be centered at a point of that number field::

        sage: # needs sage.rings.number_field
        sage: R.<x> = QQ[]
        sage: A.<a> = NumberField(x^3 + 20)
        sage: ideal = A.prime_above(3)
        sage: B = Berkovich_Cp_Projective(A, ideal)
        sage: C.<c> = NumberField(x^2 + 1)
        sage: B(c)
        Traceback (most recent call last):
        ...
        TypeError: could not convert c to Projective Space
        of dimension 1 over Number Field in a with defining polynomial x^3 + 20

    TESTS::

        sage: B = Berkovich_Cp_Projective(3)
        sage: TestSuite(B).run()
    """
    Element = Berkovich_Element_Cp_Projective
    def __init__(self, base, ideal=None) -> None:
        """
        The Python constructor.

        EXAMPLES::

            sage: Berkovich_Cp_Projective(3)
            Projective Berkovich line over Cp(3) of precision 20
        """
    def base_ring(self):
        """
        The base ring of this Berkovich Space.

        OUTPUT: a field

        EXAMPLES::

            sage: B = Berkovich_Cp_Projective(3)
            sage: B.base_ring()
            3-adic Field with capped relative precision 20

        ::

            sage: C = Berkovich_Cp_Projective(ProjectiveSpace(Qp(3, 1), 1))
            sage: C.base_ring()
            3-adic Field with capped relative precision 1

        ::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: A.<a> = NumberField(x^3 + 20)
            sage: ideal = A.prime_above(3)
            sage: D = Berkovich_Cp_Projective(A, ideal)
            sage: D.base_ring()
            Number Field in a with defining polynomial x^3 + 20
        """
