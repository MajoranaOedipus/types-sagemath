from .fgp_element import DEBUG as DEBUG, FGP_Element as FGP_Element
from .fgp_morphism import FGP_Homset as FGP_Homset, FGP_Morphism as FGP_Morphism
from _typeshed import Incomplete
from sage.arith.functions import lcm as lcm
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.superseded import deprecated_function_alias as deprecated_function_alias
from sage.modules.free_module import FreeModule_generic as FreeModule_generic
from sage.modules.module import Module as Module
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.all import parent as parent
from sage.structure.sequence import Sequence as Sequence

def FGP_Module(V, W, check: bool = True):
    """
    INPUT:

    - ``V`` -- a free `R`-module

    - ``W`` -- a free `R`-submodule of `V`

    - ``check`` -- boolean (default: ``True``); if ``True``, more checks
      on correctness are performed. In particular, we check the data
      types of ``V`` and ``W``, and that `W` is a submodule of `V`
      with the same base ring.

    OUTPUT: the quotient `V/W` as a finitely generated `R`-module

    EXAMPLES::

        sage: V = span([[1/2,1,1], [3/2,2,1], [0,0,1]], ZZ)
        sage: W = V.span([2*V.0 + 4*V.1, 9*V.0 + 12*V.1, 4*V.2])
        sage: import sage.modules.fg_pid.fgp_module
        sage: Q = sage.modules.fg_pid.fgp_module.FGP_Module(V, W)
        sage: type(Q)
        <class 'sage.modules.fg_pid.fgp_module.FGP_Module_class_with_category'>
        sage: Q is sage.modules.fg_pid.fgp_module.FGP_Module(V, W, check=False)
        True
    """
def is_FGP_Module(x):
    """
    Return ``True`` if x is an FGP module, i.e., a finitely generated
    module over a PID represented as a quotient of finitely generated
    free modules over a PID.

    EXAMPLES::

        sage: V = span([[1/2,1,1],[3/2,2,1],[0,0,1]],ZZ)
        sage: W = V.span([2*V.0 + 4*V.1, 9*V.0 + 12*V.1, 4*V.2]); Q = V/W
        sage: sage.modules.fg_pid.fgp_module.is_FGP_Module(V)
        doctest:warning...
        DeprecationWarning: the function is_FGP_Module is deprecated;
        use 'isinstance(..., FGP_Module_class)' instead
        See https://github.com/sagemath/sage/issues/37924 for details.
        False
        sage: sage.modules.fg_pid.fgp_module.is_FGP_Module(Q)
        True
    """

class FGP_Module_class(Module):
    """
    A finitely generated module over a PID presented as a quotient `V/W`.

    INPUT:

    - ``V`` -- an `R`-module

    - ``W`` -- an `R`-submodule of `V`

    - ``check`` -- boolean (default: ``True``)

    EXAMPLES::

        sage: A = (ZZ^1)/span([[100]], ZZ); A
        Finitely generated module V/W over Integer Ring with invariants (100)
        sage: A.V()
        Ambient free module of rank 1 over the principal ideal domain Integer Ring
        sage: A.W()
        Free module of degree 1 and rank 1 over Integer Ring
        Echelon basis matrix:
        [100]

        sage: V = span([[1/2,1,1], [3/2,2,1], [0,0,1]], ZZ)
        sage: W = V.span([2*V.0 + 4*V.1, 9*V.0 + 12*V.1, 4*V.2])
        sage: Q = V/W; Q
        Finitely generated module V/W over Integer Ring with invariants (4, 12)
        sage: type(Q)
        <class 'sage.modules.fg_pid.fgp_module.FGP_Module_class_with_category'>

    TESTS:

    Make sure that the problems in :issue:`7516` are fixed::

        sage: V = FreeModule(QQ, 2)
        sage: W = V.submodule([V([1,1])])
        sage: Z = W.submodule([])
        sage: WmodZ = W / Z
        sage: loads(dumps(WmodZ)) == WmodZ
        True
    """
    Element = FGP_Element
    def __init__(self, V, W, check: bool = True) -> None:
        """
        INPUT:

        - ``V`` -- an `R`-module

        - ``W`` -- an `R`-submodule of `V`

        - ``check`` -- boolean (default: ``True``); if ``True``, more checks on
          correctness are performed. In particular, we check the data types of
          ``V`` and ``W``, and that `W` is a submodule of `V` with the same
          base ring `R`.

        EXAMPLES::

            sage: V = span([[1/2,1,1], [3/2,2,1], [0,0,1]], ZZ)
            sage: W = V.span([2*V.0 + 4*V.1, 9*V.0 + 12*V.1, 4*V.2])
            sage: Q = V/W; Q
            Finitely generated module V/W over Integer Ring with invariants (4, 12)
            sage: type(Q)
            <class 'sage.modules.fg_pid.fgp_module.FGP_Module_class_with_category'>
        """
    def __truediv__(self, other):
        """
        Return the quotient ``self`` / ``other``, where ``other`` must be a
        submodule of ``self``.

        EXAMPLES::

            sage: V = span([[5, -1/2]], ZZ); W = span([[20,-2]] ,ZZ)
            sage: Q = V/W; phi = Q.hom([2*Q.0])
            sage: Q
            Finitely generated module V/W over Integer Ring with invariants (4)
            sage: Q/phi.kernel()
            Finitely generated module V/W over Integer Ring with invariants (2)
            sage: Q/Q
            Finitely generated module V/W over Integer Ring with invariants ()
        """
    def __eq__(self, other):
        """
        EXAMPLES::

            sage: V = span([[1/2,1,1], [3/2,2,1], [0,0,1]], ZZ)
            sage: W = V.span([2*V.0 + 4*V.1, 9*V.0 + 12*V.1, 4*V.2])
            sage: Q = V/W
            sage: Q == Q
            True
            sage: loads(dumps(Q)) == Q
            True
            sage: Q == V
            False
            sage: Q == V/V.zero_submodule()
            False
        """
    def __ne__(self, other):
        """
        Return ``True`` iff ``self`` is not equal to ``other``.

        This may not be needed for modules created using the function
        :func:`FGP_Module`, since those have uniqueness built into
        them, but if the modules are created directly using the
        ``__init__`` method for this class, then this may fail; in
        particular, for modules ``M`` and ``N`` with ``M == N`` returning
        True, it may be the case that ``M != N`` may also return True.
        In particular, for derived classes whose ``__init__`` methods just
        call the ``__init__`` method for this class need this.  See
        :issue:`9940` for illustrations.

        EXAMPLES:

        Make sure that the problems in :issue:`9940` are fixed::

            sage: G = AdditiveAbelianGroup([0,0])
            sage: H = AdditiveAbelianGroup([0,0])
            sage: G == H
            True
            sage: G != H # indirect doctest
            False

            sage: N1 = ToricLattice(3)
            sage: sublattice1 = N1.submodule([(1,1,0), (3,2,1)])
            sage: Q1 = N1/sublattice1
            sage: N2 = ToricLattice(3)
            sage: sublattice2 = N2.submodule([(1,1,0), (3,2,1)])
            sage: Q2 = N2/sublattice2
            sage: Q1 == Q2
            True
            sage: Q1 != Q2
            False
        """
    def __lt__(self, other):
        """
        Return ``True`` iff ``self`` is a proper submodule of ``other``.

        EXAMPLES::

            sage: V = ZZ^2; W = V.span([[1,2]]); W2 = W.scale(2)
            sage: A = V/W; B = W/W2
            sage: B < A
            False
            sage: A = V/W2; B = W/W2
            sage: B < A
            True
            sage: A < A
            False
        """
    def __gt__(self, other):
        """
        Return ``True`` iff ``other`` is a proper submodule of ``self``.

        EXAMPLES::

            sage: V = ZZ^2; W = V.span([[1,2]]); W2 = W.scale(2)
            sage: A = V/W; B = W/W2
            sage: A > B
            False
            sage: A = V/W2; B = W/W2
            sage: A > B
            True
            sage: A > A
            False
        """
    def __ge__(self, other):
        """
        Return ``True`` iff ``other`` is a submodule of ``self``.

        EXAMPLES::

            sage: V = ZZ^2; W = V.span([[1,2]]); W2 = W.scale(2)
            sage: A = V/W; B = W/W2
            sage: A >= B
            False
            sage: A = V/W2; B = W/W2
            sage: A >= B
            True
            sage: A >= A
            True
        """
    def linear_combination_of_smith_form_gens(self, x):
        """
        Compute a linear combination of the optimised generators of this module
        as returned by :meth:`smith_form_gens`.

        EXAMPLES::

            sage: X = ZZ**2 / span([[3,0], [0,2]], ZZ)
            sage: X.linear_combination_of_smith_form_gens([1])
            (1)
        """
    def __contains__(self, x) -> bool:
        """
        Return true if ``x`` is contained in ``self``.

        EXAMPLES::

            sage: V = span([[1/2,1,1], [3/2,2,1], [0,0,1]], ZZ)
            sage: W = V.span([2*V.0 + 4*V.1, 9*V.0 + 12*V.1, 4*V.2])
            sage: Q = V/W; Q
            Finitely generated module V/W over Integer Ring with invariants (4, 12)
            sage: Q.0 in Q
            True
            sage: 0 in Q
            True
            sage: vector([1,2,3/7]) in Q
            False
            sage: vector([1,2,3]) in Q
            True
            sage: Q.0 - Q.1 in Q
            True
        """
    def submodule(self, x):
        """
        Return the submodule defined by ``x``.

        INPUT:

        - ``x`` -- list, tuple, or FGP module

        EXAMPLES::

            sage: V = span([[1/2,1,1], [3/2,2,1], [0,0,1]], ZZ)
            sage: W = V.span([2*V.0 + 4*V.1, 9*V.0 + 12*V.1, 4*V.2])
            sage: Q = V/W; Q
            Finitely generated module V/W over Integer Ring with invariants (4, 12)
            sage: Q.gens()
            ((1, 0), (0, 1))

        We create submodules generated by a list or tuple of elements::

            sage: Q.submodule([Q.0])
            Finitely generated module V/W over Integer Ring with invariants (4)
            sage: Q.submodule([Q.1])
            Finitely generated module V/W over Integer Ring with invariants (12)
            sage: Q.submodule((Q.0, Q.0 + 3*Q.1))
            Finitely generated module V/W over Integer Ring with invariants (4, 4)

        A submodule defined by a submodule::

            sage: A = Q.submodule((Q.0, Q.0 + 3*Q.1)); A
            Finitely generated module V/W over Integer Ring with invariants (4, 4)
            sage: Q.submodule(A)
            Finitely generated module V/W over Integer Ring with invariants (4, 4)

        Inclusion is checked::

            sage: A.submodule(Q)
            Traceback (most recent call last):
            ...
            ValueError: x.V() must be contained in self's V.
        """
    def has_canonical_map_to(self, A) -> bool:
        """
        Return ``True`` if ``self`` has a canonical map to ``A``, relative to the
        given presentation of ``A``.

        This means that ``A`` is a finitely
        generated quotient module, ``self.V()`` is a submodule of ``A.V()``
        and ``self.W()`` is a submodule of ``A.W()``, i.e., that there is a
        natural map induced by inclusion of the V's. Note that we do
        *not* require that this natural map be injective; for this use
        :meth:`is_submodule`.

        EXAMPLES::

            sage: V = span([[1/2,1,1], [3/2,2,1], [0,0,1]], ZZ)
            sage: W = V.span([2*V.0 + 4*V.1, 9*V.0 + 12*V.1, 4*V.2])
            sage: Q = V/W; Q
            Finitely generated module V/W over Integer Ring with invariants (4, 12)
            sage: A = Q.submodule((Q.0, Q.0 + 3*Q.1)); A
            Finitely generated module V/W over Integer Ring with invariants (4, 4)
            sage: A.has_canonical_map_to(Q)
            True
            sage: Q.has_canonical_map_to(A)
            False
        """
    def is_submodule(self, A) -> bool:
        """
        Return ``True`` if ``self`` is a submodule of ``A``.

        More precisely, this returns ``True`` if ``self.V()`` is a
        submodule of ``A.V()``, with ``self.W()`` equal to ``A.W()``.

        Compare :meth:`has_canonical_map_to`.

        EXAMPLES::

            sage: V = ZZ^2; W = V.span([[1,2]]); W2 = W.scale(2)
            sage: A = V/W; B = W/W2
            sage: B.is_submodule(A)
            False
            sage: A = V/W2; B = W/W2
            sage: B.is_submodule(A)
            True

        This example illustrates that this command works in a subtle cases.::

            sage: A = ZZ^1
            sage: Q3 = A / A.span([[3]])
            sage: Q6 = A / A.span([[6]])
            sage: Q6.is_submodule(Q3)
            False
            sage: Q6.has_canonical_map_to(Q3)
            True
            sage: Q = A.span([[2]]) / A.span([[6]])
            sage: Q.is_submodule(Q6)
            True
        """
    __le__ = is_submodule
    def V(self):
        """
        If this module was constructed as a quotient V/W, return V.

        EXAMPLES::

            sage: V = span([[1/2,1,1], [3/2,2,1], [0,0,1]], ZZ)
            sage: W = V.span([2*V.0 + 4*V.1, 9*V.0 + 12*V.1, 4*V.2])
            sage: Q = V/W
            sage: Q.V()
            Free module of degree 3 and rank 3 over Integer Ring
            Echelon basis matrix:
            [1/2   0   0]
            [  0   1   0]
            [  0   0   1]
        """
    def cover(self):
        """
        If this module was constructed as `V/W`, return the cover module `V`.

        This is the same as ``self.V()``.

        EXAMPLES::

            sage: V = span([[1/2,1,1], [3/2,2,1], [0,0,1]], ZZ)
            sage: W = V.span([2*V.0 + 4*V.1, 9*V.0 + 12*V.1, 4*V.2])
            sage: Q = V/W
            sage: Q.V()
            Free module of degree 3 and rank 3 over Integer Ring
            Echelon basis matrix:
            [1/2   0   0]
            [  0   1   0]
            [  0   0   1]
        """
    def W(self):
        """
        If this module was constructed as a quotient `V/W`, return `W`.

        EXAMPLES::

            sage: V = span([[1/2,1,1], [3/2,2,1], [0,0,1]], ZZ)
            sage: W = V.span([2*V.0 + 4*V.1, 9*V.0 + 12*V.1, 4*V.2])
            sage: Q = V/W
            sage: Q.W()
            Free module of degree 3 and rank 3 over Integer Ring
            Echelon basis matrix:
            [1/2   8   0]
            [  0  12   0]
            [  0   0   4]
        """
    def relations(self):
        """
        If ``self`` was constructed as `V / W`, return the
        relations module `W`.

        This is the same as ``self.W()``.

        EXAMPLES::

            sage: V = span([[1/2,1,1], [3/2,2,1], [0,0,1]], ZZ)
            sage: W = V.span([2*V.0 + 4*V.1, 9*V.0 + 12*V.1, 4*V.2])
            sage: Q = V / W
            sage: Q.relations()
            Free module of degree 3 and rank 3 over Integer Ring
            Echelon basis matrix:
            [1/2   8   0]
            [  0  12   0]
            [  0   0   4]
        """
    def base_ring(self):
        """
        Return the base ring of ``self``.

        EXAMPLES::

            sage: V = span([[1/2,1,1], [3/2,2,1], [0,0,1]], ZZ)
            sage: W = V.span([2*V.0 + 4*V.1, 9*V.0 + 12*V.1, 4*V.2])
            sage: Q = V/W
            sage: Q.base_ring()
            Integer Ring
        """
    @cached_method
    def invariants(self, include_ones: bool = False):
        """
        Return the diagonal entries of the Smith form of the relative
        matrix that defines ``self`` (see :meth:`._relative_matrix`)
        padded with zeros, excluding 1s by default.   Thus if ``v`` is the
        list of integers returned, then ``self`` is abstractly isomorphic to
        the product of cyclic groups `\\ZZ/n\\ZZ` where `n` is in ``v``.

        INPUT:

        - ``include_ones`` -- boolean (default: ``False``); if ``True``, also
          include 1s in the output list

        EXAMPLES::

            sage: V = span([[1/2,1,1], [3/2,2,1], [0,0,1]], ZZ)
            sage: W = V.span([2*V.0 + 4*V.1, 9*V.0 + 12*V.1, 4*V.2])
            sage: Q = V/W
            sage: Q.invariants()
            (4, 12)

        An example with 1 and 0 rows::

            sage: V = ZZ^3; W = V.span([[1,2,0], [0,1,0], [0,2,0]]); Q = V/W; Q
            Finitely generated module V/W over Integer Ring with invariants (0)
            sage: Q.invariants()
            (0,)
            sage: Q.invariants(include_ones=True)
            (1, 1, 0)
        """
    def gens(self) -> tuple:
        """
        Return tuple of elements `g_0,...,g_n` of ``self`` such that the module generated by
        the `g_i` is isomorphic to the direct sum of `R/e_i R`, where `e_i` are the
        invariants of ``self`` and `R` is the base ring.

        Note that these are not generally uniquely determined, and depending on
        how Smith normal form is implemented for the base ring, they may not
        even be deterministic.

        This can safely be overridden in all derived classes.

        EXAMPLES::

            sage: V = span([[1/2,1,1], [3/2,2,1], [0,0,1]], ZZ)
            sage: W = V.span([2*V.0 + 4*V.1, 9*V.0 + 12*V.1, 4*V.2])
            sage: Q = V/W
            sage: Q.gens()
            ((1, 0), (0, 1))
            sage: Q.0
            (1, 0)
        """
    @cached_method
    def smith_form_gens(self):
        """
        Return a set of generators for ``self`` which are in Smith normal form.

        EXAMPLES::

            sage: V = span([[1/2,1,1], [3/2,2,1], [0,0,1]], ZZ)
            sage: W = V.span([2*V.0 + 4*V.1, 9*V.0 + 12*V.1, 4*V.2])
            sage: Q = V/W
            sage: Q.smith_form_gens()
            ((1, 0), (0, 1))
            sage: [x.lift() for x in Q.smith_form_gens()]
            [(0, 3, 1), (0, -1, 0)]
        """
    def gens_to_smith(self):
        """
        Return the transformation matrix from the user to Smith form generators.

        To go in the other direction, use :meth:`smith_to_gens`.

        OUTPUT: a matrix over the base ring

        EXAMPLES::

            sage: L2 = IntegralLattice(3 * matrix([[-2,0,0], [0,1,0], [0,0,-4]]))
            sage: D = L2.discriminant_group().normal_form(); D                          # needs sage.libs.pari sage.rings.padics
            Finite quadratic module over Integer Ring with invariants (3, 6, 12)
            Gram matrix of the quadratic form with values in Q/Z:
            [1/2   0   0   0   0]
            [  0 1/4   0   0   0]
            [  0   0 1/3   0   0]
            [  0   0   0 1/3   0]
            [  0   0   0   0 2/3]
            sage: D.gens_to_smith()                                                     # needs sage.libs.pari sage.rings.padics
            [0 3 0]
            [0 0 3]
            [0 4 0]
            [1 2 0]
            [0 0 4]
            sage: T = D.gens_to_smith() * D.smith_to_gens(); T                          # needs sage.libs.pari sage.rings.padics
            [ 3  0  3  0  0]
            [ 0 33  0  0  3]
            [ 4  0  4  0  0]
            [ 2  0  3  1  0]
            [ 0 44  0  0  4]

        The matrix `T` now satisfies a certain congruence::

            sage: for i in range(T.nrows()):                                            # needs sage.libs.pari sage.rings.padics
            ....:     T[:,i] = T[:,i] % D.gens()[i].order()
            sage: T                                                                     # needs sage.libs.pari sage.rings.padics
            [1 0 0 0 0]
            [0 1 0 0 0]
            [0 0 1 0 0]
            [0 0 0 1 0]
            [0 0 0 0 1]
        """
    @cached_method
    def smith_to_gens(self):
        """
        Return the transformation matrix from Smith form to user generators.

        To go in the other direction, use :meth:`gens_to_smith`.

        OUTPUT: a matrix over the base ring

        EXAMPLES::

            sage: L2 = IntegralLattice(3 * matrix([[-2,0,0], [0,1,0], [0,0,-4]]))
            sage: D = L2.discriminant_group().normal_form(); D                          # needs sage.libs.pari sage.rings.padics
            Finite quadratic module over Integer Ring with invariants (3, 6, 12)
            Gram matrix of the quadratic form with values in Q/Z:
            [1/2   0   0   0   0]
            [  0 1/4   0   0   0]
            [  0   0 1/3   0   0]
            [  0   0   0 1/3   0]
            [  0   0   0   0 2/3]
            sage: D.smith_to_gens()                                                     # needs sage.libs.pari sage.rings.padics
            [ 0  0  1  1  0]
            [ 1  0  1  0  0]
            [ 0 11  0  0  1]
            sage: T = D.smith_to_gens() * D.gens_to_smith(); T                          # needs sage.libs.pari sage.rings.padics
            [ 1  6  0]
            [ 0  7  0]
            [ 0  0 37]

        This matrix satisfies the congruence::

            sage: for i in range(T.ncols()):                                            # needs sage.libs.pari sage.rings.padics
            ....:     T[:, i] = T[:, i] % D.smith_form_gens()[i].order()
            sage: T                                                                     # needs sage.libs.pari sage.rings.padics
            [1 0 0]
            [0 1 0]
            [0 0 1]

        We create some element of our FGP module::

            sage: x = D.linear_combination_of_smith_form_gens((1,2,3)); x               # needs sage.libs.pari sage.rings.padics
            (1, 2, 3)

        and want to know some (it is not unique) linear combination
        of the user defined generators that is ``x``::

            sage: x.vector() * D.smith_to_gens()                                        # needs sage.libs.pari sage.rings.padics
            (2, 33, 3, 1, 3)
        """
    def gens_vector(self, x, reduce: bool = False):
        """
        Return coordinates of ``x`` with respect to the generators.

        INPUT:

        - ``x`` -- element of ``self``

        - ``reduce`` -- (default: ``False``) if ``True``,
          reduce coefficients modulo invariants; this is
          ignored if the base ring is not `\\ZZ`

        EXAMPLES:

        We create a derived class and overwrite :meth:`gens`::

             sage: from sage.modules.fg_pid.fgp_module import FGP_Module_class
             sage: W = ZZ^3
             sage: V = W.span(matrix.diagonal([1/6, 1/3, 1/12]))
             sage: class FGP_with_gens(FGP_Module_class):
             ....:     def __init__(self, V, W, gens):
             ....:         FGP_Module_class.__init__(self, V, W)
             ....:         self._gens = tuple([self(g) for g in gens])
             ....:     def gens(self):
             ....:         return self._gens
             sage: gens = [(1/2, 0, 0), (0, 0, 1/4), (1/3, 0, 0), (0, 1/3, 0), (0, 0, 2/3)]
             sage: gens = [V(g) for g in gens]
             sage: D = FGP_with_gens(V, W, gens)
             sage: D.gens()
             ((0, 3, 0), (0, 0, 3), (0, 4, 0), (1, 2, 0), (0, 0, 8))


        We create some element of ``D``::

            sage: x = D.linear_combination_of_smith_form_gens((1,2,3)); x
            (1, 2, 3)

        In our generators::

            sage: v = D.gens_vector(x); v                                               # needs sage.libs.pari
            (2, 9, 3, 1, 33)

        The output can be further reduced::

            sage: D.gens_vector(x, reduce=True)                                         # needs sage.libs.pari
            (0, 1, 0, 1, 0)

        Let us check::

            sage: x == sum(v[i]*D.gen(i) for i in range(len(D.gens())))                 # needs sage.libs.pari
            True
        """
    def coordinate_vector(self, x, reduce: bool = False):
        """
        Return coordinates of ``x`` with respect to the optimized
        representation of ``self``.

        INPUT:

        - ``x`` -- element of ``self``

        - ``reduce`` -- (default: ``False``) if ``True``, reduce
          coefficients modulo invariants; this is
          ignored if the base ring is not ``ZZ``

        OUTPUT:

        The coordinates as a vector. That is, the same type as
        ``self.V()``, but in general with fewer entries.

        EXAMPLES::

            sage: V = span([[1/4,0,0], [3/4,4,2], [0,0,2]], ZZ)
            sage: W = V.span([4*V.0 + 12*V.1])
            sage: Q = V/W; Q
            Finitely generated module V/W over Integer Ring with invariants (4, 0, 0)
            sage: Q.coordinate_vector(-Q.0)
            (-1, 0, 0)
            sage: Q.coordinate_vector(-Q.0, reduce=True)
            (3, 0, 0)

        If x is not in self, it is coerced in::

            sage: Q.coordinate_vector(V.0)
            (1, -3, 0)
            sage: Q.coordinate_vector(Q(V.0))
            (1, -3, 0)

        TESTS::

            sage: V = span([[1/2,0,0], [3/2,2,1], [0,0,1]], ZZ)
            sage: W = V.span([2*V.0 + 4*V.1, 9*V.0 + 12*V.1, 4*V.2])
            sage: Q = V/W; Q
            Finitely generated module V/W over Integer Ring with invariants (4, 12)
            sage: Q.coordinate_vector(Q.0 - Q.1, reduce=True)
            (1, 11)
            sage: a, b = Q.coordinate_vector(Q.0 - Q.1)
            sage: (a % 4, b % 12)
            (1, 11)

            sage: O, X = Q.optimized()
            sage: O.V()
            Free module of degree 3 and rank 2 over Integer Ring
            User basis matrix:
            [ 0  6  1]
            [ 0 -2  0]
            sage: phi = Q.hom([Q.0, 4*Q.1])
            sage: x = Q(V.0); x
            (0, 8)
            sage: Q.coordinate_vector(x, reduce=True)
            (0, 8)
            sage: a, b = Q.coordinate_vector(-x, reduce=False)
            sage: (a % 4, b % 12)
            (0, 4)
            sage: x == 8*Q.1
            True
            sage: x = Q(V.1); x
            (0, 11)
            sage: a, b = Q.coordinate_vector(x)
            sage: (a % 4, b % 12)
            (0, 11)
            sage: x == -Q.1
            True
            sage: x = Q(V.2); x
            (1, 3)
            sage: Q.coordinate_vector(x)
            (1, 3)
            sage: x == Q.0 + 3*Q.1
            True
        """
    def gen(self, i):
        """
        Return the ``i``-th generator of ``self``.

        INPUT:

        - ``i`` -- integer

        EXAMPLES::

            sage: V = span([[1/2,1,1], [3/2,2,1], [0,0,1]], ZZ)
            sage: W = V.span([2*V.0 + 4*V.1, 9*V.0 + 12*V.1, 4*V.2])
            sage: Q = V/W; Q
            Finitely generated module V/W over Integer Ring with invariants (4, 12)
            sage: Q.gen(0)
            (1, 0)
            sage: Q.gen(1)
            (0, 1)
            sage: Q.gen(2)
            Traceback (most recent call last):
            ...
            ValueError: Generator 2 not defined
            sage: Q.gen(-1)
            Traceback (most recent call last):
            ...
            ValueError: Generator -1 not defined
        """
    def smith_form_gen(self, i):
        """
        Return the ``i``-th generator of ``self``.

        This is a separate method so we can freely override :meth:`gen`
        in derived classes.

        INPUT:

        - ``i`` -- integer

        EXAMPLES::

            sage: V = span([[1/2,1,1], [3/2,2,1], [0,0,1]], ZZ)
            sage: W = V.span([2*V.0 + 4*V.1, 9*V.0 + 12*V.1, 4*V.2])
            sage: Q = V/W; Q
            Finitely generated module V/W over Integer Ring with invariants (4, 12)
            sage: Q.smith_form_gen(0)
            (1, 0)
            sage: Q.smith_form_gen(1)
            (0, 1)
        """
    def optimized(self):
        """
        Return a module isomorphic to this one, but with `V` replaced by
        a submodule of `V` such that the generators of ``self`` all lift
        trivially to generators of `V`.  Replace `W` by the intersection
        of `V` and `W`. This has the advantage that `V` has small dimension
        and any homomorphism from ``self`` trivially extends to a
        homomorphism from `V`.

        OUTPUT:

        - ``Q`` -- an optimized quotient `V_0/W_0` with `V_0` a submodule of `V`
          such that `\\phi: V_0/W_0 \\to V/W` is an isomorphism

        - ``Z`` -- matrix such that if `x` is in ``self.V()`` and
          ``c`` gives the coordinates of `x` in terms of the
          basis for ``self.V()``, then ``c*Z`` is in `V_0`
          and ``c*Z`` maps to `x` via `\\phi` above.

        EXAMPLES::

            sage: V = span([[1/2,1,1], [3/2,2,1], [0,0,1]], ZZ)
            sage: W = V.span([2*V.0 + 4*V.1, 9*V.0 + 12*V.1, 4*V.2])
            sage: Q = V/W
            sage: O, X = Q.optimized(); O
            Finitely generated module V/W over Integer Ring with invariants (4, 12)
            sage: O.V()
            Free module of degree 3 and rank 2 over Integer Ring
            User basis matrix:
            [ 0  3  1]
            [ 0 -1  0]
            sage: O.W()
            Free module of degree 3 and rank 2 over Integer Ring
            Echelon basis matrix:
            [ 0 12  0]
            [ 0  0  4]
            sage: X         # random
            [0 4 0]
            [0 1 0]
            [0 0 1]
            sage: OV = O.V()
            sage: Q(OV([0,-8,0])) == V.0
            True
            sage: Q(OV([0,1,0])) == V.1
            True
            sage: Q(OV([0,0,1])) == V.2
            True
        """
    def hom(self, im_gens, codomain=None, check: bool = True):
        """
        Homomorphism defined by giving the images of ``self.gens()`` in some
        fixed finitely generated `R`-module.

        .. NOTE::

            We do not assume that the generators given by ``self.gens()`` are
            the same as the Smith form generators, since this may not be true
            for a general derived class.

        INPUT:

        - ``im_gens`` -- list of the images of ``self.gens()`` in some
          `R`-module

        EXAMPLES::

            sage: V = span([[1/2,1,1], [3/2,2,1], [0,0,1]], ZZ)
            sage: W = V.span([2*V.0 + 4*V.1, 9*V.0 + 12*V.1, 4*V.2])
            sage: Q = V/W
            sage: phi = Q.hom([3*Q.1, Q.0])
            sage: phi
            Morphism from module over Integer Ring with invariants (4, 12)
                       to module with invariants (4, 12)
              that sends the generators to [(0, 3), (1, 0)]
            sage: phi(Q.0)
            (0, 3)
            sage: phi(Q.1)
            (1, 0)
            sage: Q.0 == phi(Q.1)
            True

        This example illustrates creating a morphism to a free module.
        The free module is turned into an FGP module (i.e., quotient
        `V/W` with `W=0`), and the morphism is constructed::

            sage: V = span([[1/2,0,0], [3/2,2,1], [0,0,1]], ZZ)
            sage: W = V.span([2*V.0 + 4*V.1])
            sage: Q = V/W; Q
            Finitely generated module V/W over Integer Ring with invariants (2, 0, 0)
            sage: phi = Q.hom([0, V.0, V.1]); phi
            Morphism from module over Integer Ring with invariants (2, 0, 0)
                       to module with invariants (0, 0, 0)
              that sends the generators to [(0, 0, 0), (1, 0, 0), (0, 1, 0)]
            sage: phi.domain()
            Finitely generated module V/W over Integer Ring with invariants (2, 0, 0)
            sage: phi.codomain()
            Finitely generated module V/W over Integer Ring with invariants (0, 0, 0)
            sage: phi(Q.0)
            (0, 0, 0)
            sage: phi(Q.1)
            (1, 0, 0)
            sage: phi(Q.2) == V.1
            True

        Constructing two zero maps from the zero module::

            sage: A = (ZZ^2)/(ZZ^2); A
            Finitely generated module V/W over Integer Ring with invariants ()
            sage: A.hom([])
            Morphism from module over Integer Ring with invariants ()
                       to module with invariants ()
              that sends the generators to []
            sage: A.hom([]).codomain() is A
            True
            sage: B = (ZZ^3)/(ZZ^3)
            sage: phi = A.hom([], codomain=B); phi
            Morphism from module over Integer Ring with invariants ()
                       to module with invariants ()
              that sends the generators to []
            sage: phi(A(0))
            ()
            sage: phi(A(0)) == B(0)
            True

        A degenerate case::

            sage: A = (ZZ^2)/(ZZ^2)
            sage: phi = A.hom([]); phi
            Morphism from module over Integer Ring with invariants ()
                       to module with invariants ()
              that sends the generators to []
            sage: phi(A(0))
            ()

        The code checks that the morphism is valid.  In the example
        below we try to send a generator of order 2 to an element of
        order 14::

            sage: V = span([[1/14,3/14], [0,1/2]], ZZ); W = ZZ^2
            sage: Q = V/W; Q
            Finitely generated module V/W over Integer Ring with invariants (2, 14)
            sage: Q.linear_combination_of_smith_form_gens([1,11]).additive_order()
            14
            sage: f = Q.hom([Q.linear_combination_of_smith_form_gens([1,11]),
            ....:            Q.linear_combination_of_smith_form_gens([1,3])]); f
            Traceback (most recent call last):
            ...
            ValueError: phi must send optimized submodule of M.W() into N.W()
        """
    def random_element(self, *args, **kwds):
        """
        Create a random element of ``self`` = `V/W`, by creating a random element of `V` and
        reducing it modulo `W`.

        All arguments are passed on to the method :meth:`random_element` of `V`.

        EXAMPLES::

            sage: V = span([[1/2,1,1], [3/2,2,1], [0,0,1]], ZZ)
            sage: W = V.span([2*V.0 + 4*V.1, 9*V.0 + 12*V.1, 4*V.2])
            sage: Q = V/W
            sage: Q.random_element().parent() is Q
            True
            sage: Q.cardinality()
            48
            sage: S = set()
            sage: while len(S) < 48:
            ....:     S.add(Q.random_element())
        """
    def cardinality(self):
        """
        Return the cardinality of this module as a set.

        EXAMPLES::

            sage: V = ZZ^2; W = V.span([[1,2], [3,4]]); A = V/W; A
            Finitely generated module V/W over Integer Ring with invariants (2)
            sage: A.cardinality()
            2
            sage: V = ZZ^2; W = V.span([[1,2]]); A = V/W; A
            Finitely generated module V/W over Integer Ring with invariants (0)
            sage: A.cardinality()
            +Infinity
            sage: V = QQ^2; W = V.span([[1,2]]); A = V/W; A
            Vector space quotient V/W of dimension 1 over Rational Field where
              V: Vector space of dimension 2 over Rational Field
              W: Vector space of degree 2 and dimension 1 over Rational Field
                 Basis matrix:
                 [1 2]
            sage: A.cardinality()
            +Infinity
        """
    def list(self):
        """
        Return a list of the elements of ``self``.

        EXAMPLES::

            sage: V = ZZ^2; W = V.span([[1,2],[3,4]])
            sage: list(V/W)
            [(0), (1)]
        """
    def __iter__(self):
        """
        Return iterator over all elements of ``self``.

        EXAMPLES::

            sage: V = span([[1/2,0,0], [3/2,2,1], [0,0,1]], ZZ); W = V.span([V.0 + 2*V.1, 4*V.0 + 2*V.1, 4*V.2])
            sage: Q = V/W; Q
            Finitely generated module V/W over Integer Ring with invariants (2, 12)
            sage: z = list(V/W)
            sage: z
            [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11),
             (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11)]
            sage: len(z)
            24

        We test that the trivial module is handled correctly (:issue:`6561`)::

            sage: A = (ZZ**1)/(ZZ**1); list(A) == [A(0)]
            True
        """
    def construction(self):
        """
        The construction functor and ambient module for ``self``.

        EXAMPLES::

            sage: W = ZZ^2
            sage: A1 = W.submodule([[1,0]])
            sage: B1 = W.submodule([[2,0]])
            sage: T1 = A1 / B1
            sage: T1.construction()
            (QuotientModuleFunctor,
             Free module of degree 2 and rank 1 over Integer Ring
             Echelon basis matrix:
             [1 0])

        TESTS::

            sage: W = ZZ^2
            sage: A1 = W.submodule([[1,0]])
            sage: A2 = W.submodule([[0,1]])
            sage: B1 = W.submodule([[2,0]])
            sage: B2 = W.submodule([[0,2]])
            sage: T1 = A1 / B1
            sage: T2 = A2 / B2
            sage: t1 = T1.an_element()
            sage: t2 = T2.an_element()

            sage: # needs sage.libs.flint (o/w infinite recursion)
            sage: t1 + t2
            (1, 1)
        """
    def is_finite(self) -> bool:
        """
        Return ``True`` if ``self`` is finite and ``False`` otherwise.

        EXAMPLES::

            sage: V = span([[1/2,0,0], [3/2,2,1], [0,0,1]], ZZ)
            sage: W = V.span([V.0 + 2*V.1, 9*V.0 + 2*V.1, 4*V.2])
            sage: Q = V/W; Q
            Finitely generated module V/W over Integer Ring with invariants (4, 16)
            sage: Q.is_finite()
            True
            sage: Q = V / V.zero_submodule(); Q
            Finitely generated module V/W over Integer Ring with invariants (0, 0, 0)
            sage: Q.is_finite()
            False
        """
    def annihilator(self):
        """
        Return the ideal of the base ring that annihilates ``self``. This
        is precisely the ideal generated by the LCM of the invariants
        of ``self`` if ``self`` is finite, and is 0 otherwise.

        EXAMPLES::

            sage: V = span([[1/2,0,0], [3/2,2,1], [0,0,1]], ZZ)
            sage: W = V.span([V.0 + 2*V.1, 9*V.0 + 2*V.1, 4*V.2])
            sage: Q = V/W; Q.annihilator()
            Principal ideal (16) of Integer Ring
            sage: Q.annihilator().gen()
            16

            sage: Q = V / V.span([V.0]); Q
            Finitely generated module V/W over Integer Ring with invariants (0, 0)
            sage: Q.annihilator()
            Principal ideal (0) of Integer Ring

        We check that :issue:`22720` is resolved::

            sage: H = AdditiveAbelianGroup([])
            sage: H.annihilator()
            Principal ideal (1) of Integer Ring
        """
    def ngens(self):
        '''
        Return the number of generators of ``self``.

        (Note for developers: This is just the length of :meth:`gens`, rather
        than of the minimal set of generators as returned by
        :meth:`.smith_form_gens`; these are the same in the
        :class:`~sage.modules.fg_pid.fgp_module.FGP_Module_class`, but not
        necessarily in derived classes.)

        EXAMPLES::

            sage: A = (ZZ**2) / span([[4,0], [0,3]], ZZ)
            sage: A.ngens()
            1

        This works (but please do not do it in production code!) ::

            sage: A.gens = lambda: [1,2,"Barcelona!"]
            sage: A.ngens()
            3
        '''
    def __hash__(self):
        """
        Calculate a hash for ``self``.

        EXAMPLES::

            sage: A = (ZZ**2) / span([[4,0], [0,3]], ZZ)
            sage: hash(A) == hash(((2, ZZ), ((4, 0), (0, 3))))
            True
        """
    @cached_method
    def quotient_map(self):
        """
        Given this quotient space `Q = V / W`, return the natural quotient
        map from `V` to `Q`.

        EXAMPLES::

            sage: A = (ZZ**2) / span([[4,0],[0,3]], ZZ)
            sage: A.quotient_map()
            Coercion map:
              From: Ambient free module of rank 2 over the principal ideal domain Integer Ring
              To:   Finitely generated module V/W over Integer Ring with invariants (12)
        """

def random_fgp_module(n, R=..., finite: bool = False):
    """
    Return a random FGP module inside a rank n free module over R.

    INPUT:

    - ``n`` -- nonnegative integer

    - ``R`` -- base ring (default: ``ZZ``)

    - ``finite`` -- boolean (default: ``True``); if ``True``, make the random
      module finite

    EXAMPLES::

        sage: import sage.modules.fg_pid.fgp_module as fgp
        sage: fgp.random_fgp_module(4)
        Finitely generated module V/W over Integer Ring with invariants (...)

    In most cases the cardinality is small or infinite::

        sage: for g in (1, 2, 3, +Infinity):
        ....:     while fgp.random_fgp_module(4).cardinality() != 1:
        ....:         pass

    One can force a finite module::

        sage: fgp.random_fgp_module(4, finite=True).is_finite()
        True

    Larger finite modules appear::

        sage: while fgp.random_fgp_module(4, finite=True).cardinality() < 100:
        ....:     pass
    """
def random_fgp_morphism_0(*args, **kwds):
    """
    Construct a random fgp module using :func:`random_fgp_module`,
    then construct a random morphism that sends each generator
    to a random multiple of itself.

    Inputs are the same as to :func:`random_fgp_module`.

    EXAMPLES::

        sage: import sage.modules.fg_pid.fgp_module as fgp
        sage: mor = fgp.random_fgp_morphism_0(4)
        sage: mor.domain() == mor.codomain()
        True
        sage: isinstance(mor.domain(), fgp.FGP_Module_class)
        True

    Each generator is sent to a random multiple of itself::

        sage: gens = mor.domain().gens()
        sage: im_gens = mor.im_gens()
        sage: all(im_gens[i] == sum(im_gens[i])*gens[i] for i in range(len(gens)))
        True
    """

test_morphism_0: Incomplete
