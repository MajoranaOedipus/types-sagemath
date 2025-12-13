from . import booleval as booleval, logicparser as logicparser, logictable as logictable
from _typeshed import Incomplete
from sage.misc.flatten import flatten as flatten

latex_operators: Incomplete

class BooleanFormula:
    """
    Boolean formulas.

    INPUT:

    - ``self`` -- calling object

    - ``exp`` -- string; this contains the boolean expression
      to be manipulated

    - ``tree`` -- list; this contains the parse tree of the expression

    - ``vo`` -- list; this contains the variables in the expression, in the
      order that they appear; each variable only occurs once in the list
    """
    def __init__(self, exp, tree, vo) -> None:
        '''
        Initialize the data fields.

        EXAMPLES:

        This example illustrates the creation of a statement::

            sage: import sage.logic.propcalc as propcalc
            sage: s = propcalc.formula("a&b|~(c|a)")
            sage: s
            a&b|~(c|a)
        '''
    def polish_notation(self):
        '''
        Convert the calling boolean formula into polish notation.

        OUTPUT: string representation of the formula in polish notation

        EXAMPLES:

        This example illustrates converting a formula to polish notation::

            sage: import sage.logic.propcalc as propcalc
            sage: f = propcalc.formula("~~a|(c->b)")
            sage: f.polish_notation()
            \'|~~a->cb\'

            sage: g = propcalc.formula("(a|~b)->c")
            sage: g.polish_notation()
            \'->|a~bc\'

        AUTHORS:

        - Paul Scurek (2013-08-03)
        '''
    def tree(self):
        '''
        Return the parse tree of this boolean expression.

        OUTPUT: the parse tree as a nested list

        EXAMPLES:

        This example illustrates how to find the parse tree of a boolean
        formula::

            sage: import sage.logic.propcalc as propcalc
            sage: s = propcalc.formula("man -> monkey & human")
            sage: s.tree()
            [\'->\', \'man\', [\'&\', \'monkey\', \'human\']]

        ::

            sage: f = propcalc.formula("a & ((~b | c) ^ a -> c) <-> ~b")
            sage: f.tree()
            [\'<->\',
             [\'&\', \'a\', [\'->\', [\'^\', [\'|\', [\'~\', \'b\', None], \'c\'], \'a\'], \'c\']],
             [\'~\', \'b\', None]]

        .. NOTE::

            This function is used by other functions in the logic module
            that perform semantic operations on a boolean formula.
        '''
    def full_tree(self):
        '''
        Return a full syntax parse tree of the calling formula.

        OUTPUT: the full syntax parse tree as a nested list

        EXAMPLES:

        This example shows how to find the full syntax parse tree
        of a formula::

            sage: import sage.logic.propcalc as propcalc
            sage: s = propcalc.formula("a->(b&c)")
            sage: s.full_tree()
            [\'->\', \'a\', [\'&\', \'b\', \'c\']]

            sage: t = propcalc.formula("a & ((~b | c) ^ a -> c) <-> ~b")
            sage: t.full_tree()
            [\'<->\', [\'&\', \'a\', [\'->\', [\'^\', [\'|\', [\'~\', \'b\'], \'c\'], \'a\'], \'c\']], [\'~\', \'b\']]

            sage: f = propcalc.formula("~~(a&~b)")
            sage: f.full_tree()
            [\'~\', [\'~\', [\'&\', \'a\', [\'~\', \'b\']]]]

        .. NOTE::

            This function is used by other functions in the logic module
            that perform syntactic operations on a boolean formula.

        AUTHORS:

        - Paul Scurek (2013-08-03)
        '''
    def __or__(self, other):
        '''
        Overload the ``|`` operator to \'or\' two statements together.

        INPUT:

        - ``other`` -- boolean formula; this is the statement
          on the right side of the operator

        OUTPUT:

        A boolean formula of the form ``self | other``.

        EXAMPLES:

        This example illustrates combining two formulas with ``|``::

            sage: import sage.logic.propcalc as propcalc
            sage: s = propcalc.formula("a&b")
            sage: f = propcalc.formula("c^d")
            sage: s | f
            (a&b)|(c^d)
        '''
    def __and__(self, other):
        '''
        Overload the ``&`` operator to \'and\' two statements together.

        INPUT:

        - ``other`` -- boolean formula; this is the formula on
          the right side of the operator

        OUTPUT: a boolean formula of the form ``self & other``

        EXAMPLES:

        This example shows how to combine two formulas with ``&``::

            sage: import sage.logic.propcalc as propcalc
            sage: s = propcalc.formula("a&b")
            sage: f = propcalc.formula("c^d")
            sage: s & f
            (a&b)&(c^d)
        '''
    def __xor__(self, other):
        '''
        Overload the ``^`` operator to \'xor\' two statements together.

        INPUT:

        - ``other`` -- boolean formula; this is the formula on
          the right side of the operator

        OUTPUT: a boolean formula of the form ``self ^ other``

        EXAMPLES:

        This example illustrates how to combine two formulas with ``^``::

            sage: import sage.logic.propcalc as propcalc
            sage: s = propcalc.formula("a&b")
            sage: f = propcalc.formula("c^d")
            sage: s ^ f
            (a&b)^(c^d)
        '''
    def __pow__(self, other):
        '''
        Overload the ``^`` operator to \'xor\' two statements together.

        INPUT:

        - ``other`` -- boolean formula; this is the formula on
          the right side of the operator

        OUTPUT: a boolean formula of the form ``self ^ other``

        EXAMPLES:

        This example shows how to combine two formulas with ``^``::

            sage: import sage.logic.propcalc as propcalc
            sage: s = propcalc.formula("a&b")
            sage: f = propcalc.formula("c^d")
            sage: s ^ f
            (a&b)^(c^d)

        .. TODO::

            This function seems to be identical to ``__xor__``.
            Thus, this function should be replaced with ``__xor__`` everywhere
            that it appears in the logic module. Then it can be deleted
            altogether.
        '''
    def __invert__(self):
        '''
        Overload the ``~`` operator to \'not\' a statement.

        OUTPUT: a boolean formula of the form ``~self``

        EXAMPLES:

        This example shows how to negate a boolean formula::

            sage: import sage.logic.propcalc as propcalc
            sage: s = propcalc.formula("a&b")
            sage: ~s
            ~(a&b)
        '''
    def ifthen(self, other):
        '''
        Combine two formulas with the ``->`` operator.

        INPUT:

        - ``other`` -- boolean formula; this is the formula
          on the right side of the operator

        OUTPUT:

        A boolean formula of the form ``self -> other``.

        EXAMPLES:

        This example illustrates how to combine two formulas with \'->\'::

            sage: import sage.logic.propcalc as propcalc
            sage: s = propcalc.formula("a&b")
            sage: f = propcalc.formula("c^d")
            sage: s.ifthen(f)
            (a&b)->(c^d)
        '''
    def iff(self, other):
        '''
        Combine two formulas with the ``<->`` operator.

        INPUT:

        - ``other`` -- boolean formula; this is the formula
          on the right side of the operator

        OUTPUT:

        A boolean formula of the form ``self <-> other``.

        EXAMPLES:

        This example illustrates how to combine two formulas with \'<->\'::

            sage: import sage.logic.propcalc as propcalc
            sage: s = propcalc.formula("a&b")
            sage: f = propcalc.formula("c^d")
            sage: s.iff(f)
            (a&b)<->(c^d)
        '''
    def __eq__(self, other):
        '''
        Overload the ``==`` operator to determine logical equivalence.

        INPUT:

        - ``other`` -- boolean formula; this is the formula
          on the right side of the comparator

        OUTPUT: a boolean value to be determined as follows:

        - ``True`` if ``self`` and ``other`` are logically equivalent

        - ``False`` if ``self`` and ``other`` are not logically equivalent

        EXAMPLES:

        This example shows how to determine logical equivalence::

            sage: import sage.logic.propcalc as propcalc
            sage: f = propcalc.formula("(a|b)&c")
            sage: g = propcalc.formula("c&(b|a)")
            sage: f == g
            True

        ::

            sage: g = propcalc.formula("a|b&c")
            sage: f == g
            False
        '''
    def truthtable(self, start: int = 0, end: int = -1):
        '''
        Return a truth table for the calling formula.

        INPUT:

        - ``start`` -- (default: 0) an integer; this is the first
          row of the truth table to be created

        - ``end`` -- (default: -1) an integer; this is the last
          row of the truth table to be created

        OUTPUT: the truth table as a 2-D array

        EXAMPLES:

        This example illustrates the creation of a truth table::

            sage: import sage.logic.propcalc as propcalc
            sage: s = propcalc.formula("a&b|~(c|a)")
            sage: s.truthtable()
            a      b      c      value
            False  False  False  True
            False  False  True   False
            False  True   False  True
            False  True   True   False
            True   False  False  False
            True   False  True   False
            True   True   False  True
            True   True   True   True

        We can now create a truthtable of rows 1 to 4, inclusive::

            sage: s.truthtable(1, 5)
            a      b      c      value
            False  False  True   False
            False  True   False  True
            False  True   True   False
            True   False  False  False

        .. NOTE::

            Each row of the table corresponds to a binary number, with
            each variable associated to a column of the number, and taking on
            a true value if that column has a value of 1.  Please see the
            logictable module for details.  The function returns a table that
            start inclusive and end exclusive so ``truthtable(0, 2)`` will
            include row 0, but not row 2.

            When sent with no start or end parameters, this is an
            exponential time function requiring `O(2^n)` time, where
            `n` is the number of variables in the expression.
        '''
    def evaluate(self, var_values):
        '''
        Evaluate a formula for the given input values.

        INPUT:

        - ``var_values`` -- dictionary; this contains the
          pairs of variables and their boolean values

        OUTPUT: the result of the evaluation as a boolean

        EXAMPLES:

        This example illustrates the evaluation of a boolean formula::

            sage: import sage.logic.propcalc as propcalc
            sage: f = propcalc.formula("a&b|c")
            sage: f.evaluate({\'a\':False, \'b\':False, \'c\':True})
            True
            sage: f.evaluate({\'a\':True, \'b\':False, \'c\':False})
            False
        '''
    def is_satisfiable(self):
        '''
        Determine if the formula is ``True`` for some assignment of values.

        OUTPUT: a boolean value to be determined as follows:

        - ``True`` if there is an assignment of values that makes the
          formula ``True``.

        - ``False`` if the formula cannot be made ``True`` by any assignment
          of values.

        EXAMPLES:

        This example illustrates how to check a formula for satisfiability::

            sage: import sage.logic.propcalc as propcalc
            sage: f = propcalc.formula("a|b")
            sage: f.is_satisfiable()
            True

            sage: g = f & (~f)
            sage: g.is_satisfiable()
            False
        '''
    def is_tautology(self):
        '''
        Determine if the formula is always ``True``.

        OUTPUT: a boolean value to be determined as follows:

        - ``True`` if the formula is a tautology.

        - ``False`` if the formula is not a tautology.

        EXAMPLES:

        This example illustrates how to check if a formula is a tautology::

            sage: import sage.logic.propcalc as propcalc
            sage: f = propcalc.formula("a|~a")
            sage: f.is_tautology()
            True

            sage: f = propcalc.formula("a&~a")
            sage: f.is_tautology()
            False

            sage: f = propcalc.formula("a&b")
            sage: f.is_tautology()
            False
        '''
    def is_contradiction(self):
        '''
        Determine if the formula is always ``False``.

        OUTPUT: a boolean value to be determined as follows:

        - ``True`` if the formula is a contradiction.

        - ``False`` if the formula is not a contradiction.

        EXAMPLES:

        This example illustrates how to check if a formula is a contradiction.

        ::

            sage: import sage.logic.propcalc as propcalc
            sage: f = propcalc.formula("a&~a")
            sage: f.is_contradiction()
            True

            sage: f = propcalc.formula("a|~a")
            sage: f.is_contradiction()
            False

            sage: f = propcalc.formula("a|b")
            sage: f.is_contradiction()
            False
        '''
    def is_consequence(self, *hypotheses):
        '''
        Determine if ``self`` (the desired conclusion) is a logical consequence of the
        hypotheses. The function call ``is_consequence(conclusion, *hypotheses)`` is a
        synonym for ``conclusion.is_consequence(*hypotheses)``.

        INPUT:

        - ``*hypotheses`` -- instances of :class:`BooleanFormula`

        OUTPUT: a boolean value to be determined as follows:

        - ``True`` -- if ``self`` (the desired conclusion) is a logical consequence
          of the set of hypotheses

        - ``False`` -- if ``self`` (the desired conclusion) is not a logical consequence
          of the set of hypotheses

        EXAMPLES::

            sage: from sage.logic.propcalc import formula
            sage: formula("a | b").is_consequence(formula("b"))
            True
            sage: formula("a & b").is_consequence(formula("b"))
            False
            sage: formula("b").is_consequence(formula("a"), formula("a -> b"))
            True
            sage: formula("b -> a").is_consequence(formula("a -> b"))
            False
            sage: formula("~b -> ~a").is_consequence(formula("a -> b"))
            True

        ::

            sage: f, g, h = propcalc.get_formulas("a & ~b", "c -> b", "c | e")
            sage: propcalc.formula("a & e").is_consequence(f, g, h)
            True
            sage: i = propcalc.formula("a & ~e")
            sage: i.is_consequence(f, g, h)
            False
            sage: from sage.logic.boolformula import is_consequence
            sage: is_consequence(i, f, g, h)
            False
            sage: is_consequence(propcalc.formula("((p <-> q) & r) -> ~c"), f, g, h)
            True

        Only a tautology is a logical consequence of an empty set of formulas::

            sage: propcalc.formula("a | ~a").is_consequence()
            True
            sage: propcalc.formula("a | b").is_consequence()
            False

        TESTS:

        Arguments must be instances of :class:`BooleanFormula` (not strings, for example)::

            sage: propcalc.formula("a | b").is_consequence("a | b")
            Traceback (most recent call last):
            ...
            TypeError: is_consequence only takes instances of BooleanFormula() class as input

        AUTHORS:

        - Paul Scurek (2013-08-12)
        '''
    def implies(self, other):
        '''
        Determine if calling formula implies other formula.

        INPUT:

        - ``self`` -- calling object

        - ``other`` -- instance of :class:`BooleanFormula`

        OUTPUT: a boolean value to be determined as follows:

        - ``True`` -- if ``self`` implies ``other``

        - ``False`` -- if ``self does not imply ``other``

        EXAMPLES:

        This example illustrates determining if one formula implies another::

            sage: import sage.logic.propcalc as propcalc
            sage: f = propcalc.formula("a<->b")
            sage: g = propcalc.formula("b->a")
            sage: f.implies(g)
            True

        ::

            sage: h = propcalc.formula("a->(a|~b)")
            sage: i = propcalc.formula("a")
            sage: h.implies(i)
            False

        AUTHORS:

        - Paul Scurek (2013-08-08)
        '''
    def equivalent(self, other):
        '''
        Determine if two formulas are semantically equivalent.

        INPUT:

        - ``self`` -- calling object

        - ``other`` -- instance of BooleanFormula class

        OUTPUT: a boolean value to be determined as follows:

        ``True`` -- if the two formulas are logically equivalent

        ``False`` -- if the two formulas are not logically equivalent

        EXAMPLES:

        This example shows how to check for logical equivalence::

            sage: import sage.logic.propcalc as propcalc
            sage: f = propcalc.formula("(a|b)&c")
            sage: g = propcalc.formula("c&(a|b)")
            sage: f.equivalent(g)
            True

            sage: g = propcalc.formula("a|b&c")
            sage: f.equivalent(g)
            False
        '''
    def convert_cnf_table(self) -> None:
        '''
        Convert boolean formula to conjunctive normal form.

        OUTPUT: an instance of :class:`BooleanFormula` in conjunctive normal form

        EXAMPLES:

        This example illustrates how to convert a formula to cnf::

            sage: import sage.logic.propcalc as propcalc
            sage: s = propcalc.formula("a ^ b <-> c")
            sage: s.convert_cnf()
            sage: s
            (a|b|~c)&(a|~b|c)&(~a|b|c)&(~a|~b|~c)

        We now show that :meth:`convert_cnf` and :meth:`convert_cnf_table`
        are aliases::

            sage: t = propcalc.formula("a ^ b <-> c")
            sage: t.convert_cnf_table(); t
            (a|b|~c)&(a|~b|c)&(~a|b|c)&(~a|~b|~c)
            sage: t == s
            True

        .. NOTE::

            This method creates the cnf parse tree by examining the logic
            table of the formula.  Creating the table requires `O(2^n)` time
            where `n` is the number of variables in the formula.
        '''
    convert_cnf = convert_cnf_table
    def convert_cnf_recur(self) -> None:
        '''
        Convert boolean formula to conjunctive normal form.

        OUTPUT: an instance of :class:`BooleanFormula` in conjunctive normal form

        EXAMPLES:

        This example hows how to convert a formula to conjunctive normal form::

            sage: import sage.logic.propcalc as propcalc
            sage: s = propcalc.formula("a^b<->c")
            sage: s.convert_cnf_recur()
            sage: s
            (~a|a|c)&(~b|a|c)&(~a|b|c)&(~b|b|c)&(~c|a|b)&(~c|~a|~b)

        .. NOTE::

            This function works by applying a set of rules that are
            guaranteed to convert the formula.  Worst case the converted
            expression has an `O(2^n)` increase in size (and time as well), but
            if the formula is already in CNF (or close to) it is only `O(n)`.

            This function can require an exponential blow up in space from the
            original expression.  This in turn can require large amounts of
            time. Unless a formula is already in (or close to) being in cnf
            :meth:`convert_cnf()` is typically preferred, but results can vary.
        '''
    def satformat(self):
        '''
        Return the satformat representation of a boolean formula.

        OUTPUT: the satformat of the formula as a string

        EXAMPLES:

        This example illustrates how to find the satformat of a formula::

            sage: import sage.logic.propcalc as propcalc
            sage: f = propcalc.formula("a&((b|c)^a->c)<->b")
            sage: f.convert_cnf()
            sage: f
            (a|~b|c)&(a|~b|~c)&(~a|b|~c)
            sage: f.satformat()
            \'p cnf 3 0\\n1 -2 3 0 1 -2 -3 \\n0 -1 2 -3\'

        .. NOTE::

            See www.cs.ubc.ca/~hoos/SATLIB/Benchmarks/SAT/satformat.ps for a
            description of satformat.

            If the instance of boolean formula has not been converted to
            CNF form by a call to :meth:`convert_cnf()` or
            :meth:`convert_cnf_recur()`, then :meth:`satformat()` will call
            :meth:`convert_cnf()`. Please see the notes for
            :meth:`convert_cnf()` and :meth:`convert_cnf_recur()` for
            performance issues.
        '''
    def convert_opt(self, tree):
        '''
        Convert a parse tree to the tuple form used by :meth:`bool_opt()`.

        INPUT:

        - ``tree`` -- list; this is a branch of a
          parse tree and can only contain the \'&\', \'|\'
          and \'~\' operators along with variables

        OUTPUT: a 3-tuple

        EXAMPLES:

        This example illustrates the conversion of a formula into its
        corresponding tuple::

            sage: import sage.logic.propcalc as propcalc, sage.logic.logicparser as logicparser
            sage: s = propcalc.formula("a&(b|~c)")
            sage: tree = [\'&\', \'a\', [\'|\', \'b\', [\'~\', \'c\', None]]]
            sage: logicparser.apply_func(tree, s.convert_opt)
            (\'and\', (\'prop\', \'a\'), (\'or\', (\'prop\', \'b\'), (\'not\', (\'prop\', \'c\'))))

        .. NOTE::

            This function only works on one branch of the parse tree. To
            apply the function to every branch of a parse tree, pass the
            function as an argument in
            :func:`~sage.logic.logicparser.apply_func()` in
            :mod:`~sage.logic.logicparser`.
        '''
    def add_statement(self, other, op):
        '''
        Combine two formulas with the given operator.

        INPUT:

        - ``other`` -- instance of :class:`BooleanFormula`; this
          is the formula on the right of the operator

        - ``op`` -- string; this is the operator used to
          combine the two formulas

        OUTPUT: the result as an instance of :class:`BooleanFormula`

        EXAMPLES:

        This example shows how to create a new formula from two others::

            sage: import sage.logic.propcalc as propcalc
            sage: s = propcalc.formula("a&b")
            sage: f = propcalc.formula("c^d")
            sage: s.add_statement(f, \'|\')
            (a&b)|(c^d)

            sage: s.add_statement(f, \'->\')
            (a&b)->(c^d)
        '''
    def get_bit(self, x, c):
        '''
        Determine if bit ``c`` of the number ``x`` is 1.

        INPUT:

        - ``x`` -- integer; this is the number from
          which to take the bit

        - ``c`` -- integer; this is the but number to
          be taken, where 0 is the low order bit

        OUTPUT: a boolean to be determined as follows:

        - ``True`` if bit ``c`` of ``x`` is 1.

        - ``False`` if bit c of x is not 1.

        EXAMPLES:

        This example illustrates the use of :meth:`get_bit`::

            sage: import sage.logic.propcalc as propcalc
            sage: s = propcalc.formula("a&b")
            sage: s.get_bit(2, 1)
            True
            sage: s.get_bit(8, 0)
            False

        It is not an error to have a bit out of range::

            sage: s.get_bit(64, 7)
            False

        Nor is it an error to use a negative number::

            sage: s.get_bit(-1, 3)
            False
            sage: s.get_bit(64, -1)
            True
            sage: s.get_bit(64, -2)
            False

        .. NOTE::

            The 0 bit is the low order bit.  Errors should be handled
            gracefully by a return of ``False``, and negative numbers ``x``
            always return ``False`` while a negative ``c`` will index from the
            high order bit.
        '''
    def reduce_op(self, tree):
        '''
        Convert if-and-only-if, if-then, and xor operations to operations
        only involving and/or operations.

        INPUT:

        - ``tree`` -- list; this represents a branch
          of a parse tree

        OUTPUT:

        A new list with no \'^\', \'->\', or \'<->\' as first element of list.

        EXAMPLES:

        This example illustrates the use of :meth:`reduce_op` with
        :func:`apply_func`::

            sage: import sage.logic.propcalc as propcalc, sage.logic.logicparser as logicparser
            sage: s = propcalc.formula("a->b^c")
            sage: tree = [\'->\', \'a\', [\'^\', \'b\', \'c\']]
            sage: logicparser.apply_func(tree, s.reduce_op)
            [\'|\', [\'~\', \'a\', None], [\'&\', [\'|\', \'b\', \'c\'], [\'~\', [\'&\', \'b\', \'c\'], None]]]

        .. NOTE::

            This function only operates on a single branch of a parse tree.
            To apply the function to an entire parse tree, pass the function
            as an argument to :func:`~sage.logic.logicparser.apply_func()`
            in :mod:`~sage.logic.logicparser`.
        '''
    def dist_not(self, tree):
        '''
        Distribute \'~\' operators over \'&\' and \'|\' operators.

        INPUT:

        - ``tree`` a list; this represents a branch
          of a parse tree

        OUTPUT: a new list

        EXAMPLES:

        This example illustrates the distribution of \'~\' over \'&\'::

            sage: import sage.logic.propcalc as propcalc, sage.logic.logicparser as logicparser
            sage: s = propcalc.formula("~(a&b)")
            sage: tree = [\'~\', [\'&\', \'a\', \'b\'], None]
            sage: logicparser.apply_func(tree, s.dist_not) #long time
            [\'|\', [\'~\', \'a\', None], [\'~\', \'b\', None]]

        .. NOTE::

            This function only operates on a single branch of a parse tree.
            To apply the function to an entire parse tree, pass the function
            as an argument to :func:`~sage.logic.logicparser.apply_func()`
            in :mod:`~sage.logic.logicparser`.
        '''
    def dist_ors(self, tree):
        '''
        Distribute \'|\' over \'&\'.

        INPUT:

        - ``tree`` -- list; this represents a branch of
          a parse tree

        OUTPUT: a new list

        EXAMPLES:

        This example illustrates the distribution of \'|\' over \'&\'::

            sage: import sage.logic.propcalc as propcalc, sage.logic.logicparser as logicparser
            sage: s = propcalc.formula("(a&b)|(a&c)")
            sage: tree = [\'|\', [\'&\', \'a\', \'b\'], [\'&\', \'a\', \'c\']]
            sage: logicparser.apply_func(tree, s.dist_ors) #long time
            [\'&\', [\'&\', [\'|\', \'a\', \'a\'], [\'|\', \'b\', \'a\']], [\'&\', [\'|\', \'a\', \'c\'], [\'|\', \'b\', \'c\']]]

        .. NOTE::

            This function only operates on a single branch of a parse tree.
            To apply the function to an entire parse tree, pass the function
            as an argument to :func:`~sage.logic.logicparser.apply_func()`
            in :mod:`~sage.logic.logicparser`.
        '''
    def to_infix(self, tree):
        '''
        Convert a parse tree from prefix to infix form.

        INPUT:

        - ``tree`` -- list; this represents a branch
          of a parse tree

        OUTPUT: a new list

        EXAMPLES:

        This example shows how to convert a parse tree from prefix to
        infix form::

            sage: import sage.logic.propcalc as propcalc, sage.logic.logicparser as logicparser
            sage: s = propcalc.formula("(a&b)|(a&c)")
            sage: tree = [\'|\', [\'&\', \'a\', \'b\'], [\'&\', \'a\', \'c\']]
            sage: logicparser.apply_func(tree, s.to_infix)
            [[\'a\', \'&\', \'b\'], \'|\', [\'a\', \'&\', \'c\']]

        .. NOTE::

            This function only operates on a single branch of a parse tree.
            To apply the function to an entire parse tree, pass the function
            as an argument to :func:`~sage.logic.logicparser.apply_func()`
            in :mod:`~sage.logic.logicparser`.
        '''
    def convert_expression(self) -> None:
        '''
        Convert the string representation of a formula to conjunctive
        normal form.

        EXAMPLES::

            sage: import sage.logic.propcalc as propcalc
            sage: s = propcalc.formula("a^b<->c")
            sage: s.convert_expression(); s
            a^b<->c
        '''
    def get_next_op(self, str):
        '''
        Return the next operator in a string.

        INPUT:

        - ``str`` -- string; this contains a logical
          expression

        OUTPUT: the next operator as a string

        EXAMPLES:

        This example illustrates how to find the next operator in a formula::

            sage: import sage.logic.propcalc as propcalc
            sage: s = propcalc.formula("f&p")
            sage: s.get_next_op("abra|cadabra")
            \'|\'

        .. NOTE::

            The parameter ``str`` is not necessarily the string
            representation of the calling object.
        '''
    def length(self):
        '''
        Return the length of ``self``.

        OUTPUT:

        The length of the Boolean formula. This is the number of operators plus
        the number of variables (counting multiplicity). Parentheses are ignored.

        EXAMPLES::

            sage: import sage.logic.propcalc as propcalc
            sage: s = propcalc.formula("a")
            sage: s.length()
            1
            sage: s = propcalc.formula("(a)")
            sage: s.length()
            1
            sage: s = propcalc.formula("~a")
            sage: s.length()
            2
            sage: s = propcalc.formula("a -> b")
            sage: s.length()
            3
            sage: s = propcalc.formula("alpha -> beta")
            sage: s.length()
            3
            sage: s = propcalc.formula("a -> a")
            sage: s.length()
            3
            sage: s = propcalc.formula("~(a -> b)")
            sage: s.length()
            4
            sage: s = propcalc.formula("((a&b)|(a&c))->~d")
            sage: s.length()
            10

        TESTS::

            sage: s = propcalc.formula("(((alpha) -> ((beta))))")
            sage: s.length()
            3
        '''
    __len__ = length

is_consequence: Incomplete
