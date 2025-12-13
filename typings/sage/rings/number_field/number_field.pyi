import sage.rings.abc
from . import maps as maps, number_field_base as number_field_base, number_field_element as number_field_element, number_field_element_quadratic as number_field_element_quadratic, number_field_morphisms as number_field_morphisms, structure as structure
from .number_field_ideal import NumberFieldFractionalIdeal as NumberFieldFractionalIdeal, NumberFieldIdeal as NumberFieldIdeal
from _typeshed import Incomplete
from collections.abc import Generator
from sage.arith.misc import euler_phi as euler_phi, factor as factor, gcd as gcd, next_prime as next_prime
from sage.categories.homset import Hom as Hom
from sage.categories.number_fields import NumberFields as NumberFields
from sage.categories.sets_cat import Sets as Sets
from sage.interfaces.abc import GapElement as GapElement
from sage.libs.pari import pari as pari
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.fast_methods import WithEqualityById as WithEqualityById
from sage.misc.functional import is_odd as is_odd, lift as lift
from sage.misc.latex import latex as latex, latex_variable_name as latex_variable_name
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.misc.sage_eval import sage_eval as sage_eval
from sage.misc.superseded import deprecation as deprecation
from sage.modules.free_module import VectorSpace as VectorSpace
from sage.modules.free_module_element import vector as vector
from sage.rings.cif import CIF as CIF
from sage.rings.finite_rings.integer_mod import mod as mod
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as IntegerModRing
from sage.rings.infinity import Infinity as Infinity
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.number_field.morphism import RelativeNumberFieldHomomorphism_from_abs as RelativeNumberFieldHomomorphism_from_abs
from sage.rings.polynomial.polynomial_element import Polynomial as Polynomial
from sage.rings.rational import Rational as Rational
from sage.rings.rational_field import QQ as QQ
from sage.rings.real_double import RDF as RDF
from sage.rings.real_lazy import CLF as CLF, RLF as RLF
from sage.rings.real_mpfr import RR as RR
from sage.structure.category_object import normalize_names as normalize_names
from sage.structure.element import Element as Element
from sage.structure.factorization import Factorization as Factorization
from sage.structure.factory import UniqueFactory as UniqueFactory
from sage.structure.parent import Parent as Parent
from sage.structure.proof.proof import get_flag as get_flag
from sage.structure.sequence import Sequence as Sequence

def is_NumberFieldHomsetCodomain(codomain, category=None):
    """
    Return whether ``codomain`` is a valid codomain for a
    :class:`NumberFieldHomset` in ``category``.

    EXAMPLES:

    This currently accepts any ring (CC, RR, ...)::

        sage: from sage.rings.number_field.number_field import is_NumberFieldHomsetCodomain
        sage: is_NumberFieldHomsetCodomain(QQ)
        True
        sage: x = polygen(ZZ, 'x')
        sage: is_NumberFieldHomsetCodomain(NumberField(x^2 + 1, 'x'))
        True
        sage: is_NumberFieldHomsetCodomain(ZZ)
        True
        sage: is_NumberFieldHomsetCodomain(3)
        False
        sage: is_NumberFieldHomsetCodomain(MatrixSpace(QQ, 2))
        True
        sage: is_NumberFieldHomsetCodomain(InfinityRing)
        True

    Gap objects are not (yet) in :class:`Fields`, and therefore not accepted as
    number field homset codomains::

        sage: is_NumberFieldHomsetCodomain(gap.Rationals)                               # needs sage.libs.gap
        False
    """
def proof_flag(t):
    '''
    Used for easily determining the correct proof flag to use.

    Return ``t`` if ``t`` is not ``None``, otherwise return the system-wide
    proof-flag for number fields (default: ``True``).

    EXAMPLES::

        sage: from sage.rings.number_field.number_field import proof_flag
        sage: proof_flag(True)
        True
        sage: proof_flag(False)
        False
        sage: proof_flag(None)
        True
        sage: proof_flag("banana")
        \'banana\'
    '''
def NumberField(polynomial, name=None, check: bool = True, names=None, embedding=None, latex_name=None, assume_disc_small: bool = False, maximize_at_primes=None, structure=None, *, latex_names=None, **kwds):
    """
    Return *the* number field (or tower of number fields) defined by the
    irreducible ``polynomial``.

    INPUT:

    - ``polynomial`` -- a polynomial over `\\QQ` or a number field, or a list
      of such polynomials
    - ``names`` (or ``name``) -- string or list of strings, the names of
      the generators
    - ``check`` -- boolean (default: ``True``); do type checking and
      irreducibility checking
    - ``embedding`` -- ``None``, an element, or a list of elements, the
      images of the generators in an ambient field (default: ``None``)
    - ``latex_names`` (or ``latex_name``) -- ``None``, a string, or a
      list of strings (default: ``None``); how the generators are printed
      for latex output
    - ``assume_disc_small`` -- boolean (default: ``False``); if ``True``,
      assume that no square of a prime greater than PARI's primelimit
      (which should be 500000). Only applies for absolute fields at
      present.
    - ``maximize_at_primes`` -- ``None`` or a list of primes (default:
      ``None``); if not ``None``, then the maximal order is computed by
      maximizing only at the primes in this list, which completely avoids
      having to factor the discriminant, but of course can lead to wrong
      results; only applies for absolute fields at present.
    - ``structure`` -- ``None``, a list or an instance of
      :class:`structure.NumberFieldStructure` (default: ``None``),
      internally used to pass in additional structural information, e.g.,
      about the field from which this field is created as a subfield.

    We accept ``implementation`` and ``prec`` attributes for compatibility
    with :class:`~sage.categories.pushout.AlgebraicExtensionFunctor`
    but we ignore them as they are not used.

    EXAMPLES::

        sage: z = QQ['z'].0
        sage: K = NumberField(z^2 - 2, 's'); K
        Number Field in s with defining polynomial z^2 - 2
        sage: s = K.0; s
        s
        sage: s*s
        2
        sage: s^2
        2

    Constructing a relative number field::

        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^2 - 2)
        sage: R.<t> = K[]
        sage: L.<b> = K.extension(t^3 + t + a); L
        Number Field in b with defining polynomial t^3 + t + a over its base field
        sage: L.absolute_field('c')
        Number Field in c with defining polynomial x^6 + 2*x^4 + x^2 - 2
        sage: a*b
        a*b
        sage: L(a)
        a
        sage: L.lift_to_base(b^3 + b)
        -a

    Constructing another number field::

        sage: k.<i> = NumberField(x^2 + 1)
        sage: R.<z> = k[]
        sage: m.<j> = NumberField(z^3 + i*z + 3)
        sage: m
        Number Field in j with defining polynomial z^3 + i*z + 3 over its base field

    Number fields are globally unique::

        sage: K.<a> = NumberField(x^3 - 5)
        sage: a^3
        5
        sage: L.<a> = NumberField(x^3 - 5)
        sage: K is L
        True

    Equality of number fields depends on the variable name of the
    defining polynomial::

        sage: x = polygen(QQ, 'x'); y = polygen(QQ, 'y')
        sage: k.<a> = NumberField(x^2 + 3)
        sage: m.<a> = NumberField(y^2 + 3)
        sage: k
        Number Field in a with defining polynomial x^2 + 3
        sage: m
        Number Field in a with defining polynomial y^2 + 3
        sage: k == m
        False

    In case of conflict of the generator name with the name given by the preparser, the name given by the preparser takes precedence::

        sage: K.<b> = NumberField(x^2 + 5, 'a'); K
        Number Field in b with defining polynomial x^2 + 5

    One can also define number fields with specified embeddings, may be used
    for arithmetic and deduce relations with other number fields which would
    not be valid for an abstract number field. ::

        sage: K.<a> = NumberField(x^3 - 2, embedding=1.2)
        sage: RR.coerce_map_from(K)
        Composite map:
          From: Number Field in a with defining polynomial x^3 - 2 with a = 1.259921049894873?
          To:   Real Field with 53 bits of precision
          Defn:   Generic morphism:
                  From: Number Field in a with defining polynomial x^3 - 2
                        with a = 1.259921049894873?
                  To:   Real Lazy Field
                  Defn: a -> 1.259921049894873?
                then
                  Conversion via _mpfr_ method map:
                  From: Real Lazy Field
                  To:   Real Field with 53 bits of precision
        sage: RR(a)
        1.25992104989487
        sage: 1.1 + a
        2.35992104989487
        sage: b = 1/(a+1); b
        1/3*a^2 - 1/3*a + 1/3
        sage: RR(b)
        0.442493334024442
        sage: L.<b> = NumberField(x^6 - 2, embedding=1.1)
        sage: L(a)
        b^2
        sage: a + b
        b^2 + b

    Note that the image only needs to be specified to enough precision
    to distinguish roots, and is exactly computed to any needed
    precision::

        sage: RealField(200)(a)
        1.2599210498948731647672106072782283505702514647015079800820

    One can embed into any other field::

        sage: K.<a> = NumberField(x^3 - 2, embedding=CC.gen() - 0.6)
        sage: CC(a)
        -0.629960524947436 + 1.09112363597172*I

        sage: # needs sage.rings.padics
        sage: L = Qp(5)
        sage: f = polygen(L)^3 - 2
        sage: K.<a> = NumberField(x^3 - 2, embedding=f.roots()[0][0])
        sage: a + L(1)
        4 + 2*5^2 + 2*5^3 + 3*5^4 + 5^5 + 4*5^6 + 2*5^8 + 3*5^9 + 4*5^12
         + 4*5^14 + 4*5^15 + 3*5^16 + 5^17 + 5^18 + 2*5^19 + O(5^20)
        sage: L.<b> = NumberField(x^6 - x^2 + 1/10, embedding=1)
        sage: K.<a> = NumberField(x^3 - x + 1/10, embedding=b^2)
        sage: a + b
        b^2 + b
        sage: CC(a) == CC(b)^2
        True
        sage: K.coerce_embedding()
        Generic morphism:
          From: Number Field in a with defining polynomial x^3 - x + 1/10 with a = b^2
          To:   Number Field in b with defining polynomial x^6 - x^2 + 1/10
                with b = 0.9724449978911874?
          Defn: a -> b^2

    The ``QuadraticField`` and ``CyclotomicField`` constructors
    create an embedding by default unless otherwise specified::

        sage: K.<zeta> = CyclotomicField(15)
        sage: CC(zeta)
        0.913545457642601 + 0.406736643075800*I
        sage: L.<sqrtn3> = QuadraticField(-3)
        sage: K(sqrtn3)
        2*zeta^5 + 1
        sage: sqrtn3 + zeta
        2*zeta^5 + zeta + 1

    Comparison depends on the (real) embedding specified (or the one selected by default).
    Note that the codomain of the embedding must be ``QQbar`` or ``AA`` for this to work
    (see :issue:`20184`)::

        sage: N.<g> = NumberField(x^3 + 2, embedding=1)
        sage: 1 < g
        False
        sage: g > 1
        False
        sage: RR(g)
        -1.25992104989487

    If no embedding is specified or is complex, the comparison is not
    returning something meaningful. ::

        sage: N.<g> = NumberField(x^3 + 2)
        sage: 1 < g
        False
        sage: g > 1
        True

    Since SageMath 6.9, number fields may be defined by polynomials
    that are not necessarily integral or monic.  The only notable
    practical point is that in the PARI interface, a monic integral
    polynomial defining the same number field is computed and used::

        sage: K.<a> = NumberField(2*x^3 + x + 1)
        sage: K.pari_polynomial()
        x^3 + 2*x + 4

    Elements and ideals may be converted to and from PARI as follows::

        sage: pari(a)
        Mod(1/2*y, y^3 + 2*y + 4)
        sage: K(pari(a))
        a
        sage: I = K.ideal(a); I
        Fractional ideal (a)
        sage: I.pari_hnf()
        [1, 0, 0; 0, 1, 0; 0, 0, 1/2]
        sage: K.ideal(I.pari_hnf())
        Fractional ideal (a)

    Here is an example where the field has non-trivial class group::

        sage: L.<b> = NumberField(3*x^2 - 1/5)
        sage: L.pari_polynomial()
        x^2 - 15
        sage: J = L.primes_above(2)[0]; J
        Fractional ideal (2, 15*b + 1)
        sage: J.pari_hnf()
        [2, 1; 0, 1]
        sage: L.ideal(J.pari_hnf())
        Fractional ideal (2, 15*b + 1)

    An example involving a variable name that defines a function in
    PARI::

        sage: theta = polygen(QQ, 'theta')
        sage: M.<z> = NumberField([theta^3 + 4, theta^2 + 3]); M
        Number Field in z0 with defining polynomial theta^3 + 4 over its base field

    TESTS::

        sage: x = QQ['x'].gen()
        sage: y = ZZ['y'].gen()
        sage: K = NumberField(x^3 + x + 3, 'a'); K
        Number Field in a with defining polynomial x^3 + x + 3
        sage: K.defining_polynomial().parent()
        Univariate Polynomial Ring in x over Rational Field

    ::

        sage: L = NumberField(y^3 + y + 3, 'a'); L
        Number Field in a with defining polynomial y^3 + y + 3
        sage: L.defining_polynomial().parent()
        Univariate Polynomial Ring in y over Rational Field

    ::

        sage: W1 = NumberField(x^2 + 1,'a')
        sage: K.<x> = CyclotomicField(5)[]
        sage: W.<a> = NumberField(x^2 + 1); W
        Number Field in a with defining polynomial x^2 + 1 over its base field

    The following has been fixed in :issue:`8800`::

        sage: P.<x> = QQ[]
        sage: K.<a> = NumberField(x^3 - 5, embedding=0)
        sage: L.<b> = K.extension(x^2 + a)
        sage: F, R = L.construction()
        sage: F(R) == L    # indirect doctest
        True

    Check that :issue:`11670` has been fixed::

        sage: K.<a> = NumberField(x^2 - x - 1)
        sage: loads(dumps(K)) is K
        True
        sage: K.<a> = NumberField(x^3 - x - 1)
        sage: loads(dumps(K)) is K
        True
        sage: K.<a> = CyclotomicField(7)
        sage: loads(dumps(K)) is K
        True

    Another problem that was found while working on :issue:`11670`,
    ``maximize_at_primes`` and ``assume_disc_small`` were lost when pickling::

        sage: # needs sage.symbolic
        sage: K.<a> = NumberField(x^3 - 2, assume_disc_small=True,
        ....:                     maximize_at_primes=[2],
        ....:                     latex_name='\\\\alpha', embedding=2^(1/3))
        sage: L = loads(dumps(K))
        sage: L._assume_disc_small
        True
        sage: L._maximize_at_primes
        (2,)

    It is an error not to specify the generator::

        sage: K = NumberField(x^2 - 2)
        Traceback (most recent call last):
        ...
        TypeError: You must specify the name of the generator.

    Check that we can construct morphisms to matrix space (:issue:`23418`)::

        sage: t = polygen(QQ)
        sage: K = NumberField(t^4 - 2, 'a')
        sage: K.hom([K.gen().matrix()])
        Ring morphism:
          From: Number Field in a with defining polynomial x^4 - 2
          To:   Full MatrixSpace of 4 by 4 dense matrices over Rational Field
          Defn: a |--> [0 1 0 0]
                       [0 0 1 0]
                       [0 0 0 1]
                       [2 0 0 0]
    """

class NumberFieldFactory(UniqueFactory):
    '''
    Factory for number fields.

    This should usually not be called directly, use :meth:`NumberField`
    instead.

    INPUT:

    - ``polynomial`` -- a polynomial over `\\QQ` or a number field
    - ``name`` -- string (default: ``\'a\'``); the name of the generator
    - ``check`` -- boolean (default: ``True``); do type checking and
      irreducibility checking
    - ``embedding`` -- ``None`` or an element, the images of the generator
      in an ambient field (default: ``None``)
    - ``latex_name`` -- ``None`` or string (default: ``None``); how the
      generator is printed for latex output
    - ``assume_disc_small`` -- boolean (default: ``False``); if ``True``,
      assume that no square of a prime greater than PARI\'s primelimit
      (which should be 500000). Only applies for absolute fields at
      present.
    - ``maximize_at_primes`` -- ``None`` or a list of primes (default:
      ``None``); if not ``None``, then the maximal order is computed by
      maximizing only at the primes in this list, which completely avoids
      having to factor the discriminant, but of course can lead to wrong
      results; only applies for absolute fields at present.
    - ``structure`` -- ``None`` or an instance of
      :class:`structure.NumberFieldStructure` (default: ``None``),
      internally used to pass in additional structural information, e.g.,
      about the field from which this field is created as a subfield.

    TESTS::

        sage: from sage.rings.number_field.number_field import NumberFieldFactory
        sage: nff = NumberFieldFactory("number_field_factory")
        sage: R.<x> = QQ[]
        sage: nff(x^2 + 1, name=\'a\', check=False, embedding=None, latex_name=None,
        ....:     assume_disc_small=False, maximize_at_primes=None, structure=None)
        Number Field in a with defining polynomial x^2 + 1

    Pickling preserves the ``structure()`` of a number field::

        sage: K.<a> = QuadraticField(2)
        sage: L.<b> = K.change_names()
        sage: M = loads(dumps(L))
        sage: M.structure()
        (Isomorphism given by variable name change map:
           From: Number Field in b with defining polynomial x^2 - 2
           To:   Number Field in a with defining polynomial x^2 - 2 with a = 1.414213562373095?,
         Isomorphism given by variable name change map:
           From: Number Field in a with defining polynomial x^2 - 2 with a = 1.414213562373095?
           To:   Number Field in b with defining polynomial x^2 - 2)
    '''
    def create_key_and_extra_args(self, polynomial, name, check, embedding, latex_name, assume_disc_small, maximize_at_primes, structure):
        '''
        Create a unique key for the number field specified by the parameters.

        TESTS::

            sage: from sage.rings.number_field.number_field import NumberFieldFactory
            sage: nff = NumberFieldFactory("number_field_factory")
            sage: R.<x> = QQ[]
            sage: nff.create_key_and_extra_args(x^2+1, name=\'a\', check=False, embedding=None,
            ....:     latex_name=None, assume_disc_small=False, maximize_at_primes=None, structure=None)
            ((Rational Field, x^2 + 1, (\'a\',), None, \'a\', None, False, None),
             {\'check\': False})
        '''
    def create_object(self, version, key, check):
        '''
        Create the unique number field defined by ``key``.

        TESTS::

            sage: from sage.rings.number_field.number_field import NumberFieldFactory
            sage: nff = NumberFieldFactory("number_field_factory")
            sage: R.<x> = QQ[]
            sage: nff.create_object(None, (QQ, x^2 + 1, (\'a\',), None, None, None, False, None), check=False)
            Number Field in a with defining polynomial x^2 + 1
        '''

NumberField_version2: Incomplete

def NumberFieldTower(polynomials, names, check: bool = True, embeddings=None, latex_names=None, assume_disc_small: bool = False, maximize_at_primes=None, structures=None):
    """
    Create the tower of number fields defined by the polynomials in the list
    ``polynomials``.

    INPUT:

    - ``polynomials`` -- list of polynomials. Each entry must be polynomial
      which is irreducible over the number field generated by the roots of the
      following entries.
    - ``names`` -- list of strings or a string, the names of the generators of
      the relative number fields. If a single string, then names are generated
      from that string.
    - ``check`` -- boolean (default: ``True``); whether to check that the
      polynomials are irreducible
    - ``embeddings`` -- list of elements or ``None`` (default: ``None``);
      embeddings of the relative number fields in an ambient field
    - ``latex_names`` -- list of strings or ``None`` (default: ``None``); names
      used to print the generators for latex output
    - ``assume_disc_small`` -- boolean (default: ``False``); if ``True``,
      assume that no square of a prime greater than PARI's ``primelimit``
      (which should be 500000). Only applies for absolute fields at
      present.
    - ``maximize_at_primes`` -- ``None`` or a list of primes (default:
      ``None``); if not ``None``, then the maximal order is computed by
      maximizing only at the primes in this list, which completely avoids
      having to factor the discriminant, but of course can lead to wrong
      results; only applies for absolute fields at present.
    - ``structures`` -- ``None`` or a list (default: ``None``), internally used
      to provide additional information about the number field such as the
      field from which it was created.

    OUTPUT:

    The relative number field generated by a root of the first entry of
    ``polynomials`` over the relative number field generated by root of the
    second entry of ``polynomials`` ... over the number field over which the
    last entry of ``polynomials`` is defined.

    EXAMPLES::

        sage: x = polygen(ZZ, 'x')
        sage: k.<a,b,c> = NumberField([x^2 + 1, x^2 + 3, x^2 + 5]); k  # indirect doctest
        Number Field in a with defining polynomial x^2 + 1 over its base field
        sage: a^2
        -1
        sage: b^2
        -3
        sage: c^2
        -5
        sage: (a+b+c)^2
        (2*b + 2*c)*a + 2*c*b - 9

    The Galois group is a product of 3 groups of order 2::

        sage: k.absolute_field(names='c').galois_group()                                # needs sage.groups
        Galois group 8T3 (2[x]2[x]2) with order 8 of x^8 + 36*x^6 + 302*x^4 + 564*x^2 + 121

    Repeatedly calling base_field allows us to descend the internally
    constructed tower of fields::

        sage: k.base_field()
        Number Field in b with defining polynomial x^2 + 3 over its base field
        sage: k.base_field().base_field()
        Number Field in c with defining polynomial x^2 + 5
        sage: k.base_field().base_field().base_field()
        Rational Field

    In the following example the second polynomial is reducible over
    the first, so we get an error::

        sage: v = NumberField([x^3 - 2, x^3 - 2], names='a')
        Traceback (most recent call last):
        ...
        ValueError: defining polynomial (x^3 - 2) must be irreducible

    We mix polynomial parent rings::

        sage: k.<y> = QQ[]
        sage: m = NumberField([y^3 - 3, x^2 + x + 1, y^3 + 2], 'beta'); m
        Number Field in beta0 with defining polynomial y^3 - 3 over its base field
        sage: m.base_field ()
        Number Field in beta1 with defining polynomial x^2 + x + 1 over its base field

    A tower of quadratic fields::

        sage: K.<a> = NumberField([x^2 + 3, x^2 + 2, x^2 + 1]); K
        Number Field in a0 with defining polynomial x^2 + 3 over its base field
        sage: K.base_field()
        Number Field in a1 with defining polynomial x^2 + 2 over its base field
        sage: K.base_field().base_field()
        Number Field in a2 with defining polynomial x^2 + 1

    LaTeX versions of generator names can be specified either as::

        sage: K = NumberField([x^3 - 2, x^3 - 3, x^3 - 5], names=['a', 'b', 'c'],
        ....:                 latex_names=[r'\\alpha', r'\\beta', r'\\gamma'])
        sage: K.inject_variables(verbose=False)
        sage: latex(a + b + c)
        \\alpha + \\beta + \\gamma

    or as::

        sage: K = NumberField([x^3 - 2, x^3 - 3, x^3 - 5], names='a', latex_names=r'\\alpha')
        sage: K.inject_variables()
        Defining a0, a1, a2
        sage: latex(a0 + a1 + a2)
        \\alpha_{0} + \\alpha_{1} + \\alpha_{2}

    A bigger tower of quadratic fields::

        sage: K.<a2,a3,a5,a7> = NumberField([x^2 + p for p in [2,3,5,7]]); K
        Number Field in a2 with defining polynomial x^2 + 2 over its base field
        sage: a2^2
        -2
        sage: a3^2
        -3
        sage: (a2+a3+a5+a7)^3
        ((6*a5 + 6*a7)*a3 + 6*a7*a5 - 47)*a2 + (6*a7*a5 - 45)*a3 - 41*a5 - 37*a7

    The function can also be called by name::

        sage: NumberFieldTower([x^2 + 1, x^2 + 2], ['a','b'])
        Number Field in a with defining polynomial x^2 + 1 over its base field
    """
def QuadraticField(D, name: str = 'a', check: bool = True, embedding: bool = True, latex_name: str = 'sqrt', **args):
    """
    Return a quadratic field obtained by adjoining a square root of
    `D` to the rational numbers, where `D` is not a
    perfect square.

    INPUT:

    - ``D`` -- a rational number

    - ``name`` -- variable name (default: ``'a'``)

    - ``check`` -- boolean (default: ``True``)

    - ``embedding`` -- boolean or square root of `D` in an ambient field
      (default: ``True``)

    - ``latex_name`` -- latex variable name (default: `\\sqrt{D}`)

    OUTPUT: a number field defined by a quadratic polynomial. Unless
    otherwise specified, it has an embedding into `\\RR` or
    `\\CC` by sending the generator to the positive
    or upper-half-plane root.

    EXAMPLES::

        sage: QuadraticField(3, 'a')
        Number Field in a with defining polynomial x^2 - 3 with a = 1.732050807568878?
        sage: K.<theta> = QuadraticField(3); K
        Number Field in theta with defining polynomial x^2 - 3 with theta = 1.732050807568878?
        sage: RR(theta)
        1.73205080756888
        sage: QuadraticField(9, 'a')
        Traceback (most recent call last):
        ...
        ValueError: D must not be a perfect square.
        sage: QuadraticField(9, 'a', check=False)
        Number Field in a with defining polynomial x^2 - 9 with a = 3

    Quadratic number fields derive from general number fields.

    ::

        sage: from sage.rings.number_field.number_field_base import NumberField
        sage: type(K)
        <class 'sage.rings.number_field.number_field.NumberField_quadratic_with_category'>
        sage: isinstance(K, NumberField)
        True

    Quadratic number fields are cached::

        sage: QuadraticField(-11, 'a') is QuadraticField(-11, 'a')
        True

    By default, quadratic fields come with a nice latex representation::

        sage: K.<a> = QuadraticField(-7)
        sage: latex(K)
        \\Bold{Q}(\\sqrt{-7})
        sage: latex(a)
        \\sqrt{-7}
        sage: latex(1/(1+a))
        -\\frac{1}{8} \\sqrt{-7} + \\frac{1}{8}
        sage: list(K.latex_variable_names())
        ['\\\\sqrt{-7}']

    We can provide our own name as well::

        sage: K.<a> = QuadraticField(next_prime(10^10), latex_name=r'\\sqrt{D}')
        sage: 1 + a
        a + 1
        sage: latex(1 + a)
        \\sqrt{D} + 1
        sage: latex(QuadraticField(-1, 'a', latex_name=None).gen())
        a

    The name of the generator does not interfere with Sage preparser, see :issue:`1135`::

        sage: K1 = QuadraticField(5, 'x')
        sage: K2.<x> = QuadraticField(5)
        sage: K3.<x> = QuadraticField(5, 'x')
        sage: K1 is K2
        True
        sage: K1 is K3
        True
        sage: K1
        Number Field in x with defining polynomial x^2 - 5 with x = 2.236067977499790?


    Note that, in presence of two different names for the generator,
    the name given by the preparser takes precedence::

        sage: K4.<y> = QuadraticField(5, 'x'); K4
        Number Field in y with defining polynomial x^2 - 5 with y = 2.236067977499790?
        sage: K1 == K4
        False

    TESTS::

        sage: QuadraticField(-11, 'a') is QuadraticField(-11, 'a', latex_name='Z')
        False
        sage: QuadraticField(-11, 'a') is QuadraticField(-11, 'a', latex_name=None)
        False

    Check that :issue:`23459` is fixed::

        sage: QuadraticField(4**1000+1)
        Number Field ...

    Check quadratic fields without embedding (:issue:`28932`)::

        sage: QuadraticField(3, embedding=False)
        Number Field in a with defining polynomial x^2 - 3
    """
def GaussianField():
    """
    The field `\\QQ[i]`.

    TESTS::

        sage: from sage.rings.number_field.number_field import GaussianField
        sage: QQi = GaussianField()
        sage: QQi.coerce_embedding()
        Generic morphism:
          From: Number Field in I with defining polynomial x^2 + 1 with I = 1*I
          To:   Complex Lazy Field
          Defn: I -> 1*I
        sage: (I + 1/2).parent() is GaussianField()
        True
    """
def is_AbsoluteNumberField(x):
    """
    Return ``True`` if ``x`` is an absolute number field.

    EXAMPLES::

        sage: from sage.rings.number_field.number_field import is_AbsoluteNumberField
        sage: x = polygen(ZZ, 'x')
        sage: is_AbsoluteNumberField(NumberField(x^2 + 1, 'a'))
        doctest:warning...
        DeprecationWarning: The function is_AbsoluteNumberField is deprecated; use 'isinstance(..., NumberField_absolute)' instead.
        See https://github.com/sagemath/sage/issues/38124 for details.
        True
        sage: is_AbsoluteNumberField(NumberField([x^3 + 17, x^2 + 1], 'a'))
        False

    The rationals are a number field, but they're not of the absolute
    number field class.

    ::

        sage: is_AbsoluteNumberField(QQ)
        False
    """

class CyclotomicFieldFactory(UniqueFactory):
    """
    Return the `n`-th cyclotomic field, where `n` is a positive integer,
    or the universal cyclotomic field if `n=0`.

    For the documentation of the universal cyclotomic field, see
    :class:`~sage.rings.universal_cyclotomic_field.UniversalCyclotomicField`.

    INPUT:

    - ``n`` -- nonnegative integer (default: `0`)

    - ``names`` -- name of generator (default: ``zetan``)

    - ``bracket`` -- defines the brackets in the case of `n=0`, and
      is ignored otherwise. Can be any even length string, with ``'()'`` being
      the default.

    - ``embedding`` -- boolean or `n`-th root of unity in an ambient field
      (default: ``True``)

    EXAMPLES:

    If called without a parameter, we get the :class:`universal cyclotomic
    field<sage.rings.universal_cyclotomic_field.UniversalCyclotomicField>`::

        sage: CyclotomicField()                                                         # needs sage.libs.gap
        Universal Cyclotomic Field

    We create the `7`\\th cyclotomic field
    `\\QQ(\\zeta_7)` with the default generator name.

    ::

        sage: k = CyclotomicField(7); k
        Cyclotomic Field of order 7 and degree 6
        sage: k.gen()
        zeta7

    The default embedding sends the generator to the complex primitive
    `n`-th root of unity of least argument.

    ::

        sage: CC(k.gen())
        0.623489801858734 + 0.781831482468030*I

    Cyclotomic fields are of a special type.

    ::

        sage: type(k)
        <class 'sage.rings.number_field.number_field.NumberField_cyclotomic_with_category'>

    We can specify a different generator name as follows.

    ::

        sage: k.<z7> = CyclotomicField(7); k
        Cyclotomic Field of order 7 and degree 6
        sage: k.gen()
        z7

    The `n` must be an integer.

    ::

        sage: CyclotomicField(3/2)
        Traceback (most recent call last):
        ...
        TypeError: no conversion of this rational to integer

    The degree must be nonnegative.

    ::

        sage: CyclotomicField(-1)
        Traceback (most recent call last):
        ...
        ValueError: n (=-1) must be a positive integer

    The special case `n=1` does *not* return the rational
    numbers::

        sage: CyclotomicField(1)
        Cyclotomic Field of order 1 and degree 1

    Due to their default embedding into `\\CC`,
    cyclotomic number fields are all compatible.

    ::

        sage: cf30 = CyclotomicField(30)
        sage: cf5 = CyclotomicField(5)
        sage: cf3 = CyclotomicField(3)
        sage: cf30.gen() + cf5.gen() + cf3.gen()
        zeta30^6 + zeta30^5 + zeta30 - 1
        sage: cf6 = CyclotomicField(6) ; z6 = cf6.0
        sage: cf3 = CyclotomicField(3) ; z3 = cf3.0
        sage: cf3(z6)
        zeta3 + 1
        sage: cf6(z3)
        zeta6 - 1
        sage: cf9 = CyclotomicField(9) ; z9 = cf9.0
        sage: cf18 = CyclotomicField(18) ; z18 = cf18.0
        sage: cf18(z9)
        zeta18^2
        sage: cf9(z18)
        -zeta9^5
        sage: cf18(z3)
        zeta18^3 - 1
        sage: cf18(z6)
        zeta18^3
        sage: cf18(z6)**2
        zeta18^3 - 1
        sage: cf9(z3)
        zeta9^3
    """
    def create_key(self, n: int = 0, names=None, embedding: bool = True):
        """
        Create the unique key for the cyclotomic field specified by the
        parameters.

        TESTS::

            sage: CyclotomicField.create_key()
            (0, None, True)
        """
    def create_object(self, version, key, **extra_args):
        """
        Create the unique cyclotomic field defined by ``key``.

        TESTS::

            sage: CyclotomicField.create_object(None, (0, None, True))                  # needs sage.libs.gap
            Universal Cyclotomic Field
        """

CyclotomicField: Incomplete
is_NumberField: Incomplete

class NumberField_generic(WithEqualityById, number_field_base.NumberField):
    """
    Generic class for number fields defined by an irreducible
    polynomial over `\\QQ`.

    EXAMPLES::

        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^3 - 2); K
        Number Field in a with defining polynomial x^3 - 2
        sage: TestSuite(K).run()

    TESTS::

        sage: k.<a> = NumberField(x^3 + 2); m.<b> = NumberField(x^3 + 2)
        sage: k == QQ
        False
        sage: k.<a> = NumberField(x^3 + 2); m.<a> = NumberField(x^3 + 2)
        sage: k is m
        True
        sage: loads(dumps(k)) is k
        True

        sage: x = QQ['x'].gen()
        sage: y = ZZ['y'].gen()
        sage: K = NumberField(x^3 + x + 3, 'a'); K
        Number Field in a with defining polynomial x^3 + x + 3
        sage: K.defining_polynomial().parent()
        Univariate Polynomial Ring in x over Rational Field

        sage: L = NumberField(y^3 + y + 3, 'a'); L
        Number Field in a with defining polynomial y^3 + y + 3
        sage: L.defining_polynomial().parent()
        Univariate Polynomial Ring in y over Rational Field
        sage: L == K
        False

        sage: NumberField(ZZ['x'].0^4 + 23, 'a') == NumberField(ZZ['y'].0^4 + 23, 'a')
        False
        sage: NumberField(ZZ['x'].0^4 + 23, 'a') == NumberField(QQ['y'].0^4 + 23, 'a')
        False
        sage: NumberField(QQ['x'].0^4 + 23, 'a') == NumberField(QQ['y'].0^4 + 23, 'a')
        False

        sage: x = polygen(QQ); y = ZZ['y'].gen()
        sage: NumberField(x^3 + x + 5, 'a') == NumberField(y^3 + y + 5, 'a')
        False
        sage: NumberField(x^3 + x + 5, 'a') == NumberField(y^4 + y + 5, 'a')
        False
        sage: NumberField(x^3 + x + 5, 'a') == NumberField(x^3 + x + 5, 'b')
        False
        sage: QuadraticField(2, 'a', embedding=2) == QuadraticField(2, 'a', embedding=-2)
        False

        sage: K.<a> = QuadraticField(2)
        sage: R.<x> = K[]
        sage: L.<b> = K.extension(x^2 + 1)
        sage: M.<b> = L.absolute_field()
        sage: M == L
        False
        sage: M['x'] == L['x']
        False

        sage: R.<x> = QQ[]
        sage: R.<y> = QQ[]
        sage: K.<a> = NumberField(x^2 + 1)
        sage: L.<a> = NumberField(y^2 + 1)
        sage: K == L
        False
        sage: hash(K) == hash(L)
        False

    Two relative number fields which are isomorphic as absolute
    fields, but which are not presented the same way, are not
    considered equal (see :issue:`18942`)::

        sage: F.<omega> = NumberField(x^2 + x + 1)
        sage: y = polygen(F)
        sage: K = F.extension(y^3 + 3*omega + 2, 'alpha')
        sage: L = F.extension(y^3 - 3*omega - 1, 'alpha')
        sage: K == L
        False
        sage: K.is_isomorphic(L)
        True
        sage: hash(K) == hash(L)
        False

    This example illustrates the issue resolved in :issue:`18942`::

        sage: F.<omega> = NumberField(x^2 + x + 1)
        sage: xx = polygen(F)
        sage: ps = [p for p, _ in F(7).factor()]
        sage: for mu in ps:
        ....:     K = F.extension(xx^3 - mu, 'alpha')
        ....:     print(K.defining_polynomial().roots(K))
        [(alpha, 1), ((-omega - 1)*alpha, 1), (omega*alpha, 1)]
        [(alpha, 1), (omega*alpha, 1), ((-omega - 1)*alpha, 1)]
        sage: for mu in ps:
        ....:     K = F.extension(xx^3 - mu, 'alpha')
        ....:     print(K.defining_polynomial().roots(K))
        [(alpha, 1), ((-omega - 1)*alpha, 1), (omega*alpha, 1)]
        [(alpha, 1), (omega*alpha, 1), ((-omega - 1)*alpha, 1)]

    This example was suggested on sage-nt; see :issue:`18942`::

        sage: G = DirichletGroup(80)                                                    # needs sage.modular
        sage: for chi in G:                     # long time                             # needs sage.modular
        ....:     D = ModularSymbols(chi, 2, -1).cuspidal_subspace().new_subspace().decomposition()
        ....:     for f in D:
        ....:         elt = f.q_eigenform(10, 'alpha')[3]
        ....:         assert elt.is_integral()
    """
    def __init__(self, polynomial, name, latex_name, check: bool = True, embedding=None, category=None, assume_disc_small: bool = False, maximize_at_primes=None, structure=None) -> None:
        """
        Create a number field.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: NumberField(x^97 - 19, 'a')
            Number Field in a with defining polynomial x^97 - 19

        The defining polynomial must be irreducible::

            sage: K.<a> = NumberField(x^2 - 1)
            Traceback (most recent call last):
            ...
            ValueError: defining polynomial (x^2 - 1) must be irreducible

        If you use ``check=False``, you avoid checking irreducibility of the
        defining polynomial, which can save time.

        ::

            sage: K.<a> = NumberField(x^2 - 1, check=False)

        It can also be dangerous::

            sage: (a-1)*(a+1)
            0

        The constructed object is in the category of number fields::

            sage: NumberField(x^2 + 3, 'a').category()
            Category of number fields
            sage: category(NumberField(x^2 + 3, 'a'))
            Category of number fields

        The special types of number fields, e.g., quadratic fields, do
        not have (yet?) their own category::

            sage: QuadraticField(2,'d').category()
            Category of number fields

        TESTS::

            sage: NumberField(ZZ['x'].0^4 + 23, 'a')
            Number Field in a with defining polynomial x^4 + 23
            sage: NumberField(QQ['x'].0^4 + 23, 'a')
            Number Field in a with defining polynomial x^4 + 23
            sage: NumberField(GF(7)['x'].0^4 + 23, 'a')                                 # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            TypeError: polynomial must be defined over rational field
        """
    def construction(self):
        """
        Construction of ``self``.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 + x^2 + 1, embedding=CC.gen())
            sage: F, R = K.construction()
            sage: F
            AlgebraicExtensionFunctor
            sage: R
            Rational Field

        The construction functor respects distinguished embeddings::

            sage: F(R) is K
            True
            sage: F.embeddings
            [0.2327856159383841? + 0.7925519925154479?*I]

        TESTS::

            sage: K.<a> = NumberField(x^3 + x + 1)
            sage: R.<t> = ZZ[]
            sage: a + t     # indirect doctest
            t + a
            sage: (a + t).parent()
            Univariate Polynomial Ring in t over Number Field in a with defining polynomial x^3 + x + 1

        The construction works for non-absolute number fields as well::

            sage: K.<a,b,c>=NumberField([x^3+x^2+1,x^2+1,x^7+x+1])
            sage: F,R = K.construction()
            sage: F(R) == K
            True

        ::

            sage: P.<x> = QQ[]
            sage: K.<a> = NumberField(x^3-5, embedding=0)
            sage: L.<b> = K.extension(x^2+a)
            sage: a*b
            a*b

        The construction preserves latex variable names::

            sage: K.<a,b,c> = NumberField([x^3+x^2+1, x^2+1, x^7+x+1], latex_names=['alpha', 'beta', 'gamma'])
            sage: F, R = K.construction()
            sage: F(R) == K
            True
        """
    @cached_method
    def structure(self):
        """
        Return fixed isomorphism or embedding structure on ``self``.

        This is used to record various isomorphisms or embeddings that
        arise naturally in other constructions.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<z> = NumberField(x^2 + 3)
            sage: L.<a> = K.absolute_field(); L
            Number Field in a with defining polynomial x^2 + 3
            sage: L.structure()
            (Isomorphism given by variable name change map:
              From: Number Field in a with defining polynomial x^2 + 3
              To:   Number Field in z with defining polynomial x^2 + 3,
             Isomorphism given by variable name change map:
              From: Number Field in z with defining polynomial x^2 + 3
              To:   Number Field in a with defining polynomial x^2 + 3)

            sage: K.<a> = QuadraticField(-3)
            sage: R.<y> = K[]
            sage: D.<x0> = K.extension(y)
            sage: D_abs.<y0> = D.absolute_field()
            sage: D_abs.structure()[0](y0)
            -a
        """
    def completion(self, p, prec, extras={}):
        """
        Return the completion of ``self`` at `p` to the specified precision.

        Only implemented at archimedean places, and then only if
        an embedding has been fixed.

        EXAMPLES::

            sage: K.<a> = QuadraticField(2)
            sage: K.completion(infinity, 100)
            Real Field with 100 bits of precision
            sage: K.<zeta> = CyclotomicField(12)
            sage: K.completion(infinity, 53, extras={'type': 'RDF'})
            Complex Double Field
            sage: zeta + 1.5                            # implicit test
            2.36602540378444 + 0.500000000000000*I
        """
    def primitive_element(self):
        """
        Return a primitive element for this field, i.e., an element that
        generates it over `\\QQ`.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 + 2)
            sage: K.primitive_element()
            a
            sage: K.<a,b,c> = NumberField([x^2 - 2, x^2 - 3, x^2 - 5])
            sage: K.primitive_element()
            a - b + c
            sage: alpha = K.primitive_element(); alpha
            a - b + c
            sage: alpha.minpoly()
            x^2 + (2*b - 2*c)*x - 2*c*b + 6
            sage: alpha.absolute_minpoly()
            x^8 - 40*x^6 + 352*x^4 - 960*x^2 + 576
        """
    def random_element(self, num_bound=None, den_bound=None, integral_coefficients: bool = False, distribution=None):
        """
        Return a random element of this number field.

        INPUT:

        - ``num_bound`` -- bound on numerator of the coefficients of
          the resulting element

        - ``den_bound`` -- bound on denominators of the coefficients
          of the resulting element

        - ``integral_coefficients`` -- boolean (default: ``False``); if
          ``True``, then the resulting element will have integral coefficients.
          This option overrides any value of ``den_bound``.

        - ``distribution`` -- distribution to use for the coefficients
          of the resulting element

        OUTPUT: element of this number field

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<j> = NumberField(x^8 + 1)
            sage: K.random_element().parent() is K
            True

            sage: while K.random_element().list()[0] != 0:
            ....:     pass
            sage: while K.random_element().list()[0] == 0:
            ....:     pass
            sage: while K.random_element().is_prime():
            ....:     pass
            sage: while not K.random_element().is_prime():
            ....:     pass

            sage: K.<a,b,c> = NumberField([x^2 - 2, x^2 - 3, x^2 - 5])
            sage: K.random_element().parent() is K
            True

            sage: while K.random_element().is_prime():
            ....:     pass
            sage: while not K.random_element().is_prime():  # long time
            ....:     pass

            sage: K.<a> = NumberField(x^5 - 2)
            sage: p = K.random_element(integral_coefficients=True)
            sage: p.is_integral()
            True
            sage: while K.random_element().is_integral():
            ....:     pass

        TESTS::

            sage: K.<a> = NumberField(x^5 - 2)
            sage: K.random_element(-1)
            Traceback (most recent call last):
            ...
            TypeError: x must be < y
            sage: K.random_element(5, 0)
            Traceback (most recent call last):
            ...
            TypeError: x must be < y
            sage: QQ[I].random_element(0)
            Traceback (most recent call last):
            ...
            TypeError: x must be > 0
        """
    def subfield(self, alpha, name=None, names=None):
        """
        Return a number field `K` isomorphic to `\\QQ(\\alpha)`
        (if this is an absolute number field) or `L(\\alpha)` (if this
        is a relative extension `M/L`) and a map from `K` to ``self`` that
        sends the generator of `K` to ``alpha``.

        INPUT:

        - ``alpha`` -- an element of ``self``, or something that
          coerces to an element of ``self``

        OUTPUT:

        - ``K`` -- a number field
        - ``from_K`` -- a homomorphism from `K` to ``self`` that
          sends the generator of `K` to ``alpha``

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^4 - 3); K
            Number Field in a with defining polynomial x^4 - 3
            sage: H.<b>, from_H = K.subfield(a^2)
            sage: H
            Number Field in b with defining polynomial x^2 - 3 with b = a^2
            sage: from_H(b)
            a^2
            sage: from_H
            Ring morphism:
              From: Number Field in b with defining polynomial x^2 - 3 with b = a^2
              To:   Number Field in a with defining polynomial x^4 - 3
              Defn: b |--> a^2

        A relative example. Note that the result returned is the subfield generated
        by `\\alpha` over ``self.base_field()``, not over `\\QQ` (see :issue:`5392`)::

            sage: L.<a> = NumberField(x^2 - 3)
            sage: M.<b> = L.extension(x^4 + 1)
            sage: K, phi = M.subfield(b^2)
            sage: K.base_field() is L
            True

        Subfields inherit embeddings::

            sage: K.<z> = CyclotomicField(5)
            sage: L, K_from_L = K.subfield(z - z^2 - z^3 + z^4)
            sage: L
            Number Field in z0 with defining polynomial x^2 - 5 with z0 = 2.236067977499790?
            sage: CLF_from_K = K.coerce_embedding(); CLF_from_K
            Generic morphism:
              From: Cyclotomic Field of order 5 and degree 4
              To:   Complex Lazy Field
              Defn: z -> 0.309016994374948? + 0.951056516295154?*I
            sage: CLF_from_L = L.coerce_embedding(); CLF_from_L
            Generic morphism:
              From: Number Field in z0 with defining polynomial x^2 - 5
                    with z0 = 2.236067977499790?
              To:   Complex Lazy Field
              Defn: z0 -> 2.236067977499790?

        Check transitivity::

            sage: CLF_from_L(L.gen())
            2.236067977499790?
            sage: CLF_from_K(K_from_L(L.gen()))
            2.23606797749979? + 0.?e-14*I

        If ``self`` has no specified embedding, then `K` comes with an
        embedding in ``self``::

            sage: K.<a> = NumberField(x^6 - 6*x^4 + 8*x^2 - 1)
            sage: L.<b>, from_L = K.subfield(a^2)
            sage: L
            Number Field in b with defining polynomial x^3 - 6*x^2 + 8*x - 1 with b = a^2
            sage: L.gen_embedding()
            a^2

        You can also view a number field as having a different generator by
        just choosing the input to generate the whole field; for that it is
        better to use :meth:`change_generator`, which gives
        isomorphisms in both directions.
        """
    def change_generator(self, alpha, name=None, names=None):
        """
        Given the number field ``self``, construct another isomorphic number
        field `K` generated by the element ``alpha`` of ``self``, along
        with isomorphisms from `K` to ``self`` and from ``self`` to
        `K`.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: L.<i> = NumberField(x^2 + 1); L
            Number Field in i with defining polynomial x^2 + 1
            sage: K, from_K, to_K = L.change_generator(i/2 + 3)
            sage: K
            Number Field in i0 with defining polynomial x^2 - 6*x + 37/4 with i0 = 1/2*i + 3
            sage: from_K
            Ring morphism:
              From: Number Field in i0 with defining polynomial x^2 - 6*x + 37/4
                    with i0 = 1/2*i + 3
              To:   Number Field in i with defining polynomial x^2 + 1
              Defn: i0 |--> 1/2*i + 3
            sage: to_K
            Ring morphism:
              From: Number Field in i with defining polynomial x^2 + 1
              To:   Number Field in i0 with defining polynomial x^2 - 6*x + 37/4
                    with i0 = 1/2*i + 3
              Defn: i |--> 2*i0 - 6

        We can also do

        ::

            sage: K.<c>, from_K, to_K = L.change_generator(i/2 + 3); K
            Number Field in c with defining polynomial x^2 - 6*x + 37/4 with c = 1/2*i + 3


        We compute the image of the generator `\\sqrt{-1}` of `L`.

        ::

            sage: to_K(i)
            2*c - 6

        Note that the image is indeed a square root of `-1`.

        ::

            sage: to_K(i)^2
            -1
            sage: from_K(to_K(i))
            i
            sage: to_K(from_K(c))
            c
        """
    def subfield_from_elements(self, alpha, name=None, polred: bool = True, threshold=None):
        """
        Return the subfield generated by the elements ``alpha``.

        If the generated subfield by the elements ``alpha`` is either the
        rational field or the complete number field, the field returned is
        respectively ``QQ`` or ``self``.

        INPUT:

        - ``alpha`` -- list of elements in this number field

        - ``name`` -- a name for the generator of the new number field

        - ``polred`` -- boolean (default: ``True``); whether to optimize the
          generator of the newly created field

        - ``threshold`` -- positive number (default: ``None``) threshold to be
          passed to the ``do_polred`` function

        OUTPUT: a triple ``(field, beta, hom)`` where

        - ``field`` -- a subfield of this number field

        - ``beta`` -- list of elements of ``field`` corresponding to ``alpha``

        - ``hom`` -- inclusion homomorphism from ``field`` to ``self``

        EXAMPLES::

            sage: x = polygen(QQ)
            sage: poly = x^4 - 4*x^2 + 1
            sage: emb = AA.polynomial_root(poly, RIF(0.51, 0.52))
            sage: K.<a> = NumberField(poly, embedding=emb)
            sage: sqrt2 = -a^3 + 3*a
            sage: sqrt3 = -a^2 + 2
            sage: assert sqrt2 ** 2 == 2 and sqrt3 ** 2 == 3
            sage: L, elts, phi = K.subfield_from_elements([sqrt2, 1 - sqrt2/3])
            sage: L
            Number Field in a0 with defining polynomial x^2 - 2 with a0 = 1.414213562373095?
            sage: elts
            [a0, -1/3*a0 + 1]
            sage: phi
            Ring morphism:
              From: Number Field in a0 with defining polynomial x^2 - 2
                    with a0 = 1.414213562373095?
              To:   Number Field in a with defining polynomial x^4 - 4*x^2 + 1
                    with a = 0.5176380902050415?
              Defn: a0 |--> -a^3 + 3*a
            sage: assert phi(elts[0]) == sqrt2
            sage: assert phi(elts[1]) == 1 - sqrt2/3


            sage: L, elts, phi = K.subfield_from_elements([1, sqrt3])
            sage: assert phi(elts[0]) == 1
            sage: assert phi(elts[1]) == sqrt3

            sage: L, elts, phi = K.subfield_from_elements([sqrt2, sqrt3])
            sage: phi
            Identity endomorphism of Number Field in a with defining polynomial
             x^4 - 4*x^2 + 1 with a = 0.5176380902050415?

        TESTS::

            sage: x = polygen(QQ)

            sage: p = x^8 - 12*x^6 + 23*x^4 - 12*x^2 + 1
            sage: K.<a> = NumberField(p)
            sage: sqrt2 = 6/7*a^7 - 71/7*a^5 + 125/7*a^3 - 43/7*a
            sage: sqrt3 = 3/7*a^6 - 32/7*a^4 + 24/7*a^2 + 10/7
            sage: sqrt5 = 8/7*a^6 - 90/7*a^4 + 120/7*a^2 - 27/7
            sage: assert sqrt2**2 == 2 and sqrt3**2 == 3 and sqrt5**2 == 5
            sage: L, elts, phi = K.subfield_from_elements([sqrt2, sqrt3], name='b')
            sage: assert phi(elts[0]) == sqrt2
            sage: assert phi(elts[1]) == sqrt3
            sage: L, elts, phi = K.subfield_from_elements([sqrt2, sqrt3], name='b', polred=False)
            sage: assert phi(elts[0]) == sqrt2
            sage: assert phi(elts[1]) == sqrt3
            sage: L, elts, phi = K.subfield_from_elements([sqrt2, sqrt5], name='b')
            sage: assert phi(elts[0]) == sqrt2
            sage: assert phi(elts[1]) == sqrt5
            sage: L, elts, phi = K.subfield_from_elements([sqrt3, sqrt5], name='b')
            sage: assert phi(elts[0]) == sqrt3
            sage: assert phi(elts[1]) == sqrt5
            sage: L, elts, phi = K.subfield_from_elements([-149582/214245 + 21423/5581*sqrt2], name='b')
            sage: assert L.polynomial() == x^2 - 2
            sage: L, elts, phi = K.subfield_from_elements([131490/777 - 1359/22*sqrt3], name='b')
            sage: assert L.polynomial() == x^2 - 3
            sage: L, elts, phi = K.subfield_from_elements([12241829/177 - 321121/22459 * sqrt5], name='b')
            sage: assert L.polynomial() == x^2 - x - 1

            sage: from sage.rings.qqbar import number_field_elements_from_algebraics
            sage: R.<x> = QQ[]
            sage: p1 = x^3 - x - 1
            sage: roots1 = p1.roots(QQbar, False)
            sage: for _ in range(10):
            ....:     p2 = R.random_element(degree=2)
            ....:     while not p2.is_irreducible(): p2 = R.random_element(degree=2)
            ....:     roots2 = p2.roots(QQbar, False)
            ....:     K, (a1,b1,c1,a2,b2), phi = number_field_elements_from_algebraics(roots1 + roots2)
            ....:     u1 = 1 - a1/17 + 3/7*a1**2
            ....:     u2 = 2 + 33/35 * a1
            ....:     L, (v1,v2), phi = K.subfield_from_elements([u1, u2], threshold=100)
            ....:     assert L.polynomial() == p1
            ....:     assert phi(v1) == u1 and phi(v2) == u2
        """
    def is_absolute(self) -> None:
        """
        Return ``True`` if ``self`` is an absolute field.

        This function will be implemented in the derived classes.

        EXAMPLES::

            sage: K = CyclotomicField(5)
            sage: K.is_absolute()
            True
        """
    def is_relative(self):
        """
        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<a> = NumberField(x^10 - 2)
            sage: K.is_absolute()
            True
            sage: K.is_relative()
            False
        """
    def quadratic_defect(self, a, p, check: bool = True):
        """
        Return the valuation of the quadratic defect of `a` at `p`.

        INPUT:

        - ``a`` -- an element of ``self``

        - ``p`` -- a prime ideal

        - ``check`` -- boolean (default: ``True``); check if `p` is prime

        ALGORITHM:

        This is an implementation of Algorithm 3.1.3 from [Kir2016]_.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<a> = NumberField(x^2 + 2)
            sage: p = K.primes_above(2)[0]
            sage: K.quadratic_defect(5, p)
            4
            sage: K.quadratic_defect(0, p)
            +Infinity
            sage: K.quadratic_defect(a, p)
            1
            sage: K.<a> = CyclotomicField(5)
            sage: p = K.primes_above(2)[0]
            sage: K.quadratic_defect(5, p)
            +Infinity

        TESTS::

            sage: x = polygen(QQ, 'x')
            sage: K.<t> = NumberField(x^10 - x^8 - 2*x^7 - x^6 + 2*x^5 + 2*x^4 - x^2 + 1)
            sage: p = K.prime_factors(2)[0]
            sage: pi = K.uniformizer(p)
            sage: a = 1 + pi^3
            sage: K.quadratic_defect(a, p)
            3
        """
    def absolute_field(self, names):
        """
        Return ``self`` as an absolute number field.

        INPUT:

        - ``names`` -- string; name of generator of the absolute field

        OUTPUT:

        - ``K`` -- this number field (since it is already absolute)

        Also, ``K.structure()`` returns ``from_K`` and ``to_K``, where
        ``from_K`` is an isomorphism from `K` to ``self`` and ``to_K``
        is an isomorphism from ``self`` to `K`.

        EXAMPLES::

            sage: K = CyclotomicField(5)
            sage: K.absolute_field('a')
            Number Field in a with defining polynomial x^4 + x^3 + x^2 + x + 1
        """
    def is_isomorphic(self, other, isomorphism_maps: bool = False) -> bool:
        """
        Return ``True`` if ``self`` is isomorphic as a number field to ``other``.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: k.<a> = NumberField(x^2 + 1)
            sage: m.<b> = NumberField(x^2 + 4)
            sage: k.is_isomorphic(m)
            True
            sage: m.<b> = NumberField(x^2 + 5)
            sage: k.is_isomorphic (m)
            False

        ::

            sage: k = NumberField(x^3 + 2, 'a')
            sage: k.is_isomorphic(NumberField((x+1/3)^3 + 2, 'b'))
            True
            sage: k.is_isomorphic(NumberField(x^3 + 4, 'b'))
            True
            sage: k.is_isomorphic(NumberField(x^3 + 5, 'b'))
            False

            sage: k = NumberField(x^2 - x - 1, 'b')
            sage: l = NumberField(x^2 - 7, 'a')
            sage: k.is_isomorphic(l, True)
            (False, [])

            sage: k = NumberField(x^2 - x - 1, 'b')
            sage: ky.<y> = k[]
            sage: l = NumberField(y, 'a')
            sage: k.is_isomorphic(l, True)
            (True, [-x, x + 1])

        TESTS:

        See :issue:`26239`::

            sage: k.<a> = NumberField(x)
            sage: k.is_isomorphic(k)
            True
        """
    def is_totally_real(self):
        """
        Return ``True`` if ``self`` is totally real, and ``False`` otherwise.

        Totally real means that every isomorphic embedding of ``self`` into the
        complex numbers has image contained in the real numbers.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: NumberField(x^2 + 2, 'alpha').is_totally_real()
            False
            sage: NumberField(x^2 - 2, 'alpha').is_totally_real()
            True
            sage: NumberField(x^4 - 2, 'alpha').is_totally_real()
            False
        """
    def is_totally_imaginary(self):
        """
        Return ``True`` if ``self`` is totally imaginary, and ``False`` otherwise.

        Totally imaginary means that no isomorphic embedding of ``self`` into
        the complex numbers has image contained in the real numbers.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: NumberField(x^2 + 2, 'alpha').is_totally_imaginary()
            True
            sage: NumberField(x^2 - 2, 'alpha').is_totally_imaginary()
            False
            sage: NumberField(x^4 - 2, 'alpha').is_totally_imaginary()
            False
        """
    def is_CM(self):
        """
        Return ``True`` if ``self`` is a CM field (i.e., a totally imaginary
        quadratic extension of a totally real field).

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: Q.<a> = NumberField(x - 1)
            sage: Q.is_CM()
            False
            sage: K.<i> = NumberField(x^2 + 1)
            sage: K.is_CM()
            True
            sage: L.<zeta20> = CyclotomicField(20)
            sage: L.is_CM()
            True
            sage: K.<omega> = QuadraticField(-3)
            sage: K.is_CM()
            True
            sage: L.<sqrt5> = QuadraticField(5)
            sage: L.is_CM()
            False
            sage: F.<a> = NumberField(x^3 - 2)
            sage: F.is_CM()
            False
            sage: F.<a> = NumberField(x^4 - x^3 - 3*x^2 + x + 1)
            sage: F.is_CM()
            False

        The following are non-CM totally imaginary fields.

        ::

            sage: F.<a> = NumberField(x^4 + x^3 - x^2 - x + 1)
            sage: F.is_totally_imaginary()
            True
            sage: F.is_CM()
            False
            sage: F2.<a> = NumberField(x^12 - 5*x^11 + 8*x^10 - 5*x^9 - x^8 + 9*x^7
            ....:                       + 7*x^6 - 3*x^5 + 5*x^4 + 7*x^3 - 4*x^2 - 7*x + 7)
            sage: F2.is_totally_imaginary()
            True
            sage: F2.is_CM()
            False

        The following is a non-cyclotomic CM field.

        ::

            sage: M.<a> = NumberField(x^4 - x^3 - x^2 - 2*x + 4)
            sage: M.is_CM()
            True

        Now, we construct a totally imaginary quadratic extension of a
        totally real field (which is not cyclotomic).

        ::

            sage: E_0.<a> = NumberField(x^7 - 4*x^6 - 4*x^5 + 10*x^4 + 4*x^3
            ....:                       - 6*x^2 - x + 1)
            sage: E_0.is_totally_real()
            True
            sage: E.<b> = E_0.extension(x^2 + 1)
            sage: E.is_CM()
            True

        Finally, a CM field that is given as an extension that is not CM.

        ::

            sage: E_0.<a> = NumberField(x^2 - 4*x + 16)
            sage: y = polygen(E_0)
            sage: E.<z> = E_0.extension(y^2 - E_0.gen() / 2)
            sage: E.is_CM()
            True
            sage: E.is_CM_extension()
            False
        """
    def complex_conjugation(self):
        """
        Return the complex conjugation of ``self``.

        This is only well-defined for fields contained in CM fields
        (i.e. for totally real fields and CM fields). Recall that a CM
        field is a totally imaginary quadratic extension of a totally
        real field. For other fields, a :exc:`ValueError` is raised.

        EXAMPLES::

            sage: QuadraticField(-1, 'I').complex_conjugation()
            Ring endomorphism of
             Number Field in I with defining polynomial x^2 + 1 with I = 1*I
              Defn: I |--> -I
            sage: CyclotomicField(8).complex_conjugation()
            Ring endomorphism of Cyclotomic Field of order 8 and degree 4
              Defn: zeta8 |--> -zeta8^3
            sage: QuadraticField(5, 'a').complex_conjugation()
            Identity endomorphism of Number Field in a with defining
             polynomial x^2 - 5 with a = 2.236067977499790?
            sage: x = polygen(QQ, 'x')
            sage: F = NumberField(x^4 + x^3 - 3*x^2 - x + 1, 'a')
            sage: F.is_totally_real()
            True
            sage: F.complex_conjugation()
            Identity endomorphism of Number Field in a with defining
             polynomial x^4 + x^3 - 3*x^2 - x + 1
            sage: F.<b> = NumberField(x^2 - 2)
            sage: F.extension(x^2 + 1, 'a').complex_conjugation()
            Relative number field endomorphism of Number Field in a
             with defining polynomial x^2 + 1 over its base field
              Defn: a |--> -a
                    b |--> b
            sage: F2.<b> = NumberField(x^2 + 2)
            sage: K2.<a> = F2.extension(x^2 + 1)
            sage: cc = K2.complex_conjugation()
            sage: cc(a)
            -a
            sage: cc(b)
            -b
        """
    def maximal_totally_real_subfield(self):
        """
        Return the maximal totally real subfield of ``self`` together with an embedding of it into ``self``.

        EXAMPLES::

            sage: F.<a> = QuadraticField(11)
            sage: F.maximal_totally_real_subfield()
            [Number Field in a with defining polynomial x^2 - 11 with a = 3.316624790355400?,
             Identity endomorphism of
              Number Field in a with defining polynomial x^2 - 11 with a = 3.316624790355400?]
            sage: F.<a> = QuadraticField(-15)
            sage: F.maximal_totally_real_subfield()
            [Rational Field, Natural morphism:
               From: Rational Field
               To:   Number Field in a with defining polynomial x^2 + 15
                     with a = 3.872983346207417?*I]
            sage: F.<a> = CyclotomicField(29)
            sage: F.maximal_totally_real_subfield()
            (Number Field in a0 with defining polynomial x^14 + x^13 - 13*x^12 - 12*x^11
               + 66*x^10 + 55*x^9 - 165*x^8 - 120*x^7 + 210*x^6 + 126*x^5 - 126*x^4
               - 56*x^3 + 28*x^2 + 7*x - 1 with a0 = 1.953241111420174?,
             Ring morphism:
               From: Number Field in a0 with defining polynomial x^14 + x^13 - 13*x^12 - 12*x^11
                     + 66*x^10 + 55*x^9 - 165*x^8 - 120*x^7 + 210*x^6 + 126*x^5 - 126*x^4
                     - 56*x^3 + 28*x^2 + 7*x - 1 with a0 = 1.953241111420174?
               To:   Cyclotomic Field of order 29 and degree 28
               Defn: a0 |--> -a^27 - a^26 - a^25 - a^24 - a^23 - a^22 - a^21 - a^20 - a^19
                             - a^18 - a^17 - a^16 - a^15 - a^14 - a^13 - a^12 - a^11 - a^10
                             - a^9 - a^8 - a^7 - a^6 - a^5 - a^4 - a^3 - a^2 - 1)
            sage: x = polygen(QQ, 'x')
            sage: F.<a> = NumberField(x^3 - 2)
            sage: F.maximal_totally_real_subfield()
            [Rational Field,
             Coercion map:
               From: Rational Field
               To:   Number Field in a with defining polynomial x^3 - 2]
            sage: F.<a> = NumberField(x^4 - x^3 - x^2 + x + 1)
            sage: F.maximal_totally_real_subfield()
            [Rational Field,
             Coercion map:
               From: Rational Field
               To:   Number Field in a with defining polynomial x^4 - x^3 - x^2 + x + 1]
            sage: F.<a> = NumberField(x^4 - x^3 + 2*x^2 + x + 1)
            sage: F.maximal_totally_real_subfield()
            [Number Field in a1 with defining polynomial x^2 - x - 1,
             Ring morphism:
              From: Number Field in a1 with defining polynomial x^2 - x - 1
              To:   Number Field in a with defining polynomial x^4 - x^3 + 2*x^2 + x + 1
              Defn: a1 |--> -1/2*a^3 - 1/2]
            sage: F.<a> = NumberField(x^4 - 4*x^2 - x + 1)
            sage: F.maximal_totally_real_subfield()
            [Number Field in a with defining polynomial x^4 - 4*x^2 - x + 1,
             Identity endomorphism of
              Number Field in a with defining polynomial x^4 - 4*x^2 - x + 1]

        An example of a relative extension where the base field is not the maximal totally real subfield.

        ::

            sage: E_0.<a> = NumberField(x^2 - 4*x + 16)
            sage: y = polygen(E_0)
            sage: E.<z> = E_0.extension(y^2 - E_0.gen() / 2)
            sage: E.maximal_totally_real_subfield()
            [Number Field in z1 with defining polynomial x^2 - 2*x - 5,
             Composite map:
               From: Number Field in z1 with defining polynomial x^2 - 2*x - 5
               To:   Number Field in z with defining polynomial x^2 - 1/2*a over its base field
               Defn:   Ring morphism:
                       From: Number Field in z1 with defining polynomial x^2 - 2*x - 5
                       To:   Number Field in z with defining
                             polynomial x^4 - 2*x^3 + x^2 + 6*x + 3
                       Defn: z1 |--> -1/3*z^3 + 1/3*z^2 + z - 1
                     then
                       Isomorphism map:
                       From: Number Field in z with defining
                             polynomial x^4 - 2*x^3 + x^2 + 6*x + 3
                       To:   Number Field in z with defining
                             polynomial x^2 - 1/2*a over its base field]
        """
    def complex_embeddings(self, prec: int = 53):
        """
        Return all homomorphisms of this number field into the approximate
        complex field with precision ``prec``.

        This always embeds into an MPFR based complex field.  If you
        want embeddings into the 53-bit double precision, which is
        faster, use ``self.embeddings(CDF)``.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: k.<a> = NumberField(x^5 + x + 17)
            sage: v = k.complex_embeddings()
            sage: ls = [phi(k.0^2) for phi in v]; ls  # random order
            [2.97572074038...,
             -2.40889943716 + 1.90254105304*I,
             -2.40889943716 - 1.90254105304*I,
             0.921039066973 + 3.07553311885*I,
             0.921039066973 - 3.07553311885*I]
            sage: K.<a> = NumberField(x^3 + 2)
            sage: ls = K.complex_embeddings(); ls  # random order
            [
            Ring morphism:
              From: Number Field in a with defining polynomial x^3 + 2
              To:   Complex Double Field
              Defn: a |--> -1.25992104989...,
            Ring morphism:
              From: Number Field in a with defining polynomial x^3 + 2
              To:   Complex Double Field
              Defn: a |--> 0.629960524947 - 1.09112363597*I,
            Ring morphism:
              From: Number Field in a with defining polynomial x^3 + 2
              To:   Complex Double Field
              Defn: a |--> 0.629960524947 + 1.09112363597*I
            ]
        """
    def real_embeddings(self, prec: int = 53):
        """
        Return all homomorphisms of this number field into the approximate
        real field with precision ``prec``.

        If ``prec`` is 53 (the default), then the real double field is
        used; otherwise the arbitrary precision (but slow) real field
        is used.  If you want embeddings into the 53-bit double
        precision, which is faster, use ``self.embeddings(RDF)``.

        .. NOTE::

            This function uses finite precision real numbers.
            In functions that should output proven results, one
            could use ``self.embeddings(AA)`` instead.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<a> = NumberField(x^3 + 2)
            sage: K.real_embeddings()
            [Ring morphism:
               From: Number Field in a with defining polynomial x^3 + 2
               To:   Real Field with 53 bits of precision
               Defn: a |--> -1.25992104989487]
            sage: K.real_embeddings(16)
            [Ring morphism:
               From: Number Field in a with defining polynomial x^3 + 2
               To:   Real Field with 16 bits of precision
               Defn: a |--> -1.260]
            sage: K.real_embeddings(100)
            [Ring morphism:
               From: Number Field in a with defining polynomial x^3 + 2
               To:   Real Field with 100 bits of precision
               Defn: a |--> -1.2599210498948731647672106073]

        As this is a numerical function, the number of embeddings
        may be incorrect if the precision is too low::

            sage: K = NumberField(x^2 + 2*10^1000*x + 10^2000 + 1, 'a')
            sage: len(K.real_embeddings())
            2
            sage: len(K.real_embeddings(100))
            2
            sage: len(K.real_embeddings(10000))
            0
            sage: len(K.embeddings(AA))
            0
        """
    def specified_complex_embedding(self):
        """
        Return the embedding of this field into the complex numbers which has
        been specified.

        Fields created with the :func:`QuadraticField` or
        :func:`CyclotomicField` constructors come with an implicit
        embedding. To get one of these fields without the embedding, use
        the generic :class:`NumberField` constructor.

        EXAMPLES::

            sage: QuadraticField(-1, 'I').specified_complex_embedding()
            Generic morphism:
              From: Number Field in I with defining polynomial x^2 + 1 with I = 1*I
              To:   Complex Lazy Field
              Defn: I -> 1*I

        ::

            sage: QuadraticField(3, 'a').specified_complex_embedding()
            Generic morphism:
              From: Number Field in a with defining polynomial x^2 - 3
                    with a = 1.732050807568878?
              To:   Real Lazy Field
              Defn: a -> 1.732050807568878?

        ::

            sage: CyclotomicField(13).specified_complex_embedding()
            Generic morphism:
              From: Cyclotomic Field of order 13 and degree 12
              To:   Complex Lazy Field
              Defn: zeta13 -> 0.885456025653210? + 0.464723172043769?*I

        Most fields don't implicitly have embeddings unless explicitly
        specified::

            sage: x = polygen(QQ, 'x')
            sage: NumberField(x^2 - 2, 'a').specified_complex_embedding() is None
            True
            sage: NumberField(x^3 - x + 5, 'a').specified_complex_embedding() is None
            True
            sage: NumberField(x^3 - x + 5, 'a', embedding=2).specified_complex_embedding()
            Generic morphism:
              From: Number Field in a with defining polynomial x^3 - x + 5
                    with a = -1.904160859134921?
              To:   Real Lazy Field
              Defn: a -> -1.904160859134921?
            sage: NumberField(x^3 - x + 5, 'a', embedding=CDF.0).specified_complex_embedding()
            Generic morphism:
              From: Number Field in a with defining polynomial x^3 - x + 5
                    with a = 0.952080429567461? + 1.311248044077123?*I
              To:   Complex Lazy Field
              Defn: a -> 0.952080429567461? + 1.311248044077123?*I

        This function only returns complex embeddings::

            sage: # needs sage.rings.padics
            sage: K.<a> = NumberField(x^2 - 2, embedding=Qp(7)(2).sqrt())
            sage: K.specified_complex_embedding() is None
            True
            sage: K.gen_embedding()
            3 + 7 + 2*7^2 + 6*7^3 + 7^4 + 2*7^5 + 7^6 + 2*7^7 + 4*7^8 + 6*7^9 + 6*7^10
             + 2*7^11 + 7^12 + 7^13 + 2*7^15 + 7^16 + 7^17 + 4*7^18 + 6*7^19 + O(7^20)
            sage: K.coerce_embedding()
            Generic morphism:
              From: Number Field in a with defining polynomial x^2 - 2
                    with a = 3 + 7 + 2*7^2 + 6*7^3 + 7^4 + 2*7^5 + 7^6 + 2*7^7 + 4*7^8
                              + 6*7^9 + 6*7^10 + 2*7^11 + 7^12 + 7^13 + 2*7^15 + 7^16
                              + 7^17 + 4*7^18 + 6*7^19 + O(7^20)
              To:   7-adic Field with capped relative precision 20
              Defn: a -> 3 + 7 + 2*7^2 + 6*7^3 + 7^4 + 2*7^5 + 7^6 + 2*7^7 + 4*7^8
                          + 6*7^9 + 6*7^10 + 2*7^11 + 7^12 + 7^13 + 2*7^15 + 7^16
                          + 7^17 + 4*7^18 + 6*7^19 + O(7^20)
        """
    @cached_method
    def gen_embedding(self):
        """
        If an embedding has been specified, return the image of the
        generator under that embedding. Otherwise return ``None``.

        EXAMPLES::

            sage: QuadraticField(-7, 'a').gen_embedding()
            2.645751311064591?*I
            sage: x = polygen(QQ, 'x')
            sage: NumberField(x^2 + 7, 'a').gen_embedding()  # None
        """
    def algebraic_closure(self):
        """
        Return the algebraic closure of ``self`` (which is ``QQbar``).

        EXAMPLES::

            sage: K.<i> = QuadraticField(-1)
            sage: K.algebraic_closure()
            Algebraic Field
            sage: x = polygen(QQ, 'x')
            sage: K.<a> = NumberField(x^3 - 2)
            sage: K.algebraic_closure()
            Algebraic Field
            sage: K = CyclotomicField(23)
            sage: K.algebraic_closure()
            Algebraic Field
        """
    @cached_method
    def conductor(self, check_abelian: bool = True):
        """
        Compute the conductor of the abelian field `K`.
        If ``check_abelian`` is set to ``False`` and the field is not an
        abelian extension of `\\QQ`, the output is not meaningful.

        INPUT:

        - ``check_abelian`` -- boolean (default: ``True``); check to see
          that this is an abelian extension of `\\QQ`

        OUTPUT: integer which is the conductor of the field

        EXAMPLES::

            sage: # needs sage.groups
            sage: K = CyclotomicField(27)
            sage: k = K.subfields(9)[0][0]
            sage: k.conductor()
            27
            sage: x = polygen(QQ, 'x')
            sage: K.<t> = NumberField(x^3 + x^2 - 2*x - 1)
            sage: K.conductor()
            7
            sage: K.<t> = NumberField(x^3 + x^2 - 36*x - 4)
            sage: K.conductor()
            109
            sage: K = CyclotomicField(48)
            sage: k = K.subfields(16)[0][0]
            sage: k.conductor()
            48
            sage: NumberField(x,'a').conductor()
            1
            sage: NumberField(x^8 - 8*x^6 + 19*x^4 - 12*x^2 + 1, 'a').conductor()
            40
            sage: NumberField(x^8 + 7*x^4 + 1, 'a').conductor()
            40
            sage: NumberField(x^8 - 40*x^6 + 500*x^4 - 2000*x^2 + 50, 'a').conductor()
            160

        ALGORITHM:

            For odd primes, it is easy to compute from the ramification
            index because the `p`-Sylow subgroup is cyclic.  For `p=2`, there
            are two choices for a given ramification index.  They can be
            distinguished by the parity of the exponent in the discriminant
            of a 2-adic completion.
        """
    def dirichlet_group(self):
        """
        Given a abelian field `K`, compute and return the
        set of all Dirichlet characters corresponding to the
        characters of the Galois group of `K/\\QQ`.

        The output is random if the field is not abelian.

        OUTPUT: list of Dirichlet characters

        EXAMPLES::

            sage: # needs sage.groups sage.modular
            sage: x = polygen(QQ, 'x')
            sage: K.<t> = NumberField(x^3 + x^2 - 36*x - 4)
            sage: K.conductor()
            109
            sage: K.dirichlet_group()  # optional - gap_package_polycyclic
            [Dirichlet character modulo 109 of conductor 1 mapping 6 |--> 1,
             Dirichlet character modulo 109 of conductor 109 mapping 6 |--> zeta3,
             Dirichlet character modulo 109 of conductor 109 mapping 6 |--> -zeta3 - 1]

            sage: # needs sage.modular
            sage: K = CyclotomicField(44)
            sage: L = K.subfields(5)[0][0]
            sage: X = L.dirichlet_group(); X  # optional - gap_package_polycyclic
            [Dirichlet character modulo 11 of conductor 1 mapping 2 |--> 1,
             Dirichlet character modulo 11 of conductor 11 mapping 2 |--> zeta5,
             Dirichlet character modulo 11 of conductor 11 mapping 2 |--> zeta5^2,
             Dirichlet character modulo 11 of conductor 11 mapping 2 |--> zeta5^3,
             Dirichlet character modulo 11 of conductor 11
               mapping 2 |--> -zeta5^3 - zeta5^2 - zeta5 - 1]
            sage: X[4]^2  # optional - gap_package_polycyclic
            Dirichlet character modulo 11 of conductor 11 mapping 2 |--> zeta5^3
            sage: X[4]^2 in X  # optional - gap_package_polycyclic
            True
        """
    def ideal(self, *gens, **kwds):
        """
        Return a fractional ideal of the field, except for the
        zero ideal, which is not a fractional ideal.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<i> = NumberField(x^2 + 1)
            sage: K.ideal(2)
            Fractional ideal (2)
            sage: K.ideal(2 + i)
            Fractional ideal (i + 2)
            sage: K.ideal(0)
            Ideal (0) of Number Field in i with defining polynomial x^2 + 1

        TESTS:

        Check that :issue:`25934` is fixed::

            sage: x = polygen(QQ)
            sage: K.<a> = NumberField(x^6 - x^5 - 5*x^4 + 4*x^3 + 6*x^2 - 3*x - 1)
            sage: K.ideal(1, 1)
            Fractional ideal (1)
        """
    def idealchinese(self, ideals, residues):
        """
        Return a solution of the Chinese Remainder Theorem problem
        for ideals in a number field.

        This is a wrapper around the pari function :pari:`idealchinese`.

        INPUT:

        - ``ideals`` -- list of ideals of the number field

        - ``residues`` -- list of elements of the number field

        OUTPUT:

        Return an element `b` of the number field such that
        `b \\equiv x_i \\bmod I_i` for all residues `x_i` and
        respective ideals `I_i`.

        .. SEEALSO::

            - :func:`crt`

        EXAMPLES:

        This is the example from the pari page on ``idealchinese``::

            sage: # needs sage.symbolic
            sage: K.<sqrt2> = NumberField(sqrt(2).minpoly())
            sage: ideals = [K.ideal(4), K.ideal(3)]
            sage: residues = [sqrt2, 1]
            sage: r = K.idealchinese(ideals, residues); r
            -3*sqrt2 + 4
            sage: all((r - a) in I for I, a in zip(ideals, residues))
            True

        The result may be non-integral if the results are non-integral::

            sage: # needs sage.symbolic
            sage: K.<sqrt2> = NumberField(sqrt(2).minpoly())
            sage: ideals = [K.ideal(4), K.ideal(21)]
            sage: residues = [1/sqrt2, 1]
            sage: r = K.idealchinese(ideals, residues); r
            -63/2*sqrt2 - 20
            sage: all(
            ....:     (r - a).valuation(P) >= k
            ....:     for I, a in zip(ideals, residues)
            ....:     for P, k in I.factor()
            ....: )
            True
        """
    def fractional_ideal(self, *gens, **kwds):
        """
        Return the ideal in `\\mathcal{O}_K` generated by ``gens``.

        This overrides the :class:`sage.rings.ring.Field` method to
        use the :class:`sage.rings.ring.Ring` one instead, since
        we are not concerned with ideals in a field but in its ring
        of integers.

        INPUT:

        - ``gens`` -- list of generators, or a number field ideal

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<a> = NumberField(x^3 - 2)
            sage: K.fractional_ideal([1/a])
            Fractional ideal (1/2*a^2)

        One can also input a number field ideal itself,
        or, more usefully, for a tower of number fields an ideal
        in one of the fields lower down the tower.

        ::

            sage: K.fractional_ideal(K.ideal(a))
            Fractional ideal (a)
            sage: L.<b> = K.extension(x^2 - 3, x^2 + 1)
            sage: M.<c> = L.extension(x^2 + 1)
            sage: L.ideal(K.ideal(2, a))
            Fractional ideal (-a)
            sage: M.ideal(K.ideal(2, a)) == M.ideal(a*(b - c)/2)
            True

        The zero ideal is not a fractional ideal!

        ::

            sage: K.fractional_ideal(0)
            Traceback (most recent call last):
            ...
            ValueError: gens must have a nonzero element (zero ideal is not a fractional ideal)
        """
    def ideals_of_bdd_norm(self, bound):
        """
        Return all integral ideals of bounded norm.

        INPUT:

        - ``bound`` -- positive integer

        OUTPUT: a dict of all integral ideals `I` such that Norm(`I`) `\\leq` ``bound``,
        keyed by norm.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<a> = NumberField(x^2 + 23)
            sage: d = K.ideals_of_bdd_norm(10)
            sage: for n in d:
            ....:     print(n)
            ....:     for I in sorted(d[n]):
            ....:         print(I)
                1
                Fractional ideal (1)
                2
                Fractional ideal (2, 1/2*a - 1/2)
                Fractional ideal (2, 1/2*a + 1/2)
                3
                Fractional ideal (3, 1/2*a - 1/2)
                Fractional ideal (3, 1/2*a + 1/2)
                4
                Fractional ideal (2)
                Fractional ideal (4, 1/2*a + 3/2)
                Fractional ideal (4, 1/2*a + 5/2)
                5
                6
                Fractional ideal (-1/2*a + 1/2)
                Fractional ideal (1/2*a + 1/2)
                Fractional ideal (6, 1/2*a + 5/2)
                Fractional ideal (6, 1/2*a + 7/2)
                7
                8
                Fractional ideal (4, a - 1)
                Fractional ideal (4, a + 1)
                Fractional ideal (-1/2*a - 3/2)
                Fractional ideal (1/2*a - 3/2)
                9
                Fractional ideal (3)
                Fractional ideal (9, 1/2*a + 7/2)
                Fractional ideal (9, 1/2*a + 11/2)
                10
            sage: [[I.norm() for I in sorted(d[n])] for n in d]
                [[1], [2, 2], [3, 3], [4, 4, 4], [], [6, 6, 6, 6], [], [8, 8, 8, 8], [9, 9, 9], []]
        """
    def primes_above(self, x, degree=None):
        """
        Return prime ideals of ``self`` lying over `x`.

        INPUT:

        - ``x`` -- usually an element or ideal of ``self``. It should be such
          that ``self.ideal(x)`` is sensible. This excludes `x=0`.

        - ``degree`` -- (default: ``None``) ``None`` or an integer.
          If ``None``, find all primes above `x` of any degree. If an
          integer, find all primes above `x` such that the resulting
          residue field has exactly this degree.

        OUTPUT: list of prime ideals of ``self`` lying over `x`. If ``degree``
        is specified and no such ideal exists, returns the empty list.
        The output is sorted by residue degree first, then by
        underlying prime (or equivalently, by norm).

        If there is a tie, the exact ordering should be assumed to be random.
        See the remark in :meth:`NumberFieldIdeal._richcmp_`.

        EXAMPLES::

            sage: x = ZZ['x'].gen()
            sage: F.<t> = NumberField(x^3 - 2)

        ::

            sage: P2s = F.primes_above(2)
            sage: P2s  # random
            [Fractional ideal (-t)]
            sage: all(2 in P2 for P2 in P2s)
            True
            sage: all(P2.is_prime() for P2 in P2s)
            True
            sage: [ P2.norm() for P2 in P2s ]
            [2]

        ::

            sage: P3s = F.primes_above(3)
            sage: P3s # random
            [Fractional ideal (t + 1)]
            sage: all(3 in P3 for P3 in P3s)
            True
            sage: all(P3.is_prime() for P3 in P3s)
            True
            sage: [ P3.norm() for P3 in P3s ]
            [3]

        The ideal `(3)` is totally ramified in `F`, so there is no degree 2
        prime above 3::

            sage: F.primes_above(3, degree=2)
            []
            sage: [ id.residue_class_degree() for id, _ in F.ideal(3).factor() ]
            [1]

        Asking for a specific degree works::

            sage: P5_1s = F.primes_above(5, degree=1)
            sage: P5_1s # random
            [Fractional ideal (-t^2 - 1)]
            sage: P5_1 = P5_1s[0]; P5_1.residue_class_degree()
            1

        ::

            sage: P5_2s = F.primes_above(5, degree=2)
            sage: P5_2s # random
            [Fractional ideal (t^2 - 2*t - 1)]
            sage: P5_2 = P5_2s[0]; P5_2.residue_class_degree()
            2

        Works in relative extensions too::

            sage: PQ.<X> = QQ[]
            sage: F.<a, b> = NumberField([X^2 - 2, X^2 - 3])
            sage: PF.<Y> = F[]
            sage: K.<c> = F.extension(Y^2 - (1 + a)*(a + b)*a*b)
            sage: I = F.ideal(a + 2*b)
            sage: P, Q = K.primes_above(I)
            sage: K.ideal(I) == P^4*Q
            True
            sage: K.primes_above(I, degree=1) == [P]
            True
            sage: K.primes_above(I, degree=4) == [Q]
            True

        It doesn't make sense to factor the ideal `(0)`, so this raises an error::

            sage: F.prime_above(0)
            Traceback (most recent call last):
            ...
            AttributeError: 'NumberFieldIdeal' object has no attribute 'prime_factors'...
        """
    def prime_above(self, x, degree=None):
        """
        Return a prime ideal of ``self`` lying over `x`.

        INPUT:

        - ``x`` -- usually an element or ideal of ``self``. It should be such
          that ``self.ideal(x)`` is sensible. This excludes `x=0`.

        - ``degree`` -- (default: ``None``) ``None`` or an integer.
          If one, find a prime above `x` of any degree. If an integer, find a
          prime above `x` such that the resulting residue field has exactly
          this degree.

        OUTPUT: a prime ideal of ``self`` lying over `x`. If ``degree`` is specified
        and no such ideal exists, raises a :exc:`ValueError`.

        EXAMPLES::

            sage: x = ZZ['x'].gen()
            sage: F.<t> = NumberField(x^3 - 2)

        ::

            sage: P2 = F.prime_above(2)
            sage: P2 # random
            Fractional ideal (-t)
            sage: 2 in P2
            True
            sage: P2.is_prime()
            True
            sage: P2.norm()
            2

        ::

            sage: P3 = F.prime_above(3)
            sage: P3 # random
            Fractional ideal (t + 1)
            sage: 3 in P3
            True
            sage: P3.is_prime()
            True
            sage: P3.norm()
            3

        The ideal `(3)` is totally ramified in `F`, so there is no degree 2
        prime above `3`::

            sage: F.prime_above(3, degree=2)
            Traceback (most recent call last):
            ...
            ValueError: No prime of degree 2 above Fractional ideal (3)
            sage: [ id.residue_class_degree() for id, _ in F.ideal(3).factor() ]
            [1]

        Asking for a specific degree works::

            sage: P5_1 = F.prime_above(5, degree=1)
            sage: P5_1 # random
            Fractional ideal (-t^2 - 1)
            sage: P5_1.residue_class_degree()
            1

        ::

            sage: P5_2 = F.prime_above(5, degree=2)
            sage: P5_2 # random
            Fractional ideal (t^2 - 2*t - 1)
            sage: P5_2.residue_class_degree()
            2

        Relative number fields are ok::

            sage: G = F.extension(x^2 - 11, 'b')
            sage: G.prime_above(7)
            Fractional ideal (b + 2)

        It doesn't make sense to factor the ideal `(0)`::

            sage: F.prime_above(0)
            Traceback (most recent call last):
            ...
            AttributeError: 'NumberFieldIdeal' object has no attribute 'prime_factors'...
        """
    def primes_of_bounded_norm(self, B):
        """
        Return a sorted list of all prime ideals with norm at most `B`.

        INPUT:

        - ``B`` -- positive integer or real; upper bound on the norms of the
          primes generated

        OUTPUT:

        A list of all prime ideals of this number field of norm at
        most `B`, sorted by norm.  Primes of the same norm are sorted
        using the comparison function for ideals, which is based on
        the Hermite Normal Form.

        .. NOTE::

            See also :meth:`primes_of_bounded_norm_iter` for an
            iterator version of this, but note that the iterator sorts
            the primes in order of underlying rational prime, not by
            norm.

        EXAMPLES::

            sage: K.<i> = QuadraticField(-1)
            sage: K.primes_of_bounded_norm(10)
            [Fractional ideal (i - 1),
             Fractional ideal (2*i - 1),
             Fractional ideal (-2*i - 1),
             Fractional ideal (3)]
            sage: K.primes_of_bounded_norm(1)
            []
            sage: K.primes_of_bounded_norm(1.1)
            []
            sage: x = polygen(QQ, 'x')
            sage: K.<a> = NumberField(x^3 - 2)
            sage: P = K.primes_of_bounded_norm(30)
            sage: P
            [Fractional ideal (a),
             Fractional ideal (a + 1),
             Fractional ideal (a^2 + 1),
             Fractional ideal (a^2 + a - 1),
             Fractional ideal (2*a + 1),
             Fractional ideal (2*a^2 + a + 1),
             Fractional ideal (a^2 - 2*a - 1),
             Fractional ideal (a + 3)]
            sage: [p.norm() for p in P]
            [2, 3, 5, 11, 17, 23, 25, 29]
        """
    def primes_of_bounded_norm_iter(self, B) -> Generator[Incomplete]:
        """
        Iterator yielding all prime ideals with norm at most `B`.

        INPUT:

        - ``B`` -- positive integer or real; upper bound on the norms of the
          primes generated

        OUTPUT:

        An iterator over all prime ideals of this number field of norm
        at most `B`.

        .. NOTE::

            The output is not sorted by norm, but by size of the
            underlying rational prime.

        EXAMPLES::

            sage: K.<i> = QuadraticField(-1)
            sage: it = K.primes_of_bounded_norm_iter(10)
            sage: list(it)
            [Fractional ideal (i - 1),
             Fractional ideal (3),
             Fractional ideal (2*i - 1),
             Fractional ideal (-2*i - 1)]
            sage: list(K.primes_of_bounded_norm_iter(1))
            []
        """
    def primes_of_degree_one_iter(self, num_integer_primes: int = 10000, max_iterations: int = 100):
        """
        Return an iterator yielding prime ideals of absolute degree one and
        small norm.

        .. warning::

           It is possible that there are no primes of `K` of
           absolute degree one of small prime norm, and it possible
           that this algorithm will not find any primes of small norm.

           See module :mod:`sage.rings.number_field.small_primes_of_degree_one`
           for details.

        INPUT:

        - ``num_integer_primes`` -- (default: 10000) an
          integer. We try to find primes of absolute norm no greater than the
          ``num_integer_primes``-th prime number. For example, if
          ``num_integer_primes`` is 2, the largest norm found will be 3, since
          the second prime is 3.

        - ``max_iterations`` -- (default: 100) an integer. We
          test ``max_iterations`` integers to find small primes before raising
          :class:`StopIteration`.

        EXAMPLES::

            sage: K.<z> = CyclotomicField(10)
            sage: it = K.primes_of_degree_one_iter()
            sage: Ps = [ next(it) for i in range(3) ]
            sage: Ps # random
            [Fractional ideal (z^3 + z + 1),
             Fractional ideal (3*z^3 - z^2 + z - 1),
             Fractional ideal (2*z^3 - 3*z^2 + z - 2)]
            sage: [P.norm() for P in Ps] # random
            [11, 31, 41]
            sage: [P.residue_class_degree() for P in Ps]
            [1, 1, 1]
        """
    def primes_of_degree_one_list(self, n, num_integer_primes: int = 10000, max_iterations: int = 100):
        """
        Return a list of `n` prime ideals of absolute degree one and small
        norm.

        .. warning::

           It is possible that there are no primes of `K` of
           absolute degree one of small prime norm, and it is possible
           that this algorithm will not find any primes of small norm.

           See module :mod:`sage.rings.number_field.small_primes_of_degree_one`
           for details.

        INPUT:

        - ``num_integer_primes`` -- integer (default: 10000). We try to find
          primes of absolute norm no greater than the ``num_integer_primes``-th
          prime number. For example, if ``num_integer_primes`` is 2, the
          largest norm found will be 3, since the second prime is 3.

        - ``max_iterations`` -- integer (default: 100). We test ``max_iterations``
          integers to find small primes before raising :class:`StopIteration`.

        EXAMPLES::

            sage: K.<z> = CyclotomicField(10)
            sage: Ps = K.primes_of_degree_one_list(3)
            sage: Ps  # random output
            [Fractional ideal (-z^3 - z^2 + 1),
             Fractional ideal (2*z^3 - 2*z^2 + 2*z - 3),
             Fractional ideal (2*z^3 - 3*z^2 + z - 2)]
            sage: [P.norm() for P in Ps]
            [11, 31, 41]
            sage: [P.residue_class_degree() for P in Ps]
            [1, 1, 1]
        """
    def completely_split_primes(self, B: int = 200):
        """
        Return a list of rational primes which split completely in the number field `K`.

        INPUT:

        - ``B`` -- positive integer bound (default: 200)

        OUTPUT: list of all primes `p < B` which split completely in ``K``

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<xi> = NumberField(x^3 - 3*x + 1)
            sage: K.completely_split_primes(100)
            [17, 19, 37, 53, 71, 73, 89]
        """
    def pari_polynomial(self, name: str = 'x'):
        """
        Return the PARI polynomial corresponding to this number field.

        INPUT:

        - ``name`` -- variable name (default: ``'x'``)

        OUTPUT:

        A monic polynomial with integral coefficients (PARI ``t_POL``)
        defining the PARI number field corresponding to ``self``.

        .. WARNING::

            This is *not* the same as simply converting the defining
            polynomial to PARI.

        EXAMPLES::

            sage: y = polygen(QQ)
            sage: k.<a> = NumberField(y^2 - 3/2*y + 5/3)
            sage: k.pari_polynomial()
            x^2 - 9*x + 60
            sage: k.polynomial().__pari__()
            x^2 - 3/2*x + 5/3
            sage: k.pari_polynomial('a')
            a^2 - 9*a + 60

        Some examples with relative number fields::

            sage: x = polygen(ZZ, 'x')
            sage: k.<a, c> = NumberField([x^2 + 3, x^2 + 1])
            sage: k.pari_polynomial()
            x^4 + 8*x^2 + 4
            sage: k.pari_polynomial('a')
            a^4 + 8*a^2 + 4
            sage: k.absolute_polynomial()
            x^4 + 8*x^2 + 4
            sage: k.relative_polynomial()
            x^2 + 3

            sage: k.<a, c> = NumberField([x^2 + 1/3, x^2 + 1/4])
            sage: k.pari_polynomial()
            x^4 - x^2 + 1
            sage: k.absolute_polynomial()
            x^4 - x^2 + 1

        This fails with arguments which are not a valid PARI variable name::

            sage: k = QuadraticField(-1)
            sage: k.pari_polynomial('I')
            Traceback (most recent call last):
            ...
            PariError: I already exists with incompatible valence
            sage: k.pari_polynomial('i')
            i^2 + 1
            sage: k.pari_polynomial('theta')
            Traceback (most recent call last):
            ...
            PariError: theta already exists with incompatible valence
        """
    def pari_nf(self, important: bool = True):
        """
        Return the PARI number field corresponding to this field.

        INPUT:

        - ``important`` -- boolean (default: ``True``); if ``False``,
          raise a :exc:`RuntimeError` if we need to do a difficult
          discriminant factorization.  This is useful when an integral
          basis is not strictly required, such as for factoring
          polynomials over this number field.

        OUTPUT:

        The PARI number field obtained by calling the PARI function
        :pari:`nfinit` with ``self.pari_polynomial('y')`` as argument.

        .. NOTE::

            This method has the same effect as ``pari(self)``.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: k.<a> = NumberField(x^4 - 3*x + 7); k
            Number Field in a with defining polynomial x^4 - 3*x + 7
            sage: k.pari_nf()[:4]
            [y^4 - 3*y + 7, [0, 2], 85621, 1]
            sage: pari(k)[:4]
            [y^4 - 3*y + 7, [0, 2], 85621, 1]

        ::

            sage: k.<a> = NumberField(x^4 - 3/2*x + 5/3); k
            Number Field in a with defining polynomial x^4 - 3/2*x + 5/3
            sage: k.pari_nf()
            [y^4 - 324*y + 2160, [0, 2], 48918708, 216, ..., [36, 36*y, y^3 + 6*y^2 - 252, -6*y^2], [1, 0, 0, 252; 0, 1, 0, 0; 0, 0, 0, 36; 0, 0, -6, 36], [1, 0, 0, 0, 0, 0, -18, -42, 0, -18, -46, 60, 0, -42, 60, -60; 0, 1, 0, 0, 1, 0, 2, 0, 0, 2, -11, 1, 0, 0, 1, 9; 0, 0, 1, 0, 0, 0, 6, -6, 1, 6, -5, 0, 0, -6, 0, 0; 0, 0, 0, 1, 0, -6, 6, -6, 0, 6, 1, 2, 1, -6, 2, 0]]
            sage: pari(k)
            [y^4 - 324*y + 2160, [0, 2], 48918708, 216, ...]
            sage: gp(k)
            [y^4 - 324*y + 2160, [0, 2], 48918708, 216, ...]

        With ``important=False``, we simply bail out if we cannot
        easily factor the discriminant::

            sage: p = next_prime(10^40); q = next_prime(10^41)
            sage: K.<a> = NumberField(x^2 - p*q)
            sage: K.pari_nf(important=False)
            Traceback (most recent call last):
            ...
            RuntimeError: Unable to factor discriminant with trial division

        Next, we illustrate the ``maximize_at_primes`` and ``assume_disc_small``
        parameters of the :class:`NumberField` constructor. The following would take
        a very long time without the ``maximize_at_primes`` option::

            sage: K.<a> = NumberField(x^2 - p*q, maximize_at_primes=[p])
            sage: K.pari_nf()
            [y^2 - 100000000000000000000...]

        Since the discriminant is square-free, this also works::

            sage: K.<a> = NumberField(x^2 - p*q, assume_disc_small=True)
            sage: K.pari_nf()
            [y^2 - 100000000000000000000...]
        """
    def pari_zk(self):
        """
        Integral basis of the PARI number field corresponding to this field.

        This is the same as ``pari_nf().getattr('zk')``, but much faster.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: k.<a> = NumberField(x^3 - 17)
            sage: k.pari_zk()
            [1, 1/3*y^2 - 1/3*y + 1/3, y]
            sage: k.pari_nf().getattr('zk')
            [1, 1/3*y^2 - 1/3*y + 1/3, y]
        """
    def __pari__(self):
        """
        Return the PARI number field corresponding to this field.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: k = NumberField(x^2 + x + 1, 'a')
            sage: k.__pari__()
            [y^2 + y + 1, [0, 1], -3, 1, ... [1, y], [1, 0; 0, 1], [1, 0, 0, -1; 0, 1, 1, -1]]
            sage: pari(k)
            [y^2 + y + 1, [0, 1], -3, 1, ...[1, y], [1, 0; 0, 1], [1, 0, 0, -1; 0, 1, 1, -1]]
        """
    def pari_bnf(self, proof=None, units: bool = True):
        """
        PARI big number field corresponding to this field.

        INPUT:

        - ``proof`` -- if ``False``, assume GRH; if ``True``, run PARI's
          :pari:`bnfcertify` to make sure that the results are correct

        - ``units`` -- (default: ``True) if ``True``, insist on having
          fundamental units; if ``False``, the units may or may not be computed

        OUTPUT: the PARI ``bnf`` structure of this number field

        .. warning::

           Even with ``proof=True``, I wouldn't trust this to mean
           that everything computed involving this number field is
           actually correct.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: k.<a> = NumberField(x^2 + 1); k
            Number Field in a with defining polynomial x^2 + 1
            sage: len(k.pari_bnf())
            10
            sage: k.pari_bnf()[:4]
            [[;], matrix(0,3), [;], ...]
            sage: len(k.pari_nf())
            9
            sage: k.<a> = NumberField(x^7 + 7); k
            Number Field in a with defining polynomial x^7 + 7
            sage: dummy = k.pari_bnf(proof=True)
        """
    def pari_rnfnorm_data(self, L, proof: bool = True):
        """
        Return the PARI :pari:`rnfisnorminit` data corresponding to the
        extension `L` / ``self``.

        EXAMPLES::

            sage: x = polygen(QQ)
            sage: K = NumberField(x^2 - 2, 'alpha')
            sage: L = K.extension(x^2 + 5, 'gamma')
            sage: ls = K.pari_rnfnorm_data(L) ; len(ls)
            8

            sage: K.<a> = NumberField(x^2 + x + 1)
            sage: P.<X> = K[]
            sage: L.<b> = NumberField(X^3 + a)
            sage: ls = K.pari_rnfnorm_data(L); len(ls)
            8
        """
    def characteristic(self):
        """
        Return the characteristic of this number field, which is of course
        0.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: k.<a> = NumberField(x^99 + 2); k
            Number Field in a with defining polynomial x^99 + 2
            sage: k.characteristic()
            0
        """
    def class_group(self, proof=None, names: str = 'c'):
        """
        Return the class group of the ring of integers of this number
        field.

        INPUT:

        - ``proof`` -- if ``True`` (default), then compute the class group
          provably correctly; call :func:`number_field_proof` to change this
          default globally

        - ``names`` -- names of the generators of this class group

        OUTPUT: the class group of this number field

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<a> = NumberField(x^2 + 23)
            sage: G = K.class_group(); G
            Class group of order 3 with structure C3 of
             Number Field in a with defining polynomial x^2 + 23
            sage: G.0
            Fractional ideal class (2, 1/2*a - 1/2)
            sage: G.gens()
            (Fractional ideal class (2, 1/2*a - 1/2),)

        ::

            sage: G.number_field()
            Number Field in a with defining polynomial x^2 + 23
            sage: G is K.class_group()
            True
            sage: G is K.class_group(proof=False)
            False
            sage: G.gens()
            (Fractional ideal class (2, 1/2*a - 1/2),)

        There can be multiple generators::

            sage: k.<a> = NumberField(x^2 + 20072)
            sage: G = k.class_group(); G
            Class group of order 76 with structure C38 x C2 of
             Number Field in a with defining polynomial x^2 + 20072
            sage: G.0 # random
            Fractional ideal class (41, a + 10)
            sage: G.0^38
            Trivial principal fractional ideal class
            sage: G.1 # random
            Fractional ideal class (2, -1/2*a)
            sage: G.1^2
            Trivial principal fractional ideal class

        Class groups of Hecke polynomials tend to be very small::

            sage: # needs sage.modular
            sage: f = ModularForms(97, 2).T(2).charpoly()
            sage: f.factor()
            (x - 3) * (x^3 + 4*x^2 + 3*x - 1) * (x^4 - 3*x^3 - x^2 + 6*x - 1)
            sage: [NumberField(g,'a').class_group().order() for g,_ in f.factor()]
            [1, 1, 1]

        .. NOTE::

            Unlike in PARI/GP, class group computations *in Sage* do *not* by
            default assume the Generalized Riemann Hypothesis. To do class
            groups computations not provably correctly you must often pass the
            flag ``proof=False`` to functions or call the function
            ``proof.number_field(False)``. It can easily take 1000s of times
            longer to do computations with ``proof=True`` (the default).
        """
    def class_number(self, proof=None):
        """
        Return the class number of this number field, as an integer.

        INPUT:

        - ``proof`` -- boolean (default: ``True``, unless you called
          ``number_field_proof``)

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: NumberField(x^2 + 23, 'a').class_number()
            3
            sage: NumberField(x^2 + 163, 'a').class_number()
            1
            sage: NumberField(x^3 + x^2 + 997*x + 1, 'a').class_number(proof=False)
            1539
        """
    def S_class_group(self, S, proof=None, names: str = 'c'):
        """
        Return the S-class group of this number field over its base field.

        INPUT:

        - ``S`` -- set of primes of the base field

        - ``proof`` -- if ``False``, assume the GRH in computing the class
          group. Default is ``True``. Call ``number_field_proof`` to change
          this default globally.

        - ``names`` -- names of the generators of this class group

        OUTPUT: the S-class group of this number field

        EXAMPLES:

        A well known example::

            sage: K.<a> = QuadraticField(-5)
            sage: K.S_class_group([])
            S-class group of order 2 with structure C2 of Number Field in a
             with defining polynomial x^2 + 5 with a = 2.236067977499790?*I

        When we include the prime `(2, a+1)`, the S-class group becomes
        trivial::

            sage: K.S_class_group([K.ideal(2, a + 1)])
            S-class group of order 1 of Number Field in a
             with defining polynomial x^2 + 5 with a = 2.236067977499790?*I

        TESTS::

            sage: K.<a> = QuadraticField(-14)
            sage: I = K.ideal(2, a)
            sage: S = (I,)
            sage: CS = K.S_class_group(S); CS
            S-class group of order 2 with structure C2 of Number Field in a
             with defining polynomial x^2 + 14 with a = 3.741657386773942?*I
            sage: T = tuple()
            sage: CT = K.S_class_group(T); CT
            S-class group of order 4 with structure C4 of Number Field in a
             with defining polynomial x^2 + 14 with a = 3.741657386773942?*I
            sage: K.class_group()
            Class group of order 4 with structure C4 of Number Field in a
             with defining polynomial x^2 + 14 with a = 3.741657386773942?*I
        """
    def S_units(self, S, proof: bool = True):
        """
        Return a list of generators of the S-units.

        INPUT:

        - ``S`` -- set of primes of the base field

        - ``proof`` -- if ``False``, assume the GRH in computing the class group

        OUTPUT: list of generators of the unit group

        .. NOTE::

            For more functionality see the function :func:`S_unit_group`.

        EXAMPLES::

            sage: K.<a> = QuadraticField(-3)
            sage: K.unit_group()
            Unit group with structure C6 of Number Field in a
             with defining polynomial x^2 + 3 with a = 1.732050807568878?*I
            sage: K.S_units([])  # random
            [1/2*a + 1/2]
            sage: K.S_units([])[0].multiplicative_order()
            6

        An example in a relative extension (see :issue:`8722`)::

            sage: x = polygen(QQ, 'x')
            sage: L.<a,b> = NumberField([x^2 + 1, x^2 - 5])
            sage: p = L.ideal((-1/2*b - 1/2)*a + 1/2*b - 1/2)
            sage: W = L.S_units([p]); [x.norm() for x in W]
            [9, 1, 1]

        Our generators should have the correct parent (:issue:`9367`)::

            sage: _.<x> = QQ[]
            sage: L.<alpha> = NumberField(x^3 + x + 1)
            sage: p = L.S_units([ L.ideal(7) ])
            sage: p[0].parent()
            Number Field in alpha with defining polynomial x^3 + x + 1

        TESTS:

        This checks that the multiple entries issue at :issue:`9341` is fixed::

            sage: _.<t> = QQ[]
            sage: K.<T> = NumberField(t - 1)
            sage: I = K.ideal(2)
            sage: K.S_units([I])
            [2, -1]
            sage: J = K.ideal(-2)
            sage: K.S_units([I, J, I])
            [2, -1]
        """
    def selmer_generators(self, S, m, proof: bool = True, orders: bool = False):
        """
        Compute generators of the group `K(S,m)`.

        INPUT:

        - ``S`` -- set of primes of ``self``

        - ``m`` -- positive integer

        - ``proof`` -- if ``False``, assume the GRH in computing the class group

        - ``orders`` -- boolean (default: ``False``); if ``True``, output two
          lists, the generators and their orders

        OUTPUT:

        A list of generators of `K(S,m)`, and (optionally) their
        orders as elements of `K^\\times/(K^\\times)^m`.  This is the
        subgroup of `K^\\times/(K^\\times)^m` consisting of elements `a`
        such that the valuation of `a` is divisible by `m` at all
        primes not in `S`.  It fits in an exact sequence between the
        units modulo `m`-th powers and the `m`-torsion in the
        `S`-class group:

        .. MATH::

            1                                    \\longrightarrow
            O_{K,S}^\\times / (O_{K,S}^\\times)^m  \\longrightarrow
            K(S,m)                               \\longrightarrow
            \\operatorname{Cl}_{K,S}[m]           \\longrightarrow
            0.

        The group `K(S,m)` contains the subgroup of those `a` such
        that `K(\\sqrt[m]{a})/K` is unramified at all primes of `K`
        outside of `S`, but may contain it properly when not all
        primes dividing `m` are in `S`.

        .. SEEALSO::

            :meth:`NumberField_generic.selmer_space`, which gives
            additional output when `m=p` is prime: as well as generators,
            it gives an abstract vector space over `\\GF{p}` isomorphic to
            `K(S,p)` and maps implementing the isomorphism between this
            space and `K(S,p)` as a subgroup of `K^*/(K^*)^p`.

        EXAMPLES::

            sage: K.<a> = QuadraticField(-5)
            sage: K.selmer_generators((), 2)
            [-1, 2]

        The previous example shows that the group generated by the
        output may be strictly larger than the group of
        elements giving extensions unramified outside `S`, since that
        has order just 2, generated by `-1`::

            sage: K.class_number()
            2
            sage: K.hilbert_class_field('b')
            Number Field in b with defining polynomial x^2 + 1 over its base field

        When `m` is prime all the orders are equal to `m`, but in general they are only divisors of `m`::

            sage: K.<a> = QuadraticField(-5)
            sage: P2 = K.ideal(2, -a + 1)
            sage: P3 = K.ideal(3, a + 1)
            sage: K.selmer_generators((), 2, orders=True)
            ([-1, 2], [2, 2])
            sage: K.selmer_generators((), 4, orders=True)
            ([-1, 4], [2, 2])
            sage: K.selmer_generators([P2], 2)
            [2, -1]
            sage: K.selmer_generators((P2,P3), 4)
            [2, -a - 1, -1]
            sage: K.selmer_generators((P2,P3), 4, orders=True)
            ([2, -a - 1, -1], [4, 4, 2])
            sage: K.selmer_generators([P2], 3)
            [2]
            sage: K.selmer_generators([P2, P3], 3)
            [2, -a - 1]
            sage: K.selmer_generators([P2, P3, K.ideal(a)], 3)  # random signs
            [2, a + 1, a]

        Example over `\\QQ` (as a number field)::

            sage: K.<a> = NumberField(polygen(QQ))
            sage: K.selmer_generators([],5)
            []
            sage: K.selmer_generators([K.prime_above(p) for p in [2,3,5]],2)
            [2, 3, 5, -1]
            sage: K.selmer_generators([K.prime_above(p) for p in [2,3,5]],6, orders=True)
            ([2, 3, 5, -1], [6, 6, 6, 2])

        TESTS::

            sage: K.<a> = QuadraticField(-5)
            sage: P2 = K.ideal(2, -a + 1)
            sage: P3 = K.ideal(3, a + 1)
            sage: P5 = K.ideal(a)
            sage: S = K.selmer_generators([P2, P3, P5], 3)
            sage: S in ([2, a + 1, a], [2, a + 1, -a], [2, -a - 1, a], [2, -a - 1, -a]) or S
            True

        Verify that :issue:`14489` is fixed;
        the representation depends on the PARI version::

            sage: x = polygen(QQ, 'x')
            sage: K.<a> = NumberField(x^3 - 381 * x + 127)
            sage: gens = K.selmer_generators(K.primes_above(13), 2)
            sage: len(gens) == 8
            True
            sage: gens[:5]
            [2/13*a^2 + 1/13*a - 677/13,
             1/13*a^2 + 7/13*a - 332/13,
             -1/13*a^2 + 6/13*a + 345/13,
             -1,
             1/13*a^2 - 19/13*a - 7/13]
            sage: gens[5] in (1/13*a^2 - 19/13*a - 7/13, 1/13*a^2 + 20/13*a - 7/13)
            True
            sage: gens[6] in (-1/13*a^2 + 45/13*a - 97/13, 1/13*a^2 - 45/13*a + 97/13)
            True
            sage: gens[7] in (2/13*a^2 + 40/13*a - 27/13, -2/13*a^2 - 40/13*a + 27/13)
            True

        Verify that :issue:`16708` is fixed::

            sage: K.<a> = QuadraticField(-5)
            sage: p = K.primes_above(2)[0]
            sage: S = K.selmer_generators((), 4)
            sage: all(4.divides(x.valuation(p)) for x in S)
            True
        """
    def selmer_group_iterator(self, S, m, proof: bool = True) -> Generator[Incomplete]:
        """
        Return an iterator through elements of the finite group `K(S,m)`.

        INPUT:

        - ``S`` -- set of primes of ``self``

        - ``m`` -- positive integer

        - ``proof`` -- if ``False``, assume the GRH in computing the class group

        OUTPUT:

        An iterator yielding the distinct elements of `K(S,m)`.  See
        the docstring for :meth:`NumberField_generic.selmer_generators` for
        more information.

        EXAMPLES::

            sage: K.<a> = QuadraticField(-5)
            sage: list(K.selmer_group_iterator((), 2))
            [1, 2, -1, -2]
            sage: list(K.selmer_group_iterator((), 4))
            [1, 4, -1, -4]
            sage: list(K.selmer_group_iterator([K.ideal(2, -a + 1)], 2))
            [1, -1, 2, -2]
            sage: list(K.selmer_group_iterator([K.ideal(2, -a + 1), K.ideal(3, a + 1)], 2))
            [1, -1, -a - 1, a + 1, 2, -2, -2*a - 2, 2*a + 2]

        Examples over `\\QQ` (as a number field)::

            sage: K.<a> = NumberField(polygen(QQ))
            sage: list(K.selmer_group_iterator([], 5))
            [1]
            sage: list(K.selmer_group_iterator([], 4))
            [1, -1]
            sage: list(K.selmer_group_iterator([K.prime_above(p) for p in [11,13]],2))
            [1, -1, 13, -13, 11, -11, 143, -143]
        """
    def selmer_space(self, S, p, proof=None):
        """
        Compute the group `K(S,p)` as a vector space with maps to and from `K^*`.

        INPUT:

        - ``S`` -- set of primes ideals of ``self``

        - ``p`` -- a prime number

        - ``proof`` -- if ``False``, assume the GRH in computing the class group

        OUTPUT:

        (tuple) ``KSp``, ``KSp_gens``, ``from_KSp``, ``to_KSp`` where

        - ``KSp`` is an abstract vector space over `GF(p)` isomorphic to `K(S,p)`;

        - ``KSp_gens`` is a list of elements of `K^*` generating `K(S,p)`;

        - ``from_KSp`` is a function from ``KSp`` to `K^*`
          implementing the isomorphism from the abstract `K(S,p)` to
          `K(S,p)` as a subgroup of `K^*/(K^*)^p`;

        - ``to_KSP`` is a partial function from `K^*` to ``KSp``,
          defined on elements `a` whose image in `K^*/(K^*)^p` lies in
          `K(S,p)`, mapping them via the inverse isomorphism to the
          abstract vector space ``KSp``.

        The group `K(S,p)` is the finite subgroup of `K^*/(K^*)^p`
        consisting of elements whose valuation at all primes not in
        `S` is a multiple of `p`.  It contains the subgroup of those
        `a\\in K^*` such that `K(\\sqrt[p]{a})/K` is unramified at all
        primes of `K` outside of `S`, but may contain it properly when
        not all primes dividing `p` are in `S`.

        EXAMPLES:

        A real quadratic field with class number 2, where the fundamental
        unit is a generator, and the class group provides another
        generator when `p=2`::

            sage: K.<a> = QuadraticField(-5)
            sage: K.class_number()
            2
            sage: P2 = K.ideal(2, -a + 1)
            sage: P3 = K.ideal(3, a + 1)
            sage: P5 = K.ideal(a)
            sage: KS2, gens, fromKS2, toKS2 = K.selmer_space([P2, P3, P5], 2)
            sage: KS2
            Vector space of dimension 4 over Finite Field of size 2
            sage: gens
            [a + 1, a, 2, -1]

        Each generator must have even valuation at primes not in `S`::

            sage: [K.ideal(g).factor() for g in gens]
            [(Fractional ideal (2, a + 1)) * (Fractional ideal (3, a + 1)),
             Fractional ideal (-a), (Fractional ideal (2, a + 1))^2, 1]

            sage: toKS2(10)
            (0, 0, 1, 1)
            sage: fromKS2([0,0,1,1])
            -2
            sage: K(10/(-2)).is_square()
            True

            sage: KS3, gens, fromKS3, toKS3 = K.selmer_space([P2, P3, P5], 3)
            sage: KS3
            Vector space of dimension 3 over Finite Field of size 3
            sage: gens
            [1/2, 1/4*a + 1/4, a]

        An example to show that the group `K(S,2)` may be strictly
        larger than the group of elements giving extensions unramified
        outside `S`.  In this case, with `K` of class number `2` and
        `S` empty, there is only one quadratic extension of `K`
        unramified outside `S`, the Hilbert Class Field
        `K(\\sqrt{-1})`::

            sage: K.<a> = QuadraticField(-5)
            sage: KS2, gens, fromKS2, toKS2 = K.selmer_space([], 2)
            sage: KS2
            Vector space of dimension 2 over Finite Field of size 2
            sage: gens
            [2, -1]
            sage: x = polygen(ZZ, 'x')
            sage: for v in KS2:
            ....:     if not v:
            ....:         continue
            ....:     a = fromKS2(v)
            ....:     print((a, K.extension(x^2 - a, 'roota').relative_discriminant().factor()))
            (2, (Fractional ideal (2, a + 1))^4)
            (-1, 1)
            (-2, (Fractional ideal (2, a + 1))^4)

            sage: K.hilbert_class_field('b')
            Number Field in b with defining polynomial x^2 + 1 over its base field
        """
    def composite_fields(self, other, names=None, both_maps: bool = False, preserve_embedding: bool = True):
        """
        Return the possible composite number fields formed from
        ``self`` and ``other``.

        INPUT:

        - ``other`` -- number field

        - ``names`` -- generator name for composite fields

        - ``both_maps`` -- boolean (default: ``False``)

        - ``preserve_embedding`` -- boolean (default: ``True``)

        OUTPUT: list of the composite fields, possibly with maps

        If ``both_maps`` is ``True``, the list consists of quadruples
        ``(F, self_into_F, other_into_F, k)`` such that
        ``self_into_F`` is an embedding of ``self`` in ``F``,
        ``other_into_F`` is an embedding of in ``F``, and ``k`` is one
        of the following:

        - an integer such that ``F.gen()`` equals
          ``other_into_F(other.gen()) + k*self_into_F(self.gen())``;

        - ``Infinity``, in which case ``F.gen()`` equals
          ``self_into_F(self.gen())``;

        - ``None`` (when ``other`` is a relative number field).

        If both ``self`` and ``other`` have embeddings into an ambient
        field, then each ``F`` will have an embedding with respect to
        which both ``self_into_F`` and ``other_into_F`` will be
        compatible with the ambient embeddings.

        If ``preserve_embedding`` is ``True`` and if ``self`` and
        ``other`` both have embeddings into the same ambient field, or
        into fields which are contained in a common field, only the
        compositum respecting both embeddings is returned.  In all
        other cases, all possible composite number fields are
        returned.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<a> = NumberField(x^4 - 2)
            sage: K.composite_fields(K)
            [Number Field in a with defining polynomial x^4 - 2,
             Number Field in a0 with defining polynomial x^8 + 28*x^4 + 2500]

        A particular compositum is selected, together with compatible maps
        into the compositum, if the fields are endowed with a real or
        complex embedding::

            sage: # needs sage.symbolic
            sage: K1 = NumberField(x^4 - 2, 'a', embedding=RR(2^(1/4)))
            sage: K2 = NumberField(x^4 - 2, 'a', embedding=RR(-2^(1/4)))
            sage: K1.composite_fields(K2)
            [Number Field in a with defining polynomial x^4 - 2 with a = 1.189207115002722?]
            sage: [F, f, g, k], = K1.composite_fields(K2, both_maps=True); F
            Number Field in a with defining polynomial x^4 - 2 with a = 1.189207115002722?
            sage: f(K1.0), g(K2.0)
            (a, -a)

        With ``preserve_embedding`` set to ``False``, the embeddings
        are ignored::

            sage: K1.composite_fields(K2, preserve_embedding=False)                     # needs sage.symbolic
            [Number Field in a with defining polynomial x^4 - 2 with a = 1.189207115002722?,
             Number Field in a0 with defining polynomial x^8 + 28*x^4 + 2500]

        Changing the embedding selects a different compositum::

            sage: K3 = NumberField(x^4 - 2, 'a', embedding=CC(2^(1/4)*I))               # needs sage.symbolic
            sage: [F, f, g, k], = K1.composite_fields(K3, both_maps=True); F            # needs sage.symbolic
            Number Field in a0 with defining polynomial x^8 + 28*x^4 + 2500
             with a0 = -2.378414230005443? + 1.189207115002722?*I
            sage: f(K1.0), g(K3.0)                                                      # needs sage.symbolic
            (1/240*a0^5 - 41/120*a0, 1/120*a0^5 + 19/60*a0)

        If no embeddings are specified, the maps into the compositum
        are chosen arbitrarily::

            sage: Q1.<a> = NumberField(x^4 + 10*x^2 + 1)
            sage: Q2.<b> = NumberField(x^4 + 16*x^2 + 4)
            sage: Q1.composite_fields(Q2, 'c')
            [Number Field in c with defining polynomial
              x^8 + 64*x^6 + 904*x^4 + 3840*x^2 + 3600]
            sage: F, Q1_into_F, Q2_into_F, k = Q1.composite_fields(Q2, 'c',
            ....:                                                  both_maps=True)[0]
            sage: Q1_into_F
            Ring morphism:
              From: Number Field in a with defining polynomial x^4 + 10*x^2 + 1
              To:   Number Field in c with defining polynomial
                    x^8 + 64*x^6 + 904*x^4 + 3840*x^2 + 3600
              Defn: a |--> 19/14400*c^7 + 137/1800*c^5 + 2599/3600*c^3 + 8/15*c

        This is just one of four embeddings of ``Q1`` into ``F``::

            sage: Hom(Q1, F).order()
            4

        Note that even with ``preserve_embedding=True``, this method may fail
        to recognize that the two number fields have compatible embeddings, and
        hence return several composite number fields::

            sage: x = polygen(ZZ)
            sage: A.<a> = NumberField(x^3 - 7, embedding=CC(-0.95+1.65*I))
            sage: r = QQbar.polynomial_root(x^9 - 7, RIF(1.2, 1.3))
            sage: B.<a> = NumberField(x^9 - 7, embedding=r)
            sage: len(A.composite_fields(B, preserve_embedding=True))
            2

        TESTS:

        Let's check that embeddings are being respected::

            sage: x = polygen(ZZ)
            sage: K0.<b> = CyclotomicField(7, 'a').subfields(3)[0][0].change_names()
            sage: K1.<a1> = K0.extension(x^2 - 2*b^2, 'a1').absolute_field()
            sage: K2.<a2> = K0.extension(x^2 - 3*b^2, 'a2').absolute_field()

        We need embeddings, so we redefine::

            sage: L1.<a1> = NumberField(K1.polynomial(), 'a1', embedding=CC.0)
            sage: L2.<a2> = NumberField(K2.polynomial(), 'a2', embedding=CC.0)
            sage: [CDF(a1), CDF(a2)]
            [-0.6293842454258951, -0.7708351267200304]

        and we get the same embeddings via the compositum::

            sage: F, L1_into_F, L2_into_F, k = L1.composite_fields(L2, both_maps=True)[0]
            sage: [CDF(L1_into_F(L1.gen())), CDF(L2_into_F(L2.gen()))]
            [-0.6293842454258952, -0.7708351267200303]

        Let's check that if only one field has an embedding, the resulting
        fields do not have embeddings::

            sage: L1.composite_fields(K2)[0].coerce_embedding() is None
            True
            sage: L2.composite_fields(K1)[0].coerce_embedding() is None
            True

        We check that other can be a relative number field::

            sage: L.<a, b> = NumberField([x^3 - 5, x^2 + 3])
            sage: CyclotomicField(3, 'w').composite_fields(L, both_maps=True)
            [(Number Field in a with defining polynomial x^3 - 5 over its base field,
              Ring morphism:
                From: Cyclotomic Field of order 3 and degree 2
                To:   Number Field in a with defining polynomial x^3 - 5 over its base field
                Defn: w |--> -1/2*b - 1/2,
              Relative number field endomorphism of Number Field in a
               with defining polynomial x^3 - 5 over its base field
                Defn: a |--> a
                      b |--> b,
              None)]

        Number fields defined by non-monic and non-integral
        polynomials are supported (:issue:`252`)::

            sage: K.<a> = NumberField(x^2 + 1/2)
            sage: L.<b> = NumberField(3*x^2 - 1)
            sage: K.composite_fields(L)
            [Number Field in ab with defining polynomial 36*x^4 + 12*x^2 + 25]
            sage: C = K.composite_fields(L, both_maps=True); C
            [(Number Field in ab with defining polynomial 36*x^4 + 12*x^2 + 25,
              Ring morphism:
                From: Number Field in a with defining polynomial x^2 + 1/2
                To:   Number Field in ab with defining polynomial 36*x^4 + 12*x^2 + 25
                Defn: a |--> -3/5*ab^3 - 7/10*ab,
              Ring morphism:
                From: Number Field in b with defining polynomial 3*x^2 - 1
                To:   Number Field in ab with defining polynomial 36*x^4 + 12*x^2 + 25
                Defn: b |--> -3/5*ab^3 + 3/10*ab,
              -1)]
            sage: M, f, g, k = C[0]
            sage: M.gen() == g(b) + k*f(a)
            True

        This also fixes the bugs reported at :issue:`14164` and
        :issue:`18243`::

            sage: R.<x> = QQ[]
            sage: f = 6*x^5 + x^4 + x^2 + 5*x + 7
            sage: r = f.roots(QQbar, multiplicities=False)
            sage: F1 = NumberField(f.monic(), 'a', embedding=r[0])
            sage: F2 = NumberField(f.monic(), 'a', embedding=r[1])
            sage: (F, map1, map2, k) = F1.composite_fields(F2, both_maps=True)[0]
            sage: F.degree()
            20
            sage: F.gen() == map2(F2.gen()) + k*map1(F1.gen())
            True

            sage: f = x^8 - 3*x^7 + 61/3*x^6 - 9*x^5 + 298*x^4 + 458*x^3 + 1875*x^2 + 4293*x + 3099
            sage: F1 = NumberField(f, 'z', embedding=-1.18126721294295 + 3.02858651117832j)
            sage: F2 = NumberField(f, 'z', embedding=-1.18126721294295 - 3.02858651117832j)
            sage: (F, map1, map2, k) = F1.composite_fields(F2, both_maps=True)[0]
            sage: F.degree()
            32
            sage: F.gen() == map2(F2.gen()) + k*map1(F1.gen())
            True

        Check that the bugs reported at :issue:`24357` are fixed::

            sage: A.<a> = NumberField(x^9 - 7)
            sage: B.<b> = NumberField(x^3 - 7, embedding=a^3)
            sage: C.<c> = QuadraticField(-1)
            sage: B.composite_fields(C)
            [Number Field in bc with defining polynomial x^6 + 3*x^4 + 14*x^3 + 3*x^2 - 42*x + 50]

            sage: y = polygen(QQ, 'y')
            sage: A.<a> = NumberField(x^3 - 7, embedding=CC(-0.95+1.65*I))
            sage: B.<b> = NumberField(y^9 - 7, embedding=CC(-1.16+0.42*I))
            sage: A.composite_fields(B)
            [Number Field in b with defining polynomial y^9 - 7
              with b = -1.166502297945062? + 0.4245721146551276?*I]
        """
    def absolute_degree(self):
        """
        Return the degree of ``self`` over `\\QQ`.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: NumberField(x^3 + x^2 + 997*x + 1, 'a').absolute_degree()
            3
            sage: NumberField(x + 1, 'a').absolute_degree()
            1
            sage: NumberField(x^997 + 17*x + 3, 'a', check=False).absolute_degree()
            997
        """
    def degree(self):
        """
        Return the degree of this number field.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: NumberField(x^3 + x^2 + 997*x + 1, 'a').degree()
            3
            sage: NumberField(x + 1, 'a').degree()
            1
            sage: NumberField(x^997 + 17*x + 3, 'a', check=False).degree()
            997
        """
    def different(self):
        """
        Compute the different fractional ideal of this number field.

        The codifferent is the fractional ideal of all `x` in `K`
        such that the trace of `xy` is an integer for
        all `y \\in O_K`.

        The different is the integral ideal which is the inverse of
        the codifferent.

        See :wikipedia:`Different_ideal`

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: k.<a> = NumberField(x^2 + 23)
            sage: d = k.different()
            sage: d
            Fractional ideal (a)
            sage: d.norm()
            23
            sage: k.disc()
            -23

        The different is cached::

            sage: d is k.different()
            True

        Another example::

            sage: k.<b> = NumberField(x^2 - 123)
            sage: d = k.different(); d
            Fractional ideal (2*b)
            sage: d.norm()
            492
            sage: k.disc()
            492
        """
    def discriminant(self, v=None):
        """
        Return the discriminant of the ring of integers of the number
        field, or if ``v`` is specified, the determinant of the trace pairing
        on the elements of the list ``v``.

        INPUT:

        - ``v`` -- (optional) list of elements of this number field

        OUTPUT: integer if ``v`` is omitted, and Rational otherwise

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<t> = NumberField(x^3 + x^2 - 2*x + 8)
            sage: K.disc()
            -503
            sage: K.disc([1, t, t^2])
            -2012
            sage: K.disc([1/7, (1/5)*t, (1/3)*t^2])
            -2012/11025
            sage: (5*7*3)^2
            11025
            sage: NumberField(x^2 - 1/2, 'a').discriminant()
            8
        """
    def disc(self, v=None):
        """
        Shortcut for :meth:`discriminant`.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: k.<b> = NumberField(x^2 - 123)
            sage: k.disc()
            492
        """
    def trace_dual_basis(self, b):
        """
        Compute the dual basis of a basis of ``self`` with respect to the trace pairing.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<a> = NumberField(x^3 + x + 1)
            sage: b = [1, 2*a, 3*a^2]
            sage: T = K.trace_dual_basis(b); T
            [4/31*a^2 - 6/31*a + 13/31, -9/62*a^2 - 1/31*a - 3/31, 2/31*a^2 - 3/31*a + 4/93]
            sage: [(b[i]*T[j]).trace() for i in range(3) for j in range(3)]
            [1, 0, 0, 0, 1, 0, 0, 0, 1]
        """
    def elements_of_norm(self, n, proof=None) -> list:
        """
        Return a list of elements of norm `n`.

        INPUT:

        - ``n`` -- integer

        - ``proof`` -- boolean (default: ``True``, unless you called
          :meth:`proof.number_field` and set it otherwise)

        OUTPUT:

        A complete system of integral elements of norm `n`, modulo
        units of positive norm.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<a> = NumberField(x^2 + 1)
            sage: K.elements_of_norm(3)
            []
            sage: K.elements_of_norm(50)
            [7*a - 1, 5*a - 5, -7*a - 1]

        TESTS:

        Number fields defined by non-monic and non-integral
        polynomials are supported (:issue:`252`);
        the representation depends on the PARI version::

            sage: K.<a> = NumberField(7/9*x^3 + 7/3*x^2 - 56*x + 123)
            sage: [x] = K.elements_of_norm(7)
            sage: x in (7/225*a^2 - 7/75*a - 42/25, 28/225*a^2 + 77/75*a - 133/25)
            True
        """
    def extension(self, poly, name=None, names=None, latex_name=None, latex_names=None, *args, **kwds):
        """
        Return the relative extension of this field by a given polynomial.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<a> = NumberField(x^3 - 2)
            sage: R.<t> = K[]
            sage: L.<b> = K.extension(t^2 + a); L
            Number Field in b with defining polynomial t^2 + a over its base field

        We create another extension::

            sage: k.<a> = NumberField(x^2 + 1); k
            Number Field in a with defining polynomial x^2 + 1
            sage: y = polygen(QQ,'y')
            sage: m.<b> = k.extension(y^2 + 2); m
            Number Field in b with defining polynomial y^2 + 2 over its base field

        Note that `b` is a root of `y^2 + 2`::

            sage: b.minpoly()
            x^2 + 2
            sage: b.minpoly('z')
            z^2 + 2

        A relative extension of a relative extension::

            sage: k.<a> = NumberField([x^2 + 1, x^3 + x + 1])
            sage: R.<z> = k[]
            sage: L.<b> = NumberField(z^3 + 3 + a); L
            Number Field in b with defining polynomial z^3 + a0 + 3 over its base field

        Extension fields with given defining data are unique
        (:issue:`20791`)::

            sage: K.<a> = NumberField(x^2 + 1)
            sage: K.extension(x^2 - 2, 'b') is K.extension(x^2 - 2, 'b')
            True
        """
    def factor(self, n):
        """
        Ideal factorization of the principal ideal generated by `n`.

        EXAMPLES:

        Here we show how to factor Gaussian integers (up to units).
        First we form a number field defined by `x^2 + 1`::

            sage: x = polygen(QQ, 'x')
            sage: K.<I> = NumberField(x^2 + 1); K
            Number Field in I with defining polynomial x^2 + 1

        Here are the factors::

            sage: fi, fj = K.factor(17); fi,fj
            ((Fractional ideal (I + 4), 1), (Fractional ideal (I - 4), 1))

        Now we extract the reduced form of the generators::

            sage: zi = fi[0].gens_reduced()[0]; zi
            I + 4
            sage: zj = fj[0].gens_reduced()[0]; zj
            I - 4

        We recover the integer that was factored in `\\ZZ[i]` (up to a unit)::

            sage: zi*zj
            -17

        One can also factor elements or ideals of the number field::

            sage: K.<a> = NumberField(x^2 + 1)
            sage: K.factor(1/3)
            (Fractional ideal (3))^-1
            sage: K.factor(1+a)
            Fractional ideal (a - 1)
            sage: K.factor(1+a/5)
            (Fractional ideal (a - 1)) * (Fractional ideal (2*a - 1))^-1 * (Fractional ideal (-2*a - 1))^-1 * (Fractional ideal (3*a + 2))

        An example over a relative number field::

            sage: pari('setrand(2)')
            sage: L.<b> = K.extension(x^2 - 7)
            sage: f = L.factor(a + 1)
            sage: f                               # representation varies, not tested
            (Fractional ideal (1/2*a*b - a + 1/2)) * (Fractional ideal (-1/2*a*b - a + 1/2))
            sage: f.value() == a+1
            True

        It doesn't make sense to factor the ideal `(0)`, so this raises an error::

            sage: L.factor(0)
            Traceback (most recent call last):
            ...
            AttributeError: 'NumberFieldIdeal' object has no attribute 'factor'...

        AUTHORS:

        - Alex Clemesha (2006-05-20), Francis Clarke (2009-04-21): examples

        TESTS:

        We test the above doctest. The representation depends on the PARI version::

            sage: K.<a> = NumberField(x^2 + 1)
            sage: L.<b> = K.extension(x^2 - 7)
            sage: f = L.factor(a + 1)
            sage: (fi, fj) = f[::]
            sage: (fi[1], fj[1])
            (1, 1)
            sage: fi[0] == L.fractional_ideal(-1/2*a*b - a + 1/2)
            True
            sage: fj[0] == L.fractional_ideal(1/2*a*b - a + 1/2)
            True
        """
    def prime_factors(self, x):
        """
        Return a list of the prime ideals of ``self`` which divide
        the ideal generated by `x`.

        OUTPUT: list of prime ideals (a new list is returned each time this
        function is called)

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<w> = NumberField(x^2 + 23)
            sage: K.prime_factors(w + 1)
            [Fractional ideal (2, 1/2*w - 1/2),
             Fractional ideal (2, 1/2*w + 1/2),
             Fractional ideal (3, 1/2*w + 1/2)]
        """
    def decomposition_type(self, p):
        """
        Return how the given prime of the base field splits in this number field.

        INPUT:

        - ``p`` -- a prime element or ideal of the base field

        OUTPUT:

        A list of triples `(e, f, g)` where

        - `e` is the ramification index,

        - `f` is the residue class degree,

        - `g` is the number of primes above `p` with given `e` and `f`

        EXAMPLES::

            sage: R.<x> = ZZ[]
            sage: K.<a> = NumberField(x^20 + 3*x^18 + 15*x^16 + 28*x^14 + 237*x^12 + 579*x^10
            ....:                      + 1114*x^8 + 1470*x^6 + 2304*x^4 + 1296*x^2 + 729)
            sage: K.is_galois()                                                         # needs sage.groups
            True
            sage: K.discriminant().factor()
            2^20 * 3^10 * 53^10
            sage: K.decomposition_type(2)
            [(2, 5, 2)]
            sage: K.decomposition_type(3)
            [(2, 1, 10)]
            sage: K.decomposition_type(53)
            [(2, 2, 5)]

        This example is only ramified at 11::

            sage: K.<a> = NumberField(x^24 + 11^2*(90*x^12 - 640*x^8 + 2280*x^6
            ....:                                   - 512*x^4 + 2432/11*x^2 - 11))
            sage: K.discriminant().factor()
            -1 * 11^43
            sage: K.decomposition_type(11)
            [(1, 1, 2), (22, 1, 1)]

        Computing the decomposition type is feasible even in large degree::

            sage: K.<a> = NumberField(x^144 + 123*x^72 + 321*x^36 + 13*x^18 + 11)
            sage: K.discriminant().factor(limit=100000)
            2^144 * 3^288 * 7^18 * 11^17 * 31^18 * 157^18 * 2153^18 * 13907^18 * ...
            sage: K.decomposition_type(2)
            [(2, 4, 3), (2, 12, 2), (2, 36, 1)]
            sage: K.decomposition_type(3)
            [(9, 3, 2), (9, 10, 1)]
            sage: K.decomposition_type(7)
            [(1, 18, 1), (1, 90, 1), (2, 1, 6), (2, 3, 4)]

        It also works for relative extensions::

            sage: K.<a> = QuadraticField(-143)
            sage: M.<c> = K.extension(x^10 - 6*x^8 + (a + 12)*x^6 + (-7/2*a - 89/2)*x^4
            ....:                      + (13/2*a - 77/2)*x^2 + 25)

        There is a unique prime above `11` and above `13` in `K`, each of which is unramified in `M`::

            sage: M.decomposition_type(11)
            [(1, 2, 5)]
            sage: P11 = K.primes_above(11)[0]
            sage: len(M.primes_above(P11))
            5
            sage: M.decomposition_type(13)
            [(1, 1, 10)]
            sage: P13 = K.primes_above(13)[0]
            sage: len(M.primes_above(P13))
            10

        There are two primes above `2`, each of which ramifies in `M`::

            sage: Q0, Q1 = K.primes_above(2)
            sage: M.decomposition_type(Q0)
            [(2, 5, 1)]
            sage: q0, = M.primes_above(Q0)
            sage: q0.residue_class_degree()
            5
            sage: q0.relative_ramification_index()
            2
            sage: M.decomposition_type(Q1)
            [(2, 5, 1)]

        Check that :issue:`34514` is fixed::

            sage: K.<a> = NumberField(x^4 + 18*x^2 - 1)
            sage: R.<y> = K[]
            sage: L.<b> = K.extension(y^2 + 9*a^3 - 2*a^2 + 162*a - 38)
            sage: [L.decomposition_type(i) for i in K.primes_above(3)]
            [[(1, 1, 2)], [(1, 1, 2)], [(1, 2, 1)]]
        """
    def gen(self, n: int = 0):
        """
        Return the generator for this number field.

        INPUT:

        - ``n`` -- must be 0 (the default), or an exception is raised

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: k.<theta> = NumberField(x^14 + 2); k
            Number Field in theta with defining polynomial x^14 + 2
            sage: k.gen()
            theta
            sage: k.gen(1)
            Traceback (most recent call last):
            ...
            IndexError: Only one generator.
        """
    def is_field(self, proof: bool = True):
        """
        Return ``True`` since a number field is a field.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: NumberField(x^5 + x + 3, 'c').is_field()
            True
        """
    @cached_method
    def is_galois(self):
        """
        Return ``True`` if this number field is a Galois extension of
        `\\QQ`.

        EXAMPLES::

            sage: # needs sage.groups
            sage: x = polygen(QQ, 'x')
            sage: NumberField(x^2 + 1, 'i').is_galois()
            True
            sage: NumberField(x^3 + 2, 'a').is_galois()
            False
            sage: K = NumberField(x^15 + x^14 - 14*x^13 - 13*x^12 + 78*x^11 + 66*x^10
            ....:                  - 220*x^9 - 165*x^8 + 330*x^7 + 210*x^6 - 252*x^5
            ....:                  - 126*x^4 + 84*x^3 + 28*x^2 - 8*x - 1, 'a')
            sage: K.is_galois()
            True
            sage: K = NumberField(x^15 + x^14 - 14*x^13 - 13*x^12 + 78*x^11 + 66*x^10
            ....:                  - 220*x^9 - 165*x^8 + 330*x^7 + 210*x^6 - 252*x^5
            ....:                  - 126*x^4 + 84*x^3 + 28*x^2 - 8*x - 10, 'a')
            sage: K.is_galois()
            False
        """
    @cached_method
    def is_abelian(self):
        """
        Return ``True`` if this number field is an abelian Galois extension of
        `\\QQ`.

        EXAMPLES::

            sage: # needs sage.groups
            sage: x = polygen(QQ, 'x')
            sage: NumberField(x^2 + 1, 'i').is_abelian()
            True
            sage: NumberField(x^3 + 2, 'a').is_abelian()
            False
            sage: NumberField(x^3 + x^2 - 2*x - 1, 'a').is_abelian()
            True
            sage: NumberField(x^6 + 40*x^3 + 1372, 'a').is_abelian()
            False
            sage: NumberField(x^6 + x^5 - 5*x^4 - 4*x^3 + 6*x^2 + 3*x - 1, 'a').is_abelian()
            True
        """
    @cached_method
    def galois_group(self, type=None, algorithm: str = 'pari', names=None, gc_numbering=None):
        '''
        Return the Galois group of the Galois closure of this number field.

        INPUT:

        - ``type`` -- deprecated; the different versions of Galois groups have been
          merged in :issue:`28782`

        - ``algorithm`` -- ``\'pari\'``, ``\'gap\'``, ``\'kash\'``, or ``\'magma\'``
          (default: ``\'pari\'``); for degrees between 12 and 15 default is
          ``\'gap\'``, and when the degree is >= 16 it is ``\'kash\'``)

        - ``names`` -- string giving a name for the generator of the Galois
          closure of ``self``, when this field is not Galois

        - ``gc_numbering`` -- if ``True``, permutations will be written
          in terms of the action on the roots of a defining polynomial
          for the Galois closure, rather than the defining polynomial for
          the original number field.  This is significantly faster;
          but not the standard way of presenting Galois groups.
          The default currently depends on the algorithm (``True`` for ``\'pari\'``,
          ``False`` for ``\'magma\'``) and may change in the future.

        The resulting group will only compute with automorphisms when necessary,
        so certain functions (such as :meth:`sage.rings.number_field.galois_group.GaloisGroup_v2.order`)
        will still be fast.  For more (important!)
        documentation, see the documentation for Galois groups of polynomials
        over `\\QQ`, e.g., by typing ``K.polynomial().galois_group?``,
        where `K` is a number field.

        EXAMPLES::

            sage: # needs sage.groups
            sage: x = polygen(QQ, \'x\')
            sage: k.<b> = NumberField(x^2 - 14)  # a Galois extension
            sage: G = k.galois_group(); G
            Galois group 2T1 (S2) with order 2 of x^2 - 14
            sage: G.gen(0)
            (1,2)
            sage: G.gen(0)(b)
            -b
            sage: G.artin_symbol(k.primes_above(3)[0])
            (1,2)

            sage: # needs sage.groups
            sage: k.<b> = NumberField(x^3 - x + 1)  # not Galois
            sage: G = k.galois_group(names=\'c\'); G
            Galois group 3T2 (S3) with order 6 of x^3 - x + 1
            sage: G.gen(0)
            (1,2,3)(4,5,6)

            sage: NumberField(x^3 + 2*x + 1, \'a\').galois_group(algorithm=\'magma\')   # optional - magma, needs sage.groups
            Galois group Transitive group number 2 of degree 3
             of the Number Field in a with defining polynomial x^3 + 2*x + 1

        EXPLICIT GALOIS GROUP: We compute the Galois group as an explicit
        group of automorphisms of the Galois closure of a field.

        ::

            sage: # needs sage.groups
            sage: K.<a> = NumberField(x^3 - 2)
            sage: L.<b1> = K.galois_closure(); L
            Number Field in b1 with defining polynomial x^6 + 108
            sage: G = End(L); G
            Automorphism group of Number Field in b1 with defining polynomial x^6 + 108
            sage: G.list()
            [Ring endomorphism of Number Field in b1 with defining polynomial x^6 + 108
               Defn: b1 |--> b1,
             ...
             Ring endomorphism of Number Field in b1 with defining polynomial x^6 + 108
               Defn: b1 |--> -1/12*b1^4 - 1/2*b1]
            sage: G[2](b1)
            1/12*b1^4 + 1/2*b1

        Many examples for higher degrees may be found in the online databases
        http://galoisdb.math.upb.de/ by Jürgen Klüners and Gunter Malle and
        https://www.lmfdb.org/NumberField/ by the LMFDB collaboration,
        although these might need a lot of computing time.

        If `L/K` is a relative number field, this method will currently return `Gal(L/\\QQ)`.  This behavior will
        change in the future, so it\'s better to explicitly call :meth:`absolute_field` if that is
        the desired behavior::

            sage: # needs sage.groups
            sage: x = polygen(QQ)
            sage: K.<a> = NumberField(x^2 + 1)
            sage: R.<t> = PolynomialRing(K)
            sage: L = K.extension(t^5 - t + a, \'b\')
            sage: L.galois_group()
            ...DeprecationWarning: Use .absolute_field().galois_group()
            if you want the Galois group of the absolute field
            See https://github.com/sagemath/sage/issues/28782 for details.
            Galois group 10T22 (S(5)[x]2) with order 240 of t^5 - t + a

        TESTS:

        We check that the changes in :issue:`28782` won\'t break code that used v1 Galois groups::

            sage: # needs sage.groups
            sage: G = NumberField(x^3 - 2, \'a\').galois_group(type=\'pari\')
            ...DeprecationWarning: the different Galois types have been merged into one class
            See https://github.com/sagemath/sage/issues/28782 for details.
            sage: G.group()
            ...DeprecationWarning: the group method is deprecated; you can use _pol_galgp if you really need it
            See https://github.com/sagemath/sage/issues/28782 for details.
            PARI group [6, -1, 2, "S3"] of degree 3
        '''
    def power_basis(self):
        """
        Return a power basis for this number field over its base field.

        If this number field is represented as `k[t]/f(t)`, then
        the basis returned is `1, t, t^2, \\ldots, t^{d-1}` where
        `d` is the degree of this number field over its base
        field.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<a> = NumberField(x^5 + 10*x + 1)
            sage: K.power_basis()
            [1, a, a^2, a^3, a^4]

        ::

            sage: L.<b> = K.extension(x^2 - 2)
            sage: L.power_basis()
            [1, b]
            sage: L.absolute_field('c').power_basis()
            [1, c, c^2, c^3, c^4, c^5, c^6, c^7, c^8, c^9]

        ::

            sage: M = CyclotomicField(15)
            sage: M.power_basis()
            [1, zeta15, zeta15^2, zeta15^3, zeta15^4, zeta15^5, zeta15^6, zeta15^7]
        """
    def integral_basis(self, v=None):
        '''
        Return a list containing a ``ZZ``-basis for the full ring of integers
        of this number field.

        INPUT:

        - ``v`` -- ``None``, a prime, or a list of primes; see the
          documentation for :meth:`maximal_order`

        EXAMPLES::

            sage: x = polygen(QQ, \'x\')
            sage: K.<a> = NumberField(x^5 + 10*x + 1)
            sage: K.integral_basis()
            [1, a, a^2, a^3, a^4]

        Next we compute the ring of integers of a cubic field in which 2 is
        an "essential discriminant divisor", so the ring of integers is not
        generated by a single element.

        ::

            sage: K.<a> = NumberField(x^3 + x^2 - 2*x + 8)
            sage: K.integral_basis()
            [1, 1/2*a^2 + 1/2*a, a^2]

        ALGORITHM: Uses the PARI library (via :pari:`_pari_integral_basis`).
        '''
    def reduced_basis(self, prec=None):
        '''
        Return an LLL-reduced basis for the Minkowski-embedding
        of the maximal order of a number field.

        INPUT:

        - ``prec`` -- (default: ``None``) the precision with which to
          compute the Minkowski embedding

        OUTPUT:

        An LLL-reduced basis for the Minkowski-embedding of the
        maximal order of a number field, given by a sequence of (integral)
        elements from the field.

        .. NOTE::

            In the non-totally-real case, the LLL routine we call is
            currently PARI\'s :pari:`qflll`, which works with floating point
            approximations, and so the result is only as good as the
            precision promised by PARI. The matrix returned will always
            be integral; however, it may only be only "almost" LLL-reduced
            when the precision is not sufficiently high.

        EXAMPLES::

            sage: x = polygen(QQ, \'x\')
            sage: F.<t> = NumberField(x^6 - 7*x^4 - x^3 + 11*x^2 + x - 1)
            sage: F.maximal_order().basis()
            [1/2*t^5 + 1/2*t^4 + 1/2*t^2 + 1/2, t, t^2, t^3, t^4, t^5]
            sage: F.reduced_basis()
            [-1, -1/2*t^5 + 1/2*t^4 + 3*t^3 - 3/2*t^2 - 4*t - 1/2, t,
             1/2*t^5 + 1/2*t^4 - 4*t^3 - 5/2*t^2 + 7*t + 1/2,
             1/2*t^5 - 1/2*t^4 - 2*t^3 + 3/2*t^2 - 1/2,
             1/2*t^5 - 1/2*t^4 - 3*t^3 + 5/2*t^2 + 4*t - 5/2]
            sage: CyclotomicField(12).reduced_basis()
            [1, zeta12^2, zeta12, zeta12^3]

        TESTS:

        Check that the bug reported at :issue:`10017` is fixed::

            sage: x = polygen(QQ)
            sage: k.<a> = NumberField(x^6 + 2218926655879913714112*x^4 - 32507675650290949030789018433536*x^3 + 4923635504174417014460581055002374467948544*x^2 - 36066074010564497464129951249279114076897746988630016*x + 264187244046129768986806800244258952598300346857154900812365824)
            sage: new_basis = k.reduced_basis(prec=120)
            sage: [c.minpoly() for c in new_basis]
            [x - 1,
             x^2 + x + 1,
             x^6 + 3*x^5 - 102*x^4 - 103*x^3 + 10572*x^2 - 59919*x + 127657,
             x^6 + 3*x^5 - 102*x^4 - 103*x^3 + 10572*x^2 - 59919*x + 127657,
             x^3 - 171*x + 848,
             x^6 + 171*x^4 + 1696*x^3 + 29241*x^2 + 145008*x + 719104]
            sage: R = k.order(new_basis)
            sage: R.discriminant()==k.discriminant()
            True
        '''
    def reduced_gram_matrix(self, prec=None):
        '''
        Return the Gram matrix of an LLL-reduced basis for
        the Minkowski embedding of the maximal order of a number field.

        INPUT:

        - ``prec`` -- (default: ``None``) the precision with which
          to calculate the Minkowski embedding (see NOTE below)

        OUTPUT: the Gram matrix `[\\langle x_i,x_j \\rangle]` of an LLL reduced
        basis for the maximal order of ``self``, where the integral basis for
        ``self`` is given by `\\{x_0, \\dots, x_{n-1}\\}`. Here `\\langle , \\rangle` is
        the usual inner product on `\\RR^n`, and ``self`` is embedded in `\\RR^n` by
        the Minkowski embedding. See the docstring for
        :meth:`NumberField_absolute.minkowski_embedding` for more information.

        .. NOTE::

           In the non-totally-real case, the LLL routine we call is
           currently PARI\'s :pari:`qflll`, which works with floating point
           approximations, and so the result is only as good as the
           precision promised by PARI. In particular, in this case,
           the returned matrix will *not* be integral, and may not
           have enough precision to recover the correct Gram matrix
           (which is known to be integral for theoretical
           reasons). Thus the need for the ``prec`` parameter above.

        If the following run-time error occurs: "PariError: not a definite
        matrix in lllgram (42)", try increasing the ``prec`` parameter,

        EXAMPLES::

            sage: x = polygen(QQ, \'x\')
            sage: F.<t> = NumberField(x^6 - 7*x^4 - x^3 + 11*x^2 + x - 1)
            sage: F.reduced_gram_matrix()
            [ 6  3  0  2  0  1]
            [ 3  9  0  1  0 -2]
            [ 0  0 14  6 -2  3]
            [ 2  1  6 16 -3  3]
            [ 0  0 -2 -3 16  6]
            [ 1 -2  3  3  6 19]
            sage: Matrix(6, [(x*y).trace()
            ....:            for x in F.integral_basis() for y in F.integral_basis()])
            [2550  133  259  664 1368 3421]
            [ 133   14    3   54   30  233]
            [ 259    3   54   30  233  217]
            [ 664   54   30  233  217 1078]
            [1368   30  233  217 1078 1371]
            [3421  233  217 1078 1371 5224]

        ::

            sage: x = polygen(QQ)
            sage: F.<alpha> = NumberField(x^4 + x^2 + 712312*x + 131001238)
            sage: F.reduced_gram_matrix(prec=128)
            [   4.0000000000000000000000000000000000000   0.00000000000000000000000000000000000000   -1.9999999999999999999999999999999999037  -0.99999999999999999999999999999999383702]
            [  0.00000000000000000000000000000000000000    46721.539331563218381658483353092335550   -11488.910026551724275122749703614966768   -418.12718083977141198754424579680468382]
            [  -1.9999999999999999999999999999999999037   -11488.910026551724275122749703614966768  5.5658915310500611768713076521847709187e8  1.4179092271494070050433368847682152174e8]
            [ -0.99999999999999999999999999999999383702   -418.12718083977141198754424579680468382  1.4179092271494070050433368847682152174e8 1.3665897267919181137884111201405279175e12]
        '''
    @cached_method
    def narrow_class_group(self, proof=None):
        """
        Return the narrow class group of this field.

        INPUT:

        - ``proof`` -- (default: ``None``) use the global proof setting, which
          defaults to ``True``

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: NumberField(x^3 + x + 9, 'a').narrow_class_group()
            Multiplicative Abelian group isomorphic to C2

        TESTS::

            sage: QuadraticField(3, 'a').narrow_class_group()
            Multiplicative Abelian group isomorphic to C2
        """
    def ngens(self):
        """
        Return the number of generators of this number field (always 1).

        OUTPUT: the python integer 1

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: NumberField(x^2 + 17,'a').ngens()
            1
            sage: NumberField(x + 3,'a').ngens()
            1
            sage: k.<a> = NumberField(x + 3)
            sage: k.ngens()
            1
            sage: k.0
            -3
        """
    def order(self):
        """
        Return the order of this number field (always +infinity).

        OUTPUT: always positive infinity

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: NumberField(x^2 + 19,'a').order()
            +Infinity
        """
    def absolute_polynomial_ntl(self):
        """
        Alias for :meth:`~polynomial_ntl`. Mostly for internal use.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: NumberField(x^2 + (2/3)*x - 9/17,'a').absolute_polynomial_ntl()
            ([-27 34 51], 51)
        """
    def polynomial_ntl(self):
        """
        Return defining polynomial of this number field as a pair, an ntl
        polynomial and a denominator.

        This is used mainly to implement some internal arithmetic.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: NumberField(x^2 + (2/3)*x - 9/17,'a').polynomial_ntl()
            ([-27 34 51], 51)
        """
    def polynomial(self):
        """
        Return the defining polynomial of this number field.

        This is exactly the same as :meth:`defining_polynomial`.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: NumberField(x^2 + (2/3)*x - 9/17,'a').polynomial()
            x^2 + 2/3*x - 9/17
        """
    def defining_polynomial(self):
        """
        Return the defining polynomial of this number field.

        This is exactly the same as :meth:`polynomial`.

        EXAMPLES::

            sage: k5.<z> = CyclotomicField(5)
            sage: k5.defining_polynomial()
            x^4 + x^3 + x^2 + x + 1
            sage: y = polygen(QQ, 'y')
            sage: k.<a> = NumberField(y^9 - 3*y + 5); k
            Number Field in a with defining polynomial y^9 - 3*y + 5
            sage: k.defining_polynomial()
            y^9 - 3*y + 5
        """
    def polynomial_ring(self):
        """
        Return the polynomial ring that we view this number field as being
        a quotient of (by a principal ideal).

        EXAMPLES: An example with an absolute field::

            sage: x = polygen(QQ, 'x')
            sage: k.<a> = NumberField(x^2 + 3)
            sage: y = polygen(QQ, 'y')
            sage: k.<a> = NumberField(y^2 + 3)
            sage: k.polynomial_ring()
            Univariate Polynomial Ring in y over Rational Field

        An example with a relative field::

            sage: y = polygen(QQ, 'y')
            sage: M.<a> = NumberField([y^3 + 97, y^2 + 1]); M
            Number Field in a0 with defining polynomial y^3 + 97 over its base field
            sage: M.polynomial_ring()
            Univariate Polynomial Ring in y over
             Number Field in a1 with defining polynomial y^2 + 1
        """
    def polynomial_quotient_ring(self):
        """
        Return the polynomial quotient ring isomorphic to this number
        field.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K = NumberField(x^3 + 2*x - 5, 'alpha')
            sage: K.polynomial_quotient_ring()
            Univariate Quotient Polynomial Ring in alpha over Rational Field
             with modulus x^3 + 2*x - 5
        """
    def regulator(self, proof=None):
        """
        Return the regulator of this number field.

        Note that PARI computes the regulator to higher precision than the
        Sage default.

        INPUT:

        - ``proof`` -- (default: ``True``) unless you set it otherwise

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: NumberField(x^2 - 2, 'a').regulator()
            0.881373587019543
            sage: NumberField(x^4 + x^3 + x^2 + x + 1, 'a').regulator()
            0.962423650119207
        """
    def residue_field(self, prime, names=None, check: bool = True):
        """
        Return the residue field of this number field at a given prime, ie
        `O_K / p O_K`.

        INPUT:

        - ``prime`` -- a prime ideal of the maximal order in
          this number field, or an element of the field which generates a
          principal prime ideal.

        - ``names`` -- the name of the variable in the residue field

        - ``check`` -- whether or not to check the primality of ``prime``

        OUTPUT: the residue field at this prime

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^4 + 3*x^2 - 17)
            sage: P = K.ideal(61).factor()[0][0]
            sage: K.residue_field(P)
            Residue field in abar of Fractional ideal (61, a^2 + 30)

        ::

            sage: K.<i> = NumberField(x^2 + 1)
            sage: K.residue_field(1+i)
            Residue field of Fractional ideal (i + 1)

        TESTS::

            sage: L.<b> = NumberField(x^2 + 5)
            sage: L.residue_field(P)
            Traceback (most recent call last):
            ...
            ValueError: Fractional ideal (61, a^2 + 30) is not an ideal of Number Field in b with defining polynomial x^2 + 5
            sage: L.residue_field(2)
            Traceback (most recent call last):
            ...
            ValueError: Fractional ideal (2) is not a prime ideal

        ::

            sage: L.residue_field(L.prime_above(5)^2)
            Traceback (most recent call last):
            ...
            ValueError: Fractional ideal (5) is not a prime ideal
        """
    def signature(self):
        """
        Return `(r_1, r_2)`, where `r_1` and `r_2` are the number of real embeddings
        and pairs of complex embeddings of this field, respectively.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: NumberField(x^2 + 1, 'a').signature()
            (0, 1)
            sage: NumberField(x^3 - 2, 'a').signature()
            (1, 1)
        """
    def trace_pairing(self, v):
        """
        Return the matrix of the trace pairing on the elements of the list
        ``v``.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<zeta3> = NumberField(x^2 + 3)
            sage: K.trace_pairing([1, zeta3])
            [ 2  0]
            [ 0 -6]
        """
    def uniformizer(self, P, others: str = 'positive'):
        '''
        Return an element of ``self`` with valuation 1 at the prime ideal `P`.

        INPUT:

        - ``self`` -- a number field

        - ``P`` -- a prime ideal of ``self``

        - ``others`` -- either ``\'positive\'`` (default), in which case the
          element will have nonnegative valuation at all other primes of
          ``self``, or ``\'negative\'``, in which case the element will have
          nonpositive valuation at all other primes of ``self``

        .. NOTE::

           When `P` is principal (e.g., always when ``self`` has class number
           one) the result may or may not be a generator of `P`!

        EXAMPLES::

            sage: x = polygen(QQ, \'x\')
            sage: K.<a> = NumberField(x^2 + 5); K
            Number Field in a with defining polynomial x^2 + 5
            sage: P, Q = K.ideal(3).prime_factors()
            sage: P
            Fractional ideal (3, a + 1)
            sage: pi = K.uniformizer(P); pi
            a + 1
            sage: K.ideal(pi).factor()
            (Fractional ideal (2, a + 1)) * (Fractional ideal (3, a + 1))
            sage: pi = K.uniformizer(P,\'negative\'); pi
            1/2*a + 1/2
            sage: K.ideal(pi).factor()
            (Fractional ideal (2, a + 1))^-1 * (Fractional ideal (3, a + 1))

        ::

            sage: K = CyclotomicField(9)
            sage: Plist = K.ideal(17).prime_factors()
            sage: pilist = [K.uniformizer(P) for P in Plist]
            sage: [pi.is_integral() for pi in pilist]
            [True, True, True]
            sage: [pi.valuation(P) for pi, P in zip(pilist, Plist)]
            [1, 1, 1]
            sage: [ pilist[i] in Plist[i] for i in range(len(Plist)) ]
            [True, True, True]

        ::

            sage: K.<t> = NumberField(x^4 - x^3 - 3*x^2 - x + 1)
            sage: [K.uniformizer(P) for P,e in factor(K.ideal(2))]
            [2]
            sage: [K.uniformizer(P) for P,e in factor(K.ideal(3))]
            [t - 1]
            sage: [K.uniformizer(P) for P,e in factor(K.ideal(5))]
            [t^2 - t + 1, t + 2, t - 2]
            sage: [K.uniformizer(P) for P,e in factor(K.ideal(7))]  # representation varies, not tested
            [t^2 + 3*t + 1]
            sage: [K.uniformizer(P) for P,e in factor(K.ideal(67))]
            [t + 23, t + 26, t - 32, t - 18]

        ALGORITHM:

            Use PARI. More precisely, use the second component of
            :pari:`idealprimedec` in the "positive" case. Use :pari:`idealappr`
            with exponent of `-1` and invert the result in the "negative"
            case.

        TESTS:

        We test the above doctest. The representation depends on the PARI version::

            sage: K.<t> = NumberField(x^4 - x^3 - 3*x^2 - x + 1)
            sage: [x] = [K.uniformizer(P) for P,e in factor(K.ideal(7))]
            sage: x in (t^2 + 3*t +1, t^2 - 4*t +1)
            True
        '''
    def units(self, proof=None):
        """
        Return generators for the unit group modulo torsion.

        ALGORITHM: Uses PARI's :pari:`bnfinit` command.

        INPUT:

        - ``proof`` -- boolean (default: ``True``); flag passed to PARI

        .. NOTE::

            For more functionality see :meth:`unit_group`.

        .. SEEALSO::

            :meth:`unit_group`
            :meth:`S_unit_group`
            :meth:`S_units`

        EXAMPLES::

            sage: x = polygen(QQ)
            sage: A = x^4 - 10*x^3 + 20*5*x^2 - 15*5^2*x + 11*5^3
            sage: K = NumberField(A, 'a')
            sage: K.units()
            (-1/275*a^3 - 4/55*a^2 + 5/11*a - 3,)

        For big number fields, provably computing the unit group can
        take a very long time.  In this case, one can ask for the
        conjectural unit group (correct if the Generalized Riemann
        Hypothesis is true)::

            sage: K = NumberField(x^17 + 3, 'a')
            sage: K.units(proof=True)  # takes forever, not tested
            ...
            sage: K.units(proof=False)  # result not independently verified
            (a^9 + a - 1,
             -a^15 + a^12 - a^10 + a^9 + 2*a^8 - 3*a^7 - a^6 + 3*a^5 - a^4 - 4*a^3 + 3*a^2 + 2*a - 2,
             a^15 + a^14 + a^13 + a^12 + a^10 - a^7 - a^6 - a^2 - 1,
             2*a^16 - 3*a^15 + 3*a^14 - 3*a^13 + 3*a^12 - a^11 + a^9 - 3*a^8 + 4*a^7 - 5*a^6 + 6*a^5 - 4*a^4 + 3*a^3 - 2*a^2 - 2*a + 4,
             -a^16 + a^15 - a^14 + a^12 - a^11 + a^10 + a^8 - a^7 + 2*a^6 - a^4 + 3*a^3 - 2*a^2 + 2*a - 1,
             a^16 - 2*a^15 - 2*a^13 - a^12 - a^11 - 2*a^10 + a^9 - 2*a^8 + 2*a^7 - 3*a^6 - 3*a^4 - 2*a^3 - a^2 - 4*a + 2,
             -a^15 - a^14 - 2*a^11 - a^10 + a^9 - a^8 - 2*a^7 + a^5 - 2*a^3 + a^2 + 3*a - 1,
             -3*a^16 - 3*a^15 - 3*a^14 - 3*a^13 - 3*a^12 - 2*a^11 - 2*a^10 - 2*a^9 - a^8 + a^7 + 2*a^6 + 3*a^5 + 3*a^4 + 4*a^3 + 6*a^2 + 8*a + 8)

        TESTS:

        Number fields defined by non-monic and non-integral
        polynomials are supported (:issue:`252`)::

            sage: K.<a> = NumberField(1/2*x^2 - 1/6)
            sage: K.units()
            (3*a + 2,)
        """
    def unit_group(self, proof=None):
        """
        Return the unit group (including torsion) of this number field.

        ALGORITHM: Uses PARI's :pari:`bnfinit` command.

        INPUT:

        - ``proof`` -- boolean (default: ``True``); flag passed to PARI

        .. NOTE::

           The group is cached.

        .. SEEALSO::

            :meth:`units`
            :meth:`S_unit_group`
            :meth:`S_units`

        EXAMPLES::

            sage: x = QQ['x'].0
            sage: A = x^4 - 10*x^3 + 20*5*x^2 - 15*5^2*x + 11*5^3
            sage: K = NumberField(A, 'a')
            sage: U = K.unit_group(); U
            Unit group with structure C10 x Z of Number Field in a
             with defining polynomial x^4 - 10*x^3 + 100*x^2 - 375*x + 1375
            sage: U.gens()
            (u0, u1)
            sage: U.gens_values()  # random
            [-1/275*a^3 + 7/55*a^2 - 6/11*a + 4, 1/275*a^3 + 4/55*a^2 - 5/11*a + 3]
            sage: U.invariants()
            (10, 0)
            sage: [u.multiplicative_order() for u in U.gens()]
            [10, +Infinity]

        For big number fields, provably computing the unit group can
        take a very long time.  In this case, one can ask for the
        conjectural unit group (correct if the Generalized Riemann
        Hypothesis is true)::

            sage: K = NumberField(x^17 + 3, 'a')
            sage: K.unit_group(proof=True)  # takes forever, not tested
            ...
            sage: U = K.unit_group(proof=False)
            sage: U
            Unit group with structure C2 x Z x Z x Z x Z x Z x Z x Z x Z of
             Number Field in a with defining polynomial x^17 + 3
            sage: U.gens()
            (u0, u1, u2, u3, u4, u5, u6, u7, u8)
            sage: U.gens_values()  # result not independently verified
            [-1,
             a^9 + a - 1,
             -a^15 + a^12 - a^10 + a^9 + 2*a^8 - 3*a^7 - a^6 + 3*a^5 - a^4 - 4*a^3 + 3*a^2 + 2*a - 2,
             a^15 + a^14 + a^13 + a^12 + a^10 - a^7 - a^6 - a^2 - 1,
             2*a^16 - 3*a^15 + 3*a^14 - 3*a^13 + 3*a^12 - a^11 + a^9 - 3*a^8 + 4*a^7 - 5*a^6 + 6*a^5 - 4*a^4 + 3*a^3 - 2*a^2 - 2*a + 4,
             -a^16 + a^15 - a^14 + a^12 - a^11 + a^10 + a^8 - a^7 + 2*a^6 - a^4 + 3*a^3 - 2*a^2 + 2*a - 1,
             a^16 - 2*a^15 - 2*a^13 - a^12 - a^11 - 2*a^10 + a^9 - 2*a^8 + 2*a^7 - 3*a^6 - 3*a^4 - 2*a^3 - a^2 - 4*a + 2,
             -a^15 - a^14 - 2*a^11 - a^10 + a^9 - a^8 - 2*a^7 + a^5 - 2*a^3 + a^2 + 3*a - 1,
             -3*a^16 - 3*a^15 - 3*a^14 - 3*a^13 - 3*a^12 - 2*a^11 - 2*a^10 - 2*a^9 - a^8 + a^7 + 2*a^6 + 3*a^5 + 3*a^4 + 4*a^3 + 6*a^2 + 8*a + 8]
        """
    def S_unit_group(self, proof=None, S=None):
        """
        Return the `S`-unit group (including torsion) of this number field.

        ALGORITHM: Uses PARI's :pari:`bnfsunit` command.

        INPUT:

        - ``proof`` -- boolean (default: ``True``); flag passed to PARI

        - ``S`` -- list or tuple of prime ideals, or an ideal, or a single
          ideal or element from which an ideal can be constructed, in
          which case the support is used.  If ``None``, the global unit
          group is constructed; otherwise, the `S`-unit group is
          constructed.

        .. NOTE::

           The group is cached.

        EXAMPLES::

            sage: x = polygen(QQ)
            sage: K.<a> = NumberField(x^4 - 10*x^3 + 20*5*x^2 - 15*5^2*x + 11*5^3)
            sage: U = K.S_unit_group(S=a); U
            S-unit group with structure C10 x Z x Z x Z of
             Number Field in a with defining polynomial x^4 - 10*x^3 + 100*x^2 - 375*x + 1375
             with S = (Fractional ideal (5, -7/275*a^3 + 1/11*a^2 - 9/11*a),
                       Fractional ideal (11, -7/275*a^3 + 1/11*a^2 - 9/11*a + 3))
            sage: U.gens()
            (u0, u1, u2, u3)
            sage: U.gens_values()  # random
            [-1/275*a^3 + 7/55*a^2 - 6/11*a + 4, 1/275*a^3 + 4/55*a^2 - 5/11*a + 3,
             1/275*a^3 + 4/55*a^2 - 5/11*a + 5, -14/275*a^3 + 21/55*a^2 - 29/11*a + 6]
            sage: U.invariants()
            (10, 0, 0, 0)
            sage: [u.multiplicative_order() for u in U.gens()]
            [10, +Infinity, +Infinity, +Infinity]
            sage: U.primes()
            (Fractional ideal (5, -7/275*a^3 + 1/11*a^2 - 9/11*a),
             Fractional ideal (11, -7/275*a^3 + 1/11*a^2 - 9/11*a + 3))

        With the default value of `S`, the S-unit group is the same as
        the global unit group::

            sage: x = polygen(QQ)
            sage: K.<a> = NumberField(x^3 + 3)
            sage: U = K.unit_group(proof=False)
            sage: U.is_isomorphic(K.S_unit_group(proof=False))
            True

        The value of `S` may be specified as a list of prime ideals,
        or an ideal, or an element of the field::

            sage: K.<a> = NumberField(x^3 + 3)
            sage: U = K.S_unit_group(proof=False, S=K.ideal(6).prime_factors()); U
            S-unit group with structure C2 x Z x Z x Z x Z
             of Number Field in a with defining polynomial x^3 + 3
             with S = (Fractional ideal (-a^2 + a - 1),
                       Fractional ideal (a + 1),
                       Fractional ideal (a))
            sage: K.<a> = NumberField(x^3 + 3)
            sage: U = K.S_unit_group(proof=False, S=K.ideal(6)); U
            S-unit group with structure C2 x Z x Z x Z x Z
             of Number Field in a with defining polynomial x^3 + 3
             with S = (Fractional ideal (-a^2 + a - 1),
                       Fractional ideal (a + 1),
                       Fractional ideal (a))
            sage: K.<a> = NumberField(x^3 + 3)
            sage: U = K.S_unit_group(proof=False, S=6); U
            S-unit group with structure C2 x Z x Z x Z x Z
             of Number Field in a with defining polynomial x^3 + 3
             with S = (Fractional ideal (-a^2 + a - 1),
                       Fractional ideal (a + 1),
                       Fractional ideal (a))
            sage: U.primes()
            (Fractional ideal (-a^2 + a - 1),
             Fractional ideal (a + 1),
             Fractional ideal (a))
            sage: U.gens()
            (u0, u1, u2, u3, u4)
            sage: U.gens_values()
            [-1, a^2 - 2, -a^2 + a - 1, a + 1, a]

        The exp and log methods can be used to create `S`-units from
        sequences of exponents, and recover the exponents::

            sage: U.gens_orders()
            (2, 0, 0, 0, 0)
            sage: u = U.exp((3,1,4,1,5)); u
            -6*a^2 + 18*a - 54
            sage: u.norm().factor()
            -1 * 2^9 * 3^5
            sage: U.log(u)
            (1, 1, 4, 1, 5)
        """
    def S_unit_solutions(self, S=[], prec: int = 106, include_exponents: bool = False, include_bound: bool = False, proof=None):
        """
        Return all solutions to the `S`-unit equation `x + y = 1` over ``self``.

        INPUT:

        - ``S`` -- list of finite primes in this number field
        - ``prec`` -- precision used for computations in real, complex, and
          `p`-adic fields (default: 106)
        - ``include_exponents`` -- whether to include the exponent vectors in
          the returned value (default: ``True``)
        - ``include_bound`` -- whether to return the final computed bound
          (default: ``False``)
        - ``proof`` -- if ``False``, assume the GRH in computing the class group;
          default is ``True``

        OUTPUT:

        A list `[(A_1, B_1, x_1, y_1), (A_2, B_2, x_2, y_2), \\dots, (A_n, B_n, x_n, y_n)]` of tuples such that:

        1. The first two entries are tuples `A_i = (a_0, a_1, \\dots, a_t)` and `B_i = (b_0, b_1, \\dots, b_t)` of exponents.
           These will be omitted if ``include_exponents`` is ``False``.

        2. The last two entries are `S`-units `x_i` and `y_i` in ``self`` with `x_i + y_i = 1`.

        3. If the default generators for the `S`-units of ``self`` are `(\\rho_0, \\rho_1, \\dots, \\rho_t)``,
           then these satisfy `x_i = \\prod(\\rho_i)^{(a_i)}` and `y_i = \\prod(\\rho_i)^{(b_i)}`.

        If ``include_bound`` is ``True``, will return a pair ``(sols, bound)`` where ``sols`` is as above
        and ``bound`` is the bound used for the entries in the exponent vectors.

        EXAMPLES::

            sage: # needs sage.rings.padics
            sage: x = polygen(QQ, 'x')
            sage: K.<xi> = NumberField(x^2 + x + 1)
            sage: S = K.primes_above(3)
            sage: K.S_unit_solutions(S)  # random, due to ordering
            [(xi + 2, -xi - 1), (1/3*xi + 2/3, -1/3*xi + 1/3), (-xi, xi + 1), (-xi + 1, xi)]

        You can get the exponent vectors::

            sage: # needs sage.rings.padics
            sage: K.S_unit_solutions(S, include_exponents=True)  # random, due to ordering
            [((2, 1), (4, 0), xi + 2, -xi - 1),
             ((5, -1), (4, -1), 1/3*xi + 2/3, -1/3*xi + 1/3),
             ((5, 0), (1, 0), -xi, xi + 1),
             ((1, 1), (2, 0), -xi + 1, xi)]

        And the computed bound::

            sage: # needs sage.rings.padics
            sage: solutions, bound = K.S_unit_solutions(S, prec=100, include_bound=True)
            sage: bound
            6
        """
    def zeta(self, n: int = 2, all: bool = False):
        """
        Return one, or a list of all, primitive `n`-th root of unity in this field.

        INPUT:

        - ``n`` -- positive integer

        - ``all`` -- boolean; if ``False`` (default), return a primitive
          `n`-th root of unity in this field, or raise a :exc:`ValueError`
          exception if there are none.  If ``True``, return a list of all
          primitive `n`-th roots of unity in this field (possibly empty).

        .. NOTE::

            To obtain the maximal order of a root of unity in this field,
            use :meth:`number_of_roots_of_unity`.

        .. NOTE::

            We do not create the full unit group since that can be
            expensive, but we do use it if it is already known.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<z> = NumberField(x^2 + 3)
            sage: K.zeta(1)
            1
            sage: K.zeta(2)
            -1
            sage: K.zeta(2, all=True)
            [-1]
            sage: K.zeta(3)
            -1/2*z - 1/2
            sage: K.zeta(3, all=True)
            [-1/2*z - 1/2, 1/2*z - 1/2]
            sage: K.zeta(4)
            Traceback (most recent call last):
            ...
            ValueError: there are no 4th roots of unity in self

        ::

            sage: r.<x> = QQ[]
            sage: K.<b> = NumberField(x^2 + 1)
            sage: K.zeta(4)
            b
            sage: K.zeta(4,all=True)
            [b, -b]
            sage: K.zeta(3)
            Traceback (most recent call last):
            ...
            ValueError: there are no 3rd roots of unity in self
            sage: K.zeta(3, all=True)
            []

        Number fields defined by non-monic and non-integral
        polynomials are supported (:issue:`252`)::

            sage: K.<a> = NumberField(1/2*x^2 + 1/6)
            sage: K.zeta(3)
            -3/2*a - 1/2

        TESTS::

            sage: K = NumberField(x**60+691*x**12-25,'a')
            sage: K.zeta(15,all=True)
            []
        """
    def zeta_order(self):
        """
        Return the number of roots of unity in this field.

        .. NOTE::

           We do not create the full unit group since that can be
           expensive, but we do use it if it is already known.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: F.<alpha> = NumberField(x^22 + 3)
            sage: F.zeta_order()
            6
            sage: F.<alpha> = NumberField(x^2 - 7)
            sage: F.zeta_order()
            2

        TESTS:

        Number fields defined by non-monic and non-integral
        polynomials are supported (:issue:`252`)::

            sage: K.<a> = NumberField(1/2*x^2 + 1/6)
            sage: K.zeta_order()
            6
        """
    number_of_roots_of_unity = zeta_order
    def primitive_root_of_unity(self):
        """
        Return a generator of the roots of unity in this field.

        OUTPUT: a primitive root of unity. No guarantee is made about
        which primitive root of unity this returns, not even for
        cyclotomic fields. Repeated calls of this function may return
        a different value.

        .. NOTE::

           We do not create the full unit group since that can be
           expensive, but we do use it if it is already known.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<i> = NumberField(x^2 + 1)
            sage: z = K.primitive_root_of_unity(); z
            i
            sage: z.multiplicative_order()
            4

            sage: K.<a> = NumberField(x^2 + x + 1)
            sage: z = K.primitive_root_of_unity(); z
            a + 1
            sage: z.multiplicative_order()
            6

            sage: x = polygen(QQ)
            sage: F.<a,b> = NumberField([x^2 - 2, x^2 - 3])
            sage: y = polygen(F)
            sage: K.<c> = F.extension(y^2 - (1 + a)*(a + b)*a*b)
            sage: K.primitive_root_of_unity()
            -1

        We do not special-case cyclotomic fields, so we do not always
        get the most obvious primitive root of unity::

            sage: K.<a> = CyclotomicField(3)
            sage: z = K.primitive_root_of_unity(); z
            a + 1
            sage: z.multiplicative_order()
            6

            sage: K = CyclotomicField(3)
            sage: z = K.primitive_root_of_unity(); z
            zeta3 + 1
            sage: z.multiplicative_order()
            6

        TESTS:

        Check for :issue:`15027`. We use a new variable name::

            sage: K.<f> = NumberField(x^2 + x + 1)
            sage: K.primitive_root_of_unity()
            f + 1
            sage: UK = K.unit_group()
            sage: K.primitive_root_of_unity()
            f + 1

        Number fields defined by non-monic and non-integral
        polynomials are supported (:issue:`252`)::

            sage: K.<a> = NumberField(3*x^2 + 1)
            sage: K.primitive_root_of_unity()
            -3/2*a + 1/2
        """
    def roots_of_unity(self):
        """
        Return all the roots of unity in this field, primitive or not.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<b> = NumberField(x^2 + 1)
            sage: zs = K.roots_of_unity(); zs
            [b, -1, -b, 1]
            sage: [z**K.number_of_roots_of_unity() for z in zs]
            [1, 1, 1, 1]
        """
    def zeta_coefficients(self, n):
        """
        Compute the first `n` coefficients of the Dedekind zeta function of
        this field as a Dirichlet series.

        EXAMPLES::

            sage: x = QQ['x'].0
            sage: NumberField(x^2 + 1, 'a').zeta_coefficients(10)
            [1, 1, 0, 1, 2, 0, 0, 1, 1, 2]
        """
    def solve_CRT(self, reslist, Ilist, check: bool = True):
        """
        Solve a Chinese remainder problem over this number field.

        INPUT:

        - ``reslist`` -- list of residues, i.e. integral number field elements

        - ``Ilist`` -- list of integral ideals, assumed pairwise coprime

        - ``check`` -- boolean (default: ``True``); if ``True``, result is checked

        OUTPUT:

        An integral element `x` such that ``x - reslist[i]`` is in ``Ilist[i]`` for all `i`.

        .. NOTE::

           The current implementation requires the ideals to be pairwise
           coprime.  A more general version would be possible.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<a> = NumberField(x^2 - 10)
            sage: Ilist = [K.primes_above(p)[0] for p in prime_range(10)]
            sage: b = K.solve_CRT([1,2,3,4], Ilist, True)
            sage: all(b - i - 1 in Ilist[i] for i in range(4))
            True
            sage: Ilist = [K.ideal(a), K.ideal(2)]
            sage: K.solve_CRT([0,1], Ilist, True)
            Traceback (most recent call last):
            ...
            ArithmeticError: ideals in solve_CRT() must be pairwise coprime
            sage: Ilist[0] + Ilist[1]
            Fractional ideal (2, a)
        """
    def valuation(self, prime):
        """
        Return the valuation on this field defined by ``prime``.

        INPUT:

        - ``prime`` -- a prime that does not split, a discrete
          (pseudo-)valuation or a fractional ideal

        EXAMPLES:

        The valuation can be specified with an integer ``prime`` that is
        completely ramified in ``R``::

            sage: x = polygen(QQ, 'x')
            sage: K.<a> = NumberField(x^2 + 1)
            sage: K.valuation(2)                                                        # needs sage.rings.padics
            2-adic valuation

        It can also be unramified in ``R``::

            sage: K.valuation(3)                                                        # needs sage.rings.padics
            3-adic valuation

        A ``prime`` that factors into pairwise distinct factors, results in an error::

            sage: K.valuation(5)                                                        # needs sage.rings.padics
            Traceback (most recent call last):
            ...
            ValueError: The valuation Gauss valuation induced by 5-adic valuation does not
            approximate a unique extension of 5-adic valuation with respect to x^2 + 1

        The valuation can also be selected by giving a valuation on the base
        ring that extends uniquely::

            sage: CyclotomicField(5).valuation(ZZ.valuation(5))                         # needs sage.rings.padics
            5-adic valuation

        When the extension is not unique, this does not work::

            sage: K.valuation(ZZ.valuation(5))                                          # needs sage.rings.padics
            Traceback (most recent call last):
            ...
            ValueError: The valuation Gauss valuation induced by 5-adic valuation does not
            approximate a unique extension of 5-adic valuation with respect to x^2 + 1

        For a number field which is of the form `K[x]/(G)`, you can specify a
        valuation by providing a discrete pseudo-valuation on `K[x]` which sends
        `G` to infinity. This lets us specify which extension of the 5-adic
        valuation we care about in the above example::

            sage: # needs sage.rings.padics
            sage: R.<x> = QQ[]
            sage: G5 = GaussValuation(R, QQ.valuation(5))
            sage: v = K.valuation(G5.augmentation(x + 2, infinity))
            sage: w = K.valuation(G5.augmentation(x + 1/2, infinity))
            sage: v == w
            False

        Note that you get the same valuation, even if you write down the
        pseudo-valuation differently::

            sage: # needs sage.rings.padics
            sage: ww = K.valuation(G5.augmentation(x + 3, infinity))
            sage: w is ww
            True

        The valuation ``prime`` does not need to send the defining polynomial `G`
        to infinity. It is sufficient if it singles out one of the valuations on
        the number field.  This is important if the prime only factors over the
        completion, i.e., if it is not possible to write down one of the factors
        within the number field::

            sage: # needs sage.rings.padics
            sage: v = G5.augmentation(x + 3, 1)
            sage: K.valuation(v)
            [ 5-adic valuation, v(x + 3) = 1 ]-adic valuation

        Finally, ``prime`` can also be a fractional ideal of a number field if it
        singles out an extension of a `p`-adic valuation of the base field::

            sage: K.valuation(K.fractional_ideal(a + 1))                                # needs sage.rings.padics
            2-adic valuation

        .. SEEALSO::

            :meth:`Order.valuation() <sage.rings.number_field.order.Order.valuation>`,
            :meth:`pAdicGeneric.valuation() <sage.rings.padics.padic_generic.pAdicGeneric.valuation>`
        """
    def some_elements(self):
        """
        Return a list of elements in the given number field.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: K.<a> =  QQ.extension(t^2 - 2); K
            Number Field in a with defining polynomial t^2 - 2
            sage: K.some_elements()
            [1, a, 2*a, 3*a - 4, 1/2, 1/3*a, 1/6*a, 0, 1/2*a, 2, ..., 12, -12*a + 18]

            sage: T.<u> = K[]
            sage: M.<b> = K.extension(t^3 - 5); M
            Number Field in b with defining polynomial t^3 - 5 over its base field
            sage: M.some_elements()
            [1, b, 1/2*a*b, ..., 2/5*b^2 + 2/5, 1/6*b^2 + 5/6*b + 13/6, 2]

        TESTS:

        This also works in trivial extensions::

            sage: R.<t> = QQ[]
            sage: K.<a> = QQ.extension(t); K
            Number Field in a with defining polynomial t
            sage: K.some_elements()
            [0, 1, 2, -1, 1/2, -1/2, 1/4, -2, 4]
        """
    def lmfdb_page(self) -> None:
        '''
        Open the LMFDB web page of the number field in a browser.

        See https://www.lmfdb.org

        EXAMPLES::

            sage: E = QuadraticField(-1)
            sage: E.lmfdb_page()  # optional -- webbrowser

        Even if the variable name is different it works::

            sage: R.<y>= PolynomialRing(QQ, "y")
            sage: K = NumberField(y^2 + 1 , "i")
            sage: K.lmfdb_page()  # optional -- webbrowser
        '''
    def maximal_order(self, v=None, assume_maximal: str = 'non-maximal-non-unique'):
        '''
        Return the maximal order, i.e., the ring of integers, associated to
        this number field.

        INPUT:

        - ``v`` -- ``None``, a prime, or a list of integer primes (default: ``None``)

          - if ``None``, return the maximal order.

          - if a prime `p`, return an order that is `p`-maximal.

          - if a list, return an order that is maximal at each prime of these primes

        - ``assume_maximal`` -- ``True``, ``False``, ``None``, or
          ``\'non-maximal-non-unique\'`` (default: ``\'non-maximal-non-unique\'``)
          ignored when ``v`` is ``None``; otherwise, controls whether we assume
          that the order :meth:`order.is_maximal` outside of ``v``.

          - if ``True``, the order is assumed to be maximal at all primes.

          - if ``False``, the order is assumed to be non-maximal at some prime
            not in ``v``.

          - if ``None``, no assumptions are made about primes not in ``v``.

          - if ``\'non-maximal-non-unique\'`` (deprecated), like ``False``,
            however, the order is not a unique parent, so creating the same
            order later does typically not poison caches with the information
            that the order is not maximal.

        EXAMPLES:

        In this example, the maximal order cannot be generated by a single
        element::

            sage: x = polygen(QQ, \'x\')
            sage: k.<a> = NumberField(x^3 + x^2 - 2*x+8)
            sage: o = k.maximal_order()
            sage: o
            Maximal Order generated by [1/2*a^2 + 1/2*a, a^2] in Number Field in a with defining polynomial x^3 + x^2 - 2*x + 8

        We compute `p`-maximal orders for several `p`. Note
        that computing a `p`-maximal order is much faster in
        general than computing the maximal order::

            sage: p = next_prime(10^22)
            sage: q = next_prime(10^23)
            sage: K.<a> = NumberField(x^3 - p*q)

            sage: K.maximal_order([3], assume_maximal=None).basis()
            [1/3*a^2 + 1/3*a + 1/3, a, a^2]

            sage: K.maximal_order([2], assume_maximal=None).basis()
            [1/3*a^2 + 1/3*a + 1/3, a, a^2]

            sage: K.maximal_order([p], assume_maximal=None).basis()
            [1/3*a^2 + 1/3*a + 1/3, a, a^2]

            sage: K.maximal_order([q], assume_maximal=None).basis()
            [1/3*a^2 + 1/3*a + 1/3, a, a^2]

            sage: K.maximal_order([p, 3], assume_maximal=None).basis()
            [1/3*a^2 + 1/3*a + 1/3, a, a^2]

        An example with bigger discriminant::

            sage: p = next_prime(10^97)
            sage: q = next_prime(10^99)
            sage: K.<a> = NumberField(x^3 - p*q)
            sage: K.maximal_order(prime_range(10000), assume_maximal=None).basis()
            [1, a, a^2]

        An example in a relative number field::

            sage: K.<a, b> = NumberField([x^2 + 1, x^2 - 3])
            sage: OK = K.maximal_order()
            sage: OK.basis()
            [1, 1/2*a - 1/2*b, -1/2*b*a + 1/2, a]

            sage: charpoly(OK.1)
            x^2 + b*x + 1
            sage: charpoly(OK.2)
            x^2 - x + 1

            sage: O2 = K.order([3*a, 2*b])
            sage: O2.index_in(OK)
            144

        An order that is maximal at a prime. We happen to know that it is
        actually maximal and mark it as such::

            sage: K.<i> = NumberField(x^2 + 1)
            sage: K.maximal_order(v=2, assume_maximal=True)
            Gaussian Integers generated by i in Number Field in i with defining polynomial x^2 + 1

        It is an error to create a maximal order and declare it non-maximal,
        however, such mistakes are only caught automatically if they evidently
        contradict previous results in this session::

            sage: K.maximal_order(v=2, assume_maximal=False)
            Traceback (most recent call last):
            ...
            ValueError: cannot assume this order to be non-maximal
            because we already found it to be a maximal order

        TESTS:

        Number fields defined by non-monic and non-integral
        polynomials are supported (:issue:`252`)::

            sage: K.<a> = NumberField(3*x^2 + 1)
            sage: K.maximal_order().basis()
            [3/2*a + 1/2, 3*a]

        The following was previously "ridiculously slow"; see :issue:`4738`::

            sage: K.<a, b> = NumberField([x^4 + 1, x^4 - 3])
            sage: K.maximal_order()
            Maximal Relative Order generated by
            [(131/4*b^3 + 9/4*b)*a^3 + (-69/4*b^2 - 521/4)*a^2 + (69/4*b^3 + 333/4*b)*a - 57/4*b^2 - 103/4,
             (21/2*b^3 - 39/4*b^2 - 25/4*b - 553/2)*a^3 + (69/4*b^3 - 21/4*b^2 + 473/2*b - 85/2)*a^2 + (37/4*b^3 - 189/2*b^2 + 55/2*b - 155/4)*a - 35*b^3 - 5*b^2 + 47/4*b - 83/4,
             (73/2*b^3 - 115/4*b^2 - 2*b - 1153/4)*a^3 + (56*b^3 - 59/4*b^2 + 237*b - 507/4)*a^2 + (17*b^3 - 353/4*b^2 + 73*b - 523/4)*a - 42*b^3 - 21/4*b^2 + 87/2*b - 117/4]
            in Number Field in a with defining polynomial x^4 + 1 over its base field

        An example with nontrivial ``v``::

            sage: L.<a, b> = NumberField([x^2 - 1000003, x^2 - 5*1000099^2])
            sage: O3 = L.maximal_order([3], assume_maximal=None)
            sage: O3.absolute_discriminant()
            400160824478095086350656915693814563600
            sage: O3.is_maximal()
            False
        '''

class NumberField_absolute(NumberField_generic):
    def __init__(self, polynomial, name, latex_name=None, check: bool = True, embedding=None, assume_disc_small: bool = False, maximize_at_primes=None, structure=None) -> None:
        """
        Function to initialize an absolute number field.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K = NumberField(x^17 + 3, 'a'); K
            Number Field in a with defining polynomial x^17 + 3
            sage: type(K)
            <class 'sage.rings.number_field.number_field.NumberField_absolute_with_category'>
            sage: TestSuite(K).run()
        """
    def base_field(self):
        """
        Return the base field of ``self``, which is always ``QQ``.

        EXAMPLES::

            sage: K = CyclotomicField(5)
            sage: K.base_field()
            Rational Field
        """
    def __iter__(self):
        """
        Iterate over ``self``.

        EXAMPLES::

            sage: K = CyclotomicField(5)
            sage: it = iter(K)
            sage: [next(it) for _ in range(20)]
            [0, 1, zeta5, zeta5^2, zeta5^3, -1, zeta5 + 1, zeta5^2 + 1,
             zeta5^3 + 1, -zeta5, zeta5^2 + zeta5, zeta5^3 + zeta5, -zeta5^2,
             zeta5^3 + zeta5^2, -zeta5^3, 1/2, zeta5 - 1, zeta5^2 - 1,
             zeta5^3 - 1, -zeta5 + 1]
        """
    def is_absolute(self):
        """
        Return ``True`` since ``self`` is an absolute field.

        EXAMPLES::

            sage: K = CyclotomicField(5)
            sage: K.is_absolute()
            True
        """
    def absolute_polynomial(self):
        """
        Return absolute polynomial that defines this absolute field. This
        is the same as :meth:`polynomial`.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<a> = NumberField(x^2 + 1)
            sage: K.absolute_polynomial ()
            x^2 + 1
        """
    def absolute_generator(self):
        """
        An alias for
        :meth:`sage.rings.number_field.number_field.NumberField_generic.gen`.
        This is provided for consistency with relative fields, where the
        element returned by
        :meth:`sage.rings.number_field.number_field_rel.NumberField_relative.gen`
        only generates the field over its base field (not necessarily over
        `\\QQ`).

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<a> = NumberField(x^2 - 17)
            sage: K.absolute_generator()
            a
        """
    def optimized_representation(self, name=None, both_maps: bool = True):
        """
        Return a field isomorphic to ``self`` with a better defining polynomial
        if possible, along with field isomorphisms from the new field to
        ``self`` and from ``self`` to the new field.

        EXAMPLES: We construct a compositum of 3 quadratic fields, then
        find an optimized representation and transform elements back and
        forth.

        ::

            sage: x = polygen(QQ, 'x')
            sage: K = NumberField([x^2 + p for p in [5, 3, 2]],'a').absolute_field('b'); K
            Number Field in b with defining polynomial x^8 + 40*x^6 + 352*x^4 + 960*x^2 + 576
            sage: L, from_L, to_L = K.optimized_representation()
            sage: L    # your answer may different, since algorithm is random
            Number Field in b1 with defining polynomial x^8 + 4*x^6 + 7*x^4 + 36*x^2 + 81
            sage: to_L(K.0)   # random
            4/189*b1^7 + 1/63*b1^6 + 1/27*b1^5 - 2/9*b1^4 - 5/27*b1^3 - 8/9*b1^2 + 3/7*b1 - 3/7
            sage: from_L(L.0)   # random
            1/1152*b^7 - 1/192*b^6 + 23/576*b^5 - 17/96*b^4 + 37/72*b^3 - 5/6*b^2 + 55/24*b - 3/4

        The transformation maps are mutually inverse isomorphisms.

        ::

            sage: from_L(to_L(K.0)) == K.0
            True
            sage: to_L(from_L(L.0)) == L.0
            True

        Number fields defined by non-monic and non-integral
        polynomials are supported (:issue:`252`)::

            sage: K.<a> = NumberField(7/9*x^3 + 7/3*x^2 - 56*x + 123)
            sage: K.optimized_representation()  # representation varies, not tested
            (Number Field in a1 with defining polynomial x^3 - 7*x - 7,
             Ring morphism:
               From: Number Field in a1 with defining polynomial x^3 - 7*x - 7
               To:   Number Field in a with defining polynomial 7/9*x^3 + 7/3*x^2 - 56*x + 123
               Defn: a1 |--> 7/225*a^2 - 7/75*a - 42/25,
             Ring morphism:
               From: Number Field in a with defining polynomial 7/9*x^3 + 7/3*x^2 - 56*x + 123
               To:   Number Field in a1 with defining polynomial x^3 - 7*x - 7
               Defn: a |--> -15/7*a1^2 + 9)

        TESTS:

        We test the above doctest. The representation depends on the PARI version::

            sage: K.<a> = NumberField(7/9*x^3 + 7/3*x^2 - 56*x + 123)
            sage: N, M1, M2 = K.optimized_representation(); N, M1, M2
            (Number Field in a1 with defining polynomial x^3 - 7*x - 7,
             Ring morphism:
               From: Number Field in a1 with defining polynomial x^3 - 7*x - 7
               To:   Number Field in a with defining polynomial 7/9*x^3 + 7/3*x^2 - 56*x + 123
               Defn: a1 |--> ...,
             Ring morphism:
               From: Number Field in a with defining polynomial 7/9*x^3 + 7/3*x^2 - 56*x + 123
               To:   Number Field in a1 with defining polynomial x^3 - 7*x - 7
               Defn: a |--> ...)
            sage: a1 = M1.domain().gens()[0]
            sage: M2(a) in (-15/7*a1^2 + 9, -60/7*a1^2 + 15*a1 + 39)
            True
            sage: M1(M2(a)) == a
            True
        """
    def optimized_subfields(self, degree: int = 0, name=None, both_maps: bool = True):
        """
        Return optimized representations of many (but *not* necessarily
        all!) subfields of ``self`` of the given ``degree``, or of all possible degrees if
        ``degree`` is 0.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K = NumberField([x^2 + p for p in [5, 3, 2]],'a').absolute_field('b'); K
            Number Field in b with defining polynomial x^8 + 40*x^6 + 352*x^4 + 960*x^2 + 576
            sage: L = K.optimized_subfields(name='b')
            sage: L[0][0]
            Number Field in b0 with defining polynomial x
            sage: L[1][0]
            Number Field in b1 with defining polynomial x^2 - 3*x + 3
            sage: [z[0] for z in L]          # random -- since algorithm is random
            [Number Field in b0 with defining polynomial x - 1,
             Number Field in b1 with defining polynomial x^2 - x + 1,
             Number Field in b2 with defining polynomial x^4 - 5*x^2 + 25,
             Number Field in b3 with defining polynomial x^4 - 2*x^2 + 4,
             Number Field in b4 with defining polynomial x^8 + 4*x^6 + 7*x^4 + 36*x^2 + 81]

        We examine one of the optimized subfields in more detail::

            sage: M, from_M, to_M = L[2]
            sage: M                             # random
            Number Field in b2 with defining polynomial x^4 - 5*x^2 + 25
            sage: from_M     # may be slightly random
            Ring morphism:
              From: Number Field in b2 with defining polynomial x^4 - 5*x^2 + 25
              To:   Number Field in a1 with defining polynomial
                    x^8 + 40*x^6 + 352*x^4 + 960*x^2 + 576
              Defn: b2 |--> -5/1152*a1^7 + 1/96*a1^6 - 97/576*a1^5 + 17/48*a1^4
                            - 95/72*a1^3 + 17/12*a1^2 - 53/24*a1 - 1

        The ``to_M`` map is ``None``, since there is no map from `K` to `M`::

            sage: to_M

        We apply the from_M map to the generator of M, which gives a
        rather large element of `K`::

            sage: from_M(M.0)          # random
            -5/1152*a1^7 + 1/96*a1^6 - 97/576*a1^5 + 17/48*a1^4
             - 95/72*a1^3 + 17/12*a1^2 - 53/24*a1 - 1

        Nevertheless, that large-ish element lies in a degree 4 subfield::

            sage: from_M(M.0).minpoly()   # random
            x^4 - 5*x^2 + 25

        TESTS:

        Number fields defined by non-monic and non-integral
        polynomials are supported (:issue:`252`)::

            sage: K.<a> = NumberField(2*x^4 + 6*x^2 + 1/2)
            sage: K.optimized_subfields()  # random
            [(Number Field in a0 with defining polynomial x,
              Ring morphism:
                From: Number Field in a0 with defining polynomial x
                To:   Number Field in a with defining polynomial 2*x^4 + 6*x^2 + 1/2
                Defn: 0 |--> 0,
              None),
             (Number Field in a1 with defining polynomial x^2 - 2*x + 2,
              Ring morphism:
                From: Number Field in a1 with defining polynomial x^2 - 2*x + 2
                To:   Number Field in a with defining polynomial 2*x^4 + 6*x^2 + 1/2
                Defn: a1 |--> a^3 + 7/2*a + 1,
              None),
             (Number Field in a2 with defining polynomial x^2 - 2*x + 2,
              Ring morphism:
                From: Number Field in a2 with defining polynomial x^2 - 2*x + 2
                To:   Number Field in a with defining polynomial 2*x^4 + 6*x^2 + 1/2
                Defn: a2 |--> -a^3 - 7/2*a + 1,
              None),
             (Number Field in a3 with defining polynomial x^2 - 2,
              Ring morphism:
                From: Number Field in a3 with defining polynomial x^2 - 2
                To:   Number Field in a with defining polynomial 2*x^4 + 6*x^2 + 1/2
                Defn: a3 |--> a^2 + 3/2,
              None),
             (Number Field in a4 with defining polynomial x^2 + 1,
              Ring morphism:
                From: Number Field in a4 with defining polynomial x^2 + 1
                To:   Number Field in a with defining polynomial 2*x^4 + 6*x^2 + 1/2
                Defn: a4 |--> a^3 + 7/2*a,
              None),
             (Number Field in a5 with defining polynomial x^2 + 2,
              Ring morphism:
                From: Number Field in a5 with defining polynomial x^2 + 2
                To:   Number Field in a with defining polynomial 2*x^4 + 6*x^2 + 1/2
                Defn: a5 |--> 2*a^3 + 5*a,
              None),
             (Number Field in a6 with defining polynomial x^4 + 1,
              Ring morphism:
                From: Number Field in a6 with defining polynomial x^4 + 1
                To:   Number Field in a with defining polynomial 2*x^4 + 6*x^2 + 1/2
                Defn: a6 |--> a^3 + 1/2*a^2 + 5/2*a + 3/4,
              Ring morphism:
                From: Number Field in a with defining polynomial 2*x^4 + 6*x^2 + 1/2
                To:   Number Field in a6 with defining polynomial x^4 + 1
                Defn: a |--> -1/2*a6^3 + a6^2 - 1/2*a6)]
        """
    def change_names(self, names):
        """
        Return number field isomorphic to ``self`` but with the given generator
        name.

        INPUT:

        - ``names`` -- should be exactly one variable name

        Also, ``K.structure()`` returns ``from_K`` and ``to_K``,
        where ``from_K`` is an isomorphism from `K` to ``self`` and ``to_K`` is an
        isomorphism from ``self`` to `K`.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<z> = NumberField(x^2 + 3); K
            Number Field in z with defining polynomial x^2 + 3
            sage: L.<ww> = K.change_names()
            sage: L
            Number Field in ww with defining polynomial x^2 + 3
            sage: L.structure()[0]
            Isomorphism given by variable name change map:
              From: Number Field in ww with defining polynomial x^2 + 3
              To:   Number Field in z with defining polynomial x^2 + 3
            sage: L.structure()[0](ww + 5/3)
            z + 5/3
        """
    def subfields(self, degree: int = 0, name=None):
        """
        Return all subfields of ``self`` of the given ``degree``,
        or of all possible degrees if ``degree`` is 0.  The subfields are returned as
        absolute fields together with an embedding into ``self``.  For the case of the
        field itself, the reverse isomorphism is also provided.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<a> = NumberField([x^3 - 2, x^2 + x + 1])
            sage: K = K.absolute_field('b')
            sage: S = K.subfields()
            sage: len(S)
            6
            sage: [k[0].polynomial() for k in S]
            [x - 3,
             x^2 - 3*x + 9,
             x^3 - 3*x^2 + 3*x + 1,
             x^3 - 3*x^2 + 3*x + 1,
             x^3 - 3*x^2 + 3*x - 17,
             x^6 - 3*x^5 + 6*x^4 - 11*x^3 + 12*x^2 + 3*x + 1]
            sage: R.<t> = QQ[]
            sage: L = NumberField(t^3 - 3*t + 1, 'c')
            sage: [k[1] for k in L.subfields()]
            [Ring morphism:
              From: Number Field in c0 with defining polynomial t
              To:   Number Field in c with defining polynomial t^3 - 3*t + 1
              Defn: 0 |--> 0,
             Ring morphism:
              From: Number Field in c1 with defining polynomial t^3 - 3*t + 1
              To:   Number Field in c with defining polynomial t^3 - 3*t + 1
              Defn: c1 |--> c]
            sage: len(L.subfields(2))
            0
            sage: len(L.subfields(1))
            1

        TESTS:

        Number fields defined by non-monic and non-integral
        polynomials are supported (:issue:`252`)::

            sage: K.<a> = NumberField(2*x^4 + 6*x^2 + 1/2)
            sage: K
            Number Field in a with defining polynomial 2*x^4 + 6*x^2 + 1/2
            sage: sorted([F.discriminant() for F, _, _ in K.subfields()])
            [-8, -4, 1, 8, 256]
        """
    def order(self, *args, **kwds):
        """
        Return the order with given ring generators in the maximal order of
        this number field.

        INPUT:

        - ``gens`` -- list of elements in this number field; if no generators
          are given, just returns the cardinality of this number field
          (`\\infty`) for consistency.

        - ``check_is_integral`` -- boolean (default: ``True``); whether to
          check that each generator is integral

        - ``check_rank`` -- boolean (default: ``True``); whether to check that
          the ring generated by ``gens`` is of full rank

        - ``allow_subfield`` -- boolean (default: ``False``); if ``True`` and
          the generators do not generate an order, i.e., they generate a
          subring of smaller rank, instead of raising an error, return an order
          in a smaller number field

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: k.<i> = NumberField(x^2 + 1)
            sage: k.order(2*i)
            Order of conductor 2 generated by 2*i in Number Field in i with defining polynomial x^2 + 1
            sage: k.order(10*i)
            Order of conductor 10 generated by 10*i in Number Field in i with defining polynomial x^2 + 1
            sage: k.order(3)
            Traceback (most recent call last):
            ...
            ValueError: the rank of the span of gens is wrong
            sage: k.order(i/2)
            Traceback (most recent call last):
            ...
            ValueError: each generator must be integral

        Alternatively, an order can be constructed by adjoining elements to
        `\\ZZ`::

            sage: K.<a> = NumberField(x^3 - 2)
            sage: ZZ[a]
            Order generated by a0 in Number Field in a0 with defining polynomial x^3 - 2 with a0 = a

        TESTS:

        We verify that :issue:`2480` is fixed::

            sage: K.<a> = NumberField(x^4 + 4*x^2 + 2)
            sage: B = K.integral_basis()
            sage: K.order(*B)
            Maximal Order generated by a in Number Field in a with defining polynomial x^4 + 4*x^2 + 2
            sage: K.order(B)
            Maximal Order generated by a in Number Field in a with defining polynomial x^4 + 4*x^2 + 2
            sage: K.order(gens=B)
            Maximal Order generated by a in Number Field in a with defining polynomial x^4 + 4*x^2 + 2
        """
    def free_module(self, base=None, basis=None, map: bool = True):
        """
        Return a vector space `V` and isomorphisms ``self`` `\\to` `V` and `V` `\\to` ``self``.

        INPUT:

        - ``base`` -- a subfield (default: ``None``); the returned vector
          space is over this subfield `R`, which defaults to the base field of this
          function field

        - ``basis`` -- a basis for this field over the base

        - ``maps`` -- boolean (default: ``True``); whether to return
          `R`-linear maps to and from `V`

        OUTPUT:

        - ``V`` -- a vector space over the rational numbers

        - ``from_V`` -- an isomorphism from `V` to ``self`` (if requested)

        - ``to_V`` -- an isomorphism from ``self`` to `V` (if requested)

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: k.<a> = NumberField(x^3 + 2)
            sage: V, from_V, to_V  = k.free_module()
            sage: from_V(V([1,2,3]))
            3*a^2 + 2*a + 1
            sage: to_V(1 + 2*a + 3*a^2)
            (1, 2, 3)
            sage: V
            Vector space of dimension 3 over Rational Field
            sage: to_V
            Isomorphism map:
              From: Number Field in a with defining polynomial x^3 + 2
              To:   Vector space of dimension 3 over Rational Field
            sage: from_V(to_V(2/3*a - 5/8))
            2/3*a - 5/8
            sage: to_V(from_V(V([0,-1/7,0])))
            (0, -1/7, 0)
        """
    def absolute_vector_space(self, *args, **kwds):
        """
        Return vector space over `\\QQ` corresponding to this
        number field, along with maps from that space to this number field
        and in the other direction.

        For an absolute extension this is identical to
        :meth:`vector_space`.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<a> = NumberField(x^3 - 5)
            sage: K.absolute_vector_space()
            (Vector space of dimension 3 over Rational Field,
             Isomorphism map:
              From: Vector space of dimension 3 over Rational Field
              To:   Number Field in a with defining polynomial x^3 - 5,
             Isomorphism map:
              From: Number Field in a with defining polynomial x^3 - 5
              To:   Vector space of dimension 3 over Rational Field)
        """
    def galois_closure(self, names=None, map: bool = False):
        '''
        Return number field `K` that is the Galois closure of ``self``,
        i.e., is generated by all roots of the defining polynomial of
        ``self``, and possibly an embedding of ``self`` into `K`.

        INPUT:

        - ``names`` -- variable name for Galois closure

        - ``map`` -- boolean (default: ``False``); also return an embedding of
          ``self`` into `K`

        EXAMPLES::

            sage: # needs sage.groups
            sage: x = polygen(QQ, \'x\')
            sage: K.<a> = NumberField(x^4 - 2)
            sage: M = K.galois_closure(\'b\'); M
            Number Field in b with defining polynomial x^8 + 28*x^4 + 2500
            sage: L.<a2> = K.galois_closure(); L
            Number Field in a2 with defining polynomial x^8 + 28*x^4 + 2500
            sage: K.galois_group(names=("a3")).order()
            8

        ::

            sage: # needs sage.groups
            sage: phi = K.embeddings(L)[0]
            sage: phi(K.0)
            1/120*a2^5 + 19/60*a2
            sage: phi(K.0).minpoly()
            x^4 - 2

            sage: # needs sage.groups
            sage: L, phi = K.galois_closure(\'b\', map=True)
            sage: L
            Number Field in b with defining polynomial x^8 + 28*x^4 + 2500
            sage: phi
            Ring morphism:
              From: Number Field in a with defining polynomial x^4 - 2
              To:   Number Field in b with defining polynomial x^8 + 28*x^4 + 2500
              Defn: a |--> 1/240*b^5 - 41/120*b

        A cyclotomic field is already Galois::

            sage: # needs sage.groups
            sage: K.<a> = NumberField(cyclotomic_polynomial(23))
            sage: L.<z> = K.galois_closure()
            sage: L
            Number Field in z with defining polynomial
             x^22 + x^21 + x^20 + x^19 + x^18 + x^17 + x^16 + x^15 + x^14 + x^13 + x^12
              + x^11 + x^10 + x^9 + x^8 + x^7 + x^6 + x^5 + x^4 + x^3 + x^2 + x + 1

        TESTS:

        Let\'s make sure we\'re renaming correctly::

            sage: # needs sage.groups
            sage: K.<a> = NumberField(x^4 - 2)
            sage: L, phi = K.galois_closure(\'cc\', map=True)
            sage: L
            Number Field in cc with defining polynomial x^8 + 28*x^4 + 2500
            sage: phi
            Ring morphism:
              From: Number Field in a with defining polynomial x^4 - 2
              To:   Number Field in cc with defining polynomial x^8 + 28*x^4 + 2500
              Defn: a |--> 1/240*cc^5 - 41/120*cc
        '''
    def automorphisms(self):
        """
        Compute all Galois automorphisms of ``self``.

        This uses PARI's :pari:`nfgaloisconj` and is much faster than
        root finding for many fields.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<a> = NumberField(x^2 + 10000)
            sage: K.automorphisms()
            [Ring endomorphism of Number Field in a with defining polynomial x^2 + 10000
               Defn: a |--> a,
             Ring endomorphism of Number Field in a with defining polynomial x^2 + 10000
               Defn: a |--> -a]

        Here's a larger example, that would take some time if we found
        roots instead of using PARI's specialized machinery::

            sage: K = NumberField(x^6 - x^4 - 2*x^2 + 1, 'a')
            sage: len(K.automorphisms())
            2

        `L` is the Galois closure of `K`::

            sage: L = NumberField(x^24 - 84*x^22 + 2814*x^20 - 15880*x^18 - 409563*x^16
            ....:                  - 8543892*x^14 + 25518202*x^12 + 32831026956*x^10
            ....:                  - 672691027218*x^8 - 4985379093428*x^6 + 320854419319140*x^4
            ....:                  + 817662865724712*x^2 + 513191437605441, 'a')
            sage: len(L.automorphisms())
            24

        Number fields defined by non-monic and non-integral
        polynomials are supported (:issue:`252`)::

            sage: R.<x> = QQ[]
            sage: f = 7/9*x^3 + 7/3*x^2 - 56*x + 123
            sage: K.<a> = NumberField(f)
            sage: A = K.automorphisms(); A
            [Ring endomorphism of Number Field in a with defining polynomial 7/9*x^3 + 7/3*x^2 - 56*x + 123
               Defn: a |--> a,
             Ring endomorphism of Number Field in a with defining polynomial 7/9*x^3 + 7/3*x^2 - 56*x + 123
               Defn: a |--> -7/15*a^2 - 18/5*a + 96/5,
             Ring endomorphism of Number Field in a with defining polynomial 7/9*x^3 + 7/3*x^2 - 56*x + 123
               Defn: a |--> 7/15*a^2 + 13/5*a - 111/5]
            sage: prod(x - sigma(a) for sigma in A) == f.monic()
            True
        """
    @cached_method
    def embeddings(self, K):
        """
        Compute all field embeddings of this field into the field `K` (which need
        not even be a number field, e.g., it could be the complex numbers).
        This will return an identical result when given `K` as input again.

        If possible, the most natural embedding of this field into `K`
        is put first in the list.

        INPUT:

        - ``K`` -- a field

        EXAMPLES::

            sage: # needs sage.groups
            sage: x = polygen(QQ, 'x')
            sage: K.<a> = NumberField(x^3 - 2)
            sage: L.<a1> = K.galois_closure(); L
            Number Field in a1 with defining polynomial x^6 + 108
            sage: K.embeddings(L)[0]
            Ring morphism:
              From: Number Field in a with defining polynomial x^3 - 2
              To:   Number Field in a1 with defining polynomial x^6 + 108
              Defn: a |--> 1/18*a1^4
            sage: K.embeddings(L) is K.embeddings(L)
            True

        We embed a quadratic field into a cyclotomic field::

            sage: L.<a> = QuadraticField(-7)
            sage: K = CyclotomicField(7)
            sage: L.embeddings(K)
            [Ring morphism:
               From: Number Field in a with defining polynomial x^2 + 7 with a = 2.645751311064591?*I
               To:   Cyclotomic Field of order 7 and degree 6
               Defn: a |--> 2*zeta7^4 + 2*zeta7^2 + 2*zeta7 + 1,
             Ring morphism:
               From: Number Field in a with defining polynomial x^2 + 7 with a = 2.645751311064591?*I
               To:   Cyclotomic Field of order 7 and degree 6
               Defn: a |--> -2*zeta7^4 - 2*zeta7^2 - 2*zeta7 - 1]

        We embed a cubic field in the complex numbers::

            sage: x = polygen(QQ, 'x')
            sage: K.<a> = NumberField(x^3 - 2)
            sage: K.embeddings(CC)  # abs tol 1e-12
            [Ring morphism:
               From: Number Field in a with defining polynomial x^3 - 2
               To:   Complex Field with 53 bits of precision
               Defn: a |--> -0.629960524947437 - 1.09112363597172*I,
             Ring morphism:
               From: Number Field in a with defining polynomial x^3 - 2
               To:   Complex Field with 53 bits of precision
               Defn: a |--> -0.629960524947437 + 1.09112363597172*I,
             Ring morphism:
               From: Number Field in a with defining polynomial x^3 - 2
               To:   Complex Field with 53 bits of precision
               Defn: a |--> 1.25992104989487]

        Some more (possible and impossible) embeddings of cyclotomic fields::

            sage: CyclotomicField(5).embeddings(QQbar)
            [Ring morphism:
               From: Cyclotomic Field of order 5 and degree 4
               To:   Algebraic Field
               Defn: zeta5 |--> 0.3090169943749474? + 0.9510565162951536?*I,
             Ring morphism:
               From: Cyclotomic Field of order 5 and degree 4
               To:   Algebraic Field
               Defn: zeta5 |--> -0.8090169943749474? + 0.5877852522924731?*I,
             Ring morphism:
               From: Cyclotomic Field of order 5 and degree 4
               To:   Algebraic Field
               Defn: zeta5 |--> -0.8090169943749474? - 0.5877852522924731?*I,
             Ring morphism:
               From: Cyclotomic Field of order 5 and degree 4
               To:   Algebraic Field
               Defn: zeta5 |--> 0.3090169943749474? - 0.9510565162951536?*I]
            sage: CyclotomicField(3).embeddings(CyclotomicField(7))
            []
            sage: CyclotomicField(3).embeddings(CyclotomicField(6))
            [Ring morphism:
               From: Cyclotomic Field of order 3 and degree 2
               To:   Cyclotomic Field of order 6 and degree 2
               Defn: zeta3 |--> zeta6 - 1,
             Ring morphism:
               From: Cyclotomic Field of order 3 and degree 2
               To:   Cyclotomic Field of order 6 and degree 2
               Defn: zeta3 |--> -zeta6]

        Test that :issue:`15053` is fixed::

            sage: K = NumberField(x^3 - 2, 'a')
            sage: K.embeddings(GF(3))
            []
        """
    def minkowski_embedding(self, B=None, prec=None):
        '''
        Return an `n \\times n` matrix over ``RDF`` whose columns are the images of the
        basis `\\{1, \\alpha, \\dots, \\alpha^{n-1}\\}` of ``self`` over
        `\\QQ` (as vector spaces), where here
        `\\alpha` is the generator of ``self`` over
        `\\QQ`, i.e. ``self.gen(0)``. If `B` is not ``None``, return
        the images of the vectors in `B` as the columns instead. If ``prec`` is
        not ``None``, use ``RealField(prec)`` instead of ``RDF``.

        This embedding is the so-called "Minkowski embedding" of a number
        field in `\\RR^n`: given the `n` embeddings
        `\\sigma_1, \\dots, \\sigma_n` of ``self`` in
        `\\CC`, write `\\sigma_1, \\dots, \\sigma_r`
        for the real embeddings, and
        `\\sigma_{r+1}, \\dots, \\sigma_{r+s}` for choices of one of
        each pair of complex conjugate embeddings (in our case, we simply
        choose the one where the image of `\\alpha` has positive
        real part). Here `(r,s)` is the signature of ``self``. Then the
        Minkowski embedding is given by

        .. MATH::

            x \\mapsto ( \\sigma_1(x), \\dots,
                     \\sigma_r(x), \\sqrt{2}\\Re(\\sigma_{r+1}(x)),
                     \\sqrt{2}\\Im(\\sigma_{r+1}(x)), \\dots,
                     \\sqrt{2}\\Re(\\sigma_{r+s}(x)),
                     \\sqrt{2}\\Im(\\sigma_{r+s}(x)))

        Equivalently, this is an embedding of ``self`` in `\\RR^n` so
        that the usual norm on `\\RR^n` coincides with
        `|x| = \\sum_i |\\sigma_i(x)|^2` on ``self``.

        .. TODO::

            This could be much improved by implementing homomorphisms
            over VectorSpaces.

        EXAMPLES::

            sage: x = polygen(QQ, \'x\')
            sage: F.<alpha> = NumberField(x^3 + 2)
            sage: F.minkowski_embedding()
            [ 1.00000000000000 -1.25992104989487  1.58740105196820]
            [ 1.41421356237... 0.8908987181... -1.12246204830...]
            [0.000000000000000  1.54308184421...  1.94416129723...]
            sage: F.minkowski_embedding([1, alpha+2, alpha^2-alpha])
            [ 1.00000000000000 0.740078950105127  2.84732210186307]
            [ 1.41421356237...  3.7193258428... -2.01336076644...]
            [0.000000000000000  1.54308184421... 0.40107945302...]
            sage: F.minkowski_embedding() * (alpha + 2).vector().column()
            [0.740078950105127]
            [ 3.7193258428...]
            [ 1.54308184421...]
        '''
    def logarithmic_embedding(self, prec: int = 53):
        """
        Return the morphism of ``self`` under the logarithmic embedding
        in the category Set.

        The logarithmic embedding is defined as a map from the number field
        ``self`` to `\\RR^n`.

        It is defined under Definition 4.9.6 in [Coh1993]_.

        INPUT:

        - ``prec`` -- desired floating point precision

        OUTPUT: the morphism of ``self`` under the logarithmic embedding in the
        category Set

        EXAMPLES::

            sage: CF.<a> = CyclotomicField(5)
            sage: f = CF.logarithmic_embedding()
            sage: f(0)
            (-1, -1)
            sage: f(7)
            (3.89182029811063, 3.89182029811063)

        ::

            sage: x = polygen(QQ, 'x')
            sage: K.<a> = NumberField(x^3 + 5)
            sage: f = K.logarithmic_embedding()
            sage: f(0)
            (-1, -1)
            sage: f(7)
            (1.94591014905531, 3.89182029811063)

        ::

            sage: F.<a> = NumberField(x^4 - 8*x^2 + 3)
            sage: f = F.logarithmic_embedding()
            sage: f(0)
            (-1, -1, -1, -1)
            sage: f(7)
            (1.94591014905531, 1.94591014905531, 1.94591014905531, 1.94591014905531)
        """
    def places(self, all_complex: bool = False, prec=None):
        """
        Return the collection of all infinite places of ``self``.

        By default, this returns the set of real places as
        homomorphisms into ``RIF`` first, followed by a choice of one of
        each pair of complex conjugate homomorphisms into ``CIF``.

        On the other hand, if ``prec`` is not ``None``, we simply return places
        into ``RealField(prec)`` and ``ComplexField(prec)`` (or ``RDF``, ``CDF`` if
        ``prec=53``). One can also use ``prec=infinity``, which returns embeddings
        into the field `\\overline{\\QQ}` of algebraic numbers (or its subfield
        `\\mathbb{A}` of algebraic reals); this permits exact computation, but
        can be extremely slow.

        There is an optional flag ``all_complex``, which defaults to ``False``. If
        ``all_complex`` is ``True``, then the real embeddings are returned as
        embeddings into ``CIF`` instead of ``RIF``.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: F.<alpha> = NumberField(x^3 - 100*x + 1); F.places()
            [Ring morphism:
               From: Number Field in alpha with defining polynomial x^3 - 100*x + 1
               To:   Real Field with 106 bits of precision
               Defn: alpha |--> -10.00499625499181184573367219280,
             Ring morphism:
               From: Number Field in alpha with defining polynomial x^3 - 100*x + 1
               To:   Real Field with 106 bits of precision
               Defn: alpha |--> 0.01000001000003000012000055000273,
             Ring morphism:
               From: Number Field in alpha with defining polynomial x^3 - 100*x + 1
               To:   Real Field with 106 bits of precision
               Defn: alpha |--> 9.994996244991781845613530439509]

        ::

            sage: F.<alpha> = NumberField(x^3 + 7); F.places()
            [Ring morphism:
               From: Number Field in alpha with defining polynomial x^3 + 7
               To:   Real Field with 106 bits of precision
               Defn: alpha |--> -1.912931182772389101199116839549,
             Ring morphism:
               From: Number Field in alpha with defining polynomial x^3 + 7
               To:   Complex Field with 53 bits of precision
               Defn: alpha |--> 0.956465591386195 + 1.65664699997230*I]

        ::

            sage: F.<alpha> = NumberField(x^3 + 7) ; F.places(all_complex=True)
            [Ring morphism:
               From: Number Field in alpha with defining polynomial x^3 + 7
               To:   Complex Field with 53 bits of precision
               Defn: alpha |--> -1.91293118277239,
             Ring morphism:
               From: Number Field in alpha with defining polynomial x^3 + 7
               To:   Complex Field with 53 bits of precision
               Defn: alpha |--> 0.956465591386195 + 1.65664699997230*I]
            sage: F.places(prec=10)
            [Ring morphism:
               From: Number Field in alpha with defining polynomial x^3 + 7
               To:   Real Field with 10 bits of precision
               Defn: alpha |--> -1.9,
             Ring morphism:
               From: Number Field in alpha with defining polynomial x^3 + 7
               To:   Complex Field with 10 bits of precision
               Defn: alpha |--> 0.96 + 1.7*I]
        """
    def real_places(self, prec=None):
        """
        Return all real places of ``self`` as homomorphisms into ``RIF``.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: F.<alpha> = NumberField(x^4 - 7) ; F.real_places()
            [Ring morphism:
               From: Number Field in alpha with defining polynomial x^4 - 7
               To:   Real Field with 106 bits of precision
               Defn: alpha |--> -1.626576561697785743211232345494,
             Ring morphism:
               From: Number Field in alpha with defining polynomial x^4 - 7
               To:   Real Field with 106 bits of precision
               Defn: alpha |--> 1.626576561697785743211232345494]
        """
    def abs_val(self, v, iota, prec=None):
        """
        Return the value `|\\iota|_{v}`.

        INPUT:

        - ``v`` -- a place of ``K``, finite (a fractional ideal) or infinite (element of ``K.places(prec)``)
        - ``iota`` -- an element of ``K``
        - ``prec`` -- (default: ``None``) the precision of the real field

        OUTPUT: the absolute value as a real number

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<xi> = NumberField(x^3 - 3)
            sage: phi_real = K.places()[0]
            sage: phi_complex = K.places()[1]
            sage: v_fin = tuple(K.primes_above(3))[0]

            sage: K.abs_val(phi_real, xi^2)
            2.08008382305190

            sage: K.abs_val(phi_complex, xi^2)
            4.32674871092223

            sage: K.abs_val(v_fin, xi^2)
            0.111111111111111

        Check that :issue:`28345` is fixed::

            sage: K.abs_val(v_fin, K.zero())
            0.000000000000000
        """
    def relativize(self, alpha, names, structure=None):
        """
        Given an element in ``self`` or an embedding of a subfield into ``self``,
        return a relative number field `K` isomorphic to ``self`` that is relative
        over the absolute field `\\QQ(\\alpha)` or the domain of `\\alpha`, along
        with isomorphisms from `K` to ``self`` and from ``self`` to `K`.

        INPUT:

        - ``alpha`` -- an element of ``self``  or an embedding of a subfield into
          ``self``
        - ``names`` -- 2-tuple of names of generator for output field `K` and the
          subfield `\\QQ(\\alpha)`
        - ``structure`` -- an instance of
          :class:`structure.NumberFieldStructure` or ``None`` (default:
          ``None``), if ``None``, then the resulting field's :meth:`structure`
          will return isomorphisms from and to this field. Otherwise, the field
          will be equipped with ``structure``.

        OUTPUT: `K` -- relative number field

        Also, ``K.structure()`` returns ``from_K`` and ``to_K``, where
        ``from_K`` is an isomorphism from `K` to ``self`` and ``to_K`` is an isomorphism
        from ``self`` to `K`.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<a> = NumberField(x^10 - 2)
            sage: L.<c,d> = K.relativize(a^4 + a^2 + 2); L
            Number Field in c with defining polynomial
             x^2 - 1/5*d^4 + 8/5*d^3 - 23/5*d^2 + 7*d - 18/5 over its base field
            sage: c.absolute_minpoly()
            x^10 - 2
            sage: d.absolute_minpoly()
            x^5 - 10*x^4 + 40*x^3 - 90*x^2 + 110*x - 58
            sage: (a^4 + a^2 + 2).minpoly()
            x^5 - 10*x^4 + 40*x^3 - 90*x^2 + 110*x - 58
            sage: from_L, to_L = L.structure()
            sage: to_L(a)
            c
            sage: to_L(a^4 + a^2 + 2)
            d
            sage: from_L(to_L(a^4 + a^2 + 2))
            a^4 + a^2 + 2

        The following demonstrates distinct embeddings of a subfield into a
        larger field::

            sage: K.<a> = NumberField(x^4 + 2*x^2 + 2)
            sage: K0 = K.subfields(2)[0][0]; K0
            Number Field in a0 with defining polynomial x^2 - 2*x + 2
            sage: rho, tau = K0.embeddings(K)
            sage: L0 = K.relativize(rho(K0.gen()), 'b'); L0
            Number Field in b0 with defining polynomial x^2 - b1 + 2 over its base field
            sage: L1 = K.relativize(rho, 'b'); L1
            Number Field in b with defining polynomial x^2 - a0 + 2 over its base field
            sage: L2 = K.relativize(tau, 'b'); L2
            Number Field in b with defining polynomial x^2 + a0 over its base field
            sage: L0.base_field() is K0
            False
            sage: L1.base_field() is K0
            True
            sage: L2.base_field() is K0
            True

        Here we see that with the different embeddings, the relative norms are
        different::

            sage: a0 = K0.gen()
            sage: L1_into_K, K_into_L1 = L1.structure()
            sage: L2_into_K, K_into_L2 = L2.structure()
            sage: len(K.factor(41))
            4
            sage: w1 = -a^2 + a + 1; P = K.ideal([w1])
            sage: Pp = L1.ideal(K_into_L1(w1)).ideal_below(); Pp == K0.ideal([4*a0 + 1])
            True
            sage: Pp == w1.norm(rho)
            True

            sage: w2 = a^2 + a - 1; Q = K.ideal([w2])
            sage: Qq = L2.ideal(K_into_L2(w2)).ideal_below(); Qq == K0.ideal([-4*a0 + 9])
            True
            sage: Qq == w2.norm(tau)
            True

            sage: Pp == Qq
            False

        TESTS:

        We can relativize over the whole field::

            sage: K.<a> = NumberField(x^4 + 2*x^2 + 2)
            sage: K.relativize(K.gen(), 'a')
            Number Field in a0 with defining polynomial x - a1 over its base field
            sage: K.relativize(2*K.gen(), 'a')
            Number Field in a0 with defining polynomial x - 1/2*a1 over its base field

        We can relativize over the prime field::

            sage: L = K.relativize(K(1), 'a'); L
            Number Field in a0 with defining polynomial x^4 + 2*x^2 + 2 over its base field
            sage: L.base_field()
            Number Field in a1 with defining polynomial x - 1
            sage: L.base_field().base_field()
            Rational Field

            sage: L = K.relativize(K(2), 'a'); L
            Number Field in a0 with defining polynomial x^4 + 2*x^2 + 2 over its base field
            sage: L.base_field()
            Number Field in a1 with defining polynomial x - 2
            sage: L.base_field().base_field()
            Rational Field

            sage: L = K.relativize(K(0), 'a'); L
            Number Field in a0 with defining polynomial x^4 + 2*x^2 + 2 over its base field
            sage: L.base_field()
            Number Field in a1 with defining polynomial x
            sage: L.base_field().base_field()
            Rational Field

        We can relativize over morphisms returned by self.subfields()::

            sage: L = NumberField(x^4 + 1, 'a')
            sage: [L.relativize(h, 'c') for (f,h,i) in L.subfields()]
            [Number Field in c with defining polynomial x^4 + 1 over its base field,
             Number Field in c with defining polynomial x^2 - a1*x + 1 over its base field,
             Number Field in c with defining polynomial x^2 - 1/2*a2 over its base field,
             Number Field in c with defining polynomial x^2 - a3*x - 1 over its base field,
             Number Field in c with defining polynomial x - a4 over its base field]

        We can relativize over a relative field::

            sage: K.<z> = CyclotomicField(16)
            sage: L, L_into_K, _ = K.subfields(4)[0]; L
            Number Field in z0 with defining polynomial x^4 + 16
             with z0 = 1.414213562373095? + 1.414213562373095?*I
            sage: F, F_into_L, _ = L.subfields(2)[0]; F
            Number Field in z0_0 with defining polynomial x^2 + 64 with z0_0 = 8*I

            sage: L_over_F = L.relativize(F_into_L, 'c'); L_over_F
            Number Field in c with defining polynomial x^2 - 1/2*z0_0 over its base field
            sage: L_over_F_into_L, _ = L_over_F.structure()

            sage: K_over_rel = K.relativize(L_into_K * L_over_F_into_L, 'a'); K_over_rel
            Number Field in a with defining polynomial x^2 - 1/2*c over its base field
            sage: K_over_rel.base_field() is L_over_F
            True
            sage: K_over_rel.structure()
            (Relative number field morphism:
              From: Number Field in a with defining polynomial x^2 - 1/2*c over its base field
              To:   Cyclotomic Field of order 16 and degree 8
              Defn: a |--> z
                    c |--> 2*z^2
                    z0_0 |--> 8*z^4, Ring morphism:
              From: Cyclotomic Field of order 16 and degree 8
              To:   Number Field in a with defining polynomial x^2 - 1/2*c over its base field
              Defn: z |--> a)

        We can relativize over a really large field::

            sage: K.<a> = CyclotomicField(3^3*2^3)
            sage: R = K.relativize(a^(3^2), 't'); R
            Number Field in t0 with defining polynomial x^9 - t1 over its base field
            sage: R.structure()
            (Relative number field morphism:
              From: Number Field in t0 with defining polynomial x^9 - t1 over its base field
              To:   Cyclotomic Field of order 216 and degree 72
              Defn: t0 |--> a
                    t1 |--> a^9,
             Ring morphism:
              From: Cyclotomic Field of order 216 and degree 72
              To:   Number Field in t0 with defining polynomial x^9 - t1 over its base field
              Defn: a |--> t0)

        Only one name is required when a morphism is given (fixing :issue:`12005`)::

            sage: R.<x> = PolynomialRing(QQ)
            sage: K.<i> = NumberField(x^2 + 1)
            sage: L.<b> = NumberField(x^4 - x^2 + 1)
            sage: phi = K.hom(b^3, L)
            sage: M.<r> = L.relativize(phi)
            sage: M
            Number Field in r with defining polynomial x^2 - i*x - 1 over its base field
            sage: M.base_field()
            Number Field in i with defining polynomial x^2 + 1

        See :issue:`27469`::

            sage: L.<z24> = CyclotomicField(24)
            sage: K.<z8> = L.subfield(z24^3)[0]
            sage: L.relativize(K.hom(L), L.variable_name()+'0' )
            Number Field in z2400 with defining polynomial x^2 + z240^3*x - z240^2 over its base field
        """
    def absolute_degree(self):
        """
        A synonym for :meth:`degree`.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<i> = NumberField(x^2 + 1)
            sage: K.absolute_degree()
            2
        """
    def relative_degree(self):
        """
        A synonym for :meth:`degree`.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<i> = NumberField(x^2 + 1)
            sage: K.relative_degree()
            2
        """
    def relative_polynomial(self):
        """
        A synonym for :meth:`polynomial`.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<i> = NumberField(x^2 + 1)
            sage: K.relative_polynomial()
            x^2 + 1
        """
    def relative_vector_space(self, *args, **kwds):
        """
        A synonym for :meth:`vector_space`.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<i> = NumberField(x^2 + 1)
            sage: K.relative_vector_space()
            (Vector space of dimension 2 over Rational Field,
             Isomorphism map:
              From: Vector space of dimension 2 over Rational Field
              To:   Number Field in i with defining polynomial x^2 + 1,
             Isomorphism map:
              From: Number Field in i with defining polynomial x^2 + 1
              To:   Vector space of dimension 2 over Rational Field)
        """
    def absolute_discriminant(self):
        """
        A synonym for :meth:`discriminant`.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<i> = NumberField(x^2 + 1)
            sage: K.absolute_discriminant()
            -4
        """
    def relative_discriminant(self):
        """
        A synonym for :meth:`discriminant`.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<i> = NumberField(x^2 + 1)
            sage: K.relative_discriminant()
            -4
        """
    def absolute_different(self):
        """
        A synonym for :meth:`different`.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<i> = NumberField(x^2 + 1)
            sage: K.absolute_different()
            Fractional ideal (2)
        """
    def relative_different(self):
        """
        A synonym for :meth:`different`.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<i> = NumberField(x^2 + 1)
            sage: K.relative_different()
            Fractional ideal (2)
        """
    def hilbert_symbol(self, a, b, P=None):
        """
        Return the Hilbert symbol `(a,b)_P` for a prime `P` of ``self``
        and nonzero elements `a` and `b` of ``self``.

        If `P` is omitted, return the global Hilbert symbol `(a,b)` instead.

        INPUT:

        - ``a``, ``b`` -- elements of ``self``

        - ``P`` -- (default: ``None``) if ``None``, compute the global
          symbol.  Otherwise, `P` should be either a prime ideal of ``self``
          (which may also be given as a generator or set of generators)
          or a real or complex embedding.

        OUTPUT: if `a` or `b` is zero, returns 0

        If `a` and `b` are nonzero and `P` is specified, returns
        the Hilbert symbol `(a,b)_P`, which is `1` if the equation
        `a x^2 + b y^2 = 1` has a solution in the completion of
        ``self`` at `P`, and is `-1` otherwise.

        If `a` and `b` are nonzero and `P` is unspecified, returns `1`
        if the equation has a solution in ``self`` and `-1` otherwise.

        EXAMPLES:

        Some global examples::

            sage: x = polygen(QQ, 'x')
            sage: K.<a> = NumberField(x^2 - 23)
            sage: K.hilbert_symbol(0, a + 5)
            0
            sage: K.hilbert_symbol(a, 0)
            0
            sage: K.hilbert_symbol(-a, a + 1)
            1
            sage: K.hilbert_symbol(-a, a + 2)
            -1
            sage: K.hilbert_symbol(a, a + 5)
            -1

        That the latter two are unsolvable should be visible in local
        obstructions.  For the first, this is a prime ideal above 19.
        For the second, the ramified prime above 23::

            sage: K.hilbert_symbol(-a, a + 2, a + 2)
            -1
            sage: K.hilbert_symbol(a, a + 5, K.ideal(23).factor()[0][0])
            -1

        More local examples::

            sage: K.hilbert_symbol(a, 0, K.fractional_ideal(5))
            0
            sage: K.hilbert_symbol(a, a + 5, K.fractional_ideal(5))
            1
            sage: K.hilbert_symbol(a + 1, 13, (a+6)*K)
            -1
            sage: [emb1, emb2] = K.embeddings(AA)
            sage: K.hilbert_symbol(a, -1, emb1)
            -1
            sage: K.hilbert_symbol(a, -1, emb2)
            1

        Ideals P can be given by generators::

            sage: K.<a> = NumberField(x^5 - 23)
            sage: pi = 2*a^4 + 3*a^3 + 4*a^2 + 15*a + 11
            sage: K.hilbert_symbol(a, a + 5, pi)
            1
            sage: rho = 2*a^4 + 3*a^3 + 4*a^2 + 15*a + 11
            sage: K.hilbert_symbol(a, a + 5, rho)
            1

        This also works for non-principal ideals::

            sage: K.<a> = QuadraticField(-5)
            sage: P = K.ideal(3).factor()[0][0]
            sage: P.gens_reduced()  # random, could be the other factor
            (3, a + 1)
            sage: K.hilbert_symbol(a, a + 3, P)
            1
            sage: K.hilbert_symbol(a, a + 3, [3, a+1])
            1

        Primes above 2::

            sage: K.<a> = NumberField(x^5 - 23)
            sage: p = [p[0] for p in (2*K).factor() if p[0].norm() == 16][0]
            sage: K.hilbert_symbol(a, a + 5, p)
            1
            sage: K.hilbert_symbol(a, 2, p)
            1
            sage: K.hilbert_symbol(-1, a - 2, p)
            -1

        Various real fields are allowed::

            sage: K.<a> = NumberField(x^3+x+1)
            sage: K.hilbert_symbol(a/3, 1/2, K.embeddings(RDF)[0])
            1
            sage: K.hilbert_symbol(a/5, -1, K.embeddings(RR)[0])
            -1
            sage: [K.hilbert_symbol(a, -1, e) for e in K.embeddings(AA)]
            [-1]

        Real embeddings are not allowed to be disguised as complex embeddings::

            sage: K.<a> = QuadraticField(5)
            sage: K.hilbert_symbol(-1, -1, K.embeddings(CC)[0])
            Traceback (most recent call last):
            ...
            ValueError: Possibly real place (=Ring morphism:
              From: Number Field in a with defining polynomial x^2 - 5
                    with a = 2.236067977499790?
              To:   Complex Field with 53 bits of precision
              Defn: a |--> -2.23606797749979)
            given as complex embedding in hilbert_symbol. Is it real or complex?
            sage: K.hilbert_symbol(-1, -1, K.embeddings(QQbar)[0])
            Traceback (most recent call last):
            ...
            ValueError: Possibly real place (=Ring morphism:
              From: Number Field in a with defining polynomial x^2 - 5
                    with a = 2.236067977499790?
              To:   Algebraic Field
              Defn: a |--> -2.236067977499790?)
            given as complex embedding in hilbert_symbol. Is it real or complex?
            sage: K.<b> = QuadraticField(-5)
            sage: K.hilbert_symbol(-1, -1, K.embeddings(CDF)[0])
            1
            sage: K.hilbert_symbol(-1, -1, K.embeddings(QQbar)[0])
            1

        `a` and `b` do not have to be integral or coprime::

            sage: K.<i> = QuadraticField(-1)
            sage: K.hilbert_symbol(1/2, 1/6, 3*K)
            1
            sage: p = 1 + i
            sage: K.hilbert_symbol(p, p, p)
            1
            sage: K.hilbert_symbol(p, 3*p, p)
            -1
            sage: K.hilbert_symbol(3, p, p)
            -1
            sage: K.hilbert_symbol(1/3, 1/5, 1 + i)
            1
            sage: L = QuadraticField(5, 'a')
            sage: L.hilbert_symbol(-3, -1/2, 2)
            1

        Various other examples::

            sage: K.<a> = NumberField(x^3 + x + 1)
            sage: K.hilbert_symbol(-6912, 24, -a^2 - a - 2)
            1
            sage: K.<a> = NumberField(x^5 - 23)
            sage: P = K.ideal(-1105*a^4 + 1541*a^3 - 795*a^2 - 2993*a + 11853)
            sage: Q = K.ideal(-7*a^4 + 13*a^3 - 13*a^2 - 2*a + 50)
            sage: b = -a+5
            sage: K.hilbert_symbol(a, b, P)
            1
            sage: K.hilbert_symbol(a, b, Q)
            1
            sage: K.<a> = NumberField(x^5 - 23)
            sage: P = K.ideal(-1105*a^4 + 1541*a^3 - 795*a^2 - 2993*a + 11853)
            sage: K.hilbert_symbol(a, a + 5, P)
            1
            sage: K.hilbert_symbol(a, 2, P)
            1
            sage: K.hilbert_symbol(a + 5, 2, P)
            -1
            sage: K.<a> = NumberField(x^3 - 4*x + 2)
            sage: K.hilbert_symbol(2, -2, K.primes_above(2)[0])
            1

        Check that the bug reported at :issue:`16043` has been fixed::

            sage: K.<a> = NumberField(x^2 + 5)
            sage: p = K.primes_above(2)[0]; p
            Fractional ideal (2, a + 1)
            sage: K.hilbert_symbol(2*a, -1, p)
            1
            sage: K.hilbert_symbol(2*a, 2, p)
            -1
            sage: K.hilbert_symbol(2*a, -2, p)
            -1

        AUTHOR:

        - Aly Deines (2010-08-19): part of the doctests

        - Marco Streng (2010-12-06)
        """
    def hilbert_symbol_negative_at_S(self, S, b, check: bool = True):
        """
        Return `a` such that the Hilbert conductor of `a` and `b` is `S`.

        INPUT:

        - ``S`` -- list of places (or prime ideals) of even cardinality
        - ``b`` -- a nonzero rational number which is a non-square locally
          at every place in `S`
        - ``check`` -- boolean (default: ``True``); perform additional checks
          on the input and confirm the output

        OUTPUT:

        - an element `a` that has negative Hilbert symbol `(a,b)_p` for
          every (finite and infinite) place `p` in `S`.

        ALGORITHM:

        The implementation is following algorithm 3.4.1 in [Kir2016]_.
        We note that class and unit groups are computed using the generalized
        Riemann hypothesis. If it is false, this may result in an infinite loop.
        Nevertheless, if the algorithm terminates the output is correct.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<a> = NumberField(x^2 + 20072)
            sage: S = [K.primes_above(3)[0], K.primes_above(23)[0]]
            sage: b = K.hilbert_symbol_negative_at_S(S, a + 1)
            sage: [K.hilbert_symbol(b, a + 1, p) for p in S]
            [-1, -1]
            sage: K.<d> = CyclotomicField(11)
            sage: S = [K.primes_above(2)[0], K.primes_above(11)[0]]
            sage: b = d + 5
            sage: a = K.hilbert_symbol_negative_at_S(S, b)
            sage: [K.hilbert_symbol(a,b,p) for p in S]
            [-1, -1]
            sage: k.<c> = K.maximal_totally_real_subfield()[0]
            sage: S = [k.primes_above(3)[0], k.primes_above(5)[0]]
            sage: S += k.real_places()[:2]
            sage: b = 5 + c + c^9
            sage: a = k.hilbert_symbol_negative_at_S(S, b)
            sage: [k.hilbert_symbol(a, b, p) for p in S]
            [-1, -1, -1, -1]

        Note that the closely related Hilbert conductor
        takes only the finite places into account::

            sage: k.hilbert_conductor(a, b)
            Fractional ideal (15)


        TESTS::

            sage: K.<a> = NumberField(x^2 + 20072)
            sage: S = [K.primes_above(3)[0], K.primes_above(23)[0]]
            sage: s = K.hilbert_symbol_negative_at_S(S, a + 1)

        AUTHORS:

        - Simon Brandhorst, Anna Haensch (01-05-2018)
        """
    def hilbert_conductor(self, a, b):
        """
        This is the product of all (finite) primes where the Hilbert symbol is `-1`.
        What is the same, this is the (reduced) discriminant of the quaternion
        algebra `(a,b)` over a number field.

        INPUT:

        - ``a``, ``b`` -- elements of the number field ``self``

        OUTPUT: squarefree ideal of the ring of integers of ``self``

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: F.<a> = NumberField(x^2 - x - 1)
            sage: F.hilbert_conductor(2*a, F(-1))
            Fractional ideal (2)
            sage: K.<b> = NumberField(x^3 - 4*x + 2)
            sage: K.hilbert_conductor(K(2), K(-2))
            Fractional ideal (1)
            sage: K.hilbert_conductor(K(2*b), K(-2))
            Fractional ideal (b^2 + b - 2)

        AUTHOR:

        - Aly Deines
        """
    def elements_of_bounded_height(self, **kwds):
        """
        Return an iterator over the elements of ``self`` with relative
        multiplicative height at most ``bound``.

        This algorithm computes 2 lists: `L` containing elements `x` in `K` such that
        `H_k(x) \\leq B`, and a list `L'` containing elements `x` in `K` that, due to
        floating point issues,
        may be slightly larger than the bound. This can be controlled
        by lowering the tolerance.

        In the current implementation, both lists `(L,L')` are merged and returned in
        form of iterator.

        ALGORITHM:

        This is an implementation of the revised algorithm (Algorithm 4) in
        [DK2013]_. Algorithm 5 is used for imaginary quadratic fields.

        INPUT: keyword arguments:

        - ``bound`` -- a real number

        - ``tolerance`` -- (default: 0.01) a rational number in `(0,1]`

        - ``precision`` -- (default: 53) a positive integer

        OUTPUT: an iterator of number field elements

        EXAMPLES:

        There are no elements in a number field with multiplicative height less
        than 1::

            sage: x = polygen(QQ, 'x')
            sage: K.<g> = NumberField(x^5 - x + 19)
            sage: list(K.elements_of_bounded_height(bound=0.9))
            []

        The only elements in a number field of height 1 are 0 and the roots of
        unity::

            sage: K.<a> = NumberField(x^2 + x + 1)
            sage: list(K.elements_of_bounded_height(bound=1))
            [0, a + 1, a, -1, -a - 1, -a, 1]

        ::

            sage: K.<a> = CyclotomicField(20)
            sage: len(list(K.elements_of_bounded_height(bound=1)))
            21

        The elements in the output iterator all have relative multiplicative
        height at most the input bound::

            sage: K.<a> = NumberField(x^6 + 2)
            sage: L = K.elements_of_bounded_height(bound=5)
            sage: for t in L:
            ....:     exp(6*t.global_height())
            1.00000000000000
            1.00000000000000
            1.00000000000000
            2.00000000000000
            2.00000000000000
            2.00000000000000
            2.00000000000000
            4.00000000000000
            4.00000000000000
            4.00000000000000
            4.00000000000000

        ::

            sage: K.<a> = NumberField(x^2 - 71)
            sage: L = K.elements_of_bounded_height(bound=20)
            sage: all(exp(2*t.global_height()) <= 20 for t in L) # long time (5 s)
            True

        ::

            sage: K.<a> = NumberField(x^2 + 17)
            sage: L = K.elements_of_bounded_height(bound=120)
            sage: len(list(L))
            9047

        ::

            sage: K.<a> = NumberField(x^4 - 5)
            sage: L = K.elements_of_bounded_height(bound=50)
            sage: len(list(L)) # long time (2 s)
            2163

        ::

            sage: K.<a> = CyclotomicField(13)
            sage: L = K.elements_of_bounded_height(bound=2)
            sage: len(list(L)) # long time (3 s)
            27

        ::

            sage: K.<a> = NumberField(x^6 + 2)
            sage: L = K.elements_of_bounded_height(bound=60, precision=100)
            sage: len(list(L)) # long time (5 s)
            1899

        ::

            sage: K.<a> = NumberField(x^4 - x^3 - 3*x^2 + x + 1)
            sage: L = K.elements_of_bounded_height(bound=10, tolerance=0.1)
            sage: len(list(L))
            99

        AUTHORS:

        - John Doyle (2013)

        - David Krumm (2013)

        - Raman Raghukul (2018)
        """

class NumberField_cyclotomic(NumberField_absolute, sage.rings.abc.NumberField_cyclotomic):
    """
    Create a cyclotomic extension of the rational field.

    The command ``CyclotomicField(n)`` creates the `n`-th cyclotomic field,
    obtained by adjoining an `n`-th root of unity to the rational field.

    EXAMPLES::

        sage: CyclotomicField(3)
        Cyclotomic Field of order 3 and degree 2
        sage: CyclotomicField(18)
        Cyclotomic Field of order 18 and degree 6
        sage: z = CyclotomicField(6).gen(); z
        zeta6
        sage: z^3
        -1
        sage: (1+z)^3
        6*zeta6 - 3

    ::

        sage: K = CyclotomicField(197)
        sage: loads(K.dumps()) == K
        True
        sage: loads((z^2).dumps()) == z^2
        True

    ::

        sage: cf12 = CyclotomicField(12)
        sage: z12 = cf12.0
        sage: cf6 = CyclotomicField(6)
        sage: z6 = cf6.0
        sage: FF = Frac(cf12['x'])
        sage: x = FF.0
        sage: z6*x^3/(z6 + x)
        zeta12^2*x^3/(x + zeta12^2)

    ::

        sage: cf6 = CyclotomicField(6); z6 = cf6.gen(0)
        sage: cf3 = CyclotomicField(3); z3 = cf3.gen(0)
        sage: cf3(z6)
        zeta3 + 1
        sage: cf6(z3)
        zeta6 - 1
        sage: type(cf6(z3))
        <class 'sage.rings.number_field.number_field_element_quadratic.NumberFieldElement_quadratic'>
        sage: cf1 = CyclotomicField(1); z1 = cf1.0
        sage: cf3(z1)
        1
        sage: type(cf3(z1))
        <class 'sage.rings.number_field.number_field_element_quadratic.NumberFieldElement_quadratic'>
    """
    def __init__(self, n, names, embedding=None, assume_disc_small: bool = False, maximize_at_primes=None) -> None:
        """
        A cyclotomic field, i.e., a field obtained by adjoining an `n`-th
        root of unity to the rational numbers.

        EXAMPLES::

            sage: k = CyclotomicField(3)
            sage: type(k)
            <class 'sage.rings.number_field.number_field.NumberField_cyclotomic_with_category'>

        TESTS:

        The ``gcd`` and ``xgcd`` methods do not agree on this field, see
        :issue:`23274`::

            sage: TestSuite(k).run()
            Failure in _test_gcd_vs_xgcd:
            ...
            AssertionError:... The methods gcd and xgcd disagree on Cyclotomic Field of order 3 and degree 2:
              gcd(0,2) = 1
             xgcd(0,2) = (2, 0, 1)
            ------------------------------------------------------------
            The following tests failed: _test_gcd_vs_xgcd

        ::

            sage: type(CyclotomicField(4).zero())
            <class 'sage.rings.number_field.number_field_element_quadratic.NumberFieldElement_gaussian'>
            sage: type(CyclotomicField(6).one())
            <class 'sage.rings.number_field.number_field_element_quadratic.NumberFieldElement_quadratic'>
            sage: type(CyclotomicField(6).an_element())
            <class 'sage.rings.number_field.number_field_element_quadratic.NumberFieldElement_quadratic'>
            sage: type(CyclotomicField(15).zero())
            <class 'sage.rings.number_field.number_field_element.NumberFieldElement_absolute'>
        """
    def construction(self):
        """
        Return data defining a functorial construction of ``self``.

        EXAMPLES::

            sage: F, R = CyclotomicField(5).construction()
            sage: R
            Rational Field
            sage: F.polys
            [x^4 + x^3 + x^2 + x + 1]
            sage: F.names
            ['zeta5']
            sage: F.embeddings
            [0.309016994374948? + 0.951056516295154?*I]
            sage: F.structures
            [None]
        """
    def is_galois(self):
        """
        Return ``True`` since all cyclotomic fields are automatically Galois.

        EXAMPLES::

            sage: CyclotomicField(29).is_galois()
            True
        """
    def is_abelian(self):
        """
        Return ``True`` since all cyclotomic fields are automatically abelian.

        EXAMPLES::

            sage: CyclotomicField(29).is_abelian()
            True
        """
    def is_isomorphic(self, other):
        """
        Return ``True`` if the cyclotomic field ``self`` is isomorphic as a number
        field to ``other``.

        EXAMPLES::

            sage: CyclotomicField(11).is_isomorphic(CyclotomicField(22))
            True
            sage: CyclotomicField(11).is_isomorphic(CyclotomicField(23))
            False
            sage: x = polygen(QQ, 'x')
            sage: CyclotomicField(3).is_isomorphic(NumberField(x^2 + x + 1, 'a'))
            True
            sage: CyclotomicField(18).is_isomorphic(CyclotomicField(9))
            True
            sage: CyclotomicField(10).is_isomorphic(NumberField(x^4 - x^3 + x^2 - x + 1, 'b'))
            True

        Check :issue:`14300`::

            sage: K = CyclotomicField(4)
            sage: N = K.extension(x^2 - 5, 'z')
            sage: K.is_isomorphic(N)
            False
            sage: K.is_isomorphic(CyclotomicField(8))
            False
        """
    def complex_embedding(self, prec: int = 53):
        """
        Return the embedding of this cyclotomic field into the approximate
        complex field with precision ``prec`` obtained by sending the generator
        `\\zeta` of ``self`` to exp(2\\*pi\\*i/n), where `n` is
        the multiplicative order of `\\zeta`.

        EXAMPLES::

            sage: C = CyclotomicField(4)
            sage: C.complex_embedding()
            Ring morphism:
              From: Cyclotomic Field of order 4 and degree 2
              To:   Complex Field with 53 bits of precision
              Defn: zeta4 |--> 6.12323399573677e-17 + 1.00000000000000*I

        Note in the example above that the way zeta is computed (using sine
        and cosine in MPFR) means that only the ``prec`` bits of the number
        after the decimal point are valid.

        ::

            sage: K = CyclotomicField(3)
            sage: phi = K.complex_embedding(10)
            sage: phi(K.0)
            -0.50 + 0.87*I
            sage: phi(K.0^3)
            1.0
            sage: phi(K.0^3 - 1)
            0.00
            sage: phi(K.0^3 + 7)
            8.0
        """
    @cached_method
    def embeddings(self, K):
        """
        Compute all field embeddings of this field into the field `K`.

        INPUT:

        - ``K`` -- a field

        EXAMPLES::

            sage: CyclotomicField(5).embeddings(ComplexField(53))[1]
            Ring morphism:
              From: Cyclotomic Field of order 5 and degree 4
              To:   Complex Field with 53 bits of precision
              Defn: zeta5 |--> -0.809016994374947 + 0.587785252292473*I
            sage: CyclotomicField(5).embeddings(Qp(11, 4, print_mode='digits'))[1]      # needs sage.rings.padics
            Ring morphism:
              From: Cyclotomic Field of order 5 and degree 4
              To:   11-adic Field with capped relative precision 4
              Defn: zeta5 |--> ...1525
        """
    def complex_embeddings(self, prec: int = 53):
        """
        Return all embeddings of this cyclotomic field into the approximate
        complex field with precision ``prec``.

        If you want 53-bit double precision, which is faster but less
        reliable, then do ``self.embeddings(CDF)``.

        EXAMPLES::

            sage: CyclotomicField(5).complex_embeddings()
            [Ring morphism:
               From: Cyclotomic Field of order 5 and degree 4
               To:   Complex Field with 53 bits of precision
               Defn: zeta5 |--> 0.309016994374947 + 0.951056516295154*I,
             Ring morphism:
               From: Cyclotomic Field of order 5 and degree 4
               To:   Complex Field with 53 bits of precision
               Defn: zeta5 |--> -0.809016994374947 + 0.587785252292473*I,
             Ring morphism:
               From: Cyclotomic Field of order 5 and degree 4
               To:   Complex Field with 53 bits of precision
               Defn: zeta5 |--> -0.809016994374947 - 0.587785252292473*I,
             Ring morphism:
               From: Cyclotomic Field of order 5 and degree 4
               To:   Complex Field with 53 bits of precision
               Defn: zeta5 |--> 0.309016994374947 - 0.951056516295154*I]
        """
    def real_embeddings(self, prec: int = 53):
        """
        Return all embeddings of this cyclotomic field into the approximate
        real field with precision ``prec``.

        Mostly, of course, there are no such embeddings.

        EXAMPLES::

            sage: len(CyclotomicField(4).real_embeddings())
            0
            sage: CyclotomicField(2).real_embeddings()
            [Ring morphism:
               From: Cyclotomic Field of order 2 and degree 1
               To:   Real Field with 53 bits of precision
               Defn: -1 |--> -1.00000000000000]
        """
    def signature(self):
        """
        Return `(r_1, r_2)`, where `r_1` and `r_2` are the number of real embeddings
        and pairs of complex embeddings of this cyclotomic field,
        respectively.

        Trivial since, apart from `\\QQ`, cyclotomic fields are totally
        complex.

        EXAMPLES::

            sage: CyclotomicField(5).signature()
            (0, 2)
            sage: CyclotomicField(2).signature()
            (1, 0)
        """
    def different(self):
        """
        Return the different ideal of the cyclotomic field ``self``.

        EXAMPLES::

            sage: C20 = CyclotomicField(20)
            sage: C20.different()
            Fractional ideal (10, 2*zeta20^6 - 4*zeta20^4 - 4*zeta20^2 + 2)
            sage: C18 = CyclotomicField(18)
            sage: D = C18.different().norm()
            sage: D == C18.discriminant().abs()
            True
        """
    def discriminant(self, v=None):
        """
        Return the discriminant of the ring of integers of the cyclotomic
        field ``self``, or if ``v`` is specified, the determinant of the trace
        pairing on the elements of the list ``v``.

        Uses the formula for the discriminant of a prime power cyclotomic
        field and Hilbert Theorem 88 on the discriminant of composita.

        INPUT:

        - ``v`` -- (optional) list of elements of this number field

        OUTPUT: integer if ``v`` is omitted, and Rational otherwise

        EXAMPLES::

            sage: CyclotomicField(20).discriminant()
            4000000
            sage: CyclotomicField(18).discriminant()
            -19683
        """
    def next_split_prime(self, p: int = 2):
        """
        Return the next prime integer `p` that splits completely in
        this cyclotomic field (and does not ramify).

        EXAMPLES::

            sage: K.<z> = CyclotomicField(3)
            sage: K.next_split_prime(7)
            13
        """
    def zeta_order(self):
        """
        Return the order of the maximal root of unity contained in this
        cyclotomic field.

        EXAMPLES::

            sage: CyclotomicField(1).zeta_order()
            2
            sage: CyclotomicField(4).zeta_order()
            4
            sage: CyclotomicField(5).zeta_order()
            10
            sage: CyclotomicField(5)._n()
            5
            sage: CyclotomicField(389).zeta_order()
            778
        """
    def zeta(self, n=None, all: bool = False):
        """
        Return an element of multiplicative order `n` in this
        cyclotomic field.

        If there is no such element, raise a :exc:`ValueError`.

        INPUT:

        - ``n`` -- integer (default: ``None``, returns element of
          maximal order)

        - ``all`` -- boolean (default: ``False``); whether to return
          a list of all primitive `n`-th roots of unity

        OUTPUT: root of unity or list

        EXAMPLES::

            sage: k = CyclotomicField(4)
            sage: k.zeta()
            zeta4
            sage: k.zeta(2)
            -1
            sage: k.zeta().multiplicative_order()
            4

        ::

            sage: k = CyclotomicField(21)
            sage: k.zeta().multiplicative_order()
            42
            sage: k.zeta(21).multiplicative_order()
            21
            sage: k.zeta(7).multiplicative_order()
            7
            sage: k.zeta(6).multiplicative_order()
            6
            sage: k.zeta(84)
            Traceback (most recent call last):
            ...
            ValueError: 84 does not divide order of generator (42)

        ::

            sage: K.<a> = CyclotomicField(7)
            sage: K.zeta(all=True)
            [-a^4, -a^5, a^5 + a^4 + a^3 + a^2 + a + 1, -a, -a^2, -a^3]
            sage: K.zeta(14, all=True)
            [-a^4, -a^5, a^5 + a^4 + a^3 + a^2 + a + 1, -a, -a^2, -a^3]
            sage: K.zeta(2, all=True)
            [-1]
            sage: K.<a> = CyclotomicField(10)
            sage: K.zeta(20, all=True)
            Traceback (most recent call last):
            ...
            ValueError: 20 does not divide order of generator (10)

        ::

            sage: K.<a> = CyclotomicField(5)
            sage: K.zeta(4)
            Traceback (most recent call last):
            ...
            ValueError: 4 does not divide order of generator (10)
            sage: v = K.zeta(5, all=True); v
            [a, a^2, a^3, -a^3 - a^2 - a - 1]
            sage: [b^5 for b in v]
            [1, 1, 1, 1]
        """
    def number_of_roots_of_unity(self):
        """
        Return number of roots of unity in this cyclotomic field.

        EXAMPLES::

            sage: K.<a> = CyclotomicField(21)
            sage: K.number_of_roots_of_unity()
            42
        """
    def roots_of_unity(self):
        """
        Return all the roots of unity in this cyclotomic field, primitive
        or not.

        EXAMPLES::

            sage: K.<a> = CyclotomicField(3)
            sage: zs = K.roots_of_unity(); zs
            [1, a, -a - 1, -1, -a, a + 1]
            sage: [z**K.number_of_roots_of_unity() for z in zs]
            [1, 1, 1, 1, 1, 1]
        """

class NumberField_quadratic(NumberField_absolute, sage.rings.abc.NumberField_quadratic):
    """
    Create a quadratic extension of the rational field.

    The command ``QuadraticField(a)`` creates the field `\\QQ(\\sqrt{a})`.

    EXAMPLES::

        sage: QuadraticField(3, 'a')
        Number Field in a with defining polynomial x^2 - 3 with a = 1.732050807568878?
        sage: QuadraticField(-4, 'b')
        Number Field in b with defining polynomial x^2 + 4 with b = 2*I
    """
    def __init__(self, polynomial, name=None, latex_name=None, check: bool = True, embedding=None, assume_disc_small: bool = False, maximize_at_primes=None, structure=None) -> None:
        """
        Create a quadratic number field.

        EXAMPLES::

            sage: k.<a> = QuadraticField(5, check=False); k
            Number Field in a with defining polynomial x^2 - 5 with a = 2.236067977499790?

        Don't do this::

            sage: k.<a> = QuadraticField(4, check=False); k
            Number Field in a with defining polynomial x^2 - 4 with a = 2

        TESTS::

            sage: k.<a> = QuadraticField(7)
            sage: type(k.zero())
            <class 'sage.rings.number_field.number_field_element_quadratic.NumberFieldElement_quadratic_sqrt'>
            sage: type(k.one())
            <class 'sage.rings.number_field.number_field_element_quadratic.NumberFieldElement_quadratic_sqrt'>

            sage: TestSuite(k).run()

        Check that :issue:`23008` is fixed::

            sage: z = polygen(ZZ, 'z')
            sage: K.<phi> = NumberField(z^2 - z - 1, embedding=QQbar(golden_ratio))     # needs sage.symbolic
            sage: floor(phi)                                                            # needs sage.symbolic
            1
        """
    def discriminant(self, v=None):
        """
        Return the discriminant of the ring of integers of the number
        field, or if ``v`` is specified, the determinant of the trace pairing
        on the elements of the list ``v``.

        INPUT:

        - ``v`` -- (optional) list of element of this number field

        OUTPUT: integer if ``v`` is omitted, and Rational otherwise

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<i> = NumberField(x^2 + 1)
            sage: K.discriminant()
            -4
            sage: K.<a> = NumberField(x^2 + 5)
            sage: K.discriminant()
            -20
            sage: K.<a> = NumberField(x^2 - 5)
            sage: K.discriminant()
            5
        """
    def is_galois(self):
        """
        Return ``True`` since all quadratic fields are automatically Galois.

        EXAMPLES::

            sage: QuadraticField(1234,'d').is_galois()
            True
        """
    def class_number(self, proof=None):
        """
        Return the size of the class group of ``self``.

        INPUT:

        - ``proof`` -- boolean (default: ``True``, unless you called
          :meth:`proof.number_field` and set it otherwise).  If
          ``proof`` is ``False`` (*not* the default!), and the
          discriminant of the field is negative, then the following
          warning from the PARI manual applies:

        .. warning::

            For `D<0`, this function may give incorrect results when
            the class group has a low exponent (has many cyclic
            factors), because implementing Shank's method in full
            generality slows it down immensely.

        EXAMPLES::

            sage: QuadraticField(-23,'a').class_number()
            3

        These are all the primes so that the class number of
        `\\QQ(\\sqrt{-p})` is `1`::

            sage: [d for d in prime_range(2,300)
            ....:  if not is_square(d) and QuadraticField(-d,'a').class_number() == 1]
            [2, 3, 7, 11, 19, 43, 67, 163]

        It is an open problem to *prove* that there are infinity many
        positive square-free `d` such that
        `\\QQ(\\sqrt{d})` has class number `1`:

        ::

            sage: len([d for d in range(2,200)
            ....:      if not is_square(d) and QuadraticField(d,'a').class_number() == 1])
            121

        TESTS::

            sage: type(QuadraticField(-23,'a').class_number())
            <class 'sage.rings.integer.Integer'>
            sage: x = polygen(QQ, 'x')
            sage: type(NumberField(x^3 + 23, 'a').class_number())
            <class 'sage.rings.integer.Integer'>
            sage: type(NumberField(x^3 + 23, 'a').extension(x^2 + 5, 'b').class_number())
            <class 'sage.rings.integer.Integer'>
            sage: type(CyclotomicField(10).class_number())
            <class 'sage.rings.integer.Integer'>
        """
    def hilbert_class_field_defining_polynomial(self, name: str = 'x'):
        """
        Return a polynomial over `\\QQ` whose roots generate the
        Hilbert class field of this quadratic field as an extension of
        this quadratic field.

        .. NOTE::

            Computed using PARI via Schertz's method. This
            implementation is quite fast.

        EXAMPLES::

            sage: K.<b> = QuadraticField(-23)
            sage: K.hilbert_class_field_defining_polynomial()
            x^3 - x^2 + 1

        Note that this polynomial is not the actual Hilbert class
        polynomial: see ``hilbert_class_polynomial``::

            sage: K.hilbert_class_polynomial()                                          # needs sage.schemes
            x^3 + 3491750*x^2 - 5151296875*x + 12771880859375

        ::

            sage: K.<a> = QuadraticField(-431)
            sage: K.class_number()
            21
            sage: K.hilbert_class_field_defining_polynomial(name='z')
            z^21 + 6*z^20 + 9*z^19 - 4*z^18 + 33*z^17 + 140*z^16 + 220*z^15 + 243*z^14
             + 297*z^13 + 461*z^12 + 658*z^11 + 743*z^10 + 722*z^9 + 681*z^8 + 619*z^7
             + 522*z^6 + 405*z^5 + 261*z^4 + 119*z^3 + 35*z^2 + 7*z + 1
        """
    def hilbert_class_field(self, names):
        """
        Return the Hilbert class field of this quadratic field as a
        relative extension of this field.

        .. NOTE::

            For the polynomial that defines this field as a relative
            extension, see the method :meth:`hilbert_class_field_defining_polynomial`,
            which is vastly faster than this method, since it doesn't
            construct a relative extension.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<a> = NumberField(x^2 + 23)
            sage: L = K.hilbert_class_field('b'); L
            Number Field in b with defining polynomial x^3 - x^2 + 1 over its base field
            sage: L.absolute_field('c')
            Number Field in c with defining polynomial
             x^6 - 2*x^5 + 70*x^4 - 90*x^3 + 1631*x^2 - 1196*x + 12743
            sage: K.hilbert_class_field_defining_polynomial()
            x^3 - x^2 + 1
        """
    def hilbert_class_polynomial(self, name: str = 'x'):
        """
        Compute the Hilbert class polynomial of this quadratic field.

        Right now, this is only implemented for imaginary quadratic
        fields.

        EXAMPLES::

            sage: K.<a> = QuadraticField(-3)
            sage: K.hilbert_class_polynomial()                                          # needs sage.schemes
            x

            sage: K.<a> = QuadraticField(-31)
            sage: K.hilbert_class_polynomial(name='z')                                  # needs sage.schemes
            z^3 + 39491307*z^2 - 58682638134*z + 1566028350940383
        """
    def number_of_roots_of_unity(self):
        """
        Return the number of roots of unity in this quadratic field.

        This is always 2 except when `d` is `-3` or `-4`.

        EXAMPLES::

            sage: QF = QuadraticField
            sage: [QF(d).number_of_roots_of_unity() for d in range(-7, -2)]
            [2, 2, 2, 4, 6]
        """
    def order_of_conductor(self, f):
        """
        Return the unique order with the given conductor in this quadratic field.

        .. SEEALSO ::

            :meth:`sage.rings.number_field.order.Order.conductor`

        EXAMPLES::

            sage: K.<t> = QuadraticField(-123)
            sage: K.order_of_conductor(1) is K.maximal_order()
            True
            sage: K.order_of_conductor(2).gens()
            (1, t)
            sage: K.order_of_conductor(44).gens()
            (1, 22*t)
            sage: K.order_of_conductor(9001).conductor()
            9001
        """

def is_fundamental_discriminant(D):
    """
    Return ``True`` if the integer `D` is a fundamental
    discriminant, i.e., if `D \\cong 0,1\\pmod{4}`, and
    `D\\neq 0, 1` and either (1) `D` is square free or
    (2) we have `D\\cong 0\\pmod{4}` with
    `D/4 \\cong 2,3\\pmod{4}` and `D/4` square free. These
    are exactly the discriminants of quadratic fields.

    EXAMPLES::

        sage: [D for D in range(-15,15) if is_fundamental_discriminant(D)]
        ...
        DeprecationWarning: is_fundamental_discriminant(D) is deprecated;
        please use D.is_fundamental_discriminant()
        ...
        [-15, -11, -8, -7, -4, -3, 5, 8, 12, 13]
        sage: [D for D in range(-15,15)
        ....:  if not is_square(D) and QuadraticField(D,'a').disc() == D]
        [-15, -11, -8, -7, -4, -3, 5, 8, 12, 13]
    """
def NumberField_absolute_v1(poly, name, latex_name, canonical_embedding=None):
    """
    Used for unpickling old pickles.

    EXAMPLES::

        sage: from sage.rings.number_field.number_field import NumberField_absolute_v1
        sage: R.<x> = QQ[]
        sage: NumberField_absolute_v1(x^2 + 1, 'i', 'i')
        Number Field in i with defining polynomial x^2 + 1
    """
NumberField_generic_v1 = NumberField_absolute_v1

def NumberField_cyclotomic_v1(zeta_order, name, canonical_embedding=None):
    """
    Used for unpickling old pickles.

    EXAMPLES::

        sage: from sage.rings.number_field.number_field import NumberField_cyclotomic_v1
        sage: NumberField_cyclotomic_v1(5,'a')
        Cyclotomic Field of order 5 and degree 4
        sage: NumberField_cyclotomic_v1(5,'a').variable_name()
        'a'
    """
def NumberField_quadratic_v1(poly, name, canonical_embedding=None):
    """
    Used for unpickling old pickles.

    EXAMPLES::

        sage: from sage.rings.number_field.number_field import NumberField_quadratic_v1
        sage: R.<x> = QQ[]
        sage: NumberField_quadratic_v1(x^2 - 2, 'd')
        Number Field in d with defining polynomial x^2 - 2
    """
def put_natural_embedding_first(v) -> None:
    """
    Helper function for embeddings() functions for number fields.

    INPUT:

    - ``v`` -- list of embeddings of a number field

    OUTPUT: none; the list is altered in-place, so that, if possible, the first
    embedding has been switched with one of the others, so that if there is an
    embedding which preserves the generator names then it appears first.

    EXAMPLES::

        sage: K.<a> = CyclotomicField(7)
        sage: embs = K.embeddings(K)
        sage: [e(a) for e in embs]  # random - there is no natural sort order
        [a, a^2, a^3, a^4, a^5, -a^5 - a^4 - a^3 - a^2 - a - 1]
        sage: id = [e for e in embs if e(a) == a][0]; id
        Ring endomorphism of Cyclotomic Field of order 7 and degree 6
          Defn: a |--> a
        sage: permuted_embs = list(embs); permuted_embs.remove(id); permuted_embs.append(id)
        sage: [e(a) for e in permuted_embs]  # random - but natural map is not first
        [a^2, a^3, a^4, a^5, -a^5 - a^4 - a^3 - a^2 - a - 1, a]
        sage: permuted_embs[0] != a
        True
        sage: from sage.rings.number_field.number_field import put_natural_embedding_first
        sage: put_natural_embedding_first(permuted_embs)
        sage: [e(a) for e in permuted_embs]  # random - but natural map is first
        [a, a^3, a^4, a^5, -a^5 - a^4 - a^3 - a^2 - a - 1, a^2]
        sage: permuted_embs[0] == id
        True
    """
def refine_embedding(e, prec=None):
    """
    Given an embedding from a number field to either `\\RR` or
    `\\CC`, return an equivalent embedding with higher precision.

    INPUT:

    - ``e`` -- an embedding of a number field into either `\\RR` or `\\CC`
      (with some precision)

    - ``prec`` -- (default: ``None``) the desired precision; if ``None``,
      current precision is doubled; if ``Infinity``, the equivalent
      embedding into either ``QQbar`` or ``AA`` is returned.

    EXAMPLES::

        sage: from sage.rings.number_field.number_field import refine_embedding
        sage: K = CyclotomicField(3)
        sage: e10 = K.complex_embedding(10)
        sage: e10.codomain().precision()
        10
        sage: e25 = refine_embedding(e10, prec=25)
        sage: e25.codomain().precision()
        25

    An example where we extend a real embedding into ``AA``::

        sage: x = polygen(QQ, 'x')
        sage: K.<a> = NumberField(x^3 - 2)
        sage: K.signature()
        (1, 1)
        sage: e = K.embeddings(RR)[0]; e
        Ring morphism:
        From: Number Field in a with defining polynomial x^3 - 2
        To:   Real Field with 53 bits of precision
        Defn: a |--> 1.25992104989487
        sage: e = refine_embedding(e, Infinity); e
        Ring morphism:
        From: Number Field in a with defining polynomial x^3 - 2
        To:   Algebraic Real Field
        Defn: a |--> 1.259921049894873?

    Now we can obtain arbitrary precision values with no trouble::

        sage: RealField(150)(e(a))
        1.2599210498948731647672106072782283505702515
        sage: _^3
        2.0000000000000000000000000000000000000000000
        sage: RealField(200)(e(a^2 - 3*a + 7))
        4.8076379022835799804500738174376232086807389337953290695624

    Complex embeddings can be extended into ``QQbar``::

        sage: e = K.embeddings(CC)[0]; e
        Ring morphism:
        From: Number Field in a with defining polynomial x^3 - 2
        To:   Complex Field with 53 bits of precision
        Defn: a |--> -0.62996052494743... - 1.09112363597172*I
        sage: e = refine_embedding(e,Infinity); e
        Ring morphism:
        From: Number Field in a with defining polynomial x^3 - 2
        To:   Algebraic Field
        Defn: a |--> -0.6299605249474365? - 1.091123635971722?*I
        sage: ComplexField(200)(e(a))
        -0.62996052494743658238360530363911417528512573235075399004099
         - 1.0911236359717214035600726141898088813258733387403009407036*I
        sage: e(a)^3
        2

    Embeddings into lazy fields work::

        sage: L = CyclotomicField(7)
        sage: x = L.specified_complex_embedding(); x
        Generic morphism:
          From: Cyclotomic Field of order 7 and degree 6
          To:   Complex Lazy Field
          Defn: zeta7 -> 0.623489801858734? + 0.781831482468030?*I
        sage: refine_embedding(x, 300)
        Ring morphism:
          From: Cyclotomic Field of order 7 and degree 6
          To:   Complex Field with 300 bits of precision
          Defn: zeta7 |--> 0.623489801858733530525004884004239810632274730896402105365549439096853652456487284575942507
                            + 0.781831482468029808708444526674057750232334518708687528980634958045091731633936441700868007*I
        sage: refine_embedding(x, infinity)
        Ring morphism:
          From: Cyclotomic Field of order 7 and degree 6
          To:   Algebraic Field
          Defn: zeta7 |--> 0.6234898018587335? + 0.7818314824680299?*I

    When the old embedding is into the real lazy field,
    then only real embeddings should be considered.
    See :issue:`17495`::

        sage: R.<x> = QQ[]
        sage: K.<a> = NumberField(x^3 + x - 1, embedding=0.68)
        sage: from sage.rings.number_field.number_field import refine_embedding
        sage: refine_embedding(K.specified_complex_embedding(), 100)
        Ring morphism:
          From: Number Field in a with defining polynomial x^3 + x - 1 with a = 0.6823278038280193?
          To:   Real Field with 100 bits of precision
          Defn: a |--> 0.68232780382801932736948373971
        sage: refine_embedding(K.specified_complex_embedding(), Infinity)
        Ring morphism:
          From: Number Field in a with defining polynomial x^3 + x - 1 with a = 0.6823278038280193?
          To:   Algebraic Real Field
          Defn: a |--> 0.6823278038280193?
    """
def is_real_place(v):
    """
    Return ``True`` if `v` is real, ``False`` if `v` is complex.

    INPUT:

    - ``v`` -- an infinite place of ``self``

    OUTPUT:

    A boolean indicating whether a place is real (``True``) or complex (``False``).

    EXAMPLES::

        sage: x = polygen(QQ, 'x')
        sage: K.<xi> = NumberField(x^3 - 3)
        sage: phi_real = K.places()[0]
        sage: phi_complex = K.places()[1]
        sage: v_fin = tuple(K.primes_above(3))[0]

        sage: is_real_place(phi_real)
        True

        sage: is_real_place(phi_complex)
        False

    It is an error to put in a finite place

    ::

        sage: is_real_place(v_fin)
        Traceback (most recent call last):
        ...
        AttributeError: 'NumberFieldFractionalIdeal' object has no attribute 'im_gens'...
    """
