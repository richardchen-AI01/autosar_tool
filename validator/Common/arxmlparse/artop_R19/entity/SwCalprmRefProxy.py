# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwCalprmRefProxy.py
from .ARObject import ARObject

class SwCalprmRefProxy(ARObject):

    def __init__(self):
        super().__init__()
        from .AutosarParameterRef import AutosarParameterRef
        from .McDataInstance import McDataInstance
        self._artop_arParameter = None
        self._artop_mcDataInstanceRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_arParameter':"AUTOSAR-PARAMETER-REF", 
         '_artop_mcDataInstanceRef':"MC-DATA-INSTANCE"})

    @property
    def ref_arParameter_(self):
        return self._artop_arParameter

    @property
    def arParameter_(self):
        if self._artop_arParameter is not None:
            if hasattr(self._artop_arParameter, "uuid"):
                return self._artop_arParameter.uuid
        return

    @property
    def ref_mcDataInstance_(self):
        return self._artop_mcDataInstanceRef

    @property
    def mcDataInstance_(self):
        if self._artop_mcDataInstanceRef is not None:
            if hasattr(self._artop_mcDataInstanceRef, "uuid"):
                return self._artop_mcDataInstanceRef.uuid
        return
