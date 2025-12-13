def parse(s):
    """
    Return a parse tree from a boolean formula ``s``.

    INPUT:

    - ``s`` -- string containing a boolean formula

    OUTPUT:

    A list containing the parse tree and a list containing the
    variables in a boolean formula in this order:

    1. the list containing the parse tree
    2. the list containing the variables

    EXAMPLES:

    This example illustrates how to produce the parse tree of a boolean
    formula ``s``::

        sage: import sage.logic.logicparser as logicparser
        sage: s = 'a|b&c'
        sage: t = logicparser.parse(s)
        sage: t
        (['|', 'a', ['&', 'b', 'c']], ['a', 'b', 'c'])
    """
def polish_parse(s):
    """
    Return the full syntax parse tree from a boolean formula ``s``.

    INPUT:

    - ``s`` -- string containing a boolean expression

    OUTPUT: the full syntax parse tree as a nested list

    EXAMPLES:

    This example illustrates how to find the full syntax parse tree
    of a boolean formula::

        sage: import sage.logic.logicparser as logicparser
        sage: s = 'a|~~b'
        sage: t = logicparser.polish_parse(s)
        sage: t
        ['|', 'a', ['~', ['~', 'b']]]

    AUTHORS:

    - Paul Scurek (2013-08-03)
    """
def get_trees(*statements):
    '''
    Return the full syntax parse trees of the statements.

    INPUT:

    - ``*statements`` -- strings or :class:`BooleanFormula` instances

    OUTPUT: the parse trees in a list

    EXAMPLES:

    This example illustrates finding the parse trees of multiple formulas.

    ::

        sage: import sage.logic.propcalc as propcalc
        sage: import sage.logic.logicparser as logicparser
        sage: f = propcalc.formula("((a|b)&~~c)")
        sage: g = "a<->(~(c))"
        sage: h = "~b"
        sage: logicparser.get_trees(f, g, h)
        [[\'&\', [\'|\', \'a\', \'b\'], [\'~\', [\'~\', \'c\']]],
        [\'<->\', \'a\', [\'~\', \'c\']],
        [\'~\', \'b\']]

    ::

        sage: i = "(~q->p)"
        sage: j = propcalc.formula("a")
        sage: logicparser.get_trees(i, j)
        [[\'->\', [\'~\', \'q\'], \'p\'], [\'a\']]

    ::

        sage: k = "p"
        sage: logicparser.get_trees(k)
        [[\'p\']]

    AUTHORS:

    - Paul Scurek (2013-08-06)
    '''
def recover_formula(prefix_tree):
    '''
    Recover the formula from a parse tree in prefix form.

    INPUT:

    - ``prefix_tree`` -- list; this is a full syntax parse
      tree in prefix form

    OUTPUT: the formula as a string

    EXAMPLES:

    This example illustrates the recovery of a formula from a parse tree::

        sage: import sage.logic.propcalc as propcalc
        sage: import sage.logic.logicparser as logicparser
        sage: t = [\'->\', [\'&\', \'a\', [\'~\', [\'~\', \'c\']]], [\'~\', [\'|\', [\'~\', \'c\'], \'d\']]]
        sage: logicparser.recover_formula(t)
        \'(a&~~c)->~(~c|d)\'

        sage: f = propcalc.formula("a&(~~c|d)")
        sage: logicparser.recover_formula(f.full_tree())
        \'a&(~~c|d)\'

        sage: r = [\'~\', \'a\']
        sage: logicparser.recover_formula(r)
        \'~a\'

        sage: s = [\'d\']
        sage: logicparser.recover_formula(s)
        \'d\'

    .. NOTE::

        The function :func:`~sage.logic.logicparser.polish_parse()` may be
        passed as an argument, but :func:`~sage.logic.logicparser.tree_parse()`
        may not unless the parameter ``polish`` is set to ``True``.

    AUTHORS:

    - Paul Scurek (2013-08-06)
    '''
def recover_formula_internal(prefix_tree):
    '''
    Recover the formula from a parse tree in prefix form.

    INPUT:

    - ``prefix_tree`` -- list; this is a simple tree
      with at most one operator in prefix form

    OUTPUT: the formula as a string

    EXAMPLES:

    This example illustrates recovering the formula from a parse tree::

        sage: import sage.logic.logicparser as logicparser
        sage: import sage.logic.propcalc as propcalc
        sage: t = [\'->\', \'a\', \'b\']
        sage: logicparser.recover_formula_internal(t)
        \'(a->b)\'

        sage: r = [\'~\', \'c\']
        sage: logicparser.recover_formula_internal(r)
        \'~c\'

        sage: s = [\'d\']
        sage: logicparser.recover_formula_internal(s)
        \'d\'

    We can pass :func:`~sage.logic.logicparser.recover_formula_internal()`
    as an argument in :func:`~sage.logic.logicparser.apply_func()`::

        sage: f = propcalc.formula("~(d|c)<->(a&~~~c)")
        sage: logicparser.apply_func(f.full_tree(), logicparser.recover_formula_internal)
        \'(~(d|c)<->(a&~~~c))\'

    .. NOTE::

        This function is for internal use by :mod:`~sage.logic.logicparser`.
        The function recovers the formula of a simple parse tree in prefix
        form. A simple parse tree contains at most one operator.

        The function :func:`~sage.logic.logicparser.polish_parse()` may be
        passed as an argument, but :func:`~sage.logic.logicparser.tree_parse()`
        may not unless the parameter ``polish`` is set to ``True``.

    AUTHORS:

    - Paul Scurek (2013-08-06)
    '''
def prefix_to_infix(prefix_tree):
    '''
    Convert a parse tree from prefix form to infix form.

    INPUT:

    - ``prefix_tree`` -- list; this is a full syntax parse
      tree in prefix form

    OUTPUT: list containing the tree in infix form

    EXAMPLES:

    This example illustrates converting a prefix tree to an infix tree::

        sage: import sage.logic.logicparser as logicparser
        sage: import sage.logic.propcalc as propcalc
        sage: t = [\'|\', [\'~\', \'a\'], [\'&\', \'b\', \'c\']]
        sage: logicparser.prefix_to_infix(t)
        [[\'~\', \'a\'], \'|\', [\'b\', \'&\', \'c\']]

    ::

        sage: f = propcalc.formula("(a&~b)<->~~~(c|d)")
        sage: logicparser.prefix_to_infix(f.full_tree())
        [[\'a\', \'&\', [\'~\', \'b\']], \'<->\', [\'~\', [\'~\', [\'~\', [\'c\', \'|\', \'d\']]]]]

    .. NOTE::

        The function :func:`~sage.logic.logicparser.polish_parse()` may be
        passed as an argument, but :func:`~sage.logic.logicparser.tree_parse()`
        may not unless the parameter ``polish`` is set to ``True``.

    AUTHORS:

    - Paul Scurek (2013-08-06)
    '''
def to_infix_internal(prefix_tree):
    '''
    Convert a simple parse tree from prefix form to infix form.

    INPUT:

    - ``prefix_tree`` -- list; this is a simple parse tree
      in prefix form with at most one operator

    OUTPUT: the tree in infix form as a list

    EXAMPLES:

    This example illustrates converting a simple tree from prefix
    to infix form::

        sage: import sage.logic.logicparser as logicparser
        sage: import sage.logic.propcalc as propcalc
        sage: t = [\'|\', \'a\', \'b\']
        sage: logicparser.to_infix_internal(t)
        [\'a\', \'|\', \'b\']

    We can pass :func:`~sage.logic.logicparser.to_infix_internal()` as an
    argument in :func:`~sage.logic.logicparser.apply_func()`::

        sage: f = propcalc.formula("(a&~b)<->~~~(c|d)")
        sage: logicparser.apply_func(f.full_tree(), logicparser.to_infix_internal)
        [[\'a\', \'&\', [\'~\', \'b\']], \'<->\', [\'~\', [\'~\', [\'~\', [\'c\', \'|\', \'d\']]]]]

    .. NOTE::

        This function is for internal use by :mod:`~sage.logic.logicparser`.
        It converts a simple parse tree from prefix form to infix form. A
        simple parse tree contains at most one operator.

        The function :func:`polish_parse` may be passed as an argument,
        but :func:`~sage.logic.logicparser.tree_parse()` may not unless the
        parameter ``polish`` is set to ``True``.

    AUTHORS:

    - Paul Scurek (2013-08-06)
    '''
def tokenize(s):
    """
    Return the tokens and the distinct variables appearing in a boolean
    formula ``s``.

    INPUT:

    - ``s`` -- string representation of a boolean formula

    OUTPUT:

    The tokens and variables as an ordered pair of lists in the following
    order:

    1. A list containing the tokens of ``s``, in the order they appear in ``s``
    2. A list containing the distinct variables in ``s``, in the order
       they appear in ``s``

    EXAMPLES:

    This example illustrates how to tokenize a string representation of a
    boolean formula::

        sage: import sage.logic.logicparser as logicparser
        sage: s = 'a|b&c'
        sage: t = logicparser.tokenize(s)
        sage: t
        (['(', 'a', '|', 'b', '&', 'c', ')'], ['a', 'b', 'c'])
    """
def tree_parse(toks, polish: bool = False):
    """
    Return a parse tree from the tokens in ``toks``.

    INPUT:

    - ``toks`` -- list of tokens from a boolean formula

    - ``polish`` -- boolean (default: ``False``); when ``True``,
      :func:`~sage.logic.logicparser.tree_parse()` will return
      the full syntax parse tree

    OUTPUT:

    A parse tree in the form of a nested list that depends on ``polish``
    as follows:

    - If ``False``, then return a simplified parse tree.

    - If ``True``, then return the full syntax parse tree.

    EXAMPLES:

    This example illustrates the use of
    :func:`~sage.logic.logicparser.tree_parse()` when ``polish`` is ``False``::

        sage: import sage.logic.logicparser as logicparser
        sage: t = ['(', 'a', '|', 'b', '&', 'c', ')']
        sage: logicparser.tree_parse(t)
        ['|', 'a', ['&', 'b', 'c']]

    We now demonstrate the use of :func:`~sage.logic.logicparser.tree_parse()`
    when ``polish`` is ``True``::

        sage: t = ['(', 'a', '->', '~', '~', 'b', ')']
        sage: logicparser.tree_parse(t)
        ['->', 'a', 'b']
        sage: t = ['(', 'a', '->', '~', '~', 'b', ')']
        sage: logicparser.tree_parse(t, polish = True)
        ['->', 'a', ['~', ['~', 'b']]]
    """
def parse_ltor(toks, n: int = 0, polish: bool = False):
    """
    Return a parse tree from ``toks``, where each token in ``toks`` is atomic.

    INPUT:

    - ``toks`` -- list of tokens; each token is atomic

    - ``n`` -- integer (default: 0) representing which order of
      operations are occurring

    - ``polish`` -- boolean (default: ``False``); when ``True``, double
      negations are not cancelled and negated statements are turned into
      list of length two

    OUTPUT: the parse tree as a nested list that depends on ``polish`` as follows:

    - If ``False``, then return a simplified parse tree.

    - If ``True``, then return the full syntax parse tree.

    EXAMPLES:

    This example illustrates the use of
    :func:`~sage.logic.logicparser.parse_ltor()` when ``polish`` is ``False``::

        sage: import sage.logic.logicparser as logicparser
        sage: t = ['a', '|', 'b', '&', 'c']
        sage: logicparser.parse_ltor(t)
        ['|', 'a', ['&', 'b', 'c']]

    ::

        sage: import sage.logic.logicparser as logicparser
        sage: t = ['a', '->', '~', '~', 'b']
        sage: logicparser.parse_ltor(t)
        ['->', 'a', 'b']

    We now repeat the previous example, but with ``polish`` being ``True``::

        sage: import sage.logic.logicparser as logicparser
        sage: t = ['a', '->', '~', '~', 'b']
        sage: logicparser.parse_ltor(t, polish = True)
        ['->', 'a', ['~', ['~', 'b']]]
    """
def apply_func(tree, func):
    """
    Apply ``func`` to each node of ``tree``, and return a new parse tree.

    INPUT:

    - ``tree`` -- a parse tree of a boolean formula

    - ``func`` -- a function to be applied to each node of tree; this may
      be a function that comes from elsewhere in the logic module

    OUTPUT: the new parse tree in the form of a nested list

    EXAMPLES:

    This example uses :func:`~sage.logic.logicparser.apply_func()` where
    ``func`` switches two entries of tree::

        sage: import sage.logic.logicparser as logicparser
        sage: t = ['|', ['&', 'a', 'b'], ['&', 'a', 'c']]
        sage: f = lambda t: [t[0], t[2], t[1]]
        sage: logicparser.apply_func(t, f)
        ['|', ['&', 'c', 'a'], ['&', 'b', 'a']]
    """
