# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticControlDTCSetting.py
from .DiagnosticServiceInstance import DiagnosticServiceInstance

class DiagnosticControlDTCSetting(DiagnosticServiceInstance):

    def __init__(self):
        super().__init__()
        from .DiagnosticControlDTCSettingClass import DiagnosticControlDTCSettingClass
        self._artop_dtcSettingParameter = None
        self._artop_dtcSettingClassRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_dtcSettingClassRef": "DIAGNOSTIC-CONTROL-DTC-SETTING-CLASS"})

    @property
    def dtcSettingParameter_(self):
        return self._artop_dtcSettingParameter

    @property
    def ref_dtcSettingClass_(self):
        return self._artop_dtcSettingClassRef

    @property
    def dtcSettingClass_(self):
        if self._artop_dtcSettingClassRef is not None:
            if hasattr(self._artop_dtcSettingClassRef, "uuid"):
                return self._artop_dtcSettingClassRef.uuid
        return
