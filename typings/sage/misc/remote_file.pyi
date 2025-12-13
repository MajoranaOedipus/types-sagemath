from pathlib import Path

def get_remote_file(filename, verbose: bool = True) -> Path:
    '''
    INPUT:

    - ``filename`` -- the URL of a file on the web, e.g.,
      ``\'http://modular.math.washington.edu/myfile.txt\'``

    - ``verbose`` -- whether to display download status

    OUTPUT:

    This creates a file in the temp directory and returns the absolute path
    to that file as a :class:`Path` object.

    EXAMPLES::

        sage: url = \'https://www.sagemath.org/files/loadtest.py\'
        sage: g = get_remote_file(url, verbose=False)      # optional - internet
        sage: with open(g) as f: print(f.read())           # optional - internet
        print("hi from the net")
        <BLANKLINE>
        print(2 + 3)
    '''
