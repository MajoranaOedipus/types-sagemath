from _typeshed import Incomplete
from sage.misc.temporary_file import tmp_filename as tmp_filename

XML_NAMESPACE: str
DTRS_PROTOCOL: str
v2_b2_k2_icgsa: str

def dump_to_tmpfile(s):
    '''
    Utility function to dump a string to a temporary file.

    EXAMPLES::

        sage: from sage.combinat.designs import ext_rep
        sage: file_loc = ext_rep.dump_to_tmpfile("boo")
        sage: os.remove(file_loc)
    '''
def check_dtrs_protocols(input_name, input_pv) -> None:
    """
    Check that the XML data is in a valid format. We can currently
    handle version 2.0. For more information see
    http://designtheory.org/library/extrep/

    EXAMPLES::

        sage: from sage.combinat.designs import ext_rep
        sage: ext_rep.check_dtrs_protocols('source', '2.0')
        sage: ext_rep.check_dtrs_protocols('source', '3.0')
        Traceback (most recent call last):
        ...
        RuntimeError: Incompatible dtrs_protocols: program: 2.0 source: 3.0
    """
def open_extrep_file(fname):
    """
    Try to guess the compression type from extension
    and open the extrep file.

    EXAMPLES::

        sage: from sage.combinat.designs import ext_rep
        sage: file_loc = ext_rep.dump_to_tmpfile(ext_rep.v2_b2_k2_icgsa)
        sage: proc = ext_rep.XTreeProcessor()
        sage: f = ext_rep.open_extrep_file(file_loc)
        sage: proc.parse(f)
        sage: f.close()
        sage: os.remove(file_loc)
    """
def open_extrep_url(url):
    '''
    Try to guess the compression type from extension
    and open the extrep file pointed to by the url. This function
    (unlike open_extrep_file) returns the uncompressed text contained in
    the file.

    EXAMPLES::

        sage: from sage.combinat.designs import ext_rep
        sage: file_loc = ext_rep.dump_to_tmpfile(ext_rep.v2_b2_k2_icgsa)
        sage: proc = ext_rep.XTreeProcessor()
        sage: s = ext_rep.open_extrep_url("file://" + file_loc)
        sage: proc.parse(s)
        sage: os.remove(file_loc)

        sage: from sage.combinat.designs import ext_rep
        sage: s = ext_rep.designs_from_XML_url("http://designtheory.org/database/v-b-k/v3-b6-k2.icgsa.txt.bz2") # optional - internet
    '''

pattern_integer: Incomplete
pattern_decimal: Incomplete
pattern_rational: Incomplete

class XTree:
    """
    A lazy class to wrap a rooted tree representing an XML document.
    The tree's nodes are tuples of the structure:
    (name, {dictionary of attributes}, [list of children])

    Methods and services of an XTree object ``t``:

    - ``t.attribute`` -- attribute named
    - ``t.child`` -- first child named
    - ``t[i]`` -- `i`-th child
    - ``for child in t:`` -- iterate over ``t``'s children
    - ``len(t)`` -- number of ``t``'s children

    If child is not an empty subtree, return the subtree as an ``XTree``
    object. If child is an empty subtree, return ``_name`` of the subtree.
    Otherwise return the child itself.

    The lazy tree idea originated from a utility class of the
    pyRXP 0.9 package by Robin Becker at ReportLab.
    """
    xt_node: Incomplete
    xt_name: Incomplete
    xt_attributes: Incomplete
    xt_children: Incomplete
    def __init__(self, node) -> None:
        """
        Initialisation method given a node in an XML document.

        EXAMPLES::

            sage: from sage.combinat.designs.ext_rep import *
            sage: xt = XTree(('blocks', {'ordered': 'true'}, [('block', {}, [[0, 1, 2]]), ('block', {}, [[0, 3, 4]]), ('block', {}, [[0, 5, 6]]), ('block', {}, [[0, 7, 8]]), ('block', {}, [[0, 9, 10]]), ('block', {}, [[0, 11, 12]]), ('block', {}, [[1, 3, 5]]), ('block', {}, [[1, 4, 6]]), ('block', {}, [[1, 7, 9]]), ('block', {}, [[1, 8, 11]]), ('block', {}, [[1, 10, 12]]), ('block', {}, [[2, 3, 7]]), ('block', {}, [[2, 4, 8]]), ('block', {}, [[2, 5, 10]]), ('block', {}, [[2, 6, 12]]), ('block', {}, [[2, 9, 11]]), ('block', {}, [[3, 6, 9]]), ('block', {}, [[3, 8, 12]]), ('block', {}, [[3, 10, 11]]), ('block', {}, [[4, 5, 11]]), ('block', {}, [[4, 7, 10]]), ('block', {}, [[4, 9, 12]]), ('block', {}, [[5, 7, 12]]), ('block', {}, [[5, 8, 9]]), ('block', {}, [[6, 7, 11]]), ('block', {}, [[6, 8, 10]])]))
            sage: xt.xt_children
            [('block', {}, [[0, 1, 2]]),
             ('block', {}, [[0, 3, 4]]),
             ('block', {}, [[0, 5, 6]]),
             ('block', {}, [[0, 7, 8]]),
             ('block', {}, [[0, 9, 10]]),
             ('block', {}, [[0, 11, 12]]),
             ('block', {}, [[1, 3, 5]]),
             ('block', {}, [[1, 4, 6]]),
             ('block', {}, [[1, 7, 9]]),
             ('block', {}, [[1, 8, 11]]),
             ('block', {}, [[1, 10, 12]]),
             ('block', {}, [[2, 3, 7]]),
             ('block', {}, [[2, 4, 8]]),
             ('block', {}, [[2, 5, 10]]),
             ('block', {}, [[2, 6, 12]]),
             ('block', {}, [[2, 9, 11]]),
             ('block', {}, [[3, 6, 9]]),
             ('block', {}, [[3, 8, 12]]),
             ('block', {}, [[3, 10, 11]]),
             ('block', {}, [[4, 5, 11]]),
             ('block', {}, [[4, 7, 10]]),
             ('block', {}, [[4, 9, 12]]),
             ('block', {}, [[5, 7, 12]]),
             ('block', {}, [[5, 8, 9]]),
             ('block', {}, [[6, 7, 11]]),
             ('block', {}, [[6, 8, 10]])]
        """
    def __getattr__(self, attr):
        """
        Return the data for the first attribute with name attr.

        EXAMPLES::

            sage: from sage.combinat.designs.ext_rep import *
            sage: xt = XTree(('blocks', {'ordered': 'true'}, [('block', {}, [[0, 1, 2]]), ('block', {}, [[0, 3, 4]]), ('block', {}, [[0, 5, 6]]), ('block', {}, [[0, 7, 8]]), ('block', {}, [[0, 9, 10]]), ('block', {}, [[0, 11, 12]]), ('block', {}, [[1, 3, 5]]), ('block', {}, [[1, 4, 6]]), ('block', {}, [[1, 7, 9]]), ('block', {}, [[1, 8, 11]]), ('block', {}, [[1, 10, 12]]), ('block', {}, [[2, 3, 7]]), ('block', {}, [[2, 4, 8]]), ('block', {}, [[2, 5, 10]]), ('block', {}, [[2, 6, 12]]), ('block', {}, [[2, 9, 11]]), ('block', {}, [[3, 6, 9]]), ('block', {}, [[3, 8, 12]]), ('block', {}, [[3, 10, 11]]), ('block', {}, [[4, 5, 11]]), ('block', {}, [[4, 7, 10]]), ('block', {}, [[4, 9, 12]]), ('block', {}, [[5, 7, 12]]), ('block', {}, [[5, 8, 9]]), ('block', {}, [[6, 7, 11]]), ('block', {}, [[6, 8, 10]])]))
            sage: xt.__getattr__('block')
            [0, 1, 2]
        """
    def __getitem__(self, i):
        """
        Get the ``i``-th item in the current node.

        EXAMPLES::

            sage: from sage.combinat.designs.ext_rep import *
            sage: xt = XTree(('blocks', {'ordered': 'true'}, [('block', {}, [[0, 1, 2]]), ('block', {}, [[0, 3, 4]]), ('block', {}, [[0, 5, 6]]), ('block', {}, [[0, 7, 8]]), ('block', {}, [[0, 9, 10]]), ('block', {}, [[0, 11, 12]]), ('block', {}, [[1, 3, 5]]), ('block', {}, [[1, 4, 6]]), ('block', {}, [[1, 7, 9]]), ('block', {}, [[1, 8, 11]]), ('block', {}, [[1, 10, 12]]), ('block', {}, [[2, 3, 7]]), ('block', {}, [[2, 4, 8]]), ('block', {}, [[2, 5, 10]]), ('block', {}, [[2, 6, 12]]), ('block', {}, [[2, 9, 11]]), ('block', {}, [[3, 6, 9]]), ('block', {}, [[3, 8, 12]]), ('block', {}, [[3, 10, 11]]), ('block', {}, [[4, 5, 11]]), ('block', {}, [[4, 7, 10]]), ('block', {}, [[4, 9, 12]]), ('block', {}, [[5, 7, 12]]), ('block', {}, [[5, 8, 9]]), ('block', {}, [[6, 7, 11]]), ('block', {}, [[6, 8, 10]])]))
            sage: xt.__getitem__(0)
            [0, 1, 2]
            sage: xt.__getitem__(1)
            [0, 3, 4]

        TESTS::

            sage: xt.__getitem__(119)
            Traceback (most recent call last):
            ...
            IndexError: XTree<blocks> has no index 119
        """
    def __len__(self) -> int:
        """
        Return the length of the current node.

        EXAMPLES::

            sage: from sage.combinat.designs.ext_rep import *
            sage: xt = XTree(('blocks', {'ordered': 'true'}, [('block', {}, [[0, 1, 2]]), ('block', {}, [[0, 3, 4]]), ('block', {}, [[0, 5, 6]]), ('block', {}, [[0, 7, 8]]), ('block', {}, [[0, 9, 10]]), ('block', {}, [[0, 11, 12]]), ('block', {}, [[1, 3, 5]]), ('block', {}, [[1, 4, 6]]), ('block', {}, [[1, 7, 9]]), ('block', {}, [[1, 8, 11]]), ('block', {}, [[1, 10, 12]]), ('block', {}, [[2, 3, 7]]), ('block', {}, [[2, 4, 8]]), ('block', {}, [[2, 5, 10]]), ('block', {}, [[2, 6, 12]]), ('block', {}, [[2, 9, 11]]), ('block', {}, [[3, 6, 9]]), ('block', {}, [[3, 8, 12]]), ('block', {}, [[3, 10, 11]]), ('block', {}, [[4, 5, 11]]), ('block', {}, [[4, 7, 10]]), ('block', {}, [[4, 9, 12]]), ('block', {}, [[5, 7, 12]]), ('block', {}, [[5, 8, 9]]), ('block', {}, [[6, 7, 11]]), ('block', {}, [[6, 8, 10]])]))
            sage: xt.__len__()
            26
        """

class XTreeProcessor:
    """
    An incremental event-driven parser for ext-rep documents.
    The processing stages:

    - ``<list_of_designs ...>`` opening element.
      call-back: ``list_of_designs_proc``

    - ``<list_definition>`` subtree.
      call-back: ``list_definition_proc``

    - ``<info>`` subtree.
      call-back: ``info_proc``

    - iterating over ``<designs>`` processing each ``<block_design>``
      separately.
      call-back: ``block_design_proc``

    - finishing with closing ``</designs>`` and ``</list_of_designs>``.
    """
    outf: Incomplete
    list_of_designs_start_proc: Incomplete
    list_definition_proc: Incomplete
    info_proc: Incomplete
    designs_start_proc: Incomplete
    block_design_proc: Incomplete
    designs_end_proc: Incomplete
    list_of_designs_end_proc: Incomplete
    save_designs: bool
    list_of_designs: Incomplete
    def __init__(self) -> None:
        """
        Internal initialisation for the processor of XTrees.

        EXAMPLES::

            sage: from sage.combinat.designs.ext_rep import *
            sage: proc = XTreeProcessor()
            sage: proc.current_node
            ('root0', {}, [])
            sage: proc.node_stack
            [('root0', {}, [])]
            sage: proc.in_item
            False
        """
    def parse(self, xml_source) -> None:
        """
        The main parsing function. Given an XML source (either a file
        handle or a string), parse the entire XML source.

        EXAMPLES::

            sage: from sage.combinat.designs import ext_rep
            sage: file_loc = ext_rep.dump_to_tmpfile(ext_rep.v2_b2_k2_icgsa)
            sage: proc = ext_rep.XTreeProcessor()
            sage: proc.save_designs = True
            sage: f = ext_rep.open_extrep_file(file_loc)
            sage: proc.parse(f)
            sage: f.close()
            sage: os.remove(file_loc)
            sage: proc.list_of_designs[0]
            (2, [[0, 1], [0, 1]])
        """

def designs_from_XML(fname):
    """
    Return a list of designs contained in an XML file fname. The list
    contains tuples of the form (v, bs) where v is the number of points of
    the design and bs is the list of blocks.

    EXAMPLES::

        sage: from sage.combinat.designs import ext_rep
        sage: file_loc = ext_rep.dump_to_tmpfile(ext_rep.v2_b2_k2_icgsa)
        sage: ext_rep.designs_from_XML(file_loc)[0]
        (2, [[0, 1], [0, 1]])
        sage: os.remove(file_loc)

        sage: from sage.combinat.designs import ext_rep
        sage: from sage.combinat.designs.block_design import BlockDesign
        sage: file_loc = ext_rep.dump_to_tmpfile(ext_rep.v2_b2_k2_icgsa)
        sage: v, blocks = ext_rep.designs_from_XML(file_loc)[0]
        sage: d = BlockDesign(v, blocks)
        sage: d.blocks()
        [[0, 1], [0, 1]]
        sage: d.is_t_design(t=2)
        True
        sage: d.is_t_design(return_parameters=True)
        (True, (2, 2, 2, 2))
    """
def designs_from_XML_url(url):
    '''
    Return a list of designs contained in an XML file named by a URL.
    The list contains tuples of the form (v, bs) where v is the number
    of points of the design and bs is the list of blocks.

    EXAMPLES::

        sage: from sage.combinat.designs import ext_rep
        sage: file_loc = ext_rep.dump_to_tmpfile(ext_rep.v2_b2_k2_icgsa)
        sage: ext_rep.designs_from_XML_url("file://" + file_loc)[0]
        (2, [[0, 1], [0, 1]])
        sage: os.remove(file_loc)

        sage: from sage.combinat.designs import ext_rep
        sage: ext_rep.designs_from_XML_url("http://designtheory.org/database/v-b-k/v3-b6-k2.icgsa.txt.bz2") # optional - internet
        [(3, [[0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 2]]),
         (3, [[0, 1], [0, 1], [0, 1], [0, 1], [0, 2], [0, 2]]),
         (3, [[0, 1], [0, 1], [0, 1], [0, 1], [0, 2], [1, 2]]),
         (3, [[0, 1], [0, 1], [0, 1], [0, 2], [0, 2], [0, 2]]),
         (3, [[0, 1], [0, 1], [0, 1], [0, 2], [0, 2], [1, 2]]),
         (3, [[0, 1], [0, 1], [0, 2], [0, 2], [1, 2], [1, 2]])]
    '''
