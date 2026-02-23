#! env /usr/bin/python3
# coding: utf-8
"""
This script test the types of the results of binary operators, listed in `operators`
acting on various objects listed in `objects`. This should output a ODS file (spreadsheet)
showing the result.
When running as a script, odfdo and matplotlib is depended.
You can also import `test_bin_ops` to your module, in which case you can programmingly
interact with the result, or check the result printed in the CLI.
Modify `operators` and `objects` if you want to test other objects.
"""

from typing import Any, cast
from collections import defaultdict, OrderedDict
from collections.abc import Sequence, Callable, Mapping

from sage.all import (
    ZZ, QQ, RR, CC, SR, Expression, Zmod, sqrt, colormaps, 
    RIF, RDF, CIF, CDF, RBF, CBF, oo, unsigned_infinity, I
)

operator_names = {
    "eq": "==",
    "ne": "!=",
    "lt": "<", 
    "gt": ">", 
    "le": "<=", 
    "ge": ">=",
    "add": "+", 
    "sub": "-", 
    "mul": "*", 
    "truediv": "/", 
    "floordiv": "//", 
    "mod": "mod",
    "pow": "**",
    "contains": "in",
    "and_": "&",
    "or_": "|",
    "xor": "^",
    # disabled because there is some bug in sage that cause a SIGSEGV
    # "lshift": "<<",
    # "rshift": ">>"
}

import operator
operators: list[Callable[[Any, Any], Any]] = list(
    getattr(operator, op) for op in operator_names
)

from builtins import sum
from gmpy2 import mpz, mpc, mpfr
from numpy import float32, float128, complex64, int32, uint16

from itertools import product

objects = [
    0, 1, 2, -3, 
    1.2, -3.0, 
    1+3j, 
    mpz(10), mpz(0), mpz(1), -mpz(3), 
    mpfr(3.2), -mpfr(1.2), 
    mpc(1+3j),
    float32(1.2), float128(1.3e2), complex64(1+2.j), int32(100), uint16(8),
    -float32(1.2), -float128(1.3e2), -int32(100), 
    ZZ(1), ZZ(3), -ZZ(4), ZZ(0),
    Zmod(7)(3), 
    QQ((1, 2)), QQ((1, 1)), -QQ((3, 2)), QQ(0),
    3 * cast(Expression, SR.var("x")) + 1, 
    ZZ["y"](1), ZZ["y"](0), ZZ["y"](3 + cast(Expression, SR.var("y"))),
    QQ["w"](1), QQ["w"](0), QQ["w"](cast(Expression, SR.var("w"))**3),
    RR["z"](1), RR["z"](0), RR["z"](cast(Expression, SR.var("z"))**2), 
    CC["u"](1), CC["u"](0), CC["u"](cast(Expression, SR.var("u")) + 4),
    ZZ[sqrt(2)](1), ZZ[sqrt(2)](0), ZZ[sqrt(2)](2), ZZ[sqrt(2)].gens()[1]
    ,
    I,
    RR(10.5), RDF(17.3), RBF(19.2), RIF(1.9),
    -RR(10.5), -RDF(17.3), -RBF(19.2), -RIF(1.9),
    CC(4-5j), CDF(5+3j), CBF(7+6j), CIF(-3+2j),
    oo, -oo, unsigned_infinity,
]


def test_bin_op(
    l, r, op: Callable[[Any, Any], Any]
) -> dict[tuple[type, type, str], set[type | Exception]]:
    """
    Test

    The output is a `defaultdict[tuple[type, type, str], list[type]]`,
    with output[type(l), type(r), op.__name__] == type(op(l, r)) if no exceptions,
    else the value would the type of the value.
    """
    if hasattr(op, "__name__"):
        op_name = op.__name__
    else:
        op_name = str(op)
    try:
        result = type(op(l, r))
    except Exception as e:
        result = e
    return {
        (type(l), type(r), op_name): {result}
    }

def test_bin_ops(
    objects: Sequence[Any],
    bin_ops: Sequence[Callable[[Any, Any], Any]],
    filter: type | tuple[type] | None = None,
    show: bool = True
) -> Mapping[tuple[type, type, str], set[type]]:
    """
    Test the types of the `op(l, r)`
    where `l, r` are in `objects` and `op` in `bin_ops`.

    List `objects` and binary operators `bin_ops` you need to test against,
    and optionally filter the outcome by a class object `filter`,
    so that only when instances of `filter` are involved the results would be included.

    If `show`, print the result to stdout.

    The output is a `defaultdict[tuple[type, type, str], set[type]]`,
    with output[type(l), type(r), op.__name__] == type(op(l, r)) if no exceptions,
    else the value would the type of the value.
    """
    results: defaultdict[tuple[type, type, str], set[type]] = defaultdict(set)

    for s, t, bin_op in product(objects, objects, bin_ops):
        if filter is not None and not isinstance(s, filter) and not isinstance(t, filter):
            continue

        try:
            result = type(bin_op(s, t))
        except Exception as e:
            result = type(e)
        L, R= type(s), type(t)
        if hasattr(bin_op, "__name__"):
            op_name = bin_op.__name__
        else:
            op_name = str(bin_op)
        results[L, R, op_name].add(result)
    
    if show:
        print(show_result(results))
    
    return results

def show_result(result: dict[tuple[type, type, str], set[type]]):
    """
    print the result returned from test_bin_op(s).
    """
    for (L, R, op), Ts in result.items():
        if op in operator_names:
            template = "{} " + operator_names[op] + " {} \t-> {}"
        elif op == "getitem":
            template = "{}[{}] \t-> {}"
        else:
            template = "{} `" + op + "` {} \t-> {}"
        
        print(template.format(L.__name__, R.__name__, " | ".join(T.__name__ for T in Ts)))

def test_pow(tests, filter: type | tuple[type] | None = None):
    """
    Test the types of the `pow(b, e, m)`
    where `b, e, m` are in `tests`.
    Print the result, returns None.

    if `filter`, only when `type(b)` or `type(e)` is or in filter` is included.
    """
    for b, e, m in product(tests, tests, tests):
     if filter is not None and not isinstance(b, filter) and not isinstance(e, filter):
         continue
     try:
         result = pow(b, e, m)
     except Exception as ex:
         result = ex
     print(f"{type(b).__name__}**{type(e).__name__} % {type(m).__name__} ->\t{type(result).__name__}")


from argparse import ArgumentParser
parser = ArgumentParser(description=f"Save results of binary operators of the following objects:\n {objects}")

parser.add_argument("output_file", help="the ODS file to write into.")

def main(file, objects=objects, operators=operators, show=False):
    results = test_bin_ops(
        objects, operators, show=show
    )

    objects = list(OrderedDict((type(obj), obj) for obj in objects).values())

    def op_symbol_and_name(op):
        try:
            op_name: str = op.__name__
        except AttributeError:
            op_name: str= str(op)
        
        if op_name in operator_names:
            return operator_names[op_name], op_name
        
        return op_name, op_name

    data: OrderedDict[str, list[list[str]]] = OrderedDict()
    data.update({
        # ODS does not support these symbols as sheet title
        op_symbol if op_symbol not in {"*", "**", "/", "//"} else op_name : [
            [op_symbol] + [type(obj_R).__name__ for obj_R in objects]
        ] + [
            [type(obj_L).__name__] + [
                " | ".join(map(lambda T: T.__name__, results[type(obj_L), type(obj_R), op_name]))
             for obj_R in objects]
            for obj_L in objects
        ]
        for op_symbol, op_name in map(op_symbol_and_name, operators)
    })

    from odfdo import (
        Document, Cell, Row, Table, create_table_cell_style, rgb2hex
    )
    from matplotlib.colors import ListedColormap
    cmp1: ListedColormap = colormaps["jet"]
    cmp2: ListedColormap = colormaps["plasma"]

    def rgb256(r, g, b, _) -> tuple[int, int, int]:
        def to_int(c):
            c_int = int(c * 256)
            c_int = min(c_int, 255)
            c_int = max(c_int, 0)
            return c_int
        return tuple(map(to_int, (r, g, b))) # type: ignore

    colors: dict[str, str] = {}

    N = len(objects)
    for i, obj in enumerate(objects):
        colors[type(obj).__name__] = rgb2hex(rgb256(*cmp1(i/N)))

    # possible Ts that are not listed in the objects
    # Used OrderedDict so that the order is preserved
    possible_Ts_: OrderedDict[str, None] = OrderedDict()

    for rows in data.values():
        all: list[str] = sum(rows, start=[])
        for t in all[1:]:
            if t not in colors:
                possible_Ts_[t] = None

    possible_Ts = list(possible_Ts_)
    N = len(possible_Ts)

    i = 0
    def is_all_error(t):
        all_error = True
        for ti in t.split("|"):
            if "Error" not in ti and "Exception" not in ti:
                all_error = False
        return all_error
    
    for t in possible_Ts:
        if is_all_error(t):
            continue
        else:
            colors[t] = rgb2hex(rgb256(*cmp2(i/N)))
            i += 1

    colors["bool"] = rgb2hex((255, 255, 255))

    document = Document("spreadsheet")
    document.body.clear()

    styles = {
        t : document.insert_style(
                style = create_table_cell_style(background_color=color),
                automatic = True
            )
        for t, color in colors.items()
    }

    error_style_name = document.insert_style(
                style = create_table_cell_style(color=rgb2hex((255, 0, 0))),
                automatic = True
            )
    for e in filter(is_all_error, possible_Ts):
        styles[e] = error_style_name

    for op, datum in data.items():
        table: Table = Table(op)
        for row_data in datum:
            row = Row()
            for cell_value in row_data:
                cell = Cell(
                    value=cell_value,
                    style = styles[cell_value] if cell_value in styles else None
                )
                row.append(cell)
            table.append_row(row)

        document.body.append(table)

    document.save(file, pretty=True)

if __name__ == "__main__":
    args = parser.parse_args()
    main(args.output_file)
    # from sage.all import log
    # from sage.functions.log import logb, polylog
    # logb.__name__ = "logb"
    # polylog.__name__ = "polylog"
    # def logb_hold(x, y):
    #     return logb(x, y, hold=True)
    # main("./logb.ods", objects, {logb, logb_hold, log, polylog})

