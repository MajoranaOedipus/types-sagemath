import _cython_3_2_1
from typing import Any, ClassVar, overload

unpickle_gaussian_mixture_distribution_v1: _cython_3_2_1.cython_function_or_method

class DiscreteDistribution(Distribution):
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class Distribution:
    """File: /build/sagemath/src/sage/src/sage/stats/hmm/distributions.pyx (starting at line 68)

        A distribution.
    """
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def plot(self, *args, **kwds) -> Any:
        """Distribution.plot(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/distributions.pyx (starting at line 117)

        Return a plot of the probability density function.

        INPUT:

        - ``args`` and ``kwds``, passed to the Sage :func:`plot` function

        OUTPUT: a :class:`Graphics` object

        EXAMPLES::

            sage: P = hmm.GaussianMixtureDistribution([(.2,-10,.5),(.6,1,1),(.2,20,.5)])
            sage: P.plot(-10,30)                                                        # needs sage.plot
            Graphics object consisting of 1 graphics primitive"""
    def prob(self, x) -> Any:
        """Distribution.prob(self, x)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/distributions.pyx (starting at line 95)

        The probability density function evaluated at `x`.

        INPUT:

        - ``x`` -- object

        OUTPUT: float

        EXAMPLES:

        This method must be defined in a derived class::

            sage: import sage.stats.hmm.distributions
            sage: sage.stats.hmm.distributions.Distribution().prob(0)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def sample(self, n=...) -> Any:
        """Distribution.sample(self, n=None)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/distributions.pyx (starting at line 72)

        Return either a single sample (the default) or `n` samples from
        this probability distribution.

        INPUT:

        - ``n`` -- ``None`` or a positive integer

        OUTPUT: a single sample if `n` is 1; otherwise many samples

        EXAMPLES:

        This method must be defined in a derived class::

            sage: import sage.stats.hmm.distributions
            sage: sage.stats.hmm.distributions.Distribution().sample()
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def sample(self, thedefault) -> Any:
        """Distribution.sample(self, n=None)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/distributions.pyx (starting at line 72)

        Return either a single sample (the default) or `n` samples from
        this probability distribution.

        INPUT:

        - ``n`` -- ``None`` or a positive integer

        OUTPUT: a single sample if `n` is 1; otherwise many samples

        EXAMPLES:

        This method must be defined in a derived class::

            sage: import sage.stats.hmm.distributions
            sage: sage.stats.hmm.distributions.Distribution().sample()
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def sample(self) -> Any:
        """Distribution.sample(self, n=None)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/distributions.pyx (starting at line 72)

        Return either a single sample (the default) or `n` samples from
        this probability distribution.

        INPUT:

        - ``n`` -- ``None`` or a positive integer

        OUTPUT: a single sample if `n` is 1; otherwise many samples

        EXAMPLES:

        This method must be defined in a derived class::

            sage: import sage.stats.hmm.distributions
            sage: sage.stats.hmm.distributions.Distribution().sample()
            Traceback (most recent call last):
            ...
            NotImplementedError"""

class GaussianDistribution(Distribution):
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class GaussianMixtureDistribution(Distribution):
    """GaussianMixtureDistribution(B, eps=1e-8, bool normalize=True)

    File: /build/sagemath/src/sage/src/sage/stats/hmm/distributions.pyx (starting at line 136)

    A probability distribution defined by taking a weighted linear
    combination of Gaussian distributions.

    EXAMPLES::

        sage: P = hmm.GaussianMixtureDistribution([(.3,1,2),(.7,-1,1)]); P
        0.3*N(1.0,2.0) + 0.7*N(-1.0,1.0)
        sage: P[0]
        (0.3, 1.0, 2.0)
        sage: P.is_fixed()
        False
        sage: P.fix(1)
        sage: P.is_fixed(0)
        False
        sage: P.is_fixed(1)
        True
        sage: P.unfix(1)
        sage: P.is_fixed(1)
        False"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, B, eps=..., boolnormalize=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/stats/hmm/distributions.pyx (starting at line 158)

                INPUT:

                - ``B`` -- list of triples ``(c_i, mean_i, std_i)``, where
                  the ``c_i`` and ``std_i`` are positive and the sum of the
                  ``c_i`` is `1`

                - ``eps`` -- positive real number; any standard deviation in B
                  less than eps is replaced by eps

                - ``normalize`` -- if ``True``, ensure that the ``c_i`` are nonnegative

                EXAMPLES::

                    sage: hmm.GaussianMixtureDistribution([(.3,1,2),(.7,-1,1)])
                    0.3*N(1.0,2.0) + 0.7*N(-1.0,1.0)
                    sage: hmm.GaussianMixtureDistribution([(1,-1,0)], eps=1e-3)
                    1.0*N(-1.0,0.001)
        """
    @overload
    def fix(self, i=...) -> Any:
        """GaussianMixtureDistribution.fix(self, i=None)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/distributions.pyx (starting at line 306)

        Set that this :class:`GaussianMixtureDistribution` (or its `i`-th
        component) is fixed when using Baum-Welch to update
        the corresponding HMM.

        INPUT:

        - ``i`` -- ``None`` (default) or integer; if given, only fix the
          `i`-th component

        EXAMPLES::

            sage: P = hmm.GaussianMixtureDistribution([(.2,-10,.5),(.6,1,1),(.2,20,.5)])
            sage: P.fix(1); P.is_fixed()
            False
            sage: P.is_fixed(1)
            True
            sage: P.fix(); P.is_fixed()
            True"""
    @overload
    def fix(self) -> Any:
        """GaussianMixtureDistribution.fix(self, i=None)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/distributions.pyx (starting at line 306)

        Set that this :class:`GaussianMixtureDistribution` (or its `i`-th
        component) is fixed when using Baum-Welch to update
        the corresponding HMM.

        INPUT:

        - ``i`` -- ``None`` (default) or integer; if given, only fix the
          `i`-th component

        EXAMPLES::

            sage: P = hmm.GaussianMixtureDistribution([(.2,-10,.5),(.6,1,1),(.2,20,.5)])
            sage: P.fix(1); P.is_fixed()
            False
            sage: P.is_fixed(1)
            True
            sage: P.fix(); P.is_fixed()
            True"""
    @overload
    def is_fixed(self, i=...) -> Any:
        """GaussianMixtureDistribution.is_fixed(self, i=None)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/distributions.pyx (starting at line 277)

        Return whether or not this :class:`GaussianMixtureDistribution` is
        fixed when using Baum-Welch to update the corresponding HMM.

        INPUT:

        - ``i`` -- ``None`` (default) or integer; if given, only return
          whether the `i`-th component is fixed

        EXAMPLES::

            sage: P = hmm.GaussianMixtureDistribution([(.2,-10,.5),(.6,1,1),(.2,20,.5)])
            sage: P.is_fixed()
            False
            sage: P.is_fixed(0)
            False
            sage: P.fix(0); P.is_fixed()
            False
            sage: P.is_fixed(0)
            True
            sage: P.fix(); P.is_fixed()
            True"""
    @overload
    def is_fixed(self) -> Any:
        """GaussianMixtureDistribution.is_fixed(self, i=None)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/distributions.pyx (starting at line 277)

        Return whether or not this :class:`GaussianMixtureDistribution` is
        fixed when using Baum-Welch to update the corresponding HMM.

        INPUT:

        - ``i`` -- ``None`` (default) or integer; if given, only return
          whether the `i`-th component is fixed

        EXAMPLES::

            sage: P = hmm.GaussianMixtureDistribution([(.2,-10,.5),(.6,1,1),(.2,20,.5)])
            sage: P.is_fixed()
            False
            sage: P.is_fixed(0)
            False
            sage: P.fix(0); P.is_fixed()
            False
            sage: P.is_fixed(0)
            True
            sage: P.fix(); P.is_fixed()
            True"""
    @overload
    def is_fixed(self) -> Any:
        """GaussianMixtureDistribution.is_fixed(self, i=None)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/distributions.pyx (starting at line 277)

        Return whether or not this :class:`GaussianMixtureDistribution` is
        fixed when using Baum-Welch to update the corresponding HMM.

        INPUT:

        - ``i`` -- ``None`` (default) or integer; if given, only return
          whether the `i`-th component is fixed

        EXAMPLES::

            sage: P = hmm.GaussianMixtureDistribution([(.2,-10,.5),(.6,1,1),(.2,20,.5)])
            sage: P.is_fixed()
            False
            sage: P.is_fixed(0)
            False
            sage: P.fix(0); P.is_fixed()
            False
            sage: P.is_fixed(0)
            True
            sage: P.fix(); P.is_fixed()
            True"""
    @overload
    def is_fixed(self) -> Any:
        """GaussianMixtureDistribution.is_fixed(self, i=None)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/distributions.pyx (starting at line 277)

        Return whether or not this :class:`GaussianMixtureDistribution` is
        fixed when using Baum-Welch to update the corresponding HMM.

        INPUT:

        - ``i`` -- ``None`` (default) or integer; if given, only return
          whether the `i`-th component is fixed

        EXAMPLES::

            sage: P = hmm.GaussianMixtureDistribution([(.2,-10,.5),(.6,1,1),(.2,20,.5)])
            sage: P.is_fixed()
            False
            sage: P.is_fixed(0)
            False
            sage: P.fix(0); P.is_fixed()
            False
            sage: P.is_fixed(0)
            True
            sage: P.fix(); P.is_fixed()
            True"""
    def prob(self, doublex) -> double:
        """GaussianMixtureDistribution.prob(self, double x) -> double

        File: /build/sagemath/src/sage/src/sage/stats/hmm/distributions.pyx (starting at line 452)

        Return the probability of `x`.

        Since this is a continuous distribution, this is defined to be
        the limit of the p's such that the probability of [x,x+h] is p*h.

        INPUT:

        - ``x`` -- float

        OUTPUT: float

        EXAMPLES::

            sage: P = hmm.GaussianMixtureDistribution([(.2,-10,.5),(.6,1,1),(.2,20,.5)])
            sage: P.prob(.5)
            0.21123919605857971
            sage: P.prob(-100)
            0.0
            sage: P.prob(20)
            0.1595769121605731"""
    def prob_m(self, doublex, intm) -> double:
        """GaussianMixtureDistribution.prob_m(self, double x, int m) -> double

        File: /build/sagemath/src/sage/src/sage/stats/hmm/distributions.pyx (starting at line 486)

        Return the probability of `x` using just the `m`-th summand.

        INPUT:

        - ``x`` -- float
        - ``m`` -- integer

        OUTPUT: float

        EXAMPLES::

            sage: P = hmm.GaussianMixtureDistribution([(.2,-10,.5),(.6,1,1),(.2,20,.5)])
            sage: P.prob_m(.5, 0)
            2.7608117680508...e-97
            sage: P.prob_m(.5, 1)
            0.21123919605857971
            sage: P.prob_m(.5, 2)
            0.0"""
    @overload
    def sample(self, n=...) -> Any:
        """GaussianMixtureDistribution.sample(self, n=None)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/distributions.pyx (starting at line 375)

        Return a single sample from this distribution (by default), or
        if `n>1`, return a :class:`TimeSeries` of samples.

        INPUT:

        - ``n`` -- integer or ``None`` (default: ``None``)

        OUTPUT:

        - float if ``n`` is ``None`` (default); otherwise a :class:`TimeSeries`

        EXAMPLES::

            sage: P = hmm.GaussianMixtureDistribution([(.2,-10,.5),(.6,1,1),(.2,20,.5)])
            sage: type(P.sample())
            <class 'float'>
            sage: l = P.sample(1)
            sage: len(l)
            1
            sage: type(l)
            <class 'sage.stats.time_series.TimeSeries'>
            sage: l = P.sample(5)
            sage: len(l)
            5
            sage: type(l)
            <class 'sage.stats.time_series.TimeSeries'>
            sage: l = P.sample(0)
            sage: len(l)
            0
            sage: type(l)
            <class 'sage.stats.time_series.TimeSeries'>
            sage: P.sample(-3)
            Traceback (most recent call last):
            ...
            ValueError: n must be nonnegative"""
    @overload
    def sample(self) -> Any:
        """GaussianMixtureDistribution.sample(self, n=None)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/distributions.pyx (starting at line 375)

        Return a single sample from this distribution (by default), or
        if `n>1`, return a :class:`TimeSeries` of samples.

        INPUT:

        - ``n`` -- integer or ``None`` (default: ``None``)

        OUTPUT:

        - float if ``n`` is ``None`` (default); otherwise a :class:`TimeSeries`

        EXAMPLES::

            sage: P = hmm.GaussianMixtureDistribution([(.2,-10,.5),(.6,1,1),(.2,20,.5)])
            sage: type(P.sample())
            <class 'float'>
            sage: l = P.sample(1)
            sage: len(l)
            1
            sage: type(l)
            <class 'sage.stats.time_series.TimeSeries'>
            sage: l = P.sample(5)
            sage: len(l)
            5
            sage: type(l)
            <class 'sage.stats.time_series.TimeSeries'>
            sage: l = P.sample(0)
            sage: len(l)
            0
            sage: type(l)
            <class 'sage.stats.time_series.TimeSeries'>
            sage: P.sample(-3)
            Traceback (most recent call last):
            ...
            ValueError: n must be nonnegative"""
    @overload
    def unfix(self, i=...) -> Any:
        """GaussianMixtureDistribution.unfix(self, i=None)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/distributions.pyx (starting at line 334)

        Set that this :class:`GaussianMixtureDistribution` (or its `i`-th
        component) is not fixed when using Baum-Welch to update the
        corresponding HMM.

        INPUT:

        - ``i`` -- ``None`` (default) or integer; if given, only fix the
          `i`-th component

        EXAMPLES::

            sage: P = hmm.GaussianMixtureDistribution([(.2,-10,.5),(.6,1,1),(.2,20,.5)])
            sage: P.fix(1); P.is_fixed(1)
            True
            sage: P.unfix(1); P.is_fixed(1)
            False
            sage: P.fix(); P.is_fixed()
            True
            sage: P.unfix(); P.is_fixed()
            False"""
    @overload
    def unfix(self) -> Any:
        """GaussianMixtureDistribution.unfix(self, i=None)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/distributions.pyx (starting at line 334)

        Set that this :class:`GaussianMixtureDistribution` (or its `i`-th
        component) is not fixed when using Baum-Welch to update the
        corresponding HMM.

        INPUT:

        - ``i`` -- ``None`` (default) or integer; if given, only fix the
          `i`-th component

        EXAMPLES::

            sage: P = hmm.GaussianMixtureDistribution([(.2,-10,.5),(.6,1,1),(.2,20,.5)])
            sage: P.fix(1); P.is_fixed(1)
            True
            sage: P.unfix(1); P.is_fixed(1)
            False
            sage: P.fix(); P.is_fixed()
            True
            sage: P.unfix(); P.is_fixed()
            False"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __getitem__(self, Py_ssize_ti) -> Any:
        """GaussianMixtureDistribution.__getitem__(self, Py_ssize_t i)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/distributions.pyx (starting at line 198)

        Return triple (coefficient, mu, std).

        INPUT:

        - ``i`` -- integer

        OUTPUT: triple of floats

        EXAMPLES::

            sage: P = hmm.GaussianMixtureDistribution([(.2,-10,.5),(.6,1,1),(.2,20,.5)])
            sage: P[0]
            (0.2, -10.0, 0.5)
            sage: P[2]
            (0.2, 20.0, 0.5)
            sage: [-1]
            [-1]
            sage: P[-1]
            (0.2, 20.0, 0.5)
            sage: P[3]
            Traceback (most recent call last):
            ...
            IndexError: index out of range
            sage: P[-4]
            Traceback (most recent call last):
            ...
            IndexError: index out of range"""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __len__(self) -> Any:
        """GaussianMixtureDistribution.__len__(self)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/distributions.pyx (starting at line 266)

        Return the number of components of this GaussianMixtureDistribution.

        EXAMPLES::

            sage: len(hmm.GaussianMixtureDistribution([(.2,-10,.5),(.6,1,1),(.2,20,.5)]))
            3"""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __reduce__(self) -> Any:
        """GaussianMixtureDistribution.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/distributions.pyx (starting at line 233)

        Used in pickling.

        EXAMPLES::

            sage: G = hmm.GaussianMixtureDistribution([(.1,1,2), (.9,0,1)])
            sage: loads(dumps(G)) == G
            True"""
