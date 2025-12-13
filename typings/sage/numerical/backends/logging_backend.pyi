from _typeshed import Incomplete
from sage.numerical.backends.generic_backend import GenericBackend as GenericBackend
from sage.rings.rational_field import QQ as QQ

class LoggingBackend(GenericBackend):
    '''
    See :class:`LoggingBackendFactory` for documentation.

    EXAMPLES::

        sage: import sage.numerical.backends.logging_backend
        sage: from sage.numerical.backends.logging_backend import LoggingBackend
        sage: from sage.numerical.backends.generic_backend import get_solver
        sage: b = get_solver(solver = "GLPK")
        sage: lb = LoggingBackend(backend=b)
        sage: lb.add_variable(obj=42, name=\'Helloooooo\')
        # p.add_variable(obj=42, name=\'Helloooooo\')
        # result: 0
        0
        sage: lb.add_variable(obj=1789)
        # p.add_variable(obj=1789)
        # result: 1
        1

    .. :no-undoc-members:
    '''
    def __init__(self, backend, printing: bool = True, doctest=None, test_method=None, base_ring=None) -> None:
        '''
        See :class:`LoggingBackendFactory` for documentation.

        EXAMPLES::

            sage: import sage.numerical.backends.logging_backend
            sage: from sage.numerical.backends.logging_backend import LoggingBackend
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: b = get_solver(solver = "GLPK")
            sage: lb = LoggingBackend(backend=b)
        '''
    def __getattr__(self, attr):
        '''
        Look up an attribute in the instance.

        It is provided to dynamically create delegating methods for all methods of
        the backend that are not part of the :class:`GenericBackend` interface,
        from which :class:`LoggingBackend` inherits.

        EXAMPLES::

            sage: import sage.numerical.backends.logging_backend
            sage: from sage.numerical.backends.logging_backend import LoggingBackend
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: b = get_solver(solver = "GLPK")
            sage: lb = LoggingBackend(backend=b)
            sage: lb.print_ranges
            <bound method ...>
        '''
    def base_ring(self):
        '''
        Return the base ring.

        The backend\'s base ring can be overridden.  It is best to run
        the tests with GLPK and override the base ring to ``QQ``.  Then
        default input to backend methods, prepared by
        :class:`MixedIntegerLinearProgram`, depends on the base ring.
        This way input will be rational and so suitable for both exact
        and inexact methods; whereas output will be float and will thus
        trigger :func:`assertAlmostEqual` tests.

        EXAMPLES::

            sage: import sage.numerical.backends.logging_backend
            sage: from sage.numerical.backends.logging_backend import LoggingBackend
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: b = get_solver(solver = "GLPK")
            sage: lb = LoggingBackend(backend=b)
            sage: lb.base_ring()
            Real Double Field
            sage: from sage.rings.rational_field import QQ
            sage: lb = LoggingBackend(backend=b, base_ring=QQ)
            sage: lb.base_ring()
            Rational Field
        '''

test_method_template: Incomplete

def LoggingBackendFactory(solver=None, printing: bool = True, doctest_file=None, test_method_file=None, test_method=None, base_ring=...):
    """
    Factory that constructs a :class:`LoggingBackend` for debugging and testing.

    An instance of it can be passed as the solver argument of
    :func:`sage.numerical.backends.generic_backend.get_solver` and
    :class:`MixedIntegerLinearProgram`.

    EXAMPLES:

    Assume that we have the following function that does some
    computation using :class:`MixedIntegerLinearProgram` (or MIP
    backend methods), and suppose we have observed that it works with
    the GLPK backend, but not with the COIN backend::

        sage: def compute_something(solver='GLPK'):
        ....:     from sage.numerical.mip import MIPSolverException
        ....:     mip = MixedIntegerLinearProgram(solver=solver)
        ....:     lb = mip.get_backend()
        ....:     lb.add_variable(obj=42, name='Helloooooo')
        ....:     lb.add_variable(obj=1789)
        ....:     try:
        ....:         lb.solve()
        ....:     except MIPSolverException:
        ....:         return 4711
        ....:     else:
        ....:         return 91

    We can investigate what the backend methods are doing by running a
    :class:`LoggingBackend` in its in-terminal logging mode::

        sage: import sage.numerical.backends.logging_backend
        sage: from sage.numerical.backends.logging_backend import LoggingBackendFactory
        sage: compute_something(solver = LoggingBackendFactory(solver='GLPK'))
        # p = get_solver(solver='GLPK')
        # p.add_variable(obj=42, name='Helloooooo')
        # result: 0
        # p.add_variable(obj=1789)
        # result: 1
        # p.solve()
        # exception: GLPK: The LP (relaxation) problem has no dual feasible solution
        4711

    By replacing 'GLPK' by 'COIN' above, we can then compare the two
    logs and see where they differ.

    Imagine that we have now fixed the bug in the COIN backend, and we
    want to add a doctest that documents this fact.  We do not want to
    call ``compute_something`` in the doctest, but rather just have a
    sequence of calls to backend methods.

    We can have the doctest autogenerated by running a
    :class:`LoggingBackend` in its doctest-writing mode::

        sage: fname = tmp_filename()
        sage: compute_something(solver = LoggingBackendFactory(solver='GLPK', printing=False,
        ....:                                                  doctest_file=fname))
        4711
        sage: with open(fname) as f:
        ....:     for line in f.readlines(): _ = sys.stdout.write('|{}'.format(line))
        |        sage: p = get_solver(solver='GLPK')
        |        sage: p.add_variable(obj=42, name='Helloooooo')
        |        0
        |        sage: p.add_variable(obj=1789)
        |        1
        |        sage: p.solve()
        |        Traceback (most recent call last):
        |        ...
        |        MIPSolverException: GLPK: The LP (relaxation) problem has no dual feasible solution

    We then copy from the generated file and paste into the source
    code of the COIN backend.

    If this test seems valuable enough that all backends should be
    tested against it, we should create a test method instead of a
    docstring.

    We can have the test method autogenerated by running a
    :class:`LoggingBackend` in its test-method-writing mode::

        sage: fname = tmp_filename()
        sage: compute_something(solver= LoggingBackendFactory(solver='GLPK', printing=False,
        ....:                                                 test_method_file=fname,
        ....:                                                 test_method='something'))
        4711
        sage: with open(fname) as f:
        ....:     for line in f.readlines(): _ = sys.stdout.write('|{}'.format(line))
        |
        |    @classmethod
        |    def _test_something(cls, tester=None, **options):
        |        ...
        |        Run tests on ...
        |
        |        TESTS::
        |
        |            sage: from sage.numerical.backends.generic_backend import GenericBackend
        |            sage: p = GenericBackend()
        |            sage: p._test_something()
        |            Traceback (most recent call last):
        |            ...
        |            NotImplementedError
        |        ...
        |        p = cls()                         # fresh instance of the backend
        |        if tester is None:
        |            tester = p._tester(**options)
        |        tester.assertEqual(p.add_variable(obj=42, name='Helloooooo'), 0)
        |        tester.assertEqual(p.add_variable(obj=1789), 1)
        |        with tester.assertRaises(MIPSolverException) as cm:
        |            p.solve()

    We then copy from the generated file and paste into the source
    code of the generic backend, where all test methods are defined.

    If ``test_method_file`` is not provided, a default output file name
    will be computed from ``test_method``.
    """
