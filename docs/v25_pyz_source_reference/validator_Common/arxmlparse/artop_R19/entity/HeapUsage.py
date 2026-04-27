# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\HeapUsage.py
from .Identifiable import Identifiable

class HeapUsage(Identifiable):

    def __init__(self):
        super().__init__()
        from .ResourceConsumption import ResourceConsumption
        from .HardwareConfiguration import HardwareConfiguration
        from .HwElement import HwElement
        from .SoftwareContext import SoftwareContext
        from .VariationPoint import VariationPoint
        self._artop_resourceConsumption = None
        self._artop_hardwareConfiguration = None
        self._artop_hwElementRef = None
        self._artop_softwareContext = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_resourceConsumption': '"RESOURCE-CONSUMPTION"', 
         '_artop_hardwareConfiguration': '"HARDWARE-CONFIGURATION"', 
         '_artop_hwElementRef': '"HW-ELEMENT"', 
         '_artop_softwareContext': '"SOFTWARE-CONTEXT"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def ref_resourceConsumption_(self):
        return self._artop_resourceConsumption

    @property
    def resourceConsumption_(self):
        if self._artop_resourceConsumption is not None:
            if hasattr(self._artop_resourceConsumption, "uuid"):
                return self._artop_resourceConsumption.uuid
        return

    @property
    def ref_hardwareConfiguration_(self):
        return self._artop_hardwareConfiguration

    @property
    def hardwareConfiguration_(self):
        if self._artop_hardwareConfiguration is not None:
            if hasattr(self._artop_hardwareConfiguration, "uuid"):
                return self._artop_hardwareConfiguration.uuid
        return

    @property
    def ref_hwElement_(self):
        return self._artop_hwElementRef

    @property
    def hwElement_(self):
        if self._artop_hwElementRef is not None:
            if hasattr(self._artop_hwElementRef, "uuid"):
                return self._artop_hwElementRef.uuid
        return

    @property
    def ref_softwareContext_(self):
        return self._artop_softwareContext

    @property
    def softwareContext_(self):
        if self._artop_softwareContext is not None:
            if hasattr(self._artop_softwareContext, "uuid"):
                return self._artop_softwareContext.uuid
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
