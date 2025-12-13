from _typeshed import Incomplete
from collections.abc import Generator, Iterator
from sage.graphs.digraph import DiGraph as DiGraph
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_function as cached_function
from sage.misc.latex import latex as latex
from sage.misc.sageinspect import sage_getargspec as sage_getargspec
from sage.misc.verbose import verbose as verbose
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.real_mpfr import RR as RR
from sage.structure.sage_object import SageObject as SageObject
from typing import NamedTuple

def full_group_by(l, key=None):
    '''
    Group iterable ``l`` by values of ``key``.

    INPUT:

    - iterable ``l``
    - key function ``key``

    OUTPUT:

    A list of pairs ``(k, elements)`` such that ``key(e)=k`` for all
    ``e`` in ``elements``.

    This is similar to :func:`itertools.groupby` except that lists are
    returned instead of iterables and no prior sorting is required.

    We do not require

    - that the keys are sortable (in contrast to the
      approach via :func:`sorted` and :func:`itertools.groupby`) and
    - that the keys are hashable (in contrast to the
      implementation proposed in `<https://stackoverflow.com/a/15250161>`_).

    However, it is required

    - that distinct keys have distinct ``str``-representations.

    The implementation is inspired by
    `<https://stackoverflow.com/a/15250161>`_, but non-hashable keys are
    allowed.

    EXAMPLES::

        sage: # needs sage.symbolic
        sage: from sage.combinat.finite_state_machine import full_group_by
        sage: t = [2/x, 1/x, 2/x]
        sage: r = full_group_by([0, 1, 2], key=lambda i: t[i])
        sage: sorted(r, key=lambda p: p[1])
        [(2/x, [0, 2]), (1/x, [1])]
        sage: from itertools import groupby
        sage: for k, elements in groupby(sorted([0, 1, 2],
        ....:                            key=lambda i:t[i]),
        ....:                            key=lambda i:t[i]):
        ....:     print("{} {}".format(k, list(elements)))
        2/x [0]
        1/x [1]
        2/x [2]

    Note that the behavior is different from :func:`itertools.groupby`
    because neither `1/x<2/x` nor `2/x<1/x` does hold.

    Here, the result ``r`` has been sorted in order to guarantee a
    consistent order for the doctest suite.
    '''
def equal(iterator):
    """
    Check whether all elements of ``iterator`` are equal.

    INPUT:

    - ``iterator`` -- an iterator of the elements to check

    OUTPUT: boolean

    This implements `<https://stackoverflow.com/a/3844832/1052778>`_.

    EXAMPLES::

        sage: from sage.combinat.finite_state_machine import equal
        sage: equal([0, 0, 0])
        True
        sage: equal([0, 1, 0])
        False
        sage: equal([])
        True
        sage: equal(iter([None, None]))
        True

    We can test other properties of the elements than the elements
    themselves. In the following example, we check whether all tuples
    have the same lengths::

        sage: equal(len(x) for x in [(1, 2), (2, 3), (3, 1)])
        True
        sage: equal(len(x) for x in [(1, 2), (1, 2, 3), (3, 1)])
        False
    """
def startswith(list_, prefix):
    """
    Determine whether list starts with the given prefix.

    INPUT:

    - ``list_`` -- list
    - ``prefix`` -- list representing the prefix

    OUTPUT: boolean

    Similar to :meth:`str.startswith`.

    EXAMPLES::

        sage: from sage.combinat.finite_state_machine import startswith
        sage: startswith([1, 2, 3], [1, 2])
        True
        sage: startswith([1], [1, 2])
        False
        sage: startswith([1, 3, 2], [1, 2])
        False
    """

FSMEmptyWordSymbol: str
EmptyWordLaTeX: str
EndOfWordLaTeX: str
tikz_automata_where: Incomplete

def FSMLetterSymbol(letter):
    """
    Return a string associated to the input letter.

    INPUT:

    - ``letter`` -- the input letter or ``None`` (representing the
      empty word)

    OUTPUT:

    If ``letter`` is ``None`` the symbol for the empty word
    ``FSMEmptyWordSymbol`` is returned, otherwise the string
    associated to the letter.

    EXAMPLES::

        sage: from sage.combinat.finite_state_machine import FSMLetterSymbol
        sage: FSMLetterSymbol(0)
        '0'
        sage: FSMLetterSymbol(None)
        '-'
    """
def FSMWordSymbol(word):
    """
    Return a string of ``word``. It may returns the symbol of the
    empty word ``FSMEmptyWordSymbol``.

    INPUT:

    - ``word`` -- the input word

    OUTPUT: string of ``word``

    EXAMPLES::

        sage: from sage.combinat.finite_state_machine import FSMWordSymbol
        sage: FSMWordSymbol([0, 1, 1])
        '0,1,1'
    """
def is_FSMState(S):
    """
    Test whether or not ``S`` inherits from :class:`FSMState`.

    TESTS::

        sage: from sage.combinat.finite_state_machine import is_FSMState, FSMState
        sage: is_FSMState(FSMState('A'))
        doctest:warning...
        DeprecationWarning: The function is_FSMState is deprecated; use 'isinstance(..., FSMState)' instead.
        See https://github.com/sagemath/sage/issues/38032 for details.
        True
    """

class FSMState(SageObject):
    '''
    Class for a state of a finite state machine.

    INPUT:

    - ``label`` -- the label of the state

    - ``word_out`` -- (default: ``None``) a word that is written when
      the state is reached

    - ``is_initial`` -- (default: ``False``)

    - ``is_final`` -- (default: ``False``)

    - ``final_word_out`` -- (default: ``None``) a word that is written when
      the state is reached as the last state of some input; only for final
      states.

    - ``initial_probability`` -- (default: ``None``) the probability of
      starting in this state if it is a state of a Markov chain

    - ``hook`` -- (default: ``None``) a function which is called when
      the state is reached during processing input. It takes two input
      parameters: the first is the current state (to allow using the same
      hook for several states), the second is the current process
      iterator object (to have full access to everything; e.g. the
      next letter from the input tape can be read in). It can output
      the next transition, i.e. the transition to take next. If it
      returns ``None`` the process iterator chooses. Moreover, this
      function can raise a ``StopIteration`` exception to stop
      processing of a finite state machine the input immediately. See
      also the example below.

    - ``color`` -- (default: ``None``) in order to distinguish states,
      they can be given an arbitrary "color" (an arbitrary object).
      This is used in :meth:`FiniteStateMachine.equivalence_classes`:
      states of different colors are never considered to be
      equivalent. Note that :meth:`Automaton.determinisation` requires
      that ``color`` is hashable.

    - ``allow_label_None`` -- boolean (default: ``False``); if ``True`` allows
      also ``None`` as label. Note that a state with label ``None`` is used in
      :class:`FSMProcessIterator`.

    OUTPUT: a state of a finite state machine

    EXAMPLES::

        sage: from sage.combinat.finite_state_machine import FSMState
        sage: A = FSMState(\'state 1\', word_out=0, is_initial=True)
        sage: A
        \'state 1\'
        sage: A.label()
        \'state 1\'
        sage: B = FSMState(\'state 2\')
        sage: A == B
        False

    We can also define a final output word of a final state which is
    used if the input of a transducer leads to this state. Such final
    output words are used in subsequential transducers. ::

        sage: C = FSMState(\'state 3\', is_final=True, final_word_out=\'end\')
        sage: C.final_word_out
        [\'end\']

    The final output word can be a single letter, ``None`` or a list of
    letters::

        sage: A = FSMState(\'A\')
        sage: A.is_final = True
        sage: A.final_word_out = 2
        sage: A.final_word_out
        [2]
        sage: A.final_word_out = [2, 3]
        sage: A.final_word_out
        [2, 3]

    Only final states can have a final output word which is not
    ``None``::

        sage: B = FSMState(\'B\')
        sage: B.final_word_out is None
        True
        sage: B.final_word_out = 2
        Traceback (most recent call last):
        ...
        ValueError: Only final states can have a final output word,
        but state B is not final.

    Setting the ``final_word_out`` of a final state to ``None`` is the
    same as setting it to ``[]`` and is also the default for a final
    state::

        sage: C = FSMState(\'C\', is_final=True)
        sage: C.final_word_out
        []
        sage: C.final_word_out = None
        sage: C.final_word_out
        []
        sage: C.final_word_out = []
        sage: C.final_word_out
        []

    It is not allowed to use ``None`` as a label::

        sage: from sage.combinat.finite_state_machine import FSMState
        sage: FSMState(None)
        Traceback (most recent call last):
        ...
        ValueError: Label None reserved for a special state,
        choose another label.

    This can be overridden by::

        sage: FSMState(None, allow_label_None=True)
        None

    Note that :meth:`Automaton.determinisation` requires that ``color``
    is hashable::

        sage: A = Automaton([[0, 0, 0]], initial_states=[0])
        sage: A.state(0).color = []
        sage: A.determinisation()
        Traceback (most recent call last):
        ...
        TypeError: unhashable type: \'list\'
        sage: A.state(0).color = ()
        sage: A.determinisation()
        Automaton with 1 state

    We can use a hook function of a state to stop processing. This is
    done by raising a ``StopIteration`` exception. The following code
    demonstrates this::

        sage: T = Transducer([(0, 1, 9, \'a\'), (1, 2, 9, \'b\'),
        ....:                 (2, 3, 9, \'c\'), (3, 4, 9, \'d\')],
        ....:                initial_states=[0],
        ....:                final_states=[4],
        ....:                input_alphabet=[9])
        sage: def stop(process, state, output):
        ....:     raise StopIteration()
        sage: T.state(3).hook = stop
        sage: T.process([9, 9, 9, 9])
        (False, 3, [\'a\', \'b\', \'c\'])

    TESTS:

    Test for ``is_initial``::

        sage: T = Automaton([(0,0,0)])
        sage: T.initial_states()
        []
        sage: T.state(0).is_initial = True
        sage: T.initial_states()
        [0]

    Test for ``initial_probability``::

        sage: from sage.combinat.finite_state_machine import FSMState
        sage: S = FSMState(\'state\', initial_probability=1/3)
        sage: S.initial_probability
        1/3
    '''
    is_initial: bool
    initial_probability: Incomplete
    word_out: Incomplete
    hook: Incomplete
    color: Incomplete
    def __init__(self, label, word_out=None, is_initial: bool = False, is_final: bool = False, final_word_out=None, initial_probability=None, hook=None, color=None, allow_label_None: bool = False) -> None:
        """
        See :class:`FSMState` for more information.

        EXAMPLES::

            sage: from sage.combinat.finite_state_machine import FSMState
            sage: FSMState('final', is_final=True)
            'final'

        TESTS::

            sage: A = FSMState('A', is_final=True)
            sage: A.final_word_out
            []
            sage: A.is_final = True
            sage: A = FSMState('A', is_final=True, final_word_out='end')
            sage: A.final_word_out
            ['end']
            sage: A = FSMState('A', is_final=True,
            ....:              final_word_out=['e', 'n', 'd'])
            sage: A.final_word_out
            ['e', 'n', 'd']
            sage: A = FSMState('A', is_final=True, final_word_out=[])
            sage: A.final_word_out
            []
            sage: A = FSMState('A', is_final=True, final_word_out=None)
            sage: A.final_word_out
            []
            sage: A = FSMState('A', is_final=False)
            sage: A.final_word_out is None
            True
            sage: A.is_final = False
            sage: A = FSMState('A', is_final=False, final_word_out='end')
            Traceback (most recent call last):
            ...
            ValueError: Only final states can have a final output word,
            but state A is not final.
            sage: A = FSMState('A', is_final=False,
            ....:              final_word_out=['e', 'n', 'd'])
            Traceback (most recent call last):
            ...
            ValueError: Only final states can have a final output word,
            but state A is not final.
            sage: A = FSMState('A', is_final=False, final_word_out=None)
            sage: A.final_word_out is None
            True
            sage: A = FSMState('A', is_final=False, final_word_out=[])
            Traceback (most recent call last):
            ...
            ValueError: Only final states can have a final output word,
            but state A is not final.
        """
    def __lt__(self, other):
        """
        Return ``True`` if label of ``self`` is less than label of ``other``.

        INPUT:

        - ``other`` -- a state

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.combinat.finite_state_machine import FSMState
            sage: FSMState(0) < FSMState(1)
            True
        """
    @property
    def final_word_out(self):
        """
        The final output word of a final state which is written if the
        state is reached as the last state of the input of the finite
        state machine. For a non-final state, the value is ``None``.

        ``final_word_out`` can be a single letter, a list or ``None``,
        but for a final-state, it is always saved as a list.

        EXAMPLES::

            sage: from sage.combinat.finite_state_machine import FSMState
            sage: A = FSMState('A', is_final=True, final_word_out=2)
            sage: A.final_word_out
            [2]
            sage: A.final_word_out = 3
            sage: A.final_word_out
            [3]
            sage: A.final_word_out = [3, 4]
            sage: A.final_word_out
            [3, 4]
            sage: A.final_word_out = None
            sage: A.final_word_out
            []
            sage: B = FSMState('B')
            sage: B.final_word_out is None
            True

        A non-final state cannot have a final output word::

            sage: B.final_word_out = [3, 4]
            Traceback (most recent call last):
            ...
            ValueError: Only final states can have a final
            output word, but state B is not final.
        """
    @final_word_out.setter
    def final_word_out(self, final_word_out) -> None:
        """
        Set the value of the final output word of a final state.

        INPUT:

        - ``final_word_out`` -- list; any element or ``None``

        OUTPUT: nothing

        TESTS::

            sage: from sage.combinat.finite_state_machine import FSMState
            sage: B = FSMState('B')
            sage: B.final_word_out = []
            Traceback (most recent call last):
            ...
            ValueError: Only final states can have a final
            output word, but state B is not final.
            sage: B.final_word_out = None
            sage: B.final_word_out is None
            True

        The exception is raised also when the initial state is a tuple
        (see :issue:`18990`)::

            sage: A = Transducer(initial_states=[(0, 0)])
            sage: A.state((0, 0)).final_word_out = []
            Traceback (most recent call last):
            ...
            ValueError: Only final states can have a final output word,
            but state (0, 0) is not final.

        No exception is raised if we set the state to be a final one::

            sage: A.state((0, 0)).is_final=True
            sage: A.state((0, 0)).final_word_out = []
            sage: A.state((0, 0)).final_word_out == []
            True
        """
    @property
    def is_final(self):
        """
        Describe whether the state is final or not.

        ``True`` if the state is final and ``False`` otherwise.

        EXAMPLES::

            sage: from sage.combinat.finite_state_machine import FSMState
            sage: A = FSMState('A', is_final=True, final_word_out=3)
            sage: A.is_final
            True
            sage: A.is_final = False
            Traceback (most recent call last):
            ...
            ValueError: State A cannot be non-final, because it has a
            final output word. Only final states can have a final output
            word.
            sage: A.final_word_out = None
            sage: A.is_final = False
            sage: A.is_final
            False
        """
    @is_final.setter
    def is_final(self, is_final) -> None:
        """
        Define the state as a final state or a non-final state.

        INPUT:

        - ``is_final`` -- ``True`` if the state should be final and
          ``False`` otherwise

        OUTPUT: nothing

        TESTS::

            sage: from sage.combinat.finite_state_machine import FSMState
            sage: A = FSMState('A', is_final=True)
            sage: A.final_word_out
            []
            sage: A.is_final = False
            sage: A.final_word_out is None
            True
            sage: A = FSMState('A', is_final=True, final_word_out='a')
            sage: A.is_final = False
            Traceback (most recent call last):
            ...
            ValueError: State A cannot be non-final, because it has a
            final output word. Only final states can have a final output
            word.

        The exception is raised also when the final state is a tuple
        (see :issue:`18990`)::

            sage: A = Transducer(final_states=[(0, 0)])
            sage: A.state((0, 0)).final_word_out = [1]
            sage: A.state((0, 0)).is_final = False
            Traceback (most recent call last):
            ...
            ValueError: State (0, 0) cannot be non-final, because it has
            a final output word. Only final states can have a final
            output word.

        No exception is raised if we empty the final_word_out of the
        state::

            sage: A.state((0, 0)).final_word_out = []
            sage: A.state((0, 0)).is_final = False
            sage: A.state((0, 0)).is_final
            False

            sage: A = FSMState('A', is_final=True, final_word_out=[])
            sage: A.is_final = False
            sage: A.final_word_out is None
            True
        """
    def label(self):
        """
        Return the label of the state.

        EXAMPLES::

            sage: from sage.combinat.finite_state_machine import FSMState
            sage: A = FSMState('state')
            sage: A.label()
            'state'
        """
    def __copy__(self):
        """
        Return a (shallow) copy of the state.

        OUTPUT: a new state

        EXAMPLES::

            sage: from sage.combinat.finite_state_machine import FSMState
            sage: A = FSMState('A')
            sage: A.is_initial = True
            sage: A.is_final = True
            sage: A.final_word_out = [1]
            sage: A.color = 'green'
            sage: A.initial_probability = 1/2
            sage: B = copy(A)
            sage: B.fully_equal(A)
            True
            sage: A.label() is B.label()
            True
            sage: A.is_initial is B.is_initial
            True
            sage: A.is_final is B.is_final
            True
            sage: A.final_word_out is B.final_word_out
            True
            sage: A.color is B.color
            True
            sage: A.initial_probability is B.initial_probability
            True
        """
    copy = __copy__
    def __deepcopy__(self, memo):
        """
        Return a deep copy of the state.

        INPUT:

        - ``memo`` -- dictionary storing already processed elements

        OUTPUT: a new state

        EXAMPLES::

            sage: from sage.combinat.finite_state_machine import FSMState
            sage: A = FSMState('A')
            sage: deepcopy(A)
            'A'
        """
    def deepcopy(self, memo=None):
        """
        Return a deep copy of the state.

        INPUT:

        - ``memo`` -- (default: ``None``) a dictionary storing already
          processed elements

        OUTPUT: a new state

        EXAMPLES::

            sage: from sage.combinat.finite_state_machine import FSMState
            sage: A = FSMState((1, 3), color=[1, 2],
            ....:              is_final=True, final_word_out=3,
            ....:              initial_probability=1/3)
            sage: B = deepcopy(A)
            sage: B
            (1, 3)
            sage: B.label() == A.label()
            True
            sage: B.label is A.label
            False
            sage: B.color == A.color
            True
            sage: B.color is A.color
            False
            sage: B.is_final == A.is_final
            True
            sage: B.is_final is A.is_final
            True
            sage: B.final_word_out == A.final_word_out
            True
            sage: B.final_word_out is A.final_word_out
            False
            sage: B.initial_probability == A.initial_probability
            True
        """
    def relabeled(self, label, memo=None):
        """
        Return a deep copy of the state with a new label.

        INPUT:

        - ``label`` -- the label of new state

        - ``memo`` -- (default: ``None``) a dictionary storing already
          processed elements

        OUTPUT: a new state

        EXAMPLES::

            sage: from sage.combinat.finite_state_machine import FSMState
            sage: A = FSMState('A')
            sage: A.relabeled('B')
            'B'
        """
    def __hash__(self):
        """
        Return a hash value for the object.

        OUTPUT: the hash of this state

        TESTS::

            sage: from sage.combinat.finite_state_machine import FSMState
            sage: A = FSMState('A')
            sage: hash(A) #random
            -269909568
        """
    def __eq__(self, other):
        """
        Return ``True`` if two states are the same, i.e., if they have
        the same labels.

        INPUT:

        - ``self`` -- a state

        - ``other`` -- a state

        OUTPUT: boolean

        Note that the hooks and whether the states are initial or
        final are not checked. To fully compare two states (including
        these attributes), use :meth:`.fully_equal`.

        As only the labels are used when hashing a state, only the
        labels can actually be compared by the equality relation.
        Note that the labels are unique within one finite state machine,
        so this may only lead to ambiguities when comparing states
        belonging to different finite state machines.

        EXAMPLES::

            sage: from sage.combinat.finite_state_machine import FSMState
            sage: A = FSMState('A')
            sage: B = FSMState('A', is_initial=True)
            sage: A == B
            True
        """
    def __ne__(self, other):
        """
        Test for inequality, complement of __eq__.

        INPUT:

        - ``self`` -- a state

        - ``other`` -- a state

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.combinat.finite_state_machine import FSMState
            sage: A = FSMState('A', is_initial=True)
            sage: B = FSMState('A', is_final=True)
            sage: A != B
            False
        """
    def fully_equal(self, other, compare_color: bool = True):
        """
        Check whether two states are fully equal, i.e., including all
        attributes except ``hook``.

        INPUT:

        - ``self`` -- a state

        - ``other`` -- a state

        - ``compare_color`` -- boolean (default: ``True``); if ``True`` colors
          are compared as well, otherwise not

        OUTPUT: boolean

        Note that usual comparison by ``==`` does only compare the labels.

        EXAMPLES::

            sage: from sage.combinat.finite_state_machine import FSMState
            sage: A = FSMState('A')
            sage: B = FSMState('A', is_initial=True)
            sage: A.fully_equal(B)
            False
            sage: A == B
            True
            sage: A.is_initial = True; A.color = 'green'
            sage: A.fully_equal(B)
            False
            sage: A.fully_equal(B, compare_color=False)
            True
        """
    def __bool__(self) -> bool:
        """
        Return ``True``.

        TESTS::

            sage: from sage.combinat.finite_state_machine import FSMState
            sage: bool(FSMState('A'))
            True
        """

def is_FSMTransition(T):
    """
    Test whether or not ``T`` inherits from :class:`FSMTransition`.

    TESTS::

        sage: from sage.combinat.finite_state_machine import is_FSMTransition, FSMTransition
        sage: is_FSMTransition(FSMTransition('A', 'B'))
        doctest:warning...
        DeprecationWarning: The function is_FSMTransition is deprecated; use 'isinstance(..., FSMTransition)' instead.
        See https://github.com/sagemath/sage/issues/38032 for details.
        True
    """

class FSMTransition(SageObject):
    """
    Class for a transition of a finite state machine.

    INPUT:

    - ``from_state`` -- state from which transition starts

    - ``to_state`` -- state in which transition ends

    - ``word_in`` -- the input word of the transitions (when the
      finite state machine is used as automaton)

    - ``word_out`` -- the output word of the transitions (when the
      finite state machine is used as transducer)

    OUTPUT: a transition of a finite state machine

    EXAMPLES::

        sage: from sage.combinat.finite_state_machine import FSMState, FSMTransition
        sage: A = FSMState('A')
        sage: B = FSMState('B')
        sage: S = FSMTransition(A, B, 0, 1)
        sage: T = FSMTransition('A', 'B', 0, 1)
        sage: T == S
        True
        sage: U = FSMTransition('A', 'B', 0)
        sage: U == T
        False
    """
    from_state: Incomplete
    to_state: Incomplete
    word_in: Incomplete
    word_out: Incomplete
    hook: Incomplete
    def __init__(self, from_state, to_state, word_in=None, word_out=None, hook=None) -> None:
        """
        See :class:`FSMTransition` for more information.

        EXAMPLES::

            sage: from sage.combinat.finite_state_machine import FSMTransition
            sage: FSMTransition('A', 'B', 0, 1)
            Transition from 'A' to 'B': 0|1
        """
    def __lt__(self, other):
        """
        Return ``True`` if ``self`` is less than ``other`` with respect to the
        key ``(self.from_state, self.word_in, self.to_state, self.word_out)``.

        INPUT:

        - ``other`` -- a transition

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.combinat.finite_state_machine import FSMTransition
            sage: FSMTransition(0,1,0,0) < FSMTransition(1,0,0,0)
            True
        """
    def __copy__(self):
        """
        Return a (shallow) copy of the transition.

        OUTPUT: a new transition

        EXAMPLES::

            sage: from sage.combinat.finite_state_machine import FSMTransition
            sage: t = FSMTransition('A', 'B', 0)
            sage: copy(t)
            Transition from 'A' to 'B': 0|-
        """
    copy = __copy__
    def __deepcopy__(self, memo):
        """
        Return a deep copy of the transition.

        INPUT:

        - ``memo`` -- dictionary storing already processed elements

        OUTPUT: a new transition

        EXAMPLES::

            sage: from sage.combinat.finite_state_machine import FSMTransition
            sage: t = FSMTransition('A', 'B', 0)
            sage: deepcopy(t)
            Transition from 'A' to 'B': 0|-
        """
    def deepcopy(self, memo=None):
        """
        Return a deep copy of the transition.

        INPUT:

        - ``memo`` -- (default: ``None``) a dictionary storing already
          processed elements

        OUTPUT: a new transition

        EXAMPLES::

            sage: from sage.combinat.finite_state_machine import FSMTransition
            sage: t = FSMTransition('A', 'B', 0)
            sage: deepcopy(t)
            Transition from 'A' to 'B': 0|-
        """
    __hash__: Incomplete
    def __eq__(self, other):
        """
        Return ``True`` if the two transitions are the same, i.e., if the
        both go from the same states to the same states and read and
        write the same words.

        Note that the hooks are not checked.

        INPUT:

        - ``self`` -- a transition

        - ``other`` -- a transition

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.combinat.finite_state_machine import FSMState, FSMTransition
            sage: A = FSMState('A', is_initial=True)
            sage: t1 = FSMTransition('A', 'B', 0, 1)
            sage: t2 = FSMTransition(A, 'B', 0, 1)
            sage: t1 == t2
            True
        """
    def __ne__(self, other):
        """
        Test for inequality, complement of __eq__.

        INPUT:

        - ``self`` -- a transition

        - ``other`` -- a transition

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.combinat.finite_state_machine import FSMState, FSMTransition
            sage: A = FSMState('A', is_initial=True)
            sage: t1 = FSMTransition('A', 'B', 0, 1)
            sage: t2 = FSMTransition(A, 'B', 0, 1)
            sage: t1 != t2
            False
        """
    def __bool__(self) -> bool:
        """
        Return ``True``.

        EXAMPLES::

            sage: from sage.combinat.finite_state_machine import FSMTransition
            sage: bool(FSMTransition('A', 'B', 0))
            True
        """

def is_FiniteStateMachine(FSM):
    """
    Test whether or not ``FSM`` inherits from :class:`FiniteStateMachine`.

    TESTS::

        sage: from sage.combinat.finite_state_machine import is_FiniteStateMachine
        sage: is_FiniteStateMachine(FiniteStateMachine())
        doctest:warning...
        DeprecationWarning: The function is_FiniteStateMachine is deprecated; use 'isinstance(..., FiniteStateMachine)' instead.
        See https://github.com/sagemath/sage/issues/38032 for details.
        True
        sage: is_FiniteStateMachine(Automaton())
        True
        sage: is_FiniteStateMachine(Transducer())
        True
    """
def duplicate_transition_ignore(old_transition, new_transition):
    """
    Default function for handling duplicate transitions in finite
    state machines. This implementation ignores the occurrence.

    See the documentation of the ``on_duplicate_transition`` parameter
    of :class:`FiniteStateMachine`.

    INPUT:

    - ``old_transition`` -- a transition in a finite state machine

    - ``new_transition`` -- a transition, identical to ``old_transition``,
      which is to be inserted into the finite state machine

    OUTPUT: the same transition, unchanged

    EXAMPLES::

        sage: from sage.combinat.finite_state_machine import duplicate_transition_ignore
        sage: from sage.combinat.finite_state_machine import FSMTransition
        sage: duplicate_transition_ignore(FSMTransition(0, 0, 1),
        ....:                             FSMTransition(0, 0, 1))
        Transition from 0 to 0: 1|-
    """
def duplicate_transition_raise_error(old_transition, new_transition) -> None:
    """
    Alternative function for handling duplicate transitions in finite
    state machines.

    This implementation raises a :exc:`ValueError`.

    See the documentation of the ``on_duplicate_transition`` parameter
    of :class:`FiniteStateMachine`.

    INPUT:

    - ``old_transition`` -- a transition in a finite state machine

    - ``new_transition`` -- a transition, identical to ``old_transition``,
      which is to be inserted into the finite state machine

    OUTPUT: nothing. A :exc:`ValueError` is raised

    EXAMPLES::

        sage: from sage.combinat.finite_state_machine import duplicate_transition_raise_error
        sage: from sage.combinat.finite_state_machine import FSMTransition
        sage: duplicate_transition_raise_error(FSMTransition(0, 0, 1),
        ....:                                  FSMTransition(0, 0, 1))
        Traceback (most recent call last):
        ...
        ValueError: Attempting to re-insert transition Transition from 0 to 0: 1|-
    """
def duplicate_transition_add_input(old_transition, new_transition):
    '''
    Alternative function for handling duplicate transitions in finite
    state machines. This implementation adds the input label of the
    new transition to the input label of the old transition.  This is
    intended for the case where a Markov chain is modelled by a finite
    state machine using the input labels as transition probabilities.

    See the documentation of the ``on_duplicate_transition`` parameter
    of :class:`FiniteStateMachine`.

    INPUT:

    - ``old_transition`` -- a transition in a finite state machine

    - ``new_transition`` -- a transition, identical to ``old_transition``,
      which is to be inserted into the finite state machine

    OUTPUT:

    A transition whose input weight is the sum of the input
    weights of ``old_transition`` and ``new_transition``.

    EXAMPLES::

        sage: from sage.combinat.finite_state_machine import duplicate_transition_add_input
        sage: from sage.combinat.finite_state_machine import FSMTransition
        sage: duplicate_transition_add_input(FSMTransition(\'a\', \'a\', 1/2),
        ....:                                FSMTransition(\'a\', \'a\', 1/2))
        Transition from \'a\' to \'a\': 1|-

    Input labels must be lists of length 1::

        sage: duplicate_transition_add_input(FSMTransition(\'a\', \'a\', [1, 1]),
        ....:                                FSMTransition(\'a\', \'a\', [1, 1]))
        Traceback (most recent call last):
        ...
        TypeError: Trying to use duplicate_transition_add_input on
        "Transition from \'a\' to \'a\': 1,1|-" and
        "Transition from \'a\' to \'a\': 1,1|-",
        but input words are assumed to be lists of length 1
    '''

class FiniteStateMachine(SageObject):
    '''
    Class for a finite state machine.

    A finite state machine is a finite set of states connected by
    transitions.

    INPUT:

    - ``data`` -- can be any of the following:

      #. a dictionary of dictionaries (of transitions),

      #. a dictionary of lists (of states or transitions),

      #. a list (of transitions),

      #. a function (transition function),

      #. an other instance of a finite state machine.

    - ``initial_states`` and ``final_states`` -- the initial and
      final states of this machine

    - ``input_alphabet`` and ``output_alphabet`` -- the input and
      output alphabets of this machine

    - ``determine_alphabets`` -- if ``True``, then the function
      :meth:`.determine_alphabets` is called after ``data`` was read and
      processed, if ``False``, then not. If it is ``None``, then it is
      decided during the construction of the finite state machine
      whether :meth:`.determine_alphabets` should be called.

    - ``with_final_word_out`` -- if given (not ``None``), then the
      function :meth:`.with_final_word_out` (more precisely, its inplace
      pendant :meth:`.construct_final_word_out`) is called with input
      ``letters=with_final_word_out`` at the end of the creation
      process.

    - ``store_states_dict`` -- if ``True``, then additionally the states
      are stored in an internal dictionary for speed up

    - ``on_duplicate_transition`` -- a function which is called when a
      transition is inserted into ``self`` which already existed (same
      ``from_state``, same ``to_state``, same ``word_in``, same ``word_out``).

      This function is assumed to take two arguments, the first being
      the already existing transition, the second being the new
      transition (as an :class:`FSMTransition`). The function must
      return the (possibly modified) original transition.

      By default, we have ``on_duplicate_transition=None``, which is
      interpreted as
      ``on_duplicate_transition=duplicate_transition_ignore``, where
      ``duplicate_transition_ignore`` is a predefined function
      ignoring the occurrence. Other such predefined functions are
      ``duplicate_transition_raise_error`` and
      ``duplicate_transition_add_input``.

    OUTPUT: a finite state machine

    The object creation of :class:`Automaton` and :class:`Transducer`
    is the same as the one described here (i.e. just replace the word
    ``FiniteStateMachine`` by ``Automaton`` or ``Transducer``).

    Each transition of an automaton has an input label. Automata can,
    for example, be determinised (see
    :meth:`Automaton.determinisation`) and minimized (see
    :meth:`Automaton.minimization`). Each transition of a transducer
    has an input and an output label. Transducers can, for example, be
    simplified (see :meth:`Transducer.simplification`).

    EXAMPLES::

        sage: from sage.combinat.finite_state_machine import FSMState, FSMTransition

    See documentation for more examples.

    We illustrate the different input formats:

    #.  The input-data can be a dictionary of dictionaries, where

        - the keys of the outer dictionary are state-labels (from-states of
          transitions),
        - the keys of the inner dictionaries are state-labels (to-states of
          transitions),
        - the values of the inner dictionaries specify the transition
          more precisely.

        The easiest is to use a tuple consisting of an input and an
        output word::

            sage: FiniteStateMachine({\'a\':{\'b\':(0, 1), \'c\':(1, 1)}})
            Finite state machine with 3 states

        Instead of the tuple anything iterable (e.g. a list) can be
        used as well.

        If you want to use the arguments of :class:`FSMTransition`
        directly, you can use a dictionary::

            sage: FiniteStateMachine({\'a\':{\'b\':{\'word_in\':0, \'word_out\':1},
            ....:                          \'c\':{\'word_in\':1, \'word_out\':1}}})
            Finite state machine with 3 states

        In the case you already have instances of
        :class:`FSMTransition`, it is possible to use them directly::

            sage: FiniteStateMachine({\'a\':{\'b\':FSMTransition(\'a\', \'b\', 0, 1),
            ....:                          \'c\':FSMTransition(\'a\', \'c\', 1, 1)}})
            Finite state machine with 3 states

    #.  The input-data can be a dictionary of lists, where the keys
        are states or label of states.

        The list-elements can be states::

            sage: a = FSMState(\'a\')
            sage: b = FSMState(\'b\')
            sage: c = FSMState(\'c\')
            sage: FiniteStateMachine({a:[b, c]})
            Finite state machine with 3 states

        Or the list-elements can simply be labels of states::

            sage: FiniteStateMachine({\'a\':[\'b\', \'c\']})
            Finite state machine with 3 states

        The list-elements can also be transitions::

            sage: FiniteStateMachine({\'a\':[FSMTransition(\'a\', \'b\', 0, 1),
            ....:                          FSMTransition(\'a\', \'c\', 1, 1)]})
            Finite state machine with 3 states

        Or they can be tuples of a label, an input word and an output
        word specifying a transition::

            sage: FiniteStateMachine({\'a\':[(\'b\', 0, 1), (\'c\', 1, 1)]})
            Finite state machine with 3 states

    #.  The input-data can be a list, where its elements specify
        transitions::

            sage: FiniteStateMachine([FSMTransition(\'a\', \'b\', 0, 1),
            ....:                     FSMTransition(\'a\', \'c\', 1, 1)])
            Finite state machine with 3 states

        It is possible to skip ``FSMTransition`` in the example above::

            sage: FiniteStateMachine([(\'a\', \'b\', 0, 1), (\'a\', \'c\', 1, 1)])
            Finite state machine with 3 states

        The parameters of the transition are given in tuples. Anyhow,
        anything iterable (e.g. a list) is possible.

        You can also name the parameters of the transition. For this
        purpose you take a dictionary::

            sage: FiniteStateMachine([{\'from_state\':\'a\', \'to_state\':\'b\',
            ....:                      \'word_in\':0, \'word_out\':1},
            ....:                     {\'from_state\':\'a\', \'to_state\':\'c\',
            ....:                      \'word_in\':1, \'word_out\':1}])
            Finite state machine with 3 states

        Other arguments, which :class:`FSMTransition` accepts, can be
        added, too.

    #.  The input-data can also be function acting as transition
        function:

        This function has two input arguments:

        #. a label of a state (from which the transition starts),

        #. a letter of the (input-)alphabet (as input-label of the transition).

        It returns a tuple with the following entries:

        #. a label of a state (to which state the transition goes),

        #. a letter of or a word over the (output-)alphabet (as
           output-label of the transition).

        It may also output a list of such tuples if several
        transitions from the from-state and the input letter exist
        (this means that the finite state machine is
        non-deterministic).

        If the transition does not exist, the function should raise a
        :exc:`LookupError` or return an empty list.

        When constructing a finite state machine in this way, some
        initial states and an input alphabet have to be specified.

        ::

            sage: def f(state_from, read):
            ....:     if int(state_from) + read <= 2:
            ....:         state_to = 2*int(state_from)+read
            ....:         write = 0
            ....:     else:
            ....:         state_to = 2*int(state_from) + read - 5
            ....:         write = 1
            ....:     return (str(state_to), write)
            sage: F = FiniteStateMachine(f, input_alphabet=[0, 1],
            ....:                        initial_states=[\'0\'],
            ....:                        final_states=[\'0\'])
            sage: F([1, 0, 1])
            (True, \'0\', [0, 0, 1])

    #.  The input-data can be an other instance of a finite state machine::

            sage: F = FiniteStateMachine()
            sage: G = Transducer(F)
            sage: G == F
            True

        The other parameters cannot be specified in that case. If you
        want to change these, use the attributes
        :attr:`FSMState.is_initial`, :attr:`FSMState.is_final`,
        :attr:`input_alphabet`, :attr:`output_alphabet`,
        :attr:`on_duplicate_transition` and methods
        :meth:`.determine_alphabets`,
        :meth:`.construct_final_word_out` on the new machine,
        respectively.

    The following examples demonstrate the use of ``on_duplicate_transition``::

        sage: F = FiniteStateMachine([[\'a\', \'a\', 1/2], [\'a\', \'a\', 1/2]])
        sage: F.transitions()
        [Transition from \'a\' to \'a\': 1/2|-]

    ::

        sage: from sage.combinat.finite_state_machine import duplicate_transition_raise_error
        sage: F1 = FiniteStateMachine([[\'a\', \'a\', 1/2], [\'a\', \'a\', 1/2]],
        ....:                         on_duplicate_transition=duplicate_transition_raise_error)
        Traceback (most recent call last):
        ...
        ValueError: Attempting to re-insert transition Transition from \'a\' to \'a\': 1/2|-

    Use ``duplicate_transition_add_input`` to emulate a Markov chain,
    the input labels are considered as transition probabilities::

        sage: from sage.combinat.finite_state_machine import duplicate_transition_add_input
        sage: F = FiniteStateMachine([[\'a\', \'a\', 1/2], [\'a\', \'a\', 1/2]],
        ....:                        on_duplicate_transition=duplicate_transition_add_input)
        sage: F.transitions()
        [Transition from \'a\' to \'a\': 1|-]

    Use ``with_final_word_out`` to construct final output::

        sage: T = Transducer([(0, 1, 0, 0), (1, 0, 0, 0)],
        ....:                initial_states=[0],
        ....:                final_states=[0],
        ....:                with_final_word_out=0)
        sage: for s in T.iter_final_states():
        ....:     print("{} {}".format(s, s.final_word_out))
        0 []
        1 [0]

    TESTS::

        sage: a = FSMState(\'S_a\', \'a\')
        sage: b = FSMState(\'S_b\', \'b\')
        sage: c = FSMState(\'S_c\', \'c\')
        sage: d = FSMState(\'S_d\', \'d\')
        sage: FiniteStateMachine({a:[b, c], b:[b, c, d],
        ....:                     c:[a, b], d:[a, c]})
        Finite state machine with 4 states

    We have several constructions which lead to the same finite
    state machine::

        sage: A = FSMState(\'A\')
        sage: B = FSMState(\'B\')
        sage: C = FSMState(\'C\')
        sage: FSM1 = FiniteStateMachine(
        ....:  {A:{B:{\'word_in\':0, \'word_out\':1},
        ....:   C:{\'word_in\':1, \'word_out\':1}}})
        sage: FSM2 = FiniteStateMachine({A:{B:(0, 1), C:(1, 1)}})
        sage: FSM3 = FiniteStateMachine(
        ....:  {A:{B:FSMTransition(A, B, 0, 1),
        ....:      C:FSMTransition(A, C, 1, 1)}})
        sage: FSM4 = FiniteStateMachine({A:[(B, 0, 1), (C, 1, 1)]})
        sage: FSM5 = FiniteStateMachine(
        ....:  {A:[FSMTransition(A, B, 0, 1), FSMTransition(A, C, 1, 1)]})
        sage: FSM6 = FiniteStateMachine(
        ....:  [{\'from_state\':A, \'to_state\':B, \'word_in\':0, \'word_out\':1},
        ....:   {\'from_state\':A, \'to_state\':C, \'word_in\':1, \'word_out\':1}])
        sage: FSM7 = FiniteStateMachine([(A, B, 0, 1), (A, C, 1, 1)])
        sage: FSM8 = FiniteStateMachine(
        ....:  [FSMTransition(A, B, 0, 1), FSMTransition(A, C, 1, 1)])

        sage: FSM1 == FSM2 == FSM3 == FSM4 == FSM5 == FSM6 == FSM7 == FSM8
        True

    It is possible to skip ``FSMTransition`` in the example above.

    Some more tests for different input-data::

        sage: FiniteStateMachine({\'a\':{\'a\':[0, 0], \'b\':[1, 1]},
        ....:                     \'b\':{\'b\':[1, 0]}})
        Finite state machine with 2 states

        sage: a = FSMState(\'S_a\', \'a\')
        sage: b = FSMState(\'S_b\', \'b\')
        sage: c = FSMState(\'S_c\', \'c\')
        sage: d = FSMState(\'S_d\', \'d\')
        sage: t1 = FSMTransition(a, b)
        sage: t2 = FSMTransition(b, c)
        sage: t3 = FSMTransition(b, d)
        sage: t4 = FSMTransition(c, d)
        sage: FiniteStateMachine([t1, t2, t3, t4])
        Finite state machine with 4 states

    We test that no input parameter is allowed when creating a finite
    state machine from an existing instance::

        sage: F = FiniteStateMachine()
        sage: FiniteStateMachine(F, initial_states=[1])
        Traceback (most recent call last):
        ...
        ValueError: initial_states cannot be specified when
        copying another finite state machine.
        sage: FiniteStateMachine(F, final_states=[1])
        Traceback (most recent call last):
        ...
        ValueError: final_states cannot be specified when
        copying another finite state machine.
        sage: FiniteStateMachine(F, input_alphabet=[1])
        Traceback (most recent call last):
        ...
        ValueError: input_alphabet cannot be specified when
        copying another finite state machine.
        sage: FiniteStateMachine(F, output_alphabet=[1])
        Traceback (most recent call last):
        ...
        ValueError: output_alphabet cannot be specified when
        copying another finite state machine.
        sage: from sage.combinat.finite_state_machine import (
        ....:     duplicate_transition_add_input)
        sage: FiniteStateMachine(F,
        ....:     on_duplicate_transition=duplicate_transition_add_input)
        Traceback (most recent call last):
        ...
        ValueError: on_duplicate_transition cannot be specified when
        copying another finite state machine.
        sage: FiniteStateMachine(F, determine_alphabets=False)
        Traceback (most recent call last):
        ...
        ValueError: determine_alphabets cannot be specified when
        copying another finite state machine.
        sage: FiniteStateMachine(F, with_final_word_out=[1])
        Traceback (most recent call last):
        ...
        ValueError: with_final_word_out cannot be specified when
        copying another finite state machine.

    :issue:`19454` rewrote automatic detection of the alphabets::

        sage: def transition_function(state, letter):
        ....:     return (0, 3 + letter)
        sage: T1 = Transducer(transition_function,
        ....:     input_alphabet=[0, 1],
        ....:     initial_states=[0],
        ....:     final_states=[0])
        sage: T1.output_alphabet
        [3, 4]
        sage: T2 = Transducer([(0, 0, 0, 3), (0, 0, 0, 4)],
        ....:     initial_states=[0],
        ....:     final_states=[0])
        sage: T2.output_alphabet
        [3, 4]
        sage: T = Transducer([(0, 0, 1, 2)])
        sage: (T.input_alphabet, T.output_alphabet)
        ([1], [2])
        sage: T = Transducer([(0, 0, 1, 2)], determine_alphabets=False)
        sage: (T.input_alphabet, T.output_alphabet)
        (None, None)
        sage: T = Transducer([(0, 0, 1, 2)], input_alphabet=[0, 1])
        sage: (T.input_alphabet, T.output_alphabet)
        ([0, 1], [2])
        sage: T = Transducer([(0, 0, 1, 2)], output_alphabet=[2, 3])
        sage: (T.input_alphabet, T.output_alphabet)
        ([1], [2, 3])
        sage: T = Transducer([(0, 0, 1, 2)], input_alphabet=[0, 1],
        ....:     output_alphabet=[2, 3])
        sage: (T.input_alphabet, T.output_alphabet)
        ([0, 1], [2, 3])

    .. automethod:: __call__
    '''
    on_duplicate_transition = duplicate_transition_ignore
    input_alphabet: Incomplete
    output_alphabet: Incomplete
    def __init__(self, data=None, initial_states=None, final_states=None, input_alphabet=None, output_alphabet=None, determine_alphabets=None, with_final_word_out=None, store_states_dict: bool = True, on_duplicate_transition=None) -> None:
        """
        See :class:`FiniteStateMachine` for more information.

        TESTS::

            sage: FiniteStateMachine()
            Empty finite state machine
        """
    def __copy__(self) -> None:
        """
        Return a (shallow) copy of the finite state machine.

        OUTPUT: a new finite state machine

        TESTS::

            sage: copy(FiniteStateMachine())
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    copy = __copy__
    def empty_copy(self, memo=None, new_class=None):
        """
        Return an empty deep copy of the finite state machine, i.e.,
        ``input_alphabet``, ``output_alphabet``, ``on_duplicate_transition``
        are preserved, but states and transitions are not.

        INPUT:

        - ``memo`` -- dictionary storing already processed elements

        - ``new_class`` -- a class for the copy; by default
          (``None``), the class of ``self`` is used

        OUTPUT: a new finite state machine

        EXAMPLES::

            sage: from sage.combinat.finite_state_machine import duplicate_transition_raise_error
            sage: F = FiniteStateMachine([('A', 'A', 0, 2), ('A', 'A', 1, 3)],
            ....:                        input_alphabet=[0, 1],
            ....:                        output_alphabet=[2, 3],
            ....:                        on_duplicate_transition=duplicate_transition_raise_error)
            sage: FE = F.empty_copy(); FE
            Empty finite state machine
            sage: FE.input_alphabet
            [0, 1]
            sage: FE.output_alphabet
            [2, 3]
            sage: FE.on_duplicate_transition == duplicate_transition_raise_error
            True

        TESTS::

            sage: T = Transducer()
            sage: type(T.empty_copy())
            <class 'sage.combinat.finite_state_machine.Transducer'>
            sage: type(T.empty_copy(new_class=Automaton))
            <class 'sage.combinat.finite_state_machine.Automaton'>
        """
    def __deepcopy__(self, memo):
        """
        Return a deep copy of the finite state machine.

        INPUT:

        - ``memo`` -- dictionary storing already processed elements

        OUTPUT: a new finite state machine

        EXAMPLES::

            sage: F = FiniteStateMachine([('A', 'A', 0, 1), ('A', 'A', 1, 0)])
            sage: deepcopy(F)
            Finite state machine with 1 state
        """
    def deepcopy(self, memo=None):
        """
        Return a deep copy of the finite state machine.

        INPUT:

        - ``memo`` -- (default: ``None``) a dictionary storing already
          processed elements

        OUTPUT: a new finite state machine

        EXAMPLES::

            sage: F = FiniteStateMachine([('A', 'A', 0, 1), ('A', 'A', 1, 0)])
            sage: deepcopy(F)
            Finite state machine with 1 state

        TESTS:

        Make sure that the links between transitions and states
        are still intact::

            sage: C = deepcopy(F)
            sage: C.transitions()[0].from_state is C.state('A')
            True
            sage: C.transitions()[0].to_state is C.state('A')
            True
        """
    def relabeled(self, memo=None, labels=None):
        """
        Return a deep copy of the finite state machine, but the
        states are relabeled.

        INPUT:

        - ``memo`` -- (default: ``None``) a dictionary storing already
          processed elements

        - ``labels`` -- (default: ``None``) a dictionary or callable
          mapping old labels to new labels. If ``None``, then the new
          labels are integers starting with 0.

        OUTPUT: a new finite state machine

        EXAMPLES::

            sage: FSM1 = FiniteStateMachine([('A', 'B'), ('B', 'C'), ('C', 'A')])
            sage: FSM1.states()
            ['A', 'B', 'C']
            sage: FSM2 = FSM1.relabeled()
            sage: FSM2.states()
            [0, 1, 2]
            sage: FSM3 = FSM1.relabeled(labels={'A': 'a', 'B': 'b', 'C': 'c'})
            sage: FSM3.states()
            ['a', 'b', 'c']
            sage: FSM4 = FSM2.relabeled(labels=lambda x: 2*x)
            sage: FSM4.states()
            [0, 2, 4]

        TESTS::

            sage: FSM2.relabeled(labels=1)
            Traceback (most recent call last):
            ...
            TypeError: labels must be None, a callable or a dictionary.
        """
    def induced_sub_finite_state_machine(self, states):
        """
        Return a sub-finite-state-machine of the finite state machine
        induced by the given states.

        INPUT:

        - ``states`` -- list (or an iterator) of states (either labels or
          instances of :class:`FSMState`) of the sub-finite-state-machine

        OUTPUT:

        A new finite state machine. It consists (of deep copies) of
        the given states and (deep copies) of all transitions of ``self``
        between these states.

        EXAMPLES::

            sage: FSM = FiniteStateMachine([(0, 1, 0), (0, 2, 0),
            ....:                           (1, 2, 0), (2, 0, 0)])
            sage: sub_FSM = FSM.induced_sub_finite_state_machine([0, 1])
            sage: sub_FSM.states()
            [0, 1]
            sage: sub_FSM.transitions()
            [Transition from 0 to 1: 0|-]
            sage: FSM.induced_sub_finite_state_machine([3])
            Traceback (most recent call last):
            ...
            ValueError: 3 is not a state of this finite state machine.

        TESTS:

        Make sure that the links between transitions and states
        are still intact::

            sage: sub_FSM.transitions()[0].from_state is sub_FSM.state(0)
            True
        """
    def __hash__(self):
        """
        Since finite state machines are mutable, they should not be
        hashable, so we return a type error.

        OUTPUT: the hash of this finite state machine

        EXAMPLES::

            sage: hash(FiniteStateMachine())
            Traceback (most recent call last):
            ...
            TypeError: Finite state machines are mutable, and thus not hashable.
        """
    def __or__(self, other):
        """
        Return the disjoint union of this and another finite state machine.

        INPUT:

        - ``other`` -- a finite state machine

        OUTPUT: a new finite state machine

        .. SEEALSO::

            :meth:`.disjoint_union`, :meth:`.__and__`,
            :meth:`Automaton.intersection`,
            :meth:`Transducer.intersection`.

        TESTS::

            sage: FiniteStateMachine() | FiniteStateMachine([('A', 'B')])
            Finite state machine with 2 states
            sage: FiniteStateMachine() | 42
            Traceback (most recent call last):
            ...
            TypeError: Can only add finite state machine
        """
    __add__ = __or__
    def __iadd__(self, other) -> None:
        """
        TESTS::

            sage: F = FiniteStateMachine()
            sage: F += FiniteStateMachine()
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def __and__(self, other):
        """
        Return the intersection of ``self`` with ``other``.

        TESTS::

            sage: FiniteStateMachine() & FiniteStateMachine([('A', 'B')])
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def __imul__(self, other) -> None:
        """
        TESTS::

            sage: F = FiniteStateMachine()
            sage: F *= FiniteStateMachine()
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def __call__(self, *args, **kwargs):
        """
        Call either method :meth:`.composition` or :meth:`.process`
        (with ``full_output=False``). If the input is not finite
        (``is_finite`` of input is ``False``), then
        :meth:`.iter_process` (with ``iterator_type='simple'``) is
        called. Moreover, the flag ``automatic_output_type`` is set
        (unless ``format_output`` is specified).
        See the documentation of these functions for possible
        parameters.

        EXAMPLES:

        The following code performs a :meth:`composition`::

            sage: F = Transducer([('A', 'B', 1, 0), ('B', 'B', 1, 1),
            ....:                 ('B', 'B', 0, 0)],
            ....:                initial_states=['A'], final_states=['B'])
            sage: G = Transducer([(1, 1, 0, 0), (1, 2, 1, 0),
            ....:                 (2, 2, 0, 1), (2, 1, 1, 1)],
            ....:                initial_states=[1], final_states=[1])
            sage: H = G(F)
            sage: H.states()
            [('A', 1), ('B', 1), ('B', 2)]

        An automaton or transducer can also act on an input (a list
        or other iterable of letters)::

            sage: binary_inverter = Transducer({'A': [('A', 0, 1), ('A', 1, 0)]},
            ....:                              initial_states=['A'], final_states=['A'])
            sage: binary_inverter([0, 1, 0, 0, 1, 1])
            [1, 0, 1, 1, 0, 0]

        We can also let them act on :doc:`words <words/words>`::

            sage: # needs sage.combinat
            sage: W = Words([0, 1]); W
            Finite and infinite words over {0, 1}
            sage: binary_inverter(W([0, 1, 1, 0, 1, 1]))
            word: 100100

        Infinite words work as well::

            sage: # needs sage.combinat
            sage: words.FibonacciWord()
            word: 0100101001001010010100100101001001010010...
            sage: binary_inverter(words.FibonacciWord())
            word: 1011010110110101101011011010110110101101...

        When only one successful path is found in a non-deterministic
        transducer, the result of that path is returned.

        ::

            sage: T = Transducer([(0, 1, 0, 1), (0, 2, 0, 2)],
            ....:                initial_states=[0], final_states=[1])
            sage: T.process([0])
            [(False, 2, [2]), (True, 1, [1])]
            sage: T([0])
            [1]

        .. SEEALSO::

            :meth:`.composition`,
            :meth:`~FiniteStateMachine.process`,
            :meth:`~FiniteStateMachine.iter_process`,
            :meth:`Automaton.process`,
            :meth:`Transducer.process`.

        TESTS::

            sage: F = FiniteStateMachine([(0, 1, 1, 'a'), (0, 2, 2, 'b')],
            ....:                        initial_states=[0],
            ....:                        final_states=[1])
            sage: A = Automaton([(0, 1, 1), (0, 2, 2)],
            ....:               initial_states=[0],
            ....:               final_states=[1])
            sage: T = Transducer([(0, 1, 1, 'a'), (0, 2, 2, 'b')],
            ....:                initial_states=[0],
            ....:                final_states=[1])
            sage: F([1])
            (True, 1, ['a'])
            sage: A([1])
            True
            sage: T([1])
            ['a']
            sage: F([2])
            (False, 2, ['b'])
            sage: A([2])
            False
            sage: T([2])
            Traceback (most recent call last):
            ...
            ValueError: Invalid input sequence.
            sage: F([3])
            (False, None, None)
            sage: A([3])
            False
            sage: T([3])
            Traceback (most recent call last):
            ...
            ValueError: Invalid input sequence.

        ::

            sage: F = FiniteStateMachine([(11, 11, 1, 'a'), (11, 12, 2, 'b'),
            ....:                         (11, 13, 3, 'c'), (11, 14, 4, 'd'),
            ....:                         (12, 13, 3, 'e'), (12, 13, 3, 'f'),
            ....:                         (12, 14, 4, 'g'), (12, 14, 4, 'h'),
            ....:                         (12, 13, 2, 'i'), (12, 14, 2, 'j')],
            ....:                        initial_states=[11],
            ....:                        final_states=[13])
            sage: def f(o):
            ....:     return ''.join(o)
            sage: F([0], format_output=f)
            (False, None, None)
            sage: F([3], format_output=f)
            (True, 13, 'c')
            sage: F([4], format_output=f)
            (False, 14, 'd')
            sage: F([2, 2], format_output=f)
            Traceback (most recent call last):
            ...
            ValueError: Got more than one output, but only allowed to show
            one. Change list_of_outputs option.
            sage: F([2, 2], format_output=f, list_of_outputs=True)
            [(False, 14, 'bj'), (True, 13, 'bi')]
            sage: F([2, 3], format_output=f)
            Traceback (most recent call last):
            ...
            ValueError: Got more than one output, but only allowed to show
            one. Change list_of_outputs option.
            sage: F([2, 3], format_output=f, list_of_outputs=True)
            [(True, 13, 'be'), (True, 13, 'bf')]
            sage: F([2, 4], format_output=f)
            Traceback (most recent call last):
            ...
            ValueError: Got more than one output, but only allowed to show
            one. Change list_of_outputs option.
            sage: F([2, 4], format_output=f, list_of_outputs=True)
            [(False, 14, 'bg'), (False, 14, 'bh')]

        ::

            sage: A = Automaton([(11, 11, 1), (11, 12, 2),
            ....:                (11, 13, 3), (11, 14, 4),
            ....:                (12, 13, 3), (12, 14, 4),
            ....:                (12, 32, 3), (12, 42, 4),
            ....:                (12, 13, 2), (12, 14, 2)],
            ....:               initial_states=[11],
            ....:               final_states=[13, 32])
            sage: def f(o):
            ....:     return ''.join(o)
            sage: A([0], format_output=f)
            False
            sage: A([3], format_output=f)
            True
            sage: A([4], format_output=f)
            False
            sage: A([2, 2], format_output=f)
            True
            sage: A([2, 2], format_output=f, list_of_outputs=True)
            [False, True]
            sage: A([2, 3], format_output=f)
            True
            sage: A([2, 3], format_output=f, list_of_outputs=True)
            [True, True]
            sage: A([2, 4], format_output=f)
            False
            sage: A([2, 4], format_output=f, list_of_outputs=True)
            [False, False]

        ::

            sage: T = Transducer([(11, 11, 1, 'a'), (11, 12, 2, 'b'),
            ....:                 (11, 13, 3, 'c'), (11, 14, 4, 'd'),
            ....:                 (12, 13, 3, 'e'), (12, 13, 3, 'f'),
            ....:                 (12, 14, 4, 'g'), (12, 14, 4, 'h'),
            ....:                 (12, 13, 2, 'i'), (12, 14, 2, 'j')],
            ....:                initial_states=[11],
            ....:                final_states=[13])
            sage: def f(o):
            ....:     return ''.join(o)
            sage: T([0], format_output=f)
            Traceback (most recent call last):
            ...
            ValueError: Invalid input sequence.
            sage: T([3], format_output=f)
            'c'
            sage: T([4], format_output=f)
            Traceback (most recent call last):
            ...
            ValueError: Invalid input sequence.
            sage: T([2, 2], format_output=f)
            'bi'
            sage: T([2, 2], format_output=f, list_of_outputs=True)
            [None, 'bi']
            sage: T([2, 2], format_output=f,
            ....:   list_of_outputs=True, only_accepted=True)
            ['bi']
            sage: T.process([2, 2], format_output=f, list_of_outputs=True)
            [(False, 14, 'bj'), (True, 13, 'bi')]
            sage: T([2, 3], format_output=f)
            Traceback (most recent call last):
            ...
            ValueError: Found more than one accepting path.
            sage: T([2, 3], format_output=f, list_of_outputs=True)
            ['be', 'bf']
            sage: T([2, 4], format_output=f)
            Traceback (most recent call last):
            ...
            ValueError: Invalid input sequence.
            sage: T([2, 4], format_output=f, list_of_outputs=True)
            [None, None]

        ::

            sage: from itertools import islice
            sage: inverter = Transducer({'A': [('A', 0, 1), ('A', 1, 0)]},
            ....:     initial_states=['A'], final_states=['A'])
            sage: inverter(words.FibonacciWord())                                       # needs sage.combinat
            word: 1011010110110101101011011010110110101101...
            sage: inverter(words.FibonacciWord(), automatic_output_type=True)           # needs sage.combinat
            word: 1011010110110101101011011010110110101101...
            sage: tuple(islice(inverter(words.FibonacciWord(),                          # needs sage.combinat
            ....:                       automatic_output_type=False), 10r))
            (1, 0, 1, 1, 0, 1, 0, 1, 1, 0)
            sage: type(inverter((1, 0, 1, 1, 0, 1, 0, 1, 1, 0),
            ....:               automatic_output_type=False))
            <class 'list'>
            sage: type(inverter((1, 0, 1, 1, 0, 1, 0, 1, 1, 0),
            ....:               automatic_output_type=True))
            <class 'tuple'>
        """
    def __bool__(self) -> bool:
        """
        Return ``True`` if the finite state machine consists of at least
        one state.

        TESTS::

            sage: bool(FiniteStateMachine())
            False
        """
    def __eq__(self, other):
        """
        Return ``True`` if the two finite state machines are equal,
        i.e., if they have the same states and the same transitions.

        INPUT:

        - ``self`` -- a finite state machine

        - ``other`` -- a finite state machine

        OUTPUT: boolean

        Note that this function compares all attributes of a state (by
        using :meth:`FSMState.fully_equal`) except for colors. Colors
        are handled as follows: If the colors coincide, then the
        finite state machines are also considered equal. If not, then
        they are considered as equal if both finite state machines are
        monochromatic.

        EXAMPLES::

            sage: F = FiniteStateMachine([('A', 'B', 1)])
            sage: F == FiniteStateMachine()
            False
            sage: G = FiniteStateMachine([('A', 'B', 1)],
            ....:                        initial_states=['A'])
            sage: F == G
            False
            sage: F.state('A').is_initial = True
            sage: F == G
            True

        This shows the behavior when the states have colors::

            sage: F.state('A').color = 'red'
            sage: G.state('A').color = 'red'
            sage: F == G
            True
            sage: G.state('A').color = 'blue'
            sage: F == G
            False
            sage: F.state('B').color = 'red'
            sage: F.is_monochromatic()
            True
            sage: G.state('B').color = 'blue'
            sage: G.is_monochromatic()
            True
            sage: F == G
            True
        """
    def __ne__(self, other):
        """
        Test for inequality, complement of :meth:`.__eq__`.

        INPUT:

        - ``self`` -- a finite state machine

        - ``other`` -- a finite state machine

        OUTPUT: boolean

        EXAMPLES::

            sage: E = FiniteStateMachine([('A', 'B', 0)])
            sage: F = Automaton([('A', 'B', 0)])
            sage: G = Transducer([('A', 'B', 0, 1)])
            sage: E == F
            True
            sage: E == G
            False
        """
    def __contains__(self, item) -> bool:
        """
        Return ``True``, if the finite state machine contains the
        state or transition item.

        Note that only the labels of the
        states and the input and output words are tested.

        INPUT:

        - ``item`` -- a state or a transition

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.combinat.finite_state_machine import FSMState, FSMTransition
            sage: F = FiniteStateMachine([('A', 'B', 0), ('B', 'A', 1)])
            sage: FSMState('A', is_initial=True) in F
            True
            sage: 'A' in F
            False
            sage: FSMTransition('A', 'B', 0) in F
            True
        """
    def is_Markov_chain(self, is_zero=None):
        """
        Check whether ``self`` is a Markov chain where the transition
        probabilities are modeled as input labels.

        INPUT:

        - ``is_zero`` -- by default (``is_zero=None``), checking for
          zero is simply done by
          :meth:`~sage.structure.element.Element.is_zero`.  This
          parameter can be used to provide a more sophisticated check
          for zero, e.g. in the case of symbolic probabilities, see
          the examples below.

        OUTPUT: boolean

        :attr:`on_duplicate_transition` must be
        :func:`duplicate_transition_add_input`, the sum of the input weights
        of the transitions leaving a state must add up to 1 and the sum of
        initial probabilities must add up to 1 (or all be ``None``).

        EXAMPLES::

            sage: from sage.combinat.finite_state_machine import duplicate_transition_add_input
            sage: F = Transducer([[0, 0, 1/4, 0], [0, 1, 3/4, 1],
            ....:                 [1, 0, 1/2, 0], [1, 1, 1/2, 1]],
            ....:                on_duplicate_transition=duplicate_transition_add_input)
            sage: F.is_Markov_chain()
            True

        :attr:`on_duplicate_transition` must be
        :func:`duplicate_transition_add_input`::

            sage: F = Transducer([[0, 0, 1/4, 0], [0, 1, 3/4, 1],
            ....:                 [1, 0, 1/2, 0], [1, 1, 1/2, 1]])
            sage: F.is_Markov_chain()
            False

        Sum of input labels of the transitions leaving states must be 1::

            sage: F = Transducer([[0, 0, 1/4, 0], [0, 1, 3/4, 1],
            ....:                 [1, 0, 1/2, 0]],
            ....:                on_duplicate_transition=duplicate_transition_add_input)
            sage: F.is_Markov_chain()
            False

        The initial probabilities of all states must be ``None`` or they must
        sum up to 1. The initial probabilities of all states have to be set in the latter case::

            sage: F = Transducer([[0, 0, 1/4, 0], [0, 1, 3/4, 1],
            ....:                 [1, 0, 1, 0]],
            ....:                on_duplicate_transition=duplicate_transition_add_input)
            sage: F.is_Markov_chain()
            True
            sage: F.state(0).initial_probability = 1/4
            sage: F.is_Markov_chain()
            False
            sage: F.state(1).initial_probability = 7
            sage: F.is_Markov_chain()
            False
            sage: F.state(1).initial_probability = 3/4
            sage: F.is_Markov_chain()
            True

        If the probabilities are variables in the symbolic ring,
        :func:`~sage.symbolic.assumptions.assume` will do the trick::

            sage: # needs sage.symbolic
            sage: var('p q')
            (p, q)
            sage: F = Transducer([(0, 0, p, 1), (0, 0, q, 0)],
            ....:                on_duplicate_transition=duplicate_transition_add_input)
            sage: assume(p + q == 1)
            sage: (p + q - 1).is_zero()
            True
            sage: F.is_Markov_chain()
            True
            sage: forget()
            sage: del(p, q)

        If the probabilities are variables in some polynomial ring,
        the parameter ``is_zero`` can be used::

            sage: R.<p, q> = PolynomialRing(QQ)
            sage: def is_zero_polynomial(polynomial):
            ....:     return polynomial in (p + q - 1)*R
            sage: F = Transducer([(0, 0, p, 1), (0, 0, q, 0)],
            ....:                on_duplicate_transition=duplicate_transition_add_input)
            sage: F.state(0).initial_probability = p + q
            sage: F.is_Markov_chain()
            False
            sage: F.is_Markov_chain(is_zero_polynomial)                                 # needs sage.libs.singular
            True
        """
    default_format_letter = latex
    format_letter = default_format_letter
    def format_letter_negative(self, letter):
        """
        Format negative numbers as overlined numbers, everything
        else by standard LaTeX formatting.

        INPUT:

        - ``letter`` -- anything

        OUTPUT:

        Overlined absolute value if letter is a negative integer,
        :func:`latex(letter) <sage.misc.latex.latex>` otherwise.

        EXAMPLES::

            sage: A = Automaton([(0, 0, -1)])
            sage: list(map(A.format_letter_negative, [-1, 0, 1, 'a', None]))
            ['\\\\overline{1}', 0, 1, \\text{\\texttt{a}}, \\mathrm{None}]
            sage: A.latex_options(format_letter=A.format_letter_negative)
            sage: print(latex(A))
            \\begin{tikzpicture}[auto, initial text=, >=latex]
            \\node[state] (v0) at (3.000000, 0.000000) {$0$};
            \\path[->] (v0) edge[loop above] node {$\\overline{1}$} ();
            \\end{tikzpicture}
        """
    def format_transition_label_reversed(self, word):
        """
        Format words in transition labels in reversed order.

        INPUT:

        - ``word`` -- list of letters

        OUTPUT:

        String representation of ``word`` suitable to be typeset in
        mathematical mode, letters are written in reversed order.

        This is the reversed version of
        :meth:`.default_format_transition_label`.

        In digit expansions, digits are frequently processed from the
        least significant to the most significant position, but it is
        customary to write the least significant digit at the
        right-most position. Therefore, the labels have to be
        reversed.

        EXAMPLES::

            sage: T = Transducer([(0, 0, 0, [1, 2, 3])])
            sage: T.format_transition_label_reversed([1, 2, 3])
            '3 2 1'
            sage: T.latex_options(format_transition_label=T.format_transition_label_reversed)
            sage: print(latex(T))
            \\begin{tikzpicture}[auto, initial text=, >=latex]
            \\node[state] (v0) at (3.000000, 0.000000) {$0$};
            \\path[->] (v0) edge[loop above] node {$0\\mid 3 2 1$} ();
            \\end{tikzpicture}

        TESTS:

        Check that :issue:`16357` is fixed::

            sage: T = Transducer()
            sage: T.format_transition_label_reversed([])
            '\\\\varepsilon'
        """
    def default_format_transition_label(self, word):
        '''
        Default formatting of words in transition labels for LaTeX output.

        INPUT:

        - ``word`` -- list of letters

        OUTPUT:

        String representation of ``word`` suitable to be typeset in
        mathematical mode.

        -   For a non-empty word: Concatenation of the letters, piped through
            ``self.format_letter`` and separated by blanks.
        -   For an empty word:
            ``sage.combinat.finite_state_machine.EmptyWordLaTeX``.

        There is also a variant :meth:`.format_transition_label_reversed`
        writing the words in reversed order.

        EXAMPLES:

        #.  Example of a non-empty word::

                sage: T = Transducer()
                sage: print(T.default_format_transition_label(
                ....:    [\'a\', \'alpha\', \'a_1\', \'0\', 0, (0, 1)]))
                \\text{\\texttt{a}} \\text{\\texttt{alpha}}
                \\text{\\texttt{a{\\char`\\_}1}} 0 0 \\left(0, 1\\right)

        #.  In the example above, ``\'a\'`` and ``\'alpha\'`` should perhaps
            be symbols::

                sage: var(\'a alpha a_1\')                                                # needs sage.symbolic
                (a, alpha, a_1)
                sage: print(T.default_format_transition_label([a, alpha, a_1]))         # needs sage.symbolic
                a \\alpha a_{1}

        #.  Example of an empty word::

                sage: print(T.default_format_transition_label([]))
                \\varepsilon

            We can change this by setting
            ``sage.combinat.finite_state_machine.EmptyWordLaTeX``::

                sage: sage.combinat.finite_state_machine.EmptyWordLaTeX = \'\'
                sage: T.default_format_transition_label([])
                \'\'

            Finally, we restore the default value::

                sage: sage.combinat.finite_state_machine.EmptyWordLaTeX = r\'\\varepsilon\'

        #.  This method is the default value for
            ``FiniteStateMachine.format_transition_label``. That can be changed to be
            any other function::

                sage: A = Automaton([(0, 1, 0)])
                sage: def custom_format_transition_label(word):
                ....:     return "t"
                sage: A.latex_options(format_transition_label=custom_format_transition_label)
                sage: print(latex(A))
                \\begin{tikzpicture}[auto, initial text=, >=latex]
                \\node[state] (v0) at (3.000000, 0.000000) {$0$};
                \\node[state] (v1) at (-3.000000, 0.000000) {$1$};
                \\path[->] (v0) edge node[rotate=360.00, anchor=south] {$t$} (v1);
                \\end{tikzpicture}

        TESTS:

        Check that :issue:`16357` is fixed::

            sage: T = Transducer()
            sage: T.default_format_transition_label([])
            \'\\\\varepsilon\'
            sage: T.default_format_transition_label(iter([]))
            \'\\\\varepsilon\'
        '''
    format_transition_label = default_format_transition_label
    format_state_label: Incomplete
    accepting_style: Incomplete
    accepting_distance: Incomplete
    accepting_show_empty: Incomplete
    def latex_options(self, coordinates=None, format_state_label=None, format_letter=None, format_transition_label=None, loop_where=None, initial_where=None, accepting_style=None, accepting_distance=None, accepting_where=None, accepting_show_empty=None) -> None:
        '''
        Set options for LaTeX output via
        :func:`~sage.misc.latex.latex` and therefore
        :func:`~sage.misc.latex.view`.

        INPUT:

        - ``coordinates`` -- dictionary or a function mapping labels
          of states to pairs interpreted as coordinates. If no
          coordinates are given, states a placed equidistantly on a
          circle of radius `3`. See also :meth:`.set_coordinates`.

        - ``format_state_label`` -- a function mapping labels of
          states to a string suitable for typesetting in LaTeX\'s
          mathematics mode. If not given, :func:`~sage.misc.latex.latex`
          is used.

        - ``format_letter`` -- a function mapping letters of the input
          and output alphabets to a string suitable for typesetting in
          LaTeX\'s mathematics mode. If not given,
          :meth:`.default_format_transition_label` uses
          :func:`~sage.misc.latex.latex`.

        - ``format_transition_label`` -- a function mapping words over
          the input and output alphabets to a string suitable for
          typesetting in LaTeX\'s mathematics mode. If not given,
          :meth:`.default_format_transition_label` is used.

        - ``loop_where`` -- dictionary or a function mapping labels of
          initial states to one of ``\'above\'``, ``\'left\'``, ``\'below\'``,
          ``\'right\'``. If not given, ``\'above\'`` is used.

        - ``initial_where`` -- dictionary or a function mapping
          labels of initial states to one of ``\'above\'``, ``\'left\'``,
          ``\'below\'``, ``\'right\'``. If not given, TikZ\' default
          (currently ``\'left\'``) is used.

        - ``accepting_style`` -- one of ``\'accepting by double\'`` and
          ``\'accepting by arrow\'``. If not given, ``\'accepting by
          double\'`` is used unless there are non-empty final output
          words.

        - ``accepting_distance`` -- string giving a LaTeX length
          used for the length of the arrow leading from a final state.
          If not given, TikZ\' default (currently ``\'3ex\'``) is used
          unless there are non-empty final output words, in which case
          ``\'7ex\'`` is used.

        - ``accepting_where`` -- dictionary or a function mapping
          labels of final states to one of ``\'above\'``, ``\'left\'``,
          ``\'below\'``, ``\'right\'``. If not given, TikZ\' default
          (currently ``\'right\'``) is used. If the final state has a
          final output word, it is also possible to give an angle
          in degrees.

        - ``accepting_show_empty`` -- if ``True`` the arrow of an
          empty final output word is labeled as well. Note that this
          implicitly implies ``accepting_style=\'accepting by
          arrow\'``. If not given, the default ``False`` is used.

        OUTPUT: nothing

        As TikZ (cf. the :wikipedia:`PGF/TikZ`) is used to typeset
        the graphics, the syntax is oriented on TikZ\' syntax.

        This is a convenience function collecting all options for
        LaTeX output. All of its functionality can also be achieved by
        directly setting the attributes

        - ``coordinates``, ``format_label``, ``loop_where``,
          ``initial_where``, and ``accepting_where`` of
          :class:`FSMState` (here, ``format_label`` is a callable
          without arguments, everything else is a specific value);

        - ``format_label`` of :class:`FSMTransition` (``format_label``
          is a callable without arguments);

        - ``format_state_label``, ``format_letter``,
          ``format_transition_label``, ``accepting_style``,
          ``accepting_distance``, and ``accepting_show_empty``
          of :class:`FiniteStateMachine`.

        This function, however, also (somewhat) checks its input and
        serves to collect documentation on all these options.

        The function can be called several times, only those arguments
        which are not ``None`` are taken into account. By the same
        means, it can be combined with directly setting some
        attributes as outlined above.

        EXAMPLES:

        See also the section on :ref:`finite_state_machine_LaTeX_output`
        in the introductory examples of this module.

        ::

            sage: T = Transducer(initial_states=[4],
            ....:     final_states=[0, 3])
            sage: for j in srange(4):
            ....:     T.add_transition(4, j, 0, [0, j])
            ....:     T.add_transition(j, 4, 0, [0, -j])
            ....:     T.add_transition(j, j, 0, 0)
            Transition from 4 to 0: 0|0,0
            Transition from 0 to 4: 0|0,0
            Transition from 0 to 0: 0|0
            Transition from 4 to 1: 0|0,1
            Transition from 1 to 4: 0|0,-1
            Transition from 1 to 1: 0|0
            Transition from 4 to 2: 0|0,2
            Transition from 2 to 4: 0|0,-2
            Transition from 2 to 2: 0|0
            Transition from 4 to 3: 0|0,3
            Transition from 3 to 4: 0|0,-3
            Transition from 3 to 3: 0|0
            sage: T.add_transition(4, 4, 0, 0)
            Transition from 4 to 4: 0|0
            sage: T.state(3).final_word_out = [0, 0]
            sage: T.latex_options(
            ....:     coordinates={4: (0, 0),
            ....:                  0: (-6, 3),
            ....:                  1: (-2, 3),
            ....:                  2: (2, 3),
            ....:                  3: (6, 3)},
            ....:     format_state_label=lambda x: r\'\\mathbf{%s}\' % x,
            ....:     format_letter=lambda x: r\'w_{%s}\' % x,
            ....:     format_transition_label=lambda x:
            ....:         r"{\\scriptstyle %s}" % T.default_format_transition_label(x),
            ....:     loop_where={4: \'below\', 0: \'left\', 1: \'above\',
            ....:                 2: \'right\', 3:\'below\'},
            ....:     initial_where=lambda x: \'above\',
            ....:     accepting_style=\'accepting by double\',
            ....:     accepting_distance=\'10ex\',
            ....:     accepting_where={0: \'left\', 3: 45}
            ....:     )
            sage: T.state(4).format_label=lambda: r\'\\mathcal{I}\'
            sage: latex(T)
            \\begin{tikzpicture}[auto, initial text=, >=latex]
            \\node[state, initial, initial where=above] (v0) at (0.000000, 0.000000) {$\\mathcal{I}$};
            \\node[state, accepting, accepting where=left] (v1) at (-6.000000, 3.000000) {$\\mathbf{0}$};
            \\node[state, accepting, accepting where=45] (v2) at (6.000000, 3.000000) {$\\mathbf{3}$};
            \\path[->] (v2.45.00) edge node[rotate=45.00, anchor=south] {$\\$ \\mid {\\scriptstyle w_{0} w_{0}}$} ++(45.00:10ex);
            \\node[state] (v3) at (-2.000000, 3.000000) {$\\mathbf{1}$};
            \\node[state] (v4) at (2.000000, 3.000000) {$\\mathbf{2}$};
            \\path[->] (v1) edge[loop left] node[rotate=90, anchor=south] {${\\scriptstyle w_{0}}\\mid {\\scriptstyle w_{0}}$} ();
            \\path[->] (v1.-21.57) edge node[rotate=-26.57, anchor=south] {${\\scriptstyle w_{0}}\\mid {\\scriptstyle w_{0} w_{0}}$} (v0.148.43);
            \\path[->] (v3) edge[loop above] node {${\\scriptstyle w_{0}}\\mid {\\scriptstyle w_{0}}$} ();
            \\path[->] (v3.-51.31) edge node[rotate=-56.31, anchor=south] {${\\scriptstyle w_{0}}\\mid {\\scriptstyle w_{0} w_{-1}}$} (v0.118.69);
            \\path[->] (v4) edge[loop right] node[rotate=90, anchor=north] {${\\scriptstyle w_{0}}\\mid {\\scriptstyle w_{0}}$} ();
            \\path[->] (v4.-118.69) edge node[rotate=56.31, anchor=north] {${\\scriptstyle w_{0}}\\mid {\\scriptstyle w_{0} w_{-2}}$} (v0.51.31);
            \\path[->] (v2) edge[loop below] node {${\\scriptstyle w_{0}}\\mid {\\scriptstyle w_{0}}$} ();
            \\path[->] (v2.-148.43) edge node[rotate=26.57, anchor=north] {${\\scriptstyle w_{0}}\\mid {\\scriptstyle w_{0} w_{-3}}$} (v0.21.57);
            \\path[->] (v0.158.43) edge node[rotate=333.43, anchor=north] {${\\scriptstyle w_{0}}\\mid {\\scriptstyle w_{0} w_{0}}$} (v1.328.43);
            \\path[->] (v0.128.69) edge node[rotate=303.69, anchor=north] {${\\scriptstyle w_{0}}\\mid {\\scriptstyle w_{0} w_{1}}$} (v3.298.69);
            \\path[->] (v0.61.31) edge node[rotate=56.31, anchor=south] {${\\scriptstyle w_{0}}\\mid {\\scriptstyle w_{0} w_{2}}$} (v4.231.31);
            \\path[->] (v0.31.57) edge node[rotate=26.57, anchor=south] {${\\scriptstyle w_{0}}\\mid {\\scriptstyle w_{0} w_{3}}$} (v2.201.57);
            \\path[->] (v0) edge[loop below] node {${\\scriptstyle w_{0}}\\mid {\\scriptstyle w_{0}}$} ();
            \\end{tikzpicture}
            sage: view(T) # not tested

        To actually see this, use the live documentation in the Sage notebook
        and execute the cells.

        By changing some of the options, we get the following output::

            sage: T.latex_options(
            ....:     format_transition_label=T.default_format_transition_label,
            ....:     accepting_style=\'accepting by arrow\',
            ....:     accepting_show_empty=True
            ....:     )
            sage: latex(T)
            \\begin{tikzpicture}[auto, initial text=, >=latex, accepting text=, accepting/.style=accepting by arrow, accepting distance=10ex]
            \\node[state, initial, initial where=above] (v0) at (0.000000, 0.000000) {$\\mathcal{I}$};
            \\node[state] (v1) at (-6.000000, 3.000000) {$\\mathbf{0}$};
            \\path[->] (v1.180.00) edge node[rotate=360.00, anchor=south] {$\\$ \\mid \\varepsilon$} ++(180.00:10ex);
            \\node[state] (v2) at (6.000000, 3.000000) {$\\mathbf{3}$};
            \\path[->] (v2.45.00) edge node[rotate=45.00, anchor=south] {$\\$ \\mid w_{0} w_{0}$} ++(45.00:10ex);
            \\node[state] (v3) at (-2.000000, 3.000000) {$\\mathbf{1}$};
            \\node[state] (v4) at (2.000000, 3.000000) {$\\mathbf{2}$};
            \\path[->] (v1) edge[loop left] node[rotate=90, anchor=south] {$w_{0}\\mid w_{0}$} ();
            \\path[->] (v1.-21.57) edge node[rotate=-26.57, anchor=south] {$w_{0}\\mid w_{0} w_{0}$} (v0.148.43);
            \\path[->] (v3) edge[loop above] node {$w_{0}\\mid w_{0}$} ();
            \\path[->] (v3.-51.31) edge node[rotate=-56.31, anchor=south] {$w_{0}\\mid w_{0} w_{-1}$} (v0.118.69);
            \\path[->] (v4) edge[loop right] node[rotate=90, anchor=north] {$w_{0}\\mid w_{0}$} ();
            \\path[->] (v4.-118.69) edge node[rotate=56.31, anchor=north] {$w_{0}\\mid w_{0} w_{-2}$} (v0.51.31);
            \\path[->] (v2) edge[loop below] node {$w_{0}\\mid w_{0}$} ();
            \\path[->] (v2.-148.43) edge node[rotate=26.57, anchor=north] {$w_{0}\\mid w_{0} w_{-3}$} (v0.21.57);
            \\path[->] (v0.158.43) edge node[rotate=333.43, anchor=north] {$w_{0}\\mid w_{0} w_{0}$} (v1.328.43);
            \\path[->] (v0.128.69) edge node[rotate=303.69, anchor=north] {$w_{0}\\mid w_{0} w_{1}$} (v3.298.69);
            \\path[->] (v0.61.31) edge node[rotate=56.31, anchor=south] {$w_{0}\\mid w_{0} w_{2}$} (v4.231.31);
            \\path[->] (v0.31.57) edge node[rotate=26.57, anchor=south] {$w_{0}\\mid w_{0} w_{3}$} (v2.201.57);
            \\path[->] (v0) edge[loop below] node {$w_{0}\\mid w_{0}$} ();
            \\end{tikzpicture}
            sage: view(T) # not tested

        TESTS::

            sage: T.latex_options(format_state_label=\'Nothing\')
            Traceback (most recent call last):
            ...
            TypeError: format_state_label must be callable.
            sage: T.latex_options(format_letter=\'\')
            Traceback (most recent call last):
            ...
            TypeError: format_letter must be callable.
            sage: T.latex_options(format_transition_label=\'\')
            Traceback (most recent call last):
            ...
            TypeError: format_transition_label must be callable.
            sage: T.latex_options(loop_where=37)
            Traceback (most recent call last):
            ...
            TypeError: loop_where must be a callable or a
            dictionary.
            sage: T.latex_options(loop_where=lambda x: \'top\')
            Traceback (most recent call last):
            ...
            ValueError: loop_where for 4 must be in [\'above\',
            \'below\', \'left\', \'right\'].
            sage: T.latex_options(initial_where=90)
            Traceback (most recent call last):
            ...
            TypeError: initial_where must be a callable or a
            dictionary.
            sage: T.latex_options(initial_where=lambda x: \'top\')
            Traceback (most recent call last):
            ...
            ValueError: initial_where for 4 must be in [\'above\',
            \'below\', \'left\', \'right\'].
            sage: T.latex_options(accepting_style=\'fancy\')
            Traceback (most recent call last):
            ...
            ValueError: accepting_style must be in [\'accepting by
            arrow\', \'accepting by double\'].
            sage: T.latex_options(accepting_where=90)
            Traceback (most recent call last):
            ...
            TypeError: accepting_where must be a callable or a
            dictionary.
            sage: T.latex_options(accepting_where=lambda x: \'top\')
            Traceback (most recent call last):
            ...
            ValueError: accepting_where for 0 must be in [\'above\',
            \'below\', \'left\', \'right\'].
            sage: T.latex_options(accepting_where={0: \'above\', 3: \'top\'})
            Traceback (most recent call last):
            ...
            ValueError: accepting_where for 3 must be a real number or
            be in [\'above\', \'below\', \'left\', \'right\'].
        '''
    def set_coordinates(self, coordinates, default: bool = True) -> None:
        """
        Set coordinates of the states for the LaTeX representation by
        a dictionary or a function mapping labels to coordinates.

        INPUT:

        - ``coordinates`` -- dictionary or a function mapping labels
          of states to pairs interpreted as coordinates

        - ``default`` -- if ``True``, then states not given by
          ``coordinates`` get a default position on a circle of
          radius 3.

        OUTPUT: nothing

        EXAMPLES::

            sage: F = Automaton([[0, 1, 1], [1, 2, 2], [2, 0, 0]])
            sage: F.set_coordinates({0: (0, 0), 1: (2, 0), 2: (1, 1)})
            sage: F.state(0).coordinates
            (0, 0)

        We can also use a function to determine the coordinates::

            sage: F = Automaton([[0, 1, 1], [1, 2, 2], [2, 0, 0]])
            sage: F.set_coordinates(lambda l: (l, 3/(l+1)))
            sage: F.state(2).coordinates
            (2, 1)
        """
    def adjacency_matrix(self, input=None, entry=None):
        """
        Return the adjacency matrix of the underlying graph.

        INPUT:

        - ``input`` -- only transitions with input label ``input`` are
          respected

        - ``entry`` -- the function ``entry`` takes a transition and the
          return value is written in the matrix as the entry
          ``(transition.from_state, transition.to_state)``. The default
          value (``None``) of entry takes the variable ``x`` to the
          power of the sum of the output word of the transition.

        OUTPUT: a matrix

        If any label of a state is not an integer, the finite state
        machine is relabeled at the beginning.  If there are more than
        one transitions between two states, then the different return
        values of ``entry`` are added up.

        EXAMPLES::

            sage: B = FiniteStateMachine({0:{0:(0, 0), 'a':(1, 0)},
            ....:                         'a':{2:(0, 0), 3:(1, 0)},
            ....:                         2:{0:(1, 1), 4:(0, 0)},
            ....:                         3:{'a':(0, 1), 2:(1, 1)},
            ....:                         4:{4:(1, 1), 3:(0, 1)}},
            ....:                        initial_states=[0])
            sage: B.adjacency_matrix()                                                  # needs sage.symbolic
            [1 1 0 0 0]
            [0 0 1 1 0]
            [x 0 0 0 1]
            [0 x x 0 0]
            [0 0 0 x x]

        This is equivalent to::

            sage: matrix(B)                                                             # needs sage.symbolic
            [1 1 0 0 0]
            [0 0 1 1 0]
            [x 0 0 0 1]
            [0 x x 0 0]
            [0 0 0 x x]

        It is also possible to use other entries in the adjacency matrix::

            sage: B.adjacency_matrix(entry=(lambda transition: 1))
            [1 1 0 0 0]
            [0 0 1 1 0]
            [1 0 0 0 1]
            [0 1 1 0 0]
            [0 0 0 1 1]
            sage: var('t')                                                              # needs sage.symbolic
            t
            sage: B.adjacency_matrix(1, entry=(lambda transition:                       # needs sage.symbolic
            ....:     exp(I*transition.word_out[0]*t)))
            [      0       1       0       0       0]
            [      0       0       0       1       0]
            [e^(I*t)       0       0       0       0]
            [      0       0 e^(I*t)       0       0]
            [      0       0       0       0 e^(I*t)]
            sage: a = Automaton([(0, 1, 0),
            ....:                (1, 2, 0),
            ....:                (2, 0, 1),
            ....:                (2, 1, 0)],
            ....:               initial_states=[0],
            ....:               final_states=[0])
            sage: a.adjacency_matrix()                                                  # needs sage.symbolic
            [0 1 0]
            [0 0 1]
            [1 1 0]
        """
    def determine_input_alphabet(self, reset: bool = True) -> None:
        """
        Determine the input alphabet according to the transitions
        of this finite state machine.

        INPUT:

        - ``reset`` -- boolean (default: ``True``); if ``True``, then
          the existing input alphabet is erased, otherwise new letters are
          appended to the existing alphabet.

        OUTPUT: nothing

        After this operation the input alphabet of this finite state machine
        is a list of letters.

        .. TODO::

            At the moment, the letters of the alphabet need to be hashable.

        EXAMPLES::

            sage: T = Transducer([(1, 1, 1, 0), (1, 2, 2, 1),
            ....:                 (2, 2, 1, 1), (2, 2, 0, 0)],
            ....:                final_states=[1],
            ....:                determine_alphabets=False)
            sage: (T.input_alphabet, T.output_alphabet)
            (None, None)
            sage: T.determine_input_alphabet()
            sage: (T.input_alphabet, T.output_alphabet)
            ([0, 1, 2], None)

        .. SEEALSO::

           :meth:`determine_output_alphabet`,
           :meth:`determine_alphabets`.
        """
    def determine_output_alphabet(self, reset: bool = True) -> None:
        """
        Determine the output alphabet according to the transitions
        of this finite state machine.

        INPUT:

        - ``reset`` -- boolean (default: ``True``); if ``True``, then
          the existing output alphabet is erased, otherwise new letters are
          appended to the existing alphabet.

        OUTPUT: nothing

        After this operation the output alphabet of this finite state machine
        is a list of letters.

        .. TODO::

            At the moment, the letters of the alphabet need to be hashable.

        EXAMPLES::

            sage: T = Transducer([(1, 1, 1, 0), (1, 2, 2, 1),
            ....:                 (2, 2, 1, 1), (2, 2, 0, 0)],
            ....:                final_states=[1],
            ....:                determine_alphabets=False)
            sage: T.state(1).final_word_out = [1, 4]
            sage: (T.input_alphabet, T.output_alphabet)
            (None, None)
            sage: T.determine_output_alphabet()
            sage: (T.input_alphabet, T.output_alphabet)
            (None, [0, 1, 4])

        .. SEEALSO::

           :meth:`determine_input_alphabet`,
           :meth:`determine_alphabets`.
        """
    def determine_alphabets(self, reset: bool = True) -> None:
        """
        Determine the input and output alphabet according to the
        transitions in this finite state machine.

        INPUT:

        - ``reset`` -- if reset is ``True``, then the existing input
          and output alphabets are erased, otherwise new letters are
          appended to the existing alphabets.

        OUTPUT: nothing

        After this operation the input alphabet and the output
        alphabet of this finite state machine are a list of letters.

        .. TODO::

            At the moment, the letters of the alphabets need to be hashable.

        EXAMPLES::

            sage: T = Transducer([(1, 1, 1, 0), (1, 2, 2, 1),
            ....:                 (2, 2, 1, 1), (2, 2, 0, 0)],
            ....:                final_states=[1],
            ....:                determine_alphabets=False)
            sage: T.state(1).final_word_out = [1, 4]
            sage: (T.input_alphabet, T.output_alphabet)
            (None, None)
            sage: T.determine_alphabets()
            sage: (T.input_alphabet, T.output_alphabet)
            ([0, 1, 2], [0, 1, 4])

        .. SEEALSO::

           :meth:`determine_input_alphabet`,
           :meth:`determine_output_alphabet`.
        """
    def states(self):
        """
        Return the states of the finite state machine.

        OUTPUT: the states of the finite state machine as list

        EXAMPLES::

            sage: FSM = Automaton([('1', '2', 1), ('2', '2', 0)])
            sage: FSM.states()
            ['1', '2']
        """
    def iter_states(self):
        """
        Return an iterator of the states.

        OUTPUT: an iterator of the states of the finite state machine

        EXAMPLES::

            sage: FSM = Automaton([('1', '2', 1), ('2', '2', 0)])
            sage: [s.label() for s in FSM.iter_states()]
            ['1', '2']
        """
    def transitions(self, from_state=None):
        """
        Return a list of all transitions.

        INPUT:

        - ``from_state`` -- (default: ``None``) if ``from_state`` is
          given, then a list of transitions starting there is given

        OUTPUT: list of all transitions

        EXAMPLES::

            sage: FSM = Automaton([('1', '2', 1), ('2', '2', 0)])
            sage: FSM.transitions()
            [Transition from '1' to '2': 1|-,
             Transition from '2' to '2': 0|-]
        """
    def iter_transitions(self, from_state=None):
        """
        Return an iterator of all transitions.

        INPUT:

        - ``from_state`` -- (default: ``None``) if ``from_state`` is
          given, then a list of transitions starting there is given

        OUTPUT: an iterator of all transitions

        EXAMPLES::

            sage: FSM = Automaton([('1', '2', 1), ('2', '2', 0)])
            sage: [(t.from_state.label(), t.to_state.label())
            ....:     for t in FSM.iter_transitions('1')]
            [('1', '2')]
            sage: [(t.from_state.label(), t.to_state.label())
            ....:     for t in FSM.iter_transitions('2')]
            [('2', '2')]
            sage: [(t.from_state.label(), t.to_state.label())
            ....:     for t in FSM.iter_transitions()]
            [('1', '2'), ('2', '2')]
        """
    def initial_states(self):
        """
        Return a list of all initial states.

        EXAMPLES::

            sage: from sage.combinat.finite_state_machine import FSMState
            sage: A = FSMState('A', is_initial=True)
            sage: B = FSMState('B')
            sage: F = FiniteStateMachine([(A, B, 1, 0)])
            sage: F.initial_states()
            ['A']
        """
    def iter_initial_states(self):
        """
        Return an iterator of the initial states.

        OUTPUT: an iterator over all initial states

        EXAMPLES::

            sage: from sage.combinat.finite_state_machine import FSMState
            sage: A = FSMState('A', is_initial=True)
            sage: B = FSMState('B')
            sage: F = FiniteStateMachine([(A, B, 1, 0)])
            sage: [s.label() for s in F.iter_initial_states()]
            ['A']
        """
    def final_states(self):
        """
        Return a list of all final states.

        EXAMPLES::

            sage: from sage.combinat.finite_state_machine import FSMState
            sage: A = FSMState('A', is_final=True)
            sage: B = FSMState('B', is_initial=True)
            sage: C = FSMState('C', is_final=True)
            sage: F = FiniteStateMachine([(A, B), (A, C)])
            sage: F.final_states()
            ['A', 'C']
        """
    def iter_final_states(self):
        """
        Return an iterator of the final states.

        OUTPUT: an iterator over all initial states

        EXAMPLES::

            sage: from sage.combinat.finite_state_machine import FSMState
            sage: A = FSMState('A', is_final=True)
            sage: B = FSMState('B', is_initial=True)
            sage: C = FSMState('C', is_final=True)
            sage: F = FiniteStateMachine([(A, B), (A, C)])
            sage: [s.label() for s in F.iter_final_states()]
            ['A', 'C']
        """
    def state(self, state):
        """
        Return the state of the finite state machine.

        INPUT:

        - ``state`` -- if ``state`` is not an instance of
          :class:`FSMState`, then it is assumed that it is the label
          of a state.

        OUTPUT: the state of the finite state machine corresponding to ``state``

        If no state is found, then a :exc:`LookupError` is thrown.

        EXAMPLES::

            sage: from sage.combinat.finite_state_machine import FSMState
            sage: A = FSMState('A')
            sage: FSM = FiniteStateMachine([(A, 'B'), ('C', A)])
            sage: FSM.state('A') == A
            True
            sage: FSM.state('xyz')
            Traceback (most recent call last):
            ...
            LookupError: No state with label xyz found.
        """
    def transition(self, transition):
        """
        Return the transition of the finite state machine.

        INPUT:

        - ``transition`` -- if ``transition`` is not an instance of
          :class:`FSMTransition`, then it is assumed that it is a
          tuple ``(from_state, to_state, word_in, word_out)``

        OUTPUT: the transition of the finite state machine corresponding
        to ``transition``

        If no transition is found, then a :exc:`LookupError` is thrown.

        EXAMPLES::

            sage: from sage.combinat.finite_state_machine import FSMTransition
            sage: t = FSMTransition('A', 'B', 0)
            sage: F = FiniteStateMachine([t])
            sage: F.transition(('A', 'B', 0))
            Transition from 'A' to 'B': 0|-
            sage: id(t) == id(F.transition(('A', 'B', 0)))
            True
        """
    def has_state(self, state) -> bool:
        """
        Return whether ``state`` is one of the states of the finite
        state machine.

        INPUT:

        - ``state`` can be a :class:`FSMState` or a label of a state.

        OUTPUT: boolean

        EXAMPLES::

            sage: FiniteStateMachine().has_state('A')
            False
        """
    def has_transition(self, transition) -> bool:
        """
        Return whether ``transition`` is one of the transitions of
        the finite state machine.

        INPUT:

        - ``transition`` has to be a :class:`FSMTransition`.

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.combinat.finite_state_machine import FSMTransition
            sage: t = FSMTransition('A', 'A', 0, 1)
            sage: FiniteStateMachine().has_transition(t)
            False
            sage: FiniteStateMachine().has_transition(('A', 'A', 0, 1))
            Traceback (most recent call last):
            ...
            TypeError: Transition is not an instance of FSMTransition.
        """
    def has_initial_state(self, state) -> bool:
        """
        Return whether ``state`` is one of the initial states of the
        finite state machine.

        INPUT:

        - ``state`` can be a :class:`FSMState` or a label.

        OUTPUT: boolean

        EXAMPLES::

            sage: F = FiniteStateMachine([('A', 'A')], initial_states=['A'])
            sage: F.has_initial_state('A')
            True
        """
    def has_initial_states(self) -> bool:
        """
        Return whether the finite state machine has an initial state.

        OUTPUT: boolean

        EXAMPLES::

            sage: FiniteStateMachine().has_initial_states()
            False
        """
    def has_final_state(self, state) -> bool:
        """
        Return whether ``state`` is one of the final states of the
        finite state machine.

        INPUT:

        - ``state`` can be a :class:`FSMState` or a label.

        OUTPUT: boolean

        EXAMPLES::

            sage: FiniteStateMachine(final_states=['A']).has_final_state('A')
            True
        """
    def has_final_states(self) -> bool:
        """
        Return whether the finite state machine has a final state.

        OUTPUT: boolean

        EXAMPLES::

            sage: FiniteStateMachine().has_final_states()
            False
        """
    def is_deterministic(self):
        """
        Return whether the finite finite state machine is deterministic.

        OUTPUT: boolean

        A finite state machine is considered to be deterministic if
        each transition has input label of length one and for each
        pair `(q,a)` where `q` is a state and `a` is an element of the
        input alphabet, there is at most one transition from `q` with
        input label `a`. Furthermore, the finite state may not have
        more than one initial state.

        EXAMPLES::

            sage: fsm = FiniteStateMachine()
            sage: fsm.add_transition(('A', 'B', 0, []))
            Transition from 'A' to 'B': 0|-
            sage: fsm.is_deterministic()
            True
            sage: fsm.add_transition(('A', 'C', 0, []))
            Transition from 'A' to 'C': 0|-
            sage: fsm.is_deterministic()
            False
            sage: fsm.add_transition(('A', 'B', [0,1], []))
            Transition from 'A' to 'B': 0,1|-
            sage: fsm.is_deterministic()
            False

        Check that :issue:`18556` is fixed::

            sage: Automaton().is_deterministic()
            True
            sage: Automaton(initial_states=[0]).is_deterministic()
            True
            sage: Automaton(initial_states=[0, 1]).is_deterministic()
            False
        """
    def is_complete(self):
        """
        Return whether the finite state machine is complete.

        OUTPUT: boolean

        A finite state machine is considered to be complete if
        each transition has an input label of length one and for each
        pair `(q, a)` where `q` is a state and `a` is an element of the
        input alphabet, there is exactly one transition from `q` with
        input label `a`.

        EXAMPLES::

            sage: fsm = FiniteStateMachine([(0, 0, 0, 0),
            ....:                           (0, 1, 1, 1),
            ....:                           (1, 1, 0, 0)],
            ....:                          determine_alphabets=False)
            sage: fsm.is_complete()
            Traceback (most recent call last):
            ...
            ValueError: No input alphabet is given. Try calling determine_alphabets().
            sage: fsm.input_alphabet = [0, 1]
            sage: fsm.is_complete()
            False
            sage: fsm.add_transition((1, 1, 1, 1))
            Transition from 1 to 1: 1|1
            sage: fsm.is_complete()
            True
            sage: fsm.add_transition((0, 0, 1, 0))
            Transition from 0 to 0: 1|0
            sage: fsm.is_complete()
            False
        """
    def is_connected(self) -> None:
        """
        TESTS::

            sage: FiniteStateMachine().is_connected()
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def process(self, *args, **kwargs):
        """
        Return whether the finite state machine accepts the input, the state
        where the computation stops and which output is generated.

        INPUT:

        - ``input_tape`` -- the input tape can be a list or an
          iterable with entries from the input alphabet. If we are
          working with a multi-tape machine (see parameter
          ``use_multitape_input`` and notes below), then the tape is a
          list or tuple of tracks, each of which can be a list or an
          iterable with entries from the input alphabet.

        - ``initial_state`` or ``initial_states`` -- the initial
          state(s) in which the machine starts. Either specify a
          single one with ``initial_state`` or a list of them with
          ``initial_states``. If both are given, ``initial_state``
          will be appended to ``initial_states``. If neither is
          specified, the initial states of the finite state machine
          are taken.

        - ``list_of_outputs`` -- (default: ``None``) a boolean or
          ``None``. If ``True``, then the outputs are given in list form
          (even if we have no or only one single output). If
          ``False``, then the result is never a list (an exception is
          raised if the result cannot be returned). If
          ``list_of_outputs=None``, the method determines automatically
          what to do (e.g. if a non-deterministic machine returns more
          than one path, then the output is returned in list form).

        - ``only_accepted`` -- boolean (default: ``False``); if set, then the
          first argument in the output is guaranteed to be ``True`` (if the
          output is a list, then the first argument of each element will be
          ``True``)

        - ``always_include_output`` -- if set (not by default), always
          include the output. This is inconsequential for a
          :class:`FiniteStateMachine`, but can be used in derived
          classes where the output is suppressed by default,
          cf. :meth:`Automaton.process`.

        - ``format_output`` -- a function that translates the written
          output (which is in form of a list) to something more
          readable. By default (``None``) identity is used here.

        - ``check_epsilon_transitions`` -- boolean (default: ``True``); if
          ``False``, then epsilon transitions are not taken into consideration
          during process

        - ``write_final_word_out`` -- boolean (default: ``True``); whether the
          final output words should be written or not

        - ``use_multitape_input`` -- boolean (default: ``False``); if ``True``,
          then the multi-tape mode of the process iterator is activated. See
          also the notes below for multi-tape machines.

        - ``process_all_prefixes_of_input`` -- boolean (default: ``False``); if
          ``True``, then each prefix of the input word is processed (instead of
          processing the whole input word at once). Consequently, there is an
          output generated for each of these prefixes.

        - ``process_iterator_class`` -- (default: ``None``) a class
          inherited from :class:`FSMProcessIterator`. If ``None``,
          then :class:`FSMProcessIterator` is taken. An instance of this
          class is created and is used during the processing.

        - ``automatic_output_type`` -- boolean (default: ``False``); if set and
          the input has a parent, then the output will have the same parent. If
          the input does not have a parent, then the output will be of the same
          type as the input.

        OUTPUT:

        A triple (or a list of triples,
        cf. parameter ``list_of_outputs``), where

        - the first entry is ``True`` if the input string is accepted,

        - the second gives the reached state after processing the
          input tape (This is a state with label ``None`` if the input
          could not be processed, i.e., if at one point no
          transition to go on could be found.), and

        - the third gives a list of the output labels written during
          processing (in the case the finite state machine runs as
          transducer).

        Note that in the case the finite state machine is not
        deterministic, all possible paths are taken into account.

        This function uses an iterator which, in its simplest form, goes
        from one state to another in each step. To decide which way to
        go, it uses the input words of the outgoing transitions and
        compares them to the input tape. More precisely, in each step,
        the iterator takes an outgoing transition of the current state,
        whose input label equals the input letter of the tape. The
        output label of the transition, if present, is written on the
        output tape.

        If the choice of the outgoing transition is not unique (i.e.,
        we have a non-deterministic finite state machine), all
        possibilities are followed. This is done by splitting the
        process into several branches, one for each of the possible
        outgoing transitions.

        The process (iteration) stops if all branches are finished,
        i.e., for no branch, there is any transition whose input word
        coincides with the processed input tape. This can simply
        happen when the entire tape was read.

        Also see :meth:`~FiniteStateMachine.__call__` for a version of
        :meth:`.process` with shortened output.

        Internally this function creates and works with an instance of
        :class:`FSMProcessIterator`. This iterator can also be obtained
        with :meth:`iter_process`.

        If working with multi-tape finite state machines, all input
        words of transitions are words of `k`-tuples of letters.
        Moreover, the input tape has to consist of `k` tracks, i.e.,
        be a list or tuple of `k` iterators, one for each track.

        .. WARNING::

            Working with multi-tape finite state machines is still
            experimental and can lead to wrong outputs.

        EXAMPLES::

            sage: binary_inverter = FiniteStateMachine({'A': [('A', 0, 1), ('A', 1, 0)]},
            ....:                                      initial_states=['A'], final_states=['A'])
            sage: binary_inverter.process([0, 1, 0, 0, 1, 1])
            (True, 'A', [1, 0, 1, 1, 0, 0])

        Alternatively, we can invoke this function by::

            sage: binary_inverter([0, 1, 0, 0, 1, 1])
            (True, 'A', [1, 0, 1, 1, 0, 0])

        Below we construct a finite state machine which tests if an input
        is a non-adjacent form, i.e., no two neighboring letters are
        both nonzero (see also the example on
        :ref:`non-adjacent forms <finite_state_machine_recognizing_NAFs_example>`
        in the documentation of the module
        :doc:`finite_state_machine`)::

            sage: NAF = FiniteStateMachine(
            ....:     {'_': [('_', 0), (1, 1)], 1: [('_', 0)]},
            ....:     initial_states=['_'], final_states=['_', 1])
            sage: [NAF.process(w)[0] for w in [[0], [0, 1], [1, 1], [0, 1, 0, 1],
            ....:                           [0, 1, 1, 1, 0], [1, 0, 0, 1, 1]]]
            [True, True, False, True, False, False]

        Working only with the first component (i.e., returning whether
        accepted or not) usually corresponds to using the more
        specialized class :class:`Automaton`.

        Non-deterministic finite state machines can be handled as well.

        ::

            sage: T = Transducer([(0, 1, 0, 0), (0, 2, 0, 0)],
            ....:     initial_states=[0])
            sage: T.process([0])
            [(False, 1, [0]), (False, 2, [0])]

        Here is another non-deterministic finite state machine. Note
        that we use ``format_output`` (see
        :class:`FSMProcessIterator`) to convert the written outputs
        (all characters) to strings.

        ::

            sage: T = Transducer([(0, 1, [0, 0], 'a'), (0, 2, [0, 0, 1], 'b'),
            ....:                 (0, 1, 1, 'c'), (1, 0, [], 'd'),
            ....:                 (1, 1, 1, 'e')],
            ....:                initial_states=[0], final_states=[0, 1])
            sage: T.process([0], format_output=lambda o: ''.join(o))
            (False, None, None)
            sage: T.process([0, 0], format_output=lambda o: ''.join(o))
            [(True, 0, 'ad'), (True, 1, 'a')]
            sage: T.process([1], format_output=lambda o: ''.join(o))
            [(True, 0, 'cd'), (True, 1, 'c')]
            sage: T.process([1, 1], format_output=lambda o: ''.join(o))
            [(True, 0, 'cdcd'), (True, 0, 'ced'),
             (True, 1, 'cdc'), (True, 1, 'ce')]
            sage: T.process([0, 0, 1], format_output=lambda o: ''.join(o))
            [(False, 2, 'b'),
             (True, 0, 'adcd'),
             (True, 0, 'aed'),
             (True, 1, 'adc'),
             (True, 1, 'ae')]
            sage: T.process([0, 0, 1], format_output=lambda o: ''.join(o),
            ....:           only_accepted=True)
            [(True, 0, 'adcd'), (True, 0, 'aed'),
             (True, 1, 'adc'), (True, 1, 'ae')]

        A simple example of a multi-tape finite state machine is the
        following: It writes the length of the first tape many letters
        ``a`` and then the length of the second tape many letters
        ``b``::

            sage: M = FiniteStateMachine([(0, 0, (1, None), 'a'),
            ....:                         (0, 1, [], []),
            ....:                         (1, 1, (None, 1), 'b')],
            ....:                        initial_states=[0],
            ....:                        final_states=[1])
            sage: M.process(([1, 1], [1]), use_multitape_input=True)
            (True, 1, ['a', 'a', 'b'])

        .. SEEALSO::

            :meth:`Automaton.process`,
            :meth:`Transducer.process`,
            :meth:`~FiniteStateMachine.iter_process`,
            :meth:`~FiniteStateMachine.__call__`,
            :class:`FSMProcessIterator`.

        TESTS::

            sage: T = Transducer([(0, 1, [0, 0], 0), (0, 2, [0, 0, 1], 0),
            ....:                 (0, 1, 1, 2), (1, 0, [], 1), (1, 1, 1, 3)],
            ....:     initial_states=[0], final_states=[0, 1])
            sage: T.process([0])
            (False, None, None)
            sage: T.process([0, 0])
            [(True, 0, [0, 1]), (True, 1, [0])]
            sage: T.process([1])
            [(True, 0, [2, 1]), (True, 1, [2])]
            sage: T.process([1, 1])
            [(True, 0, [2, 1, 2, 1]), (True, 0, [2, 3, 1]),
             (True, 1, [2, 1, 2]), (True, 1, [2, 3])]

        ::

            sage: F = FiniteStateMachine([(0, 0, 0, 0)],
            ....:                        initial_states=[0])
            sage: F.process([0], only_accepted=True)
            []
            sage: F.process([0], only_accepted=True, list_of_outputs=False)
            Traceback (most recent call last):
            ...
            ValueError: No accepting output was found but according to the
            given options, an accepting output should be returned. Change
            only_accepted and/or list_of_outputs options.
            sage: F.process([0], only_accepted=True, list_of_outputs=True)
            []
            sage: F.process([0], only_accepted=False)
            (False, 0, [0])
            sage: F.process([0], only_accepted=False, list_of_outputs=False)
            (False, 0, [0])
            sage: F.process([0], only_accepted=False, list_of_outputs=True)
            [(False, 0, [0])]
            sage: F.process([1], only_accepted=True)
            []
            sage: F.process([1], only_accepted=True, list_of_outputs=False)
            Traceback (most recent call last):
            ...
            ValueError: No accepting output was found but according to the
            given options, an accepting output should be returned. Change
            only_accepted and/or list_of_outputs options.
            sage: F.process([1], only_accepted=True, list_of_outputs=True)
            []
            sage: F.process([1], only_accepted=False)
            (False, None, None)
            sage: F.process([1], only_accepted=False, list_of_outputs=False)
            (False, None, None)
            sage: F.process([1], only_accepted=False, list_of_outputs=True)
            []

        ::

            sage: F = FiniteStateMachine([(0, 1, 1, 'a'), (0, 2, 2, 'b')],
            ....:                        initial_states=[0],
            ....:                        final_states=[1])
            sage: A = Automaton([(0, 1, 1), (0, 2, 2)],
            ....:               initial_states=[0],
            ....:               final_states=[1])
            sage: T = Transducer([(0, 1, 1, 'a'), (0, 2, 2, 'b')],
            ....:                initial_states=[0],
            ....:                final_states=[1])
            sage: F.process([1])
            (True, 1, ['a'])
            sage: A.process([1])
            (True, 1)
            sage: T.process([1])
            (True, 1, ['a'])
            sage: F.process([2])
            (False, 2, ['b'])
            sage: A.process([2])
            (False, 2)
            sage: T.process([2])
            (False, 2, ['b'])
            sage: F.process([3])
            (False, None, None)
            sage: A.process([3])
            (False, None)
            sage: T.process([3])
            (False, None, None)
        """
    def iter_process(self, input_tape=None, initial_state=None, process_iterator_class=None, iterator_type=None, automatic_output_type: bool = False, **kwargs):
        """
        This function returns an iterator for processing the input.
        See :meth:`.process` (which runs this iterator until the end)
        for more information.

        INPUT:

        - ``iterator_type`` -- if ``None`` (default), then
          an instance of :class:`FSMProcessIterator` is returned. If
          this is ``'simple'`` only an iterator over one output is
          returned (an exception is raised if this is not the case, i.e.,
          if the process has branched).

        See :meth:`process` for a description of the other parameters.

        OUTPUT: an iterator

        EXAMPLES:

        We can use :meth:`iter_process` to deal with infinite words::

            sage: inverter = Transducer({'A': [('A', 0, 1), ('A', 1, 0)]},
            ....:     initial_states=['A'], final_states=['A'])

            sage: # needs sage.combinat
            sage: words.FibonacciWord()
            word: 0100101001001010010100100101001001010010...
            sage: it = inverter.iter_process(
            ....:     words.FibonacciWord(), iterator_type='simple')
            sage: Words([0,1])(it)
            word: 1011010110110101101011011010110110101101...

        This can also be done by::

            sage: inverter.iter_process(words.FibonacciWord(),                          # needs sage.combinat
            ....:                       iterator_type='simple',
            ....:                       automatic_output_type=True)
            word: 1011010110110101101011011010110110101101...

        or even simpler by::

            sage: inverter(words.FibonacciWord())                                       # needs sage.combinat
            word: 1011010110110101101011011010110110101101...

        To see what is going on, we use :meth:`iter_process` without
        arguments::

            sage: # needs sage.combinat
            sage: from itertools import islice
            sage: it = inverter.iter_process(words.FibonacciWord())
            sage: for current in islice(it, 4r):
            ....:     print(current)
            process (1 branch)
            + at state 'A'
            +-- tape at 1, [[1]]
            process (1 branch)
            + at state 'A'
            +-- tape at 2, [[1, 0]]
            process (1 branch)
            + at state 'A'
            +-- tape at 3, [[1, 0, 1]]
            process (1 branch)
            + at state 'A'
            +-- tape at 4, [[1, 0, 1, 1]]

        The following show the difference between using the ``'simple'``-option
        and not using it. With this option, we have
        ::

            sage: it = inverter.iter_process(input_tape=[0, 1, 1],
            ....:                            iterator_type='simple')
            sage: for i, o in enumerate(it):
            ....:     print('step %s: output %s' % (i, o))
            step 0: output 1
            step 1: output 0
            step 2: output 0

        So :meth:`iter_process` is a generator expression which gives
        a new output letter in each step (and not more). In many cases
        this is sufficient.

        Doing the same without the ``'simple'``-option does not give
        the output directly; it has to be extracted first. On the
        other hand, additional information is presented::

            sage: it = inverter.iter_process(input_tape=[0, 1, 1])
            sage: for current in it:
            ....:     print(current)
            process (1 branch)
            + at state 'A'
            +-- tape at 1, [[1]]
            process (1 branch)
            + at state 'A'
            +-- tape at 2, [[1, 0]]
            process (1 branch)
            + at state 'A'
            +-- tape at 3, [[1, 0, 0]]
            process (0 branches)
            sage: it.result()
            [Branch(accept=True, state='A', output=[1, 0, 0])]

        One can see the growing of the output (the list of lists at
        the end of each entry).

        Even if the transducer has transitions with empty or multiletter
        output, the simple iterator returns one new output letter in
        each step::

            sage: T = Transducer([(0, 0, 0, []),
            ....:                 (0, 0, 1, [1]),
            ....:                 (0, 0, 2, [2, 2])],
            ....:                initial_states=[0])
            sage: it = T.iter_process(input_tape=[0, 1, 2, 0, 1, 2],
            ....:                     iterator_type='simple')
            sage: for i, o in enumerate(it):
            ....:     print('step %s: output %s' % (i, o))
            step 0: output 1
            step 1: output 2
            step 2: output 2
            step 3: output 1
            step 4: output 2
            step 5: output 2

        .. SEEALSO::

            :meth:`FiniteStateMachine.process`,
            :meth:`Automaton.process`,
            :meth:`Transducer.process`,
            :meth:`~FiniteStateMachine.__call__`,
            :class:`FSMProcessIterator`.
        """
    def add_state(self, state):
        """
        Add a state to the finite state machine and returns the new
        state. If the state already exists, that existing state is
        returned.

        INPUT:

        - ``state`` is either an instance of
          :class:`FSMState` or,
          otherwise, a label of a state.

        OUTPUT: the new or existing state

        EXAMPLES::

            sage: from sage.combinat.finite_state_machine import FSMState
            sage: F = FiniteStateMachine()
            sage: A = FSMState('A', is_initial=True)
            sage: F.add_state(A)
            'A'
        """
    def add_states(self, states) -> None:
        """
        Add several states. See add_state for more information.

        INPUT:

        - ``states`` -- list of states or iterator over states

        OUTPUT: nothing

        EXAMPLES::

            sage: F = FiniteStateMachine()
            sage: F.add_states(['A', 'B'])
            sage: F.states()
            ['A', 'B']
        """
    def add_transition(self, *args, **kwargs):
        """
        Add a transition to the finite state machine and returns the
        new transition.

        If the transition already exists, the return value of
        ``self.on_duplicate_transition`` is returned. See the
        documentation of :class:`FiniteStateMachine`.

        INPUT:

        The following forms are all accepted:

        ::

            sage: from sage.combinat.finite_state_machine import FSMState, FSMTransition
            sage: A = FSMState('A')
            sage: B = FSMState('B')

            sage: FSM = FiniteStateMachine()
            sage: FSM.add_transition(FSMTransition(A, B, 0, 1))
            Transition from 'A' to 'B': 0|1

            sage: FSM = FiniteStateMachine()
            sage: FSM.add_transition(A, B, 0, 1)
            Transition from 'A' to 'B': 0|1

            sage: FSM = FiniteStateMachine()
            sage: FSM.add_transition(A, B, word_in=0, word_out=1)
            Transition from 'A' to 'B': 0|1

            sage: FSM = FiniteStateMachine()
            sage: FSM.add_transition('A', 'B', {'word_in': 0, 'word_out': 1})
            Transition from 'A' to 'B': {'word_in': 0, 'word_out': 1}|-

            sage: FSM = FiniteStateMachine()
            sage: FSM.add_transition(from_state=A, to_state=B,
            ....:                    word_in=0, word_out=1)
            Transition from 'A' to 'B': 0|1

            sage: FSM = FiniteStateMachine()
            sage: FSM.add_transition({'from_state': A, 'to_state': B,
            ....:                    'word_in': 0, 'word_out': 1})
            Transition from 'A' to 'B': 0|1

            sage: FSM = FiniteStateMachine()
            sage: FSM.add_transition((A, B, 0, 1))
            Transition from 'A' to 'B': 0|1

            sage: FSM = FiniteStateMachine()
            sage: FSM.add_transition([A, B, 0, 1])
            Transition from 'A' to 'B': 0|1

        If the states ``A`` and ``B`` are not instances of
        :class:`FSMState`, then it is assumed that they are labels of
        states.

        OUTPUT:

        The new transition.
        """
    def add_from_transition_function(self, function, initial_states=None, explore_existing_states: bool = True) -> None:
        """
        Construct a finite state machine from a transition function.

        INPUT:

        - ``function`` may return a tuple (new_state, output_word) or a
          list of such tuples

        - ``initial_states`` -- if no initial states are given, the
          already existing initial states of ``self`` are taken

        - ``explore_existing_states`` -- boolean (default: ``True``); if
          ``True`` (default), then already existing states in ``self`` (e.g.
          already given final states) will also be processed if they are
          reachable from the initial statess

        OUTPUT: nothing

        EXAMPLES::

            sage: F = FiniteStateMachine(initial_states=['A'],
            ....:                        input_alphabet=[0, 1])
            sage: def f(state, input):
            ....:     return [('A', input), ('B', 1-input)]
            sage: F.add_from_transition_function(f)
            sage: F.transitions()
            [Transition from 'A' to 'A': 0|0,
            Transition from 'A' to 'B': 0|1,
            Transition from 'A' to 'A': 1|1,
            Transition from 'A' to 'B': 1|0,
            Transition from 'B' to 'A': 0|0,
            Transition from 'B' to 'B': 0|1,
            Transition from 'B' to 'A': 1|1,
            Transition from 'B' to 'B': 1|0]

        Initial states can also be given as a parameter::

            sage: F = FiniteStateMachine(input_alphabet=[0,1])
            sage: def f(state, input):
            ....:     return [('A', input), ('B', 1-input)]
            sage: F.add_from_transition_function(f,initial_states=['A'])
            sage: F.initial_states()
            ['A']

        Already existing states in the finite state machine (the final
        states in the example below) are also explored::

            sage: F = FiniteStateMachine(initial_states=[0],
            ....:                        final_states=[1],
            ....:                        input_alphabet=[0])
            sage: def transition_function(state, letter):
            ....:     return 1 - state, []
            sage: F.add_from_transition_function(transition_function)
            sage: F.transitions()
            [Transition from 0 to 1: 0|-,
             Transition from 1 to 0: 0|-]

        If ``explore_existing_states=False``, however, this behavior
        is turned off, i.e., already existing states are not
        explored::

            sage: F = FiniteStateMachine(initial_states=[0],
            ....:                        final_states=[1],
            ....:                        input_alphabet=[0])
            sage: def transition_function(state, letter):
            ....:     return 1 - state, []
            sage: F.add_from_transition_function(transition_function,
            ....:                                explore_existing_states=False)
            sage: F.transitions()
            [Transition from 0 to 1: 0|-]

        TESTS::

            sage: F = FiniteStateMachine(initial_states=['A'])
            sage: def f(state, input):
            ....:     return [('A', input), ('B', 1-input)]
            sage: F.add_from_transition_function(f)
            Traceback (most recent call last):
            ...
            ValueError: No input alphabet is given.
            Try calling determine_alphabets().

        ::

            sage: def transition(state, where):
            ....:     return (vector([0, 0]), 1)
            sage: Transducer(transition, input_alphabet=[0], initial_states=[0])
            Traceback (most recent call last):
            ...
            TypeError: mutable vectors are unhashable
        """
    def add_transitions_from_function(self, function, labels_as_input: bool = True) -> None:
        """
        Add one or more transitions if ``function(state, state)``
        says that there are some.

        INPUT:

        - ``function`` -- a transition function. Given two states
          ``from_state`` and ``to_state`` (or their labels if
          ``label_as_input`` is true), this function shall return a
          tuple ``(word_in, word_out)`` to add a transition from
          ``from_state`` to ``to_state`` with input and output labels
          ``word_in`` and ``word_out``, respectively. If no such
          addition is to be added, the transition function shall
          return ``None``. The transition function may also return
          a list of such tuples in order to add multiple transitions
          between the pair of states.

        - ``label_as_input`` -- (default: ``True``)

        OUTPUT: nothing

        EXAMPLES::

            sage: F = FiniteStateMachine()
            sage: F.add_states(['A', 'B', 'C'])
            sage: def f(state1, state2):
            ....:     if state1 == 'C':
            ....:         return None
            ....:     return (0, 1)
            sage: F.add_transitions_from_function(f)
            sage: len(F.transitions())
            6

        Multiple transitions are also possible::

            sage: F = FiniteStateMachine()
            sage: F.add_states([0, 1])
            sage: def f(state1, state2):
            ....:     if state1 != state2:
            ....:          return [(0, 1), (1, 0)]
            ....:     else:
            ....:          return None
            sage: F.add_transitions_from_function(f)
            sage: F.transitions()
            [Transition from 0 to 1: 0|1,
             Transition from 0 to 1: 1|0,
             Transition from 1 to 0: 0|1,
             Transition from 1 to 0: 1|0]

        TESTS::

            sage: F = FiniteStateMachine()
            sage: F.add_state(0)
            0
            sage: def f(state1, state2):
            ....:     return 1
            sage: F.add_transitions_from_function(f)
            Traceback (most recent call last):
            ...
            ValueError: The callback function for add_transitions_from_function
            is expected to return a pair (word_in, word_out) or a list of such
            pairs. For states 0 and 0 however, it returned 1,
            which is not acceptable.
        """
    def delete_transition(self, t) -> None:
        """
        Delete a transition by removing it from the list of transitions of
        the state, where the transition starts.

        INPUT:

        - ``t`` -- a transition

        OUTPUT: nothing

        EXAMPLES::

            sage: F = FiniteStateMachine([('A', 'B', 0), ('B', 'A', 1)])
            sage: F.delete_transition(('A', 'B', 0))
            sage: F.transitions()
            [Transition from 'B' to 'A': 1|-]
        """
    def delete_state(self, s) -> None:
        """
        Delete a state and all transitions coming or going to this state.

        INPUT:

        - ``s`` -- a label of a state or an :class:`FSMState`

        OUTPUT: nothing

        EXAMPLES::

            sage: from sage.combinat.finite_state_machine import FSMTransition
            sage: t1 = FSMTransition('A', 'B', 0)
            sage: t2 = FSMTransition('B', 'B', 1)
            sage: F = FiniteStateMachine([t1, t2])
            sage: F.delete_state('A')
            sage: F.transitions()
            [Transition from 'B' to 'B': 1|-]

        TESTS:

        This shows that :issue:`16024` is fixed. ::

            sage: F._states_
            ['B']
            sage: F._states_dict_
            {'B': 'B'}
        """
    def remove_epsilon_transitions(self) -> None:
        """
        TESTS::

            sage: FiniteStateMachine().remove_epsilon_transitions()
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def epsilon_successors(self, state):
        """
        Return the dictionary with states reachable from ``state``
        without reading anything from an input tape as keys. The
        values are lists of outputs.

        INPUT:

        - ``state`` -- the state whose epsilon successors should be
          determined

        OUTPUT: a dictionary mapping states to a list of output words

        The states in the output are the epsilon successors of
        ``state``. Each word of the list of output words is a word
        written when taking a path from ``state`` to the corresponding
        state.

        EXAMPLES::

            sage: T = Transducer([(0, 1, None, 'a'), (1, 2, None, 'b')])
            sage: T.epsilon_successors(0)
            {1: [['a']], 2: [['a', 'b']]}
            sage: T.epsilon_successors(1)
            {2: [['b']]}
            sage: T.epsilon_successors(2)
            {}

        If there is a cycle with only epsilon transitions, then this
        cycle is only processed once and there is no infinite loop::

            sage: S = Transducer([(0, 1, None, 'a'), (1, 0, None, 'b')])
            sage: S.epsilon_successors(0)
            {0: [['a', 'b']], 1: [['a']]}
            sage: S.epsilon_successors(1)
            {0: [['b']], 1: [['b', 'a']]}
        """
    def accessible_components(self):
        """
        Return a new finite state machine with the accessible states
        of ``self`` and all transitions between those states.

        OUTPUT:

        A finite state machine with the accessible states of ``self`` and
        all transitions between those states.

        A state is accessible if there is a directed path from an
        initial state to the state. If ``self`` has no initial states then
        a copy of the finite state machine ``self`` is returned.

        EXAMPLES::

            sage: F = Automaton([(0, 0, 0), (0, 1, 1), (1, 1, 0), (1, 0, 1)],
            ....:               initial_states=[0])
            sage: F.accessible_components()
            Automaton with 2 states

        ::

            sage: F = Automaton([(0, 0, 1), (0, 0, 1), (1, 1, 0), (1, 0, 1)],
            ....:               initial_states=[0])
            sage: F.accessible_components()
            Automaton with 1 state

        .. SEEALSO::
            :meth:`coaccessible_components`

        TESTS:

        Check whether input of length > 1 works::

            sage: F = Automaton([(0, 1, [0, 1]), (0, 2, 0)],
            ....:               initial_states=[0])
            sage: F.accessible_components()
            Automaton with 3 states
        """
    def coaccessible_components(self):
        """
        Return the sub-machine induced by the coaccessible states of this
        finite state machine.

        OUTPUT:

        A finite state machine of the same type as this finite state
        machine.

        EXAMPLES::

            sage: A = automata.ContainsWord([1, 1],
            ....:     input_alphabet=[0, 1]).complement().minimization().relabeled()
            sage: A.transitions()
            [Transition from 0 to 0: 0|-,
             Transition from 0 to 0: 1|-,
             Transition from 1 to 2: 0|-,
             Transition from 1 to 0: 1|-,
             Transition from 2 to 2: 0|-,
             Transition from 2 to 1: 1|-]
            sage: A.initial_states()
            [2]
            sage: A.final_states()
            [1, 2]
            sage: C = A.coaccessible_components()
            sage: C.transitions()
            [Transition from 1 to 2: 0|-,
             Transition from 2 to 2: 0|-,
             Transition from 2 to 1: 1|-]

        .. SEEALSO::
            :meth:`accessible_components`,
            :meth:`induced_sub_finite_state_machine`
        """
    def disjoint_union(self, other):
        """
        Return the disjoint union of this and another finite state
        machine.

        INPUT:

        -   ``other`` -- a :class:`FiniteStateMachine`

        OUTPUT:

        A finite state machine of the same type as this finite state
        machine.

        In general, the disjoint union of two finite state machines is
        non-deterministic. In the case of a automata, the language
        accepted by the disjoint union is the union of the languages
        accepted by the constituent automata. In the case of
        transducer, for each successful path in one of the constituent
        transducers, there will be one successful path with the same input
        and output labels in the disjoint union.

        The labels of the states of the disjoint union are pairs ``(i,
        s)``: for each state ``s`` of this finite state machine, there
        is a state ``(0, s)`` in the disjoint union; for each state
        ``s`` of the other finite state machine, there is a state ``(1,
        s)`` in the disjoint union.

        The input alphabet is the union of the input alphabets (if
        possible) and ``None`` otherwise. In the latter case, try
        calling :meth:`.determine_alphabets`.

        The disjoint union can also be written as ``A + B`` or ``A | B``.

        EXAMPLES::

            sage: A = Automaton([(0, 1, 0), (1, 0, 1)],
            ....:               initial_states=[0],
            ....:               final_states=[0])
            sage: A([0, 1, 0, 1])
            True
            sage: B = Automaton([(0, 1, 0), (1, 2, 0), (2, 0, 1)],
            ....:               initial_states=[0],
            ....:               final_states=[0])
            sage: B([0, 0, 1])
            True
            sage: C = A.disjoint_union(B)
            sage: C
            Automaton with 5 states
            sage: C.transitions()
            [Transition from (0, 0) to (0, 1): 0|-,
             Transition from (0, 1) to (0, 0): 1|-,
             Transition from (1, 0) to (1, 1): 0|-,
             Transition from (1, 1) to (1, 2): 0|-,
             Transition from (1, 2) to (1, 0): 1|-]
            sage: C([0, 0, 1])
            True
            sage: C([0, 1, 0, 1])
            True
            sage: C([1])
            False
            sage: C.initial_states()
            [(0, 0), (1, 0)]

        Instead of ``.disjoint_union``, alternative notations are
        available::

            sage: C1 = A + B
            sage: C1 == C
            True
            sage: C2 = A | B
            sage: C2 == C
            True

        In general, the disjoint union is not deterministic.::

            sage: C.is_deterministic()
            False
            sage: D = C.determinisation().minimization()
            sage: D.is_equivalent(Automaton([(0, 0, 0), (0, 0, 1),
            ....:    (1, 7, 0), (1, 0, 1), (2, 6, 0), (2, 0, 1),
            ....:    (3, 5, 0), (3, 0, 1), (4, 0, 0), (4, 2, 1),
            ....:    (5, 0, 0), (5, 3, 1), (6, 4, 0), (6, 0, 1),
            ....:    (7, 4, 0), (7, 3, 1)],
            ....:    initial_states=[1],
            ....:    final_states=[1, 2, 3]))
            True

        Disjoint union of transducers::

            sage: T1 = Transducer([(0, 0, 0, 1)],
            ....:                 initial_states=[0],
            ....:                 final_states=[0])
            sage: T2 = Transducer([(0, 0, 0, 2)],
            ....:                 initial_states=[0],
            ....:                 final_states=[0])
            sage: T1([0])
            [1]
            sage: T2([0])
            [2]
            sage: T = T1.disjoint_union(T2)
            sage: T([0])
            Traceback (most recent call last):
            ...
            ValueError: Found more than one accepting path.
            sage: T.process([0])
            [(True, (0, 0), [1]), (True, (1, 0), [2])]

        Handling of the input alphabet (see :issue:`18989`)::

            sage: A = Automaton([(0, 0, 0)])
            sage: B = Automaton([(0, 0, 1)], input_alphabet=[1, 2])
            sage: C = Automaton([(0, 0, 2)], determine_alphabets=False)
            sage: D = Automaton([(0, 0, [[0, 0]])], input_alphabet=[[0, 0]])
            sage: A.input_alphabet
            [0]
            sage: B.input_alphabet
            [1, 2]
            sage: C.input_alphabet is None
            True
            sage: D.input_alphabet
            [[0, 0]]
            sage: (A + B).input_alphabet
            [0, 1, 2]
            sage: (A + C).input_alphabet is None
            True
            sage: (A + D).input_alphabet is None
            True

        .. SEEALSO::

            :meth:`Automaton.intersection`,
            :meth:`Transducer.intersection`,
            :meth:`.determine_alphabets`.
        """
    def concatenation(self, other):
        """
        Concatenate this finite state machine with another finite
        state machine.

        INPUT:

        - ``other`` -- a :class:`FiniteStateMachine`

        OUTPUT:

        A :class:`FiniteStateMachine` of the same type as this finite
        state machine.

        Assume that both finite state machines are automata. If
        `\\mathcal{L}_1` is the language accepted by this automaton and
        `\\mathcal{L}_2` is the language accepted by the other automaton,
        then the language accepted by the concatenated automaton is
        `\\{ w_1w_2 \\mid w_1\\in\\mathcal{L}_1, w_2\\in\\mathcal{L}_2\\}` where
        `w_1w_2` denotes the concatenation of the words `w_1` and `w_2`.

        Assume that both finite state machines are transducers and that
        this transducer maps words `w_1\\in\\mathcal{L}_1` to words
        `f_1(w_1)` and that the other transducer maps words
        `w_2\\in\\mathcal{L}_2` to words `f_2(w_2)`. Then the concatenated
        transducer maps words `w_1w_2` with `w_1\\in\\mathcal{L}_1` and
        `w_2\\in\\mathcal{L}_2` to `f_1(w_1)f_2(w_2)`. Here, `w_1w_2` and
        `f_1(w_1)f_2(w_2)` again denote concatenation of words.

        The input alphabet is the union of the input alphabets (if
        possible) and ``None`` otherwise. In the latter case, try
        calling :meth:`.determine_alphabets`.

        Instead of ``A.concatenation(B)``, the notation ``A * B`` can be
        used.

        EXAMPLES:

        Concatenation of two automata::

            sage: A = automata.Word([0])
            sage: B = automata.Word([1])
            sage: C = A.concatenation(B)
            sage: C.transitions()
            [Transition from (0, 0) to (0, 1): 0|-,
             Transition from (0, 1) to (1, 0): -|-,
             Transition from (1, 0) to (1, 1): 1|-]
            sage: [w
            ....:  for w in ([0, 0], [0, 1], [1, 0], [1, 1])
            ....:  if C(w)]
            [[0, 1]]
            sage: from sage.combinat.finite_state_machine import (
            ....:     Automaton, Transducer)
            sage: isinstance(C, Automaton)
            True

        Concatenation of two transducers::

            sage: A = Transducer([(0, 1, 0, 1), (0, 1, 1, 2)],
            ....:                initial_states=[0],
            ....:                final_states=[1])
            sage: B = Transducer([(0, 1, 0, 1), (0, 1, 1, 0)],
            ....:                initial_states=[0],
            ....:                final_states=[1])
            sage: C = A.concatenation(B)
            sage: C.transitions()
            [Transition from (0, 0) to (0, 1): 0|1,
             Transition from (0, 0) to (0, 1): 1|2,
             Transition from (0, 1) to (1, 0): -|-,
             Transition from (1, 0) to (1, 1): 0|1,
             Transition from (1, 0) to (1, 1): 1|0]
            sage: [(w, C(w)) for w in ([0, 0], [0, 1], [1, 0], [1, 1])]
            [([0, 0], [1, 1]),
             ([0, 1], [1, 0]),
             ([1, 0], [2, 1]),
             ([1, 1], [2, 0])]
            sage: isinstance(C, Transducer)
            True


        Alternative notation as multiplication::

            sage: C == A * B
            True

        Final output words are taken into account::

            sage: A = Transducer([(0, 1, 0, 1)],
            ....:                initial_states=[0],
            ....:                final_states=[1])
            sage: A.state(1).final_word_out = 2
            sage: B = Transducer([(0, 1, 0, 3)],
            ....:                initial_states=[0],
            ....:                final_states=[1])
            sage: B.state(1).final_word_out = 4
            sage: C = A * B
            sage: C([0, 0])
            [1, 2, 3, 4]

        Handling of the input alphabet::

            sage: A = Automaton([(0, 0, 0)])
            sage: B = Automaton([(0, 0, 1)], input_alphabet=[1, 2])
            sage: C = Automaton([(0, 0, 2)], determine_alphabets=False)
            sage: D = Automaton([(0, 0, [[0, 0]])], input_alphabet=[[0, 0]])
            sage: A.input_alphabet
            [0]
            sage: B.input_alphabet
            [1, 2]
            sage: C.input_alphabet is None
            True
            sage: D.input_alphabet
            [[0, 0]]
            sage: (A * B).input_alphabet
            [0, 1, 2]
            sage: (A * C).input_alphabet is None
            True
            sage: (A * D).input_alphabet is None
            True

        .. SEEALSO::

            :meth:`~.disjoint_union`,
            :meth:`.determine_alphabets`.

        TESTS::

            sage: A = Automaton()
            sage: F = FiniteStateMachine()
            sage: A * F
            Traceback (most recent call last):
            ...
            TypeError: Cannot concatenate finite state machines of
            different types.
            sage: F * A
            Traceback (most recent call last):
            ...
            TypeError: Cannot concatenate finite state machines of
            different types.
            sage: F * 5
            Traceback (most recent call last):
            ...
            TypeError: A finite state machine can only be concatenated
            with a another finite state machine.
        """
    __mul__ = concatenation
    def kleene_star(self):
        '''
        Compute the Kleene closure of this finite state machine.

        OUTPUT:

        A :class:`FiniteStateMachine` of the same type as this finite
        state machine.

        Assume that this finite state machine is an automaton
        recognizing the language `\\mathcal{L}`.  Then the Kleene star
        recognizes the language `\\mathcal{L}^*=\\{ w_1\\ldots w_n \\mid
        n\\ge 0, w_j\\in\\mathcal{L} \\text{ for all } j\\}`.

        Assume that this finite state machine is a transducer realizing
        a function `f` on some alphabet `\\mathcal{L}`. Then the Kleene
        star realizes a function `g` on `\\mathcal{L}^*` with
        `g(w_1\\ldots w_n)=f(w_1)\\ldots f(w_n)`.

        EXAMPLES:

        Kleene star of an automaton::

            sage: A = automata.Word([0, 1])
            sage: B = A.kleene_star()
            sage: B.transitions()
            [Transition from 0 to 1: 0|-,
             Transition from 2 to 0: -|-,
             Transition from 1 to 2: 1|-]
            sage: from sage.combinat.finite_state_machine import (
            ....:     is_Automaton, is_Transducer)
            sage: isinstance(B, Automaton)
            True
            sage: [w for w in ([], [0, 1], [0, 1, 0], [0, 1, 0, 1], [0, 1, 1, 1])
            ....:  if B(w)]
            [[],
             [0, 1],
             [0, 1, 0, 1]]

        Kleene star of a transducer::

            sage: T = Transducer([(0, 1, 0, 1), (0, 1, 1, 0)],
            ....:                initial_states=[0],
            ....:                final_states=[1])
            sage: S = T.kleene_star()
            sage: S.transitions()
            [Transition from 0 to 1: 0|1,
             Transition from 0 to 1: 1|0,
             Transition from 1 to 0: -|-]
            sage: isinstance(S, Transducer)
            True
            sage: for w in ([], [0], [1], [0, 0], [0, 1]):
            ....:     print("{} {}".format(w, S.process(w)))
            []     (True, 0, [])
            [0]    [(True, 0, [1]), (True, 1, [1])]
            [1]    [(True, 0, [0]), (True, 1, [0])]
            [0, 0] [(True, 0, [1, 1]), (True, 1, [1, 1])]
            [0, 1] [(True, 0, [1, 0]), (True, 1, [1, 0])]

        Final output words are taken into account::

            sage: T = Transducer([(0, 1, 0, 1)],
            ....:                initial_states=[0],
            ....:                final_states=[1])
            sage: T.state(1).final_word_out = 2
            sage: S = T.kleene_star()
            sage: sorted(S.process([0, 0]))
            [(True, 0, [1, 2, 1, 2]), (True, 1, [1, 2, 1, 2])]

        Final output words may lead to undesirable situations if initial
        states and final states coincide::

            sage: T = Transducer(initial_states=[0], final_states=[0])
            sage: T.state(0).final_word_out = 1
            sage: T([])
            [1]
            sage: S = T.kleene_star()
            sage: S([])
            Traceback (most recent call last):
            ...
            RuntimeError: State 0 is in an epsilon cycle (no input), but
            output is written.
        '''
    def intersection(self, other) -> None:
        """
        TESTS::

            sage: FiniteStateMachine().intersection(FiniteStateMachine())
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def product_FiniteStateMachine(self, other, function, new_input_alphabet=None, only_accessible_components: bool = True, final_function=None, new_class=None):
        """
        Return a new finite state machine whose states are
        `d`-tuples of states of the original finite state machines.

        INPUT:

        - ``other`` -- a finite state machine (for `d=2`) or a list
          (or iterable) of `d-1` finite state machines

        - ``function`` has to accept `d` transitions from `A_j` to `B_j`
          for `j\\in\\{1, \\ldots, d\\}` and returns a pair ``(word_in, word_out)``
          which is the label of the transition `A=(A_1, \\ldots, A_d)` to `B=(B_1,
          \\ldots, B_d)`. If there is no transition from `A` to `B`,
          then ``function`` should raise a :exc:`LookupError`.

        - ``new_input_alphabet`` -- (optional) the new input alphabet
          as a list

        - ``only_accessible_components`` -- if ``True`` (default), then
          the result is piped through :meth:`.accessible_components`. If no
          ``new_input_alphabet`` is given, it is determined by
          :meth:`.determine_alphabets`.

        - ``final_function`` -- a function mapping `d` final states of
          the original finite state machines to the final output of
          the corresponding state in the new finite state machine. By
          default, the final output is the empty word if both final
          outputs of the constituent states are empty; otherwise, a
          :exc:`ValueError` is raised.

        - ``new_class`` -- class of the new finite state machine. By
          default (``None``), the class of ``self`` is used

        OUTPUT:

        A finite state machine whose states are `d`-tuples of states of the
        original finite state machines. A state is initial or
        final if all constituent states are initial or final,
        respectively.

        The labels of the transitions are defined by ``function``.

        The final output of a final state is determined by calling
        ``final_function`` on the constituent states.

        The color of a new state is the tuple of colors of the
        constituent states of ``self`` and ``other``. However,
        if all constituent states have color ``None``, then
        the state has color ``None``, too.

        EXAMPLES::

            sage: F = Automaton([('A', 'B', 1), ('A', 'A', 0), ('B', 'A', 2)],
            ....:               initial_states=['A'], final_states=['B'],
            ....:               determine_alphabets=True)
            sage: G = Automaton([(1, 1, 1)], initial_states=[1], final_states=[1])
            sage: def addition(transition1, transition2):
            ....:     return (transition1.word_in[0] + transition2.word_in[0],
            ....:             None)
            sage: H = F.product_FiniteStateMachine(G, addition, [0, 1, 2, 3], only_accessible_components=False)
            sage: H.transitions()
            [Transition from ('A', 1) to ('B', 1): 2|-,
             Transition from ('A', 1) to ('A', 1): 1|-,
             Transition from ('B', 1) to ('A', 1): 3|-]
            sage: [s.color for s in H.iter_states()]
            [None, None]
            sage: H1 = F.product_FiniteStateMachine(G, addition, [0, 1, 2, 3], only_accessible_components=False)
            sage: H1.states()[0].label()[0] is F.states()[0]
            True
            sage: H1.states()[0].label()[1] is G.states()[0]
            True

        ::

            sage: F = Automaton([(0,1,1/4), (0,0,3/4), (1,1,3/4), (1,0,1/4)],
            ....:                initial_states=[0] )
            sage: G = Automaton([(0,0,1), (1,1,3/4), (1,0,1/4)],
            ....:                initial_states=[0] )
            sage: H = F.product_FiniteStateMachine(
            ....:         G, lambda t1,t2: (t1.word_in[0]*t2.word_in[0], None))
            sage: H.states()
            [(0, 0), (1, 0)]

        ::

            sage: F = Automaton([(0,1,1/4), (0,0,3/4), (1,1,3/4), (1,0,1/4)],
            ....:                initial_states=[0] )
            sage: G = Automaton([(0,0,1), (1,1,3/4), (1,0,1/4)],
            ....:                initial_states=[0] )
            sage: H = F.product_FiniteStateMachine(G,
            ....:                                  lambda t1,t2: (t1.word_in[0]*t2.word_in[0], None),
            ....:                                  only_accessible_components=False)
            sage: H.states()
            [(0, 0), (1, 0), (0, 1), (1, 1)]

        Also final output words are considered according to the function
        ``final_function``::

            sage: F = Transducer([(0, 1, 0, 1), (1, 1, 1, 1), (1, 1, 0, 1)],
            ....:                final_states=[1])
            sage: F.state(1).final_word_out = 1
            sage: G = Transducer([(0, 0, 0, 1), (0, 0, 1, 0)], final_states=[0])
            sage: G.state(0).final_word_out = 1
            sage: def minus(t1, t2):
            ....:     return (t1.word_in[0] - t2.word_in[0],
            ....:                t1.word_out[0] - t2.word_out[0])
            sage: H = F.product_FiniteStateMachine(G, minus)
            Traceback (most recent call last):
            ...
            ValueError: A final function must be given.
            sage: def plus(s1, s2):
            ....:     return s1.final_word_out[0] + s2.final_word_out[0]
            sage: H = F.product_FiniteStateMachine(G, minus,
            ....:                                  final_function=plus)
            sage: H.final_states()
            [(1, 0)]
            sage: H.final_states()[0].final_word_out
            [2]

        Products of more than two finite state machines are also possible::

            sage: def plus(s1, s2, s3):
            ....:     if s1.word_in == s2.word_in == s3.word_in:
            ....:          return (s1.word_in,
            ....:                  sum(s.word_out[0] for s in (s1, s2, s3)))
            ....:     else:
            ....:         raise LookupError
            sage: T0 = transducers.CountSubblockOccurrences([0, 0], [0, 1, 2])
            sage: T1 = transducers.CountSubblockOccurrences([1, 1], [0, 1, 2])
            sage: T2 = transducers.CountSubblockOccurrences([2, 2], [0, 1, 2])
            sage: T = T0.product_FiniteStateMachine([T1, T2], plus)
            sage: T.transitions()
            [Transition from ((), (), ()) to ((0,), (), ()): 0|0,
             Transition from ((), (), ()) to ((), (1,), ()): 1|0,
             Transition from ((), (), ()) to ((), (), (2,)): 2|0,
             Transition from ((0,), (), ()) to ((0,), (), ()): 0|1,
             Transition from ((0,), (), ()) to ((), (1,), ()): 1|0,
             Transition from ((0,), (), ()) to ((), (), (2,)): 2|0,
             Transition from ((), (1,), ()) to ((0,), (), ()): 0|0,
             Transition from ((), (1,), ()) to ((), (1,), ()): 1|1,
             Transition from ((), (1,), ()) to ((), (), (2,)): 2|0,
             Transition from ((), (), (2,)) to ((0,), (), ()): 0|0,
             Transition from ((), (), (2,)) to ((), (1,), ()): 1|0,
             Transition from ((), (), (2,)) to ((), (), (2,)): 2|1]
            sage: T([0, 0, 1, 1, 2, 2, 0, 1, 2, 2])
            [0, 1, 0, 1, 0, 1, 0, 0, 0, 1]

        ``other`` can also be an iterable::

            sage: T == T0.product_FiniteStateMachine(iter([T1, T2]), plus)
            True

        TESTS:

        Check that colors are correctly dealt with. In particular, the
        new colors have to be hashable such that
        :meth:`Automaton.determinisation` does not fail::

            sage: A = Automaton([[0, 0, 0]], initial_states=[0])
            sage: B = A.product_FiniteStateMachine(A,
            ....:                                  lambda t1, t2: (0, None))
            sage: B.states()[0].color is None
            True
            sage: B.determinisation()
            Automaton with 1 state

        Check handling of the parameter ``other``::

            sage: A.product_FiniteStateMachine(None, plus)
            Traceback (most recent call last):
            ...
            ValueError: other must be a finite state machine or a list
            of finite state machines.
            sage: A.product_FiniteStateMachine([None], plus)
            Traceback (most recent call last):
            ...
            ValueError: other must be a finite state machine or a list
            of finite state machines.

        Test whether ``new_class`` works::

            sage: T = Transducer()
            sage: type(T.product_FiniteStateMachine(T, None))
            <class 'sage.combinat.finite_state_machine.Transducer'>
            sage: type(T.product_FiniteStateMachine(T, None,
            ....:      new_class=Automaton))
            <class 'sage.combinat.finite_state_machine.Automaton'>

        Check that isolated vertices are kept (:issue:`16762`)::

            sage: F = Transducer(initial_states=[0])
            sage: F.add_state(1)
            1
            sage: G = Transducer(initial_states=['A'])
            sage: F.product_FiniteStateMachine(G, None).states()
            [(0, 'A')]
            sage: F.product_FiniteStateMachine(
            ....:     G, None, only_accessible_components=False).states()
            [(0, 'A'), (1, 'A')]
        """
    def composition(self, other, algorithm=None, only_accessible_components: bool = True):
        '''
        Return a new transducer which is the composition of ``self``
        and ``other``.

        INPUT:

        - ``other`` -- a transducer

        - ``algorithm`` -- can be one of the following

          - ``direct`` -- the composition is calculated directly

            There can be arbitrarily many initial and final states,
            but the input and output labels must have length `1`.

            .. WARNING::

                The output of ``other`` is fed into ``self``.

          - ``explorative`` -- an explorative algorithm is used

            The input alphabet of ``self`` has to be specified.

            .. WARNING::

                The output of ``other`` is fed into ``self``.

          If algorithm is ``None``, then the algorithm is chosen
          automatically (at the moment always ``direct``, except when
          there are output words of ``other`` or input words of ``self``
          of length greater than `1`).

        OUTPUT: a new transducer

        The labels of the new finite state machine are pairs of states
        of the original finite state machines. The color of a new
        state is the tuple of colors of the constituent states.

        EXAMPLES::

            sage: F = Transducer([(\'A\', \'B\', 1, 0), (\'B\', \'A\', 0, 1)],
            ....:                initial_states=[\'A\', \'B\'], final_states=[\'B\'],
            ....:                determine_alphabets=True)
            sage: G = Transducer([(1, 1, 1, 0), (1, 2, 0, 1),
            ....:                 (2, 2, 1, 1), (2, 2, 0, 0)],
            ....:                initial_states=[1], final_states=[2],
            ....:                determine_alphabets=True)
            sage: Hd = F.composition(G, algorithm=\'direct\')
            sage: Hd.initial_states()
            [(1, \'B\'), (1, \'A\')]
            sage: Hd.transitions()
            [Transition from (1, \'B\') to (1, \'A\'): 1|1,
             Transition from (1, \'A\') to (2, \'B\'): 0|0,
             Transition from (2, \'B\') to (2, \'A\'): 0|1,
             Transition from (2, \'A\') to (2, \'B\'): 1|0]
            sage: He = F.composition(G, algorithm=\'explorative\')
            sage: He.initial_states()
            [(1, \'A\'), (1, \'B\')]
            sage: He.transitions()
            [Transition from (1, \'A\') to (2, \'B\'): 0|0,
             Transition from (1, \'B\') to (1, \'A\'): 1|1,
             Transition from (2, \'B\') to (2, \'A\'): 0|1,
             Transition from (2, \'A\') to (2, \'B\'): 1|0]
            sage: Hd == He
            True

        The following example has output of length `> 1`, so the
        explorative algorithm has to be used (and is selected
        automatically).

        ::

            sage: F = Transducer([(\'A\', \'B\', 1, [1, 0]), (\'B\', \'B\', 1, 1),
            ....:                 (\'B\', \'B\', 0, 0)],
            ....:                initial_states=[\'A\'], final_states=[\'B\'])
            sage: G = Transducer([(1, 1, 0, 0), (1, 2, 1, 0),
            ....:                 (2, 2, 0, 1), (2, 1, 1, 1)],
            ....:                initial_states=[1], final_states=[1])
            sage: He = G.composition(F, algorithm=\'explorative\')
            sage: He.transitions()
            [Transition from (\'A\', 1) to (\'B\', 2): 1|0,1,
             Transition from (\'B\', 2) to (\'B\', 2): 0|1,
             Transition from (\'B\', 2) to (\'B\', 1): 1|1,
             Transition from (\'B\', 1) to (\'B\', 1): 0|0,
             Transition from (\'B\', 1) to (\'B\', 2): 1|0]
            sage: Ha = G.composition(F)
            sage: Ha == He
            True

        Final output words are also considered::

            sage: F = Transducer([(\'A\', \'B\', 1, 0), (\'B\', \'A\', 0, 1)],
            ....:                initial_states=[\'A\', \'B\'],
            ....:                final_states=[\'A\', \'B\'])
            sage: F.state(\'A\').final_word_out = 0
            sage: F.state(\'B\').final_word_out = 1
            sage: G = Transducer([(1, 1, 1, 0), (1, 2, 0, 1),
            ....:                 (2, 2, 1, 1), (2, 2, 0, 0)],
            ....:                initial_states=[1], final_states=[2])
            sage: G.state(2).final_word_out = 0
            sage: Hd = F.composition(G, algorithm=\'direct\')
            sage: Hd.final_states()
            [(2, \'B\')]
            sage: He = F.composition(G, algorithm=\'explorative\')
            sage: He.final_states()
            [(2, \'B\')]

        Note that ``(2, \'A\')`` is not final, as the final output `0`
        of state `2` of `G` cannot be processed in state ``\'A\'`` of
        `F`.

        ::

            sage: [s.final_word_out for s in Hd.final_states()]
            [[1, 0]]
            sage: [s.final_word_out for s in He.final_states()]
            [[1, 0]]
            sage: Hd == He
            True

        Here is a non-deterministic example with intermediate output
        length `>1`.

        ::

            sage: F = Transducer([(1, 1, 1, [\'a\', \'a\']), (1, 2, 1, \'b\'),
            ....:                 (2, 1, 2, \'a\'), (2, 2, 2, \'b\')],
            ....:                initial_states=[1, 2])
            sage: G = Transducer([(\'A\', \'A\', \'a\', \'i\'),
            ....:                 (\'A\', \'B\', \'a\', \'l\'),
            ....:                 (\'B\', \'B\', \'b\', \'e\')],
            ....:                initial_states=[\'A\', \'B\'])
            sage: G(F).transitions()
            [Transition from (1, \'A\') to (1, \'A\'): 1|\'i\',\'i\',
             Transition from (1, \'A\') to (1, \'B\'): 1|\'i\',\'l\',
             Transition from (1, \'B\') to (2, \'B\'): 1|\'e\',
             Transition from (2, \'A\') to (1, \'A\'): 2|\'i\',
             Transition from (2, \'A\') to (1, \'B\'): 2|\'l\',
             Transition from (2, \'B\') to (2, \'B\'): 2|\'e\']

        Be aware that after composition, different transitions may
        share the same output label (same python object)::

            sage: F = Transducer([ (\'A\',\'B\',0,0), (\'B\',\'A\',0,0)],
            ....:                initial_states=[\'A\'],
            ....:                final_states=[\'A\'])
            sage: F.transitions()[0].word_out is F.transitions()[1].word_out
            False
            sage: G = Transducer([(\'C\',\'C\',0,1)],
            ....:                initial_states=[\'C\'],
            ....:                final_states=[\'C\'])
            sage: H = G.composition(F)
            sage: H.transitions()[0].word_out is H.transitions()[1].word_out
            True

        TESTS:

        In the explorative algorithm, transducers with non-empty final
        output words are implemented in :issue:`16548`::

            sage: A = transducers.GrayCode()
            sage: B = transducers.abs([0, 1])
            sage: A.composition(B, algorithm=\'explorative\').transitions()
            [Transition from (0, 0) to (0, 1): 0|-,
             Transition from (0, 0) to (0, 2): 1|-,
             Transition from (0, 1) to (0, 1): 0|0,
             Transition from (0, 1) to (0, 2): 1|1,
             Transition from (0, 2) to (0, 1): 0|1,
             Transition from (0, 2) to (0, 2): 1|0]

        Similarly, the explorative algorithm can handle
        non-deterministic finite state machines as of :issue:`16548`::

            sage: A = Transducer([(0, 0, 0, 0), (0, 1, 0, 0)],
            ....:                initial_states=[0])
            sage: B = transducers.Identity([0])
            sage: A.composition(B, algorithm=\'explorative\').transitions()
            [Transition from (0, 0) to (0, 0): 0|0,
             Transition from (0, 0) to (0, 1): 0|0]
            sage: B.composition(A, algorithm=\'explorative\').transitions()
            [Transition from (0, 0) to (0, 0): 0|0,
             Transition from (0, 0) to (1, 0): 0|0]

        In the following example, ``algorithm=\'direct\'`` is inappropriate
        as there are edges with output labels of length greater than 1::

            sage: F = Transducer([(\'A\', \'B\', 1, [1, 0]), (\'B\', \'B\', 1, 1),
            ....:                 (\'B\', \'B\', 0, 0)],
            ....:                initial_states=[\'A\'], final_states=[\'B\'])
            sage: G = Transducer([(1, 1, 0, 0), (1, 2, 1, 0),
            ....:                 (2, 2, 0, 1), (2, 1, 1, 1)],
            ....:                initial_states=[1], final_states=[1])
            sage: Hd = G.composition(F, algorithm=\'direct\')

        In the following examples, we compose transducers and automata
        and check whether the types are correct.

        ::

            sage: from sage.combinat.finite_state_machine import (
            ....:     is_Automaton, is_Transducer)
            sage: T = Transducer([(0, 0, 0, 0)], initial_states=[0])
            sage: A = Automaton([(0, 0, 0)], initial_states=[0])
            sage: isinstance(T.composition(T, algorithm=\'direct\'), Transducer)
            True
            sage: isinstance(T.composition(T, algorithm=\'explorative\'), Transducer)
            True
            sage: T.composition(A, algorithm=\'direct\')
            Traceback (most recent call last):
            ...
            TypeError: Composition with automaton is not possible.
            sage: T.composition(A, algorithm=\'explorative\')
            Traceback (most recent call last):
            ...
            TypeError: Composition with automaton is not possible.
            sage: A.composition(A, algorithm=\'direct\')
            Traceback (most recent call last):
            ...
            TypeError: Composition with automaton is not possible.
            sage: A.composition(A, algorithm=\'explorative\')
            Traceback (most recent call last):
            ...
            TypeError: Composition with automaton is not possible.
            sage: isinstance(A.composition(T, algorithm=\'direct\'), Automaton)
            True
            sage: isinstance(A.composition(T, algorithm=\'explorative\'), Automaton)
            True

        Non-deterministic final output cannot be handled::

            sage: F = Transducer([(\'I\', \'A\', 0, 42), (\'I\', \'B\', 0, 42)],
            ....:                initial_states=[\'I\'],
            ....:                final_states=[\'A\', \'B\'])
            sage: G = Transducer(initial_states=[0],
            ....:                final_states=[0],
            ....:                input_alphabet=[0])
            sage: G.state(0).final_word_out = 0
            sage: H = F.composition(G, algorithm=\'explorative\')
            sage: for s in H.final_states():
            ....:     print("{} {}".format(s, s.final_word_out))
            (0, \'I\') [42]
            sage: F.state(\'A\').final_word_out = \'a\'
            sage: F.state(\'B\').final_word_out = \'b\'
            sage: F.composition(G, algorithm=\'explorative\')
            Traceback (most recent call last):
            ...
            NotImplementedError: Stopping in state (0, \'I\') leads to
            non-deterministic final output.

        Check that the output and input alphabets are set correctly::

            sage: F = Transducer([(0, 0, 1, \'A\')],
            ....:                initial_states=[0],
            ....:                determine_alphabets=False)
            sage: G = Transducer([(2, 2, \'A\', \'a\')],
            ....:                initial_states=[2],
            ....:                determine_alphabets=False)
            sage: Hd = G(F, algorithm=\'direct\')
            sage: Hd.input_alphabet, Hd.output_alphabet
            ([1], [\'a\'])
            sage: He = G(F, algorithm=\'explorative\')
            Traceback (most recent call last):
            ...
            ValueError: No input alphabet is given. Try calling
            determine_alphabets().
            sage: F.input_alphabet = [1]
            sage: Hd = G(F, algorithm=\'direct\')
            sage: Hd.input_alphabet, Hd.output_alphabet
            ([1], [\'a\'])
            sage: He = G(F, algorithm=\'explorative\')
            sage: He.input_alphabet, He.output_alphabet
            ([1], None)
            sage: G.output_alphabet = [\'a\']
            sage: Hd = G(F, algorithm=\'direct\')
            sage: Hd.input_alphabet, Hd.output_alphabet
            ([1], [\'a\'])
            sage: He = G(F, algorithm=\'explorative\')
            sage: He.input_alphabet, He.output_alphabet
            ([1], [\'a\'])
            sage: Hd == He
            True
            sage: F.input_alphabet = None
            sage: Hd = G(F, algorithm=\'direct\')
            sage: Hd.input_alphabet, Hd.output_alphabet
            ([1], [\'a\'])
            sage: He = G(F, algorithm=\'explorative\')
            Traceback (most recent call last):
            ...
            ValueError: No input alphabet is given. Try calling
            determine_alphabets().
        '''
    def input_projection(self):
        """
        Return an automaton where the output of each transition of
        ``self`` is deleted.

        OUTPUT: an automaton

        EXAMPLES::

            sage: F = FiniteStateMachine([('A', 'B', 0, 1), ('A', 'A', 1, 1),
            ....:                         ('B', 'B', 1, 0)])
            sage: G = F.input_projection()
            sage: G.transitions()
            [Transition from 'A' to 'B': 0|-,
             Transition from 'A' to 'A': 1|-,
             Transition from 'B' to 'B': 1|-]
        """
    def output_projection(self):
        """
        Return a automaton where the input of each transition of self
        is deleted and the new input is the original output.

        OUTPUT: an automaton

        EXAMPLES::

            sage: F = FiniteStateMachine([('A', 'B', 0, 1), ('A', 'A', 1, 1),
            ....:                         ('B', 'B', 1, 0)])
            sage: G = F.output_projection()
            sage: G.transitions()
            [Transition from 'A' to 'B': 1|-,
             Transition from 'A' to 'A': 1|-,
             Transition from 'B' to 'B': 0|-]

        Final output words are also considered correctly::

            sage: H = Transducer([('A', 'B', 0, 1), ('A', 'A', 1, 1),
            ....:                 ('B', 'B', 1, 0), ('A', ('final', 0), 0, 0)],
            ....:                final_states=['A', 'B'])
            sage: H.state('B').final_word_out = 2
            sage: J = H.output_projection()
            sage: J.states()
            ['A', 'B', ('final', 0), ('final', 1)]
            sage: J.transitions()
            [Transition from 'A' to 'B': 1|-,
             Transition from 'A' to 'A': 1|-,
             Transition from 'A' to ('final', 0): 0|-,
             Transition from 'B' to 'B': 0|-,
             Transition from 'B' to ('final', 1): 2|-]
            sage: J.final_states()
            ['A', ('final', 1)]
        """
    def projection(self, what: str = 'input'):
        """
        Return an Automaton which transition labels are the projection
        of the transition labels of the input.

        INPUT:

        - ``what`` -- (default: ``input``) either ``input`` or ``output``

        OUTPUT: an automaton

        EXAMPLES::

            sage: F = FiniteStateMachine([('A', 'B', 0, 1), ('A', 'A', 1, 1),
            ....:                         ('B', 'B', 1, 0)])
            sage: G = F.projection(what='output')
            sage: G.transitions()
            [Transition from 'A' to 'B': 1|-,
             Transition from 'A' to 'A': 1|-,
             Transition from 'B' to 'B': 0|-]
        """
    def transposition(self, reverse_output_labels: bool = True):
        """
        Return a new finite state machine, where all transitions of the
        input finite state machine are reversed.

        INPUT:

        - ``reverse_output_labels`` -- boolean (default: ``True``); whether to
          reverse output labels

        EXAMPLES::

            sage: aut = Automaton([('A', 'A', 0), ('A', 'A', 1), ('A', 'B', 0)],
            ....:                 initial_states=['A'], final_states=['B'])
            sage: aut.transposition().transitions('B')
            [Transition from 'B' to 'A': 0|-]

        ::

            sage: aut = Automaton([('1', '1', 1), ('1', '2', 0), ('2', '2', 0)],
            ....:                 initial_states=['1'], final_states=['1', '2'])
            sage: aut.transposition().initial_states()
            ['1', '2']

        ::

            sage: A = Automaton([(0, 1, [1, 0])],
            ....:     initial_states=[0],
            ....:     final_states=[1])
            sage: A([1, 0])
            True
            sage: A.transposition()([0, 1])
            True

        ::

            sage: T = Transducer([(0, 1, [1, 0], [1, 0])],
            ....:     initial_states=[0],
            ....:     final_states=[1])
            sage: T([1, 0])
            [1, 0]
            sage: T.transposition()([0, 1])
            [0, 1]
            sage: T.transposition(reverse_output_labels=False)([0, 1])
            [1, 0]


        TESTS:

        If a final state of ``self`` has a non-empty final output word,
        transposition is not implemented::

            sage: T = Transducer([('1', '1', 1, 0), ('1', '2', 0, 1),
            ....:                 ('2', '2', 0, 2)],
            ....:                 initial_states=['1'],
            ....:                 final_states=['1', '2'])
            sage: T.state('1').final_word_out = [2, 5]
            sage: T.transposition()
            Traceback (most recent call last):
            ...
            NotImplementedError: Transposition for transducers with
            final output words is not implemented.
        """
    def split_transitions(self):
        """
        Return a new transducer, where all transitions in ``self`` with input
        labels consisting of more than one letter
        are replaced by a path of the corresponding length.

        OUTPUT: a new transducer

        EXAMPLES::

            sage: A = Transducer([('A', 'B', [1, 2, 3], 0)],
            ....:                initial_states=['A'], final_states=['B'])
            sage: A.split_transitions().states()
            [('A', ()), ('B', ()),
             ('A', (1,)), ('A', (1, 2))]
        """
    def final_components(self):
        """
        Return the final components of a finite state machine as finite
        state machines.

        OUTPUT:

        A list of finite state machines, each representing a final
        component of ``self``.

        A final component of a transducer ``T`` is a strongly connected
        component ``C`` such that there are no transitions of ``T``
        leaving ``C``.

        The final components are the only parts of a transducer which
        influence the main terms of the asymptotic behaviour of the sum
        of output labels of a transducer, see [HKP2015]_ and [HKW2015]_.

        EXAMPLES::

            sage: T = Transducer([['A', 'B', 0, 0], ['B', 'C', 0, 1],
            ....:                 ['C', 'B', 0, 1], ['A', 'D', 1, 0],
            ....:                 ['D', 'D', 0, 0], ['D', 'B', 1, 0],
            ....:                 ['A', 'E', 2, 0], ['E', 'E', 0, 0]])
            sage: FC = T.final_components()
            sage: sorted(FC[0].transitions())
            [Transition from 'B' to 'C': 0|1,
             Transition from 'C' to 'B': 0|1]
            sage: FC[1].transitions()
            [Transition from 'E' to 'E': 0|0]

        Another example (cycle of length 2)::

            sage: T = Automaton([[0, 1, 0], [1, 0, 0]])
            sage: len(T.final_components()) == 1
            True
            sage: T.final_components()[0].transitions()
            [Transition from 0 to 1: 0|-,
             Transition from 1 to 0: 0|-]
        """
    def completion(self, sink=None):
        """
        Return a completion of this finite state machine.

        INPUT:

        - ``sink`` -- either an instance of :class:`FSMState` or a label
          for the sink (default: ``None``); if ``None``, the least
          available nonzero integer is used

        OUTPUT:

        A :class:`FiniteStateMachine` of the same type as this finite
        state machine.

        The resulting finite state machine is a complete version of this
        finite state machine.  A finite state machine is considered to
        be complete if each transition has an input label of length one
        and for each pair `(q, a)` where `q` is a state and `a` is an
        element of the input alphabet, there is exactly one transition
        from `q` with input label `a`.

        If this finite state machine is already complete, a deep copy is
        returned. Otherwise, a new non-final state (usually called a
        sink) is created and transitions to this sink are introduced as
        appropriate.

        EXAMPLES::

            sage: F = FiniteStateMachine([(0, 0, 0, 0),
            ....:                         (0, 1, 1, 1),
            ....:                         (1, 1, 0, 0)])
            sage: F.is_complete()
            False
            sage: G1 = F.completion()
            sage: G1.is_complete()
            True
            sage: G1.transitions()
            [Transition from 0 to 0: 0|0,
             Transition from 0 to 1: 1|1,
             Transition from 1 to 1: 0|0,
             Transition from 1 to 2: 1|-,
             Transition from 2 to 2: 0|-,
             Transition from 2 to 2: 1|-]
            sage: G2 = F.completion('Sink')
            sage: G2.is_complete()
            True
            sage: G2.transitions()
            [Transition from 0 to 0: 0|0,
             Transition from 0 to 1: 1|1,
             Transition from 1 to 1: 0|0,
             Transition from 1 to 'Sink': 1|-,
             Transition from 'Sink' to 'Sink': 0|-,
             Transition from 'Sink' to 'Sink': 1|-]
            sage: F.completion(1)
            Traceback (most recent call last):
            ...
            ValueError: The finite state machine already contains a state
            '1'.

        An input alphabet must be given::

            sage: F = FiniteStateMachine([(0, 0, 0, 0),
            ....:                         (0, 1, 1, 1),
            ....:                         (1, 1, 0, 0)],
            ....:                        determine_alphabets=False)
            sage: F.is_complete()
            Traceback (most recent call last):
            ...
            ValueError: No input alphabet is given. Try calling
            determine_alphabets().

        Non-deterministic machines are not allowed. ::

            sage: F = FiniteStateMachine([(0, 0, 0, 0), (0, 1, 0, 0)])
            sage: F.is_complete()
            False
            sage: F.completion()
            Traceback (most recent call last):
            ...
            ValueError: The finite state machine must be deterministic.
            sage: F = FiniteStateMachine([(0, 0, [0, 0], 0)])
            sage: F.is_complete()
            False
            sage: F.completion()
            Traceback (most recent call last):
            ...
            ValueError: The finite state machine must be deterministic.

        .. SEEALSO::

            :meth:`is_complete`,
            :meth:`split_transitions`,
            :meth:`determine_alphabets`,
            :meth:`is_deterministic`.

        TESTS:

        Test the use of an :class:`FSMState` as sink::

            sage: F = FiniteStateMachine([(0, 0, 0, 0),
            ....:                         (0, 1, 1, 1),
            ....:                         (1, 1, 0, 0)])
            sage: from sage.combinat.finite_state_machine import FSMState
            sage: F.completion(FSMState(1))
            Traceback (most recent call last):
            ...
            ValueError: The finite state machine already contains a state
            '1'.
            sage: s = FSMState(2)
            sage: G = F.completion(s)
            sage: G.state(2) is s
            True
        """
    def prepone_output(self):
        """
        For all paths, shift the output of the path from one
        transition to the earliest possible preceding transition of
        the path.

        OUTPUT: nothing

        Apply the following to each state `s` (except initial states) of the
        finite state machine as often as possible:

        If the letter `a` is a prefix of the output label of all transitions from
        `s` (including the final output of `s`), then remove it from all these
        labels and append it to all output labels of all transitions leading
        to `s`.

        We assume that the states have no output labels, but final outputs are
        allowed.

        EXAMPLES::

            sage: A = Transducer([('A', 'B', 1, 1),
            ....:                 ('B', 'B', 0, 0),
            ....:                 ('B', 'C', 1, 0)],
            ....:                initial_states=['A'],
            ....:                final_states=['C'])
            sage: A.prepone_output()
            sage: A.transitions()
            [Transition from 'A' to 'B': 1|1,0,
             Transition from 'B' to 'B': 0|0,
             Transition from 'B' to 'C': 1|-]

        ::

            sage: B = Transducer([('A', 'B', 0, 1),
            ....:                 ('B', 'C', 1, [1, 1]),
            ....:                 ('B', 'C', 0, 1)],
            ....:                initial_states=['A'],
            ....:                final_states=['C'])
            sage: B.prepone_output()
            sage: B.transitions()
            [Transition from 'A' to 'B': 0|1,1,
             Transition from 'B' to 'C': 1|1,
             Transition from 'B' to 'C': 0|-]

        If initial states are not labeled as such, unexpected results may be
        obtained::

            sage: C = Transducer([(0,1,0,0)])
            sage: C.prepone_output()
            verbose 0 (...: finite_state_machine.py, prepone_output)
            All transitions leaving state 0 have an output label with
            prefix 0.  However, there is no inbound transition and it
            is not an initial state. This routine (possibly called by
            simplification) therefore erased this prefix from all
            outbound transitions.
            sage: C.transitions()
            [Transition from 0 to 1: 0|-]

        Also the final output of final states can be changed::

            sage: T = Transducer([('A', 'B', 0, 1),
            ....:                 ('B', 'C', 1, [1, 1]),
            ....:                 ('B', 'C', 0, 1)],
            ....:                initial_states=['A'],
            ....:                final_states=['B'])
            sage: T.state('B').final_word_out = [1]
            sage: T.prepone_output()
            sage: T.transitions()
            [Transition from 'A' to 'B': 0|1,1,
             Transition from 'B' to 'C': 1|1,
             Transition from 'B' to 'C': 0|-]
            sage: T.state('B').final_word_out
            []

        ::

            sage: S = Transducer([('A', 'B', 0, 1),
            ....:                 ('B', 'C', 1, [1, 1]),
            ....:                 ('B', 'C', 0, 1)],
            ....:                initial_states=['A'],
            ....:                final_states=['B'])
            sage: S.state('B').final_word_out = [0]
            sage: S.prepone_output()
            sage: S.transitions()
            [Transition from 'A' to 'B': 0|1,
             Transition from 'B' to 'C': 1|1,1,
             Transition from 'B' to 'C': 0|1]
            sage: S.state('B').final_word_out
            [0]

        Output labels do not have to be hashable::

            sage: C = Transducer([(0, 1, 0, []),
            ....:                 (1, 0, 0, [vector([0, 0]), 0]),
            ....:                 (1, 1, 1, [vector([0, 0]), 1]),
            ....:                 (0, 0, 1, 0)],
            ....:                 determine_alphabets=False,
            ....:                 initial_states=[0])
            sage: C.prepone_output()
            sage: sorted(C.transitions())
            [Transition from 0 to 1: 0|(0, 0),
             Transition from 0 to 0: 1|0,
             Transition from 1 to 0: 0|0,
             Transition from 1 to 1: 1|1,(0, 0)]
        """
    def equivalence_classes(self):
        '''
        Return a list of equivalence classes of states.

        Two states `a` and `b` are equivalent if and only if there is
        a bijection `\\varphi` between paths starting at `a` and paths
        starting at `b` with the following properties: Let `p_a` be a
        path from `a` to `a\'` and `p_b` a path from `b` to `b\'` such
        that `\\varphi(p_a)=p_b`, then

        - `p_a.\\mathit{word}_\\mathit{in}=p_b.\\mathit{word}_\\mathit{in}`,
        - `p_a.\\mathit{word}_\\mathit{out}=p_b.\\mathit{word}_\\mathit{out}`,
        - `a\'` and `b\'` have the same output label, and
        - `a\'` and `b\'` are both final or both non-final and have the
          same final output word.

        The function :meth:`.equivalence_classes` returns a list of
        the equivalence classes to this equivalence relation.

        This is one step of Moore\'s minimization algorithm.

        .. SEEALSO::

            :meth:`.minimization`

        EXAMPLES::

            sage: fsm = FiniteStateMachine([("A", "B", 0, 1), ("A", "B", 1, 0),
            ....:                           ("B", "C", 0, 0), ("B", "C", 1, 1),
            ....:                           ("C", "D", 0, 1), ("C", "D", 1, 0),
            ....:                           ("D", "A", 0, 0), ("D", "A", 1, 1)])
            sage: sorted(fsm.equivalence_classes())
            [[\'A\', \'C\'], [\'B\', \'D\']]
            sage: fsm.state("A").is_final = True
            sage: sorted(fsm.equivalence_classes())
            [[\'A\'], [\'B\'], [\'C\'], [\'D\']]
            sage: fsm.state("C").is_final = True
            sage: sorted(fsm.equivalence_classes())
            [[\'A\', \'C\'], [\'B\', \'D\']]
            sage: fsm.state("A").final_word_out = 1
            sage: sorted(fsm.equivalence_classes())
            [[\'A\'], [\'B\'], [\'C\'], [\'D\']]
            sage: fsm.state("C").final_word_out = 1
            sage: sorted(fsm.equivalence_classes())
            [[\'A\', \'C\'], [\'B\', \'D\']]
        '''
    def quotient(self, classes):
        '''
        Construct the quotient with respect to the equivalence classes.

        INPUT:

        - ``classes`` is a list of equivalence classes of states.

        OUTPUT: a finite state machine

        The labels of the new states are tuples of states of the
        ``self``, corresponding to ``classes``.

        Assume that `c` is a class, and `a` and `b` are states in
        `c`. Then there is a bijection `\\varphi` between the
        transitions from `a` and the transitions from `b` with the
        following properties: if `\\varphi(t_a)=t_b`, then

        - `t_a.\\mathit{word}_\\mathit{in}=t_b.\\mathit{word}_\\mathit{in}`,
        - `t_a.\\mathit{word}_\\mathit{out}=t_b.\\mathit{word}_\\mathit{out}`, and
        - `t_a` and `t_b` lead to some equivalent states `a\'` and `b\'`.

        Non-initial states may be merged with initial states, the
        resulting state is an initial state.

        All states in a class must have the same ``is_final``,
        ``final_word_out`` and ``word_out`` values.

        EXAMPLES::

            sage: fsm = FiniteStateMachine([("A", "B", 0, 1), ("A", "B", 1, 0),
            ....:                           ("B", "C", 0, 0), ("B", "C", 1, 1),
            ....:                           ("C", "D", 0, 1), ("C", "D", 1, 0),
            ....:                           ("D", "A", 0, 0), ("D", "A", 1, 1)])
            sage: fsmq = fsm.quotient([[fsm.state("A"), fsm.state("C")],
            ....:                      [fsm.state("B"), fsm.state("D")]])
            sage: fsmq.transitions()
            [Transition from (\'A\', \'C\')
                          to (\'B\', \'D\'): 0|1,
             Transition from (\'A\', \'C\')
                          to (\'B\', \'D\'): 1|0,
             Transition from (\'B\', \'D\')
                          to (\'A\', \'C\'): 0|0,
             Transition from (\'B\', \'D\')
                          to (\'A\', \'C\'): 1|1]
            sage: fsmq.relabeled().transitions()
            [Transition from 0 to 1: 0|1,
             Transition from 0 to 1: 1|0,
             Transition from 1 to 0: 0|0,
             Transition from 1 to 0: 1|1]
            sage: fsmq1 = fsm.quotient(fsm.equivalence_classes())
            sage: fsmq1 == fsmq
            True
            sage: fsm.quotient([[fsm.state("A"), fsm.state("B"), fsm.state("C"), fsm.state("D")]])
            Traceback (most recent call last):
                ...
            AssertionError: Transitions of state \'A\' and \'B\' are incompatible.

        TESTS::

            sage: fsm = FiniteStateMachine([("A", "B", 0, 1), ("A", "B", 1, 0),
            ....:                           ("B", "C", 0, 0), ("B", "C", 1, 1),
            ....:                           ("C", "D", 0, 1), ("C", "D", 1, 0),
            ....:                           ("D", "A", 0, 0), ("D", "A", 1, 1)],
            ....:                           final_states=["A", "C"])
            sage: fsm.state("A").final_word_out = 1
            sage: fsm.state("C").final_word_out = 2
            sage: fsmq = fsm.quotient([[fsm.state("A"), fsm.state("C")],
            ....:                      [fsm.state("B"), fsm.state("D")]])
            Traceback (most recent call last):
                ...
            AssertionError: Class [\'A\', \'C\'] mixes
            final states with different final output words.
        '''
    def merged_transitions(self):
        """
        Merges transitions which have the same ``from_state``,
        ``to_state`` and ``word_out`` while adding their ``word_in``.

        OUTPUT:

        A finite state machine with merged transitions. If no mergers occur,
        return ``self``.

        EXAMPLES::

            sage: from sage.combinat.finite_state_machine import duplicate_transition_add_input
            sage: T = Transducer([[1, 2, 1/4, 1], [1, -2, 1/4, 1], [1, -2, 1/2, 1],
            ....:                 [2, 2, 1/4, 1], [2, -2, 1/4, 1], [-2, -2, 1/4, 1],
            ....:                 [-2, 2, 1/4, 1], [2, 3, 1/2, 1], [-2, 3, 1/2, 1]],
            ....:                on_duplicate_transition=duplicate_transition_add_input)
            sage: T1 = T.merged_transitions()
            sage: T1 is T
            False
            sage: sorted(T1.transitions())
            [Transition from -2 to -2: 1/4|1,
             Transition from -2 to 2: 1/4|1,
             Transition from -2 to 3: 1/2|1,
             Transition from 1 to 2: 1/4|1,
             Transition from 1 to -2: 3/4|1,
             Transition from 2 to -2: 1/4|1,
             Transition from 2 to 2: 1/4|1,
             Transition from 2 to 3: 1/2|1]

        Applying the function again does not change the result::

            sage: T2 = T1.merged_transitions()
            sage: T2 is T1
            True
        """
    def markov_chain_simplification(self):
        """
        Consider ``self`` as Markov chain with probabilities as input labels
        and simplify it.

        OUTPUT: simplified version of ``self``

        EXAMPLES::

            sage: from sage.combinat.finite_state_machine import duplicate_transition_add_input
            sage: T = Transducer([[1, 2, 1/4, 0], [1, -2, 1/4, 0], [1, -2, 1/2, 0],
            ....:                 [2, 2, 1/4, 1], [2, -2, 1/4, 1], [-2, -2, 1/4, 1],
            ....:                 [-2, 2, 1/4, 1], [2, 3, 1/2, 2], [-2, 3, 1/2, 2]],
            ....:                initial_states=[1],
            ....:                final_states=[3],
            ....:                on_duplicate_transition=duplicate_transition_add_input)
            sage: T1 = T.markov_chain_simplification()
            sage: sorted(T1.transitions())
            [Transition from ((1,),) to ((2, -2),): 1|0,
             Transition from ((2, -2),) to ((2, -2),): 1/2|1,
             Transition from ((2, -2),) to ((3,),): 1/2|2]
        """
    def with_final_word_out(self, letters, allow_non_final: bool = True):
        '''
        Construct a new finite state machine with final output words
        for all states by implicitly reading trailing letters until a
        final state is reached.

        INPUT:

        - ``letters`` -- either an element of the input alphabet or a
          list of such elements. This is repeated cyclically when
          needed.

        - ``allow_non_final`` -- boolean (default: ``True``); whether we allow
          that some states may be non-final in the resulting finite state
          machine. I.e., if ``False`` then each state has to have a path to a
          final state with input label matching ``letters``.

        OUTPUT: a finite state machine

        The inplace version of this function is
        :meth:`.construct_final_word_out`.

        Suppose for the moment a single element ``letter`` as input
        for ``letters``. This is equivalent to ``letters = [letter]``.
        We will discuss the general case below.

        Let ``word_in`` be a word over the input alphabet and assume
        that the original finite state machine transforms ``word_in`` to
        ``word_out`` reaching a possibly non-final state ``s``. Let
        further `k` be the minimum number of letters ``letter`` such
        that there is a path from ``s`` to some final state ``f`` whose
        input label consists of `k` copies of ``letter`` and whose
        output label is ``path_word_out``. Then the state ``s`` of the
        resulting finite state machine is a final state with final
        output ``path_word_out + f.final_word_out``. Therefore, the new
        finite state machine transforms ``word_in`` to ``word_out +
        path_word_out + f.final_word_out``.

        This is e.g. useful for finite state machines operating on digit
        expansions: there, it is sometimes required to read a sufficient
        number of trailing zeros (at the most significant positions) in
        order to reach a final state and to flush all carries. In this
        case, this method constructs an essentially equivalent finite
        state machine in the sense that it not longer requires adding
        sufficiently many trailing zeros. However, it is the
        responsibility of the user to make sure that if adding trailing
        zeros to the input anyway, the output is equivalent.

        If ``letters`` consists of more than one letter, then it is
        assumed that (not necessarily complete) cycles of ``letters``
        are appended as trailing input.

        .. SEEALSO::

            :ref:`example on Gray code <finite_state_machine_gray_code_example>`

        EXAMPLES:

            #.  A simple transducer transforming `00` blocks to `01`
                blocks::

                    sage: T = Transducer([(0, 1, 0, 0), (1, 0, 0, 1)],
                    ....:                initial_states=[0],
                    ....:                final_states=[0])
                    sage: T.process([0, 0, 0])
                    (False, 1, [0, 1, 0])
                    sage: T.process([0, 0, 0, 0])
                    (True, 0, [0, 1, 0, 1])
                    sage: F = T.with_final_word_out(0)
                    sage: for f in F.iter_final_states():
                    ....:     print("{} {}".format(f, f.final_word_out))
                    0 []
                    1 [1]
                    sage: F.process([0, 0, 0])
                    (True, 1, [0, 1, 0, 1])
                    sage: F.process([0, 0, 0, 0])
                    (True, 0, [0, 1, 0, 1])

            #.  A more realistic example: Addition of `1` in binary. We
                construct a transition function transforming the input
                to its binary expansion::

                    sage: def binary_transition(carry, input):
                    ....:     value = carry + input
                    ....:     if value.mod(2) == 0:
                    ....:         return (value/2, 0)
                    ....:     else:
                    ....:         return ((value-1)/2, 1)

                Now, we only have to start with a carry of `1` to
                get the required transducer::

                    sage: T = Transducer(binary_transition,
                    ....:                input_alphabet=[0, 1],
                    ....:                initial_states=[1],
                    ....:                final_states=[0])

                We test this for the binary expansion of `7`::

                    sage: T.process([1, 1, 1])
                    (False, 1, [0, 0, 0])

                The final carry `1` has not be flushed yet, we have to add a
                trailing zero::

                    sage: T.process([1, 1, 1, 0])
                    (True, 0, [0, 0, 0, 1])

                We check that with this trailing zero, the transducer
                performs as advertised::

                    sage: all(ZZ(T(k.bits()+[0]), base=2) == k + 1
                    ....:     for k in srange(16))
                    True

                However, most of the time, we produce superfluous trailing
                zeros::

                    sage: T(11.bits()+[0])
                    [0, 0, 1, 1, 0]

                We now use this method::

                    sage: F = T.with_final_word_out(0)
                    sage: for f in F.iter_final_states():
                    ....:     print("{} {}".format(f, f.final_word_out))
                    1 [1]
                    0 []

                The same tests as above, but we do not have to pad with
                trailing zeros anymore::

                    sage: F.process([1, 1, 1])
                    (True, 1, [0, 0, 0, 1])
                    sage: all(ZZ(F(k.bits()), base=2) == k + 1
                    ....:     for k in srange(16))
                    True

                No more trailing zero in the output::

                    sage: F(11.bits())
                    [0, 0, 1, 1]
                    sage: all(F(k.bits())[-1] == 1
                    ....:     for k in srange(16))
                    True

            #.  Here is an example, where we allow trailing repeated `10`::

                    sage: T = Transducer([(0, 1, 0, \'a\'),
                    ....:                 (1, 2, 1, \'b\'),
                    ....:                 (2, 0, 0, \'c\')],
                    ....:                initial_states=[0],
                    ....:                final_states=[0])
                    sage: F = T.with_final_word_out([1, 0])
                    sage: for f in F.iter_final_states():
                    ....:     print(str(f) + \' \' + \'\'.join(f.final_word_out))
                    0
                    1 bc

                Trying this with trailing repeated `01` does not produce
                a ``final_word_out`` for state ``1``, but for state ``2``::

                    sage: F = T.with_final_word_out([0, 1])
                    sage: for f in F.iter_final_states():
                    ....:     print(str(f) + \' \' + \'\'.join(f.final_word_out))
                    0
                    2 c

            #.  Here another example with a more-letter trailing input::

                    sage: T = Transducer([(0, 1, 0, \'a\'),
                    ....:                 (1, 2, 0, \'b\'), (1, 2, 1, \'b\'),
                    ....:                 (2, 3, 0, \'c\'), (2, 0, 1, \'e\'),
                    ....:                 (3, 1, 0, \'d\'), (3, 1, 1, \'d\')],
                    ....:                initial_states=[0],
                    ....:                final_states=[0],
                    ....:                with_final_word_out=[0, 0, 1, 1])
                    sage: for f in T.iter_final_states():
                    ....:     print(str(f) + \' \' + \'\'.join(f.final_word_out))
                    0
                    1 bcdbcdbe
                    2 cdbe
                    3 dbe

        TESTS:

            #.  Reading copies of ``letter`` may result in a cycle. In
                this simple example, we have no final state at all::

                    sage: T = Transducer([(0, 1, 0, 0), (1, 0, 0, 0)],
                    ....:                initial_states=[0])
                    sage: T.with_final_word_out(0)
                    Traceback (most recent call last):
                    ...
                    ValueError: The finite state machine contains
                    a cycle starting at state 0 with input label 0
                    and no final state.

            #.  A unique transition with input word ``letter`` is
                required::

                    sage: T = Transducer([(0, 1, 0, 0), (0, 2, 0, 0)])
                    sage: T.with_final_word_out(0)
                    Traceback (most recent call last):
                    ...
                    ValueError: No unique transition leaving state 0
                    with input label 0.

                It is not a problem if there is no transition starting
                at state ``1`` with input word ``letter``::

                    sage: T = Transducer([(0, 1, 0, 0)])
                    sage: F = T.with_final_word_out(0)
                    sage: for f in F.iter_final_states():
                    ....:     print(f, f.final_word_out)

                Anyhow, you can override this by::

                    sage: T = Transducer([(0, 1, 0, 0)])
                    sage: T.with_final_word_out(0, allow_non_final=False)
                    Traceback (most recent call last):
                    ...
                    ValueError: No unique transition leaving state 1
                    with input label 0.

            #.  All transitions must have input labels of length `1`::

                    sage: T = Transducer([(0, 0, [], 0)])
                    sage: T.with_final_word_out(0)
                    Traceback (most recent call last):
                    ...
                    NotImplementedError: All transitions must have input
                    labels of length 1. Consider calling split_transitions().
                    sage: T = Transducer([(0, 0, [0, 1], 0)])
                    sage: T.with_final_word_out(0)
                    Traceback (most recent call last):
                    ...
                    NotImplementedError: All transitions must have input
                    labels of length 1. Consider calling split_transitions().

            #.  An empty list as input is not allowed::

                    sage: T = Transducer([(0, 0, [], 0)])
                    sage: T.with_final_word_out([])
                    Traceback (most recent call last):
                    ...
                    ValueError: letters is not allowed to be an empty list.
        '''
    def construct_final_word_out(self, letters, allow_non_final: bool = True):
        """
        This is an inplace version of :meth:`.with_final_word_out`. See
        :meth:`.with_final_word_out` for documentation and examples.

        TESTS::

            sage: T = Transducer([(0, 1, 0, 0), (1, 0, 0, 1)],
            ....:                initial_states=[0],
            ....:                final_states=[0])
            sage: F = T.with_final_word_out(0)
            sage: T.construct_final_word_out(0)
            sage: T == F  # indirect doctest
            True
            sage: T = Transducer([(0, 1, 0, None)],
            ....:                final_states=[1])
            sage: F = T.with_final_word_out(0)
            sage: F.state(0).final_word_out
            []
        """
    def graph(self, edge_labels: str = 'words_in_out'):
        """
        Return the graph of the finite state machine with labeled
        vertices and labeled edges.

        INPUT:

        - ``edge_label`` -- (default: ``'words_in_out'``) can be
            - ``'words_in_out'`` (labels will be strings ``'i|o'``)
            - a function with which takes as input a transition
              and outputs (returns) the label

        OUTPUT: a :class:`directed graph <DiGraph>`

        EXAMPLES::

            sage: from sage.combinat.finite_state_machine import FSMState
            sage: A = FSMState('A')
            sage: T = Transducer()
            sage: T.graph()
            Looped multi-digraph on 0 vertices
            sage: T.add_state(A)
            'A'
            sage: T.graph()
            Looped multi-digraph on 1 vertex
            sage: T.add_transition(('A', 'A', 0, 1))
            Transition from 'A' to 'A': 0|1
            sage: T.graph()
            Looped multi-digraph on 1 vertex

        .. SEEALSO::

            :class:`DiGraph`
        """
    digraph = graph
    def plot(self):
        """
        Plots a graph of the finite state machine with labeled
        vertices and labeled edges.

        OUTPUT: a plot of the graph of the finite state machine

        TESTS::

            sage: FiniteStateMachine([('A', 'A', 0)]).plot()                            # needs sage.plot
            Graphics object consisting of 3 graphics primitives
        """
    def predecessors(self, state, valid_input=None):
        """
        List all predecessors of a state.

        INPUT:

        - ``state`` -- the state from which the predecessors should be
          listed

        - ``valid_input`` -- if ``valid_input`` is a list, then we
          only consider transitions whose input labels are contained
          in ``valid_input``. ``state`` has to be a :class:`FSMState`
          (not a label of a state). If input labels of length larger
          than `1` are used, then ``valid_input`` has to be a list of
          lists.

        OUTPUT: list of states

        EXAMPLES::

            sage: A = Transducer([('I', 'A', 'a', 'b'), ('I', 'B', 'b', 'c'),
            ....:                 ('I', 'C', 'c', 'a'), ('A', 'F', 'b', 'a'),
            ....:                 ('B', 'F', ['c', 'b'], 'b'), ('C', 'F', 'a', 'c')],
            ....:                initial_states=['I'], final_states=['F'])
            sage: A.predecessors(A.state('A'))
            ['A', 'I']
            sage: A.predecessors(A.state('F'), valid_input=['b', 'a'])
            ['F', 'C', 'A', 'I']
            sage: A.predecessors(A.state('F'), valid_input=[['c', 'b'], 'a'])
            ['F', 'C', 'B']
        """
    def number_of_words(self, variable=None, base_ring=None):
        """
        Return the number of successful input words of given length.

        INPUT:

        - ``variable`` -- a symbol denoting the length of the words,
          by default `n`

        - ``base_ring`` -- ring (default: ``QQbar``) in which to
          compute the eigenvalues

        OUTPUT: a symbolic expression

        EXAMPLES::

            sage: NAFpm = Automaton([(0, 0, 0), (0, 1, 1),
            ....:                    (0, 1, -1), (1, 0, 0)],
            ....:                   initial_states=[0],
            ....:                   final_states=[0, 1])
            sage: N = NAFpm.number_of_words(); N                                        # needs sage.symbolic
            4/3*2^n - 1/3*(-1)^n
            sage: all(len(list(NAFpm.language(s)))                                      # needs sage.symbolic
            ....:     - len(list(NAFpm.language(s-1))) == N.subs(n=s)
            ....:     for s in srange(1, 6))
            True

        An example with non-rational eigenvalues. By default,
        eigenvalues are elements of the
        :mod:`field of algebraic numbers <sage.rings.qqbar>`. ::

            sage: NAFp = Automaton([(0, 0, 0), (0, 1, 1),  (1, 0, 0)],
            ....:                 initial_states=[0],
            ....:                 final_states=[0, 1])
            sage: N = NAFp.number_of_words(); N                                         # needs sage.rings.number_field sage.symbolic
            1.170820393249937?*1.618033988749895?^n
            - 0.1708203932499369?*(-0.618033988749895?)^n
            sage: all(len(list(NAFp.language(s)))                                       # needs sage.rings.number_field sage.symbolic
            ....:     - len(list(NAFp.language(s-1))) == N.subs(n=s)
            ....:     for s in srange(1, 6))
            True

        We specify a suitable ``base_ring`` to obtain a radical
        expression. To do so, we first compute the characteristic
        polynomial and then construct a number field generated by its
        roots. ::

            sage: # needs sage.rings.number_field sage.symbolic
            sage: M = NAFp.adjacency_matrix(entry=lambda t: 1)
            sage: M.characteristic_polynomial()
            x^2 - x - 1
            sage: R.<phi> = NumberField(x^2 - x - 1, embedding=1.6)
            sage: N = NAFp.number_of_words(base_ring=R); N
            1/2*(1/2*sqrt(5) + 1/2)^n*(3*sqrt(1/5) + 1)
            - 1/2*(-1/2*sqrt(5) + 1/2)^n*(3*sqrt(1/5) - 1)
            sage: all(len(list(NAFp.language(s)))
            ....:     - len(list(NAFp.language(s-1))) == N.subs(n=s)
            ....:     for s in srange(1, 6))
            True

        In this special case, we might also use the constant
        :class:`golden_ratio <sage.symbolic.constants.GoldenRatio>`::

            sage: # needs sage.rings.number_field sage.symbolic
            sage: R.<phi> = NumberField(x^2-x-1, embedding=golden_ratio)
            sage: N = NAFp.number_of_words(base_ring=R); N
            1/5*(3*golden_ratio + 1)*golden_ratio^n
            - 1/5*(3*golden_ratio - 4)*(-golden_ratio + 1)^n
            sage: all(len(list(NAFp.language(s)))
            ....:     - len(list(NAFp.language(s-1))) == N.subs(n=s)
            ....:     for s in srange(1, 6))
            True

        The adjacency matrix of the following example is a Jordan
        matrix of size 3 to the eigenvalue 4::

            sage: J3 = Automaton([(0, 1, -1), (1, 2, -1)],
            ....:     initial_states=[0],
            ....:     final_states=[0, 1, 2])
            sage: for i in range(3):
            ....:     for j in range(4):
            ....:         new_transition = J3.add_transition(i, i, j)
            sage: J3.adjacency_matrix(entry=lambda t: 1)
            [4 1 0]
            [0 4 1]
            [0 0 4]
            sage: N = J3.number_of_words(); N                                           # needs sage.symbolic
            1/2*4^(n - 2)*(n - 1)*n + 4^(n - 1)*n + 4^n
            sage: all(len(list(J3.language(s)))                                         # needs sage.symbolic
            ....:     - len(list(J3.language(s-1))) == N.subs(n=s)
            ....:     for s in range(1, 6))
            True

        Here is an automaton without cycles, so with eigenvalue `0`. ::

            sage: A = Automaton([(j, j+1, 0) for j in range(3)],
            ....:               initial_states=[0],
            ....:               final_states=list(range(3)))
            sage: A.number_of_words()                                                   # needs sage.symbolic
            1/2*0^(n - 2)*(n - 1)*n + 0^(n - 1)*n + 0^n

        TESTS::

            sage: A = Automaton([(0, 0, 0), (0, 1, 0)],
            ....:               initial_states=[0])
            sage: A.number_of_words()                                                   # needs sage.symbolic
            Traceback (most recent call last):
            ...
            NotImplementedError: Finite State Machine must be deterministic.
        """
    def asymptotic_moments(self, variable=None):
        '''
        Return the main terms of expectation and variance of the sum
        of output labels and its covariance with the sum of input
        labels.

        INPUT:

        - ``variable`` -- a symbol denoting the length of the input,
          (default: `n`)

        OUTPUT: a dictionary consisting of

        - ``expectation`` -- `e n + \\operatorname{Order}(1)`,
        - ``variance`` -- `v n + \\operatorname{Order}(1)`,
        - ``covariance`` -- `c n + \\operatorname{Order}(1)`

        for suitable constants `e`, `v` and `c`.

        Assume that all input and output labels are numbers and that
        ``self`` is complete and has only one final component. Assume
        further that this final component is aperiodic. Furthermore,
        assume that there is exactly one initial state and that all
        states are final.

        Denote by `X_n` the sum of output labels written by the
        finite state machine when reading a random input word of
        length `n` over the input alphabet (assuming
        equidistribution).

        Then the expectation of `X_n` is `en+O(1)`, the variance
        of `X_n` is `vn+O(1)` and the covariance of `X_n` and
        the sum of input labels is `cn+O(1)`, cf. [HKW2015]_,
        Theorem 3.9.

        In the case of non-integer input or output labels, performance
        degrades significantly. For rational input and output labels,
        consider rescaling to integers. This limitation comes from the
        fact that determinants over polynomial rings can be computed
        much more efficiently than over the symbolic ring. In fact, we
        compute (parts) of a trivariate generating function where the
        input and output labels are exponents of some indeterminates,
        see [HKW2015]_, Theorem 3.9 for details. If those exponents are
        integers, we can use a polynomial ring.

        EXAMPLES:

        #.  A trivial example: write the negative of the input::

                sage: T = Transducer([(0, 0, 0, 0), (0, 0, 1, -1)],
                ....:                initial_states=[0],
                ....:                final_states=[0])
                sage: T([0, 1, 1])
                [0, -1, -1]

                sage: # needs sage.symbolic
                sage: moments = T.asymptotic_moments()
                sage: moments[\'expectation\']
                -1/2*n + Order(1)
                sage: moments[\'variance\']
                1/4*n + Order(1)
                sage: moments[\'covariance\']
                -1/4*n + Order(1)

        #.  For the case of the Hamming weight of the non-adjacent-form
            (NAF) of integers, cf. the :wikipedia:`Non-adjacent_form`
            and the :ref:`example on recognizing NAFs
            <finite_state_machine_recognizing_NAFs_example>`, the
            following agrees with the results in [HP2007]_.

            We first use the transducer to convert the standard binary
            expansion to the NAF given in [HP2007]_. We use the parameter
            ``with_final_word_out`` such that we do not have to add
            sufficiently many trailing zeros::

                sage: NAF = Transducer([(0, 0, 0, 0),
                ....:                   (0, \'.1\', 1, None),
                ....:                   (\'.1\', 0, 0, [1, 0]),
                ....:                   (\'.1\', 1, 1, [-1, 0]),
                ....:                   (1, 1, 1, 0),
                ....:                   (1, \'.1\', 0, None)],
                ....:                  initial_states=[0],
                ....:                  final_states=[0],
                ....:                  with_final_word_out=[0])

            As an example, we compute the NAF of `27` by this
            transducer.

            ::

                sage: binary_27 = 27.bits()
                sage: binary_27
                [1, 1, 0, 1, 1]
                sage: NAF_27 = NAF(binary_27)
                sage: NAF_27
                [-1, 0, -1, 0, 0, 1, 0]
                sage: ZZ(NAF_27, base=2)
                27

            Next, we are only interested in the Hamming weight::

                sage: def weight(state, input):
                ....:     if input is None:
                ....:         result = 0
                ....:     else:
                ....:         result = ZZ(input != 0)
                ....:     return (0, result)
                sage: weight_transducer = Transducer(weight,
                ....:                                input_alphabet=[-1, 0, 1],
                ....:                                initial_states=[0],
                ....:                                final_states=[0])
                sage: NAFweight = weight_transducer.composition(NAF)
                sage: NAFweight.transitions()
                [Transition from (0, 0) to (0, 0): 0|0,
                 Transition from (0, 0) to (\'.1\', 0): 1|-,
                 Transition from (\'.1\', 0) to (0, 0): 0|1,0,
                 Transition from (\'.1\', 0) to (1, 0): 1|1,0,
                 Transition from (1, 0) to (\'.1\', 0): 0|-,
                 Transition from (1, 0) to (1, 0): 1|0]
                sage: NAFweight(binary_27)
                [1, 0, 1, 0, 0, 1, 0]

            Now, we actually compute the asymptotic moments::

                sage: # needs sage.symbolic
                sage: moments = NAFweight.asymptotic_moments()
                sage: moments[\'expectation\']
                1/3*n + Order(1)
                sage: moments[\'variance\']
                2/27*n + Order(1)
                sage: moments[\'covariance\']
                Order(1)

        #.  This is Example 3.16 in [HKW2015]_, where a transducer with
            variable output labels is given. There, the aim was to
            choose the output labels of this very simple transducer such
            that the input and output sum are asymptotically
            independent, i.e., the constant `c` vanishes.

            ::

                sage: # needs sage.symbolic
                sage: var(\'a_1, a_2, a_3, a_4\')
                (a_1, a_2, a_3, a_4)
                sage: T = Transducer([[0, 0, 0, a_1], [0, 1, 1, a_3],
                ....:                 [1, 0, 0, a_4], [1, 1, 1, a_2]],
                ....:                initial_states=[0], final_states=[0, 1])
                sage: moments = T.asymptotic_moments()
                verbose 0 (...) Non-integer output weights lead to
                significant performance degradation.
                sage: moments[\'expectation\']
                1/4*(a_1 + a_2 + a_3 + a_4)*n + Order(1)
                sage: moments[\'covariance\']
                -1/4*(a_1 - a_2)*n + Order(1)

            Therefore, the asymptotic covariance vanishes if and only if
            `a_2=a_1`.

        #.  This is Example 4.3 in [HKW2015]_, dealing with the
            transducer converting the binary expansion of an integer
            into Gray code (cf. the :wikipedia:`Gray_code` and the
            :ref:`example on Gray code
            <finite_state_machine_gray_code_example>`)::

                sage: # needs sage.symbolic
                sage: moments = transducers.GrayCode().asymptotic_moments()
                sage: moments[\'expectation\']
                1/2*n + Order(1)
                sage: moments[\'variance\']
                1/4*n + Order(1)
                sage: moments[\'covariance\']
                Order(1)

        #.  This is the first part of Example 4.4 in [HKW2015]_,
            counting the number of 10 blocks in the standard binary
            expansion. The least significant digit is at the left-most
            position::

                sage: block10 = transducers.CountSubblockOccurrences(
                ....:     [1, 0],
                ....:     input_alphabet=[0, 1])
                sage: sorted(block10.transitions())
                [Transition from () to (): 0|0,
                 Transition from () to (1,): 1|0,
                 Transition from (1,) to (): 0|1,
                 Transition from (1,) to (1,): 1|0]

                sage: # needs sage.symbolic
                sage: moments = block10.asymptotic_moments()
                sage: moments[\'expectation\']
                1/4*n + Order(1)
                sage: moments[\'variance\']
                1/16*n + Order(1)
                sage: moments[\'covariance\']
                Order(1)

        #.  This is the second part of Example 4.4 in [HKW2015]_,
            counting the number of 11 blocks in the standard binary
            expansion. The least significant digit is at the left-most
            position::

                sage: block11 = transducers.CountSubblockOccurrences(
                ....:     [1, 1],
                ....:     input_alphabet=[0, 1])
                sage: sorted(block11.transitions())
                [Transition from () to (): 0|0,
                 Transition from () to (1,): 1|0,
                 Transition from (1,) to (): 0|0,
                 Transition from (1,) to (1,): 1|1]

                sage: # needs sage.symbolic
                sage: var(\'N\')
                N
                sage: moments = block11.asymptotic_moments(N)
                sage: moments[\'expectation\']
                1/4*N + Order(1)
                sage: moments[\'variance\']
                5/16*N + Order(1)
                sage: correlation = (moments[\'covariance\'].coefficient(N) /
                ....:                (1/2 * sqrt(moments[\'variance\'].coefficient(N))))
                sage: correlation
                2/5*sqrt(5)

        #.  This is Example 4.5 in [HKW2015]_, counting the number of
            01 blocks minus the number of 10 blocks in the standard binary
            expansion. The least significant digit is at the left-most
            position::

                sage: block01 = transducers.CountSubblockOccurrences(
                ....:     [0, 1],
                ....:     input_alphabet=[0, 1])
                sage: product_01x10 = block01.cartesian_product(block10)
                sage: block_difference = transducers.sub([0, 1])(product_01x10)
                sage: T = block_difference.simplification().relabeled()
                sage: T.transitions()
                [Transition from 0 to 2: 0|-1,
                 Transition from 0 to 0: 1|0,
                 Transition from 1 to 2: 0|0,
                 Transition from 1 to 0: 1|0,
                 Transition from 2 to 2: 0|0,
                 Transition from 2 to 0: 1|1]

                sage: # needs sage.symbolic
                sage: moments = T.asymptotic_moments()
                sage: moments[\'expectation\']
                Order(1)
                sage: moments[\'variance\']
                Order(1)
                sage: moments[\'covariance\']
                Order(1)

        #.  The finite state machine must have a unique final component::

                sage: T = Transducer([(0, -1, -1, -1), (0, 1, 1, 1),
                ....:                 (-1, -1, -1, -1), (-1, -1, 1, -1),
                ....:                 (1, 1, -1, 1), (1, 1, 1, 1)],
                ....:                initial_states=[0],
                ....:                final_states=[0, 1, -1])
                sage: T.asymptotic_moments()
                Traceback (most recent call last):
                ...
                NotImplementedError: asymptotic_moments is only
                implemented for finite state machines with one final
                component.

            In this particular example, the first letter of the input
            decides whether we reach the loop at `-1` or the loop at
            `1`. In the first case, we have `X_n = -n`, while we have
            `X_n = n` in the second case. Therefore, the expectation
            `E(X_n)` of `X_n` is `E(X_n) = 0`. We get `(X_n-E(X_n))^2 =
            n^2` in all cases, which results in a variance of `n^2`.

            So this example shows that the variance may be non-linear if
            there is more than one final component.

        TESTS:

        #.  An input alphabet must be given::

                sage: T = Transducer([[0, 0, 0, 0]],
                ....:                initial_states=[0], final_states=[0],
                ....:                determine_alphabets=False)
                sage: T.asymptotic_moments()
                Traceback (most recent call last):
                ...
                ValueError: No input alphabet is given.
                Try calling determine_alphabets().

        #.  The finite state machine must have a unique initial state::

                sage: T = Transducer([(0, 0, 0, 0)])
                sage: T.asymptotic_moments()
                Traceback (most recent call last):
                ...
                ValueError: A unique initial state is required.

        #.  The finite state machine must be complete::

                sage: T = Transducer([[0, 0, 0, 0]],
                ....:                initial_states=[0], final_states=[0],
                ....:                input_alphabet=[0, 1])
                sage: T.asymptotic_moments()
                Traceback (most recent call last):
                ...
                NotImplementedError: This finite state machine is
                not complete.

        #.  The final component of the finite state machine must be
            aperiodic::

                sage: T = Transducer([(0, 1, 0, 0), (1, 0, 0, 0)],
                ....:                initial_states=[0], final_states=[0, 1])
                sage: T.asymptotic_moments()
                Traceback (most recent call last):
                ...
                NotImplementedError: asymptotic_moments is only
                implemented for finite state machines whose unique final
                component is aperiodic.

        #.  Non-integer input or output labels lead to a warning::

                sage: # needs sage.symbolic
                sage: T = Transducer([[0, 0, 0, 0], [0, 0, 1, -1/2]],
                ....:                initial_states=[0], final_states=[0])
                sage: moments = T.asymptotic_moments()
                verbose 0 (...) Non-integer output weights lead to
                significant performance degradation.
                sage: moments[\'expectation\']
                -1/4*n + Order(1)
                sage: moments[\'variance\']
                1/16*n + Order(1)
                sage: moments[\'covariance\']
                -1/8*n + Order(1)

            This warning can be silenced by :func:`~sage.misc.verbose.set_verbose`::

                sage: # needs sage.symbolic
                sage: from sage.misc.verbose import set_verbose
                sage: set_verbose(-1, "finite_state_machine.py")
                sage: moments = T.asymptotic_moments()
                sage: moments[\'expectation\']
                -1/4*n + Order(1)
                sage: moments[\'variance\']
                1/16*n + Order(1)
                sage: moments[\'covariance\']
                -1/8*n + Order(1)
                sage: set_verbose(0, "finite_state_machine.py")

        #.  Check whether ``word_out`` of ``FSMState`` are correctly
            dealt with::

                sage: from sage.combinat.finite_state_machine import FSMState
                sage: s = FSMState(0, word_out=2,
                ....:              is_initial=True,
                ....:              is_final=True)
                sage: T = Transducer([(s, s, 0, 1)],
                ....:                initial_states=[s], final_states=[s])
                sage: T([0, 0])
                [2, 1, 2, 1, 2]
                sage: T.asymptotic_moments()[\'expectation\']                             # needs sage.symbolic
                3*n + Order(1)

            The same test for non-integer output::

                sage: from sage.combinat.finite_state_machine import FSMState
                sage: s = FSMState(0, word_out=2/3)
                sage: T = Transducer([(s, s, 0, 1/2)],
                ....:                initial_states=[s], final_states=[s])
                sage: T.asymptotic_moments()[\'expectation\']                             # needs sage.symbolic
                verbose 0 (...) Non-integer output weights lead to
                significant performance degradation.
                7/6*n + Order(1)

        #.  All states of ``self`` have to be final::

                sage: T = Transducer([(0, 1, 1, 4)], initial_states=[0])
                sage: T.asymptotic_moments()
                Traceback (most recent call last):
                ...
                ValueError: Not all states are final.

        ALGORITHM:

        See [HKW2015]_, Theorem 3.9.

        REFERENCES:

        .. [HP2007] Clemens Heuberger and Helmut Prodinger, *The Hamming
           Weight of the Non-Adjacent-Form under Various Input Statistics*,
           Periodica Mathematica Hungarica Vol. 55 (1), 2007, pp. 81--96,
           :doi:`10.1007/s10998-007-3081-z`.
        '''
    def moments_waiting_time(self, test=..., is_zero=None, expectation_only: bool = False):
        """
        If this finite state machine acts as a Markov chain, return
        the expectation and variance of the number of steps until
        first writing ``True``.

        INPUT:

        - ``test`` -- (default: ``bool``) a callable deciding whether
          an output label is to be considered ``True``. By default, the
          standard conversion to boolean is used.

        - ``is_zero`` -- (default: ``None``) a callable deciding
          whether an expression for a probability is zero. By default,
          checking for zero is simply done by
          :meth:`~sage.structure.element.Element.is_zero`.  This
          parameter can be used to provide a more sophisticated check
          for zero, e.g. in the case of symbolic probabilities, see
          the examples below. This parameter is passed on to
          :meth:`is_Markov_chain`. This parameter only affects the
          input of the Markov chain.

        - ``expectation_only`` -- boolean (default: ``False``); if set, the
          variance is not computed (in order to save time). By default,
          the variance is computed.

        OUTPUT:

        A dictionary (if ``expectation_only=False``) consisting of

        - ``expectation``,
        - ``variance``.

        Otherwise, just the expectation is returned (no dictionary for
        ``expectation_only=True``).

        Expectation and variance of the number of steps until first
        writing ``True`` (as determined by the parameter ``test``).

        ALGORITHM:

        Relies on a (classical and easy) probabilistic argument,
        cf. [FGT1992]_, Eqns. (6) and (7).

        For the variance, see [FHP2015]_, Section 2.

        EXAMPLES:

        #.  The simplest example is to wait for the first `1` in a
            `0`-`1`-string where both digits appear with probability
            `1/2`. In fact, the waiting time equals `k` if and only if
            the string starts with `0^{k-1}1`. This event occurs with
            probability `2^{-k}`. Therefore, the expected waiting time
            and the variance are `\\sum_{k\\ge 1} k2^{-k}=2` and
            `\\sum_{k\\ge 1} (k-2)^2 2^{-k}=2`::

                sage: var('k')                                                          # needs sage.symbolic
                k
                sage: sum(k * 2^(-k), k, 1, infinity)                                   # needs sage.symbolic
                2
                sage: sum((k-2)^2 * 2^(-k), k, 1, infinity)                             # needs sage.symbolic
                2

            We now compute the same expectation and variance by using a
            Markov chain::

                sage: from sage.combinat.finite_state_machine import (
                ....:     duplicate_transition_add_input)
                sage: T = Transducer(
                ....:     [(0, 0, 1/2, 0), (0, 0, 1/2, 1)],
                ....:     on_duplicate_transition=\\\n                ....:         duplicate_transition_add_input,
                ....:     initial_states=[0],
                ....:     final_states=[0])
                sage: T.moments_waiting_time()
                {'expectation': 2, 'variance': 2}
                sage: T.moments_waiting_time(expectation_only=True)
                2

            In the following, we replace the output ``0`` by ``-1`` and
            demonstrate the use of the parameter ``test``::

                sage: T.delete_transition((0, 0, 1/2, 0))
                sage: T.add_transition((0, 0, 1/2, -1))
                Transition from 0 to 0: 1/2|-1
                sage: T.moments_waiting_time(test=lambda x: x<0)
                {'expectation': 2, 'variance': 2}

        #.  Make sure that the transducer is actually a Markov
            chain. Although this is checked by the code, unexpected
            behaviour may still occur if the transducer looks like a
            Markov chain. In the following example, we 'forget' to
            assign probabilities, but due to a coincidence, all
            'probabilities' add up to one. Nevertheless, `0` is never
            written, so the expectation is `1`.

            ::

                sage: T = Transducer([(0, 0, 0, 0), (0, 0, 1, 1)],
                ....:                on_duplicate_transition=\\\n                ....:                    duplicate_transition_add_input,
                ....:                initial_states=[0],
                ....:                final_states=[0])
                sage: T.moments_waiting_time()
                {'expectation': 1, 'variance': 0}

        #.  If ``True`` is never written, the moments are
            ``+Infinity``::

                sage: T = Transducer([(0, 0, 1, 0)],
                ....:                on_duplicate_transition=\\\n                ....:                    duplicate_transition_add_input,
                ....:                initial_states=[0],
                ....:                final_states=[0])
                sage: T.moments_waiting_time()
                {'expectation': +Infinity, 'variance': +Infinity}

        #.  Let `h` and `r` be positive integers. We consider random
            strings of letters `1`, `\\ldots`, `r` where the letter `j`
            occurs with probability `p_j`. Let `B` be the random
            variable giving the first position of a block of `h`
            consecutive identical letters. Then

            .. MATH::

                \\begin{aligned}
                \\mathbb{E}(B)&=\\frac1{\\displaystyle\\sum_{i=1}^r
                \\frac1{p_i^{-1}+\\cdots+p_i^{-h}}},\\\\\n                \\mathbb{V}(B)&=\\frac{\\displaystyle\\sum_{i=1}^r\\biggl(
                \\frac{p_i +p_i^h}{1-p_i^h}
                - 2h\\frac{ p_i^h(1-p_i)}{(1-p_i^h)^2}\\biggr)}
                {\\displaystyle\\biggl(\\sum_{i=1}^r
                \\frac1{p_i^{-1}+\\cdots+p_i^{-h}}\\biggr)^2}
                \\end{aligned}

            cf. [S1986]_, p. 62, or [FHP2015]_, Theorem 1. We now
            verify this with a transducer approach.

            ::

                sage: # needs sage.libs.singular
                sage: def test(h, r):
                ....:     R = PolynomialRing(
                ....:             QQ,
                ....:             names=['p_%d' % j for j in range(r)])
                ....:     p = R.gens()
                ....:     def is_zero(polynomial):
                ....:         return polynomial in (sum(p) - 1) * R
                ....:     theory_expectation = 1/(sum(1/sum(p[j]^(-i)
                ....:                     for i in range(1, h+1))
                ....:                     for j in range(r)))
                ....:     theory_variance = sum(
                ....:         (p[i] + p[i]^h)/(1 - p[i]^h)
                ....:         - 2*h*p[i]^h * (1 - p[i])/(1 - p[i]^h)^2
                ....:         for i in range(r)
                ....:         ) * theory_expectation^2
                ....:     alphabet = list(range(r))
                ....:     counters = [
                ....:         transducers.CountSubblockOccurrences([j]*h,
                ....:                     alphabet)
                ....:         for j in alphabet]
                ....:     all_counter = counters[0].cartesian_product(
                ....:         counters[1:])
                ....:     adder = transducers.add(input_alphabet=[0, 1],
                ....:         number_of_operands=r)
                ....:     probabilities = Transducer(
                ....:        [(0, 0, p[j], j) for j in alphabet],
                ....:        initial_states=[0],
                ....:        final_states=[0],
                ....:        on_duplicate_transition=\\\n                ....:            duplicate_transition_add_input)
                ....:     chain = adder(all_counter(probabilities))
                ....:     result = chain.moments_waiting_time(
                ....:        is_zero=is_zero)
                ....:     return is_zero((result['expectation'] -
                ....:                theory_expectation).numerator()) \\\n                ....:            and \\\n                ....:            is_zero((result['variance'] -
                ....:                 theory_variance).numerator())
                sage: test(2, 2)
                True
                sage: test(2, 3)
                True
                sage: test(3, 3)
                True

        #.  Consider the alphabet `\\{0, \\ldots, r-1\\}`, some `1\\le j\\le
            r` and some `h\\ge 1`.  For some probabilities `p_0`,
            `\\ldots`, `p_{r-1}`, we consider infinite words where the
            letters occur independently with the given probabilities.
            The random variable `B_j` is the first position `n` such
            that there exist `j` of the `r` letters having an `h`-run.
            The expectation of `B_j` is given in [FHP2015]_, Theorem 2.
            Here, we verify this result by using transducers::

                sage: # needs sage.libs.singular
                sage: def test(h, r, j):
                ....:     R = PolynomialRing(
                ....:             QQ,
                ....:             names=['p_%d' % i for i in range(r)])
                ....:     p = R.gens()
                ....:     def is_zero(polynomial):
                ....:         return polynomial in (sum(p) - 1) * R
                ....:     alphabet = list(range(r))
                ....:     counters = [
                ....:         transducers.Wait([0, 1])(
                ....:             transducers.CountSubblockOccurrences(
                ....:                 [i]*h,
                ....:                 alphabet))
                ....:         for i in alphabet]
                ....:     all_counter = counters[0].cartesian_product(
                ....:         counters[1:])
                ....:     adder = transducers.add(input_alphabet=[0, 1],
                ....:         number_of_operands=r)
                ....:     threshold = transducers.map(
                ....:         f=lambda x: x >= j,
                ....:         input_alphabet=srange(r+1))
                ....:     probabilities = Transducer(
                ....:         [(0, 0, p[i], i) for i in alphabet],
                ....:         initial_states=[0],
                ....:         final_states=[0],
                ....:         on_duplicate_transition=\\\n                ....:             duplicate_transition_add_input)
                ....:     chain = threshold(adder(all_counter(
                ....:         probabilities)))
                ....:     result = chain.moments_waiting_time(
                ....:         is_zero=is_zero,
                ....:         expectation_only=True)
                ....:     R_v = PolynomialRing(
                ....:             QQ,
                ....:             names=['p_%d' % i for i in range(r)])
                ....:     v = R_v.gens()
                ....:     S = 1/(1 - sum(v[i]/(1+v[i])
                ....:                    for i in range(r)))
                ....:     alpha = [(p[i] - p[i]^h)/(1 - p[i])
                ....:              for i in range(r)]
                ....:     gamma = [p[i]/(1 - p[i]) for i in range(r)]
                ....:     alphabet_set = set(alphabet)
                ....:     expectation = 0
                ....:     for q in range(j):
                ....:         for M in Subsets(alphabet_set, q):
                ....:             summand = S
                ....:             for i in M:
                ....:                 summand = summand.subs(
                ....:                     {v[i]: gamma[i]}) -\\\n                ....:                     summand.subs({v[i]: alpha[i]})
                ....:             for i in alphabet_set - set(M):
                ....:                 summand = summand.subs(
                ....:                     {v[i]: alpha[i]})
                ....:             expectation += summand
                ....:     return is_zero((result - expectation).\\\n                ....:             numerator())
                sage: test(2, 3, 2)
                True

        REFERENCES:

        .. [FGT1992] Philippe Flajolet, Danièle Gardy, Loÿs Thimonier,
           *Birthday paradox, coupon collectors, caching algorithms and
           self-organizing search*, Discrete Appl. Math. 39 (1992),
           207--229, :doi:`10.1016/0166-218X(92)90177-C`.

        .. [FHP2015] Uta Freiberg, Clemens Heuberger, Helmut Prodinger,
           *Application of Smirnov Words to Waiting Time Distributions
           of Runs*, :arxiv:`1503.08096`.

        .. [S1986] Gábor J. Székely, *Paradoxes in Probability Theory
           and Mathematical Statistics*, D. Reidel Publishing Company.

        TESTS:

        Only Markov chains are acceptable::

            sage: T = transducers.Identity([0, 1, 2])
            sage: T.moments_waiting_time()
            Traceback (most recent call last):
            ...
            ValueError: Only Markov chains can compute
            moments_waiting_time.

        There must be a unique initial state::

            sage: T = Transducer([(0, 1, 1, 1), (1, 0, 1, 0)],
            ....:                on_duplicate_transition=\\\n            ....:                    duplicate_transition_add_input)
            sage: T.moments_waiting_time()
            Traceback (most recent call last):
            ...
            ValueError: Unique initial state is required.

        Using `0` as initial state in this example, a `1` is written in
        the first step with probability `1`, so the waiting time is
        always `1`::

            sage: T.state(0).is_initial = True
            sage: T.moments_waiting_time()
            {'expectation': 1, 'variance': 0}

        Using both `0` and `1` as initial states again yields an error
        message::

            sage: T.state(1).is_initial = True
            sage: T.moments_waiting_time()
            Traceback (most recent call last):
            ...
            ValueError: Unique initial state is required.

        Detection of infinite waiting time for symbolic probabilities::

            sage: R.<p, q> = PolynomialRing(QQ)
            sage: T = Transducer([(0, 0, p, 0), (0, 0, q, 0)],
            ....:                initial_states=[0],
            ....:                on_duplicate_transition=\\\n            ....:                    duplicate_transition_add_input)
            sage: T.moments_waiting_time(
            ....:     is_zero=lambda e: e in (p + q - 1)*R)
            {'expectation': +Infinity, 'variance': +Infinity}
        """
    def is_monochromatic(self):
        """
        Check whether the colors of all states are equal.

        OUTPUT: boolean

        EXAMPLES::

            sage: G = transducers.GrayCode()
            sage: [s.color for s in G.iter_states()]
            [None, None, None]
            sage: G.is_monochromatic()
            True
            sage: G.state(1).color = 'blue'
            sage: G.is_monochromatic()
            False
        """
    def language(self, max_length=None, **kwargs) -> Generator[Incomplete]:
        '''
        Return all words that can be written by this transducer.

        INPUT:

        - ``max_length`` -- integer or ``None`` (default). Only
          output words which come from inputs of length at most
          ``max_length`` will be considered. If ``None``, then this
          iterates over all possible words without length restrictions.

        - ``kwargs`` -- will be passed on to the :class:`process
          iterator <FSMProcessIterator>`. See :meth:`process` for a
          description.

        OUTPUT: an iterator

        EXAMPLES::

            sage: NAF = Transducer([(\'I\', 0, 0, None), (\'I\', 1, 1, None),
            ....:                   (0, 0, 0, 0), (0, 1, 1, 0),
            ....:                   (1, 0, 0, 1), (1, 2, 1, -1),
            ....:                   (2, 1, 0, 0), (2, 2, 1, 0)],
            ....:                  initial_states=[\'I\'], final_states=[0],
            ....:                  input_alphabet=[0, 1])
            sage: sorted(NAF.language(4),
            ....:        key=lambda o: (ZZ(o, base=2), len(o)))
            [[], [0], [0, 0], [0, 0, 0],
             [1], [1, 0], [1, 0, 0],
             [0, 1], [0, 1, 0],
             [-1, 0, 1],
             [0, 0, 1],
             [1, 0, 1]]

        ::

            sage: iterator = NAF.language()
            sage: next(iterator)
            []
            sage: next(iterator)
            [0]
            sage: next(iterator)
            [1]
            sage: next(iterator)
            [0, 0]
            sage: next(iterator)
            [0, 1]

        .. SEEALSO::

            :meth:`Automaton.language`,
            :meth:`process`.

        TESTS::

            sage: T = Transducer([(0, 1, 0, \'a\'), (1, 2, 1, \'b\')],
            ....:                initial_states=[0], final_states=[0, 1, 2])
            sage: T.determine_alphabets()
            sage: list(T.language(2))
            [[], [\'a\'], [\'a\', \'b\']]
            sage: list(T.language(3))
            [[], [\'a\'], [\'a\', \'b\']]
            sage: from sage.combinat.finite_state_machine import  _FSMProcessIteratorAll_
            sage: it = T.iter_process(
            ....:     process_iterator_class=_FSMProcessIteratorAll_,
            ....:     max_length=3,
            ....:     process_all_prefixes_of_input=True)
            sage: for current in it:
            ....:     print(current)
            ....:     print("finished: {}".format([branch.output for branch in it._finished_]))
            process (1 branch)
            + at state 1
            +-- tape at 1, [[\'a\']]
            finished: [[]]
            process (1 branch)
            + at state 2
            +-- tape at 2, [[\'a\', \'b\']]
            finished: [[], [\'a\']]
            process (0 branches)
            finished: [[], [\'a\'], [\'a\', \'b\']]
        '''

def is_Automaton(FSM):
    """
    Test whether or not ``FSM`` inherits from :class:`Automaton`.

    TESTS::

        sage: from sage.combinat.finite_state_machine import is_FiniteStateMachine, is_Automaton
        sage: is_Automaton(FiniteStateMachine())
        doctest:warning...
        DeprecationWarning: The function is_Automaton is deprecated; use 'isinstance(..., Automaton)' instead.
        See https://github.com/sagemath/sage/issues/38032 for details.
        False
        sage: is_Automaton(Automaton())
        True
        sage: is_FiniteStateMachine(Automaton())
        doctest:warning...
        DeprecationWarning: The function is_FiniteStateMachine is deprecated; use 'isinstance(..., FiniteStateMachine)' instead.
        See https://github.com/sagemath/sage/issues/38032 for details.
        True
    """

class Automaton(FiniteStateMachine):
    """
    This creates an automaton, which is a finite state machine, whose
    transitions have input labels.

    An automaton has additional features like creating a deterministic
    and a minimized automaton.

    See class :class:`FiniteStateMachine` for more information.

    EXAMPLES:

    We can create an automaton recognizing even numbers (given in
    binary and read from left to right) in the following way::

        sage: A = Automaton([('P', 'Q', 0), ('P', 'P', 1),
        ....:                ('Q', 'P', 1), ('Q', 'Q', 0)],
        ....:               initial_states=['P'], final_states=['Q'])
        sage: A
        Automaton with 2 states
        sage: A([0])
        True
        sage: A([1, 1, 0])
        True
        sage: A([1, 0, 1])
        False

    Note that the full output of the commands can be obtained by
    calling :meth:`.process` and looks like this::

        sage: A.process([1, 0, 1])
        (False, 'P')

    TESTS::

        sage: Automaton()
        Empty automaton
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        Initialize an automaton. See :class:`Automaton` and its parent
        :class:`FiniteStateMachine` for more information.

        TESTS::

            sage: Transducer()._allow_composition_
            True
            sage: Automaton()._allow_composition_
            False
        """
    def intersection(self, other, only_accessible_components: bool = True):
        """
        Return a new automaton which accepts an input if it is
        accepted by both given automata.

        INPUT:

        - ``other`` -- an automaton

        - ``only_accessible_components`` -- if ``True`` (default), then
          the result is piped through :meth:`.accessible_components`. If no
          ``new_input_alphabet`` is given, it is determined by
          :meth:`.determine_alphabets`.

        OUTPUT:

        A new automaton which computes the intersection
        (see below) of the languages of ``self`` and ``other``.

        The set of states of the new automaton is the Cartesian product of the
        set of states of both given automata. There is a transition `((A, B),
        (C, D), a)` in the new automaton if there are transitions `(A, C, a)`
        and `(B, D, a)` in the old automata.

        The methods :meth:`.intersection` and
        :meth:`.cartesian_product` are the same (for automata).

        EXAMPLES::

            sage: aut1 = Automaton([('1', '2', 1),
            ....:                   ('2', '2', 1),
            ....:                   ('2', '2', 0)],
            ....:                  initial_states=['1'],
            ....:                  final_states=['2'],
            ....:                  determine_alphabets=True)
            sage: aut2 = Automaton([('A', 'A', 1),
            ....:                   ('A', 'B', 0),
            ....:                   ('B', 'B', 0),
            ....:                   ('B', 'A', 1)],
            ....:                  initial_states=['A'],
            ....:                  final_states=['B'],
            ....:                  determine_alphabets=True)
            sage: res = aut1.intersection(aut2)
            sage: (aut1([1, 1]), aut2([1, 1]), res([1, 1]))
            (True, False, False)
            sage: (aut1([1, 0]), aut2([1, 0]), res([1, 0]))
            (True, True, True)
            sage: res.transitions()
            [Transition from ('1', 'A') to ('2', 'A'): 1|-,
             Transition from ('2', 'A') to ('2', 'B'): 0|-,
             Transition from ('2', 'A') to ('2', 'A'): 1|-,
             Transition from ('2', 'B') to ('2', 'B'): 0|-,
             Transition from ('2', 'B') to ('2', 'A'): 1|-]

        For automata with epsilon-transitions, intersection is not well
        defined. But for any finite state machine, epsilon-transitions can be
        removed by :meth:`.remove_epsilon_transitions`.

        ::

            sage: a1 = Automaton([(0, 0, 0),
            ....:                 (0, 1, None),
            ....:                 (1, 1, 1),
            ....:                 (1, 2, 1)],
            ....:                 initial_states=[0],
            ....:                 final_states=[1],
            ....:                 determine_alphabets=True)
            sage: a2 = Automaton([(0, 0, 0), (0, 1, 1), (1, 1, 1)],
            ....:                 initial_states=[0],
            ....:                 final_states=[1],
            ....:                 determine_alphabets=True)
            sage: a1.intersection(a2)
            Traceback (most recent call last):
            ...
            ValueError: An epsilon-transition (with empty input)
            was found.
            sage: a1.remove_epsilon_transitions()  # not tested (since not implemented yet)
            sage: a1.intersection(a2)  # not tested
        """
    cartesian_product = intersection
    def determinisation(self):
        """
        Return a deterministic automaton which accepts the same input
        words as the original one.

        OUTPUT: a new automaton, which is deterministic

        The labels of the states of the new automaton are frozensets
        of states of ``self``. The color of a new state is the
        frozenset of colors of the constituent states of ``self``.
        Therefore, the colors of the constituent states have to be
        hashable. However, if all constituent states have color
        ``None``, then the resulting color is ``None``, too.

        The input alphabet must be specified.

        EXAMPLES::

            sage: aut = Automaton([('A', 'A', 0), ('A', 'B', 1), ('B', 'B', 1)],
            ....:                 initial_states=['A'], final_states=['B'])
            sage: aut.determinisation().transitions()
            [Transition from frozenset({'A'}) to frozenset({'A'}): 0|-,
             Transition from frozenset({'A'}) to frozenset({'B'}): 1|-,
             Transition from frozenset({'B'}) to frozenset(): 0|-,
             Transition from frozenset({'B'}) to frozenset({'B'}): 1|-,
             Transition from frozenset() to frozenset(): 0|-,
             Transition from frozenset() to frozenset(): 1|-]

        ::

            sage: A = Automaton([('A', 'A', 1), ('A', 'A', 0), ('A', 'B', 1),
            ....:                ('B', 'C', 0), ('C', 'C', 1), ('C', 'C', 0)],
            ....:               initial_states=['A'], final_states=['C'])
            sage: A.determinisation().states()
            [frozenset({'A'}),
             frozenset({'A', 'B'}),
             frozenset({'A', 'C'}),
             frozenset({'A', 'B', 'C'})]

        ::

            sage: A = Automaton([(0, 1, 1), (0, 2, [1, 1]), (0, 3, [1, 1, 1]),
            ....:                (1, 0, -1), (2, 0, -2), (3, 0, -3)],
            ....:               initial_states=[0], final_states=[0, 1, 2, 3])
            sage: B = A.determinisation().relabeled().coaccessible_components()
            sage: sorted(B.transitions())
            [Transition from 0 to 1: 1|-,
             Transition from 1 to 0: -1|-,
             Transition from 1 to 3: 1|-,
             Transition from 3 to 0: -2|-,
             Transition from 3 to 4: 1|-,
             Transition from 4 to 0: -3|-]

        Note that colors of states have to be hashable::

            sage: A = Automaton([[0, 0, 0]], initial_states=[0])
            sage: A.state(0).color = []
            sage: A.determinisation()
            Traceback (most recent call last):
            ...
            TypeError: unhashable type: 'list'
            sage: A.state(0).color = ()
            sage: A.determinisation()
            Automaton with 1 state

        If the colors of all constituent states are ``None``,
        the resulting color is ``None``, too (:issue:`19199`)::

            sage: A = Automaton([(0, 0, 0)],
            ....:               initial_states=[0],
            ....:               final_states=[0])
            sage: [s.color for s in A.determinisation().iter_states()]
            [None]

        TESTS:

        This is from :issue:`15078`, comment 13.

        ::

            sage: D = {'A': [('A', 'a'), ('B', 'a'), ('A', 'b')],
            ....:      'C': [], 'B': [('C', 'b')]}
            sage: auto = Automaton(D, initial_states=['A'], final_states=['C'])
            sage: auto.is_deterministic()
            False
            sage: auto.process(list('aaab'))
            [(False, 'A'), (True, 'C')]
            sage: auto.states()
            ['A', 'C', 'B']
            sage: Ddet = auto.determinisation()
            sage: Ddet
            Automaton with 3 states
            sage: Ddet.is_deterministic()
            True
            sage: sorted(Ddet.transitions())
            [Transition from frozenset({'A'}) to frozenset({'A', 'B'}): 'a'|-,
             Transition from frozenset({'A'}) to frozenset({'A'}): 'b'|-,
             Transition from frozenset({'A', 'B'}) to frozenset({'A', 'B'}): 'a'|-,
             Transition from frozenset({'A', 'B'}) to frozenset({'A', 'C'}): 'b'|-,
             Transition from frozenset({'A', 'C'}) to frozenset({'A', 'B'}): 'a'|-,
             Transition from frozenset({'A', 'C'}) to frozenset({'A'}): 'b'|-]
            sage: Ddet.initial_states()
            [frozenset({'A'})]
            sage: Ddet.final_states()
            [frozenset({'A', 'C'})]
            sage: Ddet.process(list('aaab'))
            (True, frozenset({'A', 'C'}))

        Test that :issue:`18992` is fixed::

            sage: A = Automaton([(0, 1, []), (1, 1, 0)],
            ....:               initial_states=[0], final_states=[1])
            sage: B = A.determinisation()
            sage: B.initial_states()
            [frozenset({0, 1})]
            sage: B.final_states()
            [frozenset({0, 1}), frozenset({1})]
            sage: B.transitions()
            [Transition from frozenset({0, 1}) to frozenset({1}): 0|-,
             Transition from frozenset({1}) to frozenset({1}): 0|-]
            sage: C = B.minimization().relabeled()
            sage: C.initial_states()
            [0]
            sage: C.final_states()
            [0]
            sage: C.transitions()
            [Transition from 0 to 0: 0|-]
        """
    def minimization(self, algorithm=None):
        """
        Return the minimization of the input automaton as a new automaton.

        INPUT:

        - ``algorithm`` -- either Moore's algorithm (by
          ``algorithm='Moore'`` or as default for deterministic
          automata) or Brzozowski's algorithm (when
          ``algorithm='Brzozowski'`` or when the automaton is not
          deterministic) is used.

        OUTPUT: a new automaton

        The resulting automaton is deterministic and has a minimal
        number of states.

        EXAMPLES::

            sage: A = Automaton([('A', 'A', 1), ('A', 'A', 0), ('A', 'B', 1),
            ....:                ('B', 'C', 0), ('C', 'C', 1), ('C', 'C', 0)],
            ....:               initial_states=['A'], final_states=['C'])
            sage: B = A.minimization(algorithm='Brzozowski')
            sage: B_trans = B.transitions(B.states()[1])
            sage: B_trans # random
            [Transition from frozenset({frozenset({'B', 'C'}),
                                        frozenset({'A', 'C'}),
                                        frozenset({'A', 'B', 'C'})})
                        to frozenset({frozenset({'C'}),
                                      frozenset({'B', 'C'}),
                                      frozenset({'A', 'C'}),
                                      frozenset({'A', 'B', 'C'})}):
                        0|-,
             Transition from frozenset({frozenset({'B', 'C'}),
                                        frozenset({'A', 'C'}),
                                        frozenset({'A', 'B', 'C'})})
                        to frozenset({frozenset({'B', 'C'}),
                                      frozenset({'A', 'C'}),
                                      frozenset({'A', 'B', 'C'})}):
                        1|-]
            sage: len(B.states())
            3
            sage: C = A.minimization(algorithm='Brzozowski')
            sage: C_trans = C.transitions(C.states()[1])
            sage: B_trans == C_trans
            True
            sage: len(C.states())
            3

        ::

            sage: aut = Automaton([('1', '2', 'a'), ('2', '3', 'b'),
            ....:                  ('3', '2', 'a'), ('2', '1', 'b'),
            ....:                  ('3', '4', 'a'), ('4', '3', 'b')],
            ....:                  initial_states=['1'], final_states=['1'])
            sage: min = aut.minimization(algorithm='Brzozowski')
            sage: [len(min.states()), len(aut.states())]
            [3, 4]
            sage: min = aut.minimization(algorithm='Moore')
            Traceback (most recent call last):
            ...
            NotImplementedError: Minimization via Moore's Algorithm is only
            implemented for deterministic finite state machines
        """
    def complement(self):
        """
        Return the complement of this automaton.

        OUTPUT: an :class:`Automaton`

        If this automaton recognizes language `\\mathcal{L}` over an
        input alphabet `\\mathcal{A}`, then the complement recognizes
        `\\mathcal{A}\\setminus\\mathcal{L}`.

        EXAMPLES::

            sage: A = automata.Word([0, 1])
            sage: [w for w in ([], [0], [1], [0, 0], [0, 1], [1, 0], [1, 1])
            ....:  if A(w)]
            [[0, 1]]
            sage: Ac = A.complement()
            sage: Ac.transitions()
            [Transition from 0 to 1: 0|-,
             Transition from 0 to 3: 1|-,
             Transition from 2 to 3: 0|-,
             Transition from 2 to 3: 1|-,
             Transition from 1 to 2: 1|-,
             Transition from 1 to 3: 0|-,
             Transition from 3 to 3: 0|-,
             Transition from 3 to 3: 1|-]
            sage: [w for w in ([], [0], [1], [0, 0], [0, 1], [1, 0], [1, 1])
            ....:  if Ac(w)]
            [[], [0], [1], [0, 0], [1, 0], [1, 1]]

        The automaton must be deterministic::

            sage: A = automata.Word([0]) * automata.Word([1])
            sage: A.complement()
            Traceback (most recent call last):
            ...
            ValueError: The finite state machine must be deterministic.
            sage: Ac = A.determinisation().complement()
            sage: [w for w in ([], [0], [1], [0, 0], [0, 1], [1, 0], [1, 1])
            ....:  if Ac(w)]
            [[], [0], [1], [0, 0], [1, 0], [1, 1]]
        """
    def is_equivalent(self, other):
        """
        Test whether two automata are equivalent, i.e., accept the same
        language.

        INPUT:

        - ``other`` -- an :class:`Automaton`

        EXAMPLES::

            sage: A = Automaton([(0, 0, 0), (0, 1, 1), (1, 0, 1)],
            ....:               initial_states=[0],
            ....:               final_states=[0])
            sage: B = Automaton([('a', 'a', 0), ('a', 'b', 1), ('b', 'a', 1)],
            ....:               initial_states=['a'],
            ....:               final_states=['a'])
            sage: A.is_equivalent(B)
            True
            sage: B.add_transition('b', 'a', 0)
            Transition from 'b' to 'a': 0|-
            sage: A.is_equivalent(B)
            False
        """
    def process(self, *args, **kwargs):
        """
        Return whether the automaton accepts the input and the state
        where the computation stops.

        INPUT:

        - ``input_tape`` -- the input tape can be a list or an
          iterable with entries from the input alphabet. If we are
          working with a multi-tape machine (see parameter
          ``use_multitape_input`` and notes below), then the tape is a
          list or tuple of tracks, each of which can be a list or an
          iterable with entries from the input alphabet.

        - ``initial_state`` or ``initial_states`` -- the initial
          state(s) in which the machine starts. Either specify a
          single one with ``initial_state`` or a list of them with
          ``initial_states``. If both are given, ``initial_state``
          will be appended to ``initial_states``. If neither is
          specified, the initial states of the finite state machine
          are taken.

        - ``list_of_outputs`` -- (default: ``None``) a boolean or
          ``None``. If ``True``, then the outputs are given in list form
          (even if we have no or only one single output). If
          ``False``, then the result is never a list (an exception is
          raised if the result cannot be returned). If
          ``list_of_outputs=None`` the method determines automatically
          what to do (e.g. if a non-deterministic machine returns more
          than one path, then the output is returned in list form).

        - ``only_accepted`` -- boolean (default: ``False``); if set,
          then the first argument in the output is guaranteed to be
          ``True`` (if the output is a list, then the first argument
          of each element will be ``True``).

        - ``full_output`` -- boolean (default: ``True``); if set,
          then the full output is given, otherwise only whether the
          sequence is accepted or not (the first entry below only).

        - ``always_include_output`` -- if set (not by default), always
          return a triple containing the (non-existing) output. This
          is in order to obtain output compatible with that of
          :meth:`FiniteStateMachine.process`. If this parameter is set,
          ``full_output`` has no effect.

        - ``format_output`` -- a function that translates the written
          output (which is in form of a list) to something more
          readable. By default (``None``) identity is used here.

        - ``check_epsilon_transitions`` -- boolean (default: ``True``); a
          boolean. If ``False``, then epsilon transitions are not taken into
          consideration during process.

        - ``write_final_word_out`` -- boolean (default: ``True``); whether the
          final output words should be written or not

        - ``use_multitape_input`` -- boolean (default: ``False``); if ``True``,
          then the multi-tape mode of the process iterator is activated. See
          also the notes below for multi-tape machines.

        - ``process_all_prefixes_of_input`` -- boolean (default: ``False``); if
          ``True``, then each prefix of the input word is processed (instead of
          processing the whole input word at once). Consequently, there is an
          output generated for each of these prefixes.

        - ``process_iterator_class`` -- (default: ``None``) a class
          inherited from :class:`FSMProcessIterator`. If ``None``,
          then :class:`FSMProcessIterator` is taken. An instance of this
          class is created and is used during the processing.

        OUTPUT:

        The full output is a pair (or a list of pairs,
        cf. parameter ``list_of_outputs``), where

        - the first entry is ``True`` if the input string is accepted and

        - the second gives the state reached after processing the
          input tape (This is a state with label ``None`` if the input
          could not be processed, i.e., if at one point no
          transition to go on could be found.).

        If ``full_output`` is ``False``, then only the first entry
        is returned.

        If ``always_include_output`` is set, an additional third entry
        ``[]`` is included.

        Note that in the case the automaton is not
        deterministic, all possible paths are taken into account.
        You can use :meth:`.determinisation` to get a deterministic
        automaton machine.

        This function uses an iterator which, in its simplest form, goes
        from one state to another in each step. To decide which way to
        go, it uses the input words of the outgoing transitions and
        compares them to the input tape. More precisely, in each step,
        the iterator takes an outgoing transition of the current state,
        whose input label equals the input letter of the tape.

        If the choice of the outgoing transition is not unique (i.e.,
        we have a non-deterministic finite state machine), all
        possibilities are followed. This is done by splitting the
        process into several branches, one for each of the possible
        outgoing transitions.

        The process (iteration) stops if all branches are finished,
        i.e., for no branch, there is any transition whose input word
        coincides with the processed input tape. This can simply
        happen when the entire tape was read.

        Also see :meth:`~FiniteStateMachine.__call__` for a
        version of :meth:`.process` with shortened output.

        Internally this function creates and works with an instance of
        :class:`FSMProcessIterator`. This iterator can also be obtained
        with :meth:`~FiniteStateMachine.iter_process`.

        If working with multi-tape finite state machines, all input
        words of transitions are words of `k`-tuples of letters.
        Moreover, the input tape has to consist of `k` tracks, i.e.,
        be a list or tuple of `k` iterators, one for each track.

        .. WARNING::

            Working with multi-tape finite state machines is still
            experimental and can lead to wrong outputs.

        EXAMPLES:

        In the following examples, we construct an automaton which
        accepts non-adjacent forms (see also the example on
        :ref:`non-adjacent forms <finite_state_machine_recognizing_NAFs_example>`
        in the documentation of the module
        :doc:`finite_state_machine`)
        and then test it by feeding it with several binary digit
        expansions.

        ::

            sage: NAF = Automaton(
            ....:     {'_': [('_', 0), ('1', 1)], '1': [('_', 0)]},
            ....:     initial_states=['_'], final_states=['_', '1'])
            sage: [NAF.process(w) for w in [[0], [0, 1], [1, 1], [0, 1, 0, 1],
            ....:                           [0, 1, 1, 1, 0], [1, 0, 0, 1, 1]]]
            [(True, '_'), (True, '1'), (False, None),
             (True, '1'), (False, None), (False, None)]

        If we just want a condensed output, we use::

            sage: [NAF.process(w, full_output=False)
            ....:     for w in [[0], [0, 1], [1, 1], [0, 1, 0, 1],
            ....:               [0, 1, 1, 1, 0], [1, 0, 0, 1, 1]]]
            [True, True, False, True, False, False]

        It is equivalent to::

            sage: [NAF(w) for w in [[0], [0, 1], [1, 1], [0, 1, 0, 1],
            ....:                   [0, 1, 1, 1, 0], [1, 0, 0, 1, 1]]]
            [True, True, False, True, False, False]

        The following example illustrates the difference between
        non-existing paths and reaching a non-final state::

            sage: NAF.process([2])
            (False, None)
            sage: NAF.add_transition(('_', 's', 2))
            Transition from '_' to 's': 2|-
            sage: NAF.process([2])
            (False, 's')

        A simple example of a (non-deterministic) multi-tape automaton is the
        following: It checks whether the two input tapes have the same number
        of ones::

            sage: M = Automaton([('=', '=', (1, 1)),
            ....:                ('=', '=', (None, 0)),
            ....:                ('=', '=', (0, None)),
            ....:                ('=', '<', (None, 1)),
            ....:                ('<', '<', (None, 1)),
            ....:                ('<', '<', (None, 0)),
            ....:                ('=', '>', (1, None)),
            ....:                ('>', '>', (1, None)),
            ....:                ('>', '>', (0, None))],
            ....:               initial_states=['='],
            ....:               final_states=['='])
            sage: M.process(([1, 0, 1], [1, 0]), use_multitape_input=True)
            (False, '>')
            sage: M.process(([0, 1, 0], [0, 1, 1]), use_multitape_input=True)
            (False, '<')
            sage: M.process(([1, 1, 0, 1], [0, 0, 1, 0, 1, 1]),
            ....:           use_multitape_input=True)
            (True, '=')

        Alternatively, we can use the following (non-deterministic)
        multi-tape automaton for the same check::

            sage: N = Automaton([('=', '=', (0, 0)),
            ....:                ('=', '<', (None, 1)),
            ....:                ('<', '<', (0, None)),
            ....:                ('<', '=', (1, None)),
            ....:                ('=', '>', (1, None)),
            ....:                ('>', '>', (None, 0)),
            ....:                ('>', '=', (None, 1))],
            ....:               initial_states=['='],
            ....:               final_states=['='])
            sage: N.process(([1, 0, 1], [1, 0]), use_multitape_input=True)
            (False, '>')
            sage: N.process(([0, 1, 0], [0, 1, 1]), use_multitape_input=True)
            (False, '<')
            sage: N.process(([1, 1, 0, 1], [0, 0, 1, 0, 1, 1]),
            ....:           use_multitape_input=True)
            (True, '=')

        .. SEEALSO::

            :meth:`FiniteStateMachine.process`,
            :meth:`Transducer.process`,
            :meth:`~FiniteStateMachine.iter_process`,
            :meth:`~FiniteStateMachine.__call__`,
            :class:`FSMProcessIterator`.
        """
    def shannon_parry_markov_chain(self):
        '''
        Compute a time homogeneous Markov chain such that all words of a
        given length recognized by the original automaton occur as the
        output with the same weight; the transition probabilities
        correspond to the Parry measure.

        OUTPUT:

        A Markov chain. Its input labels are the transition probabilities, the
        output labels the labels of the original automaton. In order to obtain
        equal weight for all words of the same length, an "exit weight" is
        needed. It is stored in the attribute ``color`` of the states of the
        Markov chain. The weights of the words of the same length sum up to one
        up to an exponentially small error.

        The stationary distribution of this Markov chain is
        saved as the initial probabilities of the states.

        The transition probabilities correspond to the Parry measure
        (see [S1948]_ and [P1964]_).

        The automaton is assumed to be deterministic, irreducible and
        aperiodic. All states must be final.

        EXAMPLES::

            sage: NAF = Automaton([(0, 0, 0), (0, 1, 1), (0, 1, -1),
            ....:                  (1, 0, 0)], initial_states=[0],
            ....:                 final_states=[0, 1])
            sage: P_NAF = NAF.shannon_parry_markov_chain()                              # needs sage.symbolic
            sage: P_NAF.transitions()                                                   # needs sage.symbolic
            [Transition from 0 to 0: 1/2|0,
             Transition from 0 to 1: 1/4|1,
             Transition from 0 to 1: 1/4|-1,
             Transition from 1 to 0: 1|0]
            sage: for s in P_NAF.iter_states():                                         # needs sage.symbolic
            ....:     print(s.color)
            3/4
            3/2

        The stationary distribution is also computed and saved as the
        initial probabilities of the returned Markov chain::

            sage: for s in P_NAF.states():                                              # needs sage.symbolic
            ....:     print("{} {}".format(s, s.initial_probability))
            0 2/3
            1 1/3

        The automaton is assumed to be deterministic, irreducible and aperiodic::

            sage: A = Automaton([(0, 0, 0), (0, 1, 1), (1, 1, 1), (1, 1, 0)],
            ....:               initial_states=[0])
            sage: A.shannon_parry_markov_chain()
            Traceback (most recent call last):
            ...
            NotImplementedError: Automaton must be strongly connected.
            sage: A = Automaton([(0, 0, 0), (0, 1, 0)],
            ....:               initial_states=[0])
            sage: A.shannon_parry_markov_chain()
            Traceback (most recent call last):
            ...
            NotImplementedError: Automaton must be deterministic.
            sage: A = Automaton([(0, 1, 0), (1, 0, 0)],
            ....:               initial_states=[0])
            sage: A.shannon_parry_markov_chain()
            Traceback (most recent call last):
            ...
            NotImplementedError: Automaton must be aperiodic.

        All states must be final::

            sage: A = Automaton([(0, 1, 0), (0, 0, 1), (1, 0, 0)],
            ....:               initial_states=[0])
            sage: A.shannon_parry_markov_chain()
            Traceback (most recent call last):
            ...
            NotImplementedError: All states must be final.

        ALGORITHM:

        See [HKP2015a]_, Lemma 4.1.

        REFERENCES:

        .. [HKP2015a] Clemens Heuberger, Sara Kropf, and Helmut
           Prodinger, *Analysis of Carries in Signed Digit Expansions*,
           :arxiv:`1503.08816`.
        .. [P1964] William Parry, *Intrinsic Markov chains*, Transactions
           of the American Mathematical Society 112, 1964, pp. 55-66.
           :doi:`10.1090/S0002-9947-1964-0161372-1`.
        .. [S1948] Claude E. Shannon, *A mathematical theory of communication*,
           The Bell System Technical Journal 27, 1948, 379-423,
           :doi:`10.1002/j.1538-7305.1948.tb01338.x`.
        '''
    def with_output(self, word_out_function=None):
        """
        Construct a transducer out of this automaton.

        INPUT:

        - ``word_out_function`` -- (default: ``None``) a function. It
          transforms a :class:`transition <FSMTransition>` to the
          output word for this transition.

          If this is ``None``, then the output word will be equal to
          the input word of each transition.

        OUTPUT: a transducer

        EXAMPLES::

            sage: A = Automaton([(0, 0, 'A'), (0, 1, 'B'), (1, 2, 'C')])
            sage: T = A.with_output(); T
            Transducer with 3 states
            sage: T.transitions()
            [Transition from 0 to 0: 'A'|'A',
             Transition from 0 to 1: 'B'|'B',
             Transition from 1 to 2: 'C'|'C']

        This result is in contrast to::

            sage: Transducer(A).transitions()
            [Transition from 0 to 0: 'A'|-,
             Transition from 0 to 1: 'B'|-,
             Transition from 1 to 2: 'C'|-]

        where no output labels are created.

        Here is another example::

            sage: T2 = A.with_output(lambda t: [c.lower() for c in t.word_in])
            sage: T2.transitions()
            [Transition from 0 to 0: 'A'|'a',
             Transition from 0 to 1: 'B'|'b',
             Transition from 1 to 2: 'C'|'c']

        We can obtain the same result by composing two transducers. As inner
        transducer of the composition, we use :meth:`.with_output`
        without the optional argument
        ``word_out_function`` (which makes the output of each
        transition equal to its input); as outer transducer we use a
        :meth:`map-transducer
        <sage.combinat.finite_state_machine_generators.TransducerGenerators.map>`
        (for converting to lower case).
        This gives

        ::

            sage: L = transducers.map(lambda x: x.lower(), ['A', 'B', 'C'])
            sage: L.composition(A.with_output()).relabeled().transitions()
            [Transition from 0 to 0: 'A'|'a',
             Transition from 0 to 1: 'B'|'b',
             Transition from 1 to 2: 'C'|'c']

        .. SEEALSO::

           :meth:`.input_projection`,
           :meth:`.output_projection`,
           :class:`Transducer`,
           :meth:`transducers.map()
           <sage.combinat.finite_state_machine_generators.TransducerGenerators.map>`.

        TESTS::

            sage: A.with_output().input_projection() == A
            True
            sage: NAF = Automaton(
            ....:     {'A': [('A', 0), ('B', 1), ('B', -1)], 'B': [('A', 0)]})
            sage: NAF.with_output().input_projection() == NAF
            True
            sage: B = Automaton(
            ....:     {0: [(0, 'a'), (1, ['b', 'c']), (2, ['d', 'e'])],
            ....:      1: [(0, ['f', 'g']), (1, 'h'), (2, None)],
            ....:      2: [(0, None), (1, None), (2, ['i', 'j'])]},
            ....:     initial_states=[1, 2], final_states=[0])
            sage: B.with_output(lambda t: [c.upper() for c in t.word_in]).input_projection() == B
            True
        """
    def language(self, max_length=None, **kwargs):
        """
        Return all words accepted by this automaton.

        INPUT:

        - ``max_length`` -- integer or ``None`` (default). Only
          inputs of length at most ``max_length`` will be
          considered. If ``None``, then this iterates over all
          possible words without length restrictions.

        - ``kwargs`` -- will be passed on to the :class:`process
          iterator <FSMProcessIterator>`. See :meth:`process` for a
          description.

        OUTPUT: an iterator

        EXAMPLES::

            sage: NAF = Automaton(
            ....:     {'A': [('A', 0), ('B', 1), ('B', -1)],
            ....:      'B': [('A', 0)]},
            ....:     initial_states=['A'], final_states=['A', 'B'])
            sage: list(NAF.language(3))
            [[],
             [0], [-1], [1],
             [-1, 0], [0, 0], [1, 0], [0, -1], [0, 1],
             [-1, 0, 0], [0, -1, 0], [0, 0, 0], [0, 1, 0], [1, 0, 0],
             [-1, 0, -1], [-1, 0, 1], [0, 0, -1],
             [0, 0, 1], [1, 0, -1], [1, 0, 1]]

        .. SEEALSO::

            :meth:`FiniteStateMachine.language`,
            :meth:`process`.

        TESTS::

            sage: def R(ell):
            ....:     return (2^(ell+2)-(-1)^ell)/3
            sage: import itertools
            sage: all(len(list(NAFs)) == R(ell) for ell, NAFs in
            ....:     itertools.groupby(NAF.language(5), key=len))
            True
        """

def is_Transducer(FSM):
    """
    Test whether or not ``FSM`` inherits from :class:`Transducer`.

    TESTS::

        sage: from sage.combinat.finite_state_machine import is_FiniteStateMachine, is_Transducer
        sage: is_Transducer(FiniteStateMachine())
        doctest:warning...
        DeprecationWarning: The function is_Transducer is deprecated; use 'isinstance(..., Transducer)' instead.
        See https://github.com/sagemath/sage/issues/38032 for details.
        False
        sage: is_Transducer(Transducer())
        True
        sage: is_FiniteStateMachine(Transducer())
        doctest:warning...
        DeprecationWarning: The function is_FiniteStateMachine is deprecated; use 'isinstance(..., FiniteStateMachine)' instead.
        See https://github.com/sagemath/sage/issues/38032 for details.
        True
    """

class Transducer(FiniteStateMachine):
    """
    This creates a transducer, which is a finite state machine, whose
    transitions have input and output labels.

    A transducer has additional features like creating a simplified
    transducer.

    See class :class:`FiniteStateMachine` for more information.

    EXAMPLES:

    We can create a transducer performing the addition of 1 (for
    numbers given in binary and read from right to left) in the
    following way::

        sage: T = Transducer([('C', 'C', 1, 0), ('C', 'N', 0, 1),
        ....:                 ('N', 'N', 0, 0), ('N', 'N', 1, 1)],
        ....:                initial_states=['C'], final_states=['N'])
        sage: T
        Transducer with 2 states
        sage: T([0])
        [1]
        sage: T([1,1,0])
        [0, 0, 1]
        sage: ZZ(T(15.digits(base=2)+[0]), base=2)
        16

    Note that we have padded the binary input sequence by a `0` so
    that the transducer can reach its final state.

    TESTS::

        sage: Transducer()
        Empty transducer
    """
    def intersection(self, other, only_accessible_components: bool = True):
        """
        Return a new transducer which accepts an input if it is accepted by
        both given finite state machines producing the same output.

        INPUT:

        - ``other`` -- a transducer

        - ``only_accessible_components`` -- if ``True`` (default), then
          the result is piped through :meth:`.accessible_components`. If no
          ``new_input_alphabet`` is given, it is determined by
          :meth:`.determine_alphabets`.

        OUTPUT:

        A new transducer which computes the intersection
        (see below) of the languages of ``self`` and ``other``.

        The set of states of the transducer is the Cartesian product of the
        set of states of both given transducer. There is a transition `((A,
        B), (C, D), a, b)` in the new transducer if there are
        transitions `(A, C, a, b)` and `(B, D, a, b)` in the old transducers.

        EXAMPLES::

            sage: transducer1 = Transducer([('1', '2', 1, 0),
            ....:                           ('2', '2', 1, 0),
            ....:                           ('2', '2', 0, 1)],
            ....:                          initial_states=['1'],
            ....:                          final_states=['2'])
            sage: transducer2 = Transducer([('A', 'A', 1, 0),
            ....:                           ('A', 'B', 0, 0),
            ....:                           ('B', 'B', 0, 1),
            ....:                           ('B', 'A', 1, 1)],
            ....:                          initial_states=['A'],
            ....:                          final_states=['B'])
            sage: res = transducer1.intersection(transducer2)
            sage: res.transitions()
            [Transition from ('1', 'A') to ('2', 'A'): 1|0,
             Transition from ('2', 'A') to ('2', 'A'): 1|0]

        In general, transducers are not closed under intersection. But
        for transducer which do not have epsilon-transitions, the
        intersection is well defined (cf. [BaWo2012]_). However, in
        the next example the intersection of the two transducers is
        not well defined. The intersection of the languages consists
        of `(a^n, b^n c^n)`. This set is not recognizable by a
        *finite* transducer.

        ::

            sage: t1 = Transducer([(0, 0, 'a', 'b'),
            ....:                  (0, 1, None, 'c'),
            ....:                  (1, 1, None, 'c')],
            ....:                 initial_states=[0],
            ....:                 final_states=[0, 1])
            sage: t2 = Transducer([('A', 'A', None, 'b'),
            ....:                  ('A', 'B', 'a', 'c'),
            ....:                  ('B', 'B', 'a', 'c')],
            ....:                 initial_states=['A'],
            ....:                 final_states=['A', 'B'])
            sage: t2.intersection(t1)
            Traceback (most recent call last):
            ...
            ValueError: An epsilon-transition (with empty input or output)
            was found.

        TESTS::

            sage: transducer1 = Transducer([('1', '2', 1, 0)],
            ....:                          initial_states=['1'],
            ....:                          final_states=['2'])
            sage: transducer2 = Transducer([('A', 'B', 1, 0)],
            ....:                          initial_states=['A'],
            ....:                          final_states=['B'])
            sage: res = transducer1.intersection(transducer2)
            sage: res.final_states()
            [('2', 'B')]
            sage: transducer1.state('2').final_word_out = 1
            sage: transducer2.state('B').final_word_out = 2
            sage: res = transducer1.intersection(transducer2)
            sage: res.final_states()
            []

        REFERENCES:

        .. [BaWo2012] Javier Baliosian and Dina Wonsever, *Finite State
           Transducers*, chapter in *Handbook of Finite State Based Models and
           Applications*, edited by Jiacun Wang, Chapman and Hall/CRC, 2012.
        """
    def cartesian_product(self, other, only_accessible_components: bool = True):
        """
        Return a new transducer which can simultaneously process an
        input with the machines ``self`` and ``other`` where the
        output labels are `d`-tuples of the original output labels.

        INPUT:

        - ``other`` -- a finite state machine (if `d=2`) or a list (or
          other iterable) of `d-1` finite state machines

        - ``only_accessible_components`` -- if ``True`` (default), then
          the result is piped through :meth:`.accessible_components`. If no
          ``new_input_alphabet`` is given, it is determined by
          :meth:`.determine_alphabets`.

        OUTPUT:

        A transducer which can simultaneously process an input with ``self``
        and the machine(s) in ``other``.

        The set of states of the new transducer is the Cartesian product of
        the set of states of ``self`` and ``other``.

        Let `(A_j, B_j, a_j, b_j)` for `j\\in\\{1, \\ldots, d\\}` be
        transitions in the machines ``self`` and in ``other``. Then
        there is a transition `((A_1, \\ldots, A_d), (B_1, \\ldots,
        B_d), a, (b_1, \\ldots, b_d))` in the new transducer if `a_1 =
        \\cdots = a_d =: a`.

        EXAMPLES::

            sage: transducer1 = Transducer([('A', 'A', 0, 0),
            ....:                           ('A', 'A', 1, 1)],
            ....:                          initial_states=['A'],
            ....:                          final_states=['A'],
            ....:                          determine_alphabets=True)
            sage: transducer2 = Transducer([(0, 1, 0, ['b', 'c']),
            ....:                           (0, 0, 1, 'b'),
            ....:                           (1, 1, 0, 'a')],
            ....:                          initial_states=[0],
            ....:                          final_states=[1],
            ....:                          determine_alphabets=True)
            sage: result = transducer1.cartesian_product(transducer2)
            sage: result
            Transducer with 2 states
            sage: result.transitions()
            [Transition from ('A', 0) to ('A', 1): 0|(0, 'b'),(None, 'c'),
             Transition from ('A', 0) to ('A', 0): 1|(1, 'b'),
             Transition from ('A', 1) to ('A', 1): 0|(0, 'a')]
            sage: result([1, 0, 0])
            [(1, 'b'), (0, 'b'), (None, 'c'),  (0, 'a')]
            sage: (transducer1([1, 0, 0]), transducer2([1, 0, 0]))
            ([1, 0, 0], ['b', 'b', 'c', 'a'])

        Also final output words are correctly processed::

            sage: transducer1.state('A').final_word_out = 2
            sage: result = transducer1.cartesian_product(transducer2)
            sage: result.final_states()[0].final_word_out
            [(2, None)]

        The following transducer counts the number of 11 blocks minus
        the number of 10 blocks over the alphabet ``[0, 1]``.

        ::

            sage: count_11 = transducers.CountSubblockOccurrences(
            ....:     [1, 1],
            ....:     input_alphabet=[0, 1])
            sage: count_10 = transducers.CountSubblockOccurrences(
            ....:     [1, 0],
            ....:     input_alphabet=[0, 1])
            sage: count_11x10 = count_11.cartesian_product(count_10)
            sage: difference = transducers.sub([0, 1])(count_11x10)
            sage: T = difference.simplification().relabeled()
            sage: T.initial_states()
            [1]
            sage: sorted(T.transitions())
            [Transition from 0 to 1: 0|-1,
             Transition from 0 to 0: 1|1,
             Transition from 1 to 1: 0|0,
             Transition from 1 to 0: 1|0]
            sage: input =  [0, 1, 1,  0, 1,  0, 0, 0, 1, 1, 1,  0]
            sage: output = [0, 0, 1, -1, 0, -1, 0, 0, 0, 1, 1, -1]
            sage: T(input) == output
            True

        If ``other`` is an automaton, then :meth:`.cartesian_product` returns
        ``self`` where the input is restricted to the input accepted by
        ``other``.

        For example, if the transducer transforms the standard
        binary expansion into the non-adjacent form and the automaton
        recognizes the binary expansion without adjacent ones, then the
        Cartesian product of these two is a transducer which does not change
        the input (except for changing ``a`` to ``(a, None)`` and ignoring a
        leading `0`).

        ::

            sage: NAF = Transducer([(0, 1, 0, None),
            ....:                   (0, 2, 1, None),
            ....:                   (1, 1, 0, 0),
            ....:                   (1, 2, 1, 0),
            ....:                   (2, 1, 0, 1),
            ....:                   (2, 3, 1, -1),
            ....:                   (3, 2, 0, 0),
            ....:                   (3, 3, 1, 0)],
            ....:                  initial_states=[0],
            ....:                  final_states=[1],
            ....:                  determine_alphabets=True)
            sage: aut11 = Automaton([(0, 0, 0), (0, 1, 1), (1, 0, 0)],
            ....:                   initial_states=[0],
            ....:                   final_states=[0, 1],
            ....:                   determine_alphabets=True)
            sage: res = NAF.cartesian_product(aut11)
            sage: res([1, 0, 0, 1, 0, 1, 0])
            [(1, None), (0, None), (0, None), (1, None), (0, None), (1, None)]

        This is obvious because if the standard binary expansion does not have
        adjacent ones, then it is the same as the non-adjacent form.

        Be aware that :meth:`.cartesian_product` is not commutative.

        ::

            sage: aut11.cartesian_product(NAF)
            Traceback (most recent call last):
            ...
            TypeError: Only an automaton can be intersected with an automaton.

        The Cartesian product of more than two finite state machines can also
        be computed::

            sage: T0 = transducers.CountSubblockOccurrences([0, 0], [0, 1, 2])
            sage: T1 = transducers.CountSubblockOccurrences([1, 1], [0, 1, 2])
            sage: T2 = transducers.CountSubblockOccurrences([2, 2], [0, 1, 2])
            sage: T = T0.cartesian_product([T1, T2])
            sage: T.transitions()
            [Transition from ((), (), ()) to ((0,), (), ()): 0|(0, 0, 0),
             Transition from ((), (), ()) to ((), (1,), ()): 1|(0, 0, 0),
             Transition from ((), (), ()) to ((), (), (2,)): 2|(0, 0, 0),
             Transition from ((0,), (), ()) to ((0,), (), ()): 0|(1, 0, 0),
             Transition from ((0,), (), ()) to ((), (1,), ()): 1|(0, 0, 0),
             Transition from ((0,), (), ()) to ((), (), (2,)): 2|(0, 0, 0),
             Transition from ((), (1,), ()) to ((0,), (), ()): 0|(0, 0, 0),
             Transition from ((), (1,), ()) to ((), (1,), ()): 1|(0, 1, 0),
             Transition from ((), (1,), ()) to ((), (), (2,)): 2|(0, 0, 0),
             Transition from ((), (), (2,)) to ((0,), (), ()): 0|(0, 0, 0),
             Transition from ((), (), (2,)) to ((), (1,), ()): 1|(0, 0, 0),
             Transition from ((), (), (2,)) to ((), (), (2,)): 2|(0, 0, 1)]
            sage: T([0, 0, 1, 1, 2, 2, 0, 1, 2, 2])
            [(0, 0, 0),
             (1, 0, 0),
             (0, 0, 0),
             (0, 1, 0),
             (0, 0, 0),
             (0, 0, 1),
             (0, 0, 0),
             (0, 0, 0),
             (0, 0, 0),
             (0, 0, 1)]
        """
    def simplification(self):
        '''
        Return a simplified transducer.

        OUTPUT: a new transducer

        This function simplifies a transducer by Moore\'s algorithm,
        first moving common output labels of transitions leaving a
        state to output labels of transitions entering the state
        (cf. :meth:`.prepone_output`).

        The resulting transducer implements the same function as the
        original transducer.

        EXAMPLES::

            sage: fsm = Transducer([("A", "B", 0, 1), ("A", "B", 1, 0),
            ....:                           ("B", "C", 0, 0), ("B", "C", 1, 1),
            ....:                           ("C", "D", 0, 1), ("C", "D", 1, 0),
            ....:                           ("D", "A", 0, 0), ("D", "A", 1, 1)])
            sage: fsms = fsm.simplification()
            sage: fsms
            Transducer with 2 states
            sage: fsms.transitions()
            [Transition from (\'B\', \'D\') to (\'A\', \'C\'): 0|0,
             Transition from (\'B\', \'D\') to (\'A\', \'C\'): 1|1,
             Transition from (\'A\', \'C\') to (\'B\', \'D\'): 0|1,
             Transition from (\'A\', \'C\') to (\'B\', \'D\'): 1|0]
            sage: fsms.relabeled().transitions()
            [Transition from 0 to 1: 0|0,
             Transition from 0 to 1: 1|1,
             Transition from 1 to 0: 0|1,
             Transition from 1 to 0: 1|0]

        ::

            sage: fsm = Transducer([("A", "A", 0, 0),
            ....:                   ("A", "B", 1, 1),
            ....:                   ("A", "C", 1, -1),
            ....:                   ("B", "A", 2, 0),
            ....:                   ("C", "A", 2, 0)])
            sage: fsm_simplified = fsm.simplification()
            sage: fsm_simplified
            Transducer with 2 states
            sage: fsm_simplified.transitions()
            [Transition from (\'A\',) to (\'A\',): 0|0,
             Transition from (\'A\',) to (\'B\', \'C\'): 1|1,0,
             Transition from (\'A\',) to (\'B\', \'C\'): 1|-1,0,
             Transition from (\'B\', \'C\') to (\'A\',): 2|-]

        ::

            sage: from sage.combinat.finite_state_machine import duplicate_transition_add_input
            sage: T = Transducer([(\'A\', \'A\', 1/2, 0),
            ....:                 (\'A\', \'B\', 1/4, 1),
            ....:                 (\'A\', \'C\', 1/4, 1),
            ....:                 (\'B\', \'A\', 1, 0),
            ....:                 (\'C\', \'A\', 1, 0)],
            ....:                initial_states=[0],
            ....:                final_states=[\'A\', \'B\', \'C\'],
            ....:                on_duplicate_transition=duplicate_transition_add_input)
            sage: sorted(T.simplification().transitions())
            [Transition from (\'A\',) to (\'A\',): 1/2|0,
             Transition from (\'A\',) to (\'B\', \'C\'): 1/2|1,
             Transition from (\'B\', \'C\') to (\'A\',): 1|0]

        Illustrating the use of colors in order to avoid identification of states::

            sage: T = Transducer( [[0,0,0,0], [0,1,1,1],
            ....:                  [1,0,0,0], [1,1,1,1]],
            ....:                 initial_states=[0],
            ....:                 final_states=[0,1])
            sage: sorted(T.simplification().transitions())
            [Transition from (0, 1) to (0, 1): 0|0,
             Transition from (0, 1) to (0, 1): 1|1]
            sage: T.state(0).color = 0
            sage: T.state(0).color = 1
            sage: sorted(T.simplification().transitions())
            [Transition from (0,) to (0,): 0|0,
             Transition from (0,) to (1,): 1|1,
             Transition from (1,) to (0,): 0|0,
             Transition from (1,) to (1,): 1|1]
        '''
    def process(self, *args, **kwargs):
        """
        Return whether the transducer accepts the input, the state
        where the computation stops and which output is generated.

        INPUT:

        - ``input_tape`` -- the input tape can be a list or an
          iterable with entries from the input alphabet. If we are
          working with a multi-tape machine (see parameter
          ``use_multitape_input`` and notes below), then the tape is a
          list or tuple of tracks, each of which can be a list or an
          iterable with entries from the input alphabet.

        - ``initial_state`` or ``initial_states`` -- the initial
          state(s) in which the machine starts. Either specify a
          single one with ``initial_state`` or a list of them with
          ``initial_states``. If both are given, ``initial_state``
          will be appended to ``initial_states``. If neither is
          specified, the initial states of the finite state machine
          are taken.

        - ``list_of_outputs`` -- (default: ``None``) a boolean or
          ``None``. If ``True``, then the outputs are given in list form
          (even if we have no or only one single output). If
          ``False``, then the result is never a list (an exception is
          raised if the result cannot be returned). If
          ``list_of_outputs=None`` the method determines automatically
          what to do (e.g. if a non-deterministic machine returns more
          than one path, then the output is returned in list form).

        - ``only_accepted`` -- boolean (default: ``False``); if set,
          then the first argument in the output is guaranteed to be
          ``True`` (if the output is a list, then the first argument
          of each element will be ``True``).

        - ``full_output`` -- boolean (default: ``True``); if set,
          then the full output is given, otherwise only the generated
          output (the third entry below only). If the input is not
          accepted, a :exc:`ValueError` is raised.

        - ``always_include_output`` -- if set (not by default), always
          include the output. This is inconsequential for a
          :class:`Transducer`, but can be used in other classes
          derived from :class:`FiniteStateMachine` where the output is
          suppressed by default, cf. :meth:`Automaton.process`.

        - ``format_output`` -- a function that translates the written
          output (which is in form of a list) to something more
          readable. By default (``None``) identity is used here.

        - ``check_epsilon_transitions`` -- boolean (default: ``True``); if
          ``False``, then epsilon transitions are not taken into consideration
          during process

        - ``write_final_word_out`` -- boolean (default: ``True``); whether the
          final output words should be written or not

        - ``use_multitape_input`` -- boolean (default: ``False``); if ``True``,
          then the multi-tape mode of the process iterator is activated. See
          also the notes below for multi-tape machines.

        - ``process_all_prefixes_of_input`` -- boolean (default: ``False``); if
          ``True``, then each prefix of the input word is processed (instead of
          processing the whole input word at once). Consequently, there is an
          output generated for each of these prefixes.

        - ``process_iterator_class`` -- (default: ``None``) a class
          inherited from :class:`FSMProcessIterator`. If ``None``,
          then :class:`FSMProcessIterator` is taken. An instance of this
          class is created and is used during the processing.

        - ``automatic_output_type`` -- boolean (default: ``False``); if set and
          the input has a parent, then the output will have the same parent. If
          the input does not have a parent, then the output will be of the same
          type as the input.

        OUTPUT:

        The full output is a triple (or a list of triples,
        cf. parameter ``list_of_outputs``), where

        - the first entry is ``True`` if the input string is accepted,

        - the second gives the reached state after processing the
          input tape (This is a state with label ``None`` if the input
          could not be processed, i.e., if at one point no
          transition to go on could be found.), and

        - the third gives a list of the output labels written during
          processing.

        If ``full_output`` is ``False``, then only the third entry
        is returned.

        Note that in the case the transducer is not
        deterministic, all possible paths are taken into account.

        This function uses an iterator which, in its simplest form, goes
        from one state to another in each step. To decide which way to
        go, it uses the input words of the outgoing transitions and
        compares them to the input tape. More precisely, in each step,
        the iterator takes an outgoing transition of the current state,
        whose input label equals the input letter of the tape. The
        output label of the transition, if present, is written on the
        output tape.

        If the choice of the outgoing transition is not unique (i.e.,
        we have a non-deterministic finite state machine), all
        possibilities are followed. This is done by splitting the
        process into several branches, one for each of the possible
        outgoing transitions.

        The process (iteration) stops if all branches are finished,
        i.e., for no branch, there is any transition whose input word
        coincides with the processed input tape. This can simply
        happen when the entire tape was read.

        Also see :meth:`~FiniteStateMachine.__call__` for a version of
        :meth:`.process` with shortened output.

        Internally this function creates and works with an instance of
        :class:`FSMProcessIterator`. This iterator can also be obtained
        with :meth:`~FiniteStateMachine.iter_process`.

        If working with multi-tape finite state machines, all input
        words of transitions are words of `k`-tuples of letters.
        Moreover, the input tape has to consist of `k` tracks, i.e.,
        be a list or tuple of `k` iterators, one for each track.

        .. WARNING::

            Working with multi-tape finite state machines is still
            experimental and can lead to wrong outputs.

        EXAMPLES::

            sage: binary_inverter = Transducer({'A': [('A', 0, 1), ('A', 1, 0)]},
            ....:                              initial_states=['A'], final_states=['A'])
            sage: binary_inverter.process([0, 1, 0, 0, 1, 1])
            (True, 'A', [1, 0, 1, 1, 0, 0])

        If we are only interested in the output, we can also use::

            sage: binary_inverter([0, 1, 0, 0, 1, 1])
            [1, 0, 1, 1, 0, 0]

        This can also be used with words as input::

            sage: # needs sage.combinat
            sage: W = Words([0, 1]); W
            Finite and infinite words over {0, 1}
            sage: w = W([0, 1, 0, 0, 1, 1]); w
            word: 010011
            sage: binary_inverter(w)
            word: 101100

        In this case it is automatically determined that the output is
        a word. The call above is equivalent to::

            sage: binary_inverter.process(w,                                            # needs sage.combinat
            ....:                         full_output=False,
            ....:                         list_of_outputs=False,
            ....:                         automatic_output_type=True)
            word: 101100

        The following transducer transforms `0^n 1` to `1^n 2`::

            sage: T = Transducer([(0, 0, 0, 1), (0, 1, 1, 2)])
            sage: T.state(0).is_initial = True
            sage: T.state(1).is_final = True

        We can see the different possibilities of the output by::

            sage: [T.process(w) for w in [[1], [0, 1], [0, 0, 1], [0, 1, 1],
            ....:                         [0], [0, 0], [2, 0], [0, 1, 2]]]
            [(True, 1, [2]), (True, 1, [1, 2]),
             (True, 1, [1, 1, 2]), (False, None, None),
             (False, 0, [1]), (False, 0, [1, 1]),
             (False, None, None), (False, None, None)]

        If we just want a condensed output, we use::

            sage: [T.process(w, full_output=False)
            ....:      for w in [[1], [0, 1], [0, 0, 1]]]
            [[2], [1, 2], [1, 1, 2]]
            sage: T.process([0], full_output=False)
            Traceback (most recent call last):
            ...
            ValueError: Invalid input sequence.
            sage: T.process([0, 1, 2], full_output=False)
            Traceback (most recent call last):
            ...
            ValueError: Invalid input sequence.

        It is equivalent to::

            sage: [T(w) for w in [[1], [0, 1], [0, 0, 1]]]
            [[2], [1, 2], [1, 1, 2]]
            sage: T([0])
            Traceback (most recent call last):
            ...
            ValueError: Invalid input sequence.
            sage: T([0, 1, 2])
            Traceback (most recent call last):
            ...
            ValueError: Invalid input sequence.

        A cycle with empty input and empty output is correctly processed::

            sage: T = Transducer([(0, 1, None, None), (1, 0, None, None)],
            ....:                initial_states=[0], final_states=[1])
            sage: T.process([])
            [(False, 0, []), (True, 1, [])]
            sage: _ = T.add_transition(-1, 0, 0, 'r')
            sage: T.state(-1).is_initial = True
            sage: T.state(0).is_initial = False
            sage: T.process([0])
            [(False, 0, ['r']), (True, 1, ['r'])]

        If there is a cycle with empty input but non-empty output, the
        possible outputs would be an infinite set::

            sage: T = Transducer([(0, 1, None, 'z'), (1, 0, None, None)],
            ....:                initial_states=[0], final_states=[1])
            sage: T.process([])
            Traceback (most recent call last):
            ...
            RuntimeError: State 0 is in an epsilon cycle (no input),
            but output is written.

        But if this cycle with empty input and non-empty output is not
        reached, the correct output is produced::

            sage: _ = T.add_transition(-1, 0, 0, 'r')
            sage: T.state(-1).is_initial = True
            sage: T.state(0).is_initial = False
            sage: T.process([])
            (False, -1, [])
            sage: T.process([0])
            Traceback (most recent call last):
            ...
            RuntimeError: State 0 is in an epsilon cycle (no input),
            but output is written.

        If we set ``check_epsilon_transitions=False``, then no
        transitions with empty input are considered
        anymore. Thus cycles with empty input are no problem anymore::

            sage: T.process([0], check_epsilon_transitions=False)
            (False, 0, ['r'])

        A simple example of a multi-tape transducer is the
        following: It writes the length of the first tape many letters ``a``
        and then the length of the second tape many letters ``b``::

            sage: M = Transducer([(0, 0, (1, None), 'a'),
            ....:                 (0, 1, [], []),
            ....:                 (1, 1, (None, 1), 'b')],
            ....:                initial_states=[0],
            ....:                final_states=[1])
            sage: M.process(([1, 1], [1]), use_multitape_input=True)
            (True, 1, ['a', 'a', 'b'])

        .. SEEALSO::

            :meth:`FiniteStateMachine.process`,
            :meth:`Automaton.process`,
            :meth:`~FiniteStateMachine.iter_process`,
            :meth:`~FiniteStateMachine.__call__`,
            :class:`FSMProcessIterator`.

        TESTS::

            sage: T = Transducer([(0, 1, 1, 'a'), (1, 0, 1, 'b')],
            ....:                initial_states=[0, 1], final_states=[1])
            sage: T.process([1, 1])
            [(False, 0, ['a', 'b']), (True, 1, ['b', 'a'])]
            sage: T.process([1, 1], T.state(0))
            (False, 0, ['a', 'b'])
            sage: T.state(1).final_word_out = 'c'
            sage: T.process([1, 1], T.state(1))
            (True, 1, ['b', 'a', 'c'])
            sage: T.process([1, 1], T.state(1), write_final_word_out=False)
            (True, 1, ['b', 'a'])

        The parameter ``input_tape`` is required::

            sage: T.process()
            Traceback (most recent call last):
            ...
            TypeError: No input tape given.
        """

class _FSMTapeCache_(SageObject):
    """
    This is a class for caching an input tape. It is used in
    :class:`FSMProcessIterator`.

    INPUT:

    - ``tape_cache_manager`` -- list of the existing instances of
      :class:`_FSMTapeCache_`. ``self`` will be appended to this list

    - ``tape`` -- tuple or list of the input tracks (iterables)

    - ``tape_ended`` -- list of booleans (one for each track of the
      tape), which indicate whether the track iterator has already raised
      a ``StopIteration`` exception

    - ``position`` -- tuple of pairs `(p, t)` marking the current
      positions of each of the input tracks. There `p` is the number
      of letter read from track `t`. The pairs of ``position`` are
      sorted first by `p` (smallest first) and then by `t`, i.e.,
      lexicographically.

    - ``is_multitape`` -- if ``True`` each entry of the
      input-word-tuple of a transition is interpreted as word for the
      corresponding input track. If ``False`` input-words are
      interpreted as an iterable of letters.

    OUTPUT: a tape-cache

    TESTS::

        sage: from sage.combinat.finite_state_machine import _FSMTapeCache_
        sage: TC1 = _FSMTapeCache_([], (xsrange(37, 42),),
        ....:                      [False], ((0, 0),), False)
        sage: TC2 = _FSMTapeCache_([], (xsrange(37, 42), xsrange(11,15)),
        ....:                      [False, False], ((0, 0), (0, 1)), True)
        sage: TC1
        tape at 0
        sage: TC1.tape_cache_manager
        [tape at 0]
        sage: TC2
        multi-tape at (0, 0)
        sage: TC2.tape_cache_manager
        [multi-tape at (0, 0)]
    """
    position: Incomplete
    tape: Incomplete
    tape_ended: Incomplete
    is_multitape: Incomplete
    tape_cache_manager: Incomplete
    cache: Incomplete
    def __init__(self, tape_cache_manager, tape, tape_ended, position, is_multitape) -> None:
        """
        See :class:`_FSMTapeCache_` for more details.

        TESTS::

            sage: from sage.combinat.finite_state_machine import _FSMTapeCache_
            sage: TC1 = _FSMTapeCache_([], (xsrange(37, 42),),
            ....:                      [False], ((0, 0),), False)
            sage: TC2 = _FSMTapeCache_([], (xsrange(37, 42), xsrange(11,15)),
            ....:                      [False, False], ((0, 0), (0, 1)), True)
            sage: TC1m = _FSMTapeCache_([], (xsrange(37, 42),),
            ....:                       [False], ((0, 0),), True)
            sage: TC3 = _FSMTapeCache_([], (xsrange(37, 42), xsrange(11,15)),
            ....:                      [False], ((0, 0),), False)
            Traceback (most recent call last):
            ...
            TypeError: The lengths of the inputs do not match
            sage: TC4 = _FSMTapeCache_([], (xsrange(37, 42), xsrange(11,15)),
            ....:                      [False, False], ((0, 0),), False)
            Traceback (most recent call last):
            ...
            TypeError: The lengths of the inputs do not match
            sage: TC5 = _FSMTapeCache_([], (xsrange(37, 42),),
            ....:                      [False, False], ((0, 0), (0, 1)), True)
            Traceback (most recent call last):
            ...
            TypeError: The lengths of the inputs do not match
            sage: _FSMTapeCache_([], (xsrange(37, 42), xsrange(11,15)),
            ....:                [False, False], ((0, 2), (0, 1)), True)
            Traceback (most recent call last):
            ...
            TypeError: Tape position ((0, 2), (0, 1)) wrong.
        """
    def __deepcopy__(self, memo):
        """
        See :meth:`.deepcopy` for details.

        TESTS::

            sage: from sage.combinat.finite_state_machine import _FSMTapeCache_
            sage: TC2 = _FSMTapeCache_([], (xsrange(37, 42), xsrange(11,15)),
            ....:                      [False, False], ((0, 0), (0, 1)), True)
            sage: TC3 = deepcopy(TC2)  # indirect doctest
            sage: TC3
            multi-tape at (0, 0)
            sage: TC2.tape_cache_manager
            [multi-tape at (0, 0), multi-tape at (0, 0)]
            sage: TC2.tape_cache_manager is TC3.tape_cache_manager
            True
        """
    def deepcopy(self, memo=None):
        """
        Return a deepcopy of ``self``.

        INPUT:

        - ``memo`` -- dictionary

        OUTPUT: an instance of ``_FSMCacheTape_``

        TESTS::

            sage: from sage.combinat.finite_state_machine import _FSMTapeCache_
            sage: TC2 = _FSMTapeCache_([], (xsrange(37, 42), xsrange(11,15)),
            ....:                      [False, False], ((0, 0), (0, 1)), True)
            sage: TC3 = deepcopy(TC2)  # indirect doctest
            sage: TC2
            multi-tape at (0, 0)
            sage: TC3
            multi-tape at (0, 0)
            sage: TC2.read(0), TC2.read(1), TC2.read(1)
            ((True, 37), (True, 11), (True, 12))
            sage: TC2.preview_word()
            (37, 11)
            sage: TC2.cache is TC3.cache
            False
        """
    def read(self, track_number):
        """
        Reads one letter from the given track of the input tape into
        the cache.

        INPUT:

        - ``track_number`` -- integer

        OUTPUT:

        ``(True, letter)`` if reading was successful (``letter`` was
        read), otherwise ``(False, None)``.

        Note that this updates the cache of all tapes in
        ``self.tape_cache_manager``.

        TESTS::

            sage: from sage.combinat.finite_state_machine import _FSMTapeCache_
            sage: TC2 = _FSMTapeCache_([], (xsrange(37, 42), xsrange(11,15)),
            ....:                      [False, False], ((0, 0), (0, 1)), True)
            sage: TC2.read(0), TC2.read(1), TC2.read(1)
            ((True, 37), (True, 11), (True, 12))
            sage: TC2.preview_word()
            (37, 11)
            sage: TC3 = deepcopy(TC2)
            sage: TC2.cache, TC3.cache
            ((deque([37]), deque([11, 12])), (deque([37]), deque([11, 12])))
            sage: TC3.read(1)
            (True, 13)
            sage: TC2.cache, TC3.cache
            ((deque([37]), deque([11, 12, 13])),
             (deque([37]), deque([11, 12, 13])))
            sage: TC2.read(1), TC2.read(1)
            ((True, 14), (False, None))
            sage: TC2.cache
            (deque([37]), deque([11, 12, 13, 14]))
            sage: TC2.tape_ended
            [False, True]
            sage: TC2.read(1)
            (False, None)
        """
    def finished(self, track_number=None):
        """
        Return whether the tape (or a particular track) has reached an
        end, i.e., there are no more letters in the cache and nothing
        more to read on the original tape.

        INPUT:

        - ``track_number`` -- integer or ``None`` (default); if ``None``,
          then ``True`` is returned if all tracks are finished

        OUTPUT: boolean

        TESTS::

            sage: from sage.combinat.finite_state_machine import (
            ....:     _FSMTapeCache_, FSMTransition)
            sage: TC2 = _FSMTapeCache_([], (xsrange(37, 42), xsrange(11,15)),
            ....:                      [False, False], ((0, 0), (0, 1)), True)
            sage: while True:
            ....:     try:
            ....:         word = TC2.preview_word(return_word=True)
            ....:     except RuntimeError:
            ....:         print('stop')
            ....:         break
            ....:     print('cache: {} {}'.format(TC2.cache, TC2))
            ....:     print('finished: {} {} {}'.format(TC2.finished(),
            ....:           TC2.finished(0), TC2.finished(1)))
            ....:     TC2.forward(
            ....:         FSMTransition(0, 0, word))
            cache: (deque([37]), deque([11])) multi-tape at (0, 0)
            finished: False False False
            cache: (deque([38]), deque([12])) multi-tape at (1, 1)
            finished: False False False
            cache: (deque([39]), deque([13])) multi-tape at (2, 2)
            finished: False False False
            cache: (deque([40]), deque([14])) multi-tape at (3, 3)
            finished: False False False
            stop
            sage: print('cache: {} {}'.format(TC2.cache, TC2))
            cache: (deque([41]), deque([])) multi-tape at (4, 4)
            sage: print('finished: {} {} {}'.format(TC2.finished(),
            ....:       TC2.finished(0), TC2.finished(1)))
            finished: False False True
            sage: TC2.preview_word()
            Traceback (most recent call last):
            ...
            RuntimeError: tape reached the end
            sage: print('cache: {} {}'.format(TC2.cache, TC2))
            cache: (deque([41]), deque([])) multi-tape at (4, 4)
            sage: TC2.read(0)
            (False, None)
            sage: TC2.forward(FSMTransition(0, 0, [(0, None)]))
            sage: print('finished: {} {} {}'.format(TC2.finished(),
            ....:       TC2.finished(0), TC2.finished(1)))
            finished: True True True
        """
    def preview_word(self, track_number=None, length: int = 1, return_word: bool = False):
        """
        Reads a word from the input tape.

        INPUT:

        - ``track_number`` -- integer (default: ``None``); if ``None``,
          then a tuple of words (one from each track) is returned

        - ``length`` -- (default: ``1``) the length of the word(s)

        - ``return_word`` -- boolean (default: ``False``); if set, then a word
          is returned, otherwise a single letter (in which case ``length`` has
          to be ``1``)

        OUTPUT: a single letter or a word

        A :python:`RuntimeError<library/exceptions.html#exceptions.RuntimeError>`
        is thrown if the tape (at least one track) has reached its end.

        Typically, this method is called from a hook-function of a
        state.

        The attribute ``position`` is not changed.

        TESTS::

            sage: from sage.combinat.finite_state_machine import (
            ....:     _FSMTapeCache_, FSMTransition)
            sage: TC2 = _FSMTapeCache_([], (xsrange(37, 42), xsrange(11,15)),
            ....:                      [False, False], ((0, 0), (0, 1)), True)
            sage: TC2.preview_word(), TC2.preview_word()
            ((37, 11), (37, 11))
            sage: while True:
            ....:     try:
            ....:         word = TC2.preview_word(return_word=True)
            ....:     except RuntimeError:
            ....:         print('stop')
            ....:         break
            ....:     print('read: {}'.format(word))
            ....:     print('cache: {} {}'.format(TC2.cache, TC2))
            ....:     TC2.forward(
            ....:         FSMTransition(0, 0, word))
            ....:     print('cache: {} {}'.format(TC2.cache, TC2))
            read: [(37, 11)]
            cache: (deque([37]), deque([11])) multi-tape at (0, 0)
            cache: (deque([]), deque([])) multi-tape at (1, 1)
            read: [(38, 12)]
            cache: (deque([38]), deque([12])) multi-tape at (1, 1)
            cache: (deque([]), deque([])) multi-tape at (2, 2)
            read: [(39, 13)]
            cache: (deque([39]), deque([13])) multi-tape at (2, 2)
            cache: (deque([]), deque([])) multi-tape at (3, 3)
            read: [(40, 14)]
            cache: (deque([40]), deque([14])) multi-tape at (3, 3)
            cache: (deque([]), deque([])) multi-tape at (4, 4)
            stop
            sage: print('cache: {} {}'.format(TC2.cache, TC2))
            cache: (deque([41]), deque([])) multi-tape at (4, 4)
            sage: TC2.preview_word()
            Traceback (most recent call last):
            ...
            RuntimeError: tape reached the end
            sage: print('cache: {} {}'.format(TC2.cache, TC2))
            cache: (deque([41]), deque([])) multi-tape at (4, 4)
            sage: TC2.preview_word(0)
            41
            sage: print('cache: {} {}'.format(TC2.cache, TC2))
            cache: (deque([41]), deque([])) multi-tape at (4, 4)
            sage: TC2.forward(FSMTransition(0, 0, [(41, None)]))
            sage: print('cache: {} {}'.format(TC2.cache, TC2))
            cache: (deque([]), deque([])) multi-tape at (5, 4)
        """
    def compare_to_tape(self, track_number, word):
        """
        Return whether it is possible to read ``word`` from the given
        track successfully.

        INPUT:

        - ``track_number`` -- integer

        - ``word`` -- tuple or list of letters

        OUTPUT: boolean

        TESTS::

            sage: from sage.combinat.finite_state_machine import _FSMTapeCache_
            sage: TC2 = _FSMTapeCache_([], (xsrange(37, 42), xsrange(11,15)),
            ....:                      [False, False], ((0, 0), (0, 1)), True)
            sage: TC2.compare_to_tape(0, [37])
            True
            sage: TC2.compare_to_tape(1, [37])
            False
            sage: TC2.compare_to_tape(0, [37, 38])
            True
            sage: TC2.compare_to_tape(1, srange(11,15))
            True
            sage: TC2.compare_to_tape(1, srange(11,16))
            False
            sage: TC2.compare_to_tape(1, [])
            True
        """
    def forward(self, transition):
        """
        Forwards the tape according to the given transition.

        INPUT:

        - ``transition`` -- a transition of a finite state machine

        OUTPUT: nothing

        If ``self.is_multitape`` is ``False``, then this function
        forwards ``self`` (track `0`) by the number of entries of
        ``transition.word_in`` different from ``None``.
        Otherwise (if ``self.is_multitape`` is
        ``True``), this function forwards each track of ``self`` by
        the length of each entry of ``transition.word_in``. Note that
        the actual values in the input word do not play a role
        (just the length).

        This function changes the attribute ``position``.

        TESTS::

            sage: from sage.combinat.finite_state_machine import (
            ....:     _FSMTapeCache_, FSMTransition,
            ....:     tupleofwords_to_wordoftuples)
            sage: TC2 = _FSMTapeCache_([], (xsrange(37, 42), xsrange(11,15)),
            ....:                      [False, False], ((0, 0), (0, 1)), True)
            sage: TC2, TC2.cache
            (multi-tape at (0, 0), (deque([]), deque([])))
            sage: letter = TC2.preview_word(); letter
            (37, 11)
            sage: TC2, TC2.cache
            (multi-tape at (0, 0), (deque([37]), deque([11])))
            sage: TC2.forward(FSMTransition(0, 0, [letter]))
            sage: TC2, TC2.cache
            (multi-tape at (1, 1), (deque([]), deque([])))
            sage: TC2.forward(FSMTransition(0, 0, [(0, 0), (None, 0)]))
            sage: TC2, TC2.cache
            (multi-tape at (2, 3), (deque([]), deque([])))
            sage: letter = TC2.preview_word(); letter
            (39, 14)
            sage: TC2, TC2.cache
            (multi-tape at (2, 3), (deque([39]), deque([14])))
            sage: word_in = tupleofwords_to_wordoftuples([[None], [None, None]])
            sage: TC2.forward(FSMTransition(0, 0, word_in))
            sage: TC2, TC2.cache
            (multi-tape at (2, 3), (deque([39]), deque([14])))
            sage: TC2.forward(FSMTransition(0, 0, [[0, None], [None, 0]]))
            sage: TC2, TC2.cache
            (multi-tape at (3, 4), (deque([]), deque([])))
            sage: TC2.forward(FSMTransition(0, 0, [(0, 0)]))
            Traceback (most recent call last):
            ...
            ValueError: forwarding tape is not possible
        """
    def transition_possible(self, transition):
        """
        Test whether the input word of ``transition`` can be read
        from the tape.

        INPUT:

        - ``transition`` -- a transition of a finite state machine

        OUTPUT: boolean

        TESTS::

            sage: from sage.combinat.finite_state_machine import (
            ....:     _FSMTapeCache_, FSMTransition)
            sage: TC2 = _FSMTapeCache_([], (xsrange(37, 42), xsrange(11,15)),
            ....:                      [False, False], ((0, 0), (0, 1)), True)
            sage: TC2, TC2.cache
            (multi-tape at (0, 0), (deque([]), deque([])))
            sage: TC2.transition_possible(
            ....:     FSMTransition(0, 0, [(37, 11), (38, 12), (None, 13)]))
            True
            sage: TC2.transition_possible(
            ....:     FSMTransition(0, 0, [(37, 11), (38, 13)]))
            False
            sage: TC2.transition_possible(
            ....:     FSMTransition(0, 0, [(37,), (38,)]))
            Traceback (most recent call last):
            ...
            TypeError: Transition from 0 to 0: (37,),(38,)|- has bad
            input word (entries should be tuples of size 2).
        """

class _FSMTapeCacheDetectEpsilon_(_FSMTapeCache_):
    """
    This is a class is similar to :class:`_FSMTapeCache_` but accepts
    only epsilon transitions.
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        See :class:`_FSMTapeCache_` for more details.

        TESTS::

            sage: from sage.combinat.finite_state_machine import _FSMTapeCacheDetectEpsilon_
            sage: _FSMTapeCacheDetectEpsilon_([], (xsrange(37, 42),),
            ....:                             [False], ((0, 0),), False)
            tape at 0
        """
    def __deepcopy__(self, memo):
        """
        See :meth:`_FSMTapeCache_.deepcopy` for details.

        TESTS::

            sage: from sage.combinat.finite_state_machine import _FSMTapeCacheDetectEpsilon_
            sage: TC2 = _FSMTapeCacheDetectEpsilon_([], (xsrange(37, 42),),
            ....:                                   [False], ((0, 0),), True)
            sage: TC2._visited_states_.add(1)
            sage: TC3 = deepcopy(TC2)  # indirect doctest
            sage: TC3._visited_states_
            {1}
        """

class _FSMTapeCacheDetectAll_(_FSMTapeCache_):
    """
    This is a class is similar to :class:`_FSMTapeCache_` but accepts
    each transition.
    """
    def compare_to_tape(self, track_number, word):
        """
        Return whether it is possible to read a word of the same length
        as ``word`` (but ignoring its actual content)
        from the given track successfully.

        INPUT:

        - ``track_number`` -- integer

        - ``word`` -- tuple or list of letters; only its length is used

        OUTPUT: boolean

        Note that this method usually returns ``True``. ``False`` can
        only be returned at the end of the input tape.

        TESTS::

            sage: from sage.combinat.finite_state_machine import _FSMTapeCacheDetectAll_
            sage: TC = _FSMTapeCacheDetectAll_(
            ....:     [], (iter((11, 12)),),
            ....:     [False], ((0, 0),), False)
            sage: TC.compare_to_tape(0, [])
            True
            sage: TC.compare_to_tape(0, [37])
            True
            sage: TC.compare_to_tape(0, [37, 38])
            True
            sage: TC.compare_to_tape(0, [37, 38, 39])
            False
            sage: TC.compare_to_tape(0, [1, 2])
            True
        """

def tupleofwords_to_wordoftuples(tupleofwords):
    """
    Transposes a tuple of words over the alphabet to a word of tuples.

    INPUT:

    - ``tupleofwords`` -- tuple of a list of letters

    OUTPUT: list of tuples

    Missing letters in the words are padded with the letter ``None``
    (from the empty word).

    EXAMPLES::

        sage: from sage.combinat.finite_state_machine import (
        ....:     tupleofwords_to_wordoftuples)
        sage: tupleofwords_to_wordoftuples(
        ....:     ([1, 2], [3, 4, 5, 6], [7]))
        [(1, 3, 7), (2, 4, None), (None, 5, None), (None, 6, None)]
    """
def wordoftuples_to_tupleofwords(wordoftuples):
    """
    Transposes a word of tuples to a tuple of words over the alphabet.

    INPUT:

    - ``wordoftuples`` -- list of tuples of letters

    OUTPUT: a tuple of lists

    Letters ``None`` (empty word) are removed from each word in the output.

    EXAMPLES::

        sage: from sage.combinat.finite_state_machine import (
        ....:     wordoftuples_to_tupleofwords)
        sage: wordoftuples_to_tupleofwords(
        ....:     [(1, 2), (1, None), (1, None), (1, 2), (None, 2)])
        ([1, 1, 1, 1], [2, 2, 2])
    """
def is_FSMProcessIterator(PI):
    """
    Test whether or not ``PI`` inherits from :class:`FSMProcessIterator`.

    TESTS::

        sage: from sage.combinat.finite_state_machine import is_FSMProcessIterator, FSMProcessIterator
        sage: is_FSMProcessIterator(FSMProcessIterator(FiniteStateMachine([[0, 0, 0, 0]], initial_states=[0]), []))
        doctest:warning...
        DeprecationWarning: The function is_FSMProcessIterator is deprecated; use 'isinstance(..., FSMProcessIterator)' instead.
        See https://github.com/sagemath/sage/issues/38032 for details.
        True
    """

class FSMProcessIterator(SageObject, Iterator):
    """
    This class takes an input, feeds it into a finite state machine
    (automaton or transducer, in particular), tests whether this was
    successful and calculates the written output.

    INPUT:

    - ``fsm`` -- the finite state machine on which the input should be
      processed

    - ``input_tape`` -- the input tape can be a list or an
      iterable with entries from the input alphabet. If we are
      working with a multi-tape machine (see parameter
      ``use_multitape_input`` and notes below), then the tape is a
      list or tuple of tracks, each of which can be a list or an
      iterable with entries from the input alphabet.

    - ``initial_state`` or ``initial_states`` -- the initial
      state(s) in which the machine starts. Either specify a
      single one with ``initial_state`` or a list of them with
      ``initial_states``. If both are given, ``initial_state``
      will be appended to ``initial_states``. If neither is
      specified, the initial states of the finite state machine
      are taken.

    - ``format_output`` -- a function that translates the written
      output (which is in form of a list) to something more
      readable. By default (``None``) identity is used here.

    - ``check_epsilon_transitions`` -- boolean (default: ``True``); if
      ``False``, then epsilon transitions are not taken into consideration
      during process

    - ``write_final_word_out`` -- boolean (default: ``True``); whether the
      final output words should be written or not

    - ``use_multitape_input`` -- boolean (default: ``False``); if ``True``,
      then the multi-tape mode of the process iterator is activated. See also
      the notes below for multi-tape machines.

    - ``process_all_prefixes_of_input`` -- boolean (default: ``False``); if
      ``True``, then each prefix of the input word is processed (instead of
      processing the whole input word at once). Consequently, there is an
      output generated for each of these prefixes.

    OUTPUT: an iterator

    In its simplest form, it behaves like an iterator which, in
    each step, goes from one state to another. To decide which way
    to go, it uses the input words of the outgoing transitions and
    compares them to the input tape. More precisely, in each step,
    the process iterator takes an outgoing transition of the
    current state, whose input label equals the input letter of
    the tape. The output label of the transition, if present, is
    written on the output tape.

    If the choice of the outgoing transition is not unique (i.e.,
    we have a non-deterministic finite state machine), all
    possibilities are followed. This is done by splitting the
    process into several branches, one for each of the possible
    outgoing transitions.

    The process (iteration) stops if all branches are finished,
    i.e., for no branch, there is any transition whose input word
    coincides with the processed input tape. This can simply
    happen when the entire tape was read.
    When the process stops, a ``StopIteration`` exception is thrown.

    .. WARNING::

        Processing an input tape of length `n` usually takes at least `n+1`
        iterations, since there will be `n+1` states visited (in the
        case the taken transitions have input words consisting of single
        letters).

    An instance of this class is generated when
    :meth:`FiniteStateMachine.process` or
    :meth:`FiniteStateMachine.iter_process` of a finite state machine,
    an automaton, or a transducer is invoked.

    When working with multi-tape finite state machines, all input
    words of transitions are words of `k`-tuples of letters.
    Moreover, the input tape has to consist of `k` tracks, i.e.,
    be a list or tuple of `k` iterators, one for each track.

    .. WARNING::

        Working with multi-tape finite state machines is still
        experimental and can lead to wrong outputs.

    EXAMPLES:

    The following transducer reads binary words and outputs a word,
    where blocks of ones are replaced by just a single one. Further
    only words that end with a zero are accepted.

    ::

        sage: T = Transducer({'A': [('A', 0, 0), ('B', 1, None)],
        ....:                 'B': [('B', 1, None), ('A', 0, [1, 0])]},
        ....:     initial_states=['A'], final_states=['A'])
        sage: input = [1, 1, 0, 0, 1, 0, 1, 1, 1, 0]
        sage: T.process(input)
        (True, 'A', [1, 0, 0, 1, 0, 1, 0])

    The function :meth:`FiniteStateMachine.process` (internally) uses a
    :class:`FSMProcessIterator`. We can do that manually, too, and get full
    access to the iteration process::

        sage: from sage.combinat.finite_state_machine import FSMProcessIterator
        sage: it = FSMProcessIterator(T, input_tape=input)
        sage: for current in it:
        ....:     print(current)
        process (1 branch)
        + at state 'B'
        +-- tape at 1, [[]]
        process (1 branch)
        + at state 'B'
        +-- tape at 2, [[]]
        process (1 branch)
        + at state 'A'
        +-- tape at 3, [[1, 0]]
        process (1 branch)
        + at state 'A'
        +-- tape at 4, [[1, 0, 0]]
        process (1 branch)
        + at state 'B'
        +-- tape at 5, [[1, 0, 0]]
        process (1 branch)
        + at state 'A'
        +-- tape at 6, [[1, 0, 0, 1, 0]]
        process (1 branch)
        + at state 'B'
        +-- tape at 7, [[1, 0, 0, 1, 0]]
        process (1 branch)
        + at state 'B'
        +-- tape at 8, [[1, 0, 0, 1, 0]]
        process (1 branch)
        + at state 'B'
        +-- tape at 9, [[1, 0, 0, 1, 0]]
        process (1 branch)
        + at state 'A'
        +-- tape at 10, [[1, 0, 0, 1, 0, 1, 0]]
        process (0 branches)
        sage: it.result()
        [Branch(accept=True, state='A', output=[1, 0, 0, 1, 0, 1, 0])]

    ::

        sage: T = Transducer([(0, 0, 0, 'a'), (0, 1, 0, 'b'),
        ....:                 (1, 2, 1, 'c'), (2, 0, 0, 'd'),
        ....:                 (2, 1, None, 'd')],
        ....:                initial_states=[0], final_states=[2])
        sage: sorted(T.process([0, 0, 1], format_output=lambda o: ''.join(o)))
        [(False, 1, 'abcd'), (True, 2, 'abc')]
        sage: it = FSMProcessIterator(T, input_tape=[0, 0, 1],
        ....:                         format_output=lambda o: ''.join(o))
        sage: for current in it:
        ....:     print(current)
        process (2 branches)
        + at state 0
        +-- tape at 1, [['a']]
        + at state 1
        +-- tape at 1, [['b']]
        process (2 branches)
        + at state 0
        +-- tape at 2, [['a', 'a']]
        + at state 1
        +-- tape at 2, [['a', 'b']]
        process (2 branches)
        + at state 1
        +-- tape at 3, [['a', 'b', 'c', 'd']]
        + at state 2
        +-- tape at 3, [['a', 'b', 'c']]
        process (0 branches)
        sage: sorted(it.result())
        [Branch(accept=False, state=1, output='abcd'),
         Branch(accept=True, state=2, output='abc')]

    .. SEEALSO::

        :meth:`FiniteStateMachine.process`,
        :meth:`Automaton.process`,
        :meth:`Transducer.process`,
        :meth:`FiniteStateMachine.iter_process`,
        :meth:`FiniteStateMachine.__call__`,
        :meth:`next`.

    TESTS::

        sage: T = Transducer([[0, 0, 0, 0]])
        sage: T.process([])
        Traceback (most recent call last):
        ...
        ValueError: No state is initial.

    ::

        sage: T = Transducer([[0, 1, 0, 0]], initial_states=[0, 1])
        sage: T.process([])
        [(False, 0, []), (False, 1, [])]

    ::

        sage: T = Transducer([[0, 0, 0, 0]],
        ....:                initial_states=[0], final_states=[0])
        sage: T.state(0).final_word_out = [42]
        sage: T.process([0])
        (True, 0, [0, 42])
        sage: T.process([0], write_final_word_out=False)
        (True, 0, [0])
    """
    class Current(dict):
        """
        This class stores the branches which have to be processed
        during iteration and provides a nicer formatting of them.

        This class is derived from ``dict``. It is returned by the
        ``next``-function during iteration.

        EXAMPLES:

        In the following example you can see the dict directly and
        then the nicer output provided by this class::

            sage: from sage.combinat.finite_state_machine import FSMProcessIterator
            sage: inverter = Transducer({'A': [('A', 0, 1), ('A', 1, 0)]},
            ....:     initial_states=['A'], final_states=['A'])
            sage: it = FSMProcessIterator(inverter, input_tape=[0, 1])
            sage: for current in it:
            ....:     print(dict(current))
            ....:     print(current)
            {((1, 0),): {'A': Branch(tape_cache=tape at 1, outputs=[[1]])}}
            process (1 branch)
            + at state 'A'
            +-- tape at 1, [[1]]
            {((2, 0),): {'A': Branch(tape_cache=tape at 2, outputs=[[1, 0]])}}
            process (1 branch)
            + at state 'A'
            +-- tape at 2, [[1, 0]]
            {}
            process (0 branches)
        """

    class FinishedBranch(NamedTuple):
        accept: Incomplete
        state: Incomplete
        output: Incomplete
    fsm: Incomplete
    is_multitape: Incomplete
    format_output: Incomplete
    check_epsilon_transitions: Incomplete
    write_final_word_out: Incomplete
    process_all_prefixes_of_input: Incomplete
    TapeCache: Incomplete
    def __init__(self, fsm, input_tape=None, initial_state=None, initial_states=[], use_multitape_input: bool = False, check_epsilon_transitions: bool = True, write_final_word_out: bool = True, format_output=None, process_all_prefixes_of_input: bool = False, **kwargs) -> None:
        """
        See :class:`FSMProcessIterator` for more information.

        EXAMPLES::

            sage: from sage.combinat.finite_state_machine import FSMProcessIterator
            sage: inverter = Transducer({'A': [('A', 0, 1), ('A', 1, 0)]},
            ....:     initial_states=['A'], final_states=['A'])
            sage: it = FSMProcessIterator(inverter, input_tape=[0, 1])
            sage: for current in it:
            ....:     print(current)
            process (1 branch)
            + at state 'A'
            +-- tape at 1, [[1]]
            process (1 branch)
            + at state 'A'
            +-- tape at 2, [[1, 0]]
            process (0 branches)
            sage: it.result()
            [Branch(accept=True, state='A', output=[1, 0])]
        """

    class _branch_(NamedTuple):
        tape_cache: Incomplete
        outputs: Incomplete
    def __next__(self):
        '''
        Makes one step in processing the input tape.

        OUTPUT:

        It returns the current status of the iterator (see below). A
        ``StopIteration`` exception is thrown when there is/was
        nothing to do (i.e. all branches ended with previous call
        of :meth:`.next`).

        The current status is a dictionary (encapsulated into an instance of
        :class:`~FSMProcessIterator.Current`).
        The keys are positions on
        the tape. The value corresponding to such a position is again
        a dictionary, where each entry represents a branch of the
        process. This dictionary maps the current state of a branch to
        a pair consisting of a tape cache and a list of output words,
        which were written during reaching this current state.

        EXAMPLES::

            sage: from sage.combinat.finite_state_machine import FSMProcessIterator
            sage: inverter = Transducer({\'A\': [(\'A\', 0, 1), (\'A\', 1, 0)]},
            ....:     initial_states=[\'A\'], final_states=[\'A\'])
            sage: it = FSMProcessIterator(inverter, input_tape=[0, 1])
            sage: next(it)
            process (1 branch)
            + at state \'A\'
            +-- tape at 1, [[1]]
            sage: next(it)
            process (1 branch)
            + at state \'A\'
            +-- tape at 2, [[1, 0]]
            sage: next(it)
            process (0 branches)
            sage: next(it)
            Traceback (most recent call last):
            ...
            StopIteration

        .. SEEALSO::

            :meth:`FiniteStateMachine.process`,
            :meth:`Automaton.process`,
            :meth:`Transducer.process`,
            :meth:`FiniteStateMachine.iter_process`,
            :meth:`FiniteStateMachine.__call__`,
            :class:`FSMProcessIterator`.

        TESTS::

            sage: Z = Transducer()
            sage: s = Z.add_state(0)
            sage: s.is_initial = True
            sage: s.is_final = True
            sage: s.final_word_out = [1, 2]
            sage: Z.process([])
            (True, 0, [1, 2])
            sage: it = FSMProcessIterator(Z, input_tape=[])
            sage: next(it)
            process (0 branches)
            sage: next(it)
            Traceback (most recent call last):
            ...
            StopIteration

        ::

            sage: N = Transducer([(0, 0, 0, 1)], initial_states=[0])
            sage: def h_old(state, process):
            ....:     print("{} {}".format(state, process))
            sage: N.state(0).hook = h_old
            sage: N.process([0, 0])
            Traceback (most recent call last):
            ...
            ValueError: invalid input

            sage: def h_new(process, state, outputs):
            ....:     print("{} {}".format(state, outputs))
            sage: N.state(0).hook = h_new
            sage: N.process([0, 0], check_epsilon_transitions=False)
            0 [[]]
            0 [[1]]
            0 [[1, 1]]
            (False, 0, [1, 1])
        '''
    next = __next__
    def result(self, format_output=None):
        """
        Return the already finished branches during process.

        INPUT:

        - ``format_output`` -- a function converting the output from
          list form to something more readable (default: output the
          list directly).

        OUTPUT:

        A list of triples ``(accepted, state, output)``.

        See also the parameter ``format_output`` of
        :class:`FSMProcessIterator`.

        EXAMPLES::

            sage: inverter = Transducer({'A': [('A', 0, 'one'), ('A', 1, 'zero')]},
            ....:     initial_states=['A'], final_states=['A'])
            sage: it = inverter.iter_process(input_tape=[0, 1, 1])
            sage: for _ in it:
            ....:     pass
            sage: it.result()
            [Branch(accept=True, state='A', output=['one', 'zero', 'zero'])]
            sage: it.result(lambda L: ', '.join(L))
            [(True, 'A', 'one, zero, zero')]

        Using both the parameter ``format_output`` of
        :class:`FSMProcessIterator` and the parameter ``format_output``
        of :meth:`.result` leads to concatenation of the two
        functions::

            sage: it = inverter.iter_process(input_tape=[0, 1, 1],
            ....:                            format_output=lambda L: ', '.join(L))
            sage: for _ in it:
            ....:     pass
            sage: it.result()
            [Branch(accept=True, state='A', output='one, zero, zero')]
            sage: it.result(lambda L: ', '.join(L))
            [(True, 'A', 'o, n, e, ,,  , z, e, r, o, ,,  , z, e, r, o')]
        """
    def preview_word(self, track_number=None, length: int = 1, return_word: bool = False):
        '''
        Read a word from the input tape.

        INPUT:

        - ``track_number`` -- integer (default: ``None``); if ``None``, then
          a tuple of words (one from each track) is returned

        - ``length`` -- (default: ``1``) the length of the word(s)

        - ``return_word`` -- boolean (default: ``False``); if set, then a word
          is returned, otherwise a single letter (in which case ``length`` has
          to be ``1``)

        OUTPUT: a single letter or a word

        An exception ``StopIteration`` is thrown if the tape (at least
        one track) has reached its end.

        Typically, this method is called from a hook-function of a
        state.

        EXAMPLES::

            sage: inverter = Transducer({\'A\': [(\'A\', 0, \'one\'),
            ....:                              (\'A\', 1, \'zero\')]},
            ....:     initial_states=[\'A\'], final_states=[\'A\'])
            sage: def state_hook(process, state, output):
            ....:     print("We are now in state %s." % (state.label(),))
            ....:     try:
            ....:         w = process.preview_word()
            ....:     except RuntimeError:
            ....:         raise StopIteration
            ....:     print("Next on the tape is a %s." % (w,))
            sage: inverter.state(\'A\').hook = state_hook
            sage: it = inverter.iter_process(
            ....:     input_tape=[0, 1, 1],
            ....:     check_epsilon_transitions=False)
            sage: for _ in it:
            ....:     pass
            We are now in state A.
            Next on the tape is a 0.
            We are now in state A.
            Next on the tape is a 1.
            We are now in state A.
            Next on the tape is a 1.
            We are now in state A.
            sage: it.result()
            [Branch(accept=True, state=\'A\', output=[\'one\', \'zero\', \'zero\'])]
        '''

class _FSMProcessIteratorEpsilon_(FSMProcessIterator):
    """
    This class is similar to :class:`FSMProcessIterator`, but only
    accepts epsilon transitions during process. See
    :class:`FSMProcessIterator` for more information.

    EXAMPLES::

        sage: T = Transducer([(0, 1, 0, 'a'), (0, 2, None, 'b'),
        ....:                 (2, 1, None, 'c')])
        sage: from sage.combinat.finite_state_machine import _FSMProcessIteratorEpsilon_
        sage: it = _FSMProcessIteratorEpsilon_(T, initial_state=T.state(0),
        ....:                                format_output=lambda o: ''.join(o))

    To see what is going on, we let the transducer run::

        sage: for current in it:
        ....:     print(current)
        process (1 branch)
        + at state 2
        +-- tape at 0, [['b']]
        process (1 branch)
        + at state 1
        +-- tape at 0, [['b', 'c']]
        process (0 branches)

    This class has the additional attribute ``visited_states``::

        sage: it.visited_states
        {0: [''], 1: ['bc'], 2: ['b']}

    This means the following (let us skip the state `0` for a moment):
    State `1` can be reached by a epsilon path which write ``'bc'`` as
    output. Similarly, state `2` can be reached by writing ``'b'``. We
    started in state `0`, so this is included in visited states as
    well (``''`` means that nothing was written, which is clear, since
    no path had to be taken).

    We continue with the other states as initial states::

        sage: it = _FSMProcessIteratorEpsilon_(T, initial_state=T.state(1),
        ....:                                  format_output=lambda o: ''.join(o))
        sage: for current in it:
        ....:     print(current)
        process (0 branches)
        sage: it.visited_states
        {1: ['']}
        sage: it = _FSMProcessIteratorEpsilon_(T, initial_state=T.state(2),
        ....:                                  format_output=lambda o: ''.join(o))
        sage: for current in it:
        ....:     print(current)
        process (1 branch)
        + at state 1
        +-- tape at 0, [['c']]
        process (0 branches)
        sage: it.visited_states
        {1: ['c'], 2: ['']}

    TESTS::

        sage: A = Automaton([(0, 1, 0), (1, 2, None), (2, 3, None),
        ....:                (3, 1, None), (3, 4, None), (1, 4, None)])
        sage: it = _FSMProcessIteratorEpsilon_(A, initial_state=A.state(0))
        sage: for current in it:
        ....:     print(current)
        process (0 branches)
        sage: it.visited_states
        {0: [[]]}
        sage: it = _FSMProcessIteratorEpsilon_(A, initial_state=A.state(1))
        sage: for current in it:
        ....:     print(current)
        process (2 branches)
        + at state 2
        +-- tape at 0, [[]]
        + at state 4
        +-- tape at 0, [[]]
        process (1 branch)
        + at state 3
        +-- tape at 0, [[]]
        process (1 branch)
        + at state 4
        +-- tape at 0, [[]]
        process (0 branches)
        sage: it.visited_states
        {1: [[], []], 2: [[]], 3: [[]], 4: [[], []]}

    At this point note that in the previous output, state `1` (from
    which we started) was also reached by a non-trivial
    path. Moreover, there are two different paths from `1` to `4`.

    Let us continue with the other initial states::

        sage: it = _FSMProcessIteratorEpsilon_(A, initial_state=A.state(2))
        sage: for current in it:
        ....:     print(current)
        process (1 branch)
        + at state 3
        +-- tape at 0, [[]]
        process (2 branches)
        + at state 1
        +-- tape at 0, [[]]
        + at state 4
        +-- tape at 0, [[]]
        process (1 branch)
        + at state 4
        +-- tape at 0, [[]]
        process (0 branches)
        sage: it.visited_states
        {1: [[]], 2: [[], []], 3: [[]], 4: [[], []]}
        sage: it = _FSMProcessIteratorEpsilon_(A, initial_state=A.state(3))
        sage: for current in it:
        ....:     print(current)
        process (2 branches)
        + at state 1
        +-- tape at 0, [[]]
        + at state 4
        +-- tape at 0, [[]]
        process (2 branches)
        + at state 2
        +-- tape at 0, [[]]
        + at state 4
        +-- tape at 0, [[]]
        process (0 branches)
        sage: it.visited_states
        {1: [[]], 2: [[]], 3: [[], []], 4: [[], []]}
        sage: it = _FSMProcessIteratorEpsilon_(A, initial_state=A.state(4))
        sage: for current in it:
        ....:     print(current)
        process (0 branches)
        sage: it.visited_states
        {4: [[]]}

    ::

        sage: T = Transducer([(0, 1, 0, 'a'), (1, 2, None, 'b'),
        ....:                 (2, 3, None, 'c'), (3, 1, None, 'd'),
        ....:                 (3, 4, None, 'e'), (1, 4, None, 'f')])
        sage: it = _FSMProcessIteratorEpsilon_(T, initial_state=T.state(0),
        ....:                                  format_output=lambda o: ''.join(o))
        sage: for current in it:
        ....:     print(current)
        process (0 branches)
        sage: it.visited_states
        {0: ['']}
        sage: it = _FSMProcessIteratorEpsilon_(T, initial_state=T.state(1),
        ....:                                  format_output=lambda o: ''.join(o))
        sage: for current in it:
        ....:     print(current)
        process (2 branches)
        + at state 2
        +-- tape at 0, [['b']]
        + at state 4
        +-- tape at 0, [['f']]
        process (1 branch)
        + at state 3
        +-- tape at 0, [['b', 'c']]
        process (1 branch)
        + at state 4
        +-- tape at 0, [['b', 'c', 'e']]
        process (0 branches)
        sage: it.visited_states
        {1: ['', 'bcd'], 2: ['b'],
         3: ['bc'], 4: ['f', 'bce']}
        sage: it = _FSMProcessIteratorEpsilon_(T, initial_state=T.state(2),
        ....:                                  format_output=lambda o: ''.join(o))
        sage: for current in it:
        ....:     print(current)
        process (1 branch)
        + at state 3
        +-- tape at 0, [['c']]
        process (2 branches)
        + at state 1
        +-- tape at 0, [['c', 'd']]
        + at state 4
        +-- tape at 0, [['c', 'e']]
        process (1 branch)
        + at state 4
        +-- tape at 0, [['c', 'd', 'f']]
        process (0 branches)
        sage: it.visited_states
        {1: ['cd'], 2: ['', 'cdb'],
         3: ['c'], 4: ['ce', 'cdf']}
        sage: it = _FSMProcessIteratorEpsilon_(T, initial_state=T.state(3),
        ....:                                  format_output=lambda o: ''.join(o))
        sage: for current in it:
        ....:     print(current)
        process (2 branches)
        + at state 1
        +-- tape at 0, [['d']]
        + at state 4
        +-- tape at 0, [['e']]
        process (2 branches)
        + at state 2
        +-- tape at 0, [['d', 'b']]
        + at state 4
        +-- tape at 0, [['d', 'f']]
        process (0 branches)
        sage: it.visited_states
        {1: ['d'], 2: ['db'],
         3: ['', 'dbc'], 4: ['e', 'df']}
        sage: it = _FSMProcessIteratorEpsilon_(T, initial_state=T.state(4),
        ....:                                  format_output=lambda o: ''.join(o))
        sage: for current in it:
        ....:     print(current)
        process (0 branches)
        sage: it.visited_states
        {4: ['']}

    ::

        sage: T = Transducer([(0, 1, None, 'a'), (0, 2, None, 'b'),
        ....:                 (1, 3, None, 'c'), (2, 3, None, 'd'),
        ....:                 (3, 0, None, 'e')])
        sage: it = _FSMProcessIteratorEpsilon_(T, initial_state=T.state(0),
        ....:                                  format_output=lambda o: ''.join(o))
        sage: for current in it:
        ....:     print(current)
        process (2 branches)
        + at state 1
        +-- tape at 0, [['a']]
        + at state 2
        +-- tape at 0, [['b']]
        process (1 branch)
        + at state 3
        +-- tape at 0, [['a', 'c'], ['b', 'd']]
        process (0 branches)
        sage: it.visited_states
        {0: ['', 'ace', 'bde'], 1: ['a'], 2: ['b'], 3: ['ac', 'bd']}

    ::

        sage: T = Transducer([(0, 1, None, None), (0, 2, None, 'b'),
        ....:                 (1, 3, None, None), (2, 3, None, 'd'),
        ....:                 (3, 0, None, None)])
        sage: it = _FSMProcessIteratorEpsilon_(T, initial_state=T.state(0),
        ....:                                  format_output=lambda o: ''.join(o))
        sage: for current in it:
        ....:     print(current)
        process (2 branches)
        + at state 1
        +-- tape at 0, [[]]
        + at state 2
        +-- tape at 0, [['b']]
        process (1 branch)
        + at state 3
        +-- tape at 0, [[], ['b', 'd']]
        process (0 branches)
        sage: it.visited_states
        {0: ['', '', 'bd'], 1: [''], 2: ['b'], 3: ['', 'bd']}
        sage: T.state(0)._epsilon_cycle_output_empty_(T)
        False

    ::

        sage: T = Transducer([(0, 1, None, 'a'), (1, 2, None, 'b'),
        ....:                 (0, 2, None, 'c'), (2, 3, None, 'd'),
        ....:                 (3, 0, None, 'e')])
        sage: it = _FSMProcessIteratorEpsilon_(T, initial_state=T.state(0),
        ....:                                  format_output=lambda o: ''.join(o))
        sage: for current in it:
        ....:     print(current)
        process (2 branches)
        + at state 1
        +-- tape at 0, [['a']]
        + at state 2
        +-- tape at 0, [['c']]
        process (2 branches)
        + at state 2
        +-- tape at 0, [['a', 'b']]
        + at state 3
        +-- tape at 0, [['c', 'd']]
        process (1 branch)
        + at state 3
        +-- tape at 0, [['a', 'b', 'd']]
        process (0 branches)
        sage: it.visited_states
        {0: ['', 'cde', 'abde'], 1: ['a'], 2: ['c', 'ab'], 3: ['cd', 'abd']}

    ::

        sage: T = Transducer([(0, 1, None, 'a'), (0, 2, None, 'b'),
        ....:                 (0, 2, None, 'c'), (2, 3, None, 'd'),
        ....:                 (3, 0, None, 'e')])
        sage: it = _FSMProcessIteratorEpsilon_(T, initial_state=T.state(0),
        ....:                                  format_output=lambda o: ''.join(o))
        sage: for current in it:
        ....:     print(current)
        process (2 branches)
        + at state 1
        +-- tape at 0, [['a']]
        + at state 2
        +-- tape at 0, [['b'], ['c']]
        process (1 branch)
        + at state 3
        +-- tape at 0, [['b', 'd'], ['c', 'd']]
        process (0 branches)
        sage: it.visited_states
        {0: ['', 'bde', 'cde'], 1: ['a'], 2: ['b', 'c'], 3: ['bd', 'cd']}
    """
    TapeCache: Incomplete
    visited_states: Incomplete
    def __init__(self, *args, **kwargs) -> None:
        """
        See :class:`_FSMProcessIteratorEpsilon_` and
        :class:`FSMProcessIterator` for more information.

        TESTS::

            sage: T = Transducer([(0, 1, None, 'a'), (1, 2, None, 'b')])
            sage: T.state(0)._epsilon_successors_(T)  # indirect doctest
            {1: [['a']], 2: [['a', 'b']]}
        """

class _FSMProcessIteratorAll_(FSMProcessIterator):
    """
    This class is similar to :class:`FSMProcessIterator`, but
    accepts all transitions during process. See
    :class:`FSMProcessIterator` for more information.

    This is used in :meth:`FiniteStateMachine.language`.

    EXAMPLES::

        sage: F = FiniteStateMachine(
        ....:     {'A': [('A', 0, 'z'), ('B', 1, 'o'), ('B', -1, 'm')],
        ....:      'B': [('A', 0, 'z')]},
        ....:     initial_states=['A'], final_states=['A', 'B'])
        sage: from sage.combinat.finite_state_machine import _FSMProcessIteratorAll_
        sage: it = _FSMProcessIteratorAll_(F, max_length=3,
        ....:                              format_output=lambda o: ''.join(o))
        sage: for current in it:
        ....:     print(current)
        process (2 branches)
        + at state 'A'
        +-- tape at 1, [['z']]
        + at state 'B'
        +-- tape at 1, [['m'], ['o']]
        process (2 branches)
        + at state 'A'
        +-- tape at 2, [['m', 'z'], ['o', 'z'], ['z', 'z']]
        + at state 'B'
        +-- tape at 2, [['z', 'm'], ['z', 'o']]
        process (2 branches)
        + at state 'A'
        +-- tape at 3, [['m', 'z', 'z'], ['o', 'z', 'z'], ['z', 'm', 'z'],
                        ['z', 'o', 'z'], ['z', 'z', 'z']]
        + at state 'B'
        +-- tape at 3, [['m', 'z', 'm'], ['m', 'z', 'o'], ['o', 'z', 'm'],
                        ['o', 'z', 'o'], ['z', 'z', 'm'], ['z', 'z', 'o']]
        process (0 branches)
        sage: it.result()
        [Branch(accept=True, state='A', output='mzz'),
         Branch(accept=True, state='A', output='ozz'),
         Branch(accept=True, state='A', output='zmz'),
         Branch(accept=True, state='A', output='zoz'),
         Branch(accept=True, state='A', output='zzz'),
         Branch(accept=True, state='B', output='mzm'),
         Branch(accept=True, state='B', output='mzo'),
         Branch(accept=True, state='B', output='ozm'),
         Branch(accept=True, state='B', output='ozo'),
         Branch(accept=True, state='B', output='zzm'),
         Branch(accept=True, state='B', output='zzo')]
    """
    TapeCache: Incomplete
    visited_states: Incomplete
    def __init__(self, *args, **kwargs) -> None:
        """
        See :class:`_FSMProcessIteratorAll_` and
        :class:`FSMProcessIterator` for more information.

        TESTS::

            sage: T = Transducer([(0, 1, 0, 'a'), (1, 2, 1, 'b')],
            ....:                initial_states=[0], final_states=[0, 1, 2])
            sage: T.determine_alphabets()
            sage: list(T.language(2))  # indirect doctest
            [[], ['a'], ['a', 'b']]
        """

@cached_function
def setup_latex_preamble() -> None:
    '''
    This function adds the package ``tikz`` with support for automata
    to the preamble of Latex so that the finite state machines can be
    drawn nicely.

    See the section on :ref:`finite_state_machine_LaTeX_output`
    in the introductory examples of this module.

    TESTS::

        sage: from sage.combinat.finite_state_machine import setup_latex_preamble
        sage: setup_latex_preamble()
        sage: (r"\\usepackage{tikz}" in latex.extra_preamble()) == latex.has_file("tikz.sty")
        True
    '''
