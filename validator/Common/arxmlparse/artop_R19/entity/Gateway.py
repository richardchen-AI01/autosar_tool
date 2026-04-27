# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Gateway.py
from .FibexElement import FibexElement

class Gateway(FibexElement):

    def __init__(self):
        super().__init__()
        from .EcuInstance import EcuInstance
        from .FrameMapping import FrameMapping
        from .IPduMapping import IPduMapping
        from .ISignalMapping import ISignalMapping
        self._artop_ecuRef = None
        self._artop_frameMapping = []
        self._artop_iPduMapping = []
        self._artop_signalMapping = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_ecuRef': '"ECU-INSTANCE"', 
         '_artop_frameMapping': '"FRAME-MAPPING"', 
         '_artop_iPduMapping': '"I-PDU-MAPPING"', 
         '_artop_signalMapping': '"I-SIGNAL-MAPPING"'})

    @property
    def ref_ecu_(self):
        return self._artop_ecuRef

    @property
    def ecu_(self):
        if self._artop_ecuRef is not None:
            if hasattr(self._artop_ecuRef, "uuid"):
                return self._artop_ecuRef.uuid
        return

    @property
    def frameMappings_FrameMapping(self):
        return self._artop_frameMapping

    @property
    def iPduMappings_IPduMapping(self):
        return self._artop_iPduMapping

    @property
    def signalMappings_ISignalMapping(self):
        return self._artop_signalMapping
