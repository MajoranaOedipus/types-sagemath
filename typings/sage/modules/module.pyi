import _cython_3_2_1
import sage.structure.parent
from typing import Any, ClassVar, overload

is_Module: _cython_3_2_1.cython_function_or_method
is_VectorSpace: _cython_3_2_1.cython_function_or_method

class Module(sage.structure.parent.Parent):
    """Module(base, category=None, names=None)

    File: /build/sagemath/src/sage/src/sage/modules/module.pyx (starting at line 68)

    Generic module class.

    INPUT:

    - ``base`` -- a ring; the base ring of the module

    - ``category`` -- a category (default: ``None``), the category for this
      module. If ``None``, then this is set to the category of modules/vector
      spaces over ``base``.

    - ``names`` -- names of generators

    EXAMPLES::

        sage: from sage.modules.module import Module
        sage: M = Module(ZZ)
        sage: M.base_ring()
        Integer Ring
        sage: M.category()
        Category of modules over Integer Ring

    Normally the category is set to the category of modules over ``base``. If
    ``base`` is a field, then the category is the category of vector spaces
    over ``base``::

        sage: M_QQ = Module(QQ)
        sage: M_QQ.category()
        Category of vector spaces over Rational Field

    The ``category`` parameter can be used to set a more specific category::

        sage: N = Module(ZZ, category=FiniteDimensionalModulesWithBasis(ZZ))
        sage: N.category()
        Category of finite dimensional modules with basis over Integer Ring

     TESTS:

     We check that :issue:`8119` has been resolved::

        sage: # needs sage.modules
        sage: M = ZZ^3
        sage: h = M.__hash__()
        sage: M.rename('toto')
        sage: h == M.__hash__()
        True"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, *args, **kwargs) -> None:
        """File: /build/sagemath/src/sage/src/sage/modules/module.pyx (starting at line 116)

                Initialization.

                TESTS::

                    sage: from sage.modules.module import Module
                    sage: M = Module(ZZ)
                    sage: type(M)
                    <class 'sage.modules.module.Module'>
        """
    @overload
    def base_extend(self, R) -> Any:
        """Module.base_extend(self, R)

        File: /build/sagemath/src/sage/src/sage/modules/module.pyx (starting at line 198)

        Return the base extension of ``self`` to `R`.

        This is the same as ``self.change_ring(R)`` except that a
        :exc:`TypeError` is raised if there is no canonical coerce map
        from the base ring of ``self`` to `R`.

        INPUT:

        - ``R`` -- ring

        EXAMPLES::

            sage: V = ZZ^7                                                              # needs sage.modules
            sage: V.base_extend(QQ)                                                     # needs sage.modules
            Vector space of dimension 7 over Rational Field

        TESTS::

            sage: N = ModularForms(6, 4)                                                # needs sage.modular
            sage: N.base_extend(CyclotomicField(7))                                     # needs sage.modular sage.rings.number_field
            Modular Forms space of dimension 5 for Congruence Subgroup Gamma0(6)
             of weight 4 over Cyclotomic Field of order 7 and degree 6

            sage: m = ModularForms(DirichletGroup(13).0^2,2); m                         # needs sage.modular sage.rings.number_field
            Modular Forms space of dimension 3, character [zeta6] and weight 2
             over Cyclotomic Field of order 6 and degree 2
            sage: m.base_extend(CyclotomicField(12))                                    # needs sage.modular sage.rings.number_field
            Modular Forms space of dimension 3, character [zeta6] and weight 2
             over Cyclotomic Field of order 12 and degree 4

            sage: # needs sage.modular sage.rings.number_field
            sage: chi = DirichletGroup(109, CyclotomicField(3)).0
            sage: S3 = CuspForms(chi, 2)
            sage: S9 = S3.base_extend(CyclotomicField(9)); S9
            Cuspidal subspace of dimension 8 of
             Modular Forms space of dimension 10, character [zeta3 + 1] and weight 2
              over Cyclotomic Field of order 9 and degree 6
            sage: S9.has_coerce_map_from(S3)    # not implemented
            True
            sage: S9.base_extend(CyclotomicField(3))
            Traceback (most recent call last):
            ...
            TypeError: Base extension of self (over 'Cyclotomic Field of order 9 and degree 6')
            to ring 'Cyclotomic Field of order 3 and degree 2' not defined."""
    @overload
    def base_extend(self, QQ) -> Any:
        """Module.base_extend(self, R)

        File: /build/sagemath/src/sage/src/sage/modules/module.pyx (starting at line 198)

        Return the base extension of ``self`` to `R`.

        This is the same as ``self.change_ring(R)`` except that a
        :exc:`TypeError` is raised if there is no canonical coerce map
        from the base ring of ``self`` to `R`.

        INPUT:

        - ``R`` -- ring

        EXAMPLES::

            sage: V = ZZ^7                                                              # needs sage.modules
            sage: V.base_extend(QQ)                                                     # needs sage.modules
            Vector space of dimension 7 over Rational Field

        TESTS::

            sage: N = ModularForms(6, 4)                                                # needs sage.modular
            sage: N.base_extend(CyclotomicField(7))                                     # needs sage.modular sage.rings.number_field
            Modular Forms space of dimension 5 for Congruence Subgroup Gamma0(6)
             of weight 4 over Cyclotomic Field of order 7 and degree 6

            sage: m = ModularForms(DirichletGroup(13).0^2,2); m                         # needs sage.modular sage.rings.number_field
            Modular Forms space of dimension 3, character [zeta6] and weight 2
             over Cyclotomic Field of order 6 and degree 2
            sage: m.base_extend(CyclotomicField(12))                                    # needs sage.modular sage.rings.number_field
            Modular Forms space of dimension 3, character [zeta6] and weight 2
             over Cyclotomic Field of order 12 and degree 4

            sage: # needs sage.modular sage.rings.number_field
            sage: chi = DirichletGroup(109, CyclotomicField(3)).0
            sage: S3 = CuspForms(chi, 2)
            sage: S9 = S3.base_extend(CyclotomicField(9)); S9
            Cuspidal subspace of dimension 8 of
             Modular Forms space of dimension 10, character [zeta3 + 1] and weight 2
              over Cyclotomic Field of order 9 and degree 6
            sage: S9.has_coerce_map_from(S3)    # not implemented
            True
            sage: S9.base_extend(CyclotomicField(3))
            Traceback (most recent call last):
            ...
            TypeError: Base extension of self (over 'Cyclotomic Field of order 9 and degree 6')
            to ring 'Cyclotomic Field of order 3 and degree 2' not defined."""
    @overload
    def change_ring(self, R) -> Any:
        """Module.change_ring(self, R)

        File: /build/sagemath/src/sage/src/sage/modules/module.pyx (starting at line 181)

        Return the base change of ``self`` to `R`.

        EXAMPLES::

            sage: from sage.modular.modform.space import ModularFormsSpace              # needs sage.modular
            sage: ModularFormsSpace(Gamma0(11), 2,                                      # needs sage.modular sage.rings.finite_rings
            ....:                   DirichletGroup(1)[0], QQ).change_ring(GF(7))
            Traceback (most recent call last):
            ...
            NotImplementedError: the method change_ring() has not yet been implemented"""
    @overload
    def change_ring(self) -> Any:
        """Module.change_ring(self, R)

        File: /build/sagemath/src/sage/src/sage/modules/module.pyx (starting at line 181)

        Return the base change of ``self`` to `R`.

        EXAMPLES::

            sage: from sage.modular.modform.space import ModularFormsSpace              # needs sage.modular
            sage: ModularFormsSpace(Gamma0(11), 2,                                      # needs sage.modular sage.rings.finite_rings
            ....:                   DirichletGroup(1)[0], QQ).change_ring(GF(7))
            Traceback (most recent call last):
            ...
            NotImplementedError: the method change_ring() has not yet been implemented"""
    @overload
    def endomorphism_ring(self) -> Any:
        """Module.endomorphism_ring(self)

        File: /build/sagemath/src/sage/src/sage/modules/module.pyx (starting at line 250)

        Return the endomorphism ring of this module in its category.

        EXAMPLES::

            sage: from sage.modules.module import Module
            sage: M = Module(ZZ)
            sage: M.endomorphism_ring()
            Set of Morphisms
             from <sage.modules.module.Module object at ...>
               to <sage.modules.module.Module object at ...>
               in Category of modules over Integer Ring"""
    @overload
    def endomorphism_ring(self) -> Any:
        """Module.endomorphism_ring(self)

        File: /build/sagemath/src/sage/src/sage/modules/module.pyx (starting at line 250)

        Return the endomorphism ring of this module in its category.

        EXAMPLES::

            sage: from sage.modules.module import Module
            sage: M = Module(ZZ)
            sage: M.endomorphism_ring()
            Set of Morphisms
             from <sage.modules.module.Module object at ...>
               to <sage.modules.module.Module object at ...>
               in Category of modules over Integer Ring"""
