def read_data(f, t):
    '''
    Read data from file ``f`` and class ``t`` (one element per line),
    and returns a list of elements.

    INPUT:

    - ``f`` -- a file name
    - ``t`` -- a class (objects will be coerced to that class)

    OUTPUT: list of elements of class ``t``

    EXAMPLES::

        sage: indata = tmp_filename()
        sage: f = open(indata, "w")
        sage: _ = f.write("17\\n42\\n")
        sage: f.close()
        sage: l = read_data(indata, ZZ); l
        [17, 42]
        sage: f = open(indata, "w")
        sage: _ = f.write("1.234\\n5.678\\n")
        sage: f.close()
        sage: l = read_data(indata, RealField(17)); l
        [1.234, 5.678]
    '''
