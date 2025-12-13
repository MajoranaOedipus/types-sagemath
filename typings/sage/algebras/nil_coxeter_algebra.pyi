from sage.algebras.iwahori_hecke_algebra import IwahoriHeckeAlgebra as IwahoriHeckeAlgebra
from sage.combinat.partition import Partitions as Partitions
from sage.combinat.sf.sf import SymmetricFunctions as SymmetricFunctions
from sage.misc.misc_c import prod as prod
from sage.rings.rational_field import QQ as QQ

class NilCoxeterAlgebra(IwahoriHeckeAlgebra.T):
    """
    Construct the Nil-Coxeter algebra of given type.

    This is the algebra
    with generators `u_i` for every node `i` of the corresponding Dynkin
    diagram. It has the usual braid relations (from the Weyl group) as well
    as the quadratic relation `u_i^2 = 0`.

    INPUT:

    - ``W`` -- a Weyl group
    - ``base_ring`` -- a ring (default: rational numbers)
    - ``prefix`` -- a label for the generators (default: ``'u'``)

    EXAMPLES::

        sage: U = NilCoxeterAlgebra(WeylGroup(['A',3,1]))
        sage: u0, u1, u2, u3 = U.algebra_generators()
        sage: u1*u1
        0
        sage: u2*u1*u2 == u1*u2*u1
        True
        sage: U.an_element()
        u[0,1,2,3] + 2*u[0] + 3*u[1] + 1
    """
    def __init__(self, W, base_ring=..., prefix: str = 'u') -> None:
        """
        Initiate the affine nil-Coxeter algebra corresponding to the Weyl
        group `W` over the base ring.

        EXAMPLES::

            sage: U = NilCoxeterAlgebra(WeylGroup(['A',3,1])); U
            The Nil-Coxeter Algebra of Type A3~ over Rational Field
            sage: TestSuite(U).run()

            sage: U = NilCoxeterAlgebra(WeylGroup(['C',3]), ZZ); U
            The Nil-Coxeter Algebra of Type C3 over Integer Ring
            sage: TestSuite(U).run()
        """
    def homogeneous_generator_noncommutative_variables(self, r):
        """
        Give the `r`-th homogeneous function inside the Nil-Coxeter algebra.
        In finite type `A` this is the sum of all decreasing elements of length `r`.
        In affine type `A` this is the sum of all cyclically decreasing elements of length `r`.
        This is only defined in finite type `A`, `B` and affine types `A^{(1)}`, `B^{(1)}`, `C^{(1)}`, `D^{(1)}`.

        INPUT:

        - ``r`` -- positive integer at most the rank of the Weyl group

        EXAMPLES::

            sage: U = NilCoxeterAlgebra(WeylGroup(['A',3,1]))
            sage: U.homogeneous_generator_noncommutative_variables(2)
            u[1,0] + u[2,0] + u[0,3] + u[3,2] + u[3,1] + u[2,1]

            sage: U = NilCoxeterAlgebra(WeylGroup(['B',4]))
            sage: U.homogeneous_generator_noncommutative_variables(2)
            u[1,2] + u[2,1] + u[3,1] + u[4,1] + u[2,3] + u[3,2] + u[4,2] + u[3,4] + u[4,3]

            sage: U = NilCoxeterAlgebra(WeylGroup(['C',3]))
            sage: U.homogeneous_generator_noncommutative_variables(2)
            Traceback (most recent call last):
            ...
            AssertionError: Analogue of symmetric functions in noncommutative variables is not defined in type ['C', 3]

        TESTS::

            sage: U = NilCoxeterAlgebra(WeylGroup(['B',3,1]))
            sage: U.homogeneous_generator_noncommutative_variables(-1)
            0
            sage: U.homogeneous_generator_noncommutative_variables(0)
            1
        """
    def homogeneous_noncommutative_variables(self, la):
        """
        Give the homogeneous function indexed by `la`, viewed inside the Nil-Coxeter algebra.

        This is only defined in finite type `A`, `B` and affine types `A^{(1)}`, `B^{(1)}`, `C^{(1)}`, `D^{(1)}`.

        INPUT:

        - ``la`` -- a partition with first part bounded by the rank of the Weyl group

        EXAMPLES::

            sage: U = NilCoxeterAlgebra(WeylGroup(['B',2,1]))
            sage: U.homogeneous_noncommutative_variables([2,1])
            u[1,2,0] + 2*u[2,1,0] + u[0,2,0] + u[0,2,1] + u[1,2,1] + u[2,1,2] + u[2,0,2] + u[1,0,2]

        TESTS::

            sage: U = NilCoxeterAlgebra(WeylGroup(['B',2,1]))
            sage: U.homogeneous_noncommutative_variables([])
            1
        """
    def k_schur_noncommutative_variables(self, la):
        """
        In type `A^{(1)}` this is the `k`-Schur function in noncommutative variables
        defined by Thomas Lam [Lam2005]_.

        This function is currently only defined in type `A^{(1)}`.

        INPUT:

        - ``la`` -- a partition with first part bounded by the rank of the Weyl group

        EXAMPLES::

            sage: A = NilCoxeterAlgebra(WeylGroup(['A',3,1]))
            sage: A.k_schur_noncommutative_variables([2,2])
            u[0,3,1,0] + u[3,1,2,0] + u[1,2,0,1] + u[3,2,0,3] + u[2,0,3,1] + u[2,3,1,2]

        TESTS::

            sage: A = NilCoxeterAlgebra(WeylGroup(['A',3,1]))
            sage: A.k_schur_noncommutative_variables([])
            1

            sage: A.k_schur_noncommutative_variables([1,2])
            Traceback (most recent call last):
            ...
            AssertionError: [1, 2] is not a partition.

            sage: A.k_schur_noncommutative_variables([4,2])
            Traceback (most recent call last):
            ...
            AssertionError: [4, 2] is not a 3-bounded partition.

            sage: C = NilCoxeterAlgebra(WeylGroup(['C',3,1]))
            sage: C.k_schur_noncommutative_variables([2,2])
            Traceback (most recent call last):
            ...
            AssertionError: Weyl Group of type ['C', 3, 1] (as a matrix group acting on the root space) is not affine type A.
        """
