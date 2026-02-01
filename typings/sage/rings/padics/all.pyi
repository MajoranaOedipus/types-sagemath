from sage.rings.padics.factory import (
    Qp as Qp, QpCR as QpCR, QpER as QpER, QpFP as QpFP, 
    QpLC as QpLC, QpLF as QpLF, Qq as Qq, QqCR as QqCR, 
    QqFP as QqFP, Zp as Zp, ZpCA as ZpCA, ZpCR as ZpCR, 
    ZpER as ZpER, ZpFM as ZpFM, ZpFP as ZpFP, ZpLC as ZpLC, 
    ZpLF as ZpLF, Zq as Zq, ZqCA as ZqCA, ZqCR as ZqCR, 
    ZqFM as ZqFM, ZqFP as ZqFP, pAdicExtension as pAdicExtension)
from sage.rings.padics.padic_generic import local_print_mode as local_print_mode
from sage.rings.padics.pow_computer import PowComputer as PowComputer
from sage.rings.padics.pow_computer_ext import PowComputer_ext_maker as PowComputer_ext_maker
from sage.rings.padics.witt_vector_ring import WittVectorRing as WittVectorRing

pAdicField = Qp
pAdicRing = Zp