# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwConnector.py
from .AtpStructureElement import AtpStructureElement

class SwConnector(AtpStructureElement):

    def __init__(self):
        super().__init__()
        from .CompositionSwComponentType import CompositionSwComponentType
        from .PortInterfaceMapping import PortInterfaceMapping
        from .VariationPoint import VariationPoint
        self._artop_compositionSwComponentType = None
        self._artop_mappingRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_compositionSwComponentType':"COMPOSITION-SW-COMPONENT-TYPE", 
         '_artop_mappingRef':"PORT-INTERFACE-MAPPING", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def ref_compositionSwComponentType_(self):
        return self._artop_compositionSwComponentType

    @property
    def compositionSwComponentType_(self):
        if self._artop_compositionSwComponentType is not None:
            if hasattr(self._artop_compositionSwComponentType, "uuid"):
                return self._artop_compositionSwComponentType.uuid
        return

    @property
    def ref_mapping_(self):
        return self._artop_mappingRef

    @property
    def mapping_(self):
        if self._artop_mappingRef is not None:
            if hasattr(self._artop_mappingRef, "uuid"):
                return self._artop_mappingRef.uuid
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
