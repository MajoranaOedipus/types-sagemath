import _cython_3_2_1
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

make_FvarsHandler: _cython_3_2_1.cython_function_or_method
make_KSHandler: _cython_3_2_1.cython_function_or_method

class FvarsHandler:
    '''FvarsHandler(n_slots, field, idx_to_sextuple, init_data=None, use_mp=0, pids_name=None, name=None, max_terms=20, n_bytes=32)

    File: /build/sagemath/src/sage/src/sage/algebras/fusion_rings/shm_managers.pyx (starting at line 364)

    A shared memory backed dict-like structure to manage the
    ``_fvars`` attribute of an F-matrix.

    This structure implements a representation of the F-symbols dictionary
    using a structured NumPy array backed by a contiguous shared memory
    object.

    The monomial data is stored in the ``exp_data`` structure. Monomial
    exponent data is stored contiguously and ``ticks`` are used to
    indicate different monomials.

    Coefficient data is stored in the ``coeff_nums`` and ``coeff_denom``
    arrays. The ``coeff_denom`` array stores the value
    ``d = coeff.denominator()`` for each cyclotomic coefficient. The
    ``coeff_nums`` array stores the values
    ``c.numerator() * d for c in coeff._coefficients()``, the abridged
    list representation of the cyclotomic coefficient ``coeff``.

    Each entry also has a boolean ``modified`` attribute, indicating
    whether it has been modified by the parent process. Entry retrieval
    is cached in each process, so each process must check whether
    entries have been modified before attempting retrieval.

    The parent process should construct this object without a
    ``name`` attribute. Children processes use the ``name`` attribute,
    accessed via ``self.shm.name`` to attach to the shared memory block.

    INPUT:

    - ``n_slots`` -- number of generators of the underlying polynomial ring
    - ``field`` -- base field for polynomial ring
    - ``idx_to_sextuple`` -- map relating a single integer index to a sextuple
      of ``FusionRing`` elements
    - ``init_data`` -- dictionary or :class:`FvarsHandler` object containing
      known squares for initialization, e.g., from a solver checkpoint
    - ``use_mp`` -- integer indicating the number of child processes
      used for multiprocessing; if running serially, use 0
    - ``pids_name`` -- the name of a ``ShareableList`` containing the
      process ``pid``\'s for every process in the pool (including the
      parent process)
    - ``name`` -- the name of a shared memory object
      (used by child processes for attaching)
    - ``max_terms`` -- maximum number of terms in each entry; since
      we use contiguous C-style memory blocks, the size of the block
      must be known in advance
    - ``n_bytes`` -- the number of bytes that should be allocated for
      each numerator and each denominator stored by the structure

    .. NOTE::

        To properly dispose of shared memory resources,
        ``self.shm.unlink()`` must be called before exiting.

    .. NOTE::

        If you ever encounter an :exc:`OverflowError` when running the
        :meth:`FMatrix.find_orthogonal_solution` solver, consider
        increasing the parameter ``n_bytes``.

    .. WARNING::

        The current data structure supports up to `2^16` entries,
        with each monomial in each entry having at most 254
        nonzero terms. On average, each of the ``max_terms`` monomials
        can have at most 30 terms.

    EXAMPLES::

        sage: from sage.algebras.fusion_rings.shm_managers import FvarsHandler
        sage: # Create shared data structure
        sage: f = FusionRing("A2", 1).get_fmatrix(inject_variables=True, new=True)
        creating variables fx1..fx8
        Defining fx0, fx1, fx2, fx3, fx4, fx5, fx6, fx7
        sage: f.start_worker_pool()
        sage: n_proc = f.pool._processes
        sage: pids_name = f._pid_list.shm.name
        sage: fvars = FvarsHandler(8, f._field, f._idx_to_sextuple, use_mp=n_proc, pids_name=pids_name)
        sage: # In the same shell or in a different shell, attach to fvars
        sage: name = fvars.shm.name
        sage: fvars2 = FvarsHandler(8, f._field, f._idx_to_sextuple, name=name , use_mp=n_proc, pids_name=pids_name)
        sage: from sage.algebras.fusion_rings.poly_tup_engine import poly_to_tup
        sage: rhs = tuple((exp, tuple(c._coefficients())) for exp, c in poly_to_tup(fx5**5))
        sage: fvars[f2, f1, f2, f2, f0, f0] = rhs
        sage: f._tup_to_fpoly(fvars2[f2, f1, f2, f2, f0, f0])
        fx5^5
        sage: fvars.shm.unlink()
        sage: f.shutdown_worker_pool()'''
    shm: shm
    def __init__(self, n_slots, field, idx_to_sextuple, init_data=..., use_mp=..., pids_name=..., name=..., max_terms=..., n_bytes=...) -> Any:
        '''File: /build/sagemath/src/sage/src/sage/algebras/fusion_rings/shm_managers.pyx (starting at line 454)

                Initialize ``self``.

                EXAMPLES::

                    sage: from sage.algebras.fusion_rings.shm_managers import FvarsHandler
                    sage: # Create shared data structure
                    sage: f = FusionRing("A2", 1).get_fmatrix(inject_variables=True, new=True)
                    creating variables fx1..fx8
                    Defining fx0, fx1, fx2, fx3, fx4, fx5, fx6, fx7
                    sage: f.start_worker_pool()
                    sage: n_proc = f.pool._processes
                    sage: pids_name = f._pid_list.shm.name
                    sage: fvars = FvarsHandler(8, f._field, f._idx_to_sextuple, use_mp=n_proc, pids_name=pids_name)
                    sage: TestSuite(fvars).run(skip=\'_test_pickling\')
                    sage: fvars.shm.unlink()
                    sage: f.shutdown_worker_pool()
        '''
    @overload
    def items(self) -> Any:
        '''FvarsHandler.items(self)

        File: /build/sagemath/src/sage/src/sage/algebras/fusion_rings/shm_managers.pyx (starting at line 735)

        Iterate through key-value pairs in the data structure as if it
        were a Python dict.

        As in a Python dict, the key-value pairs are yielded in no particular
        order.

        EXAMPLES::

            sage: f = FusionRing("G2", 1).get_fmatrix(inject_variables=True, new=True)
            creating variables fx1..fx5
            Defining fx0, fx1, fx2, fx3, fx4
            sage: from sage.algebras.fusion_rings.shm_managers import FvarsHandler
            sage: shared_fvars = FvarsHandler(5, f._field, f._idx_to_sextuple, init_data=f._fvars)
            sage: for sextuple, fvar in shared_fvars.items():
            ....:     if sextuple == (f1, f1, f1, f1, f1, f1):
            ....:         f._tup_to_fpoly(fvar)
            ....:
            fx4'''
    @overload
    def items(self) -> Any:
        '''FvarsHandler.items(self)

        File: /build/sagemath/src/sage/src/sage/algebras/fusion_rings/shm_managers.pyx (starting at line 735)

        Iterate through key-value pairs in the data structure as if it
        were a Python dict.

        As in a Python dict, the key-value pairs are yielded in no particular
        order.

        EXAMPLES::

            sage: f = FusionRing("G2", 1).get_fmatrix(inject_variables=True, new=True)
            creating variables fx1..fx5
            Defining fx0, fx1, fx2, fx3, fx4
            sage: from sage.algebras.fusion_rings.shm_managers import FvarsHandler
            sage: shared_fvars = FvarsHandler(5, f._field, f._idx_to_sextuple, init_data=f._fvars)
            sage: for sextuple, fvar in shared_fvars.items():
            ....:     if sextuple == (f1, f1, f1, f1, f1, f1):
            ....:         f._tup_to_fpoly(fvar)
            ....:
            fx4'''
    def __delitem__(self, other) -> None:
        """Delete self[key]."""
    def __getitem__(self, sextuple) -> Any:
        '''FvarsHandler.__getitem__(self, sextuple)

        File: /build/sagemath/src/sage/src/sage/algebras/fusion_rings/shm_managers.pyx (starting at line 518)

        Retrieve a record from the shared memory data structure by
        unflattening its representation and constructing relevant Python
        objects.

        This method returns a tuple of ``(ETuple, coeff)`` pairs,
        where ``coeff`` is an element of ``self.field``.

        EXAMPLES::

            sage: from sage.algebras.fusion_rings.shm_managers import FvarsHandler
            sage: from sage.algebras.fusion_rings.poly_tup_engine import poly_to_tup
            sage: f = FusionRing("B7", 1).get_fmatrix(inject_variables=True, new=True)
            creating variables fx1..fx14
            Defining fx0, fx1, fx2, fx3, fx4, fx5, fx6, fx7, fx8, fx9, fx10, fx11, fx12, fx13
            sage: f.start_worker_pool()
            sage: n_proc = f.pool._processes
            sage: pids_name = f._pid_list.shm.name
            sage: fvars = FvarsHandler(14, f._field, f._idx_to_sextuple, use_mp=n_proc, pids_name=pids_name)
            sage: rhs = tuple((exp, tuple(c._coefficients()))
            ....:             for exp, c in poly_to_tup(1/8*fx0**15 - 23/79*fx2*fx13**3 - 799/2881*fx1*fx2**5*fx10))
            sage: fvars[(f1, f2, f1, f2, f2, f2)] = rhs
            sage: rhs = tuple((exp, tuple(c._coefficients())) for exp, c in poly_to_tup(f._poly_ring.zero()))
            sage: fvars[f2, f2, f2, f2, f0, f0] = rhs
            sage: rhs = tuple((exp, tuple(c._coefficients())) for exp, c in poly_to_tup(-1/19*f._poly_ring.one()))
            sage: fvars[f2, f1, f2, f1, f2, f2] = rhs
            sage: s, t, r = (f1, f2, f1, f2, f2, f2), (f2, f2, f2, f2, f0, f0), (f2, f1, f2, f1, f2, f2)
            sage: f._tup_to_fpoly(fvars[s]) == 1/8*fx0**15 - 23/79*fx2*fx13**3 - 799/2881*fx1*fx2**5*fx10
            True
            sage: f._tup_to_fpoly(fvars[t]) == 0
            True
            sage: f._tup_to_fpoly(fvars[r]) == -1/19
            True
            sage: fvars.shm.unlink()
            sage: f.shutdown_worker_pool()

        .. NOTE::

            This method implements caching. Only the parent process is allowed
            to modify the shared fvars structure. Each process builds its own
            cache, so each process must update its cache before retrieving a
            modified entry, tagged via its ``modified`` property.'''
    def __reduce__(self) -> Any:
        '''FvarsHandler.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/algebras/fusion_rings/shm_managers.pyx (starting at line 711)

        Provide pickling / unpickling support for ``self``.

        TESTS::

            sage: f = FusionRing("F4", 1).get_fmatrix()
            sage: from sage.algebras.fusion_rings.shm_managers import FvarsHandler
            sage: n = f._poly_ring.ngens()
            sage: f.start_worker_pool()
            sage: n_proc = f.pool._processes
            sage: pids_name = f._pid_list.shm.name
            sage: fvars = FvarsHandler(n, f._field, f._idx_to_sextuple, init_data=f._fvars, use_mp=n_proc, pids_name=pids_name)
            sage: for s, fvar in loads(dumps(fvars)).items():
            ....:     assert f._fvars[s] == f._tup_to_fpoly(fvar)
            ....:
            sage: fvars.shm.unlink()
            sage: f.shutdown_worker_pool()'''
    def __setitem__(self, sextuple, fvar) -> Any:
        '''FvarsHandler.__setitem__(self, sextuple, fvar)

        File: /build/sagemath/src/sage/src/sage/algebras/fusion_rings/shm_managers.pyx (starting at line 624)

        Given a sextuple of labels and a tuple of ``(ETuple, cyc_coeff)`` pairs,
        create or overwrite an entry in the shared data structure
        corresponding to the given sextuple.

        EXAMPLES::

            sage: from sage.algebras.fusion_rings.shm_managers import FvarsHandler
            sage: from sage.algebras.fusion_rings.poly_tup_engine import poly_to_tup
            sage: f = FusionRing("A3", 1).get_fmatrix(inject_variables=True, new=True)
            creating variables fx1..fx27
            Defining fx0, ..., fx26
            sage: f.start_worker_pool()
            sage: n_proc = f.pool._processes
            sage: pids_name = f._pid_list.shm.name
            sage: fvars = FvarsHandler(27, f._field, f._idx_to_sextuple, use_mp=n_proc, pids_name=pids_name)
            sage: rhs = tuple((exp, tuple(c._coefficients()))
            ....:             for exp, c in poly_to_tup(1/8*fx0**15 - 23/79*fx2*fx21**3 - 799/2881*fx1*fx2**5*fx10))
            sage: fvars[(f3, f2, f1, f2, f1, f3)] = rhs
            sage: rhs = tuple((exp, tuple(c._coefficients())) for exp, c in poly_to_tup(f._poly_ring.zero()))
            sage: fvars[f3, f2, f3, f0, f1, f1] = rhs
            sage: rhs = tuple((exp, tuple(c._coefficients())) for exp, c in poly_to_tup(-1/19*f._poly_ring.one()))
            sage: fvars[f3, f3, f3, f1, f2, f2] = rhs
            sage: s, t, r = (f3, f2, f1, f2, f1, f3), (f3, f2, f3, f0, f1, f1), (f3, f3, f3, f1, f2, f2)
            sage: f._tup_to_fpoly(fvars[s]) == 1/8*fx0**15 - 23/79*fx2*fx21**3 - 799/2881*fx1*fx2**5*fx10
            True
            sage: f._tup_to_fpoly(fvars[t]) == 0
            True
            sage: f._tup_to_fpoly(fvars[r]) == -1/19
            True
            sage: fvars.shm.unlink()
            sage: f.shutdown_worker_pool()'''

class KSHandler:
    '''KSHandler(n_slots, field, use_mp=False, init_data=None, name=None)

    File: /build/sagemath/src/sage/src/sage/algebras/fusion_rings/shm_managers.pyx (starting at line 31)

    A shared memory backed dict-like structure to manage the
    ``_ks`` attribute of an F-matrix.

    This structure implements a representation of the known squares dictionary
    using a structured NumPy array backed by a contiguous shared memory
    object.

    The structure mimics a dictionary of ``(idx, known_sq)`` pairs. Each
    integer index corresponds to a variable and each ``known_sq`` is an
    element of the F-matrix factory\'s base cyclotomic field.

    Each cyclotomic coefficient is stored as a list of numerators and a
    list of denominators representing the rational coefficients. The
    structured array also maintains ``known`` attribute that indicates
    whether the structure contains an entry corresponding to the given index.

    The parent process should construct this object without a
    ``name`` attribute. Children processes use the ``name`` attribute,
    accessed via ``self.shm.name`` to attach to the shared memory block.

    INPUT:

    - ``n_slots`` -- the total number of F-symbols
    - ``field`` -- F-matrix\'s base cyclotomic field
    - ``use_mp`` -- boolean indicating whether to construct a shared
      memory block to back ``self``
    - ``init_data`` -- dictionary or :class:`KSHandler` object containing
      known squares for initialization, e.g., from a solver checkpoint
    - ``name`` -- the name of a shared memory object (used by child processes
        for attaching)

    .. NOTE::

        To properly dispose of shared memory resources,
        ``self.shm.unlink()`` must be called before exiting.

    .. WARNING::

        This structure *cannot* modify an entry that
        has already been set.

    EXAMPLES::

        sage: from sage.algebras.fusion_rings.shm_managers import KSHandler
        sage: # Create shared data structure
        sage: f = FusionRing("A1", 2).get_fmatrix(inject_variables=True, new=True)
        creating variables fx1..fx14
        Defining fx0, fx1, fx2, fx3, fx4, fx5, fx6, fx7, fx8, fx9, fx10, fx11, fx12, fx13
        sage: n = f._poly_ring.ngens()
        sage: f.start_worker_pool()
        sage: ks = KSHandler(n, f._field, use_mp=True)
        sage: # In the same shell or in a different shell, attach to fvars
        sage: name = ks.shm.name
        sage: ks2 = KSHandler(n, f._field, name=name, use_mp=True)
        sage: from sage.algebras.fusion_rings.poly_tup_engine import poly_to_tup
        sage: eqns = [fx1**2 - 4, fx3**2 + f._field.gen()**4 - 1/19*f._field.gen()**2]
        sage: ks.update([poly_to_tup(p) for p in eqns])
        sage: for idx, sq in ks.items():
        ....:     print("Index: {}, square: {}".format(idx, sq))
        ....:
        Index: 1, square: 4
        Index: 3, square: -zeta32^4 + 1/19*zeta32^2
        sage: ks.shm.unlink()
        sage: f.shutdown_worker_pool()'''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    shm: shm
    def __init__(self, n_slots, field, use_mp=..., init_data=..., name=...) -> Any:
        '''File: /build/sagemath/src/sage/src/sage/algebras/fusion_rings/shm_managers.pyx (starting at line 98)

                Initialize ``self``.

                EXAMPLES::

                    sage: from sage.algebras.fusion_rings.shm_managers import KSHandler
                    sage: # Create shared data structure
                    sage: f = FusionRing("A1", 2).get_fmatrix(inject_variables=True, new=True)
                    creating variables fx1..fx14
                    Defining fx0, fx1, fx2, fx3, fx4, fx5, fx6, fx7, fx8, fx9, fx10, fx11, fx12, fx13
                    sage: n = f._poly_ring.ngens()
                    sage: f.start_worker_pool()
                    sage: ks = KSHandler(n, f._field, use_mp=True)
                    sage: TestSuite(ks).run()
                    sage: ks.shm.unlink()
                    sage: f.shutdown_worker_pool()
        '''
    @overload
    def items(self) -> Any:
        '''KSHandler.items(self)

        File: /build/sagemath/src/sage/src/sage/algebras/fusion_rings/shm_managers.pyx (starting at line 319)

        Iterate through existing entries using Python dict-style syntax.

        EXAMPLES::

            sage: f = FusionRing("A3", 1).get_fmatrix()
            sage: f._reset_solver_state()
            sage: f.get_orthogonality_constraints(output=False)
            sage: f._ks.update(f.ideal_basis)
            sage: for idx, sq in f._ks.items():
            ....:     print("Index: {}, sq: {}".format(idx, sq))
            ....:
            Index: 0, sq: 1
            Index: 1, sq: 1
            Index: 2, sq: 1
            Index: 3, sq: 1
            Index: 4, sq: 1
            ...
            Index: 25, sq: 1
            Index: 26, sq: 1'''
    @overload
    def items(self) -> Any:
        '''KSHandler.items(self)

        File: /build/sagemath/src/sage/src/sage/algebras/fusion_rings/shm_managers.pyx (starting at line 319)

        Iterate through existing entries using Python dict-style syntax.

        EXAMPLES::

            sage: f = FusionRing("A3", 1).get_fmatrix()
            sage: f._reset_solver_state()
            sage: f.get_orthogonality_constraints(output=False)
            sage: f._ks.update(f.ideal_basis)
            sage: for idx, sq in f._ks.items():
            ....:     print("Index: {}, sq: {}".format(idx, sq))
            ....:
            Index: 0, sq: 1
            Index: 1, sq: 1
            Index: 2, sq: 1
            Index: 3, sq: 1
            Index: 4, sq: 1
            ...
            Index: 25, sq: 1
            Index: 26, sq: 1'''
    def update(self, listeqns) -> Any:
        '''KSHandler.update(self, list eqns)

        File: /build/sagemath/src/sage/src/sage/algebras/fusion_rings/shm_managers.pyx (starting at line 178)

        Update ``self``\'s ``shared_memory``-backed dictionary of known
        squares. Keys are variable indices and corresponding values
        are the squares.

        EXAMPLES::

            sage: f = FusionRing("B5", 1).get_fmatrix()
            sage: f._reset_solver_state()
            sage: for idx, sq in f._ks.items():
            ....:     k
            ....:
            sage: f.get_orthogonality_constraints()
            [fx0^2 - 1,
             fx1^2 - 1,
             fx2^2 - 1,
             fx3^2 - 1,
             fx4^2 - 1,
             fx5^2 - 1,
             fx6^2 - 1,
             fx7^2 - 1,
             fx8^2 - 1,
             fx9^2 - 1,
             fx10^2 + fx12^2 - 1,
             fx10*fx11 + fx12*fx13,
             fx10*fx11 + fx12*fx13,
             fx11^2 + fx13^2 - 1]
             sage: f.get_orthogonality_constraints(output=False)
             sage: f._ks.update(f.ideal_basis)
             sage: for idx, sq in f._ks.items():
             ....:     print(idx, "-->", sq)
             ....:
             0 --> 1
             1 --> 1
             2 --> 1
             3 --> 1
             4 --> 1
             5 --> 1
             6 --> 1
             7 --> 1
             8 --> 1
             9 --> 1

        .. WARNING::

            This method assumes every polynomial in ``eqns`` is *monic*.'''
    def __eq__(self, KSHandlerother) -> Any:
        '''KSHandler.__eq__(self, KSHandler other)

        File: /build/sagemath/src/sage/src/sage/algebras/fusion_rings/shm_managers.pyx (starting at line 279)

        Test for equality.

        TESTS::

            sage: f = FusionRing("C2", 2).get_fmatrix()
            sage: f._reset_solver_state()
            sage: f.get_orthogonality_constraints(output=False)
            sage: from sage.algebras.fusion_rings.shm_managers import KSHandler
            sage: n = f._poly_ring.ngens()
            sage: f.start_worker_pool()
            sage: ks = KSHandler(n, f._field, use_mp=True, init_data=f._ks)
            sage: # In the same shell or in a different one, attach to shared memory handler
            sage: name = ks.shm.name
            sage: k2 = KSHandler(n, f._field, name=name, use_mp=True)
            sage: ks == k2
            True
            sage: ks.shm.unlink()
            sage: f.shutdown_worker_pool()'''
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __reduce__(self) -> Any:
        '''KSHandler.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/algebras/fusion_rings/shm_managers.pyx (starting at line 302)

        Provide pickling / unpickling support for ``self``.

        TESTS::

            sage: f = FusionRing("A3", 1).get_fmatrix()
            sage: f._reset_solver_state()
            sage: loads(dumps(f._ks)) == f._ks
            True
            sage: f.find_orthogonal_solution(verbose=False)    # long time
            sage: loads(dumps(f._ks)) == f._ks
            True'''
