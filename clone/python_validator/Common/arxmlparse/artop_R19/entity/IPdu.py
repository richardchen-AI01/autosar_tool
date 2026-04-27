# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\IPdu.py
from .Pdu import Pdu

class IPdu(Pdu):

    def __init__(self):
        super().__init__()
        from .ContainedIPduProps import ContainedIPduProps
        self._artop_containedIPduProps = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_containedIPduProps": "CONTAINED-I-PDU-PROPS"})

    @property
    def ref_containedIPduProps_(self):
        return self._artop_containedIPduProps

    @property
    def containedIPduProps_(self):
        if self._artop_containedIPduProps is not None:
            if hasattr(self._artop_containedIPduProps, "uuid"):
                return self._artop_containedIPduProps.uuid
        return
