# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CouplingPortRatePolicy.py
from .ARObject import ARObject

class CouplingPortRatePolicy(ARObject):

    def __init__(self):
        super().__init__()
        from .CouplingPortDetails import CouplingPortDetails
        from .EthernetPhysicalChannel import EthernetPhysicalChannel
        self._artop_dataLength = None
        self._artop_policyAction = None
        self._artop_priority = None
        self._artop_timeInterval = None
        self._artop_couplingPortDetails = None
        self._artop_vLanRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_couplingPortDetails':"COUPLING-PORT-DETAILS", 
         '_artop_vLanRef':"ETHERNET-PHYSICAL-CHANNEL"})

    @property
    def dataLength_(self):
        return self._artop_dataLength

    @property
    def policyAction_(self):
        return self._artop_policyAction

    @property
    def priority_(self):
        return self._artop_priority

    @property
    def timeInterval_(self):
        return self._artop_timeInterval

    @property
    def ref_couplingPortDetails_(self):
        return self._artop_couplingPortDetails

    @property
    def couplingPortDetails_(self):
        if self._artop_couplingPortDetails is not None:
            if hasattr(self._artop_couplingPortDetails, "uuid"):
                return self._artop_couplingPortDetails.uuid
        return

    @property
    def ref_vLans_(self):
        return self._artop_vLanRef

    @property
    def vLans_(self):
        return self._artop_vLanRef
