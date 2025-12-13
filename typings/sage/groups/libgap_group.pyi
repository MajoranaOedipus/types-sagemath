from sage.groups.group import Group as Group
from sage.groups.libgap_mixin import GroupMixinLibGAP as GroupMixinLibGAP
from sage.groups.libgap_wrapper import ElementLibGAP as ElementLibGAP, ParentLibGAP as ParentLibGAP

class GroupLibGAP(GroupMixinLibGAP, Group, ParentLibGAP):
    Element = ElementLibGAP
    def __init__(self, *args, **kwds) -> None:
        """
        Group interface for LibGAP-based groups.

        INPUT:

        Same as :class:`~sage.groups.libgap_wrapper.ParentLibGAP`.

        TESTS::

            sage: F.<a,b> = FreeGroup()
            sage: G_gap = libgap.Group([ (a*b^2).gap() ])
            sage: from sage.groups.libgap_group import GroupLibGAP
            sage: G = GroupLibGAP(G_gap);  G
            Group([ a*b^2 ])
            sage: g = G.gen(0);  g
            a*b^2
            sage: TestSuite(G).run(skip=['_test_pickling', '_test_elements'])
            sage: TestSuite(g).run(skip=['_test_pickling'])
        """
