# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ClientServerApplicationErrorMapping.py
from .ARObject import ARObject

class ClientServerApplicationErrorMapping(ARObject):

    def __init__(self):
        super().__init__()
        from .ClientServerInterfaceMapping import ClientServerInterfaceMapping
        from .ApplicationError import ApplicationError
        self._artop_clientServerInterfaceMapping = None
        self._artop_firstApplicationErrorRef = None
        self._artop_secondApplicationErrorRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_clientServerInterfaceMapping':"CLIENT-SERVER-INTERFACE-MAPPING", 
         '_artop_firstApplicationErrorRef':"APPLICATION-ERROR", 
         '_artop_secondApplicationErrorRef':"APPLICATION-ERROR"})

    @property
    def ref_clientServerInterfaceMapping_(self):
        return self._artop_clientServerInterfaceMapping

    @property
    def clientServerInterfaceMapping_(self):
        if self._artop_clientServerInterfaceMapping is not None:
            if hasattr(self._artop_clientServerInterfaceMapping, "uuid"):
                return self._artop_clientServerInterfaceMapping.uuid
        return

    @property
    def ref_firstApplicationError_(self):
        return self._artop_firstApplicationErrorRef

    @property
    def firstApplicationError_(self):
        if self._artop_firstApplicationErrorRef is not None:
            if hasattr(self._artop_firstApplicationErrorRef, "uuid"):
                return self._artop_firstApplicationErrorRef.uuid
        return

    @property
    def ref_secondApplicationError_(self):
        return self._artop_secondApplicationErrorRef

    @property
    def secondApplicationError_(self):
        if self._artop_secondApplicationErrorRef is not None:
            if hasattr(self._artop_secondApplicationErrorRef, "uuid"):
                return self._artop_secondApplicationErrorRef.uuid
        return
