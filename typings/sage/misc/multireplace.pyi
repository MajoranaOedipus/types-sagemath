def multiple_replace(dic, text):
    '''
    Replace in \'text\' all occurrences of any key in the given
    dictionary by its corresponding value.  Returns the new string.

    EXAMPLES::

        sage: from sage.misc.multireplace import multiple_replace
        sage: txt = "This monkey really likes the bananas."
        sage: dic = {\'monkey\': \'penguin\', \'bananas\': \'fish\'}
        sage: multiple_replace(dic, txt)
        \'This penguin really likes the fish.\'
    '''
