class CoercionException(TypeError):
    """
    This is the baseclass of exceptions that the coercion model raises
    when trying to discover coercions. We do not use standard Python
    exceptions to avoid inadvertently catching and suppressing real errors.

    Usually one raises this to indicate the attempted action is not
    implemented/appropriate, but if there are other things to try not
    to immediately abort to the user.
    """
