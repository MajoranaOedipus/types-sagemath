r"""
Interface to Groebner Fan

AUTHOR:

- Anders Nedergaard Jensen: Write gfan C++ program, which implements
  algorithms many of which were invented by Jensen, Komei
  Fukuda, and Rekha Thomas.
- William Stein (2006-03-18): wrote gfan interface (first version)
- Marshall Hampton (2008-03-17): modified to use gfan-0.3, subprocess instead of os.popen2

TODO -- much functionality of gfan-0.3 is still not exposed::

   * at most 52 variables:

       - use gfan_substitute to make easier (?)
       MH: I think this is now irrelevant since gfan can accept the original ring variables

   * --symmetry is really useful
            - permutations are 0-based *not* cycle notation; a <---> 0
     output is broken up much more nicely.

   * -- can work in Z/pZ for p <= 32749

   * -- can compute individual GB's for lex and revlex (via buchberger)
"""
from sage.features.gfan import GfanExecutable as GfanExecutable
from sage.misc.decorators import rename_keyword as rename_keyword

class Gfan:
    """
    Interface to Anders Jensen's Groebner Fan program.
    """
    def __call__(self, input, cmd: str = '', verbose: bool = False, format=None):
        """
        Call Groebner Fan program with given input.

        INPUT:

        - ``input`` -- string; input
        - ``cmd`` -- string (default: ``''``); GFan command
        - ``verbose`` -- boolean (default: ``False``)

        EXAMPLES::

            sage: print(gfan('Q[x,y]{x^2-y-1,y^2-xy-2/3}', cmd='bases'))                # needs gfan
            Q[x,y]
            {{
            y^4+4/9-7/3*y^2-y^3,
            x+5/2*y+3/2*y^2-3/2*y^3}
            ,
            {
            x^2-1-y,
            x*y+2/3-y^2,
            y^3-5/3*y-y^2-2/3*x}
            ,
            {
            x^2-1-y,
            y^2-2/3-x*y}
            ,
            {
            x^4+1/3+x-2*x^2-x^3,
            y+1-x^2}
            }

        TESTS::

            sage: _ = gfan(I='Q[x,y]{x^2-y-1,y^2-xy-2/3}', cmd='bases')                 # needs gfan
            doctest:...:
            DeprecationWarning: use the option 'input' instead of 'I'
            See https://github.com/sagemath/sage/issues/33468 for details.
        """

gfan: Gfan
