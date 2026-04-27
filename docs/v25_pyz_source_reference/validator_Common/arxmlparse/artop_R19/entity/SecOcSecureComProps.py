# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SecOcSecureComProps.py
from .SecureComProps import SecureComProps

class SecOcSecureComProps(SecureComProps):

    def __init__(self):
        super().__init__()
        from .SecOcJobRequirement import SecOcJobRequirement
        self._artop_authAlgorithm = None
        self._artop_authInfoTxLength = None
        self._artop_freshnessValueLength = None
        self._artop_freshnessValueTxLength = None
        self._artop_jobRequirement = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_jobRequirement": "SEC-OC-JOB-REQUIREMENT"})

    @property
    def authAlgorithm_(self):
        return self._artop_authAlgorithm

    @property
    def authInfoTxLength_(self):
        return self._artop_authInfoTxLength

    @property
    def freshnessValueLength_(self):
        return self._artop_freshnessValueLength

    @property
    def freshnessValueTxLength_(self):
        return self._artop_freshnessValueTxLength

    @property
    def jobRequirements_SecOcJobRequirement(self):
        return self._artop_jobRequirement
