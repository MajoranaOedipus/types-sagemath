from sage.combinat.posets.elements import LatticePosetElement as LatticePosetElement
from sage.combinat.posets.lattices import FiniteLatticePoset as FiniteLatticePoset
from sage.combinat.posets.posets import FinitePoset as FinitePoset, Poset as Poset
from sage.sets.set import Set as Set

class AnalyticTypeElement(LatticePosetElement):
    '''
    Analytic types of forms and/or spaces.

    An analytic type element describes what basic analytic
    properties are contained/included in it.

    EXAMPLES::

        sage: from sage.modular.modform_hecketriangle.analytic_type import (AnalyticType, AnalyticTypeElement)
        sage: from sage.combinat.posets.elements import LatticePosetElement
        sage: AT = AnalyticType()
        sage: el = AT(["quasi", "cusp"])
        sage: el
        quasi cuspidal
        sage: isinstance(el, AnalyticTypeElement)
        True
        sage: isinstance(el, LatticePosetElement)
        True
        sage: el.parent() == AT
        True
        sage: sorted(el.element,key=str)
        [cusp, quasi]
        sage: from sage.sets.set import Set_object_enumerated
        sage: isinstance(el.element, Set_object_enumerated)
        True
        sage: first = sorted(el.element,key=str)[0]; first
        cusp
        sage: first.parent() == AT.base_poset()
        True

        sage: el2 = AT("holo")
        sage: sum = el + el2
        sage: sum
        quasi modular
        sage: sorted(sum.element,key=str)
        [cusp, holo, quasi]
        sage: el * el2
        cuspidal
    '''
    def analytic_space_name(self):
        '''
        Return the (analytic part of the) name of a space
        with the analytic type of ``self``.

        This is used for the string representation of such spaces.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.analytic_type import AnalyticType
            sage: AT = AnalyticType()
            sage: AT(["quasi", "weak"]).analytic_space_name()
            \'QuasiWeakModular\'
            sage: AT(["quasi", "cusp"]).analytic_space_name()
            \'QuasiCusp\'
            sage: AT(["quasi"]).analytic_space_name()
            \'Zero\'
            sage: AT([]).analytic_space_name()
            \'Zero\'
        '''
    def latex_space_name(self):
        '''
        Return the short (analytic part of the) name of a space
        with the analytic type of ``self`` for usage with latex.

        This is used for the latex representation of such spaces.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.analytic_type import AnalyticType
            sage: AT = AnalyticType()
            sage: AT("mero").latex_space_name()
            \'\\\\tilde{M}\'
            sage: AT("weak").latex_space_name()
            \'M^!\'
            sage: AT(["quasi", "cusp"]).latex_space_name()
            \'QC\'
            sage: AT([]).latex_space_name()
            \'Z\'
        '''
    def analytic_name(self):
        '''
        Return a string representation of the analytic type.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.analytic_type import AnalyticType
            sage: AT = AnalyticType()
            sage: AT(["quasi", "weak"]).analytic_name()
            \'quasi weakly holomorphic modular\'
            sage: AT(["quasi", "cusp"]).analytic_name()
            \'quasi cuspidal\'
            sage: AT(["quasi"]).analytic_name()
            \'zero\'
            sage: AT([]).analytic_name()
            \'zero\'
        '''
    def reduce_to(self, reduce_type):
        '''
        Return a new analytic type which contains only analytic properties
        specified in both ``self`` and ``reduce_type``.

        INPUT:

        - ``reduce_type`` -- an analytic type or something which is
          convertible to an analytic type

        OUTPUT: the new reduced analytic type

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.analytic_type import AnalyticType
            sage: AT = AnalyticType()
            sage: el = AT(["quasi", "cusp"])
            sage: el2 = AT("holo")

            sage: el.reduce_to(el2)
            cuspidal
            sage: el.reduce_to(el2) == el * el2
            True
        '''
    def extend_by(self, extend_type):
        '''
        Return a new analytic type which contains all analytic properties
        specified either in ``self`` or in ``extend_type``.

        INPUT:

        - ``extend_type`` -- an analytic type or something which is
          convertible to an analytic type

        OUTPUT: the new extended analytic type

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.analytic_type import AnalyticType
            sage: AT = AnalyticType()
            sage: el = AT(["quasi", "cusp"])
            sage: el2 = AT("holo")

            sage: el.extend_by(el2)
            quasi modular
            sage: el.extend_by(el2) == el + el2
            True
        '''
    def __iter__(self):
        '''
        Return an iterator of ``self`` which gives the basic analytic
        properties contained in ``self`` as strings.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.analytic_type import AnalyticType
            sage: el = AnalyticType()(["quasi", "weak"])
            sage: sorted(el)
            [\'cusp\', \'holo\', \'quasi\', \'weak\']
            sage: "mero" in el
            False
            sage: "cusp" in el
            True
        '''

class AnalyticType(FiniteLatticePoset):
    '''
    Container for all possible analytic types of forms and/or spaces.

    The ``analytic type`` of forms spaces or rings describes all possible
    occurring basic ``analytic properties`` of elements in the space/ring
    (or more).

    For ambient spaces/rings this means that all elements with those properties
    (and the restrictions of the space/ring) are contained in the space/ring.

    The analytic type of an element is the analytic type of its minimal
    ambient space/ring.

    The basic ``analytic properties`` are:

    - ``quasi`` -- whether the element is quasi modular (and not modular)
      or modular.
    - ``mero`` -- ``meromorphic`` -- if the element is meromorphic
      and meromorphic at infinity
    - ``weak`` -- ``weakly holomorphic`` -- if the element is holomorphic
      and meromorphic at infinity
    - ``holo`` -- ``holomorphic`` -- if the element is holomorphic and
      holomorphic at infinity
    - ``cusp`` -- ``cuspidal`` -- if the element additionally has a positive
      order at infinity

    The ``zero`` elements/property have no analytic properties (or only ``quasi``).

    For ring elements the property describes whether one of its homogeneous
    components satisfies that property and the "union" of those properties
    is returned as the ``analytic type``.

    Similarly for quasi forms the property describes whether one of its
    quasi components satisfies that property.

    There is a (natural) partial order between the basic properties
    (and analytic types) given by "inclusion". We name the analytic type
    according to its maximal analytic properties.

    For `n=3` the quasi form ``el = E6 - E2^3`` has the quasi components ``E6``
    which is ``holomorphic`` and ``E2^3`` which is ``quasi holomorphic``.
    So the analytic type of ``el`` is ``quasi holomorphic`` despite the fact
    that the sum (``el``) describes a function which is zero at infinity.

    EXAMPLES::

        sage: from sage.modular.modform_hecketriangle.space import QuasiModularForms
        sage: x,y,z,d = var("x,y,z,d")                                                  # needs sage.symbolic
        sage: el = QuasiModularForms(n=3, k=6, ep=-1)(y-z^3)                            # needs sage.symbolic
        sage: el.analytic_type()                                                        # needs sage.symbolic
        quasi modular

    Similarly the type of the ring element ``el2 = E4/Delta - E6/Delta`` is
    ``weakly holomorphic`` despite the fact that the sum (``el2``) describes
    a function which is holomorphic at infinity::

        sage: from sage.modular.modform_hecketriangle.graded_ring import WeakModularFormsRing
        sage: x,y,z,d = var("x,y,z,d")                                                  # needs sage.symbolic
        sage: el2 = WeakModularFormsRing(n=3)(x/(x^3-y^2)-y/(x^3-y^2))                  # needs sage.symbolic
        sage: el2.analytic_type()                                                       # needs sage.symbolic
        weakly holomorphic modular
    '''
    Element = AnalyticTypeElement
    @staticmethod
    def __classcall__(cls):
        """
        Directly return the classcall of UniqueRepresentation
        (skipping the classcalls of the other superclasses).

        That's because ``self`` is supposed to be used as a Singleton.
        It initializes the FinitelatticePoset with the proper arguments
        by itself in ``self.__init__()``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.analytic_type import AnalyticType
            sage: AT = AnalyticType()
            sage: AT2 = AnalyticType()
            sage: AT is AT2
            True
        """
    def __init__(self) -> None:
        """
        Container for all possible analytic types of forms and/or spaces.

        This class is supposed to be used as a Singleton.

        It first creates a ``Poset`` that contains all basic analytic
        properties to be modeled by the AnalyticType. Then the order
        ideals lattice of that Poset is taken as the underlying
        FiniteLatticePoset of ``self``.

        In particular elements of ``self`` describe what basic analytic
        properties are contained/included in that element.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.analytic_type import AnalyticType
            sage: from sage.combinat.posets.lattices import FiniteLatticePoset
            sage: AT = AnalyticType()
            sage: AT
            Analytic Type
            sage: isinstance(AT, FiniteLatticePoset)
            True

            sage: AT.is_lattice()
            True
            sage: AT.is_finite()
            True
            sage: AT.cardinality()
            10
            sage: AT.is_modular()
            True
            sage: AT.is_bounded()
            True
            sage: AT.is_distributive()
            True
            sage: sorted(AT, key=str)
            [cuspidal,
            meromorphic modular,
            modular,
            quasi cuspidal,
            quasi meromorphic modular,
            quasi modular,
            quasi weakly holomorphic modular,
            weakly holomorphic modular,
            zero,
            zero]
            sage: len(AT.relations())
            45
            sage: sortkey = lambda xy: (str(xy[0]), str(xy[1]))
            sage: sorted(AT.cover_relations(), key=sortkey)
            [[cuspidal, modular],
             [cuspidal, quasi cuspidal],
             [meromorphic modular, quasi meromorphic modular],
             [modular, quasi modular],
             [modular, weakly holomorphic modular],
             [quasi cuspidal, quasi modular],
             [quasi modular, quasi weakly holomorphic modular],
             [quasi weakly holomorphic modular, quasi meromorphic modular],
             [weakly holomorphic modular, meromorphic modular],
             [weakly holomorphic modular, quasi weakly holomorphic modular],
             [zero, cuspidal],
             [zero, quasi cuspidal],
             [zero, zero]]
            sage: AT.has_top()
            True
            sage: AT.has_bottom()
            True
            sage: AT.top()
            quasi meromorphic modular
            sage: AT.bottom()
            zero
        """
    def __call__(self, *args, **kwargs):
        '''
        Return the result of the corresponding call function
        of ``FiniteLatticePoset``.

        If more than one argument is given it is called with
        the list of those arguments instead.

        .. NOTE::

            The function just extends the ``__call__`` function to allow multiple arguments
            (see the example below).

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.analytic_type import AnalyticType
            sage: AT = AnalyticType()
            sage: AT("holo", "quasi") == AT(["holo", "quasi"])
            True
        '''
    def base_poset(self):
        """
        Return the base poset from which everything of ``self``
        was constructed. Elements of the base poset correspond
        to the basic ``analytic properties``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.analytic_type import AnalyticType
            sage: from sage.combinat.posets.posets import FinitePoset
            sage: AT = AnalyticType()
            sage: P = AT.base_poset()
            sage: P
            Finite poset containing 5 elements with distinguished linear extension
            sage: isinstance(P, FinitePoset)
            True

            sage: P.is_lattice()
            False
            sage: P.is_finite()
            True
            sage: P.cardinality()
            5
            sage: P.is_bounded()
            False
            sage: P.list()
            [cusp, holo, weak, mero, quasi]

            sage: len(P.relations())
            11
            sage: P.cover_relations()
            [[cusp, holo], [holo, weak], [weak, mero]]
            sage: P.has_top()
            False
            sage: P.has_bottom()
            False
        """
    def lattice_poset(self):
        """
        Return the underlying lattice poset of ``self``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.analytic_type import AnalyticType
            sage: AnalyticType().lattice_poset()
            Finite lattice containing 10 elements
        """
