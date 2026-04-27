# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\J1939NmNode.py
from .NmNode import NmNode

class J1939NmNode(NmNode):

    def __init__(self):
        super().__init__()
        from .J1939NodeName import J1939NodeName
        self._artop_nodeName = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_nodeName": "J-1939-NODE-NAME"})

    @property
    def ref_nodeName_(self):
        return self._artop_nodeName

    @property
    def nodeName_(self):
        if self._artop_nodeName is not None:
            if hasattr(self._artop_nodeName, "uuid"):
                return self._artop_nodeName.uuid
        return
