# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\VehicleDriverNotification.py
from .ARObject import ARObject

class VehicleDriverNotification(ARObject):

    def __init__(self):
        super().__init__()
        from .VehiclePackage import VehiclePackage
        self._artop_approvalRequired = None
        self._artop_notificationState = None
        self._artop_vehiclePackage = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_vehiclePackage": "VEHICLE-PACKAGE"})

    @property
    def approvalRequired_(self):
        if self._artop_approvalRequired:
            if self._artop_approvalRequired == "true":
                return True
            return False
        else:
            return self._artop_approvalRequired

    @property
    def notificationState_(self):
        return self._artop_notificationState

    @property
    def ref_vehiclePackage_(self):
        return self._artop_vehiclePackage

    @property
    def vehiclePackage_(self):
        if self._artop_vehiclePackage is not None:
            if hasattr(self._artop_vehiclePackage, "uuid"):
                return self._artop_vehiclePackage.uuid
        return
