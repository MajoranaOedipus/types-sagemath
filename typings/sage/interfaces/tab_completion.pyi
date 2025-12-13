class ExtraTabCompletion:
    def __dir__(self):
        """
        Add to the ``dir()`` output.

        This is used by IPython to read off the tab completions.

        EXAMPLES::

            sage: from sage.interfaces.tab_completion import ExtraTabCompletion
            sage: obj = ExtraTabCompletion()
            sage: dir(obj)
            Traceback (most recent call last):
            ...
            NotImplementedError: <class 'sage.interfaces.tab_completion.ExtraTabCompletion'> must implement _tab_completion() method
        """

def completions(s, globs):
    """
    Return a list of completions in the given context.

    INPUT:

    - ``s`` -- string

    - ``globs`` -- string: object dictionary; context in which to
      search for completions, e.g., :func:`globals()`

    OUTPUT: list of strings

    EXAMPLES::

         sage: X.<x> = PolynomialRing(QQ)
         sage: import sage.interfaces.tab_completion as s
         sage: p = x**2 + 1
         sage: s.completions('p.co',globals()) # indirect doctest
         ['p.coefficient',...]

         sage: s.completions('dic',globals()) # indirect doctest
         ['dickman_rho', 'dict']
    """
