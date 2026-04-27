# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ArgumentDataPrototype.py
from .AutosarDataPrototype import AutosarDataPrototype

class ArgumentDataPrototype(AutosarDataPrototype):

    def __init__(self):
        super().__init__()
        from .ClientServerOperation import ClientServerOperation
        from .AutosarDataTypeRefConditional import AutosarDataTypeRefConditional
        from .VariationPoint import VariationPoint
        self._artop_direction = None
        self._artop_serverArgumentImplPolicy = None
        self._artop_clientServerOperation = None
        self._artop_typeBlueprint = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_clientServerOperation':"CLIENT-SERVER-OPERATION", 
         '_artop_typeBlueprint':"AUTOSAR-DATA-TYPE-REF-CONDITIONAL", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def direction_(self):
        return self._artop_direction

    @property
    def serverArgumentImplPolicy_(self):
        return self._artop_serverArgumentImplPolicy

    @property
    def ref_clientServerOperation_(self):
        return self._artop_clientServerOperation

    @property
    def clientServerOperation_(self):
        if self._artop_clientServerOperation is not None:
            if hasattr(self._artop_clientServerOperation, "uuid"):
                return self._artop_clientServerOperation.uuid
        return

    @property
    def typeBlueprints_AutosarDataTypeRefConditional(self):
        return self._artop_typeBlueprint

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
