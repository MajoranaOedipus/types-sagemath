from sage.structure.category_object import normalize_names as normalize_names

class IndexedGenerators:
    '''nodetex
    Abstract base class for parents whose elements consist of generators
    indexed by an arbitrary set.

    Options controlling the printing of elements:

    - ``prefix`` -- string, prefix used for printing elements of this
      module (default: ``\'x\'``).  With the default, a monomial
      indexed by \'a\' would be printed as ``x[\'a\']``.

    - ``latex_prefix`` -- string or ``None``, prefix used in the `\\LaTeX`
      representation of elements (default: ``None``); if this is
      anything except the empty string, it prints the index as a
      subscript.  If this is ``None``, it uses the setting for ``prefix``,
      so if ``prefix`` is set to "B", then a monomial indexed by \'a\'
      would be printed as ``B_{a}``.  If this is the empty string, then
      don\'t print monomials as subscripts: the monomial indexed by \'a\'
      would be printed as ``a``, or as ``[a]`` if ``latex_bracket`` is
      ``True``.

    - ``names`` -- dictionary with strings as values or list of strings (optional);
      a mapping from the indices of the generators to strings giving the
      generators explicit names. This is used instead of the print options
      ``prefix`` and ``bracket`` when ``names`` is specified.

    - ``latex_names`` -- dictionary with strings as values or list of strings
      (optional); same as ``names`` except using the `\\LaTeX` representation

    - ``bracket`` -- ``None``, boolean, string, or list or tuple of
      strings (default: ``None``); if ``None``, use the value of the
      attribute ``self._repr_option_bracket``, which has default value
      ``True``.  (``self._repr_option_bracket`` is available for backwards
      compatibility.  Users should set ``bracket`` instead.  If
      ``bracket`` is set to anything except ``None``, it overrides
      the value of ``self._repr_option_bracket``.)  If ``False``, do not
      include brackets when printing elements: a monomial indexed by
      \'a\' would be printed as ``B\'a\'``, and a monomial indexed by
      (1,2,3) would be printed as ``B(1,2,3)``.  If ``True``, use "[" and
      "]" as brackets.  If it is one of "[", "(", or "{", use it and
      its partner as brackets.  If it is any other string, use it as
      both brackets.  If it is a list or tuple of strings, use the
      first entry as the left bracket and the second entry as the
      right bracket.

    - ``latex_bracket`` -- boolean, string, or list or tuple of strings
      (default: ``False``); if ``False``, do not include brackets in
      the LaTeX representation of elements.  This option is only
      relevant if ``latex_prefix`` is the empty string; otherwise,
      brackets are not used regardless.  If ``True``, use "\\left[" and
      "\\right]" as brackets.  If this is one of "[", "(", "\\\\{", "|",
      or "||", use it and its partner, prepended with "\\left" and
      "\\right", as brackets.  If this is any other string, use it as
      both brackets.  If this is a list or tuple of strings, use the
      first entry as the left bracket and the second entry as the
      right bracket.

    - ``scalar_mult`` -- string to use for scalar multiplication in
      the print representation (default: ``\'*\'``)

    - ``latex_scalar_mult`` -- string or ``None`` (default: ``None``);
      string to use for scalar multiplication in the latex
      representation.  If ``None``, use the empty string if ``scalar_mult``
      is set to "*", otherwise use the value of ``scalar_mult``.

    - ``tensor_symbol`` -- string or ``None`` (default: ``None``);
      string to use for tensor product in the print representation. If
      ``None``, use  ``sage.categories.tensor.symbol`` and
      ``sage.categories.tensor.unicode_symbol``.

    - ``sorting_key`` -- a key function (default: ``lambda x: x``);
      to use for sorting elements in the output of elements

    - ``sorting_reverse`` -- boolean (default: ``False``); if ``True``
      sort elements in reverse order in the output of elements

    - ``string_quotes`` -- boolean (default: ``True``); if ``True`` then
      display string indices with quotes

    - ``iterate_key`` -- boolean (default: ``False``); iterate through
      the elements of the key and print the result as comma separated
      objects for string output

    .. NOTE::

        These print options may also be accessed and modified using the
        :meth:`print_options` method, after the parent has been defined.

    EXAMPLES:

    We demonstrate a variety of the input options::

        sage: from sage.structure.indexed_generators import IndexedGenerators
        sage: I = IndexedGenerators(ZZ, prefix=\'A\')
        sage: I._repr_generator(2)
        \'A[2]\'
        sage: I._latex_generator(2)
        \'A_{2}\'

        sage: I = IndexedGenerators(ZZ, bracket=\'(\')
        sage: I._repr_generator(2)
        \'x(2)\'
        sage: I._latex_generator(2)
        \'x_{2}\'

        sage: I = IndexedGenerators(ZZ, prefix=\'\', latex_bracket=\'(\')
        sage: I._repr_generator(2)
        \'[2]\'
        sage: I._latex_generator(2)
        \\left( 2 \\right)

        sage: I = IndexedGenerators(ZZ, bracket=[\'|\', \'>\'])
        sage: I._repr_generator(2)
        \'x|2>\'
    '''
    def __init__(self, indices, prefix: str = 'x', **kwds) -> None:
        """
        Initialize ``self``.

        EXAMPLES:

        This is a mixin class, so don't need pickling equality::

            sage: I = sage.structure.indexed_generators.IndexedGenerators(ZZ)
            sage: TestSuite(I).run(skip='_test_pickling')
        """
    def indices(self):
        """
        Return the indices of ``self``.

        EXAMPLES::

            sage: F = CombinatorialFreeModule(QQ, ['a', 'b', 'c'])                      # needs sage.modules
            sage: F.indices()                                                           # needs sage.modules
            {'a', 'b', 'c'}
        """
    def prefix(self):
        """
        Return the prefix used when displaying elements of ``self``.

        EXAMPLES::

            sage: F = CombinatorialFreeModule(QQ, ['a', 'b', 'c'])                      # needs sage.modules
            sage: F.prefix()                                                            # needs sage.modules
            'B'

        ::

            sage: X = SchubertPolynomialRing(QQ)                                        # needs sage.combinat sage.modules
            sage: X.prefix()                                                            # needs sage.combinat sage.modules
            'X'
        """
    def print_options(self, **kwds):
        """
        Return the current print options, or set an option.

        INPUT:

        All of the input is optional; if present, it should be
        in the form of keyword pairs, such as
        ``latex_bracket='('``.  The allowable keywords are:

        - ``prefix``
        - ``latex_prefix``
        - ``names``
        - ``latex_names``
        - ``bracket``
        - ``latex_bracket``
        - ``scalar_mult``
        - ``latex_scalar_mult``
        - ``tensor_symbol``
        - ``string_quotes``
        - ``sorting_key``
        - ``sorting_reverse``
        - ``iterate_key``

        See the documentation for :class:`IndexedGenerators` for
        descriptions of the effects of setting each of these options.

        OUTPUT: if the user provides any input, set the appropriate
        option(s) and return nothing.  Otherwise, return the
        dictionary of settings for print and LaTeX representations.

        EXAMPLES::

            sage: # needs sage.modules
            sage: F = CombinatorialFreeModule(ZZ, [1,2,3], prefix='x')
            sage: F.print_options()
            {...'prefix': 'x'...}
            sage: F.print_options(bracket='(')
            sage: F.print_options()
            {...'bracket': '('...}

        TESTS::

            sage: sorted(F.print_options().items())                                     # needs sage.modules
            [('bracket', '('), ('iterate_key', False),
             ('latex_bracket', False), ('latex_names', None),
             ('latex_prefix', None), ('latex_scalar_mult', None),
             ('names', None), ('prefix', 'x'),
             ('scalar_mult', '*'),
             ('sorting_key', <function ...<lambda> at ...>),
             ('sorting_reverse', False), ('string_quotes', True),
             ('tensor_symbol', None)]
            sage: F.print_options(bracket='[')  # reset                                 # needs sage.modules
        """

def split_index_keywords(kwds):
    """
    Split the dictionary ``kwds`` into two dictionaries, one containing
    keywords for :class:`IndexedGenerators`, and the other is everything else.

    OUTPUT:

    The dictionary containing only they keywords
    for :class:`IndexedGenerators`. This modifies the dictionary ``kwds``.

    .. WARNING::

        This modifies the input dictionary ``kwds``.

    EXAMPLES::

        sage: from sage.structure.indexed_generators import split_index_keywords
        sage: d = {'string_quotes': False, 'bracket': None, 'base': QQ}
        sage: split_index_keywords(d)
        {'bracket': None, 'string_quotes': False}
        sage: d
        {'base': Rational Field}
    """
def parse_indices_names(names, index_set, prefix, kwds=None):
    """
    Parse the names, index set, and prefix input, along with setting
    default values for keyword arguments ``kwds``.

    OUTPUT:

    The triple ``(N, I, p)``:

    - ``N`` is the tuple of variable names,
    - ``I`` is the index set, and
    - ``p`` is the prefix.

    This modifies the dictionary ``kwds``.

    .. NOTE::

        When the indices, names, or prefix have not been given, it
        should be passed to this function as ``None``.

    .. NOTE::

        For handling default prefixes, if the result will be ``None`` if
        it is not processed in this function.

    EXAMPLES::

        sage: from sage.structure.indexed_generators import parse_indices_names
        sage: d = {}
        sage: parse_indices_names('x,y,z', ZZ, None, d)
        (('x', 'y', 'z'), Integer Ring, None)
        sage: d
        {}
        sage: d = {}
        sage: parse_indices_names('x,y,z', None, None, d)
        (('x', 'y', 'z'), {'x', 'y', 'z'}, '')
        sage: d
        {'string_quotes': False}
        sage: d = {}
        sage: parse_indices_names(None, ZZ, None, d)
        (None, Integer Ring, None)
        sage: d
        {}

    ::

        sage: d = {'string_quotes':True, 'bracket':'['}
        sage: parse_indices_names(['a','b','c'], ZZ, 'x', d)
        (('a', 'b', 'c'), Integer Ring, 'x')
        sage: d
        {'bracket': '[', 'string_quotes': True}
        sage: parse_indices_names('x,y,z', None, 'A', d)
        (('x', 'y', 'z'), {'x', 'y', 'z'}, 'A')
        sage: d
        {'bracket': '[', 'string_quotes': True}
    """
def standardize_names_index_set(names=None, index_set=None, ngens=None):
    """
    Standardize the ``names`` and ``index_set`` inputs.

    INPUT:

    - ``names`` -- (optional) the variable names
    - ``index_set`` -- (optional) the index set
    - ``ngens`` -- (optional) the number of generators

    If ``ngens`` is a negative number, then this does not check that
    the number of variable names matches the size of the index set.

    OUTPUT:

    A pair ``(names_std, index_set_std)``, where ``names_std`` is either
    ``None`` or a tuple of strings, and where ``index_set_std`` is a finite
    enumerated set.
    The purpose of ``index_set_std`` is to index the generators of some object
    (e.g., the basis of a module); the strings in ``names_std``, when they
    exist, are used for printing these indices. The ``ngens``

    If ``names`` contains exactly one name ``X`` and ``ngens`` is greater than
    1, then ``names_std`` are ``Xi`` for ``i`` in ``range(ngens)``.

    TESTS::

        sage: from sage.structure.indexed_generators import standardize_names_index_set
        sage: standardize_names_index_set('x,y')
        (('x', 'y'), {'x', 'y'})
        sage: standardize_names_index_set(['x','y'])
        (('x', 'y'), {'x', 'y'})
        sage: standardize_names_index_set(['x','y'], ['a','b'])
        (('x', 'y'), {'a', 'b'})
        sage: standardize_names_index_set('x,y', ngens=2)
        (('x', 'y'), {'x', 'y'})
        sage: standardize_names_index_set(index_set=['a','b'], ngens=2)
        (None, {'a', 'b'})
        sage: standardize_names_index_set('x', ngens=3)
        (('x0', 'x1', 'x2'), {'x0', 'x1', 'x2'})

        sage: standardize_names_index_set()
        Traceback (most recent call last):
        ...
        ValueError: the index_set, names, or number of generators must be specified
        sage: standardize_names_index_set(['x'], ['a', 'b'])
        Traceback (most recent call last):
        ...
        IndexError: the number of names must equal the size of the indexing set
        sage: standardize_names_index_set('x,y', ['a'])
        Traceback (most recent call last):
        ...
        IndexError: the number of names must equal the size of the indexing set
        sage: standardize_names_index_set('x,y,z', ngens=2)
        Traceback (most recent call last):
        ...
        IndexError: the number of names must equal the number of generators
        sage: standardize_names_index_set(index_set=['a'], ngens=2)
        Traceback (most recent call last):
        ...
        IndexError: the size of the indexing set must equal the number of generators
    """
