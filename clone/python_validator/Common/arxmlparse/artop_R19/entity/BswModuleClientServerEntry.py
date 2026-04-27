# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BswModuleClientServerEntry.py
from .Referrable import Referrable

class BswModuleClientServerEntry(Referrable):

    def __init__(self):
        super().__init__()
        from .BswModuleEntry import BswModuleEntry
        from .VariationPoint import VariationPoint
        self._artop_isReentrant = None
        self._artop_isSynchronous = None
        self._artop_encapsulatedEntryRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_encapsulatedEntryRef':"BSW-MODULE-ENTRY", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def isReentrant_(self):
        if self._artop_isReentrant:
            if self._artop_isReentrant == "true":
                return True
            return False
        else:
            return self._artop_isReentrant

    @property
    def isSynchronous_(self):
        if self._artop_isSynchronous:
            if self._artop_isSynchronous == "true":
                return True
            return False
        else:
            return self._artop_isSynchronous

    @property
    def ref_encapsulatedEntry_(self):
        return self._artop_encapsulatedEntryRef

    @property
    def encapsulatedEntry_(self):
        if self._artop_encapsulatedEntryRef is not None:
            if hasattr(self._artop_encapsulatedEntryRef, "uuid"):
                return self._artop_encapsulatedEntryRef.uuid
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
