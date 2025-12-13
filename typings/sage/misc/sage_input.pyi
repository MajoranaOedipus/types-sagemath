from sage.misc.lazy_import import lazy_import as lazy_import

def sage_input(x, preparse: bool = True, verify: bool = False, allow_locals: bool = False):
    """
    Return a sequence of commands that can be used to rebuild the object ``x``.

    INPUT:

    - ``x`` -- the value we want to find an input form for

    - ``preparse`` -- (default: ``True``) whether to generate code that requires
      the preparser.  With ``True``, generated code requires the preparser.
      With ``False``, generated code requires that the preparser not be used.
      With ``None``, generated code will work whether or not the preparser is
      used.

    - ``verify`` -- (default: ``False``) if ``True``, then the answer will be
      evaluated with :func:`sage_eval`, and an exception will be raised if the
      result is not equal to the original value.  (In fact, for ``verify=True``,
      :func:`sage_input` is effectively run three times, with ``preparse`` set
      to ``True``, ``False``, and ``None``, and all three results are checked.)
      This is particularly useful for doctests.

    - ``allow_locals`` -- (default: ``False``) if ``True``, then values that
      :func:`sage_input` cannot handle are returned in a dictionary, and the
      returned code assumes that this dictionary is passed as the ``locals``
      parameter of :func:`sage_eval`.  (Otherwise, if :func:`sage_input` cannot
      handle a value, an exception is raised.)

    EXAMPLES::

        sage: sage_input(GF(2)(1))
        GF(2)(1)
        sage: sage_input((GF(2)(0), GF(2)(1)), verify=True)
        # Verified
        GF_2 = GF(2)
        (GF_2(0), GF_2(1))

    When the preparser is enabled, we use the \\sage generator syntax.::

        sage: K.<x> = GF(5)[]
        sage: sage_input(x^3 + 2*x, verify=True)
        # Verified
        R.<x> = GF(5)[]
        x^3 + 2*x
        sage: sage_input(x^3 + 2*x, preparse=False)
        R = GF(5)['x']
        x = R.gen()
        x**3 + 2*x

    The result of :func:`sage_input` is actually a pair of strings with a
    special ``__repr__`` method to print nicely.::

        sage: # needs sage.rings.real_mpfr sage.symbolic
        sage: r = sage_input(RealField(20)(pi), verify=True)
        sage: r
        # Verified
        RealField(20)(3.1415939)
        sage: isinstance(r, tuple)
        True
        sage: len(r)
        2
        sage: tuple(r)
        ('# Verified\\n', 'RealField(20)(3.1415939)')

    We cannot find an input form for a function.::

        sage: sage_input((3, lambda x: x))
        Traceback (most recent call last):
        ...
        ValueError: cannot convert <function <lambda> at 0x...> to sage_input form

    But we can have :func:`sage_input` continue anyway, and return an input form
    for the rest of the expression, with ``allow_locals=True``.::

        sage: r = sage_input((3, lambda x: x), verify=True, allow_locals=True)
        sage: r
        LOCALS:
            _sil1: <function <lambda> at 0x...>
        # Verified
        (3, _sil1)
        sage: tuple(r)
        ('# Verified\\n', '(3, _sil1)', {'_sil1': <function <lambda> at 0x...>})
    """

class SageInputBuilder:
    """
    An instance of this class is passed to ``_sage_input_`` methods.
    It keeps track of the current state of the ``_sage_input_`` process,
    and contains many utility methods for building :class:`SageInputExpression`
    objects.

    In normal use, instances of :class:`SageInputBuilder` are created
    internally by :func:`sage_input`, but it may be useful to create
    an instance directly for testing or doctesting.

    EXAMPLES::

        sage: from sage.misc.sage_input import SageInputBuilder

    We can create a :class:`SageInputBuilder`, use it to create some
    :class:`SageInputExpression` s, and get a result.  (As mentioned
    above, this is only useful for testing or doctesting; normally
    you would just use :func:`sage_input`.)::

        sage: sib = SageInputBuilder()
        sage: sib.result((sib(3) + sib(4)) * (sib(5) + sib(6)))
        (3 + 4)*(5 + 6)
    """
    def __init__(self, allow_locals: bool = False, preparse: bool = True) -> None:
        """
        Initialize an instance of :class:`SageInputBuilder`.

        In normal use, instances of :class:`SageInputBuilder` are created
        internally by :func:`sage_input`, but it may be useful to create
        an instance directly for testing or doctesting.

        INPUT:

        - ``allow_locals`` -- (default: ``False``) if true, then values
          that cannot be converted to input form will be stored in
          a dictionary, which must be passed as the ``locals``
          when evaluating the result.

        - ``preparse`` -- (default: ``True``) if true, then the result
          will assume that the preparser is enabled.  If false, then
          the result will assume that the preparser is disabled.
          If ``None``, then the result will work whether or
          not the preparser is enabled.

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder
            sage: SageInputBuilder().preparse()
            True
            sage: SageInputBuilder(preparse=False).preparse()
            False
        """
    def __call__(self, x, coerced: bool = False):
        '''
        Try to convert an arbitrary value ``x`` into a
        :class:`SageInputExpression` (an SIE).

        We first check to see if an SIE has been cached for ``x``;
        if so, we return it.  If ``x`` is already an SIE, we return
        it unchanged.

        If ``x`` has a \\method{_sage_input_} method, we call that
        method.

        Otherwise, if ``x`` is a value of some Python type that
        we know how to deal with, we convert it directly.

        Finally, for values we don\'t know how to convert, if
        ``self._allow_locals`` is true, we add it to a
        ``locals`` dictionary.

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder

            sage: sib = SageInputBuilder()
            sage: sib.result(sib(sib(3)))
            3

            sage: sib = SageInputBuilder()
            sage: sib.result(sib(GF(17)(5)))
            GF(17)(5)

        The argument ``coerced=True`` or ``coerced=2`` will get
        passed to the \\method{_sage_input_} method of the argument.::

            sage: sib = SageInputBuilder()
            sage: sib.result(sib(GF(17)(5), True))
            5
            sage: sib.result(sib(RealField(200)(1.5), True))                            # needs sage.rings.real_mpfr
            1.5000000000000000000000000000000000000000000000000000000000000
            sage: sib.result(sib(RealField(200)(1.5), 2))                               # needs sage.rings.real_mpfr
            1.5

        Since :func:`sage_input` directly calls this method, all
        of the following are indirect doctests.::

            sage: sage_input(True)
            True
            sage: sage_input(-5r, verify=True)
            # Verified
            -5r
            sage: sage_input(7r, preparse=False, verify=True)
            # Verified
            7
            sage: sage_input(-11r, preparse=None, verify=True)
            # Verified
            -int(11)
            sage: sage_input(float(-infinity), preparse=True, verify=True)
            # Verified
            -float(infinity)
            sage: sage_input(float(NaN), preparse=True, verify=True)                    # needs sage.symbolic
            # Verified
            float(NaN)
            sage: sage_input(float(-pi), preparse=True, verify=True)                    # needs sage.symbolic
            # Verified
            float(-RR(3.1415926535897931))
            sage: sage_input(float(42), preparse=True, verify=True)                     # needs sage.rings.real_mpfr
            # Verified
            float(42)
            sage: sage_input("Hello, world\\n", verify=True)
            # Verified
            \'Hello, world\\n\'
            sage: sage_input("\'", verify=True)
            # Verified
            "\'"
            sage: sage_input(\'"\', verify=True)
            # Verified
            \'"\'
            sage: sage_input(\'\'\' "\'Hi,\' she said." \'\'\', verify=True)
            # Verified
            \' "\\\'Hi,\\\' she said." \'
            sage: sage_input(\'Icky chars: \\0\\n\\t\\b\\\'\\"\\200\\300\\234\', verify=True)
            # Verified
            \'Icky chars: \\x00\\n\\t\\x08\\\'"\\x80\\xc0\\x9c\'
            sage: sage_input(\'unicode with spectral: \\u1234\\U00012345\', verify=True)
            # Verified
            \'unicode with spectral: \\u1234\\U00012345\'
            sage: sage_input((2, 3.5, \'Hi\'), verify=True)                               # needs sage.rings.real_mpfr
            # Verified
            (2, 3.5, \'Hi\')
            sage: sage_input(lambda x: x)
            Traceback (most recent call last):
            ...
            ValueError: cannot convert <function <lambda> at 0x...> to sage_input form
            sage: sage_input(lambda x: x, allow_locals=True, verify=True)
            LOCALS:
              _sil1: <function <lambda> at 0x...>
            # Verified
            _sil1
        '''
    def preparse(self):
        """
        Check the preparse status.

        It returns ``True`` if the preparser will be enabled, ``False`` if it
        will be disabled, and ``None`` if the result must work whether or not
        the preparser is enabled.

        For example, this is useful in the \\method{_sage_input_}
        methods of :class:`~sage.rings.integer.Integer` and :class:`RealNumber`; but most
        \\method{_sage_input_} methods will not need to examine this.

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder
            sage: SageInputBuilder().preparse()
            True
            sage: SageInputBuilder(preparse=False).preparse()
            False
        """
    def int(self, n):
        """
        Return a raw SIE from the integer ``n``.

        As it is raw, it may read back as a Sage Integer or a Python int,
        depending on its size and whether the preparser is enabled.

        INPUT:

        - ``n`` -- a Sage Integer or a Python int

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder

            sage: sib = SageInputBuilder()
            sage: sib.result(sib.int(-3^50))
            -717897987691852588770249

            sage: sib = SageInputBuilder()
            sage: sib.result(sib.int(-42r))
            -42
        """
    def float_str(self, n):
        """
        Given a string representing a floating-point number,
        produces a :class:`SageInputExpression` that formats as that
        string.

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder

            sage: sib = SageInputBuilder()
            sage: sib.result(sib.float_str(repr(RR(e))))                                # needs sage.symbolic
            2.71828182845905
        """
    def name(self, n):
        """
        Given a string representing a Python name,
        produces a :class:`SageInputExpression` for that name.

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder

            sage: sib = SageInputBuilder()
            sage: sib.result(sib.name('pi') + sib.name('e'))
            pi + e
        """
    def cache(self, x, sie, name) -> None:
        """
        INPUT:

        - ``x`` -- an arbitrary value

        - ``sie`` -- a :class:`SageInputExpression`

        - ``name`` -- a requested variable name

        Enters ``x`` and ``sie`` in a cache, so that subsequent calls
        ``self(x)`` will directly return ``sie``.  Also, marks the
        requested name of this ``sie`` to be ``name``.

        This should almost always be called as part of the
        \\method{_sage_input_} method of a parent.  It may also be called
        on values of an arbitrary type, which may be useful if the values
        are both large and likely to be used multiple times in a single
        expression.

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder

            sage: sib = SageInputBuilder()
            sage: sie42 = sib(GF(101)(42))
            sage: sib.cache(GF(101)(42), sie42, 'the_ultimate_answer')
            sage: sib.result(sib(GF(101)(42)) + sib(GF(101)(42)))
            the_ultimate_answer = GF(101)(42)
            the_ultimate_answer + the_ultimate_answer

        Note that we don't assign the result to a variable if the value
        is only used once.::

            sage: sib = SageInputBuilder()
            sage: sie42 = sib(GF(101)(42))
            sage: sib.cache(GF(101)(42), sie42, 'the_ultimate_answer')
            sage: sib.result(sib(GF(101)(42)) + sib(GF(101)(43)))
            GF_101 = GF(101)
            GF_101(42) + GF_101(43)
        """
    def id_cache(self, x, sie, name) -> None:
        '''
        INPUT:

        - ``x`` -- an arbitrary value

        - ``sie`` -- a :class:`SageInputExpression`

        - ``name`` -- a requested variable name

        Enters ``x`` and ``sie`` in a cache, so that subsequent calls
        ``self(x)`` will directly return ``sie``.  Also, marks the
        requested name of this ``sie`` to be ``name``.  Differs from
        the \\method{cache} method in that the cache is keyed by
        ``id(x)`` instead of by ``x``.

        This may be called on values of an arbitrary type, which may
        be useful if the values are both large and likely to be used
        multiple times in a single expression; it should be preferred to
        \\method{cache} if equality on the values is difficult or impossible
        to compute.

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder

            sage: x = polygen(ZZ)
            sage: sib = SageInputBuilder()
            sage: my_42 = 42*x
            sage: sie42 = sib(my_42)
            sage: sib.id_cache(my_42, sie42, \'the_ultimate_answer\')
            sage: sib.result(sib(my_42) + sib(my_42))
            R.<x> = ZZ[]
            the_ultimate_answer = 42*x
            the_ultimate_answer + the_ultimate_answer

        Since id_cache keys off of object identity ("is"), the
        following does not trigger the cache.::

            sage: sib.result(sib(42*x) + sib(42*x))
            42*x + 42*x

        Note that we don\'t assign the result to a variable if the value
        is only used once.::

            sage: sib = SageInputBuilder()
            sage: my_42 = 42*x
            sage: sie42 = sib(my_42)
            sage: sib.id_cache(my_42, sie42, \'the_ultimate_answer\')
            sage: sib.result(sib(my_42) + sib(43*x))
            R.<x> = ZZ[]
            42*x + 43*x
        '''
    def import_name(self, module, name, alt_name=None):
        """
        INPUT:

        - ``module``, ``name``, ``alt_name`` -- strings

        Creates an expression that will import a name from a module and
        then use that name.

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder

            sage: sib = SageInputBuilder()
            sage: v1 = sib.import_name('sage.foo.bar', 'baz')
            sage: v2 = sib.import_name('sage.foo.bar', 'ZZ', 'not_the_real_ZZ')
            sage: sib.result(v1+v2)
            from sage.foo.bar import baz
            from sage.foo.bar import ZZ as not_the_real_ZZ
            baz + not_the_real_ZZ

        We adjust the names if there is a conflict.::

            sage: sib = SageInputBuilder()
            sage: v1 = sib.import_name('sage.foo', 'poly')
            sage: v2 = sib.import_name('sage.bar', 'poly')
            sage: sib.result(v1+v2)
            from sage.foo import poly as poly1
            from sage.bar import poly as poly2
            poly1 + poly2
        """
    def assign(self, e, val):
        """
        Construct a command that performs the assignment ``e=val``.

        Can only be used as an argument to the ``command`` method.

        INPUT:

        - ``e``, ``val`` -- SageInputExpression

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder

            sage: sib = SageInputBuilder()
            sage: circular = sib([None])
            sage: sib.command(circular, sib.assign(circular[0], circular))
            sage: sib.result(circular)
            si = [None]
            si[0] = si
            si
        """
    def command(self, v, cmd) -> None:
        """
        INPUT:

        - ``v``, ``cmd`` -- SageInputExpression

        Attaches a command to v, which will be executed before v is used.
        Multiple commands will be executed in the order added.

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder

            sage: sib = SageInputBuilder()
            sage: incr_list = sib([])
            sage: sib.command(incr_list, incr_list.append(1))
            sage: sib.command(incr_list, incr_list.extend([2, 3]))
            sage: sib.result(incr_list)
            si = []
            si.append(1)
            si.extend([2, 3])
            si
        """
    def dict(self, entries):
        """
        Given a dictionary, or a list of (key, value) pairs,
        produces a :class:`SageInputExpression` representing
        the dictionary.

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder

            sage: sib = SageInputBuilder()
            sage: sib.result(sib.dict({1:1, 2:5/2, 3:100/3}))
            {1:1, 2:5/2, 3:100/3}
            sage: sib.result(sib.dict([('hello', 'sunshine'), ('goodbye', 'rain')]))
            {'hello':'sunshine', 'goodbye':'rain'}
        """
    def getattr(self, sie, attr):
        """
        Given a :class:`SageInputExpression` representing ``foo``
        and an attribute name bar, produce a :class:`SageInputExpression`
        representing ``foo.bar``.  Normally, you could just use
        attribute-access syntax, but that doesn't work if bar
        is some attribute that bypasses __getattr__ (such as if
        bar is '__getattr__' itself).

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder

            sage: sib = SageInputBuilder()
            sage: sib.getattr(ZZ, '__getattr__')
            {getattr: {atomic:ZZ}.__getattr__}
            sage: sib.getattr(sib.name('foo'), '__new__')
            {getattr: {atomic:foo}.__new__}
        """
    def empty_subscript(self, parent):
        """
        Given a :class:`SageInputExpression` representing ``foo``,
        produces a :class:`SageInputExpression` representing ``foo[]``.
        Since this is not legal Python syntax, it is useful only for
        producing the \\sage generator syntax for a polynomial ring.

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder

            sage: sib = SageInputBuilder()
            sage: sib.result(sib.empty_subscript(sib(2) + sib(3)))
            (2 + 3)[]

        The following calls this method indirectly.::

            sage: sage_input(polygen(ZZ['y']))
            R.<x> = ZZ['y'][]
            x
        """
    def use_variable(self, sie, name) -> None:
        """
        Marks the :class:`SageInputExpression` ``sie`` to use a variable
        even if it is only referenced once.  (If ``sie`` is the final
        top-level expression, though, it will not use a variable.)

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder

            sage: sib = SageInputBuilder()
            sage: e = sib.name('MatrixSpace')(ZZ, 10, 10)
            sage: sib.use_variable(e, 'MS')
            sage: sib.result(e.zero_matrix())
            MS = MatrixSpace(ZZ, 10, 10)
            MS.zero_matrix()

        Without the call to use_variable, we get this instead::

            sage: sib = SageInputBuilder()
            sage: e = sib.name('MatrixSpace')(ZZ, 10, 10)
            sage: sib.result(e.zero_matrix())
            MatrixSpace(ZZ, 10, 10).zero_matrix()

        And even with the call to use_variable, we don't use a variable here::

            sage: sib = SageInputBuilder()
            sage: e = sib.name('MatrixSpace')(ZZ, 10, 10)
            sage: sib.use_variable(e, 'MS')
            sage: sib.result(e)
            MatrixSpace(ZZ, 10, 10)
        """
    def share(self, sie) -> None:
        """
        Mark the given expression as sharable, so that it will be replaced
        by a variable if it occurs multiple times in the expression.
        (Most non-single-token expressions are already sharable.)

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder

        Without explicitly using .share(), string literals are not shared::

            sage: sib = SageInputBuilder()
            sage: e = sib('hello')
            sage: sib.result(sib((e, e)))
            ('hello', 'hello')

        See the difference if we use .share()::

            sage: sib = SageInputBuilder()
            sage: e = sib('hello')
            sage: sib.share(e)
            sage: sib.result(sib((e, e)))
            si = 'hello'
            (si, si)
        """
    def parent_with_gens(self, parent, sie, gen_names, name, gens_syntax=None):
        '''
        This method is used for parents with generators, to manage the
        \\sage preparser generator syntax (like ``K.<x> = QQ[]``).

        The \\method{_sage_input_} method of a parent class with
        generators should construct a :class:`SageInputExpression` for
        the parent, and then call this method with the parent itself,
        the constructed SIE, a sequence containing the names of the
        generators, and (optionally) another SIE to use if the \\sage
        generator syntax is used; typically this will be the same as
        the first SIE except omitting a ``names`` parameter.

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder


            sage: def test_setup(use_gens=True, preparse=True):
            ....:     sib = SageInputBuilder(preparse=preparse)
            ....:     gen_names=(\'foo\', \'bar\')
            ....:     parent = "some parent"
            ....:     normal_sie = sib.name(\'make_a_parent\')(names=gen_names)
            ....:     if use_gens:
            ....:         gens_sie = sib.name(\'make_a_parent\')()
            ....:     else:
            ....:         gens_sie = None
            ....:     name = \'the_thing\'
            ....:     result = sib.parent_with_gens(parent, normal_sie,
            ....:                                   gen_names, name,
            ....:                                   gens_syntax=gens_sie)
            ....:     return sib, result

            sage: sib, par_sie = test_setup()
            sage: sib.result(par_sie)
            make_a_parent(names=(\'foo\', \'bar\'))

            sage: sib, par_sie = test_setup()
            sage: sib.result(sib(3) * sib.gen("some parent", 0))
            the_thing.<foo,bar> = make_a_parent()
            3*foo

            sage: sib, par_sie = test_setup(preparse=False)
            sage: sib.result(par_sie)
            make_a_parent(names=(\'foo\', \'bar\'))

            sage: sib, par_sie = test_setup(preparse=False)
            sage: sib.result(sib(3) * sib.gen("some parent", 0))
            the_thing = make_a_parent(names=(\'foo\', \'bar\'))
            foo,bar = the_thing.gens()
            ZZ(3)*foo

            sage: sib, par_sie = test_setup(use_gens=False)
            sage: sib.result(par_sie)
            make_a_parent(names=(\'foo\', \'bar\'))

            sage: sib, par_sie = test_setup(use_gens=False)
            sage: sib.result(sib(3) * sib.gen("some parent", 0))
            the_thing = make_a_parent(names=(\'foo\', \'bar\'))
            foo,bar = the_thing.gens()
            3*foo

            sage: sib, par_sie = test_setup()
            sage: sib.result(par_sie - sib.gen("some parent", 1))
            the_thing.<foo,bar> = make_a_parent()
            the_thing - bar
        '''
    def gen(self, parent, n: int = 0):
        """
        Given a parent, returns a :class:`SageInputExpression` for
        the `n`-th (default: 0) generator of the parent.

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder

            sage: sib = SageInputBuilder()
            sage: sib.result(sib.gen(ZZ['y']))
            R.<y> = ZZ[]
            y
        """
    def prod(self, factors, simplify: bool = False):
        """
        Given a sequence, returns a :class:`SageInputExpression`
        for the product of the elements.

        With ``simplify=True``, performs some simplifications
        first.  If any element is formatted as a string ``'0'``,
        then that element is returned directly.  If any element is
        formatted as a string ``'1'``, then it is removed
        from the sequence (unless it is the only element in the sequence).
        And any negations are removed from the elements and moved to the
        outside of the product.

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder

            sage: sib = SageInputBuilder()
            sage: sib.result(sib.prod([-1, 0, 1, -2]))
            -1*0*1*-2

            sage: sib = SageInputBuilder()
            sage: sib.result(sib.prod([-1, 0, 1, 2], simplify=True))
            0

            sage: sib = SageInputBuilder()
            sage: sib.result(sib.prod([-1, 2, -3, -4], simplify=True))
            -2*3*4

            sage: sib = SageInputBuilder()
            sage: sib.result(sib.prod([-1, 1, -1, -1], simplify=True))
            -1

            sage: sib = SageInputBuilder()
            sage: sib.result(sib.prod([1, 1, 1], simplify=True))
            1
        """
    def sum(self, terms, simplify: bool = False):
        """
        Given a sequence, returns a :class:`SageInputExpression`
        for the product of the elements.

        With ``simplify=True``, performs some simplifications
        first.  If any element is formatted as a string ``'0'``,
        then it is removed from the sequence (unless it is the only
        element in the sequence); and any instances of ``a + -b``
        are changed to ``a - b``.

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder

            sage: sib = SageInputBuilder()
            sage: sib.result(sib.sum([-1, 0, 1, 0, -1]))
            -1 + 0 + 1 + 0 + -1

            sage: sib = SageInputBuilder()
            sage: sib.result(sib.sum([-1, 0, 1, 0, -1], simplify=True))
            -1 + 1 - 1

            sage: sib = SageInputBuilder()
            sage: sib.result(sib.sum([0, 0, 0], simplify=True))
            0
        """
    def result(self, e):
        """
        Given a :class:`SageInputExpression` constructed using ``self``,
        returns a tuple of a list of commands and an expression
        (and possibly a dictionary of local variables) suitable for
        :func:`sage_eval`.

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder

            sage: sib = SageInputBuilder()
            sage: r = sib.result(sib(6) * sib(7)); r
            6*7
            sage: tuple(r)
            ('', '6*7')
        """

class SageInputExpression:
    """
    Subclasses of this class represent expressions for :func:`sage_input`.
    \\sage classes should define a \\method{_sage_input_} method, which
    will return an instance of :class:`SageInputExpression`, created using
    methods of :class:`SageInputBuilder`.

    To the extent possible, operations on :class:`SageInputExpression` objects
    construct a new :class:`SageInputExpression` representing that operation.
    That is, if ``a`` is a :class:`SageInputExpression`, then ``a + b``
    constructs a :class:`SageInputExpression` representing this sum.
    This also works for attribute access, function calls, subscripts, etc.
    Since arbitrary attribute accesses might be used to construct a new
    attribute-access expression, all internal attributes and methods
    have names that begin with ``_sie_`` to reduce the chance of
    collisions.

    It is expected that instances of this class will not be directly
    created outside this module; instead, instances will be created
    using methods of :class:`SageInputBuilder` and :class:`SageInputExpression`.

    Values of type :class:`SageInputExpression` print in a fairly ugly
    way, that reveals the internal structure of the expression tree.
    """
    def __init__(self, sib) -> None:
        """
        Initialize a :class:`SageInputExpression`.

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder
            sage: sib = SageInputBuilder()
            sage: sie = sib(3) # indirect doctest
            sage: sie
            {atomic:3}
            sage: sie._sie_builder is sib
            True
        """
    def __call__(self, *args, **kwargs):
        """
        Given a :class:`SageInputExpression`, build a new
        :class:`SageInputExpression` representing a function call node
        (with ``self`` as the function).

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder
            sage: sib = SageInputBuilder()
            sage: sie = sib(3)
            sage: sie(4)
            {call: {atomic:3}({atomic:4})}
        """
    def __getitem__(self, key):
        """
        Given a :class:`SageInputExpression`, build a new
        :class:`SageInputExpression` representing a subscript expression
        (with ``self`` as the value being subscripted).

        Currently, slices are not supported.

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder
            sage: sib = SageInputBuilder()
            sage: sie = sib(3)
            sage: sie[4]
            {subscr: {atomic:3}[{atomic:4}]}
            sage: sie[sib.name('x'), sib.name('y')]
            {subscr: {atomic:3}[{tuple: ({atomic:x}, {atomic:y})}]}
        """
    def __getattr__(self, attr):
        """
        Given a :class:`SageInputExpression`, build a new
        :class:`SageInputExpression` representing an attribute access.

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder
            sage: sib = SageInputBuilder()
            sage: sie = sib.name('x')
            sage: sie.foo
            {getattr: {atomic:x}.foo}
            sage: sie.foo()
            {call: {getattr: {atomic:x}.foo}()}
        """
    def __pow__(self, other):
        """
        Compute an expression tree for ``self ** other``.

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder
            sage: sib = SageInputBuilder()
            sage: sie = sib(3)
            sage: sie ^ 4
            {binop:** {atomic:3} {atomic:4}}
        """
    def __mul__(self, other):
        """
        Compute an expression tree for ``self * other``.

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder
            sage: sib = SageInputBuilder()
            sage: sie = sib(3)
            sage: sie * 4
            {binop:* {atomic:3} {atomic:4}}
        """
    def __truediv__(self, other):
        """
        Compute an expression tree for ``self / other``.

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder
            sage: sib = SageInputBuilder()
            sage: sie = sib(3)
            sage: sie / 4
            {binop:/ {atomic:3} {atomic:4}}
        """
    def __add__(self, other):
        """
        Compute an expression tree for ``self + other``.

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder
            sage: sib = SageInputBuilder()
            sage: sie = sib(3)
            sage: sie + 4
            {binop:+ {atomic:3} {atomic:4}}
        """
    def __sub__(self, other):
        """
        Compute an expression tree for ``self - other``.

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder
            sage: sib = SageInputBuilder()
            sage: sie = sib(3)
            sage: sie - 4
            {binop:- {atomic:3} {atomic:4}}
        """
    def __neg__(self):
        """
        Compute an expression tree for ``-self``.

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder
            sage: sib = SageInputBuilder()
            sage: sie = sib(3)
            sage: -sie
            {unop:- {atomic:3}}
        """
    def __pos__(self):
        """
        Compute an expression tree for ``+self``.

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder
            sage: sib = SageInputBuilder()
            sage: sie = sib(3)
            sage: +sie
            {unop:+ {atomic:3}}
        """
    def __invert__(self):
        """
        Compute an expression tree for ``~self``.

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder
            sage: sib = SageInputBuilder()
            sage: sie = sib(3)
            sage: ~sie
            {unop:~ {atomic:3}}
        """
    def __abs__(self):
        """
        Compute an expression tree for ``abs(self)``.

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder
            sage: sib = SageInputBuilder()
            sage: sie = sib(3)
            sage: abs(sie)
            {call: {atomic:abs}({atomic:3})}
        """

class SIE_literal(SageInputExpression):
    """
    An abstract base class for ``literals`` (basically, values which
    consist of a single token).

    EXAMPLES::

        sage: from sage.misc.sage_input import SageInputBuilder, SIE_literal

        sage: sib = SageInputBuilder()
        sage: sie = sib(3)
        sage: sie
        {atomic:3}
        sage: isinstance(sie, SIE_literal)
        True
    """

class SIE_literal_stringrep(SIE_literal):
    """
    Values in this class are leaves in a :func:`sage_input` expression
    tree.  Typically they represent a single token, and consist of the
    string representation of that token.  They are used for integer,
    floating-point, and string literals, and for name expressions.

    EXAMPLES::

        sage: from sage.misc.sage_input import SageInputBuilder, SIE_literal_stringrep

        sage: sib = SageInputBuilder()
        sage: isinstance(sib(3), SIE_literal_stringrep)
        True
        sage: isinstance(sib(3.14159, True), SIE_literal_stringrep)                     # needs sage.rings.real_mpfr
        True
        sage: isinstance(sib.name('pi'), SIE_literal_stringrep)
        True
        sage: isinstance(sib(False), SIE_literal_stringrep)
        True
        sage: sib(False)
        {atomic:False}
    """
    def __init__(self, sib, n) -> None:
        """
        Initialize a :class:`SIE_literal_stringrep` value.

        INPUT:

        - ``sib`` -- a :class:`SageInputBuilder`

        - ``n`` -- string; the value to be printed for this expression

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder

            sage: sib = SageInputBuilder()
            sage: sib(3)
            {atomic:3}
            sage: sib(3)._sie_value
            '3'
        """

class SIE_call(SageInputExpression):
    """
    This class represents a function-call node in a :func:`sage_input`
    expression tree.

    EXAMPLES::

        sage: from sage.misc.sage_input import SageInputBuilder

        sage: sib = SageInputBuilder()
        sage: sie = sib.name('GF')
        sage: sie(49)
        {call: {atomic:GF}({atomic:49})}
    """
    def __init__(self, sib, func, args, kwargs) -> None:
        """
        Initialize an instance of :class:`SIE_call`.

        INPUT:

        - ``sib`` -- a :class:`SageInputBuilder`

        - ``func`` -- a :class:`SageInputExpression` representing a function

        - ``args`` -- list of instances of :class:`SageInputExpression`
          representing the positional arguments

        - ``kwargs`` -- dictionary mapping strings to instances of
          :class:`SageInputExpression` representing the keyword arguments

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder

            sage: sib = SageInputBuilder()
            sage: sie = sib('RealField')(53, rnd='RNDZ')
        """

class SIE_subscript(SageInputExpression):
    """
    This class represents a subscript node in a :func:`sage_input`
    expression tree.

    EXAMPLES::

        sage: from sage.misc.sage_input import SageInputBuilder

        sage: sib = SageInputBuilder()
        sage: sie = sib.name('QQ')['x,y']
        sage: sie
        {subscr: {atomic:QQ}[{atomic:'x,y'}]}
    """
    def __init__(self, sib, coll, key) -> None:
        """
        Initialize an instance of :class:`SIE_subscript`.

        INPUT:

        - ``sib`` -- a :class:`SageInputBuilder`

        - ``coll`` -- a :class:`SageInputExpression` representing a collection

        - ``key`` -- a :class:`SageInputExpression` representing the subscript/key

        As a special case, ``key`` may be ``None``; this represents an
        empty subscript.  This is not legal Python syntax, but it is legal
        in the \\sage preparser in examples like ``K.<x> = QQ[]``.

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder

            sage: sib = SageInputBuilder()
            sage: sib.name('QQ')['x']
            {subscr: {atomic:QQ}[{atomic:'x'}]}
            sage: sib.name('x')[1,2,3]
            {subscr: {atomic:x}[{tuple: ({atomic:1}, {atomic:2}, {atomic:3})}]}
            sage: sib.empty_subscript(sib.name('QQ'))
            {subscr: {atomic:QQ}[]}
        """

class SIE_getattr(SageInputExpression):
    """
    This class represents a getattr node in a :func:`sage_input`
    expression tree.

    EXAMPLES::

        sage: from sage.misc.sage_input import SageInputBuilder

        sage: sib = SageInputBuilder()
        sage: sie = sib.name('CC').gen()
        sage: sie
        {call: {getattr: {atomic:CC}.gen}()}
    """
    def __init__(self, sib, obj, attr) -> None:
        """
        Initialize an instance of :class:`SIE_getattr`.

        INPUT:

        - ``sib`` -- a :class:`SageInputBuilder`

        - ``obj`` -- a :class:`SageInputExpression` representing an object

        - ``attr`` -- string; the attribute name

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder

            sage: sib = SageInputBuilder()
            sage: sib.name('QQbar').zeta(5)
            {call: {getattr: {atomic:QQbar}.zeta}({atomic:5})}
        """

class SIE_tuple(SageInputExpression):
    '''
    This class represents a tuple or list node in a :func:`sage_input`
    expression tree.

    EXAMPLES::

        sage: from sage.misc.sage_input import SageInputBuilder

        sage: sib = SageInputBuilder()
        sage: sib((1, \'howdy\'))
        {tuple: ({atomic:1}, {atomic:\'howdy\'})}
        sage: sib(["lists"])
        {list: ({atomic:\'lists\'})}
    '''
    def __init__(self, sib, values, is_list) -> None:
        '''
        Initialize an instance of :class:`SIE_tuple`.

        INPUT:

        - ``sib`` -- a :class:`SageInputBuilder`

        - ``values`` -- list of instances of :class:`SageInputExpression`
          representing the elements of this tuple

        - ``is_list`` -- is ``True`` if this class represents a list, False for a
          tuple

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder

            sage: sib = SageInputBuilder()
            sage: sib((3.5, -2))                                                        # needs sage.rings.real_mpfr
            {tuple: ({atomic:3.5}, {unop:- {atomic:2}})}
            sage: sib(["Hello", "world"])
            {list: ({atomic:\'Hello\'}, {atomic:\'world\'})}
        '''

class SIE_dict(SageInputExpression):
    """
    This class represents a dict node in a :func:`sage_input`
    expression tree.

    EXAMPLES::

        sage: from sage.misc.sage_input import SageInputBuilder

        sage: sib = SageInputBuilder()
        sage: sib.dict([('TeX', RR(pi)), ('Metafont', RR(e))])                          # needs sage.symbolic
        {dict: {{atomic:'TeX'}:{call: {atomic:RR}({atomic:3.1415926535897931})},
                {atomic:'Metafont'}:{call: {atomic:RR}({atomic:2.7182818284590451})}}}
        sage: sib.dict({-40:-40, 0:32, 100:212})
        {dict: {{unop:- {atomic:40}}:{unop:- {atomic:40}},
                {atomic:0}:{atomic:32}, {atomic:100}:{atomic:212}}}
    """
    def __init__(self, sib, entries) -> None:
        """
        Initialize an instance of :class:`SIE_dict`.

        INPUT:

        - ``sib`` -- a :class:`SageInputBuilder`

        - ``entries`` -- list of pairs of :class:`SageInputExpression`
          representing the entries of this dict

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder

            sage: sib = SageInputBuilder()
            sage: sib.dict({'me':'good', 'you':'bad'})
            {dict: {{atomic:'me'}:{atomic:'good'}, {atomic:'you'}:{atomic:'bad'}}}
            sage: sib.dict([(10, 'PS2'), (12, 'PS2'), (13, 'PS3')])
            {dict: {{atomic:10}:{atomic:'PS2'}, {atomic:12}:{atomic:'PS2'}, {atomic:13}:{atomic:'PS3'}}}
        """

class SIE_binary(SageInputExpression):
    """
    This class represents an arithmetic expression with a binary operator
    and its two arguments, in a :func:`sage_input` expression tree.

    EXAMPLES::

        sage: from sage.misc.sage_input import SageInputBuilder

        sage: sib = SageInputBuilder()
        sage: sib(3)+5
        {binop:+ {atomic:3} {atomic:5}}
    """
    def __init__(self, sib, op, lhs, rhs) -> None:
        """
        Initialize an instance of :class:`SIE_binary`.

        INPUT:

        - ``sib`` -- a :class:`SageInputBuilder`

        - ``op`` -- string representing a binary operator, such as '*' or '%'

        - ``lhs`` -- a :class:`SageInputExpression`

        - ``rhs`` -- a :class:`SageInputExpression`

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder

            sage: sib = SageInputBuilder()
            sage: sib(3)*5
            {binop:* {atomic:3} {atomic:5}}
        """

class SIE_unary(SageInputExpression):
    """
    This class represents an arithmetic expression with a unary operator
    and its argument, in a :func:`sage_input` expression tree.

    EXAMPLES::

        sage: from sage.misc.sage_input import SageInputBuilder

        sage: sib = SageInputBuilder()
        sage: -sib(256)
        {unop:- {atomic:256}}
    """
    def __init__(self, sib, op, operand) -> None:
        """
        Initialize an instance of :class:`SIE_unary`.

        INPUT:

        - ``sib`` -- a :class:`SageInputBuilder`

        - ``op`` -- string representing a unary operator, such as '-'

        - ``operand`` -- a :class:`SageInputExpression`

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder

            sage: sib = SageInputBuilder()
            sage: -sib(3)
            {unop:- {atomic:3}}
        """

class SIE_gens_constructor(SageInputExpression):
    '''
    This class represents an expression that can create a \\sage parent
    with named generators, optionally using the \\sage preparser
    generators syntax (like ``K.<x> = QQ[]``).

    EXAMPLES::

        sage: from sage.misc.sage_input import SageInputBuilder

        sage: sib = SageInputBuilder()
        sage: qq = sib.name(\'QQ\')
        sage: sib.parent_with_gens("some parent", qq[\'x\'],
        ....:                      (\'x\',), \'QQx\',
        ....:                      gens_syntax=sib.empty_subscript(qq))
        {constr_parent: {subscr: {atomic:QQ}[{atomic:\'x\'}]} with gens: (\'x\',)}
    '''
    def __init__(self, sib, constr, gen_names, gens_syntax=None) -> None:
        '''
        Initialize an instance of :class:`SIE_gens_constructor`.

        INPUT:

        - ``sib`` -- a :class:`SageInputBuilder`

        - ``constr`` -- a :class:`SageInputExpression` for constructing this
          parent ``normally``

        - ``gen_names`` -- tuple of generator names

        - ``gens_syntax`` -- an optional :class:`SageInputExpression` for
          constructing this parent using the \\sage preparser generators syntax

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder

            sage: sib = SageInputBuilder()
            sage: qq = sib.name(\'QQ\')
            sage: sib.parent_with_gens("some parent", qq[\'x\'],
            ....:                      (\'x\',), \'QQx\',
            ....:                      gens_syntax=sib.empty_subscript(qq))
            {constr_parent: {subscr: {atomic:QQ}[{atomic:\'x\'}]} with gens: (\'x\',)}
        '''

class SIE_gen(SageInputExpression):
    """
    This class represents a named generator of a parent with named
    generators.

    EXAMPLES::

        sage: from sage.misc.sage_input import SageInputBuilder

        sage: sib = SageInputBuilder()
        sage: sib.gen(ZZ['x'])
        {gen:x {constr_parent: {subscr: {atomic:ZZ}[{atomic:'x'}]} with gens: ('x',)}}
    """
    def __init__(self, sib, parent, name) -> None:
        """
        Initialize an instance of :class:`SIE_gen`.

        INPUT:

        - ``sib`` -- a :class:`SageInputBuilder`

        - ``parent`` -- a :class:`SIE_gens_constructor`

        - ``name`` -- string with the name of this generator

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder

            sage: sib = SageInputBuilder()
            sage: sib.gen(ZZ['x']) # indirect doctest
            {gen:x {constr_parent: {subscr: {atomic:ZZ}[{atomic:'x'}]} with gens: ('x',)}}
        """

class SIE_import_name(SageInputExpression):
    """
    This class represents a name which has been imported from a module.

    EXAMPLES::

        sage: from sage.misc.sage_input import SageInputBuilder

        sage: sib = SageInputBuilder()
        sage: sib.import_name('sage.rings.integer', 'make_integer')
        {import:sage.rings.integer/make_integer}
        sage: sib.import_name('sage.foo', 'happy', 'sad')
        {import:sage.foo/happy as sad}
    """
    def __init__(self, sib, module, name, alt_name=None) -> None:
        """
        Initialize an instance of :class:`SIE_import_name`.

        INPUT:

        - ``sib`` -- a :class:`SageInputBuilder`

        - ``module`` -- a module name

        - ``name`` -- an object name

        - ``alt_name`` -- an alternate object name, or None (the default)
                      to use name

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder

            sage: sib = SageInputBuilder()
            sage: sib.import_name('sage.rings.integer', 'make_integer') # indirect doctest
            {import:sage.rings.integer/make_integer}
            sage: sib.import_name('sage.foo', 'happy', 'sad')
            {import:sage.foo/happy as sad}
        """

class SIE_assign(SageInputExpression):
    """
    This class represents an assignment command.

    EXAMPLES::

        sage: from sage.misc.sage_input import SageInputBuilder

        sage: sib = SageInputBuilder()
        sage: sib.assign(sib.name('foo').x, sib.name('pi'))
        {assign: {getattr: {atomic:foo}.x} {atomic:pi}}
    """
    def __init__(self, sib, lhs, rhs) -> None:
        """
        Initialize an instance of :class:`SIE_assign`.

        INPUT:

        - ``sib`` -- a :class:`SageInputBuilder`

        - ``lhs`` -- the left-hand side of the assignment

        - ``rhs`` -- the right-hand side of the assignment

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder

            sage: sib = SageInputBuilder()
            sage: sib.assign(sib.name('foo').x, sib.name('pi'))
            {assign: {getattr: {atomic:foo}.x} {atomic:pi}}
        """

class SageInputFormatter:
    """
    An instance of this class is used to keep track of variable names
    and a sequence of generated commands during the :func:`sage_input`
    formatting process.
    """
    def __init__(self) -> None:
        """
        Initialize an instance of :class:`SageInputFormatter`.

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputFormatter
            sage: sif = SageInputFormatter()
        """
    def format(self, e, prec):
        """
        Format a Sage input expression into a string.

        INPUT:

        - ``e`` -- a :class:`SageInputExpression`

        - ``prec`` -- integer representing a precedence level

        First, we check to see if ``e`` should be replaced by a variable.
        If so, we generate the command to assign the variable, and return
        the name of the variable.

        Otherwise, we format the expression by calling its \\method{_sie_format}
        method, and add parentheses if necessary.

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputBuilder, SageInputFormatter

            sage: sib = SageInputBuilder()
            sage: sif = SageInputFormatter()
            sage: sie = sib(GF(5))

        Here we ``cheat`` by calling \\method{_sie_prepare} twice, to make it
        use a variable.::

            sage: sie._sie_prepare(sif)
            sage: sie._sie_prepare(sif)
            sage: sif._commands
            ''
            sage: sif.format(sie, 0)
            'GF_5'
            sage: sif._commands
            'GF_5 = GF(5)\\n'

        We demonstrate the use of commands, by showing how to construct
        code that will produce a random matrix::

            sage: sib = SageInputBuilder()
            sage: sif = SageInputFormatter()
            sage: sie = sib.name('matrix')(sib.name('ZZ'), 10, 10)
            sage: sib.command(sie, sie.randomize())
            sage: sie._sie_prepare(sif)
            sage: sif._commands
            ''
            sage: sif.format(sie, 0)
            'si'
            sage: sif._commands
            'si = matrix(ZZ, 10, 10)\\nsi.randomize()\\n'
        """
    def register_name(self, name) -> None:
        """
        Register that some value would like to use a given name.
        If only one request for a name is received, then we will use the
        requested name; otherwise, we will add numbers to the end of the
        name to make it unique.

        If the input name is ``None``, then it is treated as a name of
        ``'si'``.

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputFormatter

            sage: sif = SageInputFormatter()
            sage: sif._names, sif._dup_names
            (set(), {})
            sage: sif.register_name('x')
            sage: sif.register_name('y')
            sage: sif._names, sif._dup_names
            ({'x', 'y'}, {})
            sage: sif.register_name('x')
            sage: sif._names, sif._dup_names
            ({'x', 'y'}, {'x': 0})
        """
    def get_name(self, name):
        """
        Return a name corresponding to a given requested name.
        If only one request for a name is received, then we will use the
        requested name; otherwise, we will add numbers to the end of the
        name to make it unique.

        If the input name is ``None``, then it is treated as a name of
        ``'si'``.

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputFormatter

            sage: sif = SageInputFormatter()
            sage: names = ('x', 'x', 'y', 'z')
            sage: for n in names: sif.register_name(n)
            sage: for n in names: sif.get_name(n)
            'x1'
            'x2'
            'y'
            'z'
        """

def verify_same(a, b) -> None:
    """
    Verify that two Sage values are the same.  This is an extended equality
    test; it checks that the values are equal and that their parents are equal.
    (For values which are not Elements, the types are checked instead.)

    If the values are the same, we return ``None``; otherwise,
    we raise an exception.

    EXAMPLES::

        sage: from sage.misc.sage_input import verify_same
        sage: verify_same(1, 1)
        sage: verify_same(1, 2)
        Traceback (most recent call last):
        ...
        AssertionError: Expected 1 == 2
        sage: verify_same(1, 1r)
        Traceback (most recent call last):
        ...
        AttributeError: 'int' object has no attribute 'parent'...
        sage: verify_same(1r, 1)
        Traceback (most recent call last):
        ...
            assert(type(a) == type(b))
        AssertionError
        sage: verify_same(5, GF(7)(5))
        Traceback (most recent call last):
        ...
            assert(a.parent() == b.parent())
        AssertionError
    """
def verify_si_answer(x, answer, preparse) -> None:
    """
    Verify that evaluating ``answer`` gives a value equal to ``x``
    (with the same parent/type).  If ``preparse`` is ``True`` or
    ``False``, then we evaluate ``answer`` with the preparser
    enabled or disabled, respectively; if ``preparse`` is ``None``,
    then we evaluate ``answer`` both with the preparser enabled and
    disabled and check both results.

    On success, we return ``None``; on failure, we raise an exception.

    INPUT:

    - ``x`` -- an arbitrary Sage value

    - ``answer`` -- string, or a :class:`SageInputAnswer`

    - ``preparse`` -- ``True``, ``False``, or ``None``

    EXAMPLES::

        sage: from sage.misc.sage_input import verify_si_answer
        sage: verify_si_answer(1, '1', True)
        sage: verify_si_answer(1, '1', False)
        Traceback (most recent call last):
        ...
        AttributeError: 'int' object has no attribute 'parent'...
        sage: verify_si_answer(1, 'ZZ(1)', None)
    """

class SageInputAnswer(tuple):
    """
    This class inherits from tuple, so it acts like a tuple when passed
    to :func:`sage_eval`; but it prints as a sequence of commands.

    EXAMPLES::

        sage: from sage.misc.sage_input import SageInputAnswer
        sage: v = SageInputAnswer('x = 22\\n', 'x/7'); v
        x = 22
        x/7
        sage: isinstance(v, tuple)
        True
        sage: v[0]
        'x = 22\\n'
        sage: v[1]
        'x/7'
        sage: len(v)
        2
        sage: v = SageInputAnswer('', 'sin(3.14)', {'sin': math.sin}); v
        LOCALS:
          sin: <built-in function sin>
        sin(3.14)
        sage: v[0]
        ''
        sage: v[1]
        'sin(3.14)'
        sage: v[2]
        {'sin': <built-in function sin>}
    """
    def __new__(cls, cmds, expr, locals=None):
        """
        Construct an instance of :class:`SageInputAnswer`.

        EXAMPLES::

            sage: from sage.misc.sage_input import SageInputAnswer
            sage: v = SageInputAnswer('', 'sin(3.14)', {'sin': math.sin}); v
            LOCALS:
              sin: <built-in function sin>
            sin(3.14)
            sage: v[0]
            ''
            sage: v[1]
            'sin(3.14)'
            sage: v[2]
            {'sin': <built-in function sin>}
        """
