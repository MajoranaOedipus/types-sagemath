from sage.categories.basic import Fields as Fields
from sage.categories.category_singleton import Category_singleton as Category_singleton

class NumberFields(Category_singleton):
    """
    The category of number fields.

    EXAMPLES:

    We create the category of number fields::

        sage: C = NumberFields()
        sage: C
        Category of number fields

    By definition, it is infinite::

        sage: NumberFields().Infinite() is NumberFields()
        True

    Notice that the rational numbers `\\QQ` *are* considered as
    an object in this category::

        sage: RationalField() in C
        True

    However, we can define a degree 1 extension of `\\QQ`, which is of
    course also in this category::

        sage: x = PolynomialRing(RationalField(), 'x').gen()
        sage: K = NumberField(x - 1, 'a'); K                                            # needs sage.rings.number_field
        Number Field in a with defining polynomial x - 1
        sage: K in C                                                                    # needs sage.rings.number_field
        True

    Number fields all lie in this category, regardless of the name
    of the variable::

        sage: K = NumberField(x^2 + 1, 'a')                                             # needs sage.rings.number_field
        sage: K in C                                                                    # needs sage.rings.number_field
        True

    TESTS::

        sage: TestSuite(NumberFields()).run()
    """
    def super_categories(self):
        """
        EXAMPLES::

            sage: NumberFields().super_categories()
            [Category of infinite fields]
        """
    def __contains__(self, x) -> bool:
        """
        Return ``True`` if ``x`` is a number field.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: NumberField(x^2 + 1, 'a') in NumberFields()                           # needs sage.rings.number_field
            True
            sage: QuadraticField(-97, 'theta') in NumberFields()                        # needs sage.rings.number_field
            True
            sage: CyclotomicField(97) in NumberFields()                                 # needs sage.rings.number_field
            True

        Note that the rational numbers QQ are a number field::

            sage: QQ in NumberFields()
            True
            sage: ZZ in NumberFields()
            False
        """
    class ParentMethods:
        def zeta_function(self, prec: int = 53, max_imaginary_part: int = 0, max_asymp_coeffs: int = 40, algorithm: str = 'pari'):
            '''
            Return the Dedekind zeta function of this number field.

            Actually, this returns an interface for computing with the
            Dedekind zeta function `\\zeta_F(s)` of the number field `F`.

            INPUT:

            - ``prec`` -- integer (default: 53); bits of precision

            - ``max_imaginary_part`` -- real (default: 0)

            - ``max_asymp_coeffs`` -- integer (default: 40)

            - ``algorithm`` -- (default: ``\'pari\'``) either ``\'gp\'`` or
              ``\'pari\'``

            OUTPUT: the zeta function of this number field

            If algorithm is ``\'gp\'``, this returns an interface to Tim
            Dokchitser\'s gp script for computing with `L`-functions.

            If algorithm is ``\'pari\'``, this returns instead an interface to Pari\'s
            own general implementation of `L`-functions.

            EXAMPLES::

                sage: K.<a> = NumberField(ZZ[\'x\'].0^2 + ZZ[\'x\'].0 - 1)                  # needs sage.rings.number_field
                sage: Z = K.zeta_function(); Z                                          # needs sage.rings.number_field sage.symbolic
                PARI zeta function associated to Number Field in a
                 with defining polynomial x^2 + x - 1
                sage: Z(-1)                                                             # needs sage.rings.number_field sage.symbolic
                0.0333333333333333

                sage: x = polygen(QQ, \'x\')
                sage: L.<a, b, c> = NumberField([x^2 - 5, x^2 + 3, x^2 + 1])            # needs sage.rings.number_field
                sage: Z = L.zeta_function()                                             # needs sage.rings.number_field sage.symbolic
                sage: Z(5)                                                              # needs sage.rings.number_field sage.symbolic
                1.00199015670185

            Using the algorithm "pari"::

                sage: K.<a> = NumberField(ZZ[\'x\'].0^2 + ZZ[\'x\'].0 - 1)                  # needs sage.rings.number_field
                sage: Z = K.zeta_function(algorithm=\'pari\')                             # needs sage.rings.number_field sage.symbolic
                sage: Z(-1)                                                             # needs sage.rings.number_field sage.symbolic
                0.0333333333333333

                sage: x = polygen(QQ, \'x\')
                sage: L.<a, b, c> = NumberField([x^2 - 5, x^2 + 3, x^2 + 1])            # needs sage.rings.number_field
                sage: Z = L.zeta_function(algorithm=\'pari\')                             # needs sage.rings.number_field sage.symbolic
                sage: Z(5)                                                              # needs sage.rings.number_field sage.symbolic
                1.00199015670185

            TESTS::

                sage: QQ.zeta_function()                                                # needs sage.symbolic
                PARI zeta function associated to Rational Field
            '''
    class ElementMethods: ...
