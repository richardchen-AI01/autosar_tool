# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticExtendedDataRecordRefConditional.py
from .ARObject import ARObject

class DiagnosticExtendedDataRecordRefConditional(ARObject):

    def __init__(self):
        super().__init__()
        from .DiagnosticTroubleCodeProps import DiagnosticTroubleCodeProps
        from .DiagnosticExtendedDataRecord import DiagnosticExtendedDataRecord
        from .VariationPoint import VariationPoint
        self._artop_diagnosticTroubleCodeProps = None
        self._artop_diagnosticExtendedDataRecordRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_diagnosticTroubleCodeProps':"DIAGNOSTIC-TROUBLE-CODE-PROPS", 
         '_artop_diagnosticExtendedDataRecordRef':"DIAGNOSTIC-EXTENDED-DATA-RECORD", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def ref_diagnosticTroubleCodeProps_(self):
        return self._artop_diagnosticTroubleCodeProps

    @property
    def diagnosticTroubleCodeProps_(self):
        if self._artop_diagnosticTroubleCodeProps is not None:
            if hasattr(self._artop_diagnosticTroubleCodeProps, "uuid"):
                return self._artop_diagnosticTroubleCodeProps.uuid
        return

    @property
    def ref_diagnosticExtendedDataRecord_(self):
        return self._artop_diagnosticExtendedDataRecordRef

    @property
    def diagnosticExtendedDataRecord_(self):
        if self._artop_diagnosticExtendedDataRecordRef is not None:
            if hasattr(self._artop_diagnosticExtendedDataRecordRef, "uuid"):
                return self._artop_diagnosticExtendedDataRecordRef.uuid
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
