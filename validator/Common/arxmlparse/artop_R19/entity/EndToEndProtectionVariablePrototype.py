# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EndToEndProtectionVariablePrototype.py
from .ARObject import ARObject

class EndToEndProtectionVariablePrototype(ARObject):

    def __init__(self):
        super().__init__()
        from .EndToEndProtection import EndToEndProtection
        from .VariableDataPrototypeInSystemInstanceRef import VariableDataPrototypeInSystemInstanceRef
        from .VariationPoint import VariationPoint
        self._artop_shortLabel = None
        self._artop_endToEndProtection = None
        self._artop_receiverIref = []
        self._artop_senderIref = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_endToEndProtection': '"END-TO-END-PROTECTION"', 
         '_artop_receiverIref': '"VARIABLE-DATA-PROTOTYPE-IN-SYSTEM-INSTANCE-REF-IREF"', 
         '_artop_senderIref': '"VARIABLE-DATA-PROTOTYPE-IN-SYSTEM-INSTANCE-REF-IREF"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def shortLabel_(self):
        return self._artop_shortLabel

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
    def receivers_VariableDataPrototypeInSystemInstanceRef(self):
        return self._artop_receiverIref

    @property
    def ref_sender_(self):
        return self._artop_senderIref

    @property
    def sender_(self):
        if self._artop_senderIref is not None:
            if hasattr(self._artop_senderIref, "uuid"):
                return self._artop_senderIref.uuid
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
