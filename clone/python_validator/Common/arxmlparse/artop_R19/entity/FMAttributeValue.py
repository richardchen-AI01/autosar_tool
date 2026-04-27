# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FMAttributeValue.py
from .ARObject import ARObject

class FMAttributeValue(ARObject):

    def __init__(self):
        super().__init__()
        from .FMFeatureSelection import FMFeatureSelection
        from .FMAttributeDef import FMAttributeDef
        self._artop_value = None
        self._artop_fmFeatureSelection = None
        self._artop_definitionRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_fmFeatureSelection':"FM-FEATURE-SELECTION", 
         '_artop_definitionRef':"FM-ATTRIBUTE-DEF"})

    @property
    def value_(self):
        return self._artop_value

    @property
    def ref_fMFeatureSelection_(self):
        return self._artop_fmFeatureSelection

    @property
    def fMFeatureSelection_(self):
        if self._artop_fmFeatureSelection is not None:
            if hasattr(self._artop_fmFeatureSelection, "uuid"):
                return self._artop_fmFeatureSelection.uuid
        return

    @property
    def ref_definition_(self):
        return self._artop_definitionRef

    @property
    def definition_(self):
        if self._artop_definitionRef is not None:
            if hasattr(self._artop_definitionRef, "uuid"):
                return self._artop_definitionRef.uuid
        return
