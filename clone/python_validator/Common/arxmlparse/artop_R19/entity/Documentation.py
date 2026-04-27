# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Documentation.py
from .ARElement import ARElement

class Documentation(ARElement):

    def __init__(self):
        super().__init__()
        from .DocumentationContext import DocumentationContext
        from .PredefinedChapter import PredefinedChapter
        self._artop_context = []
        self._artop_documentationContent = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_context':"DOCUMENTATION-CONTEXT", 
         '_artop_documentationContent':"PREDEFINED-CHAPTER"})

    @property
    def contexts_DocumentationContext(self):
        return self._artop_context

    @property
    def ref_documentationContent_(self):
        return self._artop_documentationContent

    @property
    def documentationContent_(self):
        if self._artop_documentationContent is not None:
            if hasattr(self._artop_documentationContent, "uuid"):
                return self._artop_documentationContent.uuid
        return
