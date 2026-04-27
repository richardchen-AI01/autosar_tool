# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DataFormatTailoring.py
from .ARObject import ARObject

class DataFormatTailoring(ARObject):

    def __init__(self):
        super().__init__()
        from .DataExchangePoint import DataExchangePoint
        from .ClassTailoring import ClassTailoring
        from .ConstraintTailoring import ConstraintTailoring
        self._artop_dataExchangePoint = None
        self._artop_classTailoring = []
        self._artop_constraintTailoring = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_dataExchangePoint':"DATA-EXCHANGE-POINT", 
         '_artop_classTailoring':"CLASS-TAILORING", 
         '_artop_constraintTailoring':"CONSTRAINT-TAILORING"})

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
    def classTailorings_ClassTailoring(self):
        return self._artop_classTailoring

    @property
    def constraintTailorings_ConstraintTailoring(self):
        return self._artop_constraintTailoring
