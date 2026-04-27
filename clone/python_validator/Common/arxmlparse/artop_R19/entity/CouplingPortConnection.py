# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CouplingPortConnection.py
from .ARObject import ARObject

class CouplingPortConnection(ARObject):

    def __init__(self):
        super().__init__()
        from .EthernetClusterContent import EthernetClusterContent
        from .CouplingPort import CouplingPort
        from .VariationPoint import VariationPoint
        self._artop_ethernetClusterContent = None
        self._artop_firstPortRef = None
        self._artop_secondPortRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_ethernetClusterContent': '"ETHERNET-CLUSTER-CONTENT"', 
         '_artop_firstPortRef': '"COUPLING-PORT"', 
         '_artop_secondPortRef': '"COUPLING-PORT"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def ref_ethernetClusterContent_(self):
        return self._artop_ethernetClusterContent

    @property
    def ethernetClusterContent_(self):
        if self._artop_ethernetClusterContent is not None:
            if hasattr(self._artop_ethernetClusterContent, "uuid"):
                return self._artop_ethernetClusterContent.uuid
        return

    @property
    def ref_firstPort_(self):
        return self._artop_firstPortRef

    @property
    def firstPort_(self):
        if self._artop_firstPortRef is not None:
            if hasattr(self._artop_firstPortRef, "uuid"):
                return self._artop_firstPortRef.uuid
        return

    @property
    def ref_secondPort_(self):
        return self._artop_secondPortRef

    @property
    def secondPort_(self):
        if self._artop_secondPortRef is not None:
            if hasattr(self._artop_secondPortRef, "uuid"):
                return self._artop_secondPortRef.uuid
        return

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
