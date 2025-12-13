from sage.categories.action import Action as Action
from sage.combinat.permutation import Permutation as Permutation
from sage.groups.group import FiniteGroup as FiniteGroup
from sage.groups.semimonomial_transformations.semimonomial_transformation import SemimonomialTransformation as SemimonomialTransformation
from sage.rings.integer import Integer as Integer
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class SemimonomialTransformationGroup(FiniteGroup, UniqueRepresentation):
    """
    A semimonomial transformation group over a ring.

    The semimonomial transformation group of degree `n` over a ring `R` is
    the semidirect product of the monomial transformation group of degree `n`
    (also known as the complete monomial group over the group of units
    `R^{\\times}` of `R`) and the group of ring automorphisms.

    The multiplication of two elements `(\\phi, \\pi, \\alpha)(\\psi, \\sigma, \\beta)`
    with

        - `\\phi, \\psi \\in  {R^{\\times}}^n`

        - `\\pi, \\sigma \\in S_n` (with the multiplication `\\pi\\sigma`
          done from left to right (like in GAP) --
          that is, `(\\pi\\sigma)(i) = \\sigma(\\pi(i))` for all `i`.)

        - `\\alpha, \\beta \\in Aut(R)`

    is defined by

    .. MATH::

        (\\phi, \\pi, \\alpha)(\\psi, \\sigma, \\beta) =
        (\\phi \\cdot \\psi^{\\pi, \\alpha}, \\pi\\sigma, \\alpha \\circ \\beta)

    where
    `\\psi^{\\pi, \\alpha} = (\\alpha(\\psi_{\\pi(1)-1}), \\ldots, \\alpha(\\psi_{\\pi(n)-1}))`
    and the multiplication of vectors is defined elementwisely. (The indexing
    of vectors is `0`-based here, so `\\psi = (\\psi_0, \\psi_1, \\ldots, \\psi_{n-1})`.)

    .. TODO::

        Up to now, this group is only implemented for finite fields because of
        the limited support of automorphisms for arbitrary rings.

    EXAMPLES::

        sage: F.<a> = GF(9)
        sage: S = SemimonomialTransformationGroup(F, 4)
        sage: g = S(v = [2, a, 1, 2])
        sage: h = S(perm = Permutation('(1,2,3,4)'), autom=F.hom([a**3]))
        sage: g*h
        ((2, a, 1, 2); (1,2,3,4),
         Ring endomorphism of Finite Field in a of size 3^2 Defn: a |--> 2*a + 1)
        sage: h*g
        ((2*a + 1, 1, 2, 2); (1,2,3,4),
         Ring endomorphism of Finite Field in a of size 3^2 Defn: a |--> 2*a + 1)
        sage: S(g)
        ((2, a, 1, 2); (),
         Ring endomorphism of Finite Field in a of size 3^2 Defn: a |--> a)
        sage: S(1)
        ((1, 1, 1, 1); (),
         Ring endomorphism of Finite Field in a of size 3^2 Defn: a |--> a)
    """
    Element = SemimonomialTransformation
    def __init__(self, R, len) -> None:
        """
        Initialization.

        INPUT:

        - ``R`` -- a ring

        - ``len`` -- the degree of the monomial group

        OUTPUT: the complete semimonomial group

        EXAMPLES::

            sage: F.<a> = GF(9)
            sage: S = SemimonomialTransformationGroup(F, 4)
        """
    def base_ring(self):
        """
        Return the underlying ring of ``self``.

        EXAMPLES::

            sage: F.<a> = GF(4)
            sage: SemimonomialTransformationGroup(F, 3).base_ring() is F
            True
        """
    def degree(self) -> Integer:
        """
        Return the degree of ``self``.

        EXAMPLES::

            sage: F.<a> = GF(4)
            sage: SemimonomialTransformationGroup(F, 3).degree()
            3
        """
    def __contains__(self, item) -> bool:
        """
        EXAMPLES::

            sage: F.<a> = GF(4)
            sage: S = SemimonomialTransformationGroup(F, 3)
            sage: 1 in S  # indirect doctest
            True
            sage: a in S  # indirect doctest
            False
        """
    def gens(self) -> tuple:
        """
        Return a tuple of generators of ``self``.

        EXAMPLES::

            sage: F.<a> = GF(4)
            sage: SemimonomialTransformationGroup(F, 3).gens()
            (((a, 1, 1); (),
              Ring endomorphism of Finite Field in a of size 2^2 Defn: a |--> a),
             ((1, 1, 1); (1,2,3),
              Ring endomorphism of Finite Field in a of size 2^2 Defn: a |--> a),
             ((1, 1, 1); (1,2),
              Ring endomorphism of Finite Field in a of size 2^2 Defn: a |--> a),
             ((1, 1, 1); (),
              Ring endomorphism of Finite Field in a of size 2^2 Defn: a |--> a + 1))
        """
    def order(self) -> Integer:
        """
        Return the number of elements of ``self``.

        EXAMPLES::

            sage: F.<a> = GF(4)
            sage: SemimonomialTransformationGroup(F, 5).order() == (4-1)**5 * factorial(5) * 2
            True
        """

class SemimonomialActionVec(Action):
    """
    The natural left action of the semimonomial group on vectors.

    The action is defined by:
    `(\\phi, \\pi, \\alpha)*(v_0, \\ldots, v_{n-1}) :=
    (\\alpha(v_{\\pi(1)-1}) \\cdot \\phi_0^{-1}, \\ldots, \\alpha(v_{\\pi(n)-1}) \\cdot \\phi_{n-1}^{-1})`.
    (The indexing of vectors is `0`-based here, so
    `\\psi = (\\psi_0, \\psi_1, \\ldots, \\psi_{n-1})`.)
    """
    def __init__(self, G, V, check: bool = True) -> None:
        """
        Initialization.

        EXAMPLES::

            sage: F.<a> = GF(4)
            sage: s = SemimonomialTransformationGroup(F, 3).an_element()
            sage: v = (F**3).1
            sage: s*v   # indirect doctest
            (0, 0, 1)
        """

class SemimonomialActionMat(Action):
    """
    The left action of
    :class:`~sage.groups.semimonomial_transformations.semimonomial_transformation_group.SemimonomialTransformationGroup`
    on matrices over the same ring whose number of columns is equal to the degree.
    See :class:`~sage.groups.semimonomial_transformations.semimonomial_transformation_group.SemimonomialActionVec`
    for the definition of the action on the row vectors of such a matrix.
    """
    def __init__(self, G, M, check: bool = True) -> None:
        """
        Initialization.

        EXAMPLES::

            sage: F.<a> = GF(4)
            sage: s = SemimonomialTransformationGroup(F, 3).an_element()
            sage: M = MatrixSpace(F, 3).one()
            sage: s*M  # indirect doctest
            [    0     1     0]
            [    0     0     1]
            [a + 1     0     0]
        """
