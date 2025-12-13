from typing import Any, overload

class BinaryTree:
    """File: /build/sagemath/src/sage/src/sage/misc/binary_tree.pyx (starting at line 180)

        A simple binary tree with integer keys.
    """
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def contains(self, intkey) -> Any:
        """BinaryTree.contains(self, int key)

        File: /build/sagemath/src/sage/src/sage/misc/binary_tree.pyx (starting at line 301)

        Return whether a node with the given key exists in the tree.

        EXAMPLES::

            sage: from sage.misc.binary_tree import BinaryTree
            sage: t = BinaryTree()
            sage: t.contains(1)
            False
            sage: t.insert(1, 1)
            sage: t.contains(1)
            True"""
    def delete(self, intkey) -> Any:
        """BinaryTree.delete(self, int key)

        File: /build/sagemath/src/sage/src/sage/misc/binary_tree.pyx (starting at line 239)

        Remove a the node corresponding to key, and return the value
        associated with it.

        EXAMPLES::

            sage: from sage.misc.binary_tree import BinaryTree
            sage: t = BinaryTree()
            sage: t.insert(3,3)
            sage: t.insert(1,1)
            sage: t.insert(2,2)
            sage: t.insert(0,0)
            sage: t.insert(5,5)
            sage: t.insert(6,6)
            sage: t.insert(4,4)
            sage: t.delete(0)
            0
            sage: t.delete(3)
            3
            sage: t.delete(5)
            5
            sage: t.delete(2)
            2
            sage: t.delete(6)
            6
            sage: t.delete(1)
            1
            sage: t.delete(0)
            sage: t.get_max()
            4
            sage: t.get_min()
            4"""
    def get(self, intkey) -> Any:
        """BinaryTree.get(self, int key)

        File: /build/sagemath/src/sage/src/sage/misc/binary_tree.pyx (starting at line 283)

        Return the value associated with the key given.

        EXAMPLES::

            sage: from sage.misc.binary_tree import BinaryTree
            sage: t = BinaryTree()
            sage: t.insert(0, Matrix([[0,0], [1,1]]))                                   # needs sage.modules
            sage: t.insert(0, 1)
            sage: t.get(0)                                                              # needs sage.modules
            [0 0]
            [1 1]"""
    def get_max(self) -> Any:
        """BinaryTree.get_max(self)

        File: /build/sagemath/src/sage/src/sage/misc/binary_tree.pyx (starting at line 319)

        Return the value of the node with the maximal key value."""
    def get_min(self) -> Any:
        """BinaryTree.get_min(self)

        File: /build/sagemath/src/sage/src/sage/misc/binary_tree.pyx (starting at line 331)

        Return the value of the node with the minimal key value."""
    def insert(self, key, value=...) -> Any:
        """BinaryTree.insert(self, key, value=None)

        File: /build/sagemath/src/sage/src/sage/misc/binary_tree.pyx (starting at line 210)

        Insert a key-value pair into the BinaryTree.

        Duplicate keys are ignored.

        The first parameter, key, should be an int, or coercible (one-to-one)
        into an int.

        EXAMPLES::

            sage: from sage.misc.binary_tree import BinaryTree
            sage: t = BinaryTree()
            sage: t.insert(1)
            sage: t.insert(0)
            sage: t.insert(2)
            sage: t.insert(0,1)
            sage: t.get(0)
            0"""
    @overload
    def is_empty(self) -> Any:
        """BinaryTree.is_empty(self)

        File: /build/sagemath/src/sage/src/sage/misc/binary_tree.pyx (starting at line 425)

        Return whether the tree has no nodes.

        EXAMPLES::

            sage: from sage.misc.binary_tree import BinaryTree
            sage: t = BinaryTree()
            sage: t.is_empty()
            True
            sage: t.insert(0,0)
            sage: t.is_empty()
            False"""
    @overload
    def is_empty(self) -> Any:
        """BinaryTree.is_empty(self)

        File: /build/sagemath/src/sage/src/sage/misc/binary_tree.pyx (starting at line 425)

        Return whether the tree has no nodes.

        EXAMPLES::

            sage: from sage.misc.binary_tree import BinaryTree
            sage: t = BinaryTree()
            sage: t.is_empty()
            True
            sage: t.insert(0,0)
            sage: t.is_empty()
            False"""
    @overload
    def is_empty(self) -> Any:
        """BinaryTree.is_empty(self)

        File: /build/sagemath/src/sage/src/sage/misc/binary_tree.pyx (starting at line 425)

        Return whether the tree has no nodes.

        EXAMPLES::

            sage: from sage.misc.binary_tree import BinaryTree
            sage: t = BinaryTree()
            sage: t.is_empty()
            True
            sage: t.insert(0,0)
            sage: t.is_empty()
            False"""
    def keys(self, order=...) -> Any:
        '''BinaryTree.keys(self, order=\'inorder\')

        File: /build/sagemath/src/sage/src/sage/misc/binary_tree.pyx (starting at line 441)

        Return the keys sorted according to "order" parameter.

        The order can be one of
        "inorder", "preorder", or "postorder"'''
    @overload
    def pop_max(self) -> Any:
        """BinaryTree.pop_max(self)

        File: /build/sagemath/src/sage/src/sage/misc/binary_tree.pyx (starting at line 343)

        Return the value of the node with the maximal key value,
        and remove that node from the tree.

        EXAMPLES::

            sage: from sage.misc.binary_tree import BinaryTree
            sage: t = BinaryTree()
            sage: t.insert(4,'e')
            sage: t.insert(2,'c')
            sage: t.insert(0,'a')
            sage: t.insert(1,'b')
            sage: t.insert(3,'d')
            sage: t.insert(5,'f')
            sage: while not t.is_empty():
            ....:     print(t.pop_max())
            f
            e
            d
            c
            b
            a"""
    @overload
    def pop_max(self) -> Any:
        """BinaryTree.pop_max(self)

        File: /build/sagemath/src/sage/src/sage/misc/binary_tree.pyx (starting at line 343)

        Return the value of the node with the maximal key value,
        and remove that node from the tree.

        EXAMPLES::

            sage: from sage.misc.binary_tree import BinaryTree
            sage: t = BinaryTree()
            sage: t.insert(4,'e')
            sage: t.insert(2,'c')
            sage: t.insert(0,'a')
            sage: t.insert(1,'b')
            sage: t.insert(3,'d')
            sage: t.insert(5,'f')
            sage: while not t.is_empty():
            ....:     print(t.pop_max())
            f
            e
            d
            c
            b
            a"""
    @overload
    def pop_min(self) -> Any:
        """BinaryTree.pop_min(self)

        File: /build/sagemath/src/sage/src/sage/misc/binary_tree.pyx (starting at line 384)

        Return the value of the node with the minimal key value,
        and remove that node from the tree.

        EXAMPLES::

            sage: from sage.misc.binary_tree import BinaryTree
            sage: t = BinaryTree()
            sage: t.insert(4,'e')
            sage: t.insert(2,'c')
            sage: t.insert(0,'a')
            sage: t.insert(1,'b')
            sage: t.insert(3,'d')
            sage: t.insert(5,'f')
            sage: while not t.is_empty():
            ....:     print(t.pop_min())
            a
            b
            c
            d
            e
            f"""
    @overload
    def pop_min(self) -> Any:
        """BinaryTree.pop_min(self)

        File: /build/sagemath/src/sage/src/sage/misc/binary_tree.pyx (starting at line 384)

        Return the value of the node with the minimal key value,
        and remove that node from the tree.

        EXAMPLES::

            sage: from sage.misc.binary_tree import BinaryTree
            sage: t = BinaryTree()
            sage: t.insert(4,'e')
            sage: t.insert(2,'c')
            sage: t.insert(0,'a')
            sage: t.insert(1,'b')
            sage: t.insert(3,'d')
            sage: t.insert(5,'f')
            sage: while not t.is_empty():
            ....:     print(t.pop_min())
            a
            b
            c
            d
            e
            f"""
    def values(self, order=...) -> Any:
        '''BinaryTree.values(self, order=\'inorder\')

        File: /build/sagemath/src/sage/src/sage/misc/binary_tree.pyx (starting at line 460)

        Return the keys sorted according to "order" parameter.

        The order can be one of
        "inorder", "preorder", or "postorder"'''

class Test:
    def binary_tree(self, values=..., cycles=...) -> Any:
        """Test.binary_tree(self, values=100, cycles=100000)

        File: /build/sagemath/src/sage/src/sage/misc/binary_tree.pyx (starting at line 494)

        Perform a sequence of random operations, given random inputs
        to stress test the binary tree structure.

        This was useful during development to find memory leaks /
        segfaults.  Cycles should be at least 100 times as large as
        values, or the delete, contains, and get methods won't hit
        very often.

        INPUT:

        - ``values`` -- number of possible values to use

        - ``cycles`` -- number of operations to perform

        TESTS::

            sage: sage.misc.binary_tree.Test().random()"""
    def random(self) -> Any:
        """Test.random(self)

        File: /build/sagemath/src/sage/src/sage/misc/binary_tree.pyx (starting at line 491)"""
