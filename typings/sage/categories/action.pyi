import sage.categories.functor
import sage.categories.homset as homset
import sage.categories.morphism
from _typeshed import Incomplete
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar

class Action(sage.categories.functor.Functor):
    """Action(G, S, is_left=True, op=None)

    File: /build/sagemath/src/sage/src/sage/categories/action.pyx (starting at line 78)

    The action of ``G`` on ``S``.

    INPUT:

    - ``G`` -- a parent or Python type

    - ``S`` -- a parent or Python type

    - ``is_left`` -- boolean (default: ``True``); whether elements of
      ``G`` are on the left

    - ``op`` -- (default: ``None``) operation. This is not used by
      :class:`Action` itself, but other classes may use it"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    G: File
    op: File
    def __init__(self, G, S, is_left=..., op=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/categories/action.pyx (starting at line 94)"""
    def act(self, g, x) -> Any:
        """Action.act(self, g, x)

        File: /build/sagemath/src/sage/src/sage/categories/action.pyx (starting at line 214)

        This is a consistent interface for acting on ``x`` by ``g``,
        regardless of whether it's a left or right action.

        If needed, ``g`` and ``x`` are converted to the correct parent.

        EXAMPLES::

            sage: R.<x> = ZZ []
            sage: from sage.structure.coerce_actions import IntegerMulAction
            sage: A = IntegerMulAction(ZZ, R, True)   # Left action
            sage: A.act(5, x)
            5*x
            sage: A.act(int(5), x)
            5*x
            sage: A = IntegerMulAction(ZZ, R, False)  # Right action
            sage: A.act(5, x)
            5*x
            sage: A.act(int(5), x)
            5*x"""
    def actor(self) -> Any:
        """Action.actor(self)

        File: /build/sagemath/src/sage/src/sage/categories/action.pyx (starting at line 252)"""
    def codomain(self) -> Any:
        """Action.codomain(self)

        File: /build/sagemath/src/sage/src/sage/categories/action.pyx (starting at line 309)"""
    def domain(self) -> Any:
        """Action.domain(self)

        File: /build/sagemath/src/sage/src/sage/categories/action.pyx (starting at line 312)"""
    def is_left(self) -> Any:
        """Action.is_left(self)

        File: /build/sagemath/src/sage/src/sage/categories/action.pyx (starting at line 241)"""
    def left_domain(self) -> Any:
        """Action.left_domain(self)

        File: /build/sagemath/src/sage/src/sage/categories/action.pyx (starting at line 315)"""
    def operation(self) -> Any:
        """Action.operation(self)

        File: /build/sagemath/src/sage/src/sage/categories/action.pyx (starting at line 327)"""
    def right_domain(self) -> Any:
        """Action.right_domain(self)

        File: /build/sagemath/src/sage/src/sage/categories/action.pyx (starting at line 321)"""
    def __call__(self, *args) -> Any:
        """Action.__call__(self, *args)

        File: /build/sagemath/src/sage/src/sage/categories/action.pyx (starting at line 126)

        Let this action act.

        For a left action, ``action(a, b)`` lets ``a`` act on ``b``.
        For a right action, ``action(a, b)`` lets ``b`` act on ``a``.

        If needed, ``a`` and ``b`` are converted to the correct parent.

        .. SEEALSO::

            :meth:`act` which lets you pass the acting and acted-on
            elements directly.

        EXAMPLES::

            sage: R.<x> = ZZ []
            sage: from sage.structure.coerce_actions import IntegerMulAction
            sage: A = IntegerMulAction(ZZ, R, True)   # Left action
            sage: A(5, x)
            5*x
            sage: A(int(5), x)
            5*x
            sage: A(x, 5)
            Traceback (most recent call last):
            ...
            TypeError: x is not a constant polynomial
            sage: A = IntegerMulAction(ZZ, R, False)  # Right action
            sage: A(x, 5)
            5*x
            sage: A(x, int(5))
            5*x
            sage: A(5, x)
            Traceback (most recent call last):
            ...
            TypeError: x is not a constant polynomial"""
    def __invert__(self) -> Any:
        """Action.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/categories/action.pyx (starting at line 238)"""
    def __reduce__(self) -> Any:
        """Action.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/categories/action.pyx (starting at line 105)

        Used in pickling.

        .. WARNING::

            If you change the signature of the ``__init__`` for a subclass,
            you must override this method as well.

        TESTS:

        Check that this action can be pickled (:issue:`29031`)::

            sage: P = QQ['x']
            sage: R = (ZZ['x'])['y']
            sage: A = R.get_action(P, operator.mul, True)
            sage: loads(dumps(A)) is not None
            True"""

class ActionEndomorphism(sage.categories.morphism.Morphism):
    """ActionEndomorphism(Action action, g)

    File: /build/sagemath/src/sage/src/sage/categories/action.pyx (starting at line 552)

    The endomorphism defined by the action of one element.

    EXAMPLES::

        sage: A = ZZ['x'].get_action(QQ, self_on_left=False, op=operator.mul)
        sage: A
        Left scalar multiplication by Rational Field
         on Univariate Polynomial Ring in x over Integer Ring
        sage: A(1/2)
        Action of 1/2 on Univariate Polynomial Ring in x over Integer Ring
        under Left scalar multiplication by Rational Field on Univariate
        Polynomial Ring in x over Integer Ring."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, Actionaction, g) -> Any:
        """File: /build/sagemath/src/sage/src/sage/categories/action.pyx (starting at line 567)"""
    def __invert__(self) -> Any:
        """ActionEndomorphism.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/categories/action.pyx (starting at line 636)"""
    def __mul__(self, left, right) -> Any:
        """ActionEndomorphism.__mul__(left, right)

        File: /build/sagemath/src/sage/src/sage/categories/action.pyx (starting at line 624)"""
    def __rmul__(self, other):
        """Return value*self."""

class InverseAction(Action):
    """InverseAction(Action action)

    File: /build/sagemath/src/sage/src/sage/categories/action.pyx (starting at line 331)

    An action that acts as the inverse of the given action.

    EXAMPLES::

        sage: V = QQ^3                                                                  # needs sage.modules
        sage: v = V((1, 2, 3))                                                          # needs sage.modules
        sage: cm = get_coercion_model()

        sage: # needs sage.modules
        sage: a = cm.get_action(V, QQ, operator.mul)
        sage: a
        Right scalar multiplication by Rational Field
         on Vector space of dimension 3 over Rational Field
        sage: ~a
        Right inverse action by Rational Field
         on Vector space of dimension 3 over Rational Field
        sage: (~a)(v, 1/3)
        (3, 6, 9)

        sage: # needs sage.modules
        sage: b = cm.get_action(QQ, V, operator.mul)
        sage: b
        Left scalar multiplication by Rational Field
         on Vector space of dimension 3 over Rational Field
        sage: ~b
        Left inverse action by Rational Field
         on Vector space of dimension 3 over Rational Field
        sage: (~b)(1/3, v)
        (3, 6, 9)

        sage: c = cm.get_action(ZZ, list, operator.mul)
        sage: c
        Left action by Integer Ring on <... 'list'>
        sage: ~c
        Traceback (most recent call last):
        ...
        TypeError: no inverse defined for Left action by Integer Ring on <... 'list'>

    TESTS:

        sage: x = polygen(QQ,'x')
        sage: a = 2*x^2+2; a
        2*x^2 + 2
        sage: a / 2
        x^2 + 1
        sage: a /= 2
        sage: a
        x^2 + 1"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, Actionaction) -> Any:
        """File: /build/sagemath/src/sage/src/sage/categories/action.pyx (starting at line 382)"""
    def codomain(self) -> Any:
        """InverseAction.codomain(self)

        File: /build/sagemath/src/sage/src/sage/categories/action.pyx (starting at line 419)"""
    def __invert__(self) -> Any:
        """InverseAction.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/categories/action.pyx (starting at line 422)"""
    def __reduce__(self) -> Any:
        """InverseAction.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/categories/action.pyx (starting at line 396)

        Used in pickling.

        TESTS:

        Check that this action can be pickled (:issue:`29031`)::

            sage: # needs sage.modules
            sage: V = QQ^3
            sage: v = V((1, 2, 3))
            sage: cm = get_coercion_model()
            sage: a = cm.get_action(V, QQ, operator.mul)
            sage: loads(dumps(~a)) is not None
            True"""

class PrecomposedAction(Action):
    """PrecomposedAction(Action action, Map left_precomposition, Map right_precomposition)

    File: /build/sagemath/src/sage/src/sage/categories/action.pyx (starting at line 429)

    A precomposed action first applies given maps, and then applying an action
    to the return values of the maps.

    EXAMPLES:

    We demonstrate that an example discussed on :issue:`14711` did not become a
    problem::

        sage: # needs sage.libs.flint sage.modular
        sage: E = ModularSymbols(11).2
        sage: s = E.modular_symbol_rep()
        sage: del E,s
        sage: import gc
        sage: _ = gc.collect()
        sage: E = ModularSymbols(11).2
        sage: v = E.manin_symbol_rep()
        sage: c,x = v[0]
        sage: y = x.modular_symbol_rep()
        sage: coercion_model.get_action(QQ, parent(y), op=operator.mul)
        Left scalar multiplication by Rational Field
         on Abelian Group of all Formal Finite Sums over Rational Field
         with precomposition on right by Coercion map:
          From: Abelian Group of all Formal Finite Sums over Integer Ring
          To:   Abelian Group of all Formal Finite Sums over Rational Field"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    left_precomposition: Incomplete
    right_precomposition: Incomplete
    def __init__(self, Actionaction, Mapleft_precomposition, Mapright_precomposition) -> Any:
        """File: /build/sagemath/src/sage/src/sage/categories/action.pyx (starting at line 456)"""
    def codomain(self) -> Any:
        """PrecomposedAction.codomain(self)

        File: /build/sagemath/src/sage/src/sage/categories/action.pyx (starting at line 515)"""
    def domain(self) -> Any:
        """PrecomposedAction.domain(self)

        File: /build/sagemath/src/sage/src/sage/categories/action.pyx (starting at line 509)"""
    def __invert__(self) -> Any:
        """PrecomposedAction.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/categories/action.pyx (starting at line 540)"""
    def __reduce__(self) -> Any:
        """PrecomposedAction.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/categories/action.pyx (starting at line 483)

        Used in pickling.

        TESTS:

        Check that this action can be pickled (:issue:`29031`)::

            sage: # needs sage.libs.flint sage.modular
            sage: E = ModularSymbols(11).2
            sage: v = E.manin_symbol_rep()
            sage: c,x = v[0]
            sage: y = x.modular_symbol_rep()
            sage: act = coercion_model.get_action(QQ, parent(y), op=operator.mul)
            sage: loads(dumps(act)) is not None
            True"""
