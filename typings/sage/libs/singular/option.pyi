from typing import Any, overload

opt: LibSingularOptions
opt_ctx: LibSingularOptionsContext
opt_verb: LibSingularVerboseOptions
opt_verb_ctx: LibSingularOptionsContext

class LibSingularOptions(LibSingularOptions_abstract):
    '''LibSingularOptions(**kwds)

    File: /build/sagemath/src/sage/src/sage/libs/singular/option.pyx (starting at line 301)

    Pythonic Interface to libSingular\'s options.

    Supported options are:

    - ``return_sb`` or ``returnSB`` -- the functions ``syz``,
      ``intersect``, ``quotient``, ``modulo`` return a standard
      base instead of a generating set if ``return_sb``
      is set. This option should not be used for ``lift``.

    - ``fast_hc`` or ``fastHC`` -- tries to find the highest corner
      of the staircase (HC) as fast as possible during a standard
      basis computation (only used for local orderings).

    - ``int_strategy`` or ``intStrategy`` -- avoids division of
      coefficients during standard basis computations. This option
      is ring dependent. By default, it is set for rings with
      characteristic 0 and not set for all other rings.

    - ``lazy`` -- uses a more lazy approach in std computations, which
      was used in SINGULAR version before 2-0 (and which may lead to
      faster or slower computations, depending on the example).

    - ``length`` -- select shorter reducers in std computations

    - ``not_regularity`` or ``notRegularity`` -- disables the
      regularity bound for ``res`` and ``mres``

    - ``not_sugar`` or ``notSugar`` -- disables the sugar strategy
      during standard basis computation

    - ``not_buckets`` or ``notBuckets`` -- disables the bucket
      representation of polynomials during standard basis
      computations. This option usually decreases the memory
      usage but increases the computation time. It should only
      be set for memory-critical standard basis computations.

    - ``old_std`` or ``oldStd`` -- uses a more lazy approach in std
      computations, which was used in SINGULAR version before 2-0
      (and which may lead to faster or slower computations, depending
      on the example).

    - ``prot`` -- shows protocol information indicating the progress
      during the following computations: ``facstd``, ``fglm``,
      ``groebner``, ``lres``, ``mres``, ``minres``, ``mstd``,
      ``res``, ``slimgb``, ``sres``, ``std``, ``stdfglm``,
      ``stdhilb``, ``syz``.

    - ``red_sb`` or ``redSB`` -- computes a reduced standard basis in
      any standard basis computation

    - ``red_tail`` or ``redTail`` -- reduction of the tails of
      polynomials during standard basis computations. This option
      is ring dependent. By default, it is set for rings with global
      degree orderings and not set for all other rings.

    - ``red_through`` or ``redThrough`` -- for inhomogeneous input,
      polynomial reductions during standard basis computations are
      never postponed, but always finished through. This option is
      ring dependent. By default, it is set for rings with global
      degree orderings and not set for all other rings.

    - ``sugar_crit`` or ``sugarCrit`` -- uses criteria similar to the
      homogeneous case to keep more useless pairs

    - ``weight_m`` or ``weightM`` -- automatically computes suitable
      weights for the weighted ecart and the weighted sugar method

    In addition, two integer valued parameters are supported, namely:

    - ``deg_bound`` or ``degBound`` -- the standard basis computation
      is stopped if the total (weighted) degree exceeds ``deg_bound``.
      ``deg_bound`` should not be used for a global ordering with
      inhomogeneous input. Reset this bound by setting ``deg_bound``
      to 0. The exact meaning of "degree" depends on the ring ordering
      and the command: ``slimgb`` uses always the total degree with
      weights 1, ``std`` does so for block orderings, only.

    - ``mult_bound`` or ``multBound`` -- the standard basis computation
      is stopped if the ideal is zero-dimensional in a ring with local
      ordering and its multiplicity is lower than ``mult_bound``.
      Reset this bound by setting ``mult_bound`` to 0.

    EXAMPLES::

        sage: from sage.libs.singular.option import LibSingularOptions
        sage: libsingular_options = LibSingularOptions()
        sage: libsingular_options
        general options for libSingular (current value 0x06000082)

    Here we demonstrate the intended way of using libSingular options::

        sage: R.<x,y> = QQ[]
        sage: I = R*[x^3+y^2,x^2*y+1]
        sage: I.groebner_basis(deg_bound=2)
        [x^3 + y^2, x^2*y + 1]
        sage: I.groebner_basis()
        [x^3 + y^2, x^2*y + 1, y^3 - x]

    The option ``mult_bound`` is only relevant in the local case::

        sage: from sage.libs.singular.option import opt
        sage: Rlocal.<x,y,z> = PolynomialRing(QQ, order=\'ds\')
        sage: x^2<x
        True
        sage: J = [x^7+y^7+z^6,x^6+y^8+z^7,x^7+y^5+z^8, x^2*y^3+y^2*z^3+x^3*z^2,x^3*y^2+y^3*z^2+x^2*z^3]*Rlocal
        sage: J.groebner_basis(mult_bound=100)
        [x^3*y^2 + y^3*z^2 + x^2*z^3, x^2*y^3 + x^3*z^2 + y^2*z^3, y^5, x^6 + x*y^4*z^5, x^4*z^2 - y^4*z^2 - x^2*y*z^3 + x*y^2*z^3, z^6 - x*y^4*z^4 - x^3*y*z^5]
        sage: opt[\'red_tail\'] = True # the previous commands reset opt[\'red_tail\'] to False
        sage: J.groebner_basis()
        [x^3*y^2 + y^3*z^2 + x^2*z^3, x^2*y^3 + x^3*z^2 + y^2*z^3, y^5, x^6, x^4*z^2 - y^4*z^2 - x^2*y*z^3 + x*y^2*z^3, z^6, y^4*z^3 - y^3*z^4 - x^2*z^5, x^3*y*z^4 - x^2*y^2*z^4 + x*y^3*z^4, x^3*z^5, x^2*y*z^5 + y^3*z^5, x*y^3*z^5]'''
    def __init__(self, **kwds) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/singular/option.pyx (starting at line 414)

                Create a new option interface.

                EXAMPLES::

                    sage: from sage.libs.singular.option import LibSingularOptions
                    sage: libsingular_options = LibSingularOptions()
                    sage: libsingular_options
                    general options for libSingular (current value 0x...)
        """
    def reset_default(self) -> Any:
        """LibSingularOptions.reset_default(self)

        File: /build/sagemath/src/sage/src/sage/libs/singular/option.pyx (starting at line 444)

        Reset libSingular's default options.

        EXAMPLES::

            sage: from sage.libs.singular.option import opt
            sage: opt['red_tail']
            True
            sage: opt['red_tail'] = False
            sage: opt['red_tail']
            False
            sage: opt['deg_bound']
            0
            sage: opt['deg_bound'] = 2
            sage: opt['deg_bound']
            2
            sage: opt.reset_default()
            sage: opt['red_tail']
            True
            sage: opt['deg_bound']
            0"""

class LibSingularOptionsContext:
    """LibSingularOptionsContext(LibSingularOptions_abstract opt, **kwds)

    File: /build/sagemath/src/sage/src/sage/libs/singular/option.pyx (starting at line 557)

    Option context

    This object localizes changes to options.

    EXAMPLES::

        sage: from sage.libs.singular.option import opt, opt_ctx
        sage: opt
        general options for libSingular (current value 0x06000082)

    ::

        sage: with opt_ctx(redTail=False):
        ....:     print(opt)
        ....:     with opt_ctx(redThrough=False):
        ....:         print(opt)
        general options for libSingular (current value 0x04000082)
        general options for libSingular (current value 0x04000002)

        sage: print(opt)
        general options for libSingular (current value 0x06000082)"""
    opt: opt
    def __init__(self, LibSingularOptions_abstractopt, **kwds) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/singular/option.pyx (starting at line 587)

                Create a new context.

                EXAMPLES::

                    sage: from sage.libs.singular.option import LibSingularOptionsContext, opt
                    sage: LibSingularOptionsContext(opt)
                    general options context for libSingular
        """
    def __call__(self, **kwds) -> Any:
        """LibSingularOptionsContext.__call__(self, **kwds)

        File: /build/sagemath/src/sage/src/sage/libs/singular/option.pyx (starting at line 621)

        Return a new option context where ``**kwds`` are applied.

        EXAMPLES::

            sage: from sage.libs.singular.option import opt, opt_ctx
            sage: opt['redTail']
            True
            sage: with opt_ctx(redTail=False):
            ....:   opt['redTail']
            False"""
    def __enter__(self) -> Any:
        """LibSingularOptionsContext.__enter__(self)

        File: /build/sagemath/src/sage/src/sage/libs/singular/option.pyx (starting at line 603)

        EXAMPLES::

            sage: from sage.libs.singular.option import opt, opt_ctx
            sage: opt['redTail']
            True
            sage: with opt_ctx(redTail=False):
            ....:   opt['redTail']
            False"""
    def __exit__(self, typ, value, tb) -> Any:
        """LibSingularOptionsContext.__exit__(self, typ, value, tb)

        File: /build/sagemath/src/sage/src/sage/libs/singular/option.pyx (starting at line 637)

        EXAMPLES::

            sage: from sage.libs.singular.option import opt, opt_ctx
            sage: opt['redTail']
            True
            sage: with opt_ctx(redTail=False):
            ....:   opt['redTail']
            False"""

class LibSingularOptions_abstract:
    """LibSingularOptions_abstract(**kwds)

    File: /build/sagemath/src/sage/src/sage/libs/singular/option.pyx (starting at line 139)

    Abstract Base Class for libSingular options."""
    def __init__(self, **kwds) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/singular/option.pyx (starting at line 147)

                INPUT:

                - ``**kwds`` -- all keyword parameters are immediately applied

                EXAMPLES::

                    sage: from sage.libs.singular.option import LibSingularOptions
                    sage: opt = LibSingularOptions(redTail=False)
                    sage: opt['redTail']
                    False
                    sage: opt['redTail'] = True
                    sage: opt['redTail']
                    True
                    sage: opt['deg_bound'] = 2

                The options can be named in Python or Singular style::

                    sage: opt['degBound']
                    2
        """
    @overload
    def load(self, value=...) -> Any:
        """LibSingularOptions_abstract.load(self, value=None)

        File: /build/sagemath/src/sage/src/sage/libs/singular/option.pyx (starting at line 268)

        EXAMPLES::

            sage: from sage.libs.singular.option import opt as sopt
            sage: bck = sopt.save(); hex(bck[0]), bck[1], bck[2]
            ('0x6000082', 0, 0)
            sage: sopt['redTail'] = False
            sage: hex(int(sopt))
            '0x4000082'
            sage: sopt.load(bck)
            sage: sopt['redTail']
            True"""
    @overload
    def load(self, bck) -> Any:
        """LibSingularOptions_abstract.load(self, value=None)

        File: /build/sagemath/src/sage/src/sage/libs/singular/option.pyx (starting at line 268)

        EXAMPLES::

            sage: from sage.libs.singular.option import opt as sopt
            sage: bck = sopt.save(); hex(bck[0]), bck[1], bck[2]
            ('0x6000082', 0, 0)
            sage: sopt['redTail'] = False
            sage: hex(int(sopt))
            '0x4000082'
            sage: sopt.load(bck)
            sage: sopt['redTail']
            True"""
    @overload
    def save(self) -> Any:
        """LibSingularOptions_abstract.save(self)

        File: /build/sagemath/src/sage/src/sage/libs/singular/option.pyx (starting at line 241)

        Return a triple of integers that allow reconstruction of the options.

        EXAMPLES::

            sage: from sage.libs.singular.option import opt
            sage: opt['deg_bound']
            0
            sage: opt['red_tail']
            True
            sage: s = opt.save()
            sage: opt['deg_bound'] = 2
            sage: opt['red_tail'] = False
            sage: opt['deg_bound']
            2
            sage: opt['red_tail']
            False
            sage: opt.load(s)
            sage: opt['deg_bound']
            0
            sage: opt['red_tail']
            True
            sage: opt.reset_default()  # needed to avoid side effects"""
    @overload
    def save(self) -> Any:
        """LibSingularOptions_abstract.save(self)

        File: /build/sagemath/src/sage/src/sage/libs/singular/option.pyx (starting at line 241)

        Return a triple of integers that allow reconstruction of the options.

        EXAMPLES::

            sage: from sage.libs.singular.option import opt
            sage: opt['deg_bound']
            0
            sage: opt['red_tail']
            True
            sage: s = opt.save()
            sage: opt['deg_bound'] = 2
            sage: opt['red_tail'] = False
            sage: opt['deg_bound']
            2
            sage: opt['red_tail']
            False
            sage: opt.load(s)
            sage: opt['deg_bound']
            0
            sage: opt['red_tail']
            True
            sage: opt.reset_default()  # needed to avoid side effects"""
    def __delitem__(self, other) -> None:
        """Delete self[key]."""
    def __getitem__(self, name) -> Any:
        """LibSingularOptions_abstract.__getitem__(self, name)

        File: /build/sagemath/src/sage/src/sage/libs/singular/option.pyx (starting at line 172)

        EXAMPLES::

            sage: from sage.libs.singular.option import opt
            sage: opt['red_tail']
            True
            sage: opt['deg_bound'] = 2

        The options can be named in Python or Singular style::

            sage: opt['degBound']
            2
            sage: opt.reset_default()  # needed to avoid side effects"""
    def __int__(self) -> Any:
        """LibSingularOptions_abstract.__int__(self)

        File: /build/sagemath/src/sage/src/sage/libs/singular/option.pyx (starting at line 231)

        EXAMPLES::

            sage: from sage.libs.singular.option import opt
            sage: hex(int(opt))
            '0x6000082'"""
    def __setitem__(self, name, value) -> Any:
        """LibSingularOptions_abstract.__setitem__(self, name, value)

        File: /build/sagemath/src/sage/src/sage/libs/singular/option.pyx (starting at line 201)

        EXAMPLES::

            sage: from sage.libs.singular.option import opt, opt_ctx
            sage: opt['redTail']
            True
            sage: with opt_ctx:
            ....:    opt['redTail'] = False
            ....:    opt['redTail']
            False
            sage: opt['red_tail']
            True
            sage: opt.reset_default()  # needed to avoid side effects"""

class LibSingularVerboseOptions(LibSingularOptions_abstract):
    """LibSingularVerboseOptions(**kwds)

    File: /build/sagemath/src/sage/src/sage/libs/singular/option.pyx (starting at line 473)

    Pythonic Interface to libSingular's verbosity options.

    Supported options are:

    - ``mem`` -- shows memory usage in square brackets
    - ``yacc`` -- only available in debug version
    - ``redefine`` -- warns about variable redefinitions
    - ``reading`` -- shows the number of characters read from a file
    - ``loadLib`` or ``load_lib`` -- shows loading of libraries
    - ``debugLib`` or ``debug_lib`` -- warns about syntax errors
      when loading a library
    - ``loadProc`` or ``load_proc`` -- shows loading of procedures
      from libraries
    - ``defRes`` or ``def_res`` -- shows the names of the syzygy
      modules while converting ``resolution`` to ``list``
    - ``usage`` -- shows correct usage in error messages
    - ``Imap`` or ``imap`` -- shows the mapping of variables with
      the ``fetch`` and ``imap`` commands
    - ``notWarnSB`` or ``not_warn_sb`` -- do not warn if
      a basis is not a standard basis
    - ``contentSB`` or ``content_sb`` -- avoids to divide by the
      content of a polynomial in ``std`` and related algorithms.
      Should usually not be used.
    - ``cancelunit`` -- avoids to divide polynomials by non-constant
      units in ``std`` in the local case. Should usually not be used

    EXAMPLES::

        sage: from sage.libs.singular.option import LibSingularVerboseOptions
        sage: libsingular_verbose = LibSingularVerboseOptions()
        sage: libsingular_verbose
        verbosity options for libSingular (current value 0x00002851)"""
    def __init__(self, **kwds) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/singular/option.pyx (starting at line 508)

                Create a new option interface.

                EXAMPLES::

                    sage: from sage.libs.singular.option import LibSingularVerboseOptions
                    sage: libsingular_verb_options = LibSingularVerboseOptions()
                    sage: libsingular_verb_options
                    verbosity options for libSingular (current value 0x00002851)
        """
    def reset_default(self) -> Any:
        """LibSingularVerboseOptions.reset_default(self)

        File: /build/sagemath/src/sage/src/sage/libs/singular/option.pyx (starting at line 538)

        Return to libSingular's default verbosity options.

        EXAMPLES::

            sage: from sage.libs.singular.option import opt_verb
            sage: opt_verb['not_warn_sb']
            False
            sage: opt_verb['not_warn_sb'] = True
            sage: opt_verb['not_warn_sb']
            True
            sage: opt_verb.reset_default()
            sage: opt_verb['not_warn_sb']
            False"""
