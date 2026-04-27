# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\J1939TpPg.py
from .ARObject import ARObject

class J1939TpPg(ARObject):

    def __init__(self):
        super().__init__()
        from .J1939TpConnection import J1939TpConnection
        from .NPdu import NPdu
        from .IPdu import IPdu
        self._artop_pgn = None
        self._artop_requestable = None
        self._artop_j1939TpConnection = None
        self._artop_directPduRef = None
        self._artop_sduRef = []
        self._artop_tpSduRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_j1939TpConnection': '"J-1939-TP-CONNECTION"', 
         '_artop_directPduRef': '"N-PDU"', 
         '_artop_sduRef': '"I-PDU"', 
         '_artop_tpSduRef': '"I-PDU"'})

    @property
    def pgn_(self):
        if self._artop_pgn:
            return int(self._artop_pgn)
        return self._artop_pgn

    @property
    def requestable_(self):
        if self._artop_requestable:
            if self._artop_requestable == "true":
                return True
            return False
        else:
            return self._artop_requestable

    @property
    def ref_j1939TpConnection_(self):
        return self._artop_j1939TpConnection

    @property
    def j1939TpConnection_(self):
        if self._artop_j1939TpConnection is not None:
            if hasattr(self._artop_j1939TpConnection, "uuid"):
                return self._artop_j1939TpConnection.uuid
        return

    @property
    def ref_directPdu_(self):
        return self._artop_directPduRef

    @property
    def directPdu_(self):
        if self._artop_directPduRef is not None:
            if hasattr(self._artop_directPduRef, "uuid"):
                return self._artop_directPduRef.uuid
        return

    @property
    def ref_sdus_(self):
        return self._artop_sduRef

    @property
    def sdus_(self):
        return self._artop_sduRef

    @property
    def ref_tpSdu_(self):
        return self._artop_tpSduRef

    @property
    def tpSdu_(self):
        if self._artop_tpSduRef is not None:
            if hasattr(self._artop_tpSduRef, "uuid"):
                return self._artop_tpSduRef.uuid
        return
