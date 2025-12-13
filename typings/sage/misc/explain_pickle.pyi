from _typeshed import Incomplete
from sage.misc.persist import SageUnpickler as SageUnpickler, dumps as dumps, register_unpickle_override as register_unpickle_override, unpickle_global as unpickle_global, unpickle_override as unpickle_override
from sage.misc.sage_eval import sage_eval as sage_eval
from sage.misc.sage_input import SageInputBuilder as SageInputBuilder, SageInputExpression as SageInputExpression

ClassType: Incomplete

def explain_pickle(pickle=None, file=None, compress: bool = True, **kwargs):
    """
    Explain a pickle. That is, produce source code such that evaluating
    the code is equivalent to loading the pickle.  Feeding the result
    of :func:`explain_pickle` to :func:`sage_eval` should be totally equivalent to loading
    the ``pickle`` with ``cPickle``.

    INPUT:

    - ``pickle`` -- string (default: ``None``); the pickle to explain
    - ``file`` -- a filename of a pickle (default: ``None``)
    - ``compress`` -- boolean (default: ``True``); if ``False``, don't attempt
      to decompress the pickle
    - ``in_current_sage`` -- boolean (default: ``False``); if ``True``,
      produce potentially simpler code that is tied to the current version of
      Sage
    - ``default_assumptions`` -- boolean (default: ``False``); if ``True``,
      produce potentially simpler code that assumes that generic unpickling
      code will be used.  This code may not actually work.
    - ``eval`` -- boolean (default: ``False``); if ``True``, then evaluate the
      resulting code and return the evaluated result
    - ``preparse`` -- if ``True``, then produce code to be evaluated with
      Sage's preparser; if ``False``, then produce standard
      Python code; if ``None``, then produce code that will work
      either with or without the preparser.  (default: ``True``)
    - ``pedantic`` -- boolean (default: ``False``); if ``True``, then carefully
      ensures that the result has at least as much sharing as the result of
      cPickle (it may have more, for immutable objects)

    Exactly one of ``pickle`` (a string containing a pickle) or
    ``file`` (the filename of a pickle) must be provided.

    EXAMPLES::

        sage: explain_pickle(dumps({('a', 'b'): [1r, 2r]}))
        {('a', 'b'):[1r, 2r]}
        sage: explain_pickle(dumps(RR(pi)), in_current_sage=True)                       # needs sage.symbolic
        from sage.rings.real_mpfr import __create__RealNumber_version0
        from sage.rings.real_mpfr import __create__RealField_version0
        __create__RealNumber_version0(__create__RealField_version0(53r, False, 'RNDN'), '3.4gvml245kc0@0', 32r)
        sage: s = 'hi'
        sage: explain_pickle(dumps((s, s)))
        ('hi', 'hi')
        sage: explain_pickle(dumps((s, s)), pedantic=True)
        si = 'hi'
        (si, si)
        sage: explain_pickle(dumps(5r))
        5r
        sage: explain_pickle(dumps(5r), preparse=False)
        5
        sage: explain_pickle(dumps(5r), preparse=None)
        int(5)
        sage: explain_pickle(dumps(22/7))
        pg_make_rational = unpickle_global('sage.rings.rational', 'make_rational')
        pg_make_rational('m/7')
        sage: explain_pickle(dumps(22/7), in_current_sage=True)
        from sage.rings.rational import make_rational
        make_rational('m/7')
        sage: explain_pickle(dumps(22/7), default_assumptions=True)
        from sage.rings.rational import make_rational
        make_rational('m/7')
    """
def explain_pickle_string(pickle, in_current_sage: bool = False, default_assumptions: bool = False, eval: bool = False, preparse: bool = True, pedantic: bool = False):
    '''
    This is a helper function for :func:`explain_pickle`.  It takes a decompressed
    pickle string as input; other than that, its options are all the same
    as :func:`explain_pickle`.

    EXAMPLES::

        sage: sage.misc.explain_pickle.explain_pickle_string(dumps("Hello, world", compress=False))
        \'Hello, world\'

    (See the documentation for :func:`explain_pickle` for many more examples.)
    '''

valid_name_re: Incomplete

def name_is_valid(name):
    """
    Test whether a string is a valid Python identifier.  (We use a
    conservative test, that only allows ASCII identifiers.)

    EXAMPLES::

        sage: from sage.misc.explain_pickle import name_is_valid
        sage: name_is_valid('fred')
        True
        sage: name_is_valid('Yes!ValidName')
        False
        sage: name_is_valid('_happy_1234')
        True
    """

the_mark: str

class PickleObject:
    '''
    Pickles have a stack-based virtual machine.  The :func:`explain_pickle`
    pickle interpreter mostly uses :class:`sage.misc.sage_input.SageInputExpression` objects
    as the stack values.  However, sometimes we want some more information
    about the value on the stack, so that we can generate better
    (prettier, less confusing) code.  In such cases, we push
    a :class:`PickleObject` instead of a :class:`~sage.misc.sage_input.SageInputExpression`.
    A :class:`PickleObject`
    contains a value (which may be a standard Python value, or a
    :class:`PickleDict` or :class:`PickleInstance`), an expression
    (a :class:`~sage.misc.sage_input.SageInputExpression`),
    and an "immutable" flag (which checks whether this object
    has been converted to a :class:`SageInputExpression`; if it has, then we
    must not mutate the object, since the :class:`SageInputExpression` would not
    reflect the changes).
    '''
    value: Incomplete
    expression: Incomplete
    immutable: bool
    def __init__(self, value, expression) -> None:
        """
        Construct a PickleObject.

        TESTS::

            sage: from sage.misc.explain_pickle import *
            sage: v = PickleObject(1, 2)
            sage: v.value
            1
            sage: v.expression
            2
            sage: v.immutable
            False
        """

class PickleDict:
    """
    An object which can be used as the value of a :class:`PickleObject`.  The items
    is a list of key-value pairs, where the keys and values are
    :class:`SageInputExpression` objects.  We use this to help construct dictionary literals,
    instead of always starting with an empty dictionary and assigning to
    it.
    """
    items: Incomplete
    def __init__(self, items) -> None:
        """
        Initialize a PickleDict.

        EXAMPLES::

            sage: from sage.misc.explain_pickle import *
            sage: PickleDict([('a', 1)]).items
            [('a', 1)]
        """

class PickleInstance:
    """
    An object which can be used as the value of a :class:`PickleObject`.  Unlike
    other possible values of a :class:`PickleObject`, a :class:`PickleInstance` doesn't represent
    an exact value; instead, it gives the class (type) of the object.
    """
    klass: Incomplete
    def __init__(self, klass) -> None:
        """
        Initialize a PickleInstance.

        EXAMPLES::

            sage: from sage.misc.explain_pickle import *
            sage: PickleInstance(Integer).klass
            <class 'sage.rings.integer.Integer'>
        """

class PickleExplainer:
    """
    An interpreter for the pickle virtual machine, that executes
    symbolically and constructs :class:`SageInputExpression` objects instead of
    directly constructing values.
    """
    sib: Incomplete
    in_current_sage: Incomplete
    default_assumptions: Incomplete
    pedantic: Incomplete
    stopped: bool
    stack: Incomplete
    memo: Incomplete
    new_instance: Incomplete
    def __init__(self, sib, in_current_sage: bool = False, default_assumptions: bool = False, pedantic: bool = False) -> None:
        """
        Initialize a PickleExplainer interpreter for the pickle virtual machine.

        EXAMPLES::

            sage: from sage.misc.explain_pickle import *
            sage: from sage.misc.sage_input import SageInputBuilder
            sage: pe = PickleExplainer(SageInputBuilder(), in_current_sage=True, default_assumptions=False, pedantic=True)
            sage: pe.in_current_sage
            True
            sage: pe.pedantic
            True
        """
    def run_pickle(self, p):
        """
        Given an (uncompressed) pickle as a string, run the pickle
        in this virtual machine.  Once a STOP has been executed, return
        the result (a :class:`SageInputExpression` representing code which, when
        evaluated, will give the value of the pickle).

        EXAMPLES::

            sage: from sage.misc.explain_pickle import *
            sage: from sage.misc.sage_input import SageInputBuilder
            sage: sib = SageInputBuilder()
            sage: pe = PickleExplainer(sib, in_current_sage=True, default_assumptions=False, pedantic=True)
            sage: sib(pe.run_pickle('T\\5\\0\\0\\0hello.'))  # py2
            {atomic:'hello'}
        """
    def check_value(self, v) -> None:
        """
        Check that the given value is either a :class:`SageInputExpression` or a
        :class:`PickleObject`. Used for internal sanity checking.

        EXAMPLES::

            sage: from sage.misc.explain_pickle import *
            sage: from sage.misc.sage_input import SageInputBuilder
            sage: sib = SageInputBuilder()
            sage: pe = PickleExplainer(sib, in_current_sage=True, default_assumptions=False, pedantic=True)
            sage: pe.check_value(7)
            Traceback (most recent call last):
            ...
            AssertionError
            sage: pe.check_value(sib(7))
        """
    def push(self, v) -> None:
        """
        Push a value onto the virtual machine's stack.

        EXAMPLES::

            sage: from sage.misc.explain_pickle import *
            sage: from sage.misc.sage_input import SageInputBuilder
            sage: sib = SageInputBuilder()
            sage: pe = PickleExplainer(sib, in_current_sage=True, default_assumptions=False, pedantic=True)
            sage: pe.push(sib(7))
            sage: pe.stack[-1]
            {atomic:7}
        """
    def push_and_share(self, v) -> None:
        """
        Push a value onto the virtual machine's stack; also mark it as shared
        for :func:`sage_input` if we are in pedantic mode.

        EXAMPLES::

            sage: from sage.misc.explain_pickle import *
            sage: from sage.misc.sage_input import SageInputBuilder
            sage: sib = SageInputBuilder()
            sage: pe = PickleExplainer(sib, in_current_sage=True, default_assumptions=False, pedantic=True)
            sage: pe.push_and_share(sib(7))
            sage: pe.stack[-1]
            {atomic:7}
            sage: pe.stack[-1]._sie_share
            True
        """
    def pop(self):
        """
        Pop a value from the virtual machine's stack, and return it.

        EXAMPLES::

            sage: from sage.misc.explain_pickle import *
            sage: from sage.misc.sage_input import SageInputBuilder
            sage: sib = SageInputBuilder()
            sage: pe = PickleExplainer(sib, in_current_sage=True, default_assumptions=False, pedantic=True)
            sage: pe.push(sib(7))
            sage: pe.pop()
            {atomic:7}
        """
    def push_mark(self) -> None:
        """
        Push a 'mark' onto the virtual machine's stack.

        EXAMPLES::

            sage: from sage.misc.explain_pickle import *
            sage: from sage.misc.sage_input import SageInputBuilder
            sage: sib = SageInputBuilder()
            sage: pe = PickleExplainer(sib, in_current_sage=True, default_assumptions=False, pedantic=True)
            sage: pe.push_mark()
            sage: pe.stack[-1]
            'mark'
            sage: pe.stack[-1] is the_mark
            True
        """
    def pop_to_mark(self):
        """
        Pop all values down to the 'mark' from the virtual machine's stack,
        and return the values as a list.

        EXAMPLES::

            sage: from sage.misc.explain_pickle import *
            sage: from sage.misc.sage_input import SageInputBuilder
            sage: sib = SageInputBuilder()
            sage: pe = PickleExplainer(sib, in_current_sage=True, default_assumptions=False, pedantic=True)
            sage: pe.push_mark()
            sage: pe.push(sib(7))
            sage: pe.push(sib('hello'))
            sage: pe.pop_to_mark()
            [{atomic:7}, {atomic:'hello'}]
        """
    def share(self, v):
        """
        Mark a :func:`sage_input` value as shared, if we are in pedantic mode.

        EXAMPLES::

            sage: from sage.misc.explain_pickle import *
            sage: from sage.misc.sage_input import SageInputBuilder
            sage: sib = SageInputBuilder()
            sage: pe = PickleExplainer(sib, in_current_sage=True,
            ....:                      default_assumptions=False, pedantic=True)
            sage: v = sib(7)
            sage: v._sie_share
            False
            sage: pe.share(v)
            {atomic:7}
            sage: v._sie_share
            True
        """
    def is_mutable_pickle_object(self, v):
        """
        Test whether a :class:`PickleObject` is mutable (has never been converted
        to a :class:`SageInputExpression`).

        EXAMPLES::

            sage: from sage.misc.explain_pickle import *
            sage: from sage.misc.sage_input import SageInputBuilder
            sage: sib = SageInputBuilder()
            sage: pe = PickleExplainer(sib, in_current_sage=True,
            ....:                      default_assumptions=False, pedantic=True)
            sage: v = PickleObject(1, sib(1))
            sage: pe.is_mutable_pickle_object(v)
            True
            sage: sib(v)
            {atomic:1}
            sage: pe.is_mutable_pickle_object(v)
            False
        """
    def APPEND(self) -> None:
        """
        TESTS::

            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(['a'])
                0: \\x80 PROTO      2
                2: ]    EMPTY_LIST
                3: q    BINPUT     0
                5: X    BINUNICODE 'a'
               11: q    BINPUT     1
               13: a    APPEND
               14: .    STOP
            highest protocol among opcodes = 2
            explain_pickle in_current_sage=True/False:
            ['a']
            result: ['a']

        As shown above, we prefer to create a list literal.  This is not
        possible if the list is recursive::

            sage: v = []
            sage: v.append(v)
            sage: check_pickle(v)
                0: \\x80 PROTO      2
                2: ]    EMPTY_LIST
                3: q    BINPUT     0
                5: h    BINGET     0
                7: a    APPEND
                8: .    STOP
            highest protocol among opcodes = 2
            explain_pickle in_current_sage=True/False:
            si = []
            list.append(si, si)
            si
            result: [[...]]
        """
    def APPENDS(self) -> None:
        """
        TESTS::

            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(['a', 'b'])
                0: \\x80 PROTO      2
                2: ]    EMPTY_LIST
                3: q    BINPUT     0
                5: (    MARK
                6: X        BINUNICODE 'a'
               12: q        BINPUT     1
               14: X        BINUNICODE 'b'
               20: q        BINPUT     2
               22: e        APPENDS    (MARK at 5)
               23: .    STOP
            highest protocol among opcodes = 2
            explain_pickle in_current_sage=True/False:
            ['a', 'b']
            result: ['a', 'b']

        As shown above, we prefer to create a list literal.  This is not
        possible if the list is recursive::

            sage: v = []
            sage: v.append(v)
            sage: v.append(v)
            sage: check_pickle(v)
                0: \\x80 PROTO      2
                2: ]    EMPTY_LIST
                3: q    BINPUT     0
                5: (    MARK
                6: h        BINGET     0
                8: h        BINGET     0
               10: e        APPENDS    (MARK at 5)
               11: .    STOP
            highest protocol among opcodes = 2
            explain_pickle in_current_sage=True/False:
            si = []
            list.extend(si, [si, si])
            si
            result: [[...], [...]]
        """
    def BINFLOAT(self, f) -> None:
        """
        TESTS::

            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(float(pi))                                                # needs sage.symbolic
                0: \\x80 PROTO      2
                2: G    BINFLOAT   3.141592653589793
               11: .    STOP
            highest protocol among opcodes = 2
            explain_pickle in_current_sage=True/False:
            3.141592653589793
            result: 3.141592653589793
        """
    def BINGET(self, n) -> None:
        """
        TESTS::

            sage: from pickle import *
            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(EMPTY_LIST + BINPUT + 'x' + POP + BINGET + 'x' + '.')  # py2
                0: ]    EMPTY_LIST
                1: q    BINPUT     120
                3: 0    POP
                4: h    BINGET     120
                6: .    STOP
            highest protocol among opcodes = 1
            explain_pickle in_current_sage=True/False:
            []
            result: []
        """
    def BININT(self, n) -> None:
        """
        TESTS::

            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(dumps(100000r, compress=False))  # py2
                0: \\x80 PROTO      2
                2: J    BININT     100000
                7: .    STOP
            highest protocol among opcodes = 2
            explain_pickle in_current_sage=True/False:
            100000
            result: 100000
        """
    def BININT1(self, n) -> None:
        """
        TESTS::

            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(dumps(100r, compress=False))  # py2
                0: \\x80 PROTO      2
                2: K    BININT1    100
                4: .    STOP
            highest protocol among opcodes = 2
            explain_pickle in_current_sage=True/False:
            100
            result: 100
        """
    def BININT2(self, n) -> None:
        """
        TESTS::

            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(dumps(1000r, compress=False))  # py2
                0: \\x80 PROTO      2
                2: M    BININT2    1000
                5: .    STOP
            highest protocol among opcodes = 2
            explain_pickle in_current_sage=True/False:
            1000
            result: 1000
        """
    def BINPUT(self, n) -> None:
        """
        TESTS::

            sage: from pickle import *
            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(EMPTY_LIST + BINPUT + 'x' + POP + BINGET + 'x')  # py2
                0: ]    EMPTY_LIST
                1: q    BINPUT     120
                3: 0    POP
                4: h    BINGET     120
                6: .    STOP
            highest protocol among opcodes = 1
            explain_pickle in_current_sage=True/False:
            []
            result: []
        """
    def BINSTRING(self, s) -> None:
        """
        TESTS::

            sage: from sage.misc.explain_pickle import *
            sage: check_pickle('T\\5\\0\\0\\0hello.')  # py2
                0: T    BINSTRING 'hello'
               10: .    STOP
            highest protocol among opcodes = 1
            explain_pickle in_current_sage=True/False:
            'hello'
            result: 'hello'
        """
    def BINUNICODE(self, s) -> None:
        """
        TESTS::

            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(u'hi\\u1234\\U00012345')  # py2
                0: \\x80 PROTO      2
                2: X    BINUNICODE u'hi\\u1234\\U00012345'
               16: q    BINPUT     1
               18: .    STOP
            highest protocol among opcodes = 2
            explain_pickle in_current_sage=True/False:
            u'hi\\u1234\\U00012345'
            result: u'hi\\u1234\\U00012345'
        """
    def BUILD(self) -> None:
        """
        TESTS::

            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(TestBuild())
                0: \\x80 PROTO      2
                2: c    GLOBAL     'sage.misc.explain_pickle TestBuild'
               38: q    BINPUT     0
               40: )    EMPTY_TUPLE
               41: \\x81 NEWOBJ
               42: q    BINPUT     1
               44: }    EMPTY_DICT
               45: q    BINPUT     2
               47: X    BINUNICODE 'x'
               53: q    BINPUT     3
               55: K    BININT1    3
               57: s    SETITEM
               58: }    EMPTY_DICT
               59: q    BINPUT     4
               61: X    BINUNICODE 'y'
               67: q    BINPUT     5
               69: K    BININT1    4
               71: s    SETITEM
               72: \\x86 TUPLE2
               73: q    BINPUT     6
               75: b    BUILD
               76: .    STOP
            highest protocol among opcodes = 2
            explain_pickle in_current_sage=True:
            from sage.misc.explain_pickle import TestBuild
            si = unpickle_newobj(TestBuild, ())
            si.__dict__['x'] = 3
            setattr(si, 'y', 4)
            si
            explain_pickle in_current_sage=False:
            pg_TestBuild = unpickle_global('sage.misc.explain_pickle', 'TestBuild')
            si = unpickle_newobj(pg_TestBuild, ())
            unpickle_build(si, ({'x':3}, {'y':4}))
            si
            result: TestBuild: x=3; y=4

        ::

            sage: check_pickle(TestBuildSetstate(), verbose_eval=True)
                0: \\x80 PROTO      2
                2: c    GLOBAL     'sage.misc.explain_pickle TestBuildSetstate'
               46: q    BINPUT     0
               48: )    EMPTY_TUPLE
               49: \\x81 NEWOBJ
               50: q    BINPUT     1
               52: }    EMPTY_DICT
               53: q    BINPUT     2
               55: X    BINUNICODE 'x'
               61: q    BINPUT     3
               63: K    BININT1    3
               65: s    SETITEM
               66: }    EMPTY_DICT
               67: q    BINPUT     4
               69: X    BINUNICODE 'y'
               75: q    BINPUT     5
               77: K    BININT1    4
               79: s    SETITEM
               80: \\x86 TUPLE2
               81: q    BINPUT     6
               83: b    BUILD
               84: .    STOP
            highest protocol among opcodes = 2
            explain_pickle in_current_sage=True:
            from sage.misc.explain_pickle import TestBuildSetstate
            si = unpickle_newobj(TestBuildSetstate, ())
            si.__setstate__(({'x':3}, {'y':4}))
            si
            explain_pickle in_current_sage=False:
            pg_TestBuildSetstate = unpickle_global('sage.misc.explain_pickle', 'TestBuildSetstate')
            si = unpickle_newobj(pg_TestBuildSetstate, ())
            unpickle_build(si, ({'x':3}, {'y':4}))
            si
            evaluating explain_pickle in_current_sage=True:
            setting state from ({'x': 3}, {'y': 4})
            evaluating explain_pickle in_current_sage=False:
            setting state from ({'x': 3}, {'y': 4})
            loading pickle with cPickle:
            setting state from ({'x': 3}, {'y': 4})
            result: TestBuild: x=4; y=3
        """
    def DICT(self) -> None:
        """
        TESTS::

            sage: from pickle import *
            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(DICT, args=('mark', 'a', 1, 2, 'b'))  # py2
                0: (    MARK
                1: P        PERSID     '1'
                4: P        PERSID     '2'
                7: P        PERSID     '3'
               10: P        PERSID     '4'
               13: d        DICT       (MARK at 0)
               14: .    STOP
            highest protocol among opcodes = 0
            explain_pickle in_current_sage=True/False:
            {unpickle_persistent('1'):unpickle_persistent('2'), unpickle_persistent('3'):unpickle_persistent('4')}
            result: {'a': 1, 2: 'b'}
        """
    def DUP(self) -> None:
        """
        TESTS::

            sage: from pickle import *
            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(EMPTY_LIST + DUP + TUPLE2 + STOP)  # py2
                0: ]    EMPTY_LIST
                1: 2    DUP
                2: \\x86 TUPLE2
                3: .    STOP
            highest protocol among opcodes = 2
            explain_pickle in_current_sage=True/False:
            si = []
            (si, si)
            result: ([], [])
        """
    def EMPTY_DICT(self) -> None:
        """
        TESTS::

            sage: from pickle import *
            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(EMPTY_DICT)  # py2
                0: }    EMPTY_DICT
                1: .    STOP
            highest protocol among opcodes = 1
            explain_pickle in_current_sage=True/False:
            {}
            result: {}
        """
    def EMPTY_LIST(self) -> None:
        """
        TESTS::

            sage: from pickle import *
            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(EMPTY_LIST)  # py2
                0: ]    EMPTY_LIST
                1: .    STOP
            highest protocol among opcodes = 1
            explain_pickle in_current_sage=True/False:
            []
            result: []
        """
    def EMPTY_TUPLE(self) -> None:
        """
        TESTS::

            sage: from pickle import *
            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(EMPTY_TUPLE)  # py2
                0: )    EMPTY_TUPLE
                1: .    STOP
            highest protocol among opcodes = 1
            explain_pickle in_current_sage=True/False:
            ()
            result: ()
        """
    def EXT1(self, n) -> None:
        """
        TESTS::

            sage: from copyreg import *
            sage: from sage.misc.explain_pickle import *
            sage: add_extension('sage.misc.explain_pickle', 'EmptyNewstyleClass', 42)
            sage: check_pickle(EmptyNewstyleClass())
                0: \\x80 PROTO      2
                2: \\x82 EXT1       42
                4: )    EMPTY_TUPLE
                5: \\x81 NEWOBJ
                6: q    BINPUT     0
                8: .    STOP
            highest protocol among opcodes = 2
            explain_pickle in_current_sage=True/False:
            unpickle_newobj(unpickle_extension(42), ())
            result: EmptyNewstyleClass
            sage: remove_extension('sage.misc.explain_pickle', 'EmptyNewstyleClass', 42)
        """
    def EXT2(self, n) -> None:
        """
        TESTS::

            sage: from copyreg import *
            sage: from sage.misc.explain_pickle import *
            sage: add_extension('sage.misc.explain_pickle', 'EmptyNewstyleClass', 31415)
            sage: check_pickle(EmptyNewstyleClass())
                0: \\x80 PROTO      2
                2: \\x83 EXT2       31415
                5: )    EMPTY_TUPLE
                6: \\x81 NEWOBJ
                7: q    BINPUT     0
                9: .    STOP
            highest protocol among opcodes = 2
            explain_pickle in_current_sage=True/False:
            unpickle_newobj(unpickle_extension(31415), ())
            result: EmptyNewstyleClass
            sage: remove_extension('sage.misc.explain_pickle', 'EmptyNewstyleClass', 31415)
        """
    def EXT4(self, n) -> None:
        """
        TESTS::

            sage: from copyreg import *
            sage: from sage.misc.explain_pickle import *
            sage: add_extension('sage.misc.explain_pickle', 'EmptyNewstyleClass', 27182818)
            sage: check_pickle(EmptyNewstyleClass())
                0: \\x80 PROTO      2
                2: \\x84 EXT4       27182818
                7: )    EMPTY_TUPLE
                8: \\x81 NEWOBJ
                9: q    BINPUT     0
               11: .    STOP
            highest protocol among opcodes = 2
            explain_pickle in_current_sage=True/False:
            unpickle_newobj(unpickle_extension(27182818), ())
            result: EmptyNewstyleClass
            sage: remove_extension('sage.misc.explain_pickle', 'EmptyNewstyleClass', 27182818)
        """
    def FLOAT(self, f) -> None:
        """
        TESTS::

            sage: from pickle import *
            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(FLOAT + '2.71828\\n')  # py2
                0: F    FLOAT      2.71828
                9: .    STOP
            highest protocol among opcodes = 0
            explain_pickle in_current_sage=True/False:
            2.71828
            result: 2.71828
        """
    def GET(self, n) -> None:
        """
        TESTS::

            sage: from pickle import *
            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(EMPTY_LIST + PUT + '1\\n' + POP + GET + '1\\n' + '.')  # py2
                0: ]    EMPTY_LIST
                1: p    PUT        1
                4: 0    POP
                5: g    GET        1
                8: .    STOP
            highest protocol among opcodes = 1
            explain_pickle in_current_sage=True/False:
            []
            result: []
        """
    def GLOBAL(self, name) -> None:
        """
        TESTS::

            sage: from sage.misc.explain_pickle import *

        We've used register_unpickle_override so that unpickle_global
        will map TestGlobalOldName to TestGlobalNewName.

        ::

            sage: check_pickle(TestGlobalOldName())
                0: \\x80 PROTO      2
                2: c    GLOBAL     'sage.misc.explain_pickle TestGlobalOldName'
               46: q    BINPUT     0
               48: )    EMPTY_TUPLE
               49: \\x81 NEWOBJ
               50: q    BINPUT     1
               52: .    STOP
            highest protocol among opcodes = 2
            explain_pickle in_current_sage=True:
            from sage.misc.explain_pickle import TestGlobalNewName
            unpickle_newobj(TestGlobalNewName, ())
            explain_pickle in_current_sage=False:
            pg_TestGlobalOldName = unpickle_global('sage.misc.explain_pickle', 'TestGlobalOldName')
            unpickle_newobj(pg_TestGlobalOldName, ())
            result: TestGlobalNewName

        Note that default_assumptions blithely assumes that it should
        use the old name, giving code that doesn't actually work as
        desired::

            sage: explain_pickle(dumps(TestGlobalOldName()), default_assumptions=True)
            from sage.misc.explain_pickle import TestGlobalOldName
            unpickle_newobj(TestGlobalOldName, ())

        A class name need not be a valid identifier::

            sage: sage.misc.explain_pickle.__dict__['funny$name'] = TestGlobalFunnyName # see comment at end of file
            sage: check_pickle((TestGlobalFunnyName(), TestGlobalFunnyName()))
                0: \\x80 PROTO      2
                2: c    GLOBAL     'sage.misc.explain_pickle TestGlobalFunnyName'
               48: q    BINPUT     0
               50: )    EMPTY_TUPLE
               51: \\x81 NEWOBJ
               52: q    BINPUT     1
               54: h    BINGET     0
               56: )    EMPTY_TUPLE
               57: \\x81 NEWOBJ
               58: q    BINPUT     2
               60: \\x86 TUPLE2
               61: q    BINPUT     3
               63: .    STOP
            highest protocol among opcodes = 2
            explain_pickle in_current_sage=True:
            from sage.misc.explain_pickle import TestGlobalFunnyName
            (unpickle_newobj(TestGlobalFunnyName, ()), unpickle_newobj(TestGlobalFunnyName, ()))
            explain_pickle in_current_sage=False:
            pg_TestGlobalFunnyName = unpickle_global('sage.misc.explain_pickle', 'TestGlobalFunnyName')
            (unpickle_newobj(pg_TestGlobalFunnyName, ()), unpickle_newobj(pg_TestGlobalFunnyName, ()))
            result: (TestGlobalFunnyName, TestGlobalFunnyName)
        """
    def INST(self, name) -> None:
        """
        TESTS::

            sage: import pickle
            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(pickle.dumps(EmptyOldstyleClass(), protocol=0))  # py2
                0: (    MARK
                1: i        INST       'sage.misc.explain_pickle EmptyOldstyleClass' (MARK at 0)
               46: p    PUT        0
               49: (    MARK
               50: d        DICT       (MARK at 49)
               51: p    PUT        1
               54: b    BUILD
               55: .    STOP
            highest protocol among opcodes = 0
            explain_pickle in_current_sage=True:
            from types import InstanceType
            from sage.misc.explain_pickle import EmptyOldstyleClass
            InstanceType(EmptyOldstyleClass)
            explain_pickle in_current_sage=False:
            pg_EmptyOldstyleClass = unpickle_global('sage.misc.explain_pickle', 'EmptyOldstyleClass')
            pg = unpickle_instantiate(pg_EmptyOldstyleClass, ())
            unpickle_build(pg, {})
            pg
            result: EmptyOldstyleClass
        """
    def INT(self, n) -> None:
        '''
        TESTS::

            sage: from pickle import *
            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(INT + "-12345\\n")  # py2
                0: I    INT        -12345
                8: .    STOP
            highest protocol among opcodes = 0
            explain_pickle in_current_sage=True/False:
            -12345
            result: -12345

        INT can also be used to record True and False::

            sage: check_pickle(INT + "00\\n")  # py2
                0: I    INT        False
                4: .    STOP
            highest protocol among opcodes = 0
            explain_pickle in_current_sage=True/False:
            False
            result: False
            sage: check_pickle(INT + "01\\n")  # py2
                0: I    INT        True
                4: .    STOP
            highest protocol among opcodes = 0
            explain_pickle in_current_sage=True/False:
            True
            result: True
        '''
    def LIST(self) -> None:
        """
        TESTS::

            sage: from pickle import *
            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(MARK + NONE + NEWFALSE + LIST)  # py2
                0: (    MARK
                1: N        NONE
                2: \\x89     NEWFALSE
                3: l        LIST       (MARK at 0)
                4: .    STOP
            highest protocol among opcodes = 2
            explain_pickle in_current_sage=True/False:
            [None, False]
            result: [None, False]
        """
    def LONG(self, n) -> None:
        '''
        TESTS::

            sage: from pickle import *
            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(LONG + "12345678909876543210123456789L\\n")  # py2
                0: L    LONG       12345678909876543210123456789L
               32: .    STOP
            highest protocol among opcodes = 0
            explain_pickle in_current_sage=True/False:
            12345678909876543210123456789
            result: 12345678909876543210123456789L
        '''
    def LONG1(self, n) -> None:
        """
        TESTS::

            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(1L)  # py2
                0: \\x80 PROTO      2
                2: \\x8a LONG1      1L
                5: .    STOP
            highest protocol among opcodes = 2
            explain_pickle in_current_sage=True/False:
            1L
            result: 1L
        """
    def LONG4(self, n) -> None:
        """
        TESTS::

            sage: from pickle import *
            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(LONG4 + '\\014\\0\\0\\0' + 'hello, world')  # py2
                0: \\x8b LONG4      31079605376604435891501163880L
               17: .    STOP
            highest protocol among opcodes = 2
            explain_pickle in_current_sage=True/False:
            31079605376604435891501163880
            result: 31079605376604435891501163880L
        """
    def LONG_BINGET(self, n) -> None:
        """
        TESTS::

            sage: from pickle import *
            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(EMPTY_LIST + LONG_BINPUT + 'Sage' + POP + LONG_BINGET + 'Sage')  # py2
                0: ]    EMPTY_LIST
                1: r    LONG_BINPUT 1701273939
                6: 0    POP
                7: j    LONG_BINGET 1701273939
               12: .    STOP
            highest protocol among opcodes = 1
            explain_pickle in_current_sage=True/False:
            []
            result: []
        """
    def LONG_BINPUT(self, n) -> None:
        """
        TESTS::

            sage: from pickle import *
            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(EMPTY_LIST + LONG_BINPUT + 'Sage' + POP + LONG_BINGET + 'Sage')  # py2
                0: ]    EMPTY_LIST
                1: r    LONG_BINPUT 1701273939
                6: 0    POP
                7: j    LONG_BINGET 1701273939
               12: .    STOP
            highest protocol among opcodes = 1
            explain_pickle in_current_sage=True/False:
            []
            result: []
        """
    def MARK(self) -> None:
        """
        TESTS::

            sage: from pickle import *
            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(MARK + TUPLE)  # py2
                0: (    MARK
                1: t        TUPLE      (MARK at 0)
                2: .    STOP
            highest protocol among opcodes = 0
            explain_pickle in_current_sage=True/False:
            ()
            result: ()
        """
    def NEWFALSE(self) -> None:
        """
        TESTS::

            sage: from pickle import *
            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(NEWFALSE)  # py2
                0: \\x89 NEWFALSE
                1: .    STOP
            highest protocol among opcodes = 2
            explain_pickle in_current_sage=True/False:
            False
            result: False
        """
    def NEWTRUE(self) -> None:
        """
        TESTS::

            sage: from pickle import *
            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(NEWTRUE)  # py2
                0: \\x88 NEWTRUE
                1: .    STOP
            highest protocol among opcodes = 2
            explain_pickle in_current_sage=True/False:
            True
            result: True
        """
    def NEWOBJ(self) -> None:
        """
        TESTS::

            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(EmptyNewstyleClass())
                0: \\x80 PROTO      2
                2: c    GLOBAL     'sage.misc.explain_pickle EmptyNewstyleClass'
               47: q    BINPUT     0
               49: )    EMPTY_TUPLE
               50: \\x81 NEWOBJ
               51: q    BINPUT     1
               53: .    STOP
            highest protocol among opcodes = 2
            explain_pickle in_current_sage=True:
            from sage.misc.explain_pickle import EmptyNewstyleClass
            unpickle_newobj(EmptyNewstyleClass, ())
            explain_pickle in_current_sage=False:
            pg_EmptyNewstyleClass = unpickle_global('sage.misc.explain_pickle', 'EmptyNewstyleClass')
            unpickle_newobj(pg_EmptyNewstyleClass, ())
            result: EmptyNewstyleClass
        """
    def NONE(self) -> None:
        """
        TESTS::

            sage: from pickle import *
            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(NONE)  # py2
                0: N    NONE
                1: .    STOP
            highest protocol among opcodes = 0
            explain_pickle in_current_sage=True/False:
            None
            result: None
        """
    def OBJ(self) -> None:
        """
        TESTS::

            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(EmptyOldstyleClass())
                0: \\x80 PROTO      2
                2: c    GLOBAL     'sage.misc.explain_pickle EmptyOldstyleClass'
               47: q    BINPUT     0
               49: )    EMPTY_TUPLE
               50: \\x81 NEWOBJ
               51: q    BINPUT     1
               53: .    STOP
            highest protocol among opcodes = 2
            explain_pickle in_current_sage=True:
            from sage.misc.explain_pickle import EmptyOldstyleClass
            unpickle_newobj(EmptyOldstyleClass, ())
            explain_pickle in_current_sage=False:
            pg_EmptyOldstyleClass = unpickle_global('sage.misc.explain_pickle', 'EmptyOldstyleClass')
            unpickle_newobj(pg_EmptyOldstyleClass, ())
            result: EmptyOldstyleClass
        """
    def PERSID(self, id) -> None:
        '''
        TESTS::

            sage: from pickle import *
            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(PERSID + "0\\n" + \'.\', args=(\'Yo!\',))  # py2
                0: P    PERSID     \'0\'
                3: .    STOP
            highest protocol among opcodes = 0
            explain_pickle in_current_sage=True/False:
            unpickle_persistent(\'0\')
            result: \'Yo!\'
        '''
    def BINPERSID(self) -> None:
        '''
        TESTS::

            sage: from pickle import *
            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(INT + "0\\n" + BINPERSID + \'.\', args=(\'Yo!\',))  # py2
                0: I    INT        0
                3: Q    BINPERSID
                4: .    STOP
            highest protocol among opcodes = 1
            explain_pickle in_current_sage=True/False:
            unpickle_persistent(0)
            result: \'Yo!\'
        '''
    def POP(self) -> None:
        '''
        TESTS::

            sage: from pickle import *
            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(INT + "0\\n" + POP + INT + "42\\n")  # py2
                0: I    INT        0
                3: 0    POP
                4: I    INT        42
                8: .    STOP
            highest protocol among opcodes = 0
            explain_pickle in_current_sage=True/False:
            42
            result: 42
        '''
    def POP_MARK(self) -> None:
        """
        TESTS::

            sage: from pickle import *
            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(MARK + NONE + NEWFALSE + POP_MARK + NEWTRUE)  # py2
                0: (    MARK
                1: N        NONE
                2: \\x89     NEWFALSE
                3: 1        POP_MARK   (MARK at 0)
                4: \\x88 NEWTRUE
                5: .    STOP
            highest protocol among opcodes = 2
            explain_pickle in_current_sage=True/False:
            True
            result: True
        """
    def PROTO(self, proto) -> None:
        """
        TESTS::

            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(0r)  # py2
                0: \\x80 PROTO      2
                2: K    BININT1    0
                4: .    STOP
            highest protocol among opcodes = 2
            explain_pickle in_current_sage=True/False:
            0
            result: 0
        """
    def PUT(self, n) -> None:
        """
        TESTS::

            sage: from pickle import *
            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(EMPTY_LIST + PUT + '1\\n' + POP + GET + '1\\n' + '.')  # py2
                0: ]    EMPTY_LIST
                1: p    PUT        1
                4: 0    POP
                5: g    GET        1
                8: .    STOP
            highest protocol among opcodes = 1
            explain_pickle in_current_sage=True/False:
            []
            result: []
        """
    def REDUCE(self) -> None:
        """
        TESTS::

            sage: import pickle
            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(pickle.dumps(EmptyNewstyleClass(), protocol=1))  # py2
                0: c    GLOBAL     'copy_reg _reconstructor'
               25: q    BINPUT     0
               27: (    MARK
               28: c        GLOBAL     'sage.misc.explain_pickle EmptyNewstyleClass'
               73: q        BINPUT     1
               75: c        GLOBAL     '__builtin__ object'
               95: q        BINPUT     2
               97: N        NONE
               98: t        TUPLE      (MARK at 27)
               99: q    BINPUT     3
              101: R    REDUCE
              102: q    BINPUT     4
              104: .    STOP
            highest protocol among opcodes = 1
            explain_pickle in_current_sage=True:
            from copy_reg import _reconstructor
            from sage.misc.explain_pickle import EmptyNewstyleClass
            from __builtin__ import object
            _reconstructor(EmptyNewstyleClass, object, None)
            explain_pickle in_current_sage=False:
            pg__reconstructor = unpickle_global('copy_reg', '_reconstructor')
            pg_EmptyNewstyleClass = unpickle_global('sage.misc.explain_pickle', 'EmptyNewstyleClass')
            pg_object = unpickle_global('__builtin__', 'object')
            pg__reconstructor(pg_EmptyNewstyleClass, pg_object, None)
            result: EmptyNewstyleClass

        ::

            sage: check_pickle(TestReduceGetinitargs(), verbose_eval=True)  # py2
            Running __init__ for TestReduceGetinitargs
                0: \\x80 PROTO      2
                2: (    MARK
                3: c        GLOBAL     'sage.misc.explain_pickle TestReduceGetinitargs'
               51: q        BINPUT     1
               53: o        OBJ        (MARK at 2)
               54: q    BINPUT     2
               56: }    EMPTY_DICT
               57: q    BINPUT     3
               59: b    BUILD
               60: .    STOP
            highest protocol among opcodes = 2
            explain_pickle in_current_sage=True:
            from sage.misc.explain_pickle import TestReduceGetinitargs
            TestReduceGetinitargs()
            explain_pickle in_current_sage=False:
            pg_TestReduceGetinitargs = unpickle_global('sage.misc.explain_pickle', 'TestReduceGetinitargs')
            pg = unpickle_instantiate(pg_TestReduceGetinitargs, ())
            unpickle_build(pg, {})
            pg
            evaluating explain_pickle in_current_sage=True:
            Running __init__ for TestReduceGetinitargs
            evaluating explain_pickle in_current_sage=False:
            Running __init__ for TestReduceGetinitargs
            loading pickle with cPickle:
            Running __init__ for TestReduceGetinitargs
            result: TestReduceGetinitargs

        ::

            sage: check_pickle(TestReduceNoGetinitargs(), verbose_eval=True)  # py2
            Running __init__ for TestReduceNoGetinitargs
                0: \\x80 PROTO      2
                2: (    MARK
                3: c        GLOBAL     'sage.misc.explain_pickle TestReduceNoGetinitargs'
               53: q        BINPUT     1
               55: o        OBJ        (MARK at 2)
               56: q    BINPUT     2
               58: }    EMPTY_DICT
               59: q    BINPUT     3
               61: b    BUILD
               62: .    STOP
            highest protocol among opcodes = 2
            explain_pickle in_current_sage=True:
            from types import InstanceType
            from sage.misc.explain_pickle import TestReduceNoGetinitargs
            InstanceType(TestReduceNoGetinitargs)
            explain_pickle in_current_sage=False:
            pg_TestReduceNoGetinitargs = unpickle_global('sage.misc.explain_pickle', 'TestReduceNoGetinitargs')
            pg = unpickle_instantiate(pg_TestReduceNoGetinitargs, ())
            unpickle_build(pg, {})
            pg
            evaluating explain_pickle in_current_sage=True:
            evaluating explain_pickle in_current_sage=False:
            loading pickle with cPickle:
            result: TestReduceNoGetinitargs
        """
    def SETITEM(self) -> None:
        """
        TESTS::

            sage: import pickle
            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(pickle.dumps({'a': 'b'}))  # py2
                0: (    MARK
                1: d        DICT       (MARK at 0)
                2: p    PUT        0
                5: S    STRING     'a'
               10: p    PUT        1
               13: S    STRING     'b'
               18: p    PUT        2
               21: s    SETITEM
               22: .    STOP
            highest protocol among opcodes = 0
            explain_pickle in_current_sage=True/False:
            {'a':'b'}
            result: {'a': 'b'}

        We see above that we output the result as a dictionary literal, when
        possible.  This is impossible when a key or value is recursive.  First
        we test recursive values::

            sage: value_rec = dict()
            sage: value_rec['circular'] = value_rec
            sage: check_pickle(pickle.dumps(value_rec))  # py2
                0: (    MARK
                1: d        DICT       (MARK at 0)
                2: p    PUT        0
                5: S    STRING     'circular'
               17: p    PUT        1
               20: g    GET        0
               23: s    SETITEM
               24: .    STOP
            highest protocol among opcodes = 0
            explain_pickle in_current_sage=True/False:
            si = {}
            si['circular'] = si
            si
            result: {'circular': {...}}

        Then we test recursive keys::

            sage: key_rec = dict()
            sage: key = EmptyNewstyleClass()
            sage: key.circular = key_rec
            sage: key_rec[key] = 'circular'
            sage: check_pickle(pickle.dumps(key_rec))  # py2
                0: (    MARK
                1: d        DICT       (MARK at 0)
                2: p    PUT        0
                5: c    GLOBAL     'copy_reg _reconstructor'
               30: p    PUT        1
               33: (    MARK
               34: c        GLOBAL     'sage.misc.explain_pickle EmptyNewstyleClass'
               79: p        PUT        2
               82: c        GLOBAL     '__builtin__ object'
              102: p        PUT        3
              105: N        NONE
              106: t        TUPLE      (MARK at 33)
              107: p    PUT        4
              110: R    REDUCE
              111: p    PUT        5
              114: (    MARK
              115: d        DICT       (MARK at 114)
              116: p    PUT        6
              119: S    STRING     'circular'
              131: p    PUT        7
              134: g    GET        0
              137: s    SETITEM
              138: b    BUILD
              139: g    GET        7
              142: s    SETITEM
              143: .    STOP
            highest protocol among opcodes = 0
            explain_pickle in_current_sage=True:
            si1 = {}
            from copy_reg import _reconstructor
            from sage.misc.explain_pickle import EmptyNewstyleClass
            from __builtin__ import object
            si2 = _reconstructor(EmptyNewstyleClass, object, None)
            si2.__dict__['circular'] = si1
            si1[si2] = 'circular'
            si1
            explain_pickle in_current_sage=False:
            si1 = {}
            pg__reconstructor = unpickle_global('copy_reg', '_reconstructor')
            pg_EmptyNewstyleClass = unpickle_global('sage.misc.explain_pickle', 'EmptyNewstyleClass')
            pg_object = unpickle_global('__builtin__', 'object')
            si2 = pg__reconstructor(pg_EmptyNewstyleClass, pg_object, None)
            unpickle_build(si2, {'circular':si1})
            si1[si2] = 'circular'
            si1
            result: {EmptyNewstyleClass: 'circular'}
        """
    def SETITEMS(self) -> None:
        """
        TESTS::

            sage: import pickle
            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(pickle.dumps({'a': 'b', 1r : 2r}, protocol=2))  # py2
                0: \\x80 PROTO      2
                2: }    EMPTY_DICT
                3: q    BINPUT     0
                5: (    MARK
                6: U        SHORT_BINSTRING 'a'
                9: q        BINPUT     1
               11: U        SHORT_BINSTRING 'b'
               14: q        BINPUT     2
               16: K        BININT1    1
               18: K        BININT1    2
               20: u        SETITEMS   (MARK at 5)
               21: .    STOP
            highest protocol among opcodes = 2
            explain_pickle in_current_sage=True/False:
            {'a':'b', 1:2}
            result: {'a': 'b', 1: 2}

        Similar to the tests for SETITEM, we test recursive keys and values::

            sage: recdict = {}
            sage: recdict['Circular value'] = recdict
            sage: key = EmptyOldstyleClass()
            sage: key.recdict = recdict
            sage: recdict[key] = 'circular_key'
            sage: check_pickle(pickle.dumps(recdict, protocol=2))  # py2
                0: \\x80 PROTO      2
                2: }    EMPTY_DICT
                3: q    BINPUT     0
                5: (    MARK
                6: (        MARK
                7: c            GLOBAL     'sage.misc.explain_pickle EmptyOldstyleClass'
               52: q            BINPUT     1
               54: o            OBJ        (MARK at 6)
               55: q        BINPUT     2
               57: }        EMPTY_DICT
               58: q        BINPUT     3
               60: U        SHORT_BINSTRING 'recdict'
               69: q        BINPUT     4
               71: h        BINGET     0
               73: s        SETITEM
               74: b        BUILD
               75: U        SHORT_BINSTRING 'circular_key'
               89: q        BINPUT     5
               91: U        SHORT_BINSTRING 'Circular value'
              107: q        BINPUT     6
              109: h        BINGET     0
              111: u        SETITEMS   (MARK at 5)
              112: .    STOP
            highest protocol among opcodes = 2
            explain_pickle in_current_sage=True:
            si1 = {}
            from types import InstanceType
            from sage.misc.explain_pickle import EmptyOldstyleClass
            si2 = InstanceType(EmptyOldstyleClass)
            si2.__dict__['recdict'] = si1
            si1[si2] = 'circular_key'
            si1['Circular value'] = si1
            si1
            explain_pickle in_current_sage=False:
            si = {}
            pg_EmptyOldstyleClass = unpickle_global('sage.misc.explain_pickle', 'EmptyOldstyleClass')
            pg = unpickle_instantiate(pg_EmptyOldstyleClass, ())
            unpickle_build(pg, {'recdict':si})
            si[pg] = 'circular_key'
            si['Circular value'] = si
            si
            result: {EmptyOldstyleClass: 'circular_key', 'Circular value': {...}}
        """
    def SHORT_BINSTRING(self, s) -> None:
        """
        TESTS::

            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(dumps('hello', compress=False))  # py2
                0: \\x80 PROTO      2
                2: U    SHORT_BINSTRING 'hello'
                9: q    BINPUT     1
               11: .    STOP
            highest protocol among opcodes = 2
            explain_pickle in_current_sage=True/False:
            'hello'
            result: 'hello'
        """
    def STOP(self) -> None:
        """
        TESTS::

            sage: from pickle import *
            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(EMPTY_TUPLE)  # py2
                0: )    EMPTY_TUPLE
                1: .    STOP
            highest protocol among opcodes = 1
            explain_pickle in_current_sage=True/False:
            ()
            result: ()
        """
    def STRING(self, s) -> None:
        '''
        TESTS::

            sage: from sage.misc.explain_pickle import *
            sage: check_pickle("S\'Testing...\'\\n.")  # py2
                0: S    STRING     \'Testing...\'
               14: .    STOP
            highest protocol among opcodes = 0
            explain_pickle in_current_sage=True/False:
            \'Testing...\'
            result: \'Testing...\'
        '''
    def TUPLE(self) -> None:
        """
        TESTS::

            sage: import pickle
            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(pickle.dumps(('a',)))  # py2
                0: (    MARK
                1: S        STRING     'a'
                6: p        PUT        0
                9: t        TUPLE      (MARK at 0)
               10: p    PUT        1
               13: .    STOP
            highest protocol among opcodes = 0
            explain_pickle in_current_sage=True/False:
            ('a',)
            result: ('a',)

        We prefer to produce tuple literals, as above; but if the
        tuple is recursive, we need a more complicated
        construction. It used to be the case that the cPickle
        unpickler couldn't handle this case, but that's no longer true
        (see http://bugs.python.org/issue5794)::

            sage: v = ([],)
            sage: v[0].append(v)
            sage: check_pickle(pickle.dumps(v))  # py2
                0: (    MARK
                1: (        MARK
                2: l            LIST       (MARK at 1)
                3: p        PUT        0
                6: (        MARK
                7: g            GET        0
               10: t            TUPLE      (MARK at 6)
               11: p        PUT        1
               14: a        APPEND
               15: 0        POP
               16: 0        POP        (MARK at 0)
               17: g    GET        1
               20: .    STOP
            highest protocol among opcodes = 0
            explain_pickle in_current_sage=True/False:
            si1 = []
            si2 = (si1,)
            list.append(si1, si2)
            si2
            result: ([(...)],)
        """
    def TUPLE1(self) -> None:
        """
        TESTS::

            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(('a',))
                0: \\x80 PROTO      2
                2: X    BINUNICODE 'a'
                8: q    BINPUT     0
               10: \\x85 TUPLE1
               11: q    BINPUT     1
               13: .    STOP
            highest protocol among opcodes = 2
            explain_pickle in_current_sage=True/False:
            ('a',)
            result: ('a',)
        """
    def TUPLE2(self) -> None:
        """
        TESTS::

            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(('a','b'))
                0: \\x80 PROTO      2
                2: X    BINUNICODE 'a'
                8: q    BINPUT     0
               10: X    BINUNICODE 'b'
               16: q    BINPUT     1
               18: \\x86 TUPLE2
               19: q    BINPUT     2
               21: .    STOP
            highest protocol among opcodes = 2
            explain_pickle in_current_sage=True/False:
            ('a', 'b')
            result: ('a', 'b')
        """
    def TUPLE3(self) -> None:
        """
        TESTS::

            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(('a','b','c'))
                0: \\x80 PROTO      2
                2: X    BINUNICODE 'a'
                8: q    BINPUT     0
               10: X    BINUNICODE 'b'
               16: q    BINPUT     1
               18: X    BINUNICODE 'c'
               24: q    BINPUT     2
               26: \\x87 TUPLE3
               27: q    BINPUT     3
               29: .    STOP
            highest protocol among opcodes = 2
            explain_pickle in_current_sage=True/False:
            ('a', 'b', 'c')
            result: ('a', 'b', 'c')
        """
    def UNICODE(self, s) -> None:
        """
        TESTS::

            sage: import pickle
            sage: from sage.misc.explain_pickle import *
            sage: check_pickle(pickle.dumps(u'hi\\u1234\\U00012345'))  # py2
                0: V    UNICODE    u'hi\\u1234\\U00012345'
               20: p    PUT        0
               23: .    STOP
            highest protocol among opcodes = 0
            explain_pickle in_current_sage=True/False:
            u'hi\\u1234\\U00012345'
            result: u'hi\\u1234\\U00012345'
        """

def unpickle_newobj(klass, args):
    """
    Create a new object; this corresponds to the C code
    ``klass->tp_new(klass, args, NULL)``.  Used by :func:`explain_pickle`.

    EXAMPLES::

        sage: unpickle_newobj(tuple, ([1, 2, 3],))
        (1, 2, 3)

    TESTS:

    We can create a :class:`Sequence_generic` which would not work with
    a pure Python implementation. We just test that this does not raise
    an exception, we cannot do anything with ``s`` since ``s.__init__``
    was never called::

        sage: from sage.structure.sequence import Sequence_generic
        sage: s = unpickle_newobj(Sequence_generic, ([1, 2, 3],))
    """
def unpickle_build(obj, state) -> None:
    """
    Set the state of an object.  Used by :func:`explain_pickle`.

    EXAMPLES::

        sage: from sage.misc.explain_pickle import *
        sage: v = EmptyNewstyleClass()
        sage: unpickle_build(v, {'hello': 42})
        sage: v.hello
        42
    """
def unpickle_instantiate(fn, args):
    """
    Instantiate a new object of class ``fn`` with arguments ``args``.  Almost always
    equivalent to ``fn(*args)``.  Used by :func:`explain_pickle`.

    EXAMPLES::

        sage: unpickle_instantiate(Integer, ('42',))
        42
    """

unpickle_persistent_loader: Incomplete

def unpickle_persistent(s):
    """
    Take an integer index and return the persistent object with that
    index; works by calling whatever callable is stored in
    ``unpickle_persistent_loader``.  Used by :func:`explain_pickle`.

    EXAMPLES::

        sage: import sage.misc.explain_pickle
        sage: sage.misc.explain_pickle.unpickle_persistent_loader = lambda n: n+7
        sage: unpickle_persistent(35)
        42
    """
def unpickle_extension(code):
    """
    Take an integer index and return the extension object with that
    index.  Used by :func:`explain_pickle`.

    EXAMPLES::

        sage: from copyreg import *
        sage: add_extension('sage.misc.explain_pickle', 'EmptyNewstyleClass', 42)
        sage: unpickle_extension(42)
        <class 'sage.misc.explain_pickle.EmptyNewstyleClass'>
        sage: remove_extension('sage.misc.explain_pickle', 'EmptyNewstyleClass', 42)
    """
def unpickle_appends(lst, vals) -> None:
    """
    Given a list (or list-like object) and a sequence of values, appends the
    values to the end of the list.  This is careful to do so using the
    exact same technique that cPickle would use.  Used by :func:`explain_pickle`.

    EXAMPLES::

        sage: v = []
        sage: unpickle_appends(v, (1, 2, 3))
        sage: v
        [1, 2, 3]
    """
def check_pickle(p, verbose_eval: bool = False, pedantic: bool = False, args=()):
    """
    Test :func:`explain_pickle` on a given pickle ``p``.

    ``p`` can be:

    - a string containing an uncompressed pickle (which will always end
      with a '.')

    - a string containing a pickle fragment (not ending with '.')
      check_pickle will synthesize a pickle that will push args onto
      the stack (using persistent IDs), run the pickle fragment, and then
      STOP (if the string 'mark' occurs in args, then a mark will be pushed)

    - an arbitrary object; :func:`check_pickle` will pickle the object

    Once it has a pickle, :func:`check_pickle` will print the pickle's
    disassembly, run :func:`explain_pickle` with ``in_current_sage=True`` and
    ``False``, print the results, evaluate the results, unpickle the
    object with cPickle, and compare all three results.

    If ``verbose_eval`` is ``True``, then :func:`check_pickle` will print messages
    before evaluating the pickles; this is to allow for tests where
    the unpickling prints messages (to verify that the same operations
    occur in all cases).

    EXAMPLES::

        sage: from sage.misc.explain_pickle import *
        sage: check_pickle(['a'])
            0: \\x80 PROTO      2
            2: ]    EMPTY_LIST
            3: q    BINPUT     0
            5: X    BINUNICODE 'a'
           11: q    BINPUT     1
           13: a    APPEND
           14: .    STOP
        highest protocol among opcodes = 2
        explain_pickle in_current_sage=True/False:
        ['a']
        result: ['a']
    """

class EmptyOldstyleClass:
    """
    A featureless old-style class (does not inherit from object); used for
    testing :func:`explain_pickle`.
    """
    def __hash__(self):
        """
        Produce a predictable hash value for EmptyOldstyleClass.

        EXAMPLES::

            sage: from sage.misc.explain_pickle import *
            sage: v = EmptyOldstyleClass()
            sage: hash(v)
            0
            sage: v.__hash__()
            0
        """

class EmptyNewstyleClass:
    """
    A featureless new-style class (inherits from object); used for
    testing :func:`explain_pickle`.
    """

class TestReduceGetinitargs:
    """
    An old-style class with a :func:`__getinitargs__` method.  Used for testing
    :func:`explain_pickle`.
    """
    def __init__(self) -> None:
        """
        Initialize a TestReduceGetinitargs object.  Note that the
        constructor prints out a message.

        EXAMPLES::

            sage: from sage.misc.explain_pickle import *
            sage: TestReduceGetinitargs()
            Running __init__ for TestReduceGetinitargs
            TestReduceGetinitargs
        """
    def __getinitargs__(self):
        """
        A simple __getinitargs__ method, used for testing explain_pickle.

        EXAMPLES::

            sage: from sage.misc.explain_pickle import *
            sage: v = TestReduceGetinitargs()
            Running __init__ for TestReduceGetinitargs
            sage: v.__getinitargs__()
            ()
        """

class TestReduceNoGetinitargs:
    """
    An old-style class with no :meth:`__getinitargs__` method.  Used for testing
    :func:`explain_pickle`.
    """
    def __init__(self) -> None:
        """
        Initialize a TestReduceNoGetinitargs object.  Note that the
        constructor prints out a message.

        EXAMPLES::

            sage: from sage.misc.explain_pickle import *
            sage: TestReduceNoGetinitargs()
            Running __init__ for TestReduceNoGetinitargs
            TestReduceNoGetinitargs
        """

class TestAppendList(list):
    """
    A subclass of :class:`list`, with deliberately-broken append and extend methods.
    Used for testing :func:`explain_pickle`.
    """
    def append(self) -> None:
        """
        A deliberately broken append method.

        EXAMPLES::

            sage: from sage.misc.explain_pickle import *
            sage: v = TestAppendList()
            sage: v.append(7)
            Traceback (most recent call last):
            ...
            TypeError: ...append() takes 1 positional argument but 2 were given

        We can still append by directly using the list method::

            sage: list.append(v, 7)
            sage: v
            [7]
        """
    def extend(self) -> None:
        """
        A deliberately broken extend method.

        EXAMPLES::

            sage: from sage.misc.explain_pickle import *
            sage: v = TestAppendList()
            sage: v.extend([3,1,4,1,5,9])
            Traceback (most recent call last):
            ...
            TypeError: ...extend() takes 1 positional argument but 2 were given

        We can still extend by directly using the list method::

            sage: list.extend(v, (3,1,4,1,5,9))
            sage: v
            [3, 1, 4, 1, 5, 9]
        """

class TestAppendNonlist:
    """
    A list-like class, carefully designed to test exact unpickling
    behavior.  Used for testing :func:`explain_pickle`.
    """
    list: Incomplete
    def __init__(self) -> None:
        """
        Construct a TestAppendNonlist.

        EXAMPLES::

            sage: from sage.misc.explain_pickle import *
            sage: v = TestAppendNonlist()
            sage: v
            []
        """
    def __getattr__(self, a):
        """
        Get an 'append' method from a TestAppendNonlist.  We have this
        method so that we can distinguish how many times the append method
        is fetched.

        EXAMPLES::

            sage: from sage.misc.explain_pickle import *
            sage: v = TestAppendNonlist()
            sage: v.append(1)
            Fetching append attribute
            sage: v.append(2)
            Fetching append attribute
            sage: app = v.append
            Fetching append attribute
            sage: app(3)
            sage: app(4)
            sage: v
            [1, 2, 3, 4]
        """
    def __reduce__(self):
        """
        Implement __reduce__ for TestAppendNonlist.  Note that the
        loads(dumps(...)) test only fetches the append method once.

        EXAMPLES::

            sage: from sage.misc.explain_pickle import *
            sage: v = TestAppendNonlist()
            sage: v.list = [1,2,3,4]
            sage: v.__reduce__()
            (<class 'sage.misc.explain_pickle.TestAppendNonlist'>, (), None, <...iterator object at 0x...>)
            sage: list(v.__reduce__()[3])
            [1, 2, 3, 4]
            sage: loads(dumps(v))
            Fetching append attribute
            [1, 2, 3, 4]
        """

class TestBuild:
    """
    A simple class with a :meth:`__getstate__` but no :meth:`__setstate__`.  Used for testing
    :func:`explain_pickle`.
    """
class TestBuildSetstate(TestBuild):
    """
    A simple class with a :meth:`__getstate__` and a :meth:`__setstate__`.  Used for testing
    :func:`explain_pickle`.
    """
class TestGlobalOldName:
    """
    A featureless new-style class.  When you try to unpickle an instance
    of this class, it is redirected to create a :class:`TestGlobalNewName` instead.
    Used for testing :func:`explain_pickle`.

    EXAMPLES::

        sage: from sage.misc.explain_pickle import *
        sage: loads(dumps(TestGlobalOldName()))
        TestGlobalNewName
    """
class TestGlobalNewName:
    """
    A featureless new-style class.  When you try to unpickle an instance
    of :class:`TestGlobalOldName`, it is redirected to create an instance of this
    class instead.  Used for testing :func:`explain_pickle`.

    EXAMPLES::

        sage: from sage.misc.explain_pickle import *
        sage: loads(dumps(TestGlobalOldName()))
        TestGlobalNewName
    """
class TestGlobalFunnyName:
    """
    A featureless new-style class which has a name that's not a legal
    Python identifier.

    EXAMPLES::

        sage: from sage.misc.explain_pickle import *
        sage: globals()['funny$name'] = TestGlobalFunnyName # see comment at end of file
        sage: TestGlobalFunnyName.__name__
        'funny$name'
        sage: globals()['funny$name'] is TestGlobalFunnyName
        True
    """
