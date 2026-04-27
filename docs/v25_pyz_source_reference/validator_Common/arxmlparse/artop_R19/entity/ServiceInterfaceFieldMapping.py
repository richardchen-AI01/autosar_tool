# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ServiceInterfaceFieldMapping.py
from .ServiceInterfaceElementMapping import ServiceInterfaceElementMapping

class ServiceInterfaceFieldMapping(ServiceInterfaceElementMapping):

    def __init__(self):
        super().__init__()
        from .Field import Field
        self._artop_sourceFieldRef = None
        self._artop_targetFieldRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_sourceFieldRef':"FIELD", 
         '_artop_targetFieldRef':"FIELD"})

    @property
    def ref_sourceField_(self):
        return self._artop_sourceFieldRef

    @property
    def sourceField_(self):
        if self._artop_sourceFieldRef is not None:
            if hasattr(self._artop_sourceFieldRef, "uuid"):
                return self._artop_sourceFieldRef.uuid
        return

    @property
    def ref_targetField_(self):
        return self._artop_targetFieldRef

    @property
    def targetField_(self):
        if self._artop_targetFieldRef is not None:
            if hasattr(self._artop_targetFieldRef, "uuid"):
                return self._artop_targetFieldRef.uuid
        return
