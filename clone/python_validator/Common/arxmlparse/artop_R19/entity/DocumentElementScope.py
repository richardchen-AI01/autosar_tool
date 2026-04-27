# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DocumentElementScope.py
from .SpecElementScope import SpecElementScope

class DocumentElementScope(SpecElementScope):

    def __init__(self):
        super().__init__()
        from .SpecificationDocumentScope import SpecificationDocumentScope
        from .Traceable import Traceable
        from .DataFormatElementReference import DataFormatElementReference
        self._artop_specificationDocumentScope = None
        self._artop_customDocumentElementRef = None
        self._artop_tailoringRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_specificationDocumentScope':"SPECIFICATION-DOCUMENT-SCOPE", 
         '_artop_customDocumentElementRef':"TRACEABLE", 
         '_artop_tailoringRef':"DATA-FORMAT-ELEMENT-REFERENCE"})

    @property
    def ref_specificationDocumentScope_(self):
        return self._artop_specificationDocumentScope

    @property
    def specificationDocumentScope_(self):
        if self._artop_specificationDocumentScope is not None:
            if hasattr(self._artop_specificationDocumentScope, "uuid"):
                return self._artop_specificationDocumentScope.uuid
        return

    @property
    def ref_customDocumentElement_(self):
        return self._artop_customDocumentElementRef

    @property
    def customDocumentElement_(self):
        if self._artop_customDocumentElementRef is not None:
            if hasattr(self._artop_customDocumentElementRef, "uuid"):
                return self._artop_customDocumentElementRef.uuid
        return

    @property
    def ref_tailorings_(self):
        return self._artop_tailoringRef

    @property
    def tailorings_(self):
        return self._artop_tailoringRef
