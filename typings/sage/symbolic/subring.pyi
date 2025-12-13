from .ring import SR as SR, SymbolicRing as SymbolicRing
from _typeshed import Incomplete
from sage.categories.pushout import ConstructionFunctor as ConstructionFunctor
from sage.structure.factory import UniqueFactory as UniqueFactory

class SymbolicSubringFactory(UniqueFactory):
    """
    A factory creating a symbolic subring.

    INPUT:

    Specify one of the following keywords to create a subring.

    - ``accepting_variables`` -- (default: ``None``) a tuple or other
      iterable of variables. If specified, then a symbolic subring of
      expressions in only these variables is created.

    - ``rejecting_variables`` -- (default: ``None``) a tuple or other
      iterable of variables. If specified, then a symbolic subring of
      expressions in variables distinct to these variables is
      created.

    - ``no_variables`` -- boolean (default: ``False``); if set,
      then a symbolic subring of constant expressions (i.e.,
      expressions without a variable) is created.

    EXAMPLES::

        sage: from sage.symbolic.subring import SymbolicSubring
        sage: V = var('a, b, c, r, s, t, x, y, z')

    ::

        sage: A = SymbolicSubring(accepting_variables=(a, b, c)); A
        Symbolic Subring accepting the variables a, b, c
        sage: tuple((v, v in A) for v in V)
        ((a, True), (b, True), (c, True),
         (r, False), (s, False), (t, False),
         (x, False), (y, False), (z, False))

    ::

        sage: R = SymbolicSubring(rejecting_variables=(r, s, t)); R
        Symbolic Subring rejecting the variables r, s, t
        sage: tuple((v, v in R) for v in V)
        ((a, True), (b, True), (c, True),
         (r, False), (s, False), (t, False),
         (x, True), (y, True), (z, True))

    ::

        sage: C = SymbolicSubring(no_variables=True); C
        Symbolic Constants Subring
        sage: tuple((v, v in C) for v in V)
        ((a, False), (b, False), (c, False),
         (r, False), (s, False), (t, False),
         (x, False), (y, False), (z, False))

    TESTS::

        sage: SymbolicSubring(accepting_variables=tuple()) is C
        True

    ::

        sage: SymbolicSubring(rejecting_variables=tuple()) is SR
        True
    """
    def create_key_and_extra_args(self, accepting_variables=None, rejecting_variables=None, no_variables: bool = False, **kwds):
        """
        Given the arguments and keyword, create a key that uniquely
        determines this object.

        See :class:`SymbolicSubringFactory` for details.

        TESTS::

            sage: from sage.symbolic.subring import SymbolicSubring
            sage: SymbolicSubring.create_key_and_extra_args()
            Traceback (most recent call last):
            ...
            ValueError: cannot create a symbolic subring since nothing is specified
            sage: SymbolicSubring.create_key_and_extra_args(
            ....:     accepting_variables=('a',), rejecting_variables=('r',))
            Traceback (most recent call last):
            ...
            ValueError: cannot create a symbolic subring since input is ambiguous
            sage: SymbolicSubring.create_key_and_extra_args(
            ....:     accepting_variables=('a',), no_variables=True)
            Traceback (most recent call last):
            ...
            ValueError: cannot create a symbolic subring since input is ambiguous
            sage: SymbolicSubring.create_key_and_extra_args(
            ....:     rejecting_variables=('r',), no_variables=True)
            Traceback (most recent call last):
            ...
            ValueError: cannot create a symbolic subring since input is ambiguous
        """
    def create_object(self, version, key, **kwds):
        """
        Create an object from the given arguments.

        See :class:`SymbolicSubringFactory` for details.

        TESTS::

            sage: from sage.symbolic.subring import SymbolicSubring
            sage: SymbolicSubring(rejecting_variables=tuple()) is SR  # indirect doctest
            True
        """

SymbolicSubring: Incomplete

class GenericSymbolicSubring(SymbolicRing):
    def __init__(self, vars) -> None:
        """
        An abstract base class for a symbolic subring.

        INPUT:

        - ``vars`` -- tuple of symbolic variables

        TESTS::

            sage: from sage.symbolic.subring import SymbolicSubring
            sage: SymbolicSubring(accepting_variables=('a',))  # indirect doctest
            Symbolic Subring accepting the variable a
            sage: SymbolicSubring(rejecting_variables=('r',))  # indirect doctest
            Symbolic Subring rejecting the variable r
            sage: SymbolicSubring(no_variables=True)  # indirect doctest
            Symbolic Constants Subring
            sage: SymbolicSubring(rejecting_variables=tuple())  # indirect doctest
            Symbolic Ring

        ::

            sage: SR.subring(accepting_variables=(0, pi, sqrt(2), 'zzz', I))
            Traceback (most recent call last):
            ...
            ValueError: Invalid variables: 0, I, pi, sqrt(2)
        """
    def has_valid_variable(self, variable) -> None:
        """
        Return whether the given ``variable`` is valid in this subring.

        INPUT:

        - ``variable`` -- a symbolic variable

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.symbolic.subring import GenericSymbolicSubring
            sage: GenericSymbolicSubring(vars=tuple()).has_valid_variable(x)
            Traceback (most recent call last):
            ...
            NotImplementedError: Not implemented in this abstract base class
        """
    def __eq__(self, other):
        """
        Compare two symbolic subrings.

        EXAMPLES::

            sage: from sage.symbolic.subring import SymbolicSubring
            sage: A = SymbolicSubring(accepting_variables=('a',))
            sage: B = SymbolicSubring(accepting_variables=('b',))
            sage: AB = SymbolicSubring(accepting_variables=('a', 'b'))
            sage: A == A
            True
            sage: A == B
            False
            sage: A == AB
            False
        """
    def __ne__(self, other):
        """
        Check whether ``self`` and ``other`` are not equal.

        EXAMPLES::

            sage: from sage.symbolic.subring import SymbolicSubring
            sage: A = SymbolicSubring(accepting_variables=('a',))
            sage: B = SymbolicSubring(accepting_variables=('b',))
            sage: AB = SymbolicSubring(accepting_variables=('a', 'b'))
            sage: A != A
            False
            sage: A != B
            True
            sage: A != AB
            True
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: from sage.symbolic.subring import SymbolicSubring
            sage: A = SymbolicSubring(accepting_variables=('a',))
            sage: B = SymbolicSubring(accepting_variables=('b',))
            sage: hash(A) == hash(A)
            True
            sage: hash(A) == hash(B)
            False
        """

class GenericSymbolicSubringFunctor(ConstructionFunctor):
    """
    A base class for the functors constructing symbolic subrings.

    INPUT:

    - ``vars`` -- tuple, set, or other iterable of symbolic variables

    EXAMPLES::

        sage: from sage.symbolic.subring import SymbolicSubring
        sage: SymbolicSubring(no_variables=True).construction()[0]  # indirect doctest
        Subring<accepting no variable>

    .. SEEALSO::

        :class:`sage.categories.pushout.ConstructionFunctor`.
    """
    rank: int
    coercion_reversed: bool
    vars: Incomplete
    def __init__(self, vars) -> None:
        """
        See :class:`GenericSymbolicSubringFunctor` for details.

        TESTS::

            sage: from sage.symbolic.subring import SymbolicSubring
            sage: SymbolicSubring(accepting_variables=('a',)).construction()[0]  # indirect doctest
            Subring<accepting a>
        """
    def merge(self, other):
        """
        Merge this functor with ``other`` if possible.

        INPUT:

        - ``other`` -- a functor

        OUTPUT: a functor or ``None``

        EXAMPLES::

            sage: from sage.symbolic.subring import SymbolicSubring
            sage: F = SymbolicSubring(accepting_variables=('a',)).construction()[0]
            sage: F.merge(F) is F
            True
        """
    def __eq__(self, other):
        """
        Return whether this functor is equal to ``other``.

        INPUT:

        - ``other`` -- a functor

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.symbolic.subring import SymbolicSubring
            sage: F = SymbolicSubring(accepting_variables=('a',)).construction()[0]
            sage: F == F
            True
        """
    def __ne__(self, other):
        """
        Return whether this functor is not equal to ``other``.

        INPUT:

        - ``other`` -- a functor

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.symbolic.subring import SymbolicSubring
            sage: F = SymbolicSubring(accepting_variables=('a',)).construction()[0]
            sage: F != F
            False
        """

class SymbolicSubringAcceptingVars(GenericSymbolicSubring):
    """
    The symbolic subring consisting of symbolic expressions in the given variables.
    """
    def has_valid_variable(self, variable):
        """
        Return whether the given ``variable`` is valid in this subring.

        INPUT:

        - ``variable`` -- a symbolic variable

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.symbolic.subring import SymbolicSubring
            sage: S = SymbolicSubring(accepting_variables=('a',))
            sage: S.has_valid_variable('a')
            True
            sage: S.has_valid_variable('r')
            False
            sage: S.has_valid_variable('x')
            False
        """
    def construction(self):
        """
        Return the functorial construction of this symbolic subring.

        OUTPUT:

        A tuple whose first entry is a construction functor and its second
        is the symbolic ring.

        EXAMPLES::

            sage: from sage.symbolic.subring import SymbolicSubring
            sage: SymbolicSubring(accepting_variables=('a',)).construction()
            (Subring<accepting a>, Symbolic Ring)
        """

class SymbolicSubringAcceptingVarsFunctor(GenericSymbolicSubringFunctor):
    def merge(self, other):
        """
        Merge this functor with ``other`` if possible.

        INPUT:

        - ``other`` -- a functor

        OUTPUT: a functor or ``None``

        EXAMPLES::

            sage: from sage.symbolic.subring import SymbolicSubring
            sage: F = SymbolicSubring(accepting_variables=('a',)).construction()[0]
            sage: G = SymbolicSubring(rejecting_variables=('r',)).construction()[0]
            sage: F.merge(F) is F
            True
            sage: F.merge(G) is G
            True
        """

class SymbolicSubringRejectingVars(GenericSymbolicSubring):
    """
    The symbolic subring consisting of symbolic expressions whose variables
    are none of the given variables.
    """
    def has_valid_variable(self, variable):
        """
        Return whether the given ``variable`` is valid in this subring.

        INPUT:

        - ``variable`` -- a symbolic variable

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.symbolic.subring import SymbolicSubring
            sage: S = SymbolicSubring(rejecting_variables=('r',))
            sage: S.has_valid_variable('a')
            True
            sage: S.has_valid_variable('r')
            False
            sage: S.has_valid_variable('x')
            True
        """
    def construction(self):
        """
        Return the functorial construction of this symbolic subring.

        OUTPUT:

        A tuple whose first entry is a construction functor and its second
        is the symbolic ring.

        EXAMPLES::

            sage: from sage.symbolic.subring import SymbolicSubring
            sage: SymbolicSubring(rejecting_variables=('r',)).construction()
            (Subring<rejecting r>, Symbolic Ring)
        """

class SymbolicSubringRejectingVarsFunctor(GenericSymbolicSubringFunctor):
    def merge(self, other):
        """
        Merge this functor with ``other`` if possible.

        INPUT:

        - ``other`` -- a functor

        OUTPUT: a functor or ``None``

        EXAMPLES::

            sage: from sage.symbolic.subring import SymbolicSubring
            sage: F = SymbolicSubring(accepting_variables=('a',)).construction()[0]
            sage: G = SymbolicSubring(rejecting_variables=('r',)).construction()[0]
            sage: G.merge(G) is G
            True
            sage: G.merge(F) is G
            True
        """

class SymbolicConstantsSubring(SymbolicSubringAcceptingVars):
    """
    The symbolic subring consisting of symbolic constants.
    """
    def has_valid_variable(self, variable):
        """
        Return whether the given ``variable`` is valid in this subring.

        INPUT:

        - ``variable`` -- a symbolic variable

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.symbolic.subring import SymbolicSubring
            sage: S = SymbolicSubring(no_variables=True)
            sage: S.has_valid_variable('a')
            False
            sage: S.has_valid_variable('r')
            False
            sage: S.has_valid_variable('x')
            False
        """
