from sage.structure.sage_object import SageObject as SageObject

class OutputBuffer(SageObject):
    def __init__(self, data) -> None:
        '''
        Data stored either in memory or as a file.

        This class is an abstraction for "files", in that they can
        either be defined by a bytes array (Python 3) or string
        (Python 2) or by a file (see :meth:`from_file`).

        INPUT:

        - ``data`` -- bytes; the data that is stored in the buffer

        EXAMPLES::

            sage: from sage.repl.rich_output.buffer import OutputBuffer
            sage: buf = OutputBuffer(\'this is the buffer content\');  buf
            buffer containing 26 bytes

            sage: buf2 = OutputBuffer(buf);  buf2
            buffer containing 26 bytes

            sage: buf.get_str()
            \'this is the buffer content\'
            sage: buf.filename(ext=\'.txt\')
            \'/....txt\'
        '''
    @classmethod
    def from_file(cls, filename):
        """
        Construct buffer from data in file.

        .. WARNING::

            The buffer assumes that the file content remains the same
            during the lifetime of the Sage session. To communicate
            this to the user, the file permissions will be changed to
            read only.

        INPUT:

        - ``filename`` -- string; the filename under which the data is
          stored

        OUTPUT: string containing the buffer data

        EXAMPLES::

            sage: from sage.repl.rich_output.buffer import OutputBuffer
            sage: name = sage.misc.temporary_file.tmp_filename()
            sage: with open(name, 'wb') as f:
            ....:    _ = f.write(b'file content')
            sage: buf = OutputBuffer.from_file(name);  buf
            buffer containing 12 bytes

            sage: buf.filename() == name
            True
            sage: buf.get_str()
            'file content'
        """
    def get(self):
        """
        Return the buffer content.

        OUTPUT: bytes; string in Python 2.x

        EXAMPLES::

            sage: from sage.repl.rich_output.buffer import OutputBuffer
            sage: c = OutputBuffer('test1234').get(); c.decode('ascii')
            'test1234'
            sage: type(c) is bytes
            True
            sage: c = OutputBuffer('été').get()
            sage: type(c) is bytes
            True
        """
    def get_unicode(self):
        """
        Return the buffer content as string.

        OUTPUT:

        String. Unicode in Python 2.x. Raises a :exc:`UnicodeEncodeError`
        if the data is not valid utf-8.

        EXAMPLES::

            sage: from sage.repl.rich_output.buffer import OutputBuffer
            sage: OutputBuffer('test1234').get().decode('ascii')
            'test1234'
            sage: OutputBuffer('test1234').get_unicode()
            'test1234'
        """
    def get_str(self):
        """
        Return the buffer content as a ``str`` object for the current Python
        version.

        That is, returns a Python 2-style encoding-agnostic ``str`` on Python
        2, and returns a unicode ``str`` on Python 3 with the buffer content
        decoded from UTF-8.  In other words, this is equivalent to
        ``OutputBuffer.get`` on Python 2 and ``OutputBuffer.get_unicode`` on
        Python 3.  This is useful in some cases for cross-compatible code.

        OUTPUT: a ``str`` object

        EXAMPLES::

            sage: from sage.repl.rich_output.buffer import OutputBuffer
            sage: c = OutputBuffer('test1234').get_str(); c
            'test1234'
            sage: type(c) is str
            True
            sage: c = OutputBuffer('été').get_str()
            sage: type(c) is str
            True
        """
    def filename(self, ext=None):
        """
        Return the filename.

        INPUT:

        - ``ext`` -- string; the file extension

        OUTPUT:

        Name of a file, most likely a temporary file. If ``ext`` is
        specified, the filename will have that extension.

        You must not modify the returned file. Its permissions are set
        to readonly to help with that.

        EXAMPLES::

            sage: from sage.repl.rich_output.buffer import OutputBuffer
            sage: buf = OutputBuffer('test')
            sage: buf.filename()           # random output
            '/home/user/.sage/temp/hostname/26085/tmp_RNSfAc'

            sage: os.path.isfile(buf.filename())
            True
            sage: buf.filename(ext='txt')  # random output
            '/home/user/.sage/temp/hostname/26085/tmp_Rjjp4V.txt'
            sage: buf.filename(ext='txt').endswith('.txt')
            True
        """
    def save_as(self, filename) -> None:
        """
        Save a copy of the buffer content.

        You may edit the returned file, unlike the file returned by
        :meth:`filename`.

        INPUT:

        - ``filename`` -- string; the file name to save under

        EXAMPLES::

            sage: from sage.repl.rich_output.buffer import OutputBuffer
            sage: buf = OutputBuffer('test')
            sage: buf.filename(ext='txt')  # random output
            sage: tmp = tmp_dir()
            sage: filename = os.path.join(tmp, 'foo.txt')
            sage: buf.save_as(filename)
            sage: with open(filename, 'r') as f:
            ....:     f.read()
            'test'
        """
