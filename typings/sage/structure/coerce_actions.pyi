import _cython_3_2_1
import sage.categories.action
from sage.structure.coerce_exceptions import CoercionException as CoercionException
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

detect_element_action: _cython_3_2_1.cython_function_or_method

class ActOnAction(GenericAction):
    """File: /build/sagemath/src/sage/src/sage/structure/coerce_actions.pyx (starting at line 116)

        Class for actions defined via the _act_on_ method.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class ActedUponAction(GenericAction):
    """File: /build/sagemath/src/sage/src/sage/structure/coerce_actions.pyx (starting at line 138)

        Class for actions defined via the _acted_upon_ method.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class GenericAction(sage.categories.action.Action):
    """GenericAction(Parent G, S, is_left, bool check=True)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, ParentG, S, is_left, boolcheck=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/structure/coerce_actions.pyx (starting at line 50)

                TESTS:

                Note that coerce actions should only be used inside of the coercion
                model. For this test, we need to strongly reference the domains,
                for otherwise they could be garbage collected, giving rise to
                random errors (see :issue:`18157`). ::

                    sage: from sage.structure.coerce_actions import ActedUponAction, GenericAction
                    sage: M = MatrixSpace(ZZ, 2)                                                # needs sage.modules
                    sage: ActedUponAction(M, Cusps, True)                                       # needs sage.modular sage.modules
                    Left action
                     by Full MatrixSpace of 2 by 2 dense matrices over Integer Ring
                     on Set P^1(QQ) of all cusps

                    sage: Z6 = Zmod(6)
                    sage: GenericAction(QQ, Z6, True)
                    Traceback (most recent call last):
                    ...
                    NotImplementedError: action for <class 'sage.structure.coerce_actions.GenericAction'> not implemented

                This will break if we tried to use it::

                    sage: GenericAction(QQ, Z6, True, check=False)
                    Left action by Rational Field on Ring of integers modulo 6
        """
    @overload
    def codomain(self) -> Any:
        '''GenericAction.codomain(self)

        File: /build/sagemath/src/sage/src/sage/structure/coerce_actions.pyx (starting at line 84)

        Return the "codomain" of this action, i.e. the Parent in which the
        result elements live. Typically, this should be the same as the
        acted upon set.

        EXAMPLES:

        Note that coerce actions should only be used inside of the coercion
        model. For this test, we need to strongly reference the domains, for
        otherwise they could be garbage collected, giving rise to random
        errors (see :issue:`18157`). ::


            sage: M = MatrixSpace(ZZ, 2)                                                # needs sage.modules
            sage: A = sage.structure.coerce_actions.ActedUponAction(M, Cusps, True)     # needs sage.modular sage.modules
            sage: A.codomain()                                                          # needs sage.modular sage.modules
            Set P^1(QQ) of all cusps

            sage: # needs sage.groups
            sage: S3 = SymmetricGroup(3)
            sage: QQxyz = QQ[\'x,y,z\']
            sage: A = sage.structure.coerce_actions.ActOnAction(S3, QQxyz, False)
            sage: A.codomain()
            Multivariate Polynomial Ring in x, y, z over Rational Field'''
    @overload
    def codomain(self) -> Any:
        '''GenericAction.codomain(self)

        File: /build/sagemath/src/sage/src/sage/structure/coerce_actions.pyx (starting at line 84)

        Return the "codomain" of this action, i.e. the Parent in which the
        result elements live. Typically, this should be the same as the
        acted upon set.

        EXAMPLES:

        Note that coerce actions should only be used inside of the coercion
        model. For this test, we need to strongly reference the domains, for
        otherwise they could be garbage collected, giving rise to random
        errors (see :issue:`18157`). ::


            sage: M = MatrixSpace(ZZ, 2)                                                # needs sage.modules
            sage: A = sage.structure.coerce_actions.ActedUponAction(M, Cusps, True)     # needs sage.modular sage.modules
            sage: A.codomain()                                                          # needs sage.modular sage.modules
            Set P^1(QQ) of all cusps

            sage: # needs sage.groups
            sage: S3 = SymmetricGroup(3)
            sage: QQxyz = QQ[\'x,y,z\']
            sage: A = sage.structure.coerce_actions.ActOnAction(S3, QQxyz, False)
            sage: A.codomain()
            Multivariate Polynomial Ring in x, y, z over Rational Field'''
    @overload
    def codomain(self) -> Any:
        '''GenericAction.codomain(self)

        File: /build/sagemath/src/sage/src/sage/structure/coerce_actions.pyx (starting at line 84)

        Return the "codomain" of this action, i.e. the Parent in which the
        result elements live. Typically, this should be the same as the
        acted upon set.

        EXAMPLES:

        Note that coerce actions should only be used inside of the coercion
        model. For this test, we need to strongly reference the domains, for
        otherwise they could be garbage collected, giving rise to random
        errors (see :issue:`18157`). ::


            sage: M = MatrixSpace(ZZ, 2)                                                # needs sage.modules
            sage: A = sage.structure.coerce_actions.ActedUponAction(M, Cusps, True)     # needs sage.modular sage.modules
            sage: A.codomain()                                                          # needs sage.modular sage.modules
            Set P^1(QQ) of all cusps

            sage: # needs sage.groups
            sage: S3 = SymmetricGroup(3)
            sage: QQxyz = QQ[\'x,y,z\']
            sage: A = sage.structure.coerce_actions.ActOnAction(S3, QQxyz, False)
            sage: A.codomain()
            Multivariate Polynomial Ring in x, y, z over Rational Field'''

class IntegerAction(sage.categories.action.Action):
    '''IntegerAction(Z, S, is_left, op)

    File: /build/sagemath/src/sage/src/sage/structure/coerce_actions.pyx (starting at line 677)

    Abstract base class representing some action by integers on
    something. Here, "integer" is defined loosely in the "duck typing"
    sense.

    INPUT:

    - ``Z`` -- a type or parent representing integers

    For the other arguments, see :class:`Action`.

    .. NOTE::

        This class is used internally in Sage\'s coercion model. Outside
        of the coercion model, special precautions are needed to prevent
        domains of the action from being garbage collected.'''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, Z, S, is_left, op) -> Any:
        """File: /build/sagemath/src/sage/src/sage/structure/coerce_actions.pyx (starting at line 695)"""
    def __invert__(self) -> Any:
        """IntegerAction.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/structure/coerce_actions.pyx (starting at line 718)

        EXAMPLES::

            sage: from sage.structure.coerce_actions import IntegerMulAction
            sage: act = IntegerMulAction(ZZ, CDF)                                       # needs sage.rings.complex_double
            sage: ~act                                                                  # needs sage.rings.complex_double
            Traceback (most recent call last):
            ...
            TypeError: actions by ZZ cannot be inverted"""
    def __reduce__(self) -> Any:
        """IntegerAction.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/structure/coerce_actions.pyx (starting at line 701)

        Used in pickling.

        TESTS:

        Check that this action can be pickled (:issue:`29031`)::

            sage: from sage.structure.coerce_actions import IntegerMulAction
            sage: act = IntegerMulAction(ZZ, CDF)                                       # needs sage.rings.complex_double
            sage: loads(dumps(act)) is not None                                         # needs sage.rings.complex_double
            True"""

class IntegerMulAction(IntegerAction):
    """IntegerMulAction(Z, M, is_left=True, m=None)

    File: /build/sagemath/src/sage/src/sage/structure/coerce_actions.pyx (starting at line 732)

    Implement the action `n \\cdot a = a + a + ... + a` via repeated
    doubling.

    Both addition and negation must be defined on the set `M`.

    INPUT:

    - ``Z`` -- a type or parent representing integers

    - ``M`` -- a ``ZZ``-module

    - ``m`` -- (optional) an element of ``M``

    EXAMPLES::

        sage: from sage.structure.coerce_actions import IntegerMulAction
        sage: R.<x> = QQ['x']
        sage: act = IntegerMulAction(ZZ, R)
        sage: act(5, x)
        5*x
        sage: act(0, x)
        0
        sage: act(-3, x-1)
        -3*x + 3"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, Z, M, is_left=..., m=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/structure/coerce_actions.pyx (starting at line 759)"""

class IntegerPowAction(IntegerAction):
    """IntegerPowAction(Z, M, is_left=False, m=None)

    File: /build/sagemath/src/sage/src/sage/structure/coerce_actions.pyx (starting at line 841)

    The right action ``a ^ n = a * a * ... * a`` where `n` is an
    integer.

    The action is implemented using the ``_pow_int`` method on elements.

    INPUT:

    - ``Z`` -- a type or parent representing integers

    - ``M`` -- a parent whose elements implement ``_pow_int``

    - ``m`` -- (optional) an element of ``M``

    EXAMPLES::

        sage: from sage.structure.coerce_actions import IntegerPowAction
        sage: R.<x> = LaurentSeriesRing(QQ)
        sage: act = IntegerPowAction(ZZ, R)
        sage: act(x, 5)
        x^5
        sage: act(x, -2)
        x^-2
        sage: act(x, int(5))
        x^5

    TESTS::

        sage: IntegerPowAction(ZZ, R, True)
        Traceback (most recent call last):
        ...
        ValueError: powering must be a right action
        sage: IntegerPowAction(ZZ, QQ^3)                                                # needs sage.modules
        Traceback (most recent call last):
        ...
        TypeError: no integer powering action defined on Vector space of dimension 3 over Rational Field

    ::

        sage: var('x,y')                                                                # needs sage.symbolic
        (x, y)
        sage: RDF('-2.3')^(x+y^3+sin(x))                                                # needs sage.symbolic
        (-2.3)^(y^3 + x + sin(x))
        sage: RDF('-2.3')^x                                                             # needs sage.symbolic
        (-2.3)^x"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @overload
    def __init__(self, Z, M, is_left=..., m=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/structure/coerce_actions.pyx (starting at line 888)"""
    @overload
    def __init__(self, ZZ, R) -> Any:
        """File: /build/sagemath/src/sage/src/sage/structure/coerce_actions.pyx (starting at line 888)"""
    @overload
    def __init__(self, ZZ, R, _True) -> Any:
        """File: /build/sagemath/src/sage/src/sage/structure/coerce_actions.pyx (starting at line 888)"""

class LeftModuleAction(ModuleAction):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class ModuleAction(sage.categories.action.Action):
    """ModuleAction(G, S, g=None, a=None, check=True)

    File: /build/sagemath/src/sage/src/sage/structure/coerce_actions.pyx (starting at line 243)

    Module action.

    .. SEEALSO::

        This is an abstract class, one must actually instantiate a
        :class:`LeftModuleAction` or a :class:`RightModuleAction`.

    INPUT:

    - ``G`` -- the actor, an instance of :class:`~sage.structure.parent.Parent`
    - ``S`` -- the object that is acted upon
    - ``g`` -- (optional) an element of ``G``
    - ``a`` -- (optional) an element of ``S``
    - ``check`` -- if ``True`` (default), then there will be no consistency tests
      performed on sample elements

    NOTE:

    By default, the sample elements of ``S`` and ``G`` are obtained from
    :meth:`~sage.structure.parent.Parent.an_element`, which relies on the
    implementation of an ``_an_element_()`` method. This is not always
    available. But usually, the action is only needed when one already
    *has* two elements. Hence, by :issue:`14249`, the coercion model will
    pass these two elements to the :class:`ModuleAction` constructor.

    The actual action is implemented by the ``_rmul_`` or ``_lmul_``
    function on its elements. We must, however, be very particular about
    what we feed into these functions, because they operate under the
    assumption that the inputs lie exactly in the base ring and may
    segfault otherwise. Thus we handle all possible base extensions
    manually here."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, G, S, g=..., a=..., check=...) -> Any:
        '''File: /build/sagemath/src/sage/src/sage/structure/coerce_actions.pyx (starting at line 277)

                This creates an action of an element of a module by an element of its
                base ring. The simplest example to keep in mind is R acting on the
                polynomial ring R[x].

                EXAMPLES:

                Note that coerce actions should only be used inside of the coercion
                model. For this test, we need to strongly reference the domains,
                for otherwise they could be garbage collected, giving rise to
                random errors (see :issue:`18157`). ::


                    sage: from sage.structure.coerce_actions import LeftModuleAction
                    sage: ZZx = ZZ[\'x\']
                    sage: QQx = QQ[\'x\']
                    sage: QQy = QQ[\'y\']
                    sage: ZZxy = ZZ[\'x\'][\'y\']
                    sage: LeftModuleAction(ZZ, ZZx)
                    Left scalar multiplication by Integer Ring on Univariate Polynomial Ring in x over Integer Ring
                    sage: LeftModuleAction(ZZ, QQx)
                    Left scalar multiplication by Integer Ring on Univariate Polynomial Ring in x over Rational Field
                    sage: LeftModuleAction(QQ, ZZx)
                    Left scalar multiplication by Rational Field on Univariate Polynomial Ring in x over Integer Ring
                    sage: LeftModuleAction(QQ, ZZxy)
                    Left scalar multiplication by Rational Field
                     on Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Integer Ring

                The following tests against a problem that was relevant during work on
                :issue:`9944`::

                    sage: R.<x> = PolynomialRing(ZZ)
                    sage: S.<x> = PolynomialRing(ZZ, sparse=True)
                    sage: 1/R.0
                    1/x
                    sage: 1/S.0
                    1/x

                If there is a coercion from ``G`` to ``S``, we do not create
                the module action of ``G`` on the pushout of ``G`` and ``S``::

                    sage: G = PolynomialRing(QQ, "x")
                    sage: S = PolynomialRing(MatrixSpace(QQ, 2), "x")
                    sage: G.gen() * S.gen()
                    [1 0]
                    [0 1]*x^2

                Contrast the previous example with the following, where we
                have no coercion from ``G`` to ``S``::

                    sage: S = PolynomialRing(MatrixSpace(QQ, 2), "y")
                    sage: G.gen() * S.gen()
                    [x 0]
                    [0 x]*y
        '''
    @overload
    def codomain(self) -> Any:
        """ModuleAction.codomain(self)

        File: /build/sagemath/src/sage/src/sage/structure/coerce_actions.pyx (starting at line 433)

        The codomain of self, which may or may not be equal to the domain.

        EXAMPLES:

        Note that coerce actions should only be used inside of the coercion
        model. For this test, we need to strongly reference the domains,
        for otherwise they could be garbage collected, giving rise to
        random errors (see :issue:`18157`). ::

            sage: from sage.structure.coerce_actions import LeftModuleAction
            sage: ZZxyz = ZZ['x,y,z']
            sage: A = LeftModuleAction(QQ, ZZxyz)
            sage: A.codomain()
            Multivariate Polynomial Ring in x, y, z over Rational Field"""
    @overload
    def codomain(self) -> Any:
        """ModuleAction.codomain(self)

        File: /build/sagemath/src/sage/src/sage/structure/coerce_actions.pyx (starting at line 433)

        The codomain of self, which may or may not be equal to the domain.

        EXAMPLES:

        Note that coerce actions should only be used inside of the coercion
        model. For this test, we need to strongly reference the domains,
        for otherwise they could be garbage collected, giving rise to
        random errors (see :issue:`18157`). ::

            sage: from sage.structure.coerce_actions import LeftModuleAction
            sage: ZZxyz = ZZ['x,y,z']
            sage: A = LeftModuleAction(QQ, ZZxyz)
            sage: A.codomain()
            Multivariate Polynomial Ring in x, y, z over Rational Field"""
    @overload
    def domain(self) -> Any:
        """ModuleAction.domain(self)

        File: /build/sagemath/src/sage/src/sage/structure/coerce_actions.pyx (starting at line 454)

        The domain of self, which is the module that is being acted on.

        EXAMPLES:

        Note that coerce actions should only be used inside of the coercion
        model. For this test, we need to strongly reference the domains,
        for otherwise they could be garbage collected, giving rise to
        random errors (see :issue:`18157`). ::

            sage: from sage.structure.coerce_actions import LeftModuleAction
            sage: ZZxyz = ZZ['x,y,z']
            sage: A = LeftModuleAction(QQ, ZZxyz)
            sage: A.domain()
            Multivariate Polynomial Ring in x, y, z over Integer Ring"""
    @overload
    def domain(self) -> Any:
        """ModuleAction.domain(self)

        File: /build/sagemath/src/sage/src/sage/structure/coerce_actions.pyx (starting at line 454)

        The domain of self, which is the module that is being acted on.

        EXAMPLES:

        Note that coerce actions should only be used inside of the coercion
        model. For this test, we need to strongly reference the domains,
        for otherwise they could be garbage collected, giving rise to
        random errors (see :issue:`18157`). ::

            sage: from sage.structure.coerce_actions import LeftModuleAction
            sage: ZZxyz = ZZ['x,y,z']
            sage: A = LeftModuleAction(QQ, ZZxyz)
            sage: A.domain()
            Multivariate Polynomial Ring in x, y, z over Integer Ring"""
    def __invert__(self) -> Any:
        """ModuleAction.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/structure/coerce_actions.pyx (starting at line 473)

        EXAMPLES:

        Note that coerce actions should only be used inside of the coercion
        model. For this test, we need to strongly reference the domains, for
        otherwise they could be garbage collected, giving rise to random
        errors (see :issue:`18157`). ::

            sage: from sage.structure.coerce_actions import RightModuleAction

            sage: ZZx = ZZ['x']
            sage: x = ZZx.gen()
            sage: QQx = QQ['x']
            sage: A = ~RightModuleAction(QQ, QQx); A
            Right inverse action by Rational Field on Univariate Polynomial Ring in x over Rational Field
            sage: A(x, 2)
            1/2*x

            sage: A = ~RightModuleAction(QQ, ZZx); A
            Right inverse action by Rational Field on Univariate Polynomial Ring in x over Integer Ring
            sage: A.codomain()
            Univariate Polynomial Ring in x over Rational Field
            sage: A(x, 2)
            1/2*x

            sage: A = ~RightModuleAction(ZZ, ZZx); A
            Right inverse action by Rational Field on Univariate Polynomial Ring in x over Integer Ring
            with precomposition on right by Natural morphism:
              From: Integer Ring
              To:   Rational Field
            sage: A.codomain()
            Univariate Polynomial Ring in x over Rational Field
            sage: A(x, 2)
            1/2*x

            sage: GF5x = GF(5)['x']
            sage: A = ~RightModuleAction(ZZ, GF5x); A
            Right inverse action by Finite Field of size 5
            on Univariate Polynomial Ring in x over Finite Field of size 5
            with precomposition on right by Natural morphism:
              From: Integer Ring
              To:   Finite Field of size 5
            sage: A(x, 2)
            3*x

            sage: GF5xy = GF5x['y']
            sage: A = ~RightModuleAction(ZZ, GF5xy); A
            Right inverse action by Finite Field of size 5
            on Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Finite Field of size 5
            with precomposition on right by Natural morphism:
              From: Integer Ring
              To:   Finite Field of size 5

            sage: ZZy = ZZ['y']
            sage: ZZxyzw = ZZx['y']['z']['w']
            sage: A = ~RightModuleAction(ZZy, ZZxyzw); A
            Right inverse action by Fraction Field of Univariate Polynomial Ring in y
                over Univariate Polynomial Ring in x
                over Integer Ring
            on Univariate Polynomial Ring in w
                over Univariate Polynomial Ring in z
                over Univariate Polynomial Ring in y
                over Univariate Polynomial Ring in x
                over Integer Ring
            with precomposition on right by Conversion via FractionFieldElement map:
              From: Univariate Polynomial Ring in y over Integer Ring
              To:   Fraction Field of Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Integer Ring

        TESTS:

        See :issue:`19521`::

            sage: # needs sage.symbolic
            sage: Q.<y> = SR.subring(no_variables=True)[[]]
            sage: (y / 1).parent()
            Power Series Ring in y over Symbolic Constants Subring
            sage: R.<x> = SR.subring(no_variables=True)[]
            sage: cm = sage.structure.element.get_coercion_model()
            sage: cm.explain(x, 1, operator.truediv)
            Action discovered.
                Right inverse action by Symbolic Constants Subring
                 on Univariate Polynomial Ring in x over Symbolic Constants Subring
                with precomposition on right by Conversion via _symbolic_ method map:
                  From: Integer Ring
                  To:   Symbolic Constants Subring
            Result lives in Univariate Polynomial Ring in x over Symbolic Constants Subring
            Univariate Polynomial Ring in x over Symbolic Constants Subring"""
    def __reduce__(self) -> Any:
        """ModuleAction.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/structure/coerce_actions.pyx (starting at line 392)

        Used in pickling.

        TESTS:

        Check that this action can be pickled (:issue:`29031`)::

            sage: A = ZZ['x'].get_action(QQ, self_on_left=False, op=operator.mul)
            sage: loads(dumps(A)) is not None
            True"""

class PyScalarAction(sage.categories.action.Action):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class RightModuleAction(ModuleAction):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
