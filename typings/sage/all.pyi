import os
import operator
import math
import sys

from cysignals.signals import (AlarmInterrupt, SignalError,
                               sig_on_reset as sig_on_count)

from time import sleep as sleep
from sage.structure.all import *
from sage.arith.power import generic_power as power

from sage.cpython.all import *

from copy import copy, deepcopy

true = True
false = False

from sage.env import SAGE_ROOT, SAGE_SRC, SAGE_DOC_SRC, SAGE_LOCAL, DOT_SAGE, SAGE_ENV

from sage.misc.all import *

from sage.doctest.all import *
from sage.repl.all import *

from functools import reduce  # in order to keep reduce in python3

import sage.misc.lazy_import

from sage.misc.all import *         # takes a while
from sage.typeset.all import *

from sage.misc.sh import sh

from sage.libs.all import *
from sage.data_structures.all import *

from sage.structure.all import *
from sage.rings.all import *
from sage.arith.all import *
from sage.matrix.all import *

from sage.symbolic.all import *
from sage.modules.all import *
from sage.monoids.all import *
from sage.algebras.all import *
from sage.modular.all import *
from sage.sat.all import *
from sage.schemes.all import *
from sage.graphs.all import *
from sage.groups.all import *
from sage.databases.all import *
from sage.categories.all import *
from sage.sets.all import *
from sage.probability.all import *
from sage.interfaces.all import *

from sage.functions.all import *
from sage.calculus.all import *

from sage.cpython.all import *

from sage.crypto.all import *
import sage.crypto.mq as mq

from sage.plot.all import *
from sage.plot.plot3d.all import *

from sage.coding.all import *
from sage.combinat.all import *

from sage.lfunctions.all import *

from sage.geometry.all import *
from sage.geometry.triangulation.all import *
from sage.geometry.riemannian_manifolds.all import *

from sage.dynamics.all import *

from sage.homology.all import *

from sage.topology.all import *

from sage.quadratic_forms.all import *

from sage.games.all import *

from sage.logic.all import *

from sage.numerical.all import *

from sage.stats.all import *
import sage.stats.all as stats

from sage.parallel.all import *

from sage.ext.fast_callable import fast_callable as fast_callable
from sage.ext.fast_eval import fast_float as fast_float

from sage.sandpiles.all import *

from sage.tensor.all import *

from sage.matroids.all import *

from sage.game_theory.all import *

from sage.knots.all import *

from sage.manifolds.all import *

if sys.platform != 'win32':
    from cysignals.alarm import alarm, cancel_alarm

from sage.interacts import all as interacts

CC = ComplexField()
QQ = RationalField()
RR = RealField()
ZZ = IntegerRing()

true = True
false = False
oo = infinity
from sage.rings.imaginary_unit import I
i = I

from sage.misc.copying import license
copying = license
copyright = license

from sage.misc.persist import register_unpickle_override

def sage_globals():
    r"""
    Return the Sage namespace.

    EXAMPLES::

        sage: 'log' in sage_globals()
        True
        sage: 'MatrixSpace' in sage_globals()
        True
        sage: 'Permutations' in sage_globals()
        True
        sage: 'TheWholeUniverse' in sage_globals()
        False
    """

