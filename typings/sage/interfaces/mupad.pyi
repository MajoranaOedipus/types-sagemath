r"""
Interface to MuPAD

AUTHOR:

- Mike Hansen
- William Stein

You must have the optional commercial MuPAD interpreter installed and
available as the command \code{mupkern} in your PATH in order to use
this interface.  You do not have to install any optional \sage
packages.

TESTS::

    sage: # optional - mupad
    sage: mupad.package('"MuPAD-Combinat"')
    sage: combinat = mupad.combinat
    sage: examples = mupad.examples
    sage: S = examples.SymmetricFunctions()
    sage: S.s[2,1]^2
    s[3, 3] + s[4, 2] + s[2, 2, 1, 1] + s[2, 2, 2] + 2 s[3, 2, 1] + s[4, 1, 1] +
    s[3, 1, 1, 1]
    sage: S.omega( S.s[3] )
    s[1, 1, 1]
    sage: s = S.s
    sage: p = S.p
    sage: s(s[2,1] + p[2,1])
    s[2, 1] + s[3] - s[1, 1, 1]
    sage: s(_)
    s[2, 1] + s[3] - s[1, 1, 1]

    sage: # optional - mupad
    sage: combinat.tableaux.list(3)
                --                                      +---+ --
                |                                       | 3 |  |
                |                 +---+      +---+      +---+  |
                |                 | 3 |      | 2 |      | 2 |  |
                |  +---+---+---+  +---+---+  +---+---+  +---+  |
                |  | 1 | 2 | 3 |, | 1 | 2 |, | 1 | 3 |, | 1 |  |
                -- +---+---+---+  +---+---+  +---+---+  +---+ --
    sage: three = mupad(3)
    sage: three.combinat.tableaux.list()
                --                                      +---+ --
                |                                       | 3 |  |
                |                 +---+      +---+      +---+  |
                |                 | 3 |      | 2 |      | 2 |  |
                |  +---+---+---+  +---+---+  +---+---+  +---+  |
                |  | 1 | 2 | 3 |, | 1 | 2 |, | 1 | 3 |, | 1 |  |
                -- +---+---+---+  +---+---+  +---+---+  +---+ --
    sage: t = _[1]
    sage: t
                                 +---+---+---+
                                 | 1 | 2 | 3 |
                                 +---+---+---+
    sage: combinat.tableaux.conjugate(t)
                                     +---+
                                     | 3 |
                                     +---+
                                     | 2 |
                                     +---+
                                     | 1 |
                                     +---+

    sage: # optional - mupad
    sage: combinat.ribbonsTableaux.list([2,2],[1,1],2)
                           -- +---+---+  +---+---+ --
                           |  |   | 2 |  |     2 |  |
                           |  +   +   +, +---+---+  |
                           |  | 1 |   |  | 1     |  |
                           -- +---+---+  +---+---+ --
    sage: combinat.tableaux.kAtom([2,1],3)
                                  -- +---+     --
                                  |  | 2 |      |
                                  |  +---+---+  |
                                  |  | 1 | 1 |  |
                                  -- +---+---+ --
    sage: M = S.Macdonald()
    sage: a = M.P[1]^2
    sage: mupad.mapcoeffs(a, 'normal')
                                 q - t + q t - 1
                          P[2] + --------------- P[1, 1]
                                     q t - 1
"""
from .expect import Expect as Expect, ExpectElement as ExpectElement, ExpectFunction as ExpectFunction, FunctionElement as FunctionElement
from sage.env import DOT_SAGE as DOT_SAGE
from sage.interfaces.interface import AsciiArtString as AsciiArtString
from sage.interfaces.tab_completion import ExtraTabCompletion as ExtraTabCompletion
from sage.misc.instancedoc import instancedoc as instancedoc

COMMANDS_CACHE: str
PROMPT: str
seq: int

class Mupad(ExtraTabCompletion, Expect):
    """
    Interface to the MuPAD interpreter.
    """
    def __init__(self, maxread=None, script_subdirectory=None, server=None, server_tmpdir=None, logfile=None) -> None:
        """
        Create an instance of the MuPAD interpreter.

        EXAMPLES::

            sage: mupad == loads(dumps(mupad))                      # optional - mupad
            True
        """
    def __reduce__(self):
        """
        EXAMPLES::

            sage: Mupad().__reduce__()
            (<function reduce_load_mupad at 0x...>, ())
        """
    def expect(self):
        """
        EXAMPLES::

            sage: a = mupad(1)   # optional - mupad
            sage: mupad.expect() # optional - mupad
            <pexpect.spawn instance at 0x...>
        """
    def console(self) -> None:
        """
        Spawn a new MuPAD command-line session.

        EXAMPLES::

            sage: mupad.console() #not tested

               *----*    MuPAD Pro 4.0.2 -- The Open Computer Algebra System
              /|   /|
             *----* |    Copyright (c)  1997 - 2007  by SciFace Software
             | *--|-*                   All rights reserved.
             |/   |/
             *----*      Licensed to:   ...
        """
    def eval(self, code, strip: bool = True, **kwds):
        """
        EXAMPLES::

            sage: mupad.eval('2+2')   # optional - mupad
                                                   4
        """
    def cputime(self, t=None):
        """
        EXAMPLES::

            sage: t = mupad.cputime() #random, optional - MuPAD
            0.11600000000000001
        """
    def set(self, var, value) -> None:
        """
        Set the variable var to the given value.

        EXAMPLES::

            sage: mupad.set('a', 4) # optional - mupad
            sage: mupad.get('a').strip() # optional - mupad
            '4'
        """
    def get(self, var):
        """
        Get the value of the variable var.

        EXAMPLES::

            sage: mupad.set('a', 4) # optional - mupad
            sage: mupad.get('a').strip() # optional - mupad
            '4'
        """
    def completions(self, string, strip: bool = False):
        """
        EXAMPLES::

            sage: mupad.completions('linal') # optional - mupad
            ['linalg']
        """

class MupadFunction(ExtraTabCompletion, ExpectFunction):
    def __getattr__(self, attrname):
        """
        EXAMPLES::

            sage: mupad.linalg.addRow
            linalg::addRow
        """

class MupadFunctionElement(ExtraTabCompletion, FunctionElement):
    def __getattr__(self, attrname):
        '''
        EXAMPLES::

            sage: # optional - mupad
            sage: mupad.package(\'"MuPAD-Combinat"\')
            sage: combinat = mupad.combinat
            sage: three = mupad(3)
            sage: type(three.combinat)
            <class \'sage.interfaces.mupad.MupadFunctionElement\'>
            sage: tableaux = three.combinat.tableaux
            sage: type(tableaux)
            <class \'sage.interfaces.mupad.MupadFunctionElement\'>
        '''
    def __call__(self, *args):
        '''
        EXAMPLES::

            sage: # optional - mupad
            sage: mupad.package(\'"MuPAD-Combinat"\')
            sage: combinat = mupad.combinat
            sage: examples = mupad.examples
            sage: S = examples.SymmetricFunctions()
            sage: type(S.omega)
            <class \'sage.interfaces.mupad.MupadFunctionElement\'>
            sage: S.omega(S.s[3])
            s[1, 1, 1]
        '''

class MupadElement(ExtraTabCompletion, ExpectElement):
    def __getattr__(self, attrname):
        '''
        EXAMPLES::

            sage: # optional - mupad
            sage: mupad.package(\'"MuPAD-Combinat"\')
            sage: S = mupad.examples.SymmetricFunctions()
            sage: type(S)
            <class \'sage.interfaces.mupad.MupadElement\'>
            sage: S.s
            (examples::SymmetricFunctions(Dom::ExpressionField()))::s

            sage: x = mupad(\'x\')                    # optional - mupad-Combinat
            sage: x.diff(x)                         # optional - mupad-Combinat
                                       1
        '''
    def __len__(self) -> int:
        '''
        The analogue in MuPAD of Python\'s len is the method nops.

        EXAMPLES::

            sage: len(mupad([1,2,3])) # indirect doctest # optional - mupad
            3
            sage: type(len(mupad([1,2,3])))              # optional - mupad
            <... \'int\'>

            sage: len(mupad(4))                          # optional - mupad
            1

        Implementing this is necessary for using MuPAD\'s lists as
        standard containers::

            sage: list(map(ZZ, list(mupad([1,2,3]))))    # optional - mupad
            [1, 2, 3]

            sage: [int(x) for x in mupad([1,2,3]) ]      # optional - mupad
            [1, 2, 3]

            sage: [int(x) for x in mupad("{1,2,3,5}") ]  # optional - mupad
            [1, 2, 3, 5]
        '''

mupad: Mupad

def reduce_load_mupad():
    """
    EXAMPLES::

        sage: from sage.interfaces.mupad import reduce_load_mupad
        sage: reduce_load_mupad()
        Mupad
    """
def mupad_console() -> None:
    """
    Spawn a new MuPAD command-line session.

    EXAMPLES::

        sage: from sage.interfaces.mupad import mupad_console
        sage: mupad_console() #not tested

           *----*    MuPAD Pro 4.0.2 -- The Open Computer Algebra System
          /|   /|
         *----* |    Copyright (c)  1997 - 2007  by SciFace Software
         | *--|-*                   All rights reserved.
         |/   |/
         *----*      Licensed to:   ...
    """
