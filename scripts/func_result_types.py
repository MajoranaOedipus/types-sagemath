from collections import defaultdict
from collections.abc import Callable, Mapping, Sequence
from itertools import product
from typing import Any


def test_result_types(
    objects: Sequence[Any],
    funcs: Sequence[Callable[[Any], Any]],
    show: bool = True,
    **kwargs
) -> Mapping[tuple[str, type], set[type]]:
    """
    Test the types of the `func(x, **kwargs)`
    where `x` is in `objects` and `func` in `funcs`.

    If `show`, print the result to stdout.

    The output is a `defaultdict[tuple[str, type], set[type]]`,
    with output[func.__name__, type(obj)] == type(func(obj)) if no exceptions,
    else the value would the type of the value.
    """
    results: defaultdict[tuple[str, type], set[type]] = defaultdict(set)

    for func, x in product(funcs, objects):
        try:
            result = func(x, **kwargs)
        except Exception as e:
            result = e
        T = type(x)
        if hasattr(func, "__name__"):
            func_name = func.__name__
        else:
            func_name = str(func)
        
        results[func_name, T].add(type(result))
    
        if show:
            print(f"{func_name}({x} :: {type(x).__name__}) -> {result} :: {type(result).__name__}")
    
    return results
