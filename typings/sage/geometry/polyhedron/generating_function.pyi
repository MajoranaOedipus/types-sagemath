from _typeshed import Incomplete

Hrepresentation_str_options: Incomplete

def generating_function_of_integral_points(polyhedron, split: bool = False, result_as_tuple=None, name=None, names=None, **kwds):
    """
    Return the multivariate generating function of the
    integral points of the ``polyhedron``.

    To be precise, this returns

    .. MATH::

        \\sum_{(r_0,\\dots,r_{d-1}) \\in \\mathit{polyhedron}\\cap \\ZZ^d}
        y_0^{r_0} \\dots y_{d-1}^{r_{d-1}}.

    INPUT:

    - ``polyhedron`` -- an instance of
      :class:`~sage.geometry.polyhedron.base.Polyhedron_base`
      (see also :mod:`sage.geometry.polyhedron.constructor`)

    - ``split`` -- (default: ``False``) a boolean or list

      - ``split=False`` computes the generating function directly,
        without any splitting.

      - When ``split`` is a list of disjoint polyhedra, then
        for each of these polyhedra, ``polyhedron`` is intersected with it,
        its generating function computed and all these generating functions
        are summed up.

      - ``split=True`` splits into `d!` disjoint polyhedra.

    - ``result_as_tuple`` -- (default: ``None``) a boolean or ``None``

      This specifies whether the output is a (partial) factorization
      (``result_as_tuple=False``) or a sum of such (partial)
      factorizations (``result_as_tuple=True``). By default
      (``result_as_tuple=None``), this is automatically determined.
      If the output is a sum, it is represented as a tuple whose
      entries are the summands.

    - ``indices`` -- (default: ``None``) a list or tuple

      If this
      is ``None``, this is automatically determined.

    - ``name`` -- (default: ``'y'``) a string

      The variable names of the Laurent polynomial ring of the output
      are this string followed by an integer.

    - ``names`` -- list or tuple of names (strings), or a comma separated string

      ``name`` is extracted from ``names``, therefore ``names`` has to contain
      exactly one variable name, and ``name`` and``names`` cannot be specified
      both at the same time.

    - ``Factorization_sort`` (default: ``False``) and
      ``Factorization_simplify`` (default: ``True``) -- booleans

      These are passed on to
      :class:`sage.structure.factorization.Factorization` when creating
      the result.

    - ``sort_factors`` -- (default: ``False``) a boolean

      If set, then
      the factors of the output are sorted such that the numerator is
      first and only then all factors of the denominator. It is ensured
      that the sorting is always the same; use this for doctesting.

    OUTPUT:

    The generating function as a (partial)
    :class:`~sage.structure.factorization.Factorization`
    of the result whose factors are Laurent polynomials

    The result might be a tuple of such factorizations
    (depending on the parameter ``result_as_tuple``) as well.

    .. NOTE::

        At the moment, only polyhedra with nonnegative coordinates
        (i.e. a polyhedron in the nonnegative orthant) are handled.

    EXAMPLES::

        sage: from sage.geometry.polyhedron.generating_function import generating_function_of_integral_points

    ::

        sage: P2 = (
        ....:   Polyhedron(ieqs=[(0, 0, 0, 1), (0, 0, 1, 0), (0, 1, 0, -1)]),
        ....:   Polyhedron(ieqs=[(0, -1, 0, 1), (0, 1, 0, 0), (0, 0, 1, 0)]))
        sage: generating_function_of_integral_points(P2[0], sort_factors=True)
        1 * (-y0 + 1)^-1 * (-y1 + 1)^-1 * (-y0*y2 + 1)^-1
        sage: generating_function_of_integral_points(P2[1], sort_factors=True)
        1 * (-y1 + 1)^-1 * (-y2 + 1)^-1 * (-y0*y2 + 1)^-1
        sage: (P2[0] & P2[1]).Hrepresentation()
        (An equation (1, 0, -1) x + 0 == 0,
         An inequality (1, 0, 0) x + 0 >= 0,
         An inequality (0, 1, 0) x + 0 >= 0)
        sage: generating_function_of_integral_points(P2[0] & P2[1], sort_factors=True)
        1 * (-y1 + 1)^-1 * (-y0*y2 + 1)^-1

    ::

        sage: P3 = (
        ....:   Polyhedron(
        ....:     ieqs=[(0, 0, 0, 0, 1), (0, 0, 0, 1, 0),
        ....:           (0, 0, 1, 0, -1), (-1, 1, 0, -1, -1)]),
        ....:   Polyhedron(
        ....:     ieqs=[(0, 0, -1, 0, 1), (0, 1, 0, 0, -1),
        ....:           (0, 0, 0, 1, 0), (0, 0, 1, 0, 0), (-1, 1, -1, -1, 0)]),
        ....:   Polyhedron(
        ....:     ieqs=[(1, -1, 0, 1, 1), (1, -1, 1, 1, 0),
        ....:           (0, 0, 0, 0, 1), (0, 0, 0, 1, 0), (0, 0, 1, 0, 0),
        ....:           (1, 0, 1, 1, -1), (0, 1, 0, 0, 0), (1, 1, 1, 0, -1)]),
        ....:   Polyhedron(
        ....:     ieqs=[(0, 1, 0, -1, 0), (0, -1, 0, 0, 1),
        ....:           (-1, 0, -1, -1, 1), (0, 0, 1, 0, 0), (0, 0, 0, 1, 0)]),
        ....:   Polyhedron(
        ....:     ieqs=[(0, 1, 0, 0, 0), (0, 0, 1, 0, 0),
        ....:           (-1, -1, -1, 0, 1), (0, -1, 0, 1, 0)]))
        sage: def intersect(I):
        ....:     I = iter(I)
        ....:     result = next(I)
        ....:     for i in I:
        ....:         result &= i
        ....:     return result
        sage: for J in subsets(range(len(P3))):
        ....:     if not J:
        ....:         continue
        ....:     P = intersect([P3[j] for j in J])
        ....:     print('{}: {}'.format(J, P.Hrepresentation()))
        ....:     print(generating_function_of_integral_points(P, sort_factors=True))
        [0]: (An inequality (0, 0, 0, 1) x + 0 >= 0,
              An inequality (0, 0, 1, 0) x + 0 >= 0,
              An inequality (0, 1, 0, -1) x + 0 >= 0,
              An inequality (1, 0, -1, -1) x - 1 >= 0)
        y0 * (-y0 + 1)^-1 * (-y1 + 1)^-1 * (-y0*y2 + 1)^-1 * (-y0*y1*y3 + 1)^-1
        [1]: (An inequality (0, -1, 0, 1) x + 0 >= 0,
              An inequality (0, 0, 1, 0) x + 0 >= 0,
              An inequality (0, 1, 0, 0) x + 0 >= 0,
              An inequality (1, -1, -1, 0) x - 1 >= 0,
              An inequality (1, 0, 0, -1) x + 0 >= 0)
        (-y0^2*y2*y3 - y0^2*y3 + y0*y3 + y0) *
        (-y0 + 1)^-1 * (-y0*y2 + 1)^-1 * (-y0*y3 + 1)^-1 *
        (-y0*y1*y3 + 1)^-1 * (-y0*y2*y3 + 1)^-1
        [0, 1]: (An equation (0, 1, 0, -1) x + 0 == 0,
                 An inequality (1, -1, -1, 0) x - 1 >= 0,
                 An inequality (0, 1, 0, 0) x + 0 >= 0,
                 An inequality (0, 0, 1, 0) x + 0 >= 0)
        y0 * (-y0 + 1)^-1 * (-y0*y2 + 1)^-1 * (-y0*y1*y3 + 1)^-1
        [2]: (An inequality (-1, 0, 1, 1) x + 1 >= 0,
             An inequality (-1, 1, 1, 0) x + 1 >= 0,
              An inequality (0, 0, 0, 1) x + 0 >= 0,
              An inequality (0, 0, 1, 0) x + 0 >= 0,
              An inequality (0, 1, 0, 0) x + 0 >= 0,
              An inequality (0, 1, 1, -1) x + 1 >= 0,
              An inequality (1, 0, 0, 0) x + 0 >= 0,
              An inequality (1, 1, 0, -1) x + 1 >= 0)
        (y0^2*y1*y2*y3^2 + y0^2*y2^2*y3 + y0*y1^2*y3^2 - y0^2*y2*y3 +
         y0*y1*y2*y3 - y0*y1*y3^2 - 2*y0*y1*y3 - 2*y0*y2*y3 - y0*y2 +
         y0*y3 - y1*y3 + y0 + y3 + 1) *
        (-y1 + 1)^-1 * (-y2 + 1)^-1 * (-y0*y2 + 1)^-1 *
        (-y1*y3 + 1)^-1 * (-y0*y1*y3 + 1)^-1 * (-y0*y2*y3 + 1)^-1
        [0, 2]: (An equation (1, 0, -1, -1) x - 1 == 0,
                 An inequality (-1, 1, 1, 0) x + 1 >= 0,
                 An inequality (1, 0, -1, 0) x - 1 >= 0,
                 An inequality (0, 0, 1, 0) x + 0 >= 0)
        y0 * (-y1 + 1)^-1 * (-y0*y2 + 1)^-1 * (-y0*y1*y3 + 1)^-1
        [1, 2]: (An equation (1, -1, -1, 0) x - 1 == 0,
                 An inequality (0, -1, 0, 1) x + 0 >= 0,
                 An inequality (0, 1, 0, 0) x + 0 >= 0,
                 An inequality (1, 0, 0, -1) x + 0 >= 0,
                 An inequality (1, -1, 0, 0) x - 1 >= 0)
        (-y0^2*y2*y3 + y0*y3 + y0) *
        (-y0*y2 + 1)^-1 * (-y0*y1*y3 + 1)^-1 * (-y0*y2*y3 + 1)^-1
        [0, 1, 2]: (An equation (0, 1, 0, -1) x + 0 == 0,
                    An equation (1, -1, -1, 0) x - 1 == 0,
                    An inequality (0, 1, 0, 0) x + 0 >= 0,
                    An inequality (1, -1, 0, 0) x - 1 >= 0)
        y0 * (-y0*y2 + 1)^-1 * (-y0*y1*y3 + 1)^-1
        [3]: (An inequality (-1, 0, 0, 1) x + 0 >= 0,
              An inequality (0, -1, -1, 1) x - 1 >= 0,
              An inequality (0, 0, 1, 0) x + 0 >= 0,
              An inequality (0, 1, 0, 0) x + 0 >= 0,
              An inequality (1, 0, -1, 0) x + 0 >= 0)
        (-y0*y1*y3^2 - y0*y3^2 + y0*y3 + y3) *
        (-y3 + 1)^-1 * (-y0*y3 + 1)^-1 *
        (-y1*y3 + 1)^-1 * (-y0*y1*y3 + 1)^-1 * (-y0*y2*y3 + 1)^-1
        [0, 3]: (An equation -1 == 0,)
        0
        [1, 3]: (An equation (1, 0, 0, -1) x + 0 == 0,
                 An inequality (1, -1, -1, 0) x - 1 >= 0,
                 An inequality (0, 1, 0, 0) x + 0 >= 0,
                 An inequality (0, 0, 1, 0) x + 0 >= 0)
        y0*y3 * (-y0*y3 + 1)^-1 * (-y0*y1*y3 + 1)^-1 * (-y0*y2*y3 + 1)^-1
        [0, 1, 3]: (An equation -1 == 0,)
        0
        [2, 3]: (An equation (0, 1, 1, -1) x + 1 == 0,
                 An inequality (1, 0, -1, 0) x + 0 >= 0,
                 An inequality (-1, 1, 1, 0) x + 1 >= 0,
                 An inequality (0, 0, 1, 0) x + 0 >= 0,
                 An inequality (0, 1, 0, 0) x + 0 >= 0)
        (-y0*y1*y3^2 + y0*y3 + y3) *
        (-y1*y3 + 1)^-1 * (-y0*y1*y3 + 1)^-1 * (-y0*y2*y3 + 1)^-1
        [0, 2, 3]: (An equation -1 == 0,)
        0
        [1, 2, 3]: (An equation (1, 0, 0, -1) x + 0 == 0,
                    An equation (1, -1, -1, 0) x - 1 == 0,
                    An inequality (0, 1, 0, 0) x + 0 >= 0,
                    An inequality (1, -1, 0, 0) x - 1 >= 0)
        y0*y3 * (-y0*y1*y3 + 1)^-1 * (-y0*y2*y3 + 1)^-1
        [0, 1, 2, 3]: (An equation -1 == 0,)
        0
        [4]: (An inequality (-1, -1, 0, 1) x - 1 >= 0,
              An inequality (-1, 0, 1, 0) x + 0 >= 0,
              An inequality (0, 1, 0, 0) x + 0 >= 0,
              An inequality (1, 0, 0, 0) x + 0 >= 0)
        y3 * (-y2 + 1)^-1 * (-y3 + 1)^-1 * (-y1*y3 + 1)^-1 * (-y0*y2*y3 + 1)^-1
        [0, 4]: (An equation -1 == 0,)
        0
        [1, 4]: (An equation -1 == 0,)
        0
        [0, 1, 4]: (An equation -1 == 0,)
        0
        [2, 4]: (An equation (1, 1, 0, -1) x + 1 == 0,
                 An inequality (-1, 0, 1, 0) x + 0 >= 0,
                 An inequality (1, 0, 0, 0) x + 0 >= 0,
                 An inequality (0, 1, 0, 0) x + 0 >= 0)
        y3 * (-y2 + 1)^-1 * (-y1*y3 + 1)^-1 * (-y0*y2*y3 + 1)^-1
        [0, 2, 4]: (An equation -1 == 0,)
        0
        [1, 2, 4]: (An equation -1 == 0,)
        0
        [0, 1, 2, 4]: (An equation -1 == 0,)
        0
        [3, 4]: (An equation (1, 0, -1, 0) x + 0 == 0,
                 An inequality (0, 1, 0, 0) x + 0 >= 0,
                 An inequality (-1, -1, 0, 1) x - 1 >= 0,
                 An inequality (1, 0, 0, 0) x + 0 >= 0)
        y3 * (-y3 + 1)^-1 * (-y1*y3 + 1)^-1 * (-y0*y2*y3 + 1)^-1
        [0, 3, 4]: (An equation -1 == 0,)
        0
        [1, 3, 4]: (An equation -1 == 0,)
        0
        [0, 1, 3, 4]: (An equation -1 == 0,)
        0
        [2, 3, 4]: (An equation (1, 1, 0, -1) x + 1 == 0,
                    An equation (1, 0, -1, 0) x + 0 == 0,
                    An inequality (0, 1, 0, 0) x + 0 >= 0,
                    An inequality (1, 0, 0, 0) x + 0 >= 0)
        y3 * (-y1*y3 + 1)^-1 * (-y0*y2*y3 + 1)^-1
        [0, 2, 3, 4]: (An equation -1 == 0,)
        0
        [1, 2, 3, 4]: (An equation -1 == 0,)
        0
        [0, 1, 2, 3, 4]: (An equation -1 == 0,)
        0

    ::

        sage: P = Polyhedron(vertices=[[1], [5]])
        sage: P.generating_function_of_integral_points()
        y0^5 + y0^4 + y0^3 + y0^2 + y0

    .. SEEALSO::

        This function is accessible via
        :meth:`sage.geometry.polyhedron.base.Polyhedron_base.generating_function_of_integral_points`
        as well. More examples can be found there.

    TESTS::

        sage: generating_function_of_integral_points(
        ....:     Polyhedron(ieqs=[(0, 0, 1, 0, 0), (-1, 1, -1, 0, 0),
        ....:                      (0, 0, 0, 1, 0), (0, 0, 0, 0, 1)]),
        ....:     sort_factors=True)
        y0 * (-y0 + 1)^-1 * (-y2 + 1)^-1 * (-y3 + 1)^-1 * (-y0*y1 + 1)^-1
        sage: generating_function_of_integral_points(
        ....:     Polyhedron(ieqs=[(0, 0, -1, 0, 1), (0, 0, 1, 0, 0),
        ....:                      (0, 1, 0, 0, -1), (-1, 1, -1, 0, 0),
        ....:                      (0, 0, 0, 1, 0)]),
        ....:     sort_factors=True)
        (-y0^2*y3 + y0*y3 + y0) *
        (-y0 + 1)^-1 * (-y2 + 1)^-1 * (-y0*y3 + 1)^-1 * (-y0*y1*y3 + 1)^-1

        sage: generating_function_of_integral_points(
        ....:     Polyhedron(ieqs=[(0, 1, 0, -1, 0, 0), (0, 0, 0, 1, 0, 0)],
        ....:                eqns=[(0, 0, 0, 1, 0, -1), (0, 1, 0, 0, -1, 0),
        ....:                      (0, 1, -1, 0, 0, 0)]),
        ....:     sort_factors=True)
        1 * (-y0*y1*y3 + 1)^-1 * (-y0*y1*y2*y3*y4 + 1)^-1

    ::

        sage: G = generating_function_of_integral_points(P2[0], sort_factors=True)
        sage: S = generating_function_of_integral_points(P2[0], sort_factors=True,
        ....:                                       split=True)
        sage: sum(S) == G.value()
        True

        sage: G = generating_function_of_integral_points(P2[1], sort_factors=True)
        sage: S = generating_function_of_integral_points(P2[1], sort_factors=True,
        ....:                                       split=True)
        sage: sum(S) == G.value()
        True

        sage: G = generating_function_of_integral_points(P3[0], sort_factors=True)
        sage: S = generating_function_of_integral_points(P3[0], sort_factors=True,
        ....:                                       split=True)
        sage: sum(S) == G.value()
        True

    We show the distinct polyhedra that are used when ``split=True`` and the
    resulting polyhedra that are used in the individual computations::

        sage: import logging
        sage: logging.basicConfig(level=logging.INFO)
        sage: sum(generating_function_of_integral_points(P2[1], sort_factors=True,
        ....:                                            split=True))
        ...
        INFO:sage.geometry.polyhedron.generating_function:(1/6) split polyhedron by b0 <= b1 <= b2
        INFO:sage.geometry.polyhedron.generating_function:using polyhedron
            b0 >= 0
            b1 >= b0
            b2 >= b1
        ...
        INFO:sage.geometry.polyhedron.generating_function:(2/6) split polyhedron by b0 <= b2 < b1
        INFO:sage.geometry.polyhedron.generating_function:using polyhedron
            b2 >= b0
            b1 >= 1 + b2
            b0 >= 0
        ...
        INFO:sage.geometry.polyhedron.generating_function:(3/6) split polyhedron by b1 < b0 <= b2
        INFO:sage.geometry.polyhedron.generating_function:using polyhedron
            b2 >= b0
            b1 >= 0
            b0 >= 1 + b1
        ...
        INFO:sage.geometry.polyhedron.generating_function:(4/6) split polyhedron by b1 <= b2 < b0
        INFO:sage.geometry.polyhedron.generating_function:using polyhedron
            0 == 1
        INFO:sage.geometry.polyhedron.generating_function:(5/6) split polyhedron by b2 < b0 <= b1
        INFO:sage.geometry.polyhedron.generating_function:using polyhedron
            0 == 1
        INFO:sage.geometry.polyhedron.generating_function:(6/6) split polyhedron by b2 < b1 < b0
        INFO:sage.geometry.polyhedron.generating_function:using polyhedron
            0 == 1
        1/(-y0*y1*y2^2 + y0*y1*y2 + y0*y2^2 - y0*y2 + y1*y2 - y1 - y2 + 1)
        sage: logging.disable()

    ::

        sage: generating_function_of_integral_points(
        ....:     Polyhedron(ieqs=[(0, 0, 1, 0, 0), (-1, 1, -1, 0, 0)]),
        ....:     sort_factors=True)
        Traceback (most recent call last):
        ...
        NotImplementedError: cannot compute the generating function of
        polyhedra with negative coordinates
        sage: generating_function_of_integral_points(
        ....:     Polyhedron(ieqs=[(0, 0, -1, 0, 1), (0, 0, 1, 0, 0),
        ....:                      (0, 1, 0, 0, -1), (-1, 1, -1, 0, 0)]),
        ....:     sort_factors=True)
        Traceback (most recent call last):
        ...
        NotImplementedError: cannot compute the generating function of
        polyhedra with negative coordinates

    ::

        sage: generating_function_of_integral_points(
        ....:     Polyhedron(ieqs=[(0, 0, 1, 0), (-1, 1, -1, 1),
        ....:                      (0, 0, 0, 1), (0, 1, 0, 0)]),
        ....:     name='z',
        ....:     sort_factors=True)
        (-z0*z1*z2 - z0*z2 + z0 + z2) *
        (-z0 + 1)^-1 * (-z2 + 1)^-1 * (-z0*z1 + 1)^-1 * (-z1*z2 + 1)^-1
        sage: generating_function_of_integral_points(
        ....:     Polyhedron(ieqs=[(0, 0, 1, 0), (-1, 1, -1, 1),
        ....:                      (0, 0, 0, 1), (0, 1, 0, 0)]),
        ....:     name='mu',
        ....:     sort_factors=True)
        (-mu0*mu1*mu2 - mu0*mu2 + mu0 + mu2) *
        (-mu0 + 1)^-1 * (-mu2 + 1)^-1 * (-mu0*mu1 + 1)^-1 * (-mu1*mu2 + 1)^-1

    ::

        sage: generating_function_of_integral_points(P2[0],
        ....:     sort_factors=True, names=('a',))
        1 * (-a0 + 1)^-1 * (-a1 + 1)^-1 * (-a0*a2 + 1)^-1
        sage: generating_function_of_integral_points(P2[0],
        ....:     sort_factors=True, names=('a', 'b'))
        Traceback (most recent call last):
        ...
        NotImplementedError: exactly one variable name has to be provided
        sage: generating_function_of_integral_points(P2[0],
        ....:     sort_factors=True, name='a', names=('a',))
        1 * (-a0 + 1)^-1 * (-a1 + 1)^-1 * (-a0*a2 + 1)^-1
        sage: generating_function_of_integral_points(P2[0],
        ....:     sort_factors=True, name='a', names=('b',))
        Traceback (most recent call last):
        ...
        ValueError: keyword argument 'name' cannot be combined with 'names'

    ::

        sage: P = Polyhedron(rays=[(1, sqrt(2)), (0, 1)])
        Traceback (most recent call last):
        ...
        ValueError: no default backend for computations with Symbolic Ring
        sage: P = Polyhedron(ieqs=[(RDF(pi), RDF(1))])
        sage: P.generating_function_of_integral_points()
        Traceback (most recent call last):
        ...
        TypeError: base ring Real Double Field of the polyhedron not ZZ or QQ
    """
def __generating_function_of_integral_points__(indices, inequalities, equations, mod, name, Factorization_sort: bool = False, Factorization_simplify: bool = False, sort_factors: bool = False):
    """
    Helper function for :func:`generating_function_of_integral_points` which
    does the actual computation of the generating function.

    TESTS::

        sage: from sage.geometry.polyhedron.generating_function import __generating_function_of_integral_points__

        sage: __generating_function_of_integral_points__(
        ....:     (0, 2), [(0, 1, 0)], [(1, -1, 2)],
        ....:     {0: (2, 1)}, name='y', sort_factors=True)
        y0 * (-y0^2*y2 + 1)^-1
        sage: __generating_function_of_integral_points__(
        ....:     srange(3), [(0, 1, 0, 0), (0, 0, 1, 0)], [(1, -1, 0, 2)],
        ....:     {0: (2, 1)}, name='y', sort_factors=True)
        y0 * (-y1 + 1)^-1 * (-y0^2*y2 + 1)^-1
        sage: __generating_function_of_integral_points__(
        ....:     srange(3), [(0, 1, 0, 0), (0, -1, 1, 0)], [(0, -1, -1, 2)],
        ....:     {0: (2, 1), 1: (2, 1)}, name='y', sort_factors=True)
        y0*y1*y2 * (-y1^2*y2 + 1)^-1 * (-y0^2*y1^2*y2^2 + 1)^-1
    """

class _TransformHrepresentation:
    """
    An abstract base class for transformations of the
    Hrepresentation of a polyhedron together with its
    back-substitutions of the corresponding generating function.

    INPUT:

    - ``inequalities`` -- list of tuples of numbers

    - ``equations`` -- list of tuples of numbers

    - ``B`` -- a Laurent polynomial ring

    ATTRIBUTES:

    - ``inequalities``, ``equations`` -- list of tuples

      Determine the generating function of these inequalities
      and equations instead of the input.

    - ``factor`` -- a Laurent polynomial

      The numerator of the generating function has to be multiplied
      with ``factor`` *after* substituting ``rules``.

    - ``rules`` -- dictionary mapping Laurent polynomial variables to
      Laurent polynomials

      Substitute ``rules`` into the generating function.

    The generating function of the input ``inequalities`` and
    ``equations`` is equal to the generating function of the
    attributes ``inequalities`` and ``equations`` in which ``rules``
    were substituted and ``factor`` was multiplied (via
    :meth:`~_TransformHrepresentation.apply_rules`).
    """
    inequalities: Incomplete
    equations: Incomplete
    B: Incomplete
    def __init__(self, inequalities, equations, B) -> None:
        """
        See :class:`_TransformHrepresentation` for details.

        TESTS::

            sage: from sage.geometry.polyhedron.generating_function import _TransformHrepresentation
            sage: B = LaurentPolynomialRing(ZZ, 'y', 2)
            sage: _TransformHrepresentation([(1, 2, 3)], [(0, -1, 1)], B)
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def apply_rules(self, numerator, terms):
        """
        Substitute the generated rules.

        INPUT:

        - ``numerator`` -- a Laurent polynomial

        - ``terms`` -- tuple or other iterable of Laurent polynomials

          The denominator is the product of factors `1 - t` for each
          `t` in ``terms``.

        OUTPUT:

        A pair of a Laurent polynomial and a tuple of Laurent polynomials
        representing numerator and denominator as described in the
        INPUT-section.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.generating_function import _SplitOffSimpleInequalities as prepare
            sage: from sage.geometry.polyhedron.generating_function import _generating_function_via_Omega_ as gf
            sage: B = LaurentPolynomialRing(ZZ, 'y', 3)
            sage: ieqs = [(0, -1, 1, 0)]
            sage: T = prepare(ieqs, [], B); T.inequalities, T.factor, T.rules
            ([], 1, {y2: y2, y1: y1, y0: y0*y1})
            sage: T.apply_rules(*gf(T.inequalities, B))
            (1, (y0*y1, y1, y2))
        """

class _SplitOffSimpleInequalities(_TransformHrepresentation):
    """
    Split off (simple) inequalities which can be handled better
    without passing them to Omega.

    INPUT:

    - ``inequalities`` -- list of tuples of numbers

    - ``equations`` -- list of tuples of numbers

    - ``B`` -- a Laurent polynomial ring

    ATTRIBUTES:

    - ``inequalities``, ``equations`` -- list of tuples

      Determine the generating function of these inequalities
      and equations instead of the input.

    - ``factor`` -- a Laurent polynomial

      The numerator of the generating function has to be multiplied
      with ``factor`` *after* substituting ``rules``.

    - ``rules`` -- dictionary mapping Laurent polynomial variables to
      Laurent polynomials

      Substitute ``rules`` into the generating function.

    The generating function of the input ``inequalities`` and
    ``equations`` is equal to the generating function of the
    attributes ``inequalities`` and ``equations`` in which ``rules``
    were substitited and ``factor`` was multiplied (via
    :meth:`~_TransformHrepresentation.apply_rules`).

    EXAMPLES::

        sage: from sage.geometry.polyhedron.generating_function import _SplitOffSimpleInequalities as prepare
        sage: from sage.geometry.polyhedron.generating_function import _generating_function_via_Omega_ as gf

        sage: def eq(A, B):
        ....:     return (A[0] == B[0] and
        ....:             sorted(A[1], key=repr) == sorted(B[1], key=repr))

        sage: B = LaurentPolynomialRing(ZZ, 'y', 3)

        sage: ieqs = [(0, -1, 1, 0), (2, -1, -1, 1)]
        sage: T = prepare(ieqs, [], B); T.inequalities, T.factor, T.rules
        ([(2, -2, -1, 1)], 1, {y2: y2, y1: y1, y0: y0*y1})
        sage: T.apply_rules(*gf(T.inequalities, B))
        (y0*y1^3*y2^3 - y0*y1^3*y2^2 + y0*y1^2*y2^3 - y0*y1^2*y2^2
         - y0*y1*y2^2 - y1^2*y2 + y0*y1 + y1^2 - y1*y2 + y1 + 1,
         (y2, y1*y2, y0*y1*y2^2))
        sage: eq(_, gf(ieqs, B))
        True

        sage: ieqs = [(-1, -1, 1, 0), (2, -1, -1, 1)]
        sage: T = prepare(ieqs, [], B); T.inequalities, T.factor, T.rules
        ([(1, -2, -1, 1)], y1, {y2: y2, y1: y1, y0: y0*y1})
        sage: T.apply_rules(*gf(T.inequalities, B))
        (y0*y1^3*y2^3 - y0*y1^3*y2^2 - y0*y1^2*y2^2
         + y0*y1^2*y2 - y1^2*y2 + y1^2 + y1,
         (y2, y1*y2, y0*y1*y2^2))
        sage: eq(_, gf(ieqs, B))
        True

        sage: ieqs = [(-2, -1, 1, 0), (2, -1, -1, 1)]
        sage: T = prepare(ieqs, [], B); T.inequalities, T.factor, T.rules
        ([(0, -2, -1, 1)], y1^2, {y2: y2, y1: y1, y0: y0*y1})
        sage: T.apply_rules(*gf(T.inequalities, B))
        (y1^2, (y2, y1*y2, y0*y1*y2^2))
        sage: eq(_, gf(ieqs, B))
        True

        sage: ieqs = [(2, -1, 1, 0), (2, -1, -1, 1)]
        sage: T = prepare(ieqs, [], B); T.inequalities, T.factor, T.rules
        ([(2, -1, 1, 0), (2, -1, -1, 1)], 1, {y2: y2, y1: y1, y0: y0})
        sage: eq(T.apply_rules(*gf(T.inequalities, B)), gf(ieqs, B))
        True

    TESTS::

        sage: def eq2(A, B):
        ....:     a = SR(repr(A[0])) * prod(1-SR(repr(t)) for t in B[1])
        ....:     b = SR(repr(B[0])) * prod(1-SR(repr(t)) for t in A[1])
        ....:     return bool((a-b).full_simplify() == 0)

        sage: B = LaurentPolynomialRing(ZZ, 'y', 3)
        sage: ieqs = [(-2, 1, -1, 0), (-2, -1, 0, 1), (-1, -1, -1, 3)]
        sage: T = prepare(ieqs, [], B); T.inequalities, T.factor, T.rules
        ([(9, 2, 1, 3)], y0^2*y2^4, {y2: y2, y1: y0*y1*y2, y0: y0*y2})
        sage: T.apply_rules(*gf(T.inequalities, B))
        (y0^2*y2^4, (y2, y0*y2, y0*y1*y2))
        sage: eq2(_, gf(ieqs, B))
        True

        sage: B = LaurentPolynomialRing(ZZ, 'y', 4)
        sage: ieqs = [(-1, 1, -1, 0, 0)]
        sage: T = prepare(ieqs, [], B); T.inequalities, T.factor, T.rules
        ([], y0, {y3: y3, y2: y2, y1: y0*y1, y0: y0})
        sage: T.apply_rules(*gf(T.inequalities, B))
        (y0, (y0, y0*y1, y2, y3))
        sage: eq(_, gf(ieqs, B))
        True

        sage: ieqs = [(0, 0, -1, 0, 1), (0, 0, 1, 0, 0),
        ....:         (0, 1, 0, 0, -1), (-1, 1, -1, 0, 0)]
        sage: T = prepare(ieqs, [], B); T.inequalities, T.factor, T.rules
        ([(1, 1, 0, 0, -1)], y0, {y3: y3, y2: y2, y1: y0*y1*y3, y0: y0})
        sage: T.apply_rules(*gf(T.inequalities, B))
        (-y0^2*y3 + y0*y3 + y0, (y0*y1*y3, y2, y0, y0*y3))
        sage: eq(_, gf(ieqs, B))
        True

        sage: ieqs = [(-2, 1, -1, 0, 0)]
        sage: T = prepare(ieqs, [], B); T.inequalities, T.factor, T.rules
        ([], y0^2, {y3: y3, y2: y2, y1: y0*y1, y0: y0})

        sage: T.apply_rules(*gf(T.inequalities, B))
        (y0^2, (y0, y0*y1, y2, y3))
        sage: eq(_, gf(ieqs, B))
        True

        sage: ieqs = [(0, -1, 1, 0, 0), (-2, 0, -1, 0, 1),
        ....:         (0, -1, 0, 1, 0), (-3, 0, 0, -1, 1)]
        sage: T = prepare(ieqs, [], B); T.inequalities, T.factor, T.rules
        ([(1, 0, -1, 1, 1)],
         y3^3,
         {y3: y3, y2: y2*y3, y1: y1, y0: y0*y1*y2*y3})
        sage: T.apply_rules(*gf(T.inequalities, B))
        (-y1*y2*y3^4 - y1*y3^4 + y1*y3^3 + y3^3,
         (y0*y1*y2*y3, y2*y3, y3, y1*y2*y3, y1*y3))
        sage: eq(_, gf(ieqs, B))
        True

        sage: ieqs = [(0, -1, 1, 0, 0), (-3, 0, -1, 0, 1),
        ....:         (0, -1, 0, 1, 0), (-2, 0, 0, -1, 1)]
        sage: T = prepare(ieqs, [], B); T.inequalities, T.factor, T.rules
        ([(1, 0, 1, -1, 1)],
         y3^3,
         {y3: y3, y2: y2, y1: y1*y3, y0: y0*y1*y2*y3})
        sage: T.apply_rules(*gf(T.inequalities, B))
        (-y1*y2*y3^4 - y2*y3^4 + y2*y3^3 + y3^3,
         (y0*y1*y2*y3, y1*y3, y3, y1*y2*y3, y2*y3))
        sage: eq(_,  gf(ieqs, B))
        True

        sage: ieqs = [(0, -1, 1, 0, 0), (-2, 0, -1, 0, 1),
        ....:         (-3, -1, 0, 1, 0), (0, 0, 0, -1, 1)]
        sage: T = prepare(ieqs, [], B); T.inequalities, T.factor, T.rules
        ([(1, 0, -1, 1, 1)],
         y2^3*y3^3,
         {y3: y3, y2: y2*y3, y1: y1, y0: y0*y1*y2*y3})
        sage: T.apply_rules(*gf(T.inequalities, B))
        (-y1*y2^4*y3^4 - y1*y2^3*y3^4 + y1*y2^3*y3^3 + y2^3*y3^3,
         (y0*y1*y2*y3, y2*y3, y3, y1*y2*y3, y1*y3))
        sage: eq(_, gf(ieqs, B))
        True

        sage: ieqs = [(0, -1, 1, 0, 0), (-3, 0, -1, 0, 1),
        ....:         (-2, -1, 0, 1, 0), (0, 0, 0, -1, 1)]
        sage: T = prepare(ieqs, [], B); T.inequalities, T.factor, T.rules
        ([(1, 0, 1, -1, 1)],
         y2^2*y3^3,
         {y3: y3, y2: y2, y1: y1*y3, y0: y0*y1*y2*y3})
        sage: T.apply_rules(*gf(T.inequalities, B))
        (-y1*y2^3*y3^4 - y2^3*y3^4 + y2^3*y3^3 + y2^2*y3^3,
         (y0*y1*y2*y3, y1*y3, y3, y1*y2*y3, y2*y3))
        sage: eq(_, gf(ieqs, B))
        True

        sage: ieqs = [(-2, -1, 1, 0, 0), (0, 0, -1, 0, 1),
        ....:         (0, -1, 0, 1, 0), (-3, 0, 0, -1, 1)]
        sage: T = prepare(ieqs, [], B); T.inequalities, T.factor, T.rules
        ([(1, 0, -1, 1, 1)],
         y1^2*y3^3,
         {y3: y3, y2: y2*y3, y1: y1, y0: y0*y1*y2*y3})
        sage: T.apply_rules(*gf(T.inequalities, B))
        (-y1^3*y2*y3^4 - y1^3*y3^4 + y1^3*y3^3 + y1^2*y3^3,
         (y0*y1*y2*y3, y2*y3, y3, y1*y2*y3, y1*y3))
        sage: eq(_, gf(ieqs, B))
        True

        sage: ieqs = [(-3, -1, 1, 0, 0), (0, 0, -1, 0, 1),
        ....:         (0, -1, 0, 1, 0), (-2, 0, 0, -1, 1)]
        sage: T = prepare(ieqs, [], B); T.inequalities, T.factor, T.rules
        ([(1, 0, 1, -1, 1)],
         y1^3*y3^3,
         {y3: y3, y2: y2, y1: y1*y3, y0: y0*y1*y2*y3})
        sage: T.apply_rules(*gf(T.inequalities, B))
        (-y1^4*y2*y3^4 - y1^3*y2*y3^4 + y1^3*y2*y3^3 + y1^3*y3^3,
         (y0*y1*y2*y3, y1*y3, y3, y1*y2*y3, y2*y3))
        sage: eq(_, gf(ieqs, B))
        True

        sage: ieqs = [(-2, -1, 1, 0, 0), (0, 0, -1, 0, 1),
        ....:         (-3, -1, 0, 1, 0), (0, 0, 0, -1, 1)]
        sage: T = prepare(ieqs, [], B); T.inequalities, T.factor, T.rules
        ([(1, 0, -1, 1, 1)],
         y1^2*y2^3*y3^3,
         {y3: y3, y2: y2*y3, y1: y1, y0: y0*y1*y2*y3})
        sage: T.apply_rules(*gf(T.inequalities, B))
        (-y1^3*y2^4*y3^4 - y1^3*y2^3*y3^4 + y1^3*y2^3*y3^3 + y1^2*y2^3*y3^3,
         (y0*y1*y2*y3, y2*y3, y3, y1*y2*y3, y1*y3))
        sage: eq(_, gf(ieqs, B))
        True

        sage: ieqs = [(-3, -1, 1, 0, 0), (0, 0, -1, 0, 1),
        ....:         (-2, -1, 0, 1, 0), (0, 0, 0, -1, 1)]
        sage: T = prepare(ieqs, [], B); T.inequalities, T.factor, T.rules
        ([(1, 0, 1, -1, 1)],
         y1^3*y2^2*y3^3,
         {y3: y3, y2: y2, y1: y1*y3, y0: y0*y1*y2*y3})
        sage: T.apply_rules(*gf(T.inequalities, B))
        (-y1^4*y2^3*y3^4 - y1^3*y2^3*y3^4 + y1^3*y2^3*y3^3 + y1^3*y2^2*y3^3,
         (y0*y1*y2*y3, y1*y3, y3, y1*y2*y3, y2*y3))
        sage: eq(_, gf(ieqs, B))
        True
    """

class _EliminateByEquations(_TransformHrepresentation):
    '''
    Prepare the substitutions coming from "eliminated" variables
    in the given equations.

    INPUT:

    - ``inequalities`` -- list of tuples of numbers

    - ``equations`` -- list of tuples of numbers

    - ``B`` -- a Laurent polynomial ring

    ATTRIBUTES:

    - ``inequalities``, ``equations`` -- list of tuples

      Determine the generating function of these inequalities
      and equations instead of the input.

    - ``factor`` -- a Laurent polynomial

      The numerator of the generating function has to be multiplied
      with ``factor`` *after* substituting ``rules``.

    - ``rules`` -- dictionary mapping Laurent polynomial variables to
      Laurent polynomials

      Substitute ``rules`` into the generating function.

    - ``indices`` -- a sorted tuple of integers representing
      indices of Laurent polynomial ring variables

      These are exactly the "eliminated" variables which we take care of
      by ``factor`` and ``rules``.

    The generating function of the input ``inequalities`` and
    ``equations`` is equal to the generating function of the
    attributes ``inequalities`` and ``equations`` in which ``rules``
    were substitited and ``factor`` was multiplied (via
    :meth:`~_TransformHrepresentation.apply_rules`).

    EXAMPLES::

        sage: from sage.geometry.polyhedron.generating_function import _EliminateByEquations

        sage: def prepare_equations(equations, B):
        ....:     T = _EliminateByEquations([], equations, B)
        ....:     return T.factor, T.rules, T.indices

        sage: B = LaurentPolynomialRing(ZZ, \'y\', 4)
        sage: prepare_equations([(1, 1, 1, -1, 0)], B)
        (y2, {y1: y1*y2, y0: y0*y2}, (2,))
        sage: prepare_equations([(0, 1, 0, -1, 0)], B)
        (1, {y0: y0*y2}, (2,))
        sage: prepare_equations([(-1, 0, 1, -1, -1), (1, 1, 0, 1, 2)], B)
        (y2^-1, {y1: y1*y2^2*y3^-1, y0: y0*y2*y3^-1}, (2, 3))

    TESTS::

        sage: B = LaurentPolynomialRing(ZZ, \'y\', 4)
        sage: prepare_equations([(0, 0, 1, 0, -1), (-1, 1, -1, -1, 0)], B)
        (y2^-1, {y1: y1*y2^-1*y3, y0: y0*y2}, (2, 3))

        sage: B = LaurentPolynomialRing(ZZ, \'y\', 5)
        sage: prepare_equations([(0, 0, 0, 1, 0, -1), (0, 1, 0, 0, -1, 0),
        ....:                    (0, 1, -1, 0, 0, 0)], B)
        (1, {y2: y2*y4, y0: y0*y1*y3}, (1, 3, 4))
    '''
    @staticmethod
    def prepare_equations_transformation(E):
        '''
        Return a transformation matrix and indices which variables
        in the equation to "eliminate" and deal with later.

        INPUT:

        - ``E`` -- a matrix whose rows represent equations

        OUTPUT:

        A triple ``(TE, indices, indicesn)`` with the following properties:

        - ``TE`` -- a matrix

          This matrix arises from ``E`` by multiplying a transformation matrix
          on the left.

        - ``indices`` -- a sorted tuple of integers representing column indices

          The the sub-matrix of ``TE`` with columns ``indices``
          is the identity matrix.

        - ``indicesn`` -- a sorted tuple of integers representing column indices

          ``indicesn`` contains ``0`` and all indices of the columns of ``E``
          which are nonzero.

        TESTS::

            sage: from sage.geometry.polyhedron.generating_function import _EliminateByEquations

            sage: _EliminateByEquations.prepare_equations_transformation(matrix([(0, 1, 0, -2)]))
            ([   0 -1/2    0    1], (3,), (0, 1))
            sage: _EliminateByEquations.prepare_equations_transformation(matrix([(0, 1, -2, 0), (0, 2, 0, -3)]))
            (
            [   0 -1/2    1    0]
            [   0 -2/3    0    1], (2, 3), (0, 1)
            )
        '''

class _TransformMod(_TransformHrepresentation):
    """
    Prepare the substitutions coming from the moduli.

    INPUT:

    - ``inequalities`` -- list of tuples of numbers

    - ``equations`` -- list of tuples of numbers

    - ``B`` -- a Laurent polynomial ring

    - ``mod`` -- dictionary mapping an index ``i`` to ``(m, r)``

      This is one entry of the output tuple of :meth:`generate_mods`.

    ATTRIBUTES:

    - ``inequalities``, ``equations`` -- list of tuples

      Determine the generating function of these inequalities
      and equations instead of the input.

    - ``factor`` -- a Laurent polynomial

      The numerator of the generating function has to be multiplied
      with ``factor`` *after* substituting ``rules``.

    - ``rules`` -- dictionary mapping Laurent polynomial variables to
      Laurent polynomials

      Substitute ``rules`` into the generating function.

    The generating function of the input ``inequalities`` and
    ``equations`` is equal to the generating function of the
    attributes ``inequalities`` and ``equations`` in which ``rules``
    were substitited and ``factor`` was multiplied (via
    :meth:`~_TransformHrepresentation.apply_rules`).

    EXAMPLES::

        sage: from sage.geometry.polyhedron.generating_function import _TransformMod

        sage: def prepare_mod(mod, B, *vecs):
        ....:     inequalities, equations = vecs
        ....:     T = _TransformMod(inequalities, equations, B, mod)
        ....:     return T.factor, T.rules, T.inequalities, T.equations

        sage: B = LaurentPolynomialRing(ZZ, 'y', 3)
        sage: prepare_mod({0: (2, 1)}, B, [(1, -1, 0, 2)], [])
        (y0, {y2: y2, y1: y1, y0: y0^2}, [(0, -2, 0, 2)], [])
        sage: prepare_mod({0: (2, 1), 1: (2, 1)}, B,
        ....:             [(0, -1, -1, 2)], [(0, -1, 1, 0)])
        (y0*y1, {y2: y2, y1: y1^2, y0: y0^2},
         [(-2, -2, -2, 2)], [(0, -2, 2, 0)])
    """
    mod: Incomplete
    def __init__(self, inequalities, equations, B, mod) -> None:
        """
        See :class:`_TransformMod` for details.

        TESTS::

            sage: from sage.geometry.polyhedron.generating_function import _TransformMod
            sage: B = LaurentPolynomialRing(ZZ, 'y', 2)
            sage: _TransformMod([], [], B, {})
            <..._TransformMod object at 0x...>
        """
    @staticmethod
    def generate_mods(equations):
        """
        Extract the moduli and residue classes implied
        by the equations.

        INPUT:

        - ``equations`` -- list of tuples

        OUTPUT:

        A tuple where each entry represents one possible configuration.
        Each entry is a dictionary mapping ``i`` to ``(m, r)`` with the following
        meaning: The ``i``-th coordinate of each element of the polyhedron
        has to be congruent to ``r`` modulo ``m``.

        TESTS::

            sage: from sage.geometry.polyhedron.generating_function import _TransformMod
            sage: _TransformMod.generate_mods([(0, 1, 1, -2)])
            ({0: (2, 0), 1: (2, 0)}, {0: (2, 1), 1: (2, 1)})
        """
