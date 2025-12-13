from sage.manifolds.utilities import simplify_chain_generic as simplify_chain_generic, simplify_chain_generic_sympy as simplify_chain_generic_sympy, simplify_chain_real as simplify_chain_real, simplify_chain_real_sympy as simplify_chain_real_sympy
from sage.misc.latex import latex as latex
from sage.structure.sage_object import SageObject as SageObject
from sage.symbolic.ring import SR as SR

class CalculusMethod(SageObject):
    """
    Control of calculus backends used on coordinate charts of manifolds.

    This class stores the possible calculus methods and permits to switch
    between them, as well as to change the simplifying functions associated
    with them.
    For the moment, only two calculus backends are implemented:

    - Sage's symbolic engine (Pynac + Maxima), implemented via the
      Symbolic Ring ``SR``
    - SymPy engine, denoted ``sympy`` hereafter

    INPUT:

    - ``current`` -- (default: ``None``) string defining the calculus method
      that will be considered as the active one, until it is changed by
      :meth:`set`; must be one of

      - ``'SR'``: Sage's default symbolic engine (Symbolic Ring)
      - ``'sympy'``: SymPy
      - ``None``: the default calculus method (``'SR'``)

    - ``base_field_type`` -- (default: ``'real'``) base field type of the
      manifold (cf.
      :meth:`~sage.manifolds.manifold.TopologicalManifold.base_field_type`)

    EXAMPLES::

        sage: from sage.manifolds.calculus_method import CalculusMethod
        sage: cm = CalculusMethod()

    In the display, the currently active method is pointed out with a star::

        sage: cm
        Available calculus methods (* = current):
         - SR (default) (*)
         - sympy

    It can be changed with :meth:`set`::

        sage: cm.set('sympy')
        sage: cm
        Available calculus methods (* = current):
         - SR (default)
         - sympy (*)

    while :meth:`reset` brings back to the default::

        sage: cm.reset()
        sage: cm
        Available calculus methods (* = current):
         - SR (default) (*)
         - sympy

    See :meth:`simplify_function` for the default simplification algorithms
    associated with each calculus method and :meth:`set_simplify_function` for
    introducing a new simplification algorithm.
    """
    def __init__(self, current=None, base_field_type: str = 'real') -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: from sage.manifolds.calculus_method import CalculusMethod
            sage: cm = CalculusMethod(base_field_type='complex')
            sage: cm
            Available calculus methods (* = current):
             - SR (default) (*)
             - sympy
        """
    def simplify(self, expression, method=None):
        """
        Apply the simplifying function associated with a given calculus method
        to a symbolic expression.

        INPUT:

        - ``expression`` -- symbolic expression to simplify

        - ``method`` -- (default: ``None``) string defining the calculus method
          to use; must be one of

          - ``'SR'``: Sage's default symbolic engine (Symbolic Ring)
          - ``'sympy'``: SymPy
          - ``None``: the current calculus method of ``self`` is used

        OUTPUT: the simplified version of ``expression``

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x, y> = M.chart()
            sage: f = x^2 + sin(x)^2 + cos(x)^2
            sage: from sage.manifolds.calculus_method import CalculusMethod
            sage: cm = CalculusMethod(base_field_type='real')
            sage: cm.simplify(f)
            x^2 + 1

        Using a weaker simplifying function, like
        :func:`~sage.calculus.functional.simplify`, does not succeed in this
        case::

            sage: cm.set_simplify_function(simplify)
            sage: cm.simplify(f)
            x^2 + cos(x)^2 + sin(x)^2

        Back to the default simplifying function
        (:func:`~sage.manifolds.utilities.simplify_chain_real` in the present
        case)::

            sage: cm.set_simplify_function('default')
            sage: cm.simplify(f)
            x^2 + 1

        A ``SR`` expression, such as ``f``, cannot be simplified when the
        current calculus method is ``sympy``::

            sage: cm.set('sympy')
            sage: cm.simplify(f)
            Traceback (most recent call last):
            ...
            AttributeError: 'sage.symbolic.expression.Expression' object has no attribute 'combsimp'...

        In the present case, one should either transform ``f`` to a SymPy
        object::

            sage: cm.simplify(f._sympy_())
            x**2 + 1

        or force the calculus method to be ``'SR'``::

            sage: cm.simplify(f, method='SR')
            x^2 + 1
        """
    def is_trivial_zero(self, expression, method=None):
        """
        Check if an expression is trivially equal to zero without any
        simplification.

        INPUT:

        - ``expression`` -- expression

        - ``method`` -- (default: ``None``) string defining the calculus method
          to use; if ``None`` the current calculus method of ``self`` is used

        OUTPUT: ``True`` is expression is trivially zero, ``False`` elsewhere

        EXAMPLES::

            sage: from sage.manifolds.calculus_method import CalculusMethod
            sage: cm = CalculusMethod(base_field_type='real')
            sage: f = sin(x) - sin(x)
            sage: cm.is_trivial_zero(f)
            True
            sage: cm.is_trivial_zero(f._sympy_(), method='sympy')
            True

        ::

            sage: f = sin(x)^2 + cos(x)^2 - 1
            sage: cm.is_trivial_zero(f)
            False
            sage: cm.is_trivial_zero(f._sympy_(), method='sympy')
            False
        """
    def set(self, method) -> None:
        """
        Set the currently active calculus method.

        - ``method`` -- string defining the calculus method

        EXAMPLES::

            sage: from sage.manifolds.calculus_method import CalculusMethod
            sage: cm = CalculusMethod(base_field_type='complex')
            sage: cm
            Available calculus methods (* = current):
             - SR (default) (*)
             - sympy
            sage: cm.set('sympy')
            sage: cm
            Available calculus methods (* = current):
             - SR (default)
             - sympy (*)
            sage: cm.set('lala')
            Traceback (most recent call last):
            ...
            NotImplementedError: method lala not implemented
        """
    def current(self):
        """
        Return the active calculus method as a string.

        OUTPUT:

        String defining the calculus method; one of

        - ``'SR'`` -- Sage's default symbolic engine (Symbolic Ring)
        - ``'sympy'`` -- SymPy

        EXAMPLES::

            sage: from sage.manifolds.calculus_method import CalculusMethod
            sage: cm = CalculusMethod(); cm
            Available calculus methods (* = current):
             - SR (default) (*)
             - sympy
            sage: cm.current()
            'SR'
            sage: cm.set('sympy')
            sage: cm.current()
            'sympy'
        """
    def set_simplify_function(self, simplifying_func, method=None) -> None:
        """
        Set the simplifying function associated to a given calculus method.

        INPUT:

        - ``simplifying_func`` -- either the string ``'default'`` for restoring
          the default simplifying function or a function ``f`` of a single
          argument ``expr`` such that ``f(expr)`` returns an object of the same
          type as ``expr`` (hopefully the simplified version of ``expr``), this
          type being

          - :class:`~sage.symbolic.expression.Expression` if ``method`` = ``'SR'``
          - a SymPy type if ``method`` = ``'sympy'``

        - ``method`` -- (default: ``None``) string defining the calculus method
          for which ``simplifying_func`` is provided; must be one of

          - ``'SR'``: Sage's default symbolic engine (Symbolic Ring)
          - ``'sympy'``: SymPy
          - ``None``: the currently active calculus method of ``self`` is
            assumed

        EXAMPLES:

        On a real manifold, the default simplifying function is
        :func:`~sage.manifolds.utilities.simplify_chain_real` when the
        calculus method is ``SR``::

            sage: from sage.manifolds.calculus_method import CalculusMethod
            sage: cm = CalculusMethod(base_field_type='real'); cm
            Available calculus methods (* = current):
             - SR (default) (*)
             - sympy
            sage: cm.simplify_function() is \\\n            ....: sage.manifolds.utilities.simplify_chain_real
            True

        Let us change it to :func:`~sage.calculus.functional.simplify`::

            sage: cm.set_simplify_function(simplify)
            sage: cm.simplify_function() is simplify
            True

        Since ``SR`` is the current calculus method, the above is equivalent
        to::

            sage: cm.set_simplify_function(simplify, method='SR')
            sage: cm.simplify_function(method='SR') is simplify
            True

        We revert to the default simplifying function by::

            sage: cm.set_simplify_function('default')

        Then we are back to::

            sage: cm.simplify_function() is \\\n            ....: sage.manifolds.utilities.simplify_chain_real
            True
        """
    def simplify_function(self, method=None):
        """
        Return the simplifying function associated to a given calculus method.

        The simplifying function is that used in all computations involved
        with the calculus method.

        INPUT:

        - ``method`` -- (default: ``None``) string defining the calculus method
          for which ``simplifying_func`` is provided; must be one of

          - ``'SR'``: Sage's default symbolic engine (Symbolic Ring)
          - ``'sympy'``: SymPy
          - ``None``: the currently active calculus method of ``self`` is
            assumed

        OUTPUT: the simplifying function

        EXAMPLES::

            sage: from sage.manifolds.calculus_method import CalculusMethod
            sage: cm = CalculusMethod()
            sage: cm
            Available calculus methods (* = current):
             - SR (default) (*)
             - sympy
            sage: cm.simplify_function()  # random (memory address)
            <function simplify_chain_real at 0x7f958d5b6758>

        The output stands for the function
        :func:`~sage.manifolds.utilities.simplify_chain_real`::

            sage: cm.simplify_function() is \\\n            ....: sage.manifolds.utilities.simplify_chain_real
            True

        Since ``SR`` is the default calculus method, we have::

            sage: cm.simplify_function() is cm.simplify_function(method='SR')
            True

        The simplifying function associated with ``sympy`` is
        :func:`~sage.manifolds.utilities.simplify_chain_real_sympy`::

            sage: cm.simplify_function(method='sympy')  # random (memory address)
            <function simplify_chain_real_sympy at 0x7f0b35a578c0>
            sage: cm.simplify_function(method='sympy') is \\\n            ....: sage.manifolds.utilities.simplify_chain_real_sympy
            True

        On complex manifolds, the simplifying functions are
        :func:`~sage.manifolds.utilities.simplify_chain_generic`
        and :func:`~sage.manifolds.utilities.simplify_chain_generic_sympy`
        for respectively ``SR`` and ``sympy``::

            sage: cmc = CalculusMethod(base_field_type='complex')
            sage: cmc.simplify_function(method='SR') is \\\n            ....: sage.manifolds.utilities.simplify_chain_generic
            True
            sage: cmc.simplify_function(method='sympy') is \\\n            ....: sage.manifolds.utilities.simplify_chain_generic_sympy
            True

        Note that the simplifying functions can be customized via
        :meth:`set_simplify_function`.
        """
    def reset(self) -> None:
        """
        Set the current calculus method to the default one.

        EXAMPLES::

            sage: from sage.manifolds.calculus_method import CalculusMethod
            sage: cm = CalculusMethod(base_field_type='complex')
            sage: cm
            Available calculus methods (* = current):
             - SR (default) (*)
             - sympy
            sage: cm.set('sympy')
            sage: cm
            Available calculus methods (* = current):
             - SR (default)
             - sympy (*)
            sage: cm.reset()
            sage: cm
            Available calculus methods (* = current):
             - SR (default) (*)
             - sympy
        """
