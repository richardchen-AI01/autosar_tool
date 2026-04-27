# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ClientServerOperation.py
from .AtpStructureElement import AtpStructureElement

class ClientServerOperation(AtpStructureElement):

    def __init__(self):
        super().__init__()
        from .ArgumentDataPrototype import ArgumentDataPrototype
        from .ApApplicationError import ApApplicationError
        from .ApApplicationErrorSet import ApApplicationErrorSet
        from .ApplicationError import ApplicationError
        from .VariationPoint import VariationPoint
        self._artop_diagArgIntegrity = None
        self._artop_fireAndForget = None
        self._artop_argument = []
        self._artop_possibleApErrorRef = []
        self._artop_possibleApErrorSetRef = []
        self._artop_possibleErrorRef = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_argument': '"ARGUMENT-DATA-PROTOTYPE"', 
         '_artop_possibleApErrorRef': '"AP-APPLICATION-ERROR"', 
         '_artop_possibleApErrorSetRef': '"AP-APPLICATION-ERROR-SET"', 
         '_artop_possibleErrorRef': '"APPLICATION-ERROR"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def diagArgIntegrity_(self):
        if self._artop_diagArgIntegrity:
            if self._artop_diagArgIntegrity == "true":
                return True
            return False
        else:
            return self._artop_diagArgIntegrity

    @property
    def fireAndForget_(self):
        if self._artop_fireAndForget:
            if self._artop_fireAndForget == "true":
                return True
            return False
        else:
            return self._artop_fireAndForget

    @property
    def arguments_ArgumentDataPrototype(self):
        return self._artop_argument

    @property
    def ref_possibleApErrors_(self):
        return self._artop_possibleApErrorRef

    @property
    def possibleApErrors_(self):
        return self._artop_possibleApErrorRef

    @property
    def ref_possibleApErrorSets_(self):
        return self._artop_possibleApErrorSetRef

    @property
    def possibleApErrorSets_(self):
        return self._artop_possibleApErrorSetRef

    @property
    def ref_possibleErrors_(self):
        return self._artop_possibleErrorRef

    @property
    def possibleErrors_(self):
        return self._artop_possibleErrorRef

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
