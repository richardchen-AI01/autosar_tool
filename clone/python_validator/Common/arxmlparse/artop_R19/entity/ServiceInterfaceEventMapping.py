# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ServiceInterfaceEventMapping.py
from .ServiceInterfaceElementMapping import ServiceInterfaceElementMapping

class ServiceInterfaceEventMapping(ServiceInterfaceElementMapping):

    def __init__(self):
        super().__init__()
        from .VariableDataPrototype import VariableDataPrototype
        self._artop_sourceEventRef = None
        self._artop_targetEventRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_sourceEventRef':"VARIABLE-DATA-PROTOTYPE", 
         '_artop_targetEventRef':"VARIABLE-DATA-PROTOTYPE"})

    @property
    def ref_sourceEvent_(self):
        return self._artop_sourceEventRef

    @property
    def sourceEvent_(self):
        if self._artop_sourceEventRef is not None:
            if hasattr(self._artop_sourceEventRef, "uuid"):
                return self._artop_sourceEventRef.uuid
        return

    @property
    def ref_targetEvent_(self):
        return self._artop_targetEventRef

    @property
    def targetEvent_(self):
        if self._artop_targetEventRef is not None:
            if hasattr(self._artop_targetEventRef, "uuid"):
                return self._artop_targetEventRef.uuid
        return
