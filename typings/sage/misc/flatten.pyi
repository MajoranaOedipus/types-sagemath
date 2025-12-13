def flatten(in_list, ltypes=..., max_level=...):
    """
    Flatten a nested list.

    INPUT:

    - ``in_list`` -- list or tuple
    - ``ltypes`` -- (optional) list of particular types to flatten
    - ``max_level`` -- the maximum level to flatten

    OUTPUT: a flat list of the entries of ``in_list``

    EXAMPLES::

       sage: flatten([[1,1],[1],2])
       [1, 1, 1, 2]
       sage: flatten([[1,2,3], (4,5), [[[1],[2]]]])
       [1, 2, 3, 4, 5, 1, 2]
       sage: flatten([[1,2,3], (4,5), [[[1],[2]]]], max_level=1)
       [1, 2, 3, 4, 5, [[1], [2]]]
       sage: flatten([[[3],[]]],max_level=0)
       [[[3], []]]
       sage: flatten([[[3],[]]],max_level=1)
       [[3], []]
       sage: flatten([[[3],[]]],max_level=2)
       [3]

    In the following example, the vector is not flattened because
    it is not given in the ``ltypes`` input. ::

       sage: flatten((['Hi', 2, vector(QQ, [1,2,3])], (4,5,6)))                         # needs sage.modules
       ['Hi', 2, (1, 2, 3), 4, 5, 6]

    We give the vector type and then even the vector gets flattened::

       sage: tV = sage.modules.vector_rational_dense.Vector_rational_dense              # needs sage.modules
       sage: flatten((['Hi', 2, vector(QQ, [1,2,3])], (4,5,6)),                         # needs sage.modules
       ....:         ltypes=(list, tuple, tV))
       ['Hi', 2, 1, 2, 3, 4, 5, 6]

    We flatten a finite field. ::

       sage: flatten(GF(5))
       [0, 1, 2, 3, 4]
       sage: flatten([GF(5)])
       [Finite Field of size 5]
       sage: tGF = type(GF(5))
       sage: flatten([GF(5)], ltypes=(list, tuple, tGF))
       [0, 1, 2, 3, 4]

    Degenerate cases::

        sage: flatten([[],[]])
        []
        sage: flatten([[[]]])
        []
    """
