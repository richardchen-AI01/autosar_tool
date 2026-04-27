# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TransmissionModeCondition.py
from .ARObject import ARObject

class TransmissionModeCondition(ARObject):

    def __init__(self):
        super().__init__()
        from .TransmissionModeDeclaration import TransmissionModeDeclaration
        from .DataFilter import DataFilter
        from .ISignalToIPduMapping import ISignalToIPduMapping
        self._artop_transmissionModeDeclaration = None
        self._artop_dataFilter = None
        self._artop_iSignalInIPduRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_transmissionModeDeclaration':"TRANSMISSION-MODE-DECLARATION", 
         '_artop_dataFilter':"DATA-FILTER", 
         '_artop_iSignalInIPduRef':"I-SIGNAL-TO-I-PDU-MAPPING"})

    @property
    def ref_transmissionModeDeclaration_(self):
        return self._artop_transmissionModeDeclaration

    @property
    def transmissionModeDeclaration_(self):
        if self._artop_transmissionModeDeclaration is not None:
            if hasattr(self._artop_transmissionModeDeclaration, "uuid"):
                return self._artop_transmissionModeDeclaration.uuid
        return

    @property
    def ref_dataFilter_(self):
        return self._artop_dataFilter

    @property
    def dataFilter_(self):
        if self._artop_dataFilter is not None:
            if hasattr(self._artop_dataFilter, "uuid"):
                return self._artop_dataFilter.uuid
        return

    @property
    def ref_iSignalInIPdu_(self):
        return self._artop_iSignalInIPduRef

    @property
    def iSignalInIPdu_(self):
        if self._artop_iSignalInIPduRef is not None:
            if hasattr(self._artop_iSignalInIPduRef, "uuid"):
                return self._artop_iSignalInIPduRef.uuid
        return
