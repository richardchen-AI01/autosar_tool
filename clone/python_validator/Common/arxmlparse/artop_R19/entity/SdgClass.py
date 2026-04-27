# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SdgClass.py
from .SdgElementWithGid import SdgElementWithGid
from .Identifiable import Identifiable

class SdgClass(Identifiable, SdgElementWithGid):

    def __init__(self):
        super().__init__()
        from .SdgDef import SdgDef
        from .SdgAttribute import SdgAttribute
        from .TraceableText import TraceableText
        self._artop_extendsMetaClass = None
        self._artop_caption = None
        self._artop_sdgDef = None
        self._artop_attribute = []
        self._artop_sdgConstraintRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_sdgDef':"SDG-DEF", 
         '_artop_attribute':"SDG-ATTRIBUTE", 
         '_artop_sdgConstraintRef':"TRACEABLE-TEXT"})

    @property
    def extendsMetaClass_(self):
        return self._artop_extendsMetaClass

    @property
    def caption_(self):
        if self._artop_caption:
            if self._artop_caption == "true":
                return True
            return False
        else:
            return self._artop_caption

    @property
    def ref_sdgDef_(self):
        return self._artop_sdgDef

    @property
    def sdgDef_(self):
        if self._artop_sdgDef is not None:
            if hasattr(self._artop_sdgDef, "uuid"):
                return self._artop_sdgDef.uuid
        return

    @property
    def attributes_SdgAttribute(self):
        return self._artop_attribute

    @property
    def ref_sdgConstraints_(self):
        return self._artop_sdgConstraintRef

    @property
    def sdgConstraints_(self):
        return self._artop_sdgConstraintRef
