from sage.misc.lazy_attribute import (
    lazy_attribute as lazy_attribute,
    lazy_class_attribute as lazy_class_attribute,
)
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.verbose import (
    set_verbose as set_verbose,
    set_verbose_files as set_verbose_files,
    get_verbose_files as get_verbose_files,
    unset_verbose_files as unset_verbose_files,
    get_verbose as get_verbose,
)
from sage.misc.verbose import verbose as verbose
from sage.misc.call import attrcall as attrcall
from sage.misc.misc_c import (
    prod as prod,
    running_total as running_total,
    balanced_sum as balanced_sum,
)

mul = prod
add = sum

from sage.misc.repr import repr_lincomb as repr_lincomb
from sage.misc.flatten import flatten as flatten
from sage.misc.persist import (
    save as save,
    load as load,
    dumps as dumps,
    loads as loads,
    db as db,
    db_save as db_save,
)
from sage.misc.constant_function import ConstantFunction as ConstantFunction
from sage.misc.sage_unittest import TestSuite as TestSuite
from sage.misc.decorators import (
    specialize as specialize,
    sage_wraps as sage_wraps,
    infix_operator as infix_operator,
)
from sage.misc.unknown import Unknown as Unknown, UnknownError as UnknownError
from sage.misc.cachefunc import (
    CachedFunction as CachedFunction,
    cached_function as cached_function,
    cached_method as cached_method,
    cached_in_parent_method as cached_in_parent_method,
    disk_cached_function as disk_cached_function,
)
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.timing import walltime as walltime, cputime as cputime
from sage.misc.temporary_file import tmp_dir as tmp_dir, tmp_filename as tmp_filename
from sage.misc.sage_eval import sage_eval as sage_eval, sageobj as sageobj
from sage.misc.sage_input import sage_input as sage_input
from sage.misc.misc import (
    exists as exists,
    forall as forall,
    is_iterator as is_iterator,
    random_sublist as random_sublist,
    pad_zeros as pad_zeros,
    newton_method_sizes as newton_method_sizes,
    compose as compose,
    nest as nest,
)
from sage.misc.banner import version as version
from sage.misc.dev_tools import import_statements as import_statements
from sage.misc.html import html as html, pretty_print_default as pretty_print_default
from sage.misc.table import table as table
from sage.misc.sage_timeit_class import timeit as timeit
from sage.misc.edit_module import edit as edit
from sage.misc.map_threaded import map_threaded as map_threaded
from sage.misc.session import (
    load_session as load_session,
    save_session as save_session,
    show_identifiers as show_identifiers,
)
from sage.misc.remote_file import get_remote_file as get_remote_file
from sage.misc.mrange import (
    xmrange as xmrange,
    mrange as mrange,
    xmrange_iter as xmrange_iter,
    mrange_iter as mrange_iter,
    cartesian_product_iterator as cartesian_product_iterator,
)
from sage.misc.fpickle import (
    pickle_function as pickle_function, unpickle_function as unpickle_function
)
from sage.misc.pager import pager as pager
from sage.misc.sagedoc import (
    browse_sage_doc as browse_sage_doc,
    search_src as search_src,
    search_def as search_def,
    search_doc as search_doc,
    tutorial as tutorial,
    reference as reference,
    manual as manual,
    developer as developer,
    constructions as constructions,
    help as help,
)
from pydoc import help as _python_help
python_help = _python_help
from sage.misc.classgraph import class_graph as class_graph
from sage.misc.reset import reset as reset, restore as restore

from sage.misc.mathml import mathml as mathml

from sage.misc.defaults import (
    set_default_variable_name as set_default_variable_name,
    series_precision as series_precision,
    set_series_precision as set_series_precision,
)
from sage.misc.cython import cython_lambda as cython_lambda
from sage.misc.cython import cython_compile
cython = cython_compile
from sage.misc.func_persist import func_persist as func_persist
from sage.misc.functional import (
    additive_order as additive_order,
    base_ring as base_ring,
    base_field as base_field,
    basis as basis,
    category as category,
    charpoly as charpoly,
    characteristic_polynomial as characteristic_polynomial,
    coerce as coerce,
    cyclotomic_polynomial as cyclotomic_polynomial,
    decomposition as decomposition,
    denominator as denominator,
    det as det,
    dimension as dimension,
    dim as dim,
    discriminant as discriminant,
    disc as disc,
    eta as eta,
    fcp as fcp,
    gen as gen,
    gens as gens,
    hecke_operator as hecke_operator,
    image as image,
    integral as integral,
    integrate as integrate,
    integral_closure as integral_closure,
    interval as interval,
    xinterval as xinterval,
    is_even as is_even,
    is_odd as is_odd,
    kernel as kernel,
    krull_dimension as krull_dimension,
    lift as lift,
    log as log,
    minimal_polynomial as minimal_polynomial,
    minpoly as minpoly,
    multiplicative_order as multiplicative_order,
    ngens as ngens,
    norm as norm,
    numerator as numerator,
    numerical_approx as numerical_approx,
    n as n,
    N as N,
    objgens as objgens,
    objgen as objgen,
    order as order,
    rank as rank,
    regulator as regulator,
    round as round,
    quotient as quotient,
    quo as quo,
    isqrt as isqrt,
    squarefree_part as squarefree_part,
    sqrt as sqrt,
    symbolic_sum,
    symbolic_prod,
    transpose as transpose,
)
log_b = log
sum = symbolic_sum
product = symbolic_prod
from sage.misc.latex import (
    LatexExpr as LatexExpr, latex as latex, view as view
)

from sage.misc.randstate import (
    seed as seed, set_random_seed as set_random_seed, 
    initial_seed as initial_seed, current_randstate as current_randstate
)

from sage.misc.prandom import *

from sage.misc.explain_pickle import (
    explain_pickle as explain_pickle,
    unpickle_newobj as unpickle_newobj,
    unpickle_global as unpickle_global,
    unpickle_build as unpickle_build,
    unpickle_instantiate as unpickle_instantiate,
    unpickle_persistent as unpickle_persistent,
    unpickle_extension as unpickle_extension,
    unpickle_appends as unpickle_appends,
)

from sage.misc.inline_fortran import fortran as fortran

from sage.misc.banner import banner as banner
from sage.misc.edit_module import set_edit_template as set_edit_template
from sage.misc.profiler import Profiler as Profiler
from sage.misc.trace import trace as trace
from sage.misc.package import (
    installed_packages as installed_packages, 
    is_package_installed as is_package_installed, 
    package_versions as package_versions
)
from sage.misc.benchmark import benchmark as benchmark
from sage.repl.interpreter import logstr as logstr
