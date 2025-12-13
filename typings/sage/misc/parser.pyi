import _cython_3_2_1
from typing import Any, ClassVar, overload

enum_map: dict
foo: _cython_3_2_1.cython_function_or_method
function_map: dict
token_to_str: _cython_3_2_1.cython_function_or_method

class LookupNameMaker:
    """LookupNameMaker(names, fallback=None)"""
    def __init__(self, names, fallback=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 1054)

                This class wraps a dictionary as a callable for use in creating names.
                It takes a dictionary of names, and an (optional) callable to use
                when the given name is not found in the dictionary.

                EXAMPLES::

                    sage: # needs sage.symbolic
                    sage: from sage.misc.parser import LookupNameMaker
                    sage: maker = LookupNameMaker({'pi': pi}, var)
                    sage: maker('pi')
                    pi
                    sage: maker('pi') is pi
                    True
                    sage: maker('a')
                    a
        """
    def set_names(self, new_names) -> Any:
        """LookupNameMaker.set_names(self, new_names)

        File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 1075)

        TESTS::

            sage: from sage.misc.parser import LookupNameMaker
            sage: maker = LookupNameMaker({}, str)
            sage: maker.set_names({'a': x})                                             # needs sage.symbolic
            sage: maker('a') is x                                                       # needs sage.symbolic
            True"""
    def __call__(self, name) -> Any:
        """LookupNameMaker.__call__(self, name)

        File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 1087)

        TESTS::

            sage: # needs sage.symbolic
            sage: from sage.misc.parser import LookupNameMaker
            sage: maker = LookupNameMaker({'a': x}, str)
            sage: maker('a')
            x
            sage: maker('a') is x
            True
            sage: maker('b')
            'b'"""

class Parser:
    """Parser(make_int=int, make_float=float, make_var=str, make_function={}, bool implicit_multiplication=True)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, make_int=..., make_float=..., make_var=..., make_function=..., boolimplicit_multiplication=...) -> Any:
        '''File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 454)

                Create a symbolic expression parser.

                INPUT:

                - ``make_int`` -- callable object to construct integers from strings (default: int)
                - ``make_float`` -- callable object to construct real numbers from strings (default: float)
                - ``make_var`` -- callable object to construct variables from strings (default: str)
                  this may also be a dictionary of variable names
                - ``make_function`` -- callable object to construct callable functions from strings
                  this may also be a dictionary
                - ``implicit_multiplication`` -- whether or not to accept implicit multiplication

                OUTPUT:

                The evaluated expression tree given by the string, where the above
                functions are used to create the leaves of this tree.

                EXAMPLES::

                    sage: from sage.misc.parser import Parser
                    sage: p = Parser()
                    sage: p.parse("1+2")
                    3
                    sage: p.parse("1+2 == 3")
                    True

                    sage: p = Parser(make_var=var)                                              # needs sage.symbolic
                    sage: p.parse("a*b^c - 3a")                                                 # needs sage.symbolic
                    a*b^c - 3*a

                    sage: R.<x> = QQ[]
                    sage: p = Parser(make_var={\'x\': x})
                    sage: p.parse("(x+1)^5-x")
                    x^5 + 5*x^4 + 10*x^3 + 10*x^2 + 4*x + 1
                    sage: p.parse("(x+1)^5-x").parent() is R
                    True

                    sage: p = Parser(make_float=RR, make_var=var,                               # needs sage.symbolic
                    ....:            make_function={\'foo\': (lambda x: x*x+x)})
                    sage: p.parse("1.5 + foo(b)")                                               # needs sage.symbolic
                    b^2 + b + 1.50000000000000
                    sage: p.parse("1.9").parent()                                               # needs sage.symbolic
                    Real Field with 53 bits of precision
        '''
    def p_arg(self, *args, **kwargs):
        '''Parser.p_arg(self, Tokenizer tokens)

        File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 1006)

         Return an ``expr``, or a ``(name, expr)`` tuple corresponding to a
         single function call argument.

         EXAMPLES:

         Parsing a normal expression::

             sage: from sage.misc.parser import Parser, Tokenizer
             sage: p = Parser(make_var=var)                                              # needs sage.symbolic
             sage: p.p_arg(Tokenizer("a+b"))                                             # needs sage.symbolic
             a + b

        A keyword expression argument::

             sage: from sage.misc.parser import Parser, Tokenizer
             sage: p = Parser(make_var=var)                                              # needs sage.symbolic
             sage: p.p_arg(Tokenizer("val=a+b"))                                         # needs sage.symbolic
             (\'val\', a + b)

         A lone list::

             sage: from sage.misc.parser import Parser, Tokenizer
             sage: p = Parser(make_var=var)                                              # needs sage.symbolic
             sage: p.p_arg(Tokenizer("[x]"))                                             # needs sage.symbolic
             [x]
 '''
    def p_args(self, Tokenizertokens) -> Any:
        '''Parser.p_args(self, Tokenizer tokens)

        File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 976)

        Return a ``list, dict`` pair.

        EXAMPLES::

            sage: from sage.misc.parser import Parser, Tokenizer
            sage: p = Parser()
            sage: p.p_args(Tokenizer("1,2,a=3"))
            ([1, 2], {\'a\': 3})
            sage: p.p_args(Tokenizer("1, 2, a = 1+5^2"))
            ([1, 2], {\'a\': 26})'''
    def p_atom(self, Tokenizertokens) -> Any:
        '''Parser.p_atom(self, Tokenizer tokens)

        File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 920)

        Parse an atom. This is either a parenthesized expression, a function call, or a literal name/int/float.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: from sage.misc.parser import Parser, Tokenizer
            sage: p = Parser(make_var=var, make_function={\'sin\': sin})
            sage: p.p_atom(Tokenizer("1"))
            1
            sage: p.p_atom(Tokenizer("12"))
            12
            sage: p.p_atom(Tokenizer("12.5"))
            12.5
            sage: p.p_atom(Tokenizer("(1+a)"))
            a + 1
            sage: p.p_atom(Tokenizer("(1+a)^2"))
            a + 1
            sage: p.p_atom(Tokenizer("sin(1+a)"))
            sin(a + 1)
            sage: p = Parser(make_var=var,
            ....:            make_function={\'foo\': sage.misc.parser.foo})
            sage: p.p_atom(Tokenizer("foo(a, b, key=value)"))
            ((a, b), {\'key\': value})
            sage: p.p_atom(Tokenizer("foo()"))
            ((), {})'''
    def p_eqn(self, Tokenizertokens) -> Any:
        '''Parser.p_eqn(self, Tokenizer tokens)

        File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 727)

        Parse an equation or expression.

        This is the top-level node called by the \\code{parse} function.

        EXAMPLES::

            sage: from sage.misc.parser import Parser, Tokenizer
            sage: p = Parser(make_var=var)                                              # needs sage.symbolic
            sage: p.p_eqn(Tokenizer("1+a"))                                             # needs sage.symbolic
            a + 1

            sage: # needs sage.symbolic
            sage: p.p_eqn(Tokenizer("a == b"))
            a == b
            sage: p.p_eqn(Tokenizer("a < b"))
            a < b
            sage: p.p_eqn(Tokenizer("a > b"))
            a > b
            sage: p.p_eqn(Tokenizer("a <= b"))
            a <= b
            sage: p.p_eqn(Tokenizer("a >= b"))
            a >= b
            sage: p.p_eqn(Tokenizer("a != b"))
            a != b'''
    def p_expr(self, Tokenizertokens) -> Any:
        '''Parser.p_expr(self, Tokenizer tokens)

        File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 773)

        Parse a list of one or more terms.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: from sage.misc.parser import Parser, Tokenizer
            sage: p = Parser(make_var=var)
            sage: p.p_expr(Tokenizer("a+b"))
            a + b
            sage: p.p_expr(Tokenizer("a"))
            a
            sage: p.p_expr(Tokenizer("a - b + 4*c - d^2"))
            -d^2 + a - b + 4*c
            sage: p.p_expr(Tokenizer("a - -3"))
            a + 3
            sage: p.p_expr(Tokenizer("a + 1 == b"))
            a + 1'''
    def p_factor(self, Tokenizertokens) -> Any:
        '''Parser.p_factor(self, Tokenizer tokens)

        File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 849)

        Parse a single factor, which consists of any number of unary +/-
        and a power.

        EXAMPLES::

            sage: from sage.misc.parser import Parser, Tokenizer
            sage: R.<t> = ZZ[[\'t\']]
            sage: p = Parser(make_var={\'t\': t})
            sage: p.p_factor(Tokenizer("- -t"))
            t
            sage: p.p_factor(Tokenizer("- + - -t^2"))
            -t^2
            sage: p.p_factor(Tokenizer("t^11 * x"))
            t^11'''
    def p_list(self, Tokenizertokens) -> Any:
        '''Parser.p_list(self, Tokenizer tokens)

        File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 670)

        Parse a list of items.

        EXAMPLES::

            sage: from sage.misc.parser import Parser, Tokenizer
            sage: p = Parser(make_var=var)                                              # needs sage.symbolic
            sage: p.p_list(Tokenizer("[1+2, 1e3]"))                                     # needs sage.symbolic
            [3, 1000.0]
            sage: p.p_list(Tokenizer("[]"))                                             # needs sage.symbolic
            []'''
    def p_matrix(self, Tokenizertokens) -> Any:
        '''Parser.p_matrix(self, Tokenizer tokens)

        File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 597)

        Parse a matrix.

        EXAMPLES::

            sage: from sage.misc.parser import Parser, Tokenizer
            sage: p = Parser(make_var=var)                                              # needs sage.symbolic
            sage: p.p_matrix(Tokenizer("([a,0],[0,a])"))                                # needs sage.symbolic
            [a 0]
            [0 a]'''
    def p_power(self, Tokenizertokens) -> Any:
        '''Parser.p_power(self, Tokenizer tokens)

        File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 876)

        Parses a power. Note that exponentiation groups right to left.

        EXAMPLES::

            sage: from sage.misc.parser import Parser, Tokenizer
            sage: R.<t> = ZZ[[\'t\']]
            sage: p = Parser(make_var={\'t\': t})
            sage: p.p_factor(Tokenizer("-(1+t)^-1"))
            -1 + t - t^2 + t^3 - t^4 + t^5 - t^6 + t^7 - t^8 + t^9 - t^10 + t^11 - t^12 + t^13 - t^14 + t^15 - t^16 + t^17 - t^18 + t^19 + O(t^20)
            sage: p.p_factor(Tokenizer("t**2"))
            t^2
            sage: p.p_power(Tokenizer("2^3^2")) == 2^9
            True

            sage: # needs sage.symbolic
            sage: p = Parser(make_var=var)
            sage: p.p_factor(Tokenizer(\'x!\'))
            factorial(x)
            sage: p.p_factor(Tokenizer(\'(x^2)!\'))
            factorial(x^2)
            sage: p.p_factor(Tokenizer(\'x!^2\'))
            factorial(x)^2'''
    def p_sequence(self, Tokenizertokens) -> Any:
        '''Parser.p_sequence(self, Tokenizer tokens)

        File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 625)

        Parse a (possibly nested) set of lists and tuples.

        EXAMPLES::

            sage: from sage.misc.parser import Parser, Tokenizer
            sage: p = Parser(make_var=var)                                              # needs sage.symbolic
            sage: p.p_sequence(Tokenizer("[1+2,0]"))                                    # needs sage.symbolic
            [[3, 0]]
            sage: p.p_sequence(Tokenizer("(1,2,3) , [1+a, 2+b, (3+c), (4+d,)]"))        # needs sage.symbolic
            [(1, 2, 3), [a + 1, b + 2, c + 3, (d + 4,)]]'''
    def p_term(self, Tokenizertokens) -> Any:
        '''Parser.p_term(self, Tokenizer tokens)

        File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 808)

        Parse a single term (consisting of one or more factors).

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: from sage.misc.parser import Parser, Tokenizer
            sage: p = Parser(make_var=var)
            sage: p.p_term(Tokenizer("a*b"))
            a*b
            sage: p.p_term(Tokenizer("a * b / c * d"))
            a*b*d/c
            sage: p.p_term(Tokenizer("-a * b + c"))
            -a*b
            sage: p.p_term(Tokenizer("a*(b-c)^2"))
            a*(b - c)^2
            sage: p.p_term(Tokenizer("-3a"))
            -3*a'''
    def p_tuple(self, Tokenizertokens) -> Any:
        '''Parser.p_tuple(self, Tokenizer tokens)

        File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 692)

        Parse a tuple of items.

        EXAMPLES::

            sage: from sage.misc.parser import Parser, Tokenizer
            sage: p = Parser(make_var=var)                                              # needs sage.symbolic
            sage: p.p_tuple(Tokenizer("( (), (1), (1,), (1,2), (1,2,3), (1+2)^2, )"))   # needs sage.symbolic
            ((), 1, (1,), (1, 2), (1, 2, 3), 9)'''
    def parse(self, s, boolaccept_eqn=...) -> Any:
        '''Parser.parse(self, s, bool accept_eqn=True)

        File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 534)

        Parse the given string.

        EXAMPLES::

            sage: from sage.misc.parser import Parser
            sage: p = Parser(make_var=var)                                              # needs sage.symbolic
            sage: p.parse("E = m c^2")                                                  # needs sage.symbolic
            E == c^2*m'''
    def parse_expression(self, s) -> Any:
        """Parser.parse_expression(self, s)

        File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 556)

        Parse an expression.

        EXAMPLES::

            sage: from sage.misc.parser import Parser
            sage: p = Parser(make_var=var)                                              # needs sage.symbolic
            sage: p.parse_expression('a-3b^2')                                          # needs sage.symbolic
            -3*b^2 + a"""
    def parse_sequence(self, s) -> Any:
        '''Parser.parse_sequence(self, s)

        File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 573)

        Parse a (possibly nested) set of lists and tuples.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: from sage.misc.parser import Parser
            sage: p = Parser(make_var=var)
            sage: p.parse_sequence("1,2,3")
            [1, 2, 3]
            sage: p.parse_sequence("[1,2,(a,b,c+d)]")
            [1, 2, (a, b, c + d)]
            sage: p.parse_sequence("13")
            13'''

class Tokenizer:
    """Tokenizer(s)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, s) -> Any:
        '''File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 109)

                This class takes a string and turns it into a list of tokens for use
                by the parser.

                The tokenizer wraps a string object, to tokenize a different string
                create a new tokenizer.

                EXAMPLES::

                    sage: from sage.misc.parser import Tokenizer
                    sage: Tokenizer("1.5+2*3^4-sin(x)").test()
                    [\'FLOAT(1.5)\', \'+\', \'INT(2)\', \'*\', \'INT(3)\', \'^\', \'INT(4)\', \'-\', \'NAME(sin)\', \'(\', \'NAME(x)\', \')\']

                The single character tokens are given by::

                    sage: Tokenizer("+-*/^(),=<>[]{}").test()
                    [\'+\', \'-\', \'*\', \'/\', \'^\', \'(\', \')\', \',\', \'=\', \'<\', \'>\', \'[\', \']\', \'{\', \'}\']

                Two-character comparisons accepted are::

                    sage: Tokenizer("<= >= != == **").test()
                    [\'LESS_EQ\', \'GREATER_EQ\', \'NOT_EQ\', \'=\', \'^\']

                Integers are strings of 0-9::

                    sage: Tokenizer("1 123 9879834759873452908375013").test()
                    [\'INT(1)\', \'INT(123)\', \'INT(9879834759873452908375013)\']

                Floating point numbers can contain a single decimal point and possibly exponential notation::

                    sage: Tokenizer("1. .01 1e3 1.e-3").test()
                    [\'FLOAT(1.)\', \'FLOAT(.01)\', \'FLOAT(1e3)\', \'FLOAT(1.e-3)\']

                Note that negative signs are not attached to the token::

                    sage: Tokenizer("-1 -1.2").test()
                    [\'-\', \'INT(1)\', \'-\', \'FLOAT(1.2)\']

                Names are alphanumeric sequences not starting with a digit::

                    sage: Tokenizer("a a1 _a_24").test()
                    [\'NAME(a)\', \'NAME(a1)\', \'NAME(_a_24)\']

                There is special handling for matrices::

                    sage: Tokenizer("matrix(a)").test()
                    [\'MATRIX\', \'(\', \'NAME(a)\', \')\']

                Anything else is an error::

                    sage: Tokenizer("&@~").test()
                    [\'ERROR\', \'ERROR\', \'ERROR\']

                No attempt for correctness is made at this stage::

                    sage: Tokenizer(") )( 5e5e5").test()
                    [\')\', \')\', \'(\', \'FLOAT(5e5)\', \'NAME(e5)\']
                    sage: Tokenizer("?$%").test()
                    [\'ERROR\', \'ERROR\', \'ERROR\']

                TESTS:

                Check support for unicode characters (:issue:`29280`)::

                    sage: Tokenizer("λ+α_β0 Γ^ω").test()
                    [\'NAME(λ)\', \'+\', \'NAME(α_β0)\', \'NAME(Γ)\', \'^\', \'NAME(ω)\']
        '''
    @overload
    def backtrack(self) -> bool:
        '''Tokenizer.backtrack(self) -> bool

        File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 398)

        Put ``self`` in such a state that the subsequent call to ``next()``
        will return the same as if ``next()`` had not been called.

        Currently, one can only backtrack once.

        EXAMPLES::

            sage: from sage.misc.parser import Tokenizer, token_to_str
            sage: t = Tokenizer("a+b")
            sage: token_to_str(t.next())
            \'NAME\'
            sage: token_to_str(t.next())
            \'+\'
            sage: t.backtrack()   # the return type is bint for performance reasons
            False
            sage: token_to_str(t.next())
            \'+\''''
    @overload
    def backtrack(self) -> Any:
        '''Tokenizer.backtrack(self) -> bool

        File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 398)

        Put ``self`` in such a state that the subsequent call to ``next()``
        will return the same as if ``next()`` had not been called.

        Currently, one can only backtrack once.

        EXAMPLES::

            sage: from sage.misc.parser import Tokenizer, token_to_str
            sage: t = Tokenizer("a+b")
            sage: token_to_str(t.next())
            \'NAME\'
            sage: token_to_str(t.next())
            \'+\'
            sage: t.backtrack()   # the return type is bint for performance reasons
            False
            sage: token_to_str(t.next())
            \'+\''''
    @overload
    def last(self) -> int:
        '''Tokenizer.last(self) -> int

        File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 354)

        Return the last token seen.

        EXAMPLES::

            sage: from sage.misc.parser import Tokenizer, token_to_str
            sage: t = Tokenizer("3a")
            sage: token_to_str(t.next())
            \'INT\'
            sage: token_to_str(t.last())
            \'INT\'
            sage: token_to_str(t.next())
            \'NAME\'
            sage: token_to_str(t.last())
            \'NAME\''''
    @overload
    def last(self) -> Any:
        '''Tokenizer.last(self) -> int

        File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 354)

        Return the last token seen.

        EXAMPLES::

            sage: from sage.misc.parser import Tokenizer, token_to_str
            sage: t = Tokenizer("3a")
            sage: token_to_str(t.next())
            \'INT\'
            sage: token_to_str(t.last())
            \'INT\'
            sage: token_to_str(t.next())
            \'NAME\'
            sage: token_to_str(t.last())
            \'NAME\''''
    @overload
    def last(self) -> Any:
        '''Tokenizer.last(self) -> int

        File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 354)

        Return the last token seen.

        EXAMPLES::

            sage: from sage.misc.parser import Tokenizer, token_to_str
            sage: t = Tokenizer("3a")
            sage: token_to_str(t.next())
            \'INT\'
            sage: token_to_str(t.last())
            \'INT\'
            sage: token_to_str(t.next())
            \'NAME\'
            sage: token_to_str(t.last())
            \'NAME\''''
    @overload
    def last_token_string(self) -> Any:
        '''Tokenizer.last_token_string(self)

        File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 424)

        Return the actual contents of the last token.

        EXAMPLES::

            sage: from sage.misc.parser import Tokenizer, token_to_str
            sage: t = Tokenizer("a - 1e5")
            sage: token_to_str(t.next())
            \'NAME\'
            sage: t.last_token_string()
            \'a\'
            sage: token_to_str(t.next())
            \'-\'
            sage: token_to_str(t.next())
            \'FLOAT\'
            sage: t.last_token_string()
            \'1e5\''''
    @overload
    def last_token_string(self) -> Any:
        '''Tokenizer.last_token_string(self)

        File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 424)

        Return the actual contents of the last token.

        EXAMPLES::

            sage: from sage.misc.parser import Tokenizer, token_to_str
            sage: t = Tokenizer("a - 1e5")
            sage: token_to_str(t.next())
            \'NAME\'
            sage: t.last_token_string()
            \'a\'
            sage: token_to_str(t.next())
            \'-\'
            sage: token_to_str(t.next())
            \'FLOAT\'
            sage: t.last_token_string()
            \'1e5\''''
    @overload
    def last_token_string(self) -> Any:
        '''Tokenizer.last_token_string(self)

        File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 424)

        Return the actual contents of the last token.

        EXAMPLES::

            sage: from sage.misc.parser import Tokenizer, token_to_str
            sage: t = Tokenizer("a - 1e5")
            sage: token_to_str(t.next())
            \'NAME\'
            sage: t.last_token_string()
            \'a\'
            sage: token_to_str(t.next())
            \'-\'
            sage: token_to_str(t.next())
            \'FLOAT\'
            sage: t.last_token_string()
            \'1e5\''''
    @overload
    def next(self) -> int:
        '''Tokenizer.next(self) -> int

        File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 331)

        Return the next token in the string.

        EXAMPLES::

            sage: from sage.misc.parser import Tokenizer, token_to_str
            sage: t = Tokenizer("a+3")
            sage: token_to_str(t.next())
            \'NAME\'
            sage: token_to_str(t.next())
            \'+\'
            sage: token_to_str(t.next())
            \'INT\'
            sage: token_to_str(t.next())
            \'EOS\''''
    @overload
    def next(self) -> Any:
        '''Tokenizer.next(self) -> int

        File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 331)

        Return the next token in the string.

        EXAMPLES::

            sage: from sage.misc.parser import Tokenizer, token_to_str
            sage: t = Tokenizer("a+3")
            sage: token_to_str(t.next())
            \'NAME\'
            sage: token_to_str(t.next())
            \'+\'
            sage: token_to_str(t.next())
            \'INT\'
            sage: token_to_str(t.next())
            \'EOS\''''
    @overload
    def next(self) -> Any:
        '''Tokenizer.next(self) -> int

        File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 331)

        Return the next token in the string.

        EXAMPLES::

            sage: from sage.misc.parser import Tokenizer, token_to_str
            sage: t = Tokenizer("a+3")
            sage: token_to_str(t.next())
            \'NAME\'
            sage: token_to_str(t.next())
            \'+\'
            sage: token_to_str(t.next())
            \'INT\'
            sage: token_to_str(t.next())
            \'EOS\''''
    @overload
    def next(self) -> Any:
        '''Tokenizer.next(self) -> int

        File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 331)

        Return the next token in the string.

        EXAMPLES::

            sage: from sage.misc.parser import Tokenizer, token_to_str
            sage: t = Tokenizer("a+3")
            sage: token_to_str(t.next())
            \'NAME\'
            sage: token_to_str(t.next())
            \'+\'
            sage: token_to_str(t.next())
            \'INT\'
            sage: token_to_str(t.next())
            \'EOS\''''
    @overload
    def next(self) -> Any:
        '''Tokenizer.next(self) -> int

        File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 331)

        Return the next token in the string.

        EXAMPLES::

            sage: from sage.misc.parser import Tokenizer, token_to_str
            sage: t = Tokenizer("a+3")
            sage: token_to_str(t.next())
            \'NAME\'
            sage: token_to_str(t.next())
            \'+\'
            sage: token_to_str(t.next())
            \'INT\'
            sage: token_to_str(t.next())
            \'EOS\''''
    @overload
    def peek(self) -> int:
        '''Tokenizer.peek(self) -> int

        File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 373)

        Return the next token that will be encountered, without changing
        the state of ``self``.

        EXAMPLES::

            sage: from sage.misc.parser import Tokenizer, token_to_str
            sage: t = Tokenizer("a+b")
            sage: token_to_str(t.peek())
            \'NAME\'
            sage: token_to_str(t.next())
            \'NAME\'
            sage: token_to_str(t.peek())
            \'+\'
            sage: token_to_str(t.peek())
            \'+\'
            sage: token_to_str(t.next())
            \'+\''''
    @overload
    def peek(self) -> Any:
        '''Tokenizer.peek(self) -> int

        File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 373)

        Return the next token that will be encountered, without changing
        the state of ``self``.

        EXAMPLES::

            sage: from sage.misc.parser import Tokenizer, token_to_str
            sage: t = Tokenizer("a+b")
            sage: token_to_str(t.peek())
            \'NAME\'
            sage: token_to_str(t.next())
            \'NAME\'
            sage: token_to_str(t.peek())
            \'+\'
            sage: token_to_str(t.peek())
            \'+\'
            sage: token_to_str(t.next())
            \'+\''''
    @overload
    def peek(self) -> Any:
        '''Tokenizer.peek(self) -> int

        File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 373)

        Return the next token that will be encountered, without changing
        the state of ``self``.

        EXAMPLES::

            sage: from sage.misc.parser import Tokenizer, token_to_str
            sage: t = Tokenizer("a+b")
            sage: token_to_str(t.peek())
            \'NAME\'
            sage: token_to_str(t.next())
            \'NAME\'
            sage: token_to_str(t.peek())
            \'+\'
            sage: token_to_str(t.peek())
            \'+\'
            sage: token_to_str(t.next())
            \'+\''''
    @overload
    def peek(self) -> Any:
        '''Tokenizer.peek(self) -> int

        File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 373)

        Return the next token that will be encountered, without changing
        the state of ``self``.

        EXAMPLES::

            sage: from sage.misc.parser import Tokenizer, token_to_str
            sage: t = Tokenizer("a+b")
            sage: token_to_str(t.peek())
            \'NAME\'
            sage: token_to_str(t.next())
            \'NAME\'
            sage: token_to_str(t.peek())
            \'+\'
            sage: token_to_str(t.peek())
            \'+\'
            sage: token_to_str(t.next())
            \'+\''''
    @overload
    def reset(self, intpos=...) -> Any:
        '''Tokenizer.reset(self, int pos=0)

        File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 207)

        Reset the tokenizer to a given position.

        EXAMPLES::

            sage: from sage.misc.parser import Tokenizer
            sage: t = Tokenizer("a+b*c")
            sage: t.test()
            [\'NAME(a)\', \'+\', \'NAME(b)\', \'*\', \'NAME(c)\']
            sage: t.test()
            []
            sage: t.reset()
            sage: t.test()
            [\'NAME(a)\', \'+\', \'NAME(b)\', \'*\', \'NAME(c)\']
            sage: t.reset(3)
            sage: t.test()
            [\'*\', \'NAME(c)\']

        No care is taken to make sure we don\'t jump in the middle of a token::

            sage: t = Tokenizer("12345+a")
            sage: t.test()
            [\'INT(12345)\', \'+\', \'NAME(a)\']
            sage: t.reset(2)
            sage: t.test()
            [\'INT(345)\', \'+\', \'NAME(a)\']'''
    @overload
    def reset(self) -> Any:
        '''Tokenizer.reset(self, int pos=0)

        File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 207)

        Reset the tokenizer to a given position.

        EXAMPLES::

            sage: from sage.misc.parser import Tokenizer
            sage: t = Tokenizer("a+b*c")
            sage: t.test()
            [\'NAME(a)\', \'+\', \'NAME(b)\', \'*\', \'NAME(c)\']
            sage: t.test()
            []
            sage: t.reset()
            sage: t.test()
            [\'NAME(a)\', \'+\', \'NAME(b)\', \'*\', \'NAME(c)\']
            sage: t.reset(3)
            sage: t.test()
            [\'*\', \'NAME(c)\']

        No care is taken to make sure we don\'t jump in the middle of a token::

            sage: t = Tokenizer("12345+a")
            sage: t.test()
            [\'INT(12345)\', \'+\', \'NAME(a)\']
            sage: t.reset(2)
            sage: t.test()
            [\'INT(345)\', \'+\', \'NAME(a)\']'''
    @overload
    def test(self) -> Any:
        '''Tokenizer.test(self)

        File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 181)

        This is a utility function for easy testing of the tokenizer.

        Destructively read off the tokens in self, returning a list of string
        representations of the tokens.

        EXAMPLES::

            sage: from sage.misc.parser import Tokenizer
            sage: t = Tokenizer("a b 3")
            sage: t.test()
            [\'NAME(a)\', \'NAME(b)\', \'INT(3)\']
            sage: t.test()
            []'''
    @overload
    def test(self) -> Any:
        '''Tokenizer.test(self)

        File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 181)

        This is a utility function for easy testing of the tokenizer.

        Destructively read off the tokens in self, returning a list of string
        representations of the tokens.

        EXAMPLES::

            sage: from sage.misc.parser import Tokenizer
            sage: t = Tokenizer("a b 3")
            sage: t.test()
            [\'NAME(a)\', \'NAME(b)\', \'INT(3)\']
            sage: t.test()
            []'''
    @overload
    def test(self) -> Any:
        '''Tokenizer.test(self)

        File: /build/sagemath/src/sage/src/sage/misc/parser.pyx (starting at line 181)

        This is a utility function for easy testing of the tokenizer.

        Destructively read off the tokens in self, returning a list of string
        representations of the tokens.

        EXAMPLES::

            sage: from sage.misc.parser import Tokenizer
            sage: t = Tokenizer("a b 3")
            sage: t.test()
            [\'NAME(a)\', \'NAME(b)\', \'INT(3)\']
            sage: t.test()
            []'''
