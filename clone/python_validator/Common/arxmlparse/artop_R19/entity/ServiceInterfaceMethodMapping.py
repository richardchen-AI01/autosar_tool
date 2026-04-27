# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ServiceInterfaceMethodMapping.py
from .ServiceInterfaceElementMapping import ServiceInterfaceElementMapping

class ServiceInterfaceMethodMapping(ServiceInterfaceElementMapping):

    def __init__(self):
        super().__init__()
        from .ClientServerOperation import ClientServerOperation
        self._artop_sourceMethodRef = None
        self._artop_targetMethodRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_sourceMethodRef':"CLIENT-SERVER-OPERATION", 
         '_artop_targetMethodRef':"CLIENT-SERVER-OPERATION"})

    @property
    def ref_sourceMethod_(self):
        return self._artop_sourceMethodRef

    @property
    def sourceMethod_(self):
        if self._artop_sourceMethodRef is not None:
            if hasattr(self._artop_sourceMethodRef, "uuid"):
                return self._artop_sourceMethodRef.uuid
        return

    @property
    def ref_targetMethod_(self):
        return self._artop_targetMethodRef

    @property
    def targetMethod_(self):
        if self._artop_targetMethodRef is not None:
            if hasattr(self._artop_targetMethodRef, "uuid"):
                return self._artop_targetMethodRef.uuid
        return
