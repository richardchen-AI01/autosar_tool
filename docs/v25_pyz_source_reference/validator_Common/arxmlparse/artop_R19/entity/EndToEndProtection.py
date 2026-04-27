# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EndToEndProtection.py
from .Identifiable import Identifiable

class EndToEndProtection(Identifiable):

    def __init__(self):
        super().__init__()
        from .EndToEndProtectionSet import EndToEndProtectionSet
        from .EndToEndDescription import EndToEndDescription
        from .EndToEndProtectionISignalIPdu import EndToEndProtectionISignalIPdu
        from .EndToEndProtectionVariablePrototype import EndToEndProtectionVariablePrototype
        from .VariationPoint import VariationPoint
        self._artop_endToEndProtectionSet = None
        self._artop_endToEndProfile = None
        self._artop_endToEndProtectionISignalIPdu = []
        self._artop_endToEndProtectionVariablePrototype = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_endToEndProtectionSet': '"END-TO-END-PROTECTION-SET"', 
         '_artop_endToEndProfile': '"END-TO-END-DESCRIPTION"', 
         '_artop_endToEndProtectionISignalIPdu': '"END-TO-END-PROTECTION-I-SIGNAL-I-PDU"', 
         '_artop_endToEndProtectionVariablePrototype': '"END-TO-END-PROTECTION-VARIABLE-PROTOTYPE"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def ref_endToEndProtectionSet_(self):
        return self._artop_endToEndProtectionSet

    @property
    def endToEndProtectionSet_(self):
        if self._artop_endToEndProtectionSet is not None:
            if hasattr(self._artop_endToEndProtectionSet, "uuid"):
                return self._artop_endToEndProtectionSet.uuid
        return

    @property
    def ref_endToEndProfile_(self):
        return self._artop_endToEndProfile

    @property
    def endToEndProfile_(self):
        if self._artop_endToEndProfile is not None:
            if hasattr(self._artop_endToEndProfile, "uuid"):
                return self._artop_endToEndProfile.uuid
        return

    @property
    def endToEndProtectionISignalIPdus_EndToEndProtectionISignalIPdu(self):
        return self._artop_endToEndProtectionISignalIPdu

    @property
    def endToEndProtectionVariablePrototypes_EndToEndProtectionVariablePrototype(self):
        return self._artop_endToEndProtectionVariablePrototype

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
