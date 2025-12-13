from sage.combinat.nu_dyck_word import NuDyckWord as NuDyckWord, NuDyckWords as NuDyckWords
from sage.combinat.posets.lattices import LatticePoset as LatticePoset

def NuTamariLattice(nu):
    """
    Return the `\\nu`-Tamari lattice.

    INPUT:

    - `\\nu` -- list of 0s and 1s or a string of 0s and 1s

    OUTPUT: a finite lattice

    The elements of the lattice are
    :func:`\\nu-Dyck paths<sage.combinat.nu_dyck_word.NuDyckWord>` weakly above
    `\\nu`.

    The usual :wikipedia:`Tamari lattice<Tamari_lattice>` is the special case
    where `\\nu = (NE)^h` where `h` is the height.

    Other special cases give the `m`-Tamari lattices studied in [BMFPR]_.

    EXAMPLES::

        sage: from sage.combinat.nu_tamari_lattice import NuTamariLattice
        sage: NuTamariLattice([1,0,1,0,0,1,0])
        Finite lattice containing 7 elements
        sage: NuTamariLattice([1,0,1,0,1,0])
        Finite lattice containing 5 elements
        sage: NuTamariLattice([1,0,1,0,1,0,1,0])
        Finite lattice containing 14 elements
        sage: NuTamariLattice([1,0,1,0,1,0,0,0,1])
        Finite lattice containing 24 elements
    """
def delta_swap(p, k, delta):
    """
    Perform a covering move in the `(\\delta,\\nu)`-Tamari lattice (or alt
    `\\nu`-Tamari lattice, see [CC2023]_).

    The letter at position `k` is a North step of the `\\nu`-Dyck word `p`, and
    must be preceded by an East step.

    The vector `\\delta = (\\delta_1, \\dots, \\delta_n)` is an increment vector
    with respect to the path `\\nu`, that is to say `\\delta_i \\leq \\nu_i`, where
    `\\nu_i` is the number of East steps following the `i`-th North step of
    `\\nu`.

    INPUT:

    - ``p`` -- a `\\nu`-Dyck word

    - ``k`` -- integer between `0` and ``p.length()-1``

    - ``delta`` -- list of nonnegative integers of length ``p.height()``

    OUTPUT: a `\\nu`-Dyck word

    EXAMPLES::

        sage: from sage.combinat.nu_tamari_lattice import delta_swap
        sage: delta_swap(NuDyckWord('0101', '0101'), 3, delta = [1, 0])
        [0, 1, 1, 0]
        sage: delta_swap(NuDyckWord('1001110100', '0100010111'), 3, [3, 1, 0, 0, 0])
        [1, 0, 1, 1, 1, 0, 0, 1, 0, 0]
        sage: delta_swap(NuDyckWord('10100101000', '01001000110'), 2, [2, 3, 0, 1])
        [1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]
        sage: delta_swap(NuDyckWord('10100101000', '01001000110'), 2, [1, 1, 0, 0])
        [1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0]


    TESTS::

        sage: delta_swap(NuDyckWord('10011101000', '01000101110'), 0, [3, 1, 0, 0, 1])
        Traceback (most recent call last):
        ...
        ValueError: there is no such covering move
        sage: delta_swap(NuDyckWord('10011101000', '01000101110'), 1, [3, 1, 0, 0, 1])
        Traceback (most recent call last):
        ...
        ValueError: there is no such covering move
        sage: delta_swap(NuDyckWord('10011101000', '01000101110'), 11, [3, 1, 0, 0, 1])
        Traceback (most recent call last):
        ...
        ValueError: the index is greater than the length of the path
    """
def AltNuTamariLattice(nu, delta=None):
    """
    Return the `(\\delta,\\nu)`-Tamari lattice (or alt `\\nu`-Tamari lattice).

    For more information, see [CC2023]_.

    The path `\\nu` is a path of North steps (represented as `1` s) and East
    steps (represented as `0` s).

    The vector `\\delta = (\\delta_1, \\dots, \\delta_n)` is an increment vector
    with respect to the path `\\nu`, that is to say `\\delta_i \\leq \\nu_i`, where
    `\\nu_i` is the number of `0` s following the `i`-th `1` of `\\nu`. If not
    provided, `\\delta` is set by default to produce the classical `\\nu`-Tamari
    lattice.

    INPUT:

    - `\\nu` -- list of 0s and 1s or a string of 0s and 1s

    - `\\delta` -- list of nonnegative integers

    OUTPUT: a finite lattice

    EXAMPLES::

        sage: from sage.combinat.nu_tamari_lattice import AltNuTamariLattice, NuTamariLattice
        sage: AltNuTamariLattice('01001', [0, 0])
        Finite lattice containing 7 elements
        sage: AltNuTamariLattice('01001', [1, 0])
        Finite lattice containing 7 elements
        sage: AltNuTamariLattice('01001') == AltNuTamariLattice('01001', [2, 0])
        True
        sage: nu = '00100100101'; P = AltNuTamariLattice(nu); Q = NuTamariLattice(nu); P == Q
        True

    TESTS::

        sage: AltNuTamariLattice('012', [0,0])
        Traceback (most recent call last):
        ...
        ValueError: nu must be a list or a string of 0s and 1s
        sage: AltNuTamariLattice([0,10,0,11], [2,0,0])
        Traceback (most recent call last):
        ...
        ValueError: nu must be a list or a string of 0s and 1s
        sage: AltNuTamariLattice('01001', [0, 1, 0])
        Traceback (most recent call last):
        ...
        ValueError: delta is not a valid increment vector
        sage: AltNuTamariLattice('0100101', [3, 0, 0])
        Traceback (most recent call last):
        ...
        ValueError: delta is not a valid increment vector

    REFERENCES:

    - [PRV2017]_

    - [CC2023]_
    """
