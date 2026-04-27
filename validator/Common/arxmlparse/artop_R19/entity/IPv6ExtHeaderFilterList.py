# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\IPv6ExtHeaderFilterList.py
from .Identifiable import Identifiable

class IPv6ExtHeaderFilterList(Identifiable):

    def __init__(self):
        super().__init__()
        from .IPv6ExtHeaderFilterSet import IPv6ExtHeaderFilterSet
        self._artop_allowedIPv6ExtHeader = None
        self._artop_iPv6ExtHeaderFilterSet = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_iPv6ExtHeaderFilterSet": "I-PV-6-EXT-HEADER-FILTER-SET"})

    @property
    def allowedIPv6ExtHeader_(self):
        return self._artop_allowedIPv6ExtHeader

    @property
    def ref_iPv6ExtHeaderFilterSet_(self):
        return self._artop_iPv6ExtHeaderFilterSet

    @property
    def iPv6ExtHeaderFilterSet_(self):
        if self._artop_iPv6ExtHeaderFilterSet is not None:
            if hasattr(self._artop_iPv6ExtHeaderFilterSet, "uuid"):
                return self._artop_iPv6ExtHeaderFilterSet.uuid
        return
