from sage.misc.timing import cputime as cputime

class Profiler:
    '''
    Keeps track of CPU time used between a series of user-defined checkpoints.

    It\'s probably not a good idea to use this class in an inner loop :-)

    EXAMPLES::

        from sage.misc.profiler import Profiler
        sage: def f():                        # not tested
        ....:     p = Profiler()

    Calling ``p(message)`` creates a checkpoint::

        sage: p("try factoring 15")           # not tested

    Do something time-consuming::

        sage: x = factor(15)                  # not tested

    You can create a checkpoints without a string; ``Profiler``
    will use the source code instead::

        sage: # not tested
        sage: p()
        sage: y = factor(25)
        sage: p("last step")
        sage: z = factor(35)
        sage: p()

    This will give a nice list of timings between checkpoints::

        sage: print(p)                        # not tested

    Let\'s try it out::

        sage: f()                             # not tested
            3.020s -- try factoring 15
           15.240s -- line 17: y = factor(25)
         5000.190s -- last step

    .. SEEALSO:: :func:`runsnake`

    .. TODO::

        - Add Pyrex source code inspection (I assume it doesn\'t
          currently do this)
        - Add ability to sort output by time
        - Add option to constructor to print timing immediately when
          checkpoint is reached
        - Migrate to Pyrex?
        - Add ability to return timings in a more machine-friendly
          format

    AUTHOR:

    - David Harvey (August 2006)
    '''
    def __init__(self, systems=[], verbose: bool = False) -> None:
        """
        INPUT:

        - ``systems`` -- list of interfaces to other system which implements a
          cputime method. The cputimes of all provided systems will be added
          to the cputime of Sage itself.
        """
    def clear(self) -> None: ...
    def __call__(self, message=None) -> None:
        """ Adds a checkpoint. """
    def print_last(self):
        """
        Print the last profiler step.
        """
