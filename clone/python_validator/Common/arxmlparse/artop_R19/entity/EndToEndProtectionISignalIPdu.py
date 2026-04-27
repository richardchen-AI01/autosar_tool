# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EndToEndProtectionISignalIPdu.py
from .ARObject import ARObject

class EndToEndProtectionISignalIPdu(ARObject):

    def __init__(self):
        super().__init__()
        from .EndToEndProtection import EndToEndProtection
        from .ISignalGroup import ISignalGroup
        from .ISignalIPdu import ISignalIPdu
        from .VariationPoint import VariationPoint
        self._artop_dataOffset = None
        self._artop_endToEndProtection = None
        self._artop_iSignalGroupRef = None
        self._artop_iSignalIPduRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_endToEndProtection': '"END-TO-END-PROTECTION"', 
         '_artop_iSignalGroupRef': '"I-SIGNAL-GROUP"', 
         '_artop_iSignalIPduRef': '"I-SIGNAL-I-PDU"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def dataOffset_(self):
        if self._artop_dataOffset:
            return int(self._artop_dataOffset)
        return self._artop_dataOffset

    @property
    def ref_endToEndProtection_(self):
        return self._artop_endToEndProtection

    @property
    def endToEndProtection_(self):
        if self._artop_endToEndProtection is not None:
            if hasattr(self._artop_endToEndProtection, "uuid"):
                return self._artop_endToEndProtection.uuid
        return

    @property
    def ref_iSignalGroup_(self):
        return self._artop_iSignalGroupRef

    @property
    def iSignalGroup_(self):
        if self._artop_iSignalGroupRef is not None:
            if hasattr(self._artop_iSignalGroupRef, "uuid"):
                return self._artop_iSignalGroupRef.uuid
        return

    @property
    def ref_iSignalIPdu_(self):
        return self._artop_iSignalIPduRef

    @property
    def iSignalIPdu_(self):
        if self._artop_iSignalIPduRef is not None:
            if hasattr(self._artop_iSignalIPduRef, "uuid"):
                return self._artop_iSignalIPduRef.uuid
        return

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
