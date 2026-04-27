# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\IPSecConfigProps.py
from .ARElement import ARElement

class IPSecConfigProps(ARElement):

    def __init__(self):
        super().__init__()
        self._artop_ahCipherSuiteName = None
        self._artop_dpdAction = None
        self._artop_dpdDelay = None
        self._artop_espCipherSuiteName = None
        self._artop_ikeCipherSuiteName = None
        self._artop_ikeOverTime = None
        self._artop_ikeRandTime = None
        self._artop_ikeReauthTime = None
        self._artop_ikeRekeyTime = None
        self._artop_saOverTime = None
        self._artop_saRandTime = None
        self._artop_saRekeyTime = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def ahCipherSuiteName_(self):
        return self._artop_ahCipherSuiteName

    @property
    def dpdAction_(self):
        return self._artop_dpdAction

    @property
    def dpdDelay_(self):
        return self._artop_dpdDelay

    @property
    def espCipherSuiteName_(self):
        return self._artop_espCipherSuiteName

    @property
    def ikeCipherSuiteName_(self):
        return self._artop_ikeCipherSuiteName

    @property
    def ikeOverTime_(self):
        return self._artop_ikeOverTime

    @property
    def ikeRandTime_(self):
        return self._artop_ikeRandTime

    @property
    def ikeReauthTime_(self):
        return self._artop_ikeReauthTime

    @property
    def ikeRekeyTime_(self):
        return self._artop_ikeRekeyTime

    @property
    def saOverTime_(self):
        return self._artop_saOverTime

    @property
    def saRandTime_(self):
        return self._artop_saRandTime

    @property
    def saRekeyTime_(self):
        return self._artop_saRekeyTime
