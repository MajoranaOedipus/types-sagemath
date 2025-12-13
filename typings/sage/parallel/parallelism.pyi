from sage.misc.fast_methods import Singleton as Singleton
from sage.parallel.ncpus import ncpus as ncpus
from sage.rings.integer import Integer as Integer
from sage.structure.sage_object import SageObject as SageObject

class Parallelism(Singleton, SageObject):
    """
    Singleton class for managing the number of processes used in parallel
    computations involved in various fields.

    EXAMPLES:

    The number of processes is initialized to 1 (no parallelization) for
    each field::

        sage: Parallelism()
        Number of processes for parallelization:
         - linbox computations: 1
         - tensor computations: 1

    Using 4 processes to parallelize tensor computations::

        sage: Parallelism().set('tensor', nproc=4)
        sage: Parallelism()
        Number of processes for parallelization:
         - linbox computations: 1
         - tensor computations: 4
        sage: Parallelism().get('tensor')
        4

    Using 6 processes to parallelize all types of computations::

        sage: Parallelism().set(nproc=6)
        sage: Parallelism()
        Number of processes for parallelization:
         - linbox computations: 6
         - tensor computations: 6

    Using all the cores available on the computer to parallelize tensor
    computations::

        sage: Parallelism().set('tensor')
        sage: Parallelism()  # random (depends on the computer)
        Number of processes for parallelization:
         - linbox computations: 1
         - tensor computations: 8

    Using all the cores available on the computer to parallelize all types
    of computations::

        sage: Parallelism().set()
        sage: Parallelism()  # random (depends on the computer)
        Number of processes for parallelization:
         - linbox computations: 8
         - tensor computations: 8

    Switching off all parallelizations::

        sage: Parallelism().set(nproc=1)
    """
    def __init__(self) -> None:
        """
        Construct the single instance of class Parallelism (singleton model).

        TESTS::

            sage: par = Parallelism()
            sage: par
            Number of processes for parallelization:
             - linbox computations: 1
             - tensor computations: 1

        Test of the singleton character::

            sage: Parallelism() is par
            True

        The test suite is passed::

            sage: TestSuite(par).run()
        """
    def reset(self) -> None:
        """
        Put the singleton object ``Parallelism()`` in the same state as
        immediately after its creation.

        EXAMPLES:

        State of ``Parallelism()`` just after its creation::

            sage: Parallelism()
            Number of processes for parallelization:
             - linbox computations: 1
             - tensor computations: 1
            sage: Parallelism().get_default()  # random (depends on the computer)
            8

        Changing some values::

            sage: Parallelism().set_default(6)
            sage: Parallelism().set()
            sage: Parallelism()
            Number of processes for parallelization:
             - linbox computations: 6
             - tensor computations: 6
            sage: Parallelism().get_default()
            6

        Back to the initial state::

            sage: Parallelism().reset()
            sage: Parallelism()
            Number of processes for parallelization:
             - linbox computations: 1
             - tensor computations: 1
            sage: Parallelism().get_default()  # random (depends on the computer)
            8
        """
    def set(self, field=None, nproc=None) -> None:
        """
        Set the number of processes to be launched for parallel computations
        regarding some specific field.

        INPUT:

        - ``field`` -- (default: ``None``) string specifying the computational
          field for which the number of parallel processes is to be set; if
          ``None``, all fields are considered
        - ``nproc`` -- (default: ``None``) number of processes to be used for
          parallelization; if ``None``, the number of processes will be set to
          the default value, which, unless redefined by :meth:`set_default`,
          is the total number of cores found on the computer.

        EXAMPLES:

        The default is a single processor (no parallelization)::

            sage: Parallelism()
            Number of processes for parallelization:
             - linbox computations: 1
             - tensor computations: 1

        Asking for parallelization on 4 cores in tensor algebra::

            sage: Parallelism().set('tensor', nproc=4)
            sage: Parallelism()
            Number of processes for parallelization:
             - linbox computations: 1
             - tensor computations: 4

        Using all the cores available on the computer::

            sage: Parallelism().set('tensor')
            sage: Parallelism()  # random (depends on the computer)
            Number of processes for parallelization:
             - linbox computations: 1
             - tensor computations: 8

        Using 6 cores in all parallelizations::

            sage: Parallelism().set(nproc=6)
            sage: Parallelism()
            Number of processes for parallelization:
             - linbox computations: 6
             - tensor computations: 6

        Using all the cores available on the computer in all parallelizations::

            sage: Parallelism().set()
            sage: Parallelism()  # random (depends on the computer)
            Number of processes for parallelization:
             - linbox computations: 8
             - tensor computations: 8

        Switching off the parallelization::

            sage: Parallelism().set(nproc=1)
            sage: Parallelism()
            Number of processes for parallelization:
             - linbox computations: 1
             - tensor computations: 1
        """
    def get(self, field):
        """
        Return the number of processes which will be used in parallel
        computations regarding some specific field.

        INPUT:

        - ``field`` -- string specifying the part of Sage involved in
          parallel computations

        OUTPUT:

        - number of processes used in parallelization of computations
          pertaining to ``field``

        EXAMPLES:

        The default is a single process (no parallelization)::

            sage: Parallelism().reset()
            sage: Parallelism().get('tensor')
            1

        Asking for parallelization on 4 cores::

            sage: Parallelism().set('tensor', nproc=4)
            sage: Parallelism().get('tensor')
            4
        """
    def get_all(self):
        """
        Return the number of processes which will be used in parallel
        computations in all fields

        OUTPUT:

        - dictionary of the number of processes, with the computational fields
          as keys

        EXAMPLES::

            sage: Parallelism().reset()
            sage: Parallelism().get_all()
            {'linbox': 1, 'tensor': 1}

        Asking for parallelization on 4 cores::

            sage: Parallelism().set(nproc=4)
            sage: Parallelism().get_all()
            {'linbox': 4, 'tensor': 4}
        """
    def set_default(self, nproc=None) -> None:
        """
        Set the default number of processes to be launched in parallel
        computations.

        INPUT:

        - ``nproc`` -- (default: ``None``) default number of processes;
          if ``None``, the number of processes will be set to the total number
          of cores found on the computer.

        EXAMPLES:

        A priori the default number of process for parallelization is the
        total number of cores found on the computer::

            sage: Parallelism().get_default()  # random (depends on the computer)
            8

        Changing it thanks to ``set_default``::

            sage: Parallelism().set_default(nproc=4)
            sage: Parallelism().get_default()
            4

        Setting it back to the total number of cores available on the computer::

            sage: Parallelism().set_default()
            sage: Parallelism().get_default()  # random (depends on the computer)
            8
        """
    def get_default(self):
        """
        Return the default number of processes to be launched in parallel
        computations.

        EXAMPLES:

        A priori, the default number of process for parallelization is the
        total number of cores found on the computer::

            sage: Parallelism().reset()
            sage: Parallelism().get_default()  # random (depends on the computer)
            8

        It can be changed via :meth:`set_default`::

            sage: Parallelism().set_default(nproc=4)
            sage: Parallelism().get_default()
            4
        """
