from . import logicparser as logicparser

def eval_formula(tree, vdict):
    """
    Evaluate the tree and return a boolean value.

    INPUT:

    - ``tree`` -- list of three elements corresponding to a branch of a
      parse tree

    - ``vdict`` -- dictionary containing variable keys and boolean values

    OUTPUT: the result of the evaluation as a boolean value

    EXAMPLES:

    This example illustrates evaluating a boolean formula::

        sage: import sage.logic.booleval as booleval
        sage: t = ['|', ['&', 'a', 'b'], ['&', 'a', 'c']]
        sage: d = {'a' : True, 'b' : False, 'c' : True}
        sage: booleval.eval_formula(t, d)
        True

    ::

        sage: d['a'] = False
        sage: booleval.eval_formula(t, d)
        False
    """
def eval_f(tree):
    """
    Evaluate the tree.

    INPUT:

    - ``tree`` -- list of three elements corresponding to a branch of a
      parse tree

    OUTPUT: the result of the evaluation as a boolean value

    EXAMPLES:

    This example illustrates how to evaluate a parse tree::

         sage: import sage.logic.booleval as booleval
         sage: booleval.eval_f(['&', True, False])
         False

         sage: booleval.eval_f(['^', True, True])
         False

         sage: booleval.eval_f(['|', False, True])
         True
    """
def eval_op(op, lv, rv):
    """
    Evaluate ``lv`` and ``rv`` according to the operator ``op``.

    INPUT:

    - ``op`` -- string or character representing a boolean operator

    - ``lv`` -- boolean or variable

    - ``rv`` -- boolean or variable

    OUTPUT: the evaluation of ``lv op rv`` as a boolean value

    EXAMPLES:

    We can evaluate an operator given the values on either side::

        sage: import sage.logic.booleval as booleval
        sage: booleval.eval_op('&', True, False)
        False

        sage: booleval.eval_op('^', True, True)
        False

        sage: booleval.eval_op('|', False, True)
        True
    """
