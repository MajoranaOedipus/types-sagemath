import sage.libs.ntl.all
ntl = sage.libs.ntl.all

from sage.libs.pari.all import (
    pari as pari, 
    pari_gen as pari_gen, 
    PariError as PariError
)

import sage.libs.symmetrica.all
symmetrica = sage.libs.symmetrica.all

from sage.libs.gap.libgap import libgap as libgap

from sage.libs.eclib.constructor import CremonaModularSymbols as CremonaModularSymbols
from sage.libs.eclib.interface import (
    mwrank_EllipticCurve as mwrank_EllipticCurve, 
    mwrank_MordellWeil as mwrank_MordellWeil
)
from sage.libs.eclib.mwrank import get_precision
mwrank_get_precision = get_precision
from sage.libs.eclib.mwrank import set_precision
mwrank_set_precision = set_precision
from sage.libs.eclib.mwrank import initprimes
mwrank_initprimes = initprimes

from sage.libs.flint.qsieve_sage import qsieve as qsieve

from sage.libs.giac.giac import libgiac as libgiac