# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DataPrototypeMapping.py
from .ARObject import ARObject

class DataPrototypeMapping(ARObject):

    def __init__(self):
        super().__init__()
        from .AutosarDataPrototype import AutosarDataPrototype
        from .DataTransformation import DataTransformation
        from .SubElementMapping import SubElementMapping
        from .TextTableMapping import TextTableMapping
        self._artop_firstDataPrototypeRef = None
        self._artop_firstToSecondDataTransformationRef = None
        self._artop_secondDataPrototypeRef = None
        self._artop_secondToFirstDataTransformationRef = None
        self._artop_subElementMapping = []
        self._artop_textTableMapping = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_firstDataPrototypeRef': '"AUTOSAR-DATA-PROTOTYPE"', 
         '_artop_firstToSecondDataTransformationRef': '"DATA-TRANSFORMATION"', 
         '_artop_secondDataPrototypeRef': '"AUTOSAR-DATA-PROTOTYPE"', 
         '_artop_secondToFirstDataTransformationRef': '"DATA-TRANSFORMATION"', 
         '_artop_subElementMapping': '"SUB-ELEMENT-MAPPING"', 
         '_artop_textTableMapping': '"TEXT-TABLE-MAPPING"'})

    @property
    def ref_firstDataPrototype_(self):
        return self._artop_firstDataPrototypeRef

    @property
    def firstDataPrototype_(self):
        if self._artop_firstDataPrototypeRef is not None:
            if hasattr(self._artop_firstDataPrototypeRef, "uuid"):
                return self._artop_firstDataPrototypeRef.uuid
        return

    @property
    def ref_firstToSecondDataTransformation_(self):
        return self._artop_firstToSecondDataTransformationRef

    @property
    def firstToSecondDataTransformation_(self):
        if self._artop_firstToSecondDataTransformationRef is not None:
            if hasattr(self._artop_firstToSecondDataTransformationRef, "uuid"):
                return self._artop_firstToSecondDataTransformationRef.uuid
        return

    @property
    def ref_secondDataPrototype_(self):
        return self._artop_secondDataPrototypeRef

    @property
    def secondDataPrototype_(self):
        if self._artop_secondDataPrototypeRef is not None:
            if hasattr(self._artop_secondDataPrototypeRef, "uuid"):
                return self._artop_secondDataPrototypeRef.uuid
        return

    @property
    def ref_secondToFirstDataTransformation_(self):
        return self._artop_secondToFirstDataTransformationRef

    @property
    def secondToFirstDataTransformation_(self):
        if self._artop_secondToFirstDataTransformationRef is not None:
            if hasattr(self._artop_secondToFirstDataTransformationRef, "uuid"):
                return self._artop_secondToFirstDataTransformationRef.uuid
        return

    @property
    def subElementMappings_SubElementMapping(self):
        return self._artop_subElementMapping

    @property
    def textTableMappings_TextTableMapping(self):
        return self._artop_textTableMapping
