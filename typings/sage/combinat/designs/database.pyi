from .orthogonal_arrays import wilson_construction as wilson_construction
from _typeshed import Incomplete
from sage.combinat.designs.orthogonal_arrays import OA_from_PBD as OA_from_PBD, OA_from_quasi_difference_matrix as OA_from_quasi_difference_matrix, OA_n_times_2_pow_c_from_matrix as OA_n_times_2_pow_c_from_matrix, QDM_from_Vmt as QDM_from_Vmt, orthogonal_array as orthogonal_array
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing

cyclic_shift: Incomplete

def MOLS_10_2():
    """
    Return a pair of MOLS of order 10.

    Data obtained from
    `<http://www.cecm.sfu.ca/organics/papers/lam/paper/html/POLS10/POLS10.html>`_

    EXAMPLES::

        sage: from sage.combinat.designs.latin_squares import are_mutually_orthogonal_latin_squares
        sage: from sage.combinat.designs.database import MOLS_10_2
        sage: MOLS = MOLS_10_2()                                                        # needs sage.modules
        sage: print(are_mutually_orthogonal_latin_squares(MOLS))                        # needs sage.modules
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_arrays.is_available(2,10)
        True
    """
def MOLS_12_5():
    """
    Return 5 MOLS of order 12.

    These MOLS have been found by Brendan McKay.

    EXAMPLES::

        sage: from sage.combinat.designs.latin_squares import are_mutually_orthogonal_latin_squares
        sage: from sage.combinat.designs.database import MOLS_12_5
        sage: MOLS = MOLS_12_5()                                                        # needs sage.modules
        sage: print(are_mutually_orthogonal_latin_squares(MOLS))                        # needs sage.modules
        True
    """
def MOLS_14_4():
    """
    Return four MOLS of order 14.

    These MOLS were shared by Ian Wanless. The first proof of existence was
    given in [Todorov12]_.

    EXAMPLES::

        sage: from sage.combinat.designs.latin_squares import are_mutually_orthogonal_latin_squares
        sage: from sage.combinat.designs.database import MOLS_14_4
        sage: MOLS = MOLS_14_4()                                                        # needs sage.modules
        sage: print(are_mutually_orthogonal_latin_squares(MOLS))                        # needs sage.modules
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_arrays.is_available(4,14)                              # needs sage.schemes
        True

    REFERENCE:

    .. [Todorov12] \\D.T. Todorov,
      Four mutually orthogonal Latin squares of order 14,
      Journal of Combinatorial Designs 2012, vol.20 n.8 pp.363-367
    """
def MOLS_15_4():
    """
    Return 4 MOLS of order 15.

    These MOLS were shared by Ian Wanless.

    EXAMPLES::

        sage: from sage.combinat.designs.latin_squares import are_mutually_orthogonal_latin_squares
        sage: from sage.combinat.designs.database import MOLS_15_4
        sage: MOLS = MOLS_15_4()                                                        # needs sage.modules
        sage: print(are_mutually_orthogonal_latin_squares(MOLS))                        # needs sage.modules
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_arrays.is_available(4,15)                              # needs sage.schemes
        True
    """
def MOLS_18_3():
    """
    Return 3 MOLS of order 18.

    These MOLS were shared by Ian Wanless.

    EXAMPLES::

        sage: from sage.combinat.designs.latin_squares import are_mutually_orthogonal_latin_squares
        sage: from sage.combinat.designs.database import MOLS_18_3
        sage: MOLS = MOLS_18_3()                                                        # needs sage.modules
        sage: print(are_mutually_orthogonal_latin_squares(MOLS))                        # needs sage.modules
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_arrays.is_available(3,18)
        True
    """

MOLS_constructions: Incomplete
LIST_OF_MOLS_CONSTRUCTIONS: Incomplete

def OA_7_18():
    """
    Return an OA(7,18).

    Proved in [JulianAbel13]_.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_from_quasi_difference_matrix`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_7_18
        sage: OA = OA_7_18()
        sage: is_orthogonal_array(OA,7,18,2)
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_arrays.is_available(7,18)                              # needs sage.schemes
        True
    """
def OA_9_40():
    """
    Return an OA(9,40).

    As explained in the Handbook III.3.62 [DesignHandbook]_. Uses the fact that
    `40 = 2^3 \\times 5` and that `5` is prime.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_n_times_2_pow_c_from_matrix`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_9_40
        sage: OA = OA_9_40()                                                            # needs sage.rings.finite_rings
        sage: is_orthogonal_array(OA,9,40,2)                                            # needs sage.rings.finite_rings
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_arrays.is_available(9,40)                              # needs sage.schemes
        True
    """
def OA_7_66():
    """
    Return an OA(7,66).

    Construction shared by Julian R. Abel.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_from_PBD`

    EXAMPLES::

        sage: from sage.combinat.designs.orthogonal_arrays import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_7_66
        sage: OA = OA_7_66()                                                            # needs sage.schemes
        sage: is_orthogonal_array(OA,7,66,2)                                            # needs sage.schemes
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_arrays.is_available(7,66)                              # needs sage.schemes
        True
    """
def OA_7_68():
    """
    Return an OA(7,68).

    Construction shared by Julian R. Abel.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_from_PBD`

    EXAMPLES::

        sage: from sage.combinat.designs.orthogonal_arrays import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_7_68
        sage: OA = OA_7_68()                                                            # needs sage.schemes
        sage: is_orthogonal_array(OA,7,68,2)                                            # needs sage.schemes
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_arrays.is_available(7,68)                              # needs sage.schemes
        True
    """
def OA_8_69():
    """
    Return an OA(8,69).

    Construction shared by Julian R. Abel.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_from_PBD`

    EXAMPLES::

        sage: from sage.combinat.designs.orthogonal_arrays import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_8_69
        sage: OA = OA_8_69()                                                            # needs sage.schemes
        sage: is_orthogonal_array(OA,8,69,2)                                            # needs sage.schemes
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_arrays.is_available(8,69)                              # needs sage.schemes
        True
    """
def OA_7_74():
    """
    Return an OA(7,74).

    Construction shared by Julian R. Abel.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_from_PBD`

    EXAMPLES::

        sage: from sage.combinat.designs.orthogonal_arrays import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_7_74
        sage: OA = OA_7_74()                                                            # needs sage.schemes
        sage: is_orthogonal_array(OA,7,74,2)                                            # needs sage.schemes
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_arrays.is_available(7,74)                              # needs sage.schemes
        True
    """
def OA_8_76():
    """
    Return an OA(8,76).

    Construction shared by Julian R. Abel.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_from_PBD`

    EXAMPLES::

        sage: from sage.combinat.designs.orthogonal_arrays import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_8_76
        sage: OA = OA_8_76()                                                            # needs sage.schemes
        sage: is_orthogonal_array(OA,8,76,2)                                            # needs sage.schemes
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_arrays.is_available(8,76)                              # needs sage.schemes
        True
    """
def OA_11_80():
    """
    Return an OA(11,80).

    As explained in the Handbook III.3.76 [DesignHandbook]_. Uses the fact that
    `80 = 2^4 \\times 5` and that `5` is prime.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_n_times_2_pow_c_from_matrix`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_11_80
        sage: OA = OA_11_80()                                                           # needs sage.rings.finite_rings sage.schemes
        sage: is_orthogonal_array(OA,11,80,2)                                           # needs sage.rings.finite_rings sage.schemes
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_arrays.is_available(11,80)                             # needs sage.rings.finite_rings sage.schemes
        True
    """
def OA_15_112():
    """
    Return an OA(15,112).

    Published by Julian R. Abel in [Ab1995]_. Uses the fact that 112 = `2^4
    \\times 7` and that `7` is prime.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_n_times_2_pow_c_from_matrix`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_15_112
        sage: OA = OA_15_112()                                                          # needs sage.rings.finite_rings sage.schemes
        sage: is_orthogonal_array(OA,15,112,2)                                          # needs sage.rings.finite_rings sage.schemes
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_arrays.is_available(15,112)                            # needs sage.rings.finite_rings sage.schemes
        True
    """
def OA_9_120():
    """
    Return an OA(9,120).

    Construction shared by Julian R. Abel:

        From a resolvable `(120,8,1)-BIBD`, one can obtain 7 `MOLS(120)` or a
        resolvable `TD(8,120)` by forming a resolvable `TD(8,8) - 8.TD(8,1)` on
        `I_8 \\times B` for each block `B` in the BIBD.  This gives a `TD(8,120)
        - 120 TD(8,1)` (which is resolvable as the BIBD is resolvable).

    .. SEEALSO::

        :func:`RBIBD_120_8_1`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_9_120
        sage: OA = OA_9_120()                                                           # needs sage.modules sage.schemes
        sage: is_orthogonal_array(OA,9,120,2)                                           # needs sage.modules sage.schemes
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_arrays.is_available(9,120)                             # needs sage.schemes
        True
    """
def OA_9_135():
    """
    Return an OA(9,135).

    Construction shared by Julian R. Abel:

        This design can be built by Wilson's method (`135 = 8.16 + 7`) applied
        to an Orthogonal Array `OA(9+7,16)` with 7 groups truncated to size 1 in
        such a way that a block contain 0, 1 or 3 points of the truncated
        groups.

        This is possible, because `PG(2,2)` (the projective plane over `GF(2)`)
        is a subdesign in `PG(2,16)` (the projective plane over `GF(16)`); in a
        cyclic `PG(2,16)` or `BIBD(273,17,1)` the points `\\equiv 0
        \\pmod{39}` form such a subdesign (note that `273=16^2 + 16 +1` and
        `273 = 39 \\times 7` and `7 = 2^2 + 2 + 1`).

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_9_135
        sage: OA = OA_9_135()                                                           # needs sage.rings.finite_rings sage.schemes
        sage: is_orthogonal_array(OA,9,135,2)                                           # needs sage.rings.finite_rings sage.schemes
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_arrays.is_available(9,135)                             # needs sage.schemes
        True

    As this orthogonal array requires a `(273,17,1)` cyclic difference set, we check that
    it is available::

        sage: G,D = designs.difference_family(273,17,1); G                              # needs sage.libs.pari
        Ring of integers modulo 273
    """
def OA_11_160():
    """
    Return an OA(11,160).

    Published by Julian R. Abel in [Ab1995]_. Uses the fact that `160 = 2^5
    \\times 5` is a product of a power of `2` and a prime number.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_n_times_2_pow_c_from_matrix`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_11_160
        sage: OA = OA_11_160()                                                          # needs sage.rings.finite_rings
        sage: is_orthogonal_array(OA,11,160,2)                                          # needs sage.rings.finite_rings
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_arrays.is_available(11,160)                            # needs sage.schemes
        True
    """
def OA_16_176():
    """
    Return an OA(16,176).

    Published by Julian R. Abel in [Ab1995]_. Uses the fact that `176 = 2^4
    \\times 11` is a product of a power of `2` and a prime number.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_n_times_2_pow_c_from_matrix`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_16_176
        sage: OA = OA_16_176()                                                          # needs sage.rings.finite_rings
        sage: is_orthogonal_array(OA,16,176,2)                                          # needs sage.rings.finite_rings
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_arrays.is_available(16,176)                            # needs sage.schemes
        True
    """
def OA_11_185():
    """
    Return an OA(11,185).

    The construction is given in [Greig99]_. In Julian R. Abel's words:

        Start with a `PG(2,16)` with a `7` points Fano subplane; outside this
        plane there are `7(17-3) = 98` points on a line of the subplane and
        `273-98-7 = 168` other points.  Greig notes that the subdesign
        consisting of these `168` points is a `(168, \\{10,12\\})-PBD`. Now add
        the `17` points of a line disjoint from this subdesign (e.g. a line of
        the Fano subplane).  This line will intersect every line of the `168`
        point subdesign in `1` point. Thus the new line sizes are `11` and
        `13`, plus a unique line of size `17`, giving a `(185,\\{11,13,17\\}`-PBD
        and an `OA(11,185)`.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_11_185
        sage: OA = OA_11_185()                                                          # needs sage.rings.finite_rings
        sage: is_orthogonal_array(OA,11,185,2)                                          # needs sage.rings.finite_rings
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_arrays.is_available(11,185)                            # needs sage.schemes
        True
    """
def OA_10_205():
    """
    Return an `OA(10,205)`.

    Julian R. Abel shared the following construction, which originally appeared
    in Theorem 8.7 of [Greig99]_, and can in Lemmas 5.14-5.16 of [ColDin01]_:

        Consider a `PG(2,4^2)` containing a Baer subplane (i.e. a `PG(2,4)`) `B`
        and a point `p\\in B`. Among the `4^2+1=17` lines of `PG(2,4^2)`
        containing `p`:

        * `4+1=5` lines intersect `B` on `5` points

        * `4^2-4=12` lines intersect `B` on `1` point

        As those lines are disjoint outside of `B` we can use them as groups to
        build a GDD on `16^2+16+1-(4^4+4+1)=252` points. By keeping only 9 lines
        of the second kind, however, we obtain a `(204,\\{9,13,17\\})`-GDD of type
        12^5.16^9.

        We complete it into a PBD by adding a block `g\\cup \\{204\\}` for each
        group `g`. We then build an OA from this PBD using the fact that all
        blocks of size 9 are disjoint.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_from_PBD`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_10_205
        sage: OA = OA_10_205()                                                          # needs sage.schemes
        sage: is_orthogonal_array(OA,10,205,2)                                          # needs sage.schemes
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_arrays.is_available(10,205)                            # needs sage.schemes
        True
    """
def OA_16_208():
    """
    Return an OA(16,208).

    Published by Julian R. Abel in [Ab1995]_. Uses the fact that `208 = 2^4
    \\times 13` is a product of `2` and a prime number.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_n_times_2_pow_c_from_matrix`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_16_208
        sage: OA = OA_16_208()                  # not tested (too long)                 # needs sage.rings.finite_rings
        sage: is_orthogonal_array(OA,16,208,2)  # not tested (too long)                 # needs sage.rings.finite_rings
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_arrays.is_available(16,208)                            # needs sage.schemes
        True
    """
def OA_15_224():
    """
    Return an OA(15,224).

    Published by Julian R. Abel in [Ab1995]_ (uses the fact that `224=2^5
    \\times 7` is a product of a power of `2` and a prime number).

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_n_times_2_pow_c_from_matrix`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_15_224
        sage: OA = OA_15_224()                  # not tested (too long)                 # needs sage.rings.finite_rings
        sage: is_orthogonal_array(OA,15,224,2)  # not tested (too long)                 # needs sage.rings.finite_rings
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_arrays.is_available(15,224)                            # needs sage.schemes
        True
    """
def OA_11_254():
    """
    Return an OA(11,254).

    This constructions appears in [Greig99]_.

    From a cyclic `PG(2,19)` whose base blocks contains 7,9, and 4 points in the
    congruence classes mod 3, build a `(254,{11,13,16})-PBD` by ignoring the
    points of a congruence class. There exist `OA(12,11),OA(12,13),OA(12,16)`,
    which gives the `OA(11,254)`.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_from_PBD`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_11_254
        sage: OA = OA_11_254()                                                          # needs sage.schemes
        sage: is_orthogonal_array(OA,11,254,2)                                          # needs sage.schemes
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_arrays.is_available(11,254)                            # needs sage.schemes
        True
    """
def OA_20_352():
    """
    Return an OA(20,352).

    Published by Julian R. Abel in [Ab1995]_ (uses the fact that `352=2^5
    \\times 11` is the product of a power of `2` and a prime number).

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_n_times_2_pow_c_from_matrix`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_20_352
        sage: OA = OA_20_352()                  # not tested (~25s)                     # needs sage.rings.finite_rings
        sage: is_orthogonal_array(OA,20,352,2)  # not tested (~25s)                     # needs sage.rings.finite_rings
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_arrays.is_available(20,352)                            # needs sage.schemes
        True
    """
def OA_20_416():
    """
    Return an OA(20,416).

    Published by Julian R. Abel in [Ab1995]_ (uses the fact that `416=2^5
    \\times 13` is the product of a power of `2` and a prime number).

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_n_times_2_pow_c_from_matrix`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_20_416
        sage: OA = OA_20_416()                  # not tested (~35s)                     # needs sage.rings.finite_rings
        sage: is_orthogonal_array(OA,20,416,2)  # not tested                            # needs sage.rings.finite_rings
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_arrays.is_available(20,416)                            # needs sage.schemes
        True
    """
def OA_20_544():
    """
    Return an OA(20,544).

    Published by Julian R. Abel in [Ab1995]_ (uses the fact that
    `544=2^5 \\times 17` is the product of a power of `2` and a prime number).

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_n_times_2_pow_c_from_matrix`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_20_544
        sage: OA = OA_20_544()                  # not tested (too long ~1mn)            # needs sage.rings.finite_rings
        sage: is_orthogonal_array(OA,20,544,2)  # not tested                            # needs sage.rings.finite_rings
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_arrays.is_available(20,544)                            # needs sage.schemes
        True
    """
def OA_17_560():
    """
    Return an OA(17,560).

    This OA is built in Corollary 2.2 of [Thwarts]_.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_17_560
        sage: OA = OA_17_560()                                                          # needs sage.rings.finite_rings sage.schemes
        sage: is_orthogonal_array(OA,17,560,2)                                          # needs sage.rings.finite_rings sage.schemes
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_arrays.is_available(17,560)                            # needs sage.schemes
        True
    """
def OA_11_640():
    """
    Return an OA(11,640).

    Published by Julian R. Abel in [Ab1995]_ (uses the fact that `640=2^7
    \\times 5` is the product of a power of `2` and a prime number).

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_n_times_2_pow_c_from_matrix`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_11_640
        sage: OA = OA_11_640()                  # not tested (too long)                 # needs sage.rings.finite_rings
        sage: is_orthogonal_array(OA,11,640,2)  # not tested (too long)                 # needs sage.rings.finite_rings
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_arrays.is_available(11,640)                            # needs sage.schemes
        True
    """
def OA_10_796():
    """
    Return an OA(10,796).

    Construction shared by Julian R. Abel, from [AC07]_:

        Truncate one block of a `TD(17,47)` to size `13`, then add an extra
        point. Form a block on each group plus the extra point: we obtain a
        `(796, \\{13,16,17,47,48\\})`-PBD in which only the extra point lies in
        more than one block of size `48` (and each other point lies in exactly 1
        such block).

        For each block `B` (of size `k` say) not containing the extra point,
        construct a `TD(10, k) - k.TD(k,1)` on `I(10) X B`.  For each block `B`
        (of size `k=47` or `48`) containing the extra point, construct a
        `TD(10,k) - TD(k,1)` on `I(10) X B`, the size `1` hole being on `I(10) X
        P` where `P` is the extra point. Finally form `1` extra block of size
        `10` on `I(10) X P`.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_10_796
        sage: OA = OA_10_796()                                                          # needs sage.schemes
        sage: is_orthogonal_array(OA,10,796,2)                                          # needs sage.schemes
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_arrays.is_available(10,796)                            # needs sage.schemes
        True
    """
def OA_10_469():
    """
    Return an OA(10,469).

    This construction appears in [Brouwer80]_. It is based on the same technique
    used in
    :func:`~sage.combinat.designs.orthogonal_arrays_build_recursive.brouwer_separable_design`.

    Julian R. Abel's instructions:

        Brouwer notes that a cyclic `PG(2,37)` (or `(1407,38,1)`-BIBD) can be
        obtained with a base block containing `13,9,` and `16` points in each
        residue class mod 3. Thus, by reducing the `PG(2,37)` to its points
        congruent to `0 \\pmod 3` one obtains a `(469,\\{9,13,16\\})`-PBD which
        consists in 3 symmetric designs, i.e. 469 blocks of size 9, 469 blocks
        of size 13, and 469 blocks of size 16.

        For each block size `s`, one can build a matrix with size `s\\times 469`
        in which each block is a row, and such that each point of the PBD
        appears once per column. By multiplying a row of an `OA(9,s)-s.OA(9,1)`
        with the rows of the matrix one obtains a parallel class of a resolvable
        `OA(9,469)`.

        Add to this the parallel class of all blocks `(0,0,...),(1,1,...),...`
        to obtain a resolvable `OA(9,469)` equivalent to an `OA(10,469)`.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_10_469
        sage: OA = OA_10_469()                  # long time                             # needs sage.schemes
        sage: is_orthogonal_array(OA,10,469,2)  # long time                             # needs sage.schemes
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_arrays.is_available(10,469)                            # needs sage.schemes
        True
    """
def OA_520_plus_x(x):
    """
    Return an `OA(10+x,520+x)`.

    The construction shared by Julian R. Abel works for :func:`OA(10,520)
    <OA_10_520>`, :func:`OA(12,522) <OA_12_522>`, and :func:`OA(14,524)
    <OA_14_524>`.

        Let `n=520+x` and `k=10+x`. Build a `TD(17,31)`. Remove `8-x` points
        contained in a common block, add a new point `p` and create a block
        `g_i\\cup \\{p\\}` for every (possibly truncated) group `g_i`. The result
        is a `(520+x,{9+x,16,17,31,32})-PBD`. Note that all blocks of size `\\geq
        30` only intersect on `p`, and that the unique block `B_9` of size `9`
        intersects all blocks of size `32` on one point. Now:

        * Build an `OA(k,16)-16.OA(k,16)` for each block of size 16

        * Build an `OA(k,17)-17.OA(k,17)` for each block of size 17

        * Build an `OA(k,31)-OA(k,1)` for each block of size 31 (with the hole on
          `p`).

        * Build an `OA(k,32)-2.OA(k,1)` for each block `B` of size 32 (with the
          holes on `p` and `B\\cap B_9`).

        * Build an `OA(k,9)` on `B_9`.

        Only a row `[p,p,...]` is missing from the `OA(10+x,520+x)`

    This construction is used in :func:`OA(10,520) <OA_10_520>`,
    :func:`OA(12,522) <OA_12_522>`, and :func:`OA(14,524) <OA_14_524>`.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_520_plus_x
        sage: OA = OA_520_plus_x(0)                   # not tested (already tested in OA_10_520)
        sage: is_orthogonal_array(OA,10,520,2)  # not tested (already tested in OA_10_520)
        True
    """
def OA_10_520():
    """
    Return an OA(10,520).

    This design is built by the slightly more general construction
    :func:`OA_520_plus_x`.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_10_520
        sage: OA = OA_10_520()                                                          # needs sage.schemes
        sage: is_orthogonal_array(OA,10,520,2)                                          # needs sage.schemes
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_arrays.is_available(10,520)                            # needs sage.schemes
        True
    """
def OA_12_522():
    """
    Return an OA(12,522).

    This design is built by the slightly more general construction
    :func:`OA_520_plus_x`.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_12_522
        sage: OA = OA_12_522()                                                          # needs sage.schemes
        sage: is_orthogonal_array(OA,12,522,2)                                          # needs sage.schemes
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_arrays.is_available(12,522)                            # needs sage.schemes
        True
    """
def OA_14_524():
    """
    Return an OA(14,524).

    This design is built by the slightly more general construction
    :func:`OA_520_plus_x`.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_14_524
        sage: OA = OA_14_524()                                                          # needs sage.schemes
        sage: is_orthogonal_array(OA,14,524,2)                                          # needs sage.schemes
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_arrays.is_available(14,524)                            # needs sage.schemes
        True
    """
def OA_15_896():
    """
    Return an OA(15,896).

    Uses the fact that `896 = 2^7 \\times 7` is the product of a power of `2` and
    a prime number.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_n_times_2_pow_c_from_matrix`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_15_896
        sage: OA = OA_15_896()                  # not tested (too long, ~2min)          # needs sage.rings.finite_rings
        sage: is_orthogonal_array(OA,15,896,2)  # not tested (too long)                 # needs sage.rings.finite_rings
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_arrays.is_available(15,896)                            # needs sage.schemes
        True
    """
def OA_9_1078():
    """
    Return an OA(9,1078).

    This is obtained through the generalized Brouwer-van Rees
    construction. Indeed, `1078 = 89.11 + (99=9.11)` and there exists an
    `OA(9,100) - OA(9,11)`.

    .. NOTE::

        This function should be removed once
        :func:`~sage.combinat.designs.orthogonal_arrays_find_recursive.find_brouwer_van_rees_with_one_truncated_column`
        can handle all incomplete orthogonal arrays obtained through
        :func:`~sage.combinat.designs.orthogonal_arrays.incomplete_orthogonal_array`.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_9_1078
        sage: OA = OA_9_1078()                       # not tested -- ~3s
        sage: is_orthogonal_array(OA,9,1078,2) # not tested -- ~3s
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_arrays.is_available(9,1078)                            # needs sage.schemes
        True
    """
def OA_25_1262():
    """
    Return an OA(25,1262).

    The construction is given in [Greig99]_. In Julian R. Abel's words:

        Start with a cyclic `PG(2,43)` or `(1893,44,1)`-BIBD whose base block
        contains respectively `12,13` and `19` point in the residue classes mod
        3. In the resulting BIBD, remove one of the three classes: the result is
        a `(1262, \\{25, 31,32\\})`-PBD, from which the `OA(25,1262)` is obtained.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_25_1262
        sage: OA = OA_25_1262()                       # not tested -- too long
        sage: is_orthogonal_array(OA,25,1262,2) # not tested -- too long
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_arrays.is_available(25,1262)                           # needs sage.schemes
        True
    """
def OA_9_1612():
    """
    Return an OA(9,1612).

    This is obtained through the generalized Brouwer-van Rees
    construction. Indeed, `1612 = 89.17 + (99=9.11)` and there exists an
    `OA(9,100) - OA(9,11)`.

    .. NOTE::

        This function should be removed once
        :func:`~sage.combinat.designs.orthogonal_arrays_find_recursive.find_brouwer_van_rees_with_one_truncated_column`
        can handle all incomplete orthogonal arrays obtained through
        :func:`~sage.combinat.designs.orthogonal_arrays.incomplete_orthogonal_array`.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_9_1612
        sage: OA = OA_9_1612()                       # not tested -- ~6s
        sage: is_orthogonal_array(OA,9,1612,2) # not tested -- ~6s
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_arrays.is_available(9,1612)                            # needs sage.schemes
        True
    """
def OA_10_1620():
    """
    Return an OA(10,1620).

    This is obtained through the generalized Brouwer-van Rees
    construction. Indeed, `1620 = 144.11+(36=4.9)` and there exists an
    `OA(10,153) - OA(10,9)`.

    .. NOTE::

        This function should be removed once
        :func:`~sage.combinat.designs.orthogonal_arrays_find_recursive.find_brouwer_van_rees_with_one_truncated_column`
        can handle all incomplete orthogonal arrays obtained through
        :func:`~sage.combinat.designs.orthogonal_arrays.incomplete_orthogonal_array`.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_10_1620
        sage: OA = OA_10_1620()                       # not tested -- ~7s
        sage: is_orthogonal_array(OA,10,1620,2) # not tested -- ~7s
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_arrays.is_available(10,1620)                           # needs sage.schemes
        True
    """

OA_constructions: Incomplete
LIST_OF_OA_CONSTRUCTIONS: Incomplete

def QDM_19_6_1_1_1():
    """
    Return a `(19,6;1,1;1)`-quasi-difference matrix.

    Used to build an `OA(6,20)`

    Given in the Handbook III.3.49 [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.database import QDM_19_6_1_1_1
        sage: from sage.combinat.designs.designs_pyx import is_quasi_difference_matrix
        sage: G,M = QDM_19_6_1_1_1()
        sage: is_quasi_difference_matrix(M,G,6,1,1,1)
        True
    """
def QDM_21_5_1_1_1():
    """
    Return a `(21,5;1,1;1)`-quasi-difference matrix.

    Used to build an `OA(5,22)`

    Given in the Handbook III.3.51 [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.database import QDM_21_5_1_1_1
        sage: from sage.combinat.designs.designs_pyx import is_quasi_difference_matrix
        sage: G,M = QDM_21_5_1_1_1()
        sage: is_quasi_difference_matrix(M,G,5,1,1,1)
        True
    """
def QDM_21_6_1_1_5():
    """
    Return a `(21,6;1,1;5)`-quasi-difference matrix.

    Used to build an `OA(6,26)`

    Given in the Handbook III.3.53 [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.database import QDM_21_6_1_1_5
        sage: from sage.combinat.designs.designs_pyx import is_quasi_difference_matrix
        sage: G,M = QDM_21_6_1_1_5()
        sage: is_quasi_difference_matrix(M,G,6,1,1,5)
        True
    """
def QDM_25_6_1_1_5():
    """
    Return a `(25,6;1,1;5)`-quasi-difference matrix.

    Used to build an `OA(6,30)`

    Given in the Handbook III.3.55 [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.database import QDM_25_6_1_1_5
        sage: from sage.combinat.designs.designs_pyx import is_quasi_difference_matrix
        sage: G,M = QDM_25_6_1_1_5()                                                    # needs sage.modules
        sage: is_quasi_difference_matrix(M,G,6,1,1,5)                                   # needs sage.modules
        True
    """
def QDM_33_6_1_1_1():
    """
    Return a `(33,6;1,1;1)`-quasi-difference matrix.

    Used to build an `OA(6,34)`

    Given in the Handbook III.3.57 [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.database import QDM_33_6_1_1_1
        sage: from sage.combinat.designs.designs_pyx import is_quasi_difference_matrix
        sage: G,M = QDM_33_6_1_1_1()
        sage: is_quasi_difference_matrix(M,G,6,1,1,1)
        True
    """
def QDM_37_6_1_1_1():
    """
    Return a `(37,6;1,1;1)`-quasi-difference matrix.

    Used to build an `OA(6,38)`

    Given in the Handbook III.3.60 [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.database import QDM_37_6_1_1_1
        sage: from sage.combinat.designs.designs_pyx import is_quasi_difference_matrix
        sage: G,M = QDM_37_6_1_1_1()
        sage: is_quasi_difference_matrix(M,G,6,1,1,1)
        True
    """
def QDM_35_7_1_1_7():
    """
    Return a `(35,7;1,1;7)`-quasi-difference matrix.

    Used to build an `OA(7,42)`

    As explained in the Handbook III.3.63 [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.database import QDM_35_7_1_1_7
        sage: from sage.combinat.designs.designs_pyx import is_quasi_difference_matrix
        sage: G,M = QDM_35_7_1_1_7()
        sage: is_quasi_difference_matrix(M,G,7,1,1,7)
        True
    """
def QDM_45_7_1_1_9():
    """
    Return a `(45,7;1,1;9)`-quasi-difference matrix.

    Used to build an `OA(7,54)`

    As explained in the Handbook III.3.71 [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.database import QDM_45_7_1_1_9
        sage: from sage.combinat.designs.designs_pyx import is_quasi_difference_matrix
        sage: G,M = QDM_45_7_1_1_9()
        sage: is_quasi_difference_matrix(M,G,7,1,1,9)
        True
    """
def QDM_54_7_1_1_8():
    """
    Return a `(54,7;1,1;8)`-quasi-difference matrix.

    Used to build an `OA(7,62)`

    As explained in the Handbook III.3.74 [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.database import QDM_54_7_1_1_8
        sage: from sage.combinat.designs.designs_pyx import is_quasi_difference_matrix
        sage: G,M = QDM_54_7_1_1_8()
        sage: is_quasi_difference_matrix(M,G,7,1,1,8)
        True
    """
def QDM_57_9_1_1_8():
    """
    Return a `(57,9;1,1;8)`-quasi-difference matrix.

    Used to build an `OA(9,65)`

    Construction shared by Julian R. Abel

    EXAMPLES::

        sage: from sage.combinat.designs.database import QDM_57_9_1_1_8
        sage: from sage.combinat.designs.designs_pyx import is_quasi_difference_matrix
        sage: G,M = QDM_57_9_1_1_8()                                                    # needs sage.schemes
        sage: is_quasi_difference_matrix(M,G,9,1,1,8)                                   # needs sage.schemes
        True
    """

QDM: dict[tuple[int, int], dict]
LIST_OF_QDM: Incomplete
Vmt_vectors: Incomplete
n: Incomplete
k: Incomplete
lmbda: Incomplete
mu: Incomplete
u: Incomplete
LIST_OF_VMT_VECTORS: Incomplete
DF: Incomplete
LIST_OF_DF: Incomplete

def DM_12_6_1():
    """
    Return a `(12,6,1)`-difference matrix as built in [Hanani75]_.

    This design is Lemma 3.21 from [Hanani75]_.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_12_6_1
        sage: G,M = DM_12_6_1()
        sage: is_difference_matrix(M,G,6,1)
        True

    Can be obtained from the constructor::

        sage: _ = designs.difference_matrix(12,6)

    REFERENCES:

    .. [Hanani75] Haim Hanani,
      Balanced incomplete block designs and related designs,
      :doi:`10.1016/0012-365X(75)90040-0`,
      Discrete Mathematics, Volume 11, Issue 3, 1975, Pages 255-369.
    """
def DM_21_6_1():
    """
    Return a `(21,6,1)`-difference matrix.

    As explained in the Handbook III.3.50 [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_21_6_1
        sage: G,M = DM_21_6_1()
        sage: is_difference_matrix(M,G,6,1)
        True

    Can be obtained from the constructor::

        sage: _ = designs.difference_matrix(21,6)                                       # needs sage.rings.finite_rings
    """
def DM_24_8_1():
    """
    Return a `(24,8,1)`-difference matrix.

    As explained in the Handbook III.3.52 [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_24_8_1
        sage: G,M = DM_24_8_1()
        sage: is_difference_matrix(M,G,8,1)
        True

    Can be obtained from the constructor::

        sage: _ = designs.difference_matrix(24,8)
    """
def DM_28_6_1():
    """
    Return a `(28,6,1)`-difference matrix.

    As explained in the Handbook III.3.54 [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_28_6_1
        sage: G,M = DM_28_6_1()                                                         # needs sage.modules
        sage: is_difference_matrix(M,G,6,1)                                             # needs sage.modules
        True

    Can be obtained from the constructor::

        sage: _ = designs.difference_matrix(28,6)                                       # needs sage.modules
    """
def DM_33_6_1():
    """
    Return a `(33,6,1)`-difference matrix.

    As explained in the Handbook III.3.56 [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_33_6_1
        sage: G,M = DM_33_6_1()
        sage: is_difference_matrix(M,G,6,1)
        True

    Can be obtained from the constructor::

        sage: _ = designs.difference_matrix(33,6)                                       # needs sage.rings.finite_rings
    """
def DM_35_6_1():
    """
    Return a `(35,6,1)`-difference matrix.

    As explained in the Handbook III.3.58 [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_35_6_1
        sage: G,M = DM_35_6_1()
        sage: is_difference_matrix(M,G,6,1)
        True

    Can be obtained from the constructor::

        sage: _ = designs.difference_matrix(35,6)                                       # needs sage.rings.finite_rings
    """
def DM_36_9_1():
    """
    Return a `(36,9,1)`-difference matrix.

    As explained in the Handbook III.3.59 [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_36_9_1
        sage: G,M = DM_36_9_1()                                                         # needs sage.modules
        sage: is_difference_matrix(M,G,9,1)                                             # needs sage.modules
        True

    Can be obtained from the constructor::

        sage: _ = designs.difference_matrix(36,9)                                       # needs sage.modules
    """
def DM_39_6_1():
    """
    Return a `(39,6,1)`-difference matrix.

    As explained in the Handbook III.3.61 [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_39_6_1
        sage: G,M = DM_39_6_1()
        sage: is_difference_matrix(M,G,6,1)
        True

    The design is available from the general constructor::

        sage: designs.difference_matrix(39,6,existence=True)                            # needs sage.rings.finite_rings
        True
    """
def DM_44_6_1():
    """
    Return a `(44,6,1)`-difference matrix.

    As explained in the Handbook III.3.64 [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_44_6_1
        sage: G,M = DM_44_6_1()
        sage: is_difference_matrix(M,G,6,1)
        True

    Can be obtained from the constructor::

        sage: _ = designs.difference_matrix(44,6)
    """
def DM_45_7_1():
    """
    Return a `(45,7,1)`-difference matrix.

    As explained in the Handbook III.3.65 [DesignHandbook]_.

    ... whose description contained a very deadly typo, kindly fixed by Julian
    R. Abel.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_45_7_1
        sage: G,M = DM_45_7_1()
        sage: is_difference_matrix(M,G,7,1)
        True

    Can be obtained from the constructor::

        sage: _ = designs.difference_matrix(45,7)                                       # needs sage.rings.finite_rings
    """
def DM_48_9_1():
    """
    Return a `(48,9,1)`-difference matrix.

    As explained in the Handbook III.3.67 [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_48_9_1
        sage: G,M = DM_48_9_1()                                                         # needs sage.rings.finite_rings
        sage: is_difference_matrix(M,G,9,1)                                             # needs sage.rings.finite_rings
        True

    Can be obtained from the constructor::

        sage: _ = designs.difference_matrix(48,9)                                       # needs sage.rings.finite_rings
    """
def DM_51_6_1():
    """
    Return a `(51,6,1)`-difference matrix.

    As explained in the Handbook III.3.69 [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_51_6_1
        sage: G,M = DM_51_6_1()
        sage: is_difference_matrix(M,G,6,1)
        True

    Can be obtained from the constructor::

        sage: _ = designs.difference_matrix(51,6)                                       # needs sage.rings.finite_rings
    """
def DM_52_6_1():
    """
    Return a `(52,6,1)`-difference matrix.

    As explained in the Handbook III.3.70 [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_52_6_1
        sage: G,M = DM_52_6_1()                                                         # needs sage.rings.finite_rings
        sage: is_difference_matrix(M,G,6,1)                                             # needs sage.rings.finite_rings
        True

    Can be obtained from the constructor::

        sage: _ = designs.difference_matrix(52,6)                                       # needs sage.rings.finite_rings
    """
def DM_55_7_1():
    """
    Return a `(55,7,1)`-difference matrix.

    As explained in the Handbook III.3.72 [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_55_7_1
        sage: G,M = DM_55_7_1()
        sage: is_difference_matrix(M,G,7,1)
        True

    Can be obtained from the constructor::

        sage: _ = designs.difference_matrix(55,7)                                       # needs sage.rings.finite_rings
    """
def DM_56_8_1():
    """
    Return a `(56,8,1)`-difference matrix.

    As explained in the Handbook III.3.73 [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_56_8_1
        sage: G,M = DM_56_8_1()                                                         # needs sage.rings.finite_rings
        sage: is_difference_matrix(M,G,8,1)                                             # needs sage.rings.finite_rings
        True

    Can be obtained from the constructor::

        sage: _ = designs.difference_matrix(56,8)                                       # needs sage.rings.finite_rings
    """
def DM_57_8_1():
    """
    Return a `(57,8,1)`-difference matrix.

    Given by Julian R. Abel.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_57_8_1
        sage: G,M = DM_57_8_1()                                                         # needs sage.rings.finite_rings sage.schemes
        sage: is_difference_matrix(M,G,8,1)                                             # needs sage.rings.finite_rings sage.schemes
        True

    Can be obtained from the constructor::

        sage: _ = designs.difference_matrix(57,8)                                       # needs sage.rings.finite_rings sage.schemes
    """
def DM_60_6_1():
    """
    Return a `(60,6,1)`-difference matrix.

    As explained in [JulianAbel13]_.

    REFERENCES:

    .. [JulianAbel13] Existence of Five MOLS of Orders 18 and 60
      R. Julian R. Abel
      Journal of Combinatorial Designs
      2013

    http://onlinelibrary.wiley.com/doi/10.1002/jcd.21384/abstract

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_60_6_1
        sage: G,M = DM_60_6_1()
        sage: is_difference_matrix(M,G,6,1)
        True

    Can be obtained from the constructor::

        sage: _ = designs.difference_matrix(60,6)
    """
def DM_75_8_1():
    """
    Return a `(75,8,1)`-difference matrix.

    As explained in the Handbook III.3.75 [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_75_8_1
        sage: G,M = DM_75_8_1()
        sage: is_difference_matrix(M,G,8,1)
        True

    Can be obtained from the constructor::

        sage: _ = designs.difference_matrix(75,8)                                       # needs sage.rings.finite_rings
    """
def DM_273_17_1():
    """
    Return a `(273,17,1)`-difference matrix.

    Given by Julian R. Abel.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_273_17_1
        sage: G,M = DM_273_17_1()                                                       # needs sage.schemes
        sage: is_difference_matrix(M,G,17,1)                                            # needs sage.schemes
        True

    Can be obtained from the constructor::

        sage: _ = designs.difference_matrix(273,17)                                     # needs sage.schemes
    """
def DM_993_32_1():
    """
    Return a `(993,32,1)`-difference matrix.

    Given by Julian R. Abel.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_993_32_1
        sage: G,M = DM_993_32_1()                                                       # needs sage.schemes
        sage: is_difference_matrix(M,G,32,1)                                            # needs sage.schemes
        True

    Can be obtained from the constructor::

        sage: _ = designs.difference_matrix(993,32)                                     # needs sage.schemes
    """

DM: Incomplete
LIST_OF_DM: Incomplete

def RBIBD_120_8_1():
    """
    Return a resolvable `BIBD(120,8,1)`.

    This function output a list ``L`` of `17\\times 15` blocks such that
    ``L[i*15:(i+1)*15]`` is a partition of `120`.

    Construction shared by Julian R. Abel:

        Seiden's method: Start with a cyclic `(273,17,1)-BIBD` and let `B` be an
        hyperoval, i.e. a set of 18 points which intersects any block of the
        BIBD in either 0 points (153 blocks) or 2 points (120 blocks). Dualise
        this design and take these last 120 blocks as points in the design;
        blocks in the design will correspond to the `273-18=255` non-hyperoval
        points.

        The design is also resolvable.  In the original `PG(2,16)` take any
        point `T` in the hyperoval and consider a block `B1` containing `T`.
        The `15` points in `B1` that do not belong to the hyperoval correspond
        to `15` blocks forming a parallel class in the dualised design. The
        other `16` parallel classes come in a similar way, by using point `T`
        and the other `16` blocks containing `T`.

    .. SEEALSO::

        :func:`OA_9_120`

    EXAMPLES::

        sage: from sage.combinat.designs.database import RBIBD_120_8_1
        sage: from sage.combinat.designs.bibd import is_pairwise_balanced_design
        sage: RBIBD = RBIBD_120_8_1()                                                   # needs sage.modules
        sage: is_pairwise_balanced_design(RBIBD,120,[8])                                # needs sage.modules
        True

    It is indeed resolvable, and the parallel classes are given by 17 slices of
    consecutive 15 blocks::

        sage: for i in range(17):                                                       # needs sage.modules
        ....:     assert len(set(sum(RBIBD[i*15:(i+1)*15],[]))) == 120

    The BIBD is available from the constructor::

        sage: _ = designs.balanced_incomplete_block_design(120,8)                       # needs sage.modules
    """
def BIBD_45_9_8(from_code: bool = False):
    """
    Return a `(45,9,1)`-BIBD.

    This BIBD is obtained from the codewords of minimal weight in the
    :func:`~sage.coding.code_constructions.ExtendedQuadraticResidueCode` of
    length 48. This construction appears in VII.11.2 from [DesignHandbook]_,
    which cites [HT95]_.

    INPUT:

    - ``from_code`` -- boolean; whether to build the design from hardcoded data
      (default) or from the code object (much longer)

    EXAMPLES::

        sage: from sage.combinat.designs.database import BIBD_45_9_8
        sage: from sage.combinat.designs.bibd import BalancedIncompleteBlockDesign
        sage: B = BalancedIncompleteBlockDesign(45, BIBD_45_9_8(), lambd=8); B
        (45,9,8)-Balanced Incomplete Block Design

    TESTS:

    From the definition (takes around 12s)::

        sage: B2 = Hypergraph(BIBD_45_9_8(from_code=True))      # not tested            # needs sage.rings.finite_rings
        sage: B2.is_isomorphic(B)               # not tested                            # needs sage.rings.finite_rings
        True

    REFERENCE:

    .. [HT95] \\W. Huffman and V. Tonchev,
       The existence of extremal self-dual `[50, 25, 10]` codes and
       quasi-symmetric `2-(49, 9, 6)` designs,
       Designs, Codes and Cryptography
       September 1995, Volume 6, Issue 2, pp 97-106
    """
def BIBD_66_6_1():
    """
    Return a (66,6,1)-BIBD.

    This BIBD was obtained from La Jolla covering repository
    (https://dmgordon.org/cover) where it is attributed to Colin Barker.

    EXAMPLES::

        sage: from sage.combinat.designs.database import BIBD_66_6_1
        sage: from sage.combinat.designs.bibd import BalancedIncompleteBlockDesign
        sage: BalancedIncompleteBlockDesign(66, BIBD_66_6_1())
        (66,6,1)-Balanced Incomplete Block Design
    """
def BIBD_76_6_1():
    """
    Return a (76,6,1)-BIBD.

    This BIBD was obtained from La Jolla covering repository
    (https://dmgordon.org/cover) where it is attributed to Colin Barker.

    EXAMPLES::

        sage: from sage.combinat.designs.database import BIBD_76_6_1
        sage: from sage.combinat.designs.bibd import BalancedIncompleteBlockDesign
        sage: BalancedIncompleteBlockDesign(76, BIBD_76_6_1())
        (76,6,1)-Balanced Incomplete Block Design
    """
def BIBD_96_6_1():
    """
    Return a (96,6,1)-BIBD.

    This BIBD was obtained from La Jolla covering repository
    (https://dmgordon.org/cover) where it is attributed to Colin Barker.

    EXAMPLES::

        sage: from sage.combinat.designs.database import BIBD_96_6_1
        sage: from sage.combinat.designs.bibd import BalancedIncompleteBlockDesign
        sage: BalancedIncompleteBlockDesign(96, BIBD_96_6_1())
        (96,6,1)-Balanced Incomplete Block Design
    """
def BIBD_106_6_1():
    """
    Return a (106,6,1)-BIBD.

    This constructions appears in II.3.32 from [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.database import BIBD_106_6_1
        sage: from sage.combinat.designs.bibd import BalancedIncompleteBlockDesign
        sage: BalancedIncompleteBlockDesign(106, BIBD_106_6_1())
        (106,6,1)-Balanced Incomplete Block Design
    """
def BIBD_111_6_1():
    """
    Return a (111,6,1)-BIBD.

    This constructions appears in II.3.32 from [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.database import BIBD_111_6_1
        sage: from sage.combinat.designs.bibd import BalancedIncompleteBlockDesign
        sage: BalancedIncompleteBlockDesign(111, BIBD_111_6_1())
        (111,6,1)-Balanced Incomplete Block Design
    """
def BIBD_126_6_1():
    """
    Return a (126,6,1)-BIBD.

    This constructions appears in VI.16.92 from [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.database import BIBD_126_6_1
        sage: from sage.combinat.designs.bibd import BalancedIncompleteBlockDesign
        sage: BalancedIncompleteBlockDesign(126, BIBD_126_6_1())
        (126,6,1)-Balanced Incomplete Block Design
    """
def BIBD_136_6_1():
    """
    Return a (136,6,1)-BIBD.

    This constructions appears in II.3.32 from [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.database import BIBD_136_6_1
        sage: from sage.combinat.designs.bibd import BalancedIncompleteBlockDesign
        sage: BalancedIncompleteBlockDesign(136, BIBD_136_6_1())
        (136,6,1)-Balanced Incomplete Block Design
    """
def BIBD_141_6_1():
    """
    Return a (141,6,1)-BIBD.

    This constructions appears in II.3.32 from [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.database import BIBD_141_6_1
        sage: from sage.combinat.designs.bibd import BalancedIncompleteBlockDesign
        sage: BalancedIncompleteBlockDesign(141, BIBD_141_6_1())
        (141,6,1)-Balanced Incomplete Block Design
    """
def BIBD_171_6_1():
    """
    Return a (171,6,1)-BIBD.

    This constructions appears in II.3.32 from [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.database import BIBD_171_6_1
        sage: from sage.combinat.designs.bibd import BalancedIncompleteBlockDesign
        sage: BalancedIncompleteBlockDesign(171, BIBD_171_6_1())
        (171,6,1)-Balanced Incomplete Block Design
    """
def HigmanSimsDesign():
    """
    Return the Higman-Sims designs, which is a `(176, 50, 14)`-BIBD.

    This design is built from a from the :func:`WittDesign
    <sage.combinat.designs.block_design.WittDesign>` `W` on 24 points. We define
    two points `a,b`, and consider:

    - The collection `W_a` of all blocks of `W` containing `a` but not
      containing `b`.

    - The collection `W_b` of all blocks of `W` containing `b` but not
      containing `a`.

    The design is then obtained from the incidence structure produced by the
    blocks `A\\in W_a` and `B\\in W_b` whose intersection has cardinality 2. This
    construction, due to M.Smith, can be found in [KY04]_ or in 10.A.(v) of
    [BL1984]_.

    EXAMPLES::

        sage: H = designs.HigmanSimsDesign(); H                     # optional - gap_package_design
        Incidence structure with 176 points and 176 blocks
        sage: H.is_t_design(return_parameters=1)                    # optional - gap_package_design
        (True, (2, 176, 50, 14))

    Make sure that the automorphism group of this designs is isomorphic to the
    automorphism group of the
    :func:`~sage.graphs.generators.smallgraphs.HigmanSimsGraph`. Note that the
    first of those permutation groups acts on 176 points, while the second acts
    on 100::

        sage: gH = H.automorphism_group()                           # optional - gap_package_design
        sage: gG = graphs.HigmanSimsGraph().automorphism_group()    # optional - gap_package_design
        sage: gG.is_isomorphic(gG)                       # long time, optional - gap_package_design
        True

    REFERENCE:

    .. [KY04] \\S. Klee and L. Yates,
       Tight Subdesigns of the Higman-Sims Design,
       Rose-Hulman Undergraduate Math. J 5.2 (2004).
       https://www.rose-hulman.edu/mathjournal/archives/2004/vol5-n2/paper9/v5n2-9pd.pdf
    """
def BIBD_196_6_1():
    """
    Return a (196,6,1)-BIBD.

    This constructions appears in II.3.32 from [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.database import BIBD_196_6_1
        sage: from sage.combinat.designs.bibd import BalancedIncompleteBlockDesign
        sage: BalancedIncompleteBlockDesign(196, BIBD_196_6_1())
        (196,6,1)-Balanced Incomplete Block Design
    """
def BIBD_201_6_1():
    """
    Return a (201,6,1)-BIBD.

    This constructions appears in II.3.32 from [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.database import BIBD_201_6_1
        sage: from sage.combinat.designs.bibd import BalancedIncompleteBlockDesign
        sage: BalancedIncompleteBlockDesign(201, BIBD_201_6_1())
        (201,6,1)-Balanced Incomplete Block Design
    """
def BIBD_79_13_2():
    """
    Return a symmetric `(79,13,2)`-BIBD.

    The construction implemented is the one described in [Aschbacher71]_.
    A typo in that paper was corrected in [Hall71]_.

    .. NOTE::

        A symmetric `(v,k,\\lambda)` BIBD is a `(v,k,\\lambda)` BIBD with `v` blocks.

    EXAMPLES:

        sage: from sage.combinat.designs.database import BIBD_79_13_2
        sage: D = IncidenceStructure(BIBD_79_13_2())                                    # needs sage.libs.gap
        sage: D.is_t_design(t=2, v=79, k=13, l=2)                                       # needs sage.libs.gap
        True
    """
def BIBD_56_11_2():
    """
    Return a symmetric `(56,11,2)`-BIBD.

    The construction implemented is given in [Hall71]_.

    .. NOTE::

        A symmetric `(v,k,\\lambda)` BIBD is a `(v,k,\\lambda)` BIBD with `v` blocks.

    EXAMPLES:

        sage: from sage.combinat.designs.database import BIBD_56_11_2
        sage: D = IncidenceStructure(BIBD_56_11_2())                                    # needs sage.libs.gap
        sage: D.is_t_design(t=2, v=56, k=11, l=2)                                       # needs sage.libs.gap
        True
    """

BIBD_constructions: Incomplete
LIST_OF_BIBD: Incomplete
R: Incomplete
a: Incomplete
EDS: Incomplete
LIST_OF_EDS: Incomplete

def ca_11_2_5_3():
    """
    Return a CA with the given parameters. This CA is proven to be optimal.

    Data obtained from https://zenodo.org/records/1476059

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_covering_array
        sage: from sage.combinat.designs.database import ca_11_2_5_3
        sage: C = ca_11_2_5_3()
        sage: is_covering_array(C,2,3)
        True

    """
def ca_12_2_7_3():
    """
    Return a CA with the given parameters. This CA is proven to be optimal.

    Data obtained from https://zenodo.org/records/1476059

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_covering_array
        sage: from sage.combinat.designs.database import ca_12_2_7_3
        sage: C = ca_12_2_7_3()
        sage: is_covering_array(C,2,3)
        True

    """
def ca_13_2_9_3():
    """
    Return a CA with the given parameters. This CA is proven to be optimal.

    Data obtained from https://zenodo.org/records/1476059

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_covering_array
        sage: from sage.combinat.designs.database import ca_13_2_9_3
        sage: C = ca_13_2_9_3()
        sage: is_covering_array(C,2,3)
        True

    """
def ca_14_2_10_3():
    """
    Return a CA with the given parameters. This CA is proven to be optimal.

    Data obtained from https://zenodo.org/records/1476059

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_covering_array
        sage: from sage.combinat.designs.database import ca_14_2_10_3
        sage: C = ca_14_2_10_3()
        sage: is_covering_array(C,2,3)
        True

    """
def ca_15_2_20_3():
    """
    Return a CA with the given parameters. This CA is proven to be optimal.

    Data obtained from [Nur2004]_

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_covering_array
        sage: from sage.combinat.designs.database import ca_15_2_20_3
        sage: C = ca_15_2_20_3()
        sage: is_covering_array(C,2,3)
        True

    """
def ca_19_2_6_4():
    """
    Return a CA with the given parameters. This CA is proven to be optimal.

    Data obtained from https://zenodo.org/records/1476059

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_covering_array
        sage: from sage.combinat.designs.database import ca_19_2_6_4
        sage: C = ca_19_2_6_4()
        sage: is_covering_array(C,2,4)
        True

    """
def ca_21_2_7_4():
    """
    Return a CA with the given parameters. This CA is proven to be optimal.
    This CA is also uniform.

    Data obtained from https://zenodo.org/records/1476059

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_covering_array
        sage: from sage.combinat.designs.database import ca_21_2_7_4
        sage: C = ca_21_2_7_4()
        sage: is_covering_array(C,2,4)
        True

    """
def ca_29_2_7_5():
    """
    Return a CA with the given parameters. This CA is proven to be optimal.

    Data obtained from https://zenodo.org/records/1476059

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_covering_array
        sage: from sage.combinat.designs.database import ca_29_2_7_5
        sage: C = ca_29_2_7_5()
        sage: is_covering_array(C,2,5)
        True

    """
def ca_37_2_4_6():
    """
    Return a CA with the given parameters. This CA is proven to be optimal.

    Data obtained from https://zenodo.org/records/1476059

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_covering_array
        sage: from sage.combinat.designs.database import ca_37_2_4_6
        sage: C = ca_37_2_4_6()
        sage: is_covering_array(C,2,6)
        True

    """
def ca_39_2_5_6():
    """
    Return a CA with the given parameters. This CA is proven to be optimal.

    Data obtained from https://zenodo.org/records/1476059

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_covering_array
        sage: from sage.combinat.designs.database import ca_39_2_5_6
        sage: C = ca_39_2_5_6()
        sage: is_covering_array(C,2,6)
        True

    """
def ca_41_2_6_6():
    """
    Return a CA with the given parameters. This CA is proven to be optimal.
    This CA is also uniform.

    Data obtained from https://zenodo.org/records/1476059

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_covering_array
        sage: from sage.combinat.designs.database import ca_41_2_6_6
        sage: C = ca_41_2_6_6()
        sage: is_covering_array(C,2,6)
        True

    """

CA_constructions: Incomplete
LIST_OF_CA_CONSTRUCTIONS: Incomplete
__doc__: Incomplete
