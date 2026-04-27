# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ServerComSpec.py
from .PPortComSpec import PPortComSpec

class ServerComSpec(PPortComSpec):

    def __init__(self):
        super().__init__()
        from .ClientServerOperation import ClientServerOperation
        from .TransformationComSpecProps import TransformationComSpecProps
        self._artop_queueLength = None
        self._artop_operationRef = None
        self._artop_transformationComSpecProps = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_operationRef':"CLIENT-SERVER-OPERATION", 
         '_artop_transformationComSpecProps':"TRANSFORMATION-COM-SPEC-PROPS"})

    @property
    def queueLength_(self):
        return self._artop_queueLength

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
    def transformationComSpecProps_TransformationComSpecProps(self):
        return self._artop_transformationComSpecProps
