# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\NvBlockDataMapping.py
from .ARObject import ARObject

class NvBlockDataMapping(ARObject):

    def __init__(self):
        super().__init__()
        from .AutosarVariableRef import AutosarVariableRef
        from .VariationPoint import VariationPoint
        self._artop_bitfieldTextTableMaskNvBlockDescriptor = None
        self._artop_bitfieldTextTableMaskPortPrototype = None
        self._artop_nvRamBlockElement = None
        self._artop_readNvData = None
        self._artop_writtenNvData = None
        self._artop_writtenReadNvData = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_nvRamBlockElement': '"AUTOSAR-VARIABLE-REF"', 
         '_artop_readNvData': '"AUTOSAR-VARIABLE-REF"', 
         '_artop_writtenNvData': '"AUTOSAR-VARIABLE-REF"', 
         '_artop_writtenReadNvData': '"AUTOSAR-VARIABLE-REF"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def bitfieldTextTableMaskNvBlockDescriptor_(self):
        return self._artop_bitfieldTextTableMaskNvBlockDescriptor

    @property
    def bitfieldTextTableMaskPortPrototype_(self):
        return self._artop_bitfieldTextTableMaskPortPrototype

    @property
    def ref_nvRamBlockElement_(self):
        return self._artop_nvRamBlockElement

    @property
    def nvRamBlockElement_(self):
        if self._artop_nvRamBlockElement is not None:
            if hasattr(self._artop_nvRamBlockElement, "uuid"):
                return self._artop_nvRamBlockElement.uuid
        return

    @property
    def ref_readNvData_(self):
        return self._artop_readNvData

    @property
    def readNvData_(self):
        if self._artop_readNvData is not None:
            if hasattr(self._artop_readNvData, "uuid"):
                return self._artop_readNvData.uuid
        return

    @property
    def ref_writtenNvData_(self):
        return self._artop_writtenNvData

    @property
    def writtenNvData_(self):
        if self._artop_writtenNvData is not None:
            if hasattr(self._artop_writtenNvData, "uuid"):
                return self._artop_writtenNvData.uuid
        return

    @property
    def ref_writtenReadNvData_(self):
        return self._artop_writtenReadNvData

    @property
    def writtenReadNvData_(self):
        if self._artop_writtenReadNvData is not None:
            if hasattr(self._artop_writtenReadNvData, "uuid"):
                return self._artop_writtenReadNvData.uuid
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
