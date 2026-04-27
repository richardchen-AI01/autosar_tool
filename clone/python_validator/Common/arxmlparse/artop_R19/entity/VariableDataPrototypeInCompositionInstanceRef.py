# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\VariableDataPrototypeInCompositionInstanceRef.py
from .AtpInstanceRef import AtpInstanceRef

class VariableDataPrototypeInCompositionInstanceRef(AtpInstanceRef):

    def __init__(self):
        super().__init__()
        from .DataPrototypeGroup import DataPrototypeGroup
        from .CompositionSwComponentType import CompositionSwComponentType
        from .SwComponentPrototype import SwComponentPrototype
        from .PortPrototype import PortPrototype
        from .VariableDataPrototype import VariableDataPrototype
        from .VariationPoint import VariationPoint
        self._artop_dataPrototypeGroup = None
        self._artop_compositionSwComponentType = None
        self._artop_contextSwComponentPrototypeRef = []
        self._artop_contextPortPrototypeRef = None
        self._artop_targetVariableDataPrototypeRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_dataPrototypeGroup': '"DATA-PROTOTYPE-GROUP"', 
         '_artop_compositionSwComponentType': '"COMPOSITION-SW-COMPONENT-TYPE"', 
         '_artop_contextSwComponentPrototypeRef': '"SW-COMPONENT-PROTOTYPE"', 
         '_artop_contextPortPrototypeRef': '"PORT-PROTOTYPE"', 
         '_artop_targetVariableDataPrototypeRef': '"VARIABLE-DATA-PROTOTYPE"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def ref_dataPrototypeGroup_(self):
        return self._artop_dataPrototypeGroup

    @property
    def dataPrototypeGroup_(self):
        if self._artop_dataPrototypeGroup is not None:
            if hasattr(self._artop_dataPrototypeGroup, "uuid"):
                return self._artop_dataPrototypeGroup.uuid
        return

    @property
    def ref_base_(self):
        return self._artop_compositionSwComponentType

    @property
    def base_(self):
        if self._artop_compositionSwComponentType is not None:
            if hasattr(self._artop_compositionSwComponentType, "uuid"):
                return self._artop_compositionSwComponentType.uuid
        return

    @property
    def ref_contextSwComponentPrototypes_(self):
        return self._artop_contextSwComponentPrototypeRef

    @property
    def contextSwComponentPrototypes_(self):
        return self._artop_contextSwComponentPrototypeRef

    @property
    def ref_contextPortPrototype_(self):
        return self._artop_contextPortPrototypeRef

    @property
    def contextPortPrototype_(self):
        if self._artop_contextPortPrototypeRef is not None:
            if hasattr(self._artop_contextPortPrototypeRef, "uuid"):
                return self._artop_contextPortPrototypeRef.uuid
        return

    @property
    def ref_targetVariableDataPrototype_(self):
        return self._artop_targetVariableDataPrototypeRef

    @property
    def targetVariableDataPrototype_(self):
        if self._artop_targetVariableDataPrototypeRef is not None:
            if hasattr(self._artop_targetVariableDataPrototypeRef, "uuid"):
                return self._artop_targetVariableDataPrototypeRef.uuid
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
