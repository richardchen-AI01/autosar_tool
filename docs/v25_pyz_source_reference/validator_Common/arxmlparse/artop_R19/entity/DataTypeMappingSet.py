# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DataTypeMappingSet.py
from .AtpBlueprintable import AtpBlueprintable
from .AtpBlueprint import AtpBlueprint
from .ARElement import ARElement

class DataTypeMappingSet(ARElement, AtpBlueprint, AtpBlueprintable):

    def __init__(self):
        super().__init__()
        from .DataTypeMap import DataTypeMap
        from .ModeRequestTypeMap import ModeRequestTypeMap
        self._artop_dataTypeMap = []
        self._artop_modeRequestTypeMap = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_dataTypeMap':"DATA-TYPE-MAP", 
         '_artop_modeRequestTypeMap':"MODE-REQUEST-TYPE-MAP"})

    @property
    def dataTypeMaps_DataTypeMap(self):
        return self._artop_dataTypeMap

    @property
    def modeRequestTypeMaps_ModeRequestTypeMap(self):
        return self._artop_modeRequestTypeMap
