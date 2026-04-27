# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticEcuInstanceProps.py
from .DiagnosticCommonElement import DiagnosticCommonElement

class DiagnosticEcuInstanceProps(DiagnosticCommonElement):

    def __init__(self):
        super().__init__()
        from .EcuInstance import EcuInstance
        self._artop_dtcStatusAvailabilityMask = None
        self._artop_obdSupport = None
        self._artop_sendRespPendOnTransToBoot = None
        self._artop_ecuInstanceRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_ecuInstanceRef": "ECU-INSTANCE"})

    @property
    def dtcStatusAvailabilityMask_(self):
        return self._artop_dtcStatusAvailabilityMask

    @property
    def obdSupport_(self):
        return self._artop_obdSupport

    @property
    def sendRespPendOnTransToBoot_(self):
        if self._artop_sendRespPendOnTransToBoot:
            if self._artop_sendRespPendOnTransToBoot == "true":
                return True
            return False
        else:
            return self._artop_sendRespPendOnTransToBoot

    @property
    def ref_ecuInstances_(self):
        return self._artop_ecuInstanceRef

    @property
    def ecuInstances_(self):
        return self._artop_ecuInstanceRef
