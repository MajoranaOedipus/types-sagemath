"""

Memory management for Gens on the PARI stack or the heap
********************************************************
"""
from __future__ import annotations
from _warnings import warn
import builtins as __builtins__
import typing
__all__: list[str] = ['DetachGen', 'warn']
class DetachGen:
    """
    
        Destroy a :class:`Gen` but keep the ``GEN`` which is inside it.
    
        The typical usage is as follows:
    
        1. Creates the ``DetachGen`` object from a :class`Gen`.
    
        2. Removes all other references to that :class:`Gen`.
    
        3. Call the ``detach`` method to retrieve the ``GEN`` (or a copy of
           it if the original was not on the stack).
        
    """
    __pyx_vtable__: typing.ClassVar[typing.Any]  # value = <capsule object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setstate__(*args, **kwargs):
        ...
    def __reduce_cython__(self):
        ...
    def __setstate_cython__(self, __pyx_state):
        ...
def __pyx_unpickle_DetachGen(__pyx_type, __pyx_checksum, __pyx_state):
    ...
__pyx_capi__: dict  # value = {'new_gens2': <capsule object "PyObject *(GEN, GEN)" at 0x78603e7901d0>, 'move_gens_to_heap': <capsule object "int (pari_sp)" at 0x78603e790220>, 'set_pari_stack_size': <capsule object "int (size_t, size_t)" at 0x78603e790270>, 'before_resize': <capsule object "int (void)" at 0x78603e7902c0>, 'clone_gen': <capsule object "struct __pyx_obj_7cypari2_3gen_Gen *(GEN)" at 0x78603e790310>, 'clone_gen_noclear': <capsule object "struct __pyx_obj_7cypari2_3gen_Gen *(GEN)" at 0x78603e790360>, 'new_gen': <capsule object "struct __pyx_obj_7cypari2_3gen_Gen *(GEN)" at 0x78603e7903b0>, 'new_gen_noclear': <capsule object "struct __pyx_obj_7cypari2_3gen_Gen *(GEN)" at 0x78603e790400>, 'remove_from_pari_stack': <capsule object "void (struct __pyx_obj_7cypari2_3gen_Gen *)" at 0x78603e790450>, 'after_resize': <capsule object "void (void)" at 0x78603e7904a0>, 'clear_stack': <capsule object "void (void)" at 0x78603e7904f0>, 'reset_avma': <capsule object "void (void)" at 0x78603e790540>}
__test__: dict = {}
