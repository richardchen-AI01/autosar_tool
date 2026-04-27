# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwValueCont.py
from .ARObject import ARObject

class SwValueCont(ARObject):

    def __init__(self):
        super().__init__()
        from .ApplicationValueSpecification import ApplicationValueSpecification
        from .Unit import Unit
        from .SingleLanguageUnitNames import SingleLanguageUnitNames
        from .ValueList import ValueList
        from .SwValues import SwValues
        self._artop_applicationValueSpecification = None
        self._artop_unitRef = None
        self._artop_unitDisplayName = None
        self._artop_swArraysize = None
        self._artop_swValuesPhys = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_applicationValueSpecification': '"APPLICATION-VALUE-SPECIFICATION"', 
         '_artop_unitRef': '"UNIT"', 
         '_artop_unitDisplayName': '"SINGLE-LANGUAGE-UNIT-NAMES"', 
         '_artop_swArraysize': '"VALUE-LIST"', 
         '_artop_swValuesPhys': '"SW-VALUES"'})

    @property
    def ref_applicationValueSpecification_(self):
        return self._artop_applicationValueSpecification

    @property
    def applicationValueSpecification_(self):
        if self._artop_applicationValueSpecification is not None:
            if hasattr(self._artop_applicationValueSpecification, "uuid"):
                return self._artop_applicationValueSpecification.uuid
        return

    @property
    def ref_unit_(self):
        return self._artop_unitRef

    @property
    def unit_(self):
        if self._artop_unitRef is not None:
            if hasattr(self._artop_unitRef, "uuid"):
                return self._artop_unitRef.uuid
        return

    @property
    def ref_unitDisplayName_(self):
        return self._artop_unitDisplayName

    @property
    def unitDisplayName_(self):
        if self._artop_unitDisplayName is not None:
            if hasattr(self._artop_unitDisplayName, "uuid"):
                return self._artop_unitDisplayName.uuid
        return

    @property
    def ref_swArraysize_(self):
        return self._artop_swArraysize

    @property
    def swArraysize_(self):
        if self._artop_swArraysize is not None:
            if hasattr(self._artop_swArraysize, "uuid"):
                return self._artop_swArraysize.uuid
        return

    @property
    def ref_swValuesPhys_(self):
        return self._artop_swValuesPhys

    @property
    def swValuesPhys_(self):
        if self._artop_swValuesPhys is not None:
            if hasattr(self._artop_swValuesPhys, "uuid"):
                return self._artop_swValuesPhys.uuid
        return
