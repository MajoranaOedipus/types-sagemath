from sage.combinat.posets.lattices import LatticePoset as LatticePoset, MeetSemilattice as MeetSemilattice

def paths_in_triangle(i, j, a, b) -> list[tuple[int, ...]]:
    """
    Return all Dyck paths from `(0,0)` to `(i,j)` in the `(a \\times
    b)`-rectangle.

    This means that at each step of the path, one has `a y \\geq b x`.

    A path is represented by a sequence of `0` and `1`, where `0` is an
    horizontal step `(1,0)` and `1` is a vertical step `(0,1)`.

    INPUT:

    - ``a``, ``b`` -- integers with `a \\geq b`

    - ``i``, ``j`` -- nonnegative integers with `1 \\geq \\frac{j}{b} \\geq
      \\frac{i}{a} \\geq 0`

    OUTPUT: list of paths

    EXAMPLES::

        sage: from sage.combinat.tamari_lattices import paths_in_triangle
        sage: paths_in_triangle(2,2,2,2)
        [(1, 0, 1, 0), (1, 1, 0, 0)]
        sage: paths_in_triangle(2,3,4,4)
        [(1, 0, 1, 0, 1), (1, 1, 0, 0, 1), (1, 0, 1, 1, 0),
        (1, 1, 0, 1, 0), (1, 1, 1, 0, 0)]
        sage: paths_in_triangle(2,1,4,4)
        Traceback (most recent call last):
        ...
        ValueError: the endpoint is not valid
        sage: paths_in_triangle(3,2,5,3)
        [(1, 0, 1, 0, 0), (1, 1, 0, 0, 0)]
    """
def swap(p, i, m: int = 1) -> tuple[int, ...]:
    """
    Perform a covering move in the `(a,b)`-Tamari lattice of slope parameter `m`.

    The letter at position `i` in `p` must be a `0`, followed by at
    least one `1`.

    INPUT:

    - ``p`` -- a Dyck path in the `(a \\times b)`-rectangle

    - ``i`` -- integer between `0` and `a+b-1`

    OUTPUT: a Dyck path in the `(a \\times b)`-rectangle

    EXAMPLES::

        sage: from sage.combinat.tamari_lattices import swap
        sage: swap((1,0,1,0,0),1)
        (1, 1, 0, 0, 0)
        sage: swap((1,1,0,0,1,1,0,0,0),3)
        (1, 1, 0, 1, 1, 0, 0, 0, 0)
        sage: swap((1,0,1,0,1,0,0,0), 1, 1)
        (1, 1, 0, 0, 1, 0, 0, 0)
        sage: swap((1,0,1,0,1,0,0,0), 1, 5/3)
        (1, 1, 0, 1, 0, 0, 0, 0)


    TESTS::

        sage: swap((1,0,1,0),6)
        Traceback (most recent call last):
        ...
        ValueError: the index is greater than the length of the path
        sage: swap((1,1,0,0,1,1,0,0),2)
        Traceback (most recent call last):
        ...
        ValueError: there is no such covering move
    """
def GeneralizedTamariLattice(a, b, m: int = 1):
    """
    Return the `(a,b)`-Tamari lattice of parameter `m`.

    INPUT:

    - ``a``, ``b`` -- integers with `a \\geq b`

    - ``m`` -- a nonnegative rational number such that `a \\geq b m`

    OUTPUT:

    - a finite lattice (special case of the alt `\\nu`-Tamari lattices in [CC2023]_)

    The elements of the lattice are
    :func:`Dyck paths<sage.combinat.dyck_word.DyckWord>` in the
    `(a \\times b)`-rectangle.

    The parameter `m` (slope) is used only to define the covering relations.
    When the slope `m` is `0`, two paths are comparable if and only if
    one is always above the other.

    The usual :wikipedia:`Tamari lattice<Tamari_lattice>` of index `b`
    is the special case `a=b+1` and `m=1`.

    Other special cases give the `m`-Tamari lattices studied in [BMFPR2011]_,
    or the rational Tamari lattices when a and b are coprime and m = a/b (see [PRV2017]_).

    EXAMPLES::

        sage: from sage.combinat.tamari_lattices import GeneralizedTamariLattice
        sage: GeneralizedTamariLattice(3,2)
        Finite lattice containing 2 elements
        sage: GeneralizedTamariLattice(4,3)
        Finite lattice containing 5 elements
        sage: GeneralizedTamariLattice(7,5,2)
        Traceback (most recent call last):
        ...
        ValueError: the condition a>=b*m does not hold
        sage: P = GeneralizedTamariLattice(5,3); P
        Finite lattice containing 7 elements
        sage: P = GeneralizedTamariLattice(5, 3, m=5/3); P
        Finite lattice containing 7 elements


    TESTS::

        sage: P.coxeter_transformation()**18 == 1                                       # needs sage.libs.flint
        True

    REFERENCES:

    - [BMFPR2011]_

    - [PRV2017]_

    - [CC2023]_
    """
def TamariLattice(n, m: int = 1):
    """
    Return the `n`-th Tamari lattice.

    Using the slope parameter `m`, one can also get the `m`-Tamari lattices.

    INPUT:

    - ``n`` -- nonnegative integer (the index)

    - ``m`` -- nonnegative integer (the slope, default: 1)

    OUTPUT: a finite lattice

    In the usual case, the elements of the lattice are :func:`Dyck
    paths<sage.combinat.dyck_word.DyckWord>` in the `(n+1 \\times
    n)`-rectangle. For a general slope `m`, the elements are Dyck
    paths in the `(m n+1 \\times n)`-rectangle.

    See :wikipedia:`Tamari lattice<Tamari_lattice>` for mathematical
    background.

    EXAMPLES::

        sage: posets.TamariLattice(3)
        Finite lattice containing 5 elements

        sage: posets.TamariLattice(3, 2)
        Finite lattice containing 12 elements

    REFERENCES:

    - [BMFPR2011]_
    """
def swap_dexter(p, i) -> list[tuple[int, ...]]:
    """
    Perform covering moves in the `(a,b)`-Dexter posets.

    The letter at position `i` in `p` must be a `0`, followed by at
    least one `1`.

    INPUT:

    - ``p`` -- a Dyck path in the `(a \\times b)`-rectangle

    - ``i`` -- integer between `0` and `a+b-1`

    OUTPUT:

    - a list of Dyck paths in the `(a \\times b)`-rectangle

    EXAMPLES::

        sage: from sage.combinat.tamari_lattices import swap_dexter
        sage: swap_dexter((1,0,1,0,0),1)
        [(1, 1, 0, 0, 0)]
        sage: swap_dexter((1,1,0,0,1,1,0,0,0),3)
        [(1, 1, 0, 1, 1, 0, 0, 0, 0), (1, 1, 1, 1, 0, 0, 0, 0, 0)]
        sage: swap_dexter((1,1,0,1,0,0,0),2)
        []

    TESTS::

        sage: swap_dexter((1,0,1,0,0),6)
        Traceback (most recent call last):
        ...
        ValueError: the index is greater than the length of the path

        sage: swap_dexter((1,1,0,0,1,1,0,0,0),2)
        Traceback (most recent call last):
        ...
        ValueError: there is no such covering move
    """
def DexterSemilattice(n):
    """
    Return the `n`-th Dexter meet-semilattice.

    INPUT:

    - ``n`` -- nonnegative integer (the index)

    OUTPUT: a finite meet-semilattice

    The elements of the semilattice are :func:`Dyck
    paths<sage.combinat.dyck_word.DyckWord>` in the `(n+1 \\times
    n)`-rectangle.

    EXAMPLES::

        sage: posets.DexterSemilattice(3)
        Finite meet-semilattice containing 5 elements

        sage: P = posets.DexterSemilattice(4); P
        Finite meet-semilattice containing 14 elements
        sage: len(P.maximal_chains())
        15
        sage: len(P.maximal_elements())
        4
        sage: P.chain_polynomial()
        q^5 + 19*q^4 + 47*q^3 + 42*q^2 + 14*q + 1

    REFERENCES:

    - [Cha18]_
    """
