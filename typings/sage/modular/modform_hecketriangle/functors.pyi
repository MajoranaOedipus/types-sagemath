from .abstract_space import FormsSpace_abstract as FormsSpace_abstract
from .analytic_type import AnalyticType as AnalyticType
from .constructor import FormsRing as FormsRing, FormsSpace as FormsSpace
from .subspace import SubSpaceForms as SubSpaceForms
from _typeshed import Incomplete
from sage.categories.commutative_additive_groups import CommutativeAdditiveGroups as CommutativeAdditiveGroups
from sage.categories.functor import Functor as Functor
from sage.categories.pushout import ConstructionFunctor as ConstructionFunctor
from sage.categories.rings import Rings as Rings
from sage.categories.sets_cat import Sets as Sets
from sage.rings.infinity import infinity as infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

def ConstantFormsSpaceFunctor(group):
    '''
    Construction functor for the space of constant forms.

    When determining a common parent between a ring
    and a forms ring or space this functor is first
    applied to the ring.

    EXAMPLES::

        sage: from sage.modular.modform_hecketriangle.functors import (ConstantFormsSpaceFunctor, FormsSpaceFunctor)
        sage: ConstantFormsSpaceFunctor(4) == FormsSpaceFunctor("holo", 4, 0, 1)
        True
        sage: ConstantFormsSpaceFunctor(4)
        ModularFormsFunctor(n=4, k=0, ep=1)
    '''

class FormsSubSpaceFunctor(ConstructionFunctor):
    """
    Construction functor for forms sub spaces.
    """
    rank: int
    def __init__(self, ambient_space_functor, generators) -> None:
        '''
        Construction functor for the forms sub space
        for the given ``generators`` inside the ambient space
        which is constructed by the ``ambient_space_functor``.

        The functor can only be applied to rings for which the generators
        can be converted into the corresponding forms space
        given by the ``ambient_space_functor`` applied to the ring.

        See :meth:`__call__` for a description of the functor.

        INPUT:

        - ``ambient_space_functor`` -- a FormsSpaceFunctor

        - ``generators`` -- a list of elements of some ambient space
          over some base ring

        OUTPUT: the construction functor for the corresponding forms sub space

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.functors import (FormsSpaceFunctor, FormsSubSpaceFunctor)
            sage: from sage.modular.modform_hecketriangle.space import ModularForms
            sage: ambient_space = ModularForms(n=4, k=12, ep=1)
            sage: ambient_space_functor = FormsSpaceFunctor("holo", group=4, k=12, ep=1)
            sage: ambient_space_functor
            ModularFormsFunctor(n=4, k=12, ep=1)
            sage: el = ambient_space.gen(0).full_reduce()
            sage: FormsSubSpaceFunctor(ambient_space_functor, [el])
            FormsSubSpaceFunctor with 1 generator for the ModularFormsFunctor(n=4, k=12, ep=1)
        '''
    def __call__(self, R):
        '''
        Return the corresponding subspace of the ambient space
        constructed by ``self._ambient_space`` with the generators ``self._generators``.
        If the ambient space is not a forms space the ambient space is returned.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.functors import (FormsSpaceFunctor, FormsSubSpaceFunctor, BaseFacade)
            sage: from sage.modular.modform_hecketriangle.space import CuspForms
            sage: ambient_space = CuspForms(n=4, k=12, ep=1)
            sage: ambient_space_functor = FormsSpaceFunctor("cusp", group=4, k=12, ep=1)
            sage: el = ambient_space.gen(0)
            sage: F = FormsSubSpaceFunctor(ambient_space_functor, [el])
            sage: F
            FormsSubSpaceFunctor with 1 generator for the CuspFormsFunctor(n=4, k=12, ep=1)

            sage: F(BaseFacade(ZZ))
            Subspace of dimension 1 of CuspForms(n=4, k=12, ep=1) over Integer Ring
            sage: F(BaseFacade(QQ))
            Subspace of dimension 1 of CuspForms(n=4, k=12, ep=1) over Integer Ring
            sage: F(QQ)
            ModularFormsRing(n=4) over Integer Ring

            sage: ambient_space_functor = FormsSpaceFunctor("holo", group=4, k=0, ep=1)
            sage: F = FormsSubSpaceFunctor(ambient_space_functor, [1])
            sage: F
            FormsSubSpaceFunctor with 1 generator for the ModularFormsFunctor(n=4, k=0, ep=1)
            sage: F(BaseFacade(ZZ))
            Subspace of dimension 1 of ModularForms(n=4, k=0, ep=1) over Integer Ring
        '''
    def merge(self, other):
        '''
        Return the merged functor of ``self`` and ``other``.

        If ``other`` is a ``FormsSubSpaceFunctor`` then
        first the common ambient space functor is constructed by
        merging the two corresponding functors.

        If that ambient space functor is a FormsSpaceFunctor
        and the generators agree the corresponding ``FormsSubSpaceFunctor``
        is returned.

        If ``other`` is not a ``FormsSubSpaceFunctor`` then ``self``
        is merged as if it was its ambient space functor.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.functors import (FormsSpaceFunctor, FormsSubSpaceFunctor)
            sage: from sage.modular.modform_hecketriangle.space import ModularForms
            sage: ambient_space = ModularForms(n=4, k=12, ep=1)
            sage: ambient_space_functor1 = FormsSpaceFunctor("holo", group=4, k=12, ep=1)
            sage: ambient_space_functor2 = FormsSpaceFunctor("cusp", group=4, k=12, ep=1)
            sage: ss_functor1 = FormsSubSpaceFunctor(ambient_space_functor1, [ambient_space.gen(0)])
            sage: ss_functor2 = FormsSubSpaceFunctor(ambient_space_functor2, [ambient_space.gen(0)])
            sage: ss_functor3 = FormsSubSpaceFunctor(ambient_space_functor2, [2*ambient_space.gen(0)])
            sage: merged_ambient = ambient_space_functor1.merge(ambient_space_functor2)
            sage: merged_ambient
            ModularFormsFunctor(n=4, k=12, ep=1)
            sage: functor4 = FormsSpaceFunctor(["quasi", "cusp"], group=4, k=10, ep=-1)

            sage: ss_functor1.merge(ss_functor1) is ss_functor1
            True
            sage: ss_functor1.merge(ss_functor2)
            FormsSubSpaceFunctor with 2 generators for the ModularFormsFunctor(n=4, k=12, ep=1)
            sage: ss_functor1.merge(ss_functor2) == FormsSubSpaceFunctor(merged_ambient, [ambient_space.gen(0), ambient_space.gen(0)])
            True
            sage: ss_functor1.merge(ss_functor3) == FormsSubSpaceFunctor(merged_ambient, [ambient_space.gen(0), 2*ambient_space.gen(0)])
            True
            sage: ss_functor1.merge(ambient_space_functor2) == merged_ambient
            True
            sage: ss_functor1.merge(functor4)
            QuasiModularFormsRingFunctor(n=4, red_hom=True)
        '''
    def __eq__(self, other):
        '''
        Compare ``self`` and ``other``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.functors import (FormsSpaceFunctor, FormsSubSpaceFunctor)
            sage: from sage.modular.modform_hecketriangle.space import ModularForms
            sage: ambient_space = ModularForms(n=4, k=12, ep=1)
            sage: ambient_space_functor1 = FormsSpaceFunctor("holo", group=4, k=12, ep=1)
            sage: ss_functor1 = FormsSubSpaceFunctor(ambient_space_functor1, [ambient_space.gen(0)])
            sage: ss_functor2 = FormsSubSpaceFunctor(ambient_space_functor1, [ambient_space.gen(1)])
            sage: ss_functor1 == ss_functor2
            False
        '''

class FormsSpaceFunctor(ConstructionFunctor):
    """
    Construction functor for forms spaces.

    NOTE:

    When the base ring is not a ``BaseFacade`` the functor is first
    merged with the ConstantFormsSpaceFunctor.  This case occurs in
    the pushout constructions (when trying to find a common parent
    between a forms space and a ring which is not a ``BaseFacade``).
    """
    AT: Incomplete
    rank: int
    def __init__(self, analytic_type, group, k, ep) -> None:
        '''
        Construction functor for the forms space
        (or forms ring, see above) with
        the given ``analytic_type``, ``group``,
        weight ``k`` and multiplier ``ep``.

        See :meth:`__call__` for a description of the functor.

        INPUT:

        - ``analytic_type`` -- an element of ``AnalyticType()``

        - ``group`` -- the index of a Hecke Triangle group

        - ``k`` -- a rational number, the weight of the space

        - ``ep`` -- `1` or `-1`, the multiplier of the space

        OUTPUT: the construction functor for the corresponding forms space/ring

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.functors import FormsSpaceFunctor
            sage: FormsSpaceFunctor(["holo", "weak"], group=4, k=0, ep=-1)
            WeakModularFormsFunctor(n=4, k=0, ep=-1)
        '''
    def __call__(self, R):
        '''
        If ``R`` is a ``BaseFacade(S)`` then return the corresponding
        forms space with base ring ``_get_base_ring(S)``.

        If not then we first merge the functor with the ConstantFormsSpaceFunctor.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.functors import (FormsSpaceFunctor, BaseFacade)
            sage: F = FormsSpaceFunctor(["holo", "weak"], group=4, k=0, ep=-1)
            sage: F(BaseFacade(ZZ))
            WeakModularForms(n=4, k=0, ep=-1) over Integer Ring
            sage: F(BaseFacade(CC))
            WeakModularForms(n=4, k=0, ep=-1) over Complex Field with 53 bits of precision
            sage: F(CC)
            WeakModularFormsRing(n=4) over Complex Field with 53 bits of precision
            sage: F(CC).has_reduce_hom()
            True
        '''
    def merge(self, other):
        '''
        Return the merged functor of ``self`` and ``other``.

        It is only possible to merge instances of ``FormsSpaceFunctor``
        and ``FormsRingFunctor``. Also only if they share the same group.
        An ``FormsSubSpaceFunctors`` is replaced by its ambient space functor.

        The analytic type of the merged functor is the extension
        of the two analytic types of the functors.
        The ``red_hom`` parameter of the merged functor
        is the logical ``and`` of the two corresponding ``red_hom``
        parameters (where a forms space is assumed to have it
        set to ``True``).

        Two ``FormsSpaceFunctor`` with different (k,ep) are merged to a
        corresponding ``FormsRingFunctor``. Otherwise the corresponding
        (extended) ``FormsSpaceFunctor`` is returned.

        A ``FormsSpaceFunctor`` and ``FormsRingFunctor``
        are merged to a corresponding (extended) ``FormsRingFunctor``.

        Two ``FormsRingFunctors`` are merged to the corresponding
        (extended) ``FormsRingFunctor``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.functors import (FormsSpaceFunctor, FormsRingFunctor)
            sage: functor1 = FormsSpaceFunctor("holo", group=5, k=0, ep=1)
            sage: functor2 = FormsSpaceFunctor(["quasi", "cusp"], group=5, k=10/3, ep=-1)
            sage: functor3 = FormsSpaceFunctor(["quasi", "mero"], group=5, k=0, ep=1)
            sage: functor4 = FormsRingFunctor("cusp", group=5, red_hom=False)
            sage: functor5 = FormsSpaceFunctor("holo", group=4, k=0, ep=1)

            sage: functor1.merge(functor1) is functor1
            True
            sage: functor1.merge(functor5) is None
            True
            sage: functor1.merge(functor2)
            QuasiModularFormsRingFunctor(n=5, red_hom=True)
            sage: functor1.merge(functor3)
            QuasiMeromorphicModularFormsFunctor(n=5, k=0, ep=1)
            sage: functor1.merge(functor4)
            ModularFormsRingFunctor(n=5)
        '''
    def __eq__(self, other):
        '''
        Compare ``self`` and ``other``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.functors import FormsSpaceFunctor
            sage: functor1 = FormsSpaceFunctor("holo", group=4, k=12, ep=1)
            sage: functor2 = FormsSpaceFunctor("holo", group=4, k=12, ep=-1)
            sage: functor1 == functor2
            False
        '''

class FormsRingFunctor(ConstructionFunctor):
    """
    Construction functor for forms rings.

    NOTE:

    When the base ring is not a ``BaseFacade`` the functor is first
    merged with the ConstantFormsSpaceFunctor.  This case occurs in
    the pushout constructions.  (when trying to find a common parent
    between a forms ring and a ring which is not a ``BaseFacade``).
    """
    AT: Incomplete
    rank: int
    def __init__(self, analytic_type, group, red_hom) -> None:
        '''
        Construction functor for the forms ring
        with the given ``analytic_type``, ``group``
        and variable ``red_hom``

        See :meth:`__call__` for a description of the functor.

        INPUT:

        - ``analytic_type`` -- an element of ``AnalyticType()``

        - ``group`` -- the index of a Hecke Triangle group

        - ``red_hom`` -- a boolean variable for the parameter ``red_hom``
          (also see ``FormsRing_abstract``)

        OUTPUT: the construction functor for the corresponding forms ring

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.functors import FormsRingFunctor
            sage: FormsRingFunctor(["quasi", "mero"], group=6, red_hom=False)
            QuasiMeromorphicModularFormsRingFunctor(n=6)
            sage: FormsRingFunctor(["quasi", "mero"], group=6, red_hom=True)
            QuasiMeromorphicModularFormsRingFunctor(n=6, red_hom=True)
        '''
    def __call__(self, R):
        '''
        If ``R`` is a ``BaseFacade(S)`` then return the corresponding
        forms ring with base ring ``_get_base_ring(S)``.

        If not then we first merge the functor with the ConstantFormsSpaceFunctor.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.functors import (FormsRingFunctor, BaseFacade)
            sage: F = FormsRingFunctor(["quasi", "mero"], group=6, red_hom=False)
            sage: F(BaseFacade(ZZ))
            QuasiMeromorphicModularFormsRing(n=6) over Integer Ring
            sage: F(BaseFacade(CC))
            QuasiMeromorphicModularFormsRing(n=6) over Complex Field with 53 bits of precision
            sage: F(CC)
            QuasiMeromorphicModularFormsRing(n=6) over Complex Field with 53 bits of precision
            sage: F(CC).has_reduce_hom()
            False
        '''
    def merge(self, other):
        '''
        Return the merged functor of ``self`` and ``other``.

        It is only possible to merge instances of ``FormsSpaceFunctor``
        and ``FormsRingFunctor``. Also only if they share the same group.
        An ``FormsSubSpaceFunctors`` is replaced by its ambient space functor.

        The analytic type of the merged functor is the extension
        of the two analytic types of the functors.
        The ``red_hom`` parameter of the merged functor
        is the logical ``and`` of the two corresponding ``red_hom``
        parameters (where a forms space is assumed to have it
        set to ``True``).

        Two ``FormsSpaceFunctor`` with different (k,ep) are merged to a
        corresponding ``FormsRingFunctor``. Otherwise the corresponding
        (extended) ``FormsSpaceFunctor`` is returned.

        A ``FormsSpaceFunctor`` and ``FormsRingFunctor``
        are merged to a corresponding (extended) ``FormsRingFunctor``.

        Two ``FormsRingFunctors`` are merged to the corresponding
        (extended) ``FormsRingFunctor``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.functors import (FormsSpaceFunctor, FormsRingFunctor)
            sage: functor1 = FormsRingFunctor("mero", group=6, red_hom=True)
            sage: functor2 = FormsRingFunctor(["quasi", "cusp"], group=6, red_hom=False)
            sage: functor3 = FormsSpaceFunctor("weak", group=6, k=0, ep=1)
            sage: functor4 = FormsRingFunctor("mero", group=5, red_hom=True)

            sage: functor1.merge(functor1) is functor1
            True
            sage: functor1.merge(functor4) is None
            True
            sage: functor1.merge(functor2)
            QuasiMeromorphicModularFormsRingFunctor(n=6)
            sage: functor1.merge(functor3)
            MeromorphicModularFormsRingFunctor(n=6, red_hom=True)
        '''
    def __eq__(self, other):
        '''
        Compare ``self`` and ``other``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.functors import FormsRingFunctor
            sage: functor1 = FormsRingFunctor("holo", group=4, red_hom=True)
            sage: functor2 = FormsRingFunctor("holo", group=4, red_hom=False)
            sage: functor1 == functor2
            False
        '''

class BaseFacade(Parent, UniqueRepresentation):
    """
    BaseFacade of a ring.

    This class is used to distinguish the construction of
    constant elements (modular forms of weight 0) over the given ring
    and the construction of ``FormsRing`` or ``FormsSpace``
    based on the BaseFacade of the given ring.

    If that distinction was not made then ring elements
    couldn't be considered as constant modular forms
    in e.g. binary operations. Instead the coercion model would
    assume that the ring element lies in the common parent
    of the ring element and e.g. a ``FormsSpace`` which
    would give the ``FormsSpace`` over the ring. However
    this is not correct, the ``FormsSpace`` might
    (and probably will) not even contain the (constant)
    ring element. Hence we use the ``BaseFacade`` to
    distinguish the two cases.

    Since the ``BaseFacade`` of a ring embeds into that ring,
    a common base (resp. a coercion) between the two (or even a
    more general ring) can be found, namely the ring
    (not the ``BaseFacade`` of it).
    """
    def __init__(self, ring) -> None:
        """
        BaseFacade of ``ring`` (see above).

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.functors import BaseFacade
            sage: BaseFacade(ZZ)
            BaseFacade(Integer Ring)
            sage: ZZ.has_coerce_map_from(BaseFacade(ZZ))
            True
            sage: CC.has_coerce_map_from(BaseFacade(ZZ))
            True
        """
