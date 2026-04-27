# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticRequestPowertrainFreezeFrameData.py
from .DiagnosticServiceInstance import DiagnosticServiceInstance

class DiagnosticRequestPowertrainFreezeFrameData(DiagnosticServiceInstance):

    def __init__(self):
        super().__init__()
        from .DiagnosticPowertrainFreezeFrame import DiagnosticPowertrainFreezeFrame
        from .DiagnosticRequestPowertrainFreezeFrameDataClass import DiagnosticRequestPowertrainFreezeFrameDataClass
        self._artop_freezeFrameRef = None
        self._artop_requestPowertrainFreezeFrameDataRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_freezeFrameRef':"DIAGNOSTIC-POWERTRAIN-FREEZE-FRAME", 
         '_artop_requestPowertrainFreezeFrameDataRef':"DIAGNOSTIC-REQUEST-POWERTRAIN-FREEZE-FRAME-DATA-CLASS"})

    @property
    def ref_freezeFrame_(self):
        return self._artop_freezeFrameRef

    @property
    def freezeFrame_(self):
        if self._artop_freezeFrameRef is not None:
            if hasattr(self._artop_freezeFrameRef, "uuid"):
                return self._artop_freezeFrameRef.uuid
        return

    @property
    def ref_requestPowertrainFreezeFrameData_(self):
        return self._artop_requestPowertrainFreezeFrameDataRef

    @property
    def requestPowertrainFreezeFrameData_(self):
        if self._artop_requestPowertrainFreezeFrameDataRef is not None:
            if hasattr(self._artop_requestPowertrainFreezeFrameDataRef, "uuid"):
                return self._artop_requestPowertrainFreezeFrameDataRef.uuid
        return
