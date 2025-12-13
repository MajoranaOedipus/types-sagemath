from _typeshed import Incomplete

tok_list: Incomplete
bin_list: Incomplete
operators: str
vars: Incomplete
vars_order: Incomplete

class SymbolicLogic:
    '''
    EXAMPLES:

    This example illustrates how to create a boolean formula and print
    its table::

        sage: log = SymbolicLogic()
        sage: s = log.statement("a&b|!(c|a)")
        sage: t = log.truthtable(s)
        sage: log.print_table(t)
        a     | b     | c     | value |
        --------------------------------
        False | False | False | True  |
        False | False | True  | False |
        False | True  | False | True  |
        False | True  | True  | False |
        True  | False | False | False |
        True  | False | True  | False |
        True  | True  | False | True  |
        True  | True  | True  | True  |
    '''
    def statement(self, s):
        '''
        Return a token list to be used by other functions in the class.

        INPUT:

        - ``s`` -- string containing the logic expression to be manipulated

        - ``global vars`` -- dictionary with variable names as keys and the
          variables\' current boolean values as dictionary values

        - ``global vars_order`` -- list of the variables in the order
          that they are found

        OUTPUT: list of length three containing the following in this order:

        1. a list of tokens
        2. a dictionary of variable/value pairs
        3. a list of the variables in the order they were found

        EXAMPLES:

        This example illustrates the creation of a statement::

            sage: log = SymbolicLogic()
            sage: s = log.statement("a&b|!(c|a)")
            sage: s2 = log.statement("!((!(a&b)))")

        It is an error to use invalid variable names::

            sage: s = log.statement("3fe & @q")
            Invalid variable name:  3fe
            Invalid variable name:  @q

        It is also an error to use invalid syntax::

            sage: s = log.statement("a&&b")
            Malformed Statement
            sage: s = log.statement("a&((b)")
            Malformed Statement
        '''
    def truthtable(self, statement, start: int = 0, end: int = -1):
        '''
        Return a truth table.

        INPUT:

        - ``statement`` -- list; it contains the tokens and the two global
          variables vars and vars_order

        - ``start`` -- integer (default: 0); this represents the row of
          the truth table from which to start

        - ``end`` -- integer (default: -1); this represents the last row
          of the truth table to be created

        OUTPUT:

        The truth table as a 2d array with the creating formula tacked
        to the front.

        EXAMPLES:

        This example illustrates the creation of a statement::

            sage: log = SymbolicLogic()
            sage: s = log.statement("a&b|!(c|a)")
            sage: t = log.truthtable(s) #creates the whole truth table

        We can now create truthtable of rows 1 to 5::

            sage: s2 = log.truthtable(s, 1, 5); s2
            [[[\'OPAREN\',
               \'a\',
               \'AND\',
               \'b\',
               \'OR\',
               \'NOT\',
               \'OPAREN\',
               \'c\',
               \'OR\',
               \'a\',
               \'CPAREN\',
               \'CPAREN\'],
              {\'a\': \'True\', \'b\': \'False\', \'c\': \'False\'},
              [\'a\', \'b\', \'c\']],
             [\'False\', \'False\', \'True\', \'False\'],
             [\'False\', \'True\', \'False\', \'True\'],
             [\'False\', \'True\', \'True\', \'False\'],
             [\'True\', \'False\', \'False\', \'False\']]

        .. NOTE::

            When sent with no start or end parameters this is an
            exponential time function requiring `O(2^n)` time, where
            `n` is the number of variables in the logic expression

        TESTS:

        Verify that :issue:`32676` is fixed::

            sage: s = log.statement("a&b|!(c|a)")
            sage: copy_s2 = copy(s[2])
            sage: t = log.truthtable(s)
            sage: s[2] == copy_s2
            True
        '''
    def print_table(self, table) -> None:
        '''
        Return a truthtable corresponding to the given statement.

        INPUT:

        - ``table`` -- object created by :meth:`truthtable()` method; it
          contains the variable values and the evaluation of the statement

        OUTPUT: a formatted version of the truth table

        EXAMPLES:

        This example illustrates the creation of a statement and
        its truth table::

            sage: log = SymbolicLogic()
            sage: s = log.statement("a&b|!(c|a)")
            sage: t = log.truthtable(s) #creates the whole truth table
            sage: log.print_table(t)
            a     | b     | c     | value |
            --------------------------------
            False | False | False | True  |
            False | False | True  | False |
            False | True  | False | True  |
            False | True  | True  | False |
            True  | False | False | False |
            True  | False | True  | False |
            True  | True  | False | True  |
            True  | True  | True  | True  |

        We can also print a shortened table::

            sage: t = log.truthtable(s, 1, 5)
            sage: log.print_table(t)
            a     | b     | c     | value |
            --------------------------------
            False | False | True  | False |
            False | True  | False | True  |
            False | True  | True  | False |
            True  | False | False | False |

        TESTS:

        Verify that :issue:`32676` is fixed::

            sage: table = log.truthtable(log.statement("A->B"))
            sage: table_copy = table.copy()
            sage: log.print_table(table)
            ...
            sage: table_copy == table
            True
        '''
    def combine(self, statement1, statement2):
        '''
        Return a new statement which contains the
        two statements or\'d together.

        INPUT:

        - ``statement1`` -- the first statement
        - ``statement2`` -- the second statement

        OUTPUT: a new statement which or\'d the given statements together

        EXAMPLES::

            sage: log = SymbolicLogic()
            sage: s1 = log.statement("(a&b)")
            sage: s2 = log.statement("b")
            sage: log.combine(s1,s2)
            [[\'OPAREN\',
              \'OPAREN\',
              \'OPAREN\',
              \'a\',
              \'AND\',
              \'b\',
              \'CPAREN\',
              \'CPAREN\',
              \'OR\',
              \'OPAREN\',
              \'b\',
              \'CPAREN\',
              \'CPAREN\'],
             {\'a\': \'False\', \'b\': \'False\'},
             [\'a\', \'b\', \'b\']]
        '''
    def simplify(self, table) -> None:
        '''
        Call a C++ implementation of the ESPRESSO algorithm to simplify the
        given truth table.

        .. TODO::

            Implement this method.

        EXAMPLES::

            sage: log = SymbolicLogic()
            sage: s = log.statement("a&b|!(c|a)")
            sage: t = log.truthtable(s)
            sage: log.simplify(t)
            Traceback (most recent call last):
            ...
            NotImplementedError
        '''
    def prove(self, statement) -> None:
        '''
        A function to test to see if the statement is a tautology or
        contradiction by calling a C++ library.

        .. TODO::

            Implement this method.

        EXAMPLES::

            sage: log = SymbolicLogic()
            sage: s = log.statement("a&b|!(c|a)")
            sage: log.prove(s)
            Traceback (most recent call last):
            ...
            NotImplementedError
        '''

def get_bit(x, c):
    """
    Determine if bit ``c`` of the number ``x`` is 1.

    INPUT:

    - ``x`` -- integer; this is the number from which to take the bit

    - ``c`` -- integer; this is the bit number to be taken

    OUTPUT: a boolean value to be determined as follows:

    - ``True`` if bit ``c`` of ``x`` is 1.

    - ``False`` if bit ``c`` of ``x`` is not 1.

    .. NOTE::

        This function is for internal use by the :class:`SymbolicLogic` class.

    EXAMPLES::

        sage: from sage.logic.logic import get_bit
        sage: get_bit(int(2), int(1))
        'True'
        sage: get_bit(int(8), int(0))
        'False'
    """
def eval(toks):
    '''
    Evaluate the expression contained in ``toks``.

    INPUT:

    - ``toks`` -- list of tokens; this represents a boolean expression

    OUTPUT: a boolean value to be determined as follows:

    - ``True`` if expression evaluates to ``True``.

    - ``False`` if expression evaluates to ``False``.

    .. NOTE::

        This function is for internal use by the :class:`SymbolicLogic` class.
        The evaluations rely on setting the values of the variables in the
        global dictionary vars.

    TESTS::

        sage: log = SymbolicLogic()
        sage: s = log.statement("a&b|!(c|a)")
        sage: sage.logic.logic.eval(s[0])
        \'True\'
    '''
def eval_ltor_toks(lrtoks):
    '''
    Evaluates the expression contained in ``lrtoks``.

    INPUT:

    - ``lrtoks`` -- list of tokens; this represents a part of a boolean
      formula that contains no inner parentheses

    OUTPUT: a boolean value to be determined as follows:

    - ``True`` if expression evaluates to ``True``.

    - ``False`` if expression evaluates to ``False``.

    .. NOTE::

        This function is for internal use by the :class:`SymbolicLogic` class.
        The evaluations rely on setting the values of the variables in the
        global dictionary vars.

    TESTS::

        sage: log = SymbolicLogic()
        sage: s = log.statement("a&b|!c")
        sage: ltor = s[0][1:-1]; ltor
        [\'a\', \'AND\', \'b\', \'OR\', \'NOT\', \'c\']
        sage: sage.logic.logic.eval_ltor_toks(ltor)
        \'True\'
    '''
def reduce_bins(lrtoks) -> None:
    '''
    Evaluate ``lrtoks`` to a single boolean value.

    INPUT:

    - ``lrtoks`` -- list of tokens; this represents a part of a boolean
      formula that contains no inner parentheses or monotonic operators

    OUTPUT:

    ``None``; the pointer to lrtoks is now a list containing
    ``True`` or ``False``.

    .. NOTE::

        This function is for internal use by the :class:`SymbolicLogic` class.

    TESTS::

        sage: log = SymbolicLogic()
        sage: s = log.statement("a&b|c")
        sage: lrtoks = s[0][1:-1]; lrtoks
        [\'a\', \'AND\', \'b\', \'OR\', \'c\']
        sage: sage.logic.logic.reduce_bins(lrtoks); lrtoks
        [\'False\']
    '''
def reduce_monos(lrtoks) -> None:
    '''
    Replace monotonic operator/variable pairs with a boolean value.

    INPUT:

    - ``lrtoks`` -- list of tokens; this represents a part of a boolean
      expression that contains now inner parentheses

    OUTPUT:

    ``None``; the pointer to ``lrtoks`` is now a list containing
    monotonic operators.

    .. NOTE::

        This function is for internal use by the :class:`SymbolicLogic` class.

    TESTS::

        sage: log = SymbolicLogic()
        sage: s = log.statement("!a&!b")
        sage: lrtoks = s[0][1:-1]; lrtoks
        [\'NOT\', \'a\', \'AND\', \'NOT\', \'b\']
        sage: sage.logic.logic.reduce_monos(lrtoks); lrtoks
        [\'True\', \'AND\', \'True\']
    '''
def eval_mon_op(args):
    '''
    Return a boolean value based on the truth table of the operator
    in ``args``.

    INPUT:

    - ``args`` -- list of length 2; this contains the token \'NOT\' and
      then a variable name

    OUTPUT: a boolean value to be determined as follows:

    - ``True`` if the variable in ``args`` is ``False``.

    - ``False`` if the variable in ``args`` is ``True``.

    .. NOTE::

        This function is for internal use by the :class:`SymbolicLogic` class.

    TESTS::

        sage: log = SymbolicLogic()
        sage: s = log.statement("!(a&b)|!a"); s
        [[\'OPAREN\', \'NOT\', \'OPAREN\', \'a\', \'AND\', \'b\', \'CPAREN\', \'OR\',
         \'NOT\', \'a\', \'CPAREN\'],
         {\'a\': \'False\', \'b\': \'False\'},
         [\'a\', \'b\']]
        sage: sage.logic.logic.eval_mon_op([\'NOT\', \'a\'])
        \'True\'
    '''
def eval_bin_op(args):
    '''
    Return a boolean value based on the truth table of the operator
    in ``args``.

    INPUT:

    - ``args`` -- list of length 3; this contains a variable name,
      then a binary operator, and then a variable name, in that order

    OUTPUT:

    A boolean value; this is the evaluation of the operator based on the
    truth values of the variables.

    .. NOTE::

        This function is for internal use by the :class:`SymbolicLogic` class.

    TESTS::

        sage: log = SymbolicLogic()
        sage: s = log.statement("!(a&b)"); s
        [[\'OPAREN\', \'NOT\', \'OPAREN\', \'a\', \'AND\', \'b\', \'CPAREN\', \'CPAREN\'],
         {\'a\': \'False\', \'b\': \'False\'},
         [\'a\', \'b\']]
        sage: sage.logic.logic.eval_bin_op([\'a\', \'AND\', \'b\'])
        \'False\'
    '''
def eval_and_op(lval, rval):
    """
    Apply the 'and' operator to ``lval`` and ``rval``.

    INPUT:

    - ``lval`` -- string; this represents the value of the variable
      appearing to the left of the 'and' operator

    - ``rval`` -- string; this represents the value of the variable
      appearing to the right of the 'and' operator

    OUTPUT: the result of applying 'and' to ``lval`` and ``rval`` as a string

    .. NOTE::

        This function is for internal use by the :class:`SymbolicLogic` class.

    TESTS::

        sage: sage.logic.logic.eval_and_op('False', 'False')
        'False'
        sage: sage.logic.logic.eval_and_op('False', 'True')
        'False'
        sage: sage.logic.logic.eval_and_op('True', 'False')
        'False'
        sage: sage.logic.logic.eval_and_op('True', 'True')
        'True'
    """
def eval_or_op(lval, rval):
    """
    Apply the 'or' operator to ``lval`` and ``rval``.

    INPUT:

    - ``lval`` -- string; this represents the value of the variable
      appearing to the left of the 'or' operator

    - ``rval`` -- string; this represents the value of the variable
      appearing to the right of the 'or' operator

    OUTPUT: string representing the result of applying 'or' to ``lval`` and ``rval``

    .. NOTE::

        This function is for internal use by the :class:`SymbolicLogic` class.

    TESTS::

        sage: sage.logic.logic.eval_or_op('False', 'False')
        'False'
        sage: sage.logic.logic.eval_or_op('False', 'True')
        'True'
        sage: sage.logic.logic.eval_or_op('True', 'False')
        'True'
        sage: sage.logic.logic.eval_or_op('True', 'True')
        'True'
    """
def eval_ifthen_op(lval, rval):
    """
    Apply the 'if then' operator to ``lval`` and ``rval``.

    INPUT:

    - ``lval`` -- string; this represents the value of the variable
      appearing to the left of the 'if then' operator

    - ``rval`` -- string; this represents the value of the variable
      appearing to the right of the 'if then' operator

    OUTPUT:

    A string representing the result of applying 'if then' to
    ``lval`` and ``rval``.

    .. NOTE::

        This function is for internal use by the :class:`SymbolicLogic` class.

    TESTS::

        sage: sage.logic.logic.eval_ifthen_op('False', 'False')
        'True'
        sage: sage.logic.logic.eval_ifthen_op('False', 'True')
        'True'
        sage: sage.logic.logic.eval_ifthen_op('True', 'False')
        'False'
        sage: sage.logic.logic.eval_ifthen_op('True', 'True')
        'True'
    """
def eval_iff_op(lval, rval):
    """
    Apply the 'if and only if' operator to ``lval`` and ``rval``.

    INPUT:

    - ``lval`` -- string; this represents the value of the variable
      appearing to the left of the 'if and only if' operator

    - ``rval`` -- string; this represents the value of the variable
      appearing to the right of the 'if and only if' operator

    OUTPUT:

    A string representing the result of applying 'if and only if'
    to ``lval`` and ``rval``.

    .. NOTE::

        This function is for internal use by the :class:`SymbolicLogic` class.

    TESTS::

        sage: sage.logic.logic.eval_iff_op('False', 'False')
        'True'
        sage: sage.logic.logic.eval_iff_op('False', 'True')
        'False'
        sage: sage.logic.logic.eval_iff_op('True', 'False')
        'False'
        sage: sage.logic.logic.eval_iff_op('True', 'True')
        'True'
    """
def tokenize(s, toks) -> None:
    '''
    Tokenize ``s`` and place the tokens of ``s`` in ``toks``.

    INPUT:

    - ``s`` -- string; this contains a boolean expression

    - ``toks`` -- list; this will be populated with the tokens of ``s``

    OUTPUT: none; the tokens of ``s`` are placed in ``toks``

    .. NOTE::

        This function is for internal use by the :class:`SymbolicLogic` class.

    EXAMPLES::

        sage: from sage.logic.logic import tokenize
        sage: toks = []
        sage: tokenize("(a&b)|c", toks)
        sage: toks
        [\'OPAREN\', \'a\', \'AND\', \'b\', \'CPAREN\', \'OR\', \'c\', \'CPAREN\']
    '''
