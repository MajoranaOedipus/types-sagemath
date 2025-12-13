from _typeshed import Incomplete

class KeyConvertingDict(dict):
    '''
    A dictionary which automatically applies a conversions to its keys.

    The most common application is the case where the conversion
    function is the object representing some category, so that key
    conversion means a type conversion to adapt keys to that
    category. This allows different representations for keys which in
    turn makes accessing the correct element easier.

    INPUT:

    - ``key_conversion_function`` -- a function which will be
      applied to all method arguments which represent keys
    - ``data`` -- (optional) dictionary or sequence of key-value pairs
      to initialize this mapping

    EXAMPLES::

        sage: from sage.misc.converting_dict import KeyConvertingDict
        sage: d = KeyConvertingDict(int)
        sage: d["3"] = 42
        sage: list(d.items())
        [(3, 42)]
        sage: d[5.0] = 64
        sage: d["05"]
        64
    '''
    key_conversion_function: Incomplete
    def __init__(self, key_conversion_function, data=None) -> None:
        '''
        Construct a dictionary with a given conversion function.

        EXAMPLES::

            sage: from sage.misc.converting_dict import KeyConvertingDict
            sage: d = KeyConvertingDict(int)
            sage: d["3"] = 42
            sage: list(d.items())
            [(3, 42)]
            sage: list(KeyConvertingDict(int, {"5": 7}).items())
            [(5, 7)]
            sage: list(KeyConvertingDict(int, [("9", 99)]).items())
            [(9, 99)]
        '''
    def __getitem__(self, key):
        '''
        Retrieve an element from the dictionary.

        INPUT:

        - ``key`` -- a value identifying the element, will be converted

        EXAMPLES::

            sage: from sage.misc.converting_dict import KeyConvertingDict
            sage: d = KeyConvertingDict(int)
            sage: d[3] = 42
            sage: d["3"]
            42
        '''
    def __setitem__(self, key, value) -> None:
        '''
        Assign an element in the dictionary.

        INPUT:

        - ``key`` -- a value identifying the element, will be converted
        - ``value`` -- the associated value, will be left unmodified

        EXAMPLES::

            sage: from sage.misc.converting_dict import KeyConvertingDict
            sage: d = KeyConvertingDict(int)
            sage: d["3"] = 42
            sage: list(d.items())
            [(3, 42)]
        '''
    def __delitem__(self, key) -> None:
        '''
        Remove a mapping from the dictionary.

        INPUT:

        - ``key`` -- a value identifying the element, will be converted

        EXAMPLES::

            sage: from sage.misc.converting_dict import KeyConvertingDict
            sage: d = KeyConvertingDict(int)
            sage: d[3] = 42
            sage: del d["3"]
            sage: len(d)
            0
        '''
    def __contains__(self, key) -> bool:
        '''
        Test whether a given key is contained in the mapping.

        INPUT:

        - ``key`` -- a value identifying the element, will be converted

        EXAMPLES::

            sage: from sage.misc.converting_dict import KeyConvertingDict
            sage: d = KeyConvertingDict(int)
            sage: d[3] = 42
            sage: "3" in d
            True
            sage: 4 in d
            False
        '''
    def pop(self, key, *args):
        '''
        Remove and retrieve a given element from the dictionary.

        INPUT:

        - ``key`` -- a value identifying the element, will be converted
        - ``default`` -- the value to return if the element is not mapped, optional

        EXAMPLES::

            sage: from sage.misc.converting_dict import KeyConvertingDict
            sage: d = KeyConvertingDict(int)
            sage: d[3] = 42
            sage: d.pop("3")
            42
            sage: d.pop("3", 33)
            33
            sage: d.pop("3")
            Traceback (most recent call last):
            ...
            KeyError: ...
        '''
    def setdefault(self, key, default=None):
        '''
        Create a given mapping unless there already exists a mapping
        for that key.

        INPUT:

        - ``key`` -- a value identifying the element, will be converted
        - ``default`` -- the value to associate with the key

        EXAMPLES::

            sage: from sage.misc.converting_dict import KeyConvertingDict
            sage: d = KeyConvertingDict(int)
            sage: d.setdefault("3")
            sage: list(d.items())
            [(3, None)]
        '''
    def update(self, *args, **kwds) -> None:
        '''
        Update the dictionary with key-value pairs from another dictionary,
        sequence of key-value pairs, or keyword arguments.

        INPUT:

        - ``key`` -- a value identifying the element, will be converted
        - ``args`` -- a single dict or sequence of pairs
        - ``kwds`` -- named elements require that the conversion
          function accept strings

        EXAMPLES::

            sage: from sage.misc.converting_dict import KeyConvertingDict
            sage: d = KeyConvertingDict(int)
            sage: d.update([("3",1),(4,2)])
            sage: d[3]
            1
            sage: d.update({"5": 7, "9": 12})
            sage: d[9]
            12
            sage: d = KeyConvertingDict(QQ[\'x\'])
            sage: d.update(x=42)
            sage: d
            {x: 42}
        '''
