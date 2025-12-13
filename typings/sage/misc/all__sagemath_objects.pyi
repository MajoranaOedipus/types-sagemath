from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.cachefunc import CachedFunction as CachedFunction, cached_function as cached_function, cached_in_parent_method as cached_in_parent_method, cached_method as cached_method, disk_cached_function as disk_cached_function
from sage.misc.call import attrcall as attrcall
from sage.misc.constant_function import ConstantFunction as ConstantFunction
from sage.misc.decorators import infix_operator as infix_operator, sage_wraps as sage_wraps, specialize as specialize
from sage.misc.flatten import flatten as flatten
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute, lazy_class_attribute as lazy_class_attribute
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import balanced_sum as balanced_sum, prod as prod, running_total as running_total
from sage.misc.persist import db as db, db_save as db_save, dumps as dumps, load as load, loads as loads, save as save
from sage.misc.repr import repr_lincomb as repr_lincomb
from sage.misc.sage_unittest import TestSuite as TestSuite
from sage.misc.timing import cputime as cputime, walltime as walltime
from sage.misc.unknown import Unknown as Unknown, UnknownError as UnknownError
from sage.misc.verbose import get_verbose as get_verbose, get_verbose_files as get_verbose_files, set_verbose as set_verbose, set_verbose_files as set_verbose_files, unset_verbose_files as unset_verbose_files

mul = prod
add = sum
