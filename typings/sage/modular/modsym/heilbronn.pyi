import _cython_3_2_1
import sage.modular.modsym.p1list as p1list
from sage.arith.misc import is_prime as is_prime
from sage.misc.verbose import verbose as verbose
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

hecke_images_gamma0_weight2: _cython_3_2_1.cython_function_or_method
hecke_images_gamma0_weight_k: _cython_3_2_1.cython_function_or_method
hecke_images_nonquad_character_weight2: _cython_3_2_1.cython_function_or_method
hecke_images_quad_character_weight2: _cython_3_2_1.cython_function_or_method

class Heilbronn:
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def apply(self, intu, intv, intN) -> Any:
        """Heilbronn.apply(self, int u, int v, int N)

        File: /build/sagemath/src/sage/src/sage/modular/modsym/heilbronn.pyx (starting at line 228)

        Return a list of pairs `((c,d),m)`, which is obtained as follows:

        1) Compute the images `(a,b)` of the vector `(u,v) \\pmod N` acted on by
        each of the HeilbronnCremona matrices in ``self``.

        2) Reduce each `(a,b)` to canonical form `(c,d)` using ``p1normalize``.

        3) Sort.

        4) Create the list `((c,d),m)`, where `m` is the number of times
        that `(c,d)` appears in the list created in steps 1-3
        above. Note that the pairs `((c,d),m)` are sorted
        lexicographically by `(c,d)`.

        INPUT:

        - ``u``, ``v``, ``N`` -- integers

        OUTPUT: list

        EXAMPLES::

            sage: H = sage.modular.modsym.heilbronn.HeilbronnCremona(2); H
            The Cremona-Heilbronn matrices of determinant 2
            sage: H.apply(1,2,7)
            [((1, 1), 1), ((1, 4), 1), ((1, 5), 1), ((1, 6), 1)]"""
    @overload
    def to_list(self) -> Any:
        """Heilbronn.to_list(self)

        File: /build/sagemath/src/sage/src/sage/modular/modsym/heilbronn.pyx (starting at line 152)

        Return the list of Heilbronn matrices corresponding to ``self``.

        Each matrix is given as a list of four integers.

        EXAMPLES::

            sage: H = HeilbronnCremona(2); H
            The Cremona-Heilbronn matrices of determinant 2
            sage: H.to_list()
            [[1, 0, 0, 2], [2, 0, 0, 1], [2, 1, 0, 1], [1, 0, 1, 2]]"""
    @overload
    def to_list(self) -> Any:
        """Heilbronn.to_list(self)

        File: /build/sagemath/src/sage/src/sage/modular/modsym/heilbronn.pyx (starting at line 152)

        Return the list of Heilbronn matrices corresponding to ``self``.

        Each matrix is given as a list of four integers.

        EXAMPLES::

            sage: H = HeilbronnCremona(2); H
            The Cremona-Heilbronn matrices of determinant 2
            sage: H.to_list()
            [[1, 0, 0, 2], [2, 0, 0, 1], [2, 1, 0, 1], [1, 0, 1, 2]]"""
    def __getitem__(self, intn) -> Any:
        """Heilbronn.__getitem__(self, int n)

        File: /build/sagemath/src/sage/src/sage/modular/modsym/heilbronn.pyx (starting at line 122)

        Return the `n`-th matrix in ``self``.

        EXAMPLES::

            sage: H = HeilbronnCremona(11)
            sage: H[17]
            [-1, 0, 1, -11]
            sage: H[98234]
            Traceback (most recent call last):
            ...
            IndexError"""
    @overload
    def __len__(self) -> Any:
        """Heilbronn.__len__(self)

        File: /build/sagemath/src/sage/src/sage/modular/modsym/heilbronn.pyx (starting at line 141)

        Return the number of matrices in ``self``.

        EXAMPLES::

            sage: HeilbronnCremona(2).__len__()
            4"""
    @overload
    def __len__(self) -> Any:
        """Heilbronn.__len__(self)

        File: /build/sagemath/src/sage/src/sage/modular/modsym/heilbronn.pyx (starting at line 141)

        Return the number of matrices in ``self``.

        EXAMPLES::

            sage: HeilbronnCremona(2).__len__()
            4"""

class HeilbronnCremona(Heilbronn):
    """HeilbronnCremona(int p)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    p: p
    def __init__(self, intp) -> Any:
        """File: /build/sagemath/src/sage/src/sage/modular/modsym/heilbronn.pyx (starting at line 303)

                Create the list of Heilbronn-Cremona matrices of determinant `p`.

                EXAMPLES::

                    sage: H = HeilbronnCremona(3) ; H
                    The Cremona-Heilbronn matrices of determinant 3
                    sage: H.to_list()
                    [[1, 0, 0, 3],
                    [3, 1, 0, 1],
                    [1, 0, 1, 3],
                    [3, 0, 0, 1],
                    [3, -1, 0, 1],
                    [-1, 0, 1, -3]]
        """

class HeilbronnMerel(Heilbronn):
    """HeilbronnMerel(int n)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    n: n
    def __init__(self, intn) -> Any:
        """File: /build/sagemath/src/sage/src/sage/modular/modsym/heilbronn.pyx (starting at line 417)

                Initialize the list of Merel-Heilbronn matrices of determinant `n`.

                EXAMPLES::

                    sage: H = HeilbronnMerel(3) ; H
                    The Merel-Heilbronn matrices of determinant 3
                    sage: H.to_list()
                    [[1, 0, 0, 3],
                    [1, 0, 1, 3],
                    [1, 0, 2, 3],
                    [2, 1, 1, 2],
                    [3, 0, 0, 1],
                    [3, 1, 0, 1],
                    [3, 2, 0, 1]]
        """
