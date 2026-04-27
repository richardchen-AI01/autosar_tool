# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ImplementationDataTypeSubElementRef.py
from .SubElementRef import SubElementRef

class ImplementationDataTypeSubElementRef(SubElementRef):

    def __init__(self):
        super().__init__()
        from .ArVariableInImplementationDataInstanceRef import ArVariableInImplementationDataInstanceRef
        from .ArParameterInImplementationDataInstanceRef import ArParameterInImplementationDataInstanceRef
        self._artop_implementationDataTypeElement = None
        self._artop_parameterImplementationDataTypeElement = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_implementationDataTypeElement':"AR-VARIABLE-IN-IMPLEMENTATION-DATA-INSTANCE-REF", 
         '_artop_parameterImplementationDataTypeElement':"AR-PARAMETER-IN-IMPLEMENTATION-DATA-INSTANCE-REF"})

    @property
    def ref_implementationDataTypeElement_(self):
        return self._artop_implementationDataTypeElement

    @property
    def implementationDataTypeElement_(self):
        if self._artop_implementationDataTypeElement is not None:
            if hasattr(self._artop_implementationDataTypeElement, "uuid"):
                return self._artop_implementationDataTypeElement.uuid
        return

    @property
    def ref_parameterImplementationDataTypeElement_(self):
        return self._artop_parameterImplementationDataTypeElement

    @property
    def parameterImplementationDataTypeElement_(self):
        if self._artop_parameterImplementationDataTypeElement is not None:
            if hasattr(self._artop_parameterImplementationDataTypeElement, "uuid"):
                return self._artop_parameterImplementationDataTypeElement.uuid
        return
