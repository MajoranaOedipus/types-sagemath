from .finite_field_givaro import FiniteField_givaro as FiniteField_givaro
from .finite_field_ntl_gf2e import FiniteField_ntl_gf2e as FiniteField_ntl_gf2e
from typing import Literal
from sage.rings.finite_rings.finite_field_base import is_FiniteField as is_FiniteField
from sage.rings.integer import Integer as Integer
from sage.rings.polynomial.polynomial_element import Polynomial as Polynomial
from sage.structure.category_object import normalize_names as normalize_names
from sage.structure.factory import UniqueFactory as UniqueFactory

class FiniteFieldFactory(UniqueFactory):
    '''
    Return the globally unique finite field of given order with
    generator labeled by the given name and possibly with given
    modulus.

    INPUT:

    - ``order`` -- a prime power

    - ``name`` -- string, optional.  Note that there can be a
      substantial speed penalty (in creating extension fields) when
      omitting the variable name, since doing so triggers the
      computation of pseudo-Conway polynomials in order to define a
      coherent lattice of extensions of the prime field.  The speed
      penalty grows with the size of extension degree and with
      the number of factors of the extension degree.

    - ``modulus`` -- (optional) either a defining polynomial for the
      field, or a string specifying an algorithm to use to generate
      such a polynomial.  If ``modulus`` is a string, it is passed to
      :meth:`~sage.rings.polynomial.irreducible_element()` as the
      parameter ``algorithm``; see there for the permissible values of
      this parameter. In particular, you can specify
      ``modulus="primitive"`` to get a primitive polynomial.  You
      may not specify a modulus if you do not specify a variable name.

    - ``impl`` -- (optional) a string specifying the implementation of
      the finite field. Possible values are:

      - ``\'modn\'`` -- ring of integers modulo `p` (only for prime fields)

      - ``\'givaro\'`` -- Givaro, which uses Zech logs (only for fields
        of at most 65521 elements)

      - ``\'ntl\'`` -- NTL using GF2X (only in characteristic 2)

      - ``\'pari\'`` or ``\'pari_ffelt\'`` -- PARI\'s ``FFELT`` type (only
        for extension fields)

    - ``elem_cache`` -- (default: order < 500) cache all elements to
      avoid creation time; ignored unless ``impl=\'givaro\'``

    - ``repr`` -- (default: ``\'poly\'``) ignored unless ``impl=\'givaro\'``;
      controls the way elements are printed to the user:

      - \'log\': repr is
        :meth:`~sage.rings.finite_rings.element_givaro.FiniteField_givaroElement.log_repr()`

      - \'int\': repr is
        :meth:`~sage.rings.finite_rings.element_givaro.FiniteField_givaroElement.int_repr()`

      - \'poly\': repr is
        :meth:`~sage.rings.finite_rings.element_givaro.FiniteField_givaroElement.poly_repr()`

    - ``check_irreducible`` -- verify that the polynomial modulus is
      irreducible

    - ``proof`` -- boolean (default: ``True``); if ``True``, use provable
      primality test; otherwise only use pseudoprimality test

    ALIAS: You can also use ``GF`` instead of ``FiniteField`` -- they
    are identical.

    EXAMPLES::

        sage: k.<a> = FiniteField(9); k
        Finite Field in a of size 3^2
        sage: parent(a)
        Finite Field in a of size 3^2
        sage: charpoly(a, \'y\')
        y^2 + 2*y + 2

    We illustrate the proof flag.  The following example would hang
    for a very long time if we didn\'t use ``proof=False``.

    .. NOTE::

        Magma only supports ``proof=False`` for making finite fields,
        so falsely appears to be faster than Sage -- see :issue:`10975`.

    ::

        sage: k = FiniteField(10^1000 + 453, proof=False)
        sage: k = FiniteField((10^1000 + 453)^2, \'a\', proof=False)      # long time -- about 5 seconds

    ::

        sage: F.<x> = GF(5)[]
        sage: K.<a> = GF(5**5, name=\'a\', modulus=x^5 - x +1 )
        sage: f = K.modulus(); f
        x^5 + 4*x + 1
        sage: type(f)
         <class \'sage.rings.polynomial.polynomial_zmod_flint.Polynomial_zmod_flint\'>

    By default, the given generator is not guaranteed to be primitive
    (a generator of the multiplicative group), use
    ``modulus="primitive"`` if you need this::

        sage: K.<a> = GF(5^45)
        sage: a.multiplicative_order()
        7105427357601001858711242675781
        sage: a.is_square()
        True
        sage: K.<b> = GF(5^45, modulus=\'primitive\')
        sage: b.multiplicative_order()
        28421709430404007434844970703124

    The modulus must be irreducible::

        sage: K.<a> = GF(5**5, name=\'a\', modulus=x^5 - x)
        Traceback (most recent call last):
        ...
        ValueError: finite field modulus must be irreducible but it is not

    You can\'t accidentally fool the constructor into thinking the
    modulus is irreducible when it is not, since it actually tests
    irreducibility modulo `p`.  Also, the modulus has to be of the
    right degree (this is always checked)::

        sage: F.<x> = QQ[]
        sage: factor(x^5 + 2)
        x^5 + 2
        sage: K.<a> = GF(5^5, modulus=x^5 + 2)
        Traceback (most recent call last):
        ...
        ValueError: finite field modulus must be irreducible but it is not
        sage: K.<a> = GF(5^5, modulus=x^3 + 3*x + 3, check_irreducible=False)
        Traceback (most recent call last):
        ...
        ValueError: the degree of the modulus does not equal the degree of the field

    Any type which can be converted to the polynomial ring `GF(p)[x]`
    is accepted as modulus::

        sage: K.<a> = GF(13^3, modulus=[1,0,0,2])
        sage: K.<a> = GF(13^10, modulus=pari("ffinit(13,10)"))
        sage: var(\'x\')
        x
        sage: K.<a> = GF(13^2, modulus=x^2 - 2)
        sage: K.<a> = GF(13^2, modulus=sin(x))
        Traceback (most recent call last):
        ...
        TypeError: self must be a numeric expression

    If you wish to live dangerously, you can tell the constructor not
    to test irreducibility using ``check_irreducible=False``, but this
    can easily lead to crashes and hangs -- so do not do it unless you
    know that the modulus really is irreducible!

    ::

        sage: K.<a> = GF(5**2, name=\'a\', modulus=x^2 + 2, check_irreducible=False)

    Even for prime fields, you can specify a modulus. This will not
    change how Sage computes in this field, but it will change the
    result of the :meth:`modulus` and :meth:`gen` methods::

        sage: k.<a> = GF(5, modulus=\'primitive\')
        sage: k.modulus()
        x + 3
        sage: a
        2

    The order of a finite field must be a prime power::

        sage: GF(1)
        Traceback (most recent call last):
        ...
        ValueError: the order of a finite field must be at least 2
        sage: GF(100)
        Traceback (most recent call last):
        ...
        ValueError: the order of a finite field must be a prime power

    Finite fields with explicit random modulus are not cached::

        sage: k.<a> = GF(5**10, modulus=\'random\')
        sage: n.<a> = GF(5**10, modulus=\'random\')
        sage: while k.modulus() == n.modulus():
        ....:     n.<a> = GF(5**10, modulus=\'random\')
        sage: n is k
        False
        sage: GF(5**10, \'a\') is GF(5**10, \'a\')
        True

    We check that various ways of creating the same finite field yield
    the same object, which is cached::

        sage: K = GF(7, \'a\')
        sage: L = GF(7, \'b\')
        sage: K is L           # name is ignored for prime fields
        True
        sage: K is GF(7, modulus=K.modulus())
        True
        sage: K = GF(4,\'a\'); K.modulus()
        x^2 + x + 1
        sage: L = GF(4,\'a\', K.modulus())
        sage: K is L
        True
        sage: M = GF(4,\'a\', K.modulus().change_variable_name(\'y\'))
        sage: K is M
        True

    You may print finite field elements as integers. This currently
    only works if the order of field is `<2^{16}`, though::

        sage: k.<a> = GF(2^8, repr=\'int\')
        sage: a
        2

    The following demonstrate coercions for finite fields using Conway
    polynomials::

        sage: k = GF(5^2); a = k.gen()
        sage: l = GF(5^5); b = l.gen()
        sage: a + b
        3*z10^5 + z10^4 + z10^2 + 3*z10 + 1

    Note that embeddings are compatible in lattices of such finite
    fields::

        sage: m = GF(5^3); c = m.gen()
        sage: (a+b)+c == a+(b+c)
        True
        sage: (a*b)*c == a*(b*c)
        True
        sage: from sage.categories.pushout import pushout
        sage: n = pushout(k, l)
        sage: o = pushout(l, m)
        sage: q = pushout(n, o)
        sage: q(o(b)) == q(n(b))
        True

    Another check that embeddings are defined properly::

        sage: k = GF(3**10)
        sage: l = GF(3**20)
        sage: l(k.gen()**10) == l(k.gen())**10
        True

    Using pseudo-Conway polynomials is slow for highly
    composite extension degrees::

        sage: k = GF(3^120)  # long time (about 3 seconds)
        sage: GF(3^40).gen().minimal_polynomial()(k.gen()^((3^120-1)/(3^40-1)))  # long time (because of previous line)
        0

    Before :issue:`17569`, the boolean keyword argument ``conway``
    was required when creating finite fields without a variable
    name.  This keyword argument is now removed (:issue:`21433`).
    You can still pass in ``prefix`` as an argument, which has the
    effect of changing the variable name of the algebraic closure::

        sage: K = GF(3^10, prefix=\'w\'); L = GF(3^10); K is L
        False
        sage: K.variable_name(), L.variable_name()
        (\'w10\', \'z10\')
        sage: list(K.polynomial()) == list(L.polynomial())
        True

    TESTS:

    Check that :issue:`16934` has been fixed::

        sage: k1.<a> = GF(17^14, impl=\'pari\')
        sage: _ = a/2
        sage: k2.<a> = GF(17^14, impl=\'pari\')
        sage: k1 is k2
        True

    Check that :issue:`21433` has been fixed::

        sage: K = GF(5^2)
        sage: L = GF(5^4)
        sage: from sage.categories.pushout import pushout
        sage: pushout(K,L) is L
        True

    Check that :issue:`25182` has been fixed::

        sage: GF(next_prime(2^63)^6)
        Finite Field in z6 of size 9223372036854775837^6

    Check that :issue:`31547` has been fixed::

        sage: q=2**152
        sage: GF(q,\'a\',modulus=\'primitive\') == GF(q,\'a\',modulus=\'primitive\')
        True
    '''
    def __init__(self, *args, **kwds) -> None:
        """
        Initialization.

        EXAMPLES::

            sage: TestSuite(GF).run()
        """
    def create_key_and_extra_args(self, order, name=None, modulus=None, names=None, impl=None, proof=None, check_prime: bool = True, check_irreducible: bool = True, prefix=None, repr=None, elem_cache=None, **kwds):
        """
        EXAMPLES::

            sage: GF.create_key_and_extra_args(9, 'a')                                  # needs sage.libs.linbox
            ((9, ('a',), x^2 + 2*x + 2, 'givaro', 3, 2, True, None, 'poly', True, True, True), {})

        The order `q` can also be given as a pair `(p,n)`::

            sage: GF.create_key_and_extra_args((3, 2), 'a')                             # needs sage.libs.linbox
            ((9, ('a',), x^2 + 2*x + 2, 'givaro', 3, 2, True, None, 'poly', True, True, True), {})

        We do not take invalid keyword arguments and raise a value error
        to better ensure uniqueness::

            sage: GF.create_key_and_extra_args(9, 'a', foo='value')
            Traceback (most recent call last):
            ...
            TypeError: ...create_key_and_extra_args() got an unexpected keyword argument 'foo'

        Moreover, ``repr`` and ``elem_cache`` are ignored when not
        using givaro::

            sage: GF.create_key_and_extra_args(16, 'a', impl='ntl', repr='poly')        # needs sage.libs.ntl
            ((16, ('a',), x^4 + x + 1, 'ntl', 2, 4, True, None, None, None, True, True), {})
            sage: GF.create_key_and_extra_args(16, 'a', impl='ntl', elem_cache=False)   # needs sage.libs.ntl
            ((16, ('a',), x^4 + x + 1, 'ntl', 2, 4, True, None, None, None, True, True), {})
            sage: GF(16, impl='ntl') is GF(16, impl='ntl', repr='foo')                  # needs sage.libs.ntl
            True

        We handle extra arguments for the givaro finite field and
        create unique objects for their defaults::

            sage: GF(25, impl='givaro') is GF(25, impl='givaro', repr='poly')           # needs sage.libs.linbox
            True
            sage: GF(25, impl='givaro') is GF(25, impl='givaro', elem_cache=True)       # needs sage.libs.linbox
            True
            sage: GF(625, impl='givaro') is GF(625, impl='givaro', elem_cache=False)    # needs sage.libs.linbox
            True

        We explicitly take ``structure``, ``implementation`` and ``prec`` attributes
        for compatibility with :class:`~sage.categories.pushout.AlgebraicExtensionFunctor`
        but we ignore them as they are not used, see :issue:`21433`::

            sage: GF.create_key_and_extra_args(9, 'a', structure=None)                  # needs sage.libs.linbox
            ((9, ('a',), x^2 + 2*x + 2, 'givaro', 3, 2, True, None, 'poly', True, True, True), {})

        TESTS::

            sage: GF((6, 1), 'a')       # implicit doctest
            Traceback (most recent call last):
            ...
            ValueError: the order of a finite field must be a prime power

            sage: GF((9, 1), 'a')       # implicit doctest
            Traceback (most recent call last):
            ...
            ValueError: the order of a finite field must be a prime power

            sage: GF((5, 0), 'a')       # implicit doctest
            Traceback (most recent call last):
            ...
            ValueError: the order of a finite field must be a prime power

            sage: GF((3, 2, 1), 'a')    # implicit doctest
            Traceback (most recent call last):
            ...
            ValueError: wrong input for finite field constructor
        """
    def create_object(self, version, key, **kwds):
        """
        EXAMPLES::

            sage: K = GF(19) # indirect doctest
            sage: TestSuite(K).run()

        We try to create finite fields with various implementations::

            sage: k = GF(2, impl='modn')
            sage: k = GF(2, impl='givaro')                                              # needs sage.libs.linbox
            sage: k = GF(2, impl='ntl')                                                 # needs sage.libs.ntl
            sage: k = GF(2, impl='pari')
            Traceback (most recent call last):
            ...
            ValueError: the degree must be at least 2
            sage: k = GF(2, impl='supercalifragilisticexpialidocious')
            Traceback (most recent call last):
            ...
            ValueError: no such finite field implementation: 'supercalifragilisticexpialidocious'
            sage: k.<a> = GF(2^15, impl='modn')
            Traceback (most recent call last):
            ...
            ValueError: the 'modn' implementation requires a prime order
            sage: k.<a> = GF(2^15, impl='givaro')                                       # needs sage.libs.linbox
            sage: k.<a> = GF(2^15, impl='ntl')                                          # needs sage.libs.ntl
            sage: k.<a> = GF(2^15, impl='pari')
            sage: k.<a> = GF(3^60, impl='modn')
            Traceback (most recent call last):
            ...
            ValueError: the 'modn' implementation requires a prime order
            sage: k.<a> = GF(3^60, impl='givaro')                                       # needs sage.libs.linbox
            Traceback (most recent call last):
            ...
            ValueError: q must be < 2^16
            sage: k.<a> = GF(3^60, impl='ntl')                                          # needs sage.libs.ntl
            Traceback (most recent call last):
            ...
            ValueError: q must be a 2-power
            sage: k.<a> = GF(3^60, impl='pari')
        """

GF: FiniteFieldFactory

FiniteField: FiniteFieldFactory

def is_PrimeFiniteField(x):
    """
    Return ``True`` if ``x`` is a prime finite field.

    This function is deprecated.

    EXAMPLES::

        sage: from sage.rings.finite_rings.finite_field_constructor import is_PrimeFiniteField
        sage: is_PrimeFiniteField(QQ)
        doctest:...: DeprecationWarning: the function is_PrimeFiniteField is deprecated; use isinstance(x, sage.rings.finite_rings.finite_field_base.FiniteField) and x.is_prime_field() instead
        See https://github.com/sagemath/sage/issues/32664 for details.
        False
        sage: is_PrimeFiniteField(GF(7))
        True
        sage: is_PrimeFiniteField(GF(7^2, 'a'))
        False
        sage: is_PrimeFiniteField(GF(next_prime(10^90, proof=False)))
        True
    """

zech_log_bound: Literal[65536] 
