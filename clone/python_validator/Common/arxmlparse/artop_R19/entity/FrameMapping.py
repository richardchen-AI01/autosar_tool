# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FrameMapping.py
from .ARObject import ARObject

class FrameMapping(ARObject):

    def __init__(self):
        super().__init__()
        from .Gateway import Gateway
        from .DocumentationBlock import DocumentationBlock
        from .FrameTriggering import FrameTriggering
        from .VariationPoint import VariationPoint
        self._artop_gateway = None
        self._artop_introduction = None
        self._artop_sourceFrameRef = None
        self._artop_targetFrameRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_gateway': '"GATEWAY"', 
         '_artop_introduction': '"DOCUMENTATION-BLOCK"', 
         '_artop_sourceFrameRef': '"FRAME-TRIGGERING"', 
         '_artop_targetFrameRef': '"FRAME-TRIGGERING"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

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
    def ref_sourceFrame_(self):
        return self._artop_sourceFrameRef

    @property
    def sourceFrame_(self):
        if self._artop_sourceFrameRef is not None:
            if hasattr(self._artop_sourceFrameRef, "uuid"):
                return self._artop_sourceFrameRef.uuid
        return

    @property
    def ref_targetFrame_(self):
        return self._artop_targetFrameRef

    @property
    def targetFrame_(self):
        if self._artop_targetFrameRef is not None:
            if hasattr(self._artop_targetFrameRef, "uuid"):
                return self._artop_targetFrameRef.uuid
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
