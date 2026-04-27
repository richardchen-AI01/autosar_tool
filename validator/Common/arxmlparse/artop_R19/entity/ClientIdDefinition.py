# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ClientIdDefinition.py
from .Identifiable import Identifiable

class ClientIdDefinition(Identifiable):

    def __init__(self):
        super().__init__()
        from .ClientIdDefinitionSet import ClientIdDefinitionSet
        from .OperationInSystemInstanceRef import OperationInSystemInstanceRef
        from .VariationPoint import VariationPoint
        self._artop_clientId = None
        self._artop_clientIdDefinitionSet = None
        self._artop_clientServerOperationIref = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_clientIdDefinitionSet':"CLIENT-ID-DEFINITION-SET", 
         '_artop_clientServerOperationIref':"OPERATION-IN-SYSTEM-INSTANCE-REF-IREF", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def clientId_(self):
        return self._artop_clientId

    @property
    def ref_clientIdDefinitionSet_(self):
        return self._artop_clientIdDefinitionSet

    @property
    def clientIdDefinitionSet_(self):
        if self._artop_clientIdDefinitionSet is not None:
            if hasattr(self._artop_clientIdDefinitionSet, "uuid"):
                return self._artop_clientIdDefinitionSet.uuid
        return

    @property
    def ref_clientServerOperation_(self):
        return self._artop_clientServerOperationIref

    @property
    def clientServerOperation_(self):
        if self._artop_clientServerOperationIref is not None:
            if hasattr(self._artop_clientServerOperationIref, "uuid"):
                return self._artop_clientServerOperationIref.uuid
        return

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
