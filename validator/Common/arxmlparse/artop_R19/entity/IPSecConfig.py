# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\IPSecConfig.py
from .ARObject import ARObject

class IPSecConfig(ARObject):

    def __init__(self):
        super().__init__()
        from .NetworkEndpoint import NetworkEndpoint
        from .IPSecConfigProps import IPSecConfigProps
        from .IPSecRule import IPSecRule
        self._artop_networkEndpoint = None
        self._artop_ipSecConfigPropsRef = None
        self._artop_ipSecRule = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_networkEndpoint':"NETWORK-ENDPOINT", 
         '_artop_ipSecConfigPropsRef':"IP-SEC-CONFIG-PROPS", 
         '_artop_ipSecRule':"IP-SEC-RULE"})

    @property
    def ref_networkEndpoint_(self):
        return self._artop_networkEndpoint

    @property
    def networkEndpoint_(self):
        if self._artop_networkEndpoint is not None:
            if hasattr(self._artop_networkEndpoint, "uuid"):
                return self._artop_networkEndpoint.uuid
        return

    @property
    def ref_ipSecConfigProps_(self):
        return self._artop_ipSecConfigPropsRef

    @property
    def ipSecConfigProps_(self):
        if self._artop_ipSecConfigPropsRef is not None:
            if hasattr(self._artop_ipSecConfigPropsRef, "uuid"):
                return self._artop_ipSecConfigPropsRef.uuid
        return

    @property
    def ipSecRules_IPSecRule(self):
        return self._artop_ipSecRule
