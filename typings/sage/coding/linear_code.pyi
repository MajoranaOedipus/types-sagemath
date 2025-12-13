from sage.arith.misc import GCD as GCD, binomial as binomial
from sage.categories.cartesian_product import cartesian_product as cartesian_product
from sage.categories.fields import Fields as Fields
from sage.coding.decoder import Decoder as Decoder
from sage.coding.encoder import Encoder as Encoder
from sage.coding.linear_code_no_metric import AbstractLinearCodeNoMetric as AbstractLinearCodeNoMetric
from sage.combinat.subset import Subsets as Subsets
from sage.cpython.string import bytes_to_str as bytes_to_str
from sage.features.gap import GapPackage as GapPackage
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.functional import is_even as is_even
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.misc.randstate import current_randstate as current_randstate
from sage.modules.free_module import VectorSpace as VectorSpace
from sage.modules.free_module_element import vector as vector
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ

class AbstractLinearCode(AbstractLinearCodeNoMetric):
    '''
    Abstract base class for linear codes.

    This class contains all methods that can be used on Linear Codes and on
    Linear Codes families.  So, every Linear Code-related class should inherit
    from this abstract class.

    To implement a linear code, you need to:

    - inherit from :class:`AbstractLinearCode`

    - call :class:`AbstractLinearCode` ``__init__`` method in the subclass constructor. Example:
      ``super().__init__(base_field, length, "EncoderName", "DecoderName")``.
      By doing that, your subclass will have its ``length`` parameter
      initialized and will be properly set as a member of the category framework.
      You need of course to complete the constructor by adding any additional parameter
      needed to describe properly the code defined in the subclass.

    - Add the following two lines on the class level::

          _registered_encoders = {}
          _registered_decoders = {}


    - fill the dictionary of its encoders in ``sage.coding.__init__.py`` file. Example:
      I want to link the encoder ``MyEncoderClass`` to ``MyNewCodeClass``
      under the name ``MyEncoderName``.
      All I need to do is to write this line in the ``__init__.py`` file:
      ``MyNewCodeClass._registered_encoders["NameOfMyEncoder"] = MyEncoderClass`` and all instances of
      ``MyNewCodeClass`` will be able to use instances of ``MyEncoderClass``.

    - fill the dictionary of its decoders in ``sage.coding.__init__`` file. Example:
      I want to link the encoder ``MyDecoderClass`` to ``MyNewCodeClass``
      under the name ``MyDecoderName``.
      All I need to do is to write this line in the ``__init__.py`` file:
      ``MyNewCodeClass._registered_decoders["NameOfMyDecoder"] = MyDecoderClass`` and all instances of
      ``MyNewCodeClass`` will be able to use instances of ``MyDecoderClass``.


    As the class :class:`AbstractLinearCode` is not designed to be instantiated, it does not have any representation
    methods. You should implement ``_repr_`` and ``_latex_`` methods in the subclass.

    .. NOTE::

        :class:`AbstractLinearCode` has a generic implementation of the
        method ``__eq__`` which uses the generator matrix and is quite
        slow. In subclasses you are encouraged to override ``__eq__``
        and ``__hash__``.

    .. WARNING::

        The default encoder should always have `F^{k}` as message space, with `k` the dimension
        of the code and `F` is the base ring of the code.

        A lot of methods of the abstract class rely on the knowledge of a generator matrix.
        It is thus strongly recommended to set an encoder with a generator matrix implemented
        as a default encoder.
    '''
    def __init__(self, base_field, length, default_encoder_name, default_decoder_name) -> None:
        '''
        Initialize mandatory parameters that any linear code shares.

        This method only exists for inheritance purposes as it initializes
        parameters that need to be known by every linear code. The class
        :class:`sage.coding.linear_code.AbstractLinearCode` should never be
        directly instantiated.

        INPUT:

        - ``base_field`` -- the base field of ``self``

        - ``length`` -- the length of ``self`` (a Python int or a Sage Integer, must be > 0)

        - ``default_encoder_name`` -- the name of the default encoder of ``self``

        - ``default_decoder_name`` -- the name of the default decoder of ``self``

        EXAMPLES:

        The following example demonstrates how to subclass `AbstractLinearCode`
        for representing a new family of codes. The example family is non-sensical::

            sage: class MyCodeFamily(sage.coding.linear_code.AbstractLinearCode):
            ....:   def __init__(self, field, length, dimension, generator_matrix):
            ....:       super().__init__(field, length,
            ....:                        "GeneratorMatrix", "Syndrome")
            ....:       self._dimension = dimension
            ....:       self._generator_matrix = generator_matrix
            ....:   def generator_matrix(self):
            ....:       return self._generator_matrix
            ....:   def _repr_(self):
            ....:       return "[%d, %d] dummy code over GF(%s)" % (self.length(), self.dimension(), self.base_field().cardinality())

        We now instantiate a member of our newly made code family::

            sage: generator_matrix = matrix(GF(17), 5, 10,
            ....:                           {(i,i):1 for i in range(5)})
            sage: C = MyCodeFamily(GF(17), 10, 5, generator_matrix)

        We can check its existence and parameters::

            sage: C
            [10, 5] dummy code over GF(17)

        We can check that it is truly a part of the framework category::

            sage: C.parent()
            <class \'__main__.MyCodeFamily_with_category\'>
            sage: C.category()
            Category of facade finite dimensional vector spaces with basis over Finite Field of size 17

        And any method that works on linear codes works for our new dummy code::

            sage: C.minimum_distance()                                                  # needs sage.libs.gap
            1
            sage: C.is_self_orthogonal()
            False
            sage: print(C.divisor())  #long time
            1
        '''
    def automorphism_group_gens(self, equivalence: str = 'semilinear'):
        """
        Return generators of the automorphism group of ``self``.

        INPUT:

        - ``equivalence`` -- (optional) defines the acting group, either

          * ``'permutational'``

          * ``'linear'``

          * ``'semilinear'``

        OUTPUT:

        - generators of the automorphism group of ``self``
        - the order of the automorphism group of ``self``

        EXAMPLES:

        Note, this result can depend on the PRNG state in libgap in a way that
        depends on which packages are loaded, so we must re-seed GAP to ensure
        a consistent result for this example::

            sage: # needs sage.libs.gap
            sage: libgap.set_seed(0)
            0
            sage: C = codes.HammingCode(GF(4, 'z'), 3)
            sage: C.automorphism_group_gens()
            ([((1, 1, 1, z, z + 1, 1, 1, 1, 1, z + 1, z, z, z + 1, z + 1,
                z + 1, 1, z + 1, z, z, 1, z);
               (1,13,14,20)(2,21,8,18,7,16,19,15)(3,10,5,12,17,9,6,4),
               Ring endomorphism of Finite Field in z of size 2^2
                 Defn: z |--> z + 1),
              ((z, 1, z, z, z, z + 1, z, z, z, z, z, z, z + 1, z, z, z,
                z, z + 1, z, z, z);
               (1,11,5,12,3,19)(2,8)(6,18,13)(7,17,15)(9,10,14,16,20,21),
               Ring endomorphism of Finite Field in z of size 2^2
                 Defn: z |--> z + 1),
              ((z, z, z, z, z, z, z, z, z, z, z, z, z, z, z, z, z, z, z, z, z);
               (),
               Ring endomorphism of Finite Field in z of size 2^2
                 Defn: z |--> z)],
             362880)
            sage: C.automorphism_group_gens(equivalence='linear')
            ([((z, 1, z + 1, z + 1, 1, z + 1, z, 1, z + 1, z + 1, 1, z, 1, z + 1,
                z, 1, z, 1, z + 1, 1, 1);
               (1,12,11,10,6,8,9,20,13,21,5,14,3,16,17,19,7,4,2,15,18),
               Ring endomorphism of Finite Field in z of size 2^2
                 Defn: z |--> z),
              ((z + 1, z + 1, z + 1, z, 1, 1, z, z, 1, z + 1, z, 1, 1, z, 1, z + 1,
                z, z + 1, z + 1, 1, z);
               (1,3,18,2,17,6,19)(4,15,13,20,7,14,16)(5,11,8,21,12,9,10),
               Ring endomorphism of Finite Field in z of size 2^2
                 Defn: z |--> z),
              ((z + 1, z + 1, z + 1, z + 1, z + 1, z + 1, z + 1, z + 1, z + 1, z + 1,
                z + 1, z + 1, z + 1, z + 1, z + 1, z + 1, z + 1, z + 1, z + 1, z + 1, z + 1);
               (),
               Ring endomorphism of Finite Field in z of size 2^2
                 Defn: z |--> z)],
             181440)
            sage: C.automorphism_group_gens(equivalence='permutational')
            ([((1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);
               (1,11)(3,10)(4,9)(5,7)(12,21)(14,20)(15,19)(16,17),
               Ring endomorphism of Finite Field in z of size 2^2
                 Defn: z |--> z),
              ((1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);
               (2,18)(3,19)(4,10)(5,16)(8,13)(9,14)(11,21)(15,20),
               Ring endomorphism of Finite Field in z of size 2^2
                 Defn: z |--> z),
              ((1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);
               (1,19)(3,17)(4,21)(5,20)(7,14)(9,12)(10,16)(11,15),
               Ring endomorphism of Finite Field in z of size 2^2
                 Defn: z |--> z),
              ((1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);
               (2,13)(3,14)(4,20)(5,11)(8,18)(9,19)(10,15)(16,21),
               Ring endomorphism of Finite Field in z of size 2^2
                 Defn: z |--> z)],
            64)
        """
    def assmus_mattson_designs(self, t, mode=None):
        '''
        Assmus and Mattson Theorem (section 8.4, page 303 of [HP2003]_): Let
        `A_0, A_1, ..., A_n` be the weights of the codewords in a binary
        linear `[n , k, d]` code `C`, and let `A_0^*, A_1^*, ..., A_n^*` be
        the weights of the codewords in its dual `[n, n-k, d^*]` code `C^*`.
        Fix a `t`, `0<t<d`, and let

        .. MATH::

           s = |\\{ i\\ |\\ A_i^* \\not= 0, 0< i \\leq n-t\\}|.

        Assume `s\\leq d-t`.

        1. If `A_i\\not= 0` and `d\\leq i\\leq n`
           then `C_i = \\{ c \\in C\\ |\\ wt(c) = i\\}` holds a simple t-design.

        2. If `A_i^*\\not= 0` and `d*\\leq i\\leq n-t` then
           `C_i^* = \\{ c \\in C^*\\ |\\ wt(c) = i\\}` holds a simple t-design.

        A block design is a pair `(X,B)`, where `X` is a non-empty finite set
        of `v>0` elements called points, and `B` is a non-empty finite
        multiset of size b whose elements are called blocks, such that each
        block is a non-empty finite multiset of `k` points. `A` design without
        repeated blocks is called a simple block design. If every subset of
        points of size `t` is contained in exactly `\\lambda` blocks the block
        design is called a `t-(v,k,\\lambda)` design (or simply a `t`-design
        when the parameters are not specified). When `\\lambda=1` then the
        block design is called a `S(t,k,v)` Steiner system.

        In the Assmus and Mattson Theorem (1), `X` is the set `\\{1,2,...,n\\}`
        of coordinate locations and `B = \\{supp(c)\\ |\\ c \\in C_i\\}` is the set
        of supports of the codewords of `C` of weight `i`. Therefore, the
        parameters of the `t`-design for `C_i` are

        ::

            t =       given
            v =       n
            k =       i   (k not to be confused with dim(C))
            b =       Ai
            lambda = b*binomial(k,t)/binomial(v,t) (by Theorem 8.1.6,
                                                       p 294, in [HP2003]_)

        Setting the ``mode="verbose"`` option prints out the values of the
        parameters.

        The first example below means that the binary [24,12,8]-code C has
        the property that the (support of the) codewords of weight 8 (resp.,
        12, 16) form a 5-design. Similarly for its dual code `C^*` (of course
        `C=C^*` in this case, so this info is extraneous). The test fails to
        produce 6-designs (ie, the hypotheses of the theorem fail to hold,
        not that the 6-designs definitely don\'t exist). The command
        ``assmus_mattson_designs(C,5,mode=\'verbose\')`` returns the same value
        but prints out more detailed information.

        The second example below illustrates the blocks of the 5-(24, 8, 1)
        design (i.e., the S(5,8,24) Steiner system).

        EXAMPLES::

            sage: C = codes.GolayCode(GF(2))             #  example 1
            sage: C.assmus_mattson_designs(5)
            [\'weights from C: \', [8, 12, 16, 24],
             \'designs from C: \',  [[5, (24, 8, 1)], [5, (24, 12, 48)],
                                   [5, (24, 16, 78)], [5, (24, 24, 1)]],
             \'weights from C*: \', [8, 12, 16],
             \'designs from C*: \', [[5, (24, 8, 1)], [5, (24, 12, 48)], [5, (24, 16, 78)]]]
            sage: C.assmus_mattson_designs(6)
            0
            sage: X = range(24)                          #  example 2
            sage: blocks = [c.support()  # long time
            ....:           for c in C if c.hamming_weight()==8]; len(blocks)
            759
        '''
    def binomial_moment(self, i):
        """
        Return the `i`-th binomial moment of the `[n,k,d]_q`-code `C`:

        .. MATH::

            B_i(C) = \\sum_{S, |S|=i} \\frac{q^{k_S}-1}{q-1}

        where `k_S` is the dimension of the shortened code `C_{J-S}`,
        `J=[1,2,...,n]`. (The normalized binomial moment is
        `b_i(C) = \\binom{n}{d+i})^{-1}B_{d+i}(C)`.) In other words, `C_{J-S}`
        is isomorphic to the subcode of C of codewords supported on S.

        EXAMPLES::

            sage: C = codes.HammingCode(GF(2), 3)
            sage: C.binomial_moment(2)                                                  # needs sage.libs.gap
            0
            sage: C.binomial_moment(4)          # long time                             # needs sage.libs.gap
            35

        .. warning::

            This is slow.

        REFERENCE:

        - [Du2004]_
        """
    def canonical_representative(self, equivalence: str = 'semilinear'):
        '''
        Compute a canonical orbit representative under the action of the
        semimonomial transformation group.

        See :mod:`sage.coding.codecan.autgroup_can_label`
        for more details, for example if you would like to compute
        a canonical form under some more restrictive notion of equivalence,
        i.e. if you would like to restrict the permutation group
        to a Young subgroup.

        INPUT:

        - ``equivalence`` -- (optional) defines the acting group, either

          * ``\'permutational\'``

          * ``\'linear\'``

          * ``\'semilinear\'``

        OUTPUT:

        - a canonical representative of ``self``
        - a semimonomial transformation mapping ``self`` onto its representative

        EXAMPLES::

            sage: F.<z> = GF(4)
            sage: C = codes.HammingCode(F, 3)
            sage: CanRep, transp = C.canonical_representative()                         # needs sage.libs.gap

        Check that the transporter element is correct::

            sage: LinearCode(transp*C.generator_matrix()) == CanRep                     # needs sage.libs.gap
            True

        Check if an equivalent code has the same canonical representative::

            sage: f = F.hom([z**2])
            sage: C_iso = LinearCode(C.generator_matrix().apply_map(f))
            sage: CanRep_iso, _ = C_iso.canonical_representative()                      # needs sage.libs.gap
            sage: CanRep_iso == CanRep                                                  # needs sage.libs.gap
            True

        Since applying the Frobenius automorphism could be extended to an
        automorphism of `C`, the following must also yield ``True``::

            sage: CanRep1, _ = C.canonical_representative("linear")                     # needs sage.libs.gap
            sage: CanRep2, _ = C_iso.canonical_representative("linear")                 # needs sage.libs.gap
            sage: CanRep2 == CanRep1                                                    # needs sage.libs.gap
            True

        TESTS:

        Check that interrupting this does not segfault
        (see :issue:`21651`)::

            sage: C = LinearCode(random_matrix(GF(47), 25, 35))
            sage: from sage.doctest.util import ensure_interruptible_after
            sage: with ensure_interruptible_after(0.5): C.canonical_representative()    # needs sage.libs.gap
        '''
    def characteristic(self):
        """
        Return the characteristic of the base ring of ``self``.

        EXAMPLES::

            sage: C = codes.HammingCode(GF(2), 3)
            sage: C.characteristic()
            2
        """
    def characteristic_polynomial(self):
        """
        Return the characteristic polynomial of a linear code, as defined in
        [Lin1999]_.

        EXAMPLES::

            sage: C = codes.GolayCode(GF(2))
            sage: C.characteristic_polynomial()
            -4/3*x^3 + 64*x^2 - 2816/3*x + 4096
        """
    def chinen_polynomial(self):
        '''
        Return the Chinen zeta polynomial of the code.

        EXAMPLES::

            sage: C = codes.HammingCode(GF(2), 3)
            sage: C.chinen_polynomial()       # long time
            1/5*(2*sqrt(2)*t^3 + 2*sqrt(2)*t^2 + 2*t^2 + sqrt(2)*t + 2*t + 1)/(sqrt(2) + 1)
            sage: C = codes.GolayCode(GF(3), False)
            sage: C.chinen_polynomial()       # long time
            1/7*(3*sqrt(3)*t^3 + 3*sqrt(3)*t^2 + 3*t^2 + sqrt(3)*t + 3*t + 1)/(sqrt(3) + 1)

        This last output agrees with the corresponding example given in
        Chinen\'s paper below.

        REFERENCES:

        - Chinen, K. "An abundance of invariant polynomials satisfying the
          Riemann hypothesis", April 2007 preprint.
        '''
    @cached_method
    def covering_radius(self):
        """
        Return the minimal integer `r` such that any element in the ambient space of ``self`` has distance at most `r` to a codeword of ``self``.

        This method requires the optional GAP package Guava.

        If the covering radius of a code equals its minimum distance, then the code is called perfect.

        .. NOTE::

            This method is currently not implemented on codes over base fields
            of cardinality greater than 256 due to limitations in the underlying
            algorithm of GAP.

        EXAMPLES::

            sage: C = codes.HammingCode(GF(2), 5)
            sage: C.covering_radius()                           # optional - gap_package_guava
            ...1

            sage: C = codes.random_linear_code(GF(263), 5, 1)
            sage: C.covering_radius()                           # optional - gap_package_guava
            Traceback (most recent call last):
            ...
            NotImplementedError: the GAP algorithm that Sage is using
            is limited to computing with fields of size at most 256
        """
    def divisor(self):
        """
        Return the greatest common divisor of the weights of the nonzero codewords.

        EXAMPLES::

            sage: C = codes.GolayCode(GF(2))
            sage: C.divisor()   # Type II self-dual
            4
            sage: C = codes.QuadraticResidueCodeEvenPair(17, GF(2))[0]
            sage: C.divisor()
            2
        """
    def is_projective(self):
        """
        Test  whether the code is projective.

        A linear code `C` over a field is called *projective* when its dual `Cd`
        has minimum weight `\\geq 3`, i.e. when no two coordinate positions of
        `C` are linearly independent (cf. definition 3 from [BS2011]_ or 9.8.1 from
        [BH2012]_).

        EXAMPLES::

            sage: C = codes.GolayCode(GF(2), False)
            sage: C.is_projective()
            True
            sage: C.dual_code().minimum_distance()                                      # needs sage.libs.gap
            8

        A non-projective code::

            sage: C = codes.LinearCode(matrix(GF(2), [[1,0,1],[1,1,1]]))
            sage: C.is_projective()
            False
        """
    def direct_sum(self, other):
        """
        Return the direct sum of the codes ``self`` and ``other``.

        This returns the code given by the direct sum of the codes ``self`` and
        ``other``, which must be linear codes defined over the same base ring.

        EXAMPLES::

            sage: C1 = codes.HammingCode(GF(2), 3)
            sage: C2 = C1.direct_sum(C1); C2
            [14, 8] linear code over GF(2)
            sage: C3 = C1.direct_sum(C2); C3
            [21, 12] linear code over GF(2)
        """
    def juxtapose(self, other):
        """
        Juxtaposition of ``self`` and ``other``.

        The two codes must have equal dimension.

        EXAMPLES::

           sage: C1 = codes.HammingCode(GF(2), 3)
           sage: C2 = C1.juxtapose(C1)
           sage: C2
           [14, 4] linear code over GF(2)
        """
    def u_u_plus_v_code(self, other):
        """
        Return the `(u|u+v)`-construction with ``self=u`` and ``other=v``.

        This returns the code obtained through `(u|u+v)`-construction with ``self`` as `u`
        and ``other`` as `v`. Note that `u` and `v` must have equal lengths.
        For `u` a `[n, k_1, d_1]`-code and `v` a `[n, k_2, d_2]`-code this returns
        a `[2n, k_1+k_2, d]`-code, where `d=\\min(2d_1,d_2)`.

        EXAMPLES::

            sage: C1 = codes.HammingCode(GF(2), 3)
            sage: C2 = codes.HammingCode(GF(2), 3)
            sage: D = C1.u_u_plus_v_code(C2)
            sage: D
            [14, 8] linear code over GF(2)
        """
    def product_code(self, other):
        """
        Combines ``self`` with ``other`` to give the tensor product code.

        If ``self`` is a `[n_1, k_1, d_1]`-code and ``other`` is
        a `[n_2, k_2, d_2]`-code, the product is a `[n_1n_2, k_1k_2, d_1d_2]`-code.

        Note that the two codes have to be over the same field.

        EXAMPLES::

            sage: C = codes.HammingCode(GF(2), 3)
            sage: C
            [7, 4] Hamming Code over GF(2)
            sage: D = codes.ReedMullerCode(GF(2), 2, 2)
            sage: D
            Binary Reed-Muller Code of order 2 and number of variables 2
            sage: A = C.product_code(D)
            sage: A
            [28, 16] linear code over GF(2)
            sage: A.length() == C.length()*D.length()
            True
            sage: A.dimension() == C.dimension()*D.dimension()
            True
            sage: A.minimum_distance() == C.minimum_distance()*D.minimum_distance()     # needs sage.libs.gap
            True
        """
    def construction_x(self, other, aux):
        """
        Construction X applied to ``self=C_1``, ``other=C_2`` and ``aux=C_a``.

        ``other`` must be a subcode of ``self``.

        If `C_1` is a `[n, k_1, d_1]` linear code and `C_2` is
        a `[n, k_2, d_2]` linear code, then `k_1 > k_2` and `d_1 < d_2`. `C_a` must
        be a `[n_a, k_a, d_a]` linear code, such that `k_a + k_2 = k_1`
        and `d_a + d_1 \\leq d_2`.

        The method will then return a `[n+n_a, k_1, d_a+d_1]` linear code.

        EXAMPLES::

            sage: C = codes.BCHCode(GF(2),15,7)
            sage: C
            [15, 5] BCH Code over GF(2) with designed distance 7
            sage: D = codes.BCHCode(GF(2),15,5)
            sage: D
            [15, 7] BCH Code over GF(2) with designed distance 5
            sage: C.is_subcode(D)
            True

            sage: # needs sage.libs.gap
            sage: C.minimum_distance()
            7
            sage: D.minimum_distance()
            5
            sage: aux = codes.HammingCode(GF(2),2)
            sage: aux = aux.dual_code()
            sage: aux.minimum_distance()
            2
            sage: Cx = D.construction_x(C,aux)
            sage: Cx
            [18, 7] linear code over GF(2)
            sage: Cx.minimum_distance()
            7
        """
    def extended_code(self):
        """
        Return ``self`` as an extended code.

        See documentation of :class:`sage.coding.extended_code.ExtendedCode`
        for details.

        EXAMPLES::

            sage: C = codes.HammingCode(GF(4,'a'), 3)
            sage: C
            [21, 18] Hamming Code over GF(4)
            sage: Cx = C.extended_code()
            sage: Cx
            Extension of [21, 18] Hamming Code over GF(4)
        """
    def galois_closure(self, F0):
        """
        If ``self`` is a linear code defined over `F` and `F_0` is a subfield
        with Galois group `G = Gal(F/F_0)` then this returns the `G`-module
        `C^-` containing `C`.

        EXAMPLES::

            sage: C = codes.HammingCode(GF(4,'a'), 3)
            sage: Cc = C.galois_closure(GF(2))
            sage: C; Cc
            [21, 18] Hamming Code over GF(4)
            [21, 20] linear code over GF(4)
            sage: c = C.basis()[2]
            sage: V = VectorSpace(GF(4,'a'),21)
            sage: c2 = V([x^2 for x in c.list()])
            sage: c2 in C
            False
            sage: c2 in Cc
            True
        """
    def genus(self):
        '''
        Return the "Duursma genus" of the code, `\\gamma_C = n+1-k-d`.

        EXAMPLES::

            sage: C1 = codes.HammingCode(GF(2), 3); C1
            [7, 4] Hamming Code over GF(2)
            sage: C1.genus()
            1
            sage: C2 = codes.HammingCode(GF(4,"a"), 2); C2
            [5, 3] Hamming Code over GF(4)
            sage: C2.genus()
            0

        Since all Hamming codes have minimum distance 3, these computations
        agree with the definition, `n+1-k-d`.
        '''
    def is_permutation_equivalent(self, other, algorithm=None):
        '''
        Return ``True`` if ``self`` and ``other`` are permutation equivalent
        codes and ``False`` otherwise.

        The ``algorithm="verbose"`` option also returns a permutation (if
        ``True``) sending ``self`` to ``other``.

        Uses Robert Miller\'s double coset partition refinement work.

        EXAMPLES::

            sage: P.<x> = PolynomialRing(GF(2),"x")
            sage: g = x^3 + x + 1
            sage: C1 = codes.CyclicCode(length=7, generator_pol=g); C1
            [7, 4] Cyclic Code over GF(2)
            sage: C2 = codes.HammingCode(GF(2), 3); C2
            [7, 4] Hamming Code over GF(2)
            sage: C1.is_permutation_equivalent(C2)
            True
            sage: C1.is_permutation_equivalent(C2, algorithm=\'verbose\')                 # needs sage.groups
            (True, (3,4)(5,7,6))
            sage: C1 = codes.random_linear_code(GF(2), 10, 5)
            sage: C2 = codes.random_linear_code(GF(3), 10, 5)
            sage: C1.is_permutation_equivalent(C2)
            False
        '''
    def is_galois_closed(self):
        '''
        Check if ``self`` is equal to its Galois closure.

        EXAMPLES::

            sage: C = codes.HammingCode(GF(4,"a"), 3)
            sage: C.is_galois_closed()
            False
        '''
    @cached_method
    def minimum_distance(self, algorithm=None):
        '''
        Return the minimum distance of ``self``.

        .. NOTE::

            When using GAP, this raises a :exc:`NotImplementedError` if
            the base field of the code has size greater than 256 due
            to limitations in GAP.

        INPUT:

        - ``algorithm`` -- (default: ``None``) the name of the algorithm to use
          to perform minimum distance computation. ``algorithm`` can be:

          - ``None``, to use GAP methods (but not Guava)

          - ``\'guava\'``, to use the optional GAP package Guava

        OUTPUT: integer; minimum distance of this code

        EXAMPLES::

            sage: MS = MatrixSpace(GF(3),4,7)
            sage: G = MS([[1,1,1,0,0,0,0], [1,0,0,1,1,0,0], [0,1,0,1,0,1,0], [1,1,0,1,0,0,1]])
            sage: C = LinearCode(G)
            sage: C.minimum_distance()                                                  # needs sage.libs.gap
            3

        If ``algorithm`` is provided, then the minimum distance will be
        recomputed even if there is a stored value from a previous run.::

            sage: C.minimum_distance(algorithm=\'gap\')                                   # needs sage.libs.gap
            3
            sage: libgap.SetAllInfoLevels(0)         # to suppress extra info messages  # needs sage.libs.gap
            sage: C.minimum_distance(algorithm=\'guava\')         # optional - gap_package_guava
            ...3

        TESTS::

            sage: C = codes.random_linear_code(GF(4,"a"), 5, 2)
            sage: C.minimum_distance(algorithm=\'something\')
            Traceback (most recent call last):
            ...
            ValueError: The algorithm argument must be one of None, \'gap\' or \'guava\'; got \'something\'

        The field must be size at most 256::

            sage: C = codes.random_linear_code(GF(257,"a"), 5, 2)
            sage: C.minimum_distance()
            Traceback (most recent call last):
            ...
            NotImplementedError: the GAP algorithm that Sage is using
             is limited to computing with fields of size at most 256
        '''
    def module_composition_factors(self, gp):
        """
        Print the GAP record of the Meataxe composition factors module.

        This is displayed in Meataxe notation.

        This uses GAP but not Guava.

        EXAMPLES::

            sage: MS = MatrixSpace(GF(2),4,8)
            sage: G  = MS([[1,0,0,0,1,1,1,0], [0,1,1,1,0,0,0,0],
            ....:          [0,0,0,0,0,0,0,1], [0,0,0,0,0,1,0,0]])
            sage: C  = LinearCode(G)
            sage: gp = C.permutation_automorphism_group()                               # needs sage.libs.gap
            sage: C.module_composition_factors(gp)                                      # needs sage.libs.gap
            [ rec(
                  IsIrreducible := true,
                  IsOverFiniteField := true,
            ...) ]
        """
    def permutation_automorphism_group(self, algorithm: str = 'partition'):
        '''
        If `C` is an `[n,k,d]` code over `F`, this function computes the
        subgroup `Aut(C) \\subset S_n` of all permutation automorphisms of `C`.
        The binary case always uses the (default) partition refinement
        algorithm of Robert Miller.

        Note that if the base ring of `C` is `GF(2)` then this is the full
        automorphism group. Otherwise, you could use
        :meth:`~sage.coding.linear_code.LinearCode.automorphism_group_gens`
        to compute generators of the full automorphism group.

        INPUT:

        - ``algorithm`` -- if ``\'gap\'`` then GAP\'s MatrixAutomorphism function
          (written by Thomas Breuer) is used. The implementation combines an
          idea of mine with an improvement suggested by Cary Huffman. If
          ``\'gap+verbose\'`` then code-theoretic data is printed out at
          several stages of the computation. If ``\'partition\'`` then the
          (default) partition refinement algorithm of Robert Miller is used.
          Finally, if ``\'codecan\'`` then the partition refinement algorithm
          of Thomas Feulner is used, which also computes a canonical
          representative of ``self`` (call
          :meth:`~sage.coding.linear_code.LinearCode.canonical_representative`
          to access it).

        OUTPUT: permutation automorphism group

        EXAMPLES::

            sage: MS = MatrixSpace(GF(2),4,8)
            sage: G  = MS([[1,0,0,0,1,1,1,0], [0,1,1,1,0,0,0,0],
            ....:          [0,0,0,0,0,0,0,1], [0,0,0,0,0,1,0,0]])
            sage: C  = LinearCode(G); C
            [8, 4] linear code over GF(2)

            sage: # needs sage.groups
            sage: G = C.permutation_automorphism_group()
            sage: G.order()
            144
            sage: GG = C.permutation_automorphism_group("codecan")
            sage: GG == G
            True

        A less easy example involves showing that the permutation
        automorphism group of the extended ternary Golay code is the
        Mathieu group `M_{11}`.

        ::

            sage: # needs sage.groups
            sage: C = codes.GolayCode(GF(3))
            sage: M11 = MathieuGroup(11)
            sage: M11.order()
            7920
            sage: G = C.permutation_automorphism_group()                # long time (6s on sage.math, 2011)
            sage: G.is_isomorphic(M11)                                  # long time
            True
            sage: GG = C.permutation_automorphism_group("codecan")      # long time
            sage: GG == G                                               # long time
            True

        Other examples::

            sage: # needs sage.groups
            sage: C = codes.GolayCode(GF(2))
            sage: G = C.permutation_automorphism_group()
            sage: G.order()
            244823040
            sage: C = codes.HammingCode(GF(2), 5)
            sage: G = C.permutation_automorphism_group()
            sage: G.order()
            9999360
            sage: C = codes.HammingCode(GF(3), 2); C
            [4, 2] Hamming Code over GF(3)
            sage: C.permutation_automorphism_group(algorithm=\'partition\')
            Permutation Group with generators [(1,3,4)]
            sage: C = codes.HammingCode(GF(4,"z"), 2); C
            [5, 3] Hamming Code over GF(4)
            sage: G = C.permutation_automorphism_group(algorithm=\'partition\'); G
            Permutation Group with generators [(1,3)(4,5), (1,4)(3,5)]
            sage: GG = C.permutation_automorphism_group(algorithm=\'codecan\')    # long time
            sage: GG == G                                                       # long time
            True
            sage: C.permutation_automorphism_group(algorithm=\'gap\')     # optional - gap_package_guava
            Permutation Group with generators [(1,3)(4,5), (1,4)(3,5)]
            sage: C = codes.GolayCode(GF(3), True)
            sage: C.permutation_automorphism_group(algorithm=\'gap\')     # optional - gap_package_guava
            Permutation Group with generators
             [(5,7)(6,11)(8,9)(10,12), (4,6,11)(5,8,12)(7,10,9), (3,4)(6,8)(9,11)(10,12),
              (2,3)(6,11)(8,12)(9,10), (1,2)(5,10)(7,12)(8,9)]

        However, the option ``algorithm="gap+verbose"``, will print out::

            Minimum distance: 5 Weight distribution: [1, 0, 0, 0, 0, 132, 132,
            0, 330, 110, 0, 24]

            Using the 132 codewords of weight 5 Supergroup size: 39916800

        in addition to the output of
        ``C.permutation_automorphism_group(algorithm=\'gap\')``.
        '''
    def punctured(self, L):
        """
        Return a :class:`sage.coding.punctured_code` object from ``L``.

        INPUT:

        - ``L`` -- list of positions to puncture

        OUTPUT: an instance of :class:`sage.coding.punctured_code`

        EXAMPLES::

            sage: C = codes.HammingCode(GF(2), 3)
            sage: C.punctured([1,2])
            Puncturing of [7, 4] Hamming Code over GF(2) on position(s) [1, 2]
        """
    def relative_distance(self):
        """
        Return the ratio of the minimum distance to the code length.

        EXAMPLES::

            sage: C = codes.HammingCode(GF(2),3)
            sage: C.relative_distance()
            3/7
        """
    def shortened(self, L):
        """
        Return the code shortened at the positions ``L``, where
        `L \\subset \\{1,2,...,n\\}`.

        Consider the subcode `C(L)` consisting of all codewords `c\\in C` which
        satisfy `c_i=0` for all `i\\in L`. The punctured code `C(L)^L` is
        called the shortened code on `L` and is denoted `C_L`. The code
        constructed is actually only isomorphic to the shortened code defined
        in this way.

        By Theorem 1.5.7 in [HP2003]_, `C_L` is `((C^\\perp)^L)^\\perp`. This is used
        in the construction below.

        INPUT:

        - ``L`` -- subset of `\\{1,...,n\\}`, where `n` is the length of this code

        OUTPUT: linear code, the shortened code described above

        EXAMPLES::

            sage: C = codes.HammingCode(GF(2), 3)
            sage: C.shortened([1,2])
            [5, 2] linear code over GF(2)
        """
    @cached_method
    def weight_distribution(self, algorithm=None):
        '''
        Return the weight distribution, or spectrum, of ``self`` as a list.

        The weight distribution a code of length `n` is the sequence `A_0,
        A_1,..., A_n` where `A_i` is the number of codewords of weight `i`.

        INPUT:

        - ``algorithm`` -- (default: ``None``) if set to ``\'gap\'``,
          call GAP. If set to ``\'leon\'``, call the option GAP package GUAVA and
          call a function therein by Jeffrey Leon (see warning below). If set to
          ``\'binary\'``, use an algorithm optimized for binary codes. The default
          is to use ``\'binary\'`` for binary codes and ``\'gap\'`` otherwise.

        OUTPUT: list of nonnegative integers; the weight distribution

        .. WARNING::

            Specifying ``algorithm="leon"`` sometimes prints a traceback
            related to a stack smashing error in the C library. The result
            appears to be computed correctly, however. It appears to run much
            faster than the GAP algorithm in small examples and much slower than
            the GAP algorithm in larger examples.

        EXAMPLES::

            sage: MS = MatrixSpace(GF(2),4,7)
            sage: G = MS([[1,1,1,0,0,0,0],[1,0,0,1,1,0,0],[0,1,0,1,0,1,0],[1,1,0,1,0,0,1]])
            sage: C = LinearCode(G)
            sage: C.weight_distribution()
            [1, 0, 0, 7, 7, 0, 0, 1]
            sage: F.<z> = GF(2^2,"z")
            sage: C = codes.HammingCode(F, 2); C
            [5, 3] Hamming Code over GF(4)
            sage: C.weight_distribution()                                               # needs sage.libs.gap
            [1, 0, 0, 30, 15, 18]
            sage: C = codes.HammingCode(GF(2), 3); C
            [7, 4] Hamming Code over GF(2)
            sage: C.weight_distribution(algorithm=\'leon\')   # optional - gap_package_guava
            [1, 0, 0, 7, 7, 0, 0, 1]
            sage: C.weight_distribution(algorithm=\'gap\')                                # needs sage.libs.gap
            [1, 0, 0, 7, 7, 0, 0, 1]
            sage: C.weight_distribution(algorithm=\'binary\')
            [1, 0, 0, 7, 7, 0, 0, 1]

            sage: # optional - gap_package_guava
            sage: C = codes.HammingCode(GF(3), 3); C
            [13, 10] Hamming Code over GF(3)
            sage: C.weight_distribution() == C.weight_distribution(algorithm=\'leon\')
            True
            sage: C = codes.HammingCode(GF(5), 2); C
            [6, 4] Hamming Code over GF(5)
            sage: C.weight_distribution() == C.weight_distribution(algorithm=\'leon\')
            True
            sage: C = codes.HammingCode(GF(7), 2); C
            [8, 6] Hamming Code over GF(7)
            sage: C.weight_distribution() == C.weight_distribution(algorithm=\'leon\')
            True
        '''
    spectrum = weight_distribution
    def support(self):
        """
        Return the set of indices `j` where `A_j` is nonzero, where
        `A_j` is the number of codewords in ``self`` of Hamming weight `j`.

        OUTPUT: list of integers

        EXAMPLES::

            sage: C = codes.HammingCode(GF(2), 3)
            sage: C.weight_distribution()
            [1, 0, 0, 7, 7, 0, 0, 1]
            sage: C.support()
            [0, 3, 4, 7]
        """
    def weight_enumerator(self, names=None, bivariate: bool = True):
        '''
        Return the weight enumerator polynomial of ``self``.

        This is the bivariate, homogeneous polynomial in `x` and `y` whose
        coefficient to `x^i y^{n-i}` is the number of codewords of ``self`` of
        Hamming weight `i`. Here, `n` is the length of ``self``.

        INPUT:

        - ``names`` -- (default: ``\'xy\'``) the names of the variables in the
          homogeneous polynomial. Can be given as a single string of length 2,
          or a single string with a comma, or as a tuple or list of two strings.

        - ``bivariate`` -- boolean (default: ``True``); whether to return a
          bivariate, homogeneous polynomial or just a univariate polynomial. If
          set to ``False``, then ``names`` will be interpreted as a single
          variable name and default to ``\'x\'``.

        OUTPUT: the weight enumerator polynomial over `\\ZZ`

        EXAMPLES::

            sage: C = codes.HammingCode(GF(2), 3)
            sage: C.weight_enumerator()
            x^7 + 7*x^4*y^3 + 7*x^3*y^4 + y^7
            sage: C.weight_enumerator(names=\'st\')
            s^7 + 7*s^4*t^3 + 7*s^3*t^4 + t^7
            sage: C.weight_enumerator(names="var1, var2")
            var1^7 + 7*var1^4*var2^3 + 7*var1^3*var2^4 + var2^7
            sage: C.weight_enumerator(names=(\'var1\', \'var2\'))
            var1^7 + 7*var1^4*var2^3 + 7*var1^3*var2^4 + var2^7
            sage: C.weight_enumerator(bivariate=False)
            x^7 + 7*x^4 + 7*x^3 + 1

        An example of a code with a non-symmetrical weight enumerator::

            sage: C = codes.GolayCode(GF(3), extended=False)
            sage: C.weight_enumerator()
            24*x^11 + 110*x^9*y^2 + 330*x^8*y^3 + 132*x^6*y^5 + 132*x^5*y^6 + y^11
        '''
    def zeta_polynomial(self, name: str = 'T'):
        '''
        Return the Duursma zeta polynomial of this code.

        Assumes that the minimum distances of this code and its dual are
        greater than 1.  Prints a warning to ``stdout`` otherwise.

        INPUT:

        - ``name`` -- string (default: ``\'T\'``); variable name

        OUTPUT: polynomial over `\\QQ`

        EXAMPLES::

            sage: C = codes.HammingCode(GF(2), 3)
            sage: C.zeta_polynomial()                                                   # needs sage.libs.gap
            2/5*T^2 + 2/5*T + 1/5

            sage: C = codes.databases.best_linear_code_in_guava(6, 3, GF(2))    # optional - gap_package_guava
            sage: C.minimum_distance()                                          # optional - gap_package_guava
            3
            sage: C.zeta_polynomial()                                           # optional - gap_package_guava
            2/5*T^2 + 2/5*T + 1/5

            sage: C = codes.HammingCode(GF(2), 4)
            sage: C.zeta_polynomial()                                                   # needs sage.libs.gap
            16/429*T^6 + 16/143*T^5 + 80/429*T^4 + 32/143*T^3 + 30/143*T^2 + 2/13*T + 1/13

            sage: F.<z> = GF(4,"z")
            sage: MS = MatrixSpace(F, 3, 6)
            sage: G = MS([[1,0,0,1,z,z],[0,1,0,z,1,z],[0,0,1,z,z,1]])
            sage: C = LinearCode(G)  # the "hexacode"
            sage: C.zeta_polynomial()                                                   # needs sage.libs.gap
            1

        REFERENCES:

        - [Du2001]_
        '''
    def zeta_function(self, name: str = 'T'):
        """
        Return the Duursma zeta function of the code.

        INPUT:

        - ``name`` -- string (default: ``'T'``); variable name

        OUTPUT:

        Element of `\\QQ(T)`

        EXAMPLES::

            sage: C = codes.HammingCode(GF(2), 3)
            sage: C.zeta_function()                                                     # needs sage.libs.gap
            (1/5*T^2 + 1/5*T + 1/10)/(T^2 - 3/2*T + 1/2)
        """
    def cosetGraph(self):
        """
        Return the coset graph of this linear code.

        The coset graph of a linear code `C` is the graph whose vertices
        are the cosets of `C`, considered as a subgroup of the additive
        group of the ambient vector space, and two cosets are adjacent
        if they have representatives that differ in exactly one coordinate.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: C = codes.GolayCode(GF(3))
            sage: G = C.cosetGraph()
            sage: G.is_distance_regular()
            True
            sage: C = codes.KasamiCode(8,2)
            sage: G = C.cosetGraph()
            sage: G.is_distance_regular()
            True

        ALGORITHM:

        Instead of working with cosets we compute a (direct sum) complement
        of `C`. Let `P` be the projection of the cosets to the newly found
        subspace. Then two vectors are adjacent if they differ by
        `\\lambda P(e_i)` for some `i`.

        TESTS::

            sage: # needs sage.graphs
            sage: C = codes.KasamiCode(4,2)
            sage: C.cosetGraph()
            Hamming Graph with parameters 4,2: Graph on 16 vertices
            sage: M = matrix.identity(GF(3), 7)
            sage: C = LinearCode(M)
            sage: G = C.cosetGraph()
            sage: G.vertices(sort=False)
            [0]
            sage: G.edges(sort=False)
            []
        """

class LinearCode(AbstractLinearCode):
    '''
    Linear codes over a finite field or finite ring, represented using a
    generator matrix.

    This class should be used for arbitrary and unstructured linear codes. This
    means that basic operations on the code, such as the computation of the
    minimum distance, will use generic, slow algorithms.

    If you are looking for constructing a code from a more specific family, see
    if the family has been implemented by investigating ``codes.<tab>``. These
    more specific classes use properties particular to that family to allow
    faster algorithms, and could also have family-specific methods.

    See :wikipedia:`Linear_code` for more information on unstructured linear codes.

    INPUT:

    - ``generator`` -- a generator matrix over a finite field (``G`` can be
      defined over a finite ring but the matrices over that ring must have
      certain attributes, such as ``rank``) or a code over a finite field

    - ``d`` -- (default: ``None``) the minimum distance of the code

    .. NOTE::

        The veracity of the minimum distance ``d``, if provided, is not
        checked.

    EXAMPLES::

        sage: MS = MatrixSpace(GF(2),4,7)
        sage: G  = MS([[1,1,1,0,0,0,0], [1,0,0,1,1,0,0], [0,1,0,1,0,1,0], [1,1,0,1,0,0,1]])
        sage: C  = LinearCode(G)
        sage: C
        [7, 4] linear code over GF(2)
        sage: C.base_ring()
        Finite Field of size 2
        sage: C.dimension()
        4
        sage: C.length()
        7
        sage: C.minimum_distance()                                                      # needs sage.libs.gap
        3
        sage: C.spectrum()
        [1, 0, 0, 7, 7, 0, 0, 1]
        sage: C.weight_distribution()
        [1, 0, 0, 7, 7, 0, 0, 1]

    The minimum distance of the code, if known, can be provided as an
    optional parameter.::

        sage: C  = LinearCode(G, d=3)
        sage: C.minimum_distance()                                                      # needs sage.libs.gap
        3

    Another example.::

        sage: MS = MatrixSpace(GF(5),4,7)
        sage: G  = MS([[1,1,1,0,0,0,0], [1,0,0,1,1,0,0], [0,1,0,1,0,1,0], [1,1,0,1,0,0,1]])
        sage: C  = LinearCode(G); C
        [7, 4] linear code over GF(5)

    Providing a code as the parameter in order to "forget" its structure (see
    :issue:`20198`)::

        sage: C = codes.GeneralizedReedSolomonCode(GF(23).list(), 12)
        sage: LinearCode(C)
        [23, 12] linear code over GF(23)

    Another example::

        sage: C = codes.HammingCode(GF(7), 3)
        sage: C
        [57, 54] Hamming Code over GF(7)
        sage: LinearCode(C)
        [57, 54] linear code over GF(7)

    AUTHORS:

    - David Joyner (11-2005)
    - Charles Prior (03-2016): :issue:`20198`, LinearCode from a code
    '''
    def __init__(self, generator, d=None) -> None:
        """
        See the docstring for :meth:`LinearCode`.

        EXAMPLES::

            sage: MS = MatrixSpace(GF(2),4,7)
            sage: G  = MS([[1,1,1,0,0,0,0], [1,0,0,1,1,0,0], [0,1,0,1,0,1,0], [1,1,0,1,0,0,1]])
            sage: C  = LinearCode(G)    # indirect doctest
            sage: C
            [7, 4] linear code over GF(2)

        The minimum distance of the code, if known, can be provided as an
        optional parameter.::

            sage: C  = LinearCode(G, d=3)
            sage: C.minimum_distance()                                                  # needs sage.libs.gap
            3

        TESTS::

            sage: C = codes.HammingCode(GF(2), 3)
            sage: TestSuite(C).run()

        Check that it works even with input matrix with non full rank (see
        :issue:`17452`)::

            sage: K.<a> = GF(4)
            sage: G = matrix([[a, a + 1, 1, a + 1, 1, 0, 0],
            ....:             [0, a, a + 1, 1, a + 1, 1, 0],
            ....:             [0, 0, a, a + 1, 1, a + 1, 1],
            ....:             [a + 1, 0, 1, 0, a + 1, 1, a + 1],
            ....:             [a, a + 1, a + 1, 0, 0, a + 1, 1],
            ....:             [a + 1, a, a, 1, 0, 0, a + 1],
            ....:             [a, a + 1, 1, a + 1, 1, 0, 0]])
            sage: C = LinearCode(G)
            sage: C.basis()
            [(1, 0, 0, a + 1, 0, 1, 0),
             (0, 1, 0, 0, a + 1, 0, 1),
             (0, 0, 1, a, a + 1, a, a + 1)]
            sage: C.minimum_distance()                                                  # needs sage.libs.gap
            3

        We can construct a linear code directly from a vector space::

            sage: VS = matrix(GF(2), [[1,0,1],
            ....:                     [1,0,1]]).row_space()
            sage: C = LinearCode(VS); C
            [3, 1] linear code over GF(2)

        Forbid the zero vector space (see :issue:`17452` and :issue:`6486`)::

            sage: G = matrix(GF(2), [[0,0,0]])
            sage: C = LinearCode(G)
            Traceback (most recent call last):
            ...
            ValueError: this linear code contains no nonzero vector
        """
    def __hash__(self): ...
    def generator_matrix(self, encoder_name=None, **kwargs):
        """
        Return a generator matrix of ``self``.

        INPUT:

        - ``encoder_name`` -- (default: ``None``) name of the encoder which will be
          used to compute the generator matrix. ``self._generator_matrix``
          will be returned if default value is kept.

        - ``kwargs`` -- all additional arguments are forwarded to the construction of the
          encoder that is used

        EXAMPLES::

            sage: G = matrix(GF(3),2,[1,-1,1,-1,1,1])
            sage: code = LinearCode(G)
            sage: code.generator_matrix()
            [1 2 1]
            [2 1 1]
        """

class LinearCodeGeneratorMatrixEncoder(Encoder):
    """
    Encoder based on generator_matrix for Linear codes.

    This is the default encoder of a generic linear code, and should never be used for other codes than
    :class:`LinearCode`.

    INPUT:

    - ``code`` -- the associated :class:`LinearCode` of this encoder
    """
    def __init__(self, code) -> None:
        """
        EXAMPLES::

            sage: G = Matrix(GF(2), [[1,1,1,0,0,0,0],[1,0,0,1,1,0,0],[0,1,0,1,0,1,0],[1,1,0,1,0,0,1]])
            sage: C = LinearCode(G)
            sage: E = codes.encoders.LinearCodeGeneratorMatrixEncoder(C)
            sage: E
            Generator matrix-based encoder for [7, 4] linear code over GF(2)
        """
    def __eq__(self, other):
        """
        Test equality between LinearCodeGeneratorMatrixEncoder objects.

        EXAMPLES::

            sage: G = Matrix(GF(2), [[1,1,1,0,0,0,0],[1,0,0,1,1,0,0],[0,1,0,1,0,1,0],[1,1,0,1,0,0,1]])
            sage: E1 = LinearCode(G).encoder()
            sage: E2 = LinearCode(G).encoder()
            sage: E1 == E2
            True
        """
    @cached_method
    def generator_matrix(self):
        """
        Return a generator matrix of the associated code of ``self``.

        EXAMPLES::

            sage: G = Matrix(GF(2), [[1,1,1,0,0,0,0], [1,0,0,1,1,0,0],
            ....:                    [0,1,0,1,0,1,0], [1,1,0,1,0,0,1]])
            sage: C = LinearCode(G)
            sage: E = codes.encoders.LinearCodeGeneratorMatrixEncoder(C)
            sage: E.generator_matrix()
            [1 1 1 0 0 0 0]
            [1 0 0 1 1 0 0]
            [0 1 0 1 0 1 0]
            [1 1 0 1 0 0 1]
        """

class LinearCodeSyndromeDecoder(Decoder):
    '''
    Construct a decoder for Linear Codes based on syndrome lookup table.

    The decoding algorithm works as follows:

    - First, a lookup table is built by computing the syndrome of every error
      pattern of weight up to ``maximum_error_weight``.
    - Then, whenever one tries to decode a word ``r``, the syndrome of ``r`` is
      computed. The corresponding error pattern is recovered from the
      pre-computed lookup table.
    - Finally, the recovered error pattern is subtracted from ``r`` to recover
      the original word.

    ``maximum_error_weight`` need never exceed the covering radius of the code,
    since there are then always lower-weight errors with the same syndrome. If
    one sets ``maximum_error_weight`` to a value greater than the covering
    radius, then the covering radius will be determined while building the
    lookup-table. This lower value is then returned if you query
    ``decoding_radius`` after construction.

    If ``maximum_error_weight`` is left unspecified or set to a number at least
    the covering radius of the code, this decoder is complete, i.e. it decodes
    every vector in the ambient space.

    .. NOTE::

        Constructing the lookup table takes time exponential in the length of the
        code and the size of the code\'s base field. Afterwards, the individual
        decodings are fast.

    INPUT:

    - ``code`` -- a code associated to this decoder

    - ``maximum_error_weight`` -- (default: ``None``) the maximum number of
      errors to look for when building the table. An error is raised if it is
      set greater than `n-k`, since this is an upper bound on the covering
      radius on any linear code. If ``maximum_error_weight`` is kept
      unspecified, it will be set to `n - k`, where `n` is the length of
      ``code`` and `k` its dimension.

    EXAMPLES::

        sage: G = Matrix(GF(3), [[1,0,0,1,0,1,0,1,2],
        ....:                    [0,1,0,2,2,0,1,1,0],
        ....:                    [0,0,1,0,2,2,2,1,2]])
        sage: C = LinearCode(G)
        sage: D = codes.decoders.LinearCodeSyndromeDecoder(C)
        sage: D
        Syndrome decoder for [9, 3] linear code over GF(3) handling errors of weight up to 4

    If one wants to correct up to a lower number of errors, one can do as follows::

        sage: D = codes.decoders.LinearCodeSyndromeDecoder(C, maximum_error_weight=2)
        sage: D
        Syndrome decoder for [9, 3] linear code over GF(3) handling errors of weight up to 2

    If one checks the list of types of this decoder before constructing it,
    one will notice it contains the keyword ``dynamic``.
    Indeed, the behaviour of the syndrome decoder depends on the maximum
    error weight one wants to handle, and how it compares to the minimum
    distance and the covering radius of ``code``.
    In the following examples, we illustrate this property by computing
    different instances of syndrome decoder for the same code.

    We choose the following linear code, whose covering radius equals to 4
    and minimum distance to 5 (half the minimum distance is 2)::

        sage: G = matrix(GF(5), [[1, 0, 0, 0, 0, 4, 3, 0, 3, 1, 0],
        ....:                    [0, 1, 0, 0, 0, 3, 2, 2, 3, 2, 1],
        ....:                    [0, 0, 1, 0, 0, 1, 3, 0, 1, 4, 1],
        ....:                    [0, 0, 0, 1, 0, 3, 4, 2, 2, 3, 3],
        ....:                    [0, 0, 0, 0, 1, 4, 2, 3, 2, 2, 1]])
        sage: C = LinearCode(G)

    In the following examples, we illustrate how the choice of
    ``maximum_error_weight`` influences the types of the instance of
    syndrome decoder, alongside with its decoding radius.

    We build a first syndrome decoder, and pick a ``maximum_error_weight``
    smaller than both the covering radius and half the minimum distance::

        sage: D = C.decoder("Syndrome", maximum_error_weight=1)
        sage: D.decoder_type()
        {\'always-succeed\', \'bounded_distance\', \'hard-decision\'}
        sage: D.decoding_radius()
        1

    In that case, we are sure the decoder will always succeed. It is also
    a bounded distance decoder.

    We now build another syndrome decoder, and this time,
    ``maximum_error_weight`` is chosen to be bigger than half the minimum distance,
    but lower than the covering radius::

        sage: D = C.decoder("Syndrome", maximum_error_weight=3)
        sage: D.decoder_type()
        {\'bounded_distance\', \'hard-decision\', \'might-error\'}
        sage: D.decoding_radius()
        3

    Here, we still get a bounded distance decoder.
    But because we have a maximum error weight bigger than half the
    minimum distance, we know it might return a codeword which was not
    the original codeword.

    And now, we build a third syndrome decoder, whose ``maximum_error_weight``
    is bigger than both the covering radius and half the minimum distance::

        sage: D = C.decoder("Syndrome", maximum_error_weight=5)         # long time
        sage: D.decoder_type()                                          # long time
        {\'complete\', \'hard-decision\', \'might-error\'}
        sage: D.decoding_radius()                                       # long time
        4

    In that case, the decoder might still return an unexpected codeword, but
    it is now complete. Note the decoding radius is equal to 4: it was
    determined while building the syndrome lookup table that any error with
    weight more than 4 will be decoded incorrectly. That is because the covering
    radius for the code is 4.

    The minimum distance and the covering radius are both determined while
    computing the syndrome lookup table. They user did not explicitly ask to
    compute these on the code ``C``. The dynamic typing of the syndrome decoder
    might therefore seem slightly surprising, but in the end is quite
    informative.
    '''
    def __init__(self, code, maximum_error_weight=None) -> None:
        '''
        TESTS:

        If ``maximum_error_weight`` is greater or equal than `n-k`, where `n`
        is ``code``\'s length, and `k` is ``code``\'s dimension,
        an error is raised::

            sage: G = Matrix(GF(2), [[1,1,1,0,0,0,0],[1,0,0,1,1,0,0],[0,1,0,1,0,1,0],[1,1,0,1,0,0,1]])
            sage: C = LinearCode(G)
            sage: D = codes.decoders.LinearCodeSyndromeDecoder(C, 42)
            Traceback (most recent call last):
            ...
            ValueError: maximum_error_weight has to be less than code\'s length minus its dimension

        The Syndrome Decoder of a Hamming code should have types
        ``minimum-distance`` and ``always-succeed`` (see :issue:`20898`)::

            sage: C = codes.HammingCode(GF(5), 3)
            sage: D = C.decoder("Syndrome")
            sage: C.minimum_distance()
            3
            sage: D.maximum_error_weight()
            1
            sage: D.decoder_type()
            {\'always-succeed\', \'complete\', \'hard-decision\', \'minimum-distance\'}
        '''
    def __eq__(self, other):
        """
        Test equality between LinearCodeSyndromeDecoder objects.

        EXAMPLES::

            sage: G = Matrix(GF(3), [[1,0,0,1,0,1,0,1,2],[0,1,0,2,2,0,1,1,0],[0,0,1,0,2,2,2,1,2]])
            sage: D1 = codes.decoders.LinearCodeSyndromeDecoder(LinearCode(G))
            sage: D2 = codes.decoders.LinearCodeSyndromeDecoder(LinearCode(G))
            sage: D1 == D2
            True
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: G = Matrix(GF(3), [[1,0,0,1,0,1,0,1,2],[0,1,0,2,2,0,1,1,0],[0,0,1,0,2,2,2,1,2]])
            sage: D1 = codes.decoders.LinearCodeSyndromeDecoder(LinearCode(G))
            sage: D2 = codes.decoders.LinearCodeSyndromeDecoder(LinearCode(G))
            sage: hash(D1) == hash(D2)
            True
        """
    def decode_to_code(self, r):
        """
        Correct the errors in ``word`` and return a codeword.

        INPUT:

        - ``r`` -- a codeword of ``self``

        OUTPUT: a vector of ``self``'s message space

        EXAMPLES::

            sage: G = Matrix(GF(3), [[1, 0, 0, 0, 2, 2, 1, 1],
            ....:                    [0, 1, 0, 0, 0, 0, 1, 1],
            ....:                    [0, 0, 1, 0, 2, 0, 0, 2],
            ....:                    [0, 0, 0, 1, 0, 2, 0, 1]])
            sage: C = LinearCode(G)
            sage: D = codes.decoders.LinearCodeSyndromeDecoder(C, maximum_error_weight = 1)
            sage: Chan = channels.StaticErrorRateChannel(C.ambient_space(), 1)
            sage: c = C.random_element()
            sage: r = Chan(c)
            sage: c == D.decode_to_code(r)
            True
        """
    def maximum_error_weight(self):
        """
        Return the maximal number of errors a received word can have
        and for which ``self`` is guaranteed to return a most likely codeword.

        Same as :meth:`decoding_radius`.

        EXAMPLES::

            sage: G = Matrix(GF(3), [[1,0,0,1,0,1,0,1,2],
            ....:                    [0,1,0,2,2,0,1,1,0],
            ....:                    [0,0,1,0,2,2,2,1,2]])
            sage: C = LinearCode(G)
            sage: D = codes.decoders.LinearCodeSyndromeDecoder(C)
            sage: D.maximum_error_weight()
            4
        """
    def decoding_radius(self):
        """
        Return the maximal number of errors a received word can have
        and for which ``self`` is guaranteed to return a most likely codeword.

        EXAMPLES::

            sage: G = Matrix(GF(3), [[1,0,0,1,0,1,0,1,2],
            ....:                    [0,1,0,2,2,0,1,1,0],
            ....:                    [0,0,1,0,2,2,2,1,2]])
            sage: C = LinearCode(G)
            sage: D = codes.decoders.LinearCodeSyndromeDecoder(C)
            sage: D.decoding_radius()
            4
        """
    def syndrome_table(self):
        """
        Return the syndrome lookup table of ``self``.

        EXAMPLES::

            sage: G = Matrix(GF(2), [[1,1,1,0,0,0,0], [1,0,0,1,1,0,0],
            ....:                    [0,1,0,1,0,1,0], [1,1,0,1,0,0,1]])
            sage: C = LinearCode(G)
            sage: D = codes.decoders.LinearCodeSyndromeDecoder(C)
            sage: D.syndrome_table()
            {(0, 0, 0): (0, 0, 0, 0, 0, 0, 0),
             (1, 0, 0): (1, 0, 0, 0, 0, 0, 0),
             (0, 1, 0): (0, 1, 0, 0, 0, 0, 0),
             (1, 1, 0): (0, 0, 1, 0, 0, 0, 0),
             (0, 0, 1): (0, 0, 0, 1, 0, 0, 0),
             (1, 0, 1): (0, 0, 0, 0, 1, 0, 0),
             (0, 1, 1): (0, 0, 0, 0, 0, 1, 0),
             (1, 1, 1): (0, 0, 0, 0, 0, 0, 1)}
        """

class LinearCodeNearestNeighborDecoder(Decoder):
    """
    Construct a decoder for Linear Codes. This decoder will decode to the
    nearest codeword found.

    INPUT:

    - ``code`` -- a code associated to this decoder
    """
    def __init__(self, code) -> None:
        """
        EXAMPLES::

            sage: G = Matrix(GF(2), [[1,1,1,0,0,0,0],[1,0,0,1,1,0,0],[0,1,0,1,0,1,0],[1,1,0,1,0,0,1]])
            sage: C = LinearCode(G)
            sage: D = codes.decoders.LinearCodeNearestNeighborDecoder(C)
            sage: D
            Nearest neighbor decoder for [7, 4] linear code over GF(2)
        """
    def __eq__(self, other):
        """
        Test equality between LinearCodeNearestNeighborDecoder objects.

        EXAMPLES::

            sage: G = Matrix(GF(2), [[1,1,1,0,0,0,0],[1,0,0,1,1,0,0],[0,1,0,1,0,1,0],[1,1,0,1,0,0,1]])
            sage: D1 = codes.decoders.LinearCodeNearestNeighborDecoder(LinearCode(G))
            sage: D2 = codes.decoders.LinearCodeNearestNeighborDecoder(LinearCode(G))
            sage: D1 == D2
            True
        """
    def decode_to_code(self, r):
        """
        Corrects the errors in ``word`` and returns a codeword.

        INPUT:

        - ``r`` -- a codeword of ``self``

        OUTPUT: a vector of ``self``'s message space

        EXAMPLES::

            sage: G = Matrix(GF(2), [[1,1,1,0,0,0,0], [1,0,0,1,1,0,0],
            ....:                    [0,1,0,1,0,1,0], [1,1,0,1,0,0,1]])
            sage: C = LinearCode(G)
            sage: D = codes.decoders.LinearCodeNearestNeighborDecoder(C)
            sage: word = vector(GF(2), (1, 1, 0, 0, 1, 1, 0))
            sage: w_err = word + vector(GF(2), (1, 0, 0, 0, 0, 0, 0))
            sage: D.decode_to_code(w_err)
            (1, 1, 0, 0, 1, 1, 0)
        """
    def decoding_radius(self):
        """
        Return maximal number of errors ``self`` can decode.

        EXAMPLES::

            sage: G = Matrix(GF(2), [[1,1,1,0,0,0,0], [1,0,0,1,1,0,0],
            ....:                    [0,1,0,1,0,1,0], [1,1,0,1,0,0,1]])
            sage: C = LinearCode(G)
            sage: D = codes.decoders.LinearCodeNearestNeighborDecoder(C)
            sage: D.decoding_radius()                                                   # needs sage.libs.gap
            1
        """
