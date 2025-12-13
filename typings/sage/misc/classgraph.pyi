def class_graph(top, depth: int = 5, name_filter=None, classes=None, as_graph: bool = True):
    """
    Return the class inheritance graph of a module, class, or object.

    INPUT:

    - ``top`` -- the module, class, or object to start with (e.g. ``sage``,
      ``Integer``, ``3``)
    - ``depth`` -- maximal recursion depth within submodules (default: 5)
    - ``name_filter`` -- e.g. 'sage.rings' to only consider classes in
      :mod:`sage.rings`
    - ``classes`` -- (optional) dictionary to be filled in (it is also returned)
    - ``as_graph`` -- boolean (default: ``True``)

    OUTPUT:

    An oriented graph, with class names as vertices, and an edge
    from each class to each of its bases.

    EXAMPLES:

    We construct the inheritance graph of the classes within a given module::

        sage: from sage.rings.polynomial.padics import polynomial_padic_capped_relative_dense, polynomial_padic_flat
        sage: G = class_graph(sage.rings.polynomial.padics); G
        Digraph on 6 vertices
        sage: G.vertices(sort=True)
        ['Polynomial',
         'Polynomial_generic_cdv',
         'Polynomial_generic_dense',
         'Polynomial_padic',
         'Polynomial_padic_capped_relative_dense',
         'Polynomial_padic_flat']
        sage: G.edges(sort=True, labels=False)
        [('Polynomial_padic', 'Polynomial'),
         ('Polynomial_padic_capped_relative_dense', 'Polynomial_generic_cdv'),
         ('Polynomial_padic_capped_relative_dense', 'Polynomial_padic'),
         ('Polynomial_padic_flat', 'Polynomial_generic_dense'),
         ('Polynomial_padic_flat', 'Polynomial_padic')]

    We construct the inheritance graph of a given class::

        sage: class_graph(Parent).edges(sort=True, labels=False)
        [('CategoryObject', 'SageObject'), ('Parent', 'CategoryObject'), ('SageObject', 'object')]

    We construct the inheritance graph of the class of an object::

        sage: class_graph([1,2,3]).edges(sort=True, labels=False)
        [('list', 'object')]

    .. warning:: the output of ``class_graph`` used to be a dictionary
       mapping each class name to the list of names of its bases. This
       can be emulated by setting the option ``as_graph`` to ``False``::

        sage: class_graph(sage.rings.polynomial.padics, depth=2, as_graph=False)
        {'Polynomial_padic': ['Polynomial'],
         'Polynomial_padic_capped_relative_dense': ['Polynomial_generic_cdv',
          'Polynomial_padic'],
         'Polynomial_padic_flat': ['Polynomial_generic_dense', 'Polynomial_padic']}

    .. NOTE:: the ``classes`` and ``as_graph`` options are mostly
       intended for internal recursive use.

    .. NOTE:: ``class_graph`` does not yet handle nested classes

    TESTS::

        sage: G = class_graph(sage.rings.polynomial.padics, depth=2); G
        Digraph on 6 vertices
    """
