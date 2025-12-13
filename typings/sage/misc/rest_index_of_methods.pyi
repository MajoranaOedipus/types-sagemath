from _typeshed import Incomplete

def gen_rest_table_index(obj, names=None, sort: bool = True, only_local_functions: bool = True, root=None):
    '''
    Return a ReST table describing a list of functions.

    The list of functions can either be given explicitly, or implicitly as the
    functions/methods of a module or class.

    In the case of a class, only non-inherited methods are listed.

    INPUT:

    - ``obj`` -- list of functions, a module or a class. If given a list of
      functions, the generated table will consist of these. If given a module
      or a class, all functions/methods it defines will be listed, except
      deprecated or those starting with an underscore. In the case of a class,
      note that inherited methods are not displayed.

    - ``names`` -- dictionary associating a name to a function. Takes
      precedence over the automatically computed name for the functions. Only
      used when ``list_of_entries`` is a list.

    - ``sort`` -- boolean (default: ``True``); whether to sort the list of
      methods lexicographically

    - ``only_local_functions`` -- boolean (default: ``True``); if
      ``list_of_entries`` is a module, ``only_local_functions = True`` means
      that imported functions will be filtered out. This can be useful to
      disable for making indexes of e.g. catalog modules such as
      :mod:`sage.coding.codes_catalog`.

    - ``root`` -- module or class (default: ``None``); the module, or class,
      whose elements are to be listed. This is needed to recover the class when
      this method is called from :meth:`gen_thematic_rest_table_index` (see
      :issue:`36178`).

    .. WARNING::

        The ReST tables returned by this function use \'@\' as a delimiter for
        cells. This can cause trouble if the first sentence in the documentation
        of a function contains the \'@\' character.

    EXAMPLES::

        sage: from sage.misc.rest_index_of_methods import gen_rest_table_index
        sage: print(gen_rest_table_index([graphs.PetersenGraph]))                       # needs sage.graphs
        .. csv-table::
           :class: contentstable
           :widths: 30, 70
           :delim: @
        <BLANKLINE>
           :func:`~sage.graphs.generators.smallgraphs.PetersenGraph` @ Return the Petersen Graph.

    The table of a module::

        sage: print(gen_rest_table_index(sage.misc.rest_index_of_methods))
        .. csv-table::
           :class: contentstable
           :widths: 30, 70
           :delim: @
        <BLANKLINE>
           :func:`~sage.misc.rest_index_of_methods.doc_index` @ Attribute an index name to a function.
           :func:`~sage.misc.rest_index_of_methods.gen_rest_table_index` @ Return a ReST table describing a list of functions.
           :func:`~sage.misc.rest_index_of_methods.gen_thematic_rest_table_index` @ Return a ReST string of thematically sorted functions (or methods) of a module (or class).
           :func:`~sage.misc.rest_index_of_methods.list_of_subfunctions` @ Return the functions (resp. methods) of a given module (resp. class) with their names.
        <BLANKLINE>
        <BLANKLINE>

    The table of a class::

        sage: print(gen_rest_table_index(Graph))                                        # needs sage.graphs
        .. csv-table::
           :class: contentstable
           :widths: 30, 70
           :delim: @
        ...
           :meth:`~sage.graphs.graph.Graph.sparse6_string` @ Return the sparse6 representation of the graph as an ASCII string.
        ...

    TESTS:

    When the first sentence of the docstring spans over several lines::

        sage: def a():
        ....:     r\'\'\'
        ....:     Here is a very very very long sentence
        ....:     that spans on several lines.
        ....:
        ....:     EXAMP...
        ....:     \'\'\'
        ....:     print("hey")
        sage: \'Here is a very very very long sentence that spans on several lines\' in gen_rest_table_index([a])
        True

    The inherited methods do not show up::

        sage: # needs sage.graphs
        sage: gen_rest_table_index(sage.combinat.posets.lattices.FiniteLatticePoset).count(\'\\n\') < 75
        True
        sage: from sage.graphs.generic_graph import GenericGraph
        sage: A = gen_rest_table_index(Graph).count(\'\\n\')
        sage: B = gen_rest_table_index(GenericGraph).count(\'\\n\')
        sage: A < B
        True

    When ``only_local_functions`` is ``False``, we do not include
    ``gen_rest_table_index`` itself::

        sage: print(gen_rest_table_index(sage.misc.rest_index_of_methods, only_local_functions=True))
        .. csv-table::
           :class: contentstable
           :widths: 30, 70
           :delim: @
        <BLANKLINE>
           :func:`~sage.misc.rest_index_of_methods.doc_index` @ Attribute an index name to a function.
           :func:`~sage.misc.rest_index_of_methods.gen_rest_table_index` @ Return a ReST table describing a list of functions.
           :func:`~sage.misc.rest_index_of_methods.gen_thematic_rest_table_index` @ Return a ReST string of thematically sorted functions (or methods) of a module (or class).
           :func:`~sage.misc.rest_index_of_methods.list_of_subfunctions` @ Return the functions (resp. methods) of a given module (resp. class) with their names.
        <BLANKLINE>
        <BLANKLINE>
        sage: print(gen_rest_table_index(sage.misc.rest_index_of_methods, only_local_functions=False))
        .. csv-table::
           :class: contentstable
           :widths: 30, 70
           :delim: @
        <BLANKLINE>
           :func:`~sage.misc.rest_index_of_methods.doc_index` @ Attribute an index name to a function.
           :func:`~sage.misc.rest_index_of_methods.gen_thematic_rest_table_index` @ Return a ReST string of thematically sorted functions (or methods) of a module (or class).
           :func:`~sage.misc.rest_index_of_methods.list_of_subfunctions` @ Return the functions (resp. methods) of a given module (resp. class) with their names.
        <BLANKLINE>
        <BLANKLINE>

    A function that is imported into a class under a different name is listed
    under its \'new\' name::

        sage: \'cliques_maximum\' in gen_rest_table_index(Graph)                          # needs sage.graphs
        True
        sage: \'all_max_cliques`\' in gen_rest_table_index(Graph)                         # needs sage.graphs
        False

    Check that :issue:`36178` is fixed::

        sage: print(gen_rest_table_index(Graph))                                        # needs sage.graphs
        ...
           :meth:`~sage.graphs.graph.Graph.independent_set` @ Return a maximum independent set.
        ...
    '''
def list_of_subfunctions(root, only_local_functions: bool = True):
    """
    Return the functions (resp. methods) of a given module (resp. class) with their names.

    INPUT:

    - ``root`` -- the module, or class, whose elements are to be listed

    - ``only_local_functions`` -- boolean (default: ``True``); if ``root`` is a
      module, ``only_local_functions = True`` means that imported functions will
      be filtered out. This can be useful to disable for making indexes of
      e.g. catalog modules such as :mod:`sage.coding.codes_catalog`.

    OUTPUT:

    A pair ``(list,dict)`` where ``list`` is a list of function/methods and
    ``dict`` associates to every function/method the name under which it appears
    in ``root``.

    EXAMPLES::

        sage: from sage.misc.rest_index_of_methods import list_of_subfunctions
        sage: l = list_of_subfunctions(Graph)[0]                                        # needs sage.graphs
        sage: Graph.bipartite_color in l                                                # needs sage.graphs
        True

    TESTS:

    A ``staticmethod`` is not callable. We must handle them correctly, however::

        sage: class A:                                                                  # needs sage.graphs
        ....:     x = staticmethod(Graph.order)
        sage: list_of_subfunctions(A)                                                   # needs sage.graphs
        ([<function GenericGraph.order at 0x...>],
         {<function GenericGraph.order at 0x...>: 'x'})
    """
def gen_thematic_rest_table_index(root, additional_categories=None, only_local_functions: bool = True):
    """
    Return a ReST string of thematically sorted functions (or methods) of a
    module (or class).

    INPUT:

    - ``root`` -- the module, or class, whose elements are to be listed

    - ``additional_categories`` -- dictionary (default: ``None``); a dictionary
      associating a category (given as a string) to a function's name. Can be
      used when the decorator :func:`doc_index` does not work on a function.

    - ``only_local_functions`` -- boolean (default: ``True``); if ``root`` is a
      module, ``only_local_functions = True`` means that imported functions will
      be filtered out. This can be useful to disable for making indexes of
      e.g. catalog modules such as :mod:`sage.coding.codes_catalog`.

    EXAMPLES::

        sage: from sage.misc.rest_index_of_methods import gen_thematic_rest_table_index, list_of_subfunctions
        sage: l = list_of_subfunctions(Graph)[0]                                        # needs sage.graphs
        sage: Graph.bipartite_color in l                                                # needs sage.graphs
        True
    """
def doc_index(name):
    '''
    Attribute an index name to a function.

    This decorator can be applied to a function/method in order to specify in
    which index it must appear, in the index generated by
    :func:`gen_thematic_rest_table_index`.

    INPUT:

    - ``name`` -- string, which will become the title of the index in which
      this function/method will appear

    EXAMPLES::

        sage: from sage.misc.rest_index_of_methods import doc_index
        sage: @doc_index("Wouhouuuuu")
        ....: def a():
        ....:     print("Hey")
        sage: a.doc_index
        \'Wouhouuuuu\'
    '''

__doc__: Incomplete
