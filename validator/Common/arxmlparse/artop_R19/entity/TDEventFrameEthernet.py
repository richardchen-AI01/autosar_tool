# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TDEventFrameEthernet.py
from .TDEventCom import TDEventCom

class TDEventFrameEthernet(TDEventCom):

    def __init__(self):
        super().__init__()
        from .SocketConnectionBundle import SocketConnectionBundle
        from .StaticSocketConnection import StaticSocketConnection
        from .TDHeaderIdRange import TDHeaderIdRange
        from .PduTriggering import PduTriggering
        self._artop_tdEventType = None
        self._artop_socketConnectionBundleRef = None
        self._artop_staticSocketConnectionRef = None
        self._artop_tdHeaderIdFilter = []
        self._artop_tdPduTriggeringFilterRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_socketConnectionBundleRef': '"SOCKET-CONNECTION-BUNDLE"', 
         '_artop_staticSocketConnectionRef': '"STATIC-SOCKET-CONNECTION"', 
         '_artop_tdHeaderIdFilter': '"TD-HEADER-ID-RANGE"', 
         '_artop_tdPduTriggeringFilterRef': '"PDU-TRIGGERING"'})

    @property
    def tdEventType_(self):
        return self._artop_tdEventType

    @property
    def ref_socketConnectionBundle_(self):
        return self._artop_socketConnectionBundleRef

    @property
    def socketConnectionBundle_(self):
        if self._artop_socketConnectionBundleRef is not None:
            if hasattr(self._artop_socketConnectionBundleRef, "uuid"):
                return self._artop_socketConnectionBundleRef.uuid
        return

    @property
    def ref_staticSocketConnection_(self):
        return self._artop_staticSocketConnectionRef

    @property
    def staticSocketConnection_(self):
        if self._artop_staticSocketConnectionRef is not None:
            if hasattr(self._artop_staticSocketConnectionRef, "uuid"):
                return self._artop_staticSocketConnectionRef.uuid
        return

    @property
    def tdHeaderIdFilters_TDHeaderIdRange(self):
        return self._artop_tdHeaderIdFilter

    @property
    def ref_tdPduTriggeringFilters_(self):
        return self._artop_tdPduTriggeringFilterRef

    @property
    def tdPduTriggeringFilters_(self):
        return self._artop_tdPduTriggeringFilterRef
