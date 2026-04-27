# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TransformationPropsToServiceInterfaceElementMapping.py
from .Identifiable import Identifiable

class TransformationPropsToServiceInterfaceElementMapping(Identifiable):

    def __init__(self):
        super().__init__()
        from .TransformationPropsToServiceInterfaceElementMappingSet import TransformationPropsToServiceInterfaceElementMappingSet
        from .VariableDataPrototype import VariableDataPrototype
        from .Field import Field
        from .ClientServerOperation import ClientServerOperation
        from .TlvDataIdDefinitionSet import TlvDataIdDefinitionSet
        from .TransformationProps import TransformationProps
        self._artop_transformationPropsToServiceInterfaceElementMappingSet = None
        self._artop_eventRef = []
        self._artop_fieldRef = []
        self._artop_methodRef = []
        self._artop_tlvDataIdDefinitionRef = []
        self._artop_transformationPropsRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_transformationPropsToServiceInterfaceElementMappingSet': '"TRANSFORMATION-PROPS-TO-SERVICE-INTERFACE-ELEMENT-MAPPING-SET"', 
         '_artop_eventRef': '"VARIABLE-DATA-PROTOTYPE"', 
         '_artop_fieldRef': '"FIELD"', 
         '_artop_methodRef': '"CLIENT-SERVER-OPERATION"', 
         '_artop_tlvDataIdDefinitionRef': '"TLV-DATA-ID-DEFINITION-SET"', 
         '_artop_transformationPropsRef': '"TRANSFORMATION-PROPS"'})

    @property
    def ref_transformationPropsToServiceInterfaceElementMappingSet_(self):
        return self._artop_transformationPropsToServiceInterfaceElementMappingSet

    @property
    def transformationPropsToServiceInterfaceElementMappingSet_(self):
        if self._artop_transformationPropsToServiceInterfaceElementMappingSet is not None:
            if hasattr(self._artop_transformationPropsToServiceInterfaceElementMappingSet, "uuid"):
                return self._artop_transformationPropsToServiceInterfaceElementMappingSet.uuid
        return

    @property
    def ref_events_(self):
        return self._artop_eventRef

    @property
    def events_(self):
        return self._artop_eventRef

    @property
    def ref_fields_(self):
        return self._artop_fieldRef

    @property
    def fields_(self):
        return self._artop_fieldRef

    @property
    def ref_methods_(self):
        return self._artop_methodRef

    @property
    def methods_(self):
        return self._artop_methodRef

    @property
    def ref_tlvDataIdDefinitions_(self):
        return self._artop_tlvDataIdDefinitionRef

    @property
    def tlvDataIdDefinitions_(self):
        return self._artop_tlvDataIdDefinitionRef

    @property
    def ref_transformationProps_(self):
        return self._artop_transformationPropsRef

    @property
    def transformationProps_(self):
        if self._artop_transformationPropsRef is not None:
            if hasattr(self._artop_transformationPropsRef, "uuid"):
                return self._artop_transformationPropsRef.uuid
        return
