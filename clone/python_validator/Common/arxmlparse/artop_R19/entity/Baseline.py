# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Baseline.py
from .ARObject import ARObject

class Baseline(ARObject):

    def __init__(self):
        super().__init__()
        from .DataExchangePoint import DataExchangePoint
        from .Documentation import Documentation
        from .SdgDef import SdgDef
        self._artop_standardRevision = None
        self._artop_dataExchangePoint = None
        self._artop_customSpecificationRef = []
        self._artop_customSdgDefRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_dataExchangePoint':"DATA-EXCHANGE-POINT", 
         '_artop_customSpecificationRef':"DOCUMENTATION", 
         '_artop_customSdgDefRef':"SDG-DEF"})

    @property
    def standardRevision_(self):
        return self._artop_standardRevision

    @property
    def ref_dataExchangePoint_(self):
        return self._artop_dataExchangePoint

    @property
    def dataExchangePoint_(self):
        if self._artop_dataExchangePoint is not None:
            if hasattr(self._artop_dataExchangePoint, "uuid"):
                return self._artop_dataExchangePoint.uuid
        return

    @property
    def ref_customSpecifications_(self):
        return self._artop_customSpecificationRef

    @property
    def customSpecifications_(self):
        return self._artop_customSpecificationRef

    @property
    def ref_customSdgDefs_(self):
        return self._artop_customSdgDefRef

    @property
    def customSdgDefs_(self):
        return self._artop_customSdgDefRef
