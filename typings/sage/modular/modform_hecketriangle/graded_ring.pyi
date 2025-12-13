from .abstract_ring import FormsRing_abstract as FormsRing_abstract
from .hecke_triangle_groups import HeckeTriangleGroup as HeckeTriangleGroup
from sage.categories.algebras import Algebras as Algebras
from sage.rings.infinity import infinity as infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

def canonical_parameters(group, base_ring, red_hom, n=None):
    """
    Return a canonical version of the parameters.

    EXAMPLES::

        sage: from sage.modular.modform_hecketriangle.graded_ring import canonical_parameters
        sage: canonical_parameters(4, ZZ, 1)
        (Hecke triangle group for n = 4, Integer Ring, True, 4)
        sage: canonical_parameters(infinity, RR, 0)
        (Hecke triangle group for n = +Infinity, Real Field with 53 bits of precision, False, +Infinity)
    """

class QuasiMeromorphicModularFormsRing(FormsRing_abstract, UniqueRepresentation):
    """
    Graded ring of (Hecke) quasi meromorphic modular forms
    for the given group and base ring.
    """
    @staticmethod
    def __classcall__(cls, group=..., base_ring=..., red_hom: bool = False, n=None):
        """
        Return a (cached) instance with canonical parameters.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import (canonical_parameters, QuasiMeromorphicModularFormsRing)
            sage: (group, base_ring, red_hom, n) = canonical_parameters(4, ZZ, 1)
            sage: QuasiMeromorphicModularFormsRing(4, ZZ, 1) == QuasiMeromorphicModularFormsRing(group, base_ring, red_hom, n)
            True
        """
    def __init__(self, group, base_ring, red_hom, n) -> None:
        """
        Return the graded ring of (Hecke) quasi meromorphic modular forms
        for the given ``group`` and ``base_ring``.

        INPUT:

        - ``group`` -- the Hecke triangle group (default: ``HeckeTriangleGroup(3)``)

        - ``base_ring`` -- the base_ring (default: ``ZZ``)

        - ``red_hom`` -- if ``True`` then results of binary operations are
          considered homogeneous whenever it makes sense (default: ``False``).
          This is mainly used by the spaces of homogeneous elements.

        OUTPUT:

        The corresponding graded ring of (Hecke) quasi meromorphic modular forms
        for the given ``group`` and ``base_ring``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import QuasiMeromorphicModularFormsRing
            sage: MR = QuasiMeromorphicModularFormsRing(4, ZZ, 1)
            sage: MR
            QuasiMeromorphicModularFormsRing(n=4) over Integer Ring
            sage: MR.analytic_type()
            quasi meromorphic modular
            sage: MR.category()
            Category of commutative algebras over Integer Ring
            sage: MR in MR.category()
            True

            sage: QuasiMeromorphicModularFormsRing(n=infinity)
            QuasiMeromorphicModularFormsRing(n=+Infinity) over Integer Ring
        """

class QuasiWeakModularFormsRing(FormsRing_abstract, UniqueRepresentation):
    """
    Graded ring of (Hecke) quasi weakly holomorphic modular forms
    for the given group and base ring.
    """
    @staticmethod
    def __classcall__(cls, group=..., base_ring=..., red_hom: bool = False, n=None):
        """
        Return a (cached) instance with canonical parameters.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import (canonical_parameters, QuasiWeakModularFormsRing)
            sage: (group, base_ring, red_hom, n) = canonical_parameters(5, CC, 0)
            sage: QuasiWeakModularFormsRing(5, CC, 0) == QuasiWeakModularFormsRing(group, base_ring, red_hom, n)
            True
        """
    def __init__(self, group, base_ring, red_hom, n) -> None:
        """
        Return the graded ring of (Hecke) quasi weakly holomorphic modular forms
        for the given ``group`` and ``base_ring``.

        INPUT:

        - ``group`` -- the Hecke triangle group (default: ``HeckeTriangleGroup(3)``)

        - ``base_ring`` -- the base_ring (default: ``ZZ``)

        - ``red_hom`` -- if ``True`` then results of binary operations are
          considered homogeneous whenever it makes sense (default: ``False``).
          This is mainly used by the spaces of homogeneous elements.

        OUTPUT:

        The corresponding graded ring of (Hecke) quasi weakly holomorphic modular forms
        for the given ``group`` and ``base_ring``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import QuasiWeakModularFormsRing
            sage: MR = QuasiWeakModularFormsRing(5, CC, 0)
            sage: MR
            QuasiWeakModularFormsRing(n=5) over Complex Field with 53 bits of precision
            sage: MR.analytic_type()
            quasi weakly holomorphic modular
            sage: MR.category()
            Category of commutative algebras over Complex Field with 53 bits of precision
            sage: MR in MR.category()
            True
        """

class QuasiModularFormsRing(FormsRing_abstract, UniqueRepresentation):
    """
    Graded ring of (Hecke) quasi modular forms
    for the given group and base ring
    """
    @staticmethod
    def __classcall__(cls, group=..., base_ring=..., red_hom: bool = False, n=None):
        """
        Return a (cached) instance with canonical parameters.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import (canonical_parameters, QuasiModularFormsRing)
            sage: (group, base_ring, red_hom, n) = canonical_parameters(6, ZZ, True)
            sage: QuasiModularFormsRing(6, ZZ, True) == QuasiModularFormsRing(group, base_ring, red_hom, n)
            True
        """
    def __init__(self, group, base_ring, red_hom, n) -> None:
        """
        Return the graded ring of (Hecke) quasi modular forms
        for the given ``group`` and ``base_ring``.

        INPUT:

        - ``group`` -- the Hecke triangle group (default: ``HeckeTriangleGroup(3)``)

        - ``base_ring`` -- the base_ring (default: ``ZZ``)

        - ``red_hom`` -- if ``True`` then results of binary operations are
          considered homogeneous whenever it makes sense (default: ``False``).
          This is mainly used by the spaces of homogeneous elements.

        OUTPUT:

        The corresponding graded ring of (Hecke) quasi modular forms
        for the given ``group`` and ``base_ring``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import QuasiModularFormsRing
            sage: MR = QuasiModularFormsRing(6, ZZ, True)
            sage: MR
            QuasiModularFormsRing(n=6) over Integer Ring
            sage: MR.analytic_type()
            quasi modular
            sage: MR.category()
            Category of commutative algebras over Integer Ring
            sage: MR in MR.category()
            True
        """

class QuasiCuspFormsRing(FormsRing_abstract, UniqueRepresentation):
    """
    Graded ring of (Hecke) quasi cusp forms
    for the given group and base ring.
    """
    @staticmethod
    def __classcall__(cls, group=..., base_ring=..., red_hom: bool = False, n=None):
        """
        Return a (cached) instance with canonical parameters.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import (canonical_parameters, QuasiCuspFormsRing)
            sage: (group, base_ring, red_hom, n) = canonical_parameters(7, ZZ, 1)
            sage: QuasiCuspFormsRing(7, ZZ, 1) == QuasiCuspFormsRing(group, base_ring, red_hom, n)
            True
        """
    def __init__(self, group, base_ring, red_hom, n) -> None:
        """
        Return the graded ring of (Hecke) quasi cusp forms
        for the given ``group`` and ``base_ring``.

        INPUT:

        - ``group`` -- the Hecke triangle group (default: ``HeckeTriangleGroup(3)``)

        - ``base_ring`` -- the base_ring (default: ``ZZ``)

        - ``red_hom`` -- if ``True`` then results of binary operations are
          considered homogeneous whenever it makes sense (default: ``False``).
          This is mainly used by the spaces of homogeneous elements.

        OUTPUT:

        The corresponding graded ring of (Hecke) quasi cusp forms
        for the given ``group`` and ``base_ring``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import QuasiCuspFormsRing
            sage: MR = QuasiCuspFormsRing(7, ZZ, 1)
            sage: MR
            QuasiCuspFormsRing(n=7) over Integer Ring
            sage: MR.analytic_type()
            quasi cuspidal
            sage: MR.category()
            Category of commutative algebras over Integer Ring
            sage: MR in MR.category()
            True
        """

class MeromorphicModularFormsRing(FormsRing_abstract, UniqueRepresentation):
    """
    Graded ring of (Hecke) meromorphic modular forms
    for the given group and base ring
    """
    @staticmethod
    def __classcall__(cls, group=..., base_ring=..., red_hom: bool = False, n=None):
        """
        Return a (cached) instance with canonical parameters.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import (canonical_parameters, MeromorphicModularFormsRing)
            sage: (group, base_ring, red_hom, n) = canonical_parameters(4, ZZ, 1)
            sage: MeromorphicModularFormsRing(4, ZZ, 1) == MeromorphicModularFormsRing(group, base_ring, red_hom, n)
            True
        """
    def __init__(self, group, base_ring, red_hom, n) -> None:
        """
        Return the graded ring of (Hecke) meromorphic modular forms
        for the given ``group`` and ``base_ring``.

        INPUT:

        - ``group`` -- the Hecke triangle group (default: ``HeckeTriangleGroup(3)``)

        - ``base_ring`` -- the base_ring (default: ``ZZ``)

        - ``red_hom`` -- if ``True`` then results of binary operations are
          considered homogeneous whenever it makes sense (default: ``False``).
          This is mainly used by the spaces of homogeneous elements.

        OUTPUT:

        The corresponding graded ring of (Hecke) meromorphic modular forms
        for the given ``group`` and ``base_ring``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import MeromorphicModularFormsRing
            sage: MR = MeromorphicModularFormsRing(4, ZZ, 1)
            sage: MR
            MeromorphicModularFormsRing(n=4) over Integer Ring
            sage: MR.analytic_type()
            meromorphic modular
            sage: MR.category()
            Category of commutative algebras over Integer Ring
            sage: MR in MR.category()
            True
        """

class WeakModularFormsRing(FormsRing_abstract, UniqueRepresentation):
    """
    Graded ring of (Hecke) weakly holomorphic modular forms
    for the given group and base ring
    """
    @staticmethod
    def __classcall__(cls, group=..., base_ring=..., red_hom: bool = False, n=None):
        """
        Return a (cached) instance with canonical parameters.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import (canonical_parameters, WeakModularFormsRing)
            sage: (group, base_ring, red_hom, n) = canonical_parameters(5, ZZ, 0)
            sage: WeakModularFormsRing(5, ZZ, 0) == WeakModularFormsRing(group, base_ring, red_hom, n)
            True
        """
    def __init__(self, group, base_ring, red_hom, n) -> None:
        """
        Return the graded ring of (Hecke) weakly holomorphic modular forms
        for the given ``group`` and ``base_ring``.

        INPUT:

        - ``group`` -- the Hecke triangle group (default: ``HeckeTriangleGroup(3)``)

        - ``base_ring`` -- the base_ring (default: ``ZZ``)

        - ``red_hom`` -- if ``True`` then results of binary operations are
          considered homogeneous whenever it makes sense (default: ``False``).
          This is mainly used by the spaces of homogeneous elements.

        OUTPUT:

        The corresponding graded ring of (Hecke) weakly holomorphic modular forms
        for the given ``group`` and ``base_ring``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import WeakModularFormsRing
            sage: MR = WeakModularFormsRing(5, ZZ, 0)
            sage: MR
            WeakModularFormsRing(n=5) over Integer Ring
            sage: MR.analytic_type()
            weakly holomorphic modular
            sage: MR.category()
            Category of commutative algebras over Integer Ring
            sage: MR in MR.category()
            True
        """

class ModularFormsRing(FormsRing_abstract, UniqueRepresentation):
    """
    Graded ring of (Hecke) modular forms
    for the given group and base ring
    """
    @staticmethod
    def __classcall__(cls, group=..., base_ring=..., red_hom: bool = False, n=None):
        """
        Return a (cached) instance with canonical parameters.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import ModularFormsRing
            sage: ModularFormsRing(3, ZZ, 0) == ModularFormsRing()
            True
        """
    def __init__(self, group, base_ring, red_hom, n) -> None:
        """
        Return the graded ring of (Hecke) modular forms
        for the given ``group`` and ``base_ring``.

        INPUT:

        - ``group`` -- the Hecke triangle group (default: ``HeckeTriangleGroup(3)``)

        - ``base_ring`` -- the base_ring (default: ``ZZ``)

        - ``red_hom`` -- if ``True`` then results of binary operations are
          considered homogeneous whenever it makes sense (default: ``False``).
          This is mainly used by the spaces of homogeneous elements.

        OUTPUT:

        The corresponding graded ring of (Hecke) modular forms
        for the given ``group`` and ``base_ring``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import ModularFormsRing
            sage: MR = ModularFormsRing()
            sage: MR
            ModularFormsRing(n=3) over Integer Ring
            sage: MR.analytic_type()
            modular
            sage: MR.category()
            Category of commutative algebras over Integer Ring
            sage: MR in MR.category()
            True
        """

class CuspFormsRing(FormsRing_abstract, UniqueRepresentation):
    """
    Graded ring of (Hecke) cusp forms
    for the given group and base ring
    """
    @staticmethod
    def __classcall__(cls, group=..., base_ring=..., red_hom: bool = False, n=None):
        """
        Return a (cached) instance with canonical parameters.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import (canonical_parameters, CuspFormsRing)
            sage: (group, base_ring, red_hom, n) = canonical_parameters(5, CC, True)
            sage: CuspFormsRing(5, CC, True) == CuspFormsRing(group, base_ring, red_hom, n)
            True
        """
    def __init__(self, group, base_ring, red_hom, n) -> None:
        """
        Return the graded ring of (Hecke) cusp forms
        for the given ``group`` and ``base_ring``.

        INPUT:

        - ``group`` -- the Hecke triangle group (default: ``HeckeTriangleGroup(3)``)

        - ``base_ring`` -- the base_ring (default: ``ZZ``)

        - ``red_hom`` -- if ``True`` then results of binary operations are
          considered homogeneous whenever it makes sense (default: ``False``).
          This is mainly used by the spaces of homogeneous elements.

        OUTPUT:

        The corresponding graded ring of (Hecke) cusp forms
        for the given ``group`` and ``base_ring``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import CuspFormsRing
            sage: MR = CuspFormsRing(5, CC, True)
            sage: MR
            CuspFormsRing(n=5) over Complex Field with 53 bits of precision
            sage: MR.analytic_type()
            cuspidal
            sage: MR.category()
            Category of commutative algebras over Complex Field with 53 bits of precision
            sage: MR in MR.category()
            True

            sage: CuspFormsRing(n=infinity, base_ring=CC, red_hom=True)
            CuspFormsRing(n=+Infinity) over Complex Field with 53 bits of precision
        """
