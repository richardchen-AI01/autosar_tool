# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TlsJobMapping.py
from .Identifiable import Identifiable

class TlsJobMapping(Identifiable):

    def __init__(self):
        super().__init__()
        from .TlsDeployment import TlsDeployment
        self._artop_tlsDeployment = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_tlsDeployment": "TLS-DEPLOYMENT"})

    @property
    def ref_tlsDeployment_(self):
        return self._artop_tlsDeployment

    @property
    def tlsDeployment_(self):
        if self._artop_tlsDeployment is not None:
            if hasattr(self._artop_tlsDeployment, "uuid"):
                return self._artop_tlsDeployment.uuid
        return
