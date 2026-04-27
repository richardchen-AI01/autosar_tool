# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ApplicationRecordElement.py
from .ApplicationCompositeElementDataPrototype import ApplicationCompositeElementDataPrototype

class ApplicationRecordElement(ApplicationCompositeElementDataPrototype):

    def __init__(self):
        super().__init__()
        from .ApplicationRecordDataType import ApplicationRecordDataType
        from .VariationPoint import VariationPoint
        self._artop_isOptional = None
        self._artop_applicationRecordDataType = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_applicationRecordDataType':"APPLICATION-RECORD-DATA-TYPE", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def isOptional_(self):
        if self._artop_isOptional:
            if self._artop_isOptional == "true":
                return True
            return False
        else:
            return self._artop_isOptional

    @property
    def ref_applicationRecordDataType_(self):
        return self._artop_applicationRecordDataType

    @property
    def applicationRecordDataType_(self):
        if self._artop_applicationRecordDataType is not None:
            if hasattr(self._artop_applicationRecordDataType, "uuid"):
                return self._artop_applicationRecordDataType.uuid
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
