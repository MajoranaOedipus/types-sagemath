from sage.rings.complex_interval_field import CIF as CIF
from typing import Any, overload

class PeriodicRegion:
    """PeriodicRegion(w1, w2, data, full=True)"""
    data: File
    full: File
    w1: w1
    w2: w2
    def __init__(self, w1, w2, data, full=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/period_lattice_region.pyx (starting at line 51)

                EXAMPLES::

                    sage: import numpy as np
                    sage: from sage.schemes.elliptic_curves.period_lattice_region import PeriodicRegion
                    sage: S = PeriodicRegion(CDF(2), CDF(2*I), np.zeros((4, 4)))
                    sage: S.plot()                                                              # needs sage.plot
                    Graphics object consisting of 1 graphics primitive
                    sage: data = np.zeros((4, 4))
                    sage: data[1,1] = True
                    sage: S = PeriodicRegion(CDF(2), CDF(2*I+1), data)
                    sage: S.plot()                                                              # needs sage.plot
                    Graphics object consisting of 5 graphics primitives
        """
    @overload
    def border(self, raw=...) -> Any:
        """PeriodicRegion.border(self, raw=True)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/period_lattice_region.pyx (starting at line 562)

        Return the boundary of this region as set of tile boundaries.

        If raw is true, returns a list with respect to the internal bitmap,
        otherwise returns complex intervals covering the border.

        EXAMPLES::

            sage: import numpy as np
            sage: from sage.schemes.elliptic_curves.period_lattice_region import PeriodicRegion
            sage: data = np.zeros((4, 4))
            sage: data[1, 1] = True
            sage: PeriodicRegion(CDF(1), CDF(I), data).border()
            [(1, 1, 0), (2, 1, 0), (1, 1, 1), (1, 2, 1)]
            sage: PeriodicRegion(CDF(2), CDF(I-1/2), data).border()
            [(1, 1, 0), (2, 1, 0), (1, 1, 1), (1, 2, 1)]

            sage: PeriodicRegion(CDF(1), CDF(I), data).border(raw=False)
            [0.25000000000000000? + 1.?*I,
             0.50000000000000000? + 1.?*I,
             1.? + 0.25000000000000000?*I,
             1.? + 0.50000000000000000?*I]
            sage: PeriodicRegion(CDF(2), CDF(I-1/2), data).border(raw=False)
            [0.3? + 1.?*I,
             0.8? + 1.?*I,
             1.? + 0.25000000000000000?*I,
             1.? + 0.50000000000000000?*I]

            sage: data[1:3, 2] = True
            sage: PeriodicRegion(CDF(1), CDF(I), data).border()
            [(1, 1, 0), (2, 1, 0), (1, 1, 1), (1, 2, 0), (1, 3, 1), (3, 2, 0), (2, 2, 1), (2, 3, 1)]"""
    @overload
    def border(self) -> Any:
        """PeriodicRegion.border(self, raw=True)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/period_lattice_region.pyx (starting at line 562)

        Return the boundary of this region as set of tile boundaries.

        If raw is true, returns a list with respect to the internal bitmap,
        otherwise returns complex intervals covering the border.

        EXAMPLES::

            sage: import numpy as np
            sage: from sage.schemes.elliptic_curves.period_lattice_region import PeriodicRegion
            sage: data = np.zeros((4, 4))
            sage: data[1, 1] = True
            sage: PeriodicRegion(CDF(1), CDF(I), data).border()
            [(1, 1, 0), (2, 1, 0), (1, 1, 1), (1, 2, 1)]
            sage: PeriodicRegion(CDF(2), CDF(I-1/2), data).border()
            [(1, 1, 0), (2, 1, 0), (1, 1, 1), (1, 2, 1)]

            sage: PeriodicRegion(CDF(1), CDF(I), data).border(raw=False)
            [0.25000000000000000? + 1.?*I,
             0.50000000000000000? + 1.?*I,
             1.? + 0.25000000000000000?*I,
             1.? + 0.50000000000000000?*I]
            sage: PeriodicRegion(CDF(2), CDF(I-1/2), data).border(raw=False)
            [0.3? + 1.?*I,
             0.8? + 1.?*I,
             1.? + 0.25000000000000000?*I,
             1.? + 0.50000000000000000?*I]

            sage: data[1:3, 2] = True
            sage: PeriodicRegion(CDF(1), CDF(I), data).border()
            [(1, 1, 0), (2, 1, 0), (1, 1, 1), (1, 2, 0), (1, 3, 1), (3, 2, 0), (2, 2, 1), (2, 3, 1)]"""
    @overload
    def border(self) -> Any:
        """PeriodicRegion.border(self, raw=True)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/period_lattice_region.pyx (starting at line 562)

        Return the boundary of this region as set of tile boundaries.

        If raw is true, returns a list with respect to the internal bitmap,
        otherwise returns complex intervals covering the border.

        EXAMPLES::

            sage: import numpy as np
            sage: from sage.schemes.elliptic_curves.period_lattice_region import PeriodicRegion
            sage: data = np.zeros((4, 4))
            sage: data[1, 1] = True
            sage: PeriodicRegion(CDF(1), CDF(I), data).border()
            [(1, 1, 0), (2, 1, 0), (1, 1, 1), (1, 2, 1)]
            sage: PeriodicRegion(CDF(2), CDF(I-1/2), data).border()
            [(1, 1, 0), (2, 1, 0), (1, 1, 1), (1, 2, 1)]

            sage: PeriodicRegion(CDF(1), CDF(I), data).border(raw=False)
            [0.25000000000000000? + 1.?*I,
             0.50000000000000000? + 1.?*I,
             1.? + 0.25000000000000000?*I,
             1.? + 0.50000000000000000?*I]
            sage: PeriodicRegion(CDF(2), CDF(I-1/2), data).border(raw=False)
            [0.3? + 1.?*I,
             0.8? + 1.?*I,
             1.? + 0.25000000000000000?*I,
             1.? + 0.50000000000000000?*I]

            sage: data[1:3, 2] = True
            sage: PeriodicRegion(CDF(1), CDF(I), data).border()
            [(1, 1, 0), (2, 1, 0), (1, 1, 1), (1, 2, 0), (1, 3, 1), (3, 2, 0), (2, 2, 1), (2, 3, 1)]"""
    @overload
    def border(self, raw=...) -> Any:
        """PeriodicRegion.border(self, raw=True)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/period_lattice_region.pyx (starting at line 562)

        Return the boundary of this region as set of tile boundaries.

        If raw is true, returns a list with respect to the internal bitmap,
        otherwise returns complex intervals covering the border.

        EXAMPLES::

            sage: import numpy as np
            sage: from sage.schemes.elliptic_curves.period_lattice_region import PeriodicRegion
            sage: data = np.zeros((4, 4))
            sage: data[1, 1] = True
            sage: PeriodicRegion(CDF(1), CDF(I), data).border()
            [(1, 1, 0), (2, 1, 0), (1, 1, 1), (1, 2, 1)]
            sage: PeriodicRegion(CDF(2), CDF(I-1/2), data).border()
            [(1, 1, 0), (2, 1, 0), (1, 1, 1), (1, 2, 1)]

            sage: PeriodicRegion(CDF(1), CDF(I), data).border(raw=False)
            [0.25000000000000000? + 1.?*I,
             0.50000000000000000? + 1.?*I,
             1.? + 0.25000000000000000?*I,
             1.? + 0.50000000000000000?*I]
            sage: PeriodicRegion(CDF(2), CDF(I-1/2), data).border(raw=False)
            [0.3? + 1.?*I,
             0.8? + 1.?*I,
             1.? + 0.25000000000000000?*I,
             1.? + 0.50000000000000000?*I]

            sage: data[1:3, 2] = True
            sage: PeriodicRegion(CDF(1), CDF(I), data).border()
            [(1, 1, 0), (2, 1, 0), (1, 1, 1), (1, 2, 0), (1, 3, 1), (3, 2, 0), (2, 2, 1), (2, 3, 1)]"""
    @overload
    def border(self, raw=...) -> Any:
        """PeriodicRegion.border(self, raw=True)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/period_lattice_region.pyx (starting at line 562)

        Return the boundary of this region as set of tile boundaries.

        If raw is true, returns a list with respect to the internal bitmap,
        otherwise returns complex intervals covering the border.

        EXAMPLES::

            sage: import numpy as np
            sage: from sage.schemes.elliptic_curves.period_lattice_region import PeriodicRegion
            sage: data = np.zeros((4, 4))
            sage: data[1, 1] = True
            sage: PeriodicRegion(CDF(1), CDF(I), data).border()
            [(1, 1, 0), (2, 1, 0), (1, 1, 1), (1, 2, 1)]
            sage: PeriodicRegion(CDF(2), CDF(I-1/2), data).border()
            [(1, 1, 0), (2, 1, 0), (1, 1, 1), (1, 2, 1)]

            sage: PeriodicRegion(CDF(1), CDF(I), data).border(raw=False)
            [0.25000000000000000? + 1.?*I,
             0.50000000000000000? + 1.?*I,
             1.? + 0.25000000000000000?*I,
             1.? + 0.50000000000000000?*I]
            sage: PeriodicRegion(CDF(2), CDF(I-1/2), data).border(raw=False)
            [0.3? + 1.?*I,
             0.8? + 1.?*I,
             1.? + 0.25000000000000000?*I,
             1.? + 0.50000000000000000?*I]

            sage: data[1:3, 2] = True
            sage: PeriodicRegion(CDF(1), CDF(I), data).border()
            [(1, 1, 0), (2, 1, 0), (1, 1, 1), (1, 2, 0), (1, 3, 1), (3, 2, 0), (2, 2, 1), (2, 3, 1)]"""
    @overload
    def border(self) -> Any:
        """PeriodicRegion.border(self, raw=True)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/period_lattice_region.pyx (starting at line 562)

        Return the boundary of this region as set of tile boundaries.

        If raw is true, returns a list with respect to the internal bitmap,
        otherwise returns complex intervals covering the border.

        EXAMPLES::

            sage: import numpy as np
            sage: from sage.schemes.elliptic_curves.period_lattice_region import PeriodicRegion
            sage: data = np.zeros((4, 4))
            sage: data[1, 1] = True
            sage: PeriodicRegion(CDF(1), CDF(I), data).border()
            [(1, 1, 0), (2, 1, 0), (1, 1, 1), (1, 2, 1)]
            sage: PeriodicRegion(CDF(2), CDF(I-1/2), data).border()
            [(1, 1, 0), (2, 1, 0), (1, 1, 1), (1, 2, 1)]

            sage: PeriodicRegion(CDF(1), CDF(I), data).border(raw=False)
            [0.25000000000000000? + 1.?*I,
             0.50000000000000000? + 1.?*I,
             1.? + 0.25000000000000000?*I,
             1.? + 0.50000000000000000?*I]
            sage: PeriodicRegion(CDF(2), CDF(I-1/2), data).border(raw=False)
            [0.3? + 1.?*I,
             0.8? + 1.?*I,
             1.? + 0.25000000000000000?*I,
             1.? + 0.50000000000000000?*I]

            sage: data[1:3, 2] = True
            sage: PeriodicRegion(CDF(1), CDF(I), data).border()
            [(1, 1, 0), (2, 1, 0), (1, 1, 1), (1, 2, 0), (1, 3, 1), (3, 2, 0), (2, 2, 1), (2, 3, 1)]"""
    @overload
    def contract(self, corners=...) -> Any:
        '''PeriodicRegion.contract(self, corners=True)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/period_lattice_region.pyx (starting at line 291)

        Opposite (but not inverse) of expand; removes neighbors of complement.

        EXAMPLES::

            sage: import numpy as np
            sage: if int(np.version.short_version[0]) > 1:
            ....:     _ = np.set_printoptions(legacy="1.25")
            sage: from sage.schemes.elliptic_curves.period_lattice_region import PeriodicRegion
            sage: data = np.zeros((10, 10))
            sage: data[1:4,1:4] = True
            sage: S = PeriodicRegion(CDF(1), CDF(I + 1/2), data)
            sage: S.plot()                                                              # needs sage.plot
            Graphics object consisting of 13 graphics primitives
            sage: S.contract().plot()                                                   # needs sage.plot
            Graphics object consisting of 5 graphics primitives
            sage: S.contract().data.sum()
            1
            sage: S.contract().contract().is_empty()
            True'''
    @overload
    def contract(self) -> Any:
        '''PeriodicRegion.contract(self, corners=True)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/period_lattice_region.pyx (starting at line 291)

        Opposite (but not inverse) of expand; removes neighbors of complement.

        EXAMPLES::

            sage: import numpy as np
            sage: if int(np.version.short_version[0]) > 1:
            ....:     _ = np.set_printoptions(legacy="1.25")
            sage: from sage.schemes.elliptic_curves.period_lattice_region import PeriodicRegion
            sage: data = np.zeros((10, 10))
            sage: data[1:4,1:4] = True
            sage: S = PeriodicRegion(CDF(1), CDF(I + 1/2), data)
            sage: S.plot()                                                              # needs sage.plot
            Graphics object consisting of 13 graphics primitives
            sage: S.contract().plot()                                                   # needs sage.plot
            Graphics object consisting of 5 graphics primitives
            sage: S.contract().data.sum()
            1
            sage: S.contract().contract().is_empty()
            True'''
    @overload
    def contract(self) -> Any:
        '''PeriodicRegion.contract(self, corners=True)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/period_lattice_region.pyx (starting at line 291)

        Opposite (but not inverse) of expand; removes neighbors of complement.

        EXAMPLES::

            sage: import numpy as np
            sage: if int(np.version.short_version[0]) > 1:
            ....:     _ = np.set_printoptions(legacy="1.25")
            sage: from sage.schemes.elliptic_curves.period_lattice_region import PeriodicRegion
            sage: data = np.zeros((10, 10))
            sage: data[1:4,1:4] = True
            sage: S = PeriodicRegion(CDF(1), CDF(I + 1/2), data)
            sage: S.plot()                                                              # needs sage.plot
            Graphics object consisting of 13 graphics primitives
            sage: S.contract().plot()                                                   # needs sage.plot
            Graphics object consisting of 5 graphics primitives
            sage: S.contract().data.sum()
            1
            sage: S.contract().contract().is_empty()
            True'''
    @overload
    def contract(self) -> Any:
        '''PeriodicRegion.contract(self, corners=True)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/period_lattice_region.pyx (starting at line 291)

        Opposite (but not inverse) of expand; removes neighbors of complement.

        EXAMPLES::

            sage: import numpy as np
            sage: if int(np.version.short_version[0]) > 1:
            ....:     _ = np.set_printoptions(legacy="1.25")
            sage: from sage.schemes.elliptic_curves.period_lattice_region import PeriodicRegion
            sage: data = np.zeros((10, 10))
            sage: data[1:4,1:4] = True
            sage: S = PeriodicRegion(CDF(1), CDF(I + 1/2), data)
            sage: S.plot()                                                              # needs sage.plot
            Graphics object consisting of 13 graphics primitives
            sage: S.contract().plot()                                                   # needs sage.plot
            Graphics object consisting of 5 graphics primitives
            sage: S.contract().data.sum()
            1
            sage: S.contract().contract().is_empty()
            True'''
    @overload
    def ds(self) -> Any:
        """PeriodicRegion.ds(self)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/period_lattice_region.pyx (starting at line 127)

        Return the sides of each parallelogram tile.

        EXAMPLES::

            sage: import numpy as np
            sage: from sage.schemes.elliptic_curves.period_lattice_region import PeriodicRegion
            sage: data = np.zeros((4, 4))
            sage: S = PeriodicRegion(CDF(2), CDF(2*I), data, full=False)
            sage: S.ds()
            (0.5, 0.25*I)
            sage: _ = S._ensure_full()
            sage: S.ds()
            (0.5, 0.25*I)

            sage: data = np.zeros((8, 8))
            sage: S = PeriodicRegion(CDF(1), CDF(I + 1/2), data)
            sage: S.ds()
            (0.125, 0.0625 + 0.125*I)"""
    @overload
    def ds(self) -> Any:
        """PeriodicRegion.ds(self)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/period_lattice_region.pyx (starting at line 127)

        Return the sides of each parallelogram tile.

        EXAMPLES::

            sage: import numpy as np
            sage: from sage.schemes.elliptic_curves.period_lattice_region import PeriodicRegion
            sage: data = np.zeros((4, 4))
            sage: S = PeriodicRegion(CDF(2), CDF(2*I), data, full=False)
            sage: S.ds()
            (0.5, 0.25*I)
            sage: _ = S._ensure_full()
            sage: S.ds()
            (0.5, 0.25*I)

            sage: data = np.zeros((8, 8))
            sage: S = PeriodicRegion(CDF(1), CDF(I + 1/2), data)
            sage: S.ds()
            (0.125, 0.0625 + 0.125*I)"""
    @overload
    def ds(self) -> Any:
        """PeriodicRegion.ds(self)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/period_lattice_region.pyx (starting at line 127)

        Return the sides of each parallelogram tile.

        EXAMPLES::

            sage: import numpy as np
            sage: from sage.schemes.elliptic_curves.period_lattice_region import PeriodicRegion
            sage: data = np.zeros((4, 4))
            sage: S = PeriodicRegion(CDF(2), CDF(2*I), data, full=False)
            sage: S.ds()
            (0.5, 0.25*I)
            sage: _ = S._ensure_full()
            sage: S.ds()
            (0.5, 0.25*I)

            sage: data = np.zeros((8, 8))
            sage: S = PeriodicRegion(CDF(1), CDF(I + 1/2), data)
            sage: S.ds()
            (0.125, 0.0625 + 0.125*I)"""
    @overload
    def ds(self) -> Any:
        """PeriodicRegion.ds(self)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/period_lattice_region.pyx (starting at line 127)

        Return the sides of each parallelogram tile.

        EXAMPLES::

            sage: import numpy as np
            sage: from sage.schemes.elliptic_curves.period_lattice_region import PeriodicRegion
            sage: data = np.zeros((4, 4))
            sage: S = PeriodicRegion(CDF(2), CDF(2*I), data, full=False)
            sage: S.ds()
            (0.5, 0.25*I)
            sage: _ = S._ensure_full()
            sage: S.ds()
            (0.5, 0.25*I)

            sage: data = np.zeros((8, 8))
            sage: S = PeriodicRegion(CDF(1), CDF(I + 1/2), data)
            sage: S.ds()
            (0.125, 0.0625 + 0.125*I)"""
    @overload
    def expand(self, boolcorners=...) -> Any:
        """PeriodicRegion.expand(self, bool corners=True)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/period_lattice_region.pyx (starting at line 242)

        Return a region containing this region by adding all neighbors of
        internal tiles.

        EXAMPLES::

            sage: import numpy as np
            sage: from sage.schemes.elliptic_curves.period_lattice_region import PeriodicRegion
            sage: data = np.zeros((4, 4))
            sage: data[1,1] = True
            sage: S = PeriodicRegion(CDF(1), CDF(I + 1/2), data)
            sage: S.plot()                                                              # needs sage.plot
            Graphics object consisting of 5 graphics primitives
            sage: S.expand().plot()                                                     # needs sage.plot
            Graphics object consisting of 13 graphics primitives
            sage: S.expand().data
            array([[1, 1, 1, 0],
                   [1, 1, 1, 0],
                   [1, 1, 1, 0],
                   [0, 0, 0, 0]], dtype=int8)
            sage: S.expand(corners=False).plot()                                        # needs sage.plot
            Graphics object consisting of 13 graphics primitives
            sage: S.expand(corners=False).data
            array([[0, 1, 0, 0],
                   [1, 1, 1, 0],
                   [0, 1, 0, 0],
                   [0, 0, 0, 0]], dtype=int8)"""
    @overload
    def expand(self) -> Any:
        """PeriodicRegion.expand(self, bool corners=True)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/period_lattice_region.pyx (starting at line 242)

        Return a region containing this region by adding all neighbors of
        internal tiles.

        EXAMPLES::

            sage: import numpy as np
            sage: from sage.schemes.elliptic_curves.period_lattice_region import PeriodicRegion
            sage: data = np.zeros((4, 4))
            sage: data[1,1] = True
            sage: S = PeriodicRegion(CDF(1), CDF(I + 1/2), data)
            sage: S.plot()                                                              # needs sage.plot
            Graphics object consisting of 5 graphics primitives
            sage: S.expand().plot()                                                     # needs sage.plot
            Graphics object consisting of 13 graphics primitives
            sage: S.expand().data
            array([[1, 1, 1, 0],
                   [1, 1, 1, 0],
                   [1, 1, 1, 0],
                   [0, 0, 0, 0]], dtype=int8)
            sage: S.expand(corners=False).plot()                                        # needs sage.plot
            Graphics object consisting of 13 graphics primitives
            sage: S.expand(corners=False).data
            array([[0, 1, 0, 0],
                   [1, 1, 1, 0],
                   [0, 1, 0, 0],
                   [0, 0, 0, 0]], dtype=int8)"""
    @overload
    def expand(self) -> Any:
        """PeriodicRegion.expand(self, bool corners=True)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/period_lattice_region.pyx (starting at line 242)

        Return a region containing this region by adding all neighbors of
        internal tiles.

        EXAMPLES::

            sage: import numpy as np
            sage: from sage.schemes.elliptic_curves.period_lattice_region import PeriodicRegion
            sage: data = np.zeros((4, 4))
            sage: data[1,1] = True
            sage: S = PeriodicRegion(CDF(1), CDF(I + 1/2), data)
            sage: S.plot()                                                              # needs sage.plot
            Graphics object consisting of 5 graphics primitives
            sage: S.expand().plot()                                                     # needs sage.plot
            Graphics object consisting of 13 graphics primitives
            sage: S.expand().data
            array([[1, 1, 1, 0],
                   [1, 1, 1, 0],
                   [1, 1, 1, 0],
                   [0, 0, 0, 0]], dtype=int8)
            sage: S.expand(corners=False).plot()                                        # needs sage.plot
            Graphics object consisting of 13 graphics primitives
            sage: S.expand(corners=False).data
            array([[0, 1, 0, 0],
                   [1, 1, 1, 0],
                   [0, 1, 0, 0],
                   [0, 0, 0, 0]], dtype=int8)"""
    @overload
    def expand(self, corners=...) -> Any:
        """PeriodicRegion.expand(self, bool corners=True)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/period_lattice_region.pyx (starting at line 242)

        Return a region containing this region by adding all neighbors of
        internal tiles.

        EXAMPLES::

            sage: import numpy as np
            sage: from sage.schemes.elliptic_curves.period_lattice_region import PeriodicRegion
            sage: data = np.zeros((4, 4))
            sage: data[1,1] = True
            sage: S = PeriodicRegion(CDF(1), CDF(I + 1/2), data)
            sage: S.plot()                                                              # needs sage.plot
            Graphics object consisting of 5 graphics primitives
            sage: S.expand().plot()                                                     # needs sage.plot
            Graphics object consisting of 13 graphics primitives
            sage: S.expand().data
            array([[1, 1, 1, 0],
                   [1, 1, 1, 0],
                   [1, 1, 1, 0],
                   [0, 0, 0, 0]], dtype=int8)
            sage: S.expand(corners=False).plot()                                        # needs sage.plot
            Graphics object consisting of 13 graphics primitives
            sage: S.expand(corners=False).data
            array([[0, 1, 0, 0],
                   [1, 1, 1, 0],
                   [0, 1, 0, 0],
                   [0, 0, 0, 0]], dtype=int8)"""
    @overload
    def expand(self, corners=...) -> Any:
        """PeriodicRegion.expand(self, bool corners=True)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/period_lattice_region.pyx (starting at line 242)

        Return a region containing this region by adding all neighbors of
        internal tiles.

        EXAMPLES::

            sage: import numpy as np
            sage: from sage.schemes.elliptic_curves.period_lattice_region import PeriodicRegion
            sage: data = np.zeros((4, 4))
            sage: data[1,1] = True
            sage: S = PeriodicRegion(CDF(1), CDF(I + 1/2), data)
            sage: S.plot()                                                              # needs sage.plot
            Graphics object consisting of 5 graphics primitives
            sage: S.expand().plot()                                                     # needs sage.plot
            Graphics object consisting of 13 graphics primitives
            sage: S.expand().data
            array([[1, 1, 1, 0],
                   [1, 1, 1, 0],
                   [1, 1, 1, 0],
                   [0, 0, 0, 0]], dtype=int8)
            sage: S.expand(corners=False).plot()                                        # needs sage.plot
            Graphics object consisting of 13 graphics primitives
            sage: S.expand(corners=False).data
            array([[0, 1, 0, 0],
                   [1, 1, 1, 0],
                   [0, 1, 0, 0],
                   [0, 0, 0, 0]], dtype=int8)"""
    @overload
    def innermost_point(self) -> Any:
        """PeriodicRegion.innermost_point(self)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/period_lattice_region.pyx (starting at line 617)

        Return a point well inside the region, specifically the center of
        (one of) the last tile(s) to be removed on contraction.

        EXAMPLES::

            sage: import numpy as np
            sage: from sage.schemes.elliptic_curves.period_lattice_region import PeriodicRegion
            sage: data = np.zeros((10, 10))
            sage: data[1:4, 1:4] = True
            sage: data[1, 0:8] = True
            sage: S = PeriodicRegion(CDF(1), CDF(I+1/2), data)
            sage: S.innermost_point()
            0.375 + 0.25*I
            sage: S.plot() + point(S.innermost_point())                                 # needs sage.plot
            Graphics object consisting of 24 graphics primitives"""
    @overload
    def innermost_point(self) -> Any:
        """PeriodicRegion.innermost_point(self)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/period_lattice_region.pyx (starting at line 617)

        Return a point well inside the region, specifically the center of
        (one of) the last tile(s) to be removed on contraction.

        EXAMPLES::

            sage: import numpy as np
            sage: from sage.schemes.elliptic_curves.period_lattice_region import PeriodicRegion
            sage: data = np.zeros((10, 10))
            sage: data[1:4, 1:4] = True
            sage: data[1, 0:8] = True
            sage: S = PeriodicRegion(CDF(1), CDF(I+1/2), data)
            sage: S.innermost_point()
            0.375 + 0.25*I
            sage: S.plot() + point(S.innermost_point())                                 # needs sage.plot
            Graphics object consisting of 24 graphics primitives"""
    @overload
    def innermost_point(self) -> Any:
        """PeriodicRegion.innermost_point(self)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/period_lattice_region.pyx (starting at line 617)

        Return a point well inside the region, specifically the center of
        (one of) the last tile(s) to be removed on contraction.

        EXAMPLES::

            sage: import numpy as np
            sage: from sage.schemes.elliptic_curves.period_lattice_region import PeriodicRegion
            sage: data = np.zeros((10, 10))
            sage: data[1:4, 1:4] = True
            sage: data[1, 0:8] = True
            sage: S = PeriodicRegion(CDF(1), CDF(I+1/2), data)
            sage: S.innermost_point()
            0.375 + 0.25*I
            sage: S.plot() + point(S.innermost_point())                                 # needs sage.plot
            Graphics object consisting of 24 graphics primitives"""
    @overload
    def is_empty(self) -> Any:
        '''PeriodicRegion.is_empty(self)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/period_lattice_region.pyx (starting at line 73)

        Return whether this region is empty.

        EXAMPLES::

            sage: import numpy as np
            sage: if int(np.version.short_version[0]) > 1:
            ....:     _ = np.set_printoptions(legacy="1.25")
            sage: from sage.schemes.elliptic_curves.period_lattice_region import PeriodicRegion
            sage: data = np.zeros((4, 4))
            sage: PeriodicRegion(CDF(2), CDF(2*I), data).is_empty()
            True
            sage: data[1,1] = True
            sage: PeriodicRegion(CDF(2), CDF(2*I), data).is_empty()
            False'''
    @overload
    def is_empty(self) -> Any:
        '''PeriodicRegion.is_empty(self)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/period_lattice_region.pyx (starting at line 73)

        Return whether this region is empty.

        EXAMPLES::

            sage: import numpy as np
            sage: if int(np.version.short_version[0]) > 1:
            ....:     _ = np.set_printoptions(legacy="1.25")
            sage: from sage.schemes.elliptic_curves.period_lattice_region import PeriodicRegion
            sage: data = np.zeros((4, 4))
            sage: PeriodicRegion(CDF(2), CDF(2*I), data).is_empty()
            True
            sage: data[1,1] = True
            sage: PeriodicRegion(CDF(2), CDF(2*I), data).is_empty()
            False'''
    @overload
    def is_empty(self) -> Any:
        '''PeriodicRegion.is_empty(self)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/period_lattice_region.pyx (starting at line 73)

        Return whether this region is empty.

        EXAMPLES::

            sage: import numpy as np
            sage: if int(np.version.short_version[0]) > 1:
            ....:     _ = np.set_printoptions(legacy="1.25")
            sage: from sage.schemes.elliptic_curves.period_lattice_region import PeriodicRegion
            sage: data = np.zeros((4, 4))
            sage: PeriodicRegion(CDF(2), CDF(2*I), data).is_empty()
            True
            sage: data[1,1] = True
            sage: PeriodicRegion(CDF(2), CDF(2*I), data).is_empty()
            False'''
    def plot(self, **kwds) -> Any:
        """PeriodicRegion.plot(self, **kwds)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/period_lattice_region.pyx (starting at line 645)

        Plot this region in the fundamental lattice.  If ``full`` is ``False``, plots
        only the lower half.  Note that the true nature of this region is periodic.

        EXAMPLES::

            sage: import numpy as np
            sage: from sage.schemes.elliptic_curves.period_lattice_region import PeriodicRegion
            sage: data = np.zeros((10, 10))
            sage: data[2, 2:8] = True
            sage: data[2:5, 2] = True
            sage: data[3, 3] = True
            sage: S = PeriodicRegion(CDF(1), CDF(I + 1/2), data)
            sage: plot(S) + plot(S.expand(), rgbcolor=(1, 0, 1), thickness=2)           # needs sage.plot
            Graphics object consisting of 46 graphics primitives"""
    @overload
    def refine(self, condition=..., inttimes=...) -> Any:
        """PeriodicRegion.refine(self, condition=None, int times=1)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/period_lattice_region.pyx (starting at line 186)

        Recursive function to refine the current tiling.

        INPUT:

        - ``condition`` -- function (default: ``None``); if not ``None``, only
          keep tiles in the refinement which satisfy the condition

        - ``times`` -- integer (default: 1); the number of times to refine.
          Each refinement step halves the mesh size.

        OUTPUT: the refined PeriodicRegion

        EXAMPLES::

            sage: import numpy as np
            sage: from sage.schemes.elliptic_curves.period_lattice_region import PeriodicRegion
            sage: data = np.zeros((4, 4))
            sage: S = PeriodicRegion(CDF(2), CDF(2*I), data, full=False)
            sage: S.ds()
            (0.5, 0.25*I)
            sage: S = S.refine()
            sage: S.ds()
            (0.25, 0.125*I)
            sage: S = S.refine(2)
            sage: S.ds()
            (0.125, 0.0625*I)"""
    @overload
    def refine(self) -> Any:
        """PeriodicRegion.refine(self, condition=None, int times=1)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/period_lattice_region.pyx (starting at line 186)

        Recursive function to refine the current tiling.

        INPUT:

        - ``condition`` -- function (default: ``None``); if not ``None``, only
          keep tiles in the refinement which satisfy the condition

        - ``times`` -- integer (default: 1); the number of times to refine.
          Each refinement step halves the mesh size.

        OUTPUT: the refined PeriodicRegion

        EXAMPLES::

            sage: import numpy as np
            sage: from sage.schemes.elliptic_curves.period_lattice_region import PeriodicRegion
            sage: data = np.zeros((4, 4))
            sage: S = PeriodicRegion(CDF(2), CDF(2*I), data, full=False)
            sage: S.ds()
            (0.5, 0.25*I)
            sage: S = S.refine()
            sage: S.ds()
            (0.25, 0.125*I)
            sage: S = S.refine(2)
            sage: S.ds()
            (0.125, 0.0625*I)"""
    def verify(self, condition) -> Any:
        """PeriodicRegion.verify(self, condition)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/period_lattice_region.pyx (starting at line 151)

        Given a condition that should hold for every line segment on
        the boundary, verify that it actually does so.

        INPUT:

        - ``condition`` -- boolean-valued function on `\\CC`

        OUTPUT:

        boolean according to whether the condition holds for all lines on the
        boundary.

        EXAMPLES::

            sage: import numpy as np
            sage: from sage.schemes.elliptic_curves.period_lattice_region import PeriodicRegion
            sage: data = np.zeros((4, 4))
            sage: data[1, 1] = True
            sage: S = PeriodicRegion(CDF(1), CDF(I), data)
            sage: S.border()
            [(1, 1, 0), (2, 1, 0), (1, 1, 1), (1, 2, 1)]
            sage: condition = lambda z: z.real().abs()<1/2
            sage: S.verify(condition)
            False
            sage: condition = lambda z: z.real().abs()<1
            sage: S.verify(condition)
            True"""
    def __and__(self, left, right) -> Any:
        """PeriodicRegion.__and__(left, right)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/period_lattice_region.pyx (starting at line 466)

        Return the intersection of ``left`` and ``right``.

        EXAMPLES::

            sage: import numpy as np
            sage: from sage.schemes.elliptic_curves.period_lattice_region import PeriodicRegion
            sage: data = np.zeros((4, 4))
            sage: data[1, 1:3] = True
            sage: S1 = PeriodicRegion(CDF(1), CDF(I), data)
            sage: data = np.zeros((4, 4))
            sage: data[1:3, 1] = True
            sage: S2 = PeriodicRegion(CDF(1), CDF(I), data)
            sage: (S1 & S2).data
            array([[0, 0, 0, 0],
                   [0, 1, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0]], dtype=int8)"""
    def __contains__(self, z) -> Any:
        '''PeriodicRegion.__contains__(self, z)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/period_lattice_region.pyx (starting at line 315)

        Return whether this region contains the given point.

        EXAMPLES::

            sage: import numpy as np
            sage: if int(np.version.short_version[0]) > 1:
            ....:     _ = np.set_printoptions(legacy="1.25")
            sage: from sage.schemes.elliptic_curves.period_lattice_region import PeriodicRegion
            sage: data = np.zeros((4, 4))
            sage: data[1,1] = True
            sage: S = PeriodicRegion(CDF(2), CDF(2*I), data, full=False)
            sage: CDF(0, 0) in S
            False
            sage: CDF(0.6, 0.6) in S
            True
            sage: CDF(1.6, 0.6) in S
            False
            sage: CDF(6.6, 4.6) in S
            True
            sage: CDF(6.6, -1.4) in S
            True

            sage: w1 = CDF(1.4)
            sage: w2 = CDF(1.2 * I - .3)
            sage: S = PeriodicRegion(w1, w2, data)
            sage: z = w1/2 + w2/2; z in S
            False
            sage: z = w1/3 + w2/3; z in S
            True
            sage: z = w1/3 + w2/3 + 5*w1 - 6*w2; z in S
            True'''
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __invert__(self) -> Any:
        """PeriodicRegion.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/period_lattice_region.pyx (starting at line 444)

        Return the complement of this region.

        EXAMPLES::

            sage: import numpy as np
            sage: from sage.schemes.elliptic_curves.period_lattice_region import PeriodicRegion
            sage: data = np.zeros((4, 4))
            sage: data[1,1] = True
            sage: S = PeriodicRegion(CDF(1), CDF(I), data)
            sage: .3 + .3j in S
            True
            sage: .3 + .3j in ~S
            False
            sage: 0 in S
            False
            sage: 0 in ~S
            True"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __rand__(self, other):
        """Return value&self."""
    def __rtruediv__(self, other):
        """Return value/self."""
    def __rxor__(self, other):
        """Return value^self."""
    def __truediv__(self, unsignedintn) -> Any:
        '''PeriodicRegion.__truediv__(self, unsigned int n)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/period_lattice_region.pyx (starting at line 366)

        Return a new region of the same resolution that is the image
        of this region under the map z -> z/n.

        The resolution is the same, so some detail may be lost.  The result is
        always at worse a superset of the true image.

        EXAMPLES::

            sage: import numpy as np
            sage: if int(np.version.short_version[0]) > 1:
            ....:     _ = np.set_printoptions(legacy="1.25")
            sage: from sage.schemes.elliptic_curves.period_lattice_region import PeriodicRegion

            sage: data = np.zeros((20, 20))
            sage: data[2, 2:12] = True
            sage: data[2:6, 2] = True
            sage: data[3, 3] = True
            sage: S = PeriodicRegion(CDF(1), CDF(I + 1/2), data)
            sage: S.plot()                                                              # needs sage.plot
            Graphics object consisting of 29 graphics primitives
            sage: (S / 2).plot()                                                        # needs sage.plot
            Graphics object consisting of 57 graphics primitives
            sage: (S / 3).plot()                                                        # needs sage.plot
            Graphics object consisting of 109 graphics primitives
            sage: (S / 2 / 3) == (S / 6) == (S / 3 / 2)
            True

            sage: data = np.zeros((100, 100))
            sage: data[2, 3] = True
            sage: data[7, 9] = True
            sage: S = PeriodicRegion(CDF(1), CDF(I), data)
            sage: inside = [.025 + .035j, .075 + .095j]
            sage: all(z in S for z in inside)
            True
            sage: all(z/2 + j/2 + k/2 in S/2 for z in inside for j in range(2) for k in range(2))
            True
            sage: all(z/3 + j/3 + k/3 in S/3 for z in inside for j in range(3) for k in range(3))
            True
            sage: outside = [.025 + .095j, .075 + .035j]
            sage: any(z in S for z in outside)
            False
            sage: any(z/2 + j/2 + k/2 in S/2 for z in outside for j in range(2) for k in range(2))
            False
            sage: any(z/3 + j/3 + k/3 in S/3 for z in outside for j in range(3) for k in range(3))
            False

            sage: (S / 1) is S
            True
            sage: S / 0
            Traceback (most recent call last):
            ...
            ValueError: divisor must be positive
            sage: S / (-1)
            Traceback (most recent call last):
            ...
            OverflowError: can...t convert negative value to unsigned int'''
    def __xor__(self, left, right) -> Any:
        """PeriodicRegion.__xor__(left, right)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/period_lattice_region.pyx (starting at line 493)

        Return the union of ``left`` and ``right`` minus the intersection of
        ``left`` and ``right``.

        EXAMPLES::

            sage: import numpy as np
            sage: from sage.schemes.elliptic_curves.period_lattice_region import PeriodicRegion
            sage: data = np.zeros((4, 4))
            sage: data[1, 1:3] = True
            sage: S1 = PeriodicRegion(CDF(1), CDF(I), data)
            sage: data = np.zeros((4, 4))
            sage: data[1:3, 1] = True
            sage: S2 = PeriodicRegion(CDF(1), CDF(I), data)
            sage: (S1 ^^ S2).data
            array([[0, 0, 0, 0],
                   [0, 0, 1, 0],
                   [0, 1, 0, 0],
                   [0, 0, 0, 0]], dtype=int8)"""
