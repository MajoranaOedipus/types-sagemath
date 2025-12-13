from . import boolformula as boolformula, logicparser as logicparser
from _typeshed import Incomplete
from sage.misc.superseded import deprecated_function_alias as deprecated_function_alias

def formula(s):
    '''
    Return an instance of :class:`BooleanFormula`.

    INPUT:

    - ``s`` -- string that contains a logical expression

    OUTPUT: an instance of :class:`BooleanFormula`

    EXAMPLES:

    This example illustrates ways to create a boolean formula::

        sage: f = propcalc.formula("a&~b|c")
        sage: g = propcalc.formula("a^c<->b")
        sage: f&g|f
        ((a&~b|c)&(a^c<->b))|(a&~b|c)

    We now demonstrate some possible errors::

        sage: propcalc.formula("((a&b)")
        Traceback (most recent call last):
        ...
        SyntaxError: malformed statement
        sage: propcalc.formula("_a&b")
        Traceback (most recent call last):
        ...
        NameError: invalid variable name _a: identifiers must begin with a letter and contain only alphanumerics and underscores
    '''
def get_formulas(*statements):
    '''
    Convert statements and parse trees into instances of
    :class:`BooleanFormula`.

    INPUT:

    - ``*statements`` -- strings or lists; a list must be a
      full syntax parse tree of a formula, and a string must
      be a string representation of a formula

    OUTPUT: the converted formulas in a list

    EXAMPLES:

    This example illustrates converting strings into boolean formulas.

    ::

        sage: f = "a&(~c<->d)"
        sage: g = "d|~~b"
        sage: h = "~(a->c)<->(d|~c)"
        sage: propcalc.get_formulas(f, g, h)
        [a&(~c<->d), d|~~b, ~(a->c)<->(d|~c)]

    ::

        sage: A, B, C = propcalc.get_formulas("(a&b)->~c", "c", "~(a&b)")
        sage: A
        (a&b)->~c
        sage: B
        c
        sage: C
        ~(a&b)

    We can also convert parse trees into formulas.

    ::

        sage: t = [\'a\']
        sage: u = [\'~\', [\'|\', [\'&\', \'a\', \'b\'], [\'~\', \'c\']]]
        sage: v = "b->(~c<->d)"
        sage: formulas= propcalc.get_formulas(t, u, v)
        sage: formulas[0]
        a
        sage: formulas[1]
        ~((a&b)|~c)
        sage: formulas[2]
        b->(~c<->d)

    AUTHORS:

    - Paul Scurek (2013-08-12)
    '''
def consistent(*formulas):
    '''
    Determine if the formulas are logically consistent.

    INPUT:

    - ``*formulas`` -- instances of :class:`BooleanFormula`

    OUTPUT: a boolean value to be determined as follows:

    - ``True`` -- if the formulas are logically consistent

    - ``False`` -- if the formulas are not logically consistent

    EXAMPLES:

    This example illustrates determining if formulas are logically consistent.

    ::

        sage: f, g, h, i = propcalc.get_formulas("a<->b", "~b->~c", "d|g", "c&a")
        sage: propcalc.consistent(f, g, h, i)
        True

    ::

        sage: j, k, l, m = propcalc.get_formulas("a<->b", "~b->~c", "d|g", "c&~a")
        sage: propcalc.consistent(j, k ,l, m)
        False

    AUTHORS:

    - Paul Scurek (2013-08-12)
    '''

valid_consequence: Incomplete
