from _typeshed import Incomplete
from sage.rings.polynomial.pbori.PyPolyBoRi import Ring as Ring
from sage.rings.polynomial.pbori.pbori import Polynomial as Polynomial, Variable as Variable, VariableBlock as VariableBlock, VariableFactory as VariableFactory

class Block:
    """
    The block class represents a block of variables
    <var_name>(start_index,...,start_index+size-1), it is the preferred
    block type for simple one-dimensional variable sets
    """
    names: Incomplete
    var_name: Incomplete
    start_index: Incomplete
    reverse: Incomplete
    size: Incomplete
    def __init__(self, var_name, size, start_index: int = 0, reverse: bool = False) -> None: ...
    def __iter__(self): ...
    def __getitem__(self, i): ...
    def __len__(self) -> int: ...
    def register(self, start, context) -> None: ...

class AlternatingBlock:
    """
    The Alternating Block class is used for doing tricky variable
    schemes,where base names vary, e.g.
    a(0),b(0),a(1),b(1),a(2),b(2)
    """
    var_names: Incomplete
    size_per_variable: Incomplete
    reverse: Incomplete
    indices: Incomplete
    index2pos: Incomplete
    names: Incomplete
    def __init__(self, var_names, size_per_variable, start_index: int = 0, reverse: bool = False) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    def __getitem__(self, i): ...
    ring: Incomplete
    size: Incomplete
    def register(self, start, context): ...

def shift(f, i): ...

class AdderBlock(AlternatingBlock):
    input1: Incomplete
    input2: Incomplete
    sums: Incomplete
    carries: Incomplete
    start_index: Incomplete
    adder_bits: Incomplete
    def __init__(self, adder_bits, sums: str = 's', carries: str = 'c', input1: str = 'a', input2: str = 'b', start_index: int = 0) -> None: ...
    s: Incomplete
    c: Incomplete
    add_results: Incomplete
    carries_polys: Incomplete
    def register(self, start, context) -> None: ...
    def implement(self, equations) -> None: ...

class HigherOrderBlock:
    """
    HigherOrderBlocks are multidimensional blocks of variables.

    For each dimension a separate start_index and size can be specified.

    var_name : variables will be called <var_name>(multiindex), where
    multiindex is a tuple of the size <size_tuple>

    size_tuple : specifies the sizes of the ranges of each component of the
    multi-indices

    start_index_tuple : the multi-indices will be of the form
    start_index_tuple + a, where a is a multi-index with nonnegative components
    """
    cart: Incomplete
    cart2index: Incomplete
    var_name: Incomplete
    names: Incomplete
    def __init__(self, var_name, size_tuple, start_index_tuple=None, reverse: bool = False) -> None: ...
    def __getitem__(self, i): ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def register(self, start, context): ...

class InOutBlock:
    output: Incomplete
    input: Incomplete
    out_start_index: Incomplete
    in_start_index: Incomplete
    def __init__(self, out_size, in_size, output: str = 'out', input: str = 'in', in_start_index: int = 0, out_start_index: int = 0, out_reverse: bool = False, in_reverse: bool = False) -> None: ...
    def __iter__(self): ...
    def __getitem__(self, i): ...
    def __len__(self) -> int: ...
    out_vars: Incomplete
    in_vars: Incomplete
    def register(self, start, context) -> None: ...

class MultiBlock:
    start_indices: Incomplete
    blocks: Incomplete
    def __init__(self, sizes=None, var_names=['v'], start_indices=[], reverses=None) -> None: ...
    def __iter__(self): ...
    def __getitem__(self, i): ...
    def __len__(self) -> int: ...
    vars: Incomplete
    def register(self, start, context) -> None: ...

class PrefixedDictProxy:
    """docstring for PrefixedDictProxy"""
    wrapped: Incomplete
    prefix: Incomplete
    def __init__(self, wrapped, prefix) -> None: ...
    def __getitem__(self, k): ...
    def __setitem__(self, k, v) -> None: ...

class MacroBlock:
    prefix: Incomplete
    blocks: Incomplete
    combinations: Incomplete
    connections: Incomplete
    def __init__(self, prefix) -> None: ...
    def declare(self, blocks) -> None: ...
    def connect(self, combinations) -> None: ...
    def __iter__(self): ...
    def __getitem__(self, i): ...
    def __len__(self) -> int: ...
    def resolve(self, localname): ...
    def register(self, start, context) -> None: ...
    def implement(self, equations) -> None: ...

class IfThen:
    ifpart: Incomplete
    thenpart: Incomplete
    supposedToBeValid: Incomplete
    def __init__(self, ifpart, thenpart, supposed_to_be_valid: bool = True) -> None: ...

def if_then(i, t, supposed_to_be_valid: bool = True): ...
def declare_ring(blocks, context=None):
    '''
    Declare Ring is the preferred function to create a ring and declare a variable scheme,
    the number of variables is automatically determined, usually you pass globals() as context
    argument to store the ring and the variable mapping.

    EXAMPLES::

        sage: from sage.rings.polynomial.pbori import *
        sage: declare_ring([Block("x",10),Block("y",5)],globals())
        Boolean PolynomialRing in x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, y0, y1, y2, y3, y4

    gives  a ring with x(0..9),y(0..4) and registers the ring as r, and the variable
    blocks x and y in the context dictionary globals(), which consists of the global
    variables of the python module
    '''
def declare_block_scheme(blocks, context) -> None: ...
def main() -> None: ...
