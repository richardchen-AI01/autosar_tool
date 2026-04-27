# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\GeneralAnnotation.py
from .ARObject import ARObject

class GeneralAnnotation(ARObject):

    def __init__(self):
        super().__init__()
        from .MultilanguageLongName import MultilanguageLongName
        from .DocumentationBlock import DocumentationBlock
        self._artop_annotationOrigin = None
        self._artop_label = None
        self._artop_annotationText = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_label':"MULTILANGUAGE-LONG-NAME", 
         '_artop_annotationText':"DOCUMENTATION-BLOCK"})

    @property
    def annotationOrigin_(self):
        return self._artop_annotationOrigin

    @property
    def ref_label_(self):
        return self._artop_label

    @property
    def label_(self):
        if self._artop_label is not None:
            if hasattr(self._artop_label, "uuid"):
                return self._artop_label.uuid
        return

    @property
    def ref_annotationText_(self):
        return self._artop_annotationText

    @property
    def annotationText_(self):
        if self._artop_annotationText is not None:
            if hasattr(self._artop_annotationText, "uuid"):
                return self._artop_annotationText.uuid
        return
