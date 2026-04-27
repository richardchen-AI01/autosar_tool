# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticRequestVehicleInfo.py
from .DiagnosticServiceInstance import DiagnosticServiceInstance

class DiagnosticRequestVehicleInfo(DiagnosticServiceInstance):

    def __init__(self):
        super().__init__()
        from .DiagnosticInfoType import DiagnosticInfoType
        from .DiagnosticRequestVehicleInfoClass import DiagnosticRequestVehicleInfoClass
        self._artop_infoTypeRef = None
        self._artop_requestVehicleInformationClassRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_infoTypeRef':"DIAGNOSTIC-INFO-TYPE", 
         '_artop_requestVehicleInformationClassRef':"DIAGNOSTIC-REQUEST-VEHICLE-INFO-CLASS"})

    @property
    def ref_infoType_(self):
        return self._artop_infoTypeRef

    @property
    def infoType_(self):
        if self._artop_infoTypeRef is not None:
            if hasattr(self._artop_infoTypeRef, "uuid"):
                return self._artop_infoTypeRef.uuid
        return

    @property
    def ref_requestVehicleInformationClass_(self):
        return self._artop_requestVehicleInformationClassRef

    @property
    def requestVehicleInformationClass_(self):
        if self._artop_requestVehicleInformationClassRef is not None:
            if hasattr(self._artop_requestVehicleInformationClassRef, "uuid"):
                return self._artop_requestVehicleInformationClassRef.uuid
        return
