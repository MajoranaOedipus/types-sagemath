def ncpus():
    """
    Return the number of available CPUs in the system.

    ALGORITHM: :func:`os.sched_getaffinity` or :func:`os.cpu_count`

    EXAMPLES::

        sage: sage.parallel.ncpus.ncpus()  # random output -- depends on machine
        2
    """
