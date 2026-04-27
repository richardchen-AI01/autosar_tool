# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PortPrototypeRefConditional.py
from .ARObject import ARObject

class PortPrototypeRefConditional(ARObject):

    def __init__(self):
        super().__init__()
        from .PortGroup import PortGroup
        from .PortPrototype import PortPrototype
        from .VariationPoint import VariationPoint
        self._artop_portGroup = None
        self._artop_portPrototypeRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_portGroup':"PORT-GROUP", 
         '_artop_portPrototypeRef':"PORT-PROTOTYPE", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def ref_portGroup_(self):
        return self._artop_portGroup

    @property
    def portGroup_(self):
        if self._artop_portGroup is not None:
            if hasattr(self._artop_portGroup, "uuid"):
                return self._artop_portGroup.uuid
        return

    @property
    def ref_portPrototype_(self):
        return self._artop_portPrototypeRef

    @property
    def portPrototype_(self):
        if self._artop_portPrototypeRef is not None:
            if hasattr(self._artop_portPrototypeRef, "uuid"):
                return self._artop_portPrototypeRef.uuid
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
