from _typeshed import Incomplete
from sage.misc import persist as persist

class func_persist:
    """
    Put ``@func_persist`` right before your function
    definition to cache values it computes to disk.
    """
    __doc__: Incomplete
    def __init__(self, f, dir: str = 'func_persist') -> None: ...
    def __call__(self, *args, **kwds): ...
