# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\McParameterElementGroup.py
from .ARObject import ARObject

class McParameterElementGroup(ARObject):

    def __init__(self):
        super().__init__()
        from .McSwEmulationMethodSupport import McSwEmulationMethodSupport
        from .VariableDataPrototype import VariableDataPrototype
        from .ParameterDataPrototype import ParameterDataPrototype
        self._artop_shortLabel = None
        self._artop_mcSwEmulationMethodSupport = None
        self._artop_ramLocationRef = None
        self._artop_romLocationRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_mcSwEmulationMethodSupport':"MC-SW-EMULATION-METHOD-SUPPORT", 
         '_artop_ramLocationRef':"VARIABLE-DATA-PROTOTYPE", 
         '_artop_romLocationRef':"PARAMETER-DATA-PROTOTYPE"})

    @property
    def shortLabel_(self):
        return self._artop_shortLabel

    @property
    def ref_mcSwEmulationMethodSupport_(self):
        return self._artop_mcSwEmulationMethodSupport

    @property
    def mcSwEmulationMethodSupport_(self):
        if self._artop_mcSwEmulationMethodSupport is not None:
            if hasattr(self._artop_mcSwEmulationMethodSupport, "uuid"):
                return self._artop_mcSwEmulationMethodSupport.uuid
        return

    @property
    def ref_ramLocation_(self):
        return self._artop_ramLocationRef

    @property
    def ramLocation_(self):
        if self._artop_ramLocationRef is not None:
            if hasattr(self._artop_ramLocationRef, "uuid"):
                return self._artop_ramLocationRef.uuid
        return

    @property
    def ref_romLocation_(self):
        return self._artop_romLocationRef

    @property
    def romLocation_(self):
        if self._artop_romLocationRef is not None:
            if hasattr(self._artop_romLocationRef, "uuid"):
                return self._artop_romLocationRef.uuid
        return
