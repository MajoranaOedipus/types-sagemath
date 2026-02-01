"""

Handling PARI errors
********************

AUTHORS:

- Peter Bruin (September 2013): initial version (:trac:`9640`)

- Jeroen Demeyer (January 2015): use ``cb_pari_err_handle`` (:trac:`14894`)

"""
from __future__ import annotations
import builtins as __builtins__
__all__: list[str] = ['PariError']
class PariError(RuntimeError):
    """
    
        Error raised by PARI
        
    """
    def __repr__(self):
        """
        
                TESTS:
        
                >>> import cypari2
                >>> pari = cypari2.Pari()
                >>> PariError(11)
                PariError(11)
                
        """
    def __str__(self):
        """
        
                Return a suitable message for displaying this exception.
        
                This is simply the error text with certain trailing characters
                stripped.
        
                EXAMPLES:
        
                >>> import cypari2
                >>> pari = cypari2.Pari()
                >>> try:
                ...     pari('1/0')
                ... except PariError as err:
                ...     print(err)
                _/_: impossible inverse in gdiv: 0
        
                A syntax error:
        
                >>> pari('!@#$%^&*()')
                Traceback (most recent call last):
                ...
                PariError: syntax error, unexpected ...
                
        """
    def errdata(self):
        """
        
                Return the error data (a ``t_ERROR`` gen) corresponding to this
                error.
        
                EXAMPLES:
        
                >>> import cypari2
                >>> pari = cypari2.Pari()
                >>> try:
                ...     pari('Mod(2,6)')**-1
                ... except PariError as e:
                ...     E = e.errdata()
                >>> E
                error("impossible inverse in Fp_inv: Mod(2, 6).")
                >>> E.component(2)
                Mod(2, 6)
                
        """
    def errnum(self):
        """
        
                Return the PARI error number corresponding to this exception.
        
                EXAMPLES:
        
                >>> import cypari2
                >>> pari = cypari2.Pari()
                >>> try:
                ...     pari('1/0')
                ... except PariError as err:
                ...     print(err.errnum())
                31
                
        """
    def errtext(self):
        """
        
                Return the message output by PARI when this error occurred.
        
                EXAMPLES:
        
                >>> import cypari2
                >>> pari = cypari2.Pari()
                >>> try:
                ...     pari('pi()')
                ... except PariError as e:
                ...     print(e.errtext())
                not a function in function call
                
        """
__pyx_capi__: dict  # value = {'_pari_err_handle': <capsule object "int (GEN)" at 0x762576563d80>, '_pari_err_recover': <capsule object "void (long)" at 0x762576563d30>, '_pari_init_error_handling': <capsule object "void (void)" at 0x762576563ce0>}
__test__: dict 
