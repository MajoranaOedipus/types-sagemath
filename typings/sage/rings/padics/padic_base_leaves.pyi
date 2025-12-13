from .generic_nodes import pAdicCappedAbsoluteRingGeneric as pAdicCappedAbsoluteRingGeneric, pAdicCappedRelativeFieldGeneric as pAdicCappedRelativeFieldGeneric, pAdicCappedRelativeRingGeneric as pAdicCappedRelativeRingGeneric, pAdicFieldBaseGeneric as pAdicFieldBaseGeneric, pAdicFixedModRingGeneric as pAdicFixedModRingGeneric, pAdicFloatingPointFieldGeneric as pAdicFloatingPointFieldGeneric, pAdicFloatingPointRingGeneric as pAdicFloatingPointRingGeneric, pAdicLatticeGeneric as pAdicLatticeGeneric, pAdicRelaxedGeneric as pAdicRelaxedGeneric, pAdicRingBaseGeneric as pAdicRingBaseGeneric
from .padic_capped_absolute_element import pAdicCappedAbsoluteElement as pAdicCappedAbsoluteElement
from .padic_capped_relative_element import pAdicCappedRelativeElement as pAdicCappedRelativeElement
from .padic_fixed_mod_element import pAdicFixedModElement as pAdicFixedModElement
from .padic_floating_point_element import pAdicFloatingPointElement as pAdicFloatingPointElement
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.richcmp import op_LE as op_LE

class pAdicRingCappedRelative(pAdicRingBaseGeneric, pAdicCappedRelativeRingGeneric):
    """
    An implementation of the `p`-adic integers with capped relative
    precision.
    """
    def __init__(self, p, prec, print_mode, names, category=None) -> None:
        """
        Initialization.

        INPUT:

        - ``p`` -- prime
        - ``prec`` -- precision cap
        - ``print_mode`` -- dictionary with print options
        - ``names`` -- how to print the prime

        EXAMPLES::

            sage: R = ZpCR(next_prime(10^60))  # indirect doctest
            sage: type(R)
            <class 'sage.rings.padics.padic_base_leaves.pAdicRingCappedRelative_with_category'>

        TESTS::

            sage: # needs sage.geometry.polyhedron
            sage: R = ZpCR(2)
            sage: TestSuite(R).run()
            sage: TestSuite(R).run(elements=[R.random_element() for i in range(2^10)],              # long time
            ....:                  max_runs=2^12, skip='_test_metric_function')
            sage: R._test_metric_function(elements=[R.random_element() for i in range(2^3)])        # long time
            sage: R = ZpCR(3, 1)
            sage: TestSuite(R).run(elements=[R.random_element() for i in range(3^3)])
            sage: R = ZpCR(3, 2)
            sage: TestSuite(R).run(elements=[R.random_element() for i in range(3^6)],               # long time
            ....:                  skip='_test_metric_function')
            sage: R._test_metric_function(elements=[R.random_element() for i in range(2^3)])        # long time
            sage: R = ZpCR(next_prime(10^60))
            sage: TestSuite(R).run(elements=[R.random_element() for i in range(2^3)],               # long time
            ....:                  max_runs=2^5, skip='_test_log')
            sage: R._test_log(max_runs=2, elements=[R.random_element() for i in range(4)])          # long time
        """

class pAdicRingCappedAbsolute(pAdicRingBaseGeneric, pAdicCappedAbsoluteRingGeneric):
    """
    An implementation of the `p`-adic integers with capped absolute precision.
    """
    def __init__(self, p, prec, print_mode, names, category=None) -> None:
        """
        Initialization.

        INPUT:

        - ``p`` -- prime
        - ``prec`` -- precision cap
        - ``print_mode`` -- dictionary with print options
        - ``names`` -- how to print the prime

        EXAMPLES::

            sage: R = ZpCA(next_prime(10^60))  # indirect doctest
            sage: type(R)
            <class 'sage.rings.padics.padic_base_leaves.pAdicRingCappedAbsolute_with_category'>

        TESTS::

            sage: # needs sage.geometry.polyhedron
            sage: R = ZpCA(2)
            sage: TestSuite(R).run()
            sage: TestSuite(R).run(elements=[R.random_element() for i in range(2^10)],              # long time
            ....:                  max_runs=2^12, skip='_test_metric_function')
            sage: R._test_metric_function(elements=[R.random_element() for i in range(2^3)])        # long time
            sage: R = ZpCA(3, 1)
            sage: TestSuite(R).run(elements=[R.random_element() for i in range(3^3)])
            sage: R = ZpCA(3, 2)
            sage: TestSuite(R).run(elements=[R.random_element() for i in range(3^6)],               # long time
            ....:                  skip='_test_metric_function')
            sage: R._test_metric_function(elements=[R.random_element() for i in range(2^3)])        # long time
            sage: R = ZpCA(next_prime(10^60))
            sage: TestSuite(R).run(elements=[R.random_element() for i in range(2^3)],               # long time
            ....:                  max_runs=2^5, skip='_test_log')
            sage: R._test_log(max_runs=2, elements=[R.random_element() for i in range(4)])
        """

class pAdicRingFloatingPoint(pAdicRingBaseGeneric, pAdicFloatingPointRingGeneric):
    """
    An implementation of the `p`-adic integers with floating point
    precision.
    """
    def __init__(self, p, prec, print_mode, names, category=None) -> None:
        """
        Initialization.

        INPUT:

        - ``p`` -- prime
        - ``prec`` -- precision cap
        - ``print_mode`` -- dictionary with print options
        - ``names`` -- how to print the prime

        EXAMPLES::

            sage: R = ZpFP(next_prime(10^60))  # indirect doctest
            sage: type(R)
            <class 'sage.rings.padics.padic_base_leaves.pAdicRingFloatingPoint_with_category'>

        TESTS::

            sage: # needs sage.geometry.polyhedron
            sage: R = ZpFP(2)
            sage: TestSuite(R).run()
            sage: TestSuite(R).run(elements=[R.random_element() for i in range(2^10)],              # long time
            ....:                  max_runs=2^12, skip='_test_metric_function')
            sage: R._test_metric_function(elements=[R.random_element() for i in range(2^3)])        # long time
            sage: R = ZpFP(3, 1)
            sage: TestSuite(R).run(elements=[R.random_element() for i in range(3^3)])
            sage: R = ZpFP(3, 2)
            sage: TestSuite(R).run(elements=[R.random_element() for i in range(3^6)],               # long time
            ....:                  skip='_test_metric_function')
            sage: R._test_metric_function(elements=[R.random_element() for i in range(2^3)])        # long time
            sage: R = ZpFP(next_prime(10^60))
            sage: TestSuite(R).run(elements=[R.random_element() for i in range(2^3)],               # long time
            ....:                  max_runs=2^5, skip='_test_log')
            sage: R._test_log(max_runs=2, elements=[R.random_element() for i in range(4)])
        """

class pAdicRingFixedMod(pAdicRingBaseGeneric, pAdicFixedModRingGeneric):
    """
    An implementation of the `p`-adic integers using fixed modulus.
    """
    def __init__(self, p, prec, print_mode, names, category=None) -> None:
        """
        Initialization.

        INPUT:

        - ``p`` -- prime
        - ``prec`` -- precision cap
        - ``print_mode`` -- dictionary with print options
        - ``names`` -- how to print the prime

        EXAMPLES::

            sage: R = ZpFM(next_prime(10^60))  # indirect doctest
            sage: type(R)
            <class 'sage.rings.padics.padic_base_leaves.pAdicRingFixedMod_with_category'>

        TESTS::

            sage: # needs sage.geometry.polyhedron
            sage: R = ZpFM(2)
            sage: TestSuite(R).run()
            sage: TestSuite(R).run(elements=[R.random_element() for i in range(2^10)],  # long time
            ....:                  max_runs=2^12, skip='_test_metric_function')
            sage: R._test_metric_function(elements=[R.random_element() for i in range(2^3)])        # long time
            sage: R = ZpFM(3, 1)
            sage: TestSuite(R).run(elements=[R.random_element() for i in range(3^3)])
            sage: R = ZpFM(3, 2)
            sage: TestSuite(R).run(elements=[R.random_element() for i in range(3^6)],  # long time
            ....:                  skip='_test_metric_function')
            sage: R._test_metric_function(elements=[R.random_element() for i in range(2^3)]) # long time
            sage: R = ZpFM(next_prime(10^60))
            sage: TestSuite(R).run(skip='_test_log')
            sage: TestSuite(R).run(elements=[R.random_element() for i in range(2^4)],  # long time
            ....:                  max_runs=2^6, skip='_test_log')
            sage: R._test_log(max_runs=2, elements=[R.random_element() for i in range(4)])

        Fraction fields work after :issue:`23510`::

            sage: R = ZpFM(5)
            sage: K = R.fraction_field(); K
            5-adic Field with floating precision 20
            sage: K(R(90))
            3*5 + 3*5^2
        """

class pAdicFieldCappedRelative(pAdicFieldBaseGeneric, pAdicCappedRelativeFieldGeneric):
    """
    An implementation of `p`-adic fields with capped relative precision.

    EXAMPLES::

        sage: K = Qp(17, 1000000)  # indirect doctest
        sage: K = Qp(101)  # indirect doctest
    """
    def __init__(self, p, prec, print_mode, names, category=None) -> None:
        """
        Initialization.

        INPUT:

        - ``p`` -- prime
        - ``prec`` -- precision cap
        - ``print_mode`` -- dictionary with print options
        - ``names`` -- how to print the prime

        EXAMPLES::

            sage: K = Qp(next_prime(10^60))  # indirect doctest
            sage: type(K)
            <class 'sage.rings.padics.padic_base_leaves.pAdicFieldCappedRelative_with_category'>

        TESTS::

            sage: # needs sage.geometry.polyhedron
            sage: R = Qp(2)
            sage: TestSuite(R).run()
            sage: TestSuite(R).run(elements=[R.random_element() for i in range(2^10)],  # long time
            ....:                  max_runs=2^12, skip='_test_metric_function')
            sage: R._test_metric_function(elements=[R.random_element() for i in range(2^3)])        # long time

            sage: R = Qp(3, 1)
            sage: TestSuite(R).run(elements=[R.random_element() for i in range(3^6)],  # long time, needs sage.geometry.polyhedron
            ....:                  skip='_test_metric_function')
            sage: R._test_metric_function(elements=[R.random_element() for i in range(2^3)])  # long time

            sage: R = Qp(3, 2)
            sage: TestSuite(R).run(elements=[R.random_element() for i in range(3^9)],  # long time, needs sage.geometry.polyhedron
            ....:                  skip='_test_metric_function')
            sage: R._test_metric_function(elements=[R.random_element() for i in range(3^3)])

            sage: R = Qp(next_prime(10^60))
            sage: TestSuite(R).run(skip='_test_log')                                    # needs sage.geometry.polyhedron
            sage: TestSuite(R).run(elements=[R.random_element() for i in range(2^3)],  # long time, needs sage.geometry.polyhedron
            ....:                  max_runs=2^5, skip='_test_log')
            sage: R._test_log(max_runs=2, elements=[R.random_element() for i in range(4)])
        """
    def random_element(self, algorithm: str = 'default'):
        """
        Return a random element of ``self``, optionally using the ``algorithm``
        argument to decide how it generates the element. Algorithms currently
        implemented:

        - ``'default'``: Choose an integer `k` using the standard
          distribution on the integers.  Then choose an integer `a`
          uniformly in the range `0 \\le a < p^N` where `N` is the
          precision cap of ``self``.  Return ``self(p^k * a, absprec =
          k + self.precision_cap())``.

        EXAMPLES::

            sage: Qp(17,6).random_element().parent() is Qp(17,6)
            True
        """

class pAdicFieldFloatingPoint(pAdicFieldBaseGeneric, pAdicFloatingPointFieldGeneric):
    """
    An implementation of the `p`-adic rationals with floating point
    precision.
    """
    def __init__(self, p, prec, print_mode, names, category=None) -> None:
        """
        Initialization.

        INPUT:

        - ``p`` -- prime
        - ``prec`` -- precision cap
        - ``print_mode`` -- dictionary with print options
        - ``names`` -- how to print the prime

        EXAMPLES::

            sage: R = QpFP(next_prime(10^60))  # indirect doctest
            sage: type(R)
            <class 'sage.rings.padics.padic_base_leaves.pAdicFieldFloatingPoint_with_category'>

        TESTS::

            sage: # needs sage.geometry.polyhedron
            sage: R = QpFP(2)
            sage: TestSuite(R).run()
            sage: TestSuite(R).run(elements=[R.random_element() for i in range(2^10)],  # long time
            ....:                  max_runs=2^12, skip='_test_metric_function')
            sage: R._test_metric_function(elements=[R.random_element() for i in range(2^3)])        # long time
            sage: R = QpFP(3, 1)
            sage: TestSuite(R).run(elements=[R.random_element() for i in range(3^3)])
            sage: R = QpFP(3, 2)
            sage: TestSuite(R).run(elements=[R.random_element() for i in range(3^6)],  # long time
            ....:                  skip='_test_metric_function')
            sage: R._test_metric_function(elements=[R.random_element() for i in range(2^3)])        # long time
            sage: R = QpFP(next_prime(10^60))
            sage: TestSuite(R).run(skip='_test_log')
            sage: TestSuite(R).run(elements=[R.random_element() for i in range(2^3)],  # long time
            ....:                  max_runs=2^5, skip='_test_log')
            sage: R._test_log(max_runs=2, elements=[R.random_element() for i in range(4)])
        """

class pAdicRingLattice(pAdicLatticeGeneric, pAdicRingBaseGeneric):
    """
    An implementation of the `p`-adic integers with lattice precision.

    INPUT:

    - ``p`` -- prime

    - ``prec`` -- precision cap, given as a pair (``relative_cap``, ``absolute_cap``)

    - ``subtype`` -- either ``'cap'`` or ``'float'``

    - ``print_mode`` -- dictionary with print options

    - ``names`` -- how to print the prime

    - ``label`` -- the label of this ring

    .. SEEALSO::

        :meth:`label`

    EXAMPLES::

        sage: R = ZpLC(next_prime(10^60))  # indirect doctest
        doctest:...: FutureWarning: This class/method/function is marked as experimental.
        It, its functionality or its interface might change without a formal deprecation.
        See https://github.com/sagemath/sage/issues/23505 for details.
        sage: type(R)
        <class 'sage.rings.padics.padic_base_leaves.pAdicRingLattice_with_category'>

        sage: R = ZpLC(2, label='init')  # indirect doctest
        sage: R
        2-adic Ring with lattice-cap precision (label: init)
    """
    def __init__(self, p, prec, subtype, print_mode, names, label=None, category=None) -> None:
        """
        Initialization.

        TESTS:

            sage: R = ZpLC(7, label='init')
            sage: TestSuite(R).run(skip=['_test_teichmuller', '_test_matrix_smith'])  # long time
        """
    def random_element(self, prec=None):
        """
        Return a random element of this ring.

        INPUT:

        - ``prec`` -- integer or ``None`` (default); the
          absolute precision of the generated random element

        EXAMPLES::

            sage: R = ZpLC(2)
            sage: R.random_element()    # random
            2^3 + 2^4 + 2^5 + 2^6 + 2^7 + 2^10 + 2^11 + 2^14 + 2^15 + 2^16
             + 2^17 + 2^18 + 2^19 + 2^21 + O(2^23)

            sage: R.random_element(prec=10)    # random
            1 + 2^3 + 2^4 + 2^7 + O(2^10)
        """

class pAdicFieldLattice(pAdicLatticeGeneric, pAdicFieldBaseGeneric):
    """
    An implementation of the `p`-adic numbers with lattice precision.

    INPUT:

    - ``p`` -- prime

    - ``prec`` -- precision cap, given as a pair (``relative_cap``, ``absolute_cap``)

    - ``subtype`` -- either ``'cap'`` or ``'float'``

    - ``print_mode`` -- dictionary with print options

    - ``names`` -- how to print the prime

    - ``label`` -- the label of this ring

    .. SEEALSO::

        :meth:`label`

    EXAMPLES::

        sage: R = QpLC(next_prime(10^60))  # indirect doctest
        doctest:...: FutureWarning: This class/method/function is marked as experimental.
        It, its functionality or its interface might change without a formal deprecation.
        See https://github.com/sagemath/sage/issues/23505 for details.
        sage: type(R)
        <class 'sage.rings.padics.padic_base_leaves.pAdicFieldLattice_with_category'>

        sage: R = QpLC(2,label='init')  # indirect doctest
        sage: R
        2-adic Field with lattice-cap precision (label: init)
    """
    def __init__(self, p, prec, subtype, print_mode, names, label=None, category=None) -> None:
        """
        Initialization.

        TESTS::

            sage: R = QpLC(7, label='init')
            sage: TestSuite(R).run(skip=['_test_teichmuller', '_test_matrix_smith'])  # long time
        """
    def random_element(self, prec=None, integral: bool = False):
        """
        Return a random element of this ring.

        INPUT:

        - ``prec`` -- integer or ``None`` (default); the
          absolute precision of the generated random element

        - ``integral`` -- boolean (default: ``False``); if ``True``,
          return an element in the ring of integers

        EXAMPLES::

            sage: K = QpLC(2)
            sage: K.random_element()   # not tested, known bug (see :issue:`32126`)
            2^-8 + 2^-7 + 2^-6 + 2^-5 + 2^-3 + 1 + 2^2 + 2^3 + 2^5 + O(2^12)
            sage: K.random_element(integral=True)    # random
            2^3 + 2^4 + 2^5 + 2^6 + 2^7 + 2^10 + 2^11 + 2^14 + 2^15 + 2^16
             + 2^17 + 2^18 + 2^19 + O(2^20)

            sage: K.random_element(prec=10)    # random
            2^(-3) + 1 + 2 + 2^4 + 2^8 + O(2^10)

        If the given precision is higher than the internal cap of the
        parent, then the cap is used::

            sage: K.precision_cap_relative()
            20
            sage: K.random_element(prec=100)    # random
            2^5 + 2^8 + 2^11 + 2^12 + 2^14 + 2^18 + 2^20 + 2^24 + O(2^25)
        """

class pAdicRingRelaxed(pAdicRelaxedGeneric, pAdicRingBaseGeneric):
    """
    An implementation of relaxed arithmetics over `\\ZZ_p`.

    INPUT:

    - ``p`` -- prime

    - ``prec`` -- default precision

    - ``print_mode`` -- dictionary with print options

    - ``names`` -- how to print the prime

    EXAMPLES::

        sage: R = ZpER(5)  # indirect doctest                                           # needs sage.libs.flint
        sage: type(R)                                                                   # needs sage.libs.flint
        <class 'sage.rings.padics.padic_base_leaves.pAdicRingRelaxed_with_category'>
    """
    def __init__(self, p, prec, print_mode, names, category=None) -> None:
        """
        Initialization.

        TESTS::

            sage: # needs sage.libs.flint
            sage: R = ZpER(7)
            sage: TestSuite(R).run(skip=['_test_log', '_test_matrix_smith'])
            sage: R = ZpER(7, secure=True)
            sage: TestSuite(R).run(skip=['_test_log', '_test_matrix_smith'])
        """

class pAdicFieldRelaxed(pAdicRelaxedGeneric, pAdicFieldBaseGeneric):
    """
    An implementation of relaxed arithmetics over `\\QQ_p`.

    INPUT:

    - ``p`` -- prime

    - ``prec`` -- default precision

    - ``print_mode`` -- dictionary with print options

    - ``names`` -- how to print the prime

    EXAMPLES::

        sage: R = QpER(5)  # indirect doctest                                           # needs sage.libs.flint
        sage: type(R)                                                                   # needs sage.libs.flint
        <class 'sage.rings.padics.padic_base_leaves.pAdicFieldRelaxed_with_category'>
    """
    def __init__(self, p, prec, print_mode, names, category=None) -> None:
        """
        Initialization.

        TESTS::

            sage: # needs sage.libs.flint
            sage: K = QpER(7)
            sage: TestSuite(K).run(skip=['_test_log', '_test_matrix_smith'])
            sage: K = QpER(7, secure=True)
            sage: TestSuite(K).run(skip=['_test_log', '_test_matrix_smith'])
        """
