import unittest

class TestSuite:
    """
    Test suites for Sage objects.

    EXAMPLES::

        sage: TestSuite(ZZ).run()

    No output means that all tests passed. Which tests?
    In practice this calls all the methods ``._test_*`` of this
    object, in alphabetic order::

        sage: TestSuite(1).run(verbose = True)
        running ._test_category() . . . pass
        running ._test_eq() . . . pass
        running ._test_new() . . . pass
        running ._test_nonzero_equal() . . . pass
        running ._test_not_implemented_methods() . . . pass
        running ._test_pickling() . . . pass

    Those methods are typically implemented by abstract
    super classes, in particular via categories, in order to
    enforce standard behavior and API, or provide mathematical
    sanity checks. For example if ``self`` is in the category of
    finite semigroups, this checks that the multiplication is
    associative (at least on some elements)::

        sage: S = FiniteSemigroups().example(alphabet = ('a', 'b'))
        sage: TestSuite(S).run(verbose = True)
        running ._test_an_element() . . . pass
        running ._test_associativity() . . . pass
        running ._test_cardinality() . . . pass
        running ._test_category() . . . pass
        running ._test_construction() . . . pass
        running ._test_elements() . . .
          Running the test suite of self.an_element()
          running ._test_category() . . . pass
          running ._test_eq() . . . pass
          running ._test_new() . . . pass
          running ._test_not_implemented_methods() . . . pass
          running ._test_pickling() . . . pass
          pass
        running ._test_elements_eq_reflexive() . . . pass
        running ._test_elements_eq_symmetric() . . . pass
        running ._test_elements_eq_transitive() . . . pass
        running ._test_elements_neq() . . . pass
        running ._test_enumerated_set_contains() . . . pass
        running ._test_enumerated_set_iter_cardinality() . . . pass
        running ._test_enumerated_set_iter_list() . . . pass
        running ._test_eq() . . . pass
        running ._test_new() . . . pass
        running ._test_not_implemented_methods() . . . pass
        running ._test_pickling() . . . pass
        running ._test_some_elements() . . . pass

    The different test methods can be called independently::

        sage: S._test_associativity()

    Debugging tip: in case of failure of some test, use ``%pdb on`` to
    turn on automatic debugging on error. Run the failing test
    independently: the debugger will stop right where the first
    assertion fails. Then, introspection can be used to analyse what
    exactly the problem is. See also the ``catch = False`` option to
    :meth:`.run`.

    When meaningful, one can further customize on which elements
    the tests are run. Here, we use it to *prove* that the
    multiplication is indeed associative, by running the test on
    all the elements::

        sage: S._test_associativity(elements = S)

    Adding a new test boils down to adding a new method in the class
    of the object or any super class (e.g. in a category). This method
    should use the utility :meth:`._tester` to handle standard options
    and report test failures. See the code of
    :meth:`._test_an_element` for an example. Note: Python's testunit
    convention is to look for methods called ``.test*``; we use instead
    ``._test_*`` so as not to pollute the object's interface.

    Eventually, every implementation of a :class:`SageObject` should
    run a :class:`TestSuite` on one of its instances in its doctest
    (replacing the current ``loads(dumps(x))`` tests).

    Finally, running ``TestSuite`` on a standard Python object does
    some basic sanity checks::

        sage: TestSuite(int(1)).run(verbose = True)
        running ._test_new() . . . pass
        running ._test_pickling() . . . pass

    .. TODO::

        - Allow for customized behavior in case of failing assertion
          (warning, error, statistic accounting).
          This involves reimplementing the methods fail / failIf / ...
          of unittest.TestCase in InstanceTester

        - Don't catch the exceptions if ``TestSuite(..).run()`` is called
          under the debugger, or with ``%pdb`` on (how to detect this? see
          ``get_ipython()``, ``IPython.Magic.shell.call_pdb``, ...)
          In the mean time, see the ``catch=False`` option.

        - Run the tests according to the inheritance order, from most
          generic to most specific, rather than alphabetically. Then, the
          first failure will be the most relevant, the others being
          usually consequences.

        - Improve integration with doctests (statistics on failing/passing tests)

        - Add proper support for nested testsuites.

        - Integration with unittest:
          Make TestSuite inherit from unittest.TestSuite?
          Make ``.run(...)`` accept a result object

        - Add some standard option ``proof = True``, asking for the
          test method to choose appropriately the elements so as to
          prove the desired property. The test method may assume that
          a parent implements properly all the super categories. For
          example, the ``_test_commutative`` method of the category
          ``CommutativeSemigroups()`` may just check that the
          provided generators commute, implicitly assuming that
          generators indeed generate the semigroup (as required by
          ``Semigroups()``).
    """
    def __init__(self, instance) -> None:
        """
        TESTS::

            sage: TestSuite(ZZ)
            Test suite for Integer Ring
        """
    def run(self, category=None, skip=[], catch: bool = True, raise_on_failure: bool = False, **options) -> None:
        '''
        Run all the tests from this test suite:

        INPUT:

        - ``category`` -- a category; reserved for future use
        - ``skip`` -- string or list (or iterable) of strings
        - ``raise_on_failure`` -- boolean (default: ``False``)
        - ``catch`` -- boolean (default: ``True``)

        All other options are passed down to the individual tests.

        EXAMPLES::

            sage: TestSuite(ZZ).run()

        We now use the ``verbose`` option::

            sage: TestSuite(1).run(verbose = True)
            running ._test_category() . . . pass
            running ._test_eq() . . . pass
            running ._test_new() . . . pass
            running ._test_nonzero_equal() . . . pass
            running ._test_not_implemented_methods() . . . pass
            running ._test_pickling() . . . pass

        Some tests may be skipped using the ``skip`` option::

            sage: TestSuite(1).run(verbose = True, skip =\'_test_pickling\')
            running ._test_category() . . . pass
            running ._test_eq() . . . pass
            running ._test_new() . . . pass
            running ._test_nonzero_equal() . . . pass
            running ._test_not_implemented_methods() . . . pass
            sage: TestSuite(1).run(verbose = True, skip =["_test_pickling", "_test_category"])
            running ._test_eq() . . . pass
            running ._test_new() . . . pass
            running ._test_nonzero_equal() . . . pass
            running ._test_not_implemented_methods() . . . pass

        We now show (and test) some standard error reports::

            sage: class Blah(SageObject):
            ....:     def _test_a(self, tester): pass
            ....:     def _test_b(self, tester): tester.fail()
            ....:     def _test_c(self, tester): pass
            ....:     def _test_d(self, tester): tester.fail()

            sage: TestSuite(Blah()).run()
            Failure in _test_b:
            Traceback (most recent call last):
              ...
            AssertionError: None
            ------------------------------------------------------------
            Failure in _test_d:
            Traceback (most recent call last):
              ...
            AssertionError: None
            ------------------------------------------------------------
            Failure in _test_pickling:
            Traceback (most recent call last):
              ...
            ...PicklingError: Can\'t pickle <class \'__main__.Blah\'>: attribute
            lookup ...Blah... failed
            ------------------------------------------------------------
            The following tests failed: _test_b, _test_d, _test_pickling

            sage: TestSuite(Blah()).run(verbose = True)
            running ._test_a() . . . pass
            running ._test_b() . . . fail
            Traceback (most recent call last):
              ...
            AssertionError: None
            ------------------------------------------------------------
            running ._test_c() . . . pass
            running ._test_category() . . . pass
            running ._test_d() . . . fail
            Traceback (most recent call last):
              ...
            AssertionError: None
            ------------------------------------------------------------
            running ._test_new() . . . pass
            running ._test_not_implemented_methods() . . . pass
            running ._test_pickling() . . . fail
            Traceback (most recent call last):
              ...
            ...PicklingError: Can\'t pickle <class \'__main__.Blah\'>: attribute
            lookup ...Blah... failed
            ------------------------------------------------------------
            The following tests failed: _test_b, _test_d, _test_pickling

            File "/opt/sage/local/lib/python/site-packages/sage/misc/sage_unittest.py", line 183, in run
            test_method(tester = tester)

        The ``catch=False`` option prevents ``TestSuite`` from
        catching exceptions::

            sage: TestSuite(Blah()).run(catch=False)
            Traceback (most recent call last):
              ...
              File ..., in _test_b
                def _test_b(self, tester): tester.fail()
              ...
            AssertionError: None

        In conjunction with ``%pdb on``, this allows for the debugger
        to jump directly to the first failure location.
        '''

class TestSuiteFailure(AssertionError): ...

def instance_tester(instance, tester=None, **options):
    '''
    Return a gadget attached to ``instance`` providing testing utilities.

    EXAMPLES::

        sage: from sage.misc.sage_unittest import instance_tester
        sage: tester = instance_tester(ZZ)

        sage: tester.assertTrue(1 == 1)
        sage: tester.assertTrue(1 == 0)
        Traceback (most recent call last):
        ...
        AssertionError: False is not true
        sage: tester.assertTrue(1 == 0, "this is expected to fail")
        Traceback (most recent call last):
        ...
        AssertionError: this is expected to fail

        sage: tester.assertEqual(1, 1)
        sage: tester.assertEqual(1, 0)
        Traceback (most recent call last):
        ...
        AssertionError: 1 != 0

    The available assertion testing facilities are the same as in
    :class:`unittest.TestCase` [UNITTEST]_, which see (actually, by a slight
    abuse, tester is currently an instance of this class).

    TESTS::

        sage: instance_tester(ZZ, tester = tester) is tester
        True
    '''

class InstanceTester(unittest.TestCase):
    """
    A gadget attached to an instance providing it with testing utilities.

    EXAMPLES::

        sage: from sage.misc.sage_unittest import InstanceTester
        sage: InstanceTester(instance = ZZ, verbose = True, elements = [1,2,3])
        Testing utilities for Integer Ring

    This is used by ``SageObject._tester``, which see::

        sage: QQ._tester()
        Testing utilities for Rational Field
    """
    longMessage: bool
    def __init__(self, instance, elements=None, verbose: bool = False, prefix: str = '', max_runs: int = 4096, max_samples=None, **options) -> None:
        """
        A gadget attached to an instance providing it with testing utilities.

        EXAMPLES::

            sage: from sage.misc.sage_unittest import InstanceTester
            sage: InstanceTester(instance = ZZ, verbose = True, elements = [1,2,3])
            Testing utilities for Integer Ring

        This is used by ``SageObject._tester``, for example::

            sage: QQ._tester()
            Testing utilities for Rational Field
        """
    def runTest(self) -> None:
        """
        Trivial implementation of :meth:`unittest.TestCase.runTest` to
        please the super class :class:`TestCase`. That's the price to
        pay for abusively inheriting from it.

        EXAMPLES::

            sage: from sage.misc.sage_unittest import InstanceTester
            sage: tester = InstanceTester(ZZ, verbose = True)
            sage: tester.runTest()
        """
    def info(self, message, newline: bool = True) -> None:
        '''
        Display user information.

        EXAMPLES::

            sage: from sage.misc.sage_unittest import InstanceTester
            sage: tester = InstanceTester(ZZ, verbose = True)

            sage: tester.info("hello"); tester.info("world")
            hello
            world

            sage: tester = InstanceTester(ZZ, verbose = False)
            sage: tester.info("hello"); tester.info("world")

            sage: tester = InstanceTester(ZZ, verbose = True)
            sage: tester.info("hello", newline = False); tester.info(" world")
            hello world
        '''
    def some_elements(self, S=None, repeat=None):
        """
        Return a list (or iterable) of elements of the instance on which
        the tests should be run.

        This is only meaningful for container objects like parents.

        INPUT:

        - ``S`` -- set of elements to select from; by default this
          will use the elements passed to this tester at creation
          time, or the result of :meth:`.some_elements` if no elements
          were specified

        - ``repeat`` -- integer (default: ``None``);  if given, instead returns
          a list of tuples of length ``repeat`` from ``S``

        OUTPUT:

        A list of at most ``self._max_runs`` elements of ``S^r``,
        or a sample of at most ``self._max_samples`` if that is not ``None``.

        EXAMPLES:

        By default, this calls :meth:`.some_elements` on the instance::

            sage: from sage.misc.sage_unittest import InstanceTester
            sage: class MyParent(Parent):
            ....:     def some_elements(self):
            ....:         return [1,2,3,4,5]
            ...
            sage: tester = InstanceTester(MyParent())
            sage: list(tester.some_elements())
            [1, 2, 3, 4, 5]

            sage: tester = InstanceTester(MyParent(), max_runs=3)
            sage: list(tester.some_elements())
            [1, 2, 3]

            sage: tester = InstanceTester(MyParent(), max_runs=7)
            sage: list(tester.some_elements())
            [1, 2, 3, 4, 5]

            sage: tester = InstanceTester(MyParent(), elements=[1,3,5])
            sage: list(tester.some_elements())
            [1, 3, 5]

            sage: tester = InstanceTester(MyParent(), elements=[1,3,5], max_runs=2)
            sage: list(tester.some_elements())
            [1, 3]

            sage: tester = InstanceTester(FiniteEnumeratedSet(['a','b','c','d']), max_runs=3)
            sage: tester.some_elements()
            ['a', 'b', 'c']

            sage: tester = InstanceTester(FiniteEnumeratedSet([]))
            sage: list(tester.some_elements())
            []

            sage: tester = InstanceTester(ZZ)
            sage: ZZ.some_elements()             # yikes, shamelessly trivial ...
            <generator object ..._some_elements_from_iterator at 0x...>
            sage: list(tester.some_elements())
            [0, 1, -1, 2, -2, ..., 49, -49, 50]

            sage: tester = InstanceTester(ZZ, elements = ZZ, max_runs=5)
            sage: list(tester.some_elements())
            [0, 1, -1, 2, -2]

            sage: tester = InstanceTester(ZZ, elements = srange(100), max_runs=5)
            sage: list(tester.some_elements())
            [0, 1, 2, 3, 4]

            sage: tester = InstanceTester(ZZ, elements = srange(3), max_runs=5)
            sage: list(tester.some_elements())
            [0, 1, 2]

        The ``repeat`` keyword can give pairs or triples from ``S``::

            sage: list(tester.some_elements(repeat=2))
            [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1)]

        You can use ``max_samples`` to sample at random, instead of in order::

            sage: tester = InstanceTester(ZZ, elements = srange(8), max_samples = 4)
            sage: all(t in srange(8) for t in tester.some_elements())
            True
            sage: all(s in srange(8) and t in srange(8) for s,t in tester.some_elements(repeat=2))
            True

        Test for :issue:`15919`, :issue:`16244`::

            sage: Z = IntegerModRing(25) # random.sample, which was used pre #16244, has a threshold at 21!
            sage: Z[1]                   # since #8389, indexed access is used for ring extensions
            Traceback (most recent call last):
            ...
            ValueError: variable name '1' does not start with a letter
            sage: tester = InstanceTester(Z, elements=Z, max_runs=5)
            sage: list(tester.some_elements())
            [0, 1, 2, 3, 4]

            sage: C = cartesian_product([Z]*4)
            sage: len(C)
            390625
            sage: tester = InstanceTester(C, elements = C, max_runs=4)
            sage: list(tester.some_elements())
            [(0, 0, 0, 0), (0, 0, 0, 1), (0, 0, 0, 2), (0, 0, 0, 3)]
        """

class PythonObjectWithTests:
    '''
    Utility class for running basis tests on a plain Python object
    (that is not in SageObject). More test methods can be added here.

    EXAMPLES::

        sage: TestSuite("bla").run()
    '''
    def __init__(self, instance) -> None:
        """
        EXAMPLES::

            sage: from sage.misc.sage_unittest import PythonObjectWithTests
            sage: x = PythonObjectWithTests(int(1)); x
            <sage.misc.sage_unittest.PythonObjectWithTests object at ...>
            sage: TestSuite(x).run()
        """
