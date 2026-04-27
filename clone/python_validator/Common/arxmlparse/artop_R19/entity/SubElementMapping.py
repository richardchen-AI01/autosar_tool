# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SubElementMapping.py
from .ARObject import ARObject

class SubElementMapping(ARObject):

    def __init__(self):
        super().__init__()
        from .DataPrototypeMapping import DataPrototypeMapping
        from .SubElementRef import SubElementRef
        from .TextTableMapping import TextTableMapping
        self._artop_dataPrototypeMapping = None
        self._artop_firstElement = []
        self._artop_secondElement = []
        self._artop_textTableMapping = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_dataPrototypeMapping': '"DATA-PROTOTYPE-MAPPING"', 
         '_artop_firstElement': '"SUB-ELEMENT-REF"', 
         '_artop_secondElement': '"SUB-ELEMENT-REF"', 
         '_artop_textTableMapping': '"TEXT-TABLE-MAPPING"'})

    @property
    def ref_dataPrototypeMapping_(self):
        return self._artop_dataPrototypeMapping

    @property
    def dataPrototypeMapping_(self):
        if self._artop_dataPrototypeMapping is not None:
            if hasattr(self._artop_dataPrototypeMapping, "uuid"):
                return self._artop_dataPrototypeMapping.uuid
        return

    @property
    def firstElements_SubElementRef(self):
        return self._artop_firstElement

    @property
    def secondElements_SubElementRef(self):
        return self._artop_secondElement

    @property
    def textTableMappings_TextTableMapping(self):
        return self._artop_textTableMapping
