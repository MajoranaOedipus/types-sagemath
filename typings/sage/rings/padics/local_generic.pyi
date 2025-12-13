from _typeshed import Incomplete
from sage.categories.complete_discrete_valuation import CompleteDiscreteValuationFields as CompleteDiscreteValuationFields, CompleteDiscreteValuationRings as CompleteDiscreteValuationRings
from sage.rings.infinity import Infinity as Infinity
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.category_object import check_default_category as check_default_category
from sage.structure.parent import Parent as Parent

class LocalGeneric(Parent):
    Element: Incomplete
    def __init__(self, base, prec, names, element_class, category=None) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: R = Zp(5)  # indirect doctest
            sage: R.precision_cap()
            20

        In :issue:`14084`, the category framework has been implemented for `p`-adic rings::

            sage: TestSuite(R).run()                                                    # needs sage.geometry.polyhedron
            sage: K = Qp(7)
            sage: TestSuite(K).run()                                                    # needs sage.geometry.polyhedron

        TESTS::

            sage: R = Zp(5, 5, 'fixed-mod')
            sage: R._repr_option('element_is_atomic')
            False

            sage: R = Zp(3, 10,'fixed-mod')
            sage: R.is_finite()
            False
            sage: R.cardinality()
            +Infinity

            sage: Qp(11).is_finite()
            False
            sage: Qp(11).cardinality()
            +Infinity
        """
    def is_capped_relative(self) -> bool:
        """
        Return whether this `p`-adic ring bounds precision in a capped
        relative fashion.

        The relative precision of an element is the power of `p`
        modulo which the unit part of that element is defined.  In a
        capped relative ring, the relative precision of elements are
        bounded by a constant depending on the ring.

        EXAMPLES::

            sage: R = ZpCA(5, 15)
            sage: R.is_capped_relative()
            False
            sage: R(5^7)
            5^7 + O(5^15)
            sage: S = Zp(5, 15)
            sage: S.is_capped_relative()
            True
            sage: S(5^7)
            5^7 + O(5^22)
        """
    def is_capped_absolute(self) -> bool:
        """
        Return whether this `p`-adic ring bounds precision in a
        capped absolute fashion.

        The absolute precision of an element is the power of `p`
        modulo which that element is defined.  In a capped absolute
        ring, the absolute precision of elements are bounded by a
        constant depending on the ring.

        EXAMPLES::

            sage: R = ZpCA(5, 15)
            sage: R.is_capped_absolute()
            True
            sage: R(5^7)
            5^7 + O(5^15)
            sage: S = Zp(5, 15)
            sage: S.is_capped_absolute()
            False
            sage: S(5^7)
            5^7 + O(5^22)
        """
    def is_fixed_mod(self) -> bool:
        """
        Return whether this `p`-adic ring bounds precision in a fixed
        modulus fashion.

        The absolute precision of an element is the power of `p`
        modulo which that element is defined.  In a fixed modulus
        ring, the absolute precision of every element is defined to be
        the precision cap of the parent.  This means that some
        operations, such as division by `p`, don't return a well defined
        answer.

        EXAMPLES::

            sage: R = ZpFM(5,15)
            sage: R.is_fixed_mod()
            True
            sage: R(5^7,absprec=9)
            5^7
            sage: S = ZpCA(5, 15)
            sage: S.is_fixed_mod()
            False
            sage: S(5^7,absprec=9)
            5^7 + O(5^9)
        """
    def is_floating_point(self) -> bool:
        """
        Return whether this `p`-adic ring bounds precision in a floating
        point fashion.

        The relative precision of an element is the power of `p`
        modulo which the unit part of that element is defined.  In a
        floating point ring, elements do not store precision, but arithmetic
        operations truncate to a relative precision depending on the ring.

        EXAMPLES::

            sage: R = ZpCR(5, 15)
            sage: R.is_floating_point()
            False
            sage: R(5^7)
            5^7 + O(5^22)
            sage: S = ZpFP(5, 15)
            sage: S.is_floating_point()
            True
            sage: S(5^7)
            5^7
        """
    def is_lattice_prec(self) -> bool:
        """
        Return whether this `p`-adic ring bounds precision using
        a lattice model.

        In lattice precision, relationships between elements
        are stored in a precision object of the parent, which
        allows for optimal precision tracking at the cost of
        increased memory usage and runtime.

        EXAMPLES::

            sage: R = ZpCR(5, 15)
            sage: R.is_lattice_prec()
            False
            sage: x = R(25, 8)
            sage: x - x
            O(5^8)
            sage: S = ZpLC(5, 15)
            doctest:...: FutureWarning: This class/method/function is marked as experimental. It, its functionality or its interface might change without a formal deprecation.
            See https://github.com/sagemath/sage/issues/23505 for details.
            sage: S.is_lattice_prec()
            True
            sage: x = S(25, 8)
            sage: x - x
            O(5^30)
        """
    def is_relaxed(self) -> bool:
        """
        Return whether this `p`-adic ring bounds precision in a relaxed
        fashion.

        In a relaxed ring, elements have mechanisms for computing
        themselves to greater precision.

        EXAMPLES::

            sage: R = Zp(5)
            sage: R.is_relaxed()
            False
        """
    def change(self, **kwds):
        '''
        Return a new ring with changed attributes.

        INPUT:

        The following arguments are applied to every ring in the tower:

        - ``type`` -- string, the precision type
        - ``p`` -- the prime of the ground ring; defining polynomials
          will be converted to the new base rings
        - ``print_mode`` -- string
        - ``print_pos`` -- boolean
        - ``print_sep`` -- string
        - ``print_alphabet`` -- dictionary
        - ``show_prec`` -- boolean
        - ``check`` -- boolean
        - ``label`` -- string (only for lattice precision)

        The following arguments are only applied to the top ring in the tower:

        - ``var_name`` -- string
        - ``res_name`` -- string
        - ``unram_name`` -- string
        - ``ram_name`` -- string
        - ``names`` -- string
        - ``modulus`` -- polynomial

        The following arguments have special behavior:

        - ``prec`` -- integer; if the precision is increased on an extension ring,
          the precision on the base is increased as necessary (respecting ramification).
          If the precision is decreased, the precision of the base is unchanged.

        - ``field`` -- boolean; if ``True``, switch to a tower of fields via the fraction field
          If ``False``, switch to a tower of rings of integers

        - ``q`` -- prime power; replace the initial unramified extension of `\\QQ_p` or `\\ZZ_p`
          with an unramified extension of residue cardinality `q`.
          If the initial extension is ramified, add in an unramified extension.

        - ``base`` -- ring or field; use a specific base ring instead of recursively
          calling :meth:`change` down the tower

        See the :mod:`constructors <sage.rings.padics.factory>` for more details on the
        meaning of these arguments.

        EXAMPLES:

        We can use this method to change the precision::

            sage: Zp(5).change(prec=40)
            5-adic Ring with capped relative precision 40

        or the precision type::

            sage: Zp(5).change(type=\'capped-abs\')
            5-adic Ring with capped absolute precision 20

        or even the prime::

            sage: ZpCA(3).change(p=17)
            17-adic Ring with capped absolute precision 20

        You can switch between the ring of integers and its fraction field::

            sage: ZpCA(3).change(field=True)
            3-adic Field with capped relative precision 20

        You can also change print modes::

            sage: R = Zp(5).change(prec=5, print_mode=\'digits\')
            sage: repr(~R(17))
            \'...13403\'

        Changing print mode to \'digits\' works for Eisenstein extensions::

            sage: # needs sage.libs.ntl
            sage: S.<x> = ZZ[]
            sage: W.<w> = Zp(3).extension(x^4 + 9*x^2 + 3*x - 3)
            sage: W.print_mode()
            \'series\'
            sage: W.change(print_mode=\'digits\').print_mode()
            \'digits\'

        You can change extensions::

            sage: # needs sage.libs.flint
            sage: K.<a> = QqFP(125, prec=4)
            sage: K.change(q=64)
            2-adic Unramified Extension Field in a defined by x^6 + x^4 + x^3 + x + 1
            sage: R.<x> = QQ[]
            sage: K.change(modulus = x^2 - x + 2, print_pos=False)
            5-adic Unramified Extension Field in a defined by x^2 - x + 2

        and variable names::

            sage: K.change(names=\'b\')                                                   # needs sage.libs.flint
            5-adic Unramified Extension Field in b defined by x^3 + 3*x + 3

        and precision::

            sage: # needs sage.libs.flint
            sage: Kup = K.change(prec=8); Kup
            5-adic Unramified Extension Field in a defined by x^3 + 3*x + 3
            sage: Kup.precision_cap()
            8
            sage: Kup.base_ring()
            5-adic Field with floating precision 8

        If you decrease the precision, the precision of the base stays the same::

            sage: # needs sage.libs.flint
            sage: Kdown = K.change(prec=2); Kdown
            5-adic Unramified Extension Field in a defined by x^3 + 3*x + 3
            sage: Kdown.precision_cap()
            2
            sage: Kdown.base_ring()
            5-adic Field with floating precision 4

        Changing the prime works for extensions::

            sage: # needs sage.libs.ntl
            sage: x = polygen(ZZ)
            sage: R.<a> = Zp(5).extension(x^2 + 2)
            sage: S = R.change(p=7)
            sage: S.defining_polynomial(exact=True)
            x^2 + 2
            sage: A.<y> = Zp(5)[]
            sage: R.<a> = Zp(5).extension(y^2 + 2)
            sage: S = R.change(p=7)
            sage: S.defining_polynomial(exact=True)
            y^2 + 2

        ::

            sage: # needs sage.libs.ntl
            sage: R.<a> = Zq(5^3)
            sage: S = R.change(prec=50)
            sage: S.defining_polynomial(exact=True)
            x^3 + 3*x + 3

        Changing label for lattice precision (the precision lattice is not copied)::

            sage: R = ZpLC(37, (8,11))
            sage: S = R.change(label = "change"); S
            37-adic Ring with lattice-cap precision (label: change)
            sage: S.change(label = "new")
            37-adic Ring with lattice-cap precision (label: new)


        TESTS:

        The `secure` attribute for relaxed type is copied::

            sage: # needs sage.libs.flint
            sage: R = ZpER(5, secure=True); R
            5-adic Ring handled with relaxed arithmetics
            sage: K = R.change(field=True); K
            5-adic Field handled with relaxed arithmetics
            sage: K.is_secure()
            True

        The `check=False` option works for relaxed type::

            sage: # needs sage.libs.flint
            sage: R = ZpER(5) ; R
            5-adic Ring handled with relaxed arithmetics
            sage: K = R.change(field=True, check=False) ; K
            5-adic Field handled with relaxed arithmetics
        '''
    def precision_cap(self):
        """
        Return the precision cap for this ring.

        EXAMPLES::

            sage: R = Zp(3, 10,'fixed-mod'); R.precision_cap()
            10
            sage: R = Zp(3, 10,'capped-rel'); R.precision_cap()
            10
            sage: R = Zp(3, 10,'capped-abs'); R.precision_cap()
            10

        .. NOTE::

            This will have different meanings depending on the type of
            local ring.  For fixed modulus rings, all elements are
            considered modulo ``self.prime()^self.precision_cap()``.
            For rings with an absolute cap (i.e. the class
            ``pAdicRingCappedAbsolute``), each element has a precision
            that is tracked and is bounded above by
            ``self.precision_cap()``.  Rings with relative caps
            (e.g. the class ``pAdicRingCappedRelative``) are the same
            except that the precision is the precision of the unit
            part of each element.
        """
    def is_exact(self):
        """
        Return whether this `p`-adic ring is exact, i.e. ``False``.

        EXAMPLES::

            sage: R = Zp(5, 3, 'fixed-mod'); R.is_exact()
            False
        """
    def residue_characteristic(self):
        """
        Return the characteristic of ``self``'s residue field.

        INPUT:

        - ``self`` -- a `p`-adic ring

        OUTPUT: the characteristic of the residue field

        EXAMPLES::

            sage: R = Zp(3, 5, 'capped-rel'); R.residue_characteristic()
            3
        """
    def defining_polynomial(self, var: str = 'x', exact: bool = False):
        """
        Return the defining polynomial of this local ring.

        INPUT:

        - ``var`` -- string (default: ``'x'``); the name of the variable

        - ``exact`` -- boolean (default: ``False``); whether to return the
          underlying exact defining polynomial rather than the one with coefficients
          in the base ring

        OUTPUT: the defining polynomial of this ring as an extension over its ground ring

        EXAMPLES::

            sage: R = Zp(3, 3, 'fixed-mod')

            sage: R.defining_polynomial().parent()
            Univariate Polynomial Ring in x over 3-adic Ring of fixed modulus 3^3
            sage: R.defining_polynomial('foo')
            foo

            sage: R.defining_polynomial(exact=True).parent()
            Univariate Polynomial Ring in x over Integer Ring
        """
    def ground_ring(self):
        """
        Return ``self``.

        Will be overridden by extensions.

        INPUT:

        - ``self`` -- a local ring

        OUTPUT: the ground ring of ``self``, i.e., itself

        EXAMPLES::

            sage: R = Zp(3, 5, 'fixed-mod')
            sage: S = Zp(3, 4, 'fixed-mod')
            sage: R.ground_ring() is R
            True
            sage: S.ground_ring() is R
            False
        """
    def ground_ring_of_tower(self):
        """
        Return ``self``.

        Will be overridden by extensions.

        INPUT:

        - ``self`` -- a `p`-adic ring

        OUTPUT: the ground ring of the tower for ``self``, i.e., itself

        EXAMPLES::

            sage: R = Zp(5)
            sage: R.ground_ring_of_tower()
            5-adic Ring with capped relative precision 20
        """
    def absolute_degree(self):
        """
        Return the degree of this extension over the prime `p`-adic field/ring.

        EXAMPLES::

            sage: K.<a> = Qq(3^5)                                                       # needs sage.libs.ntl
            sage: K.absolute_degree()                                                   # needs sage.libs.ntl
            5

            sage: R.<x> = QQ[]
            sage: L.<pi> = Qp(3).extension(x^2 - 3)                                     # needs sage.libs.ntl
            sage: L.absolute_degree()                                                   # needs sage.libs.ntl
            2
        """
    def relative_degree(self):
        """
        Return the degree of this extension over its base field/ring.

        EXAMPLES::

            sage: K.<a> = Qq(3^5)                                                       # needs sage.libs.ntl
            sage: K.relative_degree()                                                   # needs sage.libs.ntl
            5

            sage: R.<x> = QQ[]
            sage: L.<pi> = Qp(3).extension(x^2 - 3)                                     # needs sage.libs.ntl
            sage: L.relative_degree()                                                   # needs sage.libs.ntl
            2
        """
    def degree(self):
        """
        Return the degree of this extension.

        Raise an error if the base ring/field is itself an extension.

        EXAMPLES::

            sage: K.<a> = Qq(3^5)                                                       # needs sage.libs.ntl
            sage: K.degree()                                                            # needs sage.libs.ntl
            5

            sage: R.<x> = QQ[]
            sage: L.<pi> = Qp(3).extension(x^2 - 3)                                     # needs sage.libs.ntl
            sage: L.degree()                                                            # needs sage.libs.ntl
            2
        """
    def absolute_e(self):
        """
        Return the absolute ramification index of this ring/field.

        EXAMPLES::

            sage: K.<a> = Qq(3^5)                                                       # needs sage.libs.ntl
            sage: K.absolute_e()                                                        # needs sage.libs.ntl
            1

            sage: R.<x> = QQ[]
            sage: L.<pi> = Qp(3).extension(x^2 - 3)                                     # needs sage.libs.ntl
            sage: L.absolute_e()                                                        # needs sage.libs.ntl
            2
        """
    def absolute_ramification_index(self):
        """
        Return the absolute ramification index of this ring/field.

        EXAMPLES::

            sage: K.<a> = Qq(3^5)                                                       # needs sage.libs.ntl
            sage: K.absolute_ramification_index()                                       # needs sage.libs.ntl
            1

            sage: R.<x> = QQ[]
            sage: L.<pi> = Qp(3).extension(x^2 - 3)                                     # needs sage.libs.ntl
            sage: L.absolute_ramification_index()                                       # needs sage.libs.ntl
            2
        """
    def relative_e(self):
        """
        Return the ramification index of this extension over its base ring/field.

        EXAMPLES::

            sage: K.<a> = Qq(3^5)                                                       # needs sage.libs.ntl
            sage: K.relative_e()                                                        # needs sage.libs.ntl
            1

            sage: R.<x> = QQ[]
            sage: L.<pi> = Qp(3).extension(x^2 - 3)                                     # needs sage.libs.ntl
            sage: L.relative_e()                                                        # needs sage.libs.ntl
            2
        """
    def relative_ramification_index(self):
        """
        Return the ramification index of this extension over its base ring/field.

        EXAMPLES::

            sage: K.<a> = Qq(3^5)                                                       # needs sage.libs.ntl
            sage: K.relative_ramification_index()                                       # needs sage.libs.ntl
            1

            sage: R.<x> = QQ[]
            sage: L.<pi> = Qp(3).extension(x^2 - 3)                                     # needs sage.libs.ntl
            sage: L.relative_ramification_index()                                       # needs sage.libs.ntl
            2
        """
    def e(self):
        """
        Return the ramification index of this extension.

        Raise an error if the base ring/field is itself an extension.

        EXAMPLES::

            sage: K.<a> = Qq(3^5)                                                       # needs sage.libs.ntl
            sage: K.e()                                                                 # needs sage.libs.ntl
            1

            sage: R.<x> = QQ[]
            sage: L.<pi> = Qp(3).extension(x^2 - 3)                                     # needs sage.libs.ntl
            sage: L.e()                                                                 # needs sage.libs.ntl
            2
        """
    def ramification_index(self):
        """
        Return the ramification index of this extension.

        Raise an error if the base ring/field is itself an extension.

        EXAMPLES::

            sage: K.<a> = Qq(3^5)                                                       # needs sage.libs.ntl
            sage: K.ramification_index()                                                # needs sage.libs.ntl
            1

            sage: R.<x> = QQ[]
            sage: L.<pi> = Qp(3).extension(x^2 - 3)                                     # needs sage.libs.ntl
            sage: L.ramification_index()                                                # needs sage.libs.ntl
            2
        """
    def absolute_f(self):
        """
        Return the degree of the residue field of this ring/field
        over its prime subfield.

        EXAMPLES::

            sage: K.<a> = Qq(3^5)                                                       # needs sage.libs.ntl
            sage: K.absolute_f()                                                        # needs sage.libs.ntl
            5

            sage: R.<x> = QQ[]
            sage: L.<pi> = Qp(3).extension(x^2 - 3)                                     # needs sage.libs.ntl
            sage: L.absolute_f()                                                        # needs sage.libs.ntl
            1
        """
    def absolute_inertia_degree(self):
        """
        Return the degree of the residue field of this ring/field
        over its prime subfield.

        EXAMPLES::

            sage: K.<a> = Qq(3^5)                                                       # needs sage.libs.ntl
            sage: K.absolute_inertia_degree()                                           # needs sage.libs.ntl
            5

            sage: R.<x> = QQ[]
            sage: L.<pi> = Qp(3).extension(x^2 - 3)                                     # needs sage.libs.ntl
            sage: L.absolute_inertia_degree()                                           # needs sage.libs.ntl
            1
        """
    def relative_f(self):
        """
        Return the degree of the residual extension over its base ring/field.

        EXAMPLES::

            sage: K.<a> = Qq(3^5)                                                       # needs sage.libs.ntl
            sage: K.relative_f()                                                        # needs sage.libs.ntl
            5

            sage: R.<x> = QQ[]
            sage: L.<pi> = Qp(3).extension(x^2 - 3)                                     # needs sage.libs.ntl
            sage: L.relative_f()                                                        # needs sage.libs.ntl
            1
        """
    def relative_inertia_degree(self):
        """
        Return the degree of the residual extension over its base ring/field.

        EXAMPLES::

            sage: K.<a> = Qq(3^5)                                                       # needs sage.libs.ntl
            sage: K.relative_inertia_degree()                                           # needs sage.libs.ntl
            5

            sage: R.<x> = QQ[]
            sage: L.<pi> = Qp(3).extension(x^2 - 3)                                     # needs sage.libs.ntl
            sage: L.relative_inertia_degree()                                           # needs sage.libs.ntl
            1
        """
    def f(self):
        """
        Return the degree of the residual extension.

        Raise an error if the base ring/field is itself an extension.

        EXAMPLES::

            sage: K.<a> = Qq(3^5)                                                       # needs sage.libs.ntl
            sage: K.f()                                                                 # needs sage.libs.ntl
            5

            sage: R.<x> = QQ[]
            sage: L.<pi> = Qp(3).extension(x^2 - 3)                                     # needs sage.libs.ntl
            sage: L.f()                                                                 # needs sage.libs.ntl
            1
        """
    def inertia_degree(self):
        """
        Return the degree of the residual extension.

        Raise an error if the base ring/field is itself an extension.

        EXAMPLES::

            sage: K.<a> = Qq(3^5)                                                       # needs sage.libs.ntl
            sage: K.inertia_degree()                                                    # needs sage.libs.ntl
            5

            sage: R.<x> = QQ[]
            sage: L.<pi> = Qp(3).extension(x^2 - 3)                                     # needs sage.libs.ntl
            sage: L.inertia_degree()                                                    # needs sage.libs.ntl
            1
        """
    def inertia_subring(self):
        """
        Return the inertia subring, i.e. ``self``.

        INPUT:

        - ``self`` -- a local ring

        OUTPUT: the inertia subring of ``self``, i.e., itself

        EXAMPLES::

            sage: R = Zp(5)
            sage: R.inertia_subring()
            5-adic Ring with capped relative precision 20
        """
    def maximal_unramified_subextension(self):
        """
        Return the maximal unramified subextension.

        INPUT:

        - ``self`` -- a local ring

        OUTPUT: the maximal unramified subextension of ``self``

        EXAMPLES::

            sage: R = Zp(5)
            sage: R.maximal_unramified_subextension()
            5-adic Ring with capped relative precision 20
        """
    def uniformiser(self):
        """
        Return a uniformiser for ``self``, ie a generator for the unique maximal ideal.

        EXAMPLES::

            sage: R = Zp(5)
            sage: R.uniformiser()
            5 + O(5^21)
            sage: A = Zp(7,10)
            sage: S.<x> = A[]                                                           # needs sage.libs.ntl
            sage: B.<t> = A.ext(x^2+7)                                                  # needs sage.libs.ntl
            sage: B.uniformiser()                                                       # needs sage.libs.ntl
            t + O(t^21)
        """
    def uniformiser_pow(self, n):
        """
        Return the `n`-th power of the uniformiser of ``self`` (as an element
        of ``self``).

        EXAMPLES::

            sage: R = Zp(5)
            sage: R.uniformiser_pow(5)
            5^5 + O(5^25)
        """
    def ext(self, *args, **kwds):
        """
        Construct an extension of ``self``.  See :meth:`extension` for more details.

        EXAMPLES::

            sage: A = Zp(7,10)
            sage: S.<x> = A[]                                                           # needs sage.libs.ntl
            sage: B.<t> = A.ext(x^2 + 7)                                                # needs sage.libs.ntl
            sage: B.uniformiser()                                                       # needs sage.libs.ntl
            t + O(t^21)
        """
