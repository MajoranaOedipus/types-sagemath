import multiprocessing as mp
from _typeshed import Incomplete
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.sets.recursively_enumerated_set import RecursivelyEnumeratedSet as RecursivelyEnumeratedSet

logger: Incomplete
ch: Incomplete
formatter: Incomplete

def proc_number(max_proc=None):
    """
    Return the number of processes to use.

    INPUT:

    - ``max_proc`` -- an upper bound on the number of processes or ``None``

    EXAMPLES::

        sage: from sage.parallel.map_reduce import proc_number
        sage: proc_number()  # random
        8
        sage: proc_number(max_proc=1)
        1
        sage: proc_number(max_proc=2) in (1, 2)
        True
    """

class AbortError(Exception):
    """
    Exception for aborting parallel computations.

    This is used both as exception or as abort message.

    TESTS::

        sage: from sage.parallel.map_reduce import AbortError
        sage: raise AbortError
        Traceback (most recent call last):
        ...
        AbortError
    """

class ActiveTaskCounterDarwin:
    """
    Handling the number of active tasks.

    A class for handling the number of active tasks in a distributed
    computation process. This is essentially a semaphore, but Darwin OSes
    do not correctly implement POSIX's semaphore semantic. So we use
    a shared integer with a lock.
    """
    def __init__(self, task_number) -> None:
        """
        TESTS::

            sage: from sage.parallel.map_reduce import ActiveTaskCounterDarwin as ATC
            sage: t = ATC(4)
            sage: TestSuite(t).run(skip='_test_pickling', verbose=True)
            running ._test_new() . . . pass
        """
    def task_start(self):
        """
        Increment the task counter by one.

        OUTPUT:

        Calling :meth:`task_start` on a zero or negative counter returns 0,
        otherwise increment the counter and returns its value after the
        incrementation.

        EXAMPLES::

            sage: from sage.parallel.map_reduce import ActiveTaskCounterDarwin as ATC
            sage: c = ATC(4); c
            ActiveTaskCounter(value=4)
            sage: c.task_start()
            5
            sage: c
            ActiveTaskCounter(value=5)

        Calling :meth:`task_start` on a zero counter does nothing::

            sage: c = ATC(0)
            sage: c.task_start()
            0
            sage: c
            ActiveTaskCounter(value=0)
        """
    def task_done(self):
        """
        Decrement the task counter by one.

        OUTPUT:

        Calling :meth:`task_done` decrements the counter and returns
        its new value.

        EXAMPLES::

            sage: from sage.parallel.map_reduce import ActiveTaskCounterDarwin as ATC
            sage: c = ATC(4); c
            ActiveTaskCounter(value=4)
            sage: c.task_done()
            3
            sage: c
            ActiveTaskCounter(value=3)

            sage: c = ATC(0)
            sage: c.task_done()
            -1
        """
    def abort(self) -> None:
        """
        Set the task counter to zero.

        EXAMPLES::

            sage: from sage.parallel.map_reduce import ActiveTaskCounterDarwin as ATC
            sage: c = ATC(4); c
            ActiveTaskCounter(value=4)
            sage: c.abort()
            sage: c
            ActiveTaskCounter(value=0)
        """

class ActiveTaskCounterPosix:
    """
    Handling the number of active tasks.

    A class for handling the number of active tasks in a distributed
    computation process. This is the standard implementation on POSIX
    compliant OSes. We essentially wrap a semaphore.

    .. NOTE::

        A legitimate question is whether there is a need in keeping the two
        implementations. I ran the following experiment on my machine::

            S = RecursivelyEnumeratedSet(
                    [[]],
                    lambda l: ([l[:i] + [len(l)] + l[i:]
                                for i in range(len(l) + 1)]
                               if len(l) < NNN else []),
                    structure='forest',
                    enumeration='depth')
            %time sp = S.map_reduce(lambda z: x**len(z)); sp

        For NNN = 10, averaging a dozen of runs, I got:

        - Posix compliant implementation: 17.04 s
        - Darwin implementation: 18.26 s

        So there is a non negligible overhead. It will probably be worth it
        if we try to cythonize the code. So I'm keeping both implementations.
    """
    def __init__(self, task_number) -> None:
        """
        TESTS::

            sage: from sage.parallel.map_reduce import ActiveTaskCounter as ATC
            sage: t = ATC(4)
            sage: TestSuite(t).run(skip='_test_pickling', verbose=True)
            running ._test_new() . . . pass
        """
    def task_start(self):
        """
        Increment the task counter by one.

        OUTPUT:

        Calling :meth:`task_start` on a zero or negative counter returns 0,
        otherwise it increments the counter and returns its new value.

        EXAMPLES::

            sage: from sage.parallel.map_reduce import ActiveTaskCounter as ATC
            sage: c = ATC(4); c
            ActiveTaskCounter(value=4)
            sage: c.task_start()
            5
            sage: c
            ActiveTaskCounter(value=5)

        Calling :meth:`task_start` on a zero counter does nothing::

            sage: c = ATC(0)
            sage: c.task_start()
            0
            sage: c
            ActiveTaskCounter(value=0)
        """
    def task_done(self):
        """
        Decrement the task counter by one.

        OUTPUT:

        Calling :meth:`task_done` decrements the counter and returns
        its new value.

        EXAMPLES::

            sage: from sage.parallel.map_reduce import ActiveTaskCounter as ATC
            sage: c = ATC(4); c
            ActiveTaskCounter(value=4)
            sage: c.task_done()
            3
            sage: c
            ActiveTaskCounter(value=3)

            sage: c = ATC(0)
            sage: c.task_done()
            -1
        """
    def abort(self) -> None:
        """
        Set the task counter to zero.

        EXAMPLES::

            sage: from sage.parallel.map_reduce import ActiveTaskCounter as ATC
            sage: c = ATC(4); c
            ActiveTaskCounter(value=4)
            sage: c.abort()
            sage: c
            ActiveTaskCounter(value=0)
        """

ActiveTaskCounter: Incomplete

class RESetMapReduce:
    """
    Map-Reduce on recursively enumerated sets.

    INPUT:

    Description of the set:

    - either ``forest=f`` -- where ``f`` is a :class:`RecursivelyEnumeratedSet_forest>`

    - or a triple ``roots, children, post_process`` as follows

      - ``roots=r`` -- the root of the enumeration
      - ``children=c`` -- a function iterating through children nodes,
        given a parent node
      - ``post_process=p`` -- a post-processing function

    The option ``post_process`` allows for customizing the nodes that
    are actually produced. Furthermore, if ``post_process(x)`` returns ``None``,
    then ``x`` won't be output at all.

    Description of the map/reduce operation:

    - ``map_function=f`` -- (default: ``None``)
    - ``reduce_function=red`` -- (default: ``None``)
    - ``reduce_init=init`` -- (default: ``None``)

    .. SEEALSO::

       :mod:`the Map/Reduce module <sage.parallel.map_reduce>` for
       details and examples.
    """
    children: Incomplete
    def __init__(self, roots=None, children=None, post_process=None, map_function=None, reduce_function=None, reduce_init=None, forest=None) -> None:
        """
        TESTS::

            sage: from sage.parallel.map_reduce import RESetMapReduce
            sage: R = RESetMapReduce([[]], lambda: [[]])
            sage: R
            <sage.parallel.map_reduce.RESetMapReduce object at 0x...>

        To silence the coverage checker::

            sage: TestSuite(R).run(skip=['_test_pickling'])
        """
    def roots(self):
        """
        Return the roots of ``self``.

        OUTPUT: an iterable of nodes

        .. NOTE:: This should be overloaded in applications.

        EXAMPLES::

            sage: from sage.parallel.map_reduce import RESetMapReduce
            sage: S = RESetMapReduce(42)
            sage: S.roots()
            42
        """
    def map_function(self, o):
        """
        Return the function mapped by ``self``.

        INPUT:

        - ``o`` -- a node

        OUTPUT: by default ``1``

        .. NOTE:: This should be overloaded in applications.

        EXAMPLES::

            sage: from sage.parallel.map_reduce import RESetMapReduce
            sage: S = RESetMapReduce()
            sage: S.map_function(7)
            1
            sage: S = RESetMapReduce(map_function = lambda x: 3*x + 5)
            sage: S.map_function(7)
            26
        """
    def reduce_function(self, a, b):
        """
        Return the reducer function for ``self``.

        INPUT:

        - ``a``, ``b`` -- two values to be reduced

        OUTPUT: by default the sum of ``a`` and ``b``

        .. NOTE:: This should be overloaded in applications.

        EXAMPLES::

            sage: from sage.parallel.map_reduce import RESetMapReduce
            sage: S = RESetMapReduce()
            sage: S.reduce_function(4, 3)
            7
            sage: S = RESetMapReduce(reduce_function=lambda x,y: x*y)
            sage: S.reduce_function(4, 3)
            12
        """
    def post_process(self, a):
        """
        Return the image of ``a`` under the post-processing function for ``self``.

        INPUT:

        - ``a`` -- a node

        With the default post-processing function, which is the identity function,
        this returns ``a`` itself.

        .. NOTE:: This should be overloaded in applications.

        EXAMPLES::

            sage: from sage.parallel.map_reduce import RESetMapReduce
            sage: S = RESetMapReduce()
            sage: S.post_process(4)
            4
            sage: S = RESetMapReduce(post_process=lambda x: x*x)
            sage: S.post_process(4)
            16
        """
    def reduce_init(self):
        """
        Return the initial element for a reduction.

        .. NOTE:: This should be overloaded in applications.

        TESTS::

            sage: from sage.parallel.map_reduce import RESetMapReduce
            sage: S = RESetMapReduce()
            sage: S.reduce_init()
            0
            sage: S = RESetMapReduce(reduce_init = 2)
            sage: S.reduce_init()
            2
        """
    def setup_workers(self, max_proc=None, reduce_locally: bool = True) -> None:
        """
        Setup the communication channels.

        INPUT:

        - ``max_proc`` -- integer; an upper bound on the number of
          worker processes

        - ``reduce_locally`` -- whether the workers should reduce locally
          their work or sends results to the master as soon as possible.
          See :class:`RESetMapReduceWorker` for details.

        TESTS::

            sage: from sage.parallel.map_reduce import RESetMapReduce
            sage: S = RESetMapReduce()
            sage: S.setup_workers(2)
            sage: S._results
            <multiprocessing.queues.Queue object at 0x...>
            sage: len(S._workers)
            2
        """
    def start_workers(self) -> None:
        '''
        Launch the workers.

        The workers should have been created using :meth:`setup_workers`.

        TESTS::

            sage: # long time
            sage: from sage.parallel.map_reduce import RESetMapReduce
            sage: def children(x):
            ....:     print(f"Starting: {x}", flush=True)
            ....:     return []
            sage: S = RESetMapReduce(roots=[1, 2], children=children)
            sage: S.setup_workers(2)
            sage: S.start_workers(); sleep(float(5))
            Starting: ...
            Starting: ...
            sage: S.finish()
        '''
    def get_results(self, timeout=None):
        """
        Get the results from the queue.

        OUTPUT:

        The reduction of the results of all the workers, that is, the result of
        the map/reduce computation.

        EXAMPLES::

            sage: from sage.parallel.map_reduce import RESetMapReduce
            sage: S = RESetMapReduce()
            sage: S.setup_workers(2)
            sage: for v in [1, 2, None, 3, None]: S._results.put(v)
            sage: S.get_results()
            6

        Cleanup::

            sage: del S._results, S._active_tasks, S._done, S._workers
        """
    def finish(self) -> None:
        """
        Destroy the workers and all the communication objects.

        Communication statistics are gathered before destroying the workers.

        TESTS::

            sage: from sage.parallel.map_reduce import RESetMPExample
            sage: S = RESetMPExample(maxl=5)
            sage: S.setup_workers(2)  # indirect doctest
            sage: S._workers[0]._todo.append([])
            sage: for w in S._workers: w.start()
            sage: _ = S.get_results()
            sage: S._shutdown()
            sage: S.print_communication_statistics()
            Traceback (most recent call last):
            ...
            AttributeError: 'RESetMPExample' object has no attribute '_stats'...

            sage: S.finish()

            sage: S.print_communication_statistics()
            #proc: ...
            ...

            sage: _ = S.run()  # cleanup

        .. SEEALSO:: :meth:`print_communication_statistics`
        """
    def abort(self) -> None:
        """
        Abort the current parallel computation.

        EXAMPLES::

            sage: from sage.parallel.map_reduce import RESetParallelIterator
            sage: S = RESetParallelIterator([[]],
            ....:     lambda l: [l + [0], l + [1]] if len(l) < 17 else [])
            sage: it = iter(S)
            sage: next(it)  # random
            []
            sage: S.abort()
            sage: hasattr(S, 'work_queue')
            False

        Cleanup::

            sage: S.finish()
        """
    def random_worker(self):
        """
        Return a random worker.

        OUTPUT: a worker for ``self`` chosen at random

        EXAMPLES::

            sage: from sage.parallel.map_reduce import RESetMPExample, RESetMapReduceWorker
            sage: from threading import Thread
            sage: EX = RESetMPExample(maxl=6)
            sage: EX.setup_workers(2)
            sage: EX.random_worker()
            <RESetMapReduceWorker...RESetMapReduceWorker-... initial...>
            sage: EX.random_worker() in EX._workers
            True

        Cleanup::

            sage: del EX._results, EX._active_tasks, EX._done, EX._workers
        """
    result: Incomplete
    def run(self, max_proc=None, reduce_locally: bool = True, timeout=None, profile=None):
        '''
        Run the computations.

        INPUT:

        - ``max_proc`` -- (integer, default: ``None``) if given, the
          maximum number of worker processors to use. The actual number
          is also bounded by the value of the environment variable
          ``SAGE_NUM_THREADS`` (the number of cores by default).
        - ``reduce_locally`` -- see :class:`RESetMapReduceWorker` (default: ``True``)
        - ``timeout`` -- a timeout on the computation (default: ``None``)
        - ``profile`` -- directory/filename prefix for profiling, or ``None``
          for no profiling (default: ``None``)

        OUTPUT:

        The result of the map/reduce computation or an exception
        :exc:`AbortError` if the computation was interrupted or timeout.

        EXAMPLES::

            sage: from sage.parallel.map_reduce import RESetMPExample
            sage: EX = RESetMPExample(maxl = 8)
            sage: EX.run()
            40320*x^8 + 5040*x^7 + 720*x^6 + 120*x^5 + 24*x^4 + 6*x^3 + 2*x^2 + x + 1

        Here is an example or how to deal with timeout::

            sage: from sage.parallel.map_reduce import AbortError
            sage: EX = RESetMPExample(maxl = 100)
            sage: try:
            ....:     res = EX.run(timeout=float(0.01))
            ....: except AbortError:
            ....:     print("Computation timeout")
            ....: else:
            ....:     print("Computation normally finished")
            ....:     res
            Computation timeout

        The following should not timeout even on a very slow machine::

            sage: from sage.parallel.map_reduce import AbortError
            sage: EX = RESetMPExample(maxl = 8)
            sage: try:
            ....:     res = EX.run(timeout=60)
            ....: except AbortError:
            ....:     print("Computation Timeout")
            ....: else:
            ....:     print("Computation normally finished")
            ....:     res
            Computation normally finished
            40320*x^8 + 5040*x^7 + 720*x^6 + 120*x^5 + 24*x^4 + 6*x^3 + 2*x^2 + x + 1
        '''
    def print_communication_statistics(self, blocksize: int = 16) -> None:
        """
        Print the communication statistics in a nice way.

        EXAMPLES::

            sage: from sage.parallel.map_reduce import RESetMPExample
            sage: S = RESetMPExample(maxl=6)
            sage: S.run()
            720*x^6 + 120*x^5 + 24*x^4 + 6*x^3 + 2*x^2 + x + 1

            sage: S.print_communication_statistics()  # random
            #proc:        0    1    2    3    4    5    6    7
            reqs sent:    5    2    3   11   21   19    1    0
            reqs rcvs:   10   10    9    5    1   11    9    2
            - thefs:      1    0    0    0    0    0    0    0
            + thefs:      0    0    1    0    0    0    0    0
        """
    def run_serial(self):
        """
        Run the computation serially (mostly for tests).

        EXAMPLES::

            sage: from sage.parallel.map_reduce import RESetMPExample
            sage: EX = RESetMPExample(maxl = 4)
            sage: EX.run_serial()
            24*x^4 + 6*x^3 + 2*x^2 + x + 1
        """

class RESetMapReduceWorker(mp.Process):
    """
    Worker for generate-map-reduce.

    This shouldn't be called directly, but instead created by
    :meth:`RESetMapReduce.setup_workers`.

    INPUT:

    - ``mapred`` -- the instance of :class:`RESetMapReduce` for which
      this process is working

    - ``iproc`` -- the id of this worker

    - ``reduce_locally`` -- when reducing the results. Three possible values
      are supported:

      * ``True`` -- means the reducing work is done all locally, the result is
        only sent back at the end of the work. This ensure the lowest level of
        communication.

      * ``False`` -- results are sent back after each finished branches, when
        the process is asking for more work.
    """
    def __init__(self, mapred, iproc, reduce_locally) -> None:
        """
        TESTS::

            sage: from sage.parallel.map_reduce import RESetMPExample, RESetMapReduceWorker
            sage: EX = RESetMPExample()
            sage: RESetMapReduceWorker(EX, 200, True)
            <RESetMapReduceWorker...RESetMapReduceWorker-... initial...>
        """
    def steal(self):
        """
        Steal some node from another worker.

        OUTPUT: a node stolen from another worker chosen at random

        EXAMPLES::

            sage: from sage.parallel.map_reduce import RESetMPExample, RESetMapReduceWorker
            sage: from threading import Thread
            sage: EX = RESetMPExample(maxl=6)
            sage: EX.setup_workers(2)

            sage: # known bug (Issue #27537)
            sage: w0, w1 = EX._workers
            sage: w0._todo.append(42)
            sage: thief0 = Thread(target = w0._thief, name='Thief')
            sage: thief0.start()
            sage: w1.steal()
            42
            sage: w0._todo
            deque([])
        """
    def run(self) -> None:
        """
        The main function executed by the worker.

        Calls :meth:`run_myself` after possibly setting up parallel profiling.

        EXAMPLES::

            sage: from sage.parallel.map_reduce import RESetMPExample, RESetMapReduceWorker
            sage: EX = RESetMPExample(maxl=6)
            sage: EX.setup_workers(1)

            sage: w = EX._workers[0]
            sage: w._todo.append(EX.roots()[0])

            sage: w.run()
            sage: sleep(int(1))
            sage: w._todo.append(None)

            sage: EX.get_results()
            720*x^6 + 120*x^5 + 24*x^4 + 6*x^3 + 2*x^2 + x + 1

        Cleanups::

            sage: del EX._results, EX._active_tasks, EX._done, EX._workers
        """
    def run_myself(self) -> None:
        """
        The main function executed by the worker.

        EXAMPLES::

            sage: from sage.parallel.map_reduce import RESetMPExample, RESetMapReduceWorker
            sage: EX = RESetMPExample(maxl=6)
            sage: EX.setup_workers(1)

            sage: w = EX._workers[0]
            sage: w._todo.append(EX.roots()[0])
            sage: w.run_myself()

            sage: sleep(int(1))
            sage: w._todo.append(None)

            sage: EX.get_results()
            720*x^6 + 120*x^5 + 24*x^4 + 6*x^3 + 2*x^2 + x + 1

        Cleanups::

            sage: del EX._results, EX._active_tasks, EX._done, EX._workers
        """
    def send_partial_result(self) -> None:
        """
        Send results to the MapReduce process.

        Send the result stored in ``self._res`` to the master and reinitialize it to
        ``master.reduce_init``.

        EXAMPLES::

            sage: from sage.parallel.map_reduce import RESetMPExample, RESetMapReduceWorker
            sage: EX = RESetMPExample(maxl=4)
            sage: EX.setup_workers(1)
            sage: w = EX._workers[0]
            sage: w._res = 4
            sage: w.send_partial_result()
            sage: w._res
            0
            sage: EX._results.get()
            4
        """
    def walk_branch_locally(self, node) -> None:
        """
        Work locally.

        Performs the map/reduce computation on the subtrees rooted at ``node``.

        INPUT:

        - ``node`` -- the root of the subtree explored

        OUTPUT: nothing, the result are stored in ``self._res``

        This is where the actual work is performed.

        EXAMPLES::

            sage: from sage.parallel.map_reduce import RESetMPExample, RESetMapReduceWorker
            sage: EX = RESetMPExample(maxl=4)
            sage: w = RESetMapReduceWorker(EX, 0, True)
            sage: def sync(): pass
            sage: w.synchronize = sync
            sage: w._res = 0

            sage: w.walk_branch_locally([])
            sage: w._res
            x^4 + x^3 + x^2 + x + 1

            sage: w.walk_branch_locally(w._todo.pop())
            sage: w._res
            2*x^4 + x^3 + x^2 + x + 1

            sage: while True: w.walk_branch_locally(w._todo.pop())
            Traceback (most recent call last):
            ...
            IndexError: pop from an empty deque
            sage: w._res
            24*x^4 + 6*x^3 + 2*x^2 + x + 1
        """

class RESetMPExample(RESetMapReduce):
    """
    An example of map reduce class.

    INPUT:

    - ``maxl`` -- the maximum size of permutations generated (default: `9`)

    This computes the generating series of permutations counted by their size
    up to size ``maxl``.

    EXAMPLES::

        sage: from sage.parallel.map_reduce import RESetMPExample
        sage: EX = RESetMPExample()
        sage: EX.run()
        362880*x^9 + 40320*x^8 + 5040*x^7 + 720*x^6 + 120*x^5
        + 24*x^4 + 6*x^3 + 2*x^2 + x + 1

    .. SEEALSO:: This is an example of :class:`RESetMapReduce`
    """
    x: Incomplete
    maxl: Incomplete
    def __init__(self, maxl: int = 9) -> None:
        """
        TESTS::

            sage: from sage.parallel.map_reduce import RESetMPExample
            sage: RESetMPExample()
            <sage.parallel.map_reduce.RESetMPExample object at 0x...>
        """
    def roots(self):
        """
        Return the empty permutation.

        EXAMPLES::

            sage: from sage.parallel.map_reduce import RESetMPExample
            sage: RESetMPExample().roots()
            [[]]
        """
    def children(self, l):
        """
        Return the children of the permutation `l`.

        INPUT:

        - ``l`` -- list containing a permutation

        OUTPUT:

        The lists with ``len(l)`` inserted at all possible positions into ``l``.

        EXAMPLES::

            sage: from sage.parallel.map_reduce import RESetMPExample
            sage: RESetMPExample().children([1,0])
            [[2, 1, 0], [1, 2, 0], [1, 0, 2]]
        """
    def map_function(self, l):
        """
        The monomial associated to the permutation `l`.

        INPUT:

        - ``l`` -- list containing a permutation

        OUTPUT:

        The monomial ``x^len(l)``.

        EXAMPLES::

            sage: from sage.parallel.map_reduce import RESetMPExample
            sage: RESetMPExample().map_function([1,0])
            x^2
        """

class RESetParallelIterator(RESetMapReduce):
    """
    A parallel iterator for recursively enumerated sets.

    This demonstrates how to use :class:`RESetMapReduce` to get an iterator on
    a recursively enumerated set for which the computations are done in
    parallel.

    EXAMPLES::

        sage: from sage.parallel.map_reduce import RESetParallelIterator
        sage: S = RESetParallelIterator([[]],
        ....:     lambda l: [l + [0], l + [1]] if len(l) < 15 else [])
        sage: sum(1 for _ in S)
        65535
    """
    def map_function(self, z):
        """
        Return a singleton tuple.

        INPUT:

        - ``z`` -- a node

        OUTPUT:

        The singleton ``(z, )``.

        EXAMPLES::

            sage: from sage.parallel.map_reduce import RESetParallelIterator
            sage: S = RESetParallelIterator( [[]],
            ....:     lambda l: [l + [0], l + [1]] if len(l) < 15 else [])
            sage: S.map_function([1, 0])
            ([1, 0],)
        """
    reduce_init = tuple
    def __iter__(self):
        """
        EXAMPLES::

            sage: from sage.parallel.map_reduce import RESetParallelIterator
            sage: S = RESetParallelIterator( [[]],
            ....:     lambda l: [l + [0], l + [1]] if len(l) < 15 else [])
            sage: it = iter(S)
            sage: next(it)  # random
            [1, 1, 0]
            sage: next(it)  # random
            [1, 1, 0, 1]
            sage: sum(1 for _ in it)
            65533
        """
