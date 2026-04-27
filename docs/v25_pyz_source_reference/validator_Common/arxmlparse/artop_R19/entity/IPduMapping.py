# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\IPduMapping.py
from .ARObject import ARObject

class IPduMapping(ARObject):

    def __init__(self):
        super().__init__()
        from .Gateway import Gateway
        from .DocumentationBlock import DocumentationBlock
        from .PduTriggering import PduTriggering
        from .TargetIPduRef import TargetIPduRef
        from .VariationPoint import VariationPoint
        self._artop_pduMaxLength = None
        self._artop_pdurTpChunkSize = None
        self._artop_gateway = None
        self._artop_introduction = None
        self._artop_sourceIPduRef = None
        self._artop_targetIPdu = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_gateway': '"GATEWAY"', 
         '_artop_introduction': '"DOCUMENTATION-BLOCK"', 
         '_artop_sourceIPduRef': '"PDU-TRIGGERING"', 
         '_artop_targetIPdu': '"TARGET-I-PDU-REF"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def pduMaxLength_(self):
        return self._artop_pduMaxLength

    @property
    def pdurTpChunkSize_(self):
        return self._artop_pdurTpChunkSize

    @property
    def ref_gateway_(self):
        return self._artop_gateway

    @property
    def gateway_(self):
        if self._artop_gateway is not None:
            if hasattr(self._artop_gateway, "uuid"):
                return self._artop_gateway.uuid
        return

    @property
    def ref_introduction_(self):
        return self._artop_introduction

    @property
    def introduction_(self):
        if self._artop_introduction is not None:
            if hasattr(self._artop_introduction, "uuid"):
                return self._artop_introduction.uuid
        return

    @property
    def ref_sourceIPdu_(self):
        return self._artop_sourceIPduRef

    @property
    def sourceIPdu_(self):
        if self._artop_sourceIPduRef is not None:
            if hasattr(self._artop_sourceIPduRef, "uuid"):
                return self._artop_sourceIPduRef.uuid
        return

    @property
    def ref_targetIPdu_(self):
        return self._artop_targetIPdu

    @property
    def targetIPdu_(self):
        if self._artop_targetIPdu is not None:
            if hasattr(self._artop_targetIPdu, "uuid"):
                return self._artop_targetIPdu.uuid
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
