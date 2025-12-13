from sage.categories.category import RR as RR
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.decorators import options as options
from sage.modular.arithgroup.congroup_gamma import Gamma_class as Gamma_class
from sage.modular.arithgroup.congroup_gamma0 import Gamma0_class as Gamma0_class
from sage.modular.arithgroup.congroup_gamma1 import Gamma1_class as Gamma1_class
from sage.modular.arithgroup.congroup_gammaH import GammaH_class as GammaH_class
from sage.modular.arithgroup.congroup_sl2z import SL2Z as SL2Z
from sage.modular.cusps import Cusp as Cusp
from sage.rings.complex_mpfr import CC as CC
from sage.rings.infinity import infinity as infinity
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, Callable, ClassVar, overload

class Farey:
    """File: /build/sagemath/src/sage/src/sage/modular/arithgroup/farey_symbol.pyx (starting at line 93)

        A class for calculating Farey symbols of arithmetics subgroups of
        `\\PSL_2(\\ZZ)`.

        The arithmetic subgroup can be either any of
        the congruence subgroups implemented in Sage, i.e. Gamma, Gamma0,
        Gamma1 and GammaH or a subgroup of `\\PSL_2(\\ZZ)` which is
        given by a user written helper class defining membership in that
        group.

        REFERENCES:

        - Ravi S. Kulkarni, ''An arithmetic-geometric method in the study of the
          subgroups of the modular group'', `Amer. J. Math., 113(6):1053--1133,
          1991. <http://www.jstor.org/stable/2374900>`_

        INPUT:

        - ``G`` -- an arithmetic subgroup of `\\PSL_2(\\ZZ)`

        EXAMPLES:

        Create a Farey symbol for the group `\\Gamma_0(11)`::

            sage: f = FareySymbol(Gamma0(11)); f
            FareySymbol(Congruence Subgroup Gamma0(11))

        Calculate the generators::

             sage: f.generators()
             [
             [1 1]  [ 7 -2]  [ 8 -3]  [-1  0]
             [0 1], [11 -3], [11 -4], [ 0 -1]
             ]

        Pickling the FareySymbol and recovering it::

             sage: f == loads(dumps(f))
             True

        Calculate the index of `\\Gamma_H(33, [2, 5])` in
        `\\PSL_2(\\ZZ)` via FareySymbol::

             sage: FareySymbol(GammaH(33, [2, 5])).index()
             48

        Calculate the generators of `\\Gamma_1(4)`::

             sage: FareySymbol(Gamma1(4)).generators()
             [
             [1 1]  [-3  1]
             [0 1], [-4  1]
             ]

        Calculate the generators of the :meth:`example
        <sage.modular.arithgroup.arithgroup_perm.HsuExample10>` of an
        index 10 arithmetic subgroup given by Tim Hsu::

             sage: from sage.modular.arithgroup.arithgroup_perm import HsuExample10
             sage: FareySymbol(HsuExample10()).generators()
             [
             [1 2]  [-2  1]  [ 4 -3]
             [0 1], [-7  3], [ 3 -2]
             ]

        Calculate the generators of the group `\\Gamma' =
        \\Gamma_0(8)\\cap\\Gamma_1(4)` using a helper class to define group membership::

             sage: class GPrime:
             ....:     def __contains__(self, M):
             ....:         return M in Gamma0(8) and M in Gamma1(4)

             sage: FareySymbol(GPrime()).generators()
             [
             [1 1]  [ 5 -1]  [ 5 -2]
             [0 1], [16 -3], [ 8 -3]
             ]

        Calculate cusps of arithmetic subgroup defined via permutation group::

            sage: L = SymmetricGroup(4)('(1, 2, 3)')

            sage: R = SymmetricGroup(4)('(1, 2, 4)')

            sage: FareySymbol(ArithmeticSubgroup_Permutation(L, R)).cusps()
            [-1, Infinity]

        Calculate the left coset representation of `\\Gamma_H(8, [3])`::

             sage: FareySymbol(GammaH(8, [3])).coset_reps()
             [
             [1 0]  [ 4 -1]  [ 3 -1]  [ 2 -1]  [ 1 -1]  [ 3 -1]  [ 2 -1]  [-1  0]
             [0 1], [ 1  0], [ 1  0], [ 1  0], [ 1  0], [ 4 -1], [ 3 -1], [ 3 -1],
             [ 1 -1]  [-1  0]  [ 0 -1]  [-1  0]
             [ 2 -1], [ 2 -1], [ 1 -1], [ 1 -1]
             ]
    """
    fundamental_domain: ClassVar[Callable] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def coset_reps(self) -> Any:
        """Farey.coset_reps(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/farey_symbol.pyx (starting at line 692)

        Left coset of the arithmetic group of the FareySymbol.

        EXAMPLES:

        Calculate the left coset of `\\Gamma_0(6)`::

            sage: FareySymbol(Gamma0(6)).coset_reps()
            [
            [1 0]  [ 3 -1]  [ 2 -1]  [ 1 -1]  [ 2 -1]  [ 3 -2]  [ 1 -1]  [-1  0]
            [0 1], [ 1  0], [ 1  0], [ 1  0], [ 3 -1], [ 2 -1], [ 2 -1], [ 2 -1],
            [ 1 -1]  [ 0 -1]  [-1  0]  [-2  1]
            [ 3 -2], [ 1 -1], [ 1 -1], [ 1 -1]
            ]"""
    def cusp_class(self, c) -> Any:
        """Farey.cusp_class(self, c)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/farey_symbol.pyx (starting at line 843)

        Cusp class of a cusp in the FareySymbol.

        INPUT:

        - ``c`` -- a cusp

        EXAMPLES::

            sage: FareySymbol(Gamma0(12)).cusp_class(Cusp(1, 12))
            5"""
    @overload
    def cusp_widths(self) -> Any:
        """Farey.cusp_widths(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/farey_symbol.pyx (starting at line 832)

        Cusps widths of the FareySymbol.

        EXAMPLES::

            sage: FareySymbol(Gamma0(6)).cusp_widths()
            [6, 2, 3, 1]"""
    @overload
    def cusp_widths(self) -> Any:
        """Farey.cusp_widths(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/farey_symbol.pyx (starting at line 832)

        Cusps widths of the FareySymbol.

        EXAMPLES::

            sage: FareySymbol(Gamma0(6)).cusp_widths()
            [6, 2, 3, 1]"""
    @overload
    def cusps(self) -> Any:
        """Farey.cusps(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/farey_symbol.pyx (starting at line 821)

        Cusps of the FareySymbol.

        EXAMPLES::

            sage: FareySymbol(Gamma0(6)).cusps()
            [0, 1/3, 1/2, Infinity]"""
    @overload
    def cusps(self) -> Any:
        """Farey.cusps(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/farey_symbol.pyx (starting at line 821)

        Cusps of the FareySymbol.

        EXAMPLES::

            sage: FareySymbol(Gamma0(6)).cusps()
            [0, 1/3, 1/2, Infinity]"""
    @overload
    def fractions(self) -> Any:
        """Farey.fractions(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/farey_symbol.pyx (starting at line 748)

        Fractions of the FareySymbol.

        EXAMPLES::

            sage: FareySymbol(Gamma(4)).fractions()
            [0, 1/2, 1, 3/2, 2, 5/2, 3, 7/2, 4]"""
    @overload
    def fractions(self) -> Any:
        """Farey.fractions(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/farey_symbol.pyx (starting at line 748)

        Fractions of the FareySymbol.

        EXAMPLES::

            sage: FareySymbol(Gamma(4)).fractions()
            [0, 1/2, 1, 3/2, 2, 5/2, 3, 7/2, 4]"""
    def generators(self) -> Any:
        '''Farey.generators(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/farey_symbol.pyx (starting at line 710)

        Minimal set of generators of the group of the FareySymbol.

        EXAMPLES:

        Calculate the generators of `\\Gamma_0(6)`::

            sage: FareySymbol(Gamma0(6)).generators()
            [
            [1 1]  [ 5 -1]  [ 7 -3]  [-1  0]
            [0 1], [ 6 -1], [12 -5], [ 0 -1]
            ]

        Calculate the generators of `\\SL_2(\\ZZ)`::

            sage: FareySymbol(SL2Z).generators()
            [
            [ 0 -1]  [ 0 -1]
            [ 1  0], [ 1 -1]
            ]

        The unique index 2 even subgroup and index 4 odd subgroup each get handled correctly::

            sage: # needs sage.groups
            sage: FareySymbol(ArithmeticSubgroup_Permutation(S2="(1,2)", S3="()")).generators()
            [
            [ 0  1]  [-1  1]
            [-1 -1], [-1  0]
            ]
            sage: FareySymbol(ArithmeticSubgroup_Permutation(S2="(1,2, 3, 4)", S3="(1,3)(2,4)")).generators()
            [
            [ 0  1]  [-1  1]
            [-1 -1], [-1  0]
            ]'''
    @overload
    def genus(self) -> Any:
        """Farey.genus(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/farey_symbol.pyx (starting at line 648)

        Return the genus of the arithmetic group of the FareySymbol.

        EXAMPLES::

            sage: [FareySymbol(Gamma0(n)).genus() for n in range(16, 32)]
            [0, 1, 0, 1, 1, 1, 2, 2, 1, 0, 2, 1, 2, 2, 3, 2]"""
    @overload
    def genus(self) -> Any:
        """Farey.genus(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/farey_symbol.pyx (starting at line 648)

        Return the genus of the arithmetic group of the FareySymbol.

        EXAMPLES::

            sage: [FareySymbol(Gamma0(n)).genus() for n in range(16, 32)]
            [0, 1, 0, 1, 1, 1, 2, 2, 1, 0, 2, 1, 2, 2, 3, 2]"""
    def index(self) -> Any:
        """Farey.index(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/farey_symbol.pyx (starting at line 636)

        Return the index of the arithmetic group of the FareySymbol
        in `\\PSL_2(\\ZZ)`.

        EXAMPLES::

            sage: [FareySymbol(Gamma0(n)).index() for n in range(1, 16)]
            [1, 3, 4, 6, 6, 12, 8, 12, 12, 18, 12, 24, 14, 24, 24]"""
    @overload
    def level(self) -> Any:
        """Farey.level(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/farey_symbol.pyx (starting at line 659)

        Return the level of the arithmetic group of the FareySymbol.

        EXAMPLES::

            sage: [FareySymbol(Gamma0(n)).level() for n in range(1, 16)]
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]"""
    @overload
    def level(self) -> Any:
        """Farey.level(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/farey_symbol.pyx (starting at line 659)

        Return the level of the arithmetic group of the FareySymbol.

        EXAMPLES::

            sage: [FareySymbol(Gamma0(n)).level() for n in range(1, 16)]
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]"""
    @overload
    def nu2(self) -> Any:
        """Farey.nu2(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/farey_symbol.pyx (starting at line 670)

        Return the number of elliptic points of order two.

        EXAMPLES::

            sage: [FareySymbol(Gamma0(n)).nu2() for n in range(1, 16)]
            [1, 1, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0]"""
    @overload
    def nu2(self) -> Any:
        """Farey.nu2(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/farey_symbol.pyx (starting at line 670)

        Return the number of elliptic points of order two.

        EXAMPLES::

            sage: [FareySymbol(Gamma0(n)).nu2() for n in range(1, 16)]
            [1, 1, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0]"""
    @overload
    def nu3(self) -> Any:
        """Farey.nu3(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/farey_symbol.pyx (starting at line 681)

        Return the number of elliptic points of order three.

        EXAMPLES::

            sage: [FareySymbol(Gamma0(n)).nu3() for n in range(1, 16)]
            [1, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0]"""
    @overload
    def nu3(self) -> Any:
        """Farey.nu3(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/farey_symbol.pyx (starting at line 681)

        Return the number of elliptic points of order three.

        EXAMPLES::

            sage: [FareySymbol(Gamma0(n)).nu3() for n in range(1, 16)]
            [1, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0]"""
    @overload
    def paired_sides(self) -> Any:
        """Farey.paired_sides(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/farey_symbol.pyx (starting at line 788)

        Pairs of index of the sides of the fundamental domain of the
        Farey symbol of the arithmetic group. The sides of the
        hyperbolic polygon are numbered 0, 1, ... from left to right.

        .. image:: ../../../media/pairing.png

        EXAMPLES::

            sage: FareySymbol(Gamma0(11)).paired_sides()
            [(0, 5), (1, 3), (2, 4)]

        indicating that the side 0 is paired with 5, 1 with 3 and 2 with 4."""
    @overload
    def paired_sides(self) -> Any:
        """Farey.paired_sides(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/farey_symbol.pyx (starting at line 788)

        Pairs of index of the sides of the fundamental domain of the
        Farey symbol of the arithmetic group. The sides of the
        hyperbolic polygon are numbered 0, 1, ... from left to right.

        .. image:: ../../../media/pairing.png

        EXAMPLES::

            sage: FareySymbol(Gamma0(11)).paired_sides()
            [(0, 5), (1, 3), (2, 4)]

        indicating that the side 0 is paired with 5, 1 with 3 and 2 with 4."""
    @overload
    def pairing_matrices(self) -> Any:
        """Farey.pairing_matrices(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/farey_symbol.pyx (starting at line 805)

        Pairing matrices of the sides of the fundamental domain. The sides
        of the hyperbolic polygon are numbered 0, 1, ... from left to right.

        EXAMPLES::

            sage: FareySymbol(Gamma0(6)).pairing_matrices()
            [
            [1 1]  [ 5 -1]  [ 7 -3]  [ 5 -3]  [ 1 -1]  [-1  1]
            [0 1], [ 6 -1], [12 -5], [12 -7], [ 6 -5], [ 0 -1]
            ]"""
    @overload
    def pairing_matrices(self) -> Any:
        """Farey.pairing_matrices(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/farey_symbol.pyx (starting at line 805)

        Pairing matrices of the sides of the fundamental domain. The sides
        of the hyperbolic polygon are numbered 0, 1, ... from left to right.

        EXAMPLES::

            sage: FareySymbol(Gamma0(6)).pairing_matrices()
            [
            [1 1]  [ 5 -1]  [ 7 -3]  [ 5 -3]  [ 1 -1]  [-1  1]
            [0 1], [ 6 -1], [12 -5], [12 -7], [ 6 -5], [ 0 -1]
            ]"""
    @overload
    def pairing_matrices_to_tietze_index(self) -> Any:
        """Farey.pairing_matrices_to_tietze_index(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/farey_symbol.pyx (starting at line 253)

        Obtain the translation table from pairing matrices
        to generators.

        The result is cached.

        OUTPUT:

        a list where the `i`-th entry is a nonzero integer `k`,
        such that if `k > 0` then the `i`-th pairing matrix is (up to sign)
        the `(k-1)`-th generator and, if `k < 0`, then the `i`-th pairing
        matrix is (up to sign) the inverse of the `(-k-1)`-th generator.

        EXAMPLES::

            sage: F = Gamma0(40).farey_symbol()
            sage: table = F.pairing_matrices_to_tietze_index()
            sage: table[12]
            (-2, -1)
            sage: F.pairing_matrices()[12]
            [  3  -1]
            [ 40 -13]
            sage: F.generators()[1]**-1
            [ -3   1]
            [-40  13]"""
    @overload
    def pairing_matrices_to_tietze_index(self) -> Any:
        """Farey.pairing_matrices_to_tietze_index(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/farey_symbol.pyx (starting at line 253)

        Obtain the translation table from pairing matrices
        to generators.

        The result is cached.

        OUTPUT:

        a list where the `i`-th entry is a nonzero integer `k`,
        such that if `k > 0` then the `i`-th pairing matrix is (up to sign)
        the `(k-1)`-th generator and, if `k < 0`, then the `i`-th pairing
        matrix is (up to sign) the inverse of the `(-k-1)`-th generator.

        EXAMPLES::

            sage: F = Gamma0(40).farey_symbol()
            sage: table = F.pairing_matrices_to_tietze_index()
            sage: table[12]
            (-2, -1)
            sage: F.pairing_matrices()[12]
            [  3  -1]
            [ 40 -13]
            sage: F.generators()[1]**-1
            [ -3   1]
            [-40  13]"""
    @overload
    def pairings(self) -> Any:
        """Farey.pairings(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/farey_symbol.pyx (starting at line 759)

        Pairings of the sides of the fundamental domain of the Farey symbol
        of the arithmetic group.

        The sides of the hyperbolic polygon are
        numbered 0, 1, ... from left to right. Conventions: even pairings are
        denoted by -2, odd pairings by -3 while free pairings are denoted by
        an integer number greater than zero.

        EXAMPLES:

        Odd pairings::

            sage: FareySymbol(Gamma0(7)).pairings()
            [1, -3, -3, 1]

        Even and odd pairings::

            FareySymbol(Gamma0(13)).pairings()
            [1, -3, -2, -2, -3, 1]

        Only free pairings::

            sage: FareySymbol(Gamma0(23)).pairings()
            [1, 2, 3, 5, 3, 4, 2, 4, 5, 1]"""
    @overload
    def pairings(self) -> Any:
        """Farey.pairings(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/farey_symbol.pyx (starting at line 759)

        Pairings of the sides of the fundamental domain of the Farey symbol
        of the arithmetic group.

        The sides of the hyperbolic polygon are
        numbered 0, 1, ... from left to right. Conventions: even pairings are
        denoted by -2, odd pairings by -3 while free pairings are denoted by
        an integer number greater than zero.

        EXAMPLES:

        Odd pairings::

            sage: FareySymbol(Gamma0(7)).pairings()
            [1, -3, -3, 1]

        Even and odd pairings::

            FareySymbol(Gamma0(13)).pairings()
            [1, -3, -2, -2, -3, 1]

        Only free pairings::

            sage: FareySymbol(Gamma0(23)).pairings()
            [1, 2, 3, 5, 3, 4, 2, 4, 5, 1]"""
    @overload
    def pairings(self) -> Any:
        """Farey.pairings(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/farey_symbol.pyx (starting at line 759)

        Pairings of the sides of the fundamental domain of the Farey symbol
        of the arithmetic group.

        The sides of the hyperbolic polygon are
        numbered 0, 1, ... from left to right. Conventions: even pairings are
        denoted by -2, odd pairings by -3 while free pairings are denoted by
        an integer number greater than zero.

        EXAMPLES:

        Odd pairings::

            sage: FareySymbol(Gamma0(7)).pairings()
            [1, -3, -3, 1]

        Even and odd pairings::

            FareySymbol(Gamma0(13)).pairings()
            [1, -3, -2, -2, -3, 1]

        Only free pairings::

            sage: FareySymbol(Gamma0(23)).pairings()
            [1, 2, 3, 5, 3, 4, 2, 4, 5, 1]"""
    @overload
    def pairings(self) -> Any:
        """Farey.pairings(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/farey_symbol.pyx (starting at line 759)

        Pairings of the sides of the fundamental domain of the Farey symbol
        of the arithmetic group.

        The sides of the hyperbolic polygon are
        numbered 0, 1, ... from left to right. Conventions: even pairings are
        denoted by -2, odd pairings by -3 while free pairings are denoted by
        an integer number greater than zero.

        EXAMPLES:

        Odd pairings::

            sage: FareySymbol(Gamma0(7)).pairings()
            [1, -3, -3, 1]

        Even and odd pairings::

            FareySymbol(Gamma0(13)).pairings()
            [1, -3, -2, -2, -3, 1]

        Only free pairings::

            sage: FareySymbol(Gamma0(23)).pairings()
            [1, 2, 3, 5, 3, 4, 2, 4, 5, 1]"""
    def reduce_to_cusp(self, r) -> Any:
        """Farey.reduce_to_cusp(self, r)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/farey_symbol.pyx (starting at line 864)

        Transformation of a rational number to cusp representative.

        INPUT:

        - ``r`` -- a rational number

        EXAMPLES::

            sage: FareySymbol(Gamma0(12)).reduce_to_cusp(5/8)
            [ 5  -3]
            [12  -7]

        Reduce 11/17 to a cusp of for HsuExample10()::

            sage: # needs sage.groups
            sage: from sage.modular.arithgroup.arithgroup_perm import HsuExample10
            sage: f = FareySymbol(HsuExample10())
            sage: f.reduce_to_cusp(11/17)
            [14 -9]
            [-3  2]
            sage: _.acton(11/17)
            1
            sage: f.cusps()[f.cusp_class(11/17)]
            1"""
    def word_problem(self, M, output=..., check=...) -> Any:
        '''Farey.word_problem(self, M, output=\'standard\', check=True)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/farey_symbol.pyx (starting at line 344)

        Solve the word problem (up to sign) using this Farey symbol.

        INPUT:

        - ``M`` -- an element `M` of `\\SL_2(\\ZZ)`

        - ``output`` -- (default: ``\'standard\'``) should be one of
          ``\'standard\'``, ``\'syllables\'``, ``\'gens\'``.

        - ``check`` -- boolean (default: ``True``); whether to check for
          correct input and output

        OUTPUT:

        A solution to the word problem for the matrix `M`.
        The format depends on the ``output`` parameter, as follows.

        - ``\'standard\'`` returns the so called Tietze representation,
          which consists of a tuple of nonzero integers.  A positive
          integer `i` indicates the `i`-th generator (that is,
          ``self.generators()[i-1]``), while a negative integer `i`
          indicates the inverse of the `i`-th generator.
        - ``\'syllables\'`` returns a tuple of tuples of the form
          `(i, n)`, where `(i, n)` represents ``self.generators()[i] ^ n``,
          whose product equals `M` up to sign.
        - ``\'gens\'`` returns a tuple of pairs `(g, n)`, where `g` is a
          matrix and `n` an integer, such that the product of the
          matrices `g^n` equals `M` up to sign.

        EXAMPLES::

            sage: F = Gamma0(30).farey_symbol()
            sage: gens = F.generators()
            sage: g = gens[3] * gens[10] * gens[8]^-1 * gens[5]
            sage: g
            [-628597   73008]
            [-692130   80387]
            sage: F.word_problem(g)
            (4, 11, -9, 6)
            sage: g = gens[3] * gens[10]^2 * gens[8]^-1 * gens[5]
            sage: g
            [-5048053   586303]
            [-5558280   645563]
            sage: F.word_problem(g, output=\'gens\')
            ((
            [109 -10]
            [120 -11], 1
            ),
             (
            [ 19  -7]
            [ 30 -11], 2
            ),
             (
            [ 49  -9]
            [ 60 -11], -1
            ),
             (
            [17 -2]
            [60 -7], 1
            ))
            sage: F.word_problem(g, output=\'syllables\')
            ((3, 1), (10, 2), (8, -1), (5, 1))

        TESTS:

        Check that problem with forgotten generator is fixed::

            sage: from sage.misc.misc_c import prod
            sage: G = Gamma0(10)
            sage: F = G.farey_symbol()
            sage: g = G([-701,-137,4600,899])
            sage: g1 = prod(F.generators()[i]**a for i, a in F.word_problem(g, output=\'syllables\'))
            sage: g == g1
            True

        Check that it works for GammaH as well (:issue:`19660`)::

            sage: G = GammaH(147, [8])
            sage: G.farey_symbol().word_problem(G([1,1,0,1]))
            (1,)

        Check that :issue:`20347` is solved::

            sage: from sage.misc.misc_c import prod
            sage: G = ArithmeticSubgroup_Permutation(S2="(1,2)(3,4)", S3="(1,2,3)")
            sage: S = G.farey_symbol()
            sage: g1, g2 = S.generators()
            sage: g = g1^3 * g2^-2 * g1 * g2
            sage: S.word_problem(g)
            (2, 2, 2, 1, 1, 1, 2, 1, 2)
            sage: h = prod(S.generators()[i]**a for i, a in S.word_problem(g, output=\'syllables\'))
            sage: g == h
            True'''
    def __contains__(self, M) -> Any:
        """Farey.__contains__(self, M)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/farey_symbol.pyx (starting at line 514)

        Test if element is in the arithmetic group of the Farey symbol
        via LLT algorithm.

        EXAMPLES::

            sage: SL2Z([0, -1, 1, 0]) in FareySymbol(Gamma0(6))
            False

            sage: SL2Z([1, 1, 0, 1]) in FareySymbol(Gamma0(6))
            True"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    @overload
    def __reduce__(self) -> Any:
        """Farey.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/farey_symbol.pyx (starting at line 563)

        Serialization for pickling::

            sage: FareySymbol(Gamma0(4)).__reduce__()
            (<class 'sage.modular.arithgroup.farey_symbol.Farey'>, ...))"""
    @overload
    def __reduce__(self) -> Any:
        """Farey.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/modular/arithgroup/farey_symbol.pyx (starting at line 563)

        Serialization for pickling::

            sage: FareySymbol(Gamma0(4)).__reduce__()
            (<class 'sage.modular.arithgroup.farey_symbol.Farey'>, ...))"""
