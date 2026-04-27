# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwCalprmAxis.py
from .ARObject import ARObject

class SwCalprmAxis(ARObject):

    def __init__(self):
        super().__init__()
        from .SwCalprmAxisSet import SwCalprmAxisSet
        from .SwCalprmAxisTypeProps import SwCalprmAxisTypeProps
        from .SwBaseType import SwBaseType
        self._artop_swAxisIndex = None
        self._artop_category = None
        self._artop_swCalibrationAccess = None
        self._artop_displayFormat = None
        self._artop_swCalprmAxisSet = None
        self._artop_swCalprmAxisTypeProps = None
        self._artop_baseTypeRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_swCalprmAxisSet':"SW-CALPRM-AXIS-SET", 
         '_artop_swCalprmAxisTypeProps':"SW-CALPRM-AXIS-TYPE-PROPS", 
         '_artop_baseTypeRef':"SW-BASE-TYPE"})

    @property
    def swAxisIndex_(self):
        return self._artop_swAxisIndex

    @property
    def category_(self):
        return self._artop_category

    @property
    def swCalibrationAccess_(self):
        return self._artop_swCalibrationAccess

    @property
    def displayFormat_(self):
        return self._artop_displayFormat

    @property
    def ref_swCalprmAxisSet_(self):
        return self._artop_swCalprmAxisSet

    @property
    def swCalprmAxisSet_(self):
        if self._artop_swCalprmAxisSet is not None:
            if hasattr(self._artop_swCalprmAxisSet, "uuid"):
                return self._artop_swCalprmAxisSet.uuid
        return

    @property
    def ref_swCalprmAxisTypeProps_(self):
        return self._artop_swCalprmAxisTypeProps

    @property
    def swCalprmAxisTypeProps_(self):
        if self._artop_swCalprmAxisTypeProps is not None:
            if hasattr(self._artop_swCalprmAxisTypeProps, "uuid"):
                return self._artop_swCalprmAxisTypeProps.uuid
        return

    @property
    def ref_baseType_(self):
        return self._artop_baseTypeRef

    @property
    def baseType_(self):
        if self._artop_baseTypeRef is not None:
            if hasattr(self._artop_baseTypeRef, "uuid"):
                return self._artop_baseTypeRef.uuid
        return
