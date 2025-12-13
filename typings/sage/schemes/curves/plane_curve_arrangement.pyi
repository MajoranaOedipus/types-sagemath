from sage.categories.sets_cat import Sets as Sets
from sage.groups.free_group import FreeGroup as FreeGroup
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.misc_c import prod as prod
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.qqbar import QQbar as QQbar
from sage.schemes.affine.affine_space import AffineSpace as AffineSpace
from sage.schemes.curves.affine_curve import AffinePlaneCurve as AffinePlaneCurve
from sage.schemes.curves.constructor import Curve as Curve
from sage.schemes.curves.projective_curve import ProjectivePlaneCurve as ProjectivePlaneCurve, ProjectiveSpace as ProjectiveSpace
from sage.schemes.curves.zariski_vankampen import braid_monodromy as braid_monodromy, fundamental_group_arrangement as fundamental_group_arrangement
from sage.structure.category_object import normalize_names as normalize_names
from sage.structure.element import Element as Element
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp as richcmp
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class PlaneCurveArrangementElement(Element):
    """
    An ordered plane curve arrangement.
    """
    def __init__(self, parent, curves, check: bool = True) -> None:
        """
        Construct a plane curve arrangement.

        INPUT:

        - ``parent`` -- the parent :class:`PlaneCurveArrangements`

        - ``curves`` -- tuple of curves

        EXAMPLES::

            sage: H.<x, y> = AffinePlaneCurveArrangements(QQ)
            sage: elt = H(x, y); elt
            Arrangement (x, y) in Affine Space of dimension 2 over Rational Field
            sage: TestSuite(elt).run()
            sage: H.<x, y, z> = ProjectivePlaneCurveArrangements(QQ)
            sage: elt = H(x, y); elt
            Arrangement (x, y) in Projective Space of dimension 2 over Rational Field
            sage: TestSuite(elt).run()
        """
    def __getitem__(self, i):
        """
        Return the `i`-th curve.

        INPUT:

        - ``i`` -- integer

        EXAMPLES::

            sage: H.<x, y> = AffinePlaneCurveArrangements(QQ)
            sage: H(y^2 - x, y^3 + 2 * x^2, x^4 + y^4 + 1)
            Arrangement (y^2 - x, y^3 + 2*x^2, x^4 + y^4 + 1)
            in Affine Space of dimension 2 over Rational Field
        """
    def __hash__(self) -> int:
        """
        TESTS::

            sage: H.<x, y> = AffinePlaneCurveArrangements(QQ)
            sage: H((x * y, x + y +1)).__hash__()   # random
            -4938643871296220686
        """
    def ncurves(self) -> int:
        """
        Return the number of curves in the arrangement.

        OUTPUT: integer

        EXAMPLES::

            sage: H.<x, y, z> = ProjectivePlaneCurveArrangements(QQ)
            sage: h = H((x * y, x + y + z))
            sage: h.ncurves()
            2
            sage: len(h)    # equivalent
            2
        """
    __len__ = ncurves
    def curves(self) -> tuple:
        """
        Return the curves in the arrangement as a tuple.

        OUTPUT: a tuple

        EXAMPLES::

            sage: H.<x, y> = AffinePlaneCurveArrangements(QQ)
            sage: h = H((x * y, x + y + 1))
            sage: h.curves()
            (Affine Plane Curve over Rational Field defined by x*y,
             Affine Plane Curve over Rational Field defined by x + y + 1)

        Note that the curves can be indexed as if they were a list::

            sage: h[1]
            Affine Plane Curve over Rational Field defined by x + y + 1
        """
    def union(self, other):
        """
        The union of ``self`` with ``other``.

        INPUT:

        - ``other`` -- a curve arrangement or something that can
          be converted into a curve arrangement

        OUTPUT: a new curve arrangement

        EXAMPLES::

            sage: H.<x, y> = AffinePlaneCurveArrangements(QQ)
            sage: h = H([x * y, x + y + 1, x^3 - y^5, x^2 * y^2 + x^5 + y^5, (x^2 + y^2)^3 + (x^3 + y^3 - 1)^2])
            sage: C = Curve(x^8 - y^8 -x^4 * y^4)
            sage: h1 = h.union(C); h1
            Arrangement of 6 curves in Affine Space of dimension 2 over Rational Field
            sage: h1 == h1.union(C)
            True
        """
    add_curves = union
    __or__ = union
    def deletion(self, curves):
        """
        Return the curve arrangement obtained by removing ``curves``.

        INPUT:

        - ``curves`` -- a curve or curve arrangement

        OUTPUT:

        A new curve arrangement with the given curve(s)
        ``h`` removed.

        EXAMPLES::

            sage: H.<x, y> = AffinePlaneCurveArrangements(QQ)
            sage: h = H([x * y, x + y + 1, x^3 - y^5, x^2 * y^2 + x^5 + y^5, (x^2 + y^2)^3 + (x^3 + y^3 - 1)^2])
            sage: C = h[-1]
            sage: h.deletion(C)
            Arrangement (x*y, x + y + 1, -y^5 + x^3, x^5 + y^5 + x^2*y^2)
            in Affine Space of dimension 2 over Rational Field
            sage: h.deletion(x)
            Traceback (most recent call last):
            ...
            ValueError: curve is not in the arrangement
            """
    def change_ring(self, base_ring):
        """
        Return curve arrangement over the new base ring.

        INPUT:

        - ``base_ring`` -- the new base ring; must be a field for
          curve arrangements

        OUTPUT:

        The curve arrangement obtained by changing the base
        field, as a new curve arrangement.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: H.<x, y> = AffinePlaneCurveArrangements(QQ)
            sage: A = H(y^2 - x^3, x, y, y^2 + x * y + x^2)
            sage: K.<a> = CyclotomicField(3)
            sage: A.change_ring(K)
            Arrangement (-x^3 + y^2, x, y, x^2 + x*y + y^2) in Affine Space of
            dimension 2 over Cyclotomic Field of order 3 and degree 2
        """
    @cached_method
    def coordinate_ring(self):
        """
        Return the coordinate ring of ``self``.

        OUTPUT: the coordinate ring of the curve arrangement

        EXAMPLES::

            sage: L.<x, y> = AffinePlaneCurveArrangements(QQ)
            sage: C = L(x, y)
            sage: C.coordinate_ring()
            Multivariate Polynomial Ring in x, y over Rational Field
            sage: P.<x, y, z> = ProjectivePlaneCurveArrangements(QQ)
            sage: C = P(x, y)
            sage: C.coordinate_ring()
            Multivariate Polynomial Ring in x, y, z over Rational Field
        """
    def defining_polynomials(self) -> tuple:
        """
        Return the defining polynomials of the elements of ``self``.

        EXAMPLES::

            sage: H.<x, y> = AffinePlaneCurveArrangements(QQ)
            sage: A = H(y^2 - x^3, x, y, y^2 + x * y + x^2)
            sage: A.defining_polynomials()
            (-x^3 + y^2, x, y, x^2 + x*y + y^2)
        """
    def defining_polynomial(self, simplified: bool = True):
        """
        Return the defining polynomial of the union of the curves in ``self``.

        EXAMPLES::

            sage: H.<x, y> = AffinePlaneCurveArrangements(QQ)
            sage: A = H(y ** 2 + x ** 2, x, y)
            sage: prod(A.defining_polynomials()) == A.defining_polynomial()
            True
        """
    def have_common_factors(self) -> bool:
        """
        Check if the curves have common factors.

        EXAMPLES::

            sage: H.<x, y> = AffinePlaneCurveArrangements(QQ)
            sage: A = H(x * y, x^2 + x* y^3)
            sage: A.have_common_factors()
            True
            sage: H(x * y, x + y^3).have_common_factors()
            False
        """
    def reduce(self, clean: bool = False, verbose: bool = False):
        """
        Replace the curves by their reduction.

        INPUT:

        - ``clean`` -- boolean (default: ``False``); if ``False``
          and there are common factors it returns ``None`` and
          a warning message. If ``True``, the common factors are kept
          only in the first occurrence.

        EXAMPLES::

            sage: H.<x, y> = AffinePlaneCurveArrangements(QQ)
            sage: A = H(y^2, (x + y)^3 * (x^2 + x * y + y^2))
            sage: A.reduce()
            Arrangement (y, x^3 + 2*x^2*y + 2*x*y^2 + y^3) in Affine Space
            of dimension 2 over Rational Field
            sage: C = H(x*y, x*(y + 1))
            sage: C.reduce(verbose=True)
            Some curves have common components
            sage: C.reduce(clean=True)
            Arrangement (x*y, y + 1) in Affine Space of dimension 2
            over Rational Field
            sage: C = H(x*y, x)
            sage: C.reduce(clean=True)
            Arrangement (x*y) in Affine Space of dimension 2 over Rational Field
        """

class AffinePlaneCurveArrangementElement(PlaneCurveArrangementElement):
    """
    An ordered affine plane curve arrangement.
    """
    def __init__(self, parent, curves, check: bool = True) -> None:
        """
        Construct an ordered affine plane curve arrangement.

        INPUT:

        - ``parent`` -- the parent :class:`AffinePlaneCurveArrangements`

        - ``curves`` -- tuple of curves

        EXAMPLES::

            sage: H.<x, y> = AffinePlaneCurveArrangements(QQ)
            sage: elt = H(x, y); elt
            Arrangement (x, y) in Affine Space of dimension 2 over Rational Field
            sage: TestSuite(elt).run()
        """
    def fundamental_group(self, simplified: bool = True, vertical: bool = True, projective: bool = False):
        """
        Return the fundamental group of the complement of the union
        of affine plane curves in `\\CC^2`.

        INPUT:

        - ``vertical`` -- boolean (default: ``True``); if ``True``, there
          are no vertical asymptotes, and there are vertical lines, then a
          simplified braid :func:`braid_monodromy` is used

        - ``simplified`` -- boolean (default: ``True``); if it is ``True``, the
          group is simplified

        - ``projective`` -- boolean (default: ``False``); to be used in the
          method for projective curves

        OUTPUT: a finitely presented group

        .. NOTE::

           This functionality requires the ``sirocco`` package to be installed.

        EXAMPLES::

            sage: # needs sirocco
            sage: H.<x, y> = AffinePlaneCurveArrangements(QQ)
            sage: A = H(y^2 + x, y + x - 1, x)
            sage: A.fundamental_group()
            Finitely presented group
            < x0, x1, x2 | x2*x0*x2^-1*x0^-1, x1*x0*x1^-1*x0^-1, (x2*x1)^2*(x2^-1*x1^-1)^2 >
            sage: A.meridians()
            {0: [x1, x2*x1*x2^-1], 1: [x0], 2: [x2],
             3: [x1^-1*x2^-1*x1^-1*x0^-1]}
            sage: G = A.fundamental_group(simplified=False)
            sage: G.sorted_presentation()
            Finitely presented group
            < x0, x1, x2, x3 | x3^-1*x2^-1*x3*x0*x1*x0^-1,
                               x3^-1*x1^-1*x3*x0*x1*x0^-1*x2^-1*x0^-1*(x2*x0)^2*x1^-1*x0^-1,
                               x3^-1*x0^-1*x3*x0*x1*x0^-1*x2^-1*x0*x2*x0*x1^-1*x0^-1,
                               x2^-1*x0^-1*x2*x0, x1^-1*x0^-1*x1*x0 >
            sage: A.meridians(simplified=False)
            {0: [x1, x2], 1: [x0], 2: [x3], 3: [x3^-1*x2^-1*x1^-1*x0^-1]}
            sage: A.fundamental_group(vertical=False)
            Finitely presented group
            < x0, x1, x2 | x2*x1^-1*x2^-1*x1, x1*x0*x1^-1*x0^-1, (x0*x2)^2*(x0^-1*x2^-1)^2 >
            sage: A.meridians(vertical=False)
            {0: [x2, x0*x2*x0^-1], 1: [x1], 2: [x0], 3: [x0*x2^-1*x0^-1*x2^-1*x1^-1*x0^-1]}
            sage: G = A.fundamental_group(simplified=False, vertical=False)
            sage: G.sorted_presentation()
            Finitely presented group
            < x0, x1, x2, x3 | x3^-1*x2^-1*x1^-1*x2*x3*x2^-1*x1*x2,
                               x3^-1*x2^-1*x1^-1*x2*x3*x2^-1*x1*x2,
                               (x3^-1*x2^-1*x0^-1*x2)^2*(x3*x2^-1*x0*x2)^2,
                               x3^-1*x2^-1*x0^-1*x2*x3^-1*x2^-1*x0*x2*x3*x2,
                               x1^-1*x0^-1*x1*x0 >
            sage: A.meridians(simplified=False, vertical=False)
            {0: [x2, x3], 1: [x1], 2: [x0], 3: [x3^-1*x2^-1*x1^-1*x0^-1]}
            sage: A = H(x * y^2 + x + y, y + x -1, x, y)
            sage: G = A.fundamental_group()
            sage: G.sorted_presentation()
            Finitely presented group
            < x0, x1, x2, x3 | x3^-1*x2^-1*x3*x2, x3^-1*x1^-1*x3*x1,
                               x3^-1*x0^-1*x3*x0, x2^-1*x1^-1*x2*x1,
                               x2^-1*x0^-1*x2*x0, x1^-1*x0^-1*x1*x0 >
        """
    def meridians(self, simplified: bool = True, vertical: bool = True) -> dict:
        """
        Return the meridians of each irreducible component.

        OUTPUT:

        A dictionary which associates the index of each curve with its meridians,
        including the line at infinity if it can be omputed

        .. NOTE::

           This functionality requires the ``sirocco`` package to be installed
           and :meth:`AffinePlaneCurveArrangements.fundamental_group` with the same options,
           where some examples are shown.

        EXAMPLES::

            sage: # needs sirocco
            sage: H.<x, y> = AffinePlaneCurveArrangements(QQ)
            sage: A = H(x-1, y, x, y - 1)
            sage: A.fundamental_group()
            Finitely presented group
            < x0, x1, x2, x3 | x2*x0*x2^-1*x0^-1, x2*x1*x2^-1*x1^-1,
                               x3*x0*x3^-1*x0^-1, x3*x1*x3^-1*x1^-1 >
            sage: A.meridians()
            {0: [x2], 1: [x0], 2: [x3], 3: [x1], 4: [x3^-1*x2^-1*x1^-1*x0^-1]}
        """
    def braid_monodromy(self, vertical: bool = True):
        """
        Return the braid monodromy of the complement of the union
        of affine plane curves in `\\CC^2`.

        If there are vertical asymptotes a change of variable is done.

        INPUT:

        - ``vertical`` -- boolean (default: ``True``); if it is ``True``, there
          are no vertical asymptotes, and there are vertical lines, then a
          simplified :func:`braid_monodromy` is computed.

        OUTPUT:

        A braid monodromy with dictionaries identifying strands with components
        and braids with vertical lines.

        .. NOTE::

           This functionality requires the ``sirocco`` package to be installed.

        EXAMPLES::

            sage: # needs sirocco
            sage: H.<x, y> = AffinePlaneCurveArrangements(QQ)
            sage: A = H(y^2 + x, y + x - 1, x)
            sage: A.braid_monodromy(vertical=False)
            [s1*s0*(s1*s2*s1)^2*s2*(s1^-1*s2^-1)^2*s1^-1*s0^-1*s1^-1,
             s1*s0*(s1*s2)^2*s2*s1^-1*s2^-1*s1^-1*s0^-1*s1^-1,
             s1*s0*s1*s2*(s1*s2^-1)^2*s0*s1*s2*s1*s0*s2^-1*s1^-3*s2*s1^-1*s2^-1*s1^-1*s0^-1*s1^-1,
             s1*s0*s1*s2*s1*s2^-1*s1^4*s2*s1^-1*s2^-1*s1^-1*s0^-1*s1^-1,
             s1*s0*s1*s2*s1*s2^-1*s1^-1*s2*s0^-1*s1^-1]
            sage: A.braid_monodromy(vertical=True)
            [s1*s0*s1*s0^-1*s1^-1*s0, s0^-1*s1*s0*s1^-1*s0, s0^-1*s1^2*s0]
        """
    def strands(self):
        """
        Return the strands for each member of the arrangement.

        OUTPUT:

        A dictionary which associates to the index of each strand
        its associated component if the braid monodromy has been
        calculated with ``vertical=False``.

        .. NOTE::

           This functionality requires the ``sirocco`` package to be installed.

        EXAMPLES::

            sage: # needs sirocco
            sage: H.<x, y> = AffinePlaneCurveArrangements(QQ)
            sage: A = H(y^2 + x, y + x - 1, x)
            sage: bm = A.braid_monodromy()
            sage: A.strands()
            {0: 2, 1: 1, 2: 0, 3: 0}
        """
    def vertical_strands(self):
        """
        Return the strands if the braid monodromy has been computed with
        the vertical option.

        OUTPUT:

        A dictionary which associates to the index of each strand
        its associated component if the braid monodromy has been
        calculated with ``vertical=True``.

        .. NOTE::

           This functionality requires the ``sirocco`` package to be installed.

        EXAMPLES::

            sage: # needs sirocco
            sage: H.<x, y> = AffinePlaneCurveArrangements(QQ)
            sage: A = H(y^2 + x, y + x - 1, x)
            sage: A.vertical_strands()
            {0: 1, 1: 0, 2: 0}
            sage: A.braid_monodromy(vertical=True)
            [s1*s0*s1*s0^-1*s1^-1*s0, s0^-1*s1*s0*s1^-1*s0, s0^-1*s1^2*s0]
        """
    def vertical_lines_in_braid_monodromy(self):
        """
        Return the vertical lines in the arrangement.

        OUTPUT:

        A dictionary which associates the index of a braid
        to the index of the vertical line associated to the braid.

        .. NOTE::

           This functionality requires the ``sirocco`` package to be installed.

        EXAMPLES::

            sage: # needs sirocco
            sage: H.<x, y> = AffinePlaneCurveArrangements(QQ)
            sage: A = H(y^2 + x, y + x - 1, x)
            sage: A.vertical_lines_in_braid_monodromy()
            {1: 2}
            sage: A.braid_monodromy(vertical=True)
            [s1*s0*s1*s0^-1*s1^-1*s0, s0^-1*s1*s0*s1^-1*s0, s0^-1*s1^2*s0]
        """

class ProjectivePlaneCurveArrangementElement(PlaneCurveArrangementElement):
    """
    An ordered projective plane curve arrangement.
    """
    def __init__(self, parent, curves, check: bool = True) -> None:
        """
        Construct an ordered projective plane curve arrangement.

        INPUT:

        - ``parent`` -- the parent :class:`ProjectivePlaneCurveArrangements`

        - ``curves`` -- tuple of curves

        EXAMPLES::

            sage: H.<x, y, z> = ProjectivePlaneCurveArrangements(QQ)
            sage: elt = H(x, y, z); elt
            Arrangement (x, y, z) in Projective Space of dimension 2 over Rational Field
            sage: TestSuite(elt).run()
        """
    def fundamental_group(self, simplified: bool = True):
        """
        Return the fundamental group of the complement of the union
        of an arrangement of projective plane curves
        in the projective plane.

        INPUT:

        - ``simplified`` -- boolean (default: ``True``); set if the group
          is simplified

        OUTPUT: a finitely presented group

        .. NOTE::

           This functionality requires the ``sirocco`` package to be installed.

        EXAMPLES::

            sage: # needs sirocco
            sage: H.<x, y, z> = ProjectivePlaneCurveArrangements(QQ)
            sage: H(z).fundamental_group()
            Finitely presented group <  |  >
            sage: H(x*y).fundamental_group()
            Finitely presented group < x |  >
            sage: A = H(y^2 + x*z, y + x - z, x)
            sage: A.fundamental_group().sorted_presentation()
            Finitely presented group < x0, x1 | x1^-1*x0^-1*x1*x0 >
            sage: A.meridians()
            {0: [x1], 1: [x0], 2: [x0^-1*x1^-2]}
            sage: G = A.fundamental_group(simplified=False)
            sage: G.sorted_presentation()
            Finitely presented group
            < x0, x1, x2, x3 | x3^-1*x2^-1*x1^-1*x0^-1, x3^-1*x2^-1*x3*x0*x1*x0^-1,
                               x3^-1*x1^-1*x3*x0*x1*x0^-1*x2^-1*x0^-1*(x2*x0)^2*x1^-1*x0^-1,
                               x3^-1*x0^-1*x3*x0*x1*x0^-1*x2^-1*x0*x2*x0*x1^-1*x0^-1,
                               x2^-1*x0^-1*x2*x0, x1^-1*x0^-1*x1*x0 >
            sage: A.meridians(simplified=False)
            {0: [x1, x2], 1: [x0], 2: [x3]}
            sage: A = H(y^2 + x*z, z, x)
            sage: A.fundamental_group()
            Finitely presented group < x0, x1 | (x1*x0)^2*(x1^-1*x0^-1)^2 >
            sage: A = H(y^2 + x*z, z*x, y)
            sage: A.fundamental_group()
            Finitely presented group
            < x0, x1, x2 | x2*x0*x1*x0^-1*x2^-1*x1^-1,
                           x1*(x2*x0)^2*x2^-1*x1^-1*x0^-1*x2^-1*x0^-1 >
        """
    def meridians(self, simplified: bool = True) -> dict:
        """
        Return the meridians of each irreducible component.

        OUTPUT:

        A dictionary which associates the index of each curve with
        its meridians, including the line at infinity if it can be
        computed

        .. NOTE::

           This function requires the ``sirocco`` package to be installed and
           :func:`ProjectivePlaneCurveArrangements.fundamental_group`
           with the same options, where some examples are shown.

        EXAMPLES::

            sage: # needs sirocco
            sage: H.<x, y, z> = ProjectivePlaneCurveArrangements(QQ)
            sage: A = H(y^2 + x*z, y + x - z, x)
            sage: A.fundamental_group().sorted_presentation()
            Finitely presented group < x0, x1 | x1^-1*x0^-1*x1*x0 >
            sage: A.meridians()
            {0: [x1], 1: [x0], 2: [x0^-1*x1^-2]}
            sage: A = H(y^2 + x*z, z, x)
            sage: A.fundamental_group()
            Finitely presented group < x0, x1 | (x1*x0)^2*(x1^-1*x0^-1)^2 >
            sage: A.meridians()
            {0: [x0, x1*x0*x1^-1], 1: [x0^-1*x1^-1*x0^-1], 2: [x1]}
            sage: A = H(y^2 + x*z, z*x, y)
            sage: A.fundamental_group()
            Finitely presented group < x0, x1, x2 | x2*x0*x1*x0^-1*x2^-1*x1^-1,
                                                    x1*(x2*x0)^2*x2^-1*x1^-1*x0^-1*x2^-1*x0^-1 >
            sage: A.meridians()
            {0: [x0, x2*x0*x2^-1], 1: [x2, x0^-1*x2^-1*x1^-1*x0^-1], 2: [x1]}
        """

class PlaneCurveArrangements(UniqueRepresentation, Parent):
    """
    Plane curve arrangements.

    INPUT:

    - ``base_ring`` -- ring; the base ring

    - ``names`` -- tuple of strings; the variable names

    EXAMPLES::

        sage: H.<x, y> = AffinePlaneCurveArrangements(QQ)
        sage: H(x, y^2, x-1, y-1)
        Arrangement (x, y^2, x - 1, y - 1) in Affine Space
        of dimension 2 over Rational Field
    """
    Element = PlaneCurveArrangementElement
    @staticmethod
    def __classcall__(cls, base, names: tuple[str, ...] = ()):
        """
        Normalize the inputs to ensure a unique representation.

        TESTS::

            sage: H.<x, y> = AffinePlaneCurveArrangements(QQ)
            sage: K = AffinePlaneCurveArrangements(QQ, names=('x', 'y'))
            sage: H is K
            True
        """
    def __init__(self, base_ring, names: tuple[str, ...] = ()) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: H.<x, y> = AffinePlaneCurveArrangements(QQ)
            sage: TestSuite(H).run()
        """
    def coordinate_ring(self):
        """
        Return the coordinate ring.

        OUTPUT: the coordinate ring of the curve arrangement

        EXAMPLES::

            sage: L.<x, y> = AffinePlaneCurveArrangements(QQ)
            sage: L.coordinate_ring()
            Multivariate Polynomial Ring in x, y over Rational Field
        """
    def change_ring(self, base_ring):
        """
        Return curve arrangements over a different base ring.

        INPUT:

        - ``base_ring`` -- a ring; the new base ring

        OUTPUT:

        A new :class:`PlaneCurveArrangements` instance over the new
        base ring

        EXAMPLES::

            sage: L.<x, y> = AffinePlaneCurveArrangements(QQ)
            sage: L.change_ring(RR).base_ring()
            Real Field with 53 bits of precision

        TESTS::

            sage: L.change_ring(QQ) is L
            True
        """
    @abstract_method
    def ambient_space(self) -> None:
        """
        Return the ambient space.

        EXAMPLES::

            sage: L.<x, y> = PlaneCurveArrangements(QQ)
            Traceback (most recent call last):
            ...
            NotImplementedError: <abstract method ambient_space at  0x...>
            sage: L.<x, y> = AffinePlaneCurveArrangements(QQ)
            sage: L.ambient_space()
            Affine Space of dimension 2 over Rational Field
            sage: L.<x, y, z> = ProjectivePlaneCurveArrangements(QQ)
            sage: L.ambient_space()
            Projective Space of dimension 2 over Rational Field
        """
    @cached_method
    def ngens(self):
        """
        Return the number of variables, i.e. 2 or 3, kept for completeness.

        OUTPUT: integer, 2 or 3, depending if the arrangement is projective or affine

        EXAMPLES::

            sage: L.<x, y> = AffinePlaneCurveArrangements(QQ)
            sage: L.ngens()
            2
            sage: L.<x, y, z> = ProjectivePlaneCurveArrangements(QQ)
            sage: L.ngens()
            3
        """
    def gens(self) -> tuple:
        """
        Return the coordinates.

        OUTPUT: a tuple of linear expressions, one for each linear variable

        EXAMPLES::

            sage: L = AffinePlaneCurveArrangements(QQ, ('x', 'y'))
            sage: L.gens()
            (x, y)
            sage: L = ProjectivePlaneCurveArrangements(QQ, ('x', 'y', 'z'))
            sage: L.gens()
            (x, y, z)
        """
    def gen(self, i):
        """
        Return the `i`-th coordinate.

        INPUT:

        - ``i`` -- integer

        OUTPUT: a variable

        EXAMPLES::

            sage: L.<x, y> = AffinePlaneCurveArrangements(QQ)
            sage: L.gen(1)
            y
            sage: L.<x, y, z> = ProjectivePlaneCurveArrangements(QQ)
            sage: L.gen(2)
            z
        """

class AffinePlaneCurveArrangements(PlaneCurveArrangements):
    """
    Affine curve arrangements.

    INPUT:

    - ``base_ring`` -- ring; the base ring

    - ``names`` -- tuple of strings; the variable names

    EXAMPLES::

        sage: H.<x, y> = AffinePlaneCurveArrangements(QQ)
        sage: H(x, y^2, x-1, y-1)
        Arrangement (x, y^2, x - 1, y - 1) in Affine Space
        of dimension 2 over Rational Field
    """
    Element = AffinePlaneCurveArrangementElement
    def ambient_space(self):
        """
        Return the ambient space.

        EXAMPLES::

            sage: L.<x, y> = AffinePlaneCurveArrangements(QQ)
            sage: L.ambient_space()
            Affine Space of dimension 2 over Rational Field
        """

class ProjectivePlaneCurveArrangements(PlaneCurveArrangements):
    """
    Projective curve arrangements.

    INPUT:

    - ``base_ring`` -- ring; the base ring

    - ``names`` -- tuple of strings; the variable names

    EXAMPLES::

        sage: H.<x, y, z> = ProjectivePlaneCurveArrangements(QQ)
        sage: H(x, y^2, x-z, y-z)
        Arrangement (x, y^2, x - z, y - z) in Projective Space
        of dimension 2 over Rational Field
    """
    Element = ProjectivePlaneCurveArrangementElement
    def ambient_space(self):
        """
        Return the ambient space.

        EXAMPLES::

            sage: L.<x, y, z> = ProjectivePlaneCurveArrangements(QQ)
            sage: L.ambient_space()
            Projective Space of dimension 2 over Rational Field
        """
