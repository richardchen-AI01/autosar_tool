# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\UcmDescription.py
from .Identifiable import Identifiable

class UcmDescription(Identifiable):

    def __init__(self):
        super().__init__()
        from .VehiclePackage import VehiclePackage
        from .UcmModuleInstantiation import UcmModuleInstantiation
        self._artop_identifier = None
        self._artop_vehiclePackage = None
        self._artop_ucmModuleInstantiationRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_vehiclePackage':"VEHICLE-PACKAGE", 
         '_artop_ucmModuleInstantiationRef':"UCM-MODULE-INSTANTIATION"})

    @property
    def identifier_(self):
        return self._artop_identifier

    @property
    def ref_vehiclePackage_(self):
        return self._artop_vehiclePackage

    @property
    def vehiclePackage_(self):
        if self._artop_vehiclePackage is not None:
            if hasattr(self._artop_vehiclePackage, "uuid"):
                return self._artop_vehiclePackage.uuid
        return

    @property
    def ref_ucmModuleInstantiation_(self):
        return self._artop_ucmModuleInstantiationRef

    @property
    def ucmModuleInstantiation_(self):
        if self._artop_ucmModuleInstantiationRef is not None:
            if hasattr(self._artop_ucmModuleInstantiationRef, "uuid"):
                return self._artop_ucmModuleInstantiationRef.uuid
        return
