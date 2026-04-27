# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PortGroup.py
from .AtpStructureElement import AtpStructureElement

class PortGroup(AtpStructureElement):

    def __init__(self):
        super().__init__()
        from .SwComponentType import SwComponentType
        from .InnerPortGroupInCompositionInstanceRef import InnerPortGroupInCompositionInstanceRef
        from .PortPrototypeRefConditional import PortPrototypeRefConditional
        from .VariationPoint import VariationPoint
        self._artop_swComponentType = None
        self._artop_innerGroupIref = []
        self._artop_outerPort = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_swComponentType': '"SW-COMPONENT-TYPE"', 
         '_artop_innerGroupIref': '"INNER-PORT-GROUP-IN-COMPOSITION-INSTANCE-REF-IREF"', 
         '_artop_outerPort': '"PORT-PROTOTYPE-REF-CONDITIONAL"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def ref_swComponentType_(self):
        return self._artop_swComponentType

    @property
    def swComponentType_(self):
        if self._artop_swComponentType is not None:
            if hasattr(self._artop_swComponentType, "uuid"):
                return self._artop_swComponentType.uuid
        return

    @property
    def innerGroups_InnerPortGroupInCompositionInstanceRef(self):
        return self._artop_innerGroupIref

    @property
    def outerPorts_PortPrototypeRefConditional(self):
        return self._artop_outerPort

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
