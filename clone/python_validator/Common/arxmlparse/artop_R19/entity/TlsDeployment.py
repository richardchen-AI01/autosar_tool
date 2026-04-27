# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TlsDeployment.py
from .SecureCommunicationDeployment import SecureCommunicationDeployment

class TlsDeployment(SecureCommunicationDeployment):

    def __init__(self):
        super().__init__()
        from .PskIdentityToKeySlotMapping import PskIdentityToKeySlotMapping
        from .TlsJobMapping import TlsJobMapping
        self._artop_pskIdentityToKeySlotMapping = []
        self._artop_tlsJobMapping = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_pskIdentityToKeySlotMapping':"PSK-IDENTITY-TO-KEY-SLOT-MAPPING", 
         '_artop_tlsJobMapping':"TLS-JOB-MAPPING"})

    @property
    def pskIdentityToKeySlotMappings_PskIdentityToKeySlotMapping(self):
        return self._artop_pskIdentityToKeySlotMapping

    @property
    def tlsJobMappings_TlsJobMapping(self):
        return self._artop_tlsJobMapping
