import types
from sage.structure.sage_object import SageObject as SageObject

class _ProofPref(SageObject):
    """
    An object that holds global proof preferences.  For now these are merely
    boolean flags for various parts of Sage that use probabilistic
    algorithms.

    A ``True`` flag means that the subsystem (such as linear algebra or number
    fields) should return results that are true unconditionally: the
    correctness should not depend on an algorithm with a nonzero probability of
    returning an incorrect answer or on the truth of any unproven conjectures.

    A ``False`` flag means that the subsystem can use faster methods to return
    answers that have a very small probability of being wrong.
    """
    def __init__(self, proof: bool = True) -> None: ...
    def arithmetic(self, t=None):
        """
        Controls the default proof strategy for integer arithmetic algorithms (such as primality testing).

        INPUT:

        - ``t`` -- boolean or ``None``

        OUTPUT:

        - if ``t == True``, requires integer arithmetic operations to (by
          default) return results that are true unconditionally: the
          correctness will not depend on an algorithm with a nonzero
          probability of returning an incorrect answer or on the truth of any
          unproven conjectures.
        - if ``t == False``, allows integer arithmetic operations to (by
          default) return results that may depend on unproven conjectures or on
          probabilistic algorithms.  Such algorithms often have a substantial
          speed improvement over those requiring proof.
        - if ``t == None``, returns the integer arithmetic proof status.

        EXAMPLES::

            sage: proof.arithmetic()
            True
            sage: proof.arithmetic(False)
            sage: proof.arithmetic()
            False
            sage: proof.arithmetic(True)
            sage: proof.arithmetic()
            True
        """
    def elliptic_curve(self, t=None):
        """
        Controls the default proof strategy for elliptic curve algorithms.

        INPUT:

        - ``t`` -- boolean or ``None``

        OUTPUT:

        - if ``t == True``, requires elliptic curve algorithms to (by default)
          return results that are true unconditionally: the correctness will
          not depend on an algorithm with a nonzero probability of returning an
          incorrect answer or on the truth of any unproven conjectures.
        - if ``t == False``, allows elliptic curve algorithms to (by default)
          return results that may depend on unproven conjectures or on
          probabilistic algorithms.  Such algorithms often have a substantial
          speed improvement over those requiring proof.
        - if ``t == None``, returns the current elliptic curve proof status.

        EXAMPLES::

            sage: proof.elliptic_curve()
            True
            sage: proof.elliptic_curve(False)
            sage: proof.elliptic_curve()
            False
            sage: proof.elliptic_curve(True)
            sage: proof.elliptic_curve()
            True
        """
    def linear_algebra(self, t=None):
        """
        Controls the default proof strategy for linear algebra algorithms.

        INPUT:

        - ``t`` -- boolean or ``None``

        OUTPUT:

        - if ``t == True``, requires linear algebra algorithms to (by default)
          return results that are true unconditionally: the correctness will
          not depend on an algorithm with a nonzero probability of returning an
          incorrect answer or on the truth of any unproven conjectures.
        - if ``t == False``, allows linear algebra algorithms to (by default)
          return results that may depend on unproven conjectures or on
          probabilistic algorithms.  Such algorithms often have a substantial
          speed improvement over those requiring proof.
        - if ``t == None``, returns the current linear algebra proof status.

        EXAMPLES::

            sage: proof.linear_algebra()
            True
            sage: proof.linear_algebra(False)
            sage: proof.linear_algebra()
            False
            sage: proof.linear_algebra(True)
            sage: proof.linear_algebra()
            True
        """
    def number_field(self, t=None):
        """
        Controls the default proof strategy for number field algorithms.

        INPUT:

        - ``t`` -- boolean or ``None``

        OUTPUT:

        - if ``t == True``, requires number field algorithms to (by default)
          return results that are true unconditionally: the correctness will
          not depend on an algorithm with a nonzero probability of returning an
          incorrect answer or on the truth of any unproven conjectures.
        - if ``t == False``, allows number field algorithms to (by default)
          return results that may depend on unproven conjectures or on
          probabilistic algorithms.  Such algorithms often have a substantial
          speed improvement over those requiring proof.
        - if ``t == None``, returns the current number field proof status.

        EXAMPLES::

            sage: proof.number_field()
            True
            sage: proof.number_field(False)
            sage: proof.number_field()
            False
            sage: proof.number_field(True)
            sage: proof.number_field()
            True
        """
    def polynomial(self, t=None):
        """
        Controls the default proof strategy for polynomial algorithms.

        INPUT:

        - ``t`` -- boolean or ``None``

        OUTPUT:

        - if ``t == True``, requires polynomial algorithms to (by default)
          return results that are true unconditionally: the correctness will
          not depend on an algorithm with a nonzero probability of returning an
          incorrect answer or on the truth of any unproven conjectures.
        - if ``t == False``, allows polynomial algorithms to (by default)
          return results that may depend on unproven conjectures or on
          probabilistic algorithms.  Such algorithms often have a substantial
          speed improvement over those requiring proof.
        - if ``t == None``, returns the current polynomial proof status.

        EXAMPLES::

            sage: proof.polynomial()
            True
            sage: proof.polynomial(False)
            sage: proof.polynomial()
            False
            sage: proof.polynomial(True)
            sage: proof.polynomial()
            True
        """

def get_flag(t=None, subsystem=None):
    """
    Used for easily determining the correct proof flag to use.

    EXAMPLES::

        sage: from sage.structure.proof.proof import get_flag
        sage: get_flag(False)
        False
        sage: get_flag(True)
        True
        sage: get_flag()
        True
        sage: proof.all(False)
        sage: get_flag()
        False
    """

class WithProof:
    '''
    Use :class:`WithProof` to temporarily set the value of one of the proof
    systems for a block of code, with a guarantee that it will be set
    back to how it was before after the block is done, even if there is an error.

    EXAMPLES:

    This would hang "forever" if attempted with ``proof=True``::

        sage: proof.arithmetic(True)
        sage: with proof.WithProof(\'arithmetic\', False):                                # needs sage.libs.pari
        ....:      print((10^1000 + 453).is_prime())
        ....:      print(1/0)
        Traceback (most recent call last):
        ...
        ZeroDivisionError: rational division by zero
        sage: proof.arithmetic()
        True
    '''
    def __init__(self, subsystem, t) -> None:
        """
        TESTS::

            sage: proof.arithmetic(True)
            sage: P = proof.WithProof('arithmetic',False); P
            <sage.structure.proof.proof.WithProof object at ...>
            sage: P._subsystem
            'arithmetic'
            sage: P._t
            False
            sage: P._t_orig
            True
        """
    def __enter__(self) -> None:
        """
        TESTS::

            sage: proof.arithmetic(True)
            sage: P = proof.WithProof('arithmetic',False)
            sage: P.__enter__()
            sage: proof.arithmetic()
            False
            sage: proof.arithmetic(True)
        """
    def __exit__(self, *args) -> None:
        """
        TESTS::

            sage: proof.arithmetic(True)
            sage: P = proof.WithProof('arithmetic',False)
            sage: P.__enter__()
            sage: proof.arithmetic()
            False
            sage: P.__exit__()
            sage: proof.arithmetic()
            True
        """
