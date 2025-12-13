from sage.categories.homset import HomsetWithBase as HomsetWithBase
from sage.matrix.constructor import identity_matrix as identity_matrix, matrix as matrix
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.modular.abvar import morphism as morphism
from sage.rings.infinity import Infinity as Infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.all import parent as parent
from sage.structure.element import Matrix as Matrix
from sage.structure.parent import Parent as Parent

class Homspace(HomsetWithBase):
    """
    A space of homomorphisms between two modular abelian varieties.
    """
    Element = morphism.Morphism
    def __init__(self, domain, codomain, cat) -> None:
        """
        Create a homspace.

        INPUT:

        - ``domain, codomain`` -- modular abelian varieties

        - ``cat`` -- category

        EXAMPLES::

            sage: H = Hom(J0(11), J0(22)); H
            Space of homomorphisms from Abelian variety J0(11) of dimension 1
             to Abelian variety J0(22) of dimension 2
            sage: Hom(J0(11), J0(11))
            Endomorphism ring of Abelian variety J0(11) of dimension 1
            sage: type(H)
            <class 'sage.modular.abvar.homspace.Homspace_with_category'>
            sage: H.homset_category()
            Category of modular abelian varieties over Rational Field
        """
    def identity(self):
        """
        Return the identity endomorphism.

        EXAMPLES::

            sage: E = End(J0(11))
            sage: E.identity()
            Abelian variety endomorphism of Abelian variety J0(11) of dimension 1
            sage: E.one()
            Abelian variety endomorphism of Abelian variety J0(11) of dimension 1

            sage: H = Hom(J0(11), J0(22))
            sage: H.identity()
            Traceback (most recent call last):
            ...
            TypeError: the identity map is only defined for endomorphisms
        """
    def __call__(self, M, **kwds):
        """
        Create a homomorphism in this space from M. M can be any of the
        following:

        - a Morphism of abelian varieties

        - a matrix of the appropriate size
          (i.e. 2\\*self.domain().dimension() x
          2\\*self.codomain().dimension()) whose entries are coercible
          into self.base_ring()

        - anything that can be coerced into self.matrix_space()

        EXAMPLES::

            sage: H = Hom(J0(11), J0(22))
            sage: phi = H(matrix(ZZ,2,4,[5..12])) ; phi
            Abelian variety morphism:
              From: Abelian variety J0(11) of dimension 1
              To:   Abelian variety J0(22) of dimension 2
            sage: phi.matrix()
            [ 5  6  7  8]
            [ 9 10 11 12]
            sage: phi.matrix().parent()
            Full MatrixSpace of 2 by 4 dense matrices over Integer Ring

        ::

            sage: H = J0(22).Hom(J0(11)*J0(11))
            sage: m1 = J0(22).degeneracy_map(11,1).matrix() ; m1
            [ 0  1]
            [-1  1]
            [-1  0]
            [ 0 -1]
            sage: m2 = J0(22).degeneracy_map(11,2).matrix() ; m2
            [ 1 -2]
            [ 0 -2]
            [ 1 -1]
            [ 0 -1]
            sage: m = m1.transpose().stack(m2.transpose()).transpose() ; m
            [ 0  1  1 -2]
            [-1  1  0 -2]
            [-1  0  1 -1]
            [ 0 -1  0 -1]
            sage: phi = H(m) ; phi
            Abelian variety morphism:
              From: Abelian variety J0(22) of dimension 2
              To:   Abelian variety J0(11) x J0(11) of dimension 2
            sage: phi.matrix()
            [ 0  1  1 -2]
            [-1  1  0 -2]
            [-1  0  1 -1]
            [ 0 -1  0 -1]
        """
    def free_module(self):
        """
        Return this endomorphism ring as a free submodule of a big
        `\\ZZ^{4nm}`, where `n` is the dimension of
        the domain abelian variety and `m` the dimension of the
        codomain.

        OUTPUT: free module

        EXAMPLES::

            sage: E = Hom(J0(11), J0(22))
            sage: E.free_module()
            Free module of degree 8 and rank 2 over Integer Ring
            Echelon basis matrix:
            [ 1  0 -3  1  1  1 -1 -1]
            [ 0  1 -3  1  1  1 -1  0]
        """
    def gen(self, i: int = 0):
        """
        Return `i`-th generator of ``self``.

        INPUT:

        - ``i`` -- integer

        OUTPUT: a morphism

        EXAMPLES::

            sage: E = End(J0(22))
            sage: E.gen(0).matrix()
            [1 0 0 0]
            [0 1 0 0]
            [0 0 1 0]
            [0 0 0 1]
        """
    def ngens(self):
        """
        Return number of generators of ``self``.

        OUTPUT: integer

        EXAMPLES::

            sage: E = End(J0(22))
            sage: E.ngens()
            4
        """
    def gens(self) -> tuple:
        """
        Return tuple of generators for this endomorphism ring.

        EXAMPLES::

            sage: E = End(J0(22))
            sage: E.gens()
            (Abelian variety endomorphism of Abelian variety J0(22) of dimension 2,
             Abelian variety endomorphism of Abelian variety J0(22) of dimension 2,
             Abelian variety endomorphism of Abelian variety J0(22) of dimension 2,
             Abelian variety endomorphism of Abelian variety J0(22) of dimension 2)
        """
    def matrix_space(self):
        """
        Return the underlying matrix space that we view this endomorphism
        ring as being embedded into.

        EXAMPLES::

            sage: E = End(J0(22))
            sage: E.matrix_space()
            Full MatrixSpace of 4 by 4 dense matrices over Integer Ring
        """
    def calculate_generators(self) -> None:
        """
        If generators haven't already been computed, calculate generators
        for this homspace. If they have been computed, do nothing.

        EXAMPLES::

            sage: E = End(J0(11))
            sage: E.calculate_generators()
        """

class EndomorphismSubring(Homspace):
    def __init__(self, A, gens=None, category=None) -> None:
        '''
        A subring of the endomorphism ring.

        INPUT:

        - ``A`` -- an abelian variety

        - ``gens`` -- (default: ``None``) if given
          should be a tuple of the generators as matrices

        EXAMPLES::

            sage: J0(23).endomorphism_ring()
            Endomorphism ring of Abelian variety J0(23) of dimension 2
            sage: sage.modular.abvar.homspace.EndomorphismSubring(J0(25))
            Endomorphism ring of Abelian variety J0(25) of dimension 0
            sage: E = J0(11).endomorphism_ring()
            sage: type(E)
            <class \'sage.modular.abvar.homspace.EndomorphismSubring_with_category\'>
            sage: E.homset_category()
            Category of modular abelian varieties over Rational Field
            sage: E.category()
            Category of endsets of modular abelian varieties over Rational Field
            sage: E in Rings()
            True
            sage: TestSuite(E).run(skip=["_test_prod"])

        TESTS:

        The following tests against a problem on 32 bit machines that
        occurred while working on :issue:`9944`::

            sage: sage.modular.abvar.homspace.EndomorphismSubring(J1(12345))
            Endomorphism ring of Abelian variety J1(12345) of dimension 5405473

        :issue:`16275` removed the custom ``__reduce__`` method, since
        :meth:`Homset.__reduce__` already implements appropriate
        unpickling by construction::

            sage: E.__reduce__.__module__
            \'sage.categories.homset\'
            sage: E.__reduce__()
            (<function Hom at ...>,
             (Abelian variety J0(11) of dimension 1,
              Abelian variety J0(11) of dimension 1,
              Category of modular abelian varieties over Rational Field,
             False))
        '''
    def abelian_variety(self):
        """
        Return the abelian variety that this endomorphism ring is attached
        to.

        EXAMPLES::

            sage: J0(11).endomorphism_ring().abelian_variety()
            Abelian variety J0(11) of dimension 1
        """
    def index_in(self, other, check: bool = True):
        """
        Return the index of ``self`` in ``other``.

        INPUT:

        - ``other`` -- another endomorphism subring of the
          same abelian variety

        - ``check`` -- boolean (default: ``True``); whether to do some
          type and other consistency checks

        EXAMPLES::

            sage: R = J0(33).endomorphism_ring()
            sage: R.index_in(R)
            1
            sage: J = J0(37) ; E = J.endomorphism_ring() ; T = E.image_of_hecke_algebra()
            sage: T.index_in(E)
            1
            sage: J = J0(22) ; E = J.endomorphism_ring() ; T = E.image_of_hecke_algebra()
            sage: T.index_in(E)
            +Infinity
        """
    def index_in_saturation(self):
        """
        Given a Hecke algebra T, compute its index in its saturation.

        EXAMPLES::

            sage: End(J0(23)).image_of_hecke_algebra().index_in_saturation()
            1
            sage: End(J0(44)).image_of_hecke_algebra().index_in_saturation()
            2
        """
    def discriminant(self):
        """
        Return the discriminant of this ring, which is the discriminant of
        the trace pairing.

        .. NOTE::

           One knows that for modular abelian varieties, the
           endomorphism ring should be isomorphic to an order in a
           number field. However, the discriminant returned by this
           function will be `2^n` ( `n =`
           self.dimension()) times the discriminant of that order,
           since the elements are represented as 2d x 2d
           matrices. Notice, for example, that the case of a one
           dimensional abelian variety, whose endomorphism ring must
           be ZZ, has discriminant 2, as in the example below.

        EXAMPLES::

            sage: J0(33).endomorphism_ring().discriminant()
            -64800
            sage: J0(46).endomorphism_ring().discriminant()  # long time (6s on sage.math, 2011)
            24200000000
            sage: J0(11).endomorphism_ring().discriminant()
            2
        """
    def image_of_hecke_algebra(self, check_every: int = 1):
        """
        Compute the image of the Hecke algebra inside this endomorphism
        subring.

        We simply calculate Hecke operators up to the Sturm bound, and look
        at the submodule spanned by them. While computing, we can check to
        see if the submodule spanned so far is saturated and of maximal
        dimension, in which case we may be done. The optional argument
        check_every determines how many Hecke operators we add in before
        checking to see if this condition is met.

        INPUT:

        - ``check_every`` -- integer (default: 1); if this integer is positive,
          this integer determines how many Hecke operators we add in before
          checking to see if the submodule spanned so far is maximal and
          saturated

        OUTPUT: the image of the Hecke algebra as a subring of ``self``

        EXAMPLES::

            sage: E = J0(33).endomorphism_ring()
            sage: E.image_of_hecke_algebra()
            Subring of endomorphism ring of Abelian variety J0(33) of dimension 3
            sage: E.image_of_hecke_algebra().gens()
            (Abelian variety endomorphism of Abelian variety J0(33) of dimension 3,
             Abelian variety endomorphism of Abelian variety J0(33) of dimension 3,
             Abelian variety endomorphism of Abelian variety J0(33) of dimension 3)
            sage: [ x.matrix() for x in E.image_of_hecke_algebra().gens() ]
            [
            [1 0 0 0 0 0]  [ 0  2  0 -1  1 -1]  [ 0  0  1 -1  1 -1]
            [0 1 0 0 0 0]  [-1 -2  2 -1  2 -1]  [ 0 -1  1  0  1 -1]
            [0 0 1 0 0 0]  [ 0  0  1 -1  3 -1]  [ 0  0  1  0  2 -2]
            [0 0 0 1 0 0]  [-2  2  0  1  1 -1]  [-2  0  1  1  1 -1]
            [0 0 0 0 1 0]  [-1  1  0  2  0 -3]  [-1  0  1  1  0 -1]
            [0 0 0 0 0 1], [-1  1 -1  1  1 -2], [-1  0  0  1  0 -1]
            ]
            sage: J0(33).hecke_operator(2).matrix()
            [-1  0  1 -1  1 -1]
            [ 0 -2  1  0  1 -1]
            [ 0  0  0  0  2 -2]
            [-2  0  1  0  1 -1]
            [-1  0  1  1 -1 -1]
            [-1  0  0  1  0 -2]
        """
