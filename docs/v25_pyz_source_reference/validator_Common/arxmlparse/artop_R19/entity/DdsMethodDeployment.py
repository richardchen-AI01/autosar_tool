# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DdsMethodDeployment.py
from .ServiceMethodDeployment import ServiceMethodDeployment

class DdsMethodDeployment(ServiceMethodDeployment):

    def __init__(self):
        super().__init__()
        from .DdsRpcServiceDeployment import DdsRpcServiceDeployment
        self._artop_transportProtocol = None
        self._artop_ddsRpcServiceRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_ddsRpcServiceRef": "DDS-RPC-SERVICE-DEPLOYMENT"})

    @property
    def transportProtocol_(self):
        return self._artop_transportProtocol

    @property
    def ref_ddsRpcService_(self):
        return self._artop_ddsRpcServiceRef

    @property
    def ddsRpcService_(self):
        if self._artop_ddsRpcServiceRef is not None:
            if hasattr(self._artop_ddsRpcServiceRef, "uuid"):
                return self._artop_ddsRpcServiceRef.uuid
        return
