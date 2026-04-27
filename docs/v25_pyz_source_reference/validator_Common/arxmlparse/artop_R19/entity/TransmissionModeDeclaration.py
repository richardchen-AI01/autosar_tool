# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TransmissionModeDeclaration.py
from .ARObject import ARObject

class TransmissionModeDeclaration(ARObject):

    def __init__(self):
        super().__init__()
        from .IPduTiming import IPduTiming
        from .ModeDrivenTransmissionModeCondition import ModeDrivenTransmissionModeCondition
        from .TransmissionModeCondition import TransmissionModeCondition
        from .TransmissionModeTiming import TransmissionModeTiming
        self._artop_iPduTiming = None
        self._artop_modeDrivenFalseCondition = []
        self._artop_modeDrivenTrueCondition = []
        self._artop_transmissionModeCondition = []
        self._artop_transmissionModeFalseTiming = None
        self._artop_transmissionModeTrueTiming = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_iPduTiming': '"I-PDU-TIMING"', 
         '_artop_modeDrivenFalseCondition': '"MODE-DRIVEN-TRANSMISSION-MODE-CONDITION"', 
         '_artop_modeDrivenTrueCondition': '"MODE-DRIVEN-TRANSMISSION-MODE-CONDITION"', 
         '_artop_transmissionModeCondition': '"TRANSMISSION-MODE-CONDITION"', 
         '_artop_transmissionModeFalseTiming': '"TRANSMISSION-MODE-TIMING"', 
         '_artop_transmissionModeTrueTiming': '"TRANSMISSION-MODE-TIMING"'})

    @property
    def ref_iPduTiming_(self):
        return self._artop_iPduTiming

    @property
    def iPduTiming_(self):
        if self._artop_iPduTiming is not None:
            if hasattr(self._artop_iPduTiming, "uuid"):
                return self._artop_iPduTiming.uuid
        return

    @property
    def modeDrivenFalseConditions_ModeDrivenTransmissionModeCondition(self):
        return self._artop_modeDrivenFalseCondition

    @property
    def modeDrivenTrueConditions_ModeDrivenTransmissionModeCondition(self):
        return self._artop_modeDrivenTrueCondition

    @property
    def transmissionModeConditions_TransmissionModeCondition(self):
        return self._artop_transmissionModeCondition

    @property
    def ref_transmissionModeFalseTiming_(self):
        return self._artop_transmissionModeFalseTiming

    @property
    def transmissionModeFalseTiming_(self):
        if self._artop_transmissionModeFalseTiming is not None:
            if hasattr(self._artop_transmissionModeFalseTiming, "uuid"):
                return self._artop_transmissionModeFalseTiming.uuid
        return

    @property
    def ref_transmissionModeTrueTiming_(self):
        return self._artop_transmissionModeTrueTiming

    @property
    def transmissionModeTrueTiming_(self):
        if self._artop_transmissionModeTrueTiming is not None:
            if hasattr(self._artop_transmissionModeTrueTiming, "uuid"):
                return self._artop_transmissionModeTrueTiming.uuid
        return
