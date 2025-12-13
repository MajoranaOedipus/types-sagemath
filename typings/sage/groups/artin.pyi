from sage.combinat.root_system.coxeter_group import CoxeterGroup as CoxeterGroup
from sage.combinat.root_system.coxeter_matrix import CoxeterMatrix as CoxeterMatrix
from sage.groups.finitely_presented import FinitelyPresentedGroup as FinitelyPresentedGroup, FinitelyPresentedGroupElement as FinitelyPresentedGroupElement
from sage.groups.free_group import FreeGroup as FreeGroup
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.rings.infinity import Infinity as Infinity
from sage.structure.richcmp import rich_to_bool as rich_to_bool, richcmp as richcmp
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class ArtinGroupElement(FinitelyPresentedGroupElement):
    """
    An element of an Artin group.

    It is a particular case of element of a finitely presented group.

    EXAMPLES::

        sage: # needs sage.rings.number_field
        sage: A.<s1,s2,s3> = ArtinGroup(['B',3])
        sage: A
        Artin group of type ['B', 3]
        sage: s1 * s2 / s3 / s2
        s1*s2*s3^-1*s2^-1
        sage: A((1, 2, -3, -2))
        s1*s2*s3^-1*s2^-1
    """
    def exponent_sum(self):
        """
        Return the exponent sum of ``self``.

        OUTPUT: integer

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: A = ArtinGroup(['E',6])
            sage: b = A([1, 4, -3, 2])
            sage: b.exponent_sum()
            2
            sage: b = A([])
            sage: b.exponent_sum()
            0

            sage: B = BraidGroup(5)
            sage: b = B([1, 4, -3, 2])
            sage: b.exponent_sum()
            2
            sage: b = B([])
            sage: b.exponent_sum()
            0
        """
    def coxeter_group_element(self, W=None):
        """
        Return the corresponding Coxeter group element under the natural
        projection.

        INPUT:

        - ``W`` -- (default: ``self.parent().coxeter_group()``) the image
          Coxeter group

        OUTPUT: an element of the Coxeter group  ``W``

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: B.<s1,s2,s3> = ArtinGroup(['B',3])
            sage: b = s1 * s2 / s3 / s2
            sage: b1 = b.coxeter_group_element(); b1
            [ 1 -1  0]
            [ 2 -1  0]
            [ a -a  1]
            sage: b.coxeter_group_element().reduced_word()
            [1, 2, 3, 2]
            sage: A.<s1,s2,s3> = ArtinGroup(['A',3])
            sage: c = s1 * s2 *s3
            sage: c1 = c.coxeter_group_element(); c1
            [4, 1, 2, 3]
            sage: c1.reduced_word()
            [3, 2, 1]
            sage: c.coxeter_group_element(W=SymmetricGroup(4))
            (1,4,3,2)
            sage: A.<s1,s2,s3> = BraidGroup(4)
            sage: c = s1 * s2 * s3^-1
            sage: c0 = c.coxeter_group_element(); c0
            [4, 1, 2, 3]
            sage: c1 = c.coxeter_group_element(W=SymmetricGroup(4)); c1
            (1,4,3,2)

        From an element of the Coxeter group it is possible to recover
        the image by the standard section to the Artin group::

            sage: # needs sage.rings.number_field
            sage: B(b1)
            s1*s2*s3*s2
            sage: A(c0)
            s1*s2*s3
            sage: A(c0) == A(c1)
            True
        """
    def burau_matrix(self, var: str = 't'):
        """
        Return the Burau matrix of the Artin group element.

        Following [BQ2024]_, the (generalized) Burau representation
        of an Artin group is defined by deforming the reflection
        representation of the corresponding Coxeter group. However,
        we substitute `q \\mapsto -t` from [BQ2024]_ to match one of
        the unitary (reduced) Burau representations of the braid group
        (see :meth:`sage.groups.braid.Braid.burau_matrix()` for details.)

        More precisely, let `(m_{ij})_{i,j \\in I}` be the
        :meth:`Coxeter matrix<coxeter_matrix>`. Then the action is
        given on the basis `(\\alpha_1, \\ldots \\alpha_n)` (corresponding
        to the reflection representation of the corresponding
        :meth:`Coxeter group<coxeter_group>`) by

        .. MATH::

            \\sigma_i(\\alpha_j) = \\alpha_j
              - \\langle \\alpha_i, \\alpha_j \\rangle_q \\alpha_i,
            \\qquad \\text{ where }
            \\langle \\alpha_i, \\alpha_j \\rangle_q := \\begin{cases}
             1 + t^2 & \\text{if } i = j, \\\\\n             -2 t \\cos(\\pi/m_{ij}) & \\text{if } i \\neq j.
            \\end{cases}.

        By convention `\\cos(\\pi/\\infty) = 1`. Note that the inverse of the
        generators act by `\\sigma_i^{-1}(\\alpha_j) = \\alpha_j - q^{-2}
        \\langle \\alpha_j, \\alpha_i \\rangle_q \\alpha_i`.

        INPUT:

        - ``var`` -- string (default: ``'t'``); the name of the
          variable in the entries of the matrix

        OUTPUT:

        The Burau matrix of the Artin group element over the Laurent
        polynomial ring in the variable ``var``.

        EXAMPLES::

            sage: A.<s1,s2,s3> = ArtinGroup(['B',3])
            sage: B1 = s1.burau_matrix()
            sage: B2 = s2.burau_matrix()
            sage: B3 = s3.burau_matrix()
            sage: [B1, B2, B3]
            [
            [-t^2    t    0]  [   1    0    0]  [   1    0    0]
            [   0    1    0]  [   t -t^2  a*t]  [   0    1    0]
            [   0    0    1], [   0    0    1], [   0  a*t -t^2]
            ]
            sage: B1 * B2 * B1 == B2 * B1 * B2
            True
            sage: B2 * B3 * B2 * B3 == B3 * B2 * B3 * B2
            True
            sage: B1 * B3 == B3 * B1
            True
            sage: (~s1).burau_matrix() * B1 == 1
            True

        We verify the example in Theorem 4.1 of [BQ2024]_::

            sage: A.<s1,s2,s3,s4> = ArtinGroup(['A', 3, 1])
            sage: [g.burau_matrix() for g in A.gens()]
            [
            [-t^2    t    0    t]  [   1    0    0    0]  [   1    0    0    0]
            [   0    1    0    0]  [   t -t^2    t    0]  [   0    1    0    0]
            [   0    0    1    0]  [   0    0    1    0]  [   0    t -t^2    t]
            [   0    0    0    1], [   0    0    0    1], [   0    0    0    1],
            <BLANKLINE>
            [   1    0    0    0]
            [   0    1    0    0]
            [   0    0    1    0]
            [   t    0    t -t^2]
            ]
            sage: a = s3^2 * s4 * s3 * s2 *s1 * ~s3 * s4 * s3 * s2 * s1^-2 * s4
            sage: b = s1^2 * ~s2 * s4 * s1 * ~s3 * s2 * ~s4 * s3 * s1 * s4 * s1 * ~s2 * s4^-2 * s3
            sage: alpha = a * s3 * ~a
            sage: beta = b * s2 * ~b
            sage: elm = alpha * beta * ~alpha * ~beta
            sage: print(elm.Tietze())
            (3, 3, 4, 3, 2, 1, -3, 4, 3, 2, -1, -1, 4, 3, -4, 1, 1, -2, -3,
             -4, 3, -1, -2, -3, -4, -3, -3, 1, 1, -2, 4, 1, -3, 2, -4, 3, 1,
             4, 1, -2, -4, -4, 3, 2, -3, 4, 4, 2, -1, -4, -1, -3, 4, -2, 3,
             -1, -4, 2, -1, -1, 3, 3, 4, 3, 2, 1, -3, 4, 3, 2, -1, -1, 4,
             -3, -4, 1, 1, -2, -3, -4, 3, -1, -2, -3, -4, -3, -3, 1, 1, -2,
             4, 1, -3, 2, -4, 3, 1, 4, 1, -2, -4, -4, 3, -2, -3, 4, 4, 2,
             -1, -4, -1, -3, 4, -2, 3, -1, -4, 2, -1, -1)
            sage: elm.burau_matrix()
            [1 0 0 0]
            [0 1 0 0]
            [0 0 1 0]
            [0 0 0 1]

        Next, we show ``elm`` is not the identity by using the embedding of
        the affine braid group `\\widetilde{B}_n \\to B_{n+1}`::

            sage: B.<t1,t2,t3,t4> = BraidGroup(5)
            sage: D = t1 * t2 * t3 * t4^2
            sage: t0 = D * t3 * ~D
            sage: t0*t1*t0 == t1*t0*t1
            True
            sage: t0*t2 == t2*t0
            True
            sage: t0*t3*t0 == t3*t0*t3
            True
            sage: T = [t0, t1, t2, t3]
            sage: emb = B.prod(T[i-1] if i > 0 else ~T[-i-1] for i in elm.Tietze())
            sage: emb.is_one()
            False

        Since the Burau representation does not respect the group embedding,
        the corresponding `B_5` element's Burau matrix is not the identity
        (Bigelow gave an example of the representation not being faithful for
        `B_5`, but it is still open for `B_4`)::

            sage: emb.burau_matrix() != 1
            True

        We also verify the result using the elements in [BQ2024]_ Remark 4.2::

            sage: ap = s3 * s1 * s2 * s1 * ~s3 * s4 * s2 * s3 * s2 * ~s3 * s1^-2 * s4
            sage: bp = s1 * ~s4 * s1^2 * s3^-2 * ~s2 * s4 * s1 * ~s3 * s2 * ~s4 * s3 * s1 * s4 * s1 * ~s2 * s4^-2 * s3
            sage: alpha = ap * s3 * ~ap
            sage: beta = bp * s2 * ~bp
            sage: elm = alpha * beta * ~alpha * ~beta
            sage: elm.burau_matrix()
            [1 0 0 0]
            [0 1 0 0]
            [0 0 1 0]
            [0 0 0 1]

        REFERENCES:

        - [BQ2024]_
        """

class FiniteTypeArtinGroupElement(ArtinGroupElement):
    """
    An element of a finite-type Artin group.
    """
    def __hash__(self):
        """
        Return a hash value for ``self``.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: B.<s1,s2,s3> = ArtinGroup(['B',3])
            sage: hash(s1*s3) == hash(s3*s1)
            True
            sage: hash(s1*s2) == hash(s2*s1)
            False
            sage: hash(s1*s2*s1) == hash(s2*s1*s2)
            True
            sage: hash(s2*s3*s2) == hash(s3*s2*s3)
            False
            sage: hash(s2*s3*s2*s3) == hash(s3*s2*s3*s2)
            True
        """
    @cached_method
    def left_normal_form(self):
        """
        Return the left normal form of ``self``.

        OUTPUT:

        A tuple of simple generators in the left normal form. The first
        element is a power of `\\Delta`, and the rest are elements of the
        natural section lift from the corresponding Coxeter group.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: A = ArtinGroup(['B',3])
            sage: A([1]).left_normal_form()
            (1, s1)
            sage: A([-1]).left_normal_form()
            (s1^-1*(s2^-1*s1^-1*s3^-1)^2*s2^-1*s3^-1, s3*(s2*s3*s1)^2*s2)
            sage: A([1, 2, 2, 1, 2]).left_normal_form()
            (1, s1*s2*s1, s2*s1)
            sage: A([3, 3, -2]).left_normal_form()
            (s1^-1*(s2^-1*s1^-1*s3^-1)^2*s2^-1*s3^-1,
             s3*s1*s2*s3*s2*s1, s3, s3*s2*s3)
            sage: A([1, 2, 3, -1, 2, -3]).left_normal_form()
            (s1^-1*(s2^-1*s1^-1*s3^-1)^2*s2^-1*s3^-1,
             (s3*s1*s2)^2*s1, s1*s2*s3*s2)
            sage: A([1,2,1,3,2,1,3,2,3,3,2,3,1,2,3,1,2,3,1,2]).left_normal_form()
            ((s3*(s2*s3*s1)^2*s2*s1)^2, s3*s2)

            sage: B = BraidGroup(4)
            sage: b = B([1, 2, 3, -1, 2, -3])
            sage: b.left_normal_form()
            (s0^-1*s1^-1*s0^-1*s2^-1*s1^-1*s0^-1, s0*s1*s2*s1*s0, s0*s2*s1)
            sage: c = B([1])
            sage: c.left_normal_form()
            (1, s0)
        """

class ArtinGroup(UniqueRepresentation, FinitelyPresentedGroup):
    """
    An Artin group.

    Fix an index set `I`. Let `M = (m_{ij})_{i,j \\in I}` be a
    :class:`Coxeter matrix
    <sage.combinat.root_system.coxeter_matrix.CoxeterMatrix>`.
    An *Artin group* is a group `A_M` that has a presentation
    given by generators `\\{ s_i \\mid i \\in I \\}` and relations

    .. MATH::

        \\underbrace{s_i s_j s_i \\cdots}_{m_{ij}}
        = \\underbrace{s_j s_i s_j \\cdots}_{\\text{$m_{ji}$ factors}}

    for all `i,j \\in I` with the usual convention that `m_{ij} = \\infty`
    implies no relation between `s_i` and `s_j`. There is a natural
    corresponding Coxeter group `W_M` by imposing the additional
    relations `s_i^2 = 1` for all `i \\in I`. Furthermore, there is
    a natural section of `W_M` by sending a reduced word
    `s_{i_1} \\cdots s_{i_{\\ell}} \\mapsto s_{i_1} \\cdots s_{i_{\\ell}}`.

    Artin groups `A_M` are classified based on the Coxeter data:

    - `A_M` is of *finite type* or *spherical* if `W_M` is finite;
    - `A_M` is of *affine type* if `W_M` is of affine type;
    - `A_M` is of *large type* if `m_{ij} \\geq 4` for all `i,j \\in I`;
    - `A_M` is of *extra-large type* if `m_{ij} \\geq 5` for all `i,j \\in I`;
    - `A_M` is *right-angled* if `m_{ij} \\in \\{2,\\infty\\}` for all `i,j \\in I`.

    Artin groups are conjectured to have many nice properties:

    - Artin groups are torsion free.
    - Finite type Artin groups have `Z(A_M) = \\ZZ` and infinite type
      Artin groups have trivial center.
    - Artin groups have solvable word problems.
    - `H_{W_M} / W_M` is a `K(A_M, 1)`-space, where `H_W` is the
      hyperplane complement of the Coxeter group `W` acting on `\\CC^n`.

    These conjectures are known when the Artin group is finite type and a
    number of other cases. See, e.g., [GP2012]_ and references therein.

    INPUT:

    - ``coxeter_data`` -- data defining a Coxeter matrix

    - ``names`` -- string or list/tuple/iterable of strings
      (default: ``'s'``); the generator names or name prefix

    EXAMPLES::

        sage: A.<a,b,c> = ArtinGroup(['B',3]);  A                                       # needs sage.rings.number_field
        Artin group of type ['B', 3]
        sage: ArtinGroup(['B',3])                                                       # needs sage.rings.number_field
        Artin group of type ['B', 3]

    The input must always include the Coxeter data, but the ``names``
    can either be a string representing the prefix of the names or
    the explicit names of the generators. Otherwise the default prefix
    of ``'s'`` is used::

        sage: ArtinGroup(['B',2]).generators()                                          # needs sage.rings.number_field
        (s1, s2)
        sage: ArtinGroup(['B',2], 'g').generators()                                     # needs sage.rings.number_field
        (g1, g2)
        sage: ArtinGroup(['B',2], 'x,y').generators()                                   # needs sage.rings.number_field
        (x, y)

    REFERENCES:

    - :wikipedia:`Artin_group`

    .. SEEALSO::

        :class:`~sage.groups.raag.RightAngledArtinGroup`
    """
    @staticmethod
    def __classcall_private__(cls, coxeter_data, names=None):
        """
        Normalize input to ensure a unique representation.

        TESTS::

            sage: # needs sage.rings.number_field
            sage: A1 = ArtinGroup(['B',3])
            sage: A2 = ArtinGroup(['B',3], 's')
            sage: A3 = ArtinGroup(['B',3],  ['s1','s2','s3'])
            sage: A1 is A2 and A2 is A3
            True

            sage: # needs sage.rings.number_field
            sage: A1 = ArtinGroup(['B',2], 'a,b')
            sage: A2 = ArtinGroup([[1,4],[4,1]], 'a,b')
            sage: A3.<a,b> = ArtinGroup('B2')
            sage: A1 is A2 and A2 is A3
            True

            sage: ArtinGroup(['A',3]) is BraidGroup(4, 's1,s2,s3')                      # needs sage.rings.number_field
            True

            sage: G = graphs.PathGraph(3)
            sage: CM = CoxeterMatrix([[1,-1,2],[-1,1,-1],[2,-1,1]], index_set=G.vertices(sort=True))
            sage: A = groups.misc.Artin(CM)                                             # needs sage.rings.number_field
            sage: Ap = groups.misc.RightAngledArtin(G, 's')                             # needs sage.rings.number_field
            sage: A is Ap                                                               # needs sage.rings.number_field
            True
        """
    def __init__(self, coxeter_matrix, names) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: # needs sage.rings.number_field
            sage: A = ArtinGroup(['D',4])
            sage: TestSuite(A).run()
            sage: A = ArtinGroup(['B',3], ['x','y','z'])
            sage: TestSuite(A).run()
        """
    def cardinality(self):
        """
        Return the number of elements of ``self``.

        OUTPUT: infinity

        EXAMPLES::

            sage: Gamma = graphs.CycleGraph(5)
            sage: G = RightAngledArtinGroup(Gamma)
            sage: G.cardinality()
            +Infinity

            sage: A = ArtinGroup(['A',1])                                               # needs sage.rings.number_field
            sage: A.cardinality()                                                       # needs sage.rings.number_field
            +Infinity
        """
    order = cardinality
    def as_permutation_group(self) -> None:
        """
        Return an isomorphic permutation group.

        This raises a :exc:`ValueError` error since Artin groups are
        infinite and have no corresponding permutation group.

        EXAMPLES::

            sage: Gamma = graphs.CycleGraph(5)
            sage: G = RightAngledArtinGroup(Gamma)
            sage: G.as_permutation_group()
            Traceback (most recent call last):
            ...
            ValueError: the group is infinite

            sage: A = ArtinGroup(['D',4], 'g')                                          # needs sage.rings.number_field
            sage: A.as_permutation_group()                                              # needs sage.rings.number_field
            Traceback (most recent call last):
            ...
            ValueError: the group is infinite
        """
    def coxeter_type(self):
        """
        Return the Coxeter type of ``self``.

        EXAMPLES::

            sage: A = ArtinGroup(['D',4])                                               # needs sage.rings.number_field
            sage: A.coxeter_type()                                                      # needs sage.rings.number_field
            Coxeter type of ['D', 4]
        """
    def coxeter_matrix(self):
        """
        Return the Coxeter matrix of ``self``.

        EXAMPLES::

            sage: A = ArtinGroup(['B',3])                                               # needs sage.rings.number_field
            sage: A.coxeter_matrix()                                                    # needs sage.rings.number_field
            [1 3 2]
            [3 1 4]
            [2 4 1]
        """
    def coxeter_group(self):
        """
        Return the Coxeter group of ``self``.

        EXAMPLES::

            sage: A = ArtinGroup(['D',4])                                               # needs sage.rings.number_field
            sage: A.coxeter_group()                                                     # needs sage.rings.number_field
            Finite Coxeter group over Integer Ring with Coxeter matrix:
            [1 3 2 2]
            [3 1 3 3]
            [2 3 1 2]
            [2 3 2 1]
        """
    def index_set(self):
        """
        Return the index set of ``self``.

        OUTPUT: tuple

        EXAMPLES::

            sage: A = ArtinGroup(['E',7])                                               # needs sage.rings.number_field
            sage: A.index_set()                                                         # needs sage.rings.number_field
            (1, 2, 3, 4, 5, 6, 7)
        """
    def some_elements(self) -> list:
        """
        Return a list of some elements of ``self``.

        EXAMPLES::

            sage: A = ArtinGroup(['B',3])                                               # needs sage.rings.number_field
            sage: A.some_elements()                                                     # needs sage.rings.number_field
            [s1, s1*s2*s3, (s1*s2*s3)^3]
        """
    Element = ArtinGroupElement

class FiniteTypeArtinGroup(ArtinGroup):
    """
    A finite-type Artin group.

    An Artin group is *finite-type* or *spherical* if the corresponding
    Coxeter group is finite. Finite type Artin groups are known to be
    torsion free, have a Garside structure given by `\\Delta` (see
    :meth:`delta`) and have a center generated by `\\Delta`.

    .. SEEALSO::

        :class:`ArtinGroup`

    EXAMPLES::

        sage: ArtinGroup(['E',7])                                                       # needs sage.rings.number_field
        Artin group of type ['E', 7]

    Since the word problem for finite-type Artin groups is solvable, their
    Cayley graph can be locally obtained as follows (see :issue:`16059`)::

        sage: def ball(group, radius):
        ....:     ret = set()
        ....:     ret.add(group.one())
        ....:     for length in range(1, radius):
        ....:         for w in Words(alphabet=group.gens(), length=length):
        ....:              ret.add(prod(w))
        ....:     return ret
        sage: A = ArtinGroup(['B',3])                                                   # needs sage.rings.number_field
        sage: GA = A.cayley_graph(elements=ball(A, 4), generators=A.gens()); GA         # needs sage.rings.number_field
        Digraph on 32 vertices

    Since the Artin group has nontrivial relations, this graph contains less
    vertices than the one associated to the free group (which is a tree)::

        sage: F = FreeGroup(3)
        sage: GF = F.cayley_graph(elements=ball(F, 4), generators=F.gens()); GF         # needs sage.combinat
        Digraph on 40 vertices
    """
    def delta(self):
        """
        Return the `\\Delta` element of ``self``.

        EXAMPLES::

            sage: A = ArtinGroup(['B',3])                                               # needs sage.rings.number_field
            sage: A.delta()                                                             # needs sage.rings.number_field
            s3*(s2*s3*s1)^2*s2*s1

            sage: A = ArtinGroup(['G',2])                                               # needs sage.rings.number_field
            sage: A.delta()                                                             # needs sage.rings.number_field
            (s2*s1)^3

            sage: B = BraidGroup(5)
            sage: B.delta()
            s0*s1*s2*s3*s0*s1*s2*s0*s1*s0
        """
    Element = FiniteTypeArtinGroupElement
