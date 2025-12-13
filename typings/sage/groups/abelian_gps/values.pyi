from sage.categories.morphism import Morphism as Morphism
from sage.groups.abelian_gps.abelian_group import AbelianGroup_class as AbelianGroup_class
from sage.groups.abelian_gps.abelian_group_element import AbelianGroupElement as AbelianGroupElement
from sage.misc.misc_c import prod as prod
from sage.rings.integer import Integer as Integer

def AbelianGroupWithValues(values, n, gens_orders=None, names: str = 'f', check: bool = False, values_group=None):
    """
    Construct an Abelian group with values associated to the generators.

    INPUT:

    - ``values`` -- list/tuple/iterable of values that you want to
      associate to the generators

    - ``n`` -- integer (optional); if not specified, will be derived
      from ``gens_orders``

    - ``gens_orders`` -- list of nonnegative integers in the form
       `[a_0, a_1, \\dots, a_{n-1}]`, typically written in increasing
       order. This list is padded with zeros if it has length less
       than n. The orders of the commuting generators, with `0`
       denoting an infinite cyclic factor.

    - ``names`` -- (optional) names of generators

    - ``values_group`` -- a parent or ``None`` (default). The common
      parent of the values. This might be a group, but can also just
      contain the values. For example, if the values are units in a
      ring then the ``values_group`` would be the whole ring. If
      ``None`` it will be derived from the values.

    EXAMPLES::

        sage: G = AbelianGroupWithValues([-1], [6])
        sage: g = G.gen(0)
        sage: for i in range(7):
        ....:     print((i, g^i, (g^i).value()))
        (0, 1, 1)
        (1, f, -1)
        (2, f^2, 1)
        (3, f^3, -1)
        (4, f^4, 1)
        (5, f^5, -1)
        (6, 1, 1)
        sage: G.values_group()
        Integer Ring

    The group elements come with a coercion embedding into the
    :meth:`values_group`, so you can use them like their
    :meth:`~sage.groups.abelian_gps.value.AbelianGroupWithValuesElement.value`
    ::

        sage: G.values_embedding()
        Generic morphism:
          From: Multiplicative Abelian group isomorphic to C6
          To:   Integer Ring
        sage: g.value()
        -1
        sage: 0 + g
        -1
        sage: 1 + 2*g
        -1
    """

class AbelianGroupWithValuesEmbedding(Morphism):
    """
    The morphism embedding the Abelian group with values in its values group.

    INPUT:

    - ``domain`` -- a :class:`AbelianGroupWithValues_class`

    - ``codomain`` -- the values group (need not be in the category of
      groups, e.g. symbolic ring)

    EXAMPLES::

        sage: # needs sage.symbolic
        sage: Z4.<g> = AbelianGroupWithValues([I], [4])
        sage: embedding = Z4.values_embedding();  embedding
        Generic morphism:
          From: Multiplicative Abelian group isomorphic to C4
          To:   Number Field in I with defining polynomial x^2 + 1 with I = 1*I
        sage: embedding(1)
        1
        sage: embedding(g)
        I
        sage: embedding(g^2)
        -1
    """
    def __init__(self, domain, codomain) -> None:
        """
        Construct the morphism.

        TESTS::

            sage: Z4 = AbelianGroupWithValues([I], [4])                                 # needs sage.symbolic
            sage: from sage.groups.abelian_gps.values import AbelianGroupWithValuesEmbedding
            sage: AbelianGroupWithValuesEmbedding(Z4, Z4.values_group())                # needs sage.symbolic
            Generic morphism:
              From: Multiplicative Abelian group isomorphic to C4
              To:   Number Field in I with defining polynomial x^2 + 1 with I = 1*I
        """

class AbelianGroupWithValuesElement(AbelianGroupElement):
    """
    An element of an Abelian group with values assigned to generators.

    INPUT:

    - ``exponents`` -- tuple of integers; the exponent vector defining
      the group element

    - ``parent`` -- the parent

    - ``value`` -- the value assigned to the group element or ``None``
      (default); in the latter case, the value is computed as needed

    EXAMPLES::

        sage: F = AbelianGroupWithValues([1,-1], [2,4])
        sage: a,b = F.gens()
        sage: TestSuite(a*b).run()
    """
    def __init__(self, parent, exponents, value=None) -> None:
        """
        Create an element.

        EXAMPLES::

            sage: F = AbelianGroupWithValues([1,-1], [2,4])
            sage: a,b = F.gens()
            sage: a*b^-1 in F
            True
            sage: (a*b^-1).value()
            -1
        """
    def value(self):
        """
        Return the value of the group element.

        OUTPUT: the value according to the values for generators; see
        :meth:`~AbelianGroupWithValues.gens_values`

        EXAMPLES::

            sage: G = AbelianGroupWithValues([5], 1)
            sage: G.0.value()
            5
        """
    def __pow__(self, n):
        """
        Exponentiate ``self``.

        INPUT:

        - ``n`` -- integer; the exponent

        TESTS::

            sage: G.<a,b> = AbelianGroupWithValues([5,2], 2)
            sage: a^3
            a^3
            sage: (a^3).value()
            125
        """
    def __invert__(self):
        """
        Return the inverse element.

        EXAMPLES::

            sage: G.<a,b> = AbelianGroupWithValues([2,-1], [0,4])
            sage: a.inverse()   # indirect doctest
            a^-1
            sage: a.inverse().value()
            1/2
            sage: a.__invert__().value()
            1/2
            sage: (~a).value()
            1/2
            sage: (a*b).value()
            -2
            sage: (a*b).inverse().value()
            -1/2
        """

class AbelianGroupWithValues_class(AbelianGroup_class):
    """
    The class of an Abelian group with values associated to the generator.

    INPUT:

    - ``generator_orders`` -- tuple of integers; the orders of the
      generators

    - ``names`` -- string or list of strings; the names for the generators

    - ``values`` -- tuple the same length as the number of
      generators; the values assigned to the generators

    - ``values_group`` -- the common parent of the values

    EXAMPLES::

        sage: G.<a,b> = AbelianGroupWithValues([2,-1], [0,4])
        sage: TestSuite(G).run()
    """
    Element = AbelianGroupWithValuesElement
    def __init__(self, generator_orders, names, values, values_group) -> None:
        """
        The Python constructor.

        TESTS::

            sage: G = AbelianGroupWithValues([2,-1], [0,4]); G
            Multiplicative Abelian group isomorphic to Z x C4

            sage: cm = sage.structure.element.get_coercion_model()
            sage: cm.explain(G, ZZ, operator.add)
            Coercion on left operand via
                Generic morphism:
                  From: Multiplicative Abelian group isomorphic to Z x C4
                  To:   Integer Ring
            Arithmetic performed after coercions.
            Result lives in Integer Ring
            Integer Ring
        """
    def gen(self, i: int = 0):
        """
        The `i`-th generator of the abelian group.

        INPUT:

        - ``i`` -- integer (default: 0); the index of the generator

        OUTPUT: a group element

        EXAMPLES::

            sage: F = AbelianGroupWithValues([1,2,3,4,5], 5, [], names='a')
            sage: F.0
            a0
            sage: F.0.value()
            1
            sage: F.2
            a2
            sage: F.2.value()
            3

            sage: G = AbelianGroupWithValues([-1,0,1], [2,1,3])
            sage: G.gens()
            (f0, 1, f2)
        """
    def gens_values(self):
        """
        Return the values associated to the generators.

        OUTPUT: tuple

        EXAMPLES::

            sage: G = AbelianGroupWithValues([-1,0,1], [2,1,3])
            sage: G.gens()
            (f0, 1, f2)
            sage: G.gens_values()
            (-1, 0, 1)
        """
    def values_group(self):
        """
        The common parent of the values.

        The values need to form a multiplicative group, but can be
        embedded in a larger structure. For example, if the values are
        units in a ring then the :meth:`values_group` would be the
        whole ring.

        OUTPUT: the common parent of the values, containing the group
        generated by all values

        EXAMPLES::

            sage: G = AbelianGroupWithValues([-1,0,1], [2,1,3])
            sage: G.values_group()
            Integer Ring

            sage: Z4 = AbelianGroupWithValues([I], [4])                                 # needs sage.symbolic
            sage: Z4.values_group()                                                     # needs sage.symbolic
            Number Field in I with defining polynomial x^2 + 1 with I = 1*I
        """
    def values_embedding(self):
        """
        Return the embedding of ``self`` in :meth:`values_group`.

        OUTPUT: a morphism

        EXAMPLES::

            sage: Z4 = AbelianGroupWithValues([I], [4])                                 # needs sage.symbolic
            sage: Z4.values_embedding()                                                 # needs sage.symbolic
            Generic morphism:
              From: Multiplicative Abelian group isomorphic to C4
              To:   Number Field in I with defining polynomial x^2 + 1 with I = 1*I
        """
