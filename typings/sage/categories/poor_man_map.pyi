from sage.structure.sage_object import SageObject as SageObject

class PoorManMap(SageObject):
    """
    A class for maps between sets which are not (yet) modeled by parents.

    Could possibly disappear when all combinatorial classes / enumerated sets will be parents.

    INPUT:

    - ``function`` -- a callable or an iterable of callables. This represents
      the underlying function used to implement this map. If it is an iterable,
      then the callables will be composed to implement this map.

    - ``domain`` -- the domain of this map or ``None`` if the domain is not
      known or should remain unspecified

    - ``codomain`` -- the codomain of this map or ``None`` if the codomain is
      not known or should remain unspecified

    - ``name`` -- a name for this map or ``None`` if this map has no particular
      name

    EXAMPLES::

        sage: from sage.categories.poor_man_map import PoorManMap
        sage: f = PoorManMap(factorial, domain=(1, 2, 3), codomain=(1, 2, 6))
        sage: f
        A map from (1, 2, 3) to (1, 2, 6)
        sage: f(3)
        6

    The composition of several functions can be created by passing in a tuple
    of functions::

        sage: i = PoorManMap((factorial, sqrt), domain=(1, 4, 9), codomain=(1, 2, 6))

    However, the same effect can also be achieved by just composing maps::

        sage: g = PoorManMap(factorial, domain=(1, 2, 3), codomain=(1, 2, 6))
        sage: h = PoorManMap(sqrt, domain=(1, 4, 9), codomain=(1, 2, 3))
        sage: i == g*h
        True
    """
    def __init__(self, function, domain=None, codomain=None, name=None) -> None:
        """
        TESTS::

            sage: from sage.categories.poor_man_map import PoorManMap
            sage: f = PoorManMap(factorial, domain=(1, 2, 3), codomain=(1, 2, 6))
            sage: g = PoorManMap(sqrt, domain=(1, 4, 9), codomain=(1, 2, 6))

            sage: TestSuite(f).run()
            sage: TestSuite(f*g).run()
        """
    def domain(self):
        """
        Return the domain of ``self``.

        EXAMPLES::

            sage: from sage.categories.poor_man_map import PoorManMap
            sage: PoorManMap(lambda x: x+1, domain=(1,2,3), codomain=(2,3,4)).domain()
            (1, 2, 3)
        """
    def codomain(self):
        """
        Return the codomain of ``self``.

        EXAMPLES::

            sage: from sage.categories.poor_man_map import PoorManMap
            sage: PoorManMap(lambda x: x+1, domain=(1,2,3), codomain=(2,3,4)).codomain()
            (2, 3, 4)
        """
    def __eq__(self, other):
        """
        Return whether this map is equal to ``other``.

        EXAMPLES::

            sage: from sage.categories.poor_man_map import PoorManMap
            sage: f = PoorManMap(factorial, domain=(1,2,3), codomain=(1,2,6))
            sage: g = PoorManMap(factorial, domain=(1,2,3), codomain=(1,2,6))
            sage: h1 = PoorManMap(factorial, domain=(1,2,3), codomain=(1,2,6,8))
            sage: h2 = PoorManMap(factorial, domain=(1,2,3), codomain=(1,2,6,8))
            sage: h3 = PoorManMap(factorial, domain=(1,2,3,4), codomain=(1,2,6))
            sage: h4 = PoorManMap(lambda x: x, domain=(1,2,3), codomain=(1,2,6))
            sage: f == g, f == h1, f == h2, f == h3, f == h4, f == 1, 1 == f
            (True, False, False, False, False, False, False)
        """
    def __ne__(self, other):
        """
        Return whether this map is not equal to ``other``.

        EXAMPLES::

            sage: from sage.categories.poor_man_map import PoorManMap
            sage: f = PoorManMap(factorial, domain=(1,2,3), codomain=(1,2,6))
            sage: g = PoorManMap(factorial, domain=(1,2,3), codomain=(1,2,6))
            sage: h1 = PoorManMap(factorial, domain=(1,2,3), codomain=(1,2,6,8))
            sage: h2 = PoorManMap(factorial, domain=(1,2,3), codomain=(1,2,6,8))
            sage: h3 = PoorManMap(factorial, domain=(1,2,3,4), codomain=(1,2,6))
            sage: h4 = PoorManMap(lambda x: x, domain=(1,2,3), codomain=(1,2,6))
            sage: f != g, f != h1, f != h2, f != h3, f != h4, f != 1, 1 != f
            (False, True, True, True, True, True, True)
        """
    def __hash__(self):
        """
        Return a hash value for this map.

        TESTS::

            sage: from sage.categories.poor_man_map import PoorManMap
            sage: f = PoorManMap(factorial, domain=(1,2,3), codomain=(1,2,6))
            sage: g = PoorManMap(factorial, domain=(1,2,3), codomain=(1,2,6))
            sage: hash(f) == hash(g)
            True
        """
    def __mul__(self, other):
        """
        Composition.

        INPUT:

        - ``self`` -- a map `f`
        - ``other`` -- a map `g`

        Returns the composition map `f\\circ g` of `f` and `g`

        EXAMPLES::

            sage: from sage.categories.poor_man_map import PoorManMap
            sage: f = PoorManMap(lambda x: x+1, domain=(1,2,3), codomain=(2,3,4))
            sage: g = PoorManMap(lambda x: -x,  domain=(2,3,4), codomain=(-2,-3,-4))
            sage: g*f
            A map from (1, 2, 3) to (-2, -3, -4)

        Note that the compatibility of the domains and codomains is for performance
        reasons only checked for proper parents. For example, the incompatibility
        is not detected here::

            sage: f*g
            A map from (2, 3, 4) to (2, 3, 4)

        But it is detected here::

            sage: g = PoorManMap(factorial, domain=ZZ, codomain=ZZ)
            sage: h = PoorManMap(sqrt, domain=RR, codomain=CC)                          # needs sage.rings.real_mpfr
            sage: g*h                                                                   # needs sage.rings.real_mpfr
            Traceback (most recent call last):
            ...
            ValueError: the codomain Complex Field with 53 bits of precision
            does not coerce into the domain Integer Ring
            sage: h*g                                                                   # needs sage.rings.real_mpfr
            A map from Integer Ring to Complex Field with 53 bits of precision
        """
    def __call__(self, *args):
        """
        EXAMPLES::

            sage: from sage.categories.poor_man_map import PoorManMap
            sage: f = PoorManMap(lambda x: x+1, domain=(1,2,3), codomain=(2,3,4))
            sage: f(2)
            3

            sage: g = PoorManMap(lambda x: -x,  domain=(2,3,4), codomain=(-2,-3,-4))
            sage: (g*f)(2)
            -3
        """
