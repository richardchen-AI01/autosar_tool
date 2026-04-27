# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\GlobalTimeGateway.py
from .Identifiable import Identifiable

class GlobalTimeGateway(Identifiable):

    def __init__(self):
        super().__init__()
        from .GlobalTimeDomain import GlobalTimeDomain
        from .EcuInstance import EcuInstance
        from .GlobalTimeMaster import GlobalTimeMaster
        from .GlobalTimeSlave import GlobalTimeSlave
        from .VariationPoint import VariationPoint
        self._artop_globalTimeDomain = None
        self._artop_hostRef = None
        self._artop_masterRef = None
        self._artop_slaveRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_globalTimeDomain': '"GLOBAL-TIME-DOMAIN"', 
         '_artop_hostRef': '"ECU-INSTANCE"', 
         '_artop_masterRef': '"GLOBAL-TIME-MASTER"', 
         '_artop_slaveRef': '"GLOBAL-TIME-SLAVE"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def ref_globalTimeDomain_(self):
        return self._artop_globalTimeDomain

    @property
    def globalTimeDomain_(self):
        if self._artop_globalTimeDomain is not None:
            if hasattr(self._artop_globalTimeDomain, "uuid"):
                return self._artop_globalTimeDomain.uuid
        return

    @property
    def ref_host_(self):
        return self._artop_hostRef

    @property
    def host_(self):
        if self._artop_hostRef is not None:
            if hasattr(self._artop_hostRef, "uuid"):
                return self._artop_hostRef.uuid
        return

    @property
    def ref_master_(self):
        return self._artop_masterRef

    @property
    def master_(self):
        if self._artop_masterRef is not None:
            if hasattr(self._artop_masterRef, "uuid"):
                return self._artop_masterRef.uuid
        return

    @property
    def ref_slave_(self):
        return self._artop_slaveRef

    @property
    def slave_(self):
        if self._artop_slaveRef is not None:
            if hasattr(self._artop_slaveRef, "uuid"):
                return self._artop_slaveRef.uuid
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
