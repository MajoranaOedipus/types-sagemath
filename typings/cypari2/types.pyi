"""
Declarations for types used by PARI

This includes both the C types as well as the PARI types (and a few
macros for dealing with those).

It is important that the functionality in this file does not call any
PARI library functions. The reason is that we want to allow just using
these types (for example, to define a Cython extension type) without
linking to PARI. This file should consist only of typedefs and macros
from PARI's include files.
"""
