# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SpecificationDocumentScope.py
from .SpecElementScope import SpecElementScope

class SpecificationDocumentScope(SpecElementScope):

    def __init__(self):
        super().__init__()
        from .SpecificationScope import SpecificationScope
        from .Documentation import Documentation
        from .DocumentElementScope import DocumentElementScope
        self._artop_specificationScope = None
        self._artop_customDocumentationRef = None
        self._artop_documentElementScope = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_specificationScope':"SPECIFICATION-SCOPE", 
         '_artop_customDocumentationRef':"DOCUMENTATION", 
         '_artop_documentElementScope':"DOCUMENT-ELEMENT-SCOPE"})

    @property
    def ref_specificationScope_(self):
        return self._artop_specificationScope

    @property
    def specificationScope_(self):
        if self._artop_specificationScope is not None:
            if hasattr(self._artop_specificationScope, "uuid"):
                return self._artop_specificationScope.uuid
        return

    @property
    def ref_customDocumentation_(self):
        return self._artop_customDocumentationRef

    @property
    def customDocumentation_(self):
        if self._artop_customDocumentationRef is not None:
            if hasattr(self._artop_customDocumentationRef, "uuid"):
                return self._artop_customDocumentationRef.uuid
        return

    @property
    def documentElementScopes_DocumentElementScope(self):
        return self._artop_documentElementScope
