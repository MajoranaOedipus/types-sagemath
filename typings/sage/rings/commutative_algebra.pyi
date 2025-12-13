from sage.categories.commutative_algebras import CommutativeAlgebras as CommutativeAlgebras

def is_CommutativeAlgebra(x):
    """
    Check to see if ``x`` is in the category of ``CommutativeAlgebras``.

    EXAMPLES::

        sage: from sage.rings.commutative_algebra import is_CommutativeAlgebra
        sage: is_CommutativeAlgebra(QQ['x'])
        doctest:warning...
        DeprecationWarning: the function is_CommutativeAlgebra is deprecated; use '... in Algebras(base_ring).Commutative()' instead
        See https://github.com/sagemath/sage/issues/35999 for details.
        True
    """
