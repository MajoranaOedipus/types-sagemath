from sage.structure.all import parent as parent

def convolution(L1, L2):
    """
    Return convolution of non-empty lists L1 and L2.

    L1 and L2 may have arbitrary lengths.

    EXAMPLES::

        sage: convolution([1, 2, 3], [4, 5, 6, 7])
        [4, 13, 28, 34, 32, 21]

    TESTS::

        sage: R = Integers(47)
        sage: L1 = [R.random_element() for _ in range(1000)]
        sage: L2 = [R.random_element() for _ in range(3756)]
        sage: L3 = convolution(L1, L2)
        sage: L3[2000] == sum([L1[i] * L2[2000-i] for i in range(1000)])
        True
        sage: len(L3) == 1000 + 3756 - 1
        True
    """
