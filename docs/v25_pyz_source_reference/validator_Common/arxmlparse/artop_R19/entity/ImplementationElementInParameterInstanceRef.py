# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ImplementationElementInParameterInstanceRef.py
from .AtpInstanceRef import AtpInstanceRef

class ImplementationElementInParameterInstanceRef(AtpInstanceRef):

    def __init__(self):
        super().__init__()
        from .McDataInstance import McDataInstance
        from .ParameterDataPrototype import ParameterDataPrototype
        from .ImplementationDataTypeElement import ImplementationDataTypeElement
        self._artop_mcDataInstance = None
        self._artop_contextRef = None
        self._artop_targetRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_mcDataInstance':"MC-DATA-INSTANCE", 
         '_artop_contextRef':"PARAMETER-DATA-PROTOTYPE", 
         '_artop_targetRef':"IMPLEMENTATION-DATA-TYPE-ELEMENT"})

    @property
    def ref_mcDataInstance_(self):
        return self._artop_mcDataInstance

    @property
    def mcDataInstance_(self):
        if self._artop_mcDataInstance is not None:
            if hasattr(self._artop_mcDataInstance, "uuid"):
                return self._artop_mcDataInstance.uuid
        return

    @property
    def ref_context_(self):
        return self._artop_contextRef

    @property
    def context_(self):
        if self._artop_contextRef is not None:
            if hasattr(self._artop_contextRef, "uuid"):
                return self._artop_contextRef.uuid
        return

    @property
    def ref_target_(self):
        return self._artop_targetRef

    @property
    def target_(self):
        if self._artop_targetRef is not None:
            if hasattr(self._artop_targetRef, "uuid"):
                return self._artop_targetRef.uuid
        return
