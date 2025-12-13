import ast

def is_function_or_cython_function(obj):
    """
    Check whether something is a function.

    This is a variant of :func:`inspect.isfunction`:
    We assume that anything which has a genuine ``__code__``
    attribute (not using ``__getattr__`` overrides) is a function.
    This is meant to support Cython functions.

    Think twice before using this function (or any function from the
    :mod:`inspect` or :mod:`sage.misc.sageinspect` modules).  Most uses of
    :func:`inspect.isfunction` in ordinary library code can be replaced by
    :func:`callable`.

    EXAMPLES::

        sage: from sage.misc.sageinspect import is_function_or_cython_function
        sage: def f(): pass
        sage: is_function_or_cython_function(f)
        True
        sage: is_function_or_cython_function(lambda x:x)
        True
        sage: from sage.categories.coercion_methods import _mul_parent
        sage: is_function_or_cython_function(_mul_parent)
        True
        sage: is_function_or_cython_function(Integer.digits)     # unbound method
        True
        sage: is_function_or_cython_function(Integer(1).digits)  # bound method
        False

    TESTS:

    Verify that ipywidgets can correctly determine signatures of Cython
    functions::

        sage: from ipywidgets.widgets.interaction import signature
        sage: from sage.dynamics.complex_dynamics.mandel_julia_helper import fast_mandelbrot_plot   # needs sage.symbolic
        sage: signature(fast_mandelbrot_plot)  # random                                 # needs sage.symbolic
        <IPython.utils._signatures.Signature object at 0x7f3ec8274e10>
    """
def isclassinstance(obj):
    """
    Check if argument is instance of non built-in class.

    INPUT:

    - ``obj`` -- object

    EXAMPLES::

        sage: from sage.misc.sageinspect import isclassinstance
        sage: isclassinstance(int)
        False
        sage: class myclass: pass
        sage: isclassinstance(myclass())
        True
        sage: isclassinstance(myclass)
        False
        sage: class mymetaclass(type): pass
        sage: class myclass2(metaclass=mymetaclass): pass
        sage: isclassinstance(myclass2)
        False
    """

class BlockFinder:
    """
    Provide a :meth:`tokeneater` method to detect the end of a code block.

    This is the Python library's :class:`inspect.BlockFinder` modified
    to recognize Cython definitions.
    """
    indent: int
    islambda: bool
    started: bool
    passline: bool
    last: int
    def __init__(self) -> None: ...
    def tokeneater(self, type, token, srow_scol, erow_ecol, line) -> None: ...

class SageArgSpecVisitor(ast.NodeVisitor):
    '''
    A simple visitor class that walks an abstract-syntax tree (AST)
    for a Python function\'s argspec.  It returns the contents of nodes
    representing the basic Python types: None, booleans, numbers,
    strings, lists, tuples, and dictionaries.  We use this class in
    :func:`_sage_getargspec_from_ast` to extract an argspec from a
    function\'s or method\'s source code.

    EXAMPLES::

        sage: import ast, sage.misc.sageinspect as sms
        sage: visitor = sms.SageArgSpecVisitor()
        sage: visitor.visit(ast.parse(\'[1,2,3]\').body[0].value)
        [1, 2, 3]
        sage: v = visitor.visit(ast.parse("{\'a\':(\'e\',2,[None,({False:True},\'pi\')]), 37.0:\'temp\'}").body[0].value)
        sage: sorted(v.items(), key=lambda x: str(x[0]))
        [(37.0, \'temp\'), (\'a\', (\'e\', 2, [None, ({False: True}, \'pi\')]))]
        sage: v = ast.parse("jc = [\'veni\', \'vidi\', \'vici\']").body[0]; v
        <...ast.Assign object at ...>
        sage: attrs = [x for x in dir(v) if not x.startswith(\'__\')]
        sage: \'_attributes\' in attrs and \'_fields\' in attrs and \'col_offset\' in attrs
        True
        sage: visitor.visit(v.targets[0])
        \'jc\'
        sage: visitor.visit(v.value)
        [\'veni\', \'vidi\', \'vici\']
    '''
    def visit_Name(self, node):
        """
        Visit a Python AST :class:`ast.Name` node.

        INPUT:

        - ``node`` -- the node instance to visit

        OUTPUT: ``None``, ``True``, ``False``, or the ``node``'s name as a string

        EXAMPLES::

            sage: import ast, sage.misc.sageinspect as sms
            sage: visitor = sms.SageArgSpecVisitor()
            sage: vis = lambda x: visitor.visit_Name(ast.parse(x).body[0].value)
            sage: [vis(n) for n in ['foo', 'bar']]
            ['foo', 'bar']
            sage: [type(vis(n)) for n in ['foo', 'bar']]
            [<class 'str'>, <class 'str'>]
        """
    def visit_NameConstant(self, node):
        """
        Visit a Python AST :class:`ast.NameConstant` node.

        This is an optimization added in Python 3.4 for the special cases
        of True, False, and None.

        INPUT:

        - ``node`` -- the node instance to visit

        OUTPUT: ``None``, ``True``, ``False``

        EXAMPLES::

            sage: import ast, sage.misc.sageinspect as sms
            sage: visitor = sms.SageArgSpecVisitor()
            sage: vis = lambda x: visitor.visit_NameConstant(ast.parse(x).body[0].value)
            sage: [vis(n) for n in ['True', 'False', 'None']]
            [True, False, None]
            sage: [type(vis(n)) for n in ['True', 'False', 'None']]
            [<class 'bool'>, <class 'bool'>, <class 'NoneType'>]
        """
    def visit_arg(self, node):
        '''
        Visit a Python AST :class:`ast.arg` node.

        This node type is only on Python 3, where function arguments are
        more complex than just an identifier (e.g. they may also include
        annotations).

        For now we simply return the argument identifier as a string.

        INPUT:

        - ``node`` -- the node instance to visit

        OUTPUT: the argument name

        EXAMPLES::

            sage: import ast, sage.misc.sageinspect as sms
            sage: s = "def f(a, b=2, c={\'a\': [4, 5.5, False]}, d=(None, True)):\\n    return"
            sage: visitor = sms.SageArgSpecVisitor()
            sage: args = ast.parse(s).body[0].args.args
            sage: [visitor.visit_arg(n) for n in args]
            [\'a\', \'b\', \'c\', \'d\']
        '''
    def visit_Num(self, node):
        """
        Visit a Python AST :class:`ast.Num` node.

        INPUT:

        - ``node`` -- the node instance to visit

        OUTPUT: the number the ``node`` represents

        EXAMPLES::

            sage: import ast, sage.misc.sageinspect as sms
            sage: visitor = sms.SageArgSpecVisitor()
            sage: vis = lambda x: visitor.visit_Num(ast.parse(x).body[0].value)
            sage: [vis(n) for n in ['123', '0.0']]
            [123, 0.0]

        .. NOTE::

            On Python 3 negative numbers are parsed first, for some reason, as
            a UnaryOp node.
        """
    def visit_Str(self, node):
        '''
        Visit a Python AST :class:`ast.Str` node.

        INPUT:

        - ``node`` -- the node instance to visit

        OUTPUT: the string the ``node`` represents

        EXAMPLES::

            sage: import ast, sage.misc.sageinspect as sms
            sage: visitor = sms.SageArgSpecVisitor()
            sage: vis = lambda x: visitor.visit_Str(ast.parse(x).body[0].value)
            sage: [vis(s) for s in [\'"abstract"\', "\'syntax\'", r\'\'\'r"tr\\ee"\'\'\']]
            [\'abstract\', \'syntax\', \'tr\\\\ee\']
        '''
    def visit_List(self, node):
        '''
        Visit a Python AST :class:`ast.List` node.

        INPUT:

        - ``node`` -- the node instance to visit

        OUTPUT: the list the ``node`` represents

        EXAMPLES::

            sage: import ast, sage.misc.sageinspect as sms
            sage: visitor = sms.SageArgSpecVisitor()
            sage: vis = lambda x: visitor.visit_List(ast.parse(x).body[0].value)
            sage: [vis(l) for l in [\'[]\', "[\'s\', \'t\', \'u\']", \'[[e], [], [pi]]\']]
            [[], [\'s\', \'t\', \'u\'], [[\'e\'], [], [\'pi\']]]
        '''
    def visit_Tuple(self, node):
        '''
        Visit a Python AST :class:`ast.Tuple` node.

        INPUT:

        - ``node`` -- the node instance to visit

        OUTPUT: the tuple the ``node`` represents

        EXAMPLES::

            sage: import ast, sage.misc.sageinspect as sms
            sage: visitor = sms.SageArgSpecVisitor()
            sage: vis = lambda x: visitor.visit_Tuple(ast.parse(x).body[0].value)
            sage: [vis(t) for t in [\'()\', \'(x,y)\', \'("Au", "Al", "Cu")\']]
            [(), (\'x\', \'y\'), (\'Au\', \'Al\', \'Cu\')]
        '''
    def visit_Dict(self, node):
        '''
        Visit a Python AST :class:`ast.Dict` node.

        INPUT:

        - ``node`` -- the node instance to visit

        OUTPUT: the dictionary the ``node`` represents

        EXAMPLES::

            sage: import ast, sage.misc.sageinspect as sms
            sage: visitor = sms.SageArgSpecVisitor()
            sage: vis = lambda x: visitor.visit_Dict(ast.parse(x).body[0].value)
            sage: v = [vis(d) for d in [\'{}\', "{1:one, \'two\':2, other:bother}"]]
            sage: [sorted(d.items(), key=lambda x: str(x[0])) for d in v]
            [[], [(1, \'one\'), (\'other\', \'bother\'), (\'two\', 2)]]
        '''
    def visit_BoolOp(self, node):
        """
        Visit a Python AST :class:`ast.BoolOp` node.

        INPUT:

        - ``node`` -- the node instance to visit

        OUTPUT: the result that ``node`` represents

        EXAMPLES::

            sage: import ast, sage.misc.sageinspect as sms
            sage: visitor = sms.SageArgSpecVisitor()
            sage: vis = lambda x: visitor.visit(ast.parse(x).body[0].value)
            sage: [vis(d) for d in ['True and 1', 'False or 3 or None', '3 and 4']] #indirect doctest
            [1, 3, 4]
        """
    def visit_Compare(self, node):
        """
        Visit a Python AST :class:`ast.Compare` node.

        INPUT:

        - ``node`` -- the node instance to visit

        OUTPUT: the result that ``node`` represents

        EXAMPLES::

            sage: import ast, sage.misc.sageinspect as sms
            sage: visitor = sms.SageArgSpecVisitor()
            sage: vis = lambda x: visitor.visit_Compare(ast.parse(x).body[0].value)
            sage: [vis(d) for d in ['1<2==2!=3', '1==1>2', '1<2>1', '1<3<2<4']]
            [True, False, True, False]
        """
    def visit_BinOp(self, node):
        """
        Visit a Python AST :class:`ast.BinOp` node.

        INPUT:

        - ``node`` -- the node instance to visit

        OUTPUT: the result that ``node`` represents

        EXAMPLES::

            sage: import ast, sage.misc.sageinspect as sms
            sage: visitor = sms.SageArgSpecVisitor()
            sage: vis = lambda x: visitor.visit(ast.parse(x).body[0].value)
            sage: [vis(d) for d in ['(3+(2*4))', '7|8', '5^3', '7/3', '7//3', '3<<4']] #indirect doctest
            [11, 15, 6, 2.3333333333333335, 2, 48]
        """
    def visit_UnaryOp(self, node):
        """
        Visit a Python AST :class:`ast.BinOp` node.

        INPUT:

        - ``node`` -- the node instance to visit

        OUTPUT: the result that ``node`` represents

        EXAMPLES::

            sage: import ast, sage.misc.sageinspect as sms
            sage: visitor = sms.SageArgSpecVisitor()
            sage: vis = lambda x: visitor.visit_UnaryOp(ast.parse(x).body[0].value)
            sage: [vis(d) for d in ['+(3*2)', '-(3*2)']]
            [6, -6]
        """

def sage_getfile(obj):
    """
    Get the full file name associated to ``obj`` as a string.

    INPUT:

    - ``obj`` -- a Sage object, module, etc.

    EXAMPLES::

        sage: from sage.misc.sageinspect import sage_getfile
        sage: sage_getfile(sage.rings.rational)
        '...sage/rings/rational.pyx'
        sage: from sage.algebras.steenrod.steenrod_algebra import Sq                    # needs sage.combinat sage.modules
        sage: sage_getfile(Sq)                                                          # needs sage.combinat sage.modules
        '...sage/algebras/steenrod/steenrod_algebra.py'
        sage: sage_getfile(x)                                                           # needs sage.symbolic
        '...sage/symbolic/expression.pyx'

    The following tests against some bugs fixed in :issue:`9976`::

        sage: obj = sage.combinat.partition_algebra.SetPartitionsAk                     # needs sage.combinat sage.modules
        sage: sage_getfile(obj)                                                         # needs sage.combinat sage.modules
        '...sage/combinat/partition_algebra.py'

    And here is another bug, fixed in :issue:`11298`::

        sage: P.<x,y> = QQ[]
        sage: sage_getfile(P)                                                           # needs sage.libs.singular
        '...sage/rings/polynomial/multi_polynomial_libsingular...'

    Another bug with editable meson install::

        sage: P.<x,y> = QQ[]
        sage: I = P * [x,y]
        sage: path = sage_getfile(I.groebner_basis); path
        '.../sage/rings/qqbar_decorators.py'
        sage: path == sage_getfile(sage.rings.qqbar_decorators)
        True

    A problem fixed in :issue:`16309`::

        sage: cython(                                                                   # needs sage.misc.cython
        ....: '''
        ....: class Bar: pass
        ....: cdef class Foo: pass
        ....: ''')
        sage: sage_getfile(Bar)                                                         # needs sage.misc.cython
        '...pyx'
        sage: sage_getfile(Foo)                                                         # needs sage.misc.cython
        '...pyx'

    By :issue:`18249`, we return an empty string for Python builtins. In that
    way, there is no error when the user types, for example, ``range?``::

        sage: sage_getfile(range)
        ''
    """
def sage_getfile_relative(obj):
    """
    Get the file name associated to ``obj`` as a string.

    This is the same as :func:`sage_getfile`, but
    if the source file is part of the ``sage.*`` namespace, it
    makes the file name relative so that it starts with ``sage/``.

    INPUT:

    - ``obj`` -- a Sage object, module, etc.

    EXAMPLES::

        sage: from sage.misc.sageinspect import sage_getfile_relative
        sage: sage_getfile_relative(sage.rings.rational)
        'sage/rings/rational.pyx'
        sage: from sage.algebras.steenrod.steenrod_algebra import Sq                    # needs sage.combinat sage.modules
        sage: sage_getfile_relative(Sq)                                                 # needs sage.combinat sage.modules
        'sage/algebras/steenrod/steenrod_algebra.py'
        sage: sage_getfile_relative(x)                                                  # needs sage.symbolic
        'sage/symbolic/expression.pyx'
        sage: sage_getfile_relative(range)
        ''
    """
def sage_getargspec(obj):
    '''
    Return the names and default values of a function\'s arguments.

    INPUT:

    - ``obj`` -- any callable object

    OUTPUT:

    A named tuple :class:`FullArgSpec` is returned, as specified by the
    Python library function :func:`inspect.getfullargspec`.

    NOTE:

    If the object has a method ``_sage_argspec_``, then the output of
    that method is transformed into a named tuple and then returned.

    If a class instance has a method ``_sage_src_``, then its output
    is studied to determine the argspec. This is because currently
    the :class:`~sage.misc.cachefunc.CachedMethod` decorator has
    no ``_sage_argspec_`` method.

    EXAMPLES::

        sage: from sage.misc.sageinspect import sage_getargspec
        sage: def f(x, y, z=1, t=2, *args, **keywords):
        ....:     pass
        sage: sage_getargspec(f)
        FullArgSpec(args=[\'x\', \'y\', \'z\', \'t\'], varargs=\'args\', varkw=\'keywords\',
                    defaults=(1, 2), kwonlyargs=[], kwonlydefaults=None, annotations={})

    We now run :func:`sage_getargspec` on some functions from the Sage library::

        sage: sage_getargspec(identity_matrix)                                          # needs sage.modules
        FullArgSpec(args=[\'ring\', \'n\', \'sparse\'], varargs=None, varkw=None,
                    defaults=(0, False), kwonlyargs=[], kwonlydefaults=None,
                    annotations={})
        sage: sage_getargspec(factor)
        FullArgSpec(args=[\'n\', \'proof\', \'int_\', \'algorithm\', \'verbose\'],
                    varargs=None, varkw=\'kwds\', defaults=(None, False, \'pari\', 0),
                    kwonlyargs=[], kwonlydefaults=None, annotations={})

    In the case of a class or a class instance, the :class:`FullArgSpec` of the
    ``__new__``, ``__init__`` or ``__call__`` method is returned::

        sage: P.<x,y> = QQ[]
        sage: sage_getargspec(P)                                                        # needs sage.libs.singular
        FullArgSpec(args=[\'base_ring\', \'n\', \'names\', \'order\'],
                    varargs=None, varkw=None, defaults=(\'degrevlex\',),
                    kwonlyargs=[], kwonlydefaults=None, annotations={})
        sage: sage_getargspec(P.__class__)                                              # needs sage.libs.singular
        FullArgSpec(args=[\'self\', \'x\'], varargs=\'args\', varkw=\'kwds\', defaults=(0,),
                    kwonlyargs=[], kwonlydefaults=None, annotations={})

    The following tests against various bugs that were fixed in
    :issue:`9976`::

        sage: from sage.rings.polynomial.real_roots import bernstein_polynomial_factory_ratlist     # needs sage.modules
        sage: sage_getargspec(bernstein_polynomial_factory_ratlist.coeffs_bitsize)                  # needs sage.modules
        FullArgSpec(args=[\'self\'], varargs=None, varkw=None, defaults=None,
                    kwonlyargs=[], kwonlydefaults=None, annotations={})
        sage: from sage.rings.polynomial.pbori.pbori import BooleanMonomialMonoid       # needs sage.rings.polynomial.pbori
        sage: sage_getargspec(BooleanMonomialMonoid.gen)                                # needs sage.rings.polynomial.pbori
        FullArgSpec(args=[\'self\', \'i\'], varargs=None, varkw=None, defaults=(0,),
                    kwonlyargs=[], kwonlydefaults=None, annotations={})
        sage: I = P*[x,y]
        sage: sage_getargspec(I.groebner_basis)                                         # needs sage.libs.singular
        FullArgSpec(args=[\'self\', \'algorithm\', \'deg_bound\', \'mult_bound\', \'prot\'],
                    varargs=\'args\', varkw=\'kwds\', defaults=(\'\', None, None, False),
                    kwonlyargs=[], kwonlydefaults=None, annotations={})
        sage: cython("cpdef int foo(x,y) except -1: return 1")                          # needs sage.misc.cython
        sage: sage_getargspec(foo)                                                      # needs sage.misc.cython
        FullArgSpec(args=[\'x\', \'y\'], varargs=None, varkw=None, defaults=None,
                    kwonlyargs=[], kwonlydefaults=None, annotations={})

    If a :func:`functools.partial` instance is involved, we see no other meaningful solution
    than to return the argspec of the underlying function::

        sage: def f(a, b, c, d=1):
        ....:     return a + b + c + d
        sage: import functools
        sage: f1 = functools.partial(f, 1, c=2)
        sage: sage_getargspec(f1)
        FullArgSpec(args=[\'a\', \'b\', \'c\', \'d\'], varargs=None, varkw=None, defaults=(1,),
                    kwonlyargs=[], kwonlydefaults=None, annotations={})

    TESTS:

    By :issue:`9976`, rather complicated cases work. In the
    following example, we dynamically create an extension class
    that returns some source code, and the example shows that
    the source code is taken for granted, i.e., the argspec of
    an instance of that class does not coincide with the argspec
    of its call method. That behaviour is intended, since a
    decorated method appears to have the generic signature
    ``*args, **kwds``, but in fact it is only supposed to be called
    with the arguments requested by the underlying undecorated
    method. We saw an easy example above, namely ``I.groebner_basis``.
    Here is a more difficult one::

        sage: # needs sage.misc.cython
        sage: cython_code = [
        ....: \'cdef class MyClass:\',
        ....: \'    def _sage_src_(self):\',
        ....: \'        return "def foo(x, a=\\\\\\\')\\\\\\"\\\\\\\', b={(2+1):\\\\\\\'bar\\\\\\\', not 1:3, 3<<4:5}): return\\\\n"\',
        ....: \'    def __call__(self, m, n): return "something"\']
        sage: cython(\'\\n\'.join(cython_code))
        sage: O = MyClass()
        sage: print(sage.misc.sageinspect.sage_getsource(O))
        def foo(x, a=\')"\', b={(2+1):\'bar\', not 1:3, 3<<4:5}): return
        sage: spec = sage.misc.sageinspect.sage_getargspec(O)
        sage: spec.args, spec.varargs, spec.varkw
        ([\'x\', \'a\', \'b\'], None, None)
        sage: spec.defaults[0]
        \')"\'
        sage: sorted(spec.defaults[1].items(), key=lambda x: str(x))
        [(3, \'bar\'), (48, 5), (False, 3)]
        sage: sage.misc.sageinspect.sage_getargspec(O.__call__)
        FullArgSpec(args=[\'self\', \'m\', \'n\'], varargs=None, varkw=None, defaults=None,
                    kwonlyargs=[], kwonlydefaults=None, annotations={})

    ::

        sage: cython(\'def foo(x, a=\\\'\\\\\\\')"\\\', b={not (2+1==3):\\\'bar\\\'}): return\')      # needs sage.misc.cython
        sage: print(sage.misc.sageinspect.sage_getsource(foo))                          # needs sage.misc.cython
        def foo(x, a=\'\\\')"\', b={not (2+1==3):\'bar\'}): return
        <BLANKLINE>
        sage: sage.misc.sageinspect.sage_getargspec(foo)                                # needs sage.misc.cython
        FullArgSpec(args=[\'x\', \'a\', \'b\'], varargs=None, varkw=None,
                    defaults=(\'\\\')"\', {False: \'bar\'}),
                    kwonlyargs=[], kwonlydefaults=None, annotations={})

    The following produced a syntax error before the patch at :issue:`11913`,
    see also :issue:`26906`::

        sage: sage.misc.sageinspect.sage_getargspec(r.lm)       # optional - rpy2
        FullArgSpec(args=[\'self\'], varargs=\'args\', varkw=\'kwds\', defaults=None,
                    kwonlyargs=[], kwonlydefaults=None, annotations={})

    The following was fixed in :issue:`16309`::

        sage: # needs sage.misc.cython
        sage: cython(
        ....: \'\'\'
        ....: class Foo:
        ....:     @staticmethod
        ....:     def join(categories, bint as_list=False, tuple ignore_axioms=(), tuple axioms=()): pass
        ....: cdef class Bar:
        ....:     @staticmethod
        ....:     def join(categories, bint as_list=False, tuple ignore_axioms=(), tuple axioms=()): pass
        ....:     cpdef meet(categories, bint as_list=False, tuple ignore_axioms=(), tuple axioms=()): pass
        ....: \'\'\')
        sage: sage_getargspec(Foo.join)
        FullArgSpec(args=[\'categories\', \'as_list\', \'ignore_axioms\', \'axioms\'], varargs=None, varkw=None,
                    defaults=(False, (), ()), kwonlyargs=[], kwonlydefaults=None, annotations={})
        sage: sage_getargspec(Bar.join)
        FullArgSpec(args=[\'categories\', \'as_list\', \'ignore_axioms\', \'axioms\'], varargs=None, varkw=None,
                    defaults=(False, (), ()), kwonlyargs=[], kwonlydefaults=None, annotations={})
        sage: sage_getargspec(Bar.meet)
        FullArgSpec(args=[\'categories\', \'as_list\', \'ignore_axioms\', \'axioms\'], varargs=None, varkw=None,
                    defaults=(False, (), ()), kwonlyargs=[], kwonlydefaults=None, annotations={})

    Test that :issue:`17009` is fixed::

        sage: sage_getargspec(gap)                                                      # needs sage.libs.gap
        FullArgSpec(args=[\'self\', \'x\', \'name\'], varargs=None, varkw=None,
                    defaults=(None,), kwonlyargs=[], kwonlydefaults=None, annotations={})

    By :issue:`17814`, the following gives the correct answer (previously, the
    defaults would have been found ``None``)::

        sage: from sage.misc.nested_class import MainClass
        sage: sage_getargspec(MainClass.NestedClass.NestedSubClass.dummy)
        FullArgSpec(args=[\'self\', \'x\', \'r\'], varargs=\'args\', varkw=\'kwds\',
                    defaults=((1, 2, 3.4),), kwonlyargs=[], kwonlydefaults=None, annotations={})

    In :issue:`18249` was decided to return a generic signature for Python
    builtin functions, rather than to raise an error (which is what Python\'s
    inspect module does)::

        sage: import inspect
        sage: sage_getargspec(range)
        FullArgSpec(args=[], varargs=\'args\', varkw=\'kwds\', defaults=None, kwonlyargs=[], kwonlydefaults=None, annotations={})

    Test that :issue:`28524` is fixed::

        sage: from sage.repl.interpreter import get_test_shell
        sage: shell = get_test_shell()
        sage: shell.run_cell(
        ....:     \'class Foo:\\n\'
        ....:     \'    def __call__(self):\\n\'
        ....:     \'        return None\\n\'
        ....:     \'    def __module__(self):\\n\'
        ....:     \'        return "sage.misc.sageinspect"\\n\'
        ....:     \'    def _sage_src_(self):\\n\'
        ....:     \'        return "the source code string"\')
        sage: shell.run_cell(\'f = Foo()\')
        sage: shell.run_cell(\'f??\')
        ...the source code string...
    '''
def sage_signature(obj):
    '''
    Return the names and default values of a function\'s arguments.

    INPUT:

    - ``obj`` -- any callable object

    OUTPUT:

    A :class:`Signature` is returned, as specified by the
    Python library function :func:`inspect.signature`.


    .. NOTE::

        Currently the type information is not returned, because the output
        is converted from the return value of :func:`sage_getargspec`.
        This should be changed in the future.

    EXAMPLES::

        sage: from sage.misc.sageinspect import sage_signature
        sage: def f(x, y, z=1, t=2, *args, **keywords):
        ....:     pass
        sage: sage_signature(f)
        <Signature (x, y, z=1, t=2, *args, **keywords)>

    We now run :func:`sage_signature` on some functions from the Sage library::

        sage: sage_signature(identity_matrix)                                          # needs sage.modules
        <Signature (ring, n=0, sparse=False)>
        sage: sage_signature(factor)
        <Signature (n, proof=None, int_=False, algorithm=\'pari\', verbose=0, **kwds)>

    In the case of a class or a class instance, the :class:`Signature` of the
    ``__new__``, ``__init__`` or ``__call__`` method is returned::

        sage: P.<x,y> = QQ[]
        sage: sage_signature(P)                                                        # needs sage.libs.singular
        <Signature (base_ring, n, names, order=\'degrevlex\')>
        sage: sage_signature(P.__class__)                                              # needs sage.libs.singular
        <Signature (self, x=0, *args, **kwds)>

    The following tests against various bugs that were fixed in
    :issue:`9976`::

        sage: from sage.rings.polynomial.real_roots import bernstein_polynomial_factory_ratlist     # needs sage.modules
        sage: sage_signature(bernstein_polynomial_factory_ratlist.coeffs_bitsize)                  # needs sage.modules
        <Signature (self)>
        sage: from sage.rings.polynomial.pbori.pbori import BooleanMonomialMonoid       # needs sage.rings.polynomial.pbori
        sage: sage_signature(BooleanMonomialMonoid.gen)                                # needs sage.rings.polynomial.pbori
        <Signature (self, i=0)>
        sage: I = P*[x,y]
        sage: sage_signature(I.groebner_basis)                                         # needs sage.libs.singular
        <Signature (self, algorithm=\'\', deg_bound=None, mult_bound=None, prot=False, *args, **kwds)>
        sage: cython("cpdef int foo(x,y) except -1: return 1")                          # needs sage.misc.cython
        sage: sage_signature(foo)                                                      # needs sage.misc.cython
        <Signature (x, y)>

    If a :func:`functools.partial` instance is involved, we see no other meaningful solution
    than to return the signature of the underlying function::

        sage: def f(a, b, c, d=1):
        ....:     return a + b + c + d
        sage: import functools
        sage: f1 = functools.partial(f, 1, c=2)
        sage: sage_signature(f1)
        <Signature (a, b, c, d=1)>
    '''
def formatannotation(annotation, base_module=None):
    """
    This is taken from Python 3.7's inspect.py; the only change is to
    add documentation.

    INPUT:

    - ``annotation`` -- annotation for a function
    - ``base_module`` -- (default: ``None``)

    This is only relevant with Python 3, so the doctests are marked
    accordingly.

    EXAMPLES::

        sage: from sage.misc.sageinspect import formatannotation
        sage: import inspect
        sage: def foo(a, *, b:int, **kwargs):
        ....:     pass
        sage: s = inspect.signature(foo)

        sage: a = s.parameters['a'].annotation
        sage: a
        <class 'inspect._empty'>
        sage: formatannotation(a)
        'inspect._empty'

        sage: b = s.parameters['b'].annotation
        sage: b
        <class 'int'>
        sage: formatannotation(b)
        'int'
    """
def sage_formatargspec(args, varargs=None, varkw=None, defaults=None, kwonlyargs=(), kwonlydefaults=None, annotations={}, formatarg=..., formatvarargs=None, formatvarkw=None, formatvalue=None, formatreturns=None, formatannotation=None):
    """
    Format an argument spec from the values returned by getfullargspec.

    The first seven arguments are (args, varargs, varkw, defaults,
    kwonlyargs, kwonlydefaults, annotations).  The other five arguments
    are the corresponding optional formatting functions that are called to
    turn names and values into strings.  The last argument is an optional
    function to format the sequence of arguments.

    This is taken from Python 3.7's inspect.py, where it is
    deprecated. The only change, aside from documentation (this
    paragraph and the next, plus doctests), is to remove the
    deprecation warning.

    Sage uses this function to format arguments, as obtained by
    :func:`sage_getargspec`. Since :func:`sage_getargspec` works for
    Cython functions while Python's inspect module does not, it makes
    sense to keep this function for formatting instances of
    ``inspect.FullArgSpec``.

    EXAMPLES::

        sage: from sage.misc.sageinspect import sage_formatargspec
        sage: args = ['a', 'b', 'c']
        sage: defaults = [3]
        sage: sage_formatargspec(args, defaults=defaults)
        '(a, b, c=3)'
    """
def sage_getdef(obj, obj_name: str = ''):
    """
    Return the definition header for any callable object.

    INPUT:

    - ``obj`` -- function
    - ``obj_name`` -- string (default: ``''``); prepended to the output

    EXAMPLES::

        sage: from sage.misc.sageinspect import sage_getdef
        sage: sage_getdef(identity_matrix)                                              # needs sage.modules
        '(ring, n=0, sparse=False)'
        sage: sage_getdef(identity_matrix, 'identity_matrix')                           # needs sage.modules
        'identity_matrix(ring, n=0, sparse=False)'

    Check that :issue:`6848` has been fixed::

        sage: sage_getdef(RDF.random_element)
        '(min=-1, max=1)'

    If an exception is generated, None is returned instead and the
    exception is suppressed.
    """
def sage_getdoc_original(obj):
    """
    Return the unformatted docstring associated to ``obj`` as a
    string.

    If ``obj`` is a Cython object with an embedded position or signature in
    its docstring, the embedded information is stripped. If the stripped
    docstring is empty, then the stripped docstring of ``obj.__init__`` is
    returned instead.

    Feed the results from this into the function
    :func:`sage.misc.sagedoc.format` for printing to the screen.

    INPUT:

    - ``obj`` -- a function, module, etc.: something with a docstring

    EXAMPLES::

        sage: from sage.misc.sageinspect import sage_getdoc_original

    Here is a class that has its own docstring::

        sage: print(sage_getdoc_original(sage.rings.integer.Integer))
        <BLANKLINE>
            The :class:`Integer` class represents arbitrary precision
            integers. It derives from the :class:`Element` class, so
            integers can be used as ring elements anywhere in Sage.
        ...

    If the class does not have a docstring, the docstring of the
    ``__init__`` method is used, but not the ``__init__`` method
    of the base class (this was fixed in :issue:`24936`)::

        sage: from sage.categories.category import Category
        sage: class A(Category):
        ....:     def __init__(self):
        ....:         '''The __init__ docstring'''
        sage: sage_getdoc_original(A)
        'The __init__ docstring'
        sage: class B(Category):
        ....:     pass
        sage: sage_getdoc_original(B)
        ''

    Old-style classes are supported::

        sage: class OldStyleClass:
        ....:     def __init__(self):
        ....:         '''The __init__ docstring'''
        ....:         pass
        sage: print(sage_getdoc_original(OldStyleClass))
        The __init__ docstring

    When there is no ``__init__`` method, we just get an empty string::

        sage: class OldStyleClass:
        ....:     pass
        sage: sage_getdoc_original(OldStyleClass)
        ''

    If an instance of a class does not have its own docstring, the docstring
    of its class results::

        sage: sage_getdoc_original(sage.plot.colors.aliceblue) == sage_getdoc_original(sage.plot.colors.Color)          # needs sage.plot
        True
    """
def sage_getdoc(obj, obj_name: str = '', embedded: bool = False):
    '''
    Return the docstring associated to ``obj`` as a string.

    If ``obj`` is a Cython object with an embedded position in its
    docstring, the embedded position is stripped.

    The optional boolean argument ``embedded`` controls the
    string formatting. It is False by default.

    INPUT:

    - ``obj`` -- a function, module, etc.: something with a docstring

    EXAMPLES::

        sage: from sage.misc.sageinspect import sage_getdoc
        sage: sage_getdoc(identity_matrix)[87:124]                                      # needs sage.modules
        \'...the n x n identity matrix...\'
        sage: def f(a, b, c, d=1): return a+b+c+d
        ...
        sage: import functools
        sage: f1 = functools.partial(f, 1,c=2)
        sage: f.__doc__ = "original documentation"
        sage: f1.__doc__ = "specialised documentation"
        sage: sage_getdoc(f)
        \'original documentation\\n\'
        sage: sage_getdoc(f1)
        \'specialised documentation\\n\'
    '''
def sage_getsource(obj):
    """
    Return the source code associated to obj as a string, or None.

    INPUT:

    - ``obj`` -- function, etc.

    EXAMPLES::

        sage: from sage.misc.sageinspect import sage_getsource
        sage: sage_getsource(identity_matrix)[19:60]                                    # needs sage.modules
        'identity_matrix(ring, n=0, sparse=False):'
        sage: sage_getsource(identity_matrix)[19:60]                                    # needs sage.modules
        'identity_matrix(ring, n=0, sparse=False):'
    """
def sage_getsourcelines(obj):
    '''
    Return a pair ([source_lines], starting line number) of the source
    code associated to obj, or None.

    INPUT:

    - ``obj`` -- function, etc.

    OUTPUT:

    (source_lines, lineno) or None: ``source_lines`` is a list of
    strings, and ``lineno`` is an integer.

    EXAMPLES::

        sage: from sage.misc.sageinspect import sage_getsourcelines

        sage: # needs sage.modules
        sage: sage_getsourcelines(matrix)[1]
        21
        sage: sage_getsourcelines(matrix)[0][0]
        \'def matrix(*args, **kwds):\\n\'

    Some classes customize this using a ``_sage_src_lines_`` method,
    which gives the source lines of a class instance, but not the class
    itself. We demonstrate this for :class:`CachedFunction`::

        sage: # needs sage.combinat
        sage: cachedfib = cached_function(fibonacci)
        sage: sage_getsourcelines(cachedfib)[0][0]
        "def fibonacci(n, algorithm=\'pari\') -> Integer:\\n"
        sage: sage_getsourcelines(type(cachedfib))[0][0]
        \'cdef class CachedFunction():\\n\'

    TESTS::

        sage: # needs sage.misc.cython
        sage: cython(\'\'\'cpdef test_funct(x, y): return\'\'\')
        sage: sage_getsourcelines(test_funct)
        ([\'cpdef test_funct(x, y): return\\n\'], 1)

    The following tests that an instance of ``functools.partial`` is correctly
    dealt with (see :issue:`9976`)::

        sage: from sage.tests.functools_partial_src import test_func
        sage: sage_getsourcelines(test_func)
        ([\'def base(x):\\n\',
        ...
        \'    return x\\n\'], 8)

    Here are some cases that were covered in :issue:`11298`;
    note that line numbers may easily change, and therefore we do
    not test them::

        sage: P.<x,y> = QQ[]
        sage: I = P*[x,y]
        sage: sage_getsourcelines(P)                                                    # needs sage.libs.singular
        ([\'cdef class MPolynomialRing_libsingular(MPolynomialRing_base):\\n\',
          \'\\n\',
          \'    def __cinit__(self):\\n\',
        ...)
        sage: sage_getsourcelines(I)                                                    # needs sage.libs.singular
        ([...\'class MPolynomialIdeal(MPolynomialIdeal_singular_repr,\\n\',
        ...)
        sage: x = var(\'x\')                                                              # needs sage.symbolic
        sage: lines, lineno = sage_getsourcelines(x); lines[0:5]                        # needs sage.symbolic
        [\'cdef class Expression(...):\\n\',
         \'\\n\',
         \'    cdef GEx _gobj\\n\',
         \'\\n\',
         \'    cpdef object pyobject(self):\\n\']
        sage: lines[-1]    # last line                                                  # needs sage.symbolic
        \'        return S\\n\'

    We show some enhancements provided by :issue:`11768`. First, we
    use a dummy parent class that has defined an element class by a
    nested class definition::

        sage: from sage.misc.test_nested_class import TestNestedParent
        sage: from sage.misc.sageinspect import sage_getsource
        sage: P = TestNestedParent()
        sage: E = P.element_class
        sage: E.__bases__
        (<class \'sage.misc.test_nested_class.TestNestedParent.Element\'>,
         <class \'sage.categories.sets_cat.Sets.element_class\'>)
        sage: print(sage_getsource(E))
            class Element:
                "This is a dummy element class"
                pass
        sage: print(sage_getsource(P))
        class TestNestedParent(UniqueRepresentation, Parent):
            ...
            class Element:
                "This is a dummy element class"
                pass

    Here is another example that relies on a nested class definition
    in the background::

        sage: C = AdditiveMagmas()
        sage: HC = C.Homsets()
        sage: sage_getsourcelines(HC)
        ([\'    class Homsets(HomsetsCategory):\\n\', ...], ...)

    Testing against a bug that has occurred during work on :issue:`11768`::

        sage: P.<x,y> = QQ[]
        sage: I = P*[x,y]
        sage: sage_getsourcelines(I)
        ([...\'class MPolynomialIdeal(MPolynomialIdeal_singular_repr,\\n\',
          \'                       MPolynomialIdeal_macaulay2_repr,\\n\',
          \'                       MPolynomialIdeal_magma_repr,\\n\',
          \'                       Ideal_generic):\\n\',
          \'    def __init__(self, ring, gens, coerce=True):\\n\',
          ...)
    '''
def sage_getvariablename(self, omit_underscore_names: bool = True):
    '''
    Attempt to get the name of a Sage object.

    INPUT:

    - ``self`` -- any object

    - ``omit_underscore_names`` -- boolean (default: ``True``)

    OUTPUT:

    If the user has assigned an object ``obj`` to a variable name,
    then return that variable name.  If several variables point to
    ``obj``, return a sorted list of those names.  If
    ``omit_underscore_names`` is ``True`` (the default) then omit names
    starting with an underscore "_".

    EXAMPLES::

        sage: # needs sage.modules
        sage: from sage.misc.sageinspect import sage_getvariablename
        sage: A = random_matrix(ZZ, 100)
        sage: sage_getvariablename(A)
        \'A\'
        sage: B = A
        sage: sage_getvariablename(A)
        [\'A\', \'B\']

    If an object is not assigned to a variable, an empty list is returned::

        sage: sage_getvariablename(random_matrix(ZZ, 60))                               # needs sage.modules
        []
    '''
def find_object_modules(obj):
    """
    Return a dictionary whose keys are the names of the modules where ``obj``
    appear and the value at a given module name is the list of names that
    ``obj`` have in that module.

    It is very unlikely that the output dictionary has several keys except when
    ``obj`` is an instance of a class.

    EXAMPLES::

        sage: from sage.misc.sageinspect import find_object_modules
        sage: find_object_modules(RR)                                                   # needs sage.rings.real_mpfr
        {'sage.rings.real_mpfr': ['RR']}
        sage: find_object_modules(ZZ)
        {'sage.rings.integer_ring': ['Z', 'ZZ']}
    """
