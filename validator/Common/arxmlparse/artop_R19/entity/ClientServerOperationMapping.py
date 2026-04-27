# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ClientServerOperationMapping.py
from .ARObject import ARObject

class ClientServerOperationMapping(ARObject):

    def __init__(self):
        super().__init__()
        from .ClientServerInterfaceMapping import ClientServerInterfaceMapping
        from .DataPrototypeMapping import DataPrototypeMapping
        from .ClientServerOperation import ClientServerOperation
        from .DataTransformation import DataTransformation
        self._artop_clientServerInterfaceMapping = None
        self._artop_argumentMapping = []
        self._artop_firstOperationRef = None
        self._artop_firstToSecondDataTransformationRef = None
        self._artop_secondOperationRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_clientServerInterfaceMapping': '"CLIENT-SERVER-INTERFACE-MAPPING"', 
         '_artop_argumentMapping': '"DATA-PROTOTYPE-MAPPING"', 
         '_artop_firstOperationRef': '"CLIENT-SERVER-OPERATION"', 
         '_artop_firstToSecondDataTransformationRef': '"DATA-TRANSFORMATION"', 
         '_artop_secondOperationRef': '"CLIENT-SERVER-OPERATION"'})

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
    def argumentMappings_DataPrototypeMapping(self):
        return self._artop_argumentMapping

    @property
    def ref_firstOperation_(self):
        return self._artop_firstOperationRef

    @property
    def firstOperation_(self):
        if self._artop_firstOperationRef is not None:
            if hasattr(self._artop_firstOperationRef, "uuid"):
                return self._artop_firstOperationRef.uuid
        return

    @property
    def ref_firstToSecondDataTransformation_(self):
        return self._artop_firstToSecondDataTransformationRef

    @property
    def firstToSecondDataTransformation_(self):
        if self._artop_firstToSecondDataTransformationRef is not None:
            if hasattr(self._artop_firstToSecondDataTransformationRef, "uuid"):
                return self._artop_firstToSecondDataTransformationRef.uuid
        return

    @property
    def ref_secondOperation_(self):
        return self._artop_secondOperationRef

    @property
    def secondOperation_(self):
        if self._artop_secondOperationRef is not None:
            if hasattr(self._artop_secondOperationRef, "uuid"):
                return self._artop_secondOperationRef.uuid
        return
