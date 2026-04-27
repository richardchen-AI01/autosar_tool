# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SOMEIPTransformationISignalPropsContent.py
from .TransformationISignalPropsContent import TransformationISignalPropsContent

class SOMEIPTransformationISignalPropsContent(TransformationISignalPropsContent):

    def __init__(self):
        super().__init__()
        from .TlvDataIdDefinition import TlvDataIdDefinition
        from .TlvDataIdDefinitionSet import TlvDataIdDefinitionSet
        self._artop_implementsLegacyStringSerialization = None
        self._artop_implementsSomeipStringHandling = None
        self._artop_interfaceVersion = None
        self._artop_isDynamicLengthFieldSize = None
        self._artop_messageType = None
        self._artop_sessionHandlingSr = None
        self._artop_sizeOfArrayLengthFields = None
        self._artop_sizeOfStructLengthFields = None
        self._artop_sizeOfUnionLengthFields = None
        self._artop_tlvDataId = []
        self._artop_tlvDataId0Ref = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_tlvDataId':"TLV-DATA-ID-DEFINITION", 
         '_artop_tlvDataId0Ref':"TLV-DATA-ID-DEFINITION-SET"})

    @property
    def implementsLegacyStringSerialization_(self):
        if self._artop_implementsLegacyStringSerialization:
            if self._artop_implementsLegacyStringSerialization == "true":
                return True
            return False
        else:
            return self._artop_implementsLegacyStringSerialization

    @property
    def implementsSomeipStringHandling_(self):
        if self._artop_implementsSomeipStringHandling:
            if self._artop_implementsSomeipStringHandling == "true":
                return True
            return False
        else:
            return self._artop_implementsSomeipStringHandling

    @property
    def interfaceVersion_(self):
        return self._artop_interfaceVersion

    @property
    def isDynamicLengthFieldSize_(self):
        if self._artop_isDynamicLengthFieldSize:
            if self._artop_isDynamicLengthFieldSize == "true":
                return True
            return False
        else:
            return self._artop_isDynamicLengthFieldSize

    @property
    def messageType_(self):
        return self._artop_messageType

    @property
    def sessionHandlingSr_(self):
        return self._artop_sessionHandlingSr

    @property
    def sizeOfArrayLengthFields_(self):
        return self._artop_sizeOfArrayLengthFields

    @property
    def sizeOfStructLengthFields_(self):
        return self._artop_sizeOfStructLengthFields

    @property
    def sizeOfUnionLengthFields_(self):
        return self._artop_sizeOfUnionLengthFields

    @property
    def tlvDataIds_TlvDataIdDefinition(self):
        return self._artop_tlvDataId

    @property
    def ref_tlvDataId0s_(self):
        return self._artop_tlvDataId0Ref

    @property
    def tlvDataId0s_(self):
        return self._artop_tlvDataId0Ref
