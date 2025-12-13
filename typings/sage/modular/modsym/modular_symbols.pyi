from _typeshed import Incomplete
from sage.misc.latex import latex as latex
from sage.modular.modsym.apply import apply_to_monomial as apply_to_monomial
from sage.modular.modsym.manin_symbol import ManinSymbol as ManinSymbol
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.richcmp import richcmp as richcmp, richcmp_method as richcmp_method
from sage.structure.sage_object import SageObject as SageObject

X: Incomplete
Y: Incomplete

class ModularSymbol(SageObject):
    """
    The modular symbol `X^i\\cdot Y^{k-2-i}\\cdot \\{\\alpha, \\beta\\}`.
    """
    def __init__(self, space, i, alpha, beta) -> None:
        """
        Initialise a modular symbol.

        INPUT:

        - ``space`` -- space of Manin symbols

        - ``i`` -- integer

        - ``alpha`` -- cusp

        - ``beta`` -- cusp

        EXAMPLES::

            sage: s = ModularSymbols(11).2.modular_symbol_rep()[0][1]; s
            {-1/9, 0}
            sage: type(s)
            <class 'sage.modular.modsym.modular_symbols.ModularSymbol'>
            sage: s = ModularSymbols(11,4).2.modular_symbol_rep()[0][1]; s
            X^2*{-1/7, 0}
        """
    def __getitem__(self, j):
        """
        Given a modular symbols `s = X^i Y^{k-2-i}\\{\\alpha, \\beta\\}`, ``s[0]`` is `\\alpha`
        and ``s[1]`` is `\\beta`.

        EXAMPLES::

            sage: s = ModularSymbols(11).2.modular_symbol_rep()[0][1]; s
            {-1/9, 0}
            sage: s[0]
            -1/9
            sage: s[1]
            0
            sage: s[2]
            Traceback (most recent call last):
            ...
            IndexError: list index out of range
        """
    def __richcmp__(self, other, op):
        """
        Compare ``self`` to ``other``.

        EXAMPLES::

            sage: M = ModularSymbols(11)
            sage: s = M.2.modular_symbol_rep()[0][1]
            sage: t = M.0.modular_symbol_rep()[0][1]
            sage: s, t
            ({-1/9, 0}, {Infinity, 0})
            sage: s < t
            True
            sage: t > s
            True
            sage: s == s
            True
            sage: t == t
            True
        """
    def __hash__(self):
        """
        EXAMPLES::

            sage: s = ModularSymbols(11).2.modular_symbol_rep()[0][1]
            sage: hash(s)  # random
            -7344656798833624820
        """
    def space(self):
        """
        The list of Manin symbols to which this symbol belongs.

        EXAMPLES::

            sage: s = ModularSymbols(11).2.modular_symbol_rep()[0][1]
            sage: s.space()
            Manin Symbol List of weight 2 for Gamma0(11)
        """
    def polynomial_part(self):
        """
        Return the polynomial part of this symbol, i.e. for a symbol of the
        form `X^i Y^{k-2-i}\\{\\alpha, \\beta\\}`, return `X^i Y^{k-2-i}`.

        EXAMPLES::

            sage: s = ModularSymbols(11).2.modular_symbol_rep()[0][1]
            sage: s.polynomial_part()
            1
            sage: s = ModularSymbols(1,28).0.modular_symbol_rep()[0][1]; s
            X^22*Y^4*{0, Infinity}
            sage: s.polynomial_part()
            X^22*Y^4
        """
    def i(self):
        """
        For a symbol of the form `X^i Y^{k-2-i}\\{\\alpha, \\beta\\}`, return `i`.

        EXAMPLES::

            sage: s = ModularSymbols(11).2.modular_symbol_rep()[0][1]
            sage: s.i()
            0
            sage: s = ModularSymbols(1,28).0.modular_symbol_rep()[0][1]; s
            X^22*Y^4*{0, Infinity}
            sage: s.i()
            22
        """
    def weight(self):
        """
        Return the weight of the modular symbols space to which this symbol
        belongs; i.e. for a symbol of the form `X^i Y^{k-2-i}\\{\\alpha,
        \\beta\\}`, return `k`.

        EXAMPLES::

            sage: s = ModularSymbols(1,28).0.modular_symbol_rep()[0][1]
            sage: s.weight()
            28
        """
    def alpha(self):
        """
        For a symbol of the form `X^i Y^{k-2-i}\\{\\alpha, \\beta\\}`, return `\\alpha`.

        EXAMPLES::

            sage: s = ModularSymbols(11,4).1.modular_symbol_rep()[0][1]; s
            X^2*{-1/6, 0}
            sage: s.alpha()
            -1/6
            sage: type(s.alpha())
            <class 'sage.modular.cusps.Cusp'>
        """
    def beta(self):
        """
        For a symbol of the form `X^i Y^{k-2-i}\\{\\alpha, \\beta\\}`, return `\\beta`.

        EXAMPLES::

            sage: s = ModularSymbols(11,4).1.modular_symbol_rep()[0][1]; s
            X^2*{-1/6, 0}
            sage: s.beta()
            0
            sage: type(s.beta())
            <class 'sage.modular.cusps.Cusp'>
        """
    def apply(self, g):
        """
        Act on this symbol by the element `g \\in {\\rm GL}_2(\\QQ)`.

        INPUT:

        - ``g`` -- list ``[a,b,c,d]``, corresponding to the 2x2 matrix
          `\\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix} \\in {\\rm GL}_2(\\QQ)`

        OUTPUT:

        - ``FormalSum`` -- a formal sum `\\sum_i c_i x_i`, where `c_i` are
          scalars and `x_i` are ModularSymbol objects, such that the sum
          `\\sum_i c_i x_i` is the image of this symbol under the action of g.
          No reduction is performed modulo the relations that hold in
          self.space().

        The action of `g` on symbols is by

        .. MATH::

           P(X,Y)\\{\\alpha, \\beta\\} \\mapsto  P(dX-bY, -cx+aY) \\{g(\\alpha), g(\\beta)\\}.

        Note that for us we have `P=X^i Y^{k-2-i}`, which simplifies computation
        of the polynomial part slightly.

        EXAMPLES::

            sage: s = ModularSymbols(11,2).1.modular_symbol_rep()[0][1]; s
            {-1/8, 0}
            sage: a = 1; b = 2; c = 3; d = 4; s.apply([a,b,c,d])
            {15/29, 1/2}
            sage: x = -1/8;  (a*x+b)/(c*x+d)
            15/29
            sage: x = 0;  (a*x+b)/(c*x+d)
            1/2
            sage: s = ModularSymbols(11,4).1.modular_symbol_rep()[0][1]; s
            X^2*{-1/6, 0}
            sage: s.apply([a,b,c,d])
            16*X^2*{11/21, 1/2} - 16*X*Y*{11/21, 1/2} + 4*Y^2*{11/21, 1/2}
            sage: P = s.polynomial_part()
            sage: X, Y = P.parent().gens()
            sage: P(d*X-b*Y, -c*X+a*Y)
            16*X^2 - 16*X*Y + 4*Y^2
            sage: x = -1/6; (a*x+b)/(c*x+d)
            11/21
            sage: x = 0; (a*x+b)/(c*x+d)
            1/2
            sage: type(s.apply([a,b,c,d]))
            <class 'sage.structure.formal_sum.FormalSum'>
        """
    def manin_symbol_rep(self):
        """
        Return a representation of ``self`` as a formal sum of Manin symbols.

        The result is not cached.

        EXAMPLES::

            sage: M = ModularSymbols(11,4)
            sage: s = M.1.modular_symbol_rep()[0][1]; s
            X^2*{-1/6, 0}
            sage: s.manin_symbol_rep()
            -2*[X*Y,(-1,0)] - [X^2,(-1,0)] - [Y^2,(1,1)] - [X^2,(-6,1)]
            sage: M(s.manin_symbol_rep()) == M([2,-1/6,0])
            True
        """
