# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PortInCompositionTypeInstanceRef.py
from .AtpInstanceRef import AtpInstanceRef

class PortInCompositionTypeInstanceRef(AtpInstanceRef):

    def __init__(self):
        super().__init__()
        from .DelegationSwConnector import DelegationSwConnector
        self._artop_delegationSwConnector = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_delegationSwConnector": "DELEGATION-SW-CONNECTOR"})

    @property
    def ref_delegationSwConnector_(self):
        return self._artop_delegationSwConnector

    @property
    def delegationSwConnector_(self):
        if self._artop_delegationSwConnector is not None:
            if hasattr(self._artop_delegationSwConnector, "uuid"):
                return self._artop_delegationSwConnector.uuid
        return
