from _typeshed import Incomplete
from sage.algebras.free_algebra import FreeAlgebra as FreeAlgebra
from sage.categories.action import Action as Action
from sage.categories.groups import Groups as Groups
from sage.combinat.permutation import Permutation as Permutation, Permutations as Permutations
from sage.combinat.subset import Subsets as Subsets
from sage.features.sagemath import sage__libs__braiding as sage__libs__braiding
from sage.functions.generalized import sign as sign
from sage.groups.artin import FiniteTypeArtinGroup as FiniteTypeArtinGroup, FiniteTypeArtinGroupElement as FiniteTypeArtinGroupElement
from sage.groups.finitely_presented import FinitelyPresentedGroup as FinitelyPresentedGroup, GroupMorphismWithGensImages as GroupMorphismWithGensImages
from sage.groups.free_group import FreeGroup as FreeGroup, is_FreeGroup as is_FreeGroup
from sage.groups.perm_gps.permgroup_named import SymmetricGroup as SymmetricGroup, SymmetricGroupElement as SymmetricGroupElement
from sage.libs.gap.libgap import libgap as libgap
from sage.matrix.constructor import identity_matrix as identity_matrix, matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.laurent_polynomial_ring import LaurentPolynomialRing as LaurentPolynomialRing
from sage.sets.set import Set as Set
from sage.structure.element import Expression as Expression
from sage.structure.richcmp import rich_to_bool as rich_to_bool, richcmp as richcmp

class Braid(FiniteTypeArtinGroupElement):
    """
    An element of a braid group.

    It is a particular case of element of a finitely presented group.

    EXAMPLES::

        sage: B.<s0,s1,s2> = BraidGroup(4)
        sage: B
        Braid group on 4 strands
        sage: s0*s1/s2/s1
        s0*s1*s2^-1*s1^-1
        sage: B((1, 2, -3, -2))
        s0*s1*s2^-1*s1^-1
    """
    def __hash__(self):
        """
        Return a hash value for ``self``.

        EXAMPLES::

            sage: B.<s0,s1,s2> = BraidGroup(4)
            sage: hash(s0*s2) == hash(s2*s0)
            True
            sage: hash(s0*s1) == hash(s1*s0)
            False
        """
    def strands(self):
        """
        Return the number of strands in the braid.

        EXAMPLES::

            sage: B = BraidGroup(4)
            sage: b = B([1, 2, -1, 3, -2])
            sage: b.strands()
            4
        """
    def components_in_closure(self):
        """
        Return the number of components of the trace closure of the braid.

        OUTPUT: a positive integer

        EXAMPLES::

            sage: B = BraidGroup(5)
            sage: b = B([1, -3])  # Three disjoint unknots
            sage: b.components_in_closure()
            3
            sage: b = B([1, 2, 3, 4])  # The unknot
            sage: b.components_in_closure()
            1
            sage: B = BraidGroup(4)
            sage: K11n42 = B([1, -2, 3, -2, 3, -2, -2, -1, 2, -3, -3, 2, 2])
            sage: K11n42.components_in_closure()
            1
        """
    def burau_matrix(self, var: str = 't', reduced: bool = False):
        """
        Return the Burau matrix of the braid.

        INPUT:

        - ``var`` -- string (default: ``'t'``); the name of the
          variable in the entries of the matrix
        - ``reduced`` -- boolean (default: ``False``); whether to
          return the reduced or unreduced Burau representation, can
          be one of the following:

          * ``True`` or ``'increasing'`` -- returns the reduced form using
            the basis given by `e_1 - e_i` for `2 \\leq i \\leq n`
          * ``'unitary'`` -- the unitary form according to Squier [Squ1984]_
          * ``'simple'`` -- returns the reduced form using the basis given
            by simple roots `e_i - e_{i+1}`, which yields the matrices
            given on the Wikipedia page

        OUTPUT:

        The Burau matrix of the braid. It is a matrix whose entries
        are Laurent polynomials in the variable ``var``. If ``reduced``
        is ``True``, return the matrix for the reduced Burau representation
        instead in the format specified. If ``reduced`` is ``'unitary'``,
        a triple ``M, Madj, H`` is returned, where ``M`` is the Burau matrix
        in the unitary form, ``Madj`` the adjoined to ``M`` and ``H``
        the hermitian form.

        EXAMPLES::

            sage: B = BraidGroup(4)
            sage: B.inject_variables()
            Defining s0, s1, s2
            sage: b = s0 * s1 / s2 / s1
            sage: b.burau_matrix()
            [       1 - t            0      t - t^2          t^2]
            [           1            0            0            0]
            [           0            0            1            0]
            [           0         t^-2 -t^-2 + t^-1    -t^-1 + 1]
            sage: s2.burau_matrix('x')
            [    1     0     0     0]
            [    0     1     0     0]
            [    0     0 1 - x     x]
            [    0     0     1     0]
            sage: s0.burau_matrix(reduced=True)
            [-t  0  0]
            [-t  1  0]
            [-t  0  1]

        Using the different reduced forms::

            sage: b.burau_matrix(reduced='simple')
            [    1 - t -t^-1 + 1        -1]
            [        1 -t^-1 + 1        -1]
            [        1     -t^-1         0]

            sage: M, Madj, H = b.burau_matrix(reduced='unitary')
            sage: M
            [-t^-2 + 1         t       t^2]
            [ t^-1 - t   1 - t^2      -t^3]
            [    -t^-2     -t^-1         0]
            sage: Madj
            [  1 - t^2 -t^-1 + t      -t^2]
            [     t^-1 -t^-2 + 1        -t]
            [     t^-2     -t^-3         0]
            sage: H
            [t^-1 + t       -1        0]
            [      -1 t^-1 + t       -1]
            [       0       -1 t^-1 + t]
            sage: M * H * Madj == H
            True

        The adjoined matrix (``Madj`` in the above example) matches the
        output of :meth:`sage.groups.artin.ArtinGroupElement.burau_matrix`::

            sage: from sage.groups.artin import ArtinGroupElement
            sage: Madj == ArtinGroupElement.burau_matrix(b)
            True

            sage: a = s0^2 * s1 * s0 * s2 *s1 * ~s0 * s1^3 * s0 * s2 * s1^-2 * s0
            sage: a.burau_matrix(reduced='unitary')[1] == ArtinGroupElement.burau_matrix(a)
            True

        We verify Bigelow's example that in `B_5` the Burau representation
        is not faithful::

            sage: B.<s1,s2,s3,s4> = BraidGroup(5)
            sage: psi1 = ~s3 * s2 * s1^2 * s2 * s4^3 * s3 * s2
            sage: psi2 = ~s4 * s3 * s2 * s1^-2 * s2 * s1^2 * s2^2 * s1 * s4^5
            sage: alpha = ~psi1 * s4 * psi1
            sage: beta = ~psi2 * s4 * s3 * s2 * s1^2 * s2 * s3 * s4 * psi2
            sage: elm = alpha * beta * ~alpha * ~beta
            sage: elm.burau_matrix()
            [1 0 0 0 0]
            [0 1 0 0 0]
            [0 0 1 0 0]
            [0 0 0 1 0]
            [0 0 0 0 1]
            sage: elm.burau_matrix(reduced=True)
            [1 0 0 0]
            [0 1 0 0]
            [0 0 1 0]
            [0 0 0 1]
            sage: elm.is_one()
            False

        REFERENCES:

        - :wikipedia:`Burau_representation`
        - [Squ1984]_
        """
    def alexander_polynomial(self, var: str = 't', normalized: bool = True):
        """
        Return the Alexander polynomial of the closure of the braid.

        INPUT:

        - ``var`` -- string (default: ``'t'``); the name of the
          variable in the entries of the matrix
        - ``normalized`` -- boolean (default: ``True``); whether to
          return the normalized Alexander polynomial

        OUTPUT: the Alexander polynomial of the braid closure of the braid

        This is computed using the reduced Burau representation. The
        unnormalized Alexander polynomial is a Laurent polynomial,
        which is only well-defined up to multiplication by plus or
        minus times a power of `t`.

        We normalize the polynomial by dividing by the largest power
        of `t` and then if the resulting constant coefficient
        is negative, we multiply by `-1`.

        EXAMPLES:

        We first construct the trefoil::

            sage: B = BraidGroup(3)
            sage: b = B([1,2,1,2])
            sage: b.alexander_polynomial(normalized=False)
            1 - t + t^2
            sage: b.alexander_polynomial()
            t^-2 - t^-1 + 1

        Next we construct the figure 8 knot::

            sage: b = B([-1,2,-1,2])
            sage: b.alexander_polynomial(normalized=False)
            -t^-2 + 3*t^-1 - 1
            sage: b.alexander_polynomial()
            t^-2 - 3*t^-1 + 1

        Our last example is the Kinoshita-Terasaka knot::

            sage: B = BraidGroup(4)
            sage: b = B([1,1,1,3,3,2,-3,-1,-1,2,-1,-3,-2])
            sage: b.alexander_polynomial(normalized=False)
            -t^-1
            sage: b.alexander_polynomial()
            1

        REFERENCES:

        - :wikipedia:`Alexander_polynomial`
        """
    def permutation(self, W=None):
        """
        Return the permutation induced by the braid in its strands.

        INPUT:

        - ``W`` -- (optional) the permutation group to project
          ``self`` to; the default is ``self.parent().coxeter_group()``

        OUTPUT: the image of ``self`` under the natural projection map to ``W``

        EXAMPLES::

            sage: B.<s0,s1,s2> = BraidGroup()
            sage: S = SymmetricGroup(4)
            sage: b = s0*s1/s2/s1
            sage: c0 = b.permutation(W=S); c0
            (1,4,2)
            sage: c1 = b.permutation(W=Permutations(4)); c1
            [4, 1, 3, 2]
            sage: c1 == b.permutation()
            True

        The canonical section from the symmetric group to the braid group
        (sending a permutation to its associated permutation braid)
        can be recovered::

            sage: B(c0)
            s0*s1*s2*s1
            sage: B(c0) == B(c1)
            True
        """
    def plot(self, color: str = 'rainbow', orientation: str = 'bottom-top', gap: float = 0.05, aspect_ratio: int = 1, axes: bool = False, **kwds):
        '''
        Plot the braid.

        The following options are available:

        - ``color`` -- (default: ``\'rainbow\'``) the color of the
          strands. Possible values are:

            * ``\'rainbow\'``, uses :meth:`~sage.plot.colors.rainbow`
              according to the number of strands.

            * a valid color name for :meth:`~sage.plot.bezier_path`
              and :meth:`~sage.plot.line`. Used for all strands.

            * a list or a tuple of colors for each individual strand.

        - ``orientation`` -- (default: ``\'bottom-top\'``) determines how
          the braid is printed. The possible values are:

            * ``\'bottom-top\'``, the braid is printed from bottom to top

            * ``\'top-bottom\'``, the braid is printed from top to bottom

            * ``\'left-right\'``, the braid is printed from left to right

        - ``gap`` -- floating point number (default: 0.05); determines
          the size of the gap left when a strand goes under another

        - ``aspect_ratio`` -- floating point number (default:
          ``1``); the aspect ratio

        - ``**kwds`` -- other keyword options that are passed to
          :meth:`~sage.plot.bezier_path` and :meth:`~sage.plot.line`

        EXAMPLES::

            sage: B = BraidGroup(3)
            sage: a = B([2, 2, -1, -1])
            sage: b = B([2, 1, 2, 1])
            sage: c = b * a / b
            sage: d = a.conjugating_braid(c)
            sage: d * c / d == a
            True
            sage: d
            s1*s0
            sage: d * a / d == c
            False
            sage: B = BraidGroup(4, \'s\')
            sage: b = B([1, 2, 3, 1, 2, 1])
            sage: b.plot()                                                              # needs sage.plot
            Graphics object consisting of 30 graphics primitives
            sage: b.plot(color=["red", "blue", "red", "blue"])                          # needs sage.plot
            Graphics object consisting of 30 graphics primitives

            sage: B.<s,t> = BraidGroup(3)
            sage: b = t^-1*s^2
            sage: b.plot(orientation=\'left-right\', color=\'red\')                         # needs sage.plot
            Graphics object consisting of 12 graphics primitives
        '''
    def plot3d(self, color: str = 'rainbow'):
        '''
        Plot the braid in 3d.

        The following option is available:

        - ``color`` -- (default: ``\'rainbow\'``) the color of the
          strands. Possible values are:

            * ``\'rainbow\'``, uses :meth:`~sage.plot.colors.rainbow`
              according to the number of strands.

            * a valid color name for :meth:`~sage.plot.plot3d.bezier3d`.
              Used for all strands.

            * a list or a tuple of colors for each individual strand.

        EXAMPLES::

            sage: B = BraidGroup(4, \'s\')
            sage: b = B([1, 2, 3, 1, 2, 1])
            sage: b.plot3d()                                                            # needs sage.plot sage.symbolic
            Graphics3d Object
            sage: b.plot3d(color=\'red\')                                                 # needs sage.plot sage.symbolic
            Graphics3d Object
            sage: b.plot3d(color=["red", "blue", "red", "blue"])                        # needs sage.plot sage.symbolic
            Graphics3d Object
        '''
    def LKB_matrix(self, variables: str = 'x,y'):
        """
        Return the Lawrence-Krammer-Bigelow representation matrix.

        The matrix is expressed in the basis `\\{e_{i, j} \\mid 1\\leq i
        < j \\leq n\\}`, where the indices are ordered
        lexicographically.  It is a matrix whose entries are in the
        ring of Laurent polynomials on the given variables.  By
        default, the variables are ``'x'`` and ``'y'``.

        INPUT:

        - ``variables`` -- string (default: ``'x,y'``); a string
          containing the names of the variables, separated by a comma

        OUTPUT: the matrix corresponding to the Lawrence-Krammer-Bigelow
        representation of the braid

        EXAMPLES::

            sage: B = BraidGroup(3)
            sage: b = B([1, 2, 1])
            sage: b.LKB_matrix()
            [             0 -x^4*y + x^3*y         -x^4*y]
            [             0         -x^3*y              0]
            [        -x^2*y  x^3*y - x^2*y              0]
            sage: c = B([2, 1, 2])
            sage: c.LKB_matrix()
            [             0 -x^4*y + x^3*y         -x^4*y]
            [             0         -x^3*y              0]
            [        -x^2*y  x^3*y - x^2*y              0]

        REFERENCES:

        - [Big2003]_
        """
    def TL_matrix(self, drain_size, variab=None, sparse: bool = True):
        """
        Return the matrix representation of the Temperley--Lieb--Jones
        representation of the braid in a certain basis.

        The basis is given by non-intersecting pairings of `(n+d)` points,
        where `n` is the number of strands, `d` is given by ``drain_size``,
        and the pairings satisfy certain rules. See
        :meth:`~sage.groups.braid.BraidGroup_class.TL_basis_with_drain()`
        for details.

        We use the convention that the eigenvalues of the standard generators
        are `1` and `-A^4`, where `A` is a variable of a Laurent
        polynomial ring.

        When `d = n - 2` and the variables are picked appropriately, the
        resulting representation is equivalent to the reduced Burau
        representation.

        INPUT:

        - ``drain_size`` -- integer between 0 and the number of strands
          (both inclusive)

        - ``variab`` -- variable (default: ``None``); the variable in the
          entries of the matrices; if ``None``, then use a default variable
          in `\\ZZ[A,A^{-1}]`

        - ``sparse`` -- boolean (default: ``True``); whether or not the
          result should be given as a sparse matrix

        OUTPUT: the matrix of the TL representation of the braid

        The parameter ``sparse`` can be set to ``False`` if it is
        expected that the resulting matrix will not be sparse. We
        currently make no attempt at guessing this.

        EXAMPLES:

        Let us calculate a few examples for `B_4` with `d = 0`::

            sage: B = BraidGroup(4)
            sage: b = B([1, 2, -3])
            sage: b.TL_matrix(0)
            [1 - A^4   -A^-2]
            [   -A^6       0]
            sage: R.<x> = LaurentPolynomialRing(GF(2))
            sage: b.TL_matrix(0, variab=x)
            [1 + x^4    x^-2]
            [    x^6       0]
            sage: b = B([])
            sage: b.TL_matrix(0)
            [1 0]
            [0 1]

        Test of one of the relations in `B_8`::

            sage: B = BraidGroup(8)
            sage: d = 0
            sage: B([4,5,4]).TL_matrix(d) == B([5,4,5]).TL_matrix(d)
            True

        An element of the kernel of the Burau representation, following
        [Big1999]_::

            sage: B = BraidGroup(6)
            sage: psi1 = B([4, -5, -2, 1])
            sage: psi2 = B([-4, 5, 5, 2, -1, -1])
            sage: w1 = psi1^(-1) * B([3]) * psi1
            sage: w2 = psi2^(-1) * B([3]) * psi2
            sage: (w1 * w2 * w1^(-1) * w2^(-1)).TL_matrix(4)
            [1 0 0 0 0]
            [0 1 0 0 0]
            [0 0 1 0 0]
            [0 0 0 1 0]
            [0 0 0 0 1]

        REFERENCES:

        - [Big1999]_
        - [Jon2005]_
        """
    def links_gould_matrix(self, symbolics: bool = False):
        """
        Return the representation matrix of ``self`` according to the R-matrix
        representation being attached to the quantum superalgebra `\\mathfrak{sl}_q(2|1)`.

        See [MW2012]_, section 3 and references given there.

        INPUT:

        - ``symbolics`` -- boolean (default: ``False``); if set to ``True`` the
          coefficients will be contained in the symbolic ring. Per default they
          are elements of a quotient ring of a three variate Laurent polynomial
          ring.

        OUTPUT: the representation matrix of ``self`` over the ring according
        to the choice of the keyword ``symbolics`` (see the corresponding
        explanation)

        EXAMPLES::

            sage: Hopf = BraidGroup(2)([-1, -1])
            sage: HopfLG = Hopf.links_gould_matrix()
            sage: HopfLG.dimensions()
            (16, 16)
            sage: HopfLG.base_ring()
            Univariate Quotient Polynomial Ring in Yrbar
              over Multivariate Laurent Polynomial Ring in s0r, s1r
              over Integer Ring with modulus Yr^2 + s0r^2*s1r^2 - s0r^2 - s1r^2 + 1
            sage: HopfLGs = Hopf.links_gould_matrix(symbolics=True)                     # needs sage.symbolic
            sage: HopfLGs.base_ring()                                                   # needs sage.symbolic
            Symbolic Ring
        """
    @cached_method
    def links_gould_polynomial(self, varnames=None, use_symbolics: bool = False):
        """
        Return the Links-Gould polynomial of the closure of ``self``.

        See [MW2012]_, section 3 and references given there.

        INPUT:

        - ``varnames`` -- string (default: ``'t0, t1'``)

        OUTPUT: a Laurent polynomial in the given variable names

        EXAMPLES::

            sage: Hopf = BraidGroup(2)([-1, -1])
            sage: Hopf.links_gould_polynomial()
            -1 + t1^-1 + t0^-1 - t0^-1*t1^-1
            sage: _ == Hopf.links_gould_polynomial(use_symbolics=True)
            True
            sage: Hopf.links_gould_polynomial(varnames='a, b')
            -1 + b^-1 + a^-1 - a^-1*b^-1
            sage: _ == Hopf.links_gould_polynomial(varnames='a, b', use_symbolics=True)
            True

        REFERENCES:

        - [MW2012]_
        """
    def tropical_coordinates(self) -> list:
        """
        Return the tropical coordinates of ``self`` in the braid group `B_n`.

        OUTPUT: list of `2n` tropical integers

        EXAMPLES::

            sage: B = BraidGroup(3)
            sage: b = B([1])
            sage: tc = b.tropical_coordinates(); tc
            [1, 0, 0, 2, 0, 1]
            sage: tc[0].parent()
            Tropical semiring over Integer Ring

            sage: b = B([-2, -2, -1, -1, 2, 2, 1, 1])
            sage: b.tropical_coordinates()
            [1, -19, -12, 9, 0, 13]

        REFERENCES:

        - [DW2007]_
        - [Deh2011]_
        """
    def markov_trace(self, variab=None, normalized: bool = True):
        """
        Return the Markov trace of the braid.

        The normalization is so that in the underlying braid group
        representation, the eigenvalues of the standard generators of
        the braid group are `1` and `-A^4`.

        INPUT:

        - ``variab`` -- variable (default: ``None``); the variable in the
          resulting polynomial; if ``None``, then use the variable `A`
          in `\\ZZ[A,A^{-1}]`

        - ``normalized`` -- boolean (default: ``True``); if specified to be
          ``False``, return instead a rescaled Laurent polynomial version of
          the Markov trace

        OUTPUT:

        If ``normalized`` is ``False``, return instead the Markov trace
        of the braid, normalized by a factor of `(A^2+A^{-2})^n`. The
        result is then a Laurent polynomial in ``variab``. Otherwise it
        is a quotient of Laurent polynomials in ``variab``.

        EXAMPLES::

            sage: B = BraidGroup(4)
            sage: b = B([1, 2, -3])
            sage: mt = b.markov_trace(); mt
            A^4/(A^12 + 3*A^8 + 3*A^4 + 1)
            sage: mt.factor()
            A^4 * (A^4 + 1)^-3

        We now give the non-normalized Markov trace::

            sage: mt = b.markov_trace(normalized=False); mt
            A^-4 + 1
            sage: mt.parent()
            Univariate Laurent Polynomial Ring in A over Integer Ring
        """
    def jones_polynomial(self, variab=None, skein_normalization: bool = False):
        '''
        Return the Jones polynomial of the trace closure of the braid.

        The normalization is so that the unknot has Jones polynomial `1`. If
        ``skein_normalization`` is ``True``, the variable of the result is
        replaced by a itself to the power of `4`, so that the result
        agrees with the conventions of [Lic1997]_ (which in particular differs
        slightly from the conventions used otherwise in this class), had
        one used the conventional Kauffman bracket variable notation directly.

        If ``variab`` is ``None`` return a polynomial in the variable `A`
        or `t`, depending on the value ``skein_normalization``. In
        particular, if ``skein_normalization`` is ``False``, return the
        result in terms of the variable `t`, also used in [Lic1997]_.

        INPUT:

        - ``variab`` -- variable (default: ``None``); the variable in the
          resulting polynomial; if unspecified, use either a default variable
          in `\\ZZ[A,A^{-1}]` or the variable `t` in the symbolic ring

        - ``skein_normalization`` -- boolean (default: ``False``); determines
          the variable of the resulting polynomial

        OUTPUT:

        If ``skein_normalization`` if ``False``, this returns an element
        in the symbolic ring as the Jones polynomial of the closure might
        have fractional powers when the closure of the braid is not a knot.
        Otherwise the result is a Laurent polynomial in ``variab``.

        EXAMPLES:

        The unknot::

            sage: B = BraidGroup(9)
            sage: b = B([1, 2, 3, 4, 5, 6, 7, 8])
            sage: b.jones_polynomial()                                                  # needs sage.symbolic
            1

        Two unlinked unknots::

            sage: B = BraidGroup(2)
            sage: b = B([])
            sage: b.jones_polynomial()                                                  # needs sage.symbolic
            -sqrt(t) - 1/sqrt(t)

        The Hopf link::

            sage: B = BraidGroup(2)
            sage: b = B([-1,-1])
            sage: b.jones_polynomial()                                                  # needs sage.symbolic
            -1/sqrt(t) - 1/t^(5/2)

        Different representations of the trefoil and one of its mirror::

            sage: # needs sage.symbolic
            sage: B = BraidGroup(2)
            sage: b = B([-1, -1, -1])
            sage: b.jones_polynomial(skein_normalization=True)
            -A^-16 + A^-12 + A^-4
            sage: b.jones_polynomial()
            1/t + 1/t^3 - 1/t^4
            sage: B = BraidGroup(3)
            sage: b = B([-1, -2, -1, -2])
            sage: b.jones_polynomial(skein_normalization=True)
            -A^-16 + A^-12 + A^-4
            sage: R.<x> = LaurentPolynomialRing(GF(2))
            sage: b.jones_polynomial(skein_normalization=True, variab=x)
            x^-16 + x^-12 + x^-4
            sage: B = BraidGroup(3)
            sage: b = B([1, 2, 1, 2])
            sage: b.jones_polynomial(skein_normalization=True)
            A^4 + A^12 - A^16

        K11n42 (the mirror of the "Kinoshita-Terasaka" knot) and K11n34 (the
        mirror of the "Conway" knot)::

            sage: B = BraidGroup(4)
            sage: b11n42 = B([1, -2, 3, -2, 3, -2, -2, -1, 2, -3, -3, 2, 2])
            sage: b11n34 = B([1, 1, 2, -3, 2, -3, 1, -2, -2, -3, -3])
            sage: bool(b11n42.jones_polynomial() == b11n34.jones_polynomial())          # needs sage.symbolic
            True
        '''
    def annular_khovanov_complex(self, qagrad=None, ring=None):
        """
        Return the annular Khovanov complex of the closure of a braid,
        as defined in [BG2013]_.

        INPUT:

        - ``qagrad`` -- tuple of quantum and annular grading for which to compute
          the chain complex; if not specified all gradings are computed

        - ``ring`` -- (default: ``ZZ``) the coefficient ring

        OUTPUT:

        The annular Khovanov complex of the braid, given as a dictionary whose
        keys are tuples of quantum and annular grading. If ``qagrad`` is
        specified only return the chain complex of that grading.

        EXAMPLES::

            sage: B = BraidGroup(3)
            sage: b = B([1,-2,1,-2])
            sage: C = b.annular_khovanov_complex()
            sage: C
            {(-5, -1): Chain complex with at most 1 nonzero terms over Integer Ring,
             (-3, -3): Chain complex with at most 1 nonzero terms over Integer Ring,
             (-3, -1): Chain complex with at most 2 nonzero terms over Integer Ring,
             (-3, 1): Chain complex with at most 1 nonzero terms over Integer Ring,
             (-1, -1): Chain complex with at most 5 nonzero terms over Integer Ring,
             (-1, 1): Chain complex with at most 2 nonzero terms over Integer Ring,
             (1, -1): Chain complex with at most 2 nonzero terms over Integer Ring,
             (1, 1): Chain complex with at most 5 nonzero terms over Integer Ring,
             (3, -1): Chain complex with at most 1 nonzero terms over Integer Ring,
             (3, 1): Chain complex with at most 2 nonzero terms over Integer Ring,
             (3, 3): Chain complex with at most 1 nonzero terms over Integer Ring,
             (5, 1): Chain complex with at most 1 nonzero terms over Integer Ring}
            sage: C[1,-1].homology()
            {1: Z x Z, 2: 0}

        TESTS::

            sage: C = BraidGroup(2)([]).annular_khovanov_complex()
            sage: {qa: C[qa].homology() for qa in C}
            {(-2, -2): {0: Z}, (0, 0): {0: Z x Z}, (2, 2): {0: Z}}

            sage: BraidGroup(3)([-1]).annular_khovanov_complex((0,1), ZZ).differential()
            {-2: [],
             -1: [0]
             [1]
             [1],
             0: []}
        """
    def annular_khovanov_homology(self, qagrad=None, ring=...):
        """
        Return the annular Khovanov homology of a closure of a braid.

        INPUT:

        - ``qagrad`` -- (optional) tuple of quantum and annular grading
          for which to compute the homology

        - ``ring`` -- (default: ``ZZ``) the coefficient ring

        OUTPUT:

        If ``qagrad`` is ``None``, return a dictionary of homologies in all
        gradings indexed by grading. If ``qagrad`` is specified, return the
        homology of that grading.

        .. NOTE::

            This is a simple wrapper around :meth:`annular_khovanov_complex`
            to compute homology from it.

        EXAMPLES::

            sage: B = BraidGroup(4)
            sage: b = B([1,3,-2])
            sage: b.annular_khovanov_homology()
            {(-3, -4): {0: Z},
             (-3, -2): {-1: Z},
             (-1, -2): {-1: 0, 0: Z x Z x Z, 1: 0},
             (-1, 0): {-1: Z x Z},
             (1, -2): {1: Z x Z},
             (1, 0): {-1: 0, 0: Z x Z x Z x Z, 1: 0, 2: 0},
             (1, 2): {-1: Z},
             (3, 0): {1: Z x Z x Z, 2: 0},
             (3, 2): {-1: 0, 0: Z x Z x Z, 1: 0},
             (5, 0): {2: Z},
             (5, 2): {1: Z x Z},
             (5, 4): {0: Z}}

            sage: B = BraidGroup(2)
            sage: b = B([1,1,1])
            sage: b.annular_khovanov_homology((7,0))
            {2: 0, 3: C2}

        TESTS::

            sage: b = BraidGroup(4)([1,-3])
            sage: b.annular_khovanov_homology((-4,-2))
            {-1: Z}
            sage: b.annular_khovanov_homology((0,2))
            {-1: Z}
        """
    @cached_method
    def left_normal_form(self, algorithm: str = 'libbraiding'):
        """
        Return the left normal form of the braid.

        INPUT:

        - ``algorithm`` -- string (default: ``'artin'``); must be one of the following:

          * ``'artin'`` -- the general method for Artin groups is used
          * ``'libbraiding'`` -- the algorithm from the ``libbraiding`` package

        OUTPUT:

        A tuple of simple generators in the left normal form. The first
        element is a power of `\\Delta`, and the rest are elements of the
        natural section lift from the corresponding symmetric group.

        EXAMPLES::

            sage: B = BraidGroup(6)
            sage: B.one().left_normal_form()
            (1,)
            sage: b = B([-2, 2, -4, -4, 4, -5, -1, 4, -1, 1])
            sage: L1 = b.left_normal_form(); L1
            (s0^-1*s1^-1*s0^-1*s2^-1*s1^-1*s0^-1*s3^-1*s2^-1*s1^-1*s0^-1*s4^-1*s3^-1*s2^-1*s1^-1*s0^-1,
             s0*s2*s1*s0*s3*s2*s1*s0*s4*s3*s2*s1,
             s3)
            sage: L1 == b.left_normal_form()
            True
            sage: B([1]).left_normal_form(algorithm='artin')
            (1, s0)
            sage: B([-3]).left_normal_form(algorithm='artin')
            (s0^-1*s1^-1*s0^-1*s2^-1*s1^-1*s0^-1*s3^-1*s2^-1*s1^-1*s0^-1*s4^-1*s3^-1*s2^-1*s1^-1*s0^-1,
             s0*s1*s2*s3*s4*s0*s1*s2*s3*s1*s2*s0*s1*s0)
            sage: B = BraidGroup(3)
            sage: B([1,2,-1]).left_normal_form()
            (s0^-1*s1^-1*s0^-1, s1*s0, s0*s1)
            sage: B([1,2,1]).left_normal_form()
            (s0*s1*s0,)
        """
    def right_normal_form(self):
        """
        Return the right normal form of the braid.

        A tuple of simple generators in the right normal form. The last
        element is a power of `\\Delta`, and the rest are elements of the
        natural section lift from the corresponding symmetric group.

        EXAMPLES::

            sage: B = BraidGroup(4)
            sage: b = B([1, 2, 1, -2, 3, 1])
            sage: b.right_normal_form()
            (s1*s0, s0*s2, 1)
        """
    def centralizer(self) -> list:
        """
        Return a list of generators of the centralizer of the braid.

        EXAMPLES::

            sage: B = BraidGroup(4)
            sage: b = B([2, 1, 3, 2])
            sage: b.centralizer()
            [s1*s0*s2*s1, s0*s2]
        """
    def super_summit_set(self) -> list:
        """
        Return a list with the super summit set of the braid.

        EXAMPLES::

            sage: B = BraidGroup(3)
            sage: b = B([1, 2, -1, -2, -2, 1])
            sage: b.super_summit_set()
            [s0^-1*s1^-1*s0^-2*s1^2*s0^2,
             (s0^-1*s1^-1*s0^-1)^2*s1^2*s0^3*s1,
             (s0^-1*s1^-1*s0^-1)^2*s1*s0^3*s1^2,
             s0^-1*s1^-1*s0^-2*s1^-1*s0*s1^3*s0]
        """
    def gcd(self, other):
        """
        Return the greatest common divisor of the two braids.

        INPUT:

        - ``other`` -- the other braid with respect with the gcd is computed

        EXAMPLES::

            sage: B = BraidGroup(3)
            sage: b = B([1, 2, -1, -2, -2, 1])
            sage: c = B([1, 2, 1])
            sage: b.gcd(c)
            s0^-1*s1^-1*s0^-2*s1^2*s0
            sage: c.gcd(b)
            s0^-1*s1^-1*s0^-2*s1^2*s0
        """
    def lcm(self, other):
        """
        Return the least common multiple of the two braids.

        INPUT:

        - ``other`` -- the other braid with respect with the lcm is computed

        EXAMPLES::

            sage: B = BraidGroup(3)
            sage: b = B([1, 2, -1, -2, -2, 1])
            sage: c = B([1, 2, 1])
            sage: b.lcm(c)
            (s0*s1)^2*s0
        """
    def conjugating_braid(self, other):
        """
        Return a conjugating braid, if it exists.

        INPUT:

        - ``other`` -- a braid in the same braid group as ``self``

        OUTPUT:

        A conjugating braid. More precisely, if the output is `d`, `o` equals
        ``other``, and `s` equals ``self`` then `o = d^{-1} \\cdot s \\cdot d`.

        EXAMPLES::

            sage: B = BraidGroup(3)
            sage: B.one().conjugating_braid(B.one())
            1
            sage: B.one().conjugating_braid(B.gen(0)) is None
            True
            sage: B.gen(0).conjugating_braid(B.gen(1))
            s1*s0
            sage: B.gen(0).conjugating_braid(B.gen(1).inverse()) is None
            True
            sage: a = B([2, 2, -1, -1])
            sage: b = B([2, 1, 2, 1])
            sage: c = b * a / b
            sage: d1 = a.conjugating_braid(c)
            sage: d1
            s1*s0
            sage: d1 * c / d1 == a
            True
            sage: d1 * a / d1 == c
            False
            sage: l = sage.groups.braid.conjugatingbraid(a,c)                           # needs sage.groups
            sage: d1 == B._element_from_libbraiding(l)                                  # needs sage.groups
            True
            sage: b = B([2, 2, 2, 2, 1])
            sage: c = b * a / b
            sage: d1 = a.conjugating_braid(c)
            sage: len(d1.Tietze())
            7
            sage: d1 * c / d1 == a
            True
            sage: d1 * a / d1 == c
            False
            sage: d1
            s1^2*s0^2*s1^2*s0
            sage: l = sage.groups.braid.conjugatingbraid(a,c)                           # needs sage.groups
            sage: d2 = B._element_from_libbraiding(l)                                   # needs sage.groups
            sage: len(d2.Tietze())                                                      # needs sage.groups
            13
            sage: c.conjugating_braid(b) is None
            True
        """
    def is_conjugated(self, other) -> bool:
        """
        Check if the two braids are conjugated.

        INPUT:

        - ``other`` -- the other braid to check for conjugacy

        EXAMPLES::

            sage: B = BraidGroup(3)
            sage: a = B([2, 2, -1, -1])
            sage: b = B([2, 1, 2, 1])
            sage: c = b * a / b
            sage: c.is_conjugated(a)
            True
            sage: c.is_conjugated(b)
            False
        """
    def pure_conjugating_braid(self, other):
        """
        Return a pure conjugating braid, i.e. a conjugating braid whose
        associated permutation is the identity, if it exists.

        INPUT:

        - ``other`` -- a braid in the same braid group as ``self``

        OUTPUT:

        A pure conjugating braid. More precisely, if the output is `d`, `o`
        equals ``other``, and `s` equals ``self`` then
        `o = d^{-1} \\cdot s \\cdot d`.

        EXAMPLES::

            sage: B = BraidGroup(4)
            sage: B.one().pure_conjugating_braid(B.one())
            1
            sage: B.one().pure_conjugating_braid(B.gen(0)) is None
            True
            sage: B.gen(0).pure_conjugating_braid(B.gen(1)) is None
            True
            sage: B.gen(0).conjugating_braid(B.gen(2).inverse()) is None
            True
            sage: a = B([1, 2, 3])
            sage: b = B([3, 2,])
            sage: c = b ^ 12 * a / b ^ 12
            sage: d1 = a.conjugating_braid(c)
            sage: len(d1.Tietze())
            30
            sage: S = SymmetricGroup(4)
            sage: d1.permutation(W=S)
            (1,3)(2,4)
            sage: d1 * c / d1 == a
            True
            sage: d1 * a / d1 == c
            False
            sage: d2 = a.pure_conjugating_braid(c)
            sage: len(d2.Tietze())
            24
            sage: d2.permutation(W=S)
            ()
            sage: d2 * c / d2 == a
            True
            sage: d2
            (s0*s1*s2^2*s1*s0)^4
            sage: a.conjugating_braid(b) is None
            True
            sage: a.pure_conjugating_braid(b) is None
            True
            sage: a1 = B([1])
            sage: a2 = B([2])
            sage: a1.conjugating_braid(a2)
            s1*s0
            sage: a1.permutation(W=S)
            (1,2)
            sage: a2.permutation(W=S)
            (2,3)
            sage: a1.pure_conjugating_braid(a2) is None
            True
            sage: (a1^2).conjugating_braid(a2^2)
            s1*s0
            sage: (a1^2).pure_conjugating_braid(a2^2) is None
            True
        """
    def ultra_summit_set(self) -> list:
        """
        Return a list with the orbits of the ultra summit set of ``self``.

        EXAMPLES::

            sage: B = BraidGroup(3)
            sage: a = B([2, 2, -1, -1, 2, 2])
            sage: b = B([2, 1, 2, 1])
            sage: b.ultra_summit_set()
            [[s0*s1*s0^2, (s0*s1)^2]]
            sage: a.ultra_summit_set()
            [[(s0^-1*s1^-1*s0^-1)^2*s1^3*s0^2*s1^3,
              (s0^-1*s1^-1*s0^-1)^2*s1^2*s0^2*s1^4,
              (s0^-1*s1^-1*s0^-1)^2*s1*s0^2*s1^5,
              s0^-1*s1^-1*s0^-2*s1^5*s0,
              (s0^-1*s1^-1*s0^-1)^2*s1^5*s0^2*s1,
              (s0^-1*s1^-1*s0^-1)^2*s1^4*s0^2*s1^2],
             [s0^-1*s1^-1*s0^-2*s1^-1*s0^2*s1^2*s0^3,
              s0^-1*s1^-1*s0^-2*s1^-1*s0*s1^2*s0^4,
              s0^-1*s1^-1*s0^-2*s1*s0^5,
              (s0^-1*s1^-1*s0^-1)^2*s1*s0^6*s1,
              s0^-1*s1^-1*s0^-2*s1^-1*s0^4*s1^2*s0,
              s0^-1*s1^-1*s0^-2*s1^-1*s0^3*s1^2*s0^2]]
        """
    def thurston_type(self) -> str:
        """
        Return the thurston_type of ``self``.

        OUTPUT: one of ``'reducible'``, ``'periodic'`` or ``'pseudo-anosov'``

        EXAMPLES::

            sage: B = BraidGroup(3)
            sage: b = B([1, 2, -1])
            sage: b.thurston_type()
            'reducible'
            sage: a = B([2, 2, -1, -1, 2, 2])
            sage: a.thurston_type()
            'pseudo-anosov'
            sage: c = B([2, 1, 2, 1])
            sage: c.thurston_type()
            'periodic'
        """
    def is_reducible(self) -> bool:
        """
        Check whether the braid is reducible.

        EXAMPLES::

            sage: B = BraidGroup(3)
            sage: b = B([1, 2, -1])
            sage: b.is_reducible()
            True
            sage: a = B([2, 2, -1, -1, 2, 2])
            sage: a.is_reducible()
            False
        """
    def is_periodic(self) -> bool:
        """
        Check whether the braid is periodic.

        EXAMPLES::

            sage: B = BraidGroup(3)
            sage: a = B([2, 2, -1, -1, 2, 2])
            sage: b = B([2, 1, 2, 1])
            sage: a.is_periodic()
            False
            sage: b.is_periodic()
            True
        """
    def is_pseudoanosov(self) -> bool:
        """
        Check if the braid is pseudo-Anosov.

        EXAMPLES::

            sage: B = BraidGroup(3)
            sage: a = B([2, 2, -1, -1, 2, 2])
            sage: b = B([2, 1, 2, 1])
            sage: a.is_pseudoanosov()
            True
            sage: b.is_pseudoanosov()
            False
        """
    def rigidity(self):
        """
        Return the rigidity of ``self``.

        EXAMPLES::

            sage: B = BraidGroup(3)
            sage: b = B([2, 1, 2, 1])
            sage: a = B([2, 2, -1, -1, 2, 2])
            sage: a.rigidity()
            6
            sage: b.rigidity()
            0
        """
    def sliding_circuits(self) -> list:
        """
        Return the sliding circuits of the braid.

        OUTPUT: list of sliding circuits. Each sliding circuit is itself
        a list of braids.

        EXAMPLES::

            sage: B = BraidGroup(3)
            sage: a = B([2, 2, -1, -1, 2, 2])
            sage: a.sliding_circuits()
            [[(s0^-1*s1^-1*s0^-1)^2*s1^3*s0^2*s1^3],
             [s0^-1*s1^-1*s0^-2*s1^-1*s0^2*s1^2*s0^3],
             [s0^-1*s1^-1*s0^-2*s1^-1*s0^3*s1^2*s0^2],
             [(s0^-1*s1^-1*s0^-1)^2*s1^4*s0^2*s1^2],
             [(s0^-1*s1^-1*s0^-1)^2*s1^2*s0^2*s1^4],
             [s0^-1*s1^-1*s0^-2*s1^-1*s0*s1^2*s0^4],
             [(s0^-1*s1^-1*s0^-1)^2*s1^5*s0^2*s1],
             [s0^-1*s1^-1*s0^-2*s1^-1*s0^4*s1^2*s0],
             [(s0^-1*s1^-1*s0^-1)^2*s1*s0^2*s1^5],
             [s0^-1*s1^-1*s0^-2*s1*s0^5],
             [(s0^-1*s1^-1*s0^-1)^2*s1*s0^6*s1],
             [s0^-1*s1^-1*s0^-2*s1^5*s0]]
            sage: b = B([2, 1, 2, 1])
            sage: b.sliding_circuits()
            [[s0*s1*s0^2, (s0*s1)^2]]
        """
    def mirror_image(self):
        """
        Return the image of ``self`` under the mirror involution (see
        :meth:`BraidGroup_class.mirror_involution`). The link closure of
        it is mirrored to the closure of ``self`` (see the example below
        of a positive amphicheiral knot).

        EXAMPLES::

            sage: B5 = BraidGroup(5)
            sage: b  = B5((-1, 2, -3, -1, -3, 4, 2, -3, 2, 4, 2, -3)) # closure K12a_427
            sage: bm = b.mirror_image(); bm
            s0*s1^-1*s2*s0*s2*s3^-1*s1^-1*s2*s1^-1*s3^-1*s1^-1*s2
            sage: bm.is_conjugated(b)
            True
            sage: bm.is_conjugated(~b)
            False
        """
    def reverse(self):
        """
        Return the reverse of ``self`` obtained by reversing the order of the
        generators in its word. This defines an anti-involution on the braid
        group. The link closure of it has the reversed orientation (see the
        example below of a non reversible knot).

        EXAMPLES::

            sage: b  = BraidGroup(3)((1, 1, -2, 1, -2, 1, -2, -2))  # closure K8_17
            sage: br = b.reverse(); br
            s1^-1*(s1^-1*s0)^3*s0
            sage: br.is_conjugated(b)
            False
        """
    def deformed_burau_matrix(self, variab: str = 'q'):
        """
        Return the deformed Burau matrix of the braid.

        INPUT:

        - ``variab`` -- variable (default: ``q``); the variable in the
          resulting laurent polynomial, which is the base ring for the
          free algebra constructed

        OUTPUT: a matrix with elements in the free algebra ``self._algebra``

        EXAMPLES::

            sage: B = BraidGroup(4)
            sage: b = B([1, 2, -3, -2, 3, 1])
            sage: db = b.deformed_burau_matrix(); db
            [                                ap_0*ap_5 ... bp_0*ap_1*cm_3*bp_4]
            ...
            [                           bm_2*bm_3*cp_5 ...      bm_2*am_3*bp_4]

        We check how this relates to the nondeformed Burau matrix::

            sage: def subs_gen(gen, q):
            ....:     gen_str = str(gen)
            ....:     v = q if 'p' in gen_str else 1/q
            ....:     if 'b' in gen_str:
            ....:         return v
            ....:     elif 'a' in gen_str:
            ....:         return 1 - v
            ....:     else:
            ....:         return 1
            sage: db_base = db.parent().base_ring()
            sage: q = db_base.base_ring().gen()
            sage: db_simp = db.subs({gen: subs_gen(gen, q)
            ....:                    for gen in db_base.gens()})
            sage: db_simp
            [ (1-2*q+q^2)      (q-q^2)  (q-q^2+q^3)    (q^2-q^3)]
            [       (1-q)            q            0            0]
            [           0            0        (1-q)            q]
            [      (q^-2)            0 -(q^-2-q^-1)    -(q^-1-1)]
            sage: burau = b.burau_matrix(); burau
            [1 - 2*t + t^2       t - t^2 t - t^2 + t^3     t^2 - t^3]
            [        1 - t             t             0             0]
            [            0             0         1 - t             t]
            [         t^-2             0  -t^-2 + t^-1     -t^-1 + 1]
            sage: t = burau.parent().base_ring().gen()
            sage: burau.subs({t:q}).change_ring(db_base) == db_simp
            True
        """
    def colored_jones_polynomial(self, N, variab=None, try_inverse: bool = True):
        """
        Return the colored Jones polynomial of the trace closure of the braid.

        INPUT:

        - ``N`` -- integer; the number of colors
        - ``variab`` -- (default: `q`) the variable in the resulting
          Laurent polynomial
        - ``try_inverse`` -- boolean (default: ``True``); if ``True``,
          attempt a faster calculation by using the inverse of the braid

        ALGORITHM:

        The algorithm used is described in [HL2018]_. We follow their
        notation, but work in a suitable free algebra over a Laurent
        polynomial ring in one variable to simplify bookkeeping.

        EXAMPLES::

            sage: trefoil = BraidGroup(2)([1,1,1])
            sage: trefoil.colored_jones_polynomial(2)
            q + q^3 - q^4
            sage: trefoil.colored_jones_polynomial(4)
            q^3 + q^7 - q^10 + q^11 - q^13 - q^14 + q^15 - q^17
             + q^19 + q^20 - q^21
            sage: trefoil.inverse().colored_jones_polynomial(4)
            -q^-21 + q^-20 + q^-19 - q^-17 + q^-15 - q^-14 - q^-13
             + q^-11 - q^-10 + q^-7 + q^-3

            sage: figure_eight = BraidGroup(3)([-1, 2, -1, 2])
            sage: figure_eight.colored_jones_polynomial(2)
            q^-2 - q^-1 + 1 - q + q^2
            sage: figure_eight.colored_jones_polynomial(3, 'Q')
            Q^-6 - Q^-5 - Q^-4 + 2*Q^-3 - Q^-2 - Q^-1 + 3 - Q - Q^2
             + 2*Q^3 - Q^4 - Q^5 + Q^6
        """
    def super_summit_set_element(self):
        """
        Return an element of the braid's super summit set and the conjugating
        braid.

        EXAMPLES::

            sage: B = BraidGroup(4)
            sage: b = B([1, 2, 1, 2, 3, -1, 2, 1, 3])
            sage: b.super_summit_set_element()
            (s0*s2*s0*s1*s2*s1*s0, s0^-1*s1^-1*s0^-1*s2^-1*s1^-1*s0^-1*s1*s0*s2*s1*s0)
        """
    def ultra_summit_set_element(self):
        """
        Return an element of the braid's ultra summit set and the conjugating
        braid.

        EXAMPLES::

            sage: B = BraidGroup(4)
            sage: b = B([1, 2, 1, 2, 3, -1, 2, -1, 3])
            sage: b.ultra_summit_set_element()
            (s0*s1*s0*s2*s1, s0^-1*s1^-1*s0^-1*s2^-1*s1^-1*s0^-1*s1*s2*s1^2*s0)
        """
    def sliding_circuits_element(self) -> tuple:
        """
        Return an element of the braid's sliding circuits, and the conjugating
        braid.

        EXAMPLES::

            sage: B = BraidGroup(4)
            sage: b = B([1, 2, 1, 2, 3, -1, 2, -1, 3])
            sage: b.sliding_circuits_element()
            (s0*s1*s0*s2*s1, s0^2*s1*s2)
        """
    def trajectory(self) -> list:
        """
        Return the braid's trajectory.

        EXAMPLES::

            sage: B = BraidGroup(4)
            sage: b = B([1, 2, 1, 2, 3, -1, 2, -1, 3])
            sage: b.trajectory()
            [s0^-1*s1^-1*s0^-1*s2^-1*s1^-1*s2*s0*s1*s2*s1*s0^2*s1*s2^2,
             s0*s1*s2^3,
             s0*s1*s2*s1^2,
             s0*s1*s0*s2*s1]
        """
    def cyclic_slidings(self) -> list:
        """
        Return the braid's cyclic slidings.

        OUTPUT: The braid's cyclic slidings. Each cyclic sliding is a list of braids.

        EXAMPLES::

            sage: B = BraidGroup(4)
            sage: b = B([1, 2, 1, 2, 3, -1, 2, 1])
            sage: b.cyclic_slidings()
            [[s0*s2*s1*s0*s1*s2, s0*s1*s2*s1*s0^2, s1*s0*s2^2*s1*s0],
             [s0*s1*s2*s1^2*s0, s0*s1*s2*s1*s0*s2, s1*s0*s2*s0*s1*s2]]
        """

class RightQuantumWord:
    """
    A right quantum word as in Definition 4.1 of [HL2018]_.

    INPUT:

    - ``words`` -- an element in a suitable free algebra over a Laurent
      polynomial ring in one variable; this input does not need to be in
      reduced form, but the monomials for the input can come in any order

    EXAMPLES::

        sage: from sage.groups.braid import RightQuantumWord
        sage: fig_8 = BraidGroup(3)([-1, 2, -1, 2])
        sage: (
        ....:  bp_1, cp_1, ap_1,
        ....:  bp_3, cp_3, ap_3,
        ....:  bm_0, cm_0, am_0,
        ....:  bm_2, cm_2, am_2
        ....: ) = fig_8.deformed_burau_matrix().parent().base_ring().gens()
        sage: q = bp_1.base_ring().gen()
        sage: RightQuantumWord(ap_1*cp_1 + q**3*bm_2*bp_1*am_0*cm_0)
        The right quantum word represented by
         q*cp_1*ap_1 + q^2*bp_1*cm_0*am_0*bm_2
         reduced from ap_1*cp_1 + q^3*bm_2*bp_1*am_0*cm_0
    """
    q: Incomplete
    iq: Incomplete
    R: Incomplete
    def __init__(self, words) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: from sage.groups.braid import RightQuantumWord
            sage: fig_8 = BraidGroup(3)([-1, 2, -1, 2])
            sage: (
            ....:  bp_1, cp_1, ap_1,
            ....:  bp_3, cp_3, ap_3,
            ....:  bm_0, cm_0, am_0,
            ....:  bm_2, cm_2, am_2
            ....: ) = fig_8.deformed_burau_matrix().parent().base_ring().gens()
            sage: q = bp_1.base_ring().gen()
            sage: Q = RightQuantumWord(ap_1*cp_1 + q**3*bm_2*bp_1*am_0*cm_0)
            sage: TestSuite(Q).run(skip='_test_pickling')
        """
    @lazy_attribute
    def tuples(self):
        """
        Get a representation of the right quantum word as a ``dict``, with
        keys monomials in the free algebra represented as tuples and
        values in elements the Laurent polynomial ring in one variable.

        This is in the reduced form as outlined in Definition 4.1
        of [HL2018]_.

        OUTPUT: a dict of tuples of ints corresponding to the exponents in the
        generators with values in the algebra's base ring

        EXAMPLES::

            sage: from sage.groups.braid import RightQuantumWord
            sage: fig_8 = BraidGroup(3)([-1, 2, -1, 2])
            sage: (
            ....:  bp_1, cp_1, ap_1,
            ....:  bp_3, cp_3, ap_3,
            ....:  bm_0, cm_0, am_0,
            ....:  bm_2, cm_2, am_2
            ....: ) = fig_8.deformed_burau_matrix().parent().base_ring().gens()
            sage: q = bp_1.base_ring().gen()
            sage: qw = RightQuantumWord(ap_1*cp_1 +
            ....:                       q**3*bm_2*bp_1*am_0*cm_0)
            sage: for key, value in qw.tuples.items():
            ....:     print(key, value)
            ....:
            (0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0) q
            (1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0) q^2
        """
    def reduced_word(self):
        """
        Return the (reduced) right quantum word.

        OUTPUT: an element in the free algebra

        EXAMPLES::

            sage: from sage.groups.braid import RightQuantumWord
            sage: fig_8 = BraidGroup(3)([-1, 2, -1, 2])
            sage: (
            ....:  bp_1, cp_1, ap_1,
            ....:  bp_3, cp_3, ap_3,
            ....:  bm_0, cm_0, am_0,
            ....:  bm_2, cm_2, am_2
            ....: ) = fig_8.deformed_burau_matrix().parent().base_ring().gens()
            sage: q = bp_1.base_ring().gen()
            sage: qw = RightQuantumWord(ap_1*cp_1 +
            ....:                            q**3*bm_2*bp_1*am_0*cm_0)
            sage: qw.reduced_word()
            q*cp_1*ap_1 + q^2*bp_1*cm_0*am_0*bm_2

        TESTS:

        Testing the equations (4.1) and (4.2) in [HL2018]_::

            sage: RightQuantumWord(ap_3*bp_3).reduced_word()
            bp_3*ap_3
            sage: RightQuantumWord(ap_3*cp_3).reduced_word()
            q*cp_3*ap_3
            sage: RightQuantumWord(cp_3*bp_3).reduced_word()
            (q^-2)*bp_3*cp_3
            sage: RightQuantumWord(am_2*bm_2).reduced_word()
            q^2*bm_2*am_2
            sage: RightQuantumWord(am_2*cm_2).reduced_word()
            (q^-1)*cm_2*am_2
            sage: RightQuantumWord(cm_2*bm_2).reduced_word()
            q^2*bm_2*cm_2

        .. TODO::

            Parallelize this function, calculating all summands in the sum
            in parallel.
        """
    def eps(self, N):
        """
        Evaluate the map `\\mathcal{E}_N` for a braid.

        INPUT:

        - ``N`` -- integer; the number of colors

        EXAMPLES::

            sage: from sage.groups.braid import RightQuantumWord
            sage: B = BraidGroup(3)
            sage: b = B([1,-2,1,2])
            sage: db = b.deformed_burau_matrix()
            sage: q = db.parent().base_ring().base_ring().gen()
            sage: (bp_0, cp_0, ap_0,
            ....:  bp_2, cp_2, ap_2,
            ....:  bp_3, cp_3, ap_3,
            ....:  bm_1, cm_1, am_1) = db.parent().base_ring().gens()
            sage: rqw = RightQuantumWord(
            ....:    q^3*bp_2*bp_0*ap_0 + q*ap_3*bm_1*am_1*bp_0)
            sage: rqw.eps(3)
            -q^-1 + 2*q - q^5
            sage: rqw.eps(2)
            -1 + 2*q - q^2 + q^3 - q^4

        TESTS::

            sage: rqw.eps(1)
            0

        .. TODO::

            Parallelize this function, calculating all summands in the sum
            in parallel.
        """

class BraidGroup_class(FiniteTypeArtinGroup):
    """
    The braid group on `n` strands.

    EXAMPLES::

        sage: B1 = BraidGroup(5)
        sage: B1
        Braid group on 5 strands
        sage: B2 = BraidGroup(3)
        sage: B1 == B2
        False
        sage: B2 is BraidGroup(3)
        True
    """
    Element = Braid
    def __init__(self, names) -> None:
        """
        Python constructor.

        INPUT:

        - ``names`` -- tuple of strings; the names of the generators

        TESTS::

            sage: B1 = BraidGroup(5) # indirect doctest
            sage: B1
            Braid group on 5 strands
            sage: TestSuite(B1).run()
            sage: B1.category()
            Category of infinite groups

        Check that :issue:`14081` is fixed::

            sage: BraidGroup(2)
            Braid group on 2 strands
            sage: BraidGroup(('a',))
            Braid group on 2 strands

        Check that :issue:`15505` is fixed::

            sage: B = BraidGroup(4)
            sage: B.relations()
            (s0*s1*s0*s1^-1*s0^-1*s1^-1, s0*s2*s0^-1*s2^-1, s1*s2*s1*s2^-1*s1^-1*s2^-1)
            sage: B = BraidGroup('a,b,c,d,e,f')
            sage: B.relations()
            (a*b*a*b^-1*a^-1*b^-1,
             a*c*a^-1*c^-1,
             a*d*a^-1*d^-1,
             a*e*a^-1*e^-1,
             a*f*a^-1*f^-1,
             b*c*b*c^-1*b^-1*c^-1,
             b*d*b^-1*d^-1,
             b*e*b^-1*e^-1,
             b*f*b^-1*f^-1,
             c*d*c*d^-1*c^-1*d^-1,
             c*e*c^-1*e^-1,
             c*f*c^-1*f^-1,
             d*e*d*e^-1*d^-1*e^-1,
             d*f*d^-1*f^-1,
             e*f*e*f^-1*e^-1*f^-1)

            sage: BraidGroup([])
            Traceback (most recent call last):
            ...
            ValueError: the number of strands must be at least 2
        """
    def __reduce__(self) -> tuple:
        """
        TESTS::

            sage: B = BraidGroup(3)
            sage: B.__reduce__()
            (<class 'sage.groups.braid.BraidGroup_class'>, (('s0', 's1'),))
            sage: B = BraidGroup(3, 'sigma')
            sage: B.__reduce__()
            (<class 'sage.groups.braid.BraidGroup_class'>, (('sigma0', 'sigma1'),))
        """
    def cardinality(self):
        """
        Return the number of group elements.

        OUTPUT: Infinity

        TESTS::

            sage: B1 = BraidGroup(5)
            sage: B1.cardinality()
            +Infinity
        """
    order = cardinality
    def as_permutation_group(self) -> None:
        """
        Return an isomorphic permutation group.

        OUTPUT: this raises a :exc:`ValueError` error since braid groups
        are infinite

        TESTS::

            sage: B = BraidGroup(4, 'g')
            sage: B.as_permutation_group()
            Traceback (most recent call last):
            ...
            ValueError: the group is infinite
        """
    def strands(self):
        """
        Return the number of strands.

        OUTPUT: integer

        EXAMPLES::

            sage: B = BraidGroup(4)
            sage: B.strands()
            4
        """
    def some_elements(self) -> list:
        """
        Return a list of some elements of the braid group.

        This is used both for illustration and testing purposes.

        EXAMPLES::

            sage: B = BraidGroup(3)
            sage: B.some_elements()
            [s0, s0*s1, (s0*s1)^3]
        """
    def dimension_of_TL_space(self, drain_size):
        """
        Return the dimension of a particular Temperley--Lieb representation
        summand of ``self``.

        Following the notation of :meth:`TL_basis_with_drain`, the summand
        is the one corresponding to the number of drains being fixed to be
        ``drain_size``.

        INPUT:

        - ``drain_size`` -- integer between 0 and the number of strands
          (both inclusive)

        EXAMPLES:

        Calculation of the dimension of the representation of `B_8`
        corresponding to having `2` drains::

            sage: B = BraidGroup(8)
            sage: B.dimension_of_TL_space(2)
            28

        The direct sum of endomorphism spaces of these vector spaces make up
        the entire Temperley--Lieb algebra::

            sage: import sage.combinat.diagram_algebras as da                           # needs sage.combinat
            sage: B = BraidGroup(6)
            sage: dimensions = [B.dimension_of_TL_space(d)**2 for d in [0, 2, 4, 6]]
            sage: total_dim = sum(dimensions)
            sage: total_dim == len(list(da.temperley_lieb_diagrams(6)))         # long time, needs sage.combinat
            True
        """
    def TL_basis_with_drain(self, drain_size):
        """
        Return a basis of a summand of the Temperley--Lieb--Jones
        representation of ``self``.

        The basis elements are given by non-intersecting pairings of `n+d`
        points in a square with `n` points marked 'on the top' and `d` points
        'on the bottom' so that every bottom point is paired with a top point.
        Here, `n` is the number of strands of the braid group, and `d` is
        specified by ``drain_size``.

        A basis element is specified as a list of integers obtained by
        considering the pairings as obtained as the 'highest term' of
        trivalent trees marked by Jones--Wenzl projectors (see e.g. [Wan2010]_).
        In practice, this is a list of nonnegative integers whose first
        element is ``drain_size``, whose last element is `0`, and satisfying
        that consecutive integers have difference `1`. Moreover, the length
        of each basis element is `n + 1`.

        Given these rules, the list of lists is constructed recursively
        in the natural way.

        INPUT:

        - ``drain_size`` -- integer between 0 and the number of strands
          (both inclusive)

        OUTPUT: list of basis elements, each of which is a list of integers

        EXAMPLES:

        We calculate the basis for the appropriate vector space for `B_5` when
        `d = 3`::

            sage: B = BraidGroup(5)
            sage: B.TL_basis_with_drain(3)
            [[3, 4, 3, 2, 1, 0],
             [3, 2, 3, 2, 1, 0],
             [3, 2, 1, 2, 1, 0],
             [3, 2, 1, 0, 1, 0]]

        The number of basis elements hopefully corresponds to the general
        formula for the dimension of the representation spaces::

            sage: B = BraidGroup(10)
            sage: d = 2
            sage: B.dimension_of_TL_space(d) == len(B.TL_basis_with_drain(d))
            True
        """
    def TL_representation(self, drain_size, variab=None):
        """
        Return representation matrices of the Temperley--Lieb--Jones
        representation of standard braid group generators and inverses
        of ``self``.

        The basis is given by non-intersecting pairings of `(n+d)` points,
        where `n` is the number of strands, and `d` is given by
        ``drain_size``, and the pairings satisfy certain rules. See
        :meth:`TL_basis_with_drain()` for details. This basis has
        the useful property that all resulting entries can be regarded as
        Laurent polynomials.

        We use the convention that the eigenvalues of the standard generators
        are `1` and `-A^4`, where `A` is the generator of the Laurent
        polynomial ring.

        When `d = n - 2` and the variables are picked appropriately, the
        resulting representation is equivalent to the reduced Burau
        representation. When `d = n`, the resulting representation is
        trivial and 1-dimensional.

        INPUT:

        - ``drain_size`` -- integer between 0 and the number of strands
          (both inclusive)
        - ``variab`` -- variable (default: ``None``); the variable in the
          entries of the matrices; if ``None``, then use a default variable
          in `\\ZZ[A,A^{-1}]`

        OUTPUT: list of matrices corresponding to the representations of each
        of the standard generators and their inverses

        EXAMPLES::

            sage: B = BraidGroup(4)
            sage: B.TL_representation(0)
            [(
              [   1    0]  [    1     0]
              [ A^2 -A^4], [ A^-2 -A^-4]
            ),
             (
              [-A^4  A^2]  [-A^-4  A^-2]
              [   0    1], [    0     1]
            ),
             (
              [   1    0]  [    1     0]
              [ A^2 -A^4], [ A^-2 -A^-4]
            )]
            sage: R.<A> = LaurentPolynomialRing(GF(2))
            sage: B.TL_representation(0, variab=A)
            [(
              [  1   0]  [   1    0]
              [A^2 A^4], [A^-2 A^-4]
            ),
             (
              [A^4 A^2]  [A^-4 A^-2]
              [  0   1], [   0    1]
            ),
             (
              [  1   0]  [   1    0]
              [A^2 A^4], [A^-2 A^-4]
            )]
            sage: B = BraidGroup(8)
            sage: B.TL_representation(8)
            [([1], [1]),
             ([1], [1]),
             ([1], [1]),
             ([1], [1]),
             ([1], [1]),
             ([1], [1]),
             ([1], [1])]
        """
    def mapping_class_action(self, F):
        """
        Return the action of ``self`` in the free group F as mapping class
        group.

        This action corresponds to the action of the braid over the
        punctured disk, whose fundamental group is the free group on
        as many generators as strands.

        In Sage, this action is the result of multiplying a free group
        element with a braid. So you generally do not have to
        construct this action yourself.

        OUTPUT: a :class:`MappingClassGroupAction`

        EXAMPLES::

            sage: B = BraidGroup(3)
            sage: B.inject_variables()
            Defining s0, s1
            sage: F.<a,b,c> = FreeGroup(3)
            sage: A = B.mapping_class_action(F)
            sage: A(a,s0)
            a*b*a^-1
            sage: a * s0    # simpler notation
            a*b*a^-1
        """
    def mirror_involution(self):
        """
        Return the mirror involution of ``self``.

        This automorphism maps a braid to another one by replacing
        each generator in its word by the inverse. In general this is
        different from the inverse of the braid since the order of the
        generators in the word is not reversed.

        EXAMPLES::

            sage: B = BraidGroup(4)
            sage: mirr = B.mirror_involution()
            sage: b = B((1,-2,-1,3,2,1))
            sage: bm = mirr(b); bm
            s0^-1*s1*s0*s2^-1*s1^-1*s0^-1
            sage: bm == ~b
            False
            sage: bm.is_conjugated(b)
            False
            sage: bm.is_conjugated(~b)
            True
        """
    def presentation_two_generators(self, isomorphisms: bool = False):
        """
        Construct a finitely presented group isomorphic to ``self`` with only two generators.

        INPUT:

        - ``isomorphism`` -- boolean (default: ``False``); if ``True``, then an isomorphism
          from ``self`` and the isomorphic group and its inverse is also returned

        EXAMPLES::

            sage: B = BraidGroup(3)
            sage: B.presentation_two_generators()
            Finitely presented group < x0, x1 | x1^3*x0^-2 >
            sage: B = BraidGroup(4)
            sage: G, hom1, hom2 = B.presentation_two_generators(isomorphisms=True)
            sage: G
            Finitely presented group < x0, x1 | x1^4*x0^-3, x0*x1*x0*x1^-2*x0^-1*x1^3*x0^-1*x1^-2 >
            sage: hom1(B.gen(0))
            x0*x1^-1
            sage: hom1(B.gen(1))
            x1*x0*x1^-2
            sage: hom1(B.gen(2))
            x1^2*x0*x1^-3
            sage: all(hom2(hom1(a)) == a for a in B.gens())
            True
            sage: all(hom2(a) == B.one() for a in G.relations())
            True
        """
    def epimorphisms(self, H) -> list:
        """
        Return the epimorphisms from ``self`` to ``H``, up to automorphism of `H` passing
        through the :meth:`two generator presentation
        <presentation_two_generators>` of ``self``.

        INPUT:

        - ``H`` -- another group

        EXAMPLES::

            sage: B = BraidGroup(5)
            sage: B.epimorphisms(SymmetricGroup(5))
            [Generic morphism:
            From: Braid group on 5 strands
            To:   Symmetric group of order 5! as a permutation group
            Defn: s0 |--> (1,5)
                  s1 |--> (4,5)
                  s2 |--> (3,4)
                  s3 |--> (2,3)]

        ALGORITHM:

        Uses libgap's GQuotients function.
        """

def BraidGroup(n=None, names: str = 's'):
    """
    Construct a Braid Group.

    INPUT:

    - ``n`` -- integer or ``None`` (default). The number of
      strands. If not specified the ``names`` are counted and the
      group is assumed to have one more strand than generators.

    - ``names`` -- string or list/tuple/iterable of strings (default:
      ``'x'``); the generator names or name prefix

    EXAMPLES::

        sage: B.<a,b> = BraidGroup();  B
        Braid group on 3 strands
        sage: H = BraidGroup('a, b')
        sage: B is H
        True
        sage: BraidGroup(3)
        Braid group on 3 strands

    The entry can be either a string with the names of the generators,
    or the number of generators and the prefix of the names to be
    given. The default prefix is ``'s'`` ::

        sage: B = BraidGroup(3); B.generators()
        (s0, s1)
        sage: BraidGroup(3, 'g').generators()
        (g0, g1)

    Since the word problem for the braid groups is solvable, their Cayley graph
    can be locally obtained as follows (see :issue:`16059`)::

        sage: def ball(group, radius):
        ....:     ret = set()
        ....:     ret.add(group.one())
        ....:     for length in range(1, radius):
        ....:         for w in Words(alphabet=group.gens(), length=length):
        ....:              ret.add(prod(w))
        ....:     return ret
        sage: B = BraidGroup(4)
        sage: GB = B.cayley_graph(elements=ball(B, 4), generators=B.gens()); GB         # needs sage.combinat sage.graphs
        Digraph on 31 vertices

    Since the braid group has nontrivial relations, this graph contains less
    vertices than the one associated to the free group (which is a tree)::

        sage: F = FreeGroup(3)
        sage: GF = F.cayley_graph(elements=ball(F, 4), generators=F.gens()); GF         # needs sage.combinat sage.graphs
        Digraph on 40 vertices

    TESTS::

        sage: G1 = BraidGroup(3, 'a,b')
        sage: G2 = BraidGroup('a,b')
        sage: G3.<a,b> = BraidGroup()
        sage: G1 is G2, G2 is G3
        (True, True)
    """

class MappingClassGroupAction(Action):
    """
    The right action of the braid group the free group as the mapping
    class group of the punctured disk.

    That is, this action is the action of the braid over the punctured
    disk, whose fundamental group is the free group on as many
    generators as strands.

    This action is defined as follows:

    .. MATH::

        x_j \\cdot \\sigma_i=\\begin{cases}
        x_{j}\\cdot x_{j+1}\\cdot {x_j}^{-1} & \\text{if $i=j$} \\\\\n        x_{j-1} & \\text{if $i=j-1$} \\\\\n        x_{j} & \\text{otherwise}
        \\end{cases},

    where `\\sigma_i` are the generators of the braid group on `n`
    strands, and `x_j` the generators of the free group of rank `n`.

    You should left multiplication of the free group element by the
    braid to compute the action. Alternatively, use the
    :meth:`~sage.groups.braid.BraidGroup_class.mapping_class_action`
    method of the braid group to construct this action.

    EXAMPLES::

        sage: B.<s0,s1,s2> = BraidGroup(4)
        sage: F.<x0,x1,x2,x3> = FreeGroup(4)
        sage: x0 * s1
        x0
        sage: x1 * s1
        x1*x2*x1^-1
        sage: x1^-1 * s1
        x1*x2^-1*x1^-1

        sage: A = B.mapping_class_action(F)
        sage: A
        Right action by Braid group on 4 strands on Free Group
        on generators {x0, x1, x2, x3}
        sage: A(x0, s1)
        x0
        sage: A(x1, s1)
        x1*x2*x1^-1
        sage: A(x1^-1, s1)
        x1*x2^-1*x1^-1
    """
    def __init__(self, G, M) -> None:
        """
        TESTS::

            sage: B = BraidGroup(3)
            sage: G = FreeGroup('a, b, c')
            sage: B.mapping_class_action(G) # indirect doctest
            Right action by Braid group on 3 strands on Free Group
            on generators {a, b, c}
        """
