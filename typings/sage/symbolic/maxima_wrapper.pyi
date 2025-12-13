from sage.interfaces.maxima import MaximaFunctionElement as MaximaFunctionElement
from sage.misc.instancedoc import instancedoc as instancedoc
from sage.structure.sage_object import SageObject as SageObject

class MaximaFunctionElementWrapper(MaximaFunctionElement):
    def __call__(self, *args, **kwds):
        """
        Return a Sage expression instead of a Maxima pexpect interface element.

        EXAMPLES::

            sage: t = sin(x)^2 + cos(x)^2; t
            cos(x)^2 + sin(x)^2
            sage: res = t.maxima_methods().trigsimp(); res
            1
            sage: parent(res)
            Symbolic Ring
        """

class MaximaWrapper(SageObject):
    def __init__(self, exp) -> None:
        """
        Wrapper around Sage expressions to give access to Maxima methods.

        We convert the given expression to Maxima and convert the return value
        back to a Sage expression. Tab completion and help strings of Maxima
        methods also work as expected.

        EXAMPLES::

            sage: t = log(sqrt(2) - 1) + log(sqrt(2) + 1); t
            log(sqrt(2) + 1) + log(sqrt(2) - 1)
            sage: u = t.maxima_methods(); u
            MaximaWrapper(log(sqrt(2) + 1) + log(sqrt(2) - 1))
            sage: type(u)
            <class 'sage.symbolic.maxima_wrapper.MaximaWrapper'>
            sage: u.logcontract()
            log((sqrt(2) + 1)*(sqrt(2) - 1))
            sage: u.logcontract().parent()
            Symbolic Ring

        TESTS:

        Test tab completions::

            sage: import sage.interfaces.tab_completion as s
            sage: u = t.maxima_methods()
            sage: s.completions('u.elliptic_',globals())
            ['u.elliptic_e', 'u.elliptic_ec', 'u.elliptic_eu', 'u.elliptic_f', 'u.elliptic_kc', 'u.elliptic_pi']
        """
    def __getattr__(self, s):
        """
        Direct attempts to get attributes of this wrapper to the corresponding
        Maxima expression. This allows tab completion to work as expected.

        We wrap the function calls in order to convert results back to Sage.

        EXAMPLES::

            sage: t = sin(x)^2 + cos(x)^2; t
            cos(x)^2 + sin(x)^2
            sage: u = t.maxima_methods()
            sage: import sage.interfaces.tab_completion as s
            sage: s.completions('u.airy_',globals())
            ['u.airy_ai', 'u.airy_bi', 'u.airy_dai', 'u.airy_dbi']
            sage: type(u.airy_ai)
            <class 'sage.symbolic.maxima_wrapper.MaximaFunctionElementWrapper'>
            sage: u.airy_ai()
            airy_ai(cos(x)^2 + sin(x)^2)
        """
    def __dir__(self):
        """
        Enable the tab completions.

        EXAMPLES::

            sage: t = sin(x) + cos(x)
            sage: u = t.maxima_methods()
            sage: 'zeta' in u.__dir__()
            True
        """
    def sage(self):
        """
        Return the Sage expression this wrapper corresponds to.

        EXAMPLES::

            sage: t = log(sqrt(2) - 1) + log(sqrt(2) + 1); t
            log(sqrt(2) + 1) + log(sqrt(2) - 1)
            sage: u = t.maxima_methods().sage()
            sage: u is t
            True
        """
    def __reduce__(self):
        """
        EXAMPLES::

            sage: t = log(sqrt(2) - 1) + log(sqrt(2) + 1); t
            log(sqrt(2) + 1) + log(sqrt(2) - 1)
            sage: u = t.maxima_methods(); u
            MaximaWrapper(log(sqrt(2) + 1) + log(sqrt(2) - 1))
            sage: loads(dumps(u))
            MaximaWrapper(log(sqrt(2) + 1) + log(sqrt(2) - 1))
        """
