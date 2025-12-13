from sage.structure.element import Element as Element

class Cipher(Element):
    """
    Cipher class
    """
    def __init__(self, parent, key) -> None:
        """
        Create a cipher.
        """
    def __eq__(self, right): ...
    def key(self): ...
    def domain(self): ...
    def codomain(self): ...

class SymmetricKeyCipher(Cipher):
    """
    Symmetric key cipher class
    """
    def __init__(self, parent, key) -> None:
        """
        Create a symmetric cipher.
        """

class PublicKeyCipher(Cipher):
    """
    Public key cipher class
    """
    def __init__(self, parent, key, public: bool = True) -> None:
        """
        Create a public key cipher.
        """
