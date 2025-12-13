from sage.misc.decorators import decorator_keywords as decorator_keywords, sage_wraps as sage_wraps

@decorator_keywords
def handle_AA_and_QQbar(func):
    """
    Decorator to call a function that only accepts arguments in number fields.

    The argument list is scanned for ideals and/or polynomials over algebraic
    fields (``QQbar`` or ``AA``).  If any exist, they are converted to a common
    number field before calling the function, and the results are converted back.
    Lists, dictionaries (values only), sets, and tuples are converted recursively.

    This decorator can not used with methods that depend on factoring, since
    factorization might require larger number fields than those required to
    express the polynomials.  No means is provided to check whether factoring
    is being attempted by a wrapped method, and if a method invoked a library
    or subprocess (like Singular), it's hard to imagine how such a check could
    be performed.

    See https://mathoverflow.net/questions/304525 for a discussion of why a
    simple attempt to overcome this limitation didn't work.
    """
