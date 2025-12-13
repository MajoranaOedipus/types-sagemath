from _typeshed import Incomplete

class SageTimeitResult:
    '''
    Represent the statistics of a timeit() command.

    Prints as a string so that it can be easily returned to a user.

    INPUT:

    - ``stats`` -- tuple of length 5 containing the following information:

        - integer, number of loops
        - integer, repeat number
        - Python integer, number of digits to print
        - number, best timing result
        - str, time unit

    EXAMPLES::

        sage: from sage.misc.sage_timeit import SageTimeitResult
        sage: SageTimeitResult( (3, 5, int(8), pi, \'ms\') )                              # needs sage.symbolic
        3 loops, best of 5: 3.1415927 ms per loop

    ::

        sage: units = [u"s", u"ms", u"μs", u"ns"]
        sage: scaling = [1, 1e3, 1e6, 1e9]
        sage: number = 7
        sage: repeat = 13
        sage: precision = int(5)
        sage: best = pi / 10 ^ 9                                                        # needs sage.symbolic
        sage: order = 3
        sage: stats = (number, repeat, precision, best * scaling[order], units[order])  # needs sage.symbolic
        sage: SageTimeitResult(stats)                                                   # needs sage.symbolic
        7 loops, best of 13: 3.1416 ns per loop

    If the third argument is not a Python integer, a :exc:`TypeError` is raised::

        sage: SageTimeitResult( (1, 2, 3, 4, \'s\') )
        <repr(<sage.misc.sage_timeit.SageTimeitResult at 0x...>) failed: TypeError: * wants int>
    '''
    stats: Incomplete
    series: Incomplete
    def __init__(self, stats, series=None) -> None:
        """
        Construction of a timing result.

        See documentation of ``SageTimeitResult`` for more details and
        examples.

        EXAMPLES::

            sage: from sage.misc.sage_timeit import SageTimeitResult
            sage: SageTimeitResult( (3, 5, int(8), pi, 'ms') )                          # needs sage.symbolic
            3 loops, best of 5: 3.1415927 ms per loop
            sage: s = SageTimeitResult( (3, 5, int(8), pi, 'ms'), [1.0,1.1,0.5])        # needs sage.symbolic
            sage: s.series                                                              # needs sage.symbolic
            [1.00000000000000, 1.10000000000000, 0.500000000000000]
        """

def sage_timeit(stmt, globals_dict=None, preparse=None, number: int = 0, repeat: int = 3, precision: int = 3, seconds: bool = False):
    '''nodetex
    Accurately measure the wall time required to execute ``stmt``.

    INPUT:

    - ``stmt`` -- a text string

    - ``globals_dict`` -- dictionary or ``None`` (default). Evaluate
      ``stmt`` in the context of the globals dictionary. If not set,
      the current ``globals()`` dictionary is used.

    - ``preparse`` -- (default: use globals preparser default) if
      ``True`` preparse ``stmt`` using the Sage preparser

    - ``number`` -- integer; (default: 0); number of loops

    - ``repeat`` -- integer; (default: 3); number of repetition

    - ``precision`` -- integer; (default: 3); precision of output time

    - ``seconds`` -- boolean (default: ``False``); whether to just
      return time in seconds

    OUTPUT:

    An instance of ``SageTimeitResult`` unless the optional parameter
    ``seconds=True`` is passed. In that case, the elapsed time in
    seconds is returned as a floating-point number.

    EXAMPLES::

        sage: from sage.misc.sage_timeit import sage_timeit
        sage: sage_timeit(\'3^100000\', globals(), preparse=True, number=50)      # random output
        \'50 loops, best of 3: 1.97 ms per loop\'
        sage: sage_timeit(\'3^100000\', globals(), preparse=False, number=50)     # random output
        \'50 loops, best of 3: 67.1 ns per loop\'
        sage: a = 10
        sage: sage_timeit(\'a^2\', globals(), number=50)                            # random output
        \'50 loops, best of 3: 4.26 us per loop\'

    If you only want to see the timing and not have access to additional
    information, just use the ``timeit`` object::

        sage: timeit(\'10^2\', number=50)
        50 loops, best of 3: ... per loop

    Using sage_timeit gives you more information though::

        sage: s = sage_timeit(\'10^2\', globals(), repeat=1000)
        sage: len(s.series)
        1000
        sage: mean(s.series)   # random output                                          # needs sage.modules
        3.1298141479492283e-07
        sage: min(s.series)    # random output
        2.9258728027343752e-07
        sage: t = stats.TimeSeries(s.series)                                            # needs numpy sage.modules
        sage: t.scale(10^6).plot_histogram(bins=20,figsize=[12,6], ymax=2)              # needs numpy sage.modules sage.plot
        Graphics object consisting of 20 graphics primitives


    The input expression can contain newlines (but doctests cannot, so
    we use ``os.linesep`` here)::

        sage: from sage.misc.sage_timeit import sage_timeit
        sage: from os import linesep as CR
        sage: # sage_timeit(r\'a = 2\\nb=131\\nfactor(a^b-1)\')
        sage: sage_timeit(\'a = 2\' + CR + \'b=131\' + CR + \'factor(a^b-1)\',                # needs sage.libs.pari
        ....:             globals(), number=10)
        10 loops, best of 3: ... per loop

    Test to make sure that ``timeit`` behaves well with output::

        sage: timeit("print(\'Hi\')", number=50)
        50 loops, best of 3: ... per loop

    If you want a machine-readable output, use the ``seconds=True`` option::

        sage: timeit("print(\'Hi\')", seconds=True)   # random output
        1.42555236816e-06
        sage: t = timeit("print(\'Hi\')", seconds=True)
        sage: t     #r random output
        3.6010742187499999e-07

    TESTS:

    Make sure that garbage collection is re-enabled after an exception
    occurs in timeit::

        sage: def f(): raise ValueError
        sage: import gc
        sage: gc.isenabled()
        True
        sage: timeit("f()")
        Traceback (most recent call last):
        ...
        ValueError
        sage: gc.isenabled()
        True
    '''
