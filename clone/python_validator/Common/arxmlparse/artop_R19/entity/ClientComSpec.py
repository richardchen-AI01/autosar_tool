# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ClientComSpec.py
from .RPortComSpec import RPortComSpec

class ClientComSpec(RPortComSpec):

    def __init__(self):
        super().__init__()
        from .Field import Field
        from .ClientServerOperation import ClientServerOperation
        from .TransformationComSpecProps import TransformationComSpecProps
        self._artop_clientCapability = None
        self._artop_endToEndCallResponseTimeout = None
        self._artop_getterRef = None
        self._artop_operationRef = None
        self._artop_setterRef = None
        self._artop_transformationComSpecProps = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_getterRef': '"FIELD"', 
         '_artop_operationRef': '"CLIENT-SERVER-OPERATION"', 
         '_artop_setterRef': '"FIELD"', 
         '_artop_transformationComSpecProps': '"TRANSFORMATION-COM-SPEC-PROPS"'})

    @property
    def clientCapability_(self):
        return self._artop_clientCapability

    @property
    def endToEndCallResponseTimeout_(self):
        return self._artop_endToEndCallResponseTimeout

    @property
    def ref_getter_(self):
        return self._artop_getterRef

    @property
    def getter_(self):
        if self._artop_getterRef is not None:
            if hasattr(self._artop_getterRef, "uuid"):
                return self._artop_getterRef.uuid
        return

    @property
    def ref_operation_(self):
        return self._artop_operationRef

    @property
    def operation_(self):
        if self._artop_operationRef is not None:
            if hasattr(self._artop_operationRef, "uuid"):
                return self._artop_operationRef.uuid
        return

    @property
    def ref_setter_(self):
        return self._artop_setterRef

    @property
    def setter_(self):
        if self._artop_setterRef is not None:
            if hasattr(self._artop_setterRef, "uuid"):
                return self._artop_setterRef.uuid
        return

    @property
    def transformationComSpecProps_TransformationComSpecProps(self):
        return self._artop_transformationComSpecProps
