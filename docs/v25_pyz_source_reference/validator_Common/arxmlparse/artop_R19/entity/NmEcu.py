# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\NmEcu.py
from .Identifiable import Identifiable

class NmEcu(Identifiable):

    def __init__(self):
        super().__init__()
        from .NmConfig import NmConfig
        from .BusspecificNmEcu import BusspecificNmEcu
        from .EcuInstance import EcuInstance
        from .NmCoordinator import NmCoordinator
        from .VariationPoint import VariationPoint
        self._artop_nmBusSynchronizationEnabled = None
        self._artop_nmComControlEnabled = None
        self._artop_nmCycletimeMainFunction = None
        self._artop_nmMultipleChannelsEnabled = None
        self._artop_nmNodeDetectionEnabled = None
        self._artop_nmNodeIdEnabled = None
        self._artop_nmPassiveModeEnabled = None
        self._artop_nmPduRxIndicationEnabled = None
        self._artop_nmRemoteSleepIndEnabled = None
        self._artop_nmRepeatMsgIndEnabled = None
        self._artop_nmStateChangeIndEnabled = None
        self._artop_nmUserDataEnabled = None
        self._artop_nmConfig = None
        self._artop_busDependentNmEcu = []
        self._artop_busSpecificNmEcu = None
        self._artop_ecuInstanceRef = None
        self._artop_nmCoordinator = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_nmConfig': '"NM-CONFIG"', 
         '_artop_busDependentNmEcu': '"BUSSPECIFIC-NM-ECU"', 
         '_artop_busSpecificNmEcu': '"BUSSPECIFIC-NM-ECU"', 
         '_artop_ecuInstanceRef': '"ECU-INSTANCE"', 
         '_artop_nmCoordinator': '"NM-COORDINATOR"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def nmBusSynchronizationEnabled_(self):
        if self._artop_nmBusSynchronizationEnabled:
            if self._artop_nmBusSynchronizationEnabled == "true":
                return True
            return False
        else:
            return self._artop_nmBusSynchronizationEnabled

    @property
    def nmComControlEnabled_(self):
        if self._artop_nmComControlEnabled:
            if self._artop_nmComControlEnabled == "true":
                return True
            return False
        else:
            return self._artop_nmComControlEnabled

    @property
    def nmCycletimeMainFunction_(self):
        return self._artop_nmCycletimeMainFunction

    @property
    def nmMultipleChannelsEnabled_(self):
        if self._artop_nmMultipleChannelsEnabled:
            if self._artop_nmMultipleChannelsEnabled == "true":
                return True
            return False
        else:
            return self._artop_nmMultipleChannelsEnabled

    @property
    def nmNodeDetectionEnabled_(self):
        if self._artop_nmNodeDetectionEnabled:
            if self._artop_nmNodeDetectionEnabled == "true":
                return True
            return False
        else:
            return self._artop_nmNodeDetectionEnabled

    @property
    def nmNodeIdEnabled_(self):
        if self._artop_nmNodeIdEnabled:
            if self._artop_nmNodeIdEnabled == "true":
                return True
            return False
        else:
            return self._artop_nmNodeIdEnabled

    @property
    def nmPassiveModeEnabled_(self):
        if self._artop_nmPassiveModeEnabled:
            if self._artop_nmPassiveModeEnabled == "true":
                return True
            return False
        else:
            return self._artop_nmPassiveModeEnabled

    @property
    def nmPduRxIndicationEnabled_(self):
        if self._artop_nmPduRxIndicationEnabled:
            if self._artop_nmPduRxIndicationEnabled == "true":
                return True
            return False
        else:
            return self._artop_nmPduRxIndicationEnabled

    @property
    def nmRemoteSleepIndEnabled_(self):
        if self._artop_nmRemoteSleepIndEnabled:
            if self._artop_nmRemoteSleepIndEnabled == "true":
                return True
            return False
        else:
            return self._artop_nmRemoteSleepIndEnabled

    @property
    def nmRepeatMsgIndEnabled_(self):
        if self._artop_nmRepeatMsgIndEnabled:
            if self._artop_nmRepeatMsgIndEnabled == "true":
                return True
            return False
        else:
            return self._artop_nmRepeatMsgIndEnabled

    @property
    def nmStateChangeIndEnabled_(self):
        if self._artop_nmStateChangeIndEnabled:
            if self._artop_nmStateChangeIndEnabled == "true":
                return True
            return False
        else:
            return self._artop_nmStateChangeIndEnabled

    @property
    def nmUserDataEnabled_(self):
        if self._artop_nmUserDataEnabled:
            if self._artop_nmUserDataEnabled == "true":
                return True
            return False
        else:
            return self._artop_nmUserDataEnabled

    @property
    def ref_nmConfig_(self):
        return self._artop_nmConfig

    @property
    def nmConfig_(self):
        if self._artop_nmConfig is not None:
            if hasattr(self._artop_nmConfig, "uuid"):
                return self._artop_nmConfig.uuid
        return

    @property
    def busDependentNmEcus_BusspecificNmEcu(self):
        return self._artop_busDependentNmEcu

    @property
    def ref_busSpecificNmEcu_(self):
        return self._artop_busSpecificNmEcu

    @property
    def busSpecificNmEcu_(self):
        if self._artop_busSpecificNmEcu is not None:
            if hasattr(self._artop_busSpecificNmEcu, "uuid"):
                return self._artop_busSpecificNmEcu.uuid
        return

    @property
    def ref_ecuInstance_(self):
        return self._artop_ecuInstanceRef

    @property
    def ecuInstance_(self):
        if self._artop_ecuInstanceRef is not None:
            if hasattr(self._artop_ecuInstanceRef, "uuid"):
                return self._artop_ecuInstanceRef.uuid
        return

    @property
    def ref_nmCoordinator_(self):
        return self._artop_nmCoordinator

    @property
    def nmCoordinator_(self):
        if self._artop_nmCoordinator is not None:
            if hasattr(self._artop_nmCoordinator, "uuid"):
                return self._artop_nmCoordinator.uuid
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
