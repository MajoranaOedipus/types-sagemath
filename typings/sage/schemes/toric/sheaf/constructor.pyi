from sage.modules.filtered_vector_space import FilteredVectorSpace as FilteredVectorSpace
from sage.schemes.toric.variety import ToricVariety_field as ToricVariety_field

def TangentBundle(X):
    """
    Construct the tangent bundle of a toric variety.

    INPUT:

    - ``X`` -- a toric variety; the base space of the bundle

    OUTPUT: the tangent bundle as a Klyachko bundle

    EXAMPLES::

        sage: dP7 = toric_varieties.dP7()
        sage: from sage.schemes.toric.sheaf.constructor import TangentBundle
        sage: TangentBundle(dP7)
        Rank 2 bundle on 2-d CPR-Fano toric variety covered by 5 affine patches.
    """
def CotangentBundle(X):
    """
    Construct the cotangent bundle of a toric variety.

    INPUT:

    - ``X`` -- a toric variety; the base space of the bundle

    OUTPUT: the cotangent bundle as a Klyachko bundle

    EXAMPLES::

        sage: dP7 = toric_varieties.dP7()
        sage: from sage.schemes.toric.sheaf.constructor import CotangentBundle
        sage: CotangentBundle(dP7)
        Rank 2 bundle on 2-d CPR-Fano toric variety covered by 5 affine patches.
    """
def TrivialBundle(X, rank: int = 1):
    """
    Return the trivial bundle of rank ``r``.

    INPUT:

    - ``X`` -- a toric variety; the base space of the bundle

    - ``rank`` -- the rank of the bundle

    OUTPUT: the trivial bundle as a Klyachko bundle

    EXAMPLES::

        sage: P2 = toric_varieties.P2()
        sage: from sage.schemes.toric.sheaf.constructor import TrivialBundle
        sage: I3 = TrivialBundle(P2, 3);  I3
        Rank 3 bundle on 2-d CPR-Fano toric variety covered by 3 affine patches.
        sage: I3.cohomology(weight=(0,0), dim=True)
        (3, 0, 0)
    """
def LineBundle(X, D):
    """
    Construct the rank-1 bundle `O(D)`.

    INPUT:

    - ``X`` -- a toric variety; the base space of the bundle

    - ``D`` -- a toric divisor

    OUTPUT:

    The line bundle `O(D)` as a Klyachko bundle of rank 1.

    EXAMPLES::

        sage: X = toric_varieties.dP8()
        sage: D = X.divisor(0)
        sage: from sage.schemes.toric.sheaf.constructor import LineBundle
        sage: O_D = LineBundle(X, D)
        sage: O_D.cohomology(dim=True, weight=(0,0))
        (1, 0, 0)
    """

class SheafLibrary:
    def __init__(self, toric_variety) -> None:
        """
        Utility object to construct sheaves on toric varieties.

        .. warning::

            You should never construct instances manually. Can be
            accessed from a toric variety via the
            :attr:`sage.schemes.toric.variety.ToricVariety_field.sheaves`
            attribute.

        EXAMPLES::

            sage: type(toric_varieties.P2().sheaves)
            <class 'sage.schemes.toric.sheaf.constructor.SheafLibrary'>
        """
    def trivial_bundle(self, rank: int = 1):
        """
        Return the trivial bundle of rank ``r``.

        INPUT:

        - ``rank`` -- integer (default: `1`); the rank of the bundle

        OUTPUT: the trivial bundle as a Klyachko bundle

        EXAMPLES::

            sage: P2 = toric_varieties.P2()
            sage: I3 = P2.sheaves.trivial_bundle(3);  I3
            Rank 3 bundle on 2-d CPR-Fano toric variety covered by 3 affine patches.
            sage: I3.cohomology(weight=(0,0), dim=True)
            (3, 0, 0)
        """
    def line_bundle(self, divisor):
        """
        Construct the rank-1 bundle `O(D)`.

        INPUT:

        - ``divisor`` -- a toric divisor

        OUTPUT:

        The line bundle `O(D)` for the given divisor as a Klyachko
        bundle of rank 1.

        EXAMPLES::

            sage: X = toric_varieties.dP8()
            sage: D = X.divisor(0)
            sage: O_D = X.sheaves.line_bundle(D)
            sage: O_D.cohomology(dim=True, weight=(0,0))
            (1, 0, 0)
        """
    def tangent_bundle(self):
        """
        Return the tangent bundle of the toric variety.

        OUTPUT: the tangent bundle as a Klyachko bundle

        EXAMPLES::

            sage: toric_varieties.dP6().sheaves.tangent_bundle()
            Rank 2 bundle on 2-d CPR-Fano toric variety covered by 6 affine patches.
        """
    def cotangent_bundle(self):
        """
        Return the cotangent bundle of the toric variety.

        OUTPUT: the cotangent bundle as a Klyachko bundle

        EXAMPLES::

            sage: dP6 = toric_varieties.dP6()
            sage: TX = dP6.sheaves.tangent_bundle()
            sage: TXdual = dP6.sheaves.cotangent_bundle()
            sage: TXdual == TX.dual()
            True
        """
    def Klyachko(self, multi_filtration):
        """
        Construct a Klyachko bundle (sheaf) from filtration data.

        INPUT:

        - ``multi_filtration`` -- a multi-filtered vectors space with
          multiple filtrations being indexed by the rays of the
          fan. Either an instance of
          :func:`~sage.modules.multi_filtered_vector_space.MultiFilteredVectorSpace`
          or something (like a dictionary of ordinary filtered vector
          spaces).

        OUTPUT:

        The Klyachko bundle defined by the filtrations, one for each
        ray, of a vector space.

        EXAMPLES::

            sage: P1 = toric_varieties.P1()
            sage: v1, v2, v3 = [(1,0,0), (0,1,0), (0,0,1)]
            sage: F1 = FilteredVectorSpace({1: [v1, v2, v3], 3: [v1]})
            sage: F2 = FilteredVectorSpace({0: [v1, v2, v3], 2: [v2, v3]})
            sage: P1 = toric_varieties.P1()
            sage: r1, r2 = P1.fan().rays()
            sage: F = MultiFilteredVectorSpace({r1:F1, r2:F2});  F
            Filtrations
                N(-1): QQ^3 >= QQ^2 >= QQ^2 >=  0   >= 0
                 N(1): QQ^3 >= QQ^3 >= QQ^1 >= QQ^1 >= 0
            sage: P1.sheaves.Klyachko(F)
            Rank 3 bundle on 1-d CPR-Fano toric variety covered by 2 affine patches.
        """
    def divisor(self, *args, **kwds):
        """
        Return a toric divisor.

        INPUT:

        This is just an alias for
        :meth:`sage.schemes.toric.variety.ToricVariety_field.divisor`,
        see there for details.

        By abuse of notation, you can usually use the divisor `D`
        interchangeably with the line bundle `O(D)`.

        OUTPUT: a toric divisor

        EXAMPLES::

            sage: dP6 = toric_varieties.dP6()
            sage: dP6.inject_variables()
            Defining x, u, y, v, z, w
            sage: D = dP6.sheaves.divisor(x*u^3);  D
            V(x) + 3*V(u)
            sage: D == dP6.divisor(x*u^3)
            True
        """
