from sage.algebras.lie_algebras.structure_coefficients import LieAlgebraWithStructureCoefficients as LieAlgebraWithStructureCoefficients
from sage.algebras.lie_algebras.subalgebra import LieSubalgebra_finite_dimensional_with_basis as LieSubalgebra_finite_dimensional_with_basis
from sage.categories.homset import Hom as Hom
from sage.categories.lie_algebras import LieAlgebras as LieAlgebras
from sage.categories.morphism import SetMorphism as SetMorphism
from sage.structure.element import Element as Element
from sage.structure.indexed_generators import standardize_names_index_set as standardize_names_index_set

class LieQuotient_finite_dimensional_with_basis(LieAlgebraWithStructureCoefficients):
    """
    A quotient Lie algebra.

    INPUT:

    - ``I`` -- an ideal or a list of generators of the ideal
    - ``ambient`` -- (optional) the Lie algebra to be quotiented;
      will be deduced from ``I`` if not given
    - ``names`` -- (optional) string or list of strings;
      names for the basis elements of the quotient. If ``names`` is a
      string, the basis will be named ``names_1``,...,``names_n``.

    EXAMPLES:

    The Engel Lie algebra as a quotient of the free nilpotent Lie algebra
    of step 3 with 2 generators::

        sage: L = LieAlgebra(QQ, 2, step=3)
        sage: L.inject_variables()
        Defining X_1, X_2, X_12, X_112, X_122
        sage: I = L.ideal(X_122)
        sage: E = L.quotient(I); E
        Lie algebra quotient L/I of dimension 4 over Rational Field where
        L: Free Nilpotent Lie algebra on 5 generators (X_1, X_2, X_12, X_112, X_122) over Rational Field
        I: Ideal (X_122)
        sage: E.category()
        Join of Category of finite dimensional nilpotent Lie algebras with basis
        over Rational Field and Category of subquotients of sets
        sage: E.basis().list()
        [X_1, X_2, X_12, X_112]
        sage: E.inject_variables()
        Defining X_1, X_2, X_12, X_112
        sage: X_1.bracket(X_2)
        X_12
        sage: X_1.bracket(X_12)
        X_112
        sage: X_2.bracket(X_12)
        0

    Shorthand for taking a quotient without creating an ideal first::

        sage: E2 = L.quotient(X_122); E2
        Lie algebra quotient L/I of dimension 4 over Rational Field where
        L: Free Nilpotent Lie algebra on 5 generators (X_1, X_2, X_12, X_112, X_122) over Rational Field
        I: Ideal (X_122)
        sage: E is E2
        True

    Custom names for the basis can be given::

        sage: E.<X,Y,Z,W> = L.quotient(X_122)
        sage: E.basis().list()
        [X, Y, Z, W]
        sage: X.bracket(Z)
        W
        sage: Y.bracket(Z)
        0

    The elements can be relabeled linearly by passing a string to the
    ``names`` parameter::

        sage: E = L.quotient(X_122, names='Y')
        sage: E.basis().list()
        [Y_1, Y_2, Y_3, Y_4]
        sage: E.inject_variables()
        Defining Y_1, Y_2, Y_3, Y_4
        sage: Y_1.bracket(Y_3)
        Y_4
        sage: Y_2.bracket(Y_3)
        0

    Conversion from the ambient Lie algebra uses the quotient projection::

        sage: L = LieAlgebra(QQ, 2, step=3)
        sage: L.inject_variables()
        Defining X_1, X_2, X_12, X_112, X_122
        sage: E = L.quotient(X_122, names='Y')
        sage: E(X_1), E(X_2), E(X_12), E(X_112), E(X_122)
        (Y_1, Y_2, Y_3, Y_4, 0)

    A non-stratifiable Lie algebra as a quotient of the free nilpotent Lie
    algebra of step 4 on 2 generators by the relation
    `[X_2, [X_1, X_2]] = [X_1, [X_1, [X_1, X_2]]]`::

        sage: L = LieAlgebra(QQ, 2, step=4)
        sage: X_1, X_2 = L.homogeneous_component_basis(1)
        sage: rel = L[X_2, [X_1, X_2]] - L[X_1, [X_1, [X_1, X_2]]]
        sage: Q = L.quotient(rel, names='Y')
        sage: Q.dimension()
        5
        sage: Q.inject_variables()
        Defining Y_1, Y_2, Y_3, Y_4, Y_5
        sage: lcs = Q.lower_central_series()
        sage: [I.basis().list() for I in lcs]
        [[Y_1, Y_2, Y_3, Y_4, Y_5], [Y_3, Y_4, Y_5], [Y_4, Y_5], [Y_5], []]
        sage: Y_2.bracket(Y_3)
        -Y_5

    Quotients when the base ring is not a field are not implemented::

        sage: L = lie_algebras.Heisenberg(ZZ, 1)
        sage: L.quotient(L.an_element())
        Traceback (most recent call last):
        ...
        NotImplementedError: quotients over non-fields not implemented

    TESTS:

    Verify that iterated quotient constructions work::

        sage: L = LieAlgebra(QQ, 2, step=3)
        sage: quots = [L]
        sage: for k in range(5):
        ....:     L = L.quotient(L.basis().list()[-1])
        ....:     quots.append(L)
        sage: [Q.dimension() for Q in quots]
        [5, 4, 3, 2, 1, 0]
        sage: all(Lp is Ln.ambient() for Lp, Ln in zip(quots,quots[1:]))
        True
        sage: X = quots[-2].an_element()
        sage: lifts = [X]
        sage: quots = list(reversed(quots[1:-1]))
        sage: for Q in quots:
        ....:     X = Q.lift(X)
        ....:     lifts.append(X)
        sage: all(X.parent() is L for X, L in zip(lifts,quots))
        True

    Verify a quotient construction when the basis ordering and indices ordering
    are different, see :issue:`26352`::

        sage: L.<c,b,a> = LieAlgebra(QQ, abelian=True)
        sage: I2 = L.ideal([a+b, a+c], order=sorted)
        sage: I2.basis()
        Finite family {'b': b + a, 'c': c + a}
        sage: Q = L.quotient(I2)
        sage: Q.basis()
        Finite family {'a': a}

    A test suite::

        sage: L.<x,y,z,w,u> = LieAlgebra(QQ, 2, step=3)
        sage: K = L.quotient(z + w)
        sage: K.dimension()
        2
        sage: TestSuite(K).run()
    """
    @staticmethod
    def __classcall_private__(cls, ambient, I, names=None, index_set=None, index_set_mapping=None, category=None):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: from sage.algebras.lie_algebras.quotient import LieQuotient_finite_dimensional_with_basis
            sage: L.<X,Y> = LieAlgebra(QQ, {('X','Y'): {'X': 1}})
            sage: Q1 = LieQuotient_finite_dimensional_with_basis(L, X)

        Variable names are extracted from the ambient Lie algebra by default::

            sage: Q2 = LieQuotient_finite_dimensional_with_basis(L, X, index_set=['Y'])
            sage: Q1 is Q2
            True
            sage: Q3 = L.quotient(X, names=['Y'])
            sage: Q1 is Q3
            True

        Check that quotients are properly constructed for ideals of
        subalgebras (:issue:`40137`)::

            sage: L.<a,b,c,d> = LieAlgebra(QQ, {('a','b'): {'c': 1, 'd':1}, ('a','c'): {'b':1}})
            sage: A = L.ideal([b,c,d])
            sage: B = L.ideal([c+d])
            sage: Q = A.quotient(B); Q
            Lie algebra quotient L/I of dimension 1 over Rational Field where
            L: Ideal (b, c, d) of Lie algebra on 4 generators (a, b, c, d) over Rational Field
            I: Ideal (b, c + d)
            sage: Q.dimension() == A.dimension() - B.dimension()
            True
        """
    def __init__(self, L, I, names, index_set, index_set_mapping, category=None) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: # needs sage.symbolic
            sage: L.<x,y,z> = LieAlgebra(SR, {('x','y'): {'x':1}})
            sage: K = L.quotient(y)
            sage: K.dimension()
            1
            sage: TestSuite(K).run()
        """
    def ambient(self):
        """
        Return the ambient Lie algebra of ``self``.

        EXAMPLES::

            sage: L.<x,y,z> = LieAlgebra(QQ, 2, step=2)
            sage: Q = L.quotient(z)
            sage: Q.ambient() == L
            True
        """
    def lift(self, X):
        """
        Return some preimage of ``X`` under the quotient projection
        into ``self``.

        INPUT:

        - ``X`` -- an element of ``self``

        EXAMPLES::

            sage: L.<x,y,z> = LieAlgebra(QQ, 2, step=2)
            sage: Q = L.quotient(x + y)
            sage: Q(y)
            -x
            sage: el = Q.lift(Q(y)); el
            -x
            sage: el.parent()
            Free Nilpotent Lie algebra on 3 generators (x, y, z) over Rational Field
        """
    def retract(self, X):
        """
        Map ``X`` under the quotient projection to ``self``.

        INPUT:

        - ``X`` -- an element of the ambient Lie algebra

        EXAMPLES::

            sage: L = LieAlgebra(QQ, 3, step=2)
            sage: L.inject_variables()
            Defining X_1, X_2, X_3, X_12, X_13, X_23
            sage: Q = L.quotient(X_1 + X_2 + X_3)
            sage: Q.retract(X_1), Q.retract(X_2), Q.retract(X_3)
            (X_1, X_2, -X_1 - X_2)
            sage: all(Q.retract(Q.lift(X)) == X for X in Q.basis())
            True
        """
    def defining_ideal(self):
        """
        Return the ideal generating this quotient Lie algebra.

        EXAMPLES::

            sage: L = lie_algebras.Heisenberg(QQ, 1)
            sage: p,q,z = L.basis()
            sage: Q = L.quotient(p)
            sage: Q.defining_ideal()
            Ideal (p1) of Heisenberg algebra of rank 1 over Rational Field
        """
    def from_vector(self, v, order=None, coerce: bool = False):
        """
        Return the element of ``self`` corresponding to the vector ``v``.

        INPUT:

        - ``v`` -- a vector in ``self.module()`` or ``self.ambient().module()``

        EXAMPLES:

        An element from a vector of the intrinsic module::

            sage: L.<X,Y,Z> = LieAlgebra(QQ, 3, abelian=True)
            sage: Q = L.quotient(X + Y + Z)
            sage: Q.dimension()
            2
            sage: el = Q.from_vector([1, 2]); el
            X + 2*Y
            sage: el.parent() == Q
            True

        An element from a vector of the ambient module::

            sage: el = Q.from_vector([1, 2, 3]); el
            -2*X - Y
            sage: el.parent() == Q
            True

        Check for the trivial ideal::

            sage: L.<x,y,z> = LieAlgebra(GF(3), {('x','z'): {'x':1, 'y':1}, ('y','z'): {'y':1}})
            sage: I = L.ideal([])
            sage: Q = L.quotient(I)
            sage: v = Q.an_element().to_vector()
            sage: Q.from_vector(v)
            x + y + z
        """
