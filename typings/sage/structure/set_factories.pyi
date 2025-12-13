from sage.misc.abstract_method import abstract_method as abstract_method
from sage.structure.parent import Parent as Parent
from sage.structure.sage_object import SageObject as SageObject
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class SetFactory(UniqueRepresentation, SageObject):
    '''
    This class is currently just a stub that we will be using to add
    more structures on factories.

    TESTS::

        sage: from sage.structure.set_factories import SetFactory
        sage: S = SetFactory()
        sage: S.__call__("foo")
        Traceback (most recent call last):
        ...
        NotImplementedError: <abstract method __call__ at ...>
        sage: S.add_constraints("foo")
        Traceback (most recent call last):
        ...
        NotImplementedError: <abstract method add_constraints at ...>
    '''
    @abstract_method
    def __call__(self, *constraints, **consdict) -> None:
        """
        Construct the parent associated with the constraints in
        argument. This should return a :class:`Parent`.

        .. NOTE::

            Currently there is no specification on how constraints are
            passed as arguments.

        EXAMPLES::

            sage: from sage.structure.set_factories_example import XYPairs
            sage: XYPairs()
            AllPairs
            sage: XYPairs(3)
            {(3, b) | b in range(5)}

            sage: XYPairs(x=3)
            {(3, b) | b in range(5)}

            sage: XYPairs(y=2)
            {(a, 2) | a in range(5)}

        TESTS::

            sage: from sage.structure.set_factories import SetFactory
            sage: F = SetFactory()
            sage: F()
            Traceback (most recent call last):
            ...
            NotImplementedError: <abstract method __call__ at 0x...>
        """
    @abstract_method
    def add_constraints(self, cons, *args, **opts) -> None:
        """
        Add constraints to the set of constraints `cons`.

        Should return a set of constraints.

        .. NOTE::

            Currently there is no specification on how constraints are
            passed as arguments.

        EXAMPLES::

            sage: from sage.structure.set_factories_example import XYPairs
            sage: XYPairs.add_constraints((3,),((None, 2), {}))
            (3, 2)

            sage: XYPairs.add_constraints((3,),((None, None), {'y': 2}))
            (3, 2)

        TESTS::

            sage: from sage.structure.set_factories import SetFactory
            sage: F = SetFactory()
            sage: F.add_constraints(())
            Traceback (most recent call last):
            ...
            NotImplementedError: <abstract method add_constraints at 0x...>
        """

class SetFactoryPolicy(UniqueRepresentation, SageObject):
    """
    Abstract base class for policies.

    A policy is a device which is passed to a parent inheriting from
    :class:`ParentWithSetFactory` in order to set-up the element
    construction framework.

    INPUT:

    - ``factory`` -- a :class:`SetFactory`

    .. WARNING::

        This class is a base class for policies, one should not try
        to create instances.
    """
    def __init__(self, factory) -> None:
        """
        TESTS::

            sage: from sage.structure.set_factories import SetFactoryPolicy
            sage: from sage.structure.set_factories_example import XYPairs
            sage: S = SetFactoryPolicy(XYPairs); S
            <sage.structure.set_factories.SetFactoryPolicy object at ...>
        """
    def factory(self):
        """
        Return the factory for ``self``.

        EXAMPLES::

            sage: from sage.structure.set_factories import SetFactoryPolicy, SelfParentPolicy
            sage: from sage.structure.set_factories_example import XYPairs, XYPair
            sage: XYPairs._default_policy.factory()
            Factory for XY pairs
            sage: XYPairs._default_policy.factory() is XYPairs
            True

        TESTS::

            sage: policy = SetFactoryPolicy(XYPairs)
            sage: policy.factory()
            Factory for XY pairs
            sage: SelfParentPolicy(XYPairs, XYPair).factory()
            Factory for XY pairs
        """
    def self_element_constructor_attributes(self, Element):
        """
        Element Constructor Attributes for non facade parent.

        The list of attributes which must be set during the init of a
        non facade parent with factory.

        INPUT:

        - ``Element`` -- the class used for the elements

        EXAMPLES::

            sage: from sage.structure.set_factories_example import XYPairs, XYPair
            sage: pol = XYPairs._default_policy
            sage: pol.self_element_constructor_attributes(XYPair)
            {'Element': <class 'sage.structure.set_factories_example.XYPair'>,
             '_parent_for': 'self'}
        """
    def facade_element_constructor_attributes(self, parent):
        """
        Element Constructor Attributes for facade parent.

        The list of attributes which must be set during the init of a
        facade parent with factory.

        INPUT:

        - ``parent`` -- the actual parent for the elements

        EXAMPLES::

            sage: from sage.structure.set_factories_example import XYPairs, XYPair
            sage: pol = XYPairs._default_policy
            sage: pol.facade_element_constructor_attributes(XYPairs())
            {'_facade_for': AllPairs,
             '_parent_for': AllPairs,
             'element_class': <class 'sage.structure.set_factories_example.AllPairs_with_category.element_class'>}
        """
    @abstract_method
    def element_constructor_attributes(self, constraints) -> None:
        """
        Element constructor attributes.

        INPUT:

        - ``constraints`` -- a bunch of constraints

        Should return the attributes that are prerequisite for element
        construction. This is coordinated with
        :meth:`ParentWithSetFactory._element_constructor_`. Currently two standard
        attributes are provided in
        :meth:`facade_element_constructor_attributes` and
        :meth:`self_element_constructor_attributes`. You should return the
        one needed depending on the given constraints.

        EXAMPLES::

            sage: from sage.structure.set_factories_example import XYPairs, XYPair
            sage: pol = XYPairs._default_policy
            sage: pol.element_constructor_attributes(())
            {'Element': <class 'sage.structure.set_factories_example.XYPair'>,
             '_parent_for': 'self'}
            sage: pol.element_constructor_attributes((1))
            {'_facade_for': AllPairs,
             '_parent_for': AllPairs,
             'element_class': <class 'sage.structure.set_factories_example.AllPairs_with_category.element_class'>}
        """

class SelfParentPolicy(SetFactoryPolicy):
    """
    Policy where each parent is a standard parent.

    INPUT:

    - ``factory`` -- an instance of :class:`SetFactory`
    - ``Element`` -- a subclass of :class:`~.element.Element`

    Given a factory ``F`` and a class ``E``, returns a policy for
    parent ``P`` creating elements in class ``E`` and parent ``P``
    itself.

    EXAMPLES::

        sage: from sage.structure.set_factories import SelfParentPolicy
        sage: from sage.structure.set_factories_example import XYPairs, XYPair, Pairs_Y
        sage: pol = SelfParentPolicy(XYPairs, XYPair)
        sage: S = Pairs_Y(3, pol)
        sage: el = S.an_element()
        sage: el.parent() is S
        True

        sage: class Foo(XYPair): pass
        sage: pol = SelfParentPolicy(XYPairs, Foo)
        sage: S = Pairs_Y(3, pol)
        sage: el = S.an_element()
        sage: isinstance(el, Foo)
        True
    """
    def __init__(self, factory, Element) -> None:
        """
        TESTS::

            sage: from sage.structure.set_factories import SelfParentPolicy
            sage: from sage.structure.set_factories_example import XYPairs, XYPair
            sage: S = SelfParentPolicy(XYPairs, XYPair); S
            Set factory policy for <class 'sage.structure.set_factories_example.XYPair'> with parent ``self``
            sage: TestSuite(S).run(skip='_test_category')
        """
    def element_constructor_attributes(self, constraints):
        """
        Return the element constructor attributes as per
        :meth:`SetFactoryPolicy.element_constructor_attributes`

        INPUT:

        - ``constraints`` -- a bunch of constraints

        TESTS::

            sage: from sage.structure.set_factories import SelfParentPolicy
            sage: from sage.structure.set_factories_example import XYPairs, XYPair
            sage: pol = SelfParentPolicy(XYPairs, XYPair)
            sage: pol.element_constructor_attributes(())
            {'Element': <class 'sage.structure.set_factories_example.XYPair'>,
             '_parent_for': 'self'}
        """

class TopMostParentPolicy(SetFactoryPolicy):
    """
    Policy where the parent of the elements is the topmost parent.

    INPUT:

    - ``factory`` -- an instance of :class:`SetFactory`
    - ``top_constraints`` -- the empty set of constraints
    - ``Element`` -- a subclass of :class:`~.element.Element`

    Given a factory ``F`` and a class ``E``, returns a policy for
    parent ``P`` creating element in class ``E`` and parent
    ``factory(*top_constraints, policy)``.

    EXAMPLES::

        sage: from sage.structure.set_factories_example import XYPairs, XYPair
        sage: P = XYPairs(); P.policy()
        Set factory policy for <class 'sage.structure.set_factories_example.XYPair'> with parent AllPairs[=Factory for XY pairs(())]
    """
    def __init__(self, factory, top_constraints, Element) -> None:
        """
        TESTS::

            sage: from sage.structure.set_factories import TopMostParentPolicy
            sage: from sage.structure.set_factories_example import XYPairs, XYPair
            sage: T = TopMostParentPolicy(XYPairs, (), XYPair); T
            Set factory policy for <class 'sage.structure.set_factories_example.XYPair'> with parent AllPairs[=Factory for XY pairs(())]
            sage: TestSuite(T).run(skip='_test_category')
        """
    def element_constructor_attributes(self, constraints):
        """
        Return the element constructor attributes as per
        :meth:`SetFactoryPolicy.element_constructor_attributes`.

        INPUT:

        - ``constraints`` -- a bunch of constraints

        TESTS::

            sage: from sage.structure.set_factories import TopMostParentPolicy
            sage: from sage.structure.set_factories_example import XYPairs, XYPair
            sage: pol = TopMostParentPolicy(XYPairs, (), XYPair)
            sage: pol.element_constructor_attributes(())
            {'Element': <class 'sage.structure.set_factories_example.XYPair'>,
             '_parent_for': 'self'}
            sage: pol.element_constructor_attributes((1))
            {'_facade_for': AllPairs,
             '_parent_for': AllPairs,
             'element_class': <class 'sage.structure.set_factories_example.AllPairs_with_category.element_class'>}
        """

class FacadeParentPolicy(SetFactoryPolicy):
    """
    Policy for facade parent.

    INPUT:

    - ``factory`` -- an instance of :class:`SetFactory`
    - ``parent`` -- an instance of :class:`Parent`

    Given a factory ``F`` and a class ``E``, returns a policy for
    parent ``P`` creating elements as if they were created by
    ``parent``.

    EXAMPLES::

        sage: from sage.structure.set_factories import SelfParentPolicy, FacadeParentPolicy
        sage: from sage.structure.set_factories_example import XYPairs, XYPair

    We create a custom standard parent ``P``::

        sage: selfpolicy = SelfParentPolicy(XYPairs, XYPair)
        sage: P = XYPairs(x=2, policy=selfpolicy)
        sage: pol = FacadeParentPolicy(XYPairs, P)
        sage: P2 = XYPairs(x=2, y=3, policy=pol)
        sage: el = P2.an_element()
        sage: el.parent() is P
        True
        sage: type(el) is P.element_class
        True

    If ``parent`` is itself a facade parent, then transitivity is
    correctly applied::

        sage: P =  XYPairs()
        sage: P2 = XYPairs(x=2)
        sage: P2.category()
        Category of facade finite enumerated sets
        sage: pol = FacadeParentPolicy(XYPairs, P)
        sage: P23 = XYPairs(x=2, y=3, policy=pol)
        sage: el = P2.an_element()
        sage: el.parent() is P
        True
        sage: type(el) is P.element_class
        True
    """
    def __init__(self, factory, parent) -> None:
        """
        TESTS::

            sage: from sage.structure.set_factories import FacadeParentPolicy
            sage: from sage.structure.set_factories_example import XYPairs, XYPair
            sage: F = FacadeParentPolicy(XYPairs, XYPairs()); F
            Set factory policy for facade parent AllPairs
            sage: TestSuite(F).run(skip='_test_category')
        """
    def element_constructor_attributes(self, constraints):
        """
        Return the element constructor attributes as per
        :meth:`SetFactoryPolicy.element_constructor_attributes`.

        INPUT:

        - ``constraints`` -- a bunch of constraints

        TESTS::

            sage: from sage.structure.set_factories import FacadeParentPolicy
            sage: from sage.structure.set_factories_example import XYPairs, XYPair
            sage: pol = FacadeParentPolicy(XYPairs, XYPairs())
            sage: pol.element_constructor_attributes(())
            {'_facade_for': AllPairs,
             '_parent_for': AllPairs,
             'element_class': <class 'sage.structure.set_factories_example.AllPairs_with_category.element_class'>}
            sage: pol.element_constructor_attributes((1))
            {'_facade_for': AllPairs,
             '_parent_for': AllPairs,
             'element_class': <class 'sage.structure.set_factories_example.AllPairs_with_category.element_class'>}
        """

class BareFunctionPolicy(SetFactoryPolicy):
    """
    Policy where element are constructed using a bare function.

    INPUT:

    - ``factory`` -- an instance of :class:`SetFactory`
    - ``constructor`` -- a function

    Given a factory ``F`` and a function ``c``, returns a policy for
    parent ``P`` creating element using the function ``f``.

    EXAMPLES::

        sage: from sage.structure.set_factories import BareFunctionPolicy
        sage: from sage.structure.set_factories_example import XYPairs
        sage: cons = lambda t, check: tuple(t) # ignore the check parameter
        sage: tuplepolicy = BareFunctionPolicy(XYPairs, cons)
        sage: P = XYPairs(x=2, policy=tuplepolicy)
        sage: el = P.an_element()
        sage: type(el)
        <... 'tuple'>
    """
    def __init__(self, factory, constructor) -> None:
        """
        TESTS::

            sage: from sage.structure.set_factories import BareFunctionPolicy
            sage: from sage.structure.set_factories_example import XYPairs
            sage: pol = BareFunctionPolicy(XYPairs, tuple)
            sage: TestSuite(pol).run(skip='_test_category')
        """
    def element_constructor_attributes(self, constraints):
        """
        Return the element constructor attributes as per
        :meth:`SetFactoryPolicy.element_constructor_attributes`.

        INPUT:

        - ``constraints`` -- a bunch of constraints

        TESTS::

            sage: from sage.structure.set_factories import BareFunctionPolicy
            sage: from sage.structure.set_factories_example import XYPairs
            sage: pol = BareFunctionPolicy(XYPairs, tuple)
            sage: pol.element_constructor_attributes(())
            {'_element_constructor_': <... 'tuple'>, '_parent_for': None}
        """

class ParentWithSetFactory(Parent):
    """
    Abstract class for parent belonging to a set factory.

    INPUT:

    - ``constraints`` -- set of constraints
    - ``policy`` -- the policy for element construction
    - ``category`` -- the category of the parent (default: ``None``)

    Depending on the constraints and the policy, initialize the parent
    in a proper category to set up element construction.

    EXAMPLES::

        sage: from sage.structure.set_factories_example import XYPairs, PairsX_
        sage: P = PairsX_(3, XYPairs._default_policy)
        sage: P is XYPairs(3)
        True
        sage: P.category()
        Category of facade finite enumerated sets
    """
    def __init__(self, constraints, policy, category=None) -> None:
        """
        TESTS::

            sage: from sage.structure.set_factories import ParentWithSetFactory
            sage: from sage.structure.set_factories_example import XYPairs
            sage: isinstance(XYPairs(3), ParentWithSetFactory)  # indirect doctest
            True
        """
    def constraints(self):
        """
        Return the constraints defining ``self``.

        .. NOTE::

            Currently there is no specification on how constraints are
            passed as arguments.

        EXAMPLES::

            sage: from sage.structure.set_factories_example import XYPairs
            sage: XYPairs().constraints()
            ()
            sage: XYPairs(x=3).constraints()
            (3, None)
            sage: XYPairs(y=2).constraints()
            (None, 2)
        """
    def policy(self):
        """
        Return the policy used when ``self`` was created.

        EXAMPLES::

            sage: from sage.structure.set_factories_example import XYPairs
            sage: XYPairs().policy()
            Set factory policy for <class 'sage.structure.set_factories_example.XYPair'> with parent AllPairs[=Factory for XY pairs(())]
            sage: XYPairs(x=3).policy()
            Set factory policy for <class 'sage.structure.set_factories_example.XYPair'> with parent AllPairs[=Factory for XY pairs(())]
        """
    def facade_policy(self):
        """
        Return the policy for parent facade for ``self``.

        EXAMPLES::

            sage: from sage.structure.set_factories import SelfParentPolicy
            sage: from sage.structure.set_factories_example import XYPairs, XYPair

        We create a custom standard parent ``P``::

            sage: selfpolicy = SelfParentPolicy(XYPairs, XYPair)
            sage: P = XYPairs(x=2, policy=selfpolicy)
            sage: P.facade_policy()
            Set factory policy for facade parent {(2, b) | b in range(5)}

        Now passing ``P.facade_policy()`` creates parent which are facade for
        ``P``::

            sage: P3 = XYPairs(x=2, y=3, policy=P.facade_policy())
            sage: P3.facade_for() == (P,)
            True
            sage: el = P3.an_element()
            sage: el.parent() is P
            True
        """
    def factory(self):
        """
        Return the factory which built ``self``.

        EXAMPLES::

            sage: from sage.structure.set_factories_example import XYPairs
            sage: XYPairs().factory() is XYPairs
            True
            sage: XYPairs(x=3).factory() is XYPairs
            True
        """
    def subset(self, *args, **options):
        """
        Return a subset of ``self`` by adding more constraints.

        .. NOTE::

            Currently there is no specification on how constraints are
            passed as arguments.

        EXAMPLES::

            sage: from sage.structure.set_factories_example import XYPairs
            sage: S = XYPairs()
            sage: S3 = S.subset(x=3)
            sage: S3.list()
            [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4)]

        TESTS::

            sage: S3 is XYPairs(3)
            True
            sage: S3 is XYPairs(x=3)
            True
        """
    @abstract_method
    def check_element(self, x, check) -> None:
        """
        Check that ``x`` verifies the constraints of ``self``.

        INPUT:

        - ``x`` -- an instance of ``self.element_class``

        - ``check`` -- the level of checking to be performed (usually a
          boolean)

        This method may assume that ``x`` was properly constructed by
        ``self`` or a possible super-set of ``self`` for which
        ``self`` is a facade. It should return nothing if ``x``
        verifies the constraints and raise a
        :exc:`~exceptions.ValueError` explaining which constraints
        ``x`` fails otherwise.

        The method should accept an extra parameter check specifying
        which level of check should be performed. It will only be
        called when ``bool(check)`` evaluates to ``True``.

        .. TODO::

            Should we always call check element and let it decide
            which check has to be performed ?

        EXAMPLES::

            sage: from sage.structure.set_factories_example import XYPairs
            sage: S = XYPairs()
            sage: el = S((2,3))
            sage: S.check_element(el, True)
            sage: XYPairs(x=2).check_element(el, True)
            sage: XYPairs(x=3).check_element(el, True)
            Traceback (most recent call last):
            ...
            ValueError: Wrong first coordinate
            sage: XYPairs(y=4).check_element(el, True)
            Traceback (most recent call last):
            ...
            ValueError: Wrong second coordinate
        """
    def __contains__(self, x) -> bool:
        """
        Default implementation for ``__contains__``.

        INPUT:

        - ``x`` -- any object

        Check for class, parent and calls ``self.check_element(x)``.

        TESTS::

            sage: from sage.structure.set_factories_example import XYPairs
            sage: S = XYPairs()
            sage: el = S((2,3))
            sage: el in S
            True
            sage: el in XYPairs(x=2)
            True
            sage: el in XYPairs(x=3)
            False
            sage: el in XYPairs(y=4)
            False
        """
    def __call__(self, *args, **keywords):
        """
        TESTS::

            sage: from sage.structure.set_factories_example import XYPairs
            sage: S = XYPairs()
            sage: el = S((2,3)); el
            (2, 3)
            sage: S(el) is el
            True

            sage: XYPairs(x=3)((2,3))
            Traceback (most recent call last):
            ...
            ValueError: Wrong first coordinate

            sage: XYPairs(x=3)(el)
            Traceback (most recent call last):
            ...
            ValueError: Wrong first coordinate
        """
