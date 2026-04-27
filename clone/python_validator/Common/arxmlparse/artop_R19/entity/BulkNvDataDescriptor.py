# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BulkNvDataDescriptor.py
from .AtpStructureElement import AtpStructureElement

class BulkNvDataDescriptor(AtpStructureElement):

    def __init__(self):
        super().__init__()
        from .NvBlockSwComponentType import NvBlockSwComponentType
        from .VariableDataPrototype import VariableDataPrototype
        from .NvBlockDataMapping import NvBlockDataMapping
        from .VariationPoint import VariationPoint
        self._artop_nvBlockSwComponentType = None
        self._artop_bulkNvBlock = None
        self._artop_nvBlockDataMapping = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_nvBlockSwComponentType': '"NV-BLOCK-SW-COMPONENT-TYPE"', 
         '_artop_bulkNvBlock': '"VARIABLE-DATA-PROTOTYPE"', 
         '_artop_nvBlockDataMapping': '"NV-BLOCK-DATA-MAPPING"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def ref_nvBlockSwComponentType_(self):
        return self._artop_nvBlockSwComponentType

    @property
    def nvBlockSwComponentType_(self):
        if self._artop_nvBlockSwComponentType is not None:
            if hasattr(self._artop_nvBlockSwComponentType, "uuid"):
                return self._artop_nvBlockSwComponentType.uuid
        return

    @property
    def ref_bulkNvBlock_(self):
        return self._artop_bulkNvBlock

    @property
    def bulkNvBlock_(self):
        if self._artop_bulkNvBlock is not None:
            if hasattr(self._artop_bulkNvBlock, "uuid"):
                return self._artop_bulkNvBlock.uuid
        return

    @property
    def nvBlockDataMappings_NvBlockDataMapping(self):
        return self._artop_nvBlockDataMapping

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
