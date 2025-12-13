from sage.functions.trig import cos as cos, sin as sin
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.structure.sage_object import SageObject as SageObject
from sage.structure.sequence import Sequence as Sequence

class IndexedSequence(SageObject):
    """
    An indexed sequence.

    INPUT:

    - ``L`` -- list

    - ``index_object`` -- must be a Sage object with an ``__iter__`` method
      containing the same number of elements as ``self``, which is a
      list of elements taken from a field
    """
    def __init__(self, L, index_object) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: J = list(range(10))
            sage: A = [1/10 for j in J]
            sage: s = IndexedSequence(A,J)
            sage: s
            Indexed sequence: [1/10, 1/10, 1/10, 1/10, 1/10, 1/10, 1/10, 1/10, 1/10, 1/10]
                indexed by [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            sage: s.dict()
            {0: 1/10,
             1: 1/10,
             2: 1/10,
             3: 1/10,
             4: 1/10,
             5: 1/10,
             6: 1/10,
             7: 1/10,
             8: 1/10,
             9: 1/10}
            sage: s.list()
            [1/10, 1/10, 1/10, 1/10, 1/10, 1/10, 1/10, 1/10, 1/10, 1/10]
            sage: s.index_object()
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            sage: s.base_ring()
            Rational Field
        """
    def dict(self):
        """
        Return a python dict of ``self`` where the keys are elements in the
        indexing set.

        EXAMPLES::

            sage: J = list(range(10))
            sage: A = [1/10 for j in J]
            sage: s = IndexedSequence(A,J)
            sage: s.dict()
            {0: 1/10, 1: 1/10, 2: 1/10, 3: 1/10, 4: 1/10, 5: 1/10, 6: 1/10, 7: 1/10, 8: 1/10, 9: 1/10}
        """
    def list(self):
        """
        Return the list of ``self``.

        EXAMPLES::

            sage: J = list(range(10))
            sage: A = [1/10 for j in J]
            sage: s = IndexedSequence(A,J)
            sage: s.list()
            [1/10, 1/10, 1/10, 1/10, 1/10, 1/10, 1/10, 1/10, 1/10, 1/10]
        """
    def base_ring(self):
        """
        This just returns the common parent `R` of the `N` list
        elements. In some applications (say, when computing the
        discrete Fourier transform, dft), it is more accurate to think
        of the base_ring as the group ring `\\QQ(\\zeta_N)[R]`.

        EXAMPLES::

            sage: J = list(range(10))
            sage: A = [1/10 for j in J]
            sage: s = IndexedSequence(A,J)
            sage: s.base_ring()
            Rational Field
        """
    def index_object(self):
        """
        Return the indexing object.

        EXAMPLES::

            sage: J = list(range(10))
            sage: A = [1/10 for j in J]
            sage: s = IndexedSequence(A,J)
            sage: s.index_object()
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        """
    def plot_histogram(self, clr=(0, 0, 1), eps: float = 0.4):
        """
        Plot the histogram plot of the sequence.

        The sequence is assumed to be real or from a finite field,
        with a real indexing set ``I`` coercible into `\\RR`.

        Options are ``clr``, which is an RGB value, and ``eps``, which
        is the spacing between the bars.

        EXAMPLES::

            sage: J = list(range(3))
            sage: A = [ZZ(i^2)+1 for i in J]
            sage: s = IndexedSequence(A,J)
            sage: P = s.plot_histogram()                                                # needs sage.plot
            sage: show(P)                       # not tested                            # needs sage.plot
        """
    def plot(self):
        """
        Plot the points of the sequence.

        Elements of the sequence are assumed to be real or from a
        finite field, with a real indexing set ``I = range(len(self))``.

        EXAMPLES::

            sage: I = list(range(3))
            sage: A = [ZZ(i^2)+1 for i in I]
            sage: s = IndexedSequence(A,I)
            sage: P = s.plot()                                                          # needs sage.plot
            sage: show(P)                       # not tested                            # needs sage.plot
        """
    def dft(self, chi=None):
        '''
        A discrete Fourier transform "over `\\QQ`" using exact
        `N`-th roots of unity.

        EXAMPLES::

            sage: J = list(range(6))
            sage: A = [ZZ(1) for i in J]
            sage: s = IndexedSequence(A,J)
            sage: s.dft(lambda x: x^2)                                                  # needs sage.rings.number_field
            Indexed sequence: [6, 0, 0, 6, 0, 0]
             indexed by [0, 1, 2, 3, 4, 5]
            sage: s.dft()                                                               # needs sage.rings.number_field
            Indexed sequence: [6, 0, 0, 0, 0, 0]
             indexed by [0, 1, 2, 3, 4, 5]

            sage: # needs sage.combinat sage.groups
            sage: G = SymmetricGroup(3)
            sage: J = G.conjugacy_classes_representatives()
            sage: s = IndexedSequence([1,2,3], J)  # 1,2,3 are the values of a class fcn on G
            sage: s.dft()   # the "scalar-valued Fourier transform" of this class fcn
            Indexed sequence: [8, 2, 2]
             indexed by [(), (1,2), (1,2,3)]

            sage: # needs sage.rings.number_field
            sage: J = AbelianGroup(2, [2,3], names=\'ab\')
            sage: s = IndexedSequence([1,2,3,4,5,6], J)
            sage: s.dft()   # the precision of output is somewhat random and architecture dependent.
            Indexed sequence: [21.0000000000000,
                               -2.99999999999997 - 1.73205080756885*I,
                               -2.99999999999999 + 1.73205080756888*I,
                               -9.00000000000000 + 0.0000000000000485744257349999*I,
                               -0.00000000000000976996261670137 - 0.0000000000000159872115546022*I,
                               -0.00000000000000621724893790087 - 0.0000000000000106581410364015*I]
             indexed by Multiplicative Abelian group isomorphic to C2 x C3

            sage: # needs sage.groups sage.rings.number_field
            sage: J = CyclicPermutationGroup(6)
            sage: s = IndexedSequence([1,2,3,4,5,6], J)
            sage: s.dft()   # the precision of output is somewhat random and architecture dependent.
            Indexed sequence: [21.0000000000000,
                               -2.99999999999997 - 1.73205080756885*I,
                               -2.99999999999999 + 1.73205080756888*I,
                               -9.00000000000000 + 0.0000000000000485744257349999*I,
                               -0.00000000000000976996261670137 - 0.0000000000000159872115546022*I,
                               -0.00000000000000621724893790087 - 0.0000000000000106581410364015*I]
             indexed by Cyclic group of order 6 as a permutation group

            sage: # needs sage.rings.number_field
            sage: p = 7; J = list(range(p)); A = [kronecker_symbol(j,p) for j in J]
            sage: s = IndexedSequence(A, J)
            sage: Fs = s.dft()
            sage: c = Fs.list()[1]; [x/c for x in Fs.list()]; s.list()
            [0, 1, 1, -1, 1, -1, -1]
            [0, 1, 1, -1, 1, -1, -1]

        The DFT of the values of the quadratic residue symbol is itself, up to
        a constant factor (denoted c on the last line above).

        .. TODO::

            Read the parent of the elements of S; if `\\QQ` or `\\CC` leave as
            is; if AbelianGroup, use abelian_group_dual; if some other
            implemented Group (permutation, matrix), call .characters()
            and test if the index list is the set of conjugacy classes.
        '''
    def idft(self):
        """
        A discrete inverse Fourier transform. Only works over `\\QQ`.

        EXAMPLES::

            sage: J = list(range(5))
            sage: A = [ZZ(1) for i in J]
            sage: s = IndexedSequence(A,J)
            sage: fs = s.dft(); fs                                                      # needs sage.rings.number_field
            Indexed sequence: [5, 0, 0, 0, 0]
                indexed by [0, 1, 2, 3, 4]
            sage: it = fs.idft(); it                                                    # needs sage.rings.number_field
            Indexed sequence: [1, 1, 1, 1, 1]
                indexed by [0, 1, 2, 3, 4]
            sage: it == s                                                               # needs sage.rings.number_field
            True
        """
    def dct(self):
        """
        A discrete Cosine transform.

        EXAMPLES::

            sage: J = list(range(5))
            sage: A = [exp(-2*pi*i*I/5) for i in J]                                     # needs sage.symbolic
            sage: s = IndexedSequence(A, J)                                             # needs sage.symbolic
            sage: s.dct()                                                               # needs sage.symbolic
            Indexed sequence: [0, 1/16*(sqrt(5) + I*sqrt(-2*sqrt(5) + 10) + ...
            indexed by [0, 1, 2, 3, 4]
        """
    def dst(self):
        """
        A discrete Sine transform.

        EXAMPLES::

            sage: J = list(range(5))
            sage: I = CC.0; pi = CC.pi()
            sage: A = [exp(-2*pi*i*I/5) for i in J]
            sage: s = IndexedSequence(A, J)

            sage: s.dst()        # discrete sine
            Indexed sequence: [0.000000000000000, 1.11022302462516e-16 - 2.50000000000000*I, ...]
            indexed by [0, 1, 2, 3, 4]
        """
    def convolution(self, other):
        """
        Convolves two sequences of the same length (automatically expands
        the shortest one by extending it by 0 if they have different lengths).

        If `\\{a_n\\}` and `\\{b_n\\}` are sequences indexed by `(n=0,1,...,N-1)`,
        extended by zero for all `n` in `\\ZZ`, then the convolution is

        .. MATH::

             c_j = \\sum_{i=0}^{N-1} a_i b_{j-i}.

        INPUT:

        - ``other`` -- a collection of elements of a ring with
          index set a finite abelian group (under `+`)

        OUTPUT: the Dirichlet convolution of ``self`` and ``other``

        EXAMPLES::

            sage: J = list(range(5))
            sage: A = [ZZ(1) for i in J]
            sage: B = [ZZ(1) for i in J]
            sage: s = IndexedSequence(A,J)
            sage: t = IndexedSequence(B,J)
            sage: s.convolution(t)
            [1, 2, 3, 4, 5, 4, 3, 2, 1]

        AUTHOR: David Joyner (2006-09)
        """
    def convolution_periodic(self, other):
        """
        Convolves two collections indexed by a ``range(...)`` of the same
        length (automatically expands the shortest one by extending it
        by 0 if they have different lengths).

        If `\\{a_n\\}` and `\\{b_n\\}` are sequences indexed by `(n=0,1,...,N-1)`,
        extended periodically for all `n` in `\\ZZ`, then the convolution is

        .. MATH::

             c_j = \\sum_{i=0}^{N-1} a_i b_{j-i}.

        INPUT:

        - ``other`` -- a sequence of elements of `\\CC`, `\\RR` or `\\GF{q}`

        OUTPUT: the Dirichlet convolution of ``self`` and ``other``

        EXAMPLES::

            sage: I = list(range(5))
            sage: A = [ZZ(1) for i in I]
            sage: B = [ZZ(1) for i in I]
            sage: s = IndexedSequence(A,I)
            sage: t = IndexedSequence(B,I)
            sage: s.convolution_periodic(t)
            [5, 5, 5, 5, 5, 5, 5, 5, 5]

        AUTHOR: David Joyner (2006-09)
        """
    def __mul__(self, other):
        """
        Implement scalar multiplication (on the right).

        EXAMPLES::

            sage: J = list(range(5))
            sage: A = [ZZ(1) for i in J]
            sage: s = IndexedSequence(A,J)
            sage: s.base_ring()
            Integer Ring
            sage: t = s*(1/3); t; t.base_ring()
            Indexed sequence: [1/3, 1/3, 1/3, 1/3, 1/3]
                indexed by [0, 1, 2, 3, 4]
            Rational Field
        """
    def __eq__(self, other):
        """
        Implement boolean equals.

        EXAMPLES::

            sage: J = list(range(5))
            sage: A = [ZZ(1) for i in J]
            sage: s = IndexedSequence(A,J)
            sage: t = s*(1/3)
            sage: t*3 == s
            1

        .. WARNING::

            ** elements are considered different if they differ
            by ``10^(-8)``, which is pretty arbitrary -- use with CAUTION!! **
        """
    def fft(self):
        """
        Wraps the gsl ``FastFourierTransform.forward()`` in
        :mod:`~sage.calculus.transforms.fft`.

        If the length is a power of 2 then this automatically uses the
        radix2 method. If the number of sample points in the input is
        a power of 2 then the wrapper for the GSL function
        ``gsl_fft_complex_radix2_forward()`` is automatically called.
        Otherwise, ``gsl_fft_complex_forward()`` is used.

        EXAMPLES::

            sage: J = list(range(5))
            sage: A = [RR(1) for i in J]
            sage: s = IndexedSequence(A,J)
            sage: t = s.fft(); t
            Indexed sequence: [5.00000000000000, 0.000000000000000, 0.000000000000000, 0.000000000000000, 0.000000000000000]
                indexed by [0, 1, 2, 3, 4]
        """
    def ifft(self):
        """
        Implement the gsl ``FastFourierTransform.inverse`` in
        :mod:`~sage.calculus.transforms.fft`.

        If the number of sample points in the input is a power of 2
        then the wrapper for the GSL function
        ``gsl_fft_complex_radix2_inverse()`` is automatically called.
        Otherwise, ``gsl_fft_complex_inverse()`` is used.

        EXAMPLES::

            sage: J = list(range(5))
            sage: A = [RR(1) for i in J]
            sage: s = IndexedSequence(A,J)
            sage: t = s.fft(); t
            Indexed sequence: [5.00000000000000, 0.000000000000000, 0.000000000000000, 0.000000000000000, 0.000000000000000]
                indexed by [0, 1, 2, 3, 4]
            sage: t.ifft()
            Indexed sequence: [1.00000000000000, 1.00000000000000, 1.00000000000000, 1.00000000000000, 1.00000000000000]
                indexed by [0, 1, 2, 3, 4]
            sage: t.ifft() == s
            1
        """
    def dwt(self, other: str = 'haar', wavelet_k: int = 2):
        """
        Wraps the gsl ``WaveletTransform.forward`` in :mod:`~sage.calculus.transforms.dwt`
        (written by Joshua Kantor). Assumes the length of the sample is a
        power of 2. Uses the GSL function ``gsl_wavelet_transform_forward()``.

        INPUT:

        - ``other`` -- the name of the type of wavelet; valid choices are:

          * ``'daubechies'``
          * ``'daubechies_centered'``
          * ``'haar'`` (default)
          * ``'haar_centered'``
          * ``'bspline'``
          * ``'bspline_centered'``

        - ``wavelet_k`` -- for daubechies wavelets, ``wavelet_k`` specifies a
          daubechie wavelet with `k/2` vanishing moments;
          `k = 4,6,...,20` for `k` even are the only ones implemented

          For Haar wavelets, ``wavelet_k`` must be 2.

          For bspline wavelets, ``wavelet_k`` equal to `103,105,202,204,
          206,208,301,305,307,309` will give biorthogonal B-spline wavelets
          of order `(i,j)` where ``wavelet_k`` equals `100 \\cdot i + j`.

        The wavelet transform uses `J = \\log_2(n)` levels.

        EXAMPLES::

            sage: J = list(range(8))
            sage: A = [RR(1) for i in J]
            sage: s = IndexedSequence(A,J)
            sage: t = s.dwt()
            sage: t        # slightly random output
            Indexed sequence: [2.82842712474999, 0.000000000000000, 0.000000000000000, 0.000000000000000, 0.000000000000000, 0.000000000000000, 0.000000000000000, 0.000000000000000]
                indexed by [0, 1, 2, 3, 4, 5, 6, 7]
        """
    def idwt(self, other: str = 'haar', wavelet_k: int = 2):
        '''
        Implement the gsl ``WaveletTransform.backward()`` in
        :mod:`~sage.calculus.transforms.dwt`.

        Assumes the length of the sample is a power of 2. Uses the
        GSL function ``gsl_wavelet_transform_backward()``.

        INPUT:

        - ``other`` -- must be one of the following:

          * ``\'haar\'``
          * ``\'daubechies\'``
          * ``\'daubechies_centered\'``
          * ``\'haar_centered\'``
          * ``\'bspline\'``
          * ``\'bspline_centered\'``

        - ``wavelet_k`` -- for daubechies wavelets, ``wavelet_k`` specifies a
          daubechie wavelet with `k/2` vanishing moments;
          `k = 4,6,...,20` for `k` even are the only ones implemented

          For Haar wavelets, ``wavelet_k`` must be 2.

          For bspline wavelets, ``wavelet_k`` equal to `103,105,202,204,
          206,208,301,305,307,309` will give biorthogonal B-spline wavelets
          of order `(i,j)` where ``wavelet_k`` equals `100 \\cdot i + j`.

        EXAMPLES::

            sage: J = list(range(8))
            sage: A = [RR(1) for i in J]
            sage: s = IndexedSequence(A,J)
            sage: t = s.dwt()
            sage: t            # random arch dependent output
            Indexed sequence: [2.82842712474999, 0.000000000000000, 0.000000000000000, 0.000000000000000, 0.000000000000000, 0.000000000000000, 0.000000000000000, 0.000000000000000]
                indexed by [0, 1, 2, 3, 4, 5, 6, 7]
            sage: t.idwt()                  # random arch dependent output
            Indexed sequence: [1.00000000000000, 1.00000000000000, 1.00000000000000, 1.00000000000000, 1.00000000000000, 1.00000000000000, 1.00000000000000, 1.00000000000000]
                indexed by [0, 1, 2, 3, 4, 5, 6, 7]
            sage: t.idwt() == s
            True
            sage: J = list(range(16))
            sage: A = [RR(1) for i in J]
            sage: s = IndexedSequence(A,J)
            sage: t = s.dwt("bspline", 103)
            sage: t   # random arch dependent output
            Indexed sequence: [4.00000000000000, 0.000000000000000, 0.000000000000000, 0.000000000000000, 0.000000000000000, 0.000000000000000, 0.000000000000000, 0.000000000000000, 0.000000000000000, 0.000000000000000, 0.000000000000000, 0.000000000000000, 0.000000000000000, 0.000000000000000, 0.000000000000000, 0.000000000000000]
                indexed by [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
            sage: t.idwt("bspline", 103) == s
            True
        '''
