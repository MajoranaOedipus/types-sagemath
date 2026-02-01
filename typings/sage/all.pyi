"""
all.py -- much of sage is imported into this module, so you don't
          have to import everything individually.

TESTS:

This is to test :issue:`10570`. If the number of stackframes at startup
changes due to a patch you made, please check that this was an
intended effect of your patch.

::

    sage: import gc
    sage: import inspect
    sage: from sage import *
    sage: frames = [x for x in gc.get_objects() if inspect.isframe(x)]

We exclude the dependencies and check to see that there are no others
except for the known bad apples::

    sage: allowed = [
    ....:     'IPython', 'prompt_toolkit', 'jedi',     # sage dependencies
    ....:     'threading', 'multiprocessing',  # doctest dependencies
    ....:     'pytz', 'importlib.resources',   # doctest dependencies
    ....:     '__main__', 'sage.doctest',      # doctesting
    ....:     'signal', 'enum', 'types'        # may appear in Python 3
    ....: ]
    sage: def is_not_allowed(frame):
    ....:     module = inspect.getmodule(frame)
    ....:     if module is None: return False
    ....:     return not any(module.__name__.startswith(name)
    ....:                    for name in allowed)
    sage: [inspect.getmodule(f).__name__ for f in frames if is_not_allowed(f)]
    []

Check lazy import of ``interacts``::

    sage: type(interacts)
    <class 'sage.misc.lazy_import.LazyImport'>
    sage: interacts
    <module 'sage.interacts.all' from '...'>

Check that :issue:`34506` is resolved::

    sage: x = int('1'*4301)
"""

from typing import Literal
import os as os
import operator as operator
import math as math
import sys as sys
import warnings as warnings
import sage as sage

deprecationWarning: tuple[str, None, type[DeprecationWarning], None, Literal[0]]

from cysignals.signals import (
    AlarmInterrupt as AlarmInterrupt, 
    SignalError as SignalError,
    sig_on_reset)
sig_on_count = sig_on_reset
from time import sleep as sleep
from sage.structure.all import *
from sage.arith.power import generic_power
power = generic_power

from sage.cpython.all import *

from copy import (
    copy as copy, 
    deepcopy as deepcopy
)

from sage.env import (
    SAGE_ROOT as SAGE_ROOT,
    SAGE_SRC as SAGE_SRC,
    SAGE_DOC_SRC as SAGE_DOC_SRC,
    SAGE_LOCAL as SAGE_LOCAL,
    DOT_SAGE as DOT_SAGE,
    SAGE_ENV as SAGE_ENV,
)

from sage.misc.all import *

from sage.doctest.all import *
from sage.repl.all import *

from functools import reduce as reduce

from sage.misc.all import *
from sage.typeset.all import *

from sage.misc.sh import sh as sh

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
import sage.crypto.mq as _mq
mq = _mq

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
import sage.stats.all as _stats
stats = _stats

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
    from cysignals.alarm import alarm as alarm, cancel_alarm as cancel_alarm

from sage.interacts import all as _interacts
interacts = _interacts

CC = ComplexField()
QQ = RationalField()
RR = RealField()
ZZ = IntegerRing()

true = True
false = False
oo = infinity
from sage.rings.imaginary_unit import I as I
i = I

from sage.misc.copying import license as license
copying = license
copyright = license

from sage.misc.persist import register_unpickle_override as register_unpickle_override

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
