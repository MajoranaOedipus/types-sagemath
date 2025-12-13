from sage.misc.cachefunc import cached_function as cached_function, cached_method as cached_method
from sage.structure.element import Element as Element, InfinityElement as InfinityElement
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import rich_to_bool as rich_to_bool, richcmp as richcmp
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation
from typing import Any

@cached_function
def list_of_representatives(N):
    """
    Return a list of ideals, coprime to the ideal ``N``, representatives of
    the ideal classes of the corresponding number field.

    .. NOTE::

        This list, used every time we check `\\Gamma_0(N)` - equivalence of
        cusps, is cached.

    INPUT:

    - ``N`` -- an ideal of a number field

    OUTPUT:

    A list of ideals coprime to the ideal ``N``, such that they are
    representatives of all the ideal classes of the number field.

    EXAMPLES::

        sage: from sage.modular.cusps_nf import list_of_representatives
        sage: x = polygen(ZZ, 'x')
        sage: k.<a> = NumberField(x^4 + 13*x^3 - 11)
        sage: N = k.ideal(713, a + 208)
        sage: L = list_of_representatives(N); L
        (Fractional ideal (1),
         Fractional ideal (47, a - 9),
         Fractional ideal (53, a - 16))
    """
@cached_function
def NFCusps(number_field):
    """
    The set of cusps of a number field `K`, i.e. `\\mathbb{P}^1(K)`.

    INPUT:

    - ``number_field`` -- a number field

    OUTPUT: the set of cusps over the given number field

    EXAMPLES::

        sage: x = polygen(ZZ, 'x')
        sage: k.<a> = NumberField(x^2 + 5)
        sage: kCusps = NFCusps(k); kCusps
        Set of all cusps of Number Field in a with defining polynomial x^2 + 5
        sage: kCusps is NFCusps(k)
        True

    Saving and loading works::

        sage: loads(kCusps.dumps()) == kCusps
        True
    """

class NFCuspsSpace(UniqueRepresentation, Parent):
    """
    The set of cusps of a number field. See ``NFCusps`` for full documentation.

    EXAMPLES::

        sage: x = polygen(ZZ, 'x')
        sage: k.<a> = NumberField(x^2 + 5)
        sage: kCusps = NFCusps(k); kCusps
        Set of all cusps of Number Field in a with defining polynomial x^2 + 5
    """
    def __init__(self, number_field) -> None:
        """
        See ``NFCusps`` for full documentation.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: k.<a> = NumberField(x^3 + x^2 + 13)
            sage: kCusps = NFCusps(k); kCusps
            Set of all cusps of Number Field in a with defining polynomial x^3 + x^2 + 13
        """
    def __eq__(self, right):
        """
        Return equality only if right is the set of cusps for the same field.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: k.<a> = NumberField(x^2 + 5)
            sage: L.<a> = NumberField(x^2 + 23)
            sage: kCusps = NFCusps(k); kCusps
            Set of all cusps of Number Field in a with defining polynomial x^2 + 5
            sage: LCusps = NFCusps(L); LCusps
            Set of all cusps of Number Field in a with defining polynomial x^2 + 23
            sage: kCusps == NFCusps(k)
            True
            sage: LCusps == NFCusps(L)
            True
            sage: LCusps == kCusps
            False
        """
    def __ne__(self, right):
        """
        Check that ``self`` is not equal to ``right``.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: k.<a> = NumberField(x^2 + 5)
            sage: L.<a> = NumberField(x^2 + 23)
            sage: kCusps = NFCusps(k); kCusps
            Set of all cusps of Number Field in a with defining polynomial x^2 + 5
            sage: LCusps = NFCusps(L); LCusps
            Set of all cusps of Number Field in a with defining polynomial x^2 + 23
            sage: kCusps != NFCusps(k)
            False
            sage: LCusps != NFCusps(L)
            False
            sage: LCusps != kCusps
            True
        """
    def __call__(self, x):
        """
        Convert x into the set of cusps of a number field.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: k.<a> = NumberField(x^2 + 5)
            sage: kCusps = NFCusps(k)
            sage: c = kCusps(a,2)
            Traceback (most recent call last):
            ...
            TypeError: ...__call__() takes 2 positional arguments but 3 were given

         ::

            sage: c = kCusps((a,2)); c
            Cusp [a: 2] of Number Field in a with defining polynomial x^2 + 5
            sage: kCusps(2/a)
            Cusp [-2*a: 5] of Number Field in a with defining polynomial x^2 + 5
            sage: kCusps(oo)
            Cusp Infinity of Number Field in a with defining polynomial x^2 + 5
        """
    @cached_method
    def zero(self):
        """
        Return the zero cusp.

        .. NOTE::

            This method just exists to make some general algorithms work.
            It is not intended that the returned cusp is an additive
            neutral element.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: k.<a> = NumberField(x^2 + 5)
            sage: kCusps = NFCusps(k)
            sage: kCusps.zero()
            Cusp [0: 1] of Number Field in a with defining polynomial x^2 + 5
        """
    def number_field(self):
        """
        Return the number field that this set of cusps is attached to.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: k.<a> = NumberField(x^2 + 1)
            sage: kCusps = NFCusps(k)
            sage: kCusps.number_field()
            Number Field in a with defining polynomial x^2 + 1
        """

class NFCusp(Element):
    '''
    Create a number field cusp, i.e., an element of `\\mathbb{P}^1(k)`.

    A cusp on a number field is either an element of the field or infinity,
    i.e., an element of the projective line over the number field.  It is
    stored as a pair (a,b), where a, b are integral elements of the number
    field.

    INPUT:

    - ``number_field`` -- the number field over which the cusp is defined

    - ``a`` -- it can be a number field element (integral or not), or
      a number field cusp

    - ``b`` -- (optional) when present, it must be either Infinity or
      coercible to an element of the number field

    - ``lreps`` -- (optional) a list of chosen representatives for all the
      ideal classes of the field. When given, the representative of the cusp
      will be changed so its associated ideal is one of the ideals in the list.

    OUTPUT:

    ``[a: b]`` -- a number field cusp.

    EXAMPLES::

        sage: x = polygen(ZZ, \'x\')
        sage: k.<a> = NumberField(x^2 + 5)
        sage: NFCusp(k, a, 2)
        Cusp [a: 2] of Number Field in a with defining polynomial x^2 + 5
        sage: NFCusp(k, (a,2))
        Cusp [a: 2] of Number Field in a with defining polynomial x^2 + 5
        sage: NFCusp(k, a, 2/(a+1))
        Cusp [a - 5: 2] of Number Field in a with defining polynomial x^2 + 5

    Cusp Infinity:

    ::

        sage: NFCusp(k, 0)
        Cusp [0: 1] of Number Field in a with defining polynomial x^2 + 5
        sage: NFCusp(k, oo)
        Cusp Infinity of Number Field in a with defining polynomial x^2 + 5
        sage: NFCusp(k, 3*a, oo)
        Cusp [0: 1] of Number Field in a with defining polynomial x^2 + 5
        sage: NFCusp(k, a + 5, 0)
        Cusp Infinity of Number Field in a with defining polynomial x^2 + 5

    Saving and loading works:

    ::

        sage: alpha = NFCusp(k, a, 2/(a+1))
        sage: loads(dumps(alpha))==alpha
        True

    Some tests:

    ::

        sage: I*I
        -1
        sage: NFCusp(k, I)
        Traceback (most recent call last):
        ...
        TypeError: unable to convert I to a cusp of the number field

    ::

        sage: NFCusp(k, oo, oo)
        Traceback (most recent call last):
        ...
        TypeError: unable to convert (+Infinity, +Infinity) to a cusp of the number field

    ::

        sage: NFCusp(k, 0, 0)
        Traceback (most recent call last):
        ...
        TypeError: unable to convert (0, 0) to a cusp of the number field

    ::

        sage: NFCusp(k, "a + 2", a)
        Cusp [-2*a + 5: 5] of Number Field in a with defining polynomial x^2 + 5

    ::

        sage: NFCusp(k, NFCusp(k, oo))
        Cusp Infinity of Number Field in a with defining polynomial x^2 + 5
        sage: c = NFCusp(k, 3, 2*a)
        sage: NFCusp(k, c, a + 1)
        Cusp [-a - 5: 20] of Number Field in a with defining polynomial x^2 + 5
        sage: L.<b> = NumberField(x^2 + 2)
        sage: NFCusp(L, c)
        Traceback (most recent call last):
        ...
        ValueError: Cannot coerce cusps from one field to another
    '''
    def __init__(self, number_field, a, b=None, parent=None, lreps=None) -> None:
        """
        Constructor of number field cusps. See ``NFCusp`` for full
        documentation.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: k.<a> = NumberField(x^2 + 1)
            sage: c = NFCusp(k, 3, a+1); c
            Cusp [3: a + 1] of Number Field in a with defining polynomial x^2 + 1
            sage: c.parent()
            Set of all cusps of Number Field in a with defining polynomial x^2 + 1
            sage: kCusps = NFCusps(k)
            sage: c.parent() is kCusps
            True
        """
    def number_field(self):
        """
        Return the number field of definition of the cusp ``self``.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: k.<a> = NumberField(x^2 + 2)
            sage: alpha = NFCusp(k, 1, a + 1)
            sage: alpha.number_field()
            Number Field in a with defining polynomial x^2 + 2
        """
    def is_infinity(self) -> bool:
        """
        Return ``True`` if this is the cusp infinity.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: k.<a> = NumberField(x^2 + 1)
            sage: NFCusp(k, a, 2).is_infinity()
            False
            sage: NFCusp(k, 2, 0).is_infinity()
            True
            sage: NFCusp(k, oo).is_infinity()
            True
        """
    def numerator(self):
        """
        Return the numerator of the cusp ``self``.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: k.<a> = NumberField(x^2 + 1)
            sage: c = NFCusp(k, a, 2)
            sage: c.numerator()
            a
            sage: d = NFCusp(k, 1, a)
            sage: d.numerator()
            1
            sage: NFCusp(k, oo).numerator()
            1
        """
    def denominator(self):
        """
        Return the denominator of the cusp ``self``.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: k.<a> = NumberField(x^2 + 1)
            sage: c = NFCusp(k, a, 2)
            sage: c.denominator()
            2
            sage: d = NFCusp(k, 1, a + 1);d
            Cusp [1: a + 1] of Number Field in a with defining polynomial x^2 + 1
            sage: d.denominator()
            a + 1
            sage: NFCusp(k, oo).denominator()
            0
        """
    def __neg__(self):
        """
        The negative of this cusp.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: k.<a> = NumberField(x^2 + 23)
            sage: c = NFCusp(k, a, a+1); c
            Cusp [a: a + 1] of Number Field in a with defining polynomial x^2 + 23
            sage: -c
            Cusp [-a: a + 1] of Number Field in a with defining polynomial x^2 + 23
        """
    def apply(self, g):
        """
        Return g(``self``), where ``g`` is a 2x2 matrix, which we view as a
        linear fractional transformation.

        INPUT:

        - ``g`` -- list of integral elements [a, b, c, d] that are the
          entries of a 2x2 matrix

        OUTPUT:

        A number field cusp, obtained by the action of ``g`` on the cusp
        ``self``.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: k.<a> = NumberField(x^2 + 23)
            sage: beta = NFCusp(k, 0, 1)
            sage: beta.apply([0, -1, 1, 0])
            Cusp Infinity of Number Field in a with defining polynomial x^2 + 23
            sage: beta.apply([1, a, 0, 1])
            Cusp [a: 1] of Number Field in a with defining polynomial x^2 + 23
        """
    def ideal(self):
        """
        Return the ideal associated to the cusp ``self``.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: k.<a> = NumberField(x^2 + 23)
            sage: alpha = NFCusp(k, 3, a-1)
            sage: alpha.ideal()
            Fractional ideal (3, 1/2*a - 1/2)
            sage: NFCusp(k, oo).ideal()
            Fractional ideal (1)
        """
    def ABmatrix(self) -> list:
        """
        Return AB-matrix associated to the cusp ``self``.

        Given R a Dedekind domain and A, B ideals of R in inverse classes, an
        AB-matrix is a matrix realizing the isomorphism between R+R and A+B.
        An AB-matrix associated to a cusp [a1: a2] is an AB-matrix with A the
        ideal associated to the cusp (A=<a1, a2>) and first column given by
        the coefficients of the cusp.

        EXAMPLES:

        ::

            sage: x = polygen(ZZ, 'x')
            sage: k.<a> = NumberField(x^3 + 11)
            sage: alpha = NFCusp(k, oo)
            sage: alpha.ABmatrix()
            [1, 0, 0, 1]

        ::

            sage: alpha = NFCusp(k, 0)
            sage: alpha.ABmatrix()
            [0, -1, 1, 0]

        Note that the AB-matrix associated to a cusp is not unique, and the
        output of the ``ABmatrix`` function may change.

        ::

            sage: alpha = NFCusp(k, 3/2, a-1)
            sage: M = alpha.ABmatrix()
            sage: M # random
            [-a^2 - a - 1, -3*a - 7, 8, -2*a^2 - 3*a + 4]
            sage: M[0] == alpha.numerator() and M[2] == alpha.denominator()
            True

        An AB-matrix associated to a cusp alpha will send Infinity to alpha:

        ::

            sage: alpha = NFCusp(k, 3, a-1)
            sage: M = alpha.ABmatrix()
            sage: (k.ideal(M[1], M[3])*alpha.ideal()).is_principal()
            True
            sage: M[0] == alpha.numerator() and M[2] == alpha.denominator()
            True
            sage: NFCusp(k, oo).apply(M) == alpha
            True
        """
    def is_Gamma0_equivalent(self, other, N, Transformation: bool = False) -> bool | tuple[bool, Any]:
        """
        Check if cusps ``self`` and ``other`` are `\\Gamma_0(N)`- equivalent.

        INPUT:

        - ``other`` -- a number field cusp or a list of two number field
          elements which define a cusp

        - ``N`` -- an ideal of the number field (level)

        OUTPUT: boolean; ``True`` if the cusps are equivalent

        - a transformation matrix -- (if ``Transformation=True``) a list of
          integral elements [a, b, c, d] which are the entries of a 2x2 matrix
          M in `\\Gamma_0(N)` such that M * ``self`` = ``other`` if ``other``
          and ``self`` are `\\Gamma_0(N)`- equivalent. If ``self`` and ``other``
          are not equivalent it returns zero.

        EXAMPLES:

        ::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 - 10)
            sage: N = K.ideal(a - 1)
            sage: alpha = NFCusp(K, 0)
            sage: beta = NFCusp(K, oo)
            sage: alpha.is_Gamma0_equivalent(beta, N)
            False
            sage: alpha.is_Gamma0_equivalent(beta, K.ideal(1))
            True
            sage: b, M = alpha.is_Gamma0_equivalent(beta, K.ideal(1),Transformation=True)
            sage: alpha.apply(M)
            Cusp Infinity of Number Field in a with defining polynomial x^3 - 10

        ::

            sage: k.<a> = NumberField(x^2 + 23)
            sage: N = k.ideal(3)
            sage: alpha1 = NFCusp(k, a+1, 4)
            sage: alpha2 = NFCusp(k, a-8, 29)
            sage: alpha1.is_Gamma0_equivalent(alpha2, N)
            True
            sage: b, M = alpha1.is_Gamma0_equivalent(alpha2, N, Transformation=True)
            sage: alpha1.apply(M) == alpha2
            True
            sage: M[2] in N
            True
        """

def Gamma0_NFCusps(N):
    """
    Return a list of inequivalent cusps for `\\Gamma_0(N)`, i.e., a set of
    representatives for the orbits of ``self`` on `\\mathbb{P}^1(k)`.

    INPUT:

    - ``N`` -- an integral ideal of the number field k (the level)

    OUTPUT: list of inequivalent number field cusps

    EXAMPLES::

        sage: x = polygen(ZZ, 'x')
        sage: k.<a> = NumberField(x^2 + 5)
        sage: N = k.ideal(3)
        sage: L = Gamma0_NFCusps(N)

    The cusps in the list are inequivalent::

        sage: any(L[i].is_Gamma0_equivalent(L[j], N)
        ....:     for i in range(len(L)) for j in range(len(L)) if i < j)
        False

    We test that we obtain the right number of orbits::

        sage: from sage.modular.cusps_nf import number_of_Gamma0_NFCusps
        sage: len(L) == number_of_Gamma0_NFCusps(N)
        True

    Another example::

        sage: x = polygen(ZZ, 'x')
        sage: k.<a> = NumberField(x^4 - x^3 -21*x^2 + 17*x + 133)
        sage: N = k.ideal(5)
        sage: from sage.modular.cusps_nf import number_of_Gamma0_NFCusps
        sage: len(Gamma0_NFCusps(N)) == number_of_Gamma0_NFCusps(N) # long time (over 1 sec)
        True
    """
def number_of_Gamma0_NFCusps(N):
    """
    Return the total number of orbits of cusps under the action of the
    congruence subgroup `\\Gamma_0(N)`.

    INPUT:

    - ``N`` -- a number field ideal

    OUTPUT: integer; the number of orbits of cusps under Gamma0(N)-action

    EXAMPLES::

        sage: x = polygen(ZZ, 'x')
        sage: k.<a> = NumberField(x^3 + 11)
        sage: N = k.ideal(2, a+1)
        sage: from sage.modular.cusps_nf import number_of_Gamma0_NFCusps
        sage: number_of_Gamma0_NFCusps(N)
        4
        sage: L = Gamma0_NFCusps(N)
        sage: len(L) == number_of_Gamma0_NFCusps(N)
        True
        sage: k.<a> = NumberField(x^2 + 7)
        sage: N = k.ideal(9)
        sage: number_of_Gamma0_NFCusps(N)
        6
        sage: N = k.ideal(a*9 + 7)
        sage: number_of_Gamma0_NFCusps(N)
        24
    """
def NFCusps_ideal_reps_for_levelN(N, nlists: int = 1):
    """
    Return a list of lists (``nlists`` different lists) of prime ideals,
    coprime to ``N``, representing every ideal class of the number field.

    INPUT:

    - ``N`` -- number field ideal

    - ``nlists`` -- (default: 1) the number of lists of prime ideals
      we want

    OUTPUT:

    A list of lists of ideals representatives of the ideal classes, all coprime
    to ``N``, representing every ideal.

    EXAMPLES::

        sage: x = polygen(ZZ, 'x')
        sage: k.<a> = NumberField(x^3 + 11)
        sage: N = k.ideal(5, a + 1)
        sage: from sage.modular.cusps_nf import NFCusps_ideal_reps_for_levelN
        sage: NFCusps_ideal_reps_for_levelN(N)
        [(Fractional ideal (1), Fractional ideal (2, a + 1))]
        sage: L = NFCusps_ideal_reps_for_levelN(N, 3)
        sage: all(len(L[i]) == k.class_number() for i in range(len(L)))
        True

    ::

        sage: k.<a> = NumberField(x^4 - x^3 - 21*x^2 + 17*x + 133)
        sage: N = k.ideal(6)
        sage: from sage.modular.cusps_nf import NFCusps_ideal_reps_for_levelN
        sage: NFCusps_ideal_reps_for_levelN(N)
        [(Fractional ideal (1),
          Fractional ideal (67, -4/7*a^3 + 13/7*a^2 + 39/7*a - 43),
          Fractional ideal (127, -4/7*a^3 + 13/7*a^2 + 39/7*a - 42),
          Fractional ideal (157, -4/7*a^3 + 13/7*a^2 + 39/7*a + 48))]
        sage: L = NFCusps_ideal_reps_for_levelN(N, 5)
        sage: all(len(L[i]) == k.class_number() for i in range(len(L)))
        True
    """
def units_mod_ideal(I):
    """
    Return integral elements of the number field representing the images of
    the global units modulo the ideal ``I``.

    INPUT:

    - ``I`` -- number field ideal

    OUTPUT:

    A list of integral elements of the number field representing the images of
    the global units modulo the ideal ``I``. Elements of the list might be
    equivalent to each other mod ``I``.

    EXAMPLES::

        sage: from sage.modular.cusps_nf import units_mod_ideal
        sage: x = polygen(ZZ, 'x')
        sage: k.<a> = NumberField(x^2 + 1)
        sage: I = k.ideal(a + 1)
        sage: units_mod_ideal(I)
        [1]
        sage: I = k.ideal(3)
        sage: units_mod_ideal(I)
        [1, a, -1, -a]

    ::

        sage: from sage.modular.cusps_nf import units_mod_ideal
        sage: k.<a> = NumberField(x^3 + 11)
        sage: k.unit_group()
        Unit group with structure C2 x Z of
         Number Field in a with defining polynomial x^3 + 11
        sage: I = k.ideal(5, a + 1)
        sage: units_mod_ideal(I)
        [1,
        2*a^2 + 4*a - 1,
        ...]

    ::

        sage: from sage.modular.cusps_nf import units_mod_ideal
        sage: k.<a> = NumberField(x^4 - x^3 -21*x^2 + 17*x + 133)
        sage: k.unit_group()
        Unit group with structure C6 x Z of
         Number Field in a with defining polynomial x^4 - x^3 - 21*x^2 + 17*x + 133
        sage: I = k.ideal(3)
        sage: U = units_mod_ideal(I)
        sage: all(U[j].is_unit() and (U[j] not in I) for j in range(len(U)))
        True
    """
