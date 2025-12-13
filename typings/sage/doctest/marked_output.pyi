class MarkedOutput(str):
    '''
    A subclass of string with context for whether another string
    matches it.

    EXAMPLES::

        sage: from sage.doctest.marked_output import MarkedOutput
        sage: s = MarkedOutput("abc")
        sage: s.rel_tol
        0
        sage: s.update(rel_tol = .05)
        \'abc\'
        sage: s.rel_tol
        0.0500000000000000

        sage: MarkedOutput("56 µs")
        \'56 µs\'
    '''
    random: bool
    rel_tol: int
    abs_tol: int
    tol: int
    def update(self, **kwds):
        '''
        EXAMPLES::

            sage: from sage.doctest.marked_output import MarkedOutput
            sage: s = MarkedOutput("0.0007401")
            sage: s.update(abs_tol = .0000001)
            \'0.0007401\'
            sage: s.rel_tol
            0
            sage: s.abs_tol
            1.00000000000000e-7
        '''
    def __reduce__(self):
        '''
        Pickling.

        EXAMPLES::

            sage: from sage.doctest.marked_output import MarkedOutput
            sage: s = MarkedOutput("0.0007401")
            sage: s.update(abs_tol = .0000001)
            \'0.0007401\'
            sage: t = loads(dumps(s)) # indirect doctest
            sage: t == s
            True
            sage: t.abs_tol
            1.00000000000000e-7
        '''

def make_marked_output(s, D):
    '''
    Auxiliary function for pickling.

    EXAMPLES::

        sage: from sage.doctest.marked_output import make_marked_output
        sage: s = make_marked_output("0.0007401", {\'abs_tol\':.0000001})
        sage: s
        \'0.0007401\'
        sage: s.abs_tol
        1.00000000000000e-7
    '''
