from .fgp_module import DEBUG as DEBUG
from sage.categories.homset import Homset as Homset
from sage.categories.morphism import Morphism as Morphism
from sage.misc.cachefunc import cached_method as cached_method
from sage.structure.richcmp import op_NE as op_NE, richcmp as richcmp

class FGP_Morphism(Morphism):
    """
    A morphism between finitely generated modules over a PID.

    EXAMPLES:

    An endomorphism::

        sage: V = span([[1/2,1,1],[3/2,2,1],[0,0,1]],ZZ); W = V.span([2*V.0+4*V.1, 9*V.0+12*V.1, 4*V.2])
        sage: Q = V/W; Q
        Finitely generated module V/W over Integer Ring with invariants (4, 12)
        sage: phi = Q.hom([Q.0+3*Q.1, -Q.1]); phi
        Morphism from module over Integer Ring with invariants (4, 12) to module with invariants (4, 12) that sends the generators to [(1, 3), (0, 11)]
        sage: phi(Q.0) == Q.0 + 3*Q.1
        True
        sage: phi(Q.1) == -Q.1
        True

    A morphism between different modules V1/W1 ---> V2/W2 in
    different ambient spaces::

        sage: V1 = ZZ^2; W1 = V1.span([[1,2],[3,4]]); A1 = V1/W1
        sage: V2 = span([[1/2,1,1],[3/2,2,1],[0,0,1]],ZZ); W2 = V2.span([2*V2.0+4*V2.1, 9*V2.0+12*V2.1, 4*V2.2]); A2=V2/W2
        sage: A1
        Finitely generated module V/W over Integer Ring with invariants (2)
        sage: A2
        Finitely generated module V/W over Integer Ring with invariants (4, 12)
        sage: phi = A1.hom([2*A2.0])
        sage: phi(A1.0)
        (2, 0)
        sage: 2*A2.0
        (2, 0)
        sage: phi(2*A1.0)
        (0, 0)

    TESTS::

        sage: V = span([[1/2,1,1],[3/2,2,1],[0,0,1]],ZZ); W = V.span([2*V.0+4*V.1, 9*V.0+12*V.1, 4*V.2]); Q = V/W
        sage: phi = Q.hom([Q.0,Q.0 + 2*Q.1])
        sage: loads(dumps(phi)) == phi
        True
    """
    def __init__(self, parent, phi, check: bool = True) -> None:
        """
        A morphism between finitely generated modules over a PID.

        EXAMPLES::

            sage: V = span([[1/2,1,1],[3/2,2,1],[0,0,1]],ZZ); W = V.span([2*V.0+4*V.1, 9*V.0+12*V.1, 4*V.2])
            sage: Q = V/W; Q
            Finitely generated module V/W over Integer Ring with invariants (4, 12)
            sage: phi = Q.hom([Q.0+3*Q.1, -Q.1]); phi
            Morphism from module over Integer Ring with invariants (4, 12) to module with invariants (4, 12) that sends the generators to [(1, 3), (0, 11)]
            sage: phi(Q.0) == Q.0 + 3*Q.1
            True
            sage: phi(Q.1) == -Q.1
            True

        For full documentation, see :class:`FGP_Morphism`.
        """
    @cached_method
    def im_gens(self):
        """
        Return tuple of the images of the generators of the domain
        under this morphism.

        EXAMPLES::

            sage: V = span([[1/2,1,1],[3/2,2,1],[0,0,1]],ZZ); W = V.span([2*V.0+4*V.1, 9*V.0+12*V.1, 4*V.2]); Q = V/W
            sage: phi = Q.hom([Q.0,Q.0 + 2*Q.1])
            sage: phi.im_gens()
            ((1, 0), (1, 2))
            sage: phi.im_gens() is phi.im_gens()
            True
        """
    def __add__(self, right):
        """
        EXAMPLES::

            sage: V = span([[1/2,1,1],[3/2,2,1],[0,0,1]],ZZ); W = V.span([2*V.0+4*V.1, 9*V.0+12*V.1, 4*V.2])
            sage: Q=V/W; phi = Q.hom([2*Q.0, Q.1]); phi
            Morphism from module over Integer Ring with invariants (4, 12) to module with invariants (4, 12) that sends the generators to [(2, 0), (0, 1)]
            sage: phi + phi
            Morphism from module over Integer Ring with invariants (4, 12) to module with invariants (4, 12) that sends the generators to [(0, 0), (0, 2)]
        """
    def __sub__(self, right):
        """
        EXAMPLES::

            sage: V = span([[1/2,1,1],[3/2,2,1],[0,0,1]],ZZ); W = V.span([2*V.0+4*V.1, 9*V.0+12*V.1, 4*V.2])
            sage: Q=V/W; phi = Q.hom([2*Q.0, Q.1])
            sage: phi - phi
            Morphism from module over Integer Ring with invariants (4, 12) to module with invariants (4, 12) that sends the generators to [(0, 0), (0, 0)]
        """
    def __neg__(self):
        """
        EXAMPLES::

            sage: V = span([[1/2,1,1],[3/2,2,1],[0,0,1]],ZZ); W = V.span([2*V.0+4*V.1, 9*V.0+12*V.1, 4*V.2])
            sage: Q=V/W; phi = Q.hom([2*Q.0, Q.1])
            sage: -phi
            Morphism from module over Integer Ring with invariants (4, 12) to module with invariants (4, 12) that sends the generators to [(2, 0), (0, 11)]
        """
    def __call__(self, x):
        """
        EXAMPLES::

            sage: V = span([[1/2,1,1],[3/2,2,1],[0,0,1]],ZZ); W = V.span([2*V.0+4*V.1, 9*V.0+12*V.1, 4*V.2])
            sage: Q = V/W
            sage: phi = Q.hom([Q.0+3*Q.1, -Q.1])
            sage: phi(Q.0) == Q.0 + 3*Q.1
            True

        We compute the image of some submodules of the domain::

            sage: phi(Q)
            Finitely generated module V/W over Integer Ring with invariants (4, 12)
            sage: phi(Q.submodule([Q.0]))
            Finitely generated module V/W over Integer Ring with invariants (4)
            sage: phi(Q.submodule([Q.1]))
            Finitely generated module V/W over Integer Ring with invariants (12)
            sage: phi(W/W)
            Finitely generated module V/W over Integer Ring with invariants ()

        We try to evaluate on a module that is not a submodule of the domain, which raises a ValueError::

            sage: phi(V/W.scale(2))
            Traceback (most recent call last):
            ...
            ValueError: x must be a submodule or element of the domain

        We evaluate on an element of the domain that is not in the V
        for the optimized representation of the domain::

            sage: V = span([[1/2,0,0],[3/2,2,1],[0,0,1]],ZZ); W = V.span([2*V.0+4*V.1, 9*V.0+12*V.1, 4*V.2])
            sage: Q = V/W; Q
            Finitely generated module V/W over Integer Ring with invariants (4, 12)
            sage: O, X = Q.optimized()
            sage: O.V()
            Free module of degree 3 and rank 2 over Integer Ring
            User basis matrix:
            [ 0  6  1]
            [ 0 -2  0]
            sage: phi = Q.hom([Q.0, 4*Q.1])
            sage: x = Q(V.0); x
            (0, 8)
            sage: x == 8*Q.1
            True
            sage: x in O.V()
            False
            sage: phi(x)
            (0, 8)
            sage: phi(8*Q.1)
            (0, 8)
            sage: phi(8*Q.1) == phi(x)
            True
        """
    def kernel(self):
        """
        Compute the kernel of this homomorphism.

        EXAMPLES::

            sage: V = span([[1/2,1,1],[3/2,2,1],[0,0,1]],ZZ); W = V.span([2*V.0+4*V.1, 9*V.0+12*V.1, 4*V.2])
            sage: Q = V/W; Q
            Finitely generated module V/W over Integer Ring with invariants (4, 12)
            sage: Q.hom([0, Q.1]).kernel()
            Finitely generated module V/W over Integer Ring with invariants (4)
            sage: A = Q.hom([Q.0, 0]).kernel(); A
            Finitely generated module V/W over Integer Ring with invariants (12)
            sage: Q.1 in A
            True
            sage: phi = Q.hom([Q.0-3*Q.1, Q.0+Q.1])
            sage: A = phi.kernel(); A
            Finitely generated module V/W over Integer Ring with invariants (4)
            sage: phi(A)
            Finitely generated module V/W over Integer Ring with invariants ()
        """
    def inverse_image(self, A):
        """
        Given a submodule A of the codomain of this morphism, return
        the inverse image of A under this morphism.

        EXAMPLES::

            sage: V = span([[1/2,1,1],[3/2,2,1],[0,0,1]],ZZ); W = V.span([2*V.0+4*V.1, 9*V.0+12*V.1, 4*V.2]); Q = V/W; Q
            Finitely generated module V/W over Integer Ring with invariants (4, 12)
            sage: phi = Q.hom([0, Q.1])
            sage: phi.inverse_image(Q.submodule([]))
            Finitely generated module V/W over Integer Ring with invariants (4)
            sage: phi.kernel()
            Finitely generated module V/W over Integer Ring with invariants (4)
            sage: phi.inverse_image(phi.codomain())
            Finitely generated module V/W over Integer Ring with invariants (4, 12)

            sage: phi.inverse_image(Q.submodule([Q.0]))
            Finitely generated module V/W over Integer Ring with invariants (4)
            sage: phi.inverse_image(Q.submodule([Q.1]))
            Finitely generated module V/W over Integer Ring with invariants (4, 12)

            sage: phi.inverse_image(ZZ^3)
            Traceback (most recent call last):
            ...
            TypeError: A must be a finitely generated quotient module
            sage: phi.inverse_image(ZZ^3 / W.scale(2))
            Traceback (most recent call last):
            ...
            ValueError: A must be a submodule of the codomain
        """
    def image(self):
        """
        Compute the image of this homomorphism.

        EXAMPLES::

            sage: V = span([[1/2,1,1],[3/2,2,1],[0,0,1]],ZZ); W = V.span([2*V.0+4*V.1, 9*V.0+12*V.1, 4*V.2])
            sage: Q = V/W; Q
            Finitely generated module V/W over Integer Ring with invariants (4, 12)
            sage: Q.hom([Q.0+3*Q.1, -Q.1]).image()
            Finitely generated module V/W over Integer Ring with invariants (4, 12)
            sage: Q.hom([3*Q.1, Q.1]).image()
            Finitely generated module V/W over Integer Ring with invariants (12)
        """
    def lift(self, x):
        """
        Given an element x in the codomain of self, if possible find an
        element y in the domain such that self(y) == x.  Raise a ValueError
        if no such y exists.

        INPUT:

        - ``x`` -- element of the codomain of self

        EXAMPLES::

            sage: V = span([[1/2,1,1],[3/2,2,1],[0,0,1]],ZZ); W = V.span([2*V.0+4*V.1, 9*V.0+12*V.1, 4*V.2])
            sage: Q=V/W; phi = Q.hom([2*Q.0, Q.1])
            sage: phi.lift(Q.1)
            (0, 1)
            sage: phi.lift(Q.0)
            Traceback (most recent call last):
            ...
            ValueError: no lift of element to domain
            sage: phi.lift(2*Q.0)
            (1, 0)
            sage: phi.lift(2*Q.0+Q.1)
            (1, 1)
            sage: V = span([[5, -1/2]],ZZ); W = span([[20,-2]],ZZ); Q = V/W; phi=Q.hom([2*Q.0])
            sage: x = phi.image().0; phi(phi.lift(x)) == x
            True
        """

def FGP_Homset(X, Y):
    """
    EXAMPLES::

        sage: V = span([[1/2,1,1],[3/2,2,1],[0,0,1]],ZZ); W = V.span([2*V.0+4*V.1, 9*V.0+12*V.1, 4*V.2]); Q = V/W
        sage: Q.Hom(Q)           # indirect doctest
        Set of Morphisms from Finitely generated module V/W over Integer Ring with invariants (4, 12) to Finitely generated module V/W over Integer Ring with invariants (4, 12) in Category of modules over Integer Ring
        sage: True # Q.Hom(Q) is Q.Hom(Q)
        True
        sage: type(Q.Hom(Q))
        <class 'sage.modules.fg_pid.fgp_morphism.FGP_Homset_class_with_category'>
    """

class FGP_Homset_class(Homset):
    """
    Homsets of :class:`~sage.modules.fg_pid.fgp_module.FGP_Module`.

    TESTS::

        sage: V = span([[1/2,1,1],[3/2,2,1],[0,0,1]],ZZ); W = V.span([2*V.0+4*V.1, 9*V.0+12*V.1, 4*V.2]); Q = V/W
        sage: H = Hom(Q,Q); H    # indirect doctest
        Set of Morphisms from Finitely generated module V/W over Integer Ring with invariants (4, 12) to Finitely generated module V/W over Integer Ring with invariants (4, 12) in Category of modules over Integer Ring
        sage: type(H)
        <class 'sage.modules.fg_pid.fgp_morphism.FGP_Homset_class_with_category'>
    """
    Element = FGP_Morphism
    def __init__(self, X, Y, category=None) -> None:
        """
        EXAMPLES::

            sage: V = span([[1/2,1,1],[3/2,2,1],[0,0,1]],ZZ); W = V.span([2*V.0+4*V.1, 9*V.0+12*V.1, 4*V.2]); Q = V/W
            sage: type(Q.Hom(Q))
            <class 'sage.modules.fg_pid.fgp_morphism.FGP_Homset_class_with_category'>
        """
    def __call__(self, x):
        """
        Convert x into an fgp morphism.

        EXAMPLES::

            sage: V = span([[1/2,0,0],[3/2,2,1],[0,0,1]],ZZ); W = V.span([V.0+2*V.1, 9*V.0+2*V.1, 4*V.2])
            sage: Q = V/W; H = Q.Hom(Q)
            sage: H(3)
            Morphism from module over Integer Ring with invariants (4, 16) to module with invariants (4, 16) that sends the generators to [(3, 0), (0, 3)]
        """
