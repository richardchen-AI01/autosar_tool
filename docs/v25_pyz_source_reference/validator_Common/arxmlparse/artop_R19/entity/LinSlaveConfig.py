# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\LinSlaveConfig.py
from .ARObject import ARObject

class LinSlaveConfig(ARObject):

    def __init__(self):
        super().__init__()
        from .LinMasterContent import LinMasterContent
        from .LinSlaveConfigIdent import LinSlaveConfigIdent
        from .LinErrorResponse import LinErrorResponse
        from .LinSlave import LinSlave
        self._artop_configuredNad = None
        self._artop_functionId = None
        self._artop_initialNad = None
        self._artop_protocolVersion = None
        self._artop_supplierId = None
        self._artop_variantId = None
        self._artop_linMasterContent = None
        self._artop_ident = None
        self._artop_linErrorResponse = None
        self._artop_linSlaveEcuRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_linMasterContent': '"LIN-MASTER-CONTENT"', 
         '_artop_ident': '"LIN-SLAVE-CONFIG-IDENT"', 
         '_artop_linErrorResponse': '"LIN-ERROR-RESPONSE"', 
         '_artop_linSlaveEcuRef': '"LIN-SLAVE"'})

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
    def protocolVersion_(self):
        return self._artop_protocolVersion

    @property
    def supplierId_(self):
        return self._artop_supplierId

    @property
    def variantId_(self):
        return self._artop_variantId

    @property
    def ref_linMasterContent_(self):
        return self._artop_linMasterContent

    @property
    def linMasterContent_(self):
        if self._artop_linMasterContent is not None:
            if hasattr(self._artop_linMasterContent, "uuid"):
                return self._artop_linMasterContent.uuid
        return

    @property
    def ref_ident_(self):
        return self._artop_ident

    @property
    def ident_(self):
        if self._artop_ident is not None:
            if hasattr(self._artop_ident, "uuid"):
                return self._artop_ident.uuid
        return

    @property
    def ref_linErrorResponse_(self):
        return self._artop_linErrorResponse

    @property
    def linErrorResponse_(self):
        if self._artop_linErrorResponse is not None:
            if hasattr(self._artop_linErrorResponse, "uuid"):
                return self._artop_linErrorResponse.uuid
        return

    @property
    def ref_linSlaveEcu_(self):
        return self._artop_linSlaveEcuRef

    @property
    def linSlaveEcu_(self):
        if self._artop_linSlaveEcuRef is not None:
            if hasattr(self._artop_linSlaveEcuRef, "uuid"):
                return self._artop_linSlaveEcuRef.uuid
        return
