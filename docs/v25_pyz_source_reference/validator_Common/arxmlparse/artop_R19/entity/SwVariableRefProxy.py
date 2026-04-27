# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwVariableRefProxy.py
from .ARObject import ARObject

class SwVariableRefProxy(ARObject):

    def __init__(self):
        super().__init__()
        from .AutosarVariableRef import AutosarVariableRef
        from .McDataInstance import McDataInstance
        self._artop_autosarVariable = None
        self._artop_mcDataInstanceVarRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_autosarVariable':"AUTOSAR-VARIABLE-REF", 
         '_artop_mcDataInstanceVarRef':"MC-DATA-INSTANCE"})

    @property
    def ref_autosarVariable_(self):
        return self._artop_autosarVariable

    @property
    def autosarVariable_(self):
        if self._artop_autosarVariable is not None:
            if hasattr(self._artop_autosarVariable, "uuid"):
                return self._artop_autosarVariable.uuid
        return

    @property
    def ref_mcDataInstanceVar_(self):
        return self._artop_mcDataInstanceVarRef

    @property
    def mcDataInstanceVar_(self):
        if self._artop_mcDataInstanceVarRef is not None:
            if hasattr(self._artop_mcDataInstanceVarRef, "uuid"):
                return self._artop_mcDataInstanceVarRef.uuid
        return
