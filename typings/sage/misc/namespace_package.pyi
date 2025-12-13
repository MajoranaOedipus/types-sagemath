def install_doc(package, doc):
    """
    Install the docstring ``doc`` to the package.

    TESTS:

        sage: from sage.misc.namespace_package import install_doc
        sage: install_doc('sage', 'hello')
        sage: from inspect import getdoc
        sage: getdoc(sage)
        'hello'
    """
def install_dict(package, dic) -> None:
    """
    Install ``dic`` to the ``__dict__`` of the package.

    TESTS:

        sage: from sage.misc.namespace_package import install_dict
        sage: install_dict('sage', {'greeting': 'hello'})
        sage: sage.greeting
        'hello'
    """
