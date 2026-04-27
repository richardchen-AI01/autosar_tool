# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\LinSlaveContent.py
from .LinCommunicationControllerContent import LinCommunicationControllerContent

class LinSlaveContent(LinCommunicationControllerContent):

    def __init__(self):
        super().__init__()
        from .LinErrorResponse import LinErrorResponse
        self._artop_assignNad = None
        self._artop_configuredNad = None
        self._artop_functionId = None
        self._artop_initialNad = None
        self._artop_nasTimeout = None
        self._artop_saveConfiguration = None
        self._artop_supplierId = None
        self._artop_variantId = None
        self._artop_linErrorResponse = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_linErrorResponse": "LIN-ERROR-RESPONSE"})

    @property
    def assignNad_(self):
        if self._artop_assignNad:
            if self._artop_assignNad == "true":
                return True
            return False
        else:
            return self._artop_assignNad

    @property
    def configuredNad_(self):
        if self._artop_configuredNad:
            return int(self._artop_configuredNad)
        return self._artop_configuredNad

    @property
    def functionId_(self):
        return self._artop_functionId

    @property
    def initialNad_(self):
        if self._artop_initialNad:
            return int(self._artop_initialNad)
        return self._artop_initialNad

    @property
    def nasTimeout_(self):
        return self._artop_nasTimeout

    @property
    def saveConfiguration_(self):
        if self._artop_saveConfiguration:
            if self._artop_saveConfiguration == "true":
                return True
            return False
        else:
            return self._artop_saveConfiguration

    @property
    def supplierId_(self):
        return self._artop_supplierId

    @property
    def variantId_(self):
        return self._artop_variantId

    @property
    def ref_linErrorResponse_(self):
        return self._artop_linErrorResponse

    @property
    def linErrorResponse_(self):
        if self._artop_linErrorResponse is not None:
            if hasattr(self._artop_linErrorResponse, "uuid"):
                return self._artop_linErrorResponse.uuid
        return
