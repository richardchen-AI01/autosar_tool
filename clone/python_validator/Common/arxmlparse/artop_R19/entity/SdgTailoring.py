# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SdgTailoring.py
from .RestrictionWithSeverity import RestrictionWithSeverity
from .DataFormatElementScope import DataFormatElementScope

class SdgTailoring(DataFormatElementScope, RestrictionWithSeverity):

    def __init__(self):
        super().__init__()
        from .ClassContentConditional import ClassContentConditional
        from .SdgClass import SdgClass
        self._artop_classContentConditional = None
        self._artop_sdgClassRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_classContentConditional':"CLASS-CONTENT-CONDITIONAL", 
         '_artop_sdgClassRef':"SDG-CLASS"})

    @property
    def ref_classContentConditional_(self):
        return self._artop_classContentConditional

    @property
    def classContentConditional_(self):
        if self._artop_classContentConditional is not None:
            if hasattr(self._artop_classContentConditional, "uuid"):
                return self._artop_classContentConditional.uuid
        return

    @property
    def ref_sdgClass_(self):
        return self._artop_sdgClassRef

    @property
    def sdgClass_(self):
        if self._artop_sdgClassRef is not None:
            if hasattr(self._artop_sdgClassRef, "uuid"):
                return self._artop_sdgClassRef.uuid
        return
