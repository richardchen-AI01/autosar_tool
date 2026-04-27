# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\NmNode.py
from .Identifiable import Identifiable

class NmNode(Identifiable):

    def __init__(self):
        super().__init__()
        from .NmCluster import NmCluster
        from .CommunicationController import CommunicationController
        from .MachineDesign import MachineDesign
        from .NmEcu import NmEcu
        from .NmPdu import NmPdu
        from .VariationPoint import VariationPoint
        self._artop_nmCoordCluster = None
        self._artop_nmCoordinatorRole = None
        self._artop_nmNodeId = None
        self._artop_nmPassiveModeEnabled = None
        self._artop_nmCluster = None
        self._artop_controllerRef = None
        self._artop_machineRef = None
        self._artop_nmIfEcuRef = None
        self._artop_rxNmPduRef = []
        self._artop_txNmPduRef = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_nmCluster': '"NM-CLUSTER"', 
         '_artop_controllerRef': '"COMMUNICATION-CONTROLLER"', 
         '_artop_machineRef': '"MACHINE-DESIGN"', 
         '_artop_nmIfEcuRef': '"NM-ECU"', 
         '_artop_rxNmPduRef': '"NM-PDU"', 
         '_artop_txNmPduRef': '"NM-PDU"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def nmCoordCluster_(self):
        return self._artop_nmCoordCluster

    @property
    def nmCoordinatorRole_(self):
        return self._artop_nmCoordinatorRole

    @property
    def nmNodeId_(self):
        if self._artop_nmNodeId:
            return int(self._artop_nmNodeId)
        return self._artop_nmNodeId

    @property
    def nmPassiveModeEnabled_(self):
        if self._artop_nmPassiveModeEnabled:
            if self._artop_nmPassiveModeEnabled == "true":
                return True
            return False
        else:
            return self._artop_nmPassiveModeEnabled

    @property
    def ref_nmCluster_(self):
        return self._artop_nmCluster

    @property
    def nmCluster_(self):
        if self._artop_nmCluster is not None:
            if hasattr(self._artop_nmCluster, "uuid"):
                return self._artop_nmCluster.uuid
        return

    @property
    def ref_controller_(self):
        return self._artop_controllerRef

    @property
    def controller_(self):
        if self._artop_controllerRef is not None:
            if hasattr(self._artop_controllerRef, "uuid"):
                return self._artop_controllerRef.uuid
        return

    @property
    def ref_machine_(self):
        return self._artop_machineRef

    @property
    def machine_(self):
        if self._artop_machineRef is not None:
            if hasattr(self._artop_machineRef, "uuid"):
                return self._artop_machineRef.uuid
        return

    @property
    def ref_nmIfEcu_(self):
        return self._artop_nmIfEcuRef

    @property
    def nmIfEcu_(self):
        if self._artop_nmIfEcuRef is not None:
            if hasattr(self._artop_nmIfEcuRef, "uuid"):
                return self._artop_nmIfEcuRef.uuid
        return

    @property
    def ref_rxNmPdus_(self):
        return self._artop_rxNmPduRef

    @property
    def rxNmPdus_(self):
        return self._artop_rxNmPduRef

    @property
    def ref_txNmPdus_(self):
        return self._artop_txNmPduRef

    @property
    def txNmPdus_(self):
        return self._artop_txNmPduRef

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
