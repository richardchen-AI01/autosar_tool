# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DataExchangePoint.py
from .ARElement import ARElement

class DataExchangePoint(ARElement):

    def __init__(self):
        super().__init__()
        from .Baseline import Baseline
        from .SpecificationScope import SpecificationScope
        from .DataFormatTailoring import DataFormatTailoring
        self._artop_kind = None
        self._artop_referencedBaseline = None
        self._artop_specificationScope = None
        self._artop_dataFormatTailoring = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_referencedBaseline':"BASELINE", 
         '_artop_specificationScope':"SPECIFICATION-SCOPE", 
         '_artop_dataFormatTailoring':"DATA-FORMAT-TAILORING"})

    @property
    def kind_(self):
        return self._artop_kind

    @property
    def ref_referencedBaseline_(self):
        return self._artop_referencedBaseline

    @property
    def referencedBaseline_(self):
        if self._artop_referencedBaseline is not None:
            if hasattr(self._artop_referencedBaseline, "uuid"):
                return self._artop_referencedBaseline.uuid
        return

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
    def ref_dataFormatTailoring_(self):
        return self._artop_dataFormatTailoring

    @property
    def dataFormatTailoring_(self):
        if self._artop_dataFormatTailoring is not None:
            if hasattr(self._artop_dataFormatTailoring, "uuid"):
                return self._artop_dataFormatTailoring.uuid
        return
