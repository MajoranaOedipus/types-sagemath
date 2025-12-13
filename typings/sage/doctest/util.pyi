from _typeshed import Incomplete
from contextlib import contextmanager

def count_noun(number, noun, plural=None, pad_number: bool = False, pad_noun: bool = False):
    '''
    EXAMPLES::

        sage: from sage.doctest.util import count_noun
        sage: count_noun(1, "apple")
        \'1 apple\'
        sage: count_noun(1, "apple", pad_noun=True)
        \'1 apple \'
        sage: count_noun(1, "apple", pad_number=3)
        \'  1 apple\'
        sage: count_noun(2, "orange")
        \'2 oranges\'
        sage: count_noun(3, "peach", "peaches")
        \'3 peaches\'
        sage: count_noun(1, "peach", plural=\'peaches\', pad_noun=True)
        \'1 peach  \'
    '''
def dict_difference(self, other):
    """
    Return a dict with all key-value pairs occurring in ``self`` but not
    in ``other``.

    EXAMPLES::

        sage: from sage.doctest.util import dict_difference
        sage: d1 = {1: 'a', 2: 'b', 3: 'c'}
        sage: d2 = {1: 'a', 2: 'x', 4: 'c'}
        sage: dict_difference(d2, d1)
        {2: 'x', 4: 'c'}

    ::

        sage: from sage.doctest.control import DocTestDefaults
        sage: D1 = DocTestDefaults()
        sage: D2 = DocTestDefaults(foobar='hello', timeout=100)
        sage: dict_difference(D2.__dict__, D1.__dict__)
        {'foobar': 'hello', 'timeout': 100}
    """

class Timer:
    """
    A simple timer.

    EXAMPLES::

        sage: from sage.doctest.util import Timer
        sage: Timer()
        {}
        sage: TestSuite(Timer()).run()
    """
    cputime: Incomplete
    walltime: Incomplete
    def start(self):
        """
        Start the timer.

        Can be called multiple times to reset the timer.

        EXAMPLES::

            sage: from sage.doctest.util import Timer
            sage: Timer().start()
            {'cputime': ..., 'walltime': ...}
        """
    def stop(self):
        """
        Stops the timer, recording the time that has passed since it
        was started.

        EXAMPLES::

            sage: from sage.doctest.util import Timer
            sage: import time
            sage: timer = Timer().start()
            sage: time.sleep(float(0.5))
            sage: timer.stop()
            {'cputime': ..., 'walltime': ...}
        """
    def annotate(self, object) -> None:
        """
        Annotates the given object with the cputime and walltime
        stored in this timer.

        EXAMPLES::

            sage: from sage.doctest.util import Timer
            sage: Timer().start().annotate(EllipticCurve)
            sage: EllipticCurve.cputime # random
            2.817255
            sage: EllipticCurve.walltime # random
            1332649288.410404
        """
    def __eq__(self, other):
        """
        Comparison.

        EXAMPLES::

            sage: from sage.doctest.util import Timer
            sage: Timer() == Timer()
            True
            sage: t = Timer().start()
            sage: loads(dumps(t)) == t
            True
        """
    def __ne__(self, other):
        """
        Test for non-equality.

        EXAMPLES::

            sage: from sage.doctest.util import Timer
            sage: Timer() == Timer()
            True
            sage: t = Timer().start()
            sage: loads(dumps(t)) != t
            False
        """

class RecordingDict(dict):
    """
    This dictionary is used for tracking the dependencies of an example.

    This feature allows examples in different doctests to be grouped
    for better timing data.  It's obtained by recording whenever
    anything is set or retrieved from this dictionary.

    EXAMPLES::

        sage: from sage.doctest.util import RecordingDict
        sage: D = RecordingDict(test=17)
        sage: D.got
        set()
        sage: D['test']
        17
        sage: D.got
        {'test'}
        sage: D.set
        set()
        sage: D['a'] = 1
        sage: D['a']
        1
        sage: D.set
        {'a'}
        sage: D.got
        {'test'}

    TESTS::

        sage: TestSuite(D).run()
    """
    def __init__(self, *args, **kwds) -> None:
        """
        Initialization arguments are the same as for a normal dictionary.

        EXAMPLES::

            sage: from sage.doctest.util import RecordingDict
            sage: D = RecordingDict(d = 42)
            sage: D.got
            set()
        """
    set: Incomplete
    got: Incomplete
    def start(self) -> None:
        """
        We track which variables have been set or retrieved.
        This function initializes these lists to be empty.

        EXAMPLES::

            sage: from sage.doctest.util import RecordingDict
            sage: D = RecordingDict(d = 42)
            sage: D.set
            set()
            sage: D['a'] = 4
            sage: D.set
            {'a'}
            sage: D.start(); D.set
            set()
        """
    def __getitem__(self, name):
        """
        EXAMPLES::

            sage: from sage.doctest.util import RecordingDict
            sage: D = RecordingDict(d = 42)
            sage: D['a'] = 4
            sage: D.got
            set()
            sage: D['a'] # indirect doctest
            4
            sage: D.got
            set()
            sage: D['d']
            42
            sage: D.got
            {'d'}
        """
    def __setitem__(self, name, value) -> None:
        """
        EXAMPLES::

            sage: from sage.doctest.util import RecordingDict
            sage: D = RecordingDict(d = 42)
            sage: D['a'] = 4 # indirect doctest
            sage: D.set
            {'a'}
        """
    def __delitem__(self, name) -> None:
        """
        EXAMPLES::

            sage: from sage.doctest.util import RecordingDict
            sage: D = RecordingDict(d = 42)
            sage: del D['d'] # indirect doctest
            sage: D.set
            {'d'}
        """
    def get(self, name, default=None):
        """
        EXAMPLES::

            sage: from sage.doctest.util import RecordingDict
            sage: D = RecordingDict(d = 42)
            sage: D.get('d')
            42
            sage: D.got
            {'d'}
            sage: D.get('not_here')
            sage: sorted(list(D.got))
            ['d', 'not_here']
        """
    def copy(self):
        """
        Note that set and got are not copied.

        EXAMPLES::

            sage: from sage.doctest.util import RecordingDict
            sage: D = RecordingDict(d = 42)
            sage: D['a'] = 4
            sage: D.set
            {'a'}
            sage: E = D.copy()
            sage: E.set
            set()
            sage: sorted(E.keys())
            ['a', 'd']
        """
    def __reduce__(self):
        """
        Pickling.

        EXAMPLES::

            sage: from sage.doctest.util import RecordingDict
            sage: D = RecordingDict(d = 42)
            sage: D['a'] = 4
            sage: D.get('not_here')
            sage: E = loads(dumps(D))
            sage: E.got
            {'not_here'}
        """

def make_recording_dict(D, st, gt):
    """
    Auxiliary function for pickling.

    EXAMPLES::

        sage: from sage.doctest.util import make_recording_dict
        sage: D = make_recording_dict({'a':4,'d':42},set(),set(['not_here']))
        sage: sorted(D.items())
        [('a', 4), ('d', 42)]
        sage: D.got
        {'not_here'}
    """

class NestedName:
    """
    Class used to construct fully qualified names based on indentation level.

    EXAMPLES::

        sage: from sage.doctest.util import NestedName
        sage: qname = NestedName('sage.categories.algebras')
        sage: qname[0] = 'Algebras'; qname
        sage.categories.algebras.Algebras
        sage: qname[4] = '__contains__'; qname
        sage.categories.algebras.Algebras.__contains__
        sage: qname[4] = 'ParentMethods'
        sage: qname[8] = 'from_base_ring'; qname
        sage.categories.algebras.Algebras.ParentMethods.from_base_ring

    TESTS::

        sage: TestSuite(qname).run()
    """
    all: Incomplete
    def __init__(self, base) -> None:
        """
        INPUT:

        - ``base`` -- string; the name of the module

        EXAMPLES::

            sage: from sage.doctest.util import NestedName
            sage: qname = NestedName('sage.categories.algebras')
            sage: qname
            sage.categories.algebras
        """
    def __setitem__(self, index, value) -> None:
        """
        Set the value at a given indentation level.

        INPUT:

        - ``index`` -- positive integer; the indentation level (often a
          multiple of 4, but not necessarily)
        - ``value`` -- string; the name of the class or function at that
          indentation level

        EXAMPLES::

            sage: from sage.doctest.util import NestedName
            sage: qname = NestedName('sage.categories.algebras')
            sage: qname[1] = 'Algebras' # indirect doctest
            sage: qname
            sage.categories.algebras.Algebras
            sage: qname.all
            ['sage.categories.algebras', None, 'Algebras']
        """
    def __eq__(self, other):
        """
        Comparison is just comparison of the underlying lists.

        EXAMPLES::

            sage: from sage.doctest.util import NestedName
            sage: qname = NestedName('sage.categories.algebras')
            sage: qname2 = NestedName('sage.categories.algebras')
            sage: qname == qname2
            True
            sage: qname[0] = 'Algebras'
            sage: qname2[2] = 'Algebras'
            sage: repr(qname) == repr(qname2)
            True
            sage: qname == qname2
            False
        """
    def __ne__(self, other):
        """
        Test for non-equality.

        EXAMPLES::

            sage: from sage.doctest.util import NestedName
            sage: qname = NestedName('sage.categories.algebras')
            sage: qname2 = NestedName('sage.categories.algebras')
            sage: qname != qname2
            False
            sage: qname[0] = 'Algebras'
            sage: qname2[2] = 'Algebras'
            sage: repr(qname) == repr(qname2)
            True
            sage: qname != qname2
            True
        """

@contextmanager
def ensure_interruptible_after(seconds: float, max_wait_after_interrupt: float = 0.2, inaccuracy_tolerance: float = 0.1):
    """
    Helper function for doctesting to ensure that the code is interruptible after a certain amount of time.
    This should only be used for internal doctesting purposes.

    EXAMPLES::

        sage: from sage.doctest.util import ensure_interruptible_after
        sage: with ensure_interruptible_after(1) as data: sleep(3)

    ``as data`` is optional, but if it is used, it will contain a few useful values::

        sage: data  # abs tol 1
        {'alarm_raised': True, 'elapsed': 1.0}

    ``max_wait_after_interrupt`` can be passed if the function may take longer than usual to be interrupted::

        sage: # needs sage.misc.cython
        sage: cython(r'''
        ....: from posix.time cimport clock_gettime, CLOCK_REALTIME, timespec, time_t
        ....: from cysignals.signals cimport sig_check
        ....:
        ....: cpdef void uninterruptible_sleep(double seconds):
        ....:     cdef timespec start_time, target_time
        ....:     clock_gettime(CLOCK_REALTIME, &start_time)
        ....:
        ....:     cdef time_t floor_seconds = <time_t>seconds
        ....:     target_time.tv_sec = start_time.tv_sec + floor_seconds
        ....:     target_time.tv_nsec = start_time.tv_nsec + <long>((seconds - floor_seconds) * 1e9)
        ....:     if target_time.tv_nsec >= 1000000000:
        ....:         target_time.tv_nsec -= 1000000000
        ....:         target_time.tv_sec += 1
        ....:
        ....:     while True:
        ....:         clock_gettime(CLOCK_REALTIME, &start_time)
        ....:         if start_time.tv_sec > target_time.tv_sec or (start_time.tv_sec == target_time.tv_sec and start_time.tv_nsec >= target_time.tv_nsec):
        ....:             break
        ....:
        ....: cpdef void check_interrupt_only_occasionally():
        ....:     for i in range(10):
        ....:         uninterruptible_sleep(0.8)
        ....:         sig_check()
        ....: ''')
        sage: with ensure_interruptible_after(1):  # not passing max_wait_after_interrupt will raise an error
        ....:     check_interrupt_only_occasionally()
        Traceback (most recent call last):
        ...
        RuntimeError: Function is not interruptible within 1.0000 seconds, only after 1.6... seconds
        sage: with ensure_interruptible_after(1, max_wait_after_interrupt=0.9):
        ....:     check_interrupt_only_occasionally()

    TESTS::

        sage: with ensure_interruptible_after(2) as data: sleep(1)
        Traceback (most recent call last):
        ...
        RuntimeError: Function terminates early after 1... < 2.0000 seconds
        sage: data  # abs tol 1
        {'alarm_raised': False, 'elapsed': 1.0}

    The test above requires a large tolerance, because both ``time.sleep`` and
    ``from posix.unistd cimport usleep`` may have slowdown on the order of 0.1s on Mac,
    likely because the system is idle and GitHub CI switches the program out,
    and context switch back takes time. Besides, there is an issue with ``Integer``
    destructor, see `<https://github.com/sagemath/cysignals/issues/215>`_
    So we use busy wait and Python integers::

        sage: # needs sage.misc.cython
        sage: cython(r'''
        ....: from posix.time cimport clock_gettime, CLOCK_REALTIME, timespec, time_t
        ....: from cysignals.signals cimport sig_check
        ....:
        ....: cpdef void interruptible_sleep(double seconds):
        ....:     cdef timespec start_time, target_time
        ....:     clock_gettime(CLOCK_REALTIME, &start_time)
        ....:
        ....:     cdef time_t floor_seconds = <time_t>seconds
        ....:     target_time.tv_sec = start_time.tv_sec + floor_seconds
        ....:     target_time.tv_nsec = start_time.tv_nsec + <long>((seconds - floor_seconds) * 1e9)
        ....:     if target_time.tv_nsec >= 1000000000:
        ....:         target_time.tv_nsec -= 1000000000
        ....:         target_time.tv_sec += 1
        ....:
        ....:     while True:
        ....:         sig_check()
        ....:         clock_gettime(CLOCK_REALTIME, &start_time)
        ....:         if start_time.tv_sec > target_time.tv_sec or (start_time.tv_sec == target_time.tv_sec and start_time.tv_nsec >= target_time.tv_nsec):
        ....:             break
        ....: ''')
        sage: with ensure_interruptible_after(2) as data: interruptible_sleep(1r)
        Traceback (most recent call last):
        ...
        RuntimeError: Function terminates early after 1.00... < 2.0000 seconds
        sage: with ensure_interruptible_after(1) as data: uninterruptible_sleep(2r)
        Traceback (most recent call last):
        ...
        RuntimeError: Function is not interruptible within 1.0000 seconds, only after 2.00... seconds
        sage: data  # abs tol 0.01
        {'alarm_raised': True, 'elapsed': 2.0}
        sage: with ensure_interruptible_after(1): uninterruptible_sleep(2r); raise RuntimeError
        Traceback (most recent call last):
        ...
        RuntimeError: Function is not interruptible within 1.0000 seconds, only after 2.00... seconds
        sage: data  # abs tol 0.01
        {'alarm_raised': True, 'elapsed': 2.0}

    ::

        sage: with ensure_interruptible_after(1) as data: raise ValueError
        Traceback (most recent call last):
        ...
        ValueError
        sage: data  # abs tol 0.01
        {'alarm_raised': False, 'elapsed': 0.0}
    """
