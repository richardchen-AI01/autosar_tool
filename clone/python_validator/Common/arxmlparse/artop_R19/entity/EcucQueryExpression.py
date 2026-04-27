# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EcucQueryExpression.py
from .ARObject import ARObject

class EcucQueryExpression(ARObject):

    def __init__(self):
        super().__init__()
        from .EcucQuery import EcucQuery
        from .EcucDefinitionElement import EcucDefinitionElement
        self._artop_mixed = None
        self._artop_ecucQuery = None
        self._artop_configElementDefGlobalRef = []
        self._artop_configElementDefLocalRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_ecucQuery':"ECUC-QUERY", 
         '_artop_configElementDefGlobalRef':"ECUC-DEFINITION-ELEMENT", 
         '_artop_configElementDefLocalRef':"ECUC-DEFINITION-ELEMENT"})

    @property
    def mixed_(self):
        return self._artop_mixed

    @property
    def ref_ecucQuery_(self):
        return self._artop_ecucQuery

    @property
    def ecucQuery_(self):
        if self._artop_ecucQuery is not None:
            if hasattr(self._artop_ecucQuery, "uuid"):
                return self._artop_ecucQuery.uuid
        return

    @property
    def ref_configElementDefGlobals_(self):
        return self._artop_configElementDefGlobalRef

    @property
    def configElementDefGlobals_(self):
        return self._artop_configElementDefGlobalRef

    @property
    def ref_configElementDefLocals_(self):
        return self._artop_configElementDefLocalRef

    @property
    def configElementDefLocals_(self):
        return self._artop_configElementDefLocalRef
