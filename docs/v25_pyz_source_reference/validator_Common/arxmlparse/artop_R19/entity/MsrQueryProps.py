# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\MsrQueryProps.py
from .ARObject import ARObject

class MsrQueryProps(ARObject):

    def __init__(self):
        super().__init__()
        from .MsrQueryArg import MsrQueryArg
        self._artop_msrQueryName = None
        self._artop_comment = None
        self._artop_msrQueryArg = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_msrQueryArg": "MSR-QUERY-ARG"})

    @property
    def msrQueryName_(self):
        return self._artop_msrQueryName

    @property
    def comment_(self):
        return self._artop_comment

    @property
    def msrQueryArgs_MsrQueryArg(self):
        return self._artop_msrQueryArg
