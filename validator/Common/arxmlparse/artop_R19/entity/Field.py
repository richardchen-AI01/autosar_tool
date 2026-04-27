# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Field.py
from .AutosarDataPrototype import AutosarDataPrototype

class Field(AutosarDataPrototype):

    def __init__(self):
        super().__init__()
        from .ServiceInterface import ServiceInterface
        from .VariationPoint import VariationPoint
        self._artop_hasGetter = None
        self._artop_hasNotifier = None
        self._artop_hasSetter = None
        self._artop_serviceInterface = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_serviceInterface':"SERVICE-INTERFACE", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def hasGetter_(self):
        if self._artop_hasGetter:
            if self._artop_hasGetter == "true":
                return True
            return False
        else:
            return self._artop_hasGetter

    @property
    def hasNotifier_(self):
        if self._artop_hasNotifier:
            if self._artop_hasNotifier == "true":
                return True
            return False
        else:
            return self._artop_hasNotifier

    @property
    def hasSetter_(self):
        if self._artop_hasSetter:
            if self._artop_hasSetter == "true":
                return True
            return False
        else:
            return self._artop_hasSetter

    @property
    def ref_serviceInterface_(self):
        return self._artop_serviceInterface

    @property
    def serviceInterface_(self):
        if self._artop_serviceInterface is not None:
            if hasattr(self._artop_serviceInterface, "uuid"):
                return self._artop_serviceInterface.uuid
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
