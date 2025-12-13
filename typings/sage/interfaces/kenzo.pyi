from _typeshed import Incomplete
from sage.categories.commutative_additive_groups import CommutativeAdditiveGroups as CommutativeAdditiveGroups
from sage.env import KENZO_FAS as KENZO_FAS
from sage.features.kenzo import Kenzo as Kenzo
from sage.groups.abelian_gps.abelian_group import AbelianGroup as AbelianGroup
from sage.groups.additive_abelian.additive_abelian_group import AdditiveAbelianGroup as AdditiveAbelianGroup
from sage.homology.chain_complex import ChainComplex as ChainComplex
from sage.homology.homology_group import HomologyGroup as HomologyGroup
from sage.libs.ecl import EclListIterator as EclListIterator, EclObject as EclObject, ecl_eval as ecl_eval
from sage.matrix.constructor import matrix as matrix
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.sage_object import SageObject as SageObject
from sage.topology.simplicial_set import AbstractSimplex as AbstractSimplex, SimplicialSet as SimplicialSet

kenzo_names: Incomplete
name: Incomplete

def Sphere(n):
    """
    Return the `n` dimensional sphere as a Kenzo simplicial set.

    INPUT:

    - ``n`` -- the dimension of the sphere

    OUTPUT: a :class:`KenzoSimplicialSet`

    EXAMPLES::

        sage: # optional - kenzo
        sage: from sage.interfaces.kenzo import Sphere
        sage: s2 = Sphere(2)
        sage: s2
        [K1 Simplicial-Set]
        sage: [s2.homology(i) for i in range(8)]
        [Z, 0, Z, 0, 0, 0, 0, 0]
    """
def MooreSpace(m, n):
    """
    Return the Moore space `M(m, n)` as a Kenzo simplicial set.

    The Moore space `M(m, n)` is the space whose `n`-th homology group
    is isomorphic to the cyclic group of order `m`, and the rest of the
    homology groups are trivial.

    INPUT:

    - ``m`` -- positive integer; the order of the nontrivial homology group

    - ``n`` -- the dimension in which the homology is not trivial

    OUTPUT: a KenzoSimplicialSet

    EXAMPLES::

        sage: # optional - kenzo
        sage: from sage.interfaces.kenzo import MooreSpace
        sage: m24 = MooreSpace(2,4)
        sage: m24
        [K10 Simplicial-Set]
        sage: [m24.homology(i) for i in range(8)]
        [Z, 0, 0, 0, C2, 0, 0, 0]
    """
def EilenbergMacLaneSpace(G, n):
    """
    Return the Eilenberg-MacLane space ``K(G, n)`` as a Kenzo simplicial group.

    The Eilenberg-MacLane space ``K(G, n)`` is the space whose has n'th homotopy
    group isomorphic to ``G``, and the rest of the homotopy groups are trivial.

    INPUT:

    - ``G`` -- group; currently only ``ZZ`` and the additive group of two
      elements are supported

    - ``n`` -- the dimension in which the homotopy is not trivial

    OUTPUT: a :class:`KenzoSimplicialGroup`

    EXAMPLES::

        sage: # optional - kenzo
        sage: from sage.interfaces.kenzo import EilenbergMacLaneSpace
        sage: e3 = EilenbergMacLaneSpace(ZZ, 3)
        sage: [e3.homology(i) for i in range(8)]
        [Z, 0, 0, Z, 0, C2, 0, C3]
        sage: f3 = EilenbergMacLaneSpace(AdditiveAbelianGroup([2]), 3)
        sage: [f3.homology(i) for i in range(8)]
        [Z, 0, 0, C2, 0, C2, C2, C2]
    """

class KenzoObject(SageObject):
    """
    Wrapper to Kenzo objects.

    INPUT:

    - ``kenzo_object`` -- a wrapper around a Kenzo object
      (which is an ecl object)
    """
    def __init__(self, kenzo_object) -> None:
        """
        Construct the chain complex.

        TESTS::

            sage: # optional - kenzo
            sage: from sage.interfaces.kenzo import KenzoObject
            sage: from sage.interfaces.kenzo import __sphere__
            sage: ks = __sphere__(2)
            sage: ks
            <ECL: [K1 Simplicial-Set]>
            sage: s2 = KenzoObject(ks)
            sage: s2
            [K1 Simplicial-Set]
            sage: TestSuite(s2).run(skip='_test_pickling')
        """

class KenzoSpectralSequence(KenzoObject):
    """
    Wrapper around Kenzo spectral sequences
    """
    def group(self, p, i, j):
        """
        Return the ``i,j``-th group of the ``p`` page.

        INPUT:

        - ``p`` -- the page to take the group from

        - ``i`` -- the column where the group is taken from

        - ``j`` -- the row where the group is taken from

        EXAMPLES::

            sage: # optional - kenzo
            sage: from sage.interfaces.kenzo import Sphere
            sage: S2 = Sphere(2)
            sage: EMS = S2.em_spectral_sequence()
            sage: EMS.group(0, -1, 2)
            Additive abelian group isomorphic to Z
            sage: EMS.group(0, -1, 3)
            Trivial group
        """
    def matrix(self, p, i, j):
        """
        Return the matrix that determines the differential from the
        ``i,j``-th group of the ``p``-th page.

        INPUT:

        - ``p`` -- the page

        - ``i`` -- the column of the differential domain

        - ``j`` -- the row of the differential domain

        EXAMPLES::

            sage: # optional - kenzo
            sage: from sage.interfaces.kenzo import Sphere
            sage: S3 = Sphere(3)
            sage: L = S3.loop_space()
            sage: EMS = L.em_spectral_sequence()
            sage: EMS.table(1, -5, -2, 5, 8)
              0   Z   Z + Z + Z   Z + Z + Z
              0   0   0           0
              0   0   Z           Z + Z
              0   0   0           0
            sage: EMS.matrix(1, -2 ,8)
            [ 3 -2  0]
            [ 3  0 -3]
            [ 0  2 -3]
        """
    def differential(self, p, i, j):
        """
        Return the ``(p, i, j)`` differential morphism of the spectral sequence.

        INPUT:

        - ``p`` -- the page

        - ``i`` -- the column of the differential domain

        - ``j`` -- the row of the differential domain

        EXAMPLES::

            sage: # optional - kenzo
            sage: from sage.interfaces.kenzo import Sphere
            sage: S3 = Sphere(3)
            sage: L = S3.loop_space()
            sage: EMS = L.em_spectral_sequence()
            sage: EMS.table(1,-5,-2,5,8)
              0   Z   Z + Z + Z   Z + Z + Z
              0   0   0           0
              0   0   Z           Z + Z
              0   0   0           0
            sage: EMS.matrix(1, -3, 8)
            [ 2 -2  2]
            sage: EMS.differential(1, -3, 8)
            Morphism from module over Integer Ring with invariants (0, 0, 0) to module with invariants (0,) that sends the generators to [(2), (-2), (2)]
        """
    def table(self, p, i1, i2, j1, j2):
        """
        Return a table printing the groups in the ``p`` page.

        INPUT:

        - ``p`` -- the page to print

        -- ``i1`` -- the first column to print

        -- ``i2`` -- the last column to print

        -- ``j1`` -- the first row to print

        -- ``j2`` -- the last row to print

        EXAMPLES::

            sage: # optional - kenzo
            sage: from sage.interfaces.kenzo import Sphere
            sage: S2 = Sphere(2)
            sage: EMS = S2.em_spectral_sequence()
            sage: EMS.table(0, -2, 2, -2, 2)
              0   Z   0   0   0
              0   0   0   0   0
              0   0   Z   0   0
              0   0   0   0   0
              0   0   0   0   0
        """

class KenzoChainComplex(KenzoObject):
    """
    Wrapper to Kenzo chain complexes. Kenzo simplicial sets are a particular case
    of Kenzo chain complexes.
    """
    def homology(self, n):
        """
        Return the `n`-th homology group of the chain complex associated to this
        kenzo object.

        INPUT:

        - ``n`` -- the dimension in which compute the homology

        OUTPUT: a homology group

        EXAMPLES::

            sage: # optional - kenzo
            sage: from sage.interfaces.kenzo import Sphere
            sage: s2 = Sphere(2)
            sage: s2
            [K1 Simplicial-Set]
            sage: s2.homology(2)
            Z
        """
    def tensor_product(self, other):
        """
        Return the tensor product of ``self`` and ``other``.

        INPUT:

        - ``other`` -- The Kenzo object with which to compute the tensor product

        OUTPUT: a :class:`KenzoChainComplex`

        EXAMPLES::

            sage: # optional - kenzo
            sage: from sage.interfaces.kenzo import Sphere
            sage: s2 = Sphere(2)
            sage: s3 = Sphere(3)
            sage: p = s2.tensor_product(s3)
            sage: type(p)
            <class 'sage.interfaces.kenzo.KenzoChainComplex'>
            sage: [p.homology(i) for i in range(8)]
            [Z, 0, Z, Z, 0, Z, 0, 0]
        """
    def basis(self, dim):
        '''
        Return the list of generators of the chain complex associated to the kenzo
        object ``self`` in dimension ``dim``.

        INPUT:

        - ``dim`` -- integer

        OUTPUT: list of the form [\'G"dim"G0\', \'G"dim"G1\', \'G"dim"G2\', ...]

        EXAMPLES::

            sage: # optional - kenzo
            sage: from sage.interfaces.kenzo import KChainComplex
            sage: m1 = matrix(ZZ, 3, 2, [-1, 1, 3, -4, 5, 6])
            sage: m4 = matrix(ZZ, 2, 2, [1, 2, 3, 6])
            sage: m5 = matrix(ZZ, 2, 3, [2, 2, 2, -1, -1, -1])
            sage: sage_chcm = ChainComplex({1: m1, 4: m4, 5: m5}, degree = -1)
            sage: kenzo_chcm = KChainComplex(sage_chcm)
            sage: kenzo_chcm
            [K... Chain-Complex]
            sage: for i in range(6):
            ....:     print("Basis in dimension %i: %s" % (i, kenzo_chcm.basis(i)))
            Basis in dimension 0: [\'G0G0\', \'G0G1\', \'G0G2\']
            Basis in dimension 1: [\'G1G0\', \'G1G1\']
            Basis in dimension 2: None
            Basis in dimension 3: [\'G3G0\', \'G3G1\']
            Basis in dimension 4: [\'G4G0\', \'G4G1\']
            Basis in dimension 5: [\'G5G0\', \'G5G1\', \'G5G2\']
        '''
    def identity_morphism(self):
        """
        Return the identity morphism (degree 0) between ``self`` and itself.

        OUTPUT: a :class:`KenzoChainComplexMorphism`

        EXAMPLES::

            sage: # optional - kenzo
            sage: from sage.interfaces.kenzo import Sphere
            sage: s2 = Sphere(2)
            sage: tp = s2.tensor_product(s2)
            sage: idnt = tp.identity_morphism()
            sage: type(idnt)
            <class 'sage.interfaces.kenzo.KenzoChainComplexMorphism'>
        """
    def null_morphism(self, target=None, degree=None):
        """
        Return the null morphism between the chain complexes ``self`` and ``target``
        of degree ``degree``.

        INPUT:

        - ``target`` -- a KenzoChainComplex or ``None`` (default)
        - ``degree`` -- integer or ``None`` (default)

        OUTPUT:

        - A :class:`KenzoChainComplexMorphism` representing the null morphism between
          ``self`` and ``target`` of degree ``degree``. If ``target`` takes ``None`` value,
          ``self`` is assumed as the target chain complex; if ``degree`` takes ``None`` value,
          0 is assumed as the degree of the null morphism.

        EXAMPLES::

            sage: # optional - kenzo
            sage: from sage.interfaces.kenzo import Sphere
            sage: s2 = Sphere(2)
            sage: s3 = Sphere(3)
            sage: tp22 = s2.tensor_product(s2)
            sage: tp22
            [K... Chain-Complex]
            sage: tp23 = s2.tensor_product(s3)
            sage: tp23
            [K... Chain-Complex]
            sage: null1 = tp22.null_morphism()
            sage: null1
            [K... Morphism (degree 0): K... -> K...]
            sage: null2 = tp22.null_morphism(target = tp23, degree = -3)
            sage: null2
            [K... Morphism (degree -3): K... -> K...]
        """
    def differential(self, dim=None, comb=None):
        """
        Return the differential of a combination.

        INPUT:

        - ``dim`` -- integer or ``None`` (default)

        - ``comb`` -- list representing a formal sum of generators in the module
          of dimension ``dim`` or ``None`` (default). For example, to represent
          G7G12 + 3*G7G0 - 5*G7G3 we use the list [3, 'G7G0', -5, 'G7G3', 1, 'G7G12'].
          Note that the generators must be in ascending order respect to the number
          after the second G in their representation; the parameter
          ``comb`` = [1, 'G7G12', 3, 'G7G0', -5, 'G7G3'] will produce an error in
          Kenzo.

        OUTPUT:

        - If ``dim`` and ``comb`` are not ``None``, it returns a Kenzo combination
          representing the differential of the formal combination represented by
          ``comb`` in the chain complex ``self`` in dimension ``dim``. On the other
          hand, if ``dim`` or ``comb`` (or both) take ``None`` value, the differential
          :class:`KenzoMorphismChainComplex` of ``self`` is returned.

        EXAMPLES::

            sage: # optional - kenzo
            sage: from sage.interfaces.kenzo import KChainComplex
            sage: m1 = matrix(ZZ, 3, 2, [-1, 1, 3, -4, 5, 6])
            sage: m4 = matrix(ZZ, 2, 2, [1, 2, 3, 6])
            sage: m5 = matrix(ZZ, 2, 3, [2, 2, 2, -1, -1, -1])
            sage: sage_chcm = ChainComplex({1: m1, 4: m4, 5: m5}, degree = -1)
            sage: kenzo_chcm = KChainComplex(sage_chcm)
            sage: kenzo_chcm
            [K... Chain-Complex]
            sage: kenzo_chcm.basis(4)
            ['G4G0', 'G4G1']
            sage: kenzo_chcm.differential(4, [1, 'G4G0'])
            <BLANKLINE>
            ----------------------------------------------------------------------{CMBN 3}
            <1 * G3G0>
            <3 * G3G1>
            ------------------------------------------------------------------------------
            <BLANKLINE>
            sage: kenzo_chcm.basis(5)
            ['G5G0', 'G5G1', 'G5G2']
            sage: kenzo_chcm.differential(5, [1, 'G5G0', 2, 'G5G2'])
            <BLANKLINE>
            ----------------------------------------------------------------------{CMBN 4}
            <6 * G4G0>
            <-3 * G4G1>
            ------------------------------------------------------------------------------
            <BLANKLINE>
        """
    def orgn(self):
        """
        Return the :orgn slot of Kenzo, which stores as a list the origin of the object.

        EXAMPLES::

            sage: # optional - kenzo
            sage: from sage.interfaces.kenzo import Sphere
            sage: s2 = Sphere(2)
            sage: l2 = s2.loop_space()
            sage: l2.orgn()
            '(LOOP-SPACE [K... Simplicial-Set])'
            sage: A = l2.cartesian_product(s2)
            sage: A.orgn()
            '(CRTS-PRDC [K... Simplicial-Group] [K... Simplicial-Set])'
        """

class KenzoSimplicialSet(KenzoChainComplex):
    """
    Wrapper to Kenzo simplicial sets.

    In Kenzo, the homology of a simplicial set in computed from its associated
    chain complex. Hence, this class inherits from `KenzoChainComplex`.
    """
    def loop_space(self, n: int = 1):
        """
        Return the `n`-th iterated loop space.

        INPUT:

        - ``n`` -- (default: 1) the number of times to iterate the loop space
          construction

        OUTPUT: a :class:`KenzoSimplicialGroup`

        EXAMPLES::

            sage: # optional - kenzo
            sage: from sage.interfaces.kenzo import Sphere
            sage: s2 = Sphere(2)
            sage: l2 = s2.loop_space()
            sage: type(l2)
            <class 'sage.interfaces.kenzo.KenzoSimplicialGroup'>
            sage: l2 = s2.loop_space()
            sage: [l2.homology(i) for i in range(8)]
            [Z, Z, Z, Z, Z, Z, Z, Z]
        """
    def cartesian_product(self, other):
        """
        Return the cartesian product of ``self`` and ``other``.

        INPUT:

        - ``other`` -- the Kenzo simplicial set with which the product is made

        OUTPUT: a :class:`KenzoSimplicialSet`

        EXAMPLES::

            sage: # optional - kenzo
            sage: from sage.interfaces.kenzo import Sphere
            sage: s2 = Sphere(2)
            sage: s3 = Sphere(3)
            sage: p = s2.cartesian_product(s3)
            sage: type(p)
            <class 'sage.interfaces.kenzo.KenzoSimplicialSet'>
            sage: [p.homology(i) for i in range(6)]
            [Z, 0, Z, Z, 0, Z]
        """
    def suspension(self):
        """
        Return the suspension of the simplicial set.

        OUTPUT: a :class:`KenzoSimplicialSet`

        EXAMPLES::

            sage: # optional - kenzo
            sage: from sage.interfaces.kenzo import EilenbergMacLaneSpace
            sage: e3 = EilenbergMacLaneSpace(ZZ, 3)
            sage: s = e3.suspension()
            sage: type(s)
            <class 'sage.interfaces.kenzo.KenzoSimplicialSet'>
            sage: [s.homology(i) for i in range(6)]
            [Z, 0, 0, 0, Z, 0]
        """
    def homotopy_group(self, n):
        """
        Return the `n`-th homotopy group of ``self``.

        INPUT:

        - ``n`` -- the dimension of the homotopy group to be computed

        EXAMPLES::

            sage: # optional - kenzo
            sage: from sage.interfaces.kenzo import Sphere
            sage: s2 = Sphere(2)
            sage: p = s2.cartesian_product(s2)
            sage: p.homotopy_group(3)
            Multiplicative Abelian group isomorphic to Z x Z


        .. WARNING::

            This method assumes that the underlying space is simply connected.
            You might get wrong answers if it is not.
        """
    def em_spectral_sequence(self):
        """
        Return the Eilenberg-Moore spectral sequence of ``self``.

        OUTPUT: a :class:`KenzoSpectralSequence`

        EXAMPLES::

            sage: # optional - kenzo
            sage: from sage.interfaces.kenzo import Sphere
            sage: S2 = Sphere(2)
            sage: EMS = S2.em_spectral_sequence()
            sage: EMS.table(0, -2, 2, -2, 2)
              0   Z   0   0   0
              0   0   0   0   0
              0   0   Z   0   0
              0   0   0   0   0
              0   0   0   0   0


        .. WARNING::

            This method assumes that the underlying space is simply connected.
            You might get wrong answers if it is not.
        """
    def sw_spectral_sequence(self):
        """
        Return the Serre sequence of the first step of the Whitehead tower.

        OUTPUT: a :class:`KenzoSpectralSequence`

        EXAMPLES::

            sage: # optional - kenzo
            sage: from sage.interfaces.kenzo import Sphere
            sage: S3 = Sphere(3)
            sage: E = S3.sw_spectral_sequence()
            sage: T = E.table(0, 0, 4, 0, 4)
            sage: T
              Z   0   0   Z   0
              0   0   0   0   0
              Z   0   0   Z   0
              0   0   0   0   0
              Z   0   0   Z   0
        """
    def serre_spectral_sequence(self):
        """
        Return the spectral sequence of ``self``.

        The object ``self`` must be created as a cartesian product (twisted or not).

        OUTPUT: a :class:`KenzoSpectralSequence`

        EXAMPLES::

            sage: # optional - kenzo
            sage: from sage.interfaces.kenzo import Sphere
            sage: S2 = Sphere(2)
            sage: S3 = Sphere(3)
            sage: P = S2.cartesian_product(S3)
            sage: E = P.serre_spectral_sequence()
            sage: E.table(0, 0, 2, 0, 3)
              Z   0   Z
              0   0   0
              0   0   0
              Z   0   Z

        .. WARNING::

            This method assumes that the underlying space is simply connected.
            You might get wrong answers if it is not.
        """
    def wedge(self, other):
        """
        Return the wedge of ``self`` and ``other``.

        INPUT:

        - ``other`` -- the Kenzo simplicial set with which the wedge is made

        OUTPUT: a :class:`KenzoSimplicialSet`

        EXAMPLES::

            sage: # optional - kenzo
            sage: from sage.interfaces.kenzo import Sphere
            sage: s2 = Sphere(2)
            sage: s3 = Sphere(3)
            sage: w = s2.wedge(s3)
            sage: type(w)
            <class 'sage.interfaces.kenzo.KenzoSimplicialSet'>
            sage: [w.homology(i) for i in range(6)]
            [Z, 0, Z, Z, 0, 0]
        """
    def join(self, other):
        """
        Return the join of ``self`` and ``other``.

        INPUT:

        - ``other`` -- the Kenzo simplicial set with which the join is made

        OUTPUT: a :class:`KenzoSimplicialSet`

        EXAMPLES::

            sage: # optional - kenzo
            sage: from sage.interfaces.kenzo import Sphere
            sage: s2 = Sphere(2)
            sage: s3 = Sphere(3)
            sage: j = s2.join(s3)
            sage: type(j)
            <class 'sage.interfaces.kenzo.KenzoSimplicialSet'>
            sage: [j.homology(i) for i in range(6)]
            [Z, 0, 0, 0, 0, 0]
        """
    def smash_product(self, other):
        """
        Return the smash product of ``self`` and ``other``.

        INPUT:

        - ``other`` -- the Kenzo simplicial set with which the smash product is made

        OUTPUT: a :class:`KenzoSimplicialSet`

        EXAMPLES::

            sage: # optional - kenzo
            sage: from sage.interfaces.kenzo import Sphere
            sage: s2 = Sphere(2)
            sage: s3 = Sphere(3)
            sage: s = s2.smash_product(s3)
            sage: type(s)
            <class 'sage.interfaces.kenzo.KenzoSimplicialSet'>
            sage: [s.homology(i) for i in range(6)]
            [Z, 0, 0, 0, 0, Z]
        """

class KenzoSimplicialGroup(KenzoSimplicialSet):
    """
    Wrapper around Kenzo simplicial groups.
    """
    def classifying_space(self):
        """
        Return the classifying space.

        OUTPUT: a :class:`KenzoSimplicialGroup`

        EXAMPLES::

            sage: # optional - kenzo
            sage: from sage.interfaces.kenzo import MooreSpace
            sage: m2 = MooreSpace(2,4)
            sage: l2 = m2.loop_space()
            sage: c = l2.classifying_space()
            sage: type(c)
            <class 'sage.interfaces.kenzo.KenzoSimplicialGroup'>
            sage: [c.homology(i) for i in range(8)]
            [Z, 0, 0, 0, C2, 0, 0, 0]
        """

def k2s_matrix(kmatrix):
    '''
    Convert an array of ECL to a matrix of Sage.

    INPUT:

    - ``kmatrix`` -- an array in ECL

    EXAMPLES::

        sage: from sage.interfaces.kenzo import k2s_matrix         # optional - kenzo
        sage: from sage.libs.ecl import EclObject
        sage: M = EclObject("#2A((1 2 3) (3 2 1) (1 1 1))")
        sage: k2s_matrix(M)                                        # optional - kenzo
        [1 2 3]
        [3 2 1]
        [1 1 1]
    '''
def s2k_matrix(smatrix):
    """
    Convert a matrix of Sage to an array of ECL.

    INPUT:

    - ``smatrix`` -- a matrix in Sage

    OUTPUT: a :class:`EclObject`

    EXAMPLES::

        sage: from sage.interfaces.kenzo import s2k_matrix      # optional - kenzo
        sage: A = Matrix([[1,2,3],[3,2,1],[1,1,1]])
        sage: s2k_matrix(A)                                     # optional - kenzo
        <ECL: #2A((1 2 3) (3 2 1) (1 1 1))>
    """
def s2k_dictmat(sdictmat):
    """
    Convert a dictionary in Sage, whose values are matrices, to an assoc list
    in ECL.

    INPUT:

    - ``sdictmat`` -- dictionary in Sage

    OUTPUT: a :class:`EclObject`

    EXAMPLES::

        sage: from sage.interfaces.kenzo import s2k_dictmat   # optional - kenzo
        sage: A = Matrix([[1,2,3],[3,2,1],[1,1,1]])
        sage: B = Matrix([[1,2],[2,1],[1,1]])
        sage: d = {1 : A, 2 : B}
        sage: s2k_dictmat(d)                                  # optional - kenzo
        <ECL: ((2 . #2A((1 2) (2 1) (1 1))) (1 . #2A((1 2 3) (3 2 1) (1 1 1))))>
    """
def pairing(slist):
    """
    Convert a list of Sage (which has an even length) to an assoc list in ECL.

    INPUT:

    - ``slist`` -- list in Sage

    OUTPUT: a :class:`EclObject`

    EXAMPLES::

        sage: from sage.interfaces.kenzo import pairing   # optional - kenzo
        sage: l = [1,2,3]
        sage: pairing(l)                                  # optional - kenzo
        <ECL: ((2 . 3))>
    """
def KChainComplex(chain_complex):
    """
    Construct a KenzoChainComplex from a ChainComplex of degree `-1` in
    Sage.

    INPUT:

    - ``chain_complex`` -- a ChainComplex of degree `-1`

    OUTPUT: a KenzoChainComplex

    EXAMPLES::

        sage: # optional - kenzo
        sage: from sage.interfaces.kenzo import KChainComplex
        sage: m1 = matrix(ZZ, 3, 2, [-1, 1, 3, -4, 5, 6])
        sage: m4 = matrix(ZZ, 2, 2, [1, 2, 3, 6])
        sage: m5 = matrix(ZZ, 2, 3, [2, 2, 2, -1, -1, -1])
        sage: sage_chcm = ChainComplex({1: m1, 4: m4, 5: m5}, degree = -1)
        sage: kenzo_chcm = KChainComplex(sage_chcm)
        sage: kenzo_chcm
        [K... Chain-Complex]
        sage: kenzo_chcm.homology(5)
        Z x Z
    """
def SChainComplex(kchaincomplex, start: int = 0, end: int = 15):
    """
    Convert the KenzoChainComplex ``kchcm`` (between dimensions ``start`` and
    ``end``) to a ChainComplex.

    INPUT:

    - ``kchaincomplex`` -- a KenzoChainComplex

    - ``start`` -- integer (default: 0)

    - ``end`` -- integer greater than or equal to ``start`` (default: 15)

    OUTPUT: a ChainComplex

    EXAMPLES::

        sage: from sage.interfaces.kenzo import KChainComplex, SChainComplex   # optional - kenzo
        sage: m1 = matrix(ZZ, 3, 2, [-1, 1, 3, -4, 5, 6])
        sage: m4 = matrix(ZZ, 2, 2, [1, 2, 3, 6])
        sage: m5 = matrix(ZZ, 2, 3, [2, 2, 2, -1, -1, -1])
        sage: sage_chcm = ChainComplex({1: m1, 4: m4, 5: m5}, degree = -1)     # optional - kenzo
        sage: SChainComplex(KChainComplex(sage_chcm)) == sage_chcm             # optional - kenzo
        True

    ::

        sage: # optional - kenzo
        sage: from sage.interfaces.kenzo import SChainComplex, Sphere
        sage: S4 = Sphere(4)
        sage: C = SChainComplex(S4)
        sage: C
        Chain complex with at most 3 nonzero terms over Integer Ring
        sage: C._ascii_art_()
        0 <-- C_4 <-- 0  ...  0 <-- C_0 <-- 0
        sage: [C.homology(i) for i in range(6)]
        [Z, 0, 0, 0, Z, 0]
    """
def SAbstractSimplex(simplex, dim):
    '''
    Convert an abstract simplex of Kenzo to an AbstractSimplex.

    INPUT:

    - ``simplex`` -- an abstract simplex of Kenzo

    - ``dim`` -- the dimension of ``simplex``

    OUTPUT: an AbstractSimplex

    EXAMPLES::

        sage: # optional - kenzo
        sage: from sage.libs.ecl import EclObject, ecl_eval
        sage: from sage.interfaces.kenzo import (
        ....:   KenzoObject, SAbstractSimplex)
        sage: KAbSm = KenzoObject(ecl_eval("(ABSM 15 \'K)"))
        sage: SAbSm1 = SAbstractSimplex(KAbSm, 2)
        sage: SAbSm2 = SAbstractSimplex(KAbSm, 7)
        sage: SAbSm1.degeneracies()
        [3, 2, 1, 0]
        sage: SAbSm1.dimension()
        6
        sage: SAbSm2.dimension()
        11
    '''
def KAbstractSimplex(simplex):
    """
    Convert an AbstractSimplex in Sage to an abstract simplex of Kenzo.

    INPUT:

    - ``simplex`` -- an AbstractSimplex

    OUTPUT: an abstract simplex of Kenzo

    EXAMPLES::

        sage: # optional - kenzo
        sage: from sage.topology.simplicial_set import AbstractSimplex
        sage: from sage.interfaces.kenzo import (
        ....:   KAbstractSimplex, SAbstractSimplex)
        sage: SAbSm = AbstractSimplex(1, (2,0,3,2,1), name = 'SAbSm')
        sage: KAbSm = KAbstractSimplex(SAbSm)
        sage: SAbSm2 = SAbstractSimplex(KAbSm, 1)
        sage: SAbSm.degeneracies() == SAbSm2.degeneracies()
        True
        sage: SAbSm.dimension() == SAbSm2.dimension()
        True
    """
def KFiniteSimplicialSet(sset):
    """
    Convert a finite SimplicialSet in Sage to a finite simplicial set of Kenzo.

    INPUT:

    - ``sset`` -- a finite SimplicialSet

    OUTPUT: a finite simplicial set of Kenzo

    EXAMPLES::

        sage: # optional - kenzo
        sage: from sage.topology.simplicial_set import AbstractSimplex, SimplicialSet
        sage: from sage.interfaces.kenzo import KFiniteSimplicialSet
        sage: s0 = AbstractSimplex(0, name='s0')
        sage: s1 = AbstractSimplex(0, name='s1')
        sage: s2 = AbstractSimplex(0, name='s2')
        sage: s01 = AbstractSimplex(1, name='s01')
        sage: s02 = AbstractSimplex(1, name='s02')
        sage: s12 = AbstractSimplex(1, name='s12')
        sage: s012 = AbstractSimplex(2, name='s012')
        sage: Triangle = SimplicialSet({s01: (s1, s0),\\\n        ....: s02: (s2, s0), s12: (s2, s1)}, base_point = s0)
        sage: KTriangle = KFiniteSimplicialSet(Triangle)
        sage: KTriangle.homology(1)
        Z
        sage: KTriangle.basis(1)
        ['CELL_1_0', 'CELL_1_1', 'CELL_1_2']
        sage: S1 = simplicial_sets.Sphere(1)
        sage: S3 = simplicial_sets.Sphere(3)
        sage: KS1vS3 = KFiniteSimplicialSet(S1.wedge(S3))
        sage: KS1vS3.homology(3)
        Z
    """
def SFiniteSimplicialSet(ksimpset, limit):
    """
    Convert the ``limit``-skeleton of a finite simplicial set in Kenzo to a
    finite SimplicialSet in Sage.

    INPUT:

    - ``ksimpset`` -- a finite simplicial set in Kenzo

    - ``limit`` -- a natural number

    OUTPUT: a finite SimplicialSet

    EXAMPLES::

        sage: # optional - kenzo
        sage: from sage.topology.simplicial_set import SimplicialSet
        sage: from sage.interfaces.kenzo import (
        ....:   AbstractSimplex, KFiniteSimplicialSet,
        ....:   SFiniteSimplicialSet, Sphere)
        sage: s0 = AbstractSimplex(0, name='s0')
        sage: s1 = AbstractSimplex(0, name='s1')
        sage: s2 = AbstractSimplex(0, name='s2')
        sage: s01 = AbstractSimplex(1, name='s01')
        sage: s02 = AbstractSimplex(1, name='s02')
        sage: s12 = AbstractSimplex(1, name='s12')
        sage: s012 = AbstractSimplex(2, name='s012')
        sage: Triangle = SimplicialSet({s01: (s1, s0),
        ....:                           s02: (s2, s0),
        ....:                           s12: (s2, s1)},
        ....:                          base_point = s0)
        sage: KTriangle = KFiniteSimplicialSet(Triangle)
        sage: STriangle = SFiniteSimplicialSet(KTriangle, 1)
        sage: STriangle.homology()
        {0: 0, 1: Z}
        sage: S1 = simplicial_sets.Sphere(1)
        sage: S3 = simplicial_sets.Sphere(3)
        sage: KS1vS3 = KFiniteSimplicialSet(S1.wedge(S3))
        sage: SS1vS3 = SFiniteSimplicialSet(KS1vS3, 3)
        sage: SS1vS3.homology()
        {0: 0, 1: Z, 2: 0, 3: Z}
    """

class KenzoChainComplexMorphism(KenzoObject):
    """
    Wrapper to Kenzo morphisms between chain complexes.
    """
    def source_complex(self):
        """
        Return the source chain complex of the morphism.

        OUTPUT: a :class:`KenzoChainComplex`

        EXAMPLES::

            sage: # optional - kenzo
            sage: from sage.interfaces.kenzo import KChainComplex
            sage: m1 = matrix(ZZ, 3, 2, [-1, 1, 3, -4, 5, 6])
            sage: m4 = matrix(ZZ, 2, 2, [1, 2, 3, 6])
            sage: m5 = matrix(ZZ, 2, 3, [2, 2, 2, -1, -1, -1])
            sage: sage_chcm = ChainComplex({1: m1, 4: m4, 5: m5}, degree = -1)
            sage: kenzo_chcm = KChainComplex(sage_chcm)
            sage: kenzo_chcm
            [K... Chain-Complex]
            sage: differential_morphism = kenzo_chcm.differential()
            sage: differential_morphism
            [K... Morphism (degree -1): K... -> K...]
            sage: differential_morphism.source_complex()
            [K... Chain-Complex]
        """
    def target_complex(self):
        """
        Return the target chain complex of the morphism.

        OUTPUT: a :class:`KenzoChainComplex`

        EXAMPLES::

            sage: # optional - kenzo
            sage: from sage.interfaces.kenzo import KChainComplex
            sage: m1 = matrix(ZZ, 3, 2, [-1, 1, 3, -4, 5, 6])
            sage: m4 = matrix(ZZ, 2, 2, [1, 2, 3, 6])
            sage: m5 = matrix(ZZ, 2, 3, [2, 2, 2, -1, -1, -1])
            sage: sage_chcm = ChainComplex({1: m1, 4: m4, 5: m5}, degree = -1)
            sage: kenzo_chcm = KChainComplex(sage_chcm)
            sage: kenzo_chcm
            [K... Chain-Complex]
            sage: differential_morphism = kenzo_chcm.differential()
            sage: differential_morphism
            [K... Morphism (degree -1): K... -> K...]
            sage: differential_morphism.target_complex()
            [K... Chain-Complex]
        """
    def degree(self):
        """
        Return the degree of the morphism.

        OUTPUT: integer; the degree of the morphism

        EXAMPLES::

            sage: # optional - kenzo
            sage: from sage.interfaces.kenzo import KChainComplex
            sage: m1 = matrix(ZZ, 3, 2, [-1, 1, 3, -4, 5, 6])
            sage: m4 = matrix(ZZ, 2, 2, [1, 2, 3, 6])
            sage: m5 = matrix(ZZ, 2, 3, [2, 2, 2, -1, -1, -1])
            sage: sage_chcm = ChainComplex({1: m1, 4: m4, 5: m5}, degree=-1)
            sage: kenzo_chcm = KChainComplex(sage_chcm)
            sage: kenzo_chcm
            [K... Chain-Complex]
            sage: differential_morphism = kenzo_chcm.differential()
            sage: differential_morphism
            [K... Morphism (degree -1): K... -> K...]
            sage: differential_morphism.degree()
            -1
            sage: differential_morphism.composite(differential_morphism).degree()
            -2
            sage: kenzo_chcm.null_morphism().degree()
            0
        """
    def evaluation(self, dim, comb):
        """
        Apply the morphism on a combination ``comb`` of dimension ``dim``.

        INPUT:

        - ``dim`` -- integer

        - ``comb`` -- list representing a formal sum of generators in the module
          of dimension ``dim``. For example, to represent G7G12 + 3*G7G0 - 5*G7G3
          we use the list [3, 'G7G0', -5, 'G7G3', 1, 'G7G12']. Note that the
          generators must be in ascending order respect to the number after the
          second G in their representation; the parameter
          ``comb`` = [1, 'G7G12', 3, 'G7G0', -5, 'G7G3'] will produce an error in
          Kenzo.

        OUTPUT:

        - A Kenzo combination representing the result of applying the morphism on the formal
          combination represented by ``comb`` in the chain complex ``self`` in
          dimension ``dim``.

        EXAMPLES::

            sage: # optional - kenzo
            sage: from sage.interfaces.kenzo import KChainComplex
            sage: m1 = matrix(ZZ, 3, 2, [-1, 1, 3, -4, 5, 6])
            sage: m4 = matrix(ZZ, 2, 2, [1, 2, 3, 6])
            sage: m5 = matrix(ZZ, 2, 3, [2, 2, 2, -1, -1, -1])
            sage: sage_chcm = ChainComplex({1: m1, 4: m4, 5: m5}, degree = -1)
            sage: kenzo_chcm = KChainComplex(sage_chcm)
            sage: kenzo_chcm
            [K... Chain-Complex]
            sage: differential_morphism = kenzo_chcm.differential()
            sage: differential_morphism
            [K... Morphism (degree -1): K... -> K...]
            sage: dif_squared = differential_morphism.composite(differential_morphism)
            sage: dif_squared
            [K... Morphism (degree -2): K... -> K...]
            sage: kenzo_chcm.basis(5)
            ['G5G0', 'G5G1', 'G5G2']
            sage: kenzo_chcm.differential(5, [1, 'G5G0', 2, 'G5G2'])
            <BLANKLINE>
            ----------------------------------------------------------------------{CMBN 4}
            <6 * G4G0>
            <-3 * G4G1>
            ------------------------------------------------------------------------------
            <BLANKLINE>
            sage: differential_morphism.evaluation(5, [1, 'G5G0', 2, 'G5G2'])
            <BLANKLINE>
            ----------------------------------------------------------------------{CMBN 4}
            <6 * G4G0>
            <-3 * G4G1>
            ------------------------------------------------------------------------------
            <BLANKLINE>
            sage: dif_squared.evaluation(5, [1, 'G5G0', 2, 'G5G2'])
            <BLANKLINE>
            ----------------------------------------------------------------------{CMBN 3}
            ------------------------------------------------------------------------------
            <BLANKLINE>
            sage: idnt = kenzo_chcm.identity_morphism()
            sage: idx2 = idnt.sum(idnt)
            sage: idnt.evaluation(5, [1, 'G5G0', 2, 'G5G2'])
            <BLANKLINE>
            ----------------------------------------------------------------------{CMBN 5}
            <1 * G5G0>
            <2 * G5G2>
            ------------------------------------------------------------------------------
            <BLANKLINE>
            sage: idx2.evaluation(5, [1, 'G5G0', 2, 'G5G2'])
            <BLANKLINE>
            ----------------------------------------------------------------------{CMBN 5}
            <2 * G5G0>
            <4 * G5G2>
            ------------------------------------------------------------------------------
            <BLANKLINE>
        """
    def opposite(self):
        """
        Return the opposite morphism of ``self``, i.e., -1 x ``self``.

        OUTPUT: a :class:`KenzoChainComplexMorphism`

        EXAMPLES::

            sage: # optional - kenzo
            sage: from sage.interfaces.kenzo import KChainComplex
            sage: m1 = matrix(ZZ, 3, 2, [-1, 1, 3, -4, 5, 6])
            sage: m4 = matrix(ZZ, 2, 2, [1, 2, 3, 6])
            sage: m5 = matrix(ZZ, 2, 3, [2, 2, 2, -1, -1, -1])
            sage: sage_chcm = ChainComplex({1: m1, 4: m4, 5: m5}, degree = -1)
            sage: kenzo_chcm = KChainComplex(sage_chcm)
            sage: kenzo_chcm
            [K... Chain-Complex]
            sage: idnt = kenzo_chcm.identity_morphism()
            sage: idnt
            [K... Morphism (degree 0): K... -> K...]
            sage: opps_id = idnt.opposite()
            sage: opps_id
            [K... Morphism (degree 0): K... -> K...]
            sage: kenzo_chcm.basis(4)
            ['G4G0', 'G4G1']
            sage: idnt.evaluation(4, [2, 'G4G0', -5, 'G4G1'])
            <BLANKLINE>
            ----------------------------------------------------------------------{CMBN 4}
            <2 * G4G0>
            <-5 * G4G1>
            ------------------------------------------------------------------------------
            <BLANKLINE>
            sage: opps_id.evaluation(4, [2, 'G4G0', -5, 'G4G1'])
            <BLANKLINE>
            ----------------------------------------------------------------------{CMBN 4}
            <-2 * G4G0>
            <5 * G4G1>
            ------------------------------------------------------------------------------
            <BLANKLINE>
        """
    def composite(self, object=None):
        """
        Return the composite of ``self`` and the morphism(s) given by the parameter ``object``.

        INPUT:

        - ``object`` -- a KenzoChainComplexMorphism instance, a
          KenzoChainComplex instance, a tuple of KenzoChainComplexMorphism and
          KenzoChainComplex instances, or ``None`` (default).

        OUTPUT:

        - A :class:`KenzoChainComplexMorphism`: if ``object`` is a KenzoChainComplexMorphism, the
          composite of ``self`` and ``object`` is returned; if ``object`` is a KenzoChainComplex,
          the composite of ``self`` and the differential morphism of ``object`` is returned; if
          ``object`` is a tuple, the composite of ``self`` and the morphisms or the differential
          morphisms of the given chain complexes in ``object`` is returned (if ``object`` is
          ``None``, ``self`` morphism is returned).

        EXAMPLES::

            sage: # optional - kenzo
            sage: from sage.interfaces.kenzo import Sphere
            sage: s2 = Sphere(2)
            sage: s3 = Sphere(3)
            sage: tp22 = s2.tensor_product(s2)
            sage: tp23 = s2.tensor_product(s3)
            sage: idnt = tp22.identity_morphism()
            sage: idnt
            [K... Morphism (degree 0): K... -> K...]
            sage: null = tp23.null_morphism(target = tp22, degree = 4)
            sage: null
            [K... Morphism (degree 4): K... -> K...]
            sage: idnt.composite((tp22, null))
            [K... Morphism (degree 3): K... -> K...]
        """
    def sum(self, object=None):
        """
        Return a morphism, sum of the morphism ``self`` and the morphism(s) given
        by the parameter ``object``.

        INPUT:

        - ``object`` -- a KenzoChainComplexMorphism instance, a tuple of
          KenzoChainComplexMorphism instances or ``None`` (default)

        OUTPUT:

        A :class:`KenzoChainComplexMorphism`, sum of the morphism ``self``
        and the morphism(s given by ``object`` (if ``object`` is ``None``,
        ``self`` morphism is returned).

        EXAMPLES::

            sage: # optional - kenzo
            sage: from sage.interfaces.kenzo import KChainComplex
            sage: m1 = matrix(ZZ, 3, 2, [-1, 1, 3, -4, 5, 6])
            sage: m4 = matrix(ZZ, 2, 2, [1, 2, 3, 6])
            sage: m5 = matrix(ZZ, 2, 3, [2, 2, 2, -1, -1, -1])
            sage: sage_chcm = ChainComplex({1: m1, 4: m4, 5: m5}, degree = -1)
            sage: kenzo_chcm = KChainComplex(sage_chcm)
            sage: kenzo_chcm
            [K... Chain-Complex]
            sage: idnt = kenzo_chcm.identity_morphism()
            sage: idnt
            [K... Morphism (degree 0): K... -> K...]
            sage: opps_id = idnt.opposite()
            sage: opps_id
            [K... Morphism (degree 0): K... -> K...]
            sage: null = kenzo_chcm.null_morphism()
            sage: null
            [K... Morphism (degree 0): K... -> K...]
            sage: idx2 = idnt.sum(idnt)
            sage: idx5 = idx2.sum(
            ....:   (opps_id, idnt, idnt, null, idx2.sum(idnt), opps_id))
            sage: kenzo_chcm.basis(4)
            ['G4G0', 'G4G1']
            sage: idx2.evaluation(4, [2, 'G4G0', -5, 'G4G1'])
            <BLANKLINE>
            ----------------------------------------------------------------------{CMBN 4}
            <4 * G4G0>
            <-10 * G4G1>
            ------------------------------------------------------------------------------
            <BLANKLINE>
            sage: idx5.evaluation(4, [2, 'G4G0', -5, 'G4G1'])
            <BLANKLINE>
            ----------------------------------------------------------------------{CMBN 4}
            <10 * G4G0>
            <-25 * G4G1>
            ------------------------------------------------------------------------------
            <BLANKLINE>
        """
    def substract(self, object=None):
        """
        Return a morphism, difference of the morphism ``self`` and the
        morphism(s) given by the parameter ``object``.

        INPUT:

        - ``object`` -- a KenzoChainComplexMorphism instance, a tuple of
          KenzoChainComplexMorphism instances or ``None`` (default)

        OUTPUT:

        A :class:`KenzoChainComplexMorphism`, difference of the morphism
        ``self`` and the morphism(s) given by ``object`` (if ``object`` is
        ``None``, ``self`` morphism is returned). For example, if ``object`` =
        (mrph1, mrph2, mrph3) the result is ``self`` - mrph1 - mrph2 - mrph3.

        EXAMPLES::

            sage: # optional - kenzo
            sage: from sage.interfaces.kenzo import KChainComplex
            sage: m1 = matrix(ZZ, 3, 2, [-1, 1, 3, -4, 5, 6])
            sage: m4 = matrix(ZZ, 2, 2, [1, 2, 3, 6])
            sage: m5 = matrix(ZZ, 2, 3, [2, 2, 2, -1, -1, -1])
            sage: sage_chcm = ChainComplex({1: m1, 4: m4, 5: m5}, degree = -1)
            sage: kenzo_chcm = KChainComplex(sage_chcm)
            sage: kenzo_chcm
            [K... Chain-Complex]
            sage: idnt = kenzo_chcm.identity_morphism()
            sage: idnt
            [K... Morphism (degree 0): K... -> K...]
            sage: opps_id = idnt.opposite()
            sage: opps_id
            [K... Morphism (degree 0): K... -> K...]
            sage: null = kenzo_chcm.null_morphism()
            sage: null
            [K... Morphism (degree 0): K... -> K...]
            sage: idx2 = idnt.substract(opps_id)
            sage: opps_idx2 = idx2.substract(
            ....:   (opps_id, idnt, idnt, null, idx2.substract(opps_id)))
            sage: kenzo_chcm.basis(4)
            ['G4G0', 'G4G1']
            sage: idx2.evaluation(4, [2, 'G4G0', -5, 'G4G1'])
            <BLANKLINE>
            ----------------------------------------------------------------------{CMBN 4}
            <4 * G4G0>
            <-10 * G4G1>
            ------------------------------------------------------------------------------
            <BLANKLINE>
            sage: opps_idx2.evaluation(4, [2, 'G4G0', -5, 'G4G1'])
            <BLANKLINE>
            ----------------------------------------------------------------------{CMBN 4}
            <-4 * G4G0>
            <10 * G4G1>
            ------------------------------------------------------------------------------
            <BLANKLINE>
        """
    def change_source_target_complex(self, source=None, target=None):
        '''
        Build, from the morphism ``self``, a new morphism with ``source``
        and ``target`` as source and target Kenzo chain complexes.

        INPUT:

        - ``source`` -- a KenzoChainComplex instance or ``None`` (default)

        - ``target`` -- a KenzoChainComplex instance or ``None`` (default)

        OUTPUT:

        - A :class:`KenzoChainComplexMorphism` inheriting from ``self`` the
          degree (:degr slot in Kenzo), the algorithm (:intr slot in Kenzo)
          and the strategy (:strt slot in Kenzo). The source and target slots
          of this new morphism are given by the parameters ``source`` and
          ``target`` respectively; if any parameter is omitted,
          the corresponding slot is inherited from ``self``.

        EXAMPLES::

            sage: # optional - kenzo
            sage: from sage.interfaces.kenzo import Sphere, KenzoChainComplex
            sage: from sage.libs.ecl import ecl_eval
            sage: ZCC = KenzoChainComplex(ecl_eval("(z-chcm)"))
            sage: ZCC
            [K... Chain-Complex]
            sage: s2 = Sphere(2)
            sage: s3 = Sphere(3)
            sage: tp = s2.tensor_product(s3)
            sage: tp
            [K... Filtered-Chain-Complex]
            sage: null = ZCC.null_morphism(tp)
            sage: null
            [K... Morphism (degree 0): K... -> K...]
            sage: null.source_complex()
            [K... Chain-Complex]
            sage: null2 = null.change_source_target_complex(source = tp)
            sage: null2
            [K... Morphism (degree 0): K... -> K...]
            sage: null2.source_complex()
            [K... Filtered-Chain-Complex]
        '''
    def destructive_change_source_target_complex(self, source=None, target=None):
        '''
        Modify destructively the morphism ``self`` taking ``source``
        and ``target`` as source and target Kenzo chain complexes of ``self``.

        INPUT:

        - ``source`` -- a KenzoChainComplex instance or ``None`` (default)

        - ``target`` -- a KenzoChainComplex instance or ``None`` (default)

        OUTPUT:

        - A :class:`KenzoChainComplexMorphism`. The source and target
          slots of ``self`` are replaced respectively by the
          parameters ``source`` and ``target``; if any parameter is
          omitted, the corresponding slot is inherited from ``self``.

        EXAMPLES::

            sage: # optional - kenzo
            sage: from sage.interfaces.kenzo import Sphere, KenzoChainComplex
            sage: from sage.libs.ecl import ecl_eval
            sage: ZCC = KenzoChainComplex(ecl_eval("(z-chcm)"))
            sage: ZCC
            [K... Chain-Complex]
            sage: s2 = Sphere(2)
            sage: s3 = Sphere(3)
            sage: tp = s2.tensor_product(s3)
            sage: tp
            [K... Filtered-Chain-Complex]
            sage: null = ZCC.null_morphism(tp)
            sage: null
            [K... Morphism (degree 0): K... -> K...]
            sage: null.target_complex()
            [K... Filtered-Chain-Complex]
            sage: null.destructive_change_source_target_complex(target = ZCC)
            [K... Cohomology-Class on K... of degree 0]
            sage: null.target_complex()
            [K... Chain-Complex]
        '''

def build_morphism(source_complex, target_complex, degree, algorithm, strategy, orgn):
    '''
    Build a morphism of chain complexes by means of the corresponding build-mrph Kenzo
    function.

    INPUT:

    - ``source_complex`` -- the source object as a KenzoChainComplex instance

    - ``target_complex`` -- the target object as a KenzoChainComplex instance

    - ``degree`` -- integer representing the degree of the morphism

    - ``algorithm`` -- a Lisp function defining the mapping (:intr slot in Kenzo)

    - ``strategy`` -- the strategy (:strt slot in Kenzo), which must be one of
      the two strings ``gnrt`` or ``cmbn``, depending if the ``algorithm`` (a Lisp
      function) uses as arguments a degree and a generator or a combination,
      respectively.

    - ``orgn`` -- list containing a description about the origin of the morphism

    OUTPUT: a :class:`KenzoChainComplexMorphism`

    EXAMPLES::

        sage: # optional - kenzo
        sage: from sage.interfaces.kenzo import (KenzoChainComplex,
        ....:                                    build_morphism)
        sage: from sage.libs.ecl import ecl_eval
        sage: ZCC = KenzoChainComplex(ecl_eval("(z-chcm)"))
        sage: A = build_morphism(
        ....:   ZCC, ZCC, -1,
        ....:   ecl_eval("#\'(lambda (comb) (cmbn (1- (degr comb))))"),
        ....:   "cmbn", ["zero morphism on ZCC"])
        sage: A.target_complex()
        [K... Chain-Complex]
        sage: A.degree()
        -1
        sage: type(A)
        <class \'sage.interfaces.kenzo.KenzoChainComplexMorphism\'>
    '''
def morphism_dictmat(morphism):
    """
    Compute a list of matrices in ECL associated to a morphism in Sage.

    INPUT:

    - ``morphism`` -- a morphism of chain complexes

    OUTPUT: a :class:`EclObject`

    EXAMPLES::

        sage: from sage.interfaces.kenzo import morphism_dictmat    # optional - kenzo
        sage: X = simplicial_complexes.Simplex(1)
        sage: Y = simplicial_complexes.Simplex(0)
        sage: g = Hom(X,Y)({0:0, 1:0})
        sage: f = g.associated_chain_complex_morphism()
        sage: morphism_dictmat(f)                                   # optional - kenzo
        <ECL: ((2 . #2A()) (1 . #2A()) (0 . #2A((1 1))))>
    """
def KChainComplexMorphism(morphism):
    """
    Construct a KenzoChainComplexMorphism from a ChainComplexMorphism in Sage.

    INPUT:

    - ``morphism`` -- a morphism of chain complexes

    OUTPUT: a :class:`KenzoChainComplexMorphism`

    EXAMPLES::

        sage: # optional - kenzo
        sage: from sage.interfaces.kenzo import KChainComplexMorphism
        sage: C = ChainComplex({0: identity_matrix(ZZ, 1)})
        sage: D = ChainComplex({0: zero_matrix(ZZ, 1), 1: zero_matrix(ZZ, 1)})
        sage: f = Hom(C,D)({0: identity_matrix(ZZ, 1), 1: zero_matrix(ZZ, 1)})
        sage: g = KChainComplexMorphism(f); g
        [K... Morphism (degree 0): K... -> K...]
        sage: g.source_complex()
        [K... Chain-Complex]
        sage: g.target_complex()
        [K... Chain-Complex]
    """
def s2k_listofmorphisms(l):
    """
    Compute a list of morphisms of chain complexes in Kenzo from a list of morphisms in Sage.

    INPUT:

    - ``l`` -- list of morphisms of chain complexes

    OUTPUT: a :class:`EclObject`

    EXAMPLES::

        sage: from sage.interfaces.kenzo import s2k_listofmorphisms  # optional - kenzo
        sage: C1 = ChainComplex({1: matrix(ZZ, 0, 2, [])}, degree_of_differential=-1)
        sage: C2 = ChainComplex({1: matrix(ZZ, 1, 2, [1, 0])},degree_of_differential=-1)
        sage: C3 = ChainComplex({0: matrix(ZZ, 0,2 , [])},degree_of_differential=-1)
        sage: M1 = Hom(C2,C1)({1: matrix(ZZ, 2, 2, [2, 0, 0, 2])})
        sage: M2 = Hom(C3,C2)({0: matrix(ZZ, 1, 2, [2, 0])})
        sage: l = [M1, M2]
        sage: s2k_listofmorphisms(l)                                 # optional - kenzo
        <ECL: ([K... Morphism (degree 0): K... -> K...] [K... Morphism (degree 0): K... -> K...])>
    """
def BicomplexSpectralSequence(l):
    """
    Construct the spectral sequence associated to the bicomplex given by a list of morphisms.

    INPUT:

    - ``l`` -- list of morphisms of chain complexes

    OUTPUT: a :class:`KenzoSpectralSequence`

    EXAMPLES::

        sage: # optional - kenzo
        sage: from sage.interfaces.kenzo import BicomplexSpectralSequence
        sage: C1 = ChainComplex({1: matrix(ZZ, 0, 2, [])}, degree_of_differential=-1)
        sage: C2 = ChainComplex({1: matrix(ZZ, 1, 2, [1, 0])},degree_of_differential=-1)
        sage: C3 = ChainComplex({0: matrix(ZZ, 0,2 , [])},degree_of_differential=-1)
        sage: M1 = Hom(C2,C1)({1: matrix(ZZ, 2, 2, [2, 0, 0, 2])})
        sage: M2 = Hom(C3,C2)({0: matrix(ZZ, 1, 2, [2, 0])})
        sage: l = [M1, M2]
        sage: E = BicomplexSpectralSequence(l)
        sage: E.group(2,0,1)
        Additive abelian group isomorphic to Z/2 + Z
        sage: E.table(3,0,2,0,2)
        0           0   0
        Z/2 + Z/4   0   0
        0           0   Z
        sage: E.matrix(2,2,0)
        [ 0  0]
        [-4  0]
    """
