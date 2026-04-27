# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticDynamicallyDefineDataIdentifierClass.py
from .DiagnosticServiceClass import DiagnosticServiceClass

class DiagnosticDynamicallyDefineDataIdentifierClass(DiagnosticServiceClass):

    def __init__(self):
        super().__init__()
        self._artop_checkPerSourceId = None
        self._artop_configurationHandling = None
        self._artop_subfunction = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def checkPerSourceId_(self):
        if self._artop_checkPerSourceId:
            if self._artop_checkPerSourceId == "true":
                return True
            return False
        else:
            return self._artop_checkPerSourceId

    @property
    def configurationHandling_(self):
        return self._artop_configurationHandling

    @property
    def subfunction_(self):
        return self._artop_subfunction
