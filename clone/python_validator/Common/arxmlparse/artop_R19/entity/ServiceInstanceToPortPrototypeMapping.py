# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ServiceInstanceToPortPrototypeMapping.py
from .UploadablePackageElement import UploadablePackageElement

class ServiceInstanceToPortPrototypeMapping(UploadablePackageElement):

    def __init__(self):
        super().__init__()
        from .PortPrototypeInExecutableInstanceRef import PortPrototypeInExecutableInstanceRef
        from .ProcessDesign import ProcessDesign
        from .AdaptivePlatformServiceInstance import AdaptivePlatformServiceInstance
        self._artop_enablesLogTrace = None
        self._artop_logTracePortId = None
        self._artop_portPrototypeIref = None
        self._artop_processRef = None
        self._artop_serviceInstanceRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_portPrototypeIref':"PORT-PROTOTYPE-IN-EXECUTABLE-INSTANCE-REF", 
         '_artop_processRef':"PROCESS-DESIGN", 
         '_artop_serviceInstanceRef':"ADAPTIVE-PLATFORM-SERVICE-INSTANCE"})

    @property
    def enablesLogTrace_(self):
        if self._artop_enablesLogTrace:
            if self._artop_enablesLogTrace == "true":
                return True
            return False
        else:
            return self._artop_enablesLogTrace

    @property
    def logTracePortId_(self):
        return self._artop_logTracePortId

    @property
    def ref_portPrototype_(self):
        return self._artop_portPrototypeIref

    @property
    def portPrototype_(self):
        if self._artop_portPrototypeIref is not None:
            if hasattr(self._artop_portPrototypeIref, "uuid"):
                return self._artop_portPrototypeIref.uuid
        return

    @property
    def ref_process_(self):
        return self._artop_processRef

    @property
    def process_(self):
        if self._artop_processRef is not None:
            if hasattr(self._artop_processRef, "uuid"):
                return self._artop_processRef.uuid
        return

    @property
    def ref_serviceInstance_(self):
        return self._artop_serviceInstanceRef

    @property
    def serviceInstance_(self):
        if self._artop_serviceInstanceRef is not None:
            if hasattr(self._artop_serviceInstanceRef, "uuid"):
                return self._artop_serviceInstanceRef.uuid
        return
